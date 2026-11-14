# Redesign method

## In short
**The rule:** a workflow is redesigned in seven steps, from the outcome it exists to deliver to measuring whether the
redesign delivers it. The [principles](05-principles.md) say what a redesign should achieve, and this method says how.

| Step | Question it answers |
|---|---|
| 1. Define the outcome | What is this workflow for? |
| 2. Inventory the workflows | What do we produce, for whom, and for which decision? |
| 3. Map the current state | What kind of work is each step? |
| 4. Assign each step an owner | Who or what should do each step? |
| 5. Redesign the flow | What does the workflow look like when built around those owners? |
| 6. Build in controls | What makes it safe to rely on? |
| 7. Measure the result | Does it work, and is the risk manager's time going where it was meant to? |

**What changes:** a manual workflow has the form "a human produces the output, then a human reviews it". A redesigned
workflow has the form "the system produces the output, and the human reviews the exceptions".

The rest of this chapter sets out each step, runs one generic workflow through all seven and lists the failure modes.

## The seven steps
### 1. Define the outcome
Each workflow is described by the outcome it delivers, in one sentence, not by the tasks it involves. "Produce the
monthly risk pack" is a task. "Ensure that the risk committee knows which portfolios have moved outside their intended
risk profile and why, in time to act" is an outcome. The outcome sentence is the test for every later step: a step that
does not serve it is a candidate for removal.

### 2. Inventory the workflows
The risk function lists its recurring workflows and records, for each one, its cadence, its inputs, its output, who uses
the output and for which decision. The inventory usually shows outputs that feed no decision: a report produced because
it has always been produced, or a table nobody reads. These are eliminated, not automated.

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

The map nearly always shows that much of the work is Gather and Approve / Wait, not the steps that require expertise.

### 4. Assign each step an owner
Each tagged step is assigned to one owner, following the core pattern.

| Tag | Owner |
|---|---|
| Gather, Compute | Risk engine |
| Interpret, Communicate | AI assistant, which drafts through the risk engine; the risk manager's edit and approval is a step of its own |
| Judge, Approve | The risk manager, or the head of risk for escalation and sign-off |
| Steps that exist only because the old process was slow | Eliminated |

The last row matters as much as the others. Re-keying figures between systems, reformatting tables, reconciling two
copies of the same number and chasing people for inputs exist because the manual process needed them. They are removed,
not handed to the risk engine or the AI assistant.

### 5. Redesign the flow
The redesigned workflow changes its shape, as the opening sets out. Three changes follow.

- **Materiality thresholds are encoded.** The rules that decide what counts as an exception, and how exceptions are
  ranked, are written down as parameters rather than applied by eye.
- **Approval gates are moved.** Gates that existed to catch manual errors, such as a second person checking that figures
  were copied correctly, are replaced by controls in the system. Gates that exist for judgement stay.
- **The output changes.** A long pack is replaced by what the decision needs, for example a two-page exception summary
  with drill-down into the detail behind each item.

### 6. Build in controls
The controls are designed in this step, not added after the workflow is live; [controls](08-controls.md) sets them out.

### 7. Measure the result
The redesigned workflow is measured against a baseline taken before it started, across capacity, speed, quality and
influence, and the risk manager's time is directed to the use decided at the start. [Measuring
value](09-measuring-value.md) sets out how.

## Worked example: a monthly risk and performance report
The example below runs one generic workflow through the method. The steps are illustrative.

**Step 1, outcome.** *The risk committee knows, within five working days of month end, which portfolios have moved
outside their intended risk or performance profile, why, and what the risk function recommends.*

**Step 2, inventory.** The report covers every portfolio, is produced by three people, and is used by the risk committee
at its monthly meeting. Two of its appendices are not referred to in any committee minutes; they are dropped.

**Step 3, current-state map.**

| # | Step | Tag |
|---|---|---|
| 1 | Extract positions, returns and limits from several systems | Gather |
| 2 | Reconcile and re-key into the reporting workbook | Gather |
| 3 | Calculate measures and compare to limits | Compute |
| 4 | Reformat tables and charts for the pack | Communicate |
| 5 | Write commentary on what changed for each portfolio | Interpret |
| 6 | Second person checks figures against source | Approve / Wait |
| 7 | Head of risk reviews and decides what to escalate | Judge |
| 8 | Final sign-off and distribution | Approve / Wait |

Steps 1, 2, 6 and 8 are gathering, checking and waiting; none of them requires risk expertise.

**Step 4, owners.** Steps 1 and 3 move to the risk engine, which reads from source systems and computes the measures.
Step 2 exists only because data was copied by hand and is eliminated. Step 4 is eliminated because the risk engine
produces the output in its final format. Step 5 becomes an AI draft from the computed facts, edited by the risk manager.
Step 6 is replaced by the grounding check and the system's reconciliation to source. Steps 7 and 8 stay with the head of
risk, who now decides on the risk manager's proposal.

**Step 5, redesigned flow.**

| # | Step | Owner |
|---|---|---|
| 1 | Load data, compute measures, compare to thresholds, rank exceptions | Risk engine |
| 2 | Draft an explanation for each exception from the computed facts | AI assistant |
| 3 | Grounding check on every draft | Risk engine |
| 4 | Review exceptions, edit explanations, propose what to escalate | Risk manager |
| 5 | Decide what to escalate; sign off the two-page summary with drill-down | Head of risk |

The output is now a ranked exception summary rather than a pack covering every portfolio at equal length, and the
committee sees it within days of month end.

**Steps 6 and 7.** The redesigned report runs in parallel with the old one for at least one full cycle before the old
one is stopped, and the risk managers' time goes to the use the risk function chose at the start, for example monthly
deep-dive reviews of the portfolios that appear most often in the exception summary.

## Common failure modes
| Failure mode | What happens | What prevents it |
|---|---|---|
| Automating outputs nobody uses | An unused output is produced faster | The inventory in step 2 |
| Letting the AI do the arithmetic | Wrong figures reach decisions | The risk engine computes every figure; the grounding check |
| Keeping every old review gate | The output arrives no sooner | Moving gates in step 5 |
| No decision on what the risk manager's time is for | The time is absorbed by existing work | A plan for that time before starting |
| A tool rollout with no workflow rebuilt | Usage rises, the work does not change | Redesign one workflow fully first |

## Sources
- Hammer, M. (1990). Reengineering Work: Don't Automate, Obliterate. *Harvard Business Review*. Redesigning a process
  around what technology makes possible, rather than speeding up the steps it already has.
