# Sources of return

Every investment return comes from two sources. Top-down views decide how much of which markets to hold. Bottom-up
selection decides which securities to hold within them. Loosely, the first is called beta and the second alpha. This
chapter sets out the two sources, who decides each, why the difference matters and how a single holding splits between
them. The [alpha and beta method](../pillars/alpha-and-beta-method.md) sets out how the split is computed.

## The two sources

| | Top-down | Bottom-up |
|---|---|---|
| **The question** | How much of which markets? | Which securities within them? |
| **Examples** | Asset allocation, market timing, sector and style tilts | Stock and bond selection |
| **Who usually decides** | Asset owner, chief investment officer, allocation team | Portfolio manager, analysts |
| **Can an index replicate it?** | The exposure, yes; the timing of it, no | No |
| **How fast it can be judged** | Slowly, because there are few calls | Faster, because there are many |
| **Loose name** | Beta | Alpha |

Both take judgement, and both can be wrong. Beta does not mean passive: market timing is a top-down view, because it
decides how much of a market to hold, and a well-timed allocation is a good beta call. What sets alpha apart is that no
index or basket can replicate it, because it comes from choosing between securities that share the same exposures.

## Who decides each
Beta divides into four lines, according to whose call it was.

| Line | What it is | Who decides |
|---|---|---|
| Policy beta | The return of the strategic allocation or benchmark | The client, asset owner or chief investment officer; the manager earns no credit for it |
| Tilts | The manager's standing positions against that allocation, recorded when taken | The manager |
| Timing | The return from recorded changes in exposure over time, which earns nothing without skill and is assessed on its own | The manager |
| Carried beta | Any exposure without a record that anyone chose it, including price drift | Nobody; the portfolio manager holds it |
| Alpha | What security selection adds once all of the above is out | The manager |

One beta is enough for general use, and the lines are there when it helps to say whose call it was. Tilts, timing and
carried beta together are active beta, and a fund's active return is active beta plus alpha.

## Why it matters

| Who | The question it answers |
|---|---|
| Asset owner | Which top-down views do I set myself, and what am I paying others for? |
| Fund house | Where are we actually good, and how do we divide risk between the two sources? |
| Risk function | Was each risk chosen, and was it paid for? |

The risk function's part needs independence. A portfolio manager has every reason to read good returns as skill, so
[performance risk](../pillars/performance-risk.md) measures the split from the risk function's own data and challenges
what it shows. Three questions follow from the [beliefs](00-philosophy.md#beliefs).

- **Was this risk chosen?** Tilts and timing were; carried beta was not. Finding the risk nobody chose is the first job.
- **Was it paid for?** Set against the risk budget, each source shows what it uses and what it earns.
- **Is the client paying for selection, or for exposure an index could replicate?** Alpha, shown beside the fee, answers
  this.

## Where the labels need care
- **A top-down exposure needs no top-down view.** A pure stock picker still has sector and style positions, because the
  picks add up to them. A manager who picks cheap small companies earns value and size returns, which are beta however
  the picks were made. That return is carried beta.
- **The instrument does not show the view.** A top-down view can be held through stocks, so only a record of what was
  chosen, and when, separates a tilt from carried beta.
- **A measurement is not skill.** One period's alpha is mostly noise, so it is read over several periods and by
  decision-maker. At an information ratio of 0.5, it takes about 16 years to reach a t-statistic of 2.

## Splitting a holding
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

To see bottom-up on its own, top-down has to come out completely. X has a market beta of 1.3 and Y of 0.8, so the book
still leans towards the market. With the market up 5%, 0.05% of its return is market return, which moves to beta. That
leaves 1.14% from top-down and 0.11% from bottom-up, 1.25% in total. The
[alpha and beta method](../pillars/alpha-and-beta-method.md) applies the same step to every declared factor.
