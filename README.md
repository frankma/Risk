# Investment risk framework

**Asset management from an investment risk perspective, and how to redesign that work around AI.**

An asset manager invests clients' money under a mandate and delivers an outcome. This framework looks at that work from
an investment risk perspective, and sets out how a risk function's part of it is redesigned around AI. The
[investment risk](framework/01-investment-risk.md#the-backdrop) chapter sets out the backdrop.

## Investment risk, in three pillars
Investment risk is the chance that a portfolio's outcome departs from what its mandate intends. A risk function's
recurring work answers three questions:

| Pillar | Question |
|---|---|
| **Market risk** | How much could we lose, in total and against the benchmark? |
| **Liquidity risk** | Can the portfolio meet every call on its cash, in time and at a fair cost, without disadvantaging the investors who stay? |
| **Performance risk** | Is the portfolio delivering what was promised, in the way it was promised? |

The pillars are connected. Underperformance drives redemptions, redemptions force sales of the most liquid assets, and
what remains is more concentrated and more volatile. Seeing the pillars together is a capability no manual process
provides.

## Two sources of return
Every return comes from two sources. Top-down views decide how much of which markets to hold, and bottom-up selection
decides which securities to hold within them. Loosely, the first is called beta and the second alpha. A risk function
uses the split to ask whether each risk was chosen and whether it was paid for; see
[sources of return](framework/02-sources-of-return.md).

## Redesigning the work around AI
Many asset managers now use AI tools, but few can show a measurable return from them. The return does not come from
inserting AI into existing workflows. A tool that drafts a report faster changes little when the real bottleneck is
gathering data, handing work between people and waiting in review queues. It comes from redesigning the workflow around
what AI makes possible.

This framework sets out how to do that for investment risk.

## The core pattern
**The risk engine computes, AI narrates, a human judges.**

The risk engine is the deterministic part of the system, where the same data always gives the same figure and every
figure can be traced and reproduced.

| Work | Owner | Why |
|---|---|---|
| Gathering data, calculating, comparing to limits | Risk engine | Deterministic; must be exact and reproducible. |
| Explaining what changed, drafting, extracting from documents | AI assistant | Language and pattern work, in seconds. |
| Judging what matters to the portfolio and its intended risk profile; bringing clarity to the risks being taken | The risk manager and head of risk | Judgement and accountability. |

Two rules make it work:

- **The AI never originates a number.** Every figure comes from the risk engine, computed from data. The AI writes text
  around the figures it is given and may combine them only in ways the grounding check can recompute; text with a
  number it cannot trace is rejected.
- **The system checks everything; a human judges what ranks.** The risk engine checks every portfolio against every
  rule each day and ranks what it finds into a queue of exceptions and watch items. The risk manager reviews that queue
  rather than every portfolio, signs off what goes out, and spends the time freed on what a person adds: judging what
  matters to the portfolio and its intended risk profile, and bringing clarity to the risks being taken.
  [Principles](framework/05-principles.md#what-the-risk-manager-adds) sets this out.

## Map
| Chapter | Covers |
|---|---|
| **The investment backdrop** | |
| [Investment risk philosophy](framework/00-philosophy.md) | What a risk function believes and is for: eight beliefs, the three decisions it serves, and transparency in three dimensions. |
| [Investment risk](framework/01-investment-risk.md) | Definition and scope, including the portfolios covered, what is measured here and what is owned elsewhere; the three pillars, with market and performance risk divided by time into forward-looking and realised. |
| [Sources of return](framework/02-sources-of-return.md) | The two sources of every return, top-down views and bottom-up selection, loosely beta and alpha; who decides each, why it matters to asset owners, asset managers and risk functions, and how a holding splits between them. |
| **The practice** | |
| [Risk data](framework/03-risk-data.md) | The data the risk engine reads, from golden source to computed figure; versioning as known, so any past output can be reproduced; quality checks before computation; the proxy policy; who owns fitness for use and who corrects; the daily data check redesigned as a ranked queue of data breaks. |
| [Limits and escalation](framework/04-limits-and-escalation.md) | Where limits come from: mandate and regulatory limits owned by compliance, internal limits owned by the risk function, and early warnings below both; what internal limits are for; how they are calibrated; the breach lifecycle and who approves what; breach handling redesigned as a tracked record. |
| **The redesign around AI** | |
| [Principles](framework/05-principles.md) | Why inserting AI fails; six principles for redesign; what the risk manager adds. |
| [Redesign method](framework/06-redesign-method.md) | Seven steps to redesign one workflow, from outcome to measured result. |
| [Controls](framework/07-controls.md) | Grounding checks, sign-off points, audit trails, governed thresholds, parallel runs, fallback, data handling, alignment with AI risk management expectations. |
| [Measuring value](framework/08-measuring-value.md) | Capacity, speed, quality and influence; a baseline and a reinvestment plan; why usage is not a measure. |
| **The pillars** | |
| [Market risk](pillars/market-risk.md) | The pillar's workflows, including ex-ante tracking error and the risk budget review; design choices for VaR and expected shortfall, factors, backtesting, stress, credit, leverage and counterparty exposure; daily monitoring redesigned as a ranked queue of exceptions and watch items with drafted explanations. |
| [Liquidity risk](pillars/liquidity-risk.md) | The pillar's workflows; design choices for fairness and capacity, time and cost to sell, scenarios for calls on cash, encumbrance and second-round effects; periodic stress tests redesigned as continuous monitoring with event-triggered stress tests. |
| [Performance risk](pillars/performance-risk.md) | The pillar's workflows; design choices for risk-adjusted measures, windows and significance, benchmarks and peer groups, and linking attribution over time; portfolio manager reviews run on risk's agenda with an evidence-based challenge pack. |
| [Integrated view](pillars/integrated-view.md) | One portfolio health view that ranks portfolios where signals across pillars combine, before any one pillar would escalate them, and shows the firm's footprint across portfolios. |
| [New portfolio review](pillars/new-portfolio-review.md) | What must be in place before a portfolio launches or changes materially: confirmed mandate terms, a tested benchmark, limits, a liquidity profile that fits the dealing terms, data readiness, the alpha and beta construction and liquidity tools; the risk function's recorded opinion; the review redesigned with a launch-day check. |
| [Alpha and beta method](pillars/alpha-and-beta-method.md) | How the split is computed for publicly traded holdings on gross returns: neutralising the book, booked and derived routes, the factor list, the test and its limits. |
| **Index** | |
| [Concept map](framework/concept-map.md) | The main concepts on one page: what each is, where it is defined and which chapters use it. |

## Using this repository
The framework chapters are written to be read in order. The pillar chapters can be read on their own once the principles
and the method are familiar. The concept map is a reference, for finding where a concept is defined and used. Each
chapter ends with the public sources it draws on.

## Disclaimer
This framework is general and illustrative. It is not advice for any particular firm, and any implementation should be
assessed against the firm's own policies and applicable regulation.
