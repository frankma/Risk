"""The narration interface and the grounding loop around it.

The template backend is the only narrator in this milestone. An AI backend would be a second class with the same
three methods, selected by environment variable; whatever it returns goes through ``draft_with_grounding`` exactly
as the template's output does, so the control does not depend on which backend wrote the text.
"""

from dataclasses import dataclass
from typing import Protocol

from riskref.narrate.facts import Facts
from riskref.narrate.grounding import GroundingResult, check
from riskref.narrate.template import TemplateNarrator


class Narrator(Protocol):
    name: str

    def draft(self, facts: Facts) -> str: ...

    def message(self, fund: str, drafts: list[str]) -> str: ...

    def log_entry(self, facts: list[Facts]) -> str: ...


@dataclass(frozen=True)
class Draft:
    text: str
    grounding: GroundingResult
    attempts: int
    flagged: bool  # True if the narrator's drafts kept failing and the plain template text was used instead
    backend: str


def draft_with_grounding(narrator: Narrator, facts: Facts, max_attempts: int) -> Draft:
    """Draft until the text passes the grounding check, then fall back to the plain template text and flag it."""
    for attempt in range(1, max_attempts + 1):
        text = narrator.draft(facts)
        result = check(text, facts)
        if result.passed:
            return Draft(text, result, attempt, flagged=False, backend=narrator.name)
    fallback = TemplateNarrator()
    text = fallback.draft(facts)
    return Draft(text, check(text, facts), max_attempts, flagged=True, backend=fallback.name)
