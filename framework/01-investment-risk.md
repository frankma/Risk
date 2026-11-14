# Investment risk

## In short
**The definition:** investment risk is the chance that a portfolio's outcome departs from what its mandate intends: a
loss, a shortfall against its objective or benchmark, or an inability to meet calls on its cash, such as redemptions,
arising from what the portfolio holds and how it is funded, not from how the firm operates.

**The mandate is the reference point:** risk is measured against the promise, not against zero. The three kinds of
departure are distinct failures with distinct causes, and each maps to one pillar.

**Three pillars organise the recurring work.** They are a lens on workflows, not a taxonomy of risks. Each pillar's
question opens its own chapter.

| Pillar | Outcome |
|---|---|
| [Market risk](../pillars/market-risk.md) | The risk manager knows, every day, which portfolios carry more risk than their mandate intends, absolute or relative, and why |
| [Liquidity risk](../pillars/liquidity-risk.md) | The risk manager knows whether each portfolio can meet plausible calls on its cash in time and at a fair cost, and whether the tools for managing liquidity are ready if it cannot |
| [Performance risk](../pillars/performance-risk.md) | The risk manager can show, with evidence, whether each portfolio is meeting its objective and whether its returns come from the sources its mandate describes |

**The scope:** every fund and segregated mandate, except money market funds, exchange-traded funds and advised model
portfolios. Risks from how the firm operates are owned elsewhere.

**The pillars connect:** the most damaging episodes pass through all three, and the [integrated
view](../pillars/integrated-view.md) watches the signals together.

The rest of this chapter is the detail behind these points. The beliefs behind the definition are in the
[philosophy](00-philosophy.md).

## Portfolios, funds and mandates
The framework covers open-ended and closed-ended funds and segregated mandates, across benchmarked long-only, absolute
return and other objective-based strategies, multi-asset, long-short and leveraged strategies, fixed income and credit,
and funds of funds, which are read through to their holdings. It calls each a **portfolio**, and says fund or mandate
only where the type matters. **The mandate** is the promise, whatever the vehicle: the objective, benchmark, style,
limits and dealing or withdrawal terms in the governing documents.

Three kinds of portfolio sit outside it:

- **Money market funds,** which follow a specialised regime of their own.
- **Exchange-traded funds,** because units are created and redeemed through authorised participants, so the calls on the
  fund's cash do not work as the liquidity pillar assumes.
- **Model portfolios the firm advises on but does not hold,** whose positions and risks sit with the party that
  implements them.

## Scope and boundaries
A risk function should be clear about where investment risk ends, so that each risk has one owner and nothing is assumed
to be covered when it is not.

Within scope, and handled inside the pillar workflows:

- **Credit risk** of the holdings, including default and migration, is in [market
  risk](../pillars/market-risk.md#credit-default-and-migration).
- **Concentration, leverage and derivative exposure** are in market risk.
- **Counterparty exposure,** to the firms a portfolio trades with, lends securities to or holds assets through, is in
  market risk.
- **Weak and stale prices** are flagged in liquidity risk.
- **The limits of the risk function's own measures,** including any AI step, are tested in every pillar.

Counterparty, valuation and model risk are therefore split. Investment risk measures and monitors; approval, pricing and
independent validation sit with functions independent of the measure's user. Market risk takes prices as fair, liquidity
risk flags where they may not be, and the owner of pricing sets and challenges them.

At the boundary, and owned elsewhere:

| Risk | What it covers | Why it sits outside |
|---|---|---|
| Operational risk | Errors, systems, processes, outsourcing | Arises from how the firm operates. |
| Compliance | The legal reading of guidelines and regulation, the monitoring of position and eligibility rules, and the breach report for every mandate and regulatory limit | A legal reading; the pillars monitor exposures and risk-measured limits, and route or report breaches. |
| Business risk | Fees, flows into the firm, its own balance sheet | Concerns the firm's results, not the portfolio's. |
| Counterparty approval | Approving which counterparties may be used | Independent of those who trade with them. |
| Pricing | Setting and challenging the prices of holdings | Independent of those who use the prices. |
| Model validation | Independent validation of models across the firm, including the AI steps in the risk function's workflows | Independent of those who build and use them. |
| Sustainability risk | Environmental, social and governance events that could lower a holding's value, and the portfolio's own sustainability commitments | Owned by a sustainability function; the pillars take its data as an input. |
| Strategy capacity | How much money a strategy can run before its returns suffer | A decision about the investment business, owned by the chief investment officer; liquidity risk's figures are an input. |

A boundary is not a wall. Signals that matter to the owner of an adjacent risk, such as a holding flagged as unpriceable
or a breach that may have a legal reading, are routed to that owner rather than resolved inside the pillar.

## The three pillars
Each pillar's question and outcome are at the top of this chapter. The pillars overlap in data but not in question, and
market and performance risk are divided by time.

| | Market risk | Liquidity risk | Performance risk |
|---|---|---|---|
| **Lens** | What could happen, from today's holdings, absolute and relative | Calls on cash against what the portfolio can raise | What did happen, and whether the promise is kept |
| **Covers** | Value at risk, expected shortfall and volatility; ex-ante tracking error and the risk budget; sensitivities; concentration; stress, reverse stress and the drawdown headroom they leave; pre-trade what-ifs; leverage; counterparty exposure | Time and cost to sell, leaving out encumbered assets; every call on cash the vehicle faces; redemption coverage; readiness of liquidity management tools; stale and unpriceable holdings | Outcome against benchmark, peers or objective; ex-post tracking error and realised drawdown; attribution, including the split between the [sources of return](02-sources-of-return.md); active share and style drift; risk-adjusted returns |
| **Typical triggers** | A limit breach; a large move | Falling coverage; a large redemption or margin call | Significant underperformance |
| **Main audience** | Risk and portfolio managers | Risk managers, fund boards | Portfolio managers, investment oversight |

Two rules keep the pillars apart.

- **Each measure has one owner.** A measure that serves two pillars, such as concentration, which drives both potential
  loss and the cost of selling, is computed once and read by both.
- **Each forecast has a realised counterpart.** Ex-ante tracking error is tested against ex-post, value at risk against
  realised losses, and the drawdown performance risk measures sets the headroom market risk reads under stress.

Each pillar's chapter sets out its workflows: [market risk](../pillars/market-risk.md), [liquidity
risk](../pillars/liquidity-risk.md) and [performance risk](../pillars/performance-risk.md).

## Sources
- Financial Stability Board (2023). *Revised Policy Recommendations to Address Structural Vulnerabilities from Liquidity
  Mismatch in Open-Ended Funds.* Liquidity matched to dealing terms as part of what an open-ended fund promises.
- International Organization of Securities Commissions (2025). *Revised Recommendations for Liquidity Risk Management
  for Collective Investment Schemes.* Both sides of the liquidity balance, and the tools for managing it.
