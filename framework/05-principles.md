# Principles

## In short
**The rule:** AI changes investment risk work when a workflow is redesigned around it, not when it is inserted into the
workflow as it stands. The unit of change is the workflow, not the task.

| # | Principle | In one line |
|---|---|---|
| 1 | Redesign, don't insert | Start from the outcome, then rebuild the steps. |
| 2 | The risk engine computes, AI analyses and narrates, a human judges | Each kind of work goes to the owner suited to it. |
| 3 | The AI never fabricates a number | Every figure has a recorded computation behind it; generated text is checked against it. |
| 4 | Exceptions over everything | The system reviews every portfolio; the human reviews what is material. |
| 5 | Decide what the risk manager's time is for before starting | Time that is not directed is absorbed by existing work. |
| 6 | Build what the manual process could not do | Look for capabilities that need every portfolio checked continuously. |

**Why inserting fails:** a tool placed inside a workflow that was designed for a manual process leaves that process's
constraints in place. A report whose commentary is drafted faster still waits for data to be gathered, for work to pass
between people and for review queues, so it arrives on the same day and says the same thing.

**What the risk manager adds:** once the system produces the outputs, the risk manager's time goes to judging what
matters, bringing clarity to the risks being taken, challenging with evidence and deciding what the system flags.

The rest of this chapter is the detail behind these points. [Working with AI](06-working-with-ai.md) follows with how
people and the AI work together.

## Six principles
### 1. Redesign, don't insert
**What it means.** A workflow exists to deliver an outcome, such as a decision made, a limit enforced or a portfolio
manager challenged. A redesign starts from that outcome and asks which steps it actually needs, rather than starting
from the existing steps and asking which of them AI can speed up.

**In practice.** Each workflow is redesigned end to end, using the [redesign method](07-redesign-method.md): unused
outputs are stopped (step 2), and steps that exist only because the old process was slow are removed rather than
automated (step 4).

### 2. The risk engine computes, AI analyses and narrates, a human judges
**What it means.** Each kind of work goes to its owner: the risk engine computes, the AI analyses, drafts, extracts and
challenges a conclusion against the data, and the risk manager judges, escalates and signs off. When the AI's work needs
a figure, the AI runs the analysis through the risk engine and does not compute it itself.

**In practice.** Each step of a redesigned workflow is assigned to exactly one of the three owners. Where a step mixes
kinds of work, it is split. A system in which the AI does the arithmetic itself, or in which a person re-types figures
that the risk engine produced, has the wrong owner for that step. [Working with AI](06-working-with-ai.md) sets out how
the person and the AI then work together.

### 3. The AI never fabricates a number
**What it means.** A risk output with a wrong figure in it is worse than no output. Every figure has a recorded
computation behind it, and generated text passes the grounding check before anyone sees it.

**In practice.** [Working with AI](06-working-with-ai.md#where-a-figure-may-come-from) sets out where a figure may come
from, and [controls](08-controls.md#the-grounding-check) how the check works. The check, and the other controls that
make it safe to rely on generated text, are what allow manual checking to be reduced.

### 4. Exceptions over everything
**What it means.** The system checks every portfolio against every threshold and ranks the results; the human reviews
what is material.

**In practice.** The main output of a monitoring workflow is a ranked exception queue with an explanation for each item,
not a long pack. The materiality thresholds that decide what counts as an exception are set by the risk function and
governed as parameters. The [market risk](../pillars/market-risk.md) chapter applies this to daily monitoring.

### 5. Decide what the risk manager's time is for before starting
**What it means.** A redesign changes what a risk manager spends time on, and time that is not directed is absorbed by
existing work. The use of the time is a design decision, made at the start rather than discovered at the end.

**In practice.** Before a workflow is redesigned, the risk function records what the risk manager's time will go to, for
example deeper portfolio reviews or more frequent challenge of portfolio managers, and then tracks whether that happens.
[Measuring value](09-measuring-value.md) sets out how.

### 6. Build what the manual process could not do
**What it means.** Doing the old process faster has a ceiling: at best the old output arrives sooner. A redesign also
looks for what the manual process could not do at all, because it needed more data, more frequent checks or more
connections than people could manage.

**In practice.** Once the risk engine covers every portfolio continuously, liquidity can be monitored continuously
rather than at each periodic stress test, and signals can be connected across market, liquidity and performance risk to
see where they combine. The [integrated view](../pillars/integrated-view.md) is the clearest example.

## What the risk manager adds
Under a manual process, much of a risk manager's time goes into producing outputs: gathering data, building tables,
writing commentary and checking that the figures agree. Under a redesigned process, the system produces the outputs, and
the risk manager's time goes to the work only a person can do, in both of the function's
[roles](00-philosophy.md#why-a-risk-function-exists): check and balance, and serving the investment process.

| From | To |
|---|---|
| Producing reports and packs | Judging ranked exceptions and watch items |
| Policing limits after the fact | Bringing clarity to the risks being taken, before and after the trade |
| Explaining figures after the fact | Challenging portfolio managers' decisions with evidence |
| Applying thresholds by hand | Deciding what the system flags, and in what order |

The value a risk manager adds is not the sign-off. The sign-off is how a person is held accountable for an output; what
they add is what goes into it.

- **Judging what matters to the portfolio and its intended risk profile.** The risk engine ranks readings by their size
  against a threshold; the risk manager decides whether a reading matters for this portfolio, given the risks its
  mandate intends. That means telling intended risk from unintended, telling signals that are connected from signals
  that merely appear together, and seeing when a drafted explanation gives weight to the wrong driver, which the
  grounding check cannot test.
- **Bringing clarity to the risks being taken.** Every unit of active risk should be paid for ([belief
  3](00-philosophy.md#beliefs)). The risk manager makes clear which risks a portfolio runs, whether they were chosen,
  what each uses of the budget and whether it is paid for. Before a trade, a what-if shows what a position adds and what
  it crowds out of the budget; after it, the review shows which bets earned their risk. That clarity lets the portfolio
  manager take risk deliberately.
- **Challenge that changes decisions.** Evidence put to the portfolio manager, and escalation where an issue stays
  unresolved. Influence is the dimension of [value](09-measuring-value.md#influence) closest to the function's purpose.
- **Deciding what the system flags, and in what order.** The thresholds that decide what reaches the queue, the ranking
  that orders it, the patterns that connect the pillars and the calibration of scenarios are where judgement is written
  down. They filter what the risk manager sees, not what the portfolio may hold, and the risk function designs, tests
  and owns them.
- **Judgement where the data runs out.** Shock sizes, how plausible a reverse stress is, regime changes, crowded exits
  and the direction in which each model errs ([beliefs 4 and 8](00-philosophy.md#beliefs)) have no history for the risk
  engine to compute from.

Deciding what the system flags matters most, because it scales: done well, it makes a risk manager's judgement apply
across every portfolio every day, not only to the portfolios they had time to look at.

## Sources
- Hammer, M. (1990). Reengineering Work: Don't Automate, Obliterate. *Harvard Business Review*. Rebuilding a process
  around what a technology makes possible, instead of automating the steps of the old one.
