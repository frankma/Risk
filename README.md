# Risk

**Asset management from an investment risk perspective, and how to redesign that work around AI.**

An asset manager takes a client's money under a mandate, invests it through top-down views and bottom-up selection, and
delivers an outcome. Investment risk is what can go wrong between that promise and that outcome, and a risk function
shows whether each portfolio takes the risks its mandate intends. This framework covers that investment side of asset
management; distribution, operations, compliance and the firm's own business sit outside it.

Many fund managers now use AI tools, but few can show a measurable return from them. The return does not come from
inserting AI into existing workflows. A tool that drafts a report faster changes little when the real bottleneck is
gathering data, handing work between people and waiting in review queues. It comes from redesigning the workflow around
what AI makes possible.

This framework sets out how to do that for investment risk.

## The core pattern
**Code computes, AI narrates, a human judges.**

| Work | Owner | Why |
|---|---|---|
| Gathering data, calculating, comparing to limits | Code | Deterministic; must be exact and reproducible. |
| Explaining what changed, drafting, extracting from documents | AI | Language and pattern work, in seconds. |
| Deciding what matters, escalating, signing off | The risk manager and head of risk | Judgement and accountability. |

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
| **The investment backdrop** | |
| [Investment risk philosophy](framework/00-philosophy.md) | What a risk function believes and is for: eight beliefs, the three decisions it serves, and transparency in three dimensions. |
| [Investment risk](framework/01-investment-risk.md) | Definition and scope, including what is measured here and what is owned elsewhere; the three pillars and the boundaries between them. |
| [Sources of return](framework/02-sources-of-return.md) | The two sources of every return, top-down views and bottom-up selection, loosely beta and alpha; who decides each, why it matters to asset owners, fund houses and risk functions, and how a holding splits between them. |
| **The redesign around AI** | |
| [Principles](framework/03-principles.md) | Why inserting AI fails; six principles for redesign; how the risk manager's role changes. |
| [Redesign method](framework/04-redesign-method.md) | Seven steps to redesign one workflow, from outcome to measured result. |
| [Controls](framework/05-controls.md) | Grounding checks, sign-off points, audit trails, governed thresholds, parallel runs, fallback, data handling, alignment with AI risk management expectations. |
| [Measuring value](framework/06-measuring-value.md) | Capacity, speed, quality and influence; a baseline and a reinvestment plan; why usage is not a measure. |
| **The pillars** | |
| [Market risk](pillars/market-risk.md) | The pillar's workflows; daily monitoring redesigned as a ranked queue of exceptions and watch items with drafted explanations. |
| [Liquidity risk](pillars/liquidity-risk.md) | The pillar's workflows; periodic stress tests redesigned as continuous monitoring with event-triggered stress tests. |
| [Performance risk](pillars/performance-risk.md) | The pillar's workflows; portfolio manager reviews run on risk's agenda with an evidence-based challenge pack. |
| [Integrated view](pillars/integrated-view.md) | One fund health view that ranks funds where signals across pillars combine, before any one pillar would escalate them, and shows the firm's footprint across funds. |
| [Alpha and beta method](pillars/alpha-and-beta-method.md) | How the split is computed for publicly traded holdings on gross returns: neutralising the book, booked and derived routes, the factor list, the test and its limits. |
| **Index** | |
| [Concept map](framework/concept-map.md) | The main concepts on one page: what each is, where it is defined and which chapters use it. |

## Using this repository
The framework chapters are written to be read in order. The pillar chapters can be read on their own once the
principles and the method are familiar. The concept map is a reference, for finding where a concept is defined and used.

## Disclaimer
This framework is general and illustrative. It is not advice for any particular firm, and any implementation should be
assessed against the firm's own policies and applicable regulation.
