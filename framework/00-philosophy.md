# Investment risk philosophy

This chapter sets out what a risk function believes about investment risk, what the function is for and how it works. It
is the ground the rest of the framework stands on: [investment risk](01-investment-risk.md) defines the scope and
organises the recurring work into three pillars, [sources of return](02-sources-of-return.md) sets out where return
comes from, and the [principles](05-principles.md), [working with AI](06-working-with-ai.md) and the [redesign
method](07-redesign-method.md) set out how the risk manager does that work alongside AI. The beliefs do not depend on
any particular model; any model a risk function uses is judged against them.

**Investment risk management shows whether every portfolio takes the risks its mandate intends, in the size it can bear,
and is paid for them, and challenges it where it does not.**

Risk management earns no return of its own. Its product is **sight**: out of millions of numbers (hundreds of
positions, thousands of risk factors, millions of possible futures), the few worth questioning and acting on.

**Investment risk is the chance that a portfolio's outcome departs from what its mandate intends:** a loss, a shortfall
against its objective or benchmark, or an inability to meet calls on its cash, such as redemptions, arising from the
investments themselves. Its scope and boundaries are set out in [investment
risk](01-investment-risk.md#scope-and-boundaries).

The capital at risk is the clients', not the firm's. So risk is judged against what each client was promised, and
the firm's franchise follows from keeping those promises.

## Beliefs
Each is a position a reasonable firm could reject. Together they decide what the rules do not. (The figures are
illustrative.)

1. **The mandate defines the risk.** Appetite belongs to the client, expressed as a benchmark, a tracking error budget,
   guidelines and liquidity terms, not a firm-wide number. Risk is judged against the promise: losing 20% when the
   benchmark loses 22% can be success.
2. **Intended risk is the product; unintended risk is the hazard.** Clients pay for the bets the investment team means
   to take. The first job is to find the ones nobody chose: a value tilt in a growth portfolio, a rates bet in a
   credit portfolio, a crowded factor riding along with stock picks.
3. **Risk must earn its place.** Risk and return are two sides of one coin. Every unit of active risk should be paid for
   by expected return. The portfolio manager decides what to hold; where return does not justify the risk, the risk
   function challenges it and escalates what stays unresolved.
4. **The tail and the path decide outcomes.** Mandates end on drawdowns and stress, not on average days. Positions are
   sized so the strategy survives the paths that end mandates, not only the average path.
5. **Liquidity is part of the promise.** A fund that offers daily dealing on assets that take weeks to sell has made a
   promise. Asset liquidity is matched to the calls the portfolio can face under stress, redemptions and margin among
   them, not in calm markets.
6. **Portfolios don't net.** Clients' money in one portfolio never offsets another's. Across portfolios the firm
   measures its footprint (concentration, liquidity, crowding) and never takes diversification credit.
7. **Stable over precise.** Portfolio managers act on changes in risk. A measure that jitters loses their trust faster
   than one that is slightly off, so a change must come from markets or positions, not from sampling noise.
8. **Every model is wrong in a known direction.** History is a prior, not a forecast. A risk function states which
   assumptions bind and which way they err, and covers the rest with stress and reverse stress: what would break this
   mandate?

## Purpose: transparency for three decisions
Sight serves decisions, and an investment has three moments:

| | Decision | What risk provides |
|---|---|---|
| Before | **Construct** | What-ifs and marginal risk inside the investment process, before the trade: what this position adds, and what it crowds out of the budget |
| During | **Oversee** | Risk against budgets and limits, monitored daily, with escalation to the head of risk and the risk committee |
| After | **Assess** | Attribution that splits return by source, beta included; persistence over several periods as evidence of skill rather than luck; and return per unit of risk by bet and by manager |

Risk is independent of the investment teams but works inside their process. Challenge comes from understanding the
strategy well enough to say "yes, and size it like this", not only "no".

## Practice: transparency in three dimensions
The three dimensions describe what every piece of risk work must provide. They cut across the
[three pillars](01-investment-risk.md#the-three-pillars), which organise the recurring work: market, liquidity and
performance risk each condense, drill in and connect.

| | Dimension | The question it answers |
|---|---|---|
| 1 | **Condensation** (summarise) | What are we exposed to, and how much could we lose against the mandate? |
| 2 | **Drill-in** (decompose) | Where do risk and return come from, and were they intended? |
| 3 | **Connection** (over time) | Is the risk we take paid for by the return we earn? |

All of it assumes the basics: data checked before use, models tested against outcomes, results reproducible. [Risk
data](03-risk-data.md) sets out how the first and the last are made true.

### 1. Condensation
**Millions of numbers become a few that people can act on, without losing what matters.** The summaries come in three
families, and a portfolio needs all three: **risk** (what it could do, with probability and dependence folded in,
keeping the tail, joint extremes and nonlinearity, and the worst it has already done), **exposure** (what it is
sensitive to, factor by factor) and **liquidity** (what it could raise, how fast and at what cost, against what
investors could take out).

| Measure | Family | What it condenses |
|---|---|---|
| Ex-ante tracking error | Risk, active | How far the portfolio can drift from its benchmark |
| Active share | Exposure, active | How different the holdings are from the benchmark's |
| VaR, expected shortfall, maximum drawdown | Risk, absolute | The loss on a bad day, the average beyond it, and the worst peak-to-trough fall |
| Equity beta, duration, duration times spread | Exposure | Sensitivity to the equity market, to rates and to credit spreads, scaled by the spread itself |
| Days to liquidate | Liquidity | How long it takes to sell the portfolio, or a stressed redemption's share of it, at a set share of daily volume |
| Redemption coverage | Liquidity | What it could raise against the calls on its cash under stress, redemptions first among them |

*It fails* when the summary hides what it should show, or moves for no reason. *The test:* the number moves when the
risk moves, and any other movement stays within a stated tolerance.

### 2. Drill-in
**Any number opens on demand, the pieces add up, and each piece has a decision-maker.**
- **Risk factor decomposition.** Tracking error split into factors (market, style, sector, country, currency, rates,
  spreads) and stock-specific risk. The shares sum to the whole: for instance, 55% sector bets, 25% currency, 20% stock
  selection (illustrative figures). A large share no one intended is belief 2 at work.
- **Performance attribution.** Active return split two ways: by decision, into allocation and selection, and by factor,
  into exposure × factor return plus the specific return.

The factor split uses the risk decomposition's factors and decision-makers, so the risk a bet takes and the return it
earns sit side by side. [Sources of return](02-sources-of-return.md) shows how a holding divides between top-down and
bottom-up, and its [method](../pillars/alpha-and-beta-method.md) joins the two splits. *It fails* when the parts do
not sum to the whole, or a residual nobody can explain is left over. *The test:* every decomposition reconciles,
within a stated tolerance.

### 3. Connection
**Exposure, risk and performance on one timeline, in one language.** Each is credible only through the others. This
dimension joins risk and return over time; the [integrated view](../pillars/integrated-view.md) links signals across
pillars.
- **Return per unit of risk:** the information ratio, by bet and by manager.
- **Risk budget against return, by source:** a bet that uses a large share of the budget and persistently earns
  nothing is challenged; the portfolio manager resizes it, cuts it or explains why it stays.
- **Forecast against outcome:** ex-ante tracking error against realised; days when losses exceeded VaR against the
  number expected.
- **Drawdown against tolerance:** how close each portfolio runs to the loss, absolute or relative, that would end its
  mandate.

*It fails* when risk and performance come from different systems and cannot be reconciled. *The test:* any period's
return and any period's change in risk can be explained by the same factors and decision-makers.

### The firm view
Holdings are aggregated across all portfolios to see the firm's **footprint**: its share of an issue or of a market's
daily volume, its exposure to one counterparty, its weight in a crowded factor. These do not net (belief 6). They show
where the firm, not one portfolio, could be the one that cannot get out. The pillars compute the footprint and the
[integrated view](../pillars/integrated-view.md#the-firms-footprint) shows it.

## Boundaries
Numbers do not replace judgement; they tell judgement where to look. Some things they cannot settle: regime changes,
crowded exits, liquidity in a panic, the next crisis that history never showed. There the risk committee decides,
informed by stress and reverse stress, not replaced by them. Risks owned outside investment risk are managed elsewhere;
investment risk works with their owners at the edges named in [investment
risk](01-investment-risk.md#scope-and-boundaries).

## Sources
- Grinold, R. and Kahn, R. (2000). *Active Portfolio Management*, 2nd edition. McGraw-Hill. The information ratio,
  active risk and its allocation to bets.
- Litterman, R. (1996). Hot Spots and Hedges. *Journal of Portfolio Management*, special issue. Decomposing risk into
  contributions that sum to the whole, and marginal risk for decisions before the trade.
