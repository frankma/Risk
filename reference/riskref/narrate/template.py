"""Deterministic template backend: fixed sentences that state the computed facts, in the style of the example drafts
in pillars/market-risk.md. It makes no recommendations; whether an item matters is the risk manager's judgement.
"""

from riskref.narrate.facts import Facts
from riskref.narrate.grounding import format_number


def pct(x: float, decimals: int = 2) -> str:
    return f"{format_number(x, decimals, 100)}%"


def points(x: float, decimals: int = 2) -> str:
    return format_number(x, decimals, 100)


def reading(f: Facts) -> str:
    """What is being measured, as it reads in a sentence."""
    v = f.values
    if f.measure == "VaR":
        return f"{v['horizon_days']}-day {format_number(v['confidence'], 0, 100)}% VaR"
    if f.measure == "counterparty exposure":
        return f"exposure to {f.subject}"
    if f.measure == "volatility":
        return "ex-ante volatility"
    return f"weight in {f.subject}"


class TemplateNarrator:
    name = "template"

    def draft(self, f: Facts) -> str:
        v = f.values
        if f.kind == "unreconciled":
            return (
                f"The change in {f.fund}'s VaR could not be reconciled to its position contributions, so no "
                "explanation has been drafted."
            )
        if f.kind == "large_change":
            text = (
                f"{f.fund}'s {reading(f)} rose from {pct(v['previous'])} to {pct(v['value'])} of net assets, a rise "
                f"of {pct(v['change_share'], 1)} since the previous day. The largest change by position was "
                f"{f.labels['position']} ({f.labels['position_issuer']}, {f.labels['position_sector']}), at "
                f"{points(v['position_driver'])} points; by sector, {f.labels['sector']} added "
                f"{points(v['sector_driver'])} points."
            )
            if "volatility" in v:
                text += " " + self._range_sentence(f, "Ex-ante volatility")
            return text
        if f.kind == "outside_range":
            return self._range_sentence(f, f"{f.fund}'s ex-ante volatility")
        if f.kind == "limit_breach":
            return f"{f.fund}'s {reading(f)} is {pct(v['value'])} of net assets, above its limit of {pct(v['limit'])}."
        if f.kind == "persistence":
            return (
                f"{f.fund}'s {reading(f)} has been above its {pct(v['early_warning'])} early warning for "
                f"{v['days']} consecutive days and stands at {pct(v['value'])}, against a limit of {pct(v['limit'])}."
            )
        if f.kind == "early_warning":
            if f.measure in ("VaR", "counterparty exposure"):
                return (
                    f"{f.fund}'s {reading(f)} is {pct(v['value'])} of net assets, {pct(v['utilisation'], 0)} of its "
                    f"{pct(v['limit'])} limit and above its early warning at {pct(v['early_warning_share'], 0)} of "
                    "the limit."
                )
            return (
                f"{f.fund}'s {reading(f)} is {pct(v['value'])} of net assets, above its early warning of "
                f"{pct(v['early_warning'])} and below its limit of {pct(v['limit'])}."
            )
        raise ValueError(f"no template for {f.kind}")

    def message(self, fund: str, drafts: list[str]) -> str:
        points_raised = "\n".join(f"- {d}" for d in drafts)
        return (
            f"Today's market risk review flagged {fund} on the points below. Could you confirm that the positions "
            f"behind them are as intended?\n\n{points_raised}"
        )

    def log_entry(self, facts: list[Facts]) -> str:
        first = facts[0]
        entries = "; ".join(f"{f.state}: {f.measure} {f.kind.replace('_', ' ')}" for f in facts)
        return f"{first.as_of.strftime('%Y-%m-%d')} | {first.fund} | {entries} | thresholds {first.thresholds_version}"

    @staticmethod
    def _range_sentence(f: Facts, start: str) -> str:
        v = f.values
        side = "above" if v["volatility"] > v["range_high"] else "below"
        return (
            f"{start} of {pct(v['volatility'])} is {side} its range of {pct(v['range_low'])} to "
            f"{pct(v['range_high'])} over the previous {v['range_window']} business days."
        )
