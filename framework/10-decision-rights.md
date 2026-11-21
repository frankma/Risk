# Decision rights

## The essentials
**The rule:** a risk function is defined by the decisions it alone may make, not by a department or by the outputs it
produces. **The work is shared; the decisions are not.** The analytics engine and the [shared
record](05-principles.md#7-hand-over-judgement-not-documents) serve the whole firm, portfolio managers serve themselves
with the risk function's governed analyses, and the AI investigates and drafts. Each decision still has one named
holder.

| Rule | In one line |
|---|---|
| Independence lives in the rules | The risk function owns what the system flags and how each risk figure is computed, and its holders report outside the investment line. |
| Self-service, independent challenge | Portfolio managers run what-ifs and read attribution themselves on governed analyses; the risk function owns the analyses and challenges what they show. |
| One holder for each decision | However many people and systems contribute, each decision is recorded with the one person or body that made it. |

**Who decides what:** the portfolio manager decides what a portfolio holds. The risk function decides what counts as an
exception, sets internal limits, judges what matters, challenges and escalates. The risk committee settles what the two
cannot agree. Compliance, pricing, independent validation and product governance hold the decisions [investment
risk](01-investment-risk.md#scope-and-boundaries) assigns them.

**The size of the core:** the rights stay the same whatever the size of the firm; the number of people who hold them
changes. A small, senior core holds the oversight rights, owns the rules and controls, and learns the craft by
investigating and judging.

The rest of this chapter is the detail behind these points.

## What defines the risk function
The function has two [roles](00-philosophy.md#why-a-risk-function-exists): a check and balance on every portfolio's
risk, and a service to the investment process. Each rests on something different.

- **The check and balance rests on rights.** Deciding what counts as an exception, setting internal limits, judging what
  matters, challenging and escalating can be done only by someone independent of the portfolio being overseen. These
  rights are what make the function.
- **The service rests on analyses.** A what-if before a trade or an attribution after a period is a governed analysis
  that anyone entitled to the portfolio may run. The function's service is making those analyses sound and challenging
  what they show, not running them for others on request.

Gathering data, computing and drafting are done by the analytics engine and the AI, and define no function. A risk
function is therefore the set of rights below, held by people independent of the investment line, together with the
analyses, rules and controls it owns. Its place on the organisation chart follows from that.

## Who decides what
The table names the holder of each decision across the framework, and the chapter that sets out how it is made. The step
tables in each chapter name the role that holds each step: "risk manager" means the person who holds the oversight right
for that portfolio, whatever their title, and "head of risk" the person who holds the function's rights as a whole.

| Decision | Holder | Set out in |
|---|---|---|
| What a portfolio holds, and each trade | Portfolio manager | [Philosophy](00-philosophy.md#why-a-risk-function-exists) |
| What counts as an exception, how the queue is ranked, the analyses set for each rule and the list the AI may choose from | Risk function, through the change record | [Controls](08-controls.md#materiality-thresholds-as-governed-parameters) |
| A new portfolio's first internal limits; a change to an internal limit | Head of risk; risk committee | [Limits and escalation](04-limits-and-escalation.md#who-approves-what) |
| Whether a ranked item matters, and what to put to the portfolio manager | Risk manager | [Principles](05-principles.md#what-the-risk-manager-adds) |
| How a breach of an internal limit is handled | Portfolio manager and risk manager together; the risk committee where they disagree | [Limits and escalation](04-limits-and-escalation.md#the-breach-lifecycle) |
| Accepting a breach of an internal limit for a set period | Head of risk | [Limits and escalation](04-limits-and-escalation.md#who-approves-what) |
| Shock sizes, scenario calibration and how plausible a reverse stress is | Risk manager | [Market risk](../pillars/market-risk.md#stress-and-reverse-stress) |
| Whether the day's measures run on data with a break | Risk manager | [Risk data](03-risk-data.md#quality-before-computation) |
| A recommendation on a liquidity management tool | Risk manager; the tool's named owner decides its use | [Liquidity risk](../pillars/liquidity-risk.md#workflows-in-this-pillar) |
| What the AI may read, run and do, and which actions run under a governed rule | Head of risk | [Working with AI](06-working-with-ai.md#what-the-ai-may-do) |
| What the firm does about combined signals and its footprint | Risk committee | [Integrated view](../pillars/integrated-view.md#ownership) |
| The risk function's opinion on a new portfolio; whether it launches | Head of risk; product governance | [New portfolio review](../pillars/new-portfolio-review.md#the-risk-functions-opinion) |
| The legal reading of a hard limit | Compliance | [Limits and escalation](04-limits-and-escalation.md#where-limits-come-from) |
| Prices, model validation and counterparty approval | The owners [investment risk](01-investment-risk.md#scope-and-boundaries) names | Investment risk |
| Where AI enters the business | Management | [Roles](10-decision-rights.md#roles) |

## Independence lives in the rules
[Deciding what the system flags](05-principles.md#what-the-risk-manager-adds) scales a risk manager's judgement across
every portfolio every day. It scales a weakened rule in the same way: a threshold loosened by someone with an interest
in a portfolio hides that portfolio every day, and no review of the queue shows what never reached it. Independence
therefore sits with whoever owns the rules.

- **The rules belong to the risk function.** The materiality thresholds, ranking rules, patterns, internal limits, the
  analyses set for each rule, the governed list of analyses, the AI's permissions, the evaluation sets and the controls
  are owned by the risk function. Anyone may propose a change; the risk function decides it through the change record,
  and independent validation and internal audit test the rules and controls themselves, as
  [controls](08-controls.md#alignment-with-supervisory-expectations) sets out.
- **The holders report outside the investment line.** The people who hold the oversight rights report to the head of
  risk, who reports outside the investment line, and their pay does not depend on the results of the portfolios they
  oversee.
- **Independence is of judgement, not of data.** Both sides read the same analytics engine and the same shared record.
  A challenge then argues about what a figure means, never about whose figure is right, and every exposure, risk and
  return can be explained by the same factors ([connection](00-philosophy.md#3-connection)).

## Self-service and challenge
The portfolio manager serves the Construct and Assess decisions themselves. Before a trade, they run a what-if; after a
period, they read their portfolio's attribution and its split by [source of return](02-sources-of-return.md). Both run
in the [investigate mode](06-working-with-ai.md#three-modes-of-working), on governed analyses and under the portfolio
manager's entitlements. Where no governed analysis answers their question, the question is logged and the risk function
decides whether to add one.

- **The risk function owns the analyses.** What each one computes, how it is validated and when it changes are the risk
  function's decisions, so a self-served figure is the same figure the risk manager sees.
- **The risk function challenges what they show.** A what-if that crowds out the budget, or an attribution that shows
  unintended beta, is challenged in the pillar workflows whether or not the portfolio manager ran it.
- **Figures from elsewhere are evidence to test.** A figure a portfolio manager brings that the analytics engine did not
  compute is tested as any explanation is, and is never stated as a fact.
- **No risk staff report to the investment line.** A risk manager may work alongside an investment team, and still holds
  the oversight right for its portfolios and reports to the head of risk.

## One holder for each decision
Shared work spreads the doing; the record keeps the deciding with one person. Each decision in the shared record carries
its holder's name, what they decided, the reasons, and what was generated that they relied on, as the [audit
trail](08-controls.md#the-audit-trail) sets out. A committee's decision names the committee and its chair.

Where many contribute to one decision (the analytics engine computing, the AI drafting and testing, the portfolio
manager explaining), only the holder the table names decides; the others contribute evidence. A decision whose deadline
passes without a recorded holder escalates, as [limits and escalation](04-limits-and-escalation.md#escalation) sets
out.

## Roles
| Role | What it holds |
|---|---|
| Risk manager | The oversight right for a set of portfolios: judging ranked items, challenging the portfolio manager, confirming what the AI extracted and reviewing what it sent or closed; a share of the function's rules |
| Head of risk | The function's rights as a whole: what the AI may do, which actions run under a governed rule, escalation and the acceptance of breaches; and what risk managers' time goes to |
| Portfolio manager | What the portfolio holds; what-ifs and attribution served on governed analyses; answers to challenge, with evidence |
| Owners of adjacent risks and of data | Their own decisions, made on the same analytics engine and shared record, with what the risk function routes to them |
| Management | Where AI enters the business, judged by the [measures of value](09-measuring-value.md), not by usage |

Within the core, three responsibilities are held by named people:

- **Methodology.** What each risk measure and governed analysis computes, recorded and tested as each pillar's design
  choices set out. The analytics engine runs as a platform for the whole firm; the risk function owns what its risk
  figures mean.
- **Stewardship of the rules.** The governed parameters, their review cycle and their change record.
- **Evaluation of the AI.** The evaluation sets, the seeded review tests and the test against the template, as
  [evaluation](08-controls.md#evaluation) sets out.

These are rights held by people, not separate teams; in a small core one person holds several.

## The size of the core
The rights do not change with the size of the firm; the number of people who hold them does. In a small firm one person
may hold every oversight right. Where a firm cannot separate that person from the investment line, the safeguards that
stand in for separation, such as the risk committee's review of the rules and of every accepted breach, are recorded.

## Learning the craft
Supervising the analytics engine and the AI needs people who know what a normal reading looks like and can tell when a
figure or an account is wrong. The craft is learned by investigating and judging: new risk managers investigate with the
AI and explain what they found, review signed-off items beside an experienced colleague, and take part in setting the
rules that decide what the system flags.

**Accountability does not move.** The AI cannot be held to account, so a named person signs every output, or reviews the
same day what a governed rule let the AI send or close, and that person can show what was generated, what they changed
and why.

## Sources
- Fama, E. and Jensen, M. (1983). Separation of Ownership and Control. *Journal of Law and Economics*. Separating the
  management of decisions (initiating and carrying them out) from their control (ratifying and monitoring them).
- Institute of Internal Auditors (2020). *The IIA's Three Lines Model: An Update of the Three Lines of Defense.* Roles
  defined by accountability, with independence for the roles that oversee and assure.
- Bainbridge, L. (1983). Ironies of Automation. *Automatica*. Automating the routine work removes the practice that
  built the skill to supervise it.
