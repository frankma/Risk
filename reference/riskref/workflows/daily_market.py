"""The redesigned daily market risk flow from pillars/market-risk.md, end to end:
load data -> compute -> rank -> draft -> grounding check -> queue ready for the risk manager's review.

Nothing is sent. Messages to portfolio managers and log entries are drafts for the risk manager to edit and approve.
"""

from dataclasses import dataclass
from pathlib import Path

import pandas as pd

from riskref.audit import trail
from riskref.compute.exceptions import Item, Thresholds, assess
from riskref.data.synthetic import MarketData
from riskref.narrate.backend import Draft, Narrator, draft_with_grounding
from riskref.narrate.facts import Facts, facts_for
from riskref.narrate.grounding import check
from riskref.narrate.template import TemplateNarrator

DEFAULT_OUTPUT = Path(__file__).resolve().parents[2] / "output"


@dataclass
class QueueEntry:
    item: Item
    facts: Facts
    draft: Draft


@dataclass
class FundDrafts:
    message: str
    log_entry: str
    grounded: bool


@dataclass
class ReviewQueue:
    as_of: pd.Timestamp
    thresholds_version: str
    entries: list[QueueEntry]  # ranked
    not_assessed: list[str]
    quiet: list[str]
    by_fund: dict[str, FundDrafts]  # in queue order
    audit_files: list[Path]


def run(
    data: MarketData, t: Thresholds, narrator: Narrator | None = None, output_dir: Path = DEFAULT_OUTPUT
) -> ReviewQueue:
    narrator = narrator or TemplateNarrator()
    assessment = assess(data, t)
    audit_dir = output_dir / "audit"
    audit_files: list[Path] = []

    entries = []
    for item in assessment.items:
        facts = facts_for(item, data.securities, t)
        draft = draft_with_grounding(narrator, facts, t.max_draft_attempts)
        entries.append(QueueEntry(item, facts, draft))
        record = trail.record_for(
            "explanation", [facts], draft.text, draft.grounding, draft.backend, draft.attempts, draft.flagged
        )
        audit_files.append(trail.write(record, audit_dir))

    by_fund: dict[str, FundDrafts] = {}
    for fund in dict.fromkeys(e.item.fund for e in entries):
        fund_entries = [e for e in entries if e.item.fund == fund]
        facts = [e.facts for e in fund_entries]
        message = narrator.message(fund, [e.draft.text for e in fund_entries])
        log_entry = narrator.log_entry(facts)
        message_check, log_check = check(message, facts), check(log_entry, facts)
        by_fund[fund] = FundDrafts(message, log_entry, message_check.passed and log_check.passed)
        for output, text, result in (("message", message, message_check), ("log_entry", log_entry, log_check)):
            audit_files.append(trail.write(trail.record_for(output, facts, text, result, narrator.name), audit_dir))

    return ReviewQueue(
        as_of=assessment.as_of,
        thresholds_version=assessment.thresholds_version,
        entries=entries,
        not_assessed=assessment.not_assessed,
        quiet=assessment.quiet,
        by_fund=by_fund,
        audit_files=audit_files,
    )


def describe(item: Item) -> str:
    text = f"{item.measure} {item.rule.replace('_', ' ')}"
    return f"{text} ({item.subject})" if item.subject else text


def render_note(queue: ReviewQueue) -> str:
    """The daily note as Markdown: ranked queue, funds not assessed, quiet funds and drafted messages."""
    day = queue.as_of.strftime("%Y-%m-%d")
    lines = [
        f"# Daily market risk note, {day}",
        "",
        f"**Draft for the risk manager's review.** Generated from synthetic data by the template backend with "
        f"thresholds version `{queue.thresholds_version}`. Every explanation has been through the grounding check. "
        "Nothing in this note has been sent.",
        "",
        "## Ranked queue",
        "",
        "| # | Fund | State | Item | Grounding |",
        "|---|---|---|---|---|",
    ]
    for n, e in enumerate(queue.entries, 1):
        grounding = "passed" if e.draft.grounding.passed else f"failed: {', '.join(e.draft.grounding.unmatched)}"
        if e.draft.flagged:
            grounding += ", fallback text (flagged)"
        lines.append(f"| {n} | {e.item.fund} | {e.item.state} | {describe(e.item)} | {grounding} |")
    lines.append("")
    for n, e in enumerate(queue.entries, 1):
        lines += [f"### {n}. {e.item.fund}: {e.item.state}, {describe(e.item)}", "", e.draft.text, ""]

    lines += ["## Not assessed", ""]
    if queue.not_assessed:
        lines += [
            f"- {fund}: no complete data for {day}. Not assessed, not shown as clean." for fund in queue.not_assessed
        ]
    else:
        lines.append("Every fund was assessed.")
    lines += ["", "## Nothing to report", "", ", ".join(queue.quiet) if queue.quiet else "None.", ""]

    lines += ["## Draft messages to portfolio managers", "", "To be edited and sent by the risk manager.", ""]
    for fund, drafts in queue.by_fund.items():
        lines += [f"### {fund}", ""] + [f"> {line}" if line else ">" for line in drafts.message.split("\n")] + [""]

    lines += ["## Draft log entries", ""] + [f"- {d.log_entry}" for d in queue.by_fund.values()] + [""]
    lines += [f"{len(queue.audit_files)} audit records written.", ""]
    return "\n".join(lines)


def write_note(queue: ReviewQueue, output_dir: Path = DEFAULT_OUTPUT) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    path = output_dir / f"daily_market_note_{queue.as_of.strftime('%Y-%m-%d')}.md"
    path.write_text(render_note(queue))
    return path
