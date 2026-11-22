# Investment risk framework

**How a risk function at an asset manager should work, with each workflow redesigned around AI.**

The [reader](https://frankma.github.io/Risk/) holds every chapter on one page and links to the
[film](https://frankma.github.io/Risk/film/): the framework in six animated scenes.

## Investment risk, in three pillars
A risk function challenges investment decisions against the mandate, and serves the investment team with insight into
the risks it takes ([philosophy](framework/00-philosophy.md#why-a-risk-function-exists)). It is defined by the decisions
it alone may make: the work is shared across the firm, the decisions are not ([decision
rights](framework/10-decision-rights.md)). Its recurring work answers three questions:

| Pillar | Question |
|---|---|
| **Market risk** | Does a portfolio carry the risk its mandate intends, no more and no less, and how much could it lose? |
| **Liquidity risk** | Can a portfolio meet every call on its cash, in time and at a fair cost, without disadvantaging the investors who stay? |
| **Performance risk** | Is a portfolio delivering what was promised, in the way it was promised? |

The pillars connect, and the [integrated view](pillars/integrated-view.md) reads them together.

## How return is earned
Fundamentally, a portfolio's return is driven by two decisions: top-down views on which markets to hold, how much and
for how long, and bottom-up selection of the securities within them. Loosely, top-down views earn beta: any return above
the risk-free rate that an index fund or a future could have delivered, paid by market and style premia. Bottom-up
selection earns alpha: the return left once beta is carved out, paid by skill. Performance risk dissects each
portfolio's return along this line; see [how return is earned](framework/01-sources-of-return.md).

## The core pattern
**The analytics engine computes, the AI interprets and narrates, a person judges.**

Each workflow is redesigned around this pattern, not handed an AI tool. The analytics engine is the deterministic part
of the system, where the same data always gives the same figure and every figure can be traced and reproduced.

| Work | Owner |
|---|---|
| Gathering data, calculating, comparing to limits | Analytics engine |
| Investigating each exception through the analytics engine, drafting, challenging conclusions, extracting from documents, notices and minutes | AI |
| Prioritising, checking the work, challenging it, judging what matters to the portfolio and its intended risk profile, and deciding | The risk manager and head of risk |

Two rules make it work:

- **The AI never fabricates a number.** Every figure it reports was computed by the analytics engine, in the daily run
  or in an analysis the AI ran through it, such as an aggregation, an attribution or a what-if. The run is recorded and
  can be reproduced, and text with a figure that has no computation behind it is rejected.
- **Exceptions over everything.** The analytics engine checks every portfolio against every rule each day and triages
  what it finds into a queue of exceptions and watch items. The risk manager prioritises and reviews that queue rather
  than every portfolio, and signs off what goes out, or reviews the same day what a governed rule lets the AI send or
  close. [Principles](framework/05-principles.md#4-exceptions-over-everything) sets this out.

## Map
Every chapter except the concept map opens with **The essentials**, which states the chapter whole, and the detail
follows beneath it. Reading the essentials in order gives the framework; the detail is there when a point needs it.

| Chapter | Covers |
|---|---|
| **Foundations** | |
| [Philosophy](framework/00-philosophy.md) | What a risk function believes and is for. |
| [How return is earned](framework/01-sources-of-return.md) | Top-down views and bottom-up selection, beta and alpha, and how the split is read. |
| [What investment risk means](framework/02-investment-risk.md) | The definition, the scope and the three pillars. |
| **The pillars** | |
| [Market risk](pillars/market-risk.md) | Whether a portfolio carries the risk its mandate intends: daily monitoring as a triaged queue with drafted explanations. |
| [Liquidity risk](pillars/liquidity-risk.md) | Whether a portfolio can meet its calls on cash fairly: continuous monitoring with event-triggered stress tests. |
| [Performance risk](pillars/performance-risk.md) | Whether the promise is kept: portfolio manager reviews on the risk function's agenda. |
| [Integrated view](pillars/integrated-view.md) | Where signals combine across the pillars, the firm's footprint, and what the firm is paid for. |
| **Practice** | |
| [Risk data](framework/03-risk-data.md) | The data every figure rests on: checked, versioned, proxied and corrected at source. |
| [Limits and escalation](framework/04-limits-and-escalation.md) | Hard limits, internal limits and early warnings; the breach lifecycle and the escalation path. |
| [New portfolio review](pillars/new-portfolio-review.md) | What must be in place before a portfolio launches or changes materially. |
| [Alpha and beta method](pillars/alpha-and-beta-method.md) | How the split is computed, on three portfolios. |
| **The redesign around AI** | |
| [Principles](framework/05-principles.md) | Seven principles for redesigning the work around AI, and what the risk manager adds. |
| [Working with AI](framework/06-working-with-ai.md) | What "AI" means, three modes of working, what the AI reads, where a figure may come from and what the AI may do. |
| [Redesign method](framework/07-redesign-method.md) | Seven steps to redesign one workflow. |
| [Controls](framework/08-controls.md) | What makes a redesigned workflow safe to rely on, from the grounding check and automated actions to evaluation, incidents and fallback. |
| [Measuring value](framework/09-measuring-value.md) | How to know a redesigned workflow works. |
| [Decision rights](framework/10-decision-rights.md) | Who decides what once the work is shared: independence in the rules, self-service, one holder for each decision, the roles and the size of the function. |
| **Index** | |
| [Concept map](framework/concept-map.md) | Every concept: what it is, where it is defined and which chapters use it. |

Each chapter ends with the public sources it draws on.

## Disclaimer
This framework is general and illustrative. It is not advice for any particular firm, and any implementation should be
assessed against the firm's own policies and applicable regulation.
