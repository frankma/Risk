# Investment risk

Investment risk is the chance that a portfolio's outcome departs from what its mandate intends, arising from the
investments themselves. This chapter defines it, sets out what sits inside and outside its scope, and organises a risk
function's recurring work into three pillars: market, liquidity and performance risk. The pillars are a lens on
workflows rather than a taxonomy of risks, and they connect.

## Definition
**Investment risk is the chance that a portfolio's outcome departs from what its mandate intends: a loss, a shortfall
against its objective or benchmark, or an inability to meet redemptions, arising from the investments themselves.**

Three parts of this definition do the work.

- **The mandate is the reference point.** A fund that loses money when its benchmark loses more may be doing exactly
  what was promised; a fund that gains money while taking risks its mandate does not allow is not. Risk is measured
  against the promise, not against zero.
- **There are three kinds of departure.** A portfolio can lose more than its investors were led to expect, fail to
  deliver its objective or benchmark, or fail to meet redemptions fairly. Each is a distinct failure with distinct
  causes, and each maps to one pillar.
- **The source is the investments.** The definition covers risks that arise from what the portfolio holds and how it is
  funded by its investors. Risks that arise from how the firm operates belong elsewhere.

## Scope and boundaries
A risk function should be clear about where investment risk ends, so that each risk has one owner and nothing is
assumed to be covered when it is not.

Within scope, and handled inside the pillar workflows:

- **Credit risk** of the portfolio's holdings is part of market risk: spread risk, spread duration, and default and
  migration risk are measured and monitored with the other sources of loss.
- **Concentration and leverage** are part of market risk: concentration by issuer, sector, country or factor, and
  leverage and derivative exposure, are drivers of how much the portfolio could lose.
- **Counterparty exposure** is part of market risk: each fund's exposure to the firms it trades with or holds assets
  through is monitored against limits.
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
| Compliance | The legal reading of guidelines and regulation | A legal reading; the pillars monitor exposures. |
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
**Question:** How much could we lose?

**Outcome:** the risk manager knows, every day, which funds carry more absolute risk than their mandate intends, and
why.

**Covers:** absolute risk measures such as value at risk, expected shortfall, volatility and drawdown against tolerance;
sensitivities such as duration, spread duration, equity beta and currency exposure; concentration; stress, reverse
stress and scenario tests; pre-trade what-ifs; leverage and derivative exposure; and counterparty exposure against
limits. The redesigned workflow is set out in [market risk](../pillars/market-risk.md).

### Liquidity risk
**Question:** Can we meet redemptions without disadvantaging the investors who stay?

**Outcome:** the risk manager knows whether each fund can meet plausible redemptions in time and at a fair cost, and
whether the tools for managing liquidity are ready if it cannot.

**Covers:** both sides of the balance, read together. On the asset side, what the portfolio can raise and how fast: the
time and cost to liquidate holdings. On the liability side, what investors could redeem: investor and distributor
concentration, flow patterns and stressed outflows. Redemption coverage compares the two. The pillar also covers the
readiness of liquidity management tools such as swing pricing, redemption gates, in-kind redemptions and slowing
purchases of illiquid assets, and the flagging of holdings whose prices are stale or that cannot be priced. See
[liquidity risk](../pillars/liquidity-risk.md).

### Performance risk
**Question:** Is the fund delivering what was promised, in the way it was promised?

**Outcome:** the risk manager can show, with evidence, whether each fund is meeting its objective and whether its
returns come from the sources its mandate describes.

**Covers:** risk and return relative to the promise. Tracking error and active share; risk budgets against return;
outcome against benchmark, peers or objective; attribution, to test whether returns come from the intended sources;
style drift; and consistency and risk-adjusted returns. See [performance risk](../pillars/performance-risk.md).

## Boundaries between pillars
The three pillars overlap in data but not in question, and the dividing lines follow from the questions.

- **Market risk is absolute.** It asks how much the portfolio could lose in total, whatever its benchmark does.
- **Performance risk is relative.** It asks how the fund behaves against its promise, so active risk, such as tracking
  error, belongs here even though it is computed from the same positions and market data as market risk.
- **Liquidity risk is about flows and fairness.** It asks whether the fund can meet what investors take out without
  shifting cost to those who remain.

| | Market risk | Liquidity risk | Performance risk |
|---|---|---|---|
| **Lens** | Absolute loss | Assets against redemptions | Relative to the promise |
| **Typical measures** | VaR, volatility, stress tests | Liquidation cost, coverage | Tracking error, attribution |
| **Typical triggers** | A limit breach; a large move | Falling coverage; big redemption | Persistent underperformance |
| **Main audience** | Risk and portfolio managers | Risk managers, fund boards | Portfolio managers, oversight |

The table shows typical entries only; each pillar section above lists the full coverage.

Placing each measure in exactly one pillar keeps ownership clear. Where a measure serves two pillars, for example
concentration, which drives both potential loss and the cost of selling, it is computed once and read by both.

## The pillars connect
The pillars are separate lenses on one portfolio, and the most damaging episodes pass through all three.
Underperformance prompts redemptions. Redemptions force sales, and the most liquid assets are usually sold first. The
portfolio that remains is more concentrated and more volatile, which raises market risk and makes further
underperformance more likely.

A manual process tends to see these links late, because each pillar is reviewed on its own cycle by different people. A
redesigned process can watch the signals together and flag funds where they combine, which is a capability the manual
process does not have. The [integrated view](../pillars/integrated-view.md) sets this out, along with the firm's
footprint across funds.
