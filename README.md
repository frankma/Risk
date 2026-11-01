# Risk

**A framework for redesigning investment risk management around AI.**

Most fund managers now use AI tools, yet few can point to a measurable return. The return does not come from inserting
AI into existing workflows. A tool that drafts a report faster changes little when the real bottleneck is gathering
data, handing work between people and waiting in review queues. It comes from redesigning the workflow around what AI
makes possible.

This framework sets out how to do that for investment risk.

## The core pattern
**Code computes, AI narrates, a human judges.**

| Work | Owner | Why |
|---|---|---|
| Gathering data, calculating, comparing to limits | Code | Deterministic; must be exact and reproducible. |
| Explaining what changed, drafting, extracting from documents | AI | Language and pattern work, in seconds. |
| Deciding what matters, escalating, signing off | The risk manager | Judgement and accountability. |

Two rules make it safe: **the AI never produces a number**, and **the human reviews ranked exceptions, not everything.**

## Investment risk, in three pillars
Investment risk is the chance that a portfolio's outcome departs from what its mandate intends. A risk function's
recurring work answers three questions:

| Pillar | Question |
|---|---|
| **Market risk** | How much could we lose? |
| **Liquidity risk** | Can we meet redemptions without disadvantaging the investors who stay? |
| **Performance risk** | Is the fund delivering what was promised, in the way it was promised? |

The pillars are connected. Underperformance drives redemptions, redemptions force sales of the most liquid assets, and
what remains is more concentrated and more volatile. Seeing the pillars together is a capability no manual process
provides.

## Map
| Chapter | Covers |
|---|---|
| **Framework** | |
| [Principles](framework/01-principles.md) | Redesign rather than insert; the core pattern; exceptions over everything; reinvesting freed time. |
| [Investment risk](framework/02-investment-risk.md) | Definition and scope, the three pillars and the boundaries between them. |
| [Redesign method](framework/03-redesign-method.md) | Seven steps to redesign one workflow, from outcome to measured result. |
| [Controls](framework/04-controls.md) | Grounding checks, sign-off points, audit trails, parallel runs, alignment with AI risk management expectations. |
| [Measuring value](framework/05-measuring-value.md) | Capacity, speed, quality and influence, and why usage is not a measure. |
| **Pillars** | |
| [Market risk](pillars/market-risk.md) | Daily monitoring redesigned as a ranked exception queue with explanations of what changed. |
| [Liquidity risk](pillars/liquidity-risk.md) | From periodic stress tests to continuous monitoring with event-triggered stress tests. |
| [Performance risk](pillars/performance-risk.md) | Portfolio manager reviews run on risk's agenda, with an evidence-based challenge pack. |
| [Integrated view](pillars/integrated-view.md) | One fund health view that ranks funds where signals across pillars combine. |
| **Reference** | |
| [Reference implementations](reference/) | Runnable examples on synthetic data. |

## Using this repository
The framework chapters are written to be read in order. The pillar chapters can be read on their own once the
principles and the method are familiar.

The reference implementations use synthetic data only and run without an AI service; an optional AI backend can be
configured.

## Disclaimer
This framework is general and illustrative. It is not advice for any particular firm, and any implementation should be
assessed against the firm's own policies and applicable regulation.
