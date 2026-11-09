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
| Three decisions | Construct, Oversee and Assess: before, during and after an investment | [Philosophy](00-philosophy.md#purpose-transparency-for-three-decisions) | Market risk's what-ifs, alpha and beta |
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
| Beta portfolio | The portfolio's own weight in each asset class and sector, following the index inside each | [Sources of return](02-sources-of-return.md#how-does-one-holding-split) | Alpha and beta method |
| Long-short book | The alpha weights, which sum to zero within each sector | [Sources of return](02-sources-of-return.md#how-does-one-holding-split) | Alpha and beta method |

## Risk data

| Concept | What it is | Defined in | Used by |
|---|---|---|---|
| Golden source | The one system or provider whose record of a domain the firm treats as correct | [Risk data](03-risk-data.md#from-source-to-computed-figure) | Controls |
| Snapshot | The checked and enriched data a run computes from, and only from | [Risk data](03-risk-data.md#from-source-to-computed-figure) | Controls, all pillars |
| Versioned as known | Each record keeps the date it describes and the date it became known, so past outputs can be reproduced | [Risk data](03-risk-data.md#versioned-as-known) | Controls |
| Data break | A failed quality check, recorded with the portfolios and measures it affects | [Risk data](03-risk-data.md#quality-before-computation) | Controls, all pillars |
| Proxy policy | How gaps in data are filled: flagged, governed, measured and temporary | [Risk data](03-risk-data.md#proxies) | Market risk, all pillars |
| Fitness for use | The risk function's call on whether data is good enough to compute from; correction stays with the source's owner | [Risk data](03-risk-data.md#who-owns-what) | Controls |

## Redesigning the work

| Concept | What it is | Defined in | Used by |
|---|---|---|---|
| Core pattern | The risk engine computes, AI narrates, a human judges | [Principles](04-principles.md#2-the-risk-engine-computes-ai-narrates-a-human-judges) | Every chapter |
| Risk engine | The deterministic part of the system: the same data always gives the same figure | [Principles](04-principles.md#2-the-risk-engine-computes-ai-narrates-a-human-judges) | Every chapter |
| Six principles | What a redesign should follow | [Principles](04-principles.md#six-principles) | Redesign method, all pillars |
| Seven steps | How one workflow is redesigned, from outcome to measured result | [Redesign method](05-redesign-method.md#the-seven-steps) | All pillars |
| Step tags | Gather, Compute, Interpret, Judge, Communicate, Approve / Wait | [Redesign method](05-redesign-method.md#3-map-the-current-state) | All pillars |
| Risk manager's value | Judging what matters to the portfolio and its intended risk profile, bringing clarity to the risks being taken, challenge, deciding what the system flags and judgement where the data runs out; the sign-off is the accountability | [Principles](04-principles.md#what-the-risk-manager-adds) | README, measuring value, all pillars |
| Owners | Who or what does each step: the risk engine, the AI assistant, the risk manager or the head of risk | [Redesign method](05-redesign-method.md#4-assign-each-step-an-owner) | All pillars |
| Four dimensions of value | Capacity, speed, quality and influence | [Measuring value](07-measuring-value.md#four-dimensions) | All pillars |
| Baseline | A record of the current state, taken before anything changes | [Measuring value](07-measuring-value.md#baseline-first) | Redesign method |
| Reinvestment plan | What freed time will be spent on, decided in advance | [Measuring value](07-measuring-value.md#reinvestment-plan) | Principles, redesign method, market risk |

## Exceptions and ranking

| Concept | What it is | Defined in | Used by |
|---|---|---|---|
| Exception | A reading where a rule has fired | [Each pillar's rules](../pillars/market-risk.md#materiality-and-exceptions) | Controls, integrated view |
| Watch item | A reading moving towards a threshold | [Each pillar's rules](../pillars/market-risk.md#materiality-and-exceptions) | Integrated view |
| Ranked queue | What the human reviews instead of everything | [Principles](04-principles.md#4-exceptions-over-everything) | Market risk, redesign method |
| Not assessed | How a portfolio with missing data is shown, never as clean | [Market risk](../pillars/market-risk.md#controls-specific-to-this-pillar) | Risk data, integrated view |
| Watch list | The firm's single list of portfolios with unresolved issues, owned by the risk function | [Performance risk](../pillars/performance-risk.md#workflows-in-this-pillar) | Integrated view |
| Pattern | A named chain of signals across pillars | [Integrated view](../pillars/integrated-view.md#patterns) | Integrated view's rules |
| Lead time | How much earlier the view ranked a portfolio than the first escalation from any single pillar | [Integrated view](../pillars/integrated-view.md#measuring-value) | Integrated view |

## Controls

| Concept | What it is | Defined in | Used by |
|---|---|---|---|
| Grounding check | Every number in generated text is a computed fact, or a simple operation on computed facts that the check recomputes | [Controls](06-controls.md#the-grounding-check) | Principles, all pillars, alpha and beta |
| Sign-off point | Where a human must approve, and what they are approving | [Controls](06-controls.md#sign-off-points) | Every redesigned workflow |
| Audit trail | The record of facts, versions, generated text, edits and approval | [Controls](06-controls.md#the-audit-trail) | Every redesigned workflow |
| Governed parameter | A threshold or rule with an owner, a review cycle and a change record | [Controls](06-controls.md#materiality-thresholds-as-governed-parameters) | All pillars, alpha and beta |
| Parallel run | The new workflow runs beside the old one before the old one stops | [Controls](06-controls.md#parallel-runs) | Redesign method, measuring value |
| Fallback | What happens when a component fails, including a template in place of AI text | [Controls](06-controls.md#fallback) | Grounding check |

## Measures

| Concept | What it is | Defined in | Used by |
|---|---|---|---|
| Ex-ante tracking error | The forecast of how far a portfolio could drift from its benchmark | [Market risk](../pillars/market-risk.md#workflows-in-this-pillar) | Philosophy, performance risk, integrated view |
| Ex-post tracking error | How far a portfolio's realised return has drifted from its benchmark | [Performance risk](../pillars/performance-risk.md#workflows-in-this-pillar) | Market risk, integrated view |
| Exposure | What a holding is sensitive to, computed once in the daily run | [Market risk](../pillars/market-risk.md#workflows-in-this-pillar) | Performance risk, alpha and beta |
| Stress and reverse stress | Losses under scenarios, and the shocks that would break a mandate | [Market risk](../pillars/market-risk.md#workflows-in-this-pillar) | Philosophy, liquidity risk, alpha and beta |
| Redemption coverage | What a portfolio could raise, leaving out encumbered assets, against the calls on its cash under stress | [Liquidity risk](../pillars/liquidity-risk.md#materiality-and-exceptions) | Philosophy, investment risk, integrated view |
| Stale or unpriceable holding | A holding whose value is uncertain, flagged to the owner of pricing | [Liquidity risk](../pillars/liquidity-risk.md#workflows-in-this-pillar) | Market risk, integrated view, alpha and beta |
| Risk budget | Active risk allotted to bets, read against the return they earn | [Philosophy](00-philosophy.md#3-connection) | Market risk, which owns the review; performance risk's challenge pack; integrated view |
| Realised drawdown | The fall from a portfolio's peak value, absolute and relative to its benchmark | [Performance risk](../pillars/performance-risk.md#workflows-in-this-pillar) | Market risk, integrated view |
| Headroom | A stress loss set against what is left of the drawdown tolerance | [Market risk](../pillars/market-risk.md#materiality-and-exceptions) | Integrated view |

## Alpha and beta method

| Concept | What it is | Defined in | Used by |
|---|---|---|---|
| Beta | The return from market and factor exposure, however it arose | [Alpha and beta method](../pillars/alpha-and-beta-method.md) | Sources of return, performance risk |
| Alpha | The add-on return from security selection, neutral to all beta at every moment | [Alpha and beta method](../pillars/alpha-and-beta-method.md) | Sources of return, performance risk |
| Gross return and the bridge | The split's basis, and the link from it to the net return | [Alpha and beta method](../pillars/alpha-and-beta-method.md#scope-and-basis) | Performance risk |
| Declared factor list | The factors alpha must stay neutral to, held as a governed parameter | [Alpha and beta method](../pillars/alpha-and-beta-method.md) | Performance risk |
| Factor return | The return of the investable index or basket for a declared factor | [Alpha and beta method](../pillars/alpha-and-beta-method.md#neutral-to-all-of-beta) | Philosophy |
| Booked and derived books | Two routes to the same split, with different evidence | [Alpha and beta method](../pillars/alpha-and-beta-method.md#booked-or-derived) | That page only |
