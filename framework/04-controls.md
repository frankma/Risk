# Controls

Controls are what make a redesigned workflow safe enough to remove the manual checks it replaces. This chapter sets out
the controls every redesigned risk workflow should have, from the grounding check on generated text to fallback when a
component fails, and how they align with supervisory expectations for AI risk management. It closes with why the risk
function should own them.

## Why controls come first
A redesign removes steps that existed to catch errors: a second person checking figures, a manager reading every page.
Those steps can only be removed if something at least as reliable takes their place. Without that, either the old
checks stay and the redesign saves little, or they are removed and errors reach decisions. The controls below are what
make the [redesign method](03-redesign-method.md) work in practice, and they should be designed in step 6, not added
after the workflow is live.

| Control | What it protects against |
|---|---|
| Grounding check | A wrong number in generated text |
| Sign-off points | An output reaching its audience without accountable review |
| Audit trail | Being unable to show what was produced, changed and approved |
| Governed thresholds | Silent changes to what counts as material |
| Parallel run | Switching to a workflow that disagrees with the one it replaces |
| Fallback | A failed component stopping the workflow |
| Data handling | Sensitive data reaching a service it should not |

## The grounding check
The grounding check enforces the principle that
[the AI never produces a number](01-principles.md#3-the-ai-never-produces-a-number). Every number in a piece of
generated text is extracted and matched against the computed facts the text was generated from. Numbers written as
words, such as "three months", are extracted and matched in the same way as numerals.

The match allows for formatting but not for substance. A computed value of 0.0473 matches "4.7%" and "4.73%"; a
computed value of 12,450,000 matches "12.45 million" and "12.5m"; a value expressed in basis points matches the same
value expressed as a percentage. It does not match a figure that cannot be traced to a computed value, a figure rounded
beyond the stated precision, or a figure attached to the wrong fund or measure where the check can tell. (The values are
illustrative.)

Text with an unmatched number is rejected before anyone sees it. The system then regenerates it, with the failure noted,
up to a set number of attempts; if it still fails, the item falls back to the template text described under fallback,
which states the computed facts in fixed sentences, and is flagged to the risk manager. The rejection, the attempts and
the outcome are all recorded in the audit trail. A grounding check that warns rather than rejects is not a control.

The check is limited to numbers. It does not test whether the text's reasoning is sound or whether its emphasis is
right; that remains the risk manager's judgement at the sign-off point.

## Sign-off points
Each redesigned workflow names the points at which a human must approve before an output moves on, and what exactly
they are approving. A sign-off is a statement about content, not a click to release a document.

| Sign-off | Who | What they are approving |
|---|---|---|
| Exception review | Risk manager | Which items are material, and that each explanation is fair |
| Escalation | Head of risk or delegate | That escalated items, and recommended actions, are right |
| Release | Owner of the output | That the output may go to its audience |

The risk manager sees the computed facts alongside the generated text, so that the review is of the content and not of
the arithmetic, which the system has already checked.

## The audit trail
For every output, the workflow records: the input facts it was generated from, with their data versions; the
threshold, prompt, template and model versions in force; the text as generated; every edit the human made; the
grounding check result; who approved it and when. The record is kept in a form that can be retrieved by output, by fund
and by date.

The trail serves three purposes. It allows any figure or sentence in a released output to be traced back to its source.
It shows how often humans change generated text and in what way, which is evidence of whether the AI step is working.
It supports review by internal audit and by supervisors.

## Materiality thresholds as governed parameters
The thresholds that decide what counts as an exception, and the rules that rank exceptions, determine what the risk
manager sees and what they do not. They encode the risk function's judgement and should be governed like any other
risk parameter.

- **Ownership.** Each threshold has a named owner in the risk function.
- **Review.** Thresholds are reviewed on a set cycle, and when the exception queue shows signs of being set too tight
  (too many items to review properly) or too loose (issues found outside the queue).
- **Change record.** Every change records the old and new values, the reason, who approved it and when it took effect.
  Thresholds are versioned, so that any past output can be reproduced with the thresholds in force at the time.

## Parallel runs
A redesigned workflow runs alongside the existing process for at least one full cycle before the old process is
stopped. For a monthly workflow that means at least one month end; for a daily workflow, enough days to include a
period of market stress or an unusual event, where possible.

Agreement criteria are set before the run starts. Typical criteria: every computed figure agrees with the existing
process within a stated tolerance, or the difference is explained; every exception the old process escalated also
appears in the new queue; and the risk manager judges the new explanations at least as useful as the old commentary.
Differences are investigated, not averaged away. A difference often shows an error in the old process, which is
recorded as a result of the run.

## Fallback
Each workflow defines what happens when a component fails.

- **Data pipeline failure.** The workflow does not run on stale or partial data without saying so. It either waits, or
  runs with the affected funds clearly marked, according to a rule set in advance.
- **AI backend failure.** The workflow falls back to a deterministic template that states the computed facts in fixed
  sentences. The output is plainer, but complete and correct, and the workflow's deadlines still hold.

Because the template backend produces correct output without an AI service, the workflow can always run. The same
template covers a draft that repeatedly fails the grounding check, and the reference implementations use it for
testing and demonstration.

## Data handling
A risk function sends data to an AI service only under rules set before the workflow is built.

- **What may be sent.** The workflow defines which data may go to which service. Computed facts about a fund are often
  enough; raw positions, investor details and personal data are sent only where the service is approved for them.
- **Confidentiality.** Investor and portfolio information is confidential. The terms of any external service should
  prevent the data being retained or used to train models, and this should be verified, not assumed.
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
| Board and senior management oversight | Regular reporting of AI use, results and incidents |

The risk function owns the testing of its own AI steps, through the grounding check, parallel runs and ongoing
monitoring above, as part of the limits of its own measures and tools that it is responsible for. Independent
validation of models sits with a separate function, as set out in [investment risk](02-investment-risk.md). A firm
should map these expectations to the specific requirements that apply to it.

## Why risk should own the controls
The controls in this chapter are what allow manual checks to be removed with confidence. A risk function that designs
and owns them decides how safe is safe enough, and can then remove its own manual checks on that basis. That makes
risk the function that enables redesign across the firm, rather than the one that blocks it. A risk function that
leaves the controls to others will find that each redesign waits for its approval and that the checks it trusts are
the ones it cannot remove.
