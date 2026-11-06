# Integrated view

The integrated view ranks funds where signals across market, liquidity and performance risk are combining, so that the
risk function sees a developing problem before any one pillar would escalate it. It computes nothing new: it
reads the signals the three pillar chapters already define, applies rules for the combinations that matter, and puts
the funds where those combinations appear in front of a human with an account of what is happening.

## Why an integrated view
The episodes that do most damage to a fund pass through all three pillars. Underperformance prompts redemptions.
Redemptions are met by selling the most liquid assets first. The portfolio that remains is more concentrated and more
volatile, which makes further underperformance more likely, and the cycle repeats.

A manual process tends to see this late. Each pillar is reviewed on its own cycle, often by different people, and each
sees its own signal as moderate: a performance shortfall that is not yet severe, outflows that are higher than usual but
within coverage, concentration that is rising but below its limit. No single threshold is breached, so no single
workflow escalates.

The view's outcome:

> The risk function knows which funds have signals combining across pillars, and why, before any one pillar would
> escalate them.

This is the framework's clearest example of [principle
6](../framework/01-principles.md#6-new-capabilities-beat-faster-old-ones). The manual process cannot watch every signal
for every fund every day and connect them.

## What the view reads
The view reads each pillar's signals for each fund. Every signal carries a state and the date it was computed. The
states are the ones each pillar chapter assigns to its rules:

- **Exception:** the pillar's rule has fired, such as a limit breach, a fired trigger or a persistent shortfall.
- **Watch:** the reading is moving towards a threshold, such as an early warning, a reading drifting towards a
  threshold, or a shortfall that is not yet persistent.
- **Normal:** neither.

The signals, each defined in its pillar chapter's rules:

- **[Market risk](market-risk.md#materiality-and-exceptions):** limit utilisation; change since the previous day;
  readings against the fund's own history, including volatility; issuer or sector concentration; drawdown against
  tolerance; counterparty exposure.
- **[Liquidity risk](liquidity-risk.md#materiality-and-exceptions):** redemption coverage; large redemptions; flows
  against history; investor and distributor concentration; time and cost to liquidate; stale or unpriceable holdings.
- **[Performance risk](performance-risk.md#materiality-and-exceptions):** relative return; persistence of shortfall;
  tracking error; active share; risk budget; source of return; style consistency; overdue actions.

The view takes these signals as the pillars produce them and never computes its own version.

## Patterns
A pattern is a named chain of signals across pillars that, together, describe a known way for a fund to get into
difficulty.

| Pattern | Chain of signals |
|---|---|
| Redemption spiral | Persistent shortfall → rising outflows → falling coverage → rising concentration |
| Hidden illiquidity | Stale or unpriceable holdings + volatility below its usual range; steady return as context |
| Concentrated and hard to sell | Rising issuer or sector concentration + rising time or cost to sell those holdings |
| Drift under pressure | Style drift or falling active share + rising outflows |

**The redemption spiral** is the self-reinforcing cycle set out above; outflows concentrated in a few distributors
can stand in for rising outflows. Its early links are in performance and liquidity, its later links in market risk.

**Hidden illiquidity** is a combination in which one signal makes others look better than they are. Holdings whose
prices are stale do not move, so volatility looks low and returns look smooth. A fund in this pattern may show normal
market and performance readings because of, not despite, its liquidity signal.

**Concentrated and hard to sell** joins a rising concentration in market risk with a rising time or cost to sell those
same holdings in liquidity risk. Either alone may be acceptable; together they mean the fund holds more of something
that is becoming harder to sell.

**Drift under pressure** joins a performance signal about how the fund is managed, such as style drift or falling
active share, with investors leaving. The combination suggests the portfolio may be changing in response to outflows
or underperformance rather than to its mandate, which is a question for the portfolio manager.

Signals do not move together. Performance and flows usually move first, because they respond to outcomes; liquidity
and market risk move later, because they respond to the selling that follows. A sharp market loss is the exception:
there, market risk moves first and performance follows. The view gives weight to the early signals for that reason:
by the time market risk readings rise, the cycle is usually under way.

## Flagship redesign: the fund health review
The example below follows the fund health review for a range of 40 funds and a monthly risk committee. **The steps,
hours and elapsed times are illustrative.**

**Current state.** There is no integrated view. Before each committee, the head of risk assembles one by reading the
three pillars' outputs and connecting them from memory and experience.

| # | Step | Tag | Hours | Elapsed |
|---|---|---|---|---|
| 1 | Read the latest outputs of the three pillars | Gather | 3 | 2 days |
| 2 | Pull more data for the funds that look worrying | Gather | 2 | 1 day |
| 3 | Connect signals across pillars from memory and experience | Interpret | 3 | 1 day |
| 4 | Decide which funds to raise with the committee | Judge | 1 | 1 day |
| 5 | Write the committee note | Communicate | 3 | 2 days |
| 6 | Review and sign off the note | Approve / Wait | 1 | 2 days |

The review takes 13 hours and 9 working days each month. It happens on the committee's cycle, so a combination that
forms just after one committee is not seen until the next. It depends on one person, and it covers the funds that
person thinks of, which with 40 funds is rarely all of them.

**Owner assignment.**

- Steps 1 and 2 move to code, which reads every pillar's signals for every fund each day, rather than one person
  reading reports for the funds they recall.
- Step 3 is split. Code aligns the signals by date, applies the pattern rules and ranks the funds, which is
  computation; the AI drafts an account for each ranked fund that connects its signals, which is interpretation.
- Step 4 stays with a human. The risk manager judges each ranked fund as it appears and decides whether it goes on the
  fund watch list or is escalated.
- Step 5 is eliminated. Code assembles what the committee sees from the ranked funds, their accounts and the signals
  behind them.
- Step 6 stays with the head of risk.

**Redesigned flow.** Hours are per month. Step 6 assumes eight accounts reviewed in the month at a quarter of an hour
each.

| # | Step | Owner | Hours | Elapsed |
|---|---|---|---|---|
| 1 | Read every pillar's signals for every fund; align them by date | Code | 0 | Daily |
| 2 | Apply the pattern and combination rules; rank funds | Code | 0 | Daily |
| 3 | Draft an account for each ranked fund | AI | 0 | Daily |
| 4 | Grounding check on every account | Code | 0 | Daily |
| 5 | Assemble the committee view from the top-ranked funds | Code | 0 | Minutes |
| 6 | Judge each ranked fund; add it to the fund watch list or escalate | Risk manager | 2 | Same day |
| 7 | Review and sign off the committee view | Head of risk | 1 | 1 day |

The work falls to 3 hours a month. A combination is seen on the day it forms, by the risk manager, rather than at the
next committee, and the committee view is signed off in 1 working day instead of 9.

**The shift.** The integrated picture moves from one assembled occasionally by one person, for the funds they think
of, to one maintained continuously for every fund.

## Combination rules and ranking
The rules that decide which funds rank, and in what order, are
[governed parameters](../framework/04-controls.md#materiality-thresholds-as-governed-parameters). **The rules below are
illustrative kinds of rule, not recommendations;** each risk function sets its own.

| Kind of rule | Example (illustrative) |
|---|---|
| Pattern match | A fund ranks if every signal a named pattern requires is at watch or exception |
| Breadth | A fund ranks if it has signals at watch or exception in at least two pillars |
| Ordering | Pattern matches first, then more exceptions, then more pillars at watch, then longer persistence |
| Grouping | Signals that share one underlying driver count once |

A pattern may also show signals as context that it does not require, such as the steady return in hidden
illiquidity; context signals can be normal. A fund with an exception in one pillar and nothing elsewhere does not rank
in the view. Its exception is handled by that pillar's workflow, as it would be anyway; the view is for combinations.

**Avoiding double counting.** One underlying driver can appear in two pillars. Concentration in a few holdings shows as
issuer concentration in market risk, and, because those holdings take longer to sell, as a rising time to liquidate in
liquidity risk. The view groups signals that share a driver and counts the group once for breadth. The groups are part
of the governed rules: concentration in market risk and the time to sell the same holdings form one group, while
investor concentration, which concerns who owns the fund rather than what it holds, is a separate driver. The pattern
*concentrated and hard to sell* still names the combination, so that it is seen, but it does not count as two pillars.

## The firm's footprint
Funds do not net, so the firm's footprint is read across them rather than ranked within them. The pillars compute it:
[market risk](market-risk.md#workflows-in-this-pillar) the firm's totals by issuer, counterparty and factor, [liquidity
risk](liquidity-risk.md#workflows-in-this-pillar) its share of each issue and of each market's daily volume. The view
lists the readings above a governed threshold, largest first, beside the ranked funds. Each fund involved shows the
reading as context only: it does not count towards the fund's rank, because one reading could otherwise rank many funds
at once.

## What the AI drafts
The AI drafts each fund's account from the signals and facts the view read, and from nothing else. Every number in
each draft appears in the facts beside it, so the
[grounding check](../framework/04-controls.md#the-grounding-check) would pass. The account describes the combination;
it does not recommend an action or claim that one signal caused another. **The funds and figures are illustrative.**

**A redemption spiral forming.**

| Fact | Value |
|---|---|
| Fund | Fund K |
| Pattern matched | Redemption spiral |
| Shortfall against benchmark | 4 consecutive quarters (performance, exception) |
| Net outflows, last month | 3.2% of net assets, near the top of the usual range (liquidity, watch) |
| Redemption coverage, today / three months ago | 1.8x / 2.6x (liquidity, watch) |
| Largest issuer weight, today / three months ago | 9.3% / 6.1% (market, watch) |

> Fund K matches the redemption spiral pattern. It has been below its benchmark for 4 consecutive quarters. At the
> same time, net outflows last month were 3.2% of net assets, near the top of the fund's usual range; redemption
> coverage has fallen from 2.6x to 1.8x over three months; and its largest issuer weight has risen from 6.1% to
> 9.3%. Only the performance signal is at exception; the liquidity and market signals are at watch.

**Hidden illiquidity.**

| Fact | Value |
|---|---|
| Fund | Fund L |
| Pattern matched | Hidden illiquidity |
| Stale or unpriceable holdings | 12% of net assets (liquidity, exception) |
| Volatility, today / usual range | 4.1% / 6% to 9% (market, exception) |
| Return against benchmark, last 12 months | +1.9% (performance, normal; context) |
| Measures using the flagged prices | Volatility; relative return |

> Fund L matches the hidden illiquidity pattern. 12% of its net assets are in holdings flagged as stale or
> unpriceable, and at the same time its volatility of 4.1% is below its usual range of 6% to 9%. Its return over the
> last 12 months is 1.9% above its benchmark. Both volatility and relative return are computed using the prices of the
> flagged holdings.

## Limits of the view
The view inherits every limit of the pillar measures it reads, and adds four of its own.

- **Co-occurrence is not cause.** Signals that appear together may be unrelated. The view shows that they combine; the
  risk manager judges whether they are connected.
- **Patterns encode judgement.** The rules catch the combinations someone has defined and miss those nobody has.
- **Signals have different cadences.** A daily liquidity reading and a quarterly performance reading are not
  contemporaneous, so the view shows each signal's as-of date and treats a signal beyond a set age as stale.
- **Too many ranked funds defeats the purpose.** If the view ranks most funds, it becomes another report. The share of
  ranked funds the risk manager judges worth action is watched, and the rules are tightened when it falls.

The function tests the view by replaying past episodes: taking funds that ran into difficulty and checking whether the
view, with the rules in force at the time, would have ranked them, and how much earlier than any pillar. Episodes it
would have missed are the main source of new patterns. The AI step is tested, as in the pillars, through the risk
manager's edits to the accounts.

## Controls specific to the view
The general controls in [controls](../framework/04-controls.md) apply in full. The view adds four.

- **Every signal shows its pillar and as-of date.** Nothing in an account is shown without its source.
- **Missing data is not health.** A fund with missing signals from a pillar is shown as partly assessed, never as
  healthy.
- **The view never overrides a pillar.** A pillar's exception still goes through that pillar's workflow, whether or
  not the view ranks the fund.
- **Pattern and grouping rules are governed.** Adding, removing or changing a pattern or a driver group is recorded
  like any other threshold change.

## Measuring value
The measure that matters most for the view is **lead time**: how much earlier the view ranked a fund than the first
escalation from any single pillar. Lead time is measured from replays of past episodes and from live cases. The other
dimensions come from [measuring value](../framework/05-measuring-value.md).

| Dimension | Measure for the view |
|---|---|
| Lead time | Days between the view ranking a fund and the first single-pillar escalation |
| Speed | Time from a combination forming to the risk manager seeing it |
| Capacity | Funds covered by the integrated view: every fund, against those one person recalls |
| Quality | Combinations first seen through a pillar escalation rather than through the view |
| Influence | Ranked funds discussed by the committee, and actions taken |

## Ownership and connections
The head of risk, or a delegate, owns the view: its patterns, its grouping of drivers, its ranking rules and its
footprint thresholds. Risk managers judge the ranked funds as they appear and add them to the fund watch list, which the
head of risk owns, or escalate them. The risk committee sees the top-ranked funds, each with its account and the signals
behind it, and the firm's footprint, and decides what the firm should do.

Actions route back to the workflows that own them. A question about liquidity goes to the
[liquidity risk](liquidity-risk.md) workflows, a challenge to the portfolio manager goes into the next review in
[performance risk](performance-risk.md), and a concentration issue is followed in [market risk](market-risk.md). The
view does not hold actions of its own; it shows where the pillars' signals combine, and the pillars do the work.
