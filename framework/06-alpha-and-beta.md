# Alpha and beta

This chapter defines beta and alpha and shows how any holding splits between them. The split serves the Assess decision
in the [philosophy](00-philosophy.md#purpose-transparency-for-three-decisions) and runs in
[performance risk](../pillars/performance-risk.md#computing-the-split).

**Beta is the return from market and factor exposure, whether an allocation call set it or a security pick carried it.
Alpha is the add-on return from security selection, measured after all the beta constructions, as a long-short book
neutral to them at every moment.**

## Definitions
**Beta** is what a portfolio earns from its exposure to markets and factors. Index funds, futures and factor baskets
can replicate this exposure.

| Source | Why it is beta |
|---|---|
| Strategic and tactical asset allocation | It sets the exposure to each market |
| Market timing | It is an asset allocation call, and at every moment it is market exposure |
| Tilts by sector, country, currency, rates, spreads or style | Each can be held through an index, a future or a basket |
| Exposure carried by security picks | It is the same exposure, whether or not anyone chose it |

**Alpha** is what security selection adds once every beta construction has been taken out. It stays neutral to markets
and factors at every moment, and no index or basket can replicate it, because it comes from choosing between securities
that share the same exposures.

- **Selection is alpha only after beta is out.** A manager who picks cheap small companies earns value and size
  returns, which are beta however the picks were made.
- **Beta is not always a decision.** Tilts and timing have a decision-maker and are assessed: a well-timed allocation is
  a good beta call, not alpha. Carried beta is a by-product of security picks: the portfolio manager holds it, but
  nobody chose it.
- **Alpha depends on a declared list.** It is what the declared factors leave unexplained. When an index or basket can
  replicate a return, it joins the list: value was once called alpha.

## Scope and basis
The split runs on publicly traded holdings, on the asset side and on gross returns: after trading and financing costs,
before fees. Fees and investor flows belong to the liability side. Holdings that are not publicly traded have no index
to replicate them, so they sit on one line that is not split, and nothing unmeasured is called alpha.

A bridge from the gross return to the net return shows fees and flow effects, with the fee beside alpha, so that a
reader can see whether alpha covers it. Performance risk's outcome tests stay on what the client receives.

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

The holding in X earned 0.50%, of which 0.30% is beta and 0.20% is alpha. The book counts not holding Y as a 2.0% short,
whether or not anyone decided against Y. The alpha weights sum to zero within each sector, so together they form a
long-short book. Every portfolio has this book, including one that never shorts a security.

A holding outside the index has a beta weight of zero, so its whole position enters the book, and the next step removes
its exposures. Because the beta portfolio uses the fund's own sector weights, the book's return equals the selection and
interaction effects of an attribution. For bonds, the buckets are maturity, rating and sector, and the book holds the
issues chosen within them.

## Neutral to all of beta
Zero net weight is not zero exposure. If X has a market beta of 1.3 and Y a market beta of 0.8, the book has a net
market beta of 0.01 (2.0% × 1.3 less 2.0% × 0.8). With the market up 5%, 0.05% of the book's return is market return.
That is carried beta, and it moves to beta.

| | Beta | Alpha | Total |
|---|---|---|---|
| Split of weights | 1.09% | 0.16% | 1.25% |
| Carried beta | +0.05% | -0.05% | 0.00% |
| **Result** | **1.14%** | **0.11%** | **1.25%** |

The same step applies to every declared factor: market, style, sector, country, currency, rates and spreads. The book's
return divides into exposure times factor return, which moves to beta, and specific return, which is alpha. This joins
the two attribution splits in the [philosophy](00-philosophy.md#2-drill-in).

**Factor returns** come from investable indices and baskets, because beta is what can be replicated. **Exposure** comes
from daily holdings, measured as often as calls are made, which keeps timing in beta. The same split applies to risk,
using the same baskets: factor risk is beta and stock-specific risk is alpha.

## Booked or derived
Two routes apply the same split.

| | Booked | Derived |
|---|---|---|
| Form | Separate beta and alpha books, with each trade tagged to one | Alpha weights computed from the fund's holdings |
| Suits | Funds that can short | Funds that cannot short or do not book separately |
| Evidence | Of selection decisions: each short was chosen | Of where return came from: labelled an estimate |
| Weakness | A tilt can be tagged as selection; hedge error lands in alpha | Most shorts are names nobody considered; an underweight cannot exceed the beta weight |

The booked book is the standard. Its profit and loss is observed, but its hedge rests on estimated betas. Its return is
stated after borrow and financing costs and without the interest on its cash. A tag is a label rather than evidence, so
both routes pass the same test.

On either route, the construction is on record before the period starts: the buckets, the index inside each and the
factor list decide how much return counts as alpha. They are
[governed parameters](04-controls.md#materiality-thresholds-as-governed-parameters), owned by the risk function and
versioned. A factor joins the list only if an index or basket can hold it at the fund's size and a stated cost, and a
change applies from its effective date. Weights still move during the period; the rules for splitting them do not.

## The test and its limits
*It fails* when the construction is chosen after the result, or alpha carries exposure to a declared factor. *The test:*
within stated tolerances, the lines sum to the gross return, linked over longer periods by a stated method, and alpha's
return shows no exposure to any declared factor when regressed on the baskets.

Passing the test shows that the split is clean, not that the alpha is skill or that it is safe.

- **A measurement is not skill.** One period's alpha is mostly noise, so it is read over several periods and by
  decision-maker. At an information ratio of 0.5, it takes about 16 years to reach a t-statistic of 2.
- **The list can miss a factor.** A book whose specific return moves more than independent positions would imply shares
  something the list does not cover, and the risk manager judges what it is.
- **Neutral to the list is not free of risk.** Crowded books can lose together, and a book that sells options can show
  no exposure until the tail arrives, so the
  [firm's footprint](../pillars/integrated-view.md#the-firms-footprint) and stress tests still apply.
- **Weak prices flatter alpha.** Stale prices understate measured exposure, which moves beta into alpha, so holdings
  flagged in [liquidity risk](../pillars/liquidity-risk.md) are marked in the split.

## Fine-tuning beta
One beta is enough for general use. Where it helps to say whose call it was, it divides into four lines. **Policy beta**
is the return of the strategic allocation or benchmark, usually set by the client or a chief investment officer, and
earns the manager no credit. **Tilts** are the manager's standing positions against it. **Timing** is the return from
varying exposure over time, which earns nothing without skill and is assessed on its own. **Carried beta** is the
exposure the alpha book brings along. The last three are active beta, and a fund's active return is active beta plus
alpha. A benchmark that cannot be held, such as inflation plus a margin, still judges the promise, but an investable
stand-in or cash serves as policy beta, and the gap is shown on its own line.

## In the workflow
Within [attribution reporting](../pillars/performance-risk.md#workflows-in-this-pillar), code computes the split and
checks that it reconciles; a split that does not is an exception and is not drafted. A large share of excess return from
carried beta fires the [source-of-return rule](../pillars/performance-risk.md#materiality-and-exceptions). The AI drafts
the explanation, and the [grounding check](04-controls.md#the-grounding-check) tests every number in it. The risk
manager judges whether alpha persists, whether beta was intended and which questions to put to the portfolio manager,
who decides what to hold.
