"""Seeded synthetic market data for the reference implementations.

Everything here is invented: generic fund, issuer, security and counterparty names, a simple factor model for returns,
and illustrative limits. The data is small enough to generate in well under a second and is planted with the
situations the daily market risk example needs to show (see ``PLANTED``).
"""

from dataclasses import dataclass

import numpy as np
import pandas as pd

AS_OF = pd.Timestamp("2026-10-30")
N_PRICE_DAYS = 320
N_POSITION_DAYS = 61
N_SECURITIES = 60
N_ISSUERS = 40
HOLDINGS_PER_FUND = 25
FUNDS = [f"Fund {letter}" for letter in "ABCDEFGHIJKL"]
SECTORS = ["Technology", "Financials", "Health Care", "Energy", "Utilities", "Consumer"]
CURRENCIES = ["USD", "EUR", "GBP", "JPY"]
COUNTERPARTIES = ["Counterparty X", "Counterparty Y", "Counterparty Z"]

# Daily volatility of each sector factor; Technology is the most volatile and Utilities the least.
SECTOR_VOL = {"Technology": 0.016, "Financials": 0.006, "Health Care": 0.005, "Energy": 0.008, "Utilities": 0.003,
              "Consumer": 0.005}
MARKET_VOL = 0.008
CURRENCY_VOL = 0.004
IDIOSYNCRATIC_VOL = 0.012
Z_99 = 2.3263478740408408

# What each planted fund is meant to show in the daily market risk note.
PLANTED = {
    "Fund A": "VaR rises sharply on the last day after a new Technology position, to about 92% of its limit",
    "Fund B": "exposure to Counterparty X rises towards its limit after new forwards",
    "Fund C": "largest issuer weight above its early warning for the last 6 days",
    "Fund D": "issuer weight above its limit on the last day",
    "Fund E": "no positions on the last day",
}


@dataclass
class MarketData:
    """All inputs to the daily market risk workflow."""

    as_of: pd.Timestamp
    securities: pd.DataFrame  # index: security; columns: issuer, sector, currency
    returns: pd.DataFrame  # index: date; columns: security; daily simple returns
    prices: pd.DataFrame  # index: date; columns: security
    fx_returns: pd.DataFrame  # index: date; columns: currency; daily returns against the base currency
    funds: pd.DataFrame  # index: fund; columns: cash, var_limit, issuer_limit, sector_limit, counterparty_limit
    positions: pd.DataFrame  # columns: date, fund, security, quantity
    forwards: pd.DataFrame  # columns: fund, counterparty, currency, notional, direction, trade_date


def generate(seed: int = 2026) -> MarketData:
    """Generate the synthetic market, funds, positions and forwards, with the planted situations."""
    rng = np.random.default_rng(seed)
    dates = pd.bdate_range(end=AS_OF, periods=N_PRICE_DAYS)
    position_dates = dates[-N_POSITION_DAYS:]

    securities = _securities(rng)
    returns, fx_returns = _returns(rng, dates, securities)
    prices = 100.0 * (1.0 + returns).cumprod()

    holdings = {fund: _initial_holdings(rng, securities) for fund in FUNDS}
    trades: dict[str, list[tuple[pd.Timestamp, str, float]]] = {fund: [] for fund in FUNDS}
    nav0 = {fund: float(rng.uniform(150e6, 600e6)) for fund in FUNDS}
    cash_share = {fund: 0.05 for fund in FUNDS}
    cash_share["Fund A"] = 0.30  # room for the new Technology position
    cash_share["Fund D"] = 0.10  # room for the purchase that breaches the issuer limit

    start = position_dates[0]
    quantities = {
        fund: {sec: w * nav0[fund] / prices.at[start, sec] for sec, w in holdings[fund].items()} for fund in FUNDS
    }
    cash = {fund: cash_share[fund] * nav0[fund] for fund in FUNDS}

    _plant_fund_a(securities, prices, quantities, cash, trades, holdings)
    _plant_issuer_purchase("Fund C", position_dates[-6], 0.096, securities, prices, quantities, cash, trades)
    _plant_issuer_purchase("Fund D", AS_OF, 0.104, securities, prices, quantities, cash, trades)

    positions = _positions(position_dates, quantities, trades)
    positions = positions[~((positions["fund"] == "Fund E") & (positions["date"] == AS_OF))]

    forwards = _forwards(rng, position_dates, fx_returns)
    funds = _limits(securities, returns, prices, positions, cash, forwards, fx_returns, position_dates)
    return MarketData(AS_OF, securities, returns, prices, fx_returns, funds, positions.reset_index(drop=True), forwards)


def _securities(rng: np.random.Generator) -> pd.DataFrame:
    issuer_sector = [SECTORS[i % len(SECTORS)] for i in range(N_ISSUERS)]
    issuer_currency = [CURRENCIES[rng.integers(len(CURRENCIES))] for _ in range(N_ISSUERS)]
    rows = []
    for k in range(N_SECURITIES):
        issuer = k % N_ISSUERS  # the first 20 issuers have two securities each
        rows.append({
            "security": f"Security {k + 1:02d}",
            "issuer": f"Issuer {issuer + 1:02d}",
            "sector": issuer_sector[issuer],
            "currency": issuer_currency[issuer],
        })
    return pd.DataFrame(rows).set_index("security")


def _returns(
    rng: np.random.Generator, dates: pd.DatetimeIndex, securities: pd.DataFrame
) -> tuple[pd.DataFrame, pd.DataFrame]:
    n = len(dates)
    market = rng.normal(0.0002, MARKET_VOL, n)
    sector = {s: rng.normal(0.0, vol, n) for s, vol in SECTOR_VOL.items()}
    fx = {c: (np.zeros(n) if c == "USD" else rng.normal(0.0, CURRENCY_VOL, n)) for c in CURRENCIES}
    columns = {}
    for sec, row in securities.iterrows():
        beta = rng.uniform(0.7, 1.3)
        columns[sec] = beta * market + sector[row["sector"]] + fx[row["currency"]] + rng.normal(
            0.0, IDIOSYNCRATIC_VOL, n
        )
    return pd.DataFrame(columns, index=dates), pd.DataFrame(fx, index=dates)


def _initial_holdings(rng: np.random.Generator, securities: pd.DataFrame) -> dict[str, float]:
    """Weights for one fund: one security per issuer, no position above 6% of net assets."""
    first_of_issuer = securities.reset_index().drop_duplicates("issuer")["security"].to_numpy()
    chosen = rng.choice(first_of_issuer, size=HOLDINGS_PER_FUND, replace=False)
    weights = rng.dirichlet(np.full(HOLDINGS_PER_FUND, 8.0))
    weights = np.minimum(weights, 0.06 / 0.95)
    weights = 0.95 * weights / weights.sum()
    return dict(zip(chosen, weights, strict=True))


def _plant_fund_a(securities, prices, quantities, cash, trades, holdings) -> None:
    """On the last day, Fund A buys three Technology securities from new issuers, 8.5% of net assets each."""
    fund = "Fund A"
    held_issuers = {securities.at[s, "issuer"] for s in holdings[fund]}
    tech = (
        securities[(securities["sector"] == "Technology") & ~securities["issuer"].isin(held_issuers)]
        .drop_duplicates("issuer")
        .index
    )
    nav = _nav(fund, AS_OF, prices, quantities, cash)
    for sec in tech[:3]:
        qty = 0.085 * nav / prices.at[AS_OF, sec]
        trades[fund].append((AS_OF, sec, qty))
        cash[fund] -= qty * prices.at[AS_OF, sec]


def _plant_issuer_purchase(fund, date, target, securities, prices, quantities, cash, trades) -> None:
    """Buy more of the fund's largest holding on ``date`` so that its issuer weight reaches ``target``."""
    nav = _nav(fund, date, prices, quantities, cash)
    sec = max(quantities[fund], key=lambda s: quantities[fund][s] * prices.at[date, s])
    current = quantities[fund][sec] * prices.at[date, sec] / nav
    qty = (target - current) * nav / prices.at[date, sec]
    trades[fund].append((date, sec, qty))
    cash[fund] -= qty * prices.at[date, sec]


def _nav(fund, date, prices, quantities, cash) -> float:
    return sum(q * prices.at[date, s] for s, q in quantities[fund].items()) + cash[fund]


def _positions(position_dates, quantities, trades) -> pd.DataFrame:
    rows = []
    for fund in FUNDS:
        for date in position_dates:
            held = dict(quantities[fund])
            for trade_date, sec, qty in trades[fund]:
                if date >= trade_date:
                    held[sec] = held.get(sec, 0.0) + qty
            rows.extend({"date": date, "fund": fund, "security": s, "quantity": q} for s, q in held.items())
    return pd.DataFrame(rows)


def _forwards(rng: np.random.Generator, position_dates: pd.DatetimeIndex, fx_returns: pd.DataFrame) -> pd.DataFrame:
    """A few forwards per fund against the base currency (USD).

    ``direction`` is +1 for a forward that buys the foreign currency and -1 for one that sells it.
    """
    rows = []
    for fund in FUNDS:
        for counterparty in COUNTERPARTIES:
            rows.append({
                "fund": fund,
                "counterparty": counterparty,
                "currency": CURRENCIES[1 + rng.integers(3)],
                "notional": float(rng.uniform(5e6, 20e6)),
                "direction": int(rng.choice([-1, 1])),
                "trade_date": position_dates[0],
            })
    # Fund B adds large new forwards with Counterparty X ten business days before the last day, on the side that the
    # currency has since moved in favour of, so that its exposure to that counterparty builds up.
    trade_date = position_dates[-11]
    fx_index = (1.0 + fx_returns).cumprod()
    for currency in ("EUR", "GBP", "JPY"):
        move = fx_index.at[AS_OF, currency] / fx_index.at[trade_date, currency] - 1.0
        rows.append({"fund": "Fund B", "counterparty": "Counterparty X", "currency": currency, "notional": 60e6,
                     "direction": 1 if move >= 0 else -1, "trade_date": trade_date})
    return pd.DataFrame(rows)


def _limits(securities, returns, prices, positions, cash, forwards, fx_returns, position_dates) -> pd.DataFrame:
    """Illustrative limits, set from each fund's typical risk as a risk function might calibrate them.

    Most funds sit comfortably inside their limits. The planted funds' limits are set so that the last day shows
    the intended situation.
    """
    rows = {}
    for fund in FUNDS:
        var_by_date = {d: _typical_var(fund, d, securities, returns, prices, positions, cash) for d in position_dates}
        var_series = pd.Series(var_by_date).dropna()
        var_limit = var_series.iloc[:-1].max() / 0.75
        if fund == "Fund A":
            var_limit = var_series.iloc[-1] / 0.92
        exposure = _max_counterparty_exposure(fund, forwards, fx_returns, prices, positions, cash, position_dates)
        cp_limit = max(exposure.max() / 0.6, 0.02)
        if fund == "Fund B":
            cp_limit = exposure.iloc[-1] / 0.88
        rows[fund] = {
            "cash": cash[fund],
            "var_limit": round(float(var_limit), 4),
            "issuer_limit": 0.10,
            "sector_limit": 0.40,
            "counterparty_limit": round(float(cp_limit), 4),
        }
    return pd.DataFrame.from_dict(rows, orient="index")


def _typical_var(fund, date, securities, returns, prices, positions, cash) -> float:
    """Parametric 99% VaR used only to calibrate the illustrative limits (``compute.market`` does the real work)."""
    held = positions[(positions["fund"] == fund) & (positions["date"] == date)]
    if held.empty:
        return float("nan")
    values = held.set_index("security")["quantity"] * prices.loc[date, held["security"]].to_numpy()
    nav = values.sum() + cash[fund]
    weights = values / nav
    window = returns.loc[:date].iloc[-250:][weights.index]
    sigma = float(np.sqrt(weights.to_numpy() @ window.cov().to_numpy() @ weights.to_numpy()))
    return Z_99 * sigma


def _max_counterparty_exposure(fund, forwards, fx_returns, prices, positions, cash, position_dates) -> pd.Series:
    """Largest counterparty exposure per day, as a share of net assets, used to calibrate the illustrative limits."""
    fx_index = (1.0 + fx_returns).cumprod()
    out = {}
    for date in position_dates:
        held = positions[(positions["fund"] == fund) & (positions["date"] == date)]
        if held.empty:
            continue
        nav = (held.set_index("security")["quantity"] * prices.loc[date, held["security"]].to_numpy()).sum()
        nav += cash[fund]
        live = forwards[(forwards["fund"] == fund) & (forwards["trade_date"] <= date)]
        mtm = live.apply(
            lambda f, d=date: f["notional"] * f["direction"]
            * (fx_index.at[d, f["currency"]] / fx_index.at[f["trade_date"], f["currency"]] - 1.0),
            axis=1,
        )
        by_cp = mtm.clip(lower=0.0).groupby(live["counterparty"]).sum() / nav
        out[date] = by_cp.max() if not by_cp.empty else 0.0
    return pd.Series(out)
