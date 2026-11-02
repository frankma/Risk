"""Rules, states and ranking for the daily market risk queue, as set out in pillars/market-risk.md.

An exception is a reading where a rule has fired; a watch item is a reading moving towards a threshold. Exceptions
rank before watch items: breaches, then other exceptions, then early warnings, then persistence. Within a tier, a fund
with several items ranks above a fund with fewer, then items are ordered by size relative to their threshold.

With parametric VaR, VaR and ex-ante volatility are the same portfolio volatility on different scales, so a sharp
rise in VaR usually also takes volatility outside its usual range. When both rules fire for a fund they describe one
move, and are grouped into a single exception: the large-change item, carrying the volatility reading with it.
"""

import tomllib
from dataclasses import dataclass
from pathlib import Path

import pandas as pd

from riskref.compute.market import Decomposition, FundDay, covariances, decompose, fund_history, z_score
from riskref.data.synthetic import MarketData

DEFAULT_THRESHOLDS = Path(__file__).resolve().parents[2] / "config" / "thresholds.toml"

EXCEPTION = "exception"
WATCH = "watch"

# rule -> (state, tier)
RULES = {
    "limit_breach": (EXCEPTION, 1),
    "large_change": (EXCEPTION, 2),
    "outside_range": (EXCEPTION, 2),
    "unreconciled": (EXCEPTION, 2),
    "early_warning": (WATCH, 3),
    "persistence": (WATCH, 4),
}

LIMITS = {  # measure -> column in the fund limits table
    "VaR": "var_limit",
    "issuer weight": "issuer_limit",
    "sector weight": "sector_limit",
    "counterparty exposure": "counterparty_limit",
}


@dataclass(frozen=True)
class Thresholds:
    version: str
    confidence: float
    covariance_window: int
    early_warning_share: float
    var_change_share: float
    persistence_days: int
    range_window: int
    reconciliation_tolerance: float
    max_draft_attempts: int


def load_thresholds(path: Path = DEFAULT_THRESHOLDS) -> Thresholds:
    with path.open("rb") as f:
        raw = tomllib.load(f)
    return Thresholds(version=raw["version"], **raw["var"], **raw["rules"], **raw["checks"], **raw["narration"])


@dataclass
class Item:
    """One entry in the queue. Values are fractions (0.0231 means 2.31%) except ``days``."""

    fund: str
    rule: str
    measure: str
    value: float
    threshold: float
    ratio: float  # size relative to the threshold; larger means further past it
    as_of: pd.Timestamp
    thresholds_version: str
    subject: str | None = None  # the issuer, sector or counterparty concerned
    limit: float | None = None
    previous: float | None = None
    days: int | None = None
    range_low: float | None = None
    range_high: float | None = None
    volatility: float | None = None  # set on a large-change item that absorbed an outside-range item
    decomposition: Decomposition | None = None

    @property
    def state(self) -> str:
        return RULES[self.rule][0]

    @property
    def tier(self) -> int:
        return RULES[self.rule][1]


@dataclass
class Assessment:
    as_of: pd.Timestamp
    thresholds_version: str
    items: list[Item]  # ranked
    not_assessed: list[str]
    quiet: list[str]
    today: dict[str, FundDay]
    decompositions: dict[str, Decomposition]


def limit_items(
    fund: str, measure: str, subject: str | None, series: pd.Series, limit: float, t: Thresholds
) -> list[Item]:
    """Breach, early warning and persistence for one measure's daily series (index: date, last value is today)."""
    as_of, value = series.index[-1], float(series.iloc[-1])
    common = dict(
        fund=fund, measure=measure, value=value, as_of=as_of, thresholds_version=t.version, subject=subject, limit=limit
    )
    if value > limit:
        return [Item(rule="limit_breach", threshold=limit, ratio=value / limit, **common)]
    warning = t.early_warning_share * limit
    if value <= warning:
        return []
    items = [Item(rule="early_warning", threshold=warning, ratio=value / limit, **common)]
    above = (series > warning).to_numpy()[::-1]
    days = int(above.argmin()) if not above.all() else len(above)
    if days >= t.persistence_days:
        items.append(Item(rule="persistence", threshold=warning, ratio=value / limit, days=days, **common))
    return items


def change_item(
    fund: str, today: FundDay, previous: FundDay, decomposition: Decomposition, t: Thresholds
) -> list[Item]:
    """VaR rising by more than the set share since the previous day."""
    share = today.var / previous.var - 1.0
    if share <= t.var_change_share:
        return []
    return [
        Item(
            fund=fund,
            rule="large_change",
            measure="VaR",
            value=today.var,
            threshold=t.var_change_share,
            ratio=share / t.var_change_share,
            as_of=today.date,
            thresholds_version=t.version,
            previous=previous.var,
            decomposition=decomposition,
        )
    ]


def range_item(fund: str, volatility: pd.Series, t: Thresholds) -> list[Item]:
    """Ex-ante volatility above the highest or below the lowest of the previous ``range_window`` days."""
    if len(volatility) < t.range_window + 1:
        return []
    today = float(volatility.iloc[-1])
    window = volatility.iloc[-t.range_window - 1 : -1]
    low, high = float(window.min()), float(window.max())
    if low <= today <= high:
        return []
    threshold, ratio = (high, today / high) if today > high else (low, low / today)
    return [
        Item(
            fund=fund,
            rule="outside_range",
            measure="volatility",
            value=today,
            threshold=threshold,
            ratio=ratio,
            as_of=volatility.index[-1],
            thresholds_version=t.version,
            range_low=low,
            range_high=high,
        )
    ]


def evaluate_fund(
    fund: str, history: dict[pd.Timestamp, FundDay], limits: pd.Series, securities: pd.DataFrame, t: Thresholds
) -> tuple[list[Item], Decomposition | None]:
    """Every rule for one fund. ``history`` must include the as-of date as its last day."""
    dates = sorted(history)
    today = history[dates[-1]]
    items: list[Item] = []

    var = pd.Series({d: history[d].var for d in dates})
    items += limit_items(fund, "VaR", None, var, float(limits[LIMITS["VaR"]]), t)
    by_subject = {
        "issuer weight": pd.DataFrame({d: history[d].issuer_weights for d in dates}).T.fillna(0.0),
        "sector weight": pd.DataFrame({d: history[d].sector_weights for d in dates}).T.fillna(0.0),
        "counterparty exposure": pd.DataFrame({d: history[d].counterparty_exposure for d in dates}).T.fillna(0.0),
    }
    for measure, table in by_subject.items():
        for subject in table.columns:
            items += limit_items(fund, measure, subject, table[subject], float(limits[LIMITS[measure]]), t)

    decomposition = None
    if len(dates) >= 2:
        previous = history[dates[-2]]
        decomposition = decompose(today, previous, securities)
        if not decomposition.reconciles(t.reconciliation_tolerance):
            items.append(
                Item(
                    fund=fund,
                    rule="unreconciled",
                    measure="VaR",
                    value=decomposition.sum_of_changes,
                    threshold=decomposition.total_change,
                    ratio=1.0,
                    as_of=today.date,
                    thresholds_version=t.version,
                    decomposition=decomposition,
                )
            )
        else:
            items += change_item(fund, today, previous, decomposition, t)

    volatility = pd.Series({d: history[d].volatility for d in dates})
    items += range_item(fund, volatility, t)
    return group_shared_driver(items), decomposition


def group_shared_driver(items: list[Item]) -> list[Item]:
    """Fold a fund's outside-range volatility item into its large-change VaR item when both fired."""
    change = next((i for i in items if i.rule == "large_change"), None)
    outside = next((i for i in items if i.rule == "outside_range"), None)
    if change is None or outside is None:
        return items
    change.volatility, change.range_low, change.range_high = outside.value, outside.range_low, outside.range_high
    return [i for i in items if i is not outside]


def rank(items: list[Item]) -> list[Item]:
    count = pd.Series([i.fund for i in items]).value_counts().to_dict() if items else {}
    return sorted(items, key=lambda i: (i.tier, -count[i.fund], -i.ratio))


def assess(data: MarketData, t: Thresholds) -> Assessment:
    """Run every rule for every fund on the as-of date and rank the results."""
    dates = pd.DatetimeIndex(sorted(data.positions["date"].unique()))
    covs = covariances(data.returns, dates, t.covariance_window)
    z = z_score(t.confidence)
    items: list[Item] = []
    not_assessed, quiet = [], []
    today: dict[str, FundDay] = {}
    decompositions: dict[str, Decomposition] = {}
    for fund in data.funds.index:
        history = fund_history(data, fund, covs, z)
        if data.as_of not in history:
            not_assessed.append(fund)
            continue
        history = {d: day for d, day in history.items() if d <= data.as_of}
        fund_items, decomposition = evaluate_fund(fund, history, data.funds.loc[fund], data.securities, t)
        today[fund] = history[data.as_of]
        if decomposition is not None:
            decompositions[fund] = decomposition
        if fund_items:
            items += fund_items
        else:
            quiet.append(fund)
    return Assessment(data.as_of, t.version, rank(items), not_assessed, quiet, today, decompositions)
