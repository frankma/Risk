# New portfolio review

## In short
**The question:** is everything the pillars rely on in place before a portfolio takes its first client money, or changes
enough to be a new portfolio in all but name?

**The outcome:**

> Before a portfolio launches or changes materially, the risk function knows that its mandate can be monitored as
> promised, and has put its view on record.

**How the work is done:** the review computes nothing of its own. The AI extracts the draft mandate terms from the
documents. The risk engine runs the pillars' measures on a model portfolio, checks data readiness and proposes limits
and the alpha and beta construction. The risk manager confirms the terms, decides the limits and writes the opinion, and
on launch day the risk engine confirms that everything agreed is in place. The review can start as soon as draft
documents exist.

| # | Step | Owner |
|---|---|---|
| 1 | Extract the draft mandate terms, each linked to its passage | AI assistant |
| 2 | Confirm the terms; request the model portfolio | Risk manager |
| 3 | Run the pillars' measures on the model portfolio; test the benchmark and the liquidity profile | Risk engine |
| 4 | Check data readiness; propose internal limits, early warnings and the alpha and beta construction | Risk engine |
| 5 | Consult the portfolio manager; decide the limits and the construction | Risk manager |
| 6 | Draft the readiness summary | AI assistant |
| 7 | Grounding check on the summary | Risk engine |
| 8 | Write the opinion and any conditions | Risk manager |
| 9 | Sign off the opinion; product governance decides | Head of risk |
| 10 | On launch day, confirm every agreed item is in place | Risk engine |

**The opinion is not a veto:** product governance decides whether a portfolio launches. The risk function gives a
recorded opinion and can escalate to the risk committee.

**Why before launch:** a portfolio that launches without confirmed mandate terms, internal limits, data for its
instruments or a liquidity profile that fits its dealing terms is monitored badly from its first day. The gaps are
cheapest to fix before launch.

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

## What must be in place before launch
| Item | What is tested | Defined in |
|---|---|---|
| Mandate terms | The objective, benchmark, style, limits and dealing terms, extracted and confirmed | [Performance risk](performance-risk.md#mandate-terms) |
| Benchmark | It passes the benchmark tests: specified in advance, investable, unambiguous, measurable, appropriate to the style and owned | [Performance risk](performance-risk.md#benchmarks-and-peer-groups) |
| Limits | Internal limits and early warnings set by the risk function; the mandate and regulatory limits recorded, with each risk-measured limit set up for the risk function to monitor | [Limits and escalation](../framework/04-limits-and-escalation.md) |
| Liquidity profile | Redemption coverage under the scenarios for calls on cash, at the launch size and the expected size, against the dealing terms | [Liquidity risk](liquidity-risk.md#calls-on-cash) |
| Data | Every instrument the portfolio expects to hold, and every instrument in its top-down portfolio, can be priced and classified, or has a proxy under the policy | [Risk data](../framework/03-risk-data.md#proxies) |
| Alpha and beta construction | The benchmark portfolio, the buckets, the instrument inside each and the factor list, declared before the first period | [Alpha and beta method](alpha-and-beta-method.md#booked-or-derived) |
| Liquidity management tools | The tools the documents provide for, and whether each can be used | [Liquidity risk](liquidity-risk.md#workflows-in-this-pillar) |

The liquidity profile carries [belief 5](../framework/00-philosophy.md#beliefs): a portfolio that will offer daily
dealing on assets that take weeks to sell is making a promise it cannot keep, and the time to see that is before launch.

## The risk function's opinion
Product governance decides whether a portfolio launches. The risk function gives a **recorded opinion**: whether the
portfolio can be monitored as its mandate promises, any conditions that must be met, and its reasons. The risk function
can escalate to the risk committee where product governance proceeds against its opinion.

The opinion is not a veto, in keeping with the
[philosophy](../framework/00-philosophy.md#purpose-transparency-for-three-decisions): the risk function is independent
of the investment team but works inside its process. The internal limits set at this stage follow the same spirit: they
exist first to keep everyone on top of the portfolio's risks, as set out in [limits and
escalation](../framework/04-limits-and-escalation.md#what-internal-limits-are-for), not to decide the launch.

## What the AI drafts
The AI extracts and drafts from the documents and facts it is given, and from nothing else. Every figure it extracts
must appear in the passage it links to, and every number in a draft appears in the facts beside it, so the [grounding
check](../framework/08-controls.md#the-grounding-check) would pass. The AI does not write the opinion or its conditions.
**The funds and figures are illustrative.**

**Extracted mandate terms.**

| Term | Extracted value | Source passage |
|---|---|---|
| Single-issuer limit | 10% of net assets | "not more than 10% of its net assets in securities of any single issuer" |
| Dealing | Daily | "shares may be redeemed on any business day" |
| Benchmark | A broad index of large companies | "measured against a broad index of large companies" |

Each extracted value is confirmed by the risk manager before it is used, and the single-issuer limit, a hard limit, is
reconciled to compliance's coded rule.

**A readiness summary.**

| Fact | Value |
|---|---|
| Fund | Fund S (proposed) |
| Dealing terms | Daily |
| Benchmark tests passed | 6 of 6 |
| Redemption coverage under the worst scenario, at the expected size | 1.3x |
| Coverage threshold | 1.5x |
| Expected instruments without a price source or proxy | 2 of 140 |
| Alpha and beta construction | Declared |

> Fund S passes all 6 benchmark tests, and its alpha and beta construction is declared. At its expected size, redemption
> coverage under the worst scenario is 1.3x, below the 1.5x threshold for a fund dealing daily. 2 of the 140 instruments
> it expects to hold have neither a price source nor a proxy.

The opinion on whether Fund S should launch, and on what conditions, is the risk manager's.

## Controls and measures specific to the review
The general [controls](../framework/08-controls.md) apply in full. The review adds four.

- **Terms are confirmed before anything is tested against them.**
- **The opinion is written by a person.** The AI drafts the summary of facts; the risk manager writes the opinion and
  its conditions.
- **Conditions are tracked.** Each condition has a due date and is tracked until it is met or escalated.
- **Launch is checked.** On launch day the risk engine confirms that the terms, limits, data and construction agreed in
  the review are in place, and a gap is an exception.

The measures for the review, from [measuring value](../framework/09-measuring-value.md):

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
