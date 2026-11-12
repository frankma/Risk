# Investment risk

Investment risk is the chance that a portfolio's outcome departs from what its mandate intends, arising from the
investments themselves. This chapter defines it, sets out what sits inside and outside its scope, and organises a risk
function's recurring work into three pillars: market, liquidity and performance risk. The pillars are a lens on
workflows rather than a taxonomy of risks, and they connect. The beliefs behind this definition are set out in the
[philosophy](00-philosophy.md).

## The backdrop
An asset manager takes a client's money under a mandate, invests it and delivers an outcome. The mandate is the promise,
the investing runs through [top-down views and bottom-up selection](02-sources-of-return.md), and the outcome is what
the client receives. Distribution, operations and the firm's own business matter to an asset manager too, but they are
not the subject here. A risk function sits beside the investment team and looks at this chain from one angle: how far
the outcome could depart from the promise, and why.

### Portfolios, funds and mandates
The framework applies to every vehicle through which an asset manager invests for clients:

- **Open-ended pooled funds,** dealing daily or less often, where many investors share one portfolio and can redeem.
- **Closed-ended funds,** where investors cannot redeem, but the fund may borrow, pay distributions and make
  commitments.
- **Segregated mandates,** where one client's money is managed in its own portfolio under an investment management
  agreement.

It covers benchmarked long-only, absolute return and other objective-based strategies, multi-asset, long-short and
leveraged strategies, fixed income and credit, and portfolios that invest in other funds, which are read through to
their holdings. Money market funds follow a specialised regime of their own and sit outside it.

The framework calls each of these a **portfolio**, and says fund or mandate only where the type matters, as it does for
redemptions, which only open-ended funds face. **The mandate** is the promise, whatever the vehicle: the objective,
benchmark, guidelines and dealing or withdrawal terms set out in the portfolio's governing documents, which are the
prospectus of a fund or the investment management agreement of a segregated mandate.

## Definition
**Investment risk is the chance that a portfolio's outcome departs from what its mandate intends: a loss, a shortfall
against its objective or benchmark, or an inability to meet calls on its cash, such as redemptions, arising from the
investments themselves.**

Three parts of this definition do the work.

- **The mandate is the reference point.** A portfolio that loses money when its benchmark loses more may be doing
  exactly what was promised; a portfolio that gains money while taking risks its mandate does not allow is not. Risk
  is measured against the promise, not against zero.
- **There are three kinds of departure.** A portfolio can lose more than its investors were led to expect, fail to
  deliver its objective or benchmark, or fail to meet the calls on its cash in time and fairly. Each is a distinct
  failure with distinct causes, and each maps to one pillar.
- **The source is the investments.** The definition covers risks that arise from what the portfolio holds, how it is
  funded by its investors and the calls its positions make on its cash, such as margin. Risks that arise from how the
  firm operates belong elsewhere.

## Scope and boundaries
A risk function should be clear about where investment risk ends, so that each risk has one owner and nothing is
assumed to be covered when it is not.

Within scope, and handled inside the pillar workflows:

- **Credit risk** of the portfolio's holdings is part of market risk: spread risk through spread duration and duration
  times spread, default through the loss if each issuer defaulted, and migration through spread stress, all measured
  and monitored with the other sources of loss, as set out in market risk's
  [design choices](../pillars/market-risk.md#credit-spreads-default-and-migration).
- **Concentration and leverage** are part of market risk: concentration by issuer, sector, country or factor, and
  leverage and derivative exposure, are drivers of how much the portfolio could lose.
- **Counterparty exposure** is part of market risk: each portfolio's exposure to the firms it trades with or holds
  assets through is monitored against limits.
- **Weak and stale prices** are part of liquidity risk: the risk function knows which of its measures rest on prices
  that are weak or stale, and flags holdings that are stale or cannot be priced.
- **The limits of the risk function's own measures** apply to every pillar: the function understands and tests what its
  measures and tools assume and where they are weak, including any AI step in its workflows.

Counterparty, valuation and model risk are therefore split. Investment risk measures and monitors; approval, pricing
and independent validation sit with functions that are independent of the measure's user.

At the boundary, and owned elsewhere:

| Risk | What it covers | Why it sits outside |
|---|---|---|
| Operational risk | Errors, systems, processes, outsourcing | Arises from how the firm operates. |
| Compliance | The legal reading of guidelines and regulation, the monitoring of position and eligibility rules, and the breach report for every mandate and regulatory limit | A legal reading; the pillars monitor exposures and risk-measured limits, and route or report breaches. |
| Business risk | Fees, flows into the firm, its own balance sheet | Concerns the firm's results, not the portfolio's. |
| Counterparty approval | Approving which counterparties may be used | Independent of those who trade with them. |
| Pricing | Setting and challenging the prices of holdings | Independent of those who use the prices. |
| Model validation | Independent validation of models across the firm | Independent of those who build and use them. |

The valuation split needs a word of explanation. Market risk measurement takes the prices of holdings as fair: it asks
how much the portfolio could lose from those prices, not whether the prices themselves are right. Where that
assumption is weak, for example in thinly traded assets, the risk function should know which of its measures rest on
it and flag the holdings concerned. Setting the price, and challenging it, remain with the owner of pricing.

A boundary is not a wall. Risk managers will often see signals that matter to the owner of an adjacent risk, such as a
holding flagged as unpriceable or a breach that may have a legal reading, and the workflows should route those signals
to the right owner rather than resolve them inside the pillar.

## The three pillars
A risk function's recurring work answers three questions. Each pillar has a question, an outcome the workflow must
deliver, and the measures it covers.

### Market risk
**Question:** How much could we lose, in total and against the benchmark?

**Outcome:** the risk manager knows, every day, which portfolios carry more risk than their mandate intends, absolute or
relative, and why.

**Covers:** what could happen, from today's holdings. Absolute risk measures such as value at risk, expected shortfall
and volatility; relative risk, measured by ex-ante tracking error, and the risk budget that allots it to bets;
sensitivities such as duration, spread duration, duration times spread, equity beta and currency exposure;
concentration; stress, reverse stress and scenario tests, and the headroom they leave against the portfolio's drawdown
tolerance; pre-trade what-ifs; leverage and derivative exposure; and counterparty exposure against limits. The
redesigned workflow is set out in [market risk](../pillars/market-risk.md).

### Liquidity risk
**Question:** Can the portfolio meet every call on its cash, in time and at a fair cost, without disadvantaging the
investors who stay?

**Outcome:** the risk manager knows whether each portfolio can meet plausible calls on its cash in time and at a fair
cost, and whether the tools for managing liquidity are ready if it cannot.

**Covers:** both sides of the balance, read together. On the asset side, what the portfolio can raise and how fast: the
time and cost to liquidate holdings, leaving out assets already posted as collateral or otherwise encumbered. On the
liability side, the calls the portfolio could face, which depend on the vehicle: redemptions from an open-ended fund,
shown by investor and distributor concentration, flow patterns and stressed outflows; the withdrawals and planned
cash needs of a segregated mandate's client; borrowing to roll over, distributions and commitments of a closed-ended
fund; and margin and collateral calls on any portfolio that holds derivatives. Redemption coverage compares the two.
Margin calls arrive when markets fall, and the collateral they take is no longer available to sell, so they press on
both sides at once. The pillar also covers the readiness of liquidity management tools such as swing pricing,
redemption gates, in-kind redemptions and slowing purchases of illiquid assets, and the flagging of holdings whose
prices are stale or that cannot be priced. See [liquidity risk](../pillars/liquidity-risk.md).

### Performance risk
**Question:** Is the portfolio delivering what was promised, in the way it was promised?

**Outcome:** the risk manager can show, with evidence, whether each portfolio is meeting its objective and whether its
returns come from the sources its mandate describes.

**Covers:** whether the promise is kept: realised outcomes, and whether holdings match the promised style. Outcome
against benchmark, peers or objective; ex-post tracking error and realised drawdown, absolute and relative; attribution,
to test whether returns come from the intended sources, including the split between the two
[sources of return](02-sources-of-return.md); active share and style drift against the mandate terms; and consistency
and risk-adjusted returns. See [performance risk](../pillars/performance-risk.md).

## Boundaries between pillars
The three pillars overlap in data but not in question, and the dividing lines follow from the questions. Market and
performance risk are divided by time.

- **Market risk is forward-looking.** It asks what could happen from today's holdings, in total and against the
  benchmark. Ex-ante tracking error, the forecast of how far the portfolio could drift from its benchmark, belongs here
  beside value at risk, and so does the risk budget that allots it to bets.
- **Performance risk is about the promise kept.** It asks what did happen, and whether the portfolio is run the way it
  was promised: realised return, ex-post tracking error, realised drawdown and attribution, and whether holdings match
  the promised style.
- **Liquidity risk is about flows and fairness.** It asks whether the portfolio can meet the calls on its cash without
  shifting cost to the investors who remain.

| | Market risk | Liquidity risk | Performance risk |
|---|---|---|---|
| **Lens** | What could happen, absolute and relative | Calls on cash against assets | Whether the promise is kept |
| **Typical measures** | VaR, ex-ante tracking error, stress tests | Liquidation cost, coverage | Realised return, ex-post tracking error, attribution |
| **Typical triggers** | A limit breach; a large move | Falling coverage; a large redemption or margin call | Persistent underperformance |
| **Main audience** | Risk and portfolio managers | Risk managers, fund boards | Portfolio managers, oversight |

The table shows typical entries only; each pillar section above lists the full coverage.

Each measure is owned by exactly one pillar, which keeps ownership clear. Where a measure serves two pillars, for
example concentration, which drives both potential loss and the cost of selling, it is computed once and read by both.

The division by time gives each forecast a realised counterpart in the other pillar, and comparing the two tests the
forecast: ex-ante tracking error against ex-post tracking error, and value at risk against realised losses. Drawdown
works the same way. Performance risk measures how far the portfolio has fallen from its peak, absolute and relative,
and market risk reads how much headroom that leaves under stress before the drawdown tolerance is reached.

## The pillars connect
The pillars are separate lenses on one portfolio, and the most damaging episodes pass through all three.
Underperformance prompts redemptions. Redemptions force sales, and the most liquid assets are usually sold first. The
portfolio that remains is more concentrated and more volatile, which raises market risk and makes further
underperformance more likely.

A manual process tends to see these links late, because each pillar is reviewed on its own cycle by different people. A
redesigned process can watch the signals together and flag portfolios where they combine, which is a capability the
manual process does not have. The [integrated view](../pillars/integrated-view.md) sets this out, along with the firm's
footprint across portfolios.

## Sources
- Financial Stability Board (2023). *Revised Policy Recommendations to Address Structural Vulnerabilities from Liquidity
  Mismatch in Open-Ended Funds.* Liquidity matched to dealing terms as part of what an open-ended fund promises.
- International Organization of Securities Commissions (2025). *Revised Recommendations for Liquidity Risk Management
  for Collective Investment Schemes.* Both sides of the liquidity balance, and the tools for managing it.
