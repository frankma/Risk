# How return is earned

## The essentials
Fundamentally, a portfolio's return is driven by two decisions: **top-down views** on which markets to hold, how much
and for how long, and **bottom-up selection** of the securities within them. They are two sources with different skills,
often with different decision-makers, and they need to work together toward one result.

Loosely, top-down views earn beta: any return above the risk-free rate that an index fund or a future could have
delivered, paid by market risk premia and style premia. Bottom-up selection earns alpha: the return left once beta is
carved out, paid by skill.

[Performance risk](../pillars/performance-risk.md) dissects each portfolio's return along this line, on three
portfolios. The benchmark portfolio's return above the risk-free rate is policy beta, the increment from it to the
top-down portfolio is active beta, and the increment from the top-down portfolio to the real portfolio is alpha. Because
the two sources sit with different skills and decision-makers, a clear attribution lets each call be judged on its
merits and supports a fair reward system that encourages more right calls, for the longevity of the team and the firm.
The [alpha and beta method](../pillars/alpha-and-beta-method.md) sets out the computation.

The rest of this chapter is the detail behind these points.

## What are the two sources?
A portfolio's return divides into two sources, by the decision that puts each part there: top-down views, loosely beta,
and bottom-up selection, loosely alpha. Apart from the risk-free return, the cost of holding beta and holdings that are
not publicly traded, every part of a portfolio's return lands in exactly one place in this breakdown.

- **Portfolio return**
  - **Top-down views**, loosely beta: paid by market risk premia and style premia
    - **Set in the mandate:** policy beta
    - **Chosen by a decision-maker:** tilts and timing
    - **Chosen by nobody:** unintended beta
  - **Bottom-up selection**, loosely alpha: paid by skill, and what selection adds once top-down is out

Beta does not mean passive: a well-timed allocation is a good beta call.

## What generates return?
Three return generators pay the two sources: market risk premia and style premia pay beta, and skill pays alpha.

| Generator | What it is | Why it pays | Source |
|---|---|---|---|
| **Market risk premia** | The return for holding a market: the equity premium, the term premium in rates and the credit premium in spreads. Currency exposure is tagged here by convention | It compensates for losses that arrive in bad times, when they hurt most | Beta |
| **Style premia** | The return of a rule that an index or basket can follow: value, momentum, size, carry, and the premium for holding less liquid public securities | Disputed: a risk, or a pattern in investor behaviour that persists; the framework takes no side, because the method needs only that an index fund or a future can deliver it | Beta, once declared |
| **Skill** | The return from choosing between securities that share the same exposures | One investor finds a wrong price before others do. Measured against the market, before costs and with the market's holdings unchanged, it is zero-sum: what one manager gains, another loses | Alpha |

The line between style premia and skill moves. A return counts as skill until an index or basket can replicate it, and
from then on it is a style premium. Value was once called alpha. A premium that no instrument holds at the portfolio's
size, as is often true of the premium for less liquid securities, is measured as alpha until one does, and the holdings
that [liquidity risk](../pillars/liquidity-risk.md) flags are [marked in the
split](../pillars/alpha-and-beta-method.md#the-test-and-its-limits).

A generator is not a decision. The mandate, the manager or nobody may have chosen how much of a premium a portfolio
holds, and [who chose it](01-sources-of-return.md#who-chose-each-part) is a separate question. A timing call changes how
much of a premium is held; the return the change adds is the timing line.

## How does each generator fail?
| Generator | How it fails | Where it is watched |
|---|---|---|
| **Market risk premia** | A large drawdown when the economy or the markets turn, with equities, rates and spreads often moving together | Market risk's [stress tests](../pillars/market-risk.md#stress-and-reverse-stress) and its rule on drawdown headroom |
| **Style premia** | Long periods that pay nothing, and sharp reversals when many holders leave at once. The premium for less liquid securities is lost when they must be sold | The stress tests, the [firm's footprint](../pillars/integrated-view.md#the-firms-footprint) and [liquidity risk](../pillars/liquidity-risk.md) |
| **Skill** | It decays as others find the same prices, crowded books lose together, and one period's result is mostly noise | Performance risk's [significance tests](../pillars/performance-risk.md#windows-and-significance) and the firm's footprint |

[Performance risk](../pillars/performance-risk.md) puts a different question to the portfolio manager for each
generator. Of a market risk premium: was the exposure chosen, and can the mandate bear its drawdown? Of a style premium:
is it in the mandate terms, and how crowded is it? Of skill: is it more than noise, and does it cover the fee?

## Who chose each part?
Top-down return has three branches, according to whose call it was.

- **Set in the mandate.** Policy beta is the return, above the risk-free rate, of the benchmark or strategic allocation
  in the portfolio's governing documents. A client, an asset owner or a chief investment officer may have set it, or,
  for a pooled fund, the manager when the fund was launched, which investors accepted when they bought. Whoever chose
  it, it is part of the promise and earns no one credit.
- **Chosen by a decision-maker.** Tilts are standing positions against that allocation, and timing is the return from
  changing exposure over time. Both count only if recorded when taken, and each is credited to whoever recorded it: a
  chief investment officer or an allocation committee for an overlay, or the portfolio manager. Timing earns nothing
  without skill, so it is assessed on its own.
- **Chosen by nobody.** Unintended beta is any exposure with no record that anyone chose it, including price drift. A
  pure stock picker still has sector and style positions, because the picks add up to them: a manager who picks cheap
  small companies earns value and size premia, which are beta however the picks were made. "Unintended" is a test of
  record, not of motive: an exposure someone meant to take but did not record counts here until it is recorded. A
  recorded tilt is still read against the risk budget like any other bet, and a tilt outside the confirmed mandate terms
  still fails the style check.

Alpha belongs to whoever selected the securities. The decision-maker's branch and the unintended branch together are
active beta, and a portfolio's active return is active beta plus alpha, after the cost of holding the beta.

A portfolio manager has every reason to read good returns as skill, so [performance
risk](../pillars/performance-risk.md) measures the split from the risk function's own data and challenges what it shows.

## How does one holding split?
A holding's weight is split, not its return, across the [three
portfolios](../pillars/alpha-and-beta-method.md#the-three-portfolios). In the method's [worked
example](../pillars/alpha-and-beta-method.md#building-the-top-down-portfolio), one sector's 1.25% return splits into
0.87% from the benchmark portfolio, which is the risk-free return and policy beta together, 0.22% from a tilt on record,
0.05% unintended beta and 0.11% alpha.

## Sources
- Sharpe, W. (1991). The Arithmetic of Active Management. *Financial Analysts Journal*. Before costs, active returns
  measured against the market sum to zero.
- Pedersen, L. (2018). Sharpening the Arithmetic of Active Management. *Financial Analysts Journal*. Why the zero-sum
  result holds only while the market's holdings do not change.
- Ilmanen, A. (2011). *Expected Returns: An Investor's Guide to Harvesting Market Rewards*. Wiley. Market and style
  premia, why each may pay and how each has failed.
- Ang, A. (2014). *Asset Management: A Systematic Approach to Factor Investing*. Oxford University Press. Premia as
  compensation for losses in bad times.
- Lakonishok, J., Shleifer, A. and Vishny, R. (1994). Contrarian Investment, Extrapolation, and Risk. *Journal of
  Finance*. The behavioural explanation of the value premium, against the risk explanation of Fama and French.
- Amihud, Y. and Mendelson, H. (1986). Asset Pricing and the Bid-Ask Spread. *Journal of Financial Economics*. The
  premium for holding less liquid securities.
- Brinson, G., Hood, L. and Beebower, G. (1986). Determinants of Portfolio Performance. *Financial Analysts Journal*.
  The split of active return into allocation and selection.
- Sharpe, W. (1992). Asset Allocation: Management Style and Performance Measurement. *Journal of Portfolio Management*.
  Return explained by exposure to asset class indices, with selection as what is left.
- Fama, E. and French, K. (1993). Common Risk Factors in the Returns on Stocks and Bonds. *Journal of Financial
  Economics*. Style factors such as value and size as sources of return that an index can hold.
- Grinold, R. and Kahn, R. (2000). *Active Portfolio Management*, 2nd edition. McGraw-Hill. The link between the
  information ratio, time and statistical significance.
