# Investment risk framework

**How a risk function at an asset manager should work, with each workflow redesigned around AI.**

## Investment risk, in three pillars
A risk function is a check and balance on every portfolio's risk, and a service to the investment process under
uncertainty ([philosophy](framework/00-philosophy.md#why-a-risk-function-exists)). Its recurring work answers three
questions:

| Pillar | Question |
|---|---|
| **Market risk** | How much could we lose, in total and against the benchmark? |
| **Liquidity risk** | Can the portfolio meet every call on its cash, in time and at a fair cost, without disadvantaging the investors who stay? |
| **Performance risk** | Is the portfolio delivering what was promised, in the way it was promised? |

The pillars connect, and the [integrated view](pillars/integrated-view.md) reads them together.

## Sources of return
Every return above cash is paid by one of three return generators: market risk premia, style premia or skill. The first
two are beta, held through top-down views; skill is alpha, earned by bottom-up selection. A risk function uses the
generators to ask how a return could stop, and the split to ask whether each risk was chosen and paid for; see [sources
of return](framework/02-sources-of-return.md).

## The core pattern
**The risk engine computes, AI analyses and narrates, a human judges.**

Each workflow is redesigned around this pattern, not handed an AI tool. The risk engine is the deterministic part of
the system, where the same data always gives the same figure and every figure can be traced and reproduced.

| Work | Owner |
|---|---|
| Gathering data, calculating, comparing to limits | Risk engine |
| Drafting, investigating through the risk engine, challenging conclusions, extracting from documents | AI assistant |
| Judging what matters to the portfolio and its intended risk profile; bringing clarity to the risks being taken | The risk manager and head of risk |

Two rules make it work:

- **The AI never fabricates a number.** Every figure it reports was computed by the risk engine, in the daily run or in
  an analysis the AI ran through it, such as an aggregation, an attribution or a what-if. The run is recorded and can
  be reproduced, and text with a figure that has no computation behind it is rejected.
- **Exceptions over everything.** The risk engine checks every portfolio against every rule each day and ranks what it
  finds into a queue of exceptions and watch items. The risk manager reviews that queue rather than every portfolio,
  and signs off what goes out. [Principles](framework/05-principles.md#4-exceptions-over-everything) sets this out.

## Map
Every chapter opens with an **In short** block that states the chapter whole, and the detail follows beneath it. Reading
the In short blocks in order gives the framework; the detail is there when a point needs it.

| Chapter | Covers |
|---|---|
| **Foundations** | |
| [Investment risk philosophy](framework/00-philosophy.md) | What a risk function believes and is for. |
| [Investment risk](framework/01-investment-risk.md) | The definition, the scope and the three pillars. |
| [Sources of return](framework/02-sources-of-return.md) | The three return generators, and the split into beta and alpha. |
| **The pillars** | |
| [Market risk](pillars/market-risk.md) | How much a portfolio could lose: daily monitoring as a ranked queue with drafted explanations. |
| [Liquidity risk](pillars/liquidity-risk.md) | Whether a portfolio can meet its calls on cash fairly: continuous monitoring with event-triggered stress tests. |
| [Performance risk](pillars/performance-risk.md) | Whether the promise is kept: portfolio manager reviews on the risk function's agenda. |
| [Integrated view](pillars/integrated-view.md) | Where signals combine across the pillars, and the firm's footprint. |
| **Practice** | |
| [Risk data](framework/03-risk-data.md) | The data every figure rests on: checked, versioned, proxied and corrected at source. |
| [Limits and escalation](framework/04-limits-and-escalation.md) | Hard limits, internal limits and early warnings; the breach lifecycle and the escalation path. |
| [New portfolio review](pillars/new-portfolio-review.md) | What must be in place before a portfolio launches or changes materially. |
| [Alpha and beta method](pillars/alpha-and-beta-method.md) | How the split is computed, on three portfolios. |
| **The redesign around AI** | |
| [Principles](framework/05-principles.md) | Six principles for redesigning the work around AI, and what the risk manager adds. |
| [Working with AI](framework/06-working-with-ai.md) | Three modes of working, where a figure may come from and what the AI may do. |
| [Redesign method](framework/07-redesign-method.md) | Seven steps to redesign one workflow. |
| [Controls](framework/08-controls.md) | What makes a redesigned workflow safe to rely on, from the grounding check to fallback. |
| [Measuring value](framework/09-measuring-value.md) | How to know a redesigned workflow works. |
| **Index** | |
| [Concept map](framework/concept-map.md) | Every concept: what it is, where it is defined and which chapters use it. |

Each chapter ends with the public sources it draws on.

## Disclaimer
This framework is general and illustrative. It is not advice for any particular firm, and any implementation should be
assessed against the firm's own policies and applicable regulation.
