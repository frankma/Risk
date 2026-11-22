# Philosophy

## The essentials
An asset manager earns its return through two kinds of investment decision: top-down views and bottom-up selection. A
risk function exists to **challenge** those decisions against the mandate, while **serving** the investment team with
insight into the risks it takes.

**The system does the work; people judge:** the system has two parts, the analytics engine, which computes, and the AI,
which investigates iteratively with it and drafts. People prioritise, check, challenge, decide and are accountable. The
AI adds breadth and depth, never a figure or a rule of its own, and weaves the signals into one integrated web.

**At its root, risk work is insight:** the few numbers, out of millions, that show where each portfolio stands against
its mandate and what to challenge.

**What guides the work:** eight beliefs settle what the rules leave open; the two purposes meet in three decisions
(construct, oversee, assess); and every piece of the work condenses, drills in and connects. No model is assumed; every
model is judged against these.

The rest of this chapter is the detail behind these points.

## Why a risk function exists
- **Challenge.** An independent test, for the firm's governance and its clients, of whether the investment decisions in
  every portfolio take the risks its mandate intends, in the size it can bear. Where they do not, the function
  challenges them, and escalates what stays unresolved.
- **Serve.** Insight into the risks the investment team takes, brought to its decisions: what could happen, what each
  position adds and whether the risk is paid for, before and after the trade. It comes from understanding the strategy
  well enough to say "yes, and size it like this", not only "no".

Both rest on the same measures. Challenge escalates, service informs, and the portfolio manager decides what to hold.
Independence is what makes the service credible, and it rests on the decisions only the risk function may make, which
[decision rights](10-decision-rights.md) sets out. The two purposes meet in three decisions:

| | Decision | Purpose | What risk provides |
|---|---|---|---|
| Before | **Construct** | Serve | What-ifs and marginal risk before the trade, on analyses the risk function owns and anyone can trace: what this position adds to risk and to time to sell, and what it crowds out of the budget |
| During | **Oversee** | Challenge | Risk against budgets and limits, monitored daily, with escalation to the head of risk and the risk committee |
| After | **Assess** | Serve | Attribution after the period, on analyses the risk function owns, at any level from a single bet to the whole firm: return split by source, beta included; significance over several periods as evidence of skill rather than luck; and return per unit of risk |

## How the work is done
**Decisions, not departments.** A risk function is defined by the decisions it must make, not by titles, teams or who
does the work: what counts as an exception, whether a reading matters, what to challenge and what to escalate. Each
decision has a named holder, independent of the investment line; who does the work, and how it is organised, is for
each firm to decide, as [decision rights](10-decision-rights.md) sets out.

**The system does the work; people judge.** The system has two parts, the analytics engine and the AI. The analytics
engine computes every figure for every portfolio every day. The AI investigates like an analyst, working iteratively
with the analytics engine: it reads the findings, chooses the next analysis from a governed list, runs it through the
analytics engine and reads the result, until the picture holds. Only then does it draft, and only then does a person see
it: they weigh it against the rest of the queue, check it against the facts, challenge it and decide, and are
accountable for the decision. Every workflow is designed this way from the start. The AI adds breadth and depth, never a
figure or a rule of its own: it takes on, for every item, the small steps of reading, connecting and following up that
were never worth a person's time, and weaves them into one integrated web of signals, as [working with
AI](06-working-with-ai.md) sets out.

## Beliefs
Each is a position a reasonable firm could reject. Together they decide what the rules do not.

1. **The mandate defines the risk.** Appetite belongs to the client, expressed as a benchmark, a tracking error budget,
   guidelines and liquidity terms, not a firm-wide number. The capital at risk is the clients', not the firm's.
2. **Intended risk is the product; unintended risk is the hazard.** Clients pay for the bets the investment team means
   to take. The first job is to find the ones nobody chose: a value tilt in a growth portfolio, a rates bet in a credit
   portfolio, a crowded factor riding along with stock picks.
3. **Risk must earn its place.** Every unit of active risk should be paid for by expected return.
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

## What every piece of risk work provides
The three apply in every pillar. All of it assumes the basics: data checked before use,
models tested against outcomes, results reproducible, as [risk data](03-risk-data.md) sets out.

| | Dimension | The question it answers |
|---|---|---|
| 1 | **Condensation** (summarise) | What are we exposed to, and how much could we lose against the mandate? |
| 2 | **Drill-in** (decompose) | Where do risk and return come from, and were they intended? |
| 3 | **Connection** (over time) | Is the risk we take paid for by the return we earn? |

The analytics engine provides all three for every portfolio; the AI makes them readable and answers questions on demand,
so drill-in is open to anyone entitled to the portfolio.

### 1. Condensation
**Millions of numbers become a few that people can act on, without losing what matters.** A portfolio needs summaries in
three families: risk, exposure and liquidity.

| Measure | Family |
|---|---|
| Ex-ante tracking error | Risk, active |
| Active share | Exposure, active |
| VaR, expected shortfall, maximum drawdown | Risk, absolute |
| Equity beta, duration, duration times spread | Exposure |
| Days to liquidate | Liquidity |
| Redemption coverage | Liquidity |

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
earns sit side by side. [How return is earned](01-sources-of-return.md) shows how a holding divides between top-down and
bottom-up, and its [method](../pillars/alpha-and-beta-method.md) joins the two splits. *It fails* when the parts do not
sum to the whole, or a residual nobody can explain is left over. *The test:* every decomposition reconciles, within a
stated tolerance.

### 3. Connection
**Exposure, risk and performance on one timeline, in one language.** Each is credible only through the others. The links
are return per unit of risk, by bet and by manager; the [risk
budget](../pillars/market-risk.md#workflows-in-this-pillar) against return; each forecast against its [realised
counterpart](02-investment-risk.md#the-three-pillars); and drawdown against tolerance.

*It fails* when risk and performance come from different systems and cannot be reconciled. *The test:* any period's
return and any period's change in risk can be explained by the same factors and decision-makers.

### The firm view
Portfolios don't net (belief 6), so the firm's footprint across them is read on its own, as the [integrated
view](../pillars/integrated-view.md#the-firms-footprint) sets out.

## Boundaries
Neither the numbers nor the AI replace judgement; they tell it where to look. Some things they cannot settle: regime
changes, crowded exits, liquidity in a panic, the next crisis that history never showed. There the risk committee
decides, informed by stress and reverse stress, not replaced by them.

## Sources
- Fama, E. and Jensen, M. (1983). Separation of Ownership and Control. *Journal of Law and Economics*. Separating the
  management of decisions from their control, which defines a function by the decisions it holds.
- Grinold, R. and Kahn, R. (2000). *Active Portfolio Management*, 2nd edition. McGraw-Hill. The information ratio,
  active risk and its allocation to bets.
- Litterman, R. (1996). Hot Spots and Hedges. *Journal of Portfolio Management*, special issue. Decomposing risk into
  contributions that sum to the whole, and marginal risk for decisions before the trade.
