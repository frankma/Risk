from datetime import UTC, datetime

import pandas as pd

from riskref.audit import trail
from riskref.narrate.facts import Facts
from riskref.narrate.grounding import check

FACTS = Facts(
    "Fund D", "limit_breach", "exception", "issuer weight", "Issuer 15", pd.Timestamp("2026-10-30"),
    "illustrative-2026.1", {"value": 0.104, "limit": 0.10}, {"subject": "Issuer 15"},
)  # fmt: skip
TEXT = "Fund D's weight in Issuer 15 is 10.40% of net assets, above its limit of 10.00%."


def test_record_round_trips_through_json(tmp_path):
    record = trail.record_for("explanation", [FACTS], TEXT, check(TEXT, FACTS), "template")
    path = trail.write(record, tmp_path)
    assert path.name == "2026-10-30-fund-d-explanation-limit-breach-issuer-15.json"
    assert trail.read(path) == record
    assert record.thresholds_version == "illustrative-2026.1"
    assert record.grounding_passed


def test_sign_off_keeps_the_generated_text():
    record = trail.record_for("explanation", [FACTS], TEXT, check(TEXT, FACTS), "template")
    when = datetime(2026, 10, 30, 9, 15, tzinfo=UTC)
    signed = trail.sign_off(
        record, "Fund D is above its Issuer 15 limit; PM confirms a sale today.", "Risk manager", when
    )
    assert signed.generated_text == TEXT
    assert signed.edited_text.startswith("Fund D is above")
    assert signed.approver == "Risk manager"
    assert signed.approved_at == "2026-10-30T09:15:00+00:00"
    assert record.edited_text is None  # the original record is unchanged
