"""Run the daily market risk workflow on the synthetic data and write the note to reference/output/.

uv run python reference/examples/daily_market_note.py
"""

from riskref.compute.exceptions import load_thresholds
from riskref.data.synthetic import generate
from riskref.workflows.daily_market import run, write_note


def main() -> None:
    queue = run(generate(), load_thresholds())
    path = write_note(queue)
    print(f"{len(queue.entries)} items in the queue, {len(queue.not_assessed)} fund(s) not assessed.")
    print(f"Note written to {path}")


if __name__ == "__main__":
    main()
