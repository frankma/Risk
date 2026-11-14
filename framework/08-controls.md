# Controls

## In short
**The rule:** a redesign removes steps that existed to catch errors, such as a second person checking figures. Those
steps can be removed only if something at least as reliable takes their place. The controls below are designed in step 6
of the [redesign method](07-redesign-method.md), not added after the workflow is live.

| Control | What it protects against |
|---|---|
| Grounding check | A wrong number in generated text |
| AI permissions | The AI reading, running or doing something the risk function did not delegate |
| Sign-off points | An output reaching its audience without accountable review |
| Audit trail | Being unable to show what was produced, changed and approved |
| Governed thresholds | Silent changes to what counts as material |
| Parallel run | Switching to a workflow that disagrees with the one it replaces |
| Fallback | A failed component stopping the workflow |
| Data handling | Sensitive data reaching a service it should not |

**Who owns them:** the risk function designs and owns the controls, under independent validation, and can then remove
its own manual checks on that basis.

The rest of this chapter is the detail behind these points.

## The grounding check
The grounding check enforces the principle that [the AI never fabricates a
number](05-principles.md#3-the-ai-never-fabricates-a-number). Every number in a piece of generated text is extracted and
traced to the computed facts behind it: the facts from the daily run that the text was generated from, and the results
of any analysis the AI ran through the risk engine, each recorded as a run. Numbers written as words, such as "three
months", are extracted and traced in the same way as numerals.

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

**Direction and comparison are checked.** Words of direction and comparison, such as "rose", "fell", "above", "below",
"within" and "breached", are tested against the linked facts. With a limit of 2.00%, "VaR fell from 1.84% to 2.31%,
within its limit" fails twice, though every number in it is a computed fact. (The values are illustrative.)

The match allows for formatting but not for substance. A computed value of 0.0473 matches "4.7%" and "4.73%"; a computed
value of 12,450,000 matches "12.45 million" and "12.5m"; a value expressed in basis points matches the same value
expressed as a percentage. It does not match a figure that cannot be traced to a computed value, a figure rounded beyond
the stated precision, or a figure attached to the wrong portfolio or measure. (The values are illustrative.)

Text that fails any part of the check is rejected before anyone sees it. The system then regenerates it, with the
failure noted, up to a set number of attempts; if it still fails, the item falls back to the template text described
under fallback, which states the computed facts in fixed sentences, and is flagged to the risk manager. The rejection,
the attempts and the outcome are all recorded in the audit trail. A grounding check that warns rather than rejects is
not a control.

The check covers numbers, the direction of a change and comparisons with a limit or threshold. It does not test a stated
cause, what was left out, whether the reasoning is sound or whether the emphasis is right; those remain the risk
manager's judgement at the sign-off point.

## AI permissions
The AI works under a permission that the risk function sets and records: the data it may read, the analyses it may run
and the actions it may never take, as set out in [working with AI](06-working-with-ai.md#what-the-ai-may-do). The risk
engine enforces it. An analysis outside the governed list does not run. The one thing the AI may run outside the list is
a read-only exploratory query, whose result is labelled unvalidated and kept out of outputs. The AI has no write access
to data or to governed parameters, and nothing it produces leaves the function without a sign-off. Every run the AI
starts is recorded with its parameters, the person who asked and the result, so that any answer can be reproduced.

## Sign-off points
Each redesigned workflow names the points at which a human must approve before an output moves on, and what exactly they
are approving. A sign-off is a statement about content, not a click to release a document.

| Sign-off | Who | What they are approving |
|---|---|---|
| Exception review | Risk manager | Which items are material, and that each explanation is fair |
| Escalation | Head of risk or delegate | That what is escalated, and any action the risk manager recommends, is right |
| Release | Owner of the output | That the output may go to its audience |

The risk manager sees the computed facts alongside the generated text, so that the review is of the content and not of
the arithmetic, which the system has already checked.

## The audit trail
For every output, the workflow records: the input facts it was generated from, with their data
[versions](03-risk-data.md#versioned-as-known); the analysis runs behind it, with their parameters; the threshold,
prompt, template and model versions in force; the text as generated; every edit the human made; the grounding check
result; who approved it and when. The record is kept in a form that can be retrieved by output, by portfolio and by
date.

The trail serves three purposes. It allows any figure or sentence in a released output to be traced back to its source.
It shows how often humans change generated text and in what way, which is evidence of whether the AI step is working. It
supports review by internal audit and by supervisors.

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
- **AI backend failure.** The workflow falls back to a deterministic template that states the computed facts in fixed
  sentences. The output is plainer, but complete and correct, and the workflow's deadlines still hold.

Because the template backend produces correct output without an AI service, the workflow can always run.

## Data handling
A risk function sends data to an AI service only under rules set before the workflow is built. The data the risk engine
itself reads, and the checks it passes, are set out in [risk data](03-risk-data.md).

- **What may be sent.** The workflow defines which data may go to which service. Computed facts about a portfolio are
  often enough; raw positions, investor details and personal data are sent only where the service is approved for them.
- **Retention.** The terms of any external service prevent the data being retained or used to train models, and this is
  verified, not assumed.
- **Vendor and third-party risk.** An external AI service is a third party and is assessed as one: its security, its
  resilience, where it processes data, and what happens if it changes or withdraws its service.

## Alignment with supervisory expectations
Supervisors' expectations for AI risk management share a common shape. The controls in this chapter map onto it.

| Expectation | How a redesigned workflow meets it |
|---|---|
| An inventory of AI use | Each workflow records where AI is used and for what |
| Risk materiality assessment | Each AI step is rated by the impact of an error |
| Testing before deployment | Parallel runs with agreement criteria |
| Ongoing monitoring | Grounding check results and human edit rates over time |
| Human oversight | Named sign-off points with defined content |
| Change management | Versioned thresholds, prompts and templates, with change records |
| Independent review | Independent validation of each AI step and of the grounding check; internal audit's tests of the controls |
| Board and senior management oversight | Regular reporting of AI use, results and incidents |

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
- ISO/IEC 42001:2023. *Information technology — Artificial intelligence — Management system.* Requirements for
  inventory, risk assessment, change management and oversight of AI systems.
