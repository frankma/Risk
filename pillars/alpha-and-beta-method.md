# Alpha and beta method

## In short
**The question:** how much of a portfolio's return is beta, and how much is alpha?

**The rule:** the split rests on three portfolios: the benchmark portfolio, the top-down portfolio and the real
portfolio. Beta is the step from the first to the second, where all market and factor exposure is measured, whether an
allocation call set it or a security pick carried it. Alpha is the step from the second to the third: the add-on return
from security selection, once the top-down portfolio has carried all the beta out.

**How the work is done:** within [attribution reporting](performance-risk.md#workflows-in-this-pillar), the risk engine
builds the top-down portfolio each day, computes the split and checks that it reconciles; a split that does not is an
exception and is not drafted. The AI drafts the explanation, and the [grounding
check](../framework/08-controls.md#the-grounding-check) tests it. The risk manager judges whether alpha persists,
whether beta was intended and which questions to put to the portfolio manager, who decides what to hold.

**Alpha depends on a declared list:** it is what the declared factors leave unexplained. When an ETF or a future can
replicate a return, it joins the list; value was once called alpha. Each declared factor is tagged with the [return
generator](../framework/02-sources-of-return.md#what-generates-return) that pays it, a market risk premium or a style
premium, so that beta can be read by generator and alpha is read as skill.

This page is a companion to [sources of return](../framework/02-sources-of-return.md) and [performance
risk](performance-risk.md). The rest of it is the detail behind these points.

## Scope and basis
The split runs on publicly traded holdings and on gross returns: after trading and financing costs, before fees.
Holdings that are not publicly traded have no index to replicate them, so they sit on one line that is not split, and
nothing unmeasured is called alpha.

A bridge from gross to net return shows fees and flow effects, with the fee beside alpha to show whether alpha covers
it. Performance risk's outcome tests stay on what the client receives.

A benchmark that cannot be held, such as inflation plus a margin or a peer-group median, still judges the promise, but
an investable stand-in or cash serves as the benchmark portfolio, and the gap is shown on its own line.

## The three portfolios
| Portfolio | What it holds | What its return gives |
|---|---|---|
| Benchmark portfolio | The benchmark or strategic allocation in the governing documents, built mostly from indices | Policy beta |
| Top-down portfolio | Investable ETFs, futures and cash, carrying the real portfolio's exposure to every declared factor on each day | Active beta, after the cost of holding it: its return less the benchmark portfolio's |
| Real portfolio | The portfolio's actual holdings | Alpha: its return less the top-down portfolio's |

The real portfolio's gross return is the benchmark portfolio's return plus the two steps, so no line is what a model
leaves over.

The top-down portfolio follows exposure as held, not as called. If it held only the calls on record, the beta that
security picks carry would stay in the last step and be counted as alpha. Because it holds all of the real portfolio's
exposure, the last step is selection alone, and the record divides the step before it.

## The beta lines
The [sources of return](../framework/02-sources-of-return.md#who-chose-each-part) chapter groups top-down return by
whose call it was. The method keeps the manager's branch as two lines, because timing needs its own skill test. Policy
beta is the benchmark portfolio's return, and the other lines divide the step from the benchmark portfolio to the
top-down portfolio.

| Line | What it is | Who decides |
|---|---|---|
| Policy beta | The return of the benchmark or strategic allocation in the governing documents | [Whoever set the mandate](../framework/02-sources-of-return.md#who-chose-each-part) |
| Tilts | Standing positions against that allocation, recorded when taken | The manager |
| Timing | The return from recorded changes in exposure over time | The manager |
| Unintended beta | Any exposure with no record that anyone chose it, including price drift | Nobody |
| Cost of holding beta | The return of the top-down portfolio's instruments less the return of the indices they track | Nobody |

**The cost of holding beta** exists because ETFs charge fees and futures carry roll and financing costs, while the
indices behind the benchmark portfolio cost nothing, so a top-down portfolio that copied the benchmark exactly would
still trail it. It is shown beside the fee, because it is what the replicable part of the return costs to buy.

## Building the top-down portfolio
The top-down portfolio is built in two steps, each day, from the real portfolio's holdings.

**Bucket weights.** It first takes the real portfolio's own weight in each asset class and sector, held through an ETF
or a future on the index of each. The weights of the real portfolio less this first step form the long-short book.
The book counts a security the portfolio does not hold as a short, whether or not anyone decided against it. A holding
outside the index has no weight in the top-down portfolio, so its whole position enters the book, and the next step
removes its exposures. Because this step uses the real portfolio's own sector weights, the book's return equals the
selection and interaction effects of an attribution. For bonds, the buckets are maturity, rating and sector, and the
book holds the issues chosen within them.

**A worked example.** Take one sector, where the benchmark portfolio holds 16% of net assets and the real portfolio
20%, a tilt on record. The sector index holds X at 15%, Y at 10% and the rest at 75%. The top-down portfolio holds 20%
in an ETF on the sector index, shown here by what is inside it. (The figures are illustrative.)

| Security | Benchmark portfolio | Top-down portfolio | Real portfolio | Real less top-down | Return |
|---|---|---|---|---|---|
| X | 2.4% | 3.0% | 5.0% | +2.0% | 10% |
| Y | 1.6% | 2.0% | 0.0% | -2.0% | 2% |
| Rest of sector | 12.0% | 15.0% | 15.0% | 0.0% | 5% |
| **Total** | **16.0%** | **20.0%** | **20.0%** | **0.0%** | |
| **Return from the sector** | **0.87%** | **1.09%** | **1.25%** | **0.16%** | |

Of the real portfolio's 5.0% in X, 2.4% is the benchmark's, 0.6% is the tilt's and 2.0% is the manager's selection. The
real portfolio less the top-down portfolio sums to zero within the sector: a long-short book, long what the manager
prefers and short what is preferred less. Every portfolio has this book, including one that never shorts a security.

**The book's exposures.** Zero net weight is not zero exposure. In the example above, X has a market beta of 1.3 and Y
a market beta of 0.8, so the book has a net market beta of 0.01 (2.0% × 1.3 less 2.0% × 0.8). The top-down portfolio
takes that exposure on as index futures worth 1% of net assets. With the market up 5%, the futures earn 0.05%, which
leaves the book and joins beta. No call is on record for it, so it is unintended beta. (The figures are illustrative,
and leave out the cost of holding the instruments.)

| Portfolio | Return from the sector | Step | Line |
|---|---|---|---|
| Benchmark portfolio | 0.87% | 0.87% | Policy beta |
| Top-down portfolio, bucket weights | 1.09% | +0.22% | Tilt, on record |
| Top-down portfolio, with the book's exposures | 1.14% | +0.05% | Unintended beta |
| **Real portfolio** | **1.25%** | **+0.11%** | **Alpha** |

The same step applies to every declared factor: market, style, sector, country, currency, rates and spreads. Each is
carried by an ETF or a future on the index or basket that defines it, and the top-down portfolio holds each in the
amount of the real portfolio's exposure.

**Each factor carries one generator tag.** The equity market, rates, spreads and currency are market risk premia, and a
sector or country index takes the tag of the market it is a slice of. Value, momentum, size, carry and a basket of less
liquid securities are style premia. The tag changes no line of the split. It groups the beta lines, so that policy beta,
tilts, timing and unintended beta can each be shown by the generator that paid them.

The book's return divides into exposure times factor return, which the top-down portfolio carries, and specific return,
which is alpha. This joins the two attribution splits in the [philosophy](../framework/00-philosophy.md#2-drill-in).

**Factor returns** are the returns of those instruments. **Exposure** is computed once, in [market risk's daily
run](market-risk.md#factors), from daily holdings; measuring it as often as calls are made keeps timing
in beta. The same split applies to risk, using the same instruments: factor risk is beta and stock-specific risk is
alpha.

The top-down portfolio is rebuilt against each day's holdings. Exposure is each day's weights times betas estimated over
a long window, so the last step is neutral to estimated exposure, not to a true exposure no one can observe. Error in
the estimates is one of the limits set out below, and the regression test is what catches it.

## Computing the split
The risk engine weights the exposures by each day's holdings, builds the top-down portfolio from them and compares its
positions with the benchmark portfolio, the confirmed mandate terms and the tilts and timing calls on record; anything
without a record, including price drift, is unintended beta. The risk manager's judgement on it is noted beside the line
and does not change the line. The book's return is shown separately for names held and
names not held.

The **trading effect** is the gap between the portfolio's actual return and the return of its start-of-day holdings:
trading cost, and the gains and losses from trading during the day. A booked book charges it by trade tag. A derived
book charges any net change in a bucket's weight to beta and the rest to alpha, which is approximate. The cost of trades
forced by redemptions or other calls on cash stays where it lands, because those trades cannot be reliably identified.

A large share of gross excess return from unintended beta, over several periods, fires the [source-of-return
rule](performance-risk.md#materiality-and-exceptions).

## Booked or derived
Two routes apply the same split; on the booked route, hedge error stays in alpha.

| | Booked | Derived |
|---|---|---|
| Form | The top-down portfolio is held as a beta book beside an alpha book, with each trade tagged to one | The top-down portfolio is kept on paper, and the long-short book is computed from the portfolio's holdings |
| Suits | Portfolios that can short | Portfolios that cannot short or do not book separately |
| Evidence | Of each selection decision: each short was chosen | Of the manager's selection over several periods: labelled an estimate, with names held and not held shown apart |
| Weakness | A tilt can be tagged as selection; hedge error lands in alpha | Most shorts are names nobody considered; an underweight cannot exceed the top-down weight |

**Hedge error is the exception to the as-held rule.** On the booked route the top-down portfolio is the beta book as
booked, so exposure that the alpha book fails to hedge stays in the alpha line. The regression test still runs on the
booked book, and the exposure it finds is reported as hedge error beside alpha, so that the reader sees how much of the
alpha is unhedged beta.

The booked book is the standard. Its profit and loss is observed, but its hedge rests on estimated betas. Its return is
stated after borrow and financing costs and without the interest on its cash, which belongs to the cash bucket. A tag is
a label rather than evidence, so both routes pass the same test.

On either route, the construction is on record before the period starts: the benchmark portfolio, the buckets, the
instrument inside each, the factor list and each factor's generator tag decide how much return counts as alpha and which
generator the rest is read against. They are [governed
parameters](../framework/08-controls.md#materiality-thresholds-as-governed-parameters), owned by the risk function and
versioned. A factor joins the list only if an ETF or a future can hold it at the portfolio's size and a stated cost, and
a change applies from its effective date. Weights still move during the period, but a tilt or timing call counts only if
recorded when taken.

## The test and its limits
*It fails* when the construction is chosen after the result, or alpha carries exposure to a declared factor. *The test:*
within stated tolerances, the lines sum to the gross return, linked over longer periods by a stated method, and alpha's
return shows no exposure to any declared factor when regressed on the top-down portfolio's instruments.

Passing shows that the split is clean, not that alpha is skill or safe.

- **The list can miss a factor.** A book whose specific return moves more than independent positions would imply shares
  something the list does not cover, and the risk manager judges what it is. Until it is declared, a style premium that
  the list misses is measured as alpha and read as skill.
- **Betas are estimates.** The top-down portfolio matches exposure as estimated on each day's holdings. Estimation error
  leaves a little beta in alpha, which the regression test detects; a persistent finding is a reason to review the
  estimation, not the split.
- **Neutral to the list is not free of risk.** Crowded books can lose together. ETFs and futures move in line with their
  markets, so a book that sells options can show no exposure until the tail arrives. The [firm's
  footprint](integrated-view.md#the-firms-footprint) and stress tests still apply.
- **Weak prices flatter alpha.** Stale prices understate measured exposure, which moves beta into alpha, so holdings
  flagged in [liquidity risk](liquidity-risk.md) are marked in the split.

## Sources
- Sharpe, W. (1992). Asset Allocation: Management Style and Performance Measurement. *Journal of Portfolio Management*.
  Return explained by exposure to investable indices.
- Fama, E. and French, K. (1993). Common Risk Factors in the Returns on Stocks and Bonds. *Journal of Financial
  Economics*. Style factors that a basket can hold.
- Carhart, M. (1997). On Persistence in Mutual Fund Performance. *Journal of Finance*. Apparent skill that a further
  factor explains, which is why alpha depends on the declared list.
- Grinold, R. and Kahn, R. (2000). *Active Portfolio Management*, 2nd edition. McGraw-Hill. Specific return and risk,
  and the regression test of residual exposure.
