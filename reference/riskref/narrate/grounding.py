"""The grounding check from framework/04-controls.md.

Every number in a text is extracted and matched against the facts the text was drafted from. Formatting and rounding
to the stated precision are allowed ("2.55%" for 0.0255, "12.5m" for 12,450,000); a different figure is not. Text with
an unmatched number fails.
"""

import re
from dataclasses import dataclass
from decimal import ROUND_HALF_UP, Decimal

from riskref.narrate.facts import Facts

_UNITS = {  # unit as written -> scale applied to a fact before comparing
    "%": 100,
    "percent": 100,
    "percentage points": 100,
    "percentage point": 100,
    "points": 100,
    "pp": 100,
    "bp": 10_000,
    "x": 1,
    "million": Decimal("0.000001"),
    "m": Decimal("0.000001"),
    "billion": Decimal("0.000000001"),
    "bn": Decimal("0.000000001"),
}
_UNIT_PATTERN = "|".join(sorted((re.escape(u) for u in _UNITS), key=len, reverse=True))
_NUMBER = re.compile(
    rf"(?<![\w.])(?P<number>[-+]?\d{{1,3}}(?:,\d{{3}})+(?:\.\d+)?|[-+]?\d+(?:\.\d+)?)"
    rf"(?:\s?(?P<unit>{_UNIT_PATTERN})(?![\w]))?"
)

_ONES = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]
_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
_WORDS = {word: n for n, word in enumerate(_ONES)}
for i, tens in enumerate(_TENS):
    _WORDS[tens] = 20 + 10 * i
    for j in range(1, 10):
        _WORDS[f"{tens}-{_ONES[j]}"] = 20 + 10 * i + j
_WORD = re.compile(r"\b(" + "|".join(sorted(_WORDS, key=len, reverse=True)) + r")\b", re.IGNORECASE)


@dataclass(frozen=True)
class Number:
    text: str
    value: Decimal
    decimals: int
    unit: str | None


@dataclass(frozen=True)
class GroundingResult:
    passed: bool
    unmatched: list[str]


def round_half_up(value: Decimal, decimals: int) -> Decimal:
    return value.quantize(Decimal(1).scaleb(-decimals), rounding=ROUND_HALF_UP)


def format_number(value: float, decimals: int, scale: int | Decimal = 1) -> str:
    """Format a fact the way the grounding check reads it back; templates use this so they always match."""
    return f"{round_half_up(Decimal(repr(float(value))) * scale, decimals):f}"


def extract_numbers(text: str, identifiers: list[str] | None = None) -> list[Number]:
    """Every number in ``text``, with its unit. Digits inside identifiers ("Issuer 07") are not numbers."""
    for name in sorted(identifiers or [], key=len, reverse=True):
        text = text.replace(name, " ")
    found = []
    for m in _NUMBER.finditer(text):
        raw = m.group("number").replace(",", "")
        decimals = len(raw.split(".")[1]) if "." in raw else 0
        unit = m.group("unit").lower() if m.group("unit") else None
        found.append(Number(m.group(0).strip(), Decimal(raw), decimals, unit))
    for m in _WORD.finditer(text):
        found.append(Number(m.group(0), Decimal(_WORDS[m.group(0).lower()]), 0, None))
    return found


def matches(number: Number, fact: float) -> bool:
    scale = _UNITS[number.unit] if number.unit else 1
    return round_half_up(Decimal(repr(float(fact))) * scale, number.decimals) == number.value


def check(text: str, facts: Facts | list[Facts]) -> GroundingResult:
    """Pass if every number in ``text`` matches a value in the facts at the precision written."""
    facts = facts if isinstance(facts, list) else [facts]
    values = [v for f in facts for v in f.numbers()]
    identifiers = [name for f in facts for name in f.identifiers()]
    unmatched = [n.text for n in extract_numbers(text, identifiers) if not any(matches(n, v) for v in values)]
    return GroundingResult(passed=not unmatched, unmatched=unmatched)
