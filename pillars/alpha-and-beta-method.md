# Alpha and beta method

This page sets out how a risk function computes the split between the two
[sources of return](../framework/02-sources-of-return.md). It is a companion to
[performance risk](performance-risk.md), whose attribution reporting runs it.

**Beta is the return from market and factor exposure, whether an allocation call set it or a security pick carried it.
Alpha is the add-on return from security selection, measured after all the beta constructions, as a long-short book
neutral to them at every moment.**

Alpha depends on a declared list: it is what the declared factors leave unexplained. When an index or basket can
replicate a return, it joins the list. Value was once called alpha.

## Scope and basis
The split runs on publicly traded holdings, on the asset side and on gross returns: after trading and financing costs,
before fees. Fees and investor flows belong to the liability side. Holdings that are not publicly traded have no index
to replicate them, so they sit on one line that is not split, and nothing unmeasured is called alpha.

A bridge from gross to net return shows fees and flow effects, with the fee beside alpha to show whether alpha covers
it. Performance risk's outcome tests stay on what the client receives.

A benchmark that cannot be held, such as inflation plus a margin or a peer-group median, still judges the promise, but
an investable stand-in or cash serves as policy beta, and the gap is shown on its own line.

## The four beta lines
The [sources of return](../framework/02-sources-of-return.md#who-chose-each-part) chapter groups top-down return by
whose call it was. The method keeps the manager's branch as two lines, because timing needs its own skill test.

| Line | What it is | Who decides |
|---|---|---|
| Policy beta | The return of the benchmark or strategic allocation in the governing documents | Whoever set the mandate: the client, an asset owner, a chief investment officer, or the manager at a fund's launch |
| Tilts | Standing positions against that allocation, recorded when taken | The manager |
| Timing | The return from recorded changes in exposure over time | The manager |
| Unintended beta | Any exposure with no record that anyone chose it, including price drift | Nobody |

## Weights
The weight split is set out in [sources of return](../framework/02-sources-of-return.md#how-does-one-holding-split),
with a worked example. The book counts a security the portfolio does not hold as a short, whether or not anyone decided
against it. A holding outside the index has a beta weight of zero, so its whole position enters the book, and the next
step removes its exposures. Because the beta portfolio uses the portfolio's own sector weights, the book's return equals
the selection and interaction effects of an attribution. For bonds, the buckets are maturity, rating and sector, and the
book holds the issues chosen within them.

## Neutral to all of beta
Zero net weight is not zero exposure. In the worked example, X has a market beta of 1.3 and Y a market beta of 0.8, so
the book has a net market beta of 0.01 (2.0% × 1.3 less 2.0% × 0.8). With the market up 5%, 0.05% of the book's return
is market return. That is unintended beta, and it moves to beta. (The figures are illustrative.)

| | Beta | Alpha | Total |
|---|---|---|---|
| Split of weights | 1.09% | 0.16% | 1.25% |
| Unintended beta | +0.05% | -0.05% | 0.00% |
| **Result** | **1.14%** | **0.11%** | **1.25%** |

The same step applies to every declared factor: market, style, sector, country, currency, rates and spreads. The book's
return divides into exposure times factor return, which moves to beta, and specific return, which is alpha. This joins
the two attribution splits in the [philosophy](../framework/00-philosophy.md#2-drill-in).

**Factor returns** come from investable indices and baskets. **Exposure** is computed once, in
[market risk's daily run](market-risk.md#workflows-in-this-pillar), from daily holdings: a direct measure where one
exists, such as duration, and an estimated beta otherwise. Measuring it as often as calls are made keeps timing in beta.
The same split applies to risk, using the same baskets: factor risk is beta and stock-specific risk is alpha.

"At every moment" means against each day's holdings. Exposure is each day's weights times betas estimated over a long
window, so the book is neutral to estimated exposure, not to a true exposure no one can observe. Error in the estimates
is one of the limits set out below, and the regression test is what catches it.

## Computing the split
The risk engine weights the exposures by each day's holdings and compares them with the confirmed mandate terms and the
tilts and timing calls on record; anything without a record, including price drift, is unintended beta. The risk
manager's judgement on it is noted beside the line and does not change the line, and a tilt the manager confirms counts
once it is recorded, and is then accountable, not exempt: it is read against the risk budget like any other bet. The
book's return is shown separately for names held and names not held.

Trading cost is the gap between the portfolio's actual return and the return of its start-of-day holdings. A booked book
charges it by trade tag. A derived book charges any net change in a bucket's weight to beta and the rest to alpha, which
is approximate. The cost of trades forced by redemptions or other calls on cash stays where it lands, because those
trades cannot be reliably identified.

## Booked or derived
Two routes apply the same split.

| | Booked | Derived |
|---|---|---|
| Form | Separate beta and alpha books, with each trade tagged to one | Alpha weights computed from the portfolio's holdings |
| Suits | Portfolios that can short | Portfolios that cannot short or do not book separately |
| Evidence | Of each selection decision: each short was chosen | Of the manager's selection over several periods: labelled an estimate, with names held and not held shown apart |
| Weakness | A tilt can be tagged as selection; hedge error lands in alpha | Most shorts are names nobody considered; an underweight cannot exceed the beta weight |

The booked book is the standard. Its profit and loss is observed, but its hedge rests on estimated betas. Its return is
stated after borrow and financing costs and without the interest on its cash, which belongs to the cash bucket. A tag
is a label rather than evidence, so both routes pass the same test.

On either route, the construction is on record before the period starts: the buckets, the index inside each and the
factor list decide how much return counts as alpha. They are [governed
parameters](../framework/06-controls.md#materiality-thresholds-as-governed-parameters), owned by the risk function and
versioned. A factor joins the list only if an index or basket can hold it at the portfolio's size and a stated cost, and
a change applies from its effective date. Weights still move during the period, but a tilt or timing call counts only if
recorded when taken.

## The test and its limits
*It fails* when the construction is chosen after the result, or alpha carries exposure to a declared factor. *The test:*
within stated tolerances, the lines sum to the gross return, linked over longer periods by a stated method, and alpha's
return shows no exposure to any declared factor when regressed on the baskets.

Passing shows that the split is clean, not that alpha is skill or safe.

- **The list can miss a factor.** A book whose specific return moves more than independent positions would imply shares
  something the list does not cover, and the risk manager judges what it is.
- **Betas are estimates.** The book is neutral to exposure as estimated on each day's holdings. Estimation error leaves
  a little beta in alpha, which the regression test detects; a persistent finding is a reason to review the estimation,
  not the split.
- **Neutral to the list is not free of risk.** Crowded books can lose together, and a book that sells options can show
  no exposure until the tail arrives, so the [firm's footprint](integrated-view.md#the-firms-footprint) and stress tests
  still apply.
- **Weak prices flatter alpha.** Stale prices understate measured exposure, which moves beta into alpha, so holdings
  flagged in [liquidity risk](liquidity-risk.md) are marked in the split.

## In the workflow
Within [attribution reporting](performance-risk.md#workflows-in-this-pillar), the risk engine computes the split and
checks that it reconciles; a split that does not is an exception and is not drafted. A large share of gross excess
return from unintended beta, over several periods, fires the [source-of-return
rule](performance-risk.md#materiality-and-exceptions). The AI drafts the explanation, and the [grounding
check](../framework/06-controls.md#the-grounding-check) tests it. The risk manager judges whether alpha persists,
whether beta was intended and which questions to put to the portfolio manager, who decides what to hold.

## Sources
- Sharpe, W. (1992). Asset Allocation: Management Style and Performance Measurement. *Journal of Portfolio
  Management*. Return explained by exposure to investable indices.
- Fama, E. and French, K. (1993). Common Risk Factors in the Returns on Stocks and Bonds. *Journal of Financial
  Economics*. Style factors that a basket can hold.
- Carhart, M. (1997). On Persistence in Mutual Fund Performance. *Journal of Finance*. Apparent skill that a further
  factor explains, which is why alpha depends on the declared list.
- Grinold, R. and Kahn, R. (2000). *Active Portfolio Management*, 2nd edition. McGraw-Hill. Specific return and risk,
  and the regression test of residual exposure.
