# New portfolio review

## The essentials
**New portfolio review** asks whether everything the pillars rely on is in place before a portfolio takes its first
client money, or changes enough to be a new portfolio in all but name.

**How the work is done:** the AI extracts the draft mandate terms from the documents, and the analytics engine shows any
expected term it did not find as a gap, runs the pillars' measures on a model portfolio and checks that the data is
ready. The risk manager confirms the terms, proposes the first internal limits to the head of risk and writes the
opinion. On launch day the analytics engine confirms that everything agreed is in place.

**The opinion is not a veto:** product governance decides whether a portfolio launches. The risk function gives a
recorded opinion and can escalate to the risk committee.

**Ready on day one:** a portfolio is monitored as promised from its first day only if its mandate terms, internal
limits, data and a liquidity profile that fits its dealing terms are in place before launch. The review starts as soon
as draft documents exist and closes the gaps before the first client money arrives.

The rest of this chapter is the detail behind these points.

## What the review covers
- **New open-ended and closed-ended funds.**
- **New segregated mandates.**
- **Material changes to an existing portfolio:** a change of strategy or benchmark, a merger, or a change in dealing
  terms. A change of strategy is a relaunch in everything but name, and is reviewed as one.

A change to a portfolio's governing documents triggers the re-extraction of its mandate terms, as set out in
[performance risk](performance-risk.md#controls-and-measures-specific-to-this-pillar); where the change is material, it
also triggers this review. A new instrument that an existing portfolio wants to hold is reviewed in [market
risk](market-risk.md#workflows-in-this-pillar), not here.

The review runs in twelve steps:

| # | Step | Owner |
|---|---|---|
| 1 | Extract the draft mandate terms, each linked to its passage | AI |
| 2 | Check the terms against those expected for the portfolio's type; show each missing term as a gap | Analytics engine |
| 3 | Confirm the terms; request the model portfolio | Risk manager |
| 4 | Run the pillars' measures on the model portfolio; test the benchmark and the liquidity profile | Analytics engine |
| 5 | Check data readiness; propose internal limits, early warnings and the alpha and beta construction | Analytics engine |
| 6 | Consult the portfolio manager; decide the early warnings and the construction; put the internal limits to the head of risk | Risk manager |
| 7 | Approve the first internal limits | Head of risk |
| 8 | Draft the readiness summary | AI |
| 9 | Grounding check on the summary | Analytics engine |
| 10 | Write the opinion and any conditions | Risk manager |
| 11 | Sign off the opinion, which goes to product governance for its decision | Head of risk |
| 12 | On launch day, confirm every agreed item is in place | Analytics engine |

## What must be in place before launch
| Item | What is tested | Defined in |
|---|---|---|
| Mandate terms | The objective, benchmark, style, limits and dealing terms, extracted and confirmed | [Performance risk](performance-risk.md#mandate-terms) |
| Benchmark | It passes the benchmark tests: specified in advance, investable, unambiguous, measurable, appropriate to the style and owned | [Performance risk](performance-risk.md#benchmarks-and-peer-groups) |
| Limits | Internal limits and early warnings set by the risk function; the mandate and regulatory limits recorded, with each risk-measured limit set up for the risk function to monitor | [Limits and escalation](../framework/04-limits-and-escalation.md) |
| Liquidity profile | Redemption coverage under the scenarios for calls on cash, at the launch size and the expected size, against the dealing terms | [Liquidity risk](liquidity-risk.md#calls-on-cash) |
| Data | Every instrument the portfolio expects to hold, and every instrument in its top-down portfolio, can be priced, classified and measured by the analytics engine, or has a proxy under the policy | [Data integrity](../framework/03-data-integrity.md#proxies) |
| Alpha and beta construction | The benchmark portfolio, the risk-free rate, the buckets, the instrument inside each, the factor list and each factor's generator tag, declared before the first period | [Alpha and beta method](alpha-and-beta-method.md#booked-or-derived) |
| Liquidity management tools | The tools the documents provide for, and whether each is ready by liquidity risk's readiness test | [Liquidity risk](liquidity-risk.md#workflows-in-this-pillar) |
| Stress | The model portfolio's stress loss against the drawdown tolerance | [Market risk](market-risk.md#stress-and-reverse-stress) |
| Seed investors | Expected investor concentration at launch is recorded, with the date or size at which it should fall below the rule; until then the breach is expected, not an exception | [Liquidity risk](liquidity-risk.md#materiality-and-exceptions) |

## The risk function's opinion
The opinion states whether the portfolio can be monitored as its mandate promises, any conditions that must be met, and
the reasons. It links to the readiness summary and the review's results in the [shared
record](../framework/05-principles.md#7-hand-over-judgement-not-documents), where product governance reads them. Where
product governance proceeds against it, the risk function can escalate to the risk committee.

## What the AI drafts
Every figure the AI extracts must appear in the passage it links to, and every number in a draft appears in the facts
beside it, so the [grounding check](../framework/08-controls.md#the-grounding-check) would pass. **The funds and figures
are illustrative.**

**Extracted mandate terms.**

| Term | Extracted value | Source passage |
|---|---|---|
| Single-issuer limit | 10% of net assets | "not more than 10% of its net assets in securities of any single issuer" |
| Dealing | Daily | "shares may be redeemed on any business day" |
| Benchmark | A broad index of large companies | "measured against a broad index of large companies" |
| Liquidity management tools | Not found: a gap, as a fund dealing daily is expected to state them | None |

Each extracted value is confirmed by the risk manager before it is used, and the single-issuer limit, a hard limit, is
reconciled to compliance's coded rule. The missing liquidity management tools are a gap the risk manager resolves with
the product team before the opinion.

**A readiness summary.**

| Fact | Value |
|---|---|
| Fund | Fund S (proposed) |
| Dealing terms | Daily |
| Benchmark tests passed | 6 of 6 |
| Redemption coverage under the worst scenario, at the expected size | 1.3x |
| Coverage limit | 1.5x |
| Expected instruments without a price source or proxy | 2 of 140 |
| Alpha and beta construction | Declared |

> Fund S passes all 6 benchmark tests, and its alpha and beta construction is declared. At its expected size, redemption
> coverage under the worst scenario is 1.3x, below the 1.5x limit for a fund dealing daily. 2 of the 140 instruments
> it expects to hold have neither a price source nor a proxy.

## Controls and measures specific to the review
The general [controls](../framework/08-controls.md) apply in full. The review adds three.

- **Missing terms show.** Extracted terms are checked against those expected for the portfolio's type, and each missing
  term is a gap resolved before the opinion.
- **Conditions are tracked.** Each condition has a due date and is tracked until it is met or escalated.
- **Launch is checked.** On launch day the analytics engine confirms that the terms, limits, data and construction
  agreed in the review are in place, and a gap is an exception.

The measures for the review, on the [four dimensions](../framework/07-redesign-method.md#four-dimensions) a redesigned
workflow is measured on:

| Dimension | Measure for the review |
|---|---|
| Speed | Working days from draft documents to a recorded opinion |
| Capacity | Reviews completed at full depth, including material changes |
| Quality | Issues found after launch that the review should have caught; agreed items missing on launch day |
| Influence | Conditions adopted; designs changed as a result of the review |
| Review specific | Share of launches with every agreed item in place on launch day |

## Sources
- International Organization of Securities Commissions (2025). *Revised Recommendations for Liquidity Risk Management
  for Collective Investment Schemes.* Liquidity considered at the design stage, matching assets to the dealing terms
  before launch.
- Bailey, J. (1992). Evaluating Benchmark Quality. *Financial Analysts Journal*. The properties a benchmark should have
  before it is used.
