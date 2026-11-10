# Liquidity risk

Liquidity risk asks whether a portfolio can meet every call on its cash, in time and at a fair cost, without
disadvantaging the investors who stay. This chapter applies the [redesign method](../framework/06-redesign-method.md) to
the pillar: it lists the pillar's recurring workflows, redesigns periodic stress testing into continuous monitoring with
event-triggered stress tests, and sets out the thresholds, limits, controls and measures that make the redesign work,
and the design choices behind the pillar's measures. The redesign is a new capability, not only a faster version of the
old process: the risk function sees a portfolio's liquidity when an event happens, not when the calendar says so.

## The outcome
The pillar's outcome, as defined in [investment risk](../framework/01-investment-risk.md#liquidity-risk):

> The risk manager knows whether each portfolio can meet plausible calls on its cash in time and at a fair cost, and
> whether the tools for managing liquidity are ready if it cannot.

"At a fair cost" carries the pillar's purpose. When an open-ended fund meets redemptions by selling its most liquid
holdings, the investors who stay are left with a less liquid and more concentrated portfolio, and they bear the cost of
the selling. The pillar exists to protect them from that transfer, as well as to make sure redemptions are met at all.
Liquidity management tools, such as swing pricing, redemption gates, in-kind redemptions and slowing purchases of
illiquid assets, are the means of doing so, and their readiness is part of the outcome.

The calls on cash differ by vehicle, and so does the question of fairness. An open-ended fund faces redemptions, and
fairness is between the investors who leave and those who stay. A segregated mandate has one client, so the question
is whether the client's withdrawals and planned cash needs can be met in time and at a fair cost. A closed-ended fund
faces no redemptions, but must roll over its borrowing, pay its distributions and meet its commitments. Any portfolio
that holds derivatives faces margin and collateral calls, which press on both sides of the balance at once: they arrive
when markets fall, and the collateral they take is encumbered and can no longer be sold to meet other calls. The
pillar's measures leave encumbered assets out of what a portfolio can raise.

## Workflows in this pillar

| Workflow | Cadence | Output | Used by | For which decision |
|---|---|---|---|---|
| Liquidity monitoring and stress tests | Daily; on events | Coverage, stress results | Risk manager | Whether to act |
| Redemption and cash-call monitoring | Daily | Flows, margin and other calls against the portfolio's history | Risk manager | Whether calls are unusual |
| Investor and distributor concentration | Daily | Largest holders' shares | Risk manager | Whether it is too high |
| Liquidity tool readiness | Quarterly | Readiness of each tool | Risk manager, fund board | Whether tools can be used |
| Board reporting | Monthly | Liquidity paper | Fund board | Whether liquidity is adequate |
| Stale or unpriceable holdings | Daily | Flagged holdings | Pricing owner | Whether prices need challenge |

Liquidity monitoring and stress testing is the flagship, because it is where the calendar-driven process leaves the
largest gap. Monitoring of redemptions, other calls and concentration becomes an input to it: they are the sources of
the triggers that run the stress test. Board reporting draws on the period's monitoring rather than being a separate
exercise. The daily run also computes the firm's share of each issue and of each market's daily volume for the [firm's
footprint](integrated-view.md#the-firms-footprint).

Flagging stale or unpriceable holdings is the measuring side of valuation risk that this pillar owns, as set out in
[investment risk](../framework/01-investment-risk.md#scope-and-boundaries). The risk function flags the holdings and
knows which of its measures rest on them; setting and challenging the prices remains with the owner of pricing.

## Flagship redesign: from periodic stress testing to continuous liquidity monitoring
The example below follows the liquidity work for a range of 40 portfolios, assessed monthly in the current state. **The
steps, hours and elapsed times are illustrative.**

**Current state.** Each month, the risk manager builds a liquidity assessment for every portfolio and a paper for the
fund board.

| # | Step | Tag | Hours | Elapsed |
|---|---|---|---|---|
| 1 | Pull holdings and trading volumes for every portfolio | Gather | 6 | 2 days |
| 2 | Assign each holding to a liquidity bucket from its trading volume | Compute | 8 | 2 days |
| 3 | Apply redemption scenarios in the workbook | Compute | 6 | 1 day |
| 4 | Second person checks the workbook | Approve / Wait | 3 | 2 days |
| 5 | Explain the results for each portfolio | Interpret | 6 | 2 days |
| 6 | Decide which portfolios need attention and what to recommend | Judge | 2 | 1 day |
| 7 | Write the paper for the fund board | Communicate | 6 | 2 days |
| 8 | Review and sign off the paper | Approve / Wait | 2 | 3 days |

The cycle takes 39 hours and 15 working days. The result is a snapshot of holdings and flows at the start of the
cycle, around three weeks old by the time the board reads it. An event in the middle of the month, such as a large
redemption, is either handled outside the process by hand or waits for the next cycle.

**Owner assignment.**

- Steps 1 to 3 move to the risk engine, which assigns liquidity to every holding and applies the scenarios every day.
- Step 4 is replaced by the grounding check and the system's reconciliation to source, and is eliminated as a manual
  step.
- Steps 5 and 7 become AI drafts: the narrative for each portfolio, and the board paper.
- Step 6 stays with the risk manager, who also proposes the calibration of the scenarios, which the risk function owns,
  and makes the recommendation on whether to use liquidity management tools.
- Step 8 stays with the head of risk.

**Redesigned flow.** Hours are per month. Step 6 assumes four triggered portfolios in the month at half an hour each.

| # | Step | Owner | Hours | Elapsed |
|---|---|---|---|---|
| 1 | Compute each portfolio's liquidity profile and redemption coverage | Risk engine | 0 | Daily |
| 2 | Monitor flows, margin calls and investor concentration against each portfolio's history | Risk engine | 0 | Daily |
| 3 | Run the stress test when an event trigger fires | Risk engine | 0 | Same day |
| 4 | Draft the narrative for each triggered portfolio | AI assistant | 0 | Same day |
| 5 | Grounding check on every draft | Risk engine | 0 | Same day |
| 6 | Review each triggered portfolio; recommend on liquidity tools | Risk manager | 2 | Same day |
| 7 | Draft the board paper from the period's results and events | AI assistant | 0 | Minutes |
| 8 | Review scenario calibration; edit the board paper | Risk manager | 4 | 2 days |
| 9 | Review and sign off the paper | Head of risk | 1 | 1 day |

The work falls to 7 hours a month, and the board paper is ready 3 working days after the end of the period rather
than 15. The larger change is in timing: a portfolio's liquidity is current every day, and an event is assessed on the
day it happens rather than at the next cycle.

**The shift.** Liquidity work moves from calendar-driven to event-driven. The manual process could not run a stress
test every time a large redemption arrived, concentration rose or market liquidity worsened, because each run took
days. The redesigned process does exactly that, which is a capability the old process did not have at any speed.

## Materiality and exceptions
An **exception** in this pillar is a rule that has fired: a reading that shows a portfolio may not meet its calls on
cash fairly, or an event that should trigger the stress test. A **watch item** is a reading drifting towards a
threshold. Each rule is a [governed
parameter](../framework/07-controls.md#materiality-thresholds-as-governed-parameters). **The example values below are
illustrative and are not recommendations;** each risk function sets its own.

| Kind of rule | Example (illustrative) | What it catches |
|---|---|---|
| Redemption coverage | Unencumbered liquid assets below a set multiple of the stressed calls on cash | Portfolios that may not meet their calls |
| Large redemption | A single redemption above a set share of net assets | Events that change the profile |
| Margin and collateral calls | Calls under stress above a set share of unencumbered liquid assets | Derivative positions draining liquidity |
| Flows against history | Net outflows outside the portfolio's usual range | Unusual investor behaviour |
| Investor and distributor concentration | One investor or distributor above a set share of the portfolio | Dependence on few investors or distributors |
| Market liquidity | Time or cost to liquidate rising above a set level | Assets becoming harder to sell |
| Stale or unpriceable | No price change for a set number of trading days | Holdings whose value is uncertain |

The large redemption, margin and collateral call, investor and distributor concentration, and market liquidity rules are
also triggers: when one fires, the risk engine runs the stress test for that portfolio the same day. Every rule in the
table gives an exception when it fires; a reading drifting towards one of those thresholds, such as coverage falling
towards its threshold, is a watch item. The risk engine ranks exceptions before watch items: portfolios with coverage
below its threshold come first, then portfolios with a fired trigger, then other exceptions, then watch items. Stale and
unpriceable holdings are listed separately and routed to the owner of pricing, as well as being shown against the
measures they affect.

## What the AI drafts
The AI drafts from the facts that the risk engine produced and from nothing else. Every number in each draft appears in
the facts beside it, so the [grounding check](../framework/07-controls.md#the-grounding-check) would pass. **The
funds and figures are illustrative.**

**A large redemption.**

| Fact | Value |
|---|---|
| Fund | Fund D |
| Redemption notified | 6.5% of net assets |
| Large-redemption trigger | 5.0% of net assets |
| Redemption coverage before / after | 2.4x / 1.6x |
| Coverage threshold | 1.5x |
| Share of the redemption met from the most liquid holdings | 80% |

> Fund D has received a redemption notice for 6.5% of net assets, above the 5.0% trigger, and the stress test has been
> rerun. Redemption coverage falls from 2.4x to 1.6x, still above the 1.5x threshold. 80% of the redemption would be
> met from the most liquid holdings, leaving the investors who stay with a less liquid portfolio.

**Rising investor concentration.**

| Fact | Value |
|---|---|
| Fund | Fund E |
| Largest investor's share, today / three months ago | 18% / 11% |
| Single-investor trigger | 15% |
| Top five investors' share | 46% |
| Days to liquidate 18% of the portfolio at normal volumes | 7 |

> The largest investor in Fund E now holds 18% of the portfolio, up from 11% three months ago and above the 15% trigger.
> Meeting a full redemption by that investor would take 7 days of selling at normal volumes. The top five investors
> together hold 46%.

**Stale prices.**

| Fact | Value |
|---|---|
| Fund | Fund F |
| Holdings with no price change for 10 or more trading days | 3 |
| Their share of net assets | 4.2% |

> 3 holdings in Fund F, together 4.2% of net assets, have had no price change for at least 10 trading days. They have
> been flagged to the owner of pricing for review.

None of the drafts recommends whether to use a liquidity management tool. That recommendation is the risk manager's.

## Design choices
A risk function chooses how each of its liquidity measures is computed, and records the choice. This section sets out
the choices for this pillar, what each trades off, and how the function tests what it chose. The risk function owns the
model risk in its own liquidity measures; independent validation of the models sits elsewhere, as set out in
[investment risk](../framework/01-investment-risk.md#scope-and-boundaries).

### Fairness and capacity
A portfolio can meet a call on its cash in two ways, and each answers a different question, so both are computed.

| Way of selling | What it answers | What it shows |
|---|---|---|
| A slice of every holding | The fairness test: can the call be met without changing the portfolio the investors who stay are left with? | The time and cost of selling in proportion |
| The most liquid first | The capacity test: how much can be raised, and how fast? | The most the portfolio can raise in each period |

Redemption coverage reads the capacity test, because it asks whether the call can be met at all. The gap between the
two is shown beside it: it measures how much of the cost of meeting the call would be shifted onto the investors who
stay if the portfolio sold its most liquid holdings first, which is the "fair cost" in the pillar's outcome made
measurable.

### Time and cost to sell
| Choice | Options | Trade-off |
|---|---|---|
| Time | Fixed buckets by asset type; a capped share of each holding's daily volume | Buckets are simple but blind to size; a share of volume scales with the position |
| Volumes under stress | Normal volumes; volumes reduced by a stress factor | Normal volumes flatter exactly when liquidity matters |
| Cost | The bid-offer spread alone; the spread plus a market-impact model | The spread alone misses the price move that a large sale causes |

**Illustrative setup** (not a recommendation): time from a capped share of each holding's daily volume, with volumes
reduced under stress; cost as half the bid-offer spread plus a market-impact term that rises with the square root of
the trade's size relative to daily volume, scaled by the holding's volatility. Both are standard and transparent, and
both become more conservative under stress.

### Calls on cash
The calls a portfolio could face are built from three scenarios, and **the worst of the three binds**:

- **The portfolio's own history:** the largest outflows it has seen over a set horizon.
- **Behaviour by investor type:** stressed outflows applied by type of investor, since retail investors on platforms,
  institutions and funds of funds behave differently.
- **Concentration:** the largest investors, or the investors behind the largest distributors, leave at once.

Each scenario catches a failure the others miss: history misses what has not happened yet, behaviour by type misses a
single large holder, and concentration misses a broad run. For other vehicles, the same three views apply to the calls
they face: a segregated mandate's withdrawals and planned cash needs, a closed-ended fund's borrowing to roll over,
distributions and commitments, and margin and collateral calls on any portfolio that holds derivatives.

### Encumbrance and second-round effects
- **Encumbered assets are not liquid.** Collateral already posted, and assets lent out, are left out of what a
  portfolio can raise.
- **Margin calls press on both sides.** In a stressed scenario, the same market move that cuts liquidity raises margin
  and collateral calls, and the collateral posted against them is then encumbered, so the scenario applies both at once.
- **The firm's own selling moves prices.** When several portfolios sell the same holdings, the firm's combined sale is
  larger than any one portfolio's, and so is its cost. The stress uses the firm's share of each issue and of each
  market's daily volume from the [firm's footprint](integrated-view.md#the-firms-footprint), so that the cost of
  selling reflects the whole firm's sale.

The readiness of liquidity management tools is assessed as set out under the pillar's workflows; how each tool is
calibrated sits outside these design choices.

### Where the measures are weak
| Measure | Where it is weak | How the function tests it |
|---|---|---|
| Time and cost to liquidate | Volumes and costs worsen under stress | Comparison with trading in stressed periods |
| Market-impact model | Impact depends on who else is selling | Comparison with the cost of past large sales |
| Scenarios for calls on cash | Investor behaviour differs from the assumption | Comparison with realised flows |
| Redemption coverage | Outflows and market stress tend to arrive together | Scenarios that stress both sides at once |
| Margin and collateral calls | Calls rise with the market moves that cut liquidity | One market shock applied to margin and to liquidity together |
| Any measure using prices | Stale prices make holdings look stable | Stale flags; sale prices against prior prices |

Liquidity estimates assume that past trading volumes and costs hold under stress, and they often do not: the assets
that are easy to sell in normal markets can become hard to sell exactly when redemptions rise. Scenarios for calls on
cash rest on assumptions about how investors behave, which are tested against the flows that actually occur. Stale
prices make illiquid holdings look more stable than they are, which understates both their risk and the cost of
selling them; where realised sale prices differ from prior prices, the difference is evidence for the owner of pricing.

The AI step has its own limit: a narrative can describe a portfolio's position accurately and still understate how
urgent it is. The function tests this by reviewing how risk managers edit the narratives for triggered portfolios, and
by checking a sample against the full stress results.

## Controls specific to this pillar
The general controls in [controls](../framework/07-controls.md) apply in full. This pillar adds four.

- **Every trigger is recorded.** Each firing, the stress test it ran and the result are kept in the audit trail, so the
  record shows that an event was assessed, and when.
- **Scenario calibration is governed.** Outflow assumptions and stress adjustments to liquidation time and cost are
  governed parameters owned by the risk function, with every change recorded.
- **The recommendation is not drafted.** The AI drafts the facts and the narrative; the recommendation on liquidity
  management tools is written by the risk manager.
- **Investor data is minimised.** Facts sent to an AI service describe shares and flows, not investor identities, in
  line with [data handling](../framework/07-controls.md#data-handling).

## Measuring value
The measures from [measuring value](../framework/08-measuring-value.md) that matter most for this pillar are speed and
quality: how soon an event is assessed, and whether any event is missed.

| Dimension | Measure for this pillar |
|---|---|
| Speed | Time from a triggering event to a stress result and narrative |
| Speed | Working days from period end to signed-off board paper |
| Capacity | Portfolios with a current liquidity view |
| Quality | Events assessed late or not at all; parallel-run agreement on coverage |
| Influence | Recommendations on liquidity tools made and acted on |
| Pillar-specific | Age of the liquidity view when a decision is made |

The pillar-specific measure captures the new capability directly. In the flagship example, the liquidity view that
informs a decision falls from as much as a month old to a day old, and the board paper is signed off 3 working days
after period end instead of 15. (The figures are illustrative.)

## Connections
Liquidity risk sits between the other two pillars. Rising volatility and concentration from
[market risk](market-risk.md) raise the time and cost of selling; stale prices flagged here weaken the measures that
pillar relies on. Underperformance from [performance risk](performance-risk.md) often comes before redemptions, so
flows in underperforming portfolios are watched more closely. In the other direction, meeting redemptions by selling the
most liquid holdings leaves a more concentrated and more volatile portfolio, which raises market risk. The
[integrated view](integrated-view.md) brings these signals together for each portfolio.

## Sources
- International Organization of Securities Commissions (2025). *Revised Recommendations for Liquidity Risk Management
  for Collective Investment Schemes.* Matching assets to redemption terms, stress testing and liquidity management
  tools.
- International Organization of Securities Commissions (2023). *Anti-dilution Liquidity Management Tools: Guidance for
  Effective Implementation of the Recommendations for Liquidity Risk Management for Collective Investment Schemes.*
  Swing pricing and other tools that charge the cost of selling to the investors who leave.
- Financial Stability Board (2023). *Revised Policy Recommendations to Address Structural Vulnerabilities from Liquidity
  Mismatch in Open-Ended Funds.* Liquidity of assets set against the dealing terms an open-ended fund offers.
- Brunnermeier, M. and Pedersen, L. (2009). Market Liquidity and Funding Liquidity. *Review of Financial Studies*. How
  margin calls and falling market liquidity reinforce each other.
- European Securities and Markets Authority (2019). *Guidelines on Liquidity Stress Testing in UCITS and AIFs.*
  Stressing both sides of the balance, with a method of selling that reflects how the portfolio would be sold.
- Bouchaud, J.-P., Bonart, J., Donier, J. and Gould, M. (2018). *Trades, Quotes and Prices: Financial Markets Under the
  Microscope.* Cambridge University Press. The square-root law of market impact.
