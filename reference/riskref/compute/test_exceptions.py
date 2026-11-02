import dataclasses

import pandas as pd
import pytest

from riskref.compute import exceptions as ex
from riskref.data import synthetic

T = ex.load_thresholds()
DATES = pd.bdate_range(end="2026-10-30", periods=10)


def _series(values: list[float]) -> pd.Series:
    return pd.Series(values, index=DATES[-len(values) :])


def _rules(items: list[ex.Item]) -> list[str]:
    return [i.rule for i in items]


def test_thresholds_carry_a_version():
    assert T.version
    assert 0 < T.early_warning_share < 1


def test_limit_breach_fires_and_clean_reading_does_not():
    assert _rules(ex.limit_items("Fund T", "VaR", None, _series([0.020, 0.026]), 0.025, T)) == ["limit_breach"]
    assert ex.limit_items("Fund T", "VaR", None, _series([0.020, 0.020]), 0.025, T) == []


def test_early_warning_is_a_watch_item():
    items = ex.limit_items("Fund T", "VaR", None, _series([0.020, 0.0235]), 0.025, T)
    assert _rules(items) == ["early_warning"]
    assert items[0].state == ex.WATCH


def test_persistence_needs_consecutive_days_above_the_early_warning():
    persistent = _series([0.020] + [0.0235] * T.persistence_days)
    items = ex.limit_items("Fund T", "issuer weight", "Issuer 01", persistent, 0.025, T)
    assert _rules(items) == ["early_warning", "persistence"]
    assert items[1].days == T.persistence_days
    interrupted = _series([0.0235, 0.020] + [0.0235] * (T.persistence_days - 1))
    assert _rules(ex.limit_items("Fund T", "issuer weight", "Issuer 01", interrupted, 0.025, T)) == ["early_warning"]


def test_volatility_outside_its_range_fires_in_both_directions():
    history = [0.15] * T.range_window
    dates = pd.bdate_range(end="2026-10-30", periods=T.range_window + 1)
    for today, expected in [(0.17, ["outside_range"]), (0.13, ["outside_range"]), (0.15, [])]:
        assert _rules(ex.range_item("Fund T", pd.Series(history + [today], index=dates), T)) == expected


def test_ranking_follows_the_chapter():
    def item(fund: str, rule: str, ratio: float) -> ex.Item:
        return ex.Item(fund, rule, "VaR", 0.0, 0.0, ratio, DATES[-1], T.version)

    items = [
        item("Fund P", "persistence", 0.99),
        item("Fund W", "early_warning", 0.95),
        item("Fund X", "large_change", 1.5),
        item("Fund B", "limit_breach", 1.01),
        item("Fund Y", "outside_range", 1.2),
        item("Fund Y", "early_warning", 0.91),
    ]
    ranked = [(i.fund, i.rule) for i in ex.rank(items)]
    assert ranked == [
        ("Fund B", "limit_breach"),
        ("Fund Y", "outside_range"),  # a fund with two items ranks above one with one, within a tier
        ("Fund X", "large_change"),
        ("Fund Y", "early_warning"),
        ("Fund W", "early_warning"),
        ("Fund P", "persistence"),
    ]


@pytest.fixture(scope="module")
def assessment():
    return ex.assess(synthetic.generate(), T)


def test_missing_data_is_not_assessed(assessment):
    assert assessment.not_assessed == ["Fund E"]
    assert "Fund E" not in assessment.quiet
    assert all(i.fund != "Fund E" for i in assessment.items)


def test_planted_funds_give_their_expected_items(assessment):
    found = {(i.fund, i.rule, i.measure, i.subject) for i in assessment.items}
    assert found == {
        ("Fund A", "large_change", "VaR", None),
        ("Fund A", "early_warning", "VaR", None),
        ("Fund B", "early_warning", "counterparty exposure", "Counterparty X"),
        ("Fund C", "early_warning", "issuer weight", "Issuer 31"),
        ("Fund C", "persistence", "issuer weight", "Issuer 31"),
        ("Fund D", "limit_breach", "issuer weight", "Issuer 15"),
    }
    assert assessment.quiet == [f"Fund {x}" for x in "FGHIJKL"]


def test_every_result_records_the_thresholds_version(assessment):
    assert {i.thresholds_version for i in assessment.items} == {T.version}


def test_unreconciled_decomposition_is_an_item_and_nothing_is_drafted_from_it(assessment):
    data = synthetic.generate()
    today = assessment.today["Fund A"]
    previous = dataclasses.replace(today, date=DATES[-2], var=today.var * 0.5)  # contributions no longer explain it
    items, _ = ex.evaluate_fund(
        "Fund A", {previous.date: previous, today.date: today}, data.funds.loc["Fund A"], data.securities, T
    )
    assert "unreconciled" in _rules(items)
    assert "large_change" not in _rules(items)


def test_a_var_jump_and_volatility_outside_its_range_are_grouped_into_one_exception():
    def item(rule: str, **kw) -> ex.Item:
        return ex.Item("Fund T", rule, "VaR", 0.02, 0.1, 1.2, DATES[-1], T.version, **kw)

    change = item("large_change", previous=0.017)
    outside = item("outside_range", range_low=0.14, range_high=0.15)
    warning = item("early_warning")
    grouped = ex.group_shared_driver([change, outside, warning])
    assert _rules(grouped) == ["large_change", "early_warning"]
    assert grouped[0].volatility == outside.value
    assert (grouped[0].range_low, grouped[0].range_high) == (0.14, 0.15)
    assert _rules(ex.group_shared_driver([outside])) == ["outside_range"]  # on its own, it stays


def test_fund_a_large_change_carries_its_volatility_reading(assessment):
    change = next(i for i in assessment.items if i.fund == "Fund A" and i.rule == "large_change")
    assert change.volatility is not None
    assert change.volatility > change.range_high
