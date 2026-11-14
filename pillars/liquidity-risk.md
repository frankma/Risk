# Liquidity risk

## In short
**The question:** can a portfolio meet every call on its cash, in time and at a fair cost, without disadvantaging the
investors who stay?

**The outcome:**

> The risk manager knows whether each portfolio can meet plausible calls on its cash in time and at a fair cost, and
> whether the tools for managing liquidity are ready if it cannot.

**How the work is done:** the risk engine measures every portfolio's liquidity every day and runs a stress test on the
day an event fires a trigger, not when the calendar says so. The AI drafts the narrative for each triggered portfolio
and the board paper. The risk manager reviews each triggered portfolio and makes any recommendation on liquidity
management tools.

| # | Step | Owner |
|---|---|---|
| 1 | Compute each portfolio's liquidity profile and redemption coverage | Risk engine |
| 2 | Monitor flows, margin calls and investor concentration against each portfolio's history | Risk engine |
| 3 | Run the stress test when an event trigger fires | Risk engine |
| 4 | Draft the narrative for each triggered portfolio | AI assistant |
| 5 | Grounding check on every draft | Risk engine |
| 6 | Review each triggered portfolio; recommend on liquidity tools | Risk manager |
| 7 | Draft the board paper from the period's results and events | AI assistant |
| 8 | Review scenario calibration; edit the board paper | Risk manager |
| 9 | Review and sign off the paper | Head of risk |

**What "a fair cost" means:** the investors who stay must not bear the cost of others leaving, and liquidity management
tools are the means. A segregated mandate has one client, so the question is whether the client's withdrawals and
planned cash needs can be met in time and at a fair cost.

**Where it connects:** [market risk](market-risk.md) raises the time and cost of selling, underperformance in
[performance risk](performance-risk.md) often comes before redemptions, and the [integrated view](integrated-view.md)
reads them together.

The rest of this chapter is the detail behind these points.

## Workflows in this pillar

| Workflow | Cadence | Output | Used by | For which decision |
|---|---|---|---|---|
| Liquidity monitoring and stress tests | Daily; on events | Coverage, stress results | Risk manager | Whether to act |
| Redemption and cash-call monitoring | Daily | Flows, margin and other calls against the portfolio's history | Risk manager | Whether calls are unusual |
| Investor and distributor concentration | Daily | Largest holders' shares | Risk manager | Whether it is too high |
| Liquidity tool readiness | Quarterly | Readiness of each tool | Risk manager, fund board | Whether tools can be used |
| Board reporting | Monthly | Liquidity paper | Fund board | Whether liquidity is adequate |
| Stale or unpriceable holdings | Daily | Flagged holdings | Pricing owner | Whether prices need challenge |

Liquidity monitoring and stress testing is the flagship, shown in the table at the top.

- **Monitoring of redemptions, other calls and concentration** feeds it: these are the sources of the triggers that run
  the stress test.
- **Board reporting** draws on the period's monitoring and is not a separate exercise.
- **Investigations.** Between triggers, the risk manager can ask what a redemption of a given size, or the loss of a
  named distributor, would do to a portfolio's coverage. The AI runs the stress test through the risk engine with those
  parameters and reports the result with the run behind it, as set out in [working with
  AI](../framework/06-working-with-ai.md#three-modes-of-working).
- **Stale or unpriceable holdings** are shown against the measures that rest on them.
- **Liquidity tool readiness.** A tool is ready when the governing documents provide for it, the operations to apply it
  have been tested, and the decision to use it has a named owner and a process.
- **The firm's footprint.** The daily run computes the firm's share of each issue and of each market's daily volume for
  the [firm's footprint](integrated-view.md#the-firms-footprint).

## Materiality and exceptions
An **exception** in this pillar is a reading that has crossed a rule's threshold, and a **watch item** is a reading
drifting towards one. A rule marked as a trigger also runs the stress test for that portfolio the same day. Each rule is
a [governed parameter](../framework/08-controls.md#materiality-thresholds-as-governed-parameters). **The example values
below are illustrative and are not recommendations;** each risk function sets its own.

| Kind of rule | Example (illustrative) | What it catches | Trigger |
|---|---|---|---|
| Redemption coverage | Unencumbered liquid assets that can be raised within the limit's horizon, below a set multiple of the stressed calls on cash due within it | Portfolios that may not meet their calls | No |
| Large redemption | A single redemption above a set share of net assets | Events that change the profile | Yes |
| Margin and collateral calls | Calls under stress above a set share of unencumbered liquid assets | Derivative positions draining liquidity | Yes |
| Flows against history | Net outflows outside the portfolio's usual range | Unusual investor behaviour | No |
| Investor and distributor concentration | One investor or distributor above a set share of the portfolio | Dependence on few investors or distributors | Yes |
| Market liquidity | Time or cost to liquidate rising above a set level | Assets becoming harder to sell | Yes |
| Stale or unpriceable | No price change for a set number of trading days | Holdings whose value is uncertain | No |

The risk engine ranks exceptions before watch items: portfolios with coverage below its threshold come first, then
portfolios with a fired trigger, then other exceptions, then watch items. Stale and unpriceable holdings are also listed
separately and routed to the owner of pricing.

Where the governing documents or regulation set a liquidity limit, it is a [risk-measured hard
limit](../framework/04-limits-and-escalation.md#where-limits-come-from): the risk function monitors it, a breach must be
cured, and compliance writes the breach report. The internal limit on redemption coverage sits inside it.

## What the AI drafts
The AI drafts from the facts that the risk engine produced and from nothing else. Every number in the draft appears in
the facts beside it, so the [grounding check](../framework/08-controls.md#the-grounding-check) would pass. **The fund
and figures are illustrative.**

| Fact | Value |
|---|---|
| Fund | Fund D |
| Redemption notified | 6.5% of net assets |
| Large-redemption trigger | 5.0% of net assets |
| Redemption coverage before / after | 2.4x / 1.6x |
| Coverage threshold | 1.5x |
| Share of the redemption met from the most liquid holdings | 80% |

> Fund D has received a redemption notice for 6.5% of net assets, above the 5.0% trigger, and the stress test has been
> rerun. Redemption coverage falls from 2.4x to 1.6x, still above the 1.5x threshold. 80% of the redemption would be met
> from the most liquid holdings.

The draft does not recommend whether to use a liquidity management tool. That recommendation is the risk manager's.

## Design choices
A risk function chooses how each of its liquidity measures is computed, records the choice and tests it. Independent
validation of the models sits outside the risk function, as set out in [investment
risk](../framework/01-investment-risk.md#scope-and-boundaries).

### Fairness and capacity
A portfolio can meet a call on its cash in two ways, and each answers a different question, so both are computed.

| Way of selling | What it answers | What it shows |
|---|---|---|
| A slice of every holding | The fairness test: can the call be met without changing the portfolio the investors who stay are left with? | The time and cost of selling in proportion |
| The most liquid first | The capacity test: how much can be raised, and how fast? | The most the portfolio can raise in each period |

The first is also called vertical slicing, or selling pro rata, and the second horizontal slicing, or a waterfall.
Redemption coverage reads the capacity test, because it asks whether the call can be met at all. The gap between the two
is shown beside it: it measures how much of the cost of meeting the call would be shifted onto the investors who stay if
the portfolio sold its most liquid holdings first, which is the "fair cost" in the pillar's outcome made measurable.

**Coverage has a horizon.** Assets that take a month to sell do not cover a call due in two days, so coverage compares
what can be raised within a period with the calls due within it. It is shown over several horizons, illustrated here as
1 day, 1 week and 1 month. The internal limit applies at the horizon that matches the portfolio's dealing frequency,
notice period and settlement period, because that is how long the portfolio has to pay.

### Time and cost to sell
| Choice | Options | Trade-off |
|---|---|---|
| Time | Fixed buckets by asset type; a capped share of each holding's daily volume | Buckets are simple but blind to size; a share of volume scales with the position |
| Volumes under stress | Normal volumes; volumes reduced by a stress factor | Normal volumes flatter exactly when liquidity matters |
| Cost | The bid-offer spread alone; the spread plus a market-impact model | The spread alone misses the price move that a large sale causes |

**Illustrative setup** (not a recommendation): time from a capped share of each holding's daily volume, with volumes
reduced under stress; cost as half the bid-offer spread plus a market-impact term that rises with the square root of the
trade's size relative to daily volume, scaled by the holding's volatility.

### Calls on cash
The calls a portfolio could face are built from three scenarios, and **the worst of the three binds**:

- **The portfolio's own history:** the largest outflows it has seen over a set horizon.
- **Behaviour by investor type:** stressed outflows applied by type of investor.
- **Concentration:** the largest investors, or the investors behind the largest distributors, leave at once.

Each scenario catches a failure the others miss: history misses what has not happened yet, behaviour by type misses a
single large holder, and concentration misses a broad run. For other vehicles, the same three views apply to the calls
they face: a segregated mandate's withdrawals and planned cash needs, a closed-ended fund's borrowing to roll over,
distributions and commitments, and margin and collateral calls on any portfolio that holds derivatives.

Two further calls are counted in every scenario, because they arrive whatever investors do.

- **Currency hedges that roll.** A hedge that has lost value is settled in cash when it rolls. This covers a portfolio's
  own hedges and the hedges of its hedged share classes: the loss belongs to the class, but it is paid from the
  portfolio's cash.
- **Securities lending.** Cash collateral is returned when a loan ends, so where it has been reinvested, the
  reinvestment is measured for time and cost to sell like any other holding. A security on loan can be sold only once it
  has been recalled, which the next section covers.

### Encumbrance and second-round effects
- **Encumbered assets are not liquid.** Collateral already posted is left out of what a portfolio can raise, and a
  security on loan is left out until the end of its recall period.
- **Margin calls press on both sides.** In a stressed scenario, the same market move that cuts liquidity raises margin
  and collateral calls, and the collateral posted against them is then encumbered, so the scenario applies both at once.
- **The firm's own selling moves prices.** When several portfolios sell the same holdings, the firm's combined sale is
  larger than any one portfolio's, and so is its cost. The stress uses the firm's share of each issue and of each
  market's daily volume from the [firm's footprint](integrated-view.md#the-firms-footprint), so that the cost of selling
  reflects the whole firm's sale.

### Where the measures are weak
| Measure | Where it is weak | How the function tests it |
|---|---|---|
| Time and cost to liquidate | Volumes and costs worsen under stress, when redemptions rise | Comparison with trading in stressed periods |
| Market-impact model | Impact depends on who else is selling | Comparison with the cost of past large sales |
| Scenarios for calls on cash | Investor behaviour differs from the assumption | Comparison with realised flows |
| Redemption coverage | Outflows and market stress tend to arrive together | Scenarios that stress both sides at once |
| Margin and collateral calls | Calls rise with the market moves that cut liquidity | One market shock applied to margin and to liquidity together |
| Any measure using prices | Stale prices make holdings look stable | Stale flags; sale prices against prior prices |
| AI narratives | A narrative can be accurate and still understate how urgent a position is | How risk managers edit the narratives for triggered portfolios; a sample checked against the full stress results |

## Controls and measures specific to this pillar
The general [controls](../framework/08-controls.md) apply in full. This pillar adds four.

- **Every trigger is recorded.** Each firing, the stress test it ran and the result are kept in the audit trail, so the
  record shows that an event was assessed, and when.
- **Scenario calibration is governed.** Outflow assumptions and stress adjustments to liquidation time and cost are
  governed parameters owned by the risk function, with every change recorded.
- **The recommendation is not drafted.** The AI drafts the facts and the narrative; the recommendation on liquidity
  management tools is written by the risk manager.
- **Investor data is minimised.** Facts sent to an AI service describe shares and flows, not investor identities, in
  line with [data handling](../framework/08-controls.md#data-handling).

Of the measures in [measuring value](../framework/09-measuring-value.md), speed and quality matter most here: how soon
an event is assessed, and whether any event is missed. The pillar-specific measure captures the new capability directly.

| Dimension | Measure for this pillar |
|---|---|
| Speed | Time from a triggering event to a stress result and narrative |
| Speed | Working days from period end to signed-off board paper |
| Capacity | Portfolios with a current liquidity view |
| Quality | Events assessed late or not at all; parallel-run agreement on coverage |
| Influence | Recommendations on liquidity tools made and acted on |
| Pillar-specific | Age of the liquidity view when a decision is made |

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
- Bouveret, A. (2017). *Liquidity Stress Tests for Investment Funds: A Practical Guide.* International Monetary Fund
  Working Paper 17/226. Selling a slice of every holding against selling the most liquid first, and the redemption
  coverage ratio.
- Bouchaud, J.-P., Bonart, J., Donier, J. and Gould, M. (2018). *Trades, Quotes and Prices: Financial Markets Under the
  Microscope.* Cambridge University Press. The square-root law of market impact.
