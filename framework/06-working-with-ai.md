# Working with AI

The [principles](05-principles.md) divide the work between the risk engine, the AI and a person. This chapter sets out
how the person and the AI then work together: three modes of working, where a figure may come from, what the AI may do
alone, with sign-off or never, how people supervise it, and what changes for the people involved. It is written for
the whole firm, because the working relationship reaches beyond the risk function to the portfolio managers who
receive its questions and the management that decides where AI enters the business.

## Three modes of working
The AI does more than draft. It works in three modes, and in each one the risk engine does the computing and a person
keeps the judgement.

| Mode | What starts it | What the AI does | What the person does |
|---|---|---|---|
| **Prepare** | The daily run, a trigger or a schedule | Drafts explanations, notices, packs and minutes from what the risk engine found | Judges the ranked items, edits and signs off |
| **Investigate** | A person's question | Runs analyses through the risk engine and reports the figures with the runs behind them | Asks, follows up and decides what the answer means |
| **Challenge** | A conclusion or an explanation | Tests it against the data, looks for the figures that would contradict it and reports what it finds | Weighs the challenge and decides |

**Prepare** is the mode the pillar chapters redesign their flagship workflows around: the system produces the output and
the person reviews the exceptions.

**Investigate** replaces the ad hoc query. A risk manager, or a portfolio manager before a trade, asks a question in
plain words. The AI works out which analyses answer it, runs them through the risk engine, and reports what they show:
a drill-down into a change, an aggregation across portfolios, an attribution over a period, a what-if on a proposed
trade, a scenario. The answer arrives in minutes, with every figure tied to the run that produced it.

**Challenge** turns the AI on a conclusion. The conclusion may be a portfolio manager's explanation of a breach, a risk
manager's own reading of a portfolio, or a draft paper for a committee. The AI looks for what would contradict it and
reports the evidence either way. A challenge is evidence put to a person, not a verdict.

## Where a figure may come from
**The AI never fabricates a number.** Every figure it reports has a computation behind it that is recorded and can be
reproduced. Aggregating and attributing produce numbers, and the AI may do both, because the risk engine does the
arithmetic and the AI only chooses what to run. A figure with no computation behind it is a fabrication, and text that
contains one is rejected.

| Source of a figure | What it is | May it reach an output? |
|---|---|---|
| The daily run | Computed by the risk engine for every portfolio | Yes |
| An analysis run | One of the risk engine's governed analyses, run by the AI with its own parameters: a drill-down, an aggregation, an attribution, a what-if, a scenario | Yes, with the run recorded |
| Simple arithmetic | A sum, a difference, a ratio or a percentage change of figures from the two rows above, which the grounding check recomputes | Yes |
| A document | A figure extracted from a source passage, such as a limit in a portfolio's mandate terms | Once the risk manager has confirmed it |
| An exploratory query | A read-only query the AI composed over the risk data, where no governed analysis answers the question | No. It is labelled unvalidated and stays out of outputs |
| Nothing | A figure the AI stated with no computation behind it | Never |

The analyses the AI may run are a [governed parameter](08-controls.md#materiality-thresholds-as-governed-parameters),
owned by the risk function. An exploratory query is how the function learns what it cannot yet compute: one that proves
useful is adopted into the risk engine through the same change process as any other analysis, and from then on its
figures may reach an output. The [grounding check](08-controls.md#the-grounding-check) enforces the table.

## What the AI may do
The AI works under a permission of its own, set by the risk function: what it may read, which analyses it may run and
what it may never do. The pillar chapters state these limits where they bite; this table holds them in one place.

| The AI may | Examples |
|---|---|
| **Do alone** | Draft text from computed facts; run a governed analysis; compose an exploratory query; start a run inside the risk engine; propose scenarios, questions and challenges |
| **Do with a person's sign-off** | Anything that leaves the function: an explanation, a notice, a pack, minutes; the mandate terms it extracted from a portfolio's documents |
| **Never do** | Send a message; write a recommendation, an opinion or its conditions; decide what matters, what to escalate or whether a breach is accepted; set a shock size; change a threshold, a limit, a rule or any other governed parameter; correct data |

Everything outward stays with a person. The AI can start work inside the risk engine, but it cannot commit the function
to a view, a message or a decision.

## Supervising the AI
Working with the AI is a skill, and the hardest part of it is staying critical of fluent text.

- **Read the figures before the words.** The facts and the runs are shown beside the text, so that the review is of
  what was computed and then of what was said about it.
- **Open the run.** A figure from an analysis run is correct for the question the run asked. The run shows which
  portfolios, which dates and which analysis, so the person can see whether that was the question they meant.
- **Ask what is missing.** A draft can be accurate in every figure and leave out the one that matters. No check sees an
  omission; a person who knows the portfolio does.
- **Distrust easy agreement.** An AI tends to follow the framing of the question it was asked. Asking it to argue the
  other side, in the challenge mode, is the remedy.
- **Keep the judgement.** A challenge can also manufacture doubt where the conclusion was sound. The person weighs it,
  and the decision and its reasons are theirs.

A sign-off given without reading is the failure this section exists to prevent, and it leaves no trace in the edits. The
risk function therefore reviews a sample of signed-off items against the facts and runs behind them, as each pillar
sets out for its own drafts.

## A worked exchange
A risk manager asks why Fund T's ex-ante tracking error rose over the week, and whether other portfolios are exposed
to the same thing. The AI runs three analyses and one exploratory query. **The fund and figures are illustrative.**

| Run | Kind | What was run | Result |
|---|---|---|---|
| 1 | Analysis | Tracking error by factor for Fund T, today and 5 business days ago | 3.1% and 2.4%; the value factor's contribution rose from 0.5 to 1.1 points |
| 2 | Analysis | Value factor exposure across all portfolios, today | 6 of 40 portfolios above 0.30 |
| 3 | Exploratory query, unvalidated | Holdings of Fund T bought in the last 5 business days | 4 holdings, 3.8% of net assets |
| 4 | Analysis | Tilts and timing calls on record for Fund T | None |

> Fund T's ex-ante tracking error rose from 2.4% to 3.1% over 5 business days, and most of the rise is the value
> factor, whose contribution went from 0.5 to 1.1 points (run 1). Across the firm, 6 of 40 portfolios hold a value
> exposure above 0.30 (run 2). An exploratory query, not validated, suggests the rise came with 4 holdings bought in
> the period, 3.8% of net assets (run 3).

The risk manager reads this as a deliberate value tilt and asks the AI to challenge that reading.

> No tilt or timing call is on record for Fund T (run 4), so on the record the value exposure is unintended beta, not
> a tilt.

What the exposure means, and what to ask the portfolio manager, is the risk manager's judgement. The figure from the
exploratory query can guide the question, but it stays out of any output.

## What changes for people
| Who | What changes |
|---|---|
| Risk manager | Less time producing outputs and more judging them, with a new skill: directing and supervising the AI |
| Head of risk | Owns what the AI may do in the function, the rules it works within and what risk managers' time goes to |
| Portfolio manager | Receives questions sooner and with evidence, can ask for a what-if before a trade, and has explanations tested against the data |
| Owners of adjacent risks and of data | Receive what is routed to them with the evidence attached |
| Management | Decides, workflow by workflow, where AI enters the business, and judges the result by the [measures of value](09-measuring-value.md), not by usage |

**The craft still has to be learned.** Producing outputs by hand was how a new risk manager learned what a normal
reading looks like. When the system produces the output, that learning is designed in: new risk managers investigate
with the AI and explain what they found, review signed-off items beside an experienced colleague, and take part in
setting the rules that decide what the system flags.

**Accountability does not move.** The AI cannot be held to account, so a named person signs every output, and that
person can show what was generated, what they changed and why.

## How the working relationship improves
Each mode leaves a record, and the record is how the system gets better. Edits to drafts show where the AI's
explanations miss. Challenges that changed a conclusion, and challenges that were set aside, show where it helps.
Exploratory queries show what the risk engine cannot yet compute. The risk function reads these on a set cycle and
turns them into governed changes: a new analysis, a retuned threshold, a rule added to a pillar.

## Sources
- Parasuraman, R., Sheridan, T. and Wickens, C. (2000). A Model for Types and Levels of Human Interaction with
  Automation. *IEEE Transactions on Systems, Man, and Cybernetics, Part A*. Deciding, function by function, what
  automation does alone and what a person keeps.
- Parasuraman, R. and Manzey, D. (2010). Complacency and Bias in Human Use of Automation: An Attentional Integration.
  *Human Factors*. Why people over-trust automated output, and why review has to be designed and tested.
- Bainbridge, L. (1983). Ironies of Automation. *Automatica*. Automating the routine work removes the practice that
  built the skill to supervise it.
- National Institute of Standards and Technology (2023). *Artificial Intelligence Risk Management Framework
  (AI RMF 1.0).* Defined roles and responsibilities for the people who oversee AI systems.
