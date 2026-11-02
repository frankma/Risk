"""The structured facts a draft is built from. A draft may use these numbers and names and nothing else."""

from dataclasses import dataclass, field

import pandas as pd

from riskref.compute.exceptions import Item, Thresholds

HORIZON_DAYS = 1


@dataclass(frozen=True)
class Facts:
    """Everything the narrator may say about one queue item.

    ``values`` holds every number the text may use: shares as fractions (0.0255 means 2.55%), counts as integers.
    ``labels`` holds every name the text may use; the grounding check ignores digits inside them ("Issuer 07").
    """

    fund: str
    kind: str  # the rule that produced the item
    state: str
    measure: str
    subject: str | None
    as_of: pd.Timestamp
    thresholds_version: str
    values: dict[str, float] = field(default_factory=dict)
    labels: dict[str, str] = field(default_factory=dict)

    def numbers(self) -> list[float]:
        return list(self.values.values())

    def identifiers(self) -> list[str]:
        return [self.fund, self.thresholds_version, self.as_of.strftime("%Y-%m-%d"), *self.labels.values()]


def facts_for(item: Item, securities: pd.DataFrame, t: Thresholds) -> Facts:
    """Build the facts for one queue item from what the compute step produced."""
    values: dict[str, float] = {}
    labels: dict[str, str] = {}
    if item.subject is not None:
        labels["subject"] = item.subject

    if item.measure == "VaR":
        values.update(horizon_days=HORIZON_DAYS, confidence=t.confidence)
    if item.limit is not None:
        values.update(value=item.value, limit=item.limit, utilisation=item.value / item.limit)
        values.update(early_warning=t.early_warning_share * item.limit, early_warning_share=t.early_warning_share)
    if item.days is not None:
        values["days"] = item.days

    if item.rule == "large_change":
        values.update(value=item.value, previous=item.previous, change=item.value - item.previous)
        values["change_share"] = item.value / item.previous - 1.0
        decomposition = item.decomposition
        driver = decomposition.by_position.idxmax()
        sector = decomposition.by_sector.idxmax()
        values.update(position_driver=decomposition.by_position[driver], sector_driver=decomposition.by_sector[sector])
        labels.update(
            position=driver,
            position_issuer=securities.at[driver, "issuer"],
            position_sector=securities.at[driver, "sector"],
            sector=sector,
        )
    if item.rule == "outside_range" or item.volatility is not None:
        volatility = item.volatility if item.volatility is not None else item.value
        values.update(volatility=volatility, range_low=item.range_low, range_high=item.range_high)
        values["range_window"] = t.range_window
    return Facts(
        fund=item.fund,
        kind=item.rule,
        state=item.state,
        measure=item.measure,
        subject=item.subject,
        as_of=item.as_of,
        thresholds_version=item.thresholds_version,
        values=values,
        labels=labels,
    )
