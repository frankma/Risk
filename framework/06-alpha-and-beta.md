# Alpha and beta

A portfolio's return comes from two kinds of call: how it allocates, and which securities it selects within that
allocation. This chapter defines the return from each, shows how any holding splits between them, and sets out the
long-short book that makes the split exact. The split serves the Assess decision in the
[philosophy](00-philosophy.md#purpose-transparency-for-three-decisions) and runs in
[performance risk](../pillars/performance-risk.md), which tests whether returns come from the sources a mandate
describes.

**Beta is the return from allocation calls. Alpha is the add-on return from security selection, measured after all the
beta constructions, as a long-short book neutral to them.**

## Definitions
**Beta** is what a portfolio earns from its exposure to markets and factors. This exposure can be bought cheaply,
through index funds, futures and factor baskets.

| Call | Why it is beta |
|---|---|
| Strategic and tactical asset allocation | It sets the exposure to each market |
| Market timing | It is an asset allocation call, held for a shorter time |
| Tilts by sector, country, currency, rates or spreads | Each can be held through an index, a future or a basket |
| Style tilts, such as value or size | Each can be held through a factor basket |

**Alpha** is what security selection adds once every beta construction has been taken out. It cannot be bought cheaply,
because it comes from choosing between securities that share the same exposures.

Three points follow from these definitions.

- **Selection is alpha only after beta is out.** A manager who picks cheap small companies earns value and size
  returns, which are beta however the picks were made.
- **Beta is still a decision.** Tilts and timing spend the risk budget, have a decision-maker and are assessed. A
  well-timed allocation is a good beta call, not alpha.
- **Alpha depends on a declared list.** It is what the declared factors leave unexplained. When a return becomes cheap
  to buy, it joins the list: value was once called alpha.

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

The holding in X earned 0.50%, of which 0.30% is beta and 0.20% is alpha. Not holding Y is also a selection call, in
effect a 2.0% short. The alpha weights sum to zero within each sector, so together they form a long-short book. Every
portfolio has this book, including one that never shorts a security.

Three details complete the split. A holding outside the index has a beta weight of zero, so the whole position is
alpha. Because the beta portfolio uses the fund's own sector weights, the book's return equals the selection and
interaction effects of an allocation and selection attribution. For bonds, the buckets are maturity, rating and sector,
and the book holds the issues chosen within them.

## Neutral to all of beta
Zero net weight is not zero exposure. If X has a market beta of 1.3 and Y a market beta of 0.8, the book has a net
market beta of 0.01 (2.0% × 1.3 less 2.0% × 0.8). With the market up 5%, 0.05% of the book's return is market return,
and it moves to beta.

| | Beta | Alpha | Fund |
|---|---|---|---|
| Split of weights | 1.09% | 0.16% | 1.25% |
| Market return in the book | +0.05% | -0.05% | 0.00% |
| **Result** | **1.14%** | **0.11%** | **1.25%** |

The same step applies to every declared factor: market, style, sector, country, currency, rates and spreads. The book's
return divides into exposure times factor return, which moves to beta, and specific return, which is alpha. This is
where the two attribution splits in the [philosophy](00-philosophy.md#2-drill-in) meet: selection's factor return moves
to beta, and the rest of selection is the specific return.

The same cut applies to risk. Factor risk is beta and stock-specific risk is alpha, so the risk budget can set what each
uses against what each earns.

## Booked or derived
Two routes reach the same book.

| | Booked | Derived |
|---|---|---|
| Form | Separate beta and alpha books, with each trade tagged to one | Alpha weights computed from the fund's holdings |
| Return | Observed profit and loss | Computed from weights and returns |
| Neutrality | Held by a hedge | Reached by calculation |
| Suits | Funds that can short | Funds that cannot short or do not book separately |
| Weakness | A tilt can be tagged as selection | An underweight cannot exceed the beta weight |

The booked book is the cleanest form, because its return is observed rather than estimated. That return is stated after
borrow and financing costs and without the interest earned on the book's cash. The derived book is the same cut where
booking is not possible. A tag is a label rather than evidence, so both routes pass the same test below.

On either route, the construction is on record before the period starts. Whoever picks the buckets, the index inside
each and the factor list after the result is known can move return between beta and alpha. These choices are therefore
[governed parameters](04-controls.md#materiality-thresholds-as-governed-parameters), owned by the risk function and
versioned, so that any past split can be reproduced. Weights still move during the period, because tilts and timing are
beta calls; the rules for splitting them do not.

## The test and its limits
*It fails* when the construction is chosen after the result, or the alpha book carries exposure to a declared factor.
*The test:* beta and alpha sum to the fund's return, and the book's exposure to each declared factor stays within a
stated tolerance.

Passing the test shows that the split is clean, not that the alpha is skill or that it is safe.

- **A measurement is not skill.** One period's alpha is mostly noise, so it is read over several periods and by
  decision-maker. At an information ratio of 0.5, it takes about 16 years to reach a t-statistic of 2.
- **Neutral to the list is not free of risk.** Books crowded into the same positions can lose together, so the
  [firm's footprint](../pillars/integrated-view.md#the-firms-footprint) reads crowding across funds. A book that sells
  options can show no exposure until the tail arrives, so stress tests still apply.
- **Weak prices flatter alpha.** Stale prices understate measured exposure, which moves beta into alpha. Holdings
  flagged in [liquidity risk](../pillars/liquidity-risk.md) are marked in the split.

## Fine-tuning beta
One beta is enough for general use. Where it helps to say whose call it was, beta divides in two. **Policy beta** is the
return of the strategic allocation or benchmark, usually set by the client or a chief investment officer, and the
manager earns no credit for it. **Active beta** is the return from the manager's tilts and timing against that
allocation, and it spends the tracking-error budget. A fund's active return is then active beta plus alpha.

## In the workflow
The split follows the framework's core pattern, within
[attribution reporting](../pillars/performance-risk.md#workflows-in-this-pillar). Code computes the weights, the book,
its exposures and the contributions, and checks that they reconcile; a split that does not reconcile is not drafted. The
AI drafts the explanation from those figures, and the [grounding check](04-controls.md#the-grounding-check) tests every
number in it. The risk manager judges what the split means: whether alpha persists, whether beta was intended, and which
questions to put to the portfolio manager, who decides what to hold.
