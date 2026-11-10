# Limits and escalation

Limits turn a mandate's intent into readings a risk function can watch every day. This chapter sets out where limits
come from and who owns each kind, what internal limits are for, how they are calibrated, how a breach of an internal
limit is handled from detection to closure, and who approves what. It closes with breach handling redesigned from email
chains into tracked stages. The [philosophy](00-philosophy.md#beliefs) holds that appetite belongs to the client and is
judged against each mandate, not against a firm-wide number; limits are how that belief is applied.

## Where limits come from
Limits come in three layers.

| Layer | What it is | Who owns it |
|---|---|---|
| Mandate and regulatory limits | Limits written in the portfolio's governing documents or in regulation, such as a maximum weight in one issuer | Compliance |
| Internal limits | Limits the risk function sets where the mandate is silent, such as an absolute risk limit for a benchmarked portfolio | The risk function |
| Early warnings | Levels set below a limit of either kind, so that a reading is seen before it breaches | The risk function |

**Mandate and regulatory limits are hard limits.** A breach must be cured, and compliance owns their legal reading, the
breach process, cures and any extension, as set out in [investment risk](01-investment-risk.md#scope-and-boundaries).
The risk function watches them as a courtesy: it shows each one beside its own readings, sets its own early warnings
below them, and routes any breach it sees to compliance rather than handling it.

**Internal limits are soft limits.** They are [governed
parameters](07-controls.md#materiality-thresholds-as-governed-parameters), owned by the risk function, and they cover
what the mandate leaves unsaid. A mandate that sets a benchmark and a tracking error budget rarely says how much the
portfolio may lose in total; an internal limit on value at risk says it for the risk function. Each internal limit is
set for its portfolio, from what the mandate intends, not copied from a firm-wide number. For a new portfolio, internal
limits are first set in the [new portfolio review](../pillars/new-portfolio-review.md).

**Early warnings sit below every limit,** hard or soft. A reading above an early warning is a watch item, not a breach.

## What internal limits are for
Internal limits exist first to produce insight: they keep the portfolio manager, the risk manager and oversight on top
of an issue, start the conversation and record its outcome. They are designed so that they can constrain when needed,
but whether to use them that way is a judgement, not an automatic ruling. Automatic constraint is what the mandate and
regulatory limits, owned by compliance, are for.

By default, a risk function sets internal limits on:

| Measure | What the limit covers | Pillar |
|---|---|---|
| Value at risk or expected shortfall | Absolute forward-looking risk | [Market risk](../pillars/market-risk.md) |
| Ex-ante tracking error | A range, so that active risk is neither too high nor too low for the mandate | [Market risk](../pillars/market-risk.md) |
| Leverage, gross and commitment | The scale of positions and the risk they take after netting and hedging | [Market risk](../pillars/market-risk.md) |
| Counterparty exposure | Exposure to each firm the portfolio trades with or holds assets through | [Market risk](../pillars/market-risk.md) |
| Redemption coverage | Unencumbered liquid assets against the stressed calls on cash | [Liquidity risk](../pillars/liquidity-risk.md) |

Other readings, such as stress losses against the drawdown tolerance, concentration below a mandate limit, flows and
relative return, are watched through early warnings and the pillars' rules rather than limits.

## How internal limits are calibrated
A risk function chooses how to calibrate each internal limit, and records the choice. The approaches differ in what
they anchor to.

| Approach | What it anchors to | Strength | Weakness |
|---|---|---|---|
| From the mandate | The tracking error budget, the risk of the benchmark, the loss the mandate can bear | Follows what the client intended (belief 1) | Many mandates say little about absolute risk, so the anchor is partly judgement |
| From the portfolio's history | The risk the portfolio has run over a long window, plus a buffer | Simple and specific to the portfolio | Builds in whatever risk the portfolio already ran, intended or not |
| From comparable portfolios | The risk run by portfolios with the same strategy | Shows when a portfolio is out of line with its peers | Peers can share the same unintended risk |
| From stress | The loss under stress that would break the mandate, worked back to a limit | Ties the limit to the tail and the path (belief 4) | Rests on the scenarios being plausible |

Whatever the approach, a limit is tested by how it behaves. A limit that is never approached says nothing, and one that
is breached all the time is ignored; both are reviewed on the cycle set out in
[controls](07-controls.md#materiality-thresholds-as-governed-parameters).

## The breach lifecycle
The lifecycle below applies to internal limits. A breach of a mandate or regulatory limit follows compliance's process.

| # | Stage | What happens |
|---|---|---|
| 1 | Detect | The risk engine finds the breach in the daily run |
| 2 | Verify | The breach is checked against [data breaks](03-risk-data.md#quality-before-computation): is the reading real? |
| 3 | Classify | Active, caused by a trade or decision, or passive, caused by market moves, flows or corporate actions |
| 4 | Notify | The portfolio manager and oversight are told, with the facts |
| 5 | Explain | The portfolio manager explains the position, and the explanation is recorded |
| 6 | Decide | Cure it, accept it for a set period, or escalate it |
| 7 | Cure | Where the decision is to cure, the reading returns within the limit by a deadline |
| 8 | Close | The outcome is recorded, with the reason, and the breach is closed |

**Active and passive breaches differ.** An active breach comes from a choice, so the question is why it was made and
whether it should stand. A passive breach comes from markets or flows, so the question is whether the position still
fits the mandate now that conditions have changed. Deadlines differ accordingly, and are set in advance: for example,
an active breach is decided within a day and a passive breach within a set number of business days. (The examples are
illustrative.)

**Accepting a breach is a decision, not a lapse.** A breach accepted for a set period is recorded with its reason and an
expiry date, and returns to the queue when it expires. Repeated acceptance is a sign that the limit needs
recalibrating, not that it should be ignored.

## Who approves what
Each approval is recorded, and each one expires.

| Decision | Who approves | Record |
|---|---|---|
| Acknowledging a reading above an early warning | Risk manager | The reading, the reason it stands and when it will be looked at again |
| Accepting a breach of an internal limit for a set period | Head of risk | The breach, the reason, the expiry date and any conditions |
| Changing an internal limit or how it is calibrated | Risk committee | The old and new values, the reason and the date it takes effect |
| Anything about a mandate or regulatory limit | Compliance, under its own process | Routed by the risk function, with the evidence |

## Flagship redesign: handling a breach
The example below follows the handling of one breach of an internal limit. **The steps, hours and elapsed times are
illustrative.**

**Current state.** A breach is noticed in the morning check and handled by email.

| # | Step | Tag | Hours | Elapsed |
|---|---|---|---|---|
| 1 | Notice the breach while checking the day's readings | Compute | 0.25 | Half a day |
| 2 | Check that the data behind the reading is right | Gather | 0.5 | 1 day |
| 3 | Email the portfolio manager for an explanation | Communicate | 0.25 | 2 days |
| 4 | Chase the reply | Communicate | 0.5 | 2 days |
| 5 | Write it up for the head of risk | Communicate | 1 | 1 day |
| 6 | Head of risk decides | Approve / Wait | 0.25 | 2 days |
| 7 | Track the cure in a spreadsheet and chase it | Communicate | 1 | Ongoing |
| 8 | Write the outcome up for the risk committee | Communicate | 0.5 | At month end |

Each breach takes about 4.25 hours, and around 8.5 working days pass before a decision. Whether a breach was active or
passive is often not recorded, accepted breaches have no expiry, and nothing shows when the same limit is breached again
and again.

**Owner assignment.**

- Steps 1 and 2 move to the risk engine, which detects the breach in the daily run and checks it against the day's data
  breaks.
- Classification is added as a step for the risk engine, which compares the reading with the previous day's trades and
  market moves; the risk manager confirms it.
- Steps 3 to 5 become an AI draft of the notice from the facts, and a draft of the decision note once the portfolio
  manager has replied, both edited by the risk manager.
- Step 6 stays with the head of risk.
- Steps 7 and 8 move to the risk engine, which tracks each breach to its deadline, escalates one that is missed and
  assembles the record for the committee.

**Redesigned flow.**

| # | Step | Owner | Hours | Elapsed |
|---|---|---|---|---|
| 1 | Detect the breach; check it against data breaks; classify it as active or passive | Risk engine | 0 | Overnight |
| 2 | Draft the notice to the portfolio manager and oversight | AI assistant | 0 | Overnight |
| 3 | Grounding check on the notice | Risk engine | 0 | Overnight |
| 4 | Confirm the breach and its classification; send the notice | Risk manager | 0.25 | Same morning |
| 5 | Record the explanation; draft the decision note | AI assistant | 0 | On reply |
| 6 | Decide: cure, accept for a set period, or escalate | Head of risk | 0.25 | 1 day |
| 7 | Track the cure to its deadline; escalate a missed deadline | Risk engine | 0 | Ongoing |
| 8 | Confirm the close; the record goes to the risk committee | Risk manager | 0.25 | Same day |

Each breach takes about 0.75 hours, and a decision follows in about a day. Every breach carries its classification,
its explanation, its decision and, where accepted, its expiry.

**The shift.** Breaches move from threads of email to a tracked record. Nothing is lost between stages, and the record
shows which limits are breached repeatedly, which is the evidence for recalibrating them.

## What the AI drafts
The AI drafts from the facts the risk engine recorded and from nothing else. Every number in each draft appears in the
facts beside it, so the [grounding check](07-controls.md#the-grounding-check) would pass. The AI does not decide
whether a breach is real, how it is classified or what is done about it. **The funds and figures are illustrative.**

**A passive breach of an internal limit.**

| Fact | Value |
|---|---|
| Fund | Fund P |
| Measure | 1-day 99% VaR, under an internal limit |
| Today / previous day | 2.62% / 2.41% |
| Limit | 2.50% |
| Trades on the previous day | None |
| Classification | Passive: market volatility rose |
| Deadline for a decision on a passive breach | 5 business days |

> Fund P's 1-day 99% VaR is 2.62%, above its internal limit of 2.50%, up from 2.41% the previous day. The breach is
> passive: no trades were made, and the rise came from higher market volatility. A decision to cure, accept or escalate
> is due within 5 business days.

**A breach of a mandate limit, routed to compliance.**

| Fact | Value |
|---|---|
| Fund | Fund Q |
| Measure | Largest single-issuer weight |
| Today | 10.4% |
| Mandate limit, owned by compliance | 10.0% |
| Risk function's early warning | 9.0% |

> Fund Q's largest single-issuer weight is 10.4%, above the mandate limit of 10.0%. This limit is owned by compliance,
> and the breach has been routed to compliance with the supporting data. The risk function's early warning at 9.0%
> remains in its own queue.

## Controls specific to limits
The general controls in [controls](07-controls.md) apply in full. Limits add four.

- **Every breach is recorded.** Detection, verification, classification, notice, explanation, decision and close are
  kept in the audit trail.
- **Approvals expire.** An accepted breach returns to the queue on its expiry date.
- **Hard limits stay with compliance.** The risk function routes a breach of a mandate or regulatory limit and does not
  handle it.
- **Limits are reviewed by their behaviour.** A limit that is never approached, or is breached repeatedly, is reviewed.

## Measuring value
The measures from [measuring value](08-measuring-value.md) that matter most for limits are speed and influence: how soon
a breach is known and decided, and whether the decisions are made and kept.

| Dimension | Measure for limits |
|---|---|
| Speed | Time from detection to notice; time from notice to decision |
| Capacity | Breaches handled with a full record, against those handled by email |
| Quality | Breaches first noticed outside the risk function; decisions made after their deadline |
| Influence | Breaches cured or accepted by a recorded decision; limits recalibrated from the record |
| Limits specific | Share of internal limits that were never approached, or were breached repeatedly, in a year |

In the flagship example, each breach falls from about 4.25 hours to about 0.75 hours, and a decision follows in about a
day rather than 8.5 working days. (The figures are illustrative.)

## Sources
- Financial Stability Board (2013). *Principles for an Effective Risk Appetite Framework.* Risk appetite expressed as
  limits, with roles, escalation and the link between appetite and the limits that apply it.
- Committee of Sponsoring Organizations of the Treadway Commission (2017). *Enterprise Risk Management: Integrating
  with Strategy and Performance.* Appetite, tolerance and the review of limits as part of governing risk.
