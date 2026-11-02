# Redesign method

A workflow is redesigned in seven steps, from defining the outcome it exists to deliver to measuring whether the
redesign delivered it. This chapter sets out each step, runs one generic workflow through all seven, and closes with
the failure modes that most often prevent a return. It is the core of the framework: the
[principles](01-principles.md) say what a redesign should achieve, and this method says how.

## The seven steps

| Step | Question it answers |
|---|---|
| 1. Define the outcome | What is this workflow for? |
| 2. Inventory the workflows | What do we produce, for whom, and at what cost? |
| 3. Map the current state | Where does the time actually go? |
| 4. Assign each step an owner | Who or what should do each step? |
| 5. Redesign the flow | What does the workflow look like when built around those owners? |
| 6. Build in controls | What makes it safe to rely on? |
| 7. Measure and reinvest | Did it work, and where did the freed time go? |

### 1. Define the outcome
Each workflow is described by the outcome it delivers, in one sentence, not by the tasks it involves. "Produce the
monthly risk pack" is a task. "Ensure that the risk committee knows which funds have moved outside their intended risk
profile and why, in time to act" is an outcome. The outcome sentence is the test for every later step: a step that
does not serve it is a candidate for removal.

### 2. Inventory the workflows
The risk function lists its recurring workflows and records, for each one, its cadence, its inputs, its output, who
uses the output and for which decision, and how many hours a cycle takes. The inventory usually shows outputs that feed
no decision: a report produced because it has always been produced, or a table nobody reads. These are eliminated, not
automated. Automating an unused output turns a waste of time into a waste of money.

### 3. Map the current state
The chosen workflow is mapped step by step as it actually runs, not as the procedure describes it. Each step is tagged
with the kind of work it is.

| Tag | Meaning |
|---|---|
| Gather | Pull data, find documents |
| Compute | Calculate, compare to limits |
| Interpret | Explain what changed and why |
| Judge | Decide whether it matters and what to do |
| Communicate | Write it up, send it |
| Approve / Wait | Sign-offs, queues |

Each step also records the time it takes and the elapsed time it adds, which are often very different: a sign-off that
takes ten minutes may add three days of waiting. The map nearly always shows that most of the elapsed time sits in
Gather and Approve / Wait, not in the steps that require expertise.

### 4. Assign each step an owner
Each tagged step is assigned to one owner, following the core pattern.

| Tag | Owner |
|---|---|
| Gather, Compute | Code |
| Interpret, Communicate | AI drafts; the risk manager edits and approves |
| Judge, Approve | The risk manager, or the head of risk for escalation and sign-off |
| Steps that exist only because the old process was slow | Eliminated |

The last row matters as much as the others. Re-keying figures between systems, reformatting tables, reconciling two
copies of the same number and chasing people for inputs exist because the manual process needed them. They are
removed, not handed to code or AI.

### 5. Redesign the flow
The redesigned workflow changes its shape, not only its speed. A manual workflow has the form "a human produces the
output, then a human reviews it". A redesigned workflow has the form "the system produces the output, and the human
reviews the exceptions". Three changes follow.

- **Materiality thresholds are encoded.** The rules that decide what counts as an exception, and how exceptions are
  ranked, are written down as parameters rather than applied by eye.
- **Approval gates are moved.** Gates that existed to catch manual errors, such as a second person checking that
  figures were copied correctly, are replaced by controls in the system. Gates that exist for judgement stay.
- **The output changes.** A long pack is replaced by what the decision needs, for example a two-page exception summary
  with drill-down into the detail behind each item.

### 6. Build in controls
A redesigned workflow is only worth adopting if it can be relied on with fewer manual checks. The grounding check,
sign-off points, audit trail, threshold governance, parallel run, fallback and data handling that make this possible
are set out in [controls](04-controls.md).

### 7. Measure and reinvest
The redesign is measured against a baseline taken before it started, across capacity, speed, quality and influence,
and the freed time is directed to the use decided at the start. [Measuring value](05-measuring-value.md) sets out how.

## Worked example: a monthly risk and performance report
The example below runs one generic workflow through the method. The steps, hours and elapsed days are illustrative.

**Step 1, outcome.** *The risk committee knows, within five working days of month end, which funds have moved outside
their intended risk or performance profile, why, and what the risk function recommends.*

**Step 2, inventory.** The report covers every fund, takes around 60 hours a cycle across three people, and is used by
the risk committee at its monthly meeting. Two of its appendices are not referred to in any committee minutes; they are
dropped.

**Step 3, current-state map.**

| # | Step | Tag | Hours | Elapsed |
|---|---|---|---|---|
| 1 | Extract positions, returns and limits from several systems | Gather | 12 | 3 days |
| 2 | Reconcile and re-key into the reporting workbook | Gather | 10 | 2 days |
| 3 | Calculate measures and compare to limits | Compute | 8 | 1 day |
| 4 | Reformat tables and charts for the pack | Communicate | 6 | 1 day |
| 5 | Write commentary on what changed for each fund | Interpret | 14 | 3 days |
| 6 | Second person checks figures against source | Approve / Wait | 4 | 3 days |
| 7 | Head of risk reviews and decides what to escalate | Judge | 3 | 2 days |
| 8 | Final sign-off and distribution | Approve / Wait | 3 | 2 days |

The cycle takes around 60 hours and 17 working days. Steps 1, 2, 6 and 8 account for half the hours and most of the
elapsed time; none of them requires risk expertise.

**Step 4, owners.** Steps 1 and 3 move to code, which reads from source systems and computes the measures. Step 2
exists only because data was copied by hand and is eliminated. Step 4 is eliminated because code produces the output
in its final format. Step 5 becomes an AI draft from the computed facts, edited by the risk manager. Step 6 is replaced
by the grounding check and the system's reconciliation to source. Steps 7 and 8 stay with the risk manager and the head
of risk.

**Step 5, redesigned flow.**

| # | Step | Owner | Hours | Elapsed |
|---|---|---|---|---|
| 1 | Load data, compute measures, compare to thresholds, rank exceptions | Code | 0 | Same day |
| 2 | Draft an explanation for each exception from the computed facts | AI | 0 | Same day |
| 3 | Grounding check on every draft | Code | 0 | Same day |
| 4 | Review exceptions, edit explanations, decide what to escalate | Risk manager | 6 | 2 days |
| 5 | Sign off the two-page summary with drill-down | Head of risk | 1 | 1 day |

The cycle falls to around 7 hours and 3 working days. The output is now a ranked exception summary rather than a pack
covering every fund at equal length, and the committee sees it around three weeks earlier.

**Steps 6 and 7.** The redesigned report runs in parallel with the old one for at least one full cycle before the old
one is stopped, and the freed hours go to the use the risk function chose at the start, for example monthly
deep-dive reviews of the funds that appear most often in the exception summary.

## Common failure modes

| Failure mode | What happens | What prevents it |
|---|---|---|
| Automating outputs nobody uses | Cost falls, value does not rise | The inventory in step 2 |
| Letting the AI calculate | Wrong figures reach decisions | Code computes; the grounding check |
| Keeping every old review gate | Elapsed time barely changes | Moving gates in step 5 |
| No decision on freed time | Savings disappear into other work | A reinvestment plan before starting |
| A tool rollout with no workflow rebuilt | Usage rises, returns do not | Redesign one workflow fully first |

The last failure mode is the most common. Giving everyone a tool spreads small savings thinly across many tasks and
rebuilds nothing. Redesigning one workflow fully, measuring the result and then moving to the next produces a return
that can be shown.
