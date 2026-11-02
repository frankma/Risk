import re

import pandas as pd
import pytest

from riskref.narrate.facts import Facts
from riskref.narrate.grounding import check, extract_numbers

AS_OF = pd.Timestamp("2026-10-30")


def facts(values: dict[str, float], **labels: str) -> Facts:
    return Facts("Fund A", "test", "watch", "VaR", None, AS_OF, "illustrative-2026.1", values, labels)


# The three example drafts in pillars/market-risk.md, with their facts tables.
CHAPTER_EXAMPLES = [
    (
        "Fund A's 1-day 99% VaR rose from 1.84% to 2.31%, which is 92% of its 2.50% limit. Most of the 0.47 percentage "
        "point rise came from the technology equity basket (0.29 points), with a further 0.12 points from higher US "
        "dollar exposure.",
        Facts("Fund A", "large_change", "watch", "VaR", None, AS_OF, "v", {
            "horizon": 1, "confidence": 0.99, "today": 0.0231, "previous": 0.0184, "change": 0.0047,
            "limit": 0.025, "utilisation": 0.92, "position": 0.0029, "factor": 0.0012,
        }),
    ),
    (
        "Fund B's exposure to Counterparty X rose from 3.1% to 4.4% of net assets, 88% of its 5.0% limit. The increase "
        "follows new currency forwards traded with that counterparty on the previous day.",
        Facts("Fund B", "early_warning", "watch", "counterparty exposure", "Counterparty X", AS_OF, "v", {
            "today": 0.044, "previous": 0.031, "limit": 0.05, "utilisation": 0.88,
        }, {"subject": "Counterparty X"}),
    ),
    (
        "Fund C's largest single-issuer weight has been above its 9.0% early-warning level for 6 consecutive days and "
        "stands at 9.6% today, against a limit of 10.0%.",
        Facts("Fund C", "persistence", "watch", "issuer weight", None, AS_OF, "v", {
            "today": 0.096, "early_warning": 0.09, "limit": 0.10, "days": 6,
        }),
    ),
]  # fmt: skip


@pytest.mark.parametrize(("text", "chapter_facts"), CHAPTER_EXAMPLES)
def test_the_chapter_examples_pass(text, chapter_facts):
    assert check(text, chapter_facts).passed


@pytest.mark.parametrize(("text", "chapter_facts"), CHAPTER_EXAMPLES)
def test_changing_any_number_in_a_chapter_example_makes_it_fail(text, chapter_facts):
    numbers = list(re.finditer(r"\d+(?:\.\d+)?", text))
    assert numbers
    for m in numbers:
        last = m.group(0)[-1]
        altered = text[: m.end() - 1] + ("3" if last != "3" else "4") + text[m.end() :]
        result = check(altered, chapter_facts)
        assert not result.passed, f"altering {m.group(0)} still passed"


def test_number_words_are_checked():
    assert check("up from 11% three months ago", facts({"months": 3, "previous": 0.11})).passed
    assert not check("up from 11% four months ago", facts({"months": 3, "previous": 0.11})).passed
    assert check("over twenty-one days", facts({"days": 21})).passed


def test_percentages_points_and_basis_points():
    f = facts({"change": 0.0047})
    for text in ["0.47%", "0.47 percentage points", "0.47 percentage point rise", "0.47 points", "47 bp"]:
        assert check(text, f).passed, text
    assert not check("0.48 points", f).passed


def test_multiples():
    f = facts({"before": 2.4, "after": 1.6})
    assert check("coverage falls from 2.4x to 1.6x", f).passed
    assert not check("coverage falls from 2.4x to 1.7x", f).passed


def test_scaled_values_round_to_the_stated_precision():
    f = facts({"notional": 12_450_000})
    for text in ["12.45 million", "12.5m", "12,450,000", "12 million"]:
        assert check(text, f).passed, text
    assert not check("12.4m", f).passed
    assert not check("13 million", f).passed


def test_rounding_beyond_the_stated_precision_fails():
    f = facts({"var": 0.0255})
    assert check("2.55%", f).passed
    assert check("2.6%", f).passed
    assert not check("2.5%", f).passed
    assert not check("2%", f).passed


def test_an_untraceable_number_fails():
    result = check("VaR rose by 7.5% after 3 new positions.", facts({"var": 0.0255}))
    assert not result.passed
    assert result.unmatched == ["7.5%", "3"]


def test_digits_inside_names_are_not_figures():
    f = facts({"weight": 0.0945}, subject="Issuer 31", security="Security 07")
    assert check("Security 07 of Issuer 31 is 9.45% of net assets.", f).passed
    assert [n.text for n in extract_numbers("Issuer 31 at 9.45%", ["Issuer 31"])] == ["9.45%"]


def test_dates_and_versions_in_a_log_entry_are_identifiers():
    assert check("2026-10-30 | Fund A | thresholds illustrative-2026.1", facts({})).passed
