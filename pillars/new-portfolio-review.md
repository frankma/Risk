# New portfolio review

The new portfolio review makes sure that everything the pillars rely on is in place before a portfolio takes its first
client money, and again whenever a portfolio changes enough to be a new portfolio in all but name. It draws on every
pillar: the mandate terms that performance risk tests against, the limits that market and liquidity risk watch, the
liquidity the dealing terms promise, the data the risk engine reads and the construction the alpha and beta split runs
on. It computes nothing of its own beyond what those chapters define.

## The outcome
> Before a portfolio launches or changes materially, the risk function knows that its mandate can be monitored as
> promised, and has put its view on record.

A portfolio that launches without confirmed mandate terms, internal limits, data for the instruments it will hold or a
liquidity profile that fits its dealing terms is monitored badly from its first day, and the gaps are found later, at
greater cost. The review moves that work to before launch, when it is cheapest to fix.

## What the review covers
- **New open-ended and closed-ended funds.**
- **New segregated mandates.**
- **Material changes to an existing portfolio:** a change of strategy or benchmark, a merger, or a change in dealing
  terms. A change of strategy is a relaunch in everything but name, and is reviewed as one.

A change to a portfolio's governing documents triggers the re-extraction of its mandate terms, as set out in
[performance risk](performance-risk.md#controls-specific-to-this-pillar); where the change is material, it also triggers
this review.

## What must be in place before launch
| Item | What is tested | Defined in |
|---|---|---|
| Mandate terms | The objective, benchmark, guidelines and dealing terms, extracted and confirmed | [Performance risk](performance-risk.md#flagship-redesign-the-periodic-portfolio-manager-review) |
| Benchmark | It passes the benchmark tests: specified in advance, investable, unambiguous, measurable, appropriate to the style and owned | [Performance risk](performance-risk.md#benchmarks-and-peer-groups) |
| Limits | Internal limits and early warnings set by the risk function; compliance's mandate and regulatory limits recorded | [Limits and escalation](../framework/04-limits-and-escalation.md) |
| Liquidity profile | Redemption coverage under the scenarios for calls on cash, at the launch size and the expected size, against the dealing terms | [Liquidity risk](liquidity-risk.md#calls-on-cash) |
| Data | Every instrument the portfolio expects to hold can be priced and classified, or has a proxy under the policy | [Risk data](../framework/03-risk-data.md#proxies) |
| Alpha and beta construction | The buckets, the index inside each and the factor list, declared before the first period | [Alpha and beta method](alpha-and-beta-method.md#booked-or-derived) |
| Liquidity management tools | The tools the documents provide for, and whether each can be used | [Liquidity risk](liquidity-risk.md#workflows-in-this-pillar) |

The liquidity profile carries [belief 5](../framework/00-philosophy.md#beliefs): a portfolio that will offer daily
dealing on assets that take weeks to sell is making a promise it cannot keep, and the time to see that is before
launch.

## The risk function's opinion
Product governance decides whether a portfolio launches. The risk function gives a **recorded opinion**: whether the
portfolio can be monitored as its mandate promises, any conditions that must be met, and its reasons. The risk
function can escalate to the risk committee where product governance proceeds against its opinion.

The opinion is not a veto, in keeping with the
[philosophy](../framework/00-philosophy.md#purpose-transparency-for-three-decisions): the risk function is independent
of the investment team but works inside its process. The internal limits set at this stage follow the same spirit: they
exist first to keep everyone on top of the portfolio's risks, as set out in [limits and
escalation](../framework/04-limits-and-escalation.md#what-internal-limits-are-for), not to decide the launch.

## Flagship redesign: the review of one new portfolio
The example below follows the review of one new open-ended fund. **The steps, hours and elapsed times are
illustrative.**

**Current state.** The risk function receives the draft documents late in the product process and works through them by
hand.

| # | Step | Tag | Hours | Elapsed |
|---|---|---|---|---|
| 1 | Read the draft documents and note the terms | Interpret | 4 | 3 days |
| 2 | Ask the portfolio manager for the intended strategy and a model portfolio | Gather | 1 | 5 days |
| 3 | Build risk and liquidity estimates on the model portfolio in a workbook | Compute | 6 | 3 days |
| 4 | Check whether data can be sourced for the expected instruments | Gather | 3 | 5 days |
| 5 | Agree limits with the portfolio manager by email | Communicate | 3 | 5 days |
| 6 | Write the risk opinion for product governance | Communicate | 4 | 3 days |
| 7 | Head of risk signs off the opinion | Approve / Wait | 1 | 3 days |

The review takes about 22 hours and 27 working days. It often starts too late to change the design, the liquidity test
uses a workbook nobody reruns, and nothing checks on launch day that what was agreed has been set up.

**Owner assignment.**

- Step 1 becomes an AI extraction of the draft mandate terms, each linked to its passage, confirmed by the risk
  manager.
- Steps 3 and 4 move to the risk engine, which runs the pillars' measures on the model portfolio, tests the benchmark,
  checks data readiness for every expected instrument and proposes internal limits and the alpha and beta construction.
- Step 2 stays, earlier: the model portfolio is requested when the review starts.
- Step 5 becomes a conversation about the proposed limits and construction, settled by the risk manager with the
  portfolio manager.
- Step 6 is split. The AI drafts the readiness summary from the facts; the risk manager writes the opinion and any
  conditions.
- Step 7 stays with the head of risk.
- A launch-day check is added: the risk engine confirms that every item agreed is in place.

**Redesigned flow.**

| # | Step | Owner | Hours | Elapsed |
|---|---|---|---|---|
| 1 | Extract the draft mandate terms, each linked to its passage | AI assistant | 0 | Same day |
| 2 | Confirm the terms; request the model portfolio | Risk manager | 2 | 1 day |
| 3 | Run the pillars' measures on the model portfolio; test the benchmark and the liquidity profile | Risk engine | 0 | Same day |
| 4 | Check data readiness; propose internal limits, early warnings and the alpha and beta construction | Risk engine | 0 | Same day |
| 5 | Settle limits and construction with the portfolio manager | Risk manager | 3 | 3 days |
| 6 | Draft the readiness summary; grounding check | AI assistant, risk engine | 0 | Minutes |
| 7 | Write the opinion and any conditions | Risk manager | 2 | 1 day |
| 8 | Sign off the opinion; product governance decides | Head of risk | 1 | 2 days |
| 9 | On launch day, confirm every agreed item is in place | Risk engine | 0 | Launch day |

The review falls to about 8 hours and 7 working days, and it can start as soon as draft documents exist.

**The shift.** The review moves from a late, manual assessment to a readiness check that runs the same measures the
portfolio will be monitored with, and that confirms on launch day that what was agreed is in place.

## What the AI drafts
The AI extracts and drafts from the documents and facts it is given, and from nothing else. Every figure it extracts
must appear in the passage it links to, and every number in a draft appears in the facts beside it, so the
[grounding check](../framework/07-controls.md#the-grounding-check) would pass. The AI does not write the opinion or its
conditions. **The funds and figures are illustrative.**

**Extracted mandate terms.**

| Term | Extracted value | Source passage |
|---|---|---|
| Single-issuer limit | 10% of net assets | "not more than 10% of its net assets in securities of any single issuer" |
| Dealing | Daily | "shares may be redeemed on any business day" |
| Benchmark | A broad index of large companies | "measured against a broad index of large companies" |

Each extracted value is confirmed by the risk manager before it is used.

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

## Controls specific to the review
The general controls in [controls](../framework/07-controls.md) apply in full. The review adds four.

- **Terms are confirmed before anything is tested against them.**
- **The opinion is written by a person.** The AI drafts the summary of facts; the risk manager writes the opinion and
  its conditions.
- **Conditions are tracked.** Each condition has a due date and is tracked until it is met or escalated.
- **Launch is checked.** On launch day the risk engine confirms that the terms, limits, data and construction agreed in
  the review are in place, and a gap is an exception.

## Measuring value
| Dimension | Measure for the review |
|---|---|
| Speed | Working days from draft documents to a recorded opinion |
| Capacity | Reviews completed at full depth, including material changes |
| Quality | Issues found after launch that the review should have caught; agreed items missing on launch day |
| Influence | Conditions adopted; designs changed as a result of the review |
| Review specific | Share of launches with every agreed item in place on launch day |

In the flagship example, the review falls from about 22 hours and 27 working days to about 8 hours and 7 working days.
(The figures are illustrative.)

## Connections
The review sets up what the other chapters use. The mandate terms it confirms are the ones
[performance risk](performance-risk.md) tests against; the limits it sets are watched by [market
risk](market-risk.md) and [liquidity risk](liquidity-risk.md) under [limits and
escalation](../framework/04-limits-and-escalation.md); the data readiness it checks follows [risk
data](../framework/03-risk-data.md); and the construction it declares is the one the
[alpha and beta method](alpha-and-beta-method.md) runs on from the first period. A new instrument that an existing
portfolio wants to hold is reviewed in [market risk](market-risk.md#workflows-in-this-pillar), not here.

## Sources
- International Organization of Securities Commissions (2018). *Recommendations for Liquidity Risk Management for
  Collective Investment Schemes.* Liquidity considered at the design stage, matching assets to the dealing terms
  before launch.
- Bailey, J. (1992). Evaluating Benchmark Quality. *Financial Analysts Journal*. The properties a benchmark should
  have before it is used.
