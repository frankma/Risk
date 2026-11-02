import pytest

from riskref.compute.exceptions import assess, load_thresholds
from riskref.data.synthetic import generate
from riskref.narrate.backend import draft_with_grounding
from riskref.narrate.facts import facts_for
from riskref.narrate.grounding import check
from riskref.narrate.template import TemplateNarrator

T = load_thresholds()


@pytest.fixture(scope="module")
def queue():
    data = generate()
    assessment = assess(data, T)
    return [facts_for(item, data.securities, T) for item in assessment.items]


def test_every_template_draft_passes_the_grounding_check(queue):
    narrator = TemplateNarrator()
    for f in queue:
        draft = draft_with_grounding(narrator, f, T.max_draft_attempts)
        assert draft.grounding.passed, (f.fund, f.kind, draft.grounding.unmatched)
        assert draft.attempts == 1
        assert not draft.flagged


def test_drafts_make_no_recommendations(queue):
    narrator = TemplateNarrator()
    for f in queue:
        text = narrator.draft(f).lower()
        assert not any(word in text for word in ("should", "recommend", "must", "reduce", "sell"))


def test_message_and_log_entry_are_grounded(queue):
    narrator = TemplateNarrator()
    fund_a = [f for f in queue if f.fund == "Fund A"]
    message = narrator.message("Fund A", [narrator.draft(f) for f in fund_a])
    log_entry = narrator.log_entry(fund_a)
    assert check(message, fund_a).passed
    assert check(log_entry, fund_a).passed


class AlwaysWrong:
    """A stand-in for a narrator that keeps inventing a number."""

    name = "always-wrong"

    def __init__(self):
        self.calls = 0

    def draft(self, facts):
        self.calls += 1
        return f"{facts.fund}'s VaR is 9.99% of net assets."

    def message(self, fund, drafts):
        return ""

    def log_entry(self, facts):
        return ""


def test_repeated_failures_fall_back_to_the_plain_template_and_are_flagged(queue):
    narrator = AlwaysWrong()
    draft = draft_with_grounding(narrator, queue[0], T.max_draft_attempts)
    assert narrator.calls == T.max_draft_attempts
    assert draft.flagged
    assert draft.backend == "template"
    assert draft.text == TemplateNarrator().draft(queue[0])
    assert draft.grounding.passed
