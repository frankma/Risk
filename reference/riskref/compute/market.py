"""Market risk measures: parametric VaR with Euler contributions, change decomposition, ex-ante volatility,
concentration and counterparty exposure.

The methods are deliberately simple and transparent; the reference implementations demonstrate a workflow, not a risk
model. VaR covers securities only: currency forwards enter counterparty exposure but not VaR.
"""

from dataclasses import dataclass
from statistics import NormalDist

import numpy as np
import pandas as pd

from riskref.data.synthetic import MarketData

TRADING_DAYS = 252


@dataclass
class FundDay:
    """One fund's measures on one day. Shares are fractions of net assets (0.0231 means 2.31%)."""

    fund: str
    date: pd.Timestamp
    nav: float
    weights: pd.Series  # by security
    var: float
    sigma: float  # daily volatility of portfolio returns
    contributions: pd.Series  # Euler contributions to VaR, by security; they sum to ``var``
    issuer_weights: pd.Series
    sector_weights: pd.Series
    counterparty_exposure: pd.Series  # positive mark-to-market by counterparty

    @property
    def volatility(self) -> float:
        """Ex-ante annualised volatility."""
        return self.sigma * np.sqrt(TRADING_DAYS)


@dataclass
class Decomposition:
    """The change in VaR between two days, split by position and grouped by sector and currency."""

    total_change: float
    by_position: pd.Series
    by_sector: pd.Series
    by_currency: pd.Series

    @property
    def sum_of_changes(self) -> float:
        return float(self.by_position.sum())

    def reconciles(self, tolerance: float) -> bool:
        return abs(self.total_change - self.sum_of_changes) <= tolerance


def z_score(confidence: float) -> float:
    return NormalDist().inv_cdf(confidence)


def covariances(returns: pd.DataFrame, dates: pd.DatetimeIndex, window: int) -> dict[pd.Timestamp, pd.DataFrame]:
    """Sample covariance of daily security returns over the ``window`` days ending on each date."""
    return {date: returns.loc[:date].iloc[-window:].cov() for date in dates}


def var_contributions(weights: pd.Series, cov: pd.DataFrame, z: float) -> tuple[float, float, pd.Series]:
    """Parametric VaR, daily portfolio volatility and Euler contributions by position."""
    w = weights.to_numpy()
    sigma_w = cov.loc[weights.index, weights.index].to_numpy() @ w
    sigma = float(np.sqrt(w @ sigma_w))
    contributions = pd.Series(z * w * sigma_w / sigma, index=weights.index)
    return z * sigma, sigma, contributions


def counterparty_exposure(data: MarketData, fund: str, date: pd.Timestamp, nav: float) -> pd.Series:
    """Positive mark-to-market of live forwards, summed by counterparty, as a share of net assets."""
    fx_index = (1.0 + data.fx_returns).cumprod()
    live = data.forwards[(data.forwards["fund"] == fund) & (data.forwards["trade_date"] <= date)]
    if live.empty:
        return pd.Series(dtype=float)
    now = fx_index.loc[date, live["currency"]].to_numpy()
    then = np.array([fx_index.at[d, c] for d, c in zip(live["trade_date"], live["currency"], strict=True)])
    mtm = live["notional"].to_numpy() * live["direction"].to_numpy() * (now / then - 1.0)
    return pd.Series(np.clip(mtm, 0.0, None), index=live["counterparty"]).groupby(level=0).sum() / nav


def fund_day(data: MarketData, fund: str, date: pd.Timestamp, cov: pd.DataFrame, z: float) -> FundDay | None:
    """All measures for one fund on one day, or ``None`` if the fund has no positions that day."""
    held = data.positions[(data.positions["fund"] == fund) & (data.positions["date"] == date)]
    if held.empty:
        return None
    quantities = held.groupby("security")["quantity"].sum()
    values = quantities * data.prices.loc[date, quantities.index]
    nav = float(values.sum() + data.funds.at[fund, "cash"])
    weights = values / nav
    var, sigma, contributions = var_contributions(weights, cov, z)
    issuers = data.securities.loc[weights.index, "issuer"]
    sectors = data.securities.loc[weights.index, "sector"]
    return FundDay(
        fund=fund,
        date=date,
        nav=nav,
        weights=weights,
        var=var,
        sigma=sigma,
        contributions=contributions,
        issuer_weights=weights.groupby(issuers).sum(),
        sector_weights=weights.groupby(sectors).sum(),
        counterparty_exposure=counterparty_exposure(data, fund, date, nav),
    )


def fund_history(
    data: MarketData, fund: str, covs: dict[pd.Timestamp, pd.DataFrame], z: float
) -> dict[pd.Timestamp, FundDay]:
    """Measures for every day the fund has positions, keyed by date."""
    days = {date: fund_day(data, fund, date, cov, z) for date, cov in covs.items()}
    return {date: day for date, day in days.items() if day is not None}


def decompose(today: FundDay, previous: FundDay, securities: pd.DataFrame) -> Decomposition:
    """Split the change in VaR into the change in each position's contribution.

    A position held on only one of the two days contributes zero on the other, so the changes sum exactly to the
    change in total VaR.
    """
    index = today.contributions.index.union(previous.contributions.index)
    change = today.contributions.reindex(index, fill_value=0.0) - previous.contributions.reindex(index, fill_value=0.0)
    return Decomposition(
        total_change=today.var - previous.var,
        by_position=change,
        by_sector=change.groupby(securities.loc[index, "sector"]).sum(),
        by_currency=change.groupby(securities.loc[index, "currency"]).sum(),
    )
