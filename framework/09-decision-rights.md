# Decision rights

## The essentials
A risk function is defined by the **decisions** it alone may make, not by a department or by the outputs it produces:
**the work is shared; the decisions are not.** The analytics engine and the [shared
record](05-principles.md#7-hand-over-judgement-not-documents) serve the whole firm, investment teams serve themselves
with the risk function's governed analyses, and the AI investigates and drafts. Each decision still has one named
decision-maker.

| Rule | In one line |
|---|---|
| Independence lives in the rules | The risk function owns what the system flags and how each risk figure is computed, and its holders report outside the investment line. |
| Self-service, independent challenge | Investment teams run what-ifs and read attribution themselves on governed analyses; the risk function owns the analyses and challenges what they show. |
| One decision-maker for each decision | However many people and systems contribute, each decision is a person's or a committee's, recorded with the one who made it, who is accountable for it. |

**Who decides what:** the portfolio manager decides what a portfolio holds. The risk function decides what counts as an
exception, sets internal limits, judges what matters, challenges and escalates. The risk committee decides what the risk
function escalates. Compliance, pricing, independent validation and product governance hold the decisions [investment
risk](02-investment-risk.md#scope-and-boundaries) assigns them.

**The size of the function:** every firm needs a risk function, and the rights stay the same whatever its size; the
number of people who hold them changes. A small firm has one person, often in a combined role outside the investment
line, with the analytics engine and the AI doing the work; a large firm has a dedicated team under one head of risk.
Every right is named, because one that is not falls in practice to the portfolio manager, and then there is no check.

The rest of this chapter is the detail behind these points.

## What defines the risk function
The function has two [purposes](00-philosophy.md#why-a-risk-function-exists): to challenge investment decisions against
the mandate, and to serve the investment team with insight into the risks it takes. Each rests on something different.

- **The challenge rests on rights.** Deciding what counts as an exception, setting internal limits, judging what
  matters, challenging and escalating can be done only by someone independent of the portfolio being overseen. These
  rights are what make the function.
- **The service rests on analyses.** A what-if before a trade or an attribution after a period is a governed analysis
  that anyone entitled to the portfolio may run. The function's service is making those analyses sound and challenging
  what they show, not running them for others on request.

Gathering data, computing and drafting are done by the analytics engine and the AI, and define no function. A risk
function is therefore the set of rights below, held by people independent of the investment line, together with the
analyses, rules and controls it owns. Its place on the organisation chart follows from that.

## Who decides what
The table names the decision-maker for each decision across the framework, and the chapter that sets out how it is made.
The step tables in each chapter name the role that holds each step: "risk manager" means the person who holds the
oversight right for that portfolio, whatever their title, and "head of risk" the person who holds the function's rights
as a whole.

| Decision | Decision-maker | Set out in |
|---|---|---|
| What a portfolio holds, and each trade | Portfolio manager | [Philosophy](00-philosophy.md#why-a-risk-function-exists) |
| What counts as an exception, how the queue is triaged, the analyses set for each rule and the list the AI may choose from | Head of risk, on the proposal of the steward of the rules | [Controls](08-controls.md#governed-parameters) |
| A new portfolio's first internal limits; a change to an internal limit | Head of risk; risk committee | [Limits and escalation](04-limits-and-escalation.md#who-approves-what) |
| A drawdown tolerance the governing documents do not state | Head of risk | [Performance risk](../pillars/performance-risk.md#mandate-terms) |
| Which items to act on first, whether each matters, and what to put to the portfolio manager | Risk manager | [Principles](05-principles.md#what-the-risk-manager-adds) |
| How a breach of an internal limit is handled | Portfolio manager; the risk committee where the risk manager disagrees | [Limits and escalation](04-limits-and-escalation.md#the-breach-lifecycle) |
| Accepting a breach of an internal limit for a set period | Head of risk | [Limits and escalation](04-limits-and-escalation.md#who-approves-what) |
| Whether a new kind of instrument can be held, as the risk function measures it | Risk manager | [Market risk](../pillars/market-risk.md#workflows-in-this-pillar) |
| Shock sizes, scenario calibration and how plausible a reverse stress is | Risk manager | [Market risk](../pillars/market-risk.md#stress-and-reverse-stress) |
| Whether the day's measures run on data with a break | Risk manager | [Data integrity](03-data-integrity.md#quality-before-computation) |
| Correcting data at source | Each domain's named owner | [Data integrity](03-data-integrity.md#who-owns-what) |
| A recommendation on a liquidity management tool | Risk manager; the tool's named owner decides its use | [Liquidity risk](../pillars/liquidity-risk.md#workflows-in-this-pillar) |
| What the AI may read, run and do, and which actions run under a governed rule | Head of risk | [Working with AI](06-working-with-ai.md#what-the-ai-may-do) |
| What the firm does about combined signals and its footprint | Risk committee | [Integrated view](../pillars/integrated-view.md#ownership) |
| Strategy capacity and the product range | Chief investment officer, informed by the reading of what the firm is paid for | [Integrated view](../pillars/integrated-view.md#what-the-firm-is-paid-for) |
| The risk function's opinion on a new portfolio; whether it launches | Head of risk; product governance | [New portfolio review](../pillars/new-portfolio-review.md#the-risk-functions-opinion) |
| The legal reading of a hard limit | Compliance | [Limits and escalation](04-limits-and-escalation.md#where-limits-come-from) |
| Prices, model validation and counterparty approval | The owners named at the boundary | [What investment risk means](02-investment-risk.md#scope-and-boundaries) |
| Where AI enters the business | Management | [Roles](09-decision-rights.md#roles) |

## Independence lives in the rules
[Deciding what the system flags](05-principles.md#what-the-risk-manager-adds) scales a risk manager's judgement across
every portfolio every day. It scales a weakened rule in the same way: a threshold loosened by someone with an interest
in a portfolio hides that portfolio every day, and no review of the queue shows what never reached it. Independence
therefore sits with whoever owns the rules.

- **The rules belong to the risk function.** The materiality thresholds, triage rules, patterns, internal limits, the
  analyses set for each rule, the governed list of analyses, the AI's permissions, the evaluation sets and the controls
  are owned by the risk function. Anyone may propose a change through the steward of the rules, and the head of risk
  decides it; a change to an internal limit goes to the risk committee. Independent validation and internal audit test
  the rules and controls themselves, as [controls](08-controls.md#alignment-with-supervisory-expectations) sets out.
- **The holders report outside the investment line.** The people who hold the oversight rights report to the head of
  risk, who reports outside the investment line.
- **Independence is of judgement, not of data.** Both sides read the same analytics engine and the same shared record.
  A challenge then argues about what a figure means, never about whose figure is right, and every exposure, risk and
  return can be explained by the same factors ([connection](00-philosophy.md#3-connection)). One system is also one
  point of error, and a wrong figure reaches both sides at once; reconciliation to source and independent validation
  catch it, not a second system.

## Self-service and challenge
The investment team serves the Construct and Assess decisions itself. Before a trade, it runs a what-if; after a period,
it reads its portfolio's attribution and its split by [source of return](01-return.md). Both run in the
[investigate mode](06-working-with-ai.md#three-modes-of-working), on governed analyses and under the entitlements of the
person who runs them. Where no governed analysis answers a question, the question is logged and the risk function
decides whether to add one.

- **The risk function owns the analyses.** What each one computes, how it is validated and when it changes are the risk
  function's decisions, so a self-served figure is the same figure the risk manager sees.
- **The risk function challenges what they show.** A what-if that crowds out the budget, or an attribution that shows
  unintended beta, is challenged in the pillar workflows whether or not the investment team ran it.
- **Figures from elsewhere are evidence to test.** A figure the investment team brings that the analytics engine did not
  compute is tested as any explanation is, and is never stated as a fact.
- **No risk staff report to the investment line.** A risk manager may be colocated with an investment team, and still
  holds the oversight right for its portfolios and reports to the head of risk.

## One decision-maker for each decision
Shared work spreads the doing; the record keeps the deciding with one person. Each decision in the shared record carries
its decision-maker's name, what they decided, the reasons, and what was generated that they relied on, as the [audit
trail](08-controls.md#the-audit-trail) sets out. A committee's decision names the committee and its chair.

Where many contribute to one decision (the analytics engine computing, the AI drafting and testing, the portfolio
manager explaining), only the decision-maker the table names decides; the others contribute evidence. A decision whose
deadline passes without a recorded decision-maker escalates, as [limits and
escalation](04-limits-and-escalation.md#escalation) sets out.

**The decision-maker is accountable.** A decision is always a person's, or a committee's, never the system's: the
analytics engine and the AI contribute evidence and never decide. The person who decides is the one held to account for
the decision. Accountability never rests with those who only contributed, whether the risk manager who ran an analysis
or the portfolio manager who explained, and a committee answers for its decision through its chair.

## Roles
| Role | What it holds |
|---|---|
| Risk manager | The oversight right for a set of portfolios: prioritising and judging items in the queue, challenging the portfolio manager, confirming what the AI extracted and reviewing what it sent or closed; a share of the function's rules |
| Head of risk | The function's rights as a whole: what the AI may do, which actions run under a governed rule, changes to the governed parameters, escalation and the acceptance of breaches; and what risk managers' time goes to |
| Portfolio manager | What the portfolio holds; answers to challenge, with evidence; with the investment team, what-ifs and attribution served on governed analyses |
| Owners of adjacent risks and of data | Their own decisions, made on the same analytics engine and shared record, with what the risk function routes to them |
| Management | Where AI enters the business, judged by the [measures of value](07-redesign-method.md#measuring-the-result), not by usage |

Within the core, three responsibilities are each held by a named person, because a responsibility everyone shares is in
practice held by no one:

- **Methodology.** What each risk measure and governed analysis computes, recorded and tested as each pillar's design
  choices set out. The analytics engine is the firm's infrastructure: one integrated system of data and logic every
  function computes on, as [principle
  2](05-principles.md#2-the-analytics-engine-computes-the-ai-interprets-and-narrates-a-person-judges) sets out. Whether
  its parts are bought or built in-house is decided with the functions that use it, and what is built passes the same
  independent validation. The risk function owns what its risk figures mean, and any change to the system that alters a
  risk figure passes through its change record. Each methodology is agreed with the functions that use it and reviewed
  with them on a set cycle, and independent validation reviews it at first use and at each material change, so the risk
  function never judges its own methods alone.
- **Stewardship of the rules.** The governed parameters, their review cycle and their change record; the steward
  proposes each change to the head of risk.
- **What the AI must get right.** The standard each AI step is held to: its evaluation set and the criteria set in
  advance, the seeded review tests and the test against the template, as [evaluation](08-controls.md#evaluation) sets
  out. Independent validation reviews the standard and validates each step against it.

These are rights held by people, not separate teams; in a small core one person holds several.

## The size of the function
Every firm needs a risk function, and its size follows the firm's: the rights do not change, the number of people who
hold them does.

**A small firm** cannot afford people dedicated to the rights. One person holds them all, often with another role
outside the investment line, and the analytics engine and the AI do the work.

- **The analytics engine and the AI do the work.** The analytics engine checks every portfolio and triages what it
  finds, and the AI investigates each item, drafts and challenges, as in any firm. The items reach the holder directly,
  never through the portfolio manager.
- **A person holds the rights.** The holder owns the rules the analytics engine and the AI run on, decides what matters,
  challenges, escalates, and signs or reviews each output. The role may be part-time and held with another outside the
  investment line, such as an independent director or the head of operations.
- **Every right is named.** A right no one is named for is held in practice by whoever makes the decision, usually the
  portfolio manager, and then there is no check.
- **The holder may sit outside the firm.** A group risk function, or a third party the firm delegates to, may hold the
  rights, and records its decisions in the same shared record under the same rules.
- **A holder inside the investment line needs safeguards.** Where a firm cannot separate the holder from the investment
  line, a body outside it, such as the risk committee, approves every change to the rules and reviews every accepted
  breach, and the arrangement is recorded with its reasons.
- **The AI is no substitute for the holder.** However independent its challenge looks, its permissions and the rules
  behind its queue are set by a person, and independence is that person's.

**A large firm** has a dedicated team: holders who do nothing else, reporting to one head of risk. The team is sized by
the portfolios that need judgement and the rules to look after, not by the outputs it produces, which the analytics
engine and the AI make. Its members may be colocated with investment teams. What holds them together is the reporting
line, one set of rules and one methodology, and review of each other's judgement, so that a breach one holder escalates
is not accepted by another. The line also gives a challenge its standing.

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
