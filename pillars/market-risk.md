# Market risk

Market risk asks how much a portfolio could lose, in total and against its benchmark, and the risk function answers that
question every day for every portfolio. This chapter applies the [redesign method](../framework/07-redesign-method.md)
to the pillar: it lists the pillar's recurring workflows, redesigns daily monitoring from a manual scan of every
portfolio into a ranked queue of exceptions and watch items with drafted explanations, and sets out the thresholds,
limits, controls and measures that make the redesign work, and the design choices behind the pillar's measures.

## The outcome
The pillar's outcome, as defined in [investment risk](../framework/01-investment-risk.md#market-risk):

> The risk manager knows, every day, which portfolios carry more risk than their mandate intends, absolute or
> relative, and why.

Every workflow below is judged against that sentence. A workflow that does not help the risk manager know which
portfolios are outside their intended risk, or why, is a candidate for removal rather than redesign.

## Workflows in this pillar

| Workflow | Cadence | Output | Used by | For which decision |
|---|---|---|---|---|
| Daily monitoring and exceptions | Daily | Ranked queue, explained | Risk manager | What to escalate or query |
| Risk budget review | Daily use; monthly review | Budget use against realised return, by bet | Risk manager | Which bets to challenge |
| Periodic risk report | Monthly | Risk profile of each portfolio | Risk committee | Whether profiles fit appetite |
| Stress and scenario testing | Daily run; library reviewed monthly and on events | Stress losses by portfolio | Risk committee | Whether tolerable |
| Pre-trade what-ifs | On request | What a proposed trade adds to risk | Portfolio managers | Whether and how much to trade |
| Counterparty exposure monitoring | Daily | Exposure against limits | Risk manager | Whether to reduce exposure |
| New instrument review | On request | How it is measured | Risk manager, investment team | Whether it can be held |
| Ad hoc queries | On request | Answers on exposures and risk | Portfolio managers | Positioning decisions |

Daily monitoring is the flagship, because it runs most often and because most of the other workflows draw on what it
computes. The periodic risk report becomes largely a summary of the month's exceptions and their resolution, as in the
worked example in the [redesign
method](../framework/07-redesign-method.md#worked-example-a-monthly-risk-and-performance-report). Counterparty exposure
monitoring runs inside the same daily process, with its own limits; approving which counterparties may be used remains
with the function that owns that decision. The same run totals holdings across portfolios by issuer, counterparty and
factor for the [firm's footprint](integrated-view.md#the-firms-footprint); these totals do not net.

The daily run also computes **ex-ante tracking error**: the forecast standard deviation of the portfolio's return
relative to its benchmark, from today's holdings and the risk model. It is the relative counterpart of value at risk
and, like it, looks forward, so it belongs to this pillar. Its realised counterpart, ex-post tracking error, is measured
in [performance risk](performance-risk.md), and comparing the two is one of this pillar's tests of its own measures.

The **risk budget review** allots ex-ante tracking error to the portfolio's bets and reads what each bet uses against
the return it has earned, which performance risk measures. The budget carries no limit of its own: the daily check is of
ex-ante tracking error against its range. Each month, a bet that uses a large share of the budget and has earned nothing
over several periods is challenged: the portfolio manager resizes it, cuts it or explains why it stays. The exceptions
go into the next challenge pack in performance risk, so that the challenge is made in the portfolio manager review and
tracked in its action log.

The same run computes each holding's exposures once, for this pillar and for the
[alpha and beta method](alpha-and-beta-method.md#computing-the-split). A direct measure is used where one exists:
duration for rates, duration times spread for credit and the currency weight for currency, each scaled against its
basket, so that a bond with a duration of 6 against a basket of 4 has an exposure of 1.5. Equity market and style
exposures are betas, estimated together against all the baskets so that overlapping baskets do not count the same
return twice, over a long window with gradual decay so that they do not jump when an old day drops out
([belief 7](../framework/00-philosophy.md#beliefs)). A security with little history uses a proxy under the
[proxy policy](../framework/03-risk-data.md#proxies), such as its sector's beta. (The figures are illustrative.)

Pre-trade what-ifs run the daily calculations on a proposed trade: the risk engine computes what it adds to VaR,
concentration, tracking error and budget use, and the portfolio manager decides.

Ad hoc queries become investigations. A portfolio manager or a risk manager asks a question in plain words, and the AI
runs the drill-down, the aggregation or the what-if through the risk engine and reports the figures with the runs
behind them, as set out in [working with AI](../framework/06-working-with-ai.md#three-modes-of-working).

Stress and scenario testing benefits from a different kind of redesign. A scenario library is usually refreshed
occasionally, so its scenarios describe the conditions of the last refresh rather than today's. In a redesigned
workflow, the AI drafts candidate forward-looking scenarios from current conditions, such as a sharp move in a market
the portfolios are newly exposed to. The AI proposes the story and names a historical analogue, but never states a
shock size. Sizes come from data, where the risk engine computes the analogue's moves from market history, or from the
risk manager, who decides which scenarios to adopt and adjusts and approves the shocks. The risk engine then runs every
scenario against every portfolio. The library stays current, and the calibration, which is the judgement, stays with
the risk manager. Reverse stress testing works the other way: it starts from the loss that would break the
mandate and asks which shocks would cause it, and the risk manager judges how plausible they are.

## Flagship redesign: daily monitoring and exception handling
The example below follows one risk manager covering 40 portfolios. **The steps, hours and elapsed times are
illustrative.**

**Current state.** Each morning, once the overnight data is available, the risk manager works through every portfolio.

| # | Step | Tag | Hours | Elapsed |
|---|---|---|---|---|
| 1 | Download risk reports and position files from several systems | Gather | 0.5 | 0.5 h |
| 2 | Copy measures into the monitoring workbook | Gather | 0.5 | 0.5 h |
| 3 | Check every measure against its limit | Compute | 0.5 | 0.5 h |
| 4 | Scan every portfolio for large moves since the previous day | Compute | 1.0 | 1.0 h |
| 5 | Dig into positions to find the cause of each move | Interpret | 1.5 | 1.5 h |
| 6 | Decide which moves matter | Judge | 0.5 | 0.5 h |
| 7 | Email the portfolio manager where needed | Communicate | 0.5 | 0.5 h |
| 8 | Log each issue | Communicate | 0.5 | 0.5 h |

The cycle takes 5.5 hours a day. Because one person does every step in sequence, elapsed time equals effort, and a
portfolio manager hears about an issue about five hours after the data was available. Steps 1 to 4 take 2.5 hours and
need no expertise. The scan in step 4 is also shallow: with 40 portfolios, the risk manager can look closely at only a
few, so a moderate move in a portfolio that is not on their mind can pass unnoticed.

**Owner assignment.**

- Steps 1, 3 and 4 move to the risk engine, which loads data from source, computes every measure, compares each to its
  limit and to the previous day, and does so for every portfolio.
- Step 2 exists only because data was copied by hand, and is eliminated.
- Step 5 is split. The risk engine decomposes each change by position and by risk factor, which is computation; the AI
  drafts an explanation from that decomposition, which is interpretation.
- Step 6 stays with the risk manager, who now judges a ranked queue rather than raw data.
- Steps 7 and 8 become AI drafts that the risk manager edits and sends.

**Redesigned flow.**

| # | Step | Owner | Hours | Elapsed |
|---|---|---|---|---|
| 1 | Load data, compute every measure, compare to limits and the previous day | Risk engine | 0 | Overnight |
| 2 | Decompose each change by position and risk factor | Risk engine | 0 | Overnight |
| 3 | Rank portfolios by materiality | Risk engine | 0 | Overnight |
| 4 | Draft an explanation for each flagged portfolio | AI assistant | 0 | Overnight |
| 5 | Grounding check on every draft | Risk engine | 0 | Overnight |
| 6 | Review the ranked queue, edit explanations, decide what matters | Risk manager | 1.0 | 1.0 h |
| 7 | Draft the message to the portfolio manager and the log entry | AI assistant | 0 | Minutes |
| 8 | Edit and send the message; confirm the log entry | Risk manager | 0.5 | 0.5 h |

The cycle falls to 1.5 hours a day, and portfolio managers hear about issues within about 1.5 hours of the start of
the day. The 4 hours a day freed are directed in advance, for example to deep-dive reviews of the portfolios that appear
most often in the queue.

**The shift.** The risk manager no longer scans everything to find what matters. The system checks every portfolio
against every threshold, and the risk manager's work is to judge which of the ranked items matter and why, and what to
do about them. Coverage improves at the same time: every portfolio is checked in full every day, rather than the few the
risk manager had time to examine.

## Materiality and exceptions
The queue holds the readings the risk manager should see today. An **exception** is a reading that has crossed a limit
or another rule's threshold; a **watch item** is a reading approaching one, which an early warning or a persistence
rule picks up. Both come from a small number of kinds of rule, each owned and versioned as a
[governed parameter](../framework/08-controls.md#materiality-thresholds-as-governed-parameters).
**The example values below are illustrative and are not recommendations;** each risk function sets its own.

| Kind of rule | Example (illustrative) | What it catches |
|---|---|---|
| Level against limit | VaR above its limit, or above an early warning such as 90% of it | Breaches and near-breaches |
| Change since the previous day | Any measure with a limit, such as VaR, moving by more than a set share in one day; each measure has its own threshold | Sudden shifts in risk |
| Against the portfolio's own history | A measure, such as volatility, outside its usual range | Unusual risk for this portfolio |
| Headroom against drawdown tolerance | A stress loss larger than the headroom left before the drawdown tolerance, absolute or relative, or above an early warning of it | Mandates nearing the loss that would end them |
| Ex-ante tracking error | Outside the range the mandate terms imply, or beyond an early warning of it | Too much or too little active risk |
| Persistence | A near-limit reading for several consecutive days | Slow drift towards a limit |
| Concentration | One issuer or sector above the risk function's early warning, set below the mandate's limit | Build-up of single-name risk |
| Jump to default | The loss if one issuer defaulted, net of expected recovery, above an early warning | Single-name credit loss |
| Rating floor | A holding within one notch of the mandate's rating floor, read with its time to sell | A downgrade that would force a sale |
| Leverage | Gross or net exposure above its internal limit, or above an early warning of it | Scale or risk beyond what the mandate intends |
| Counterparty exposure | Exposure to one counterparty, net of collateral and with the add-on, above a share of its limit | Concentrated counterparty risk |
| Risk budget | A bet using a large share of the budget with no return over several periods | Risk that has not earned its place |

Breaches of an internal limit, including a tracking error range and a leverage limit, are exceptions. So are a stress
loss beyond the drawdown headroom, large changes since the previous day, readings outside the portfolio's usual range
and a fired risk budget rule. Early warnings, persistent near-limit readings, jump to default above its early warning,
holdings near a rating floor and counterparty exposure approaching its limit are watch items. A breach of a position or
eligibility rule, such as a limit on one issuer's weight, is owned by compliance: it is shown beside the queue and
routed to compliance, while the risk function's own early warning below that limit stays in the queue. A breach of a
risk-measured hard limit, such as a regulatory limit on leverage, is the risk function's to monitor: it enters the queue
as an exception and is reported to compliance the same day. [Limits and
escalation](../framework/04-limits-and-escalation.md) sets out which limits are internal and how a breach is handled.

The risk engine ranks exceptions before watch items. Breaches come first, then the other exceptions, then early
warnings, then persistence. Within a tier, items are ordered by size relative to the threshold, and a portfolio with
several items ranks above a portfolio with one. The ranking rule is itself a governed parameter, because it decides what
the risk manager reads first.

Ex-ante tracking error and risk budget exceptions enter this queue, because both look forward. Both also go into the
next challenge pack in [performance risk](performance-risk.md), where the portfolio manager answers them. Each measure
is computed once and owned by one pillar: realised drawdown is computed in performance risk, and this pillar reads only
the headroom it leaves.

## What the AI drafts
The AI drafts from the facts that the risk engine produced and from nothing else. In each example below, the facts are
shown alongside the draft; every number in the draft appears in the facts, so the [grounding
check](../framework/08-controls.md#the-grounding-check) would pass. Fund A is an exception, for its large one-day rise,
and also a watch item, for being above its early warning. Fund B is likewise an exception, for a one-day rise above its
change threshold, and a watch item approaching its counterparty limit. Fund C is a watch item that has stayed near its
limit. **The funds and figures are illustrative.**

**A rise in VaR.**

| Fact | Value |
|---|---|
| Fund | Fund A |
| Measure | 1-day 99% VaR |
| Today / previous day | 2.31% / 1.84% |
| Change | +0.47 percentage points |
| Limit / utilisation | 2.50% / 92% |
| Largest contributor (position) | Technology equity basket, +0.29 points |
| Second contributor (position) | Energy equity basket, +0.12 points |

> Fund A's 1-day 99% VaR rose from 1.84% to 2.31%, which is 92% of its 2.50% limit. Most of the 0.47 percentage point
> rise came from the technology equity basket (0.29 points), with a further 0.12 points from the energy equity basket.

**Counterparty exposure near its limit.**

| Fact | Value |
|---|---|
| Fund | Fund B |
| Counterparty | Counterparty X |
| Exposure today / previous day | 4.4% / 3.1% of net assets |
| Change | +1.3 percentage points |
| One-day change threshold | 25% of the previous day's exposure |
| Limit / utilisation | 5.0% / 88% |
| Early-warning share of the limit | 85% |
| Driver | New currency forwards traded on the previous day |

> Fund B's exposure to Counterparty X rose by 1.3 percentage points in one day, from 3.1% to 4.4% of net assets, above
> its one-day change threshold of 25%, and now stands at 88% of its 5.0% limit. The increase follows new currency
> forwards traded on the previous day.

**A reading that persists.**

| Fact | Value |
|---|---|
| Fund | Fund C |
| Measure | Largest single-issuer weight |
| Today | 9.6% |
| Risk function's early warning / mandate limit | 9.0% / 10.0% |
| Consecutive days above early warning | 6 |

> Fund C's largest single-issuer weight has been above its 9.0% early-warning level for 6 consecutive days and stands
> at 9.6% today, against a mandate limit of 10.0%, which compliance owns.

None of the drafts recommends an action. Whether a reading matters, and what to ask the portfolio manager, is the risk
manager's judgement at the sign-off point.

## Design choices
A risk function chooses how each of its measures is computed, and records the choice. This section sets out the
choices for this pillar, what each trades off, and how the function tests what it chose. The risk function owns the
model risk in its own measures; independent validation of the models sits elsewhere, as set out in
[investment risk](../framework/01-investment-risk.md#scope-and-boundaries).

### Value at risk and expected shortfall
| Choice | Options | Trade-off |
|---|---|---|
| Method | Historical simulation, parametric, Monte Carlo | Historical keeps the shape of past moves but only those moves; parametric is fast and smooth but thin in the tail; Monte Carlo is flexible but rests on the model behind it |
| Confidence and horizon | For example 99% over one day, or 97.5% | Higher confidence says more about the tail and is noisier; a longer horizon needs scaling or overlapping periods |
| Lookback and weighting | A short window, a long window, a long window with gradual decay | A short window reacts fast and jitters; a long window is stable and slow; decay sits between |
| Expected shortfall | Alongside value at risk, or instead of it | Expected shortfall measures the average loss beyond the threshold, which value at risk ignores, but needs more data to estimate |
| Stressed period | A separate measure on a fixed period of stress | Keeps a stressed view when the recent window is calm |

**Illustrative setup** (not a recommendation): historical simulation; 1-day 99% value at risk alongside 97.5% expected
shortfall; a long window with gradual decay, the same as the betas use, so the measure moves when markets or positions
move rather than when an old day drops out ([belief 7](../framework/00-philosophy.md#beliefs)); and a separate value at
risk on a fixed stressed period.

### Factors
The factor model behind ex-ante tracking error and the risk decomposition is chosen by the risk function's set process,
and run by the risk engine. Whatever model is chosen, its factors are the
[declared factor list](alpha-and-beta-method.md) of the alpha and beta method, or map to it one to one, and carry the
same generator tags. Risk by factor and return by factor then line up, and each can be grouped by return generator, so
that the risk budget review can set what each bet uses beside what it earns, and any period's return and change in risk
can be explained by the same factors
([connection](../framework/00-philosophy.md#3-connection)).

### Backtesting
A backtest compares the days on which losses exceeded value at risk with the number the confidence level implies, and
it is judged against what the chosen design implies, stated before the test.

- **A long lookback is built to be stable,** so breaches cluster when conditions change: the measure adjusts slowly by
  design. Clustering is expected and recorded, and does not by itself lead to recalibration. The judgement is the count
  of breaches over a long period against the number expected, read in zones set in advance, for example green, amber
  and red. Recalibrating whenever breaches cluster would chase a moving target.
- **A short, responsive measure is built to adapt,** so for it, clustered breaches are a failure, and the backtest adds
  a check that breaches are independent of each other.
- **Expected shortfall** is checked against the average of the losses beyond value at risk.

A stable measure is paired with a responsive one. Value at risk on the long window carries the limits; volatility on a
short window serves as the early warning that conditions are changing, through the rule on readings outside the
portfolio's usual range.

### Stress and reverse stress
- **The library** holds historical episodes, hypothetical scenarios and sensitivity shocks to single factors, and is
  reviewed on a set cycle and when conditions change.
- **The library covers how each return generator fails.** The
  [sources of return](../framework/02-sources-of-return.md#how-does-each-generator-fail) chapter names three ways: a
  drawdown in market risk premia, a crowded reversal in a style premium, and books built on skill losing together. The
  review of the library checks that each has at least one scenario.
- **A scenario becomes shocks to every factor** in two steps: shocks are set on the factors that drive the scenario,
  and the other factors are filled in from how they moved with those factors in the past.
- **Shock sizes** come from data, where the risk engine computes them from a historical episode, or from the risk
  manager; the AI proposes the story and never the size.
- **Reverse stress** works back from the loss that would break the mandate: the risk engine searches for the smallest
  combination of shocks that would cause it, and the risk manager judges how plausible that combination is.

### Credit: spreads, default and migration
Spread duration and duration times spread measure the loss when spreads move. They do not capture the loss when an
issuer defaults, where the price falls to its recovery value at once. That loss is **jump to default**: for each issuer,
the position times one minus the expected recovery rate, which is a governed parameter. It is read as a concentration
measure, with an early warning, because a single default in a concentrated or high-yield portfolio can cost far more
than spread volatility suggests. A downgrade shows up as spreads widening, so migration is covered by spread stress and
needs no model of its own. One event is not covered that way: a downgrade below a mandate's rating floor forces a sale,
at a cost that depends on how long the holding takes to sell. An early warning therefore flags holdings close to the
floor, read with their [time to sell](liquidity-risk.md#time-and-cost-to-sell).

### Leverage and options
Leverage is measured two ways, each with an internal limit: **gross exposure**, the sum of all positions without
netting, which shows scale; and **net exposure**, what is left after netting and hedging, which shows the risk actually
taken. Derivatives are converted to the equivalent position in the underlying before either is summed: an option by
its delta, and an interest rate derivative by its duration against a common maturity. Raw notional would overstate
interest rate derivatives many times over. Options carry
delta, gamma and vega, so that the daily measures see how their value changes with the underlying and with volatility.
Sensitivities assume small moves, so stress tests revalue options in full.

### Counterparty exposure
Exposure to a counterparty is the current exposure net of the collateral held under netting agreements, plus an add-on
for how far it could grow before the next collateral call. The internal limit applies to the total. Without the add-on,
a portfolio could reach its limit between two collateral calls without warning.

### Where the measures are weak
| Measure | Where it is weak | How the function tests it |
|---|---|---|
| VaR and expected shortfall | Regime changes; losses beyond the tail | Backtesting judged against the design, as above |
| Ex-ante tracking error | Model and factor choice; regime changes | Comparison with ex-post tracking error from performance risk |
| Sensitivities | Large moves; non-linear positions such as options | Comparison with full revaluation |
| Estimated betas | Estimation noise; short histories | Comparison with a regression on portfolio returns |
| Jump to default | The recovery rate assumed | Comparison with recoveries in past defaults |
| Stress tests | Scenarios nobody thought of | Review of the library against current conditions |
| All measures | Thinly traded or stale-priced holdings | Flags from [liquidity risk](liquidity-risk.md) |

VaR and expected shortfall assume that the chosen history and model describe the future, and they say little about
losses beyond the tail they measure; stress tests complement them for that reason, but rest in turn on the scenarios
being plausible. Sensitivities assume small moves from today's position and can mislead for large ones. Every measure
takes the prices of holdings as fair, which is why the flags for stale and unpriceable holdings matter here. Ex-ante
tracking error is a forecast like value at risk, and is tested the same way: against the ex-post tracking error that
performance risk measures.

The AI step has its own limits: an explanation can give weight to the wrong driver even when every number in it is
correct. The function tests this by tracking how often, and how substantially, risk managers edit the drafts, and by
reviewing a sample of explanations against the full decomposition.

## Controls specific to this pillar
The general controls in [controls](../framework/08-controls.md) apply in full. This pillar adds four.

- **Decomposition reconciles before drafting.** The contributions by position and by factor must add up to the total
  change, within a stated tolerance, before the AI drafts from them. A decomposition that does not reconcile is an
  exception in its own right.
- **Silence is not a clean result.** A portfolio with missing or incomplete data is shown as not assessed, never as
  having nothing to report, as set out in [risk data](../framework/03-risk-data.md#quality-before-computation).
- **Messages are sent by the risk manager.** Drafted messages to portfolio managers are never sent automatically.
- **The scenario library is governed.** Scenarios the AI proposes are recorded as proposals; the risk manager's
  calibration and approval are recorded before a scenario enters the library.

## Measuring value
The measures from [measuring value](../framework/09-measuring-value.md) that matter most for this pillar are speed and
capacity: how soon a portfolio manager hears about an issue, and how many portfolios are reviewed in depth.

| Dimension | Measure for this pillar |
|---|---|
| Speed | Time from data availability to the first message to a portfolio manager |
| Capacity | Portfolios reviewed in depth per day |
| Quality | Issues found late, for example a limit breach first noticed by someone else |
| Influence | Issues raised with portfolio managers and actions taken |
| Pillar-specific | Share of drafts that needed substantive edits; backtesting breaches within expectation |

In the flagship example, the time to the first message falls from about five hours to about an hour and a half,
and the 4 hours freed each day are tracked against the reinvestment plan. (The figures are illustrative.)

## Connections
Market risk signals feed the other pillars. Rising concentration and volatility raise the cost and time of selling
holdings, which matters to [liquidity risk](liquidity-risk.md); stress losses inform the redemption scenarios that
pillar uses. Ex-ante tracking error and the risk budget belong here, and their realised counterparts to [performance
risk](performance-risk.md), which also receives both kinds of exception in its challenge pack and measures the drawdown
whose headroom is read here. Performance and flows usually move before market risk, but a sharp market loss is the case
where market risk moves first, ahead of the underperformance that pillar watches. The [integrated
view](integrated-view.md) brings these signals together for each portfolio.

## Sources
- International Organization of Securities Commissions (2019). *Recommendations for a Framework Assessing Leverage in
  Investment Funds.* Gross and net exposure, with derivatives converted to the equivalent position in the underlying.
- Jorion, P. (2006). *Value at Risk: The New Benchmark for Managing Financial Risk*, 3rd edition. McGraw-Hill. Value
  at risk, expected shortfall, stress testing and backtesting.
- Litterman, R. (1996). Hot Spots and Hedges. *Journal of Portfolio Management*, special issue. Decomposing a change in
  risk by position and factor, and marginal risk for what-ifs.
- Grinold, R. and Kahn, R. (2000). *Active Portfolio Management*, 2nd edition. McGraw-Hill. Ex-ante tracking error
  and allotting active risk to bets.
- Kupiec, P. (1995). Techniques for Verifying the Accuracy of Risk Measurement Models. *Journal of Derivatives*.
  Counting value at risk breaches against the number expected.
- Christoffersen, P. (1998). Evaluating Interval Forecasts. *International Economic Review*. Testing whether breaches
  are independent of each other as well as correct in number.
- Acerbi, C. and Tasche, D. (2002). On the Coherence of Expected Shortfall. *Journal of Banking and Finance*. Expected
  shortfall as the average loss beyond the threshold.
- Breuer, T., Jandacka, M., Rheinberger, K. and Summer, M. (2009). How to Find Plausible, Severe and Useful Stress
  Scenarios. *International Journal of Central Banking*. Searching for the scenarios that break a portfolio, and
  judging their plausibility.
