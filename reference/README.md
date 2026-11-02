# Reference implementations

Runnable examples on synthetic data that show the framework's core pattern: **code computes, AI narrates, a human
judges.** Code computes every figure and ranks what needs attention; a narrator drafts text from those figures only;
the grounding check rejects any text with a number the code did not produce; the risk manager reviews, edits and signs
off. The examples run without an AI service: the narrator is a deterministic template, and the grounding check runs on
its output, so the control is exercised on every run.

The first example is the **daily market risk exception note**, which implements the redesigned flow in
[market risk](../pillars/market-risk.md).

## Run it
Requires Python 3.12 or later and [uv](https://docs.astral.sh/uv/).

```bash
uv sync
uv run pytest
uv run ruff check
uv run python reference/examples/daily_market_note.py
```

The example writes `reference/output/daily_market_note_2026-10-30.md` and one audit record per output under
`reference/output/audit/`. The output folder is not committed.

## What the note shows
The synthetic data is staged so that the note shows each kind of item in the market risk chapter. All names and
figures are invented.

| Fund | Situation | In the note |
|---|---|---|
| Fund A | A new Technology position lifts VaR sharply, close to its limit | Exception: VaR large change, with volatility outside its usual range grouped into it; watch: VaR early warning |
| Fund B | New forwards build exposure to Counterparty X | Watch: counterparty exposure approaching its limit |
| Fund C | An issuer weight has stayed above its early warning | Watch: early warning and persistence |
| Fund D | An issuer weight is above its limit | Exception: limit breach |
| Fund E | No positions on the last day | Not assessed, never shown as clean |
| Funds F–L | Ordinary drift | Nothing to report |

## Modules

| Module | What it does | Framework |
|---|---|---|
| `riskref/data/synthetic.py` | Seeded synthetic market, funds, positions, forwards and illustrative limits | |
| `riskref/compute/market.py` | Parametric VaR with Euler contributions, change decomposition, ex-ante volatility, concentration, counterparty exposure | [Market risk](../pillars/market-risk.md), flagship redesign |
| `riskref/compute/exceptions.py` | Rules, exception and watch states, ranking; funds with missing data are not assessed | [Market risk](../pillars/market-risk.md#materiality-and-exceptions) |
| `config/thresholds.toml` | Governed parameters with a version string recorded on every result | [Controls](../framework/04-controls.md#materiality-thresholds-as-governed-parameters) |
| `riskref/narrate/facts.py` | The facts a draft may use, and nothing else | [Principles](../framework/01-principles.md#3-the-ai-never-produces-a-number) |
| `riskref/narrate/template.py` | Deterministic template narrator: explanations, messages to portfolio managers, log entries | [Controls](../framework/04-controls.md#fallback) |
| `riskref/narrate/backend.py` | The narrator interface; retries and falls back to the template, flagged, after repeated grounding failures | [Controls](../framework/04-controls.md#the-grounding-check) |
| `riskref/narrate/grounding.py` | The grounding check: numbers, number words, percentages, points, basis points, multiples, scaled values | [Controls](../framework/04-controls.md#the-grounding-check) |
| `riskref/audit/trail.py` | One JSON record per output; sign-off keeps the generated text beside the edited text | [Controls](../framework/04-controls.md#the-audit-trail) |
| `riskref/workflows/daily_market.py` | Load, compute, rank, draft, grounding check, review queue and note | [Market risk](../pillars/market-risk.md#flagship-redesign-daily-monitoring-and-exception-handling) |
| `examples/daily_market_note.py` | Runs the workflow for the last day and writes the note | |

Tests sit next to the modules they cover (`test_*.py`).

## Methods and simplifications
The examples demonstrate a workflow, not a risk model.

- **VaR** is 1-day 99% parametric (normal) VaR on securities, from the sample covariance of daily returns over 250
  business days. Euler contributions by position sum exactly to VaR, so the day-on-day change decomposes exactly by
  position, sector and currency. Currency forwards enter counterparty exposure but not VaR.
- **Volatility against its own history** compares today's ex-ante volatility with the highest and lowest of the
  previous 60 business days. VaR and ex-ante volatility come from the same portfolio volatility, so when a VaR jump
  also takes volatility outside its range, the two are grouped into one exception.
- **Counterparty exposure** is the positive mark-to-market of forwards per counterparty, as a share of net assets.
- **Limits** are illustrative and set from each fund's typical risk. The seed and the planted trades are chosen so that
  each situation above appears cleanly and the other funds stay quiet.
- **Ranking** puts exceptions before watch items: breaches, then other exceptions, then early warnings, then
  persistence. Within a tier, a fund with more items ranks higher, then items are ordered by size relative to their
  threshold.

## Narrators
The template narrator is deterministic, so tests and demonstrations run offline and give the same note every time.
To add an AI narrator, implement the same three methods (`draft`, `message`, `log_entry`) in
`riskref/narrate/backend.py` and select it by environment variable, reading any key from the environment. Whatever any
narrator writes passes through the same grounding check, retry and fallback, and is recorded in the same audit trail.
