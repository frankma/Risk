# Principles

AI produces a return in investment risk when the workflow is redesigned around it, not when it is inserted into the
workflow as it stands. This chapter sets out why insertion fails and the six principles a redesign should follow, then
sets out what the risk manager adds once the system produces the outputs. The [philosophy](00-philosophy.md) sets out
what the function is for; these principles set out how to redesign its work around AI.

## The problem: insertion, not redesign
Many asset managers now give their staff AI tools, but few can show a measurable return from them. The tools usually
work as intended. The return is missing because the tools are placed inside workflows that were designed for a manual
process, and the constraints of that process stay in place.

Take a recurring monthly risk report. Its cycle runs three to four weeks from month end to distribution. An AI tool that
drafts the commentary in four hours instead of fourteen looks like a large saving, yet the report still goes out on the
same day. The commentary was never the bottleneck: most of the cycle was spent gathering data from several systems,
handing work between people and waiting in review queues. Saving ten hours inside a cycle of more than three weeks
changes neither when the report arrives nor what it says. (The figures are illustrative.)

The evidence points the same way. A large survey of organisations using generative AI tested 25 organisational
attributes and found that workflow redesign had the biggest effect on whether they saw an impact on earnings (see
Sources). The lesson for a risk function is that the unit of change is the workflow, not the task.

## Six principles

| # | Principle | In one line |
|---|---|---|
| 1 | Redesign, don't insert | Start from the outcome, then rebuild the steps. |
| 2 | The risk engine computes, AI narrates, a human judges | Each kind of work goes to the owner suited to it. |
| 3 | The AI never produces a number | Every figure comes from the risk engine; generated text is checked against it. |
| 4 | Exceptions over everything | The system reviews every portfolio; the human reviews what is material. |
| 5 | Decide where freed time goes before starting | Unredirected hours never show up as value. |
| 6 | New capabilities beat faster old ones | The largest gains are things the manual process could not do. |

### 1. Redesign, don't insert
**What it means.** A workflow exists to deliver an outcome, such as a decision made, a limit enforced or a portfolio
manager challenged. A redesign starts from that outcome and asks which steps it actually needs, rather than starting
from the existing steps and asking which of them AI can speed up.

**In practice.** Each workflow is redesigned end to end, using the [redesign method](04-redesign-method.md). Steps that
exist only because the old process was slow, such as re-keying data, reformatting tables or chasing inputs, are removed
rather than automated. An output that feeds no decision is stopped rather than produced faster.

### 2. The risk engine computes, AI narrates, a human judges
**What it means.** The work in a risk workflow falls into three kinds, and each has a natural owner. Gathering data,
calculating measures and comparing them to limits must be exact and reproducible, so it belongs to the risk engine: the
deterministic part of the system, where the same data always gives the same figure and every figure can be traced and
reproduced. Explaining what changed, drafting text and extracting information from documents is language and pattern
work, which the AI assistant does in seconds. Deciding what matters, escalating and signing off require judgement and
accountability, and belong to the risk manager, and to the head of risk where escalation or sign-off requires it.

**In practice.** Each step of a redesigned workflow is assigned to exactly one of the three owners. Where a step mixes
kinds of work, it is split. A system in which AI calculates, or in which a person re-types figures that the risk engine
produced, has the wrong owner for that step.

### 3. The AI never produces a number
**What it means.** Language models can produce plausible figures that are wrong, and a risk output with a wrong figure
in it is worse than no output. Every number therefore comes from the risk engine that computed it from data. The AI
interprets: it writes text around the figures it is given, and at most combines them in simple ways that can be
checked, such as a difference or a ratio. It never originates a number.

**In practice.** Generated text passes a grounding check before anyone sees it: every number in it is matched against
the computed values it was generated from, or recomputed from them, and text with a number that cannot be traced is
rejected. This check, and the other [controls](05-controls.md) that make it safe to rely on generated text, are what
allow manual checking to be reduced.

### 4. Exceptions over everything
**What it means.** A manual process cannot review every portfolio in depth every day, so it samples or reviews
everything at a shallow level. A redesigned workflow lets the system check every portfolio against every threshold and
rank the results, so that the human reviews what is material instead of handing over everything.

**In practice.** The main output of a monitoring workflow is a ranked exception queue with an explanation for each
item, not a long pack. The materiality thresholds that decide what counts as an exception are set by the risk function
and governed as parameters. The [market risk](../pillars/market-risk.md) chapter applies this to daily monitoring.

### 5. Decide where freed time goes before starting
**What it means.** A redesign frees time, but freed time that is not redirected disappears into existing work and
never shows up as value. The use of the time is a design decision, made at the start rather than discovered at the end.

**In practice.** Before a workflow is redesigned, the risk function records what the freed capacity will be spent on,
for example deeper portfolio reviews or more frequent challenge of portfolio managers, and then tracks whether that
happens. [Measuring value](06-measuring-value.md) sets out how.

### 6. New capabilities beat faster old ones
**What it means.** Doing the old process faster has a ceiling: at best the old output arrives sooner. The larger gains
come from things the manual process could not do at all, because they needed more data, more frequent checks or more
connections than people could manage.

**In practice.** A redesign looks for capabilities that become possible once the risk engine covers every portfolio
continuously: monitoring liquidity continuously rather than at each periodic stress test, or connecting signals across
market, liquidity and performance risk to see where they combine. The [integrated view](../pillars/integrated-view.md)
is the clearest example.

## What the risk manager adds
Under a manual process, much of a risk manager's time goes into producing outputs: gathering data, building tables,
writing commentary and checking that the figures agree. Under a redesigned process, the system produces the outputs,
and the risk manager's time goes to the work only a person can do.

| From | To |
|---|---|
| Producing reports and packs | Judging ranked exceptions and watch items |
| Policing limits after the fact | Bringing clarity to the risks being taken, before and after the trade |
| Explaining figures after the fact | Challenging portfolio managers' decisions with evidence |
| Applying thresholds by hand | Deciding what the system flags, and in what order |

The value a risk manager adds is not the sign-off. The sign-off is how a person is held accountable for an output;
what they add is what goes into it.

- **Judging what matters to the portfolio and its intended risk profile.** The risk engine ranks readings by their
  size against a threshold; the risk manager decides whether a reading matters for this portfolio, given the risks its
  mandate intends. That means telling intended risk from unintended, telling signals that are connected from signals
  that merely appear together, and seeing when a drafted explanation gives weight to the wrong driver, which the
  grounding check cannot test.
- **Bringing clarity to the risks being taken.** Risk and return are two sides of one coin
  ([belief 3](00-philosophy.md#beliefs)). The risk manager makes clear which risks a portfolio runs, whether they were
  chosen, what each uses of the budget and whether it is paid for. Before a trade, a what-if shows what a position adds
  and what it crowds out of the budget; after it, the review shows which bets earned their risk. That clarity lets the
  portfolio manager take risk deliberately, and the return follows from deliberate risk-taking. The risk manager stays
  independent of the investment team, and that independence is what makes the clarity credible.
- **Challenge that changes decisions.** Evidence put to the portfolio manager, and escalation where an issue stays
  unresolved. Influence is the dimension of [value](06-measuring-value.md#influence) closest to the function's
  purpose.
- **Deciding what the system flags, and in what order.** The thresholds that decide what reaches the queue, the
  ranking that orders it, the patterns that connect the pillars and the calibration of scenarios are where judgement is
  written down. They filter what the risk manager sees, not what the portfolio may hold, and the risk function
  designs, tests and owns them.
- **Judgement where the data runs out.** Shock sizes, how plausible a reverse stress is, regime changes, crowded exits
  and the direction in which each model errs ([beliefs 4 and 8](00-philosophy.md#beliefs)) have no history for the
  risk engine to compute from.

Deciding what the system flags matters most, because it scales. Done well, it makes a risk manager's judgement apply
across every portfolio every day, not only to the portfolios they had time to look at. The sign-off rests on all five,
and the role becomes less about producing information and more about deciding what it means, acting on it and giving
each portfolio clarity on the risks it takes.

## Sources
- McKinsey & Company (2025). *The State of AI: How Organizations Are Rewiring to Capture Value.* Global survey,
  March 2025. Workflow redesign as the attribute with the largest effect on the earnings impact of generative AI.
