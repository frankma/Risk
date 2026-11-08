# Sources of return

Every investment return comes from two sources. Top-down views decide how much of which markets to hold. Bottom-up
selection decides which securities to hold within them. Loosely, the first is called beta and the second alpha. This
chapter answers five questions about them. The [alpha and beta method](../pillars/alpha-and-beta-method.md) sets out
how the split is computed.

## What are the two sources?
Every part of a fund's return lands in exactly one place in this breakdown.

- **Fund return**
  - **Top-down views**, loosely beta
    - **Set by the client:** policy beta
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

- **Set by the client.** Policy beta is the return of the strategic allocation or benchmark, set by the client, the
  asset owner or a chief investment officer. The manager earns no credit for it.
- **Chosen by the manager.** Tilts are standing positions against that allocation, and timing is the return from
  changing exposure over time. Both count only if recorded when taken. Timing earns nothing without skill, so it is
  assessed on its own.
- **Chosen by nobody.** Unintended beta is any exposure with no record that anyone chose it, including price drift. The
  portfolio manager holds it, but nobody decided it. "Unintended" is a test of record, not of motive: an exposure the
  manager meant to take but did not record counts here until it is recorded.

Alpha belongs to the manager who selected the securities. The manager's branch and the unintended branch together are
active beta, and a fund's active return is active beta plus alpha. One beta is enough for general use; the branches are
there when it helps to say whose call it was.

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
A holding's weight is split, not its return. The beta portfolio holds the fund's own weight in each asset class and
sector, and follows the index inside each one. A security's beta weight is the fund's sector weight times the
security's weight in the sector index. Its alpha weight is the fund's weight less the beta weight.

Take a fund with 20% of net assets in one sector, where the sector index holds X at 15%, Y at 10% and the rest at 75%.
(The figures are illustrative.)

| Security | Fund weight | Beta weight | Alpha weight | Return | Beta contribution | Alpha contribution |
|---|---|---|---|---|---|---|
| X | 5.0% | 3.0% | +2.0% | 10% | 0.30% | +0.20% |
| Y | 0.0% | 2.0% | -2.0% | 2% | 0.04% | -0.04% |
| Rest of sector | 15.0% | 15.0% | 0.0% | 5% | 0.75% | 0.00% |
| **Total** | **20.0%** | **20.0%** | **0.0%** | | **1.09%** | **0.16%** |

The holding in X earned 0.50%, of which 0.30% is beta and 0.20% is alpha. The alpha weights sum to zero within each
sector, so together they form a long-short book: long what the fund prefers, short what it prefers less. Every portfolio
has this book, including one that never shorts a security.

The book still leans slightly towards the market, because X moves more with it than Y does. The
[alpha and beta method](../pillars/alpha-and-beta-method.md) takes that lean out as well. In this example, that leaves
1.14% from top-down and 0.11% from bottom-up, 1.25% in total.
