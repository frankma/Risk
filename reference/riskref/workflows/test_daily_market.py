import pytest

from riskref.compute.exceptions import load_thresholds
from riskref.data.synthetic import generate
from riskref.workflows import daily_market


@pytest.fixture(scope="module")
def run(tmp_path_factory):
    output = tmp_path_factory.mktemp("output")
    queue = daily_market.run(generate(), load_thresholds(), output_dir=output)
    return queue, output


def test_queue_is_ranked_as_the_chapter_describes(run):
    queue, _ = run
    order = [(e.item.fund, e.item.rule) for e in queue.entries]
    assert order == [
        ("Fund D", "limit_breach"),
        ("Fund A", "large_change"),
        ("Fund C", "early_warning"),
        ("Fund A", "early_warning"),
        ("Fund B", "early_warning"),
        ("Fund C", "persistence"),
    ]


def test_missing_data_is_not_assessed_and_quiet_funds_are_listed(run):
    queue, _ = run
    assert queue.not_assessed == ["Fund E"]
    assert queue.quiet == [f"Fund {x}" for x in "FGHIJKL"]


def test_every_output_passes_grounding(run):
    queue, _ = run
    assert all(e.draft.grounding.passed and not e.draft.flagged for e in queue.entries)
    assert all(d.grounded for d in queue.by_fund.values())


def test_audit_records_are_written_for_every_output(run):
    queue, output = run
    files = sorted((output / "audit").glob("*.json"))
    assert len(files) == len(queue.entries) + 2 * len(queue.by_fund)
    assert set(files) == set(queue.audit_files)


def test_note_shows_queue_not_assessed_funds_and_drafts(run, tmp_path):
    queue, _ = run
    path = daily_market.write_note(queue, tmp_path)
    note = path.read_text()
    assert path.name == "daily_market_note_2026-10-30.md"
    assert "Nothing in this note has been sent." in note
    assert "Fund E: no complete data" in note
    assert "### Fund A" in note
    for entry in queue.entries:
        assert entry.draft.text in note


def test_the_run_is_reproducible(run, tmp_path):
    queue, _ = run
    again = daily_market.run(generate(), load_thresholds(), output_dir=tmp_path)
    assert daily_market.render_note(again) == daily_market.render_note(queue)
