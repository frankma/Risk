# Measuring value

A risk function earns no revenue, so the return on redesign has to be shown in other terms. This chapter sets out four
dimensions of value (capacity, speed, quality and influence), the baseline and reinvestment plan that make them
measurable, and why usage of AI tools is not a measure. It closes with an illustrative scorecard for one redesigned
workflow.

## What value means for a risk function
The [philosophy](00-philosophy.md) sets out a risk function's purpose: to show whether every portfolio takes the risks
its mandate intends, in the size it can bear, and is paid for them, and to challenge it where it does not. A redesign
creates value when it lets the function do more of that, do it sooner, do it more reliably, or have more effect on the
decisions it informs. Hours saved are a means to those ends, not the end itself: an hour saved and spent on nothing has
no value, and an hour saved and spent on challenging a portfolio manager may have a great deal.

This is why value is measured in four dimensions rather than one, and why the measurement starts before the redesign
does.

## Four dimensions

| Dimension | Question | Example measures |
|---|---|---|
| Capacity | How much can be covered in depth? | Portfolios covered in depth per person; deep-dive reviews per month |
| Speed | How quickly does the function know? | Data availability to signed-off output; alert to explanation |
| Quality | Does it catch what matters? | Issues missed or found late; errors found in review; parallel-run agreement |
| Influence | Does its work change decisions? | Issues raised and actions taken; share of time on challenge |

### Capacity
Capacity measures how much risk work the function can do at the depth it should be done. Portfolios covered in depth per
person captures breadth; deep-dive reviews per month captures depth. A redesign that lets each risk manager cover more
portfolios properly, or review the most important ones more often, raises capacity even if headcount and hours are
unchanged.

### Speed
Speed measures elapsed time, not effort. Time from data availability to signed-off output shows how soon a decision can
be made on a recurring output; time from alert to explanation shows how soon the function understands an unexpected
event. Elapsed time is usually dominated by gathering and waiting rather than by work, as the
[redesign method](04-redesign-method.md) shows, so speed is often where a redesign shows its largest change.

### Quality
Quality measures whether the function catches what matters and gets it right. Issues missed or detected late are the
most important measure and the hardest to collect; they are recorded as they come to light, for example from
post-event reviews. Errors found in review show how much rework the workflow creates. Parallel-run agreement, from the
[controls](05-controls.md) chapter, shows whether a redesigned workflow can be relied on before the old one is stopped.

### Influence
Influence measures whether the function's work changes what happens. Issues raised with portfolio managers, and the
actions taken in response, show whether challenge is being made and heard. The share of the risk manager's time spent
on challenge rather than on producing outputs shows whether the shift described in the
[principles](03-principles.md#what-the-risk-manager-adds) is happening. Influence is the dimension that most
directly reflects the purpose of the function, and the one most often left unmeasured.

## Baseline first
Every measure needs a starting point, and the starting point must be taken before anything changes. Once a workflow has
been redesigned, the old process can no longer be observed, and estimates made afterwards tend to flatter the result.

The simplest baseline is a time study of one typical cycle of the workflow: each step, who did it, the hours it took
and the elapsed time it added, recorded as the cycle runs. This is the same information as the current-state map in
step 3 of the redesign method, so the two are done together. The baseline also records the current values of the other
measures that apply, such as the number of portfolios reviewed in depth and the number of issues raised with portfolio
managers.

A baseline taken from one cycle is approximate. It is still far better than none, and it can be refined by observing a
second cycle where the workflow varies a lot from one cycle to the next.

## Reinvestment plan
Before a workflow is redesigned, the risk function decides what the freed time will be spent on, and records it. The
plan names the activity, the expected volume, and who will do it: for example, monthly deep-dive reviews of the
portfolios that appear most often in the exception queue, or a structured challenge session with each portfolio manager
every quarter.

After the redesign, the plan is tracked like any other commitment. If the freed time is not going where it was planned
to go, the reason is found and either the plan or the work is changed. Without a plan, freed time is absorbed by
existing work and the redesign shows a saving that no one can find.

## Why usage is not a measure
The number of people using an AI tool, or the number of prompts they send, is easy to count and says nothing about
value. High usage is consistent with a tool used for small tasks inside workflows that are otherwise unchanged, which
is the insertion pattern the [principles](03-principles.md) warn against. Low usage is consistent with a workflow that
has been redesigned so that AI runs inside it without anyone prompting it at all.

Usage can be a useful diagnostic, for example to see whether a new tool is being adopted, but it is not reported as a
measure of return.

## Illustrative scorecard
The scorecard below is for one redesigned workflow, the monthly risk and performance report from the worked example in
the [redesign method](04-redesign-method.md#worked-example-a-monthly-risk-and-performance-report). **All figures are
illustrative.**

| Dimension | Measure | Before | After |
|---|---|---|---|
| Effort | Hours per cycle | 60 | 7 |
| Capacity | Deep-dive portfolio reviews per month | 1 | 4 |
| Speed | Working days from month end to signed-off report | 17 | 3 |
| Speed | Days from a threshold breach to an explanation | 5 | 1 |
| Quality | Figure errors found in review per cycle | 6 | 0 |
| Quality | Parallel-run agreement on escalated items | n/a | 100% |
| Influence | Issues raised with portfolio managers per quarter | 8 | 20 |
| Influence | Share of risk manager time on challenge | 20% | 55% |

Effort is shown alongside the four dimensions because it is where the freed time comes from, while capacity is what
that time buys.

The scorecard reads as a whole. The hours saved (effort) are shown going into deep-dive reviews (capacity), which is the
reinvestment plan in action. The earlier report (speed) gives the committee time to act. Errors caught by the
grounding check and reconciliation, rather than by a reviewer, improve quality. More issues raised, and more time spent
on challenge, show the change in influence that the redesign was for.

## Sources
- Kaplan, R. and Norton, D. (1992). The Balanced Scorecard: Measures That Drive Performance. *Harvard Business
  Review*. Measuring a function on several dimensions read together, rather than on one.
