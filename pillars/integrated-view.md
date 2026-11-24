# Integrated view

## The essentials
**The integrated view** asks where signals are combining across market, liquidity and performance risk, before any one
pillar would escalate.

**Oversee, every day:** the analytics engine reads the signals the three pillars already produce, applies rules for the
combinations that matter and triages the portfolios. The AI investigates each one and drafts an account. The risk
manager prioritises, judges whether the signals are connected, and adds the portfolio to the watch list or escalates it.

**Assess, after a period:** on a set cycle, and whenever market conditions call for it, the view reads performance
risk's split by strategy across all portfolios: whether each strategy's skill holds and, with the firm's footprint,
where the same skill runs through many portfolios. It informs the chief investment officer's decisions on strategy
capacity and the product range.

**Why it is needed:** the pillars are connected by nature: they read one portfolio, its holdings and its investors, so a
move in one travels to the others. A wrong call, top-down or bottom-up, or an exposure nobody chose, brings
underperformance; underperformance prompts redemptions; redemptions are met by selling the most liquid assets; and what
remains is more concentrated and more volatile. Read pillar by pillar, each signal looks moderate and no single workflow
escalates; read as one web, the cycle shows.

The rest of this chapter is the detail behind these points.

## What the view reads
The view reads every rule in each pillar's table: [market risk](market-risk.md#materiality-and-exceptions), [liquidity
risk](liquidity-risk.md#materiality-and-exceptions) and [performance
risk](performance-risk.md#materiality-and-exceptions). Every signal carries its pillar's state (exception, watch item or
within) and the date it was computed. The view computes no measure of its own: it takes the signals as the pillars
produce them, and never computes its own version. The daily run has seven steps:

| # | Step | Owner |
|---|---|---|
| 1 | Read every pillar's signals for every portfolio; align them by date | Analytics engine |
| 2 | Apply the pattern and combination rules; triage portfolios; run the analyses set for each one's pattern | Analytics engine |
| 3 | Follow up where the findings point further; draft an account | AI |
| 4 | Grounding check on every account | Analytics engine |
| 5 | Assemble the committee view from the top of the queue | Analytics engine |
| 6 | Prioritise and judge each portfolio in the queue; add it to the watch list or escalate it to the head of risk | Risk manager |
| 7 | Review and sign off the committee view | Head of risk |

## Patterns
A pattern is a named chain of signals across pillars that, together, describe a known way for a portfolio to get into
difficulty.

| Pattern | Chain of signals |
|---|---|
| Redemption spiral | Shortfall, at watch or significant → rising outflows → falling coverage → rising concentration |
| Hidden illiquidity | Stale or unpriceable holdings + volatility below its usual range; steady return as context |
| Concentrated and hard to sell | Rising issuer or sector concentration + rising time or cost to sell those holdings |
| Drift under pressure | Style drift or falling active share + rising outflows |
| Margin squeeze | Market loss or volatility above its range → rising margin and collateral calls → falling coverage; leverage as context |

**The redemption spiral** is the self-reinforcing cycle described at the top; outflows concentrated in a few
distributors can stand in for rising outflows. Because relative return is read every day over a rolling window, the
first link can appear at watch as soon as a shortfall forms, rather than only once it is significant. Its early links
are in performance and liquidity, its later links in market risk.

**Hidden illiquidity** is a combination in which one signal makes others look better than they are. Holdings whose
prices are stale do not move, so volatility looks low and returns look smooth. A portfolio in this pattern may show
normal market and performance readings because of, not despite, its liquidity signal.

**Concentrated and hard to sell** joins a rising concentration in market risk with a rising time or cost to sell those
same holdings in liquidity risk. Either alone may be acceptable; together they mean the portfolio holds more of
something that is becoming harder to sell.

**Drift under pressure** joins a performance signal about how the portfolio is managed, such as style drift or falling
active share, with investors leaving. The combination suggests the portfolio may be changing in response to outflows or
underperformance rather than to its mandate, which is a question for the portfolio manager.

**The margin squeeze** is the leveraged counterpart of the redemption spiral. A fall in markets brings margin and
collateral calls; the collateral posted is encumbered and can no longer be sold; coverage falls; and the portfolio is
left to sell what it still can, at stressed prices, which can bring further losses and further calls. It is the case in
which market risk moves first, and its links follow within days rather than quarters.

The view weights early signals, because by the time market risk readings rise the cycle is usually under way.

## Combination rules and triage
The rules that decide which portfolios enter the view, and in what order, are [governed
parameters](../framework/08-controls.md#materiality-thresholds-as-governed-parameters). **The rules below are
illustrative kinds of rule, not recommendations;** each risk function sets its own.

| Kind of rule | Example (illustrative) |
|---|---|
| Pattern match | A portfolio enters the view if every signal a named pattern requires is at watch or exception |
| Breadth | A portfolio enters the view if it has signals at watch or exception in at least two pillars |
| Ordering | Pattern matches first, then more exceptions, then more pillars at watch, then signals held for longer |
| Grouping | Signals that share one underlying driver count once |

A pattern may also show signals as context that it does not require, such as the steady return in hidden illiquidity;
context signals can be within. A portfolio with an exception in one pillar and nothing elsewhere does not enter the
view. Its exception is handled by that pillar's workflow, as it would be anyway; the view is for combinations.

For each portfolio in the view the analytics engine runs the analyses set for its pattern, which are governed parameters
drawn from the pillars' governed analyses: for example, how the portfolio's weights have moved by time to sell, the
same pattern in other portfolios, and the earlier accounts of the portfolio. The view adds no analysis of its own.

**Avoiding double counting.** One driver can show in two pillars, as issuer concentration and a rising time to sell the
same holdings, or as margin calls and the fall in coverage they cause. Signals that share a driver are grouped and count
once for breadth; investor concentration is a separate driver. The groups are governed rules, and a pattern such as
*concentrated and hard to sell* still names the combination.

## The firm's footprint
Portfolios do not net, so the firm's footprint is read across them rather than counted in any one of them. The pillars
compute it: [market risk](market-risk.md#workflows-in-this-pillar) the firm's totals by issuer, counterparty and factor,
[liquidity risk](liquidity-risk.md#workflows-in-this-pillar) its share of each issue and of each market's daily volume.
The view lists the readings above a governed threshold, largest first, beside the portfolios in the view. Each portfolio
involved shows the reading as context only: it does not count towards the portfolio's place in the view, because one
reading could otherwise bring many portfolios into it at once.

## What the firm is paid for
On a set cycle, annual by default, and whenever market conditions call for it, such as a change of regime, a crowded
reversal in a style premium or a sharp change in a strategy's results, the view reads [performance
risk](performance-risk.md)'s split of return by strategy across all portfolios. The reading is unweighted, so that a
small strategy with lasting skill is as visible as a large one. It shows how much of each strategy's return is beta that
an index fund or a future could have delivered and how much is skill; whether that skill holds, read through performance
risk's [significance tests](performance-risk.md#windows-and-significance) over successive periods; and, with the firm's
footprint, where the same skill runs through many portfolios and would fail in all of them at once. The view computes
nothing new. The reading informs the chief investment officer's decisions on strategy capacity and the product range; it
is not a measure of the firm's business, and the decisions are not the risk function's.

## What the AI drafts
Every number in the draft appears in the facts beside it, so the [grounding
check](../framework/08-controls.md#the-grounding-check) would pass. The account describes the combination; it does not
claim that one signal caused another, and the grounding check rejects a causal claim no analysis computed. **The fund
and figures are illustrative.**

| Fact | Value |
|---|---|
| Fund | Fund K |
| Pattern matched | Redemption spiral |
| Shortfall against benchmark, last 12 months | 4.6%, significant against tracking error (performance, exception) |
| Net outflows, last month | 3.2% of net assets, near the top of the usual range (liquidity, watch) |
| Redemption coverage, today / three months ago | 1.8x / 2.6x (liquidity, watch) |
| Largest issuer weight, today / three months ago | 9.3% / 6.1% (market, watch) |
| Holdings that take more than 5 days to sell, today / three months ago (run 1) | 31% / 22% of net assets |

> Fund K matches the redemption spiral pattern. It is 4.6% below its benchmark over the last 12 months, a significant
> shortfall. At the same time, net outflows last month were 3.2% of net assets, near the top of the portfolio's usual
> range; redemption coverage has fallen from 2.6x to 1.8x over three months; and its largest issuer weight has risen
> from 6.1% to 9.3%. Over the same three months, holdings that take more than 5 days to sell have risen from 22% to 31%
> of net assets (run 1). Only the performance signal is at exception; the liquidity and market signals are at watch.

## Limits of the view
The view inherits every limit of the pillar measures it reads, and adds four of its own.

- **Co-occurrence is not cause.** Signals that appear together may be unrelated. The view shows that they combine; the
  risk manager judges whether they are connected. The analyses set for a pattern give evidence either way; they do not
  settle it.
- **Patterns encode judgement.** The rules catch the combinations someone has defined and miss those nobody has.
- **Signals have different cadences.** Most signals are read daily, including relative return over its rolling window,
  but runs of periods are counted in whole periods and some inputs, such as investor registers, update less often. The
  view shows each signal's as-of date and treats a signal beyond a set age as stale.
- **Too many portfolios in the view defeats the purpose.** If the view picks up most portfolios, it becomes another
  report. The share of portfolios in the view the risk manager judges worth action is watched, and the rules are
  tightened when it falls.

The function tests the view by replaying past episodes: taking portfolios that ran into difficulty and checking whether
the view, with the rules in force at the time, would have picked them up, and how much earlier than any pillar. Episodes
it would have missed are the main source of new patterns. The AI step is tested, as in the pillars, through the risk
manager's edits to the accounts, a sample reviewed against the signals and runs behind them, and seeded accounts, as
[evaluation](../framework/08-controls.md#evaluation) sets out.

## Controls and measures specific to the view
The general [controls](../framework/08-controls.md) apply in full. The view adds four.

- **Every signal shows its pillar and as-of date.** Nothing in an account is shown without its source.
- **Missing data is not health.** A portfolio with missing signals from a pillar is shown as partly assessed, never as
  healthy.
- **The view never overrides a pillar.** A pillar's exception still goes through that pillar's workflow, whether or not
  the view picks up the portfolio, and actions the view raises route back to the pillar that owns them. The view holds
  no actions of its own.
- **Pattern and grouping rules are governed.** Adding, removing or changing a pattern or a driver group is recorded like
  any other threshold change.

The view's own measure, **lead time**, matters most here, ahead of the [four
dimensions](../framework/07-redesign-method.md#four-dimensions) a redesigned workflow is measured on. It is measured
from replays of past episodes and from live cases.

| Dimension | Measure for the view |
|---|---|
| View-specific | Lead time: days between the view picking up a portfolio and the first single-pillar escalation |
| Speed | Time from a combination forming to the risk manager seeing it |
| Capacity | Portfolios covered by the integrated view |
| Quality | Combinations first seen through a pillar escalation rather than through the view |
| Influence | Portfolios in the view discussed by the committee, and actions taken |

## Ownership
The risk function owns the view: its patterns, its grouping of drivers, its triage rules and its footprint thresholds.
The risk committee reads the portfolios at the top of the queue in the [shared
record](../framework/05-principles.md#7-hand-over-judgement-not-documents), each with its account and the signals behind
it, and the firm's footprint, and receives a decision paper for what the firm should do, which it decides. The reading
of what the firm is paid for goes to the chief investment officer, who decides.

## Sources
- Chen, Q., Goldstein, I. and Jiang, W. (2010). Payoff Complementarities and Financial Fragility: Evidence from Mutual
  Fund Outflows. *Journal of Financial Economics*. Poor performance, outflows and the cost to investors who stay.
- Brunnermeier, M. and Pedersen, L. (2009). Market Liquidity and Funding Liquidity. *Review of Financial Studies*.
  Spirals in which losses, margin calls and falling liquidity reinforce each other.
