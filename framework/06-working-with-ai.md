# Working with AI

## The essentials
**The rule:** the analytics engine computes, the AI interprets and narrates, and a person judges.

**What "AI" means:** the language model that investigates, drafts, extracts and challenges. Statistical and
machine-learning models, such as a flow forecast or a market impact model, are part of the analytics engine: fitted,
validated as models and deterministic once fitted.

**Three modes:** the AI prepares outputs, starting from the analyses the analytics engine ran for each ranked item and
following up where they point further; investigates a person's question; and challenges a conclusion against the data.
In each mode the analytics engine does the computing and a person keeps the judgement.

**What it reads:** governing documents, notices, minutes and the function's own record, never external news. What it
extracts is used only once a person has confirmed it, and what it retrieves from the record is cited as evidence,
never as a recommendation.

**Numbers:** the AI never fabricates a number. Every figure it reports has a recorded computation behind it that can be
reproduced.

**Permissions:** the AI may draft, run governed analyses and propose. Under a governed rule it may also send a routine
breach notice and close a breach that came from a data break, and a person reviews each the same day. Anything else that
leaves the function needs a person's sign-off. The AI never sends any other message, writes a recommendation, decides
what matters or changes a governed parameter.

**People:** supervising the AI is a skill. Who holds each decision, how the craft is learned and why accountability
does not move are in [decision rights](10-decision-rights.md).

The rest of this chapter is the detail behind these points.

## Three modes of working
| Mode | What starts it | What the AI does | What the person does |
|---|---|---|---|
| **Prepare** | The daily run, a trigger or a schedule | Reads the analyses the analytics engine ran for each ranked item, chooses follow-up analyses where the findings point further, then drafts explanations, notices, packs and minutes from what was found | Judges the ranked items, edits and signs off |
| **Investigate** | A person's question | Runs analyses through the analytics engine and reports the figures with the runs behind them | Asks, follows up and decides what the answer means |
| **Challenge** | A conclusion or an explanation | Tests it against the data, looks for the figures that would contradict it and reports what it finds | Weighs the challenge and decides |

**Prepare** is the mode each pillar's flagship workflow runs in. For each ranked item the analytics engine first runs
the analyses set for that kind of rule, such as the same driver across other portfolios and the tilts on record. The
rule fixes them, so they are the engine's work and arrive as computed facts. The AI's investigation starts there: it
chooses which follow-up analyses to run from the governed list, given what the first ones show, up to a set number of
runs, and drafts from all of it. It may choose none. The analyses set for each kind of rule, the list the AI may choose
from and the cap on runs are [governed parameters](08-controls.md#materiality-thresholds-as-governed-parameters). The
risk manager starts from an item already investigated, with every figure tied to its run.

**Investigate** replaces the ad hoc query, and is how an investment team [serves
itself](10-decision-rights.md#self-service-and-challenge). A risk manager, or a member of an investment team before a
trade or after a period, asks a question in plain words. Each run uses the entitlements of the person who asked, so a
member of an investment team sees figures only for the portfolios the team manages. The AI works out which analyses
answer it, runs them through the analytics engine, and reports what they show: a drill-down into a change, an
aggregation across portfolios, an attribution over a period, a what-if on a proposed trade, a scenario. Every figure is
tied to the run that produced it. Where no governed analysis answers an investment team's question, the AI says so and
the question is logged for the risk function.

**Challenge** turns the AI on a conclusion. The conclusion may be a portfolio manager's explanation of a breach, a risk
manager's own reading of a portfolio, or a draft paper for a committee. The AI looks for what would contradict it and
reports the evidence either way. A challenge is evidence put to a person, not a verdict.

**Extraction is not a mode.** It runs when a document arrives or changes, and its result is a record a person confirms
before anything uses it.

## Where a figure may come from
A figure may reach an output only from the sources below; a figure with no computation behind it is a fabrication, and
text that contains one is rejected.

| Source of a figure | What it is | May it reach an output? |
|---|---|---|
| The daily run | Computed by the analytics engine for every portfolio, with the analyses set for each ranked item's rule | Yes |
| An analysis run | One of the analytics engine's governed analyses, run by the AI with its own parameters: a drill-down, an aggregation, an attribution, a what-if, a scenario | Yes, with the run recorded |
| Simple arithmetic | A sum, a difference, a ratio, a percentage change or a simple multiple of figures from the two rows above, which the grounding check recomputes | Yes |
| A document | A figure extracted from a source passage, such as a limit in a portfolio's mandate terms or the size of a redemption in a notice | Once the risk manager has confirmed it |
| An exploratory query | A read-only query the AI composed over the risk data, where no governed analysis answers the question | No. It is labelled unvalidated, stays out of outputs and is shown only within the risk function |
| Nothing | A figure the AI stated with no computation behind it | Never |

The analyses the AI may run are a [governed parameter](08-controls.md#materiality-thresholds-as-governed-parameters),
owned by the risk function. An exploratory query is how the function learns what it cannot yet compute: one that proves
useful is adopted into the analytics engine through the same change process as any other analysis, and from then on its
figures may reach an output. The [grounding check](08-controls.md#the-grounding-check) enforces the table.

## What the AI reads
Besides what the analytics engine computed and the analyses it runs, the AI reads the
[documents](03-risk-data.md#what-the-analytics-engine-reads) the risk function keeps as received, and the function's
own record. It reads no external news or commentary, and no recording or transcript of a meeting: an event reaches it
only as data in a domain or as a document in the store, and what was said at a meeting reaches it as the risk manager's
notes.

| Source | What the AI does with it | Before it is used |
|---|---|---|
| Governing documents | Extracts the [mandate terms](../pillars/performance-risk.md#mandate-terms), including the provisions for each liquidity management tool, each linked to its passage | The risk manager confirms each term, and an expected term that was not found shows as a gap |
| Dealing notices | Reads a redemption or other notice into an event, linked to the notice | The risk manager confirms the event, which then enters the run and can fire a trigger |
| Minutes | Extracts each tilt and timing call with its decision-maker, size and date, linked to the passage | The risk manager confirms it, and the record takes the meeting's date where the minutes were received within the set window, and otherwise the date they were received |
| The function's own record | Retrieves how similar breaches were decided, and what was explained and agreed at earlier reviews; drafts a review's minutes from the risk manager's notes of it | Cited with its source beside the facts of the current case |

**Precedent informs; it does not decide.** A past decision shows how a similar case was judged, not how this one should
be. The AI cites it as evidence, and the decision stays with the people who own it.

## What the AI may do
The AI works under a permission of its own, set by the risk function: what it may read, which analyses it may run and
what it may never do. The pillar chapters state these limits where they bite; this table holds them in one place.

| The AI may | Examples |
|---|---|
| **Do alone** | Follow up each ranked item with further governed analyses, within the cap; draft text from computed facts; run a governed analysis; compose an exploratory query; start a run inside the analytics engine; extract terms, events and recorded decisions from documents, notices and minutes; cite precedent from the record; propose scenarios, questions and challenges |
| **Do under a governed rule, reviewed the same day** | The [automated actions](08-controls.md#automated-actions), where the analytics engine decides the rule applies: send a breach notice the rule covers, such as a passive breach of an internal limit on a standard template, once the grounding check passes; close a breach the engine matched to a recorded data break |
| **Do with a person's sign-off** | Anything else that leaves the function: an explanation, a notice, a pack, minutes; the terms, events and recorded decisions it extracted, before any is used |
| **Never do** | Send any other message; write a recommendation, an opinion or its conditions; decide what matters, what to escalate or whether a breach is accepted; set a shock size; change a threshold, a limit, a rule or any other governed parameter; correct data; read external news or commentary; present a precedent as a recommendation |

Everything else outward stays with a person. The AI can start work inside the analytics engine and act under a rule a
person has set, but it cannot commit the function to a view, a decision or any message the rule does not cover.

## Supervising the AI
Working with the AI is a skill, and the hardest part of it is staying critical of fluent text.

- **Read the figures before the words.** The facts and the runs are shown beside the text, so that the review is of what
  was computed and then of what was said about it.
- **Open the run.** A figure from an analysis run is correct for the question the run asked. The run shows which
  portfolios, which dates and which analysis, so the person can see whether that was the question they meant.
- **Ask what is missing.** A draft can be accurate in every figure and leave out the one that matters. No check sees an
  omission; a person who knows the portfolio does.
- **Distrust easy agreement.** An AI tends to follow the framing of the question it was asked. Asking it to argue the
  other side, in the challenge mode, is the remedy.
- **Keep the judgement.** A challenge can also manufacture doubt where the conclusion was sound. The person weighs it,
  and the decision and its reasons are theirs.

A sign-off given without reading is the failure this section exists to prevent, and it leaves no trace in the edits. The
risk function therefore reviews a sample of signed-off items against the facts and runs behind them, as each pillar sets
out for its own drafts, and tests the review with seeded drafts, as [evaluation](08-controls.md#evaluation) sets out.

## A worked exchange
A risk manager asks why Fund T's ex-ante tracking error rose over the week, and whether other portfolios are exposed to
the same thing. The AI runs three analyses and one exploratory query. **The fund and figures are illustrative.**

| Run | Kind | What was run | Result |
|---|---|---|---|
| 1 | Analysis | Tracking error by factor for Fund T, today and 5 business days ago | 3.1% and 2.4%, a rise of 0.7 points; the value factor's contribution rose from 0.5 to 1.1 points, 0.6 of the rise |
| 2 | Analysis | Value factor exposure across all portfolios, today | 6 of 40 portfolios above 0.30 |
| 3 | Exploratory query, unvalidated | Holdings of Fund T bought in the last 5 business days | 4 holdings, 3.8% of net assets |
| 4 | Analysis | Tilts and timing calls on record for Fund T | None |

> Fund T's ex-ante tracking error rose from 2.4% to 3.1% over 5 business days, and most of the rise is the value factor,
> whose contribution went from 0.5 to 1.1 points (run 1). Across the firm, 6 of 40 portfolios hold a value exposure
> above 0.30 (run 2). An exploratory query, not validated, finds 4 holdings bought in the period, 3.8% of net assets
> (run 3).

The risk manager reads this as a deliberate value tilt and asks the AI to challenge that reading.

> No tilt or timing call is on record for Fund T (run 4), so on the record the value exposure is unintended beta, not a
> tilt.

What the exposure means, and what to ask the portfolio manager, is the risk manager's judgement. The figure from the
exploratory query can guide the question, but it stays out of any output and is never shown to the portfolio manager.

## How the working relationship improves
Each mode leaves a record, and the record is how the system gets better. Edits to drafts show where the AI's
explanations miss. Challenges that changed a conclusion, and challenges that were set aside, show where it helps.
Exploratory queries show what the analytics engine cannot yet compute. The risk function reads these on a set cycle and
turns them into governed changes: a new analysis, a retuned threshold, a rule added to a pillar.

## Sources
- Parasuraman, R., Sheridan, T. and Wickens, C. (2000). A Model for Types and Levels of Human Interaction with
  Automation. *IEEE Transactions on Systems, Man, and Cybernetics, Part A*. Deciding, function by function, what
  automation does alone and what a person keeps.
- Parasuraman, R. and Manzey, D. (2010). Complacency and Bias in Human Use of Automation: An Attentional Integration.
  *Human Factors*. Why people over-trust automated output, and why review has to be designed and tested.
- Bainbridge, L. (1983). Ironies of Automation. *Automatica*. Automating the routine work removes the practice that
  built the skill to supervise it.
- National Institute of Standards and Technology (2023). *Artificial Intelligence Risk Management Framework (AI RMF
  1.0).* Defined roles and responsibilities for the people who oversee AI systems.
