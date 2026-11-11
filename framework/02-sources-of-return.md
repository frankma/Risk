# Sources of return

Every investment return comes from two sources. Top-down views decide how much of which markets to hold. Bottom-up
selection decides which securities to hold within them. Loosely, the first is called beta and the second alpha. This
chapter answers five questions about them. The [alpha and beta method](../pillars/alpha-and-beta-method.md) sets out
how the split is computed.

## What are the two sources?
Every part of a portfolio's return lands in exactly one place in this breakdown.

- **Portfolio return**
  - **Top-down views**, loosely beta
    - **Set in the mandate:** policy beta
    - **Chosen by the manager:** tilts and timing
    - **Chosen by nobody:** unintended beta
  - **Bottom-up selection**, loosely alpha: what selection adds once top-down is out

| | Top-down | Bottom-up |
|---|---|---|
| **The question** | How much of which markets? | Which securities within them? |
| **Examples** | Asset allocation, market timing, sector and style tilts | Stock and bond selection |
| **Who usually decides** | Asset owner, chief investment officer, allocation team | Portfolio manager, analysts |
| **Loose name** | Beta | Alpha |

Both take judgement, and both can be wrong. Beta does not mean passive: market timing is a top-down view, and a
well-timed allocation is a good beta call. Two things set the sources apart. An index or basket can replicate top-down
exposure, though not the timing of it, while nothing can replicate selection, because it chooses between securities
that share the same exposures. And top-down views are judged slowly, because there are few calls, while selection can be
judged faster, because there are many.

## Who chose each part?
Top-down return has three branches, according to whose call it was.

- **Set in the mandate.** Policy beta is the return of the benchmark or strategic allocation in the portfolio's
  governing documents. A client, an asset owner or a chief investment officer may have set it, or, for a pooled fund,
  the manager when the fund was launched, which investors accepted when they bought. Whoever chose it, it is part of
  the promise, and the manager earns no credit for it.
- **Chosen by the manager.** Tilts are standing positions against that allocation, and timing is the return from
  changing exposure over time. Both count only if recorded when taken. Timing earns nothing without skill, so it is
  assessed on its own.
- **Chosen by nobody.** Unintended beta is any exposure with no record that anyone chose it, including price drift. The
  portfolio manager holds it, but nobody decided it. "Unintended" is a test of record, not of motive: an exposure the
  manager meant to take but did not record counts here until it is recorded. Recording a tilt makes it accountable,
  not exempt: a recorded tilt is still read against the risk budget, which challenges one that uses budget and earns
  nothing, and a tilt outside the confirmed mandate terms still fails the style check.

Alpha belongs to the manager who selected the securities. The manager's branch and the unintended branch together are
active beta, and a portfolio's active return is active beta plus alpha. One beta is enough for general use; the branches
are there when it helps to say whose call it was.

## Why does it matter?

| Who | What the split answers |
|---|---|
| Asset owner | Which top-down views do I set myself, and what am I paying others for? |
| Asset manager | Where are we actually good, and how do we divide risk between the two sources? |
| Risk function | Was each risk chosen? Was it paid for? Is the client paying for selection, or for exposure an index could replicate? |

The risk function's part needs independence. A portfolio manager has every reason to read good returns as skill, so
[performance risk](../pillars/performance-risk.md) measures the split from the risk function's own data and challenges
what it shows. Its three questions come from the [beliefs](00-philosophy.md#beliefs). Finding the risk nobody chose is
the first job. Set against the risk budget, each source shows what it uses and what it earns. And alpha, shown beside
the fee, tells the client whether selection is what they are paying for.

## Where do the labels mislead?
- **A top-down exposure needs no top-down view.** A pure stock picker still has sector and style positions, because the
  picks add up to them. A manager who picks cheap small companies earns value and size returns, which are beta however
  the picks were made. That return is unintended beta.
- **The instrument does not show the view.** A top-down view can be held through stocks, so only a record of what was
  chosen, and when, separates a tilt from unintended beta.
- **A measurement is not skill.** One period's alpha is mostly noise, so it is read over several periods and by
  decision-maker. At an information ratio of 0.5, it takes about 16 years to reach a t-statistic of 2.

## How does one holding split?
The split rests on three portfolios, each of which could be held.

| Portfolio | What it holds | What its return gives |
|---|---|---|
| **Benchmark portfolio** | The benchmark or strategic allocation in the governing documents, built mostly from indices | Policy beta |
| **Top-down portfolio** | Investable ETFs, futures and cash, carrying the real portfolio's exposure to every market and factor, each day | Active beta: its return less the benchmark portfolio's |
| **Real portfolio** | What the portfolio actually holds | Alpha: its return less the top-down portfolio's |

Beta is the step from the benchmark portfolio to the top-down portfolio, and every top-down call is measured there.
Alpha is the step from the top-down portfolio to the real portfolio: the top-down portfolio has carried all the beta
out, and what is left is selection. The top-down portfolio follows exposure as it is held, whether or not anyone chose
it, and the record then divides the first step: exposure with a call on record is a tilt or timing, and exposure with
no record is unintended beta.

A holding's weight is split, not its return. Take one sector, where the benchmark portfolio holds 16% of net assets
and the real portfolio 20%, a tilt on record. The sector index holds X at 15%, Y at 10% and the rest at 75%. The
top-down portfolio holds 20% in an ETF on the sector index, shown here by what is inside it. (The figures are
illustrative.)

| Security | Benchmark portfolio | Top-down portfolio | Real portfolio | Real less top-down | Return |
|---|---|---|---|---|---|
| X | 2.4% | 3.0% | 5.0% | +2.0% | 10% |
| Y | 1.6% | 2.0% | 0.0% | -2.0% | 2% |
| Rest of sector | 12.0% | 15.0% | 15.0% | 0.0% | 5% |
| **Total** | **16.0%** | **20.0%** | **20.0%** | **0.0%** | |
| **Return from the sector** | **0.87%** | **1.09%** | **1.25%** | **0.16%** | |

Of the real portfolio's 5.0% in X, 2.4% is the benchmark's, 0.6% is the tilt's and 2.0% is the manager's selection.
The weights of the real portfolio less the top-down portfolio sum to zero within each sector, so together they form a
long-short book: long what the manager prefers, short what is preferred less. Every portfolio has this book, including
one that never shorts a security.

The book still leans slightly towards the market, because X moves more with it than Y does. The top-down portfolio
carries that lean too, as a small position in index futures that nobody called; the
[alpha and beta method](../pillars/alpha-and-beta-method.md#building-the-top-down-portfolio) sets out how. In this
example, the sector's 1.25% is 0.87% policy beta, 0.22% from the tilt, 0.05% unintended beta and 0.11% alpha: 1.14%
from top-down and 0.11% from bottom-up. The tilt's funding sits in other sectors and is left out here.

## Sources
- Brinson, G., Hood, L. and Beebower, G. (1986). Determinants of Portfolio Performance. *Financial Analysts Journal*.
  The split of active return into allocation and selection.
- Sharpe, W. (1992). Asset Allocation: Management Style and Performance Measurement. *Journal of Portfolio
  Management*. Return explained by exposure to asset class indices, with selection as what is left.
- Fama, E. and French, K. (1993). Common Risk Factors in the Returns on Stocks and Bonds. *Journal of Financial
  Economics*. Style factors such as value and size as sources of return that an index can hold.
- Grinold, R. and Kahn, R. (2000). *Active Portfolio Management*, 2nd edition. McGraw-Hill. The link between the
  information ratio, time and statistical significance.
