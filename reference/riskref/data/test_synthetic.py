import pandas as pd
import pytest

from riskref.data import synthetic


@pytest.fixture(scope="module")
def data():
    return synthetic.generate()


def test_generation_is_reproducible(data):
    again = synthetic.generate()
    pd.testing.assert_frame_equal(data.prices, again.prices)
    pd.testing.assert_frame_equal(data.positions, again.positions)
    pd.testing.assert_frame_equal(data.funds, again.funds)


def test_sizes(data):
    assert len(data.funds) == 12
    assert len(data.securities) == 60
    assert len(data.prices) == synthetic.N_PRICE_DAYS
    assert data.positions["date"].nunique() == synthetic.N_POSITION_DAYS
    assert data.as_of == data.prices.index[-1]


def test_names_are_generic(data):
    assert all(name.startswith("Fund ") for name in data.funds.index)
    assert all(name.startswith("Issuer ") for name in data.securities["issuer"])
    assert all(name.startswith("Counterparty ") for name in data.forwards["counterparty"])


def test_fund_e_has_no_positions_on_the_last_day(data):
    last_day = data.positions[data.positions["date"] == data.as_of]
    assert "Fund E" not in set(last_day["fund"])
    assert set(last_day["fund"]) == set(data.funds.index) - {"Fund E"}


def test_every_fund_has_limits(data):
    limits = data.funds[["var_limit", "issuer_limit", "sector_limit", "counterparty_limit"]]
    assert (limits > 0).all().all()
