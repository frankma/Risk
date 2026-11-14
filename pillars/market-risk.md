# Market risk

## In short
**The question:** how much could a portfolio lose, in total and against its benchmark?

**The outcome:**

> The risk manager knows, every day, which portfolios carry more risk than their mandate intends, absolute or relative,
> and why.

**How the work is done:** the risk engine measures every portfolio every day and ranks what needs attention. The AI
drafts an explanation of each ranked item. The risk manager judges which items matter and sends what goes out.

| # | Step | Owner |
|---|---|---|
| 1 | Load data, compute every measure, compare to limits and the previous day | Risk engine |
| 2 | Decompose each change by position and risk factor | Risk engine |
| 3 | Rank portfolios by materiality | Risk engine |
| 4 | Draft an explanation for each flagged portfolio | AI assistant |
| 5 | Grounding check on every draft | Risk engine |
| 6 | Review the ranked queue, edit explanations, decide what matters | Risk manager |
| 7 | Draft the message to the portfolio manager and the log entry | AI assistant |
| 8 | Edit and send the message; confirm the log entry | Risk manager |

**What reaches the risk manager:** a ranked queue. An exception is a reading that has crossed a limit or another rule's
threshold, and a watch item is a reading approaching one. Every portfolio is checked in full, and breaches rank first.

**Where it connects:** the pillar's forward-looking measures have realised counterparts in [performance
risk](performance-risk.md), and its signals feed [liquidity risk](liquidity-risk.md) and the [integrated
view](integrated-view.md).

The rest of this chapter is the detail behind these points.

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

Daily monitoring is the flagship, shown in the table at the top: it runs most often, and most of the other workflows
draw on what it computes.

- **Periodic risk report.** Largely a summary of the month's exceptions and their resolution, as in the [redesign
  method's worked example](../framework/07-redesign-method.md#worked-example-a-monthly-risk-and-performance-report).
- **Stress and scenario testing.** The AI drafts candidate scenarios from current conditions and names a historical
  analogue, but never states a shock size. The risk manager decides which to adopt and approves the shocks, and the risk
  engine runs every scenario against every portfolio. [Stress and reverse
  stress](market-risk.md#stress-and-reverse-stress) has the detail.
- **Pre-trade what-ifs.** The risk engine runs the daily calculations on a proposed trade and computes what it adds to
  VaR, concentration, tracking error and budget use. The portfolio manager decides.
- **Counterparty exposure monitoring.** Runs inside the daily process, with its own limits. Approving which
  counterparties may be used stays with the function that owns that decision.
- **Ad hoc queries.** They become investigations: someone asks in plain words, and the AI runs the drill-down, the
  aggregation or the what-if through the risk engine and reports the figures with the runs behind them, as set out in
  [working with AI](../framework/06-working-with-ai.md#three-modes-of-working).
- **The firm's footprint.** The daily run totals holdings across portfolios by issuer, counterparty and factor for the
  [firm's footprint](integrated-view.md#the-firms-footprint). These totals do not net.

**Ex-ante tracking error** looks forward, so it belongs to this pillar. Its realised counterpart, ex-post tracking
error, is measured in [performance risk](performance-risk.md), and comparing the two tests this pillar's measures.

**The risk budget review** allots ex-ante tracking error to the portfolio's bets and reads what each bet uses against
the return it has earned, which performance risk measures. The budget carries no limit of its own: the daily check is of
ex-ante tracking error against its range. Each month, a bet that uses a large share of the budget is tested on its
cumulative return against the risk it has used. A bet whose return is
[significantly](performance-risk.md#windows-and-significance) below zero is challenged: the portfolio manager resizes
it, cuts it or explains why it stays. A bet that has only earned nothing for several periods is a watch item.

**Exposures are computed once,** for this pillar and for the [alpha and beta
method](alpha-and-beta-method.md#computing-the-split). A direct measure is used where one exists: duration for rates,
duration times spread for credit and the currency weight for currency, each scaled against its basket, so that a bond
with a duration of 6 against a basket of 4 has an exposure of 1.5. Equity market and style exposures are betas,
estimated together against all the baskets so that overlapping baskets do not count the same return twice, over a long
window with gradual decay ([belief 7](../framework/00-philosophy.md#beliefs)). A security with little history uses a
proxy under the [proxy policy](../framework/03-risk-data.md#proxies), such as its sector's beta. (The figures are
illustrative.)

## Materiality and exceptions
The queue comes from a small number of kinds of rule, each owned and versioned as a [governed
parameter](../framework/08-controls.md#materiality-thresholds-as-governed-parameters). **The example values below are
illustrative and are not recommendations;** each risk function sets its own.

| Kind of rule | Example (illustrative) | What it catches | What it gives |
|---|---|---|---|
| Level against limit | VaR above its limit, or above an early warning such as 90% of it | Breaches and near-breaches | Exception on a breach; watch item above the early warning |
| Change since the previous day | Any measure with a limit, such as VaR, moving by more than a set share in one day; each measure has its own threshold | Sudden shifts in risk | Exception |
| Against the portfolio's own history | A measure, such as volatility, outside its usual range | Unusual risk for this portfolio | Exception |
| Headroom against drawdown tolerance | A stress loss larger than the headroom left before the drawdown tolerance, absolute or relative, or above an early warning of it | Mandates nearing the loss that would end them | Exception beyond the headroom; watch item above the early warning |
| Ex-ante tracking error | Outside the range the mandate terms imply, or beyond an early warning of it | Too much or too little active risk | Exception outside the range; watch item beyond the early warning |
| Persistence | A near-limit reading for several consecutive days | Slow drift towards a limit | Watch item |
| Concentration | One issuer or sector above the risk function's early warning, set below the mandate's limit | Build-up of single-name risk | Watch item |
| Jump to default | The loss if one issuer defaulted, net of expected recovery, above an early warning | Single-name credit loss | Watch item |
| Rating floor | A holding within one notch of the mandate's rating floor, read with its time to sell | A downgrade that would force a sale | Watch item |
| Leverage | Gross or net exposure above its internal limit, or above an early warning of it | Scale or risk beyond what the mandate intends | Exception above the limit; watch item above the early warning |
| Counterparty exposure | Exposure to one counterparty, net of collateral and with the add-on, above a share of its limit | Concentrated counterparty risk | Watch item; exception on a breach |
| Risk budget | A bet using a large share of the budget whose cumulative return is significantly below zero for the risk it used | Risk that has not earned its place | Exception; a run of periods without return is a watch item |

**Hard limits.** A breach of a position or eligibility rule, such as a limit on one issuer's weight, is owned by
compliance: it is shown beside the queue and routed to compliance, while the risk function's own early warning below
that limit stays in the queue. A breach of a risk-measured hard limit, such as a regulatory limit on leverage, is the
risk function's to monitor: it enters the queue as an exception and is reported to compliance the same day. [Limits and
escalation](../framework/04-limits-and-escalation.md) sets out which limits are internal and how a breach is handled.

**Ranking.** Exceptions rank before watch items: breaches first, then the other exceptions, then early warnings, then
persistence. Within a tier, items are ordered by size relative to the threshold, and a portfolio with several items
ranks above a portfolio with one. The ranking rule is itself a governed parameter, because it decides what the risk
manager reads first.

**Shared with performance risk.** Ex-ante tracking error and risk budget exceptions also go into the next challenge pack
in [performance risk](performance-risk.md), where the portfolio manager answers them. Each measure is computed once and
owned by one pillar: realised drawdown is computed in performance risk, and this pillar reads only the headroom it
leaves.

## What the AI drafts
The AI drafts from the facts that the risk engine produced and from nothing else. Every number in the draft appears in
the facts beside it, so the [grounding check](../framework/08-controls.md#the-grounding-check) would pass. Fund A is an
exception, for its large one-day rise, and also a watch item, for being above its early warning. **The fund and figures
are illustrative.**

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

The draft recommends no action. Whether a reading matters, and what to ask the portfolio manager, is the risk manager's
judgement at the sign-off point.

## Design choices
A risk function chooses how each of its measures is computed, records the choice and tests it. Independent validation of
the models sits outside the risk function, as set out in [investment
risk](../framework/01-investment-risk.md#scope-and-boundaries).

### Value at risk and expected shortfall
| Choice | Options | Trade-off |
|---|---|---|
| Method | Historical simulation, parametric, Monte Carlo | Historical keeps the shape of past moves but only those moves; parametric is fast and smooth but thin in the tail; Monte Carlo is flexible but rests on the model behind it |
| Confidence and horizon | For example 99% over one day, or 97.5% | Higher confidence says more about the tail and is noisier; a longer horizon needs scaling or overlapping periods |
| Lookback and weighting | A short window, a long window, a long window with gradual decay | A short window reacts fast and jitters; a long window is stable and slow; decay sits between |
| Expected shortfall | Alongside value at risk, or instead of it | Sees the tail beyond the threshold, but needs more data to estimate |
| Stressed period | A separate measure on a fixed period of stress | Keeps a stressed view when the recent window is calm |

**Illustrative setup** (not a recommendation): historical simulation; 1-day 99% value at risk alongside 97.5% expected
shortfall; a long window with gradual decay, the same as the betas use, so the measure moves when markets or positions
move rather than when an old day drops out; and a separate value at risk on a fixed stressed period.

### Factors
The risk function chooses the factor model behind ex-ante tracking error and the risk decomposition, and the risk engine
runs it. Its factors are the [declared factor list](alpha-and-beta-method.md) of the alpha and beta method, or map to it
one to one, and carry the same generator tags. Risk by factor and return by factor then line up, so the risk budget
review can set what each bet uses beside what it earns, and one set of factors explains any period's return and change
in risk ([connection](../framework/00-philosophy.md#3-connection)).

### Backtesting
A backtest is judged against what the chosen design implies, stated before the test.

- **A long lookback is built to be stable,** so breaches cluster when conditions change. Clustering is expected and
  recorded, and does not by itself lead to recalibration. The judgement is the count of breaches over a long period
  against the number expected, read in zones set in advance, for example green, amber and red.
- **A short, responsive measure is built to adapt,** so for it clustered breaches are a failure, and the backtest adds a
  check that breaches are independent of each other.
- **Expected shortfall** is checked against the average of the losses beyond value at risk.

A stable measure is paired with a responsive one. Value at risk on the long window carries the limits; volatility on a
short window is the early warning that conditions are changing, through the rule on readings outside the portfolio's
usual range.

### Stress and reverse stress
- **The library** holds historical episodes, hypothetical scenarios and sensitivity shocks to single factors, and is
  reviewed on a set cycle and when conditions change.
- **The library covers how each return generator fails.** The [sources of
  return](../framework/02-sources-of-return.md#how-does-each-generator-fail) chapter names three ways: a drawdown in
  market risk premia, a crowded reversal in a style premium, and books built on skill losing together. The review of the
  library checks that each has at least one scenario.
- **A scenario becomes shocks to every factor** in two steps: shocks are set on the factors that drive the scenario, and
  the other factors are filled in from how they moved with those factors in the past.
- **Shock sizes** come from data, where the risk engine computes them from a historical episode, or from the risk
  manager. The AI proposes the story and never the size.
- **Reverse stress** works back from the loss that would break the mandate: the risk engine searches for the smallest
  combination of shocks that would cause it, and the risk manager judges how plausible that combination is.

### Credit: spreads, default and migration
- **Default.** **Jump to default** is the position times one minus the expected recovery rate, which is a governed
  parameter. It is read as a concentration measure, with an early warning, because one default in a concentrated or
  high-yield portfolio can cost far more than spread volatility suggests.
- **Migration.** A downgrade shows up as wider spreads, so spread stress covers it. One event is not covered that way: a
  downgrade below a mandate's rating floor forces a sale, at a cost that depends on how long the holding takes to sell.
  An early warning therefore flags holdings close to the floor, read with their [time to
  sell](liquidity-risk.md#time-and-cost-to-sell).

### Leverage and options
Leverage is measured two ways, each with an internal limit: **gross exposure**, the sum of all positions without
netting, which shows scale; and **net exposure**, what is left after netting and hedging, which shows the risk actually
taken. Derivatives are converted to the equivalent position in the underlying before either is summed: an option by its
delta, and an interest rate derivative by its duration against a common maturity.

Options are measured by delta, gamma and vega in the daily run, and revalued in full under stress.

### Counterparty exposure
Exposure to a counterparty is the current exposure net of the collateral held under netting agreements, plus an add-on
for how far it could grow before the next collateral call. It includes the counterparties to share-class hedges and the
borrowers of lent securities, net of the collateral they have posted. The internal limit applies to the total.

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
| AI explanations | Weight on the wrong driver, even when every number is correct | How often and how much risk managers edit the drafts; a sample reviewed against the full decomposition |

## Controls and measures specific to this pillar
The general [controls](../framework/08-controls.md) apply in full. This pillar adds four.

- **Decomposition reconciles before drafting.** The contributions by position and by factor must add up to the total
  change, within a stated tolerance, before the AI drafts from them. A decomposition that does not reconcile is an
  exception in its own right.
- **Silence is not a clean result.** A portfolio with missing or incomplete data is shown as not assessed, never as
  having nothing to report, as set out in [risk data](../framework/03-risk-data.md#quality-before-computation).
- **Messages are sent by the risk manager.** Drafted messages to portfolio managers are never sent automatically.
- **The scenario library is governed.** Scenarios the AI proposes are recorded as proposals; the risk manager's
  calibration and approval are recorded before a scenario enters the library.

Of the measures in [measuring value](../framework/09-measuring-value.md), speed and capacity matter most here.

| Dimension | Measure for this pillar |
|---|---|
| Speed | Time from data availability to the first message to a portfolio manager |
| Capacity | Portfolios reviewed in depth per day |
| Quality | Issues found late, for example a limit breach first noticed by someone else |
| Influence | Issues raised with portfolio managers and actions taken |
| Pillar-specific | Share of drafts that needed substantive edits; backtesting breaches within expectation |

## Sources
- Basel Committee on Banking Supervision (1996). *Supervisory Framework for the Use of "Backtesting" in Conjunction with
  the Internal Models Approach to Market Risk Capital Requirements.* The green, amber and red zones for reading a count
  of breaches.
- International Organization of Securities Commissions (2019). *Recommendations for a Framework Assessing Leverage in
  Investment Funds.* Gross and net exposure, with derivatives converted to the equivalent position in the underlying.
- Jorion, P. (2006). *Value at Risk: The New Benchmark for Managing Financial Risk*, 3rd edition. McGraw-Hill. Value at
  risk, expected shortfall, stress testing and backtesting.
- Litterman, R. (1996). Hot Spots and Hedges. *Journal of Portfolio Management*, special issue. Decomposing a change in
  risk by position and factor, and marginal risk for what-ifs.
- Grinold, R. and Kahn, R. (2000). *Active Portfolio Management*, 2nd edition. McGraw-Hill. Ex-ante tracking error and
  allotting active risk to bets.
- Kupiec, P. (1995). Techniques for Verifying the Accuracy of Risk Measurement Models. *Journal of Derivatives*.
  Counting value at risk breaches against the number expected.
- Christoffersen, P. (1998). Evaluating Interval Forecasts. *International Economic Review*. Testing whether breaches
  are independent of each other as well as correct in number.
- Acerbi, C. and Tasche, D. (2002). On the Coherence of Expected Shortfall. *Journal of Banking and Finance*. Expected
  shortfall as the average loss beyond the threshold.
- Breuer, T., Jandacka, M., Rheinberger, K. and Summer, M. (2009). How to Find Plausible, Severe and Useful Stress
  Scenarios. *International Journal of Central Banking*. Searching for the scenarios that break a portfolio, and judging
  their plausibility.
