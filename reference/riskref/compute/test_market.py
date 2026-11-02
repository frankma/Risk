import numpy as np
import pandas as pd
import pytest

from riskref.compute import market
from riskref.data import synthetic

Z = market.z_score(0.99)


def _cov(securities: list[str], seed: int = 1) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    a = rng.normal(0.0, 0.01, (len(securities), len(securities)))
    return pd.DataFrame(a @ a.T + np.eye(len(securities)) * 1e-5, index=securities, columns=securities)


def _day(weights: pd.Series, cov: pd.DataFrame) -> market.FundDay:
    var, sigma, contributions = market.var_contributions(weights, cov, Z)
    empty = pd.Series(dtype=float)
    return market.FundDay(
        "Fund T", pd.Timestamp("2026-10-30"), 1.0, weights, var, sigma, contributions, empty, empty, empty
    )


def test_var_matches_the_closed_form():
    cov = pd.DataFrame([[0.0001, 0.0], [0.0, 0.0004]], index=["S1", "S2"], columns=["S1", "S2"])
    var, sigma, _ = market.var_contributions(pd.Series([0.5, 0.5], index=["S1", "S2"]), cov, Z)
    assert sigma == pytest.approx(np.sqrt(0.25 * 0.0001 + 0.25 * 0.0004))
    assert var == pytest.approx(Z * sigma)


def test_contributions_sum_to_var():
    securities = [f"S{i}" for i in range(8)]
    weights = pd.Series(np.linspace(0.05, 0.15, 8), index=securities)
    var, _, contributions = market.var_contributions(weights, _cov(securities), Z)
    assert contributions.sum() == pytest.approx(var, rel=1e-12)


def test_change_decomposition_reconciles_when_positions_enter_and_leave():
    securities = [f"S{i}" for i in range(6)]
    cov = _cov(securities)
    info = pd.DataFrame({"sector": ["A", "A", "B", "B", "C", "C"], "currency": ["USD", "EUR"] * 3}, index=securities)
    previous = _day(pd.Series([0.2, 0.2, 0.2, 0.2], index=securities[:4]), cov)
    today = _day(pd.Series([0.3, 0.2, 0.2, 0.25], index=securities[2:]), cov)
    decomposition = market.decompose(today, previous, info)
    assert decomposition.reconciles(1e-12)
    assert decomposition.by_sector.sum() == pytest.approx(decomposition.total_change)
    assert decomposition.by_currency.sum() == pytest.approx(decomposition.total_change)


def test_volatility_is_annualised():
    day = _day(pd.Series([1.0], index=["S1"]), pd.DataFrame([[0.0001]], index=["S1"], columns=["S1"]))
    assert day.volatility == pytest.approx(0.01 * np.sqrt(252))


def test_counterparty_exposure_counts_only_positive_mark_to_market():
    data = synthetic.generate()
    exposure = market.counterparty_exposure(data, "Fund B", data.as_of, nav=1e9)
    assert (exposure >= 0).all()
    assert exposure["Counterparty X"] > 0
