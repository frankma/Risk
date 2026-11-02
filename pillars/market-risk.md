# Market risk

Market risk asks how much a fund could lose, and the risk function answers that question every day for every fund.
This chapter applies the [redesign method](../framework/03-redesign-method.md) to the pillar: it lists the pillar's
recurring workflows, redesigns daily monitoring from a manual scan of every fund into a ranked queue of exceptions and
watch items with drafted explanations, and sets out the thresholds, limits, controls and measures that make the
redesign work.

## The outcome
The pillar's outcome, as defined in [investment risk](../framework/02-investment-risk.md#market-risk):

> The risk manager knows, every day, which funds carry more absolute risk than their mandate intends, and why.

Every workflow below is judged against that sentence. A workflow that does not help the risk manager know which funds
are outside their intended risk, or why, is a candidate for removal rather than redesign.

## Workflows in this pillar

| Workflow | Cadence | Output | Used by | For which decision |
|---|---|---|---|---|
| Daily monitoring and exceptions | Daily | Ranked queue, explained | Risk manager | What to escalate or query |
| Periodic risk report | Monthly | Risk profile of each fund | Risk committee | Whether profiles fit appetite |
| Stress and scenario testing | Monthly, on events | Stress losses by fund | Risk committee | Whether tolerable |
| Counterparty exposure monitoring | Daily | Exposure against limits | Risk manager | Whether to reduce exposure |
| New instrument review | On request | How it is measured | Risk manager, investment team | Whether it can be held |
| Ad hoc queries | On request | Answers on exposures and risk | Portfolio managers | Positioning decisions |

Daily monitoring is the flagship, because it runs most often and because most of the other workflows draw on what it
computes. The periodic risk report becomes largely a summary of the month's exceptions and their resolution, as in the
worked example in the
[redesign method](../framework/03-redesign-method.md#worked-example-a-monthly-risk-and-performance-report).
Counterparty exposure monitoring runs inside the same daily process, with its own limits; approving which
counterparties may be used remains with the function that owns that decision.

Stress and scenario testing benefits from a different kind of redesign. A scenario library is usually refreshed
occasionally, so its scenarios describe the conditions of the last refresh rather than today's. In a redesigned
workflow, the AI drafts candidate forward-looking scenarios from current conditions, such as a sharp move in a market
the funds are newly exposed to, and the risk manager decides which to adopt and calibrates the shocks. Code then runs
every scenario against every fund. The library stays current, and the calibration, which is the judgement, stays with
the risk manager.

## Flagship redesign: daily monitoring and exception handling
The example below follows one risk manager covering 40 funds. **The steps, hours and elapsed times are
illustrative.**

**Current state.** Each morning, once the overnight data is available, the risk manager works through every fund.

| # | Step | Tag | Hours | Elapsed |
|---|---|---|---|---|
| 1 | Download risk reports and position files from several systems | Gather | 0.5 | 0.5 h |
| 2 | Copy measures into the monitoring workbook | Gather | 0.5 | 0.5 h |
| 3 | Check every measure against its limit | Compute | 0.5 | 0.5 h |
| 4 | Scan every fund for large moves since the previous day | Compute | 1.0 | 1.0 h |
| 5 | Dig into positions to find the cause of each move | Interpret | 1.5 | 1.5 h |
| 6 | Decide which moves matter | Judge | 0.5 | 0.5 h |
| 7 | Email the portfolio manager where needed | Communicate | 0.5 | 0.5 h |
| 8 | Log each issue | Communicate | 0.5 | 0.5 h |

The cycle takes 5.5 hours a day. Because one person does every step in sequence, elapsed time equals effort, and a
portfolio manager hears about an issue about five hours after the data was available. Steps 1 to 4 take 2.5 hours
and need no expertise. The scan in step 4 is also shallow: with 40 funds, the risk manager can look closely at only a
few, so a moderate move in a fund that is not on their mind can pass unnoticed.

**Owner assignment.**

- Steps 1, 3 and 4 move to code, which loads data from source, computes every measure, compares each to its limit and
  to the previous day, and does so for every fund.
- Step 2 exists only because data was copied by hand, and is eliminated.
- Step 5 is split. Code decomposes each change by position and by risk factor, which is computation; the AI drafts an
  explanation from that decomposition, which is interpretation.
- Step 6 stays with the risk manager, who now judges a ranked queue rather than raw data.
- Steps 7 and 8 become AI drafts that the risk manager edits and sends.

**Redesigned flow.**

| # | Step | Owner | Hours | Elapsed |
|---|---|---|---|---|
| 1 | Load data, compute every measure, compare to limits and the previous day | Code | 0 | Overnight |
| 2 | Decompose each change by position and risk factor | Code | 0 | Overnight |
| 3 | Rank funds by materiality | Code | 0 | Overnight |
| 4 | Draft an explanation for each flagged fund | AI | 0 | Overnight |
| 5 | Grounding check on every draft | Code | 0 | Overnight |
| 6 | Review the ranked queue, edit explanations, decide what matters | Risk manager | 1.0 | 1.0 h |
| 7 | Draft the message to the portfolio manager and the log entry | AI | 0 | Minutes |
| 8 | Edit and send the message; confirm the log entry | Risk manager | 0.5 | 0.5 h |

The cycle falls to 1.5 hours a day, and portfolio managers hear about issues within about 1.5 hours of the start of
the day. The 4 hours a day freed are directed in advance, for example to deep-dive reviews of the funds that appear
most often in the queue.

**The shift.** The risk manager no longer scans everything to find what matters. The system checks every fund against
every threshold, and the risk manager's work is to judge which of the ranked items matter and why, and what to do
about them. Coverage improves at the same time: every fund is checked in full every day, rather than the few the risk
manager had time to examine.

## Materiality and exceptions
The queue holds the readings the risk manager should see today. An **exception** is a reading where a rule has fired;
a **watch item** is a reading moving towards a threshold. Both come from a small number of kinds of rule, each owned
and versioned as a
[governed parameter](../framework/04-controls.md#materiality-thresholds-as-governed-parameters).
**The example values below are illustrative and are not recommendations;** each risk function sets its own.

| Kind of rule | Example (illustrative) | What it catches |
|---|---|---|
| Level against limit | VaR above its limit, or above an early warning such as 90% of it | Breaches and near-breaches |
| Change since the previous day | VaR up by more than a set share in one day | Sudden shifts in risk |
| Against the fund's own history | A measure, such as volatility, outside its usual range | Unusual risk for this fund |
| Persistence | A near-limit reading for several consecutive days | Slow drift towards a limit |
| Concentration | One issuer or sector above a set share of the fund | Build-up of single-name risk |
| Counterparty exposure | Exposure to one counterparty above a share of its limit | Concentrated counterparty risk |

Breaches of a limit, including a concentration limit, large changes since the previous day and readings outside the
fund's usual range are exceptions. Early warnings, persistent near-limit readings and counterparty exposure approaching
its limit are watch items.

Code ranks exceptions before watch items. Breaches come first, then the other exceptions, then early warnings, then
persistence. Within a tier, items are ordered by size relative to the threshold, and a fund with several items ranks
above a fund with one. The ranking rule is itself a governed parameter, because it decides what the risk manager reads
first.

Tracking error is computed in the same daily run, because it uses the same positions and market data, but it is a
measure of active risk and belongs to [performance risk](performance-risk.md). Its exceptions are routed to that
pillar's workflows rather than to this queue, so each measure is computed once and owned by one pillar.

## What the AI drafts
The AI drafts from the facts that code produced and from nothing else. In each example below, the facts are shown
alongside the draft; every number in the draft appears in the facts, so the
[grounding check](../framework/04-controls.md#the-grounding-check) would pass. All three examples are watch items:
Fund A is above its early warning, Fund B is approaching its counterparty limit and Fund C has stayed near its limit.
Exceptions are drafted in the same way. **The funds and figures are illustrative.**

**A rise in VaR.**

| Fact | Value |
|---|---|
| Fund | Fund A |
| Measure | 1-day 99% VaR |
| Today / previous day | 2.31% / 1.84% |
| Change | +0.47 percentage points |
| Limit / utilisation | 2.50% / 92% |
| Largest contributor (position) | Technology equity basket, +0.29 points |
| Second contributor (factor) | US dollar exposure, +0.12 points |

> Fund A's 1-day 99% VaR rose from 1.84% to 2.31%, which is 92% of its 2.50% limit. Most of the 0.47 percentage point
> rise came from the technology equity basket (0.29 points), with a further 0.12 points from higher US dollar exposure.

**Counterparty exposure near its limit.**

| Fact | Value |
|---|---|
| Fund | Fund B |
| Counterparty | Counterparty X |
| Exposure today / previous day | 4.4% / 3.1% of net assets |
| Limit / utilisation | 5.0% / 88% |
| Driver | New currency forwards traded on the previous day |

> Fund B's exposure to Counterparty X rose from 3.1% to 4.4% of net assets, 88% of its 5.0% limit. The increase follows
> new currency forwards traded with that counterparty on the previous day.

**A reading that persists.**

| Fact | Value |
|---|---|
| Fund | Fund C |
| Measure | Largest single-issuer weight |
| Today | 9.6% |
| Early-warning level / limit | 9.0% / 10.0% |
| Consecutive days above early warning | 6 |

> Fund C's largest single-issuer weight has been above its 9.0% early-warning level for 6 consecutive days and stands
> at 9.6% today, against a limit of 10.0%.

None of the drafts recommends an action. Whether a reading matters, and what to ask the portfolio manager, is the risk
manager's judgement at the sign-off point.

## Limits of the measures
The risk function owns the model risk in its own measures: it should know what each assumes, where it is weak, and
test it. Independent validation of the models sits elsewhere, as set out in
[investment risk](../framework/02-investment-risk.md#scope-and-boundaries).

| Measure | Where it is weak | How the function tests it |
|---|---|---|
| VaR and expected shortfall | Regime changes; losses beyond the tail | Backtesting against realised results |
| Sensitivities | Large moves; non-linear positions such as options | Comparison with full revaluation |
| Stress tests | Scenarios nobody thought of | Review of the library against current conditions |
| All measures | Thinly traded or stale-priced holdings | Flags from [liquidity risk](liquidity-risk.md) |

VaR and expected shortfall assume that the chosen history and model describe the future, and they say little about
losses beyond the tail they measure; stress tests complement them for that reason, but rest in turn on the scenarios
being plausible. Sensitivities assume small moves from today's position and can mislead for large ones. Every measure
takes the prices of holdings as fair, which is why the flags for stale and unpriceable holdings matter here.

The AI step has its own limits: an explanation can give weight to the wrong driver even when every number in it is
correct. The function tests this by tracking how often, and how substantially, risk managers edit the drafts, and by
reviewing a sample of explanations against the full decomposition.

## Controls specific to this pillar
The general controls in [controls](../framework/04-controls.md) apply in full. This pillar adds four.

- **Decomposition reconciles before drafting.** The contributions by position and by factor must add up to the total
  change, within a stated tolerance, before the AI drafts from them. A decomposition that does not reconcile is an
  exception in its own right.
- **Silence is not a clean result.** A fund with missing or incomplete data is shown as not assessed, never as having
  nothing to report.
- **Messages are sent by the risk manager.** Drafted messages to portfolio managers are never sent automatically.
- **The scenario library is governed.** Scenarios the AI proposes are recorded as proposals; the risk manager's
  calibration and approval are recorded before a scenario enters the library.

## Measuring value
The measures from [measuring value](../framework/05-measuring-value.md) that matter most for this pillar are speed and
capacity: how soon a portfolio manager hears about an issue, and how many funds are reviewed in depth.

| Dimension | Measure for this pillar |
|---|---|
| Speed | Time from data availability to the first message to a portfolio manager |
| Capacity | Funds reviewed in depth per day |
| Quality | Issues found late, for example a limit breach first noticed by someone else |
| Influence | Issues raised with portfolio managers and actions taken |
| Pillar-specific | Share of drafts that needed substantive edits; backtesting exceptions within expectation |

In the flagship example, the time to the first message falls from about five hours to about an hour and a half,
and the 4 hours freed each day are tracked against the reinvestment plan. (The figures are illustrative.)

## Connections
Market risk signals feed the other pillars. Rising concentration and volatility raise the cost and time of selling
holdings, which matters to [liquidity risk](liquidity-risk.md); stress losses inform the redemption scenarios that
pillar uses. Tracking error, computed here, is routed to [performance risk](performance-risk.md). Performance and flows
usually move before market risk, but a sharp market loss is the case where market risk moves first, ahead of the
underperformance that pillar watches. The [integrated view](integrated-view.md) brings
these signals together for each fund.
