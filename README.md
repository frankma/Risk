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
Every return above cash is paid by one of three return generators: market risk premia, style premia and skill. They
group into two sources. Top-down views decide how much of which markets and styles to hold, and bottom-up selection
decides which securities to hold within them. Loosely, the first is called beta and the second alpha. A risk function
uses the generators to ask how a return could stop, and the split to ask whether each risk was chosen and whether it
was paid for; see
[sources of return](framework/02-sources-of-return.md).

## Redesigning the work around AI
AI changes investment risk work when a workflow is redesigned around it, not when it is inserted into the workflow as
it stands. A tool that drafts a report faster changes little when the report still waits for data to be gathered, for
work to pass between people and for review queues.

This framework sets out how to do that for investment risk, and how people and the AI then work together. It is
written for the whole firm: the risk managers who do the work, the portfolio managers who receive it and the management
that decides where AI enters the business.

## The core pattern
**The risk engine computes, AI analyses and narrates, a human judges.**

The risk engine is the deterministic part of the system, where the same data always gives the same figure and every
figure can be traced and reproduced.

| Work | Owner | Why |
|---|---|---|
| Gathering data, calculating, comparing to limits | Risk engine | Deterministic; must be exact and reproducible. |
| Investigating through the risk engine, explaining what changed, drafting, extracting from documents | AI assistant | Language and pattern work, in seconds, on figures the risk engine computes. |
| Judging what matters to the portfolio and its intended risk profile; bringing clarity to the risks being taken | The risk manager and head of risk | Judgement and accountability. |

Two rules make it work:

- **The AI never fabricates a number.** Every figure it reports was computed by the risk engine, in the daily run or in
  an analysis the AI ran through it, such as an aggregation, an attribution or a what-if. The run is recorded and can
  be reproduced, and text with a figure that has no computation behind it is rejected.
- **The system checks everything; a human judges what ranks.** The risk engine checks every portfolio against every
  rule each day and ranks what it finds into a queue of exceptions and watch items. The risk manager reviews that queue
  rather than every portfolio, signs off what goes out, and spends that time on what a person adds: judging what
  matters to the portfolio and its intended risk profile, and bringing clarity to the risks being taken.
  [Principles](framework/05-principles.md#what-the-risk-manager-adds) sets this out.

## Map
Every chapter opens with an **In short** block that states the chapter whole, and the detail follows beneath it. Reading
the In short blocks in order gives the framework; the detail is there when a point needs it.

| Chapter | Covers |
|---|---|
| **The investment backdrop** | |
| [Investment risk philosophy](framework/00-philosophy.md) | What a risk function believes and is for. |
| [Investment risk](framework/01-investment-risk.md) | The definition, the scope and the three pillars. |
| [Sources of return](framework/02-sources-of-return.md) | The three return generators, and the split into beta and alpha. |
| **The practice** | |
| [Risk data](framework/03-risk-data.md) | The data every figure rests on: checked, versioned, proxied and corrected at source. |
| [Limits and escalation](framework/04-limits-and-escalation.md) | Hard limits, internal limits and early warnings; the breach lifecycle and the escalation path. |
| **The redesign around AI** | |
| [Principles](framework/05-principles.md) | Six principles for redesigning the work around AI, and what the risk manager adds. |
| [Working with AI](framework/06-working-with-ai.md) | Three modes of working, where a figure may come from and what the AI may do. |
| [Redesign method](framework/07-redesign-method.md) | Seven steps to redesign one workflow. |
| [Controls](framework/08-controls.md) | What makes a redesigned workflow safe to rely on, from the grounding check to fallback. |
| [Measuring value](framework/09-measuring-value.md) | How to know a redesigned workflow works. |
| **The pillars** | |
| [Market risk](pillars/market-risk.md) | How much a portfolio could lose: daily monitoring as a ranked queue with drafted explanations. |
| [Liquidity risk](pillars/liquidity-risk.md) | Whether a portfolio can meet its calls on cash fairly: continuous monitoring with event-triggered stress tests. |
| [Performance risk](pillars/performance-risk.md) | Whether the promise is kept: portfolio manager reviews on the risk function's agenda. |
| [Integrated view](pillars/integrated-view.md) | Where signals combine across the pillars, and the firm's footprint. |
| [New portfolio review](pillars/new-portfolio-review.md) | What must be in place before a portfolio launches or changes materially. |
| [Alpha and beta method](pillars/alpha-and-beta-method.md) | How the split is computed, on three portfolios. |
| **Index** | |
| [Concept map](framework/concept-map.md) | Every concept: what it is, where it is defined and which chapters use it. |

Each chapter ends with the public sources it draws on.

## Disclaimer
This framework is general and illustrative. It is not advice for any particular firm, and any implementation should be
assessed against the firm's own policies and applicable regulation.
