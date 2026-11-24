# Limits and escalation

## The essentials
**Limits and escalation** asks which limits apply to a portfolio, who owns each, and what happens when one is breached.

**A band, not a line:** a mandate intends a range of risk, and leeway within it is expected. Limits and early warnings
put numbers on the edges of that range, so that the portfolio manager, the risk manager and investment oversight stay on
top of where each portfolio stands. Hard limits, from the mandate or regulation, must be rectified, and compliance owns
their legal reading. Internal limits are soft: the risk function sets them where the mandate is silent, to produce
insight first. Early warnings sit ahead of both.

**How the work is done:** the analytics engine detects a breach in the daily run, checks it against data breaks and
classifies it as active or passive. The AI explains what the checks found, drafts the notice and tests the portfolio
manager's explanation against the data. The portfolio manager and the risk manager agree how a breach of an internal
limit is handled: rectify it, or accept it for a set period with the head of risk's approval.

**Escalation has an end:** where the two disagree, the risk committee decides and its decision binds. What it cannot
resolve goes to the executive committee, and the board is the last resort.

The rest of this chapter is the detail behind these points.

## Where limits come from
Limits come in three layers, and the first has two kinds.

| Layer | What it is | Who owns it |
|---|---|---|
| Mandate and regulatory limits: position and eligibility rules | Limits written in the portfolio's governing documents or in regulation on what may be held and how much of it, such as a maximum weight in one issuer | Compliance |
| Mandate and regulatory limits: risk-measured limits | Limits written in the governing documents or in regulation on a measure that only the analytics engine computes: leverage, exposure measured by value at risk, counterparty exposure and liquidity | The risk function monitors them; compliance owns the legal reading and the breach report |
| Internal limits | Limits the risk function sets where the mandate is silent, such as an absolute risk limit for a benchmarked portfolio | The risk function |
| Early warnings | Levels set ahead of a limit of either kind, so that a reading is seen before it breaches, or on a measure that has no limit | The risk function |

**Hard limits must be rectified.** Compliance's coded rule is the master reading of every hard limit. Where the risk
function's [mandate terms](../pillars/performance-risk.md#mandate-terms) hold the same limit, they are reconciled to
compliance's rule, and a difference is routed to compliance.

**Position and eligibility rules:** the risk function shows each one beside its own readings, sets its own early
warnings ahead of them, and routes any breach it sees to compliance.

**Risk-measured limits** are the risk function's own duty, because only the analytics engine can compute them. It
detects and verifies a breach, tells compliance and the portfolio manager on the same day, and tracks the rectification.

**Internal limits are soft limits.** They are [governed
parameters](08-controls.md#materiality-thresholds-as-governed-parameters), owned by the risk function, and they cover
what the mandate leaves unsaid. A mandate that sets a benchmark and a tracking error budget rarely says how much the
portfolio may lose in total; an internal limit on value at risk says it for the risk function. Each internal limit is
set for its portfolio, from what the mandate intends, not copied from a firm-wide number. For a new portfolio, internal
limits are first set in the [new portfolio review](../pillars/new-portfolio-review.md), with the head of risk's
approval.

**Early warnings sit ahead of every limit,** hard or soft, on the side a reading approaches from: below a ceiling and
above a floor. A measure with no limit can carry an early warning of its own. A reading beyond an early warning is a
watch item, not a breach.

## What internal limits are for
Internal limits exist first to produce insight: they keep the portfolio manager, the risk manager and investment
oversight on top of an issue, start the conversation and record its outcome. They are designed so that they can
constrain when needed, but whether to use them that way is a judgement, not an automatic ruling. Automatic constraint is
what hard limits are for.

By default, a risk function sets internal limits on:

| Measure | What the limit covers | Pillar |
|---|---|---|
| Value at risk or expected shortfall | Absolute forward-looking risk | [Market risk](../pillars/market-risk.md) |
| Ex-ante tracking error | A range, so that active risk is neither too high nor too low for the mandate | [Market risk](../pillars/market-risk.md) |
| Leverage, as gross and net exposure | The scale of positions, and the exposure left after netting and hedging | [Market risk](../pillars/market-risk.md) |
| Counterparty exposure | Exposure to each firm the portfolio trades with, lends securities to or holds assets through | [Market risk](../pillars/market-risk.md) |
| Redemption coverage | Unencumbered liquid assets against the stressed calls on cash, at the horizon the dealing terms set | [Liquidity risk](../pillars/liquidity-risk.md) |

Where the governing documents or regulation already set a limit on one of these measures, that limit is a risk-measured
hard limit, and the internal limit sits inside it.

Other readings, such as stress losses against the drawdown tolerance, concentration below a mandate limit, flows and
relative return, are watched through early warnings and the pillars' rules rather than limits.

## How internal limits are calibrated
A risk function chooses how to calibrate each internal limit, and records the choice. The approaches differ in what they
anchor to.

| Approach | What it anchors to | Strength | Weakness |
|---|---|---|---|
| From the mandate | The tracking error budget, the risk of the benchmark, the loss the mandate can bear | Follows what the client intended (belief 1) | Many mandates say little about absolute risk, so the anchor is partly judgement |
| From the portfolio's history | The risk the portfolio has run over a long window, plus a buffer | Simple and specific to the portfolio | Builds in whatever risk the portfolio already ran, intended or not |
| From comparable portfolios | The risk run by portfolios with the same strategy | Shows when a portfolio is out of line with its peers | Peers can share the same unintended risk |
| From stress | The loss under stress that would break the mandate, worked back to a limit | Ties the limit to the tail and the path (belief 4) | Rests on the scenarios being plausible |

Whatever the approach, a limit is tested by how it behaves. A limit that is never approached says nothing, and one that
is breached all the time is ignored; both are reviewed on the cycle set out in
[controls](08-controls.md#materiality-thresholds-as-governed-parameters).

## The breach lifecycle
The lifecycle below applies to internal limits. A breach of a risk-measured hard limit follows the same stages, except
that the decision is always to rectify and compliance writes the breach report. A breach of a position or eligibility
rule follows compliance's process.

| # | Stage | What happens |
|---|---|---|
| 1 | Detect | The analytics engine finds the breach in the daily run |
| 2 | Verify | The analytics engine checks the breach against recorded [data breaks](03-risk-data.md#quality-before-computation): is the reading real? A breach it matches to a break is closed by the AI with the record, and the risk manager reviews the close the same day; the risk manager confirms every other breach |
| 3 | Classify | Active, caused by a trade or decision, or passive, caused by market moves, flows or corporate actions; the analytics engine classifies from the trade records and the risk manager confirms |
| 4 | Notify | The portfolio manager, investment oversight and the head of risk are told, with the facts; where the engine finds a governed rule covers the notice, the AI sends it, and the risk manager reviews it the same day |
| 5 | Explain | The portfolio manager explains the position, and the explanation is recorded; the AI tests it against the data and reports what supports it and what contradicts it |
| 6 | Decide | The portfolio manager and the risk manager agree: rectify it, or accept it for a set period with the head of risk's approval; a disagreement goes to the risk committee |
| 7 | Rectify | Where the decision is to rectify, the reading returns within the limit by a deadline |
| 8 | Close | The outcome is recorded, with the reason, the breach is closed and the head of risk is told |

Who does each step:

| # | Step | Owner |
|---|---|---|
| 1 | Detect the breach; check it against recorded data breaks; classify it as active or passive; decide whether a governed rule covers its notice | Analytics engine |
| 2 | Explain what the checks found; close a breach the engine matched to a data break; draft the notice to the portfolio manager, investment oversight and the head of risk, and send it, once the grounding check in step 3 passes, where the engine found the rule covers it | AI |
| 3 | Grounding check on the notice | Analytics engine |
| 4 | Confirm the breach and its classification; send a notice the rule does not cover; review the same day what the AI sent or closed | Risk manager |
| 5 | Record the portfolio manager's explanation | Analytics engine |
| 6 | Test the portfolio manager's explanation against the data; draft the decision note with what supports and what contradicts it, citing how similar breaches were decided | AI |
| 7 | Agree the decision: rectify, or accept for a set period; take a disagreement to the risk committee | Portfolio manager and risk manager |
| 8 | Approve an acceptance for a set period | Head of risk |
| 9 | Track the rectification to its deadline; escalate a missed deadline | Analytics engine |
| 10 | Confirm the close and report it to the head of risk; the record goes to the risk committee | Risk manager |

**Investment oversight**, told at the Notify stage, is the head of investments, or the committee that supervises the
portfolio managers on the firm's behalf.

**Active and passive breaches differ.** An active breach comes from a choice, so the question is why it was made and
whether it should stand. A passive breach comes from markets or flows, so the question is whether the position still
fits the mandate now that conditions have changed. Deadlines differ accordingly, and are set in advance: for example, an
active breach is decided within a day and a passive breach within a set number of business days. (The examples are
illustrative.)

**Accepting a breach is a decision, not a lapse.** A breach accepted for a set period is recorded with its reason and an
expiry date, and returns to the queue when it expires. Repeated acceptance is a sign that the limit needs recalibrating,
not that it should be ignored.

## Escalation
Escalation follows a stated path. **The deadlines are illustrative.**

| Trigger | From | To | Deadline | What the body can decide |
|---|---|---|---|---|
| A rectification passes its deadline | Analytics engine | Head of risk | The same day | Require the rectification, or extend the deadline once, with a reason |
| A decision on a breach passes its deadline | Analytics engine | The risk committee's chair | The same day | Decide, or call the committee |
| The portfolio manager and the risk manager disagree on a breach of an internal limit | Risk manager, presented by the head of risk | Risk committee | Its next meeting, or one called within 5 business days | Require rectification by a date, accept the breach for a set period, or change the limit |
| The risk committee cannot resolve a breach, or its decision is not followed | The risk committee's chair | The executive committee, the risk committee's parent body | Its next meeting, or one called sooner | Direct the outcome |
| The executive committee cannot resolve a breach | The executive committee's chair | The board | Its next meeting, or one called sooner | Direct the outcome; the board is the last resort |
| A member of the risk committee dissents from its decision | The member | The board | The board's next report | Ask the committee to review its decision; the decision stands until then |
| A breach of a hard limit | Risk function | Compliance | The same day | Under compliance's process |
| Product governance proceeds against the risk function's opinion on a new portfolio | Head of risk | Risk committee | Its next meeting | Require conditions, or record the dissent for the board |
| A watch list portfolio that investment oversight escalates | Investment oversight | Risk committee | Its next meeting | Require an action by a date, or keep the portfolio under watch |

**The risk committee decides an unrectified breach of a soft limit and an escalated watch list portfolio,** and its
decision binds the portfolio manager. It is a committee of the executive committee, with authority delegated over risk
decisions; it is chaired by someone independent of the investment teams, and includes the head of risk and the head of
investments. At the executive committee, the chief executive and the investment and business heads settle a breach
together.

**The board sees the outcomes.** On its reporting cycle, the board receives the breaches of hard limits, the breaches
accepted and their expiry dates, the committee's binding decisions and any dissent. What the client of a segregated
mandate is told follows the mandate's reporting terms and compliance's process.

## Who approves what
| Decision | Who approves | Record |
|---|---|---|
| Acknowledging a reading beyond an early warning | Risk manager | The reading, the reason it stands and when it will be looked at again |
| How a breach of an internal limit is handled: rectify or accept | Portfolio manager and risk manager, together | The decision note, with the reason |
| Accepting a breach of an internal limit for a set period | Head of risk | The breach, the reason, the expiry date and any conditions |
| Setting a new portfolio's first internal limits | Head of risk, on the risk manager's proposal | The limits, how each was calibrated and the reason |
| Allowing an action to run under a governed rule without sign-off beforehand | Head of risk | The rule, the evidence that it passed the four tests and the date it takes effect |
| Changing an internal limit or how it is calibrated | Risk committee | The old and new values, the reason and the date it takes effect |
| The legal reading of a hard limit, its breach report and any extension | Compliance, under its own process | Routed or reported by the risk function, with the evidence |

## What the AI drafts
Every number in the draft appears in the facts beside it, so the [grounding check](08-controls.md#the-grounding-check)
would pass. **The fund and figures are illustrative.**

| Fact | Value |
|---|---|
| Fund | Fund P |
| Measure | 1-day 99% VaR, under an internal limit |
| Today / previous day | 2.62% / 2.41% |
| Limit | 2.50% |
| Trades on the previous day | None |
| Classification | Passive |
| Change by source (decomposition) | Market volatility +0.21 points; position changes none |
| Deadline for a decision on a passive breach | 5 business days |

> Fund P's 1-day 99% VaR is 2.62%, above its internal limit of 2.50%, up from 2.41% the previous day. The breach is
> passive: no trades were made, and the rise came from higher market volatility. A decision to rectify or accept is due
> within 5 business days.

## Controls and measures specific to limits
The general [controls](08-controls.md) apply in full. Limits add six.

- **Every breach is recorded.** Detection, verification, classification, notice, explanation, decision and close are
  kept in the audit trail.
- **What the AI sends or closes is reviewed.** The risk manager reviews every notice the AI sent and every breach it
  closed the same day, and a review that disagrees follows the path in [automated
  actions](08-controls.md#automated-actions).
- **Approvals expire.** An accepted breach returns to the queue on its expiry date.
- **Hard limits are never accepted.** A breach of one is always rectified; who routes, reports and tracks it is set out
  under [where limits come from](04-limits-and-escalation.md#where-limits-come-from).
- **Escalation has an end.** Every path in the escalation table finishes with a decision that binds; a dissent does not
  suspend it.
- **Limits are reviewed by their behaviour.** A limit that is never approached, or is breached repeatedly, is reviewed.

Of the [four dimensions](07-redesign-method.md#four-dimensions) a redesigned workflow is measured on, speed and
influence matter most here: how soon a breach is known and decided, and whether the decisions are made and kept.

| Dimension | Measure for limits |
|---|---|
| Speed | Time from detection to notice; time from notice to decision |
| Capacity | Breaches handled with a full record |
| Quality | Breaches first noticed outside the risk function; decisions made after their deadline |
| Influence | Breaches rectified or accepted by a recorded decision; limits recalibrated from the record |
| Limits specific | Share of internal limits that were never approached, or were breached repeatedly, in a year |

## Sources
- Financial Stability Board (2013). *Principles for an Effective Risk Appetite Framework.* Risk appetite expressed as
  limits, with roles, escalation and the link between appetite and the limits that apply it.
- International Organization of Securities Commissions (2019). *Recommendations for a Framework Assessing Leverage in
  Investment Funds.* Gross and net exposure as measures of leverage, with derivatives converted to the underlying.
- Committee of Sponsoring Organizations of the Treadway Commission (2017). *Enterprise Risk Management: Integrating with
  Strategy and Performance.* Appetite, tolerance and the review of limits as part of governing risk.
