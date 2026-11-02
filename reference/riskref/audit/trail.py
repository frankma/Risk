"""Audit records, as set out in framework/04-controls.md: for every output, the facts it was generated from, the text
as generated, the grounding result and attempts, the thresholds version, and the human's edits, approver and time.
"""

import json
import re
from dataclasses import asdict, dataclass, replace
from datetime import UTC, datetime
from pathlib import Path

from riskref.narrate.facts import Facts
from riskref.narrate.grounding import GroundingResult


@dataclass(frozen=True)
class AuditRecord:
    record_id: str
    output: str  # "explanation", "message" or "log_entry"
    as_of: str
    fund: str
    facts: list[dict]
    generated_text: str
    backend: str
    grounding_passed: bool
    unmatched: list[str]
    attempts: int
    flagged: bool
    thresholds_version: str
    edited_text: str | None = None
    approver: str | None = None
    approved_at: str | None = None


def facts_to_dict(f: Facts) -> dict:
    out = asdict(f)
    out["as_of"] = f.as_of.strftime("%Y-%m-%d")
    out["values"] = {k: float(v) for k, v in f.values.items()}
    return out


def record_for(
    output: str,
    facts: list[Facts],
    text: str,
    grounding: GroundingResult,
    backend: str,
    attempts: int = 1,
    flagged: bool = False,
) -> AuditRecord:
    first = facts[0]
    parts = [first.as_of.strftime("%Y-%m-%d"), first.fund, output]
    if output == "explanation":
        parts += [first.kind, first.subject or first.measure]
    record_id = re.sub(r"[^a-z0-9]+", "-", " ".join(parts).lower()).strip("-")
    return AuditRecord(
        record_id=record_id,
        output=output,
        as_of=parts[0],
        fund=first.fund,
        facts=[facts_to_dict(f) for f in facts],
        generated_text=text,
        backend=backend,
        grounding_passed=grounding.passed,
        unmatched=list(grounding.unmatched),
        attempts=attempts,
        flagged=flagged,
        thresholds_version=first.thresholds_version,
    )


def write(record: AuditRecord, directory: Path) -> Path:
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / f"{record.record_id}.json"
    path.write_text(json.dumps(asdict(record), indent=2, sort_keys=True) + "\n")
    return path


def read(path: Path) -> AuditRecord:
    return AuditRecord(**json.loads(path.read_text()))


def sign_off(record: AuditRecord, edited_text: str, approver: str, when: datetime | None = None) -> AuditRecord:
    """Record the human's edited text and approval. The generated text is kept unchanged alongside it."""
    when = when or datetime.now(UTC)
    return replace(record, edited_text=edited_text, approver=approver, approved_at=when.isoformat(timespec="seconds"))
