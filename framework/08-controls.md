# Controls

## The essentials
**The rule:** a redesign removes steps that existed to catch errors, such as a second person checking figures. Those
steps can be removed only if something at least as reliable takes their place. The controls below are designed in step 6
of the [redesign method](07-redesign-method.md), not added after the workflow is live.

| Control | What it protects against |
|---|---|
| Grounding check | A wrong number, an unsupported cause, or a quantifier or severity the facts do not bear, in generated text |
| AI permissions | The AI reading, running or doing something the risk function did not delegate |
| Automated actions | An action taken without sign-off that a rule did not decide, or that cannot be undone |
| Input handling | Text the AI reads steering what it does |
| Sign-off points | An output reaching its audience without accountable review |
| Audit trail | Being unable to show what was produced, changed and approved |
| Evaluation | An AI step that has stopped working, or a review that has stopped reading |
| Governed thresholds | Silent changes to what counts as material |
| Parallel run | Switching to a workflow that disagrees with the one it replaces |
| Fallback | A failed component stopping the workflow |
| Incidents | An error repeating, or an output already sent left uncorrected |
| Data handling | Sensitive data reaching a service it should not |

**Who owns them:** the risk function designs and owns the controls, under independent validation, and can then remove
its own manual checks on that basis.

The rest of this chapter is the detail behind these points.

## The grounding check
The grounding check enforces the principle that [the AI never fabricates a
number](05-principles.md#3-the-ai-never-fabricates-a-number). Every number in a piece of generated text is extracted and
traced to the computed facts behind it: the facts from the daily run that the text was generated from, and the results
of any analysis the AI ran through the analytics engine, each recorded as a run. Numbers written as words, such as
"three months", are extracted and traced in the same way as numerals.

A number in generated text is grounded if it is one of the computed facts, the result of a recorded analysis run, or the
result of a simple operation on them that the AI states and the check can recompute: a sum, a difference, a percentage
change, a ratio or a simple multiple, including words such as "doubled" or "a third". A number the check cannot
recompute from the facts is rejected like any unmatched number. Figures read from documents, such as the limits in a
portfolio's mandate terms, follow the same rule: each must appear, as numerals or as words, in the source passage it is
linked to, and the risk manager confirms it before it is used. A figure from an exploratory query is rejected in any
text bound for an output.

**Derivations are stated, not searched for.** For each derived number the AI states which facts it used and which
operation, and the check verifies that derivation only, one operation deep. It does not search the facts for any
combination that reproduces the number, because in a long table of facts some combination will, by chance.

**Each sentence is linked to its facts.** The AI marks every sentence with the facts it rests on. A sentence that states
something about a portfolio and links to no fact is rejected, and the link tells the check which portfolio and measure
each number belongs to, so a figure attached to the wrong one fails.

**A sentence that cites the record or a document** links to its passage, which is shown beside it. The check confirms
that the passage exists and that any figure taken from it appears there; the reading stays with the reviewer.

**Direction and comparison are checked.** Words of direction and comparison, such as "rose", "fell", "above", "below",
"within" and "breached", are tested against the linked facts. With a limit of 2.00%, "VaR fell from 1.84% to 2.31%,
within its limit" fails twice, though every number in it is a computed fact. (The values are illustrative.)

**Causes are computed, not asserted.** A sentence may say that one thing drove or caused another only where an
attribution or decomposition computed that link and the sentence is linked to it. "The rise came from the technology
basket" passes when the decomposition shows it; "the outflows came from the underperformance" fails, because no
analysis computes it.

**Quantifiers and severity follow the facts.** Words of proportion, such as "most", "half" and "nearly all", are tested
against the share they describe, under bands held as a governed parameter: "most" means more than half. Words of
severity, such as "urgent", "serious" and "minor", follow the computed state of the item, exception, watch item or
within, from a fixed vocabulary for each state, so the tone of a draft cannot understate or overstate it.

The match allows for formatting but not for substance. A computed value of 0.0473 matches "4.7%" and "4.73%"; a computed
value of 12,460,000 matches "12.46 million" and "12.5m"; a value expressed in basis points matches the same value
expressed as a percentage. It does not match a figure that cannot be traced to a computed value, a figure rounded beyond
the stated precision, or a figure attached to the wrong portfolio or measure. (The values are illustrative.)

Text that fails any part of the check is rejected before anyone sees it. The system then regenerates it, with the
failure noted, up to a set number of attempts; if it still fails, the item falls back to the template text described
under fallback, which states the computed facts in fixed sentences, and is flagged to the risk manager. The rejection,
the attempts and the outcome are all recorded in the audit trail. A grounding check that warns rather than rejects is
not a control.

The check runs on every piece of generated text in a workflow. The step tables show it once, after the first draft; a
later draft, such as a message, a decision note, minutes or a decision paper, passes the same check before anyone sees
it.

The check covers numbers, the direction of a change, comparisons with a limit or threshold, causes, quantifiers and
severity. It does not test what was left out, whether the reasoning is sound or whether the emphasis is right; those
remain the risk manager's judgement at the sign-off point, and [evaluation](08-controls.md#evaluation) tests how well
that judgement is exercised.

## AI permissions
The AI works under a permission that the risk function sets and records: the data it may read, the analyses it may run
and the actions it may never take, as set out in [working with AI](06-working-with-ai.md#what-the-ai-may-do). The engine
enforces it. An analysis outside the governed list does not run. The one thing the AI may run outside the list is a
read-only exploratory query, whose result is labelled unvalidated, kept out of outputs, shown only within the risk
function and never used for a limit. The AI has no write access to data or to governed parameters, and nothing it
produces leaves the function without a sign-off, except the [automated actions](08-controls.md#automated-actions) a
governed rule allows. Publishing an item to readers of the [shared
record](05-principles.md#7-hand-over-judgement-not-documents) outside the risk function counts as leaving it. Every run
the AI starts is recorded with its parameters, the person who asked and the result, so that any answer can be
reproduced.

**Every run uses the entitlements of the person who asked.** In Prepare, that is the risk function, for the portfolios
in its queue. A portfolio manager who asks a question, or runs a what-if before a trade, sees figures only for the
portfolios they manage, and an aggregation across portfolios returns only the firm-level totals the risk function
publishes. The analytics engine enforces the entitlement, not the AI.

**An output takes the entitlements of its audience.** A figure or a precedent from another portfolio stays within the
risk function unless it is a firm-level total the risk function publishes, and the analytics engine blocks a release
that carries one. The shared record works the same way: each reader sees the items for the portfolios they are
entitled to, and the firm-level totals the risk function publishes.

## Automated actions
An action may be taken without a person's sign-off beforehand only if it passes four tests. The rule that allows it is a
governed parameter, the head of risk approves that an action has passed the tests, and the risk manager reviews each
action the same day.

- **Decided by a rule.** The analytics engine decides from computed facts whether the action applies. The AI only
  writes its text, which passes the grounding check.
- **Standard.** The output follows a fixed template, and the rule sets its audience.
- **Reversible.** A notice can be corrected and a closed breach reopened the same day, with no loss to a client.
- **Proven.** The action ran under sign-off for a set period, the risk manager changed no more than a set share of its
  outputs, and the seeded tests of its review were caught at the set rate over that period.

Two actions pass. A routine breach notice goes out where the engine finds that the breach meets the rule's conditions,
such as a passive breach of an internal limit. A breach is closed where the engine matches it to a recorded data break.

**When the same-day review disagrees,** the risk manager corrects or recalls the notice and tells its recipients, or
reopens the breach, which re-enters the lifecycle at the stage it skipped. The error is recorded as an
[incident](08-controls.md#incidents), and the head of risk decides whether to suspend the rule while it is investigated.
An action that fails a test returns to sign-off until it passes again and the head of risk approves its return.

## Input handling
Text the AI reads is data, never instructions. Governing documents, notices and minutes come only from the risk
function's [documents domain](03-risk-data.md#what-the-analytics-engine-reads), kept as received with their source, and
a portfolio manager's explanation is recorded as text from a named person, or in the risk manager's notes of a review.
Nothing in them changes what the AI may do: its tools are the governed analyses, the exploratory query, the extractions
and retrieval from the record set out in [working with AI](06-working-with-ai.md#what-the-ai-reads). A passage that
reads as an instruction to the AI is flagged to the risk manager and not followed, and text a portfolio manager supplies
is evidence to test, never a fact the AI may state as true.

## Sign-off points
Each redesigned workflow names the points at which a human must approve before an output moves on or, for a routine
action under a governed rule, review it the same day, and what exactly they are approving. A sign-off is a statement
about content, not a click to release a document.

| Sign-off | Who | What they are approving |
|---|---|---|
| Exception review | Risk manager | Which items are material, and that each explanation is fair |
| Escalation | Head of risk or delegate | That what is escalated, and any action the risk manager recommends, is right |
| Release | Owner of the output | That the output may go to its audience, or an item be published in the shared record beyond the risk function |
| Same-day review | Risk manager | That each notice the AI sent, and each breach it closed, under a governed rule was right |
| Confirmation of an extraction | Risk manager | That each term, event or recorded decision says what its passage says, and that every expected term is found or resolved |

The risk manager sees the computed facts alongside the generated text, so that the review is of the content and not of
the arithmetic, which the system has already checked.

**Every output says what drafted it.** An output the AI drafted states so beside the name of the person who signed it
off; an action under a governed rule names the rule.

## The audit trail
For every output, the workflow records: the input facts it was generated from, with their data
[versions](03-risk-data.md#versioned-as-known); the analysis runs behind it, with their parameters; the threshold,
prompt, template and model versions in force; the text as generated; every edit the human made; the grounding check
result; who approved it and when or, for an action under a governed rule, the rule applied and who reviewed it. The
record is kept in a form that can be retrieved by output, by portfolio and by date. For every extraction it records the
document and passage, the value extracted, any expected term not found and who confirmed it, or that the risk manager
entered it by hand.

The trail serves three purposes. It allows any figure or sentence in a released output to be traced back to its source.
It shows how often humans change generated text and in what way, which is evidence of whether the AI step is working. It
supports review by internal audit and by supervisors.

## Evaluation
Each AI step has an **evaluation set**: past cases with reference outcomes, built by the risk function from its own
record and reviewed by independent validation. For a draft, the reference is the facts it must state and the claims it
must not make; for an extraction, the terms each document holds; for an investigation, the follow-up analyses each case
should run, and for a person's question the analyses that answer it. The set is rerun before first use and at every
change of model, prompt or template, and a change goes live only when the results meet criteria set in advance.

**Review is tested too.** Edit rates fall when drafts improve, and also when reviewers stop reading. On a set cycle, a
few drafts with a known flaw, such as a wrong driver or a missing fact, are sent through review, and the share caught is
recorded. A seeded draft is inserted after the grounding check, marked in the audit trail and withdrawn before release
whatever the review decides. A seeded flaw that passes is a finding about the review, not only about the reviewer.

**The AI is tested against its template.** On a sample, the risk manager compares the AI's draft with the template text
for the same item without knowing which is which. A step whose drafts are not judged better than the template is
replaced by it.

## Materiality thresholds as governed parameters
The thresholds that decide what counts as an exception, and the rules that rank exceptions, determine what the risk
manager sees and what they do not. They encode the risk function's judgement and should be governed like any other risk
parameter.

- **Ownership.** Each threshold is owned by the risk function, which sets it, reviews it and records every change.
- **Review.** Thresholds are reviewed on a set cycle, and when the exception queue shows signs of being set too tight
  (too many items to review properly) or too loose (issues found outside the queue).
- **Change record.** Every change records the old and new values, the reason, who approved it and when it took effect.
  Thresholds are versioned, so that any past output can be reproduced with the thresholds in force at the time.

Internal limits are governed in the same way. [Limits and escalation](04-limits-and-escalation.md) sets out where limits
come from, how internal limits are calibrated and how a breach is handled.

## Parallel runs
A redesigned workflow runs alongside the existing process for at least one full cycle before the old process is stopped.
For a monthly workflow that means at least one month end; for a daily workflow, enough days to include a period of
market stress or an unusual event, where possible.

Agreement criteria are set before the run starts. Typical criteria: every computed figure agrees with the existing
process within a stated tolerance, or the difference is explained; every exception the old process escalated also
appears in the new queue; and the risk manager judges the new explanations at least as useful as the old commentary.
Differences are investigated, not averaged away. A difference often shows an error in the old process, which is recorded
as a result of the run.

## Fallback
Each workflow defines what happens when a component fails.

- **Data pipeline failure.** The run follows the rule set in advance in [risk
  data](03-risk-data.md#quality-before-computation): it waits, or runs with the affected portfolios marked.
- **AI backend failure.** The fallback depends on the kind of step. A drafting step falls back to a deterministic
  template that states the computed facts in fixed sentences, including what the analyses set for the item's rule
  found. The output is plainer, but complete and correct. The AI's follow-up analyses do not run, and the item says
  so. An extraction step falls to the risk manager, who reads the document and enters the record, linked to its
  passage and marked as entered by hand. The check against the expected terms still runs, and a document unread past
  a set time ranks in the queue.

Every step has a path that needs no AI service, so a workflow can always run.

## Incidents
An **incident** is an output that reached its audience wrong, an automated action the same-day review overturned, or a
control that failed. Each is recorded with what went wrong, who received the output and how it was corrected; recipients
of a wrong output are told and sent the correction. The head of risk can suspend any AI step or governed rule at once: a
suspended step falls back as [fallback](08-controls.md#fallback) sets out, and a suspended rule returns its actions to
sign-off. A step returns to service once its evaluation set passes again.

## Data handling
A risk function sends data to an AI service only under rules set before the workflow is built. The data the analytics
engine itself reads, and the checks it passes, are set out in [risk data](03-risk-data.md).

- **What may be sent.** The workflow defines which data may go to which service. Computed facts about a portfolio are
  often enough for a draft. Raw positions, investor details and personal data are sent only where the service is
  approved for them, and that includes the documents and the record the AI reads: a dealing notice, a set of minutes or
  a risk manager's notes can name investors and people.
- **Retention.** The terms of any external service prevent the data being retained or used to train models, and this is
  verified, not assumed.
- **Vendor and third-party risk.** An external AI service is a third party and is assessed as one: its security, its
  resilience, where it processes data, and what happens if it changes or withdraws its service.

## Alignment with supervisory expectations
Supervisors' expectations for AI risk management share a common shape. The controls in this chapter map onto it.
Statistical and machine-learning models in the analytics engine are inventoried and validated as models, and count
towards these expectations where a supervisor's definition of AI covers them.

| Expectation | How a redesigned workflow meets it |
|---|---|
| An inventory of AI use | Each workflow records where AI is used and for what |
| Risk materiality assessment | Each AI step is rated by the impact of an error |
| Testing before deployment | Parallel runs with agreement criteria; an evaluation set for each AI step |
| Ongoing monitoring | Grounding check results, edit rates, seeded review tests and evaluation reruns over time |
| Human oversight | Named sign-off points with defined content |
| Change management | Versioned thresholds, prompts and templates, with change records |
| Independent review | Independent validation of each AI step and of the grounding check; internal audit's tests of the controls |
| Board and senior management oversight | Regular reporting of AI use, results, incidents and suspensions |

The risk function tests its own AI steps day to day, through the grounding check, parallel runs and ongoing monitoring
above, as part of the limits of its own measures and tools that it is responsible for. It is not the only judge of them.
The independent validation function, which sits outside the risk function as set out in [investment
risk](01-investment-risk.md), reviews each AI step and the grounding check at first use and at each material change: a
new model, a changed prompt or template, a new analysis on the governed list or a change to the check itself. Internal
audit tests that the controls operate as described, from the audit trail, the sign-offs and the change records. A firm
should map these expectations to the specific requirements that apply to it.

## Sources
- International Organization of Securities Commissions (2021). *The Use of Artificial Intelligence and Machine Learning
  by Market Intermediaries and Asset Managers.* Final report. Supervisory expectations for governance, testing,
  monitoring and oversight of AI in asset management.
- National Institute of Standards and Technology (2023). *Artificial Intelligence Risk Management Framework (AI RMF
  1.0).* The common shape of AI risk management: govern, map, measure and manage.
- National Institute of Standards and Technology (2024). *Artificial Intelligence Risk Management Framework: Generative
  Artificial Intelligence Profile* (NIST AI 600-1). Risks particular to language models, including confabulation, and
  the evaluation and incident practices that address them.
- OWASP Foundation (2024). *OWASP Top 10 for LLM Applications 2025.* Prompt injection through the text a model reads,
  and excessive agency in the actions it may take.
- ISO/IEC 42001:2023. *Information technology — Artificial intelligence — Management system.* Requirements for
  inventory, risk assessment, change management and oversight of AI systems.
