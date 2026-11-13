# Integrated view

## In short
**The question:** where are signals combining across market, liquidity and performance risk, before any one pillar would
escalate?

**The outcome:**

> The risk function knows which portfolios have signals combining across pillars, and why, before any one pillar would
> escalate them.

**How the work is done:** the view computes nothing new. The risk engine reads the signals the three pillars already
produce, for every portfolio every day, applies rules for the combinations that matter and ranks the portfolios. The AI
drafts an account of each ranked portfolio. The risk manager judges each one and adds it to the watch list or escalates
it.

| # | Step | Owner |
|---|---|---|
| 1 | Read every pillar's signals for every portfolio; align them by date | Risk engine |
| 2 | Apply the pattern and combination rules; rank portfolios | Risk engine |
| 3 | Draft an account for each ranked portfolio | AI assistant |
| 4 | Grounding check on every account | Risk engine |
| 5 | Assemble the committee view from the top-ranked portfolios | Risk engine |
| 6 | Judge each ranked portfolio; add it to the watch list or escalate | Risk manager |
| 7 | Review and sign off the committee view | Head of risk |

**Why it is needed:** the episodes that do most damage pass through all three pillars. Underperformance prompts
redemptions, redemptions are met by selling the most liquid assets, and the portfolio that remains is more concentrated
and more volatile, which makes further underperformance more likely. Each pillar sees its own signal as moderate, so no
single threshold is breached and no single workflow escalates. Watching every signal for every portfolio every day is
something a manual process cannot do ([principle
6](../framework/05-principles.md#6-new-capabilities-beat-faster-old-ones)).

The rest of this chapter is the detail behind these points.

## What the view reads
The view reads each pillar's signals for each portfolio. Every signal carries a state and the date it was computed. The
states are the ones each pillar chapter assigns to its rules:

- **Exception:** the reading has crossed a limit or another rule's threshold, such as a limit breach, a fired trigger or
  a significant shortfall.
- **Watch:** the reading is approaching one: it is above an early warning, is drifting towards a threshold, or is a
  shortfall that is not yet significant.
- **Normal:** neither.

The signals, each defined in its pillar chapter's rules:

- **[Market risk](market-risk.md#materiality-and-exceptions):** limit utilisation; change since the previous day;
  readings against the portfolio's own history, including volatility; issuer or sector concentration; headroom against
  drawdown tolerance; ex-ante tracking error; risk budget; counterparty exposure.
- **[Liquidity risk](liquidity-risk.md#materiality-and-exceptions):** redemption coverage; large redemptions; margin and
  collateral calls; flows against history; investor and distributor concentration; time and cost to liquidate; stale or
  unpriceable holdings.
- **[Performance risk](performance-risk.md#materiality-and-exceptions):** relative return over the rolling window;
  significance of shortfall; ex-post tracking error; realised drawdown; active share; source of return; style
  consistency; overdue actions.

The view takes these signals as the pillars produce them. If a pillar changes how a signal is computed, the view changes
with it; the view never computes its own version.

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

Signals do not move together. Performance and flows usually move first, because they respond to outcomes; liquidity and
market risk move later, because they respond to the selling that follows. A sharp market loss is the exception: there,
market risk moves first and performance follows. The view gives weight to the early signals for that reason: by the time
market risk readings rise, the cycle is usually under way.

## Combination rules and ranking
The rules that decide which portfolios rank, and in what order, are [governed
parameters](../framework/08-controls.md#materiality-thresholds-as-governed-parameters). **The rules below are
illustrative kinds of rule, not recommendations;** each risk function sets its own.

| Kind of rule | Example (illustrative) |
|---|---|
| Pattern match | A portfolio ranks if every signal a named pattern requires is at watch or exception |
| Breadth | A portfolio ranks if it has signals at watch or exception in at least two pillars |
| Ordering | Pattern matches first, then more exceptions, then more pillars at watch, then longer persistence |
| Grouping | Signals that share one underlying driver count once |

A pattern may also show signals as context that it does not require, such as the steady return in hidden illiquidity;
context signals can be normal. A portfolio with an exception in one pillar and nothing elsewhere does not rank in the
view. Its exception is handled by that pillar's workflow, as it would be anyway; the view is for combinations.

**Avoiding double counting.** One underlying driver can appear in two pillars. Concentration in a few holdings shows as
issuer concentration in market risk, and, because those holdings take longer to sell, as a rising time to liquidate in
liquidity risk. Counted twice, it would make a portfolio look as if two pillars were elevated when there is one driver.
The view groups signals that share a driver and counts the group once for breadth. The groups are part of the governed
rules: concentration in market risk and the time to sell the same holdings form one group, as do margin and collateral
calls and the fall in coverage they cause, while investor concentration, which concerns who owns the portfolio rather
than what it holds, is a separate driver. The pattern *concentrated and hard to sell* still names the combination, so
that it is seen, but it does not count as two pillars.

## The firm's footprint
Portfolios do not net, so the firm's footprint is read across them rather than ranked within them. The pillars compute
it: [market risk](market-risk.md#workflows-in-this-pillar) the firm's totals by issuer, counterparty and factor,
[liquidity risk](liquidity-risk.md#workflows-in-this-pillar) its share of each issue and of each market's daily volume.
The view lists the readings above a governed threshold, largest first, beside the ranked portfolios. Each portfolio
involved shows the reading as context only: it does not count towards the portfolio's rank, because one reading could
otherwise rank many portfolios at once.

## What the AI drafts
The AI drafts each portfolio's account from the signals and facts the view read, and from nothing else. Every number in
the draft appears in the facts beside it, so the [grounding check](../framework/08-controls.md#the-grounding-check)
would pass. The account describes the combination; it does not recommend an action or claim that one signal caused
another. **The fund and figures are illustrative.**

| Fact | Value |
|---|---|
| Fund | Fund K |
| Pattern matched | Redemption spiral |
| Shortfall against benchmark, last 12 months | 4.6%, significant against tracking error (performance, exception) |
| Net outflows, last month | 3.2% of net assets, near the top of the usual range (liquidity, watch) |
| Redemption coverage, today / three months ago | 1.8x / 2.6x (liquidity, watch) |
| Largest issuer weight, today / three months ago | 9.3% / 6.1% (market, watch) |

> Fund K matches the redemption spiral pattern. It is 4.6% below its benchmark over the last 12 months, a significant
> shortfall. At the same time, net outflows last month were 3.2% of net assets, near the top of the portfolio's usual
> range; redemption coverage has fallen from 2.6x to 1.8x over three months; and its largest issuer weight has risen
> from 6.1% to 9.3%. Only the performance signal is at exception; the liquidity and market signals are at watch.

## Limits of the view
The view inherits every limit of the pillar measures it reads, and adds four of its own.

- **Co-occurrence is not cause.** Signals that appear together may be unrelated. The view shows that they combine; the
  risk manager judges whether they are connected.
- **Patterns encode judgement.** The rules catch the combinations someone has defined and miss those nobody has.
- **Signals have different cadences.** Most signals are read daily, including relative return over its rolling window,
  but runs of periods are counted in whole periods and some inputs, such as investor registers, update less often. The
  view shows each signal's as-of date and treats a signal beyond a set age as stale.
- **Too many ranked portfolios defeats the purpose.** If the view ranks most portfolios, it becomes another report. The
  share of ranked portfolios the risk manager judges worth action is watched, and the rules are tightened when it falls.

The function tests the view by replaying past episodes: taking portfolios that ran into difficulty and checking whether
the view, with the rules in force at the time, would have ranked them, and how much earlier than any pillar. Episodes it
would have missed are the main source of new patterns. The AI step is tested, as in the pillars, through the risk
manager's edits to the accounts.

## Controls and measures specific to the view
The general [controls](../framework/08-controls.md) apply in full. The view adds four.

- **Every signal shows its pillar and as-of date.** Nothing in an account is shown without its source.
- **Missing data is not health.** A portfolio with missing signals from a pillar is shown as partly assessed, never as
  healthy.
- **The view never overrides a pillar.** A pillar's exception still goes through that pillar's workflow, whether or not
  the view ranks the portfolio.
- **Pattern and grouping rules are governed.** Adding, removing or changing a pattern or a driver group is recorded like
  any other threshold change.

The measure that matters most for the view is **lead time**: how much earlier the view ranked a portfolio than the first
escalation from any single pillar. Lead time is measured from replays of past episodes and from live cases. The other
dimensions come from [measuring value](../framework/09-measuring-value.md).

| Dimension | Measure for the view |
|---|---|
| Lead time | Days between the view ranking a portfolio and the first single-pillar escalation |
| Speed | Time from a combination forming to the risk manager seeing it |
| Capacity | Portfolios covered by the integrated view: every one, against those one person recalls |
| Quality | Combinations first seen through a pillar escalation rather than through the view |
| Influence | Ranked portfolios discussed by the committee, and actions taken |

## Ownership and connections
The risk function owns the view: its patterns, its grouping of drivers, its ranking rules and its footprint thresholds.
Risk managers judge the ranked portfolios as they appear and add them to the watch list, which the risk function owns,
or escalate them. The risk committee sees the top-ranked portfolios, each with its account and the signals behind it,
and the firm's footprint, and decides what the firm should do.

Actions route back to the workflows that own them. A question about liquidity goes to the [liquidity
risk](liquidity-risk.md) workflows, a challenge to the portfolio manager goes into the next review in [performance
risk](performance-risk.md), and a concentration issue is followed in [market risk](market-risk.md). The view does not
hold actions of its own; it shows where the pillars' signals combine, and the pillars do the work.

## Sources
- Chen, Q., Goldstein, I. and Jiang, W. (2010). Payoff Complementarities and Financial Fragility: Evidence from Mutual
  Fund Outflows. *Journal of Financial Economics*. Poor performance, outflows and the cost to investors who stay.
- Brunnermeier, M. and Pedersen, L. (2009). Market Liquidity and Funding Liquidity. *Review of Financial Studies*.
  Spirals in which losses, margin calls and falling liquidity reinforce each other.
