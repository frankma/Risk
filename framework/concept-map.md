# Concept map

This page lists the framework's main concepts: what each one is, where it is defined and which chapters use it. It
defines nothing new. The chapter named under "Defined in" is the single source for each concept, and a reader who wants
the reasoning goes there.

## Purpose and beliefs

| Concept | What it is | Defined in | Used by |
|---|---|---|---|
| Investment risk | The chance that a portfolio's outcome departs from what its mandate intends | [Investment risk](01-investment-risk.md#definition) | Every chapter |
| Sight | The few numbers worth questioning and acting on, out of millions | [Philosophy](00-philosophy.md) | The three decisions |
| Beliefs | Eight positions that decide what the rules do not | [Philosophy](00-philosophy.md#beliefs) | Market risk; any model a risk function uses |
| Three decisions | Construct, Oversee and Assess: before, during and after an investment | [Philosophy](00-philosophy.md#purpose-transparency-for-three-decisions) | Market risk's what-ifs, new portfolio review |
| Three dimensions | Condensation, drill-in and connection: what every piece of risk work provides | [Philosophy](00-philosophy.md#practice-transparency-in-three-dimensions) | All pillars |
| Decision-maker | Whoever a piece of a decomposition belongs to | [Philosophy](00-philosophy.md#2-drill-in) | Alpha and beta |
| Mandate terms | A portfolio's objective, style and limits in a form the risk engine can test, confirmed by the risk manager | [Performance risk](../pillars/performance-risk.md#flagship-redesign-the-periodic-portfolio-manager-review) | Performance risk's rules and split |

## Scope

| Concept | What it is | Defined in | Used by |
|---|---|---|---|
| The backdrop | A client's mandate, invested and delivered as an outcome: the chain a risk function looks at | [Investment risk](01-investment-risk.md#the-backdrop) | README |
| Portfolio | The general term for a fund or a segregated mandate; its mandate is the promise | [Investment risk](01-investment-risk.md#portfolios-funds-and-mandates) | Every chapter |
| Three pillars | Market, liquidity and performance risk: a lens on the recurring work, with market and performance risk divided by time into forward-looking and realised | [Investment risk](01-investment-risk.md#the-three-pillars) | Every chapter |
| Forecast against outcome | Each forward-looking measure tested against its realised counterpart in the other pillar | [Investment risk](01-investment-risk.md#boundaries-between-pillars) | Philosophy, market risk, performance risk |
| Calls on cash | Redemptions, withdrawals, margin and collateral calls, borrowing to roll over, distributions and commitments | [Investment risk](01-investment-risk.md#liquidity-risk) | Philosophy, liquidity risk |
| Measuring and approving | Investment risk measures and monitors; approval, pricing and validation sit elsewhere | [Investment risk](01-investment-risk.md#scope-and-boundaries) | Market risk, liquidity risk, controls |
| New portfolio review | What must be in place before a portfolio launches or changes materially | [New portfolio review](../pillars/new-portfolio-review.md) | Performance risk, limits and escalation |
| Risk opinion | The risk function's recorded view on a launch, with conditions; product governance decides | [New portfolio review](../pillars/new-portfolio-review.md#the-risk-functions-opinion) | That chapter only |
| Material change | A change of strategy or benchmark, a merger or a change in dealing terms, reviewed as a launch | [New portfolio review](../pillars/new-portfolio-review.md#what-the-review-covers) | Performance risk |
| Integrated view | One view that ranks portfolios where signals across pillars combine | [Integrated view](../pillars/integrated-view.md) | Principles, investment risk, all pillars |
| Firm's footprint | Holdings aggregated across portfolios, which do not net | [Philosophy](00-philosophy.md#the-firm-view) | Market risk, liquidity risk, integrated view, alpha and beta |

## Sources of return

| Concept | What it is | Defined in | Used by |
|---|---|---|---|
| Top-down view | Decides how much of which markets to hold; loosely, beta | [Sources of return](02-sources-of-return.md#what-are-the-two-sources) | Philosophy |
| Bottom-up selection | Decides which securities to hold within them; loosely, alpha | [Sources of return](02-sources-of-return.md#what-are-the-two-sources) | Philosophy |
| Policy beta | The return of the benchmark or strategic allocation in the governing documents | [Sources of return](02-sources-of-return.md#who-chose-each-part) | Alpha and beta method |
| Tilts | The manager's standing positions against that allocation, recorded when taken | [Sources of return](02-sources-of-return.md#who-chose-each-part) | Alpha and beta method |
| Timing | The return from recorded changes in exposure over time | [Sources of return](02-sources-of-return.md#who-chose-each-part) | Alpha and beta method |
| Unintended beta | Any exposure with no record that anyone chose it; a test of record, not of motive | [Sources of return](02-sources-of-return.md#who-chose-each-part) | Performance risk's source-of-return rule, alpha and beta method |
| Benchmark portfolio | The benchmark or strategic allocation in the governing documents, built mostly from indices; its return is policy beta | [Sources of return](02-sources-of-return.md#how-does-one-holding-split) | Alpha and beta method |
| Top-down portfolio | Investable ETFs, futures and cash carrying the real portfolio's exposure as held; its return less the benchmark portfolio's is active beta, which the record divides | [Sources of return](02-sources-of-return.md#how-does-one-holding-split) | Alpha and beta method, new portfolio review |
| Real portfolio | What the portfolio actually holds; its return less the top-down portfolio's is alpha | [Sources of return](02-sources-of-return.md#how-does-one-holding-split) | Alpha and beta method |
| Long-short book | The real portfolio's weights less the top-down portfolio's, which sum to zero within each sector | [Sources of return](02-sources-of-return.md#how-does-one-holding-split) | Alpha and beta method |

## Risk data

| Concept | What it is | Defined in | Used by |
|---|---|---|---|
| Golden source | The one system or provider whose record of a domain the firm treats as correct | [Risk data](03-risk-data.md#from-source-to-computed-figure) | That chapter only |
| Snapshot | The checked and enriched data a run computes from, and only from | [Risk data](03-risk-data.md#from-source-to-computed-figure) | That chapter only |
| Versioned as known | Each record keeps the date it describes and the date it became known, so past outputs can be reproduced | [Risk data](03-risk-data.md#versioned-as-known) | Controls |
| Data break | A failed quality check, recorded with the portfolios and measures it affects | [Risk data](03-risk-data.md#quality-before-computation) | Limits and escalation |
| Proxy policy | How gaps in data are filled: flagged, governed, measured and temporary | [Risk data](03-risk-data.md#proxies) | Market risk, all pillars |
| Fitness for use | The risk function's call on whether data is good enough to compute from; correction stays with the source's owner | [Risk data](03-risk-data.md#who-owns-what) | That chapter only |

## Limits and escalation

| Concept | What it is | Defined in | Used by |
|---|---|---|---|
| Hard limit | A mandate or regulatory limit; compliance owns its breach process, and the risk function watches it as a courtesy | [Limits and escalation](04-limits-and-escalation.md#where-limits-come-from) | Investment risk, market risk |
| Internal limit | A soft limit the risk function sets where the mandate is silent, to produce insight first and constrain when judged necessary | [Limits and escalation](04-limits-and-escalation.md#what-internal-limits-are-for) | Market risk, liquidity risk, controls |
| Early warning | A level ahead of a hard or internal limit, or on a measure with no limit; a reading beyond it is a watch item | [Limits and escalation](04-limits-and-escalation.md#where-limits-come-from) | All pillars |
| Breach lifecycle | Detect, verify, classify, notify, explain, decide, cure and close | [Limits and escalation](04-limits-and-escalation.md#the-breach-lifecycle) | Market risk |
| Active and passive breach | A breach caused by a trade or decision, or by markets, flows or corporate actions | [Limits and escalation](04-limits-and-escalation.md#the-breach-lifecycle) | Market risk |

## Redesigning the work

| Concept | What it is | Defined in | Used by |
|---|---|---|---|
| Core pattern | The risk engine computes, AI narrates, a human judges | [Principles](05-principles.md#2-the-risk-engine-computes-ai-narrates-a-human-judges) | Every chapter |
| Risk engine | The deterministic part of the system: the same data always gives the same figure | [Principles](05-principles.md#2-the-risk-engine-computes-ai-narrates-a-human-judges) | Every chapter |
| Six principles | What a redesign should follow | [Principles](05-principles.md#six-principles) | Redesign method, all pillars |
| Seven steps | How one workflow is redesigned, from outcome to measured result | [Redesign method](06-redesign-method.md#the-seven-steps) | All pillars |
| Step tags | Gather, Compute, Interpret, Judge, Communicate, Approve / Wait | [Redesign method](06-redesign-method.md#3-map-the-current-state) | All pillars |
| Risk manager's value | Judging what matters to the portfolio and its intended risk profile, bringing clarity to the risks being taken, challenge, deciding what the system flags and judgement where the data runs out; the sign-off is the accountability | [Principles](05-principles.md#what-the-risk-manager-adds) | README, measuring value, all pillars |
| Owners | Who or what does each step: the risk engine, the AI assistant, the risk manager or the head of risk | [Redesign method](06-redesign-method.md#4-assign-each-step-an-owner) | All pillars |
| Four dimensions of value | Capacity, speed, quality and influence | [Measuring value](08-measuring-value.md#four-dimensions) | All pillars |
| Baseline | A record of the current state, taken before anything changes | [Measuring value](08-measuring-value.md#baseline-first) | Redesign method |
| Reinvestment plan | What freed time will be spent on, decided in advance | [Measuring value](08-measuring-value.md#reinvestment-plan) | Principles, redesign method, market risk |

## Exceptions and ranking

| Concept | What it is | Defined in | Used by |
|---|---|---|---|
| Exception | A reading that has crossed a limit or another rule's threshold | [Each pillar's rules](../pillars/market-risk.md#materiality-and-exceptions) | Controls, integrated view |
| Watch item | A reading approaching a limit or threshold, picked up by an early warning or a persistence rule | [Each pillar's rules](../pillars/market-risk.md#materiality-and-exceptions) | Integrated view |
| Ranked queue | What the human reviews instead of everything | [Principles](05-principles.md#4-exceptions-over-everything) | Market risk, redesign method |
| Not assessed | How a portfolio with missing data is shown, never as clean | [Risk data](03-risk-data.md#quality-before-computation) | Market risk, integrated view |
| Watch list | The firm's single list of portfolios with unresolved issues, owned by the risk function | [Performance risk](../pillars/performance-risk.md#workflows-in-this-pillar) | Integrated view |
| Pattern | A named chain of signals across pillars | [Integrated view](../pillars/integrated-view.md#patterns) | Integrated view's rules |
| Lead time | How much earlier the view ranked a portfolio than the first escalation from any single pillar | [Integrated view](../pillars/integrated-view.md#measuring-value) | Integrated view |

## Controls

| Concept | What it is | Defined in | Used by |
|---|---|---|---|
| Grounding check | Every number in generated text is a computed fact, or a simple operation on computed facts that the check recomputes | [Controls](07-controls.md#the-grounding-check) | Principles, all pillars, alpha and beta |
| Sign-off point | Where a human must approve, and what they are approving | [Controls](07-controls.md#sign-off-points) | Every redesigned workflow |
| Audit trail | The record of facts, versions, generated text, edits and approval | [Controls](07-controls.md#the-audit-trail) | Every redesigned workflow |
| Governed parameter | A threshold or rule with an owner, a review cycle and a change record | [Controls](07-controls.md#materiality-thresholds-as-governed-parameters) | All pillars, alpha and beta |
| Parallel run | The new workflow runs beside the old one before the old one stops | [Controls](07-controls.md#parallel-runs) | Redesign method, measuring value |
| Fallback | What happens when a component fails, including a template in place of AI text | [Controls](07-controls.md#fallback) | Grounding check |

## Measures

| Concept | What it is | Defined in | Used by |
|---|---|---|---|
| Ex-ante tracking error | The forecast of how far a portfolio could drift from its benchmark | [Market risk](../pillars/market-risk.md#workflows-in-this-pillar) | Philosophy, performance risk, integrated view |
| Ex-post tracking error | How far a portfolio's realised return has drifted from its benchmark | [Performance risk](../pillars/performance-risk.md#workflows-in-this-pillar) | Market risk, integrated view |
| Exposure | What a holding is sensitive to, computed once in the daily run | [Market risk](../pillars/market-risk.md#workflows-in-this-pillar) | Performance risk, alpha and beta |
| Stress and reverse stress | Losses under scenarios, and the shocks that would break a mandate | [Market risk](../pillars/market-risk.md#stress-and-reverse-stress) | Philosophy, liquidity risk, alpha and beta |
| Redemption coverage | What a portfolio could raise, leaving out encumbered assets, against the calls on its cash under stress | [Liquidity risk](../pillars/liquidity-risk.md#materiality-and-exceptions) | Philosophy, investment risk, integrated view |
| Fairness and capacity | Selling a slice of every holding against selling the most liquid first; the gap is the cost shifted to the investors who stay | [Liquidity risk](../pillars/liquidity-risk.md#fairness-and-capacity) | Investment risk |
| Encumbrance | Collateral posted and assets lent out, left out of what a portfolio can raise | [Liquidity risk](../pillars/liquidity-risk.md#encumbrance-and-second-round-effects) | Investment risk, integrated view |
| Second-round effect | The extra cost when several of the firm's portfolios sell the same holdings, or when a market move also raises margin calls | [Liquidity risk](../pillars/liquidity-risk.md#encumbrance-and-second-round-effects) | That chapter only |
| Stale or unpriceable holding | A holding whose value is uncertain, flagged to the owner of pricing | [Liquidity risk](../pillars/liquidity-risk.md#workflows-in-this-pillar) | Market risk, integrated view, alpha and beta |
| Jump to default | The loss if an issuer defaulted, net of expected recovery, read as a concentration measure | [Market risk](../pillars/market-risk.md#credit-spreads-default-and-migration) | Investment risk |
| Gross and commitment leverage | Total notional, and exposure after netting and hedging, each with an internal limit | [Market risk](../pillars/market-risk.md#leverage-and-options) | Limits and escalation |
| Backtest against the design | VaR breaches judged against what the chosen design implies, stated in advance | [Market risk](../pillars/market-risk.md#backtesting) | Philosophy |
| Information ratio and t-statistic | Active return per unit of active risk, shown with how much of it could be noise | [Performance risk](../pillars/performance-risk.md#windows-and-significance) | Sources of return, philosophy |
| Windows | Every performance measure shown over 1, 3, 12 and 36 months, with 12 months the default for the relative return rule | [Performance risk](../pillars/performance-risk.md#windows-and-significance) | Integrated view |
| Benchmark tests | Specified in advance, investable, unambiguous, measurable, appropriate to the style and owned | [Performance risk](../pillars/performance-risk.md#benchmarks-and-peer-groups) | New portfolio review |
| Linking method | How single-period attribution is made to sum over longer periods, held as a governed parameter | [Performance risk](../pillars/performance-risk.md#linking-attribution-over-time) | Alpha and beta |
| Risk budget | Active risk allotted to bets, read against the return they earn | [Market risk](../pillars/market-risk.md#workflows-in-this-pillar) | Philosophy; performance risk's challenge pack; integrated view |
| Realised drawdown | The fall from a portfolio's peak value, absolute and relative to its benchmark | [Performance risk](../pillars/performance-risk.md#workflows-in-this-pillar) | Market risk, integrated view |
| Headroom | A stress loss set against what is left of the drawdown tolerance | [Market risk](../pillars/market-risk.md#materiality-and-exceptions) | Integrated view |

## Alpha and beta method

| Concept | What it is | Defined in | Used by |
|---|---|---|---|
| Beta | The return from market and factor exposure, however it arose | [Alpha and beta method](../pillars/alpha-and-beta-method.md#the-three-portfolios) | Sources of return, performance risk |
| Alpha | The add-on return from security selection: the real portfolio's return less the top-down portfolio's | [Alpha and beta method](../pillars/alpha-and-beta-method.md#the-three-portfolios) | Sources of return, performance risk |
| Gross return and the bridge | The split's basis, and the link from it to the net return | [Alpha and beta method](../pillars/alpha-and-beta-method.md#scope-and-basis) | Performance risk |
| Declared factor list | The factors alpha must stay neutral to, held as a governed parameter | [Alpha and beta method](../pillars/alpha-and-beta-method.md#booked-or-derived) | Market risk, performance risk |
| Factor return | The return of the ETF or future that carries a declared factor | [Alpha and beta method](../pillars/alpha-and-beta-method.md#building-the-top-down-portfolio) | Philosophy |
| Cost of holding beta | The top-down portfolio's instruments against the indices they track, on its own line beside the fee | [Alpha and beta method](../pillars/alpha-and-beta-method.md#the-four-beta-lines) | That page only |
| Booked and derived books | Two routes to the same split, with different evidence | [Alpha and beta method](../pillars/alpha-and-beta-method.md#booked-or-derived) | That page only |
