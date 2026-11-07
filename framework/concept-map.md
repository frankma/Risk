# Concept map

This page lists the framework's main concepts: what each one is, where it is defined and which chapters use it. It
defines nothing new. The chapter named under "Defined in" is the single source for each concept, and a reader who wants
the reasoning goes there.

## Purpose and beliefs

| Concept | What it is | Defined in | Used by |
|---|---|---|---|
| Investment risk | The chance that a portfolio's outcome departs from what its mandate intends | [Investment risk](02-investment-risk.md#definition) | Every chapter |
| Sight | The few numbers worth questioning and acting on, out of millions | [Philosophy](00-philosophy.md) | The three decisions |
| Beliefs | Eight positions that decide what the rules do not | [Philosophy](00-philosophy.md#beliefs) | Market risk; any model a risk function uses |
| Three decisions | Construct, Oversee and Assess: before, during and after an investment | [Philosophy](00-philosophy.md#purpose-transparency-for-three-decisions) | Market risk's what-ifs, alpha and beta |
| Three dimensions | Condensation, drill-in and connection: what every piece of risk work provides | [Philosophy](00-philosophy.md#practice-transparency-in-three-dimensions) | All pillars |
| Decision-maker | Whoever a piece of a decomposition belongs to | [Philosophy](00-philosophy.md#2-drill-in) | Alpha and beta |
| Mandate terms | A fund's objective, style and limits in a form code can test, confirmed by the risk manager | [Performance risk](../pillars/performance-risk.md#flagship-redesign-the-periodic-portfolio-manager-review) | Performance risk's rules and split |

## Scope

| Concept | What it is | Defined in | Used by |
|---|---|---|---|
| Three pillars | Market, liquidity and performance risk: a lens on the recurring work | [Investment risk](02-investment-risk.md#the-three-pillars) | Every chapter |
| Measuring and approving | Investment risk measures and monitors; approval, pricing and validation sit elsewhere | [Investment risk](02-investment-risk.md#scope-and-boundaries) | Market risk, liquidity risk, controls |
| Integrated view | One view that ranks funds where signals across pillars combine | [Integrated view](../pillars/integrated-view.md) | Principles, investment risk, all pillars |
| Firm's footprint | Holdings aggregated across funds, which do not net | [Philosophy](00-philosophy.md#the-firm-view) | Market risk, liquidity risk, integrated view, alpha and beta |

## Redesigning the work

| Concept | What it is | Defined in | Used by |
|---|---|---|---|
| Core pattern | Code computes, AI narrates, a human judges | [Principles](01-principles.md#2-code-computes-ai-narrates-a-human-judges) | Every chapter |
| Six principles | What a redesign should follow | [Principles](01-principles.md#six-principles) | Redesign method, all pillars |
| Seven steps | How one workflow is redesigned, from outcome to measured result | [Redesign method](03-redesign-method.md#the-seven-steps) | All pillars |
| Step tags | Gather, Compute, Interpret, Judge, Communicate, Approve / Wait | [Redesign method](03-redesign-method.md#3-map-the-current-state) | All pillars |
| Owners | Who or what does each step: code, AI, the risk manager or the head of risk | [Redesign method](03-redesign-method.md#4-assign-each-step-an-owner) | All pillars |
| Four dimensions of value | Capacity, speed, quality and influence | [Measuring value](05-measuring-value.md#four-dimensions) | All pillars |
| Baseline | A record of the current state, taken before anything changes | [Measuring value](05-measuring-value.md#baseline-first) | Redesign method |
| Reinvestment plan | What freed time will be spent on, decided in advance | [Measuring value](05-measuring-value.md#reinvestment-plan) | Principles, redesign method, market risk |

## Exceptions and ranking

| Concept | What it is | Defined in | Used by |
|---|---|---|---|
| Exception | A reading where a rule has fired | [Each pillar's rules](../pillars/market-risk.md#materiality-and-exceptions) | Controls, integrated view |
| Watch item | A reading moving towards a threshold | [Each pillar's rules](../pillars/market-risk.md#materiality-and-exceptions) | Integrated view |
| Ranked queue | What the human reviews instead of everything | [Principles](01-principles.md#4-exceptions-over-everything) | Market risk, redesign method |
| Not assessed | How a fund with missing data is shown, never as clean | [Market risk](../pillars/market-risk.md#controls-specific-to-this-pillar) | Integrated view |
| Fund watch list | The firm's single list of funds with unresolved issues, owned by the head of risk | [Performance risk](../pillars/performance-risk.md#workflows-in-this-pillar) | Integrated view |
| Pattern | A named chain of signals across pillars | [Integrated view](../pillars/integrated-view.md#patterns) | Integrated view's rules |
| Lead time | How much earlier the view ranked a fund than the first escalation from any single pillar | [Integrated view](../pillars/integrated-view.md#measuring-value) | Integrated view |

## Controls

| Concept | What it is | Defined in | Used by |
|---|---|---|---|
| Grounding check | Every number in generated text is matched against computed facts | [Controls](04-controls.md#the-grounding-check) | Principles, all pillars, alpha and beta |
| Sign-off point | Where a human must approve, and what they are approving | [Controls](04-controls.md#sign-off-points) | Every redesigned workflow |
| Audit trail | The record of facts, versions, generated text, edits and approval | [Controls](04-controls.md#the-audit-trail) | Every redesigned workflow |
| Governed parameter | A threshold or rule with an owner, a review cycle and a change record | [Controls](04-controls.md#materiality-thresholds-as-governed-parameters) | All pillars, alpha and beta |
| Parallel run | The new workflow runs beside the old one before the old one stops | [Controls](04-controls.md#parallel-runs) | Redesign method, measuring value |
| Fallback | What happens when a component fails, including a template in place of AI text | [Controls](04-controls.md#fallback) | Grounding check |

## Measures

| Concept | What it is | Defined in | Used by |
|---|---|---|---|
| Tracking error | How far a portfolio can drift from its benchmark | [Philosophy](00-philosophy.md#1-condensation) | Computed in market risk, owned by performance risk |
| Exposure | What a holding is sensitive to, computed once in the daily run | [Market risk](../pillars/market-risk.md#workflows-in-this-pillar) | Performance risk, alpha and beta |
| Stress and reverse stress | Losses under scenarios, and the shocks that would break a mandate | [Market risk](../pillars/market-risk.md#workflows-in-this-pillar) | Philosophy, liquidity risk, alpha and beta |
| Redemption coverage | What a fund could raise against what investors could redeem under stress | [Liquidity risk](../pillars/liquidity-risk.md#materiality-and-exceptions) | Philosophy, investment risk, integrated view |
| Stale or unpriceable holding | A holding whose value is uncertain, flagged to the owner of pricing | [Liquidity risk](../pillars/liquidity-risk.md#workflows-in-this-pillar) | Market risk, integrated view, alpha and beta |
| Risk budget | Active risk allotted to bets, read against the return they earn | [Philosophy](00-philosophy.md#3-connection) | Market risk, performance risk, integrated view |

## Alpha and beta

| Concept | What it is | Defined in | Used by |
|---|---|---|---|
| Beta | The return from market and factor exposure, however it arose | [Alpha and beta](06-alpha-and-beta.md#definitions) | Performance risk |
| Alpha | The add-on return from security selection, neutral to all beta at every moment | [Alpha and beta](06-alpha-and-beta.md#definitions) | Performance risk |
| Gross return and the bridge | The split's basis, and the link from it to the net return | [Alpha and beta](06-alpha-and-beta.md#scope-and-basis) | Performance risk |
| Beta portfolio | The fund's own weight in each asset class and sector, following the index inside each | [Alpha and beta](06-alpha-and-beta.md#splitting-a-holding) | That chapter only |
| Long-short book | The alpha weights, which sum to zero within each sector | [Alpha and beta](06-alpha-and-beta.md#splitting-a-holding) | Performance risk |
| Declared factor list | The factors alpha must stay neutral to, held as a governed parameter | [Alpha and beta](06-alpha-and-beta.md#neutral-to-all-of-beta) | Performance risk |
| Factor return | The return of the investable index or basket for a declared factor | [Alpha and beta](06-alpha-and-beta.md#neutral-to-all-of-beta) | Philosophy |
| Booked and derived books | Two routes to the same split, with different evidence | [Alpha and beta](06-alpha-and-beta.md#booked-or-derived) | Performance risk |
| Policy beta | The return of the strategic allocation or benchmark | [Alpha and beta](06-alpha-and-beta.md#fine-tuning-beta) | That chapter only |
| Tilts | The manager's standing positions against that allocation, recorded when taken | [Alpha and beta](06-alpha-and-beta.md#fine-tuning-beta) | Performance risk |
| Timing | The return from recorded changes in exposure over time | [Alpha and beta](06-alpha-and-beta.md#fine-tuning-beta) | Performance risk |
| Carried beta | Any exposure without a record that anyone chose it | [Alpha and beta](06-alpha-and-beta.md#fine-tuning-beta) | Performance risk's source-of-return rule |
