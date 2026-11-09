# Performance risk

Performance risk asks whether a portfolio is delivering what was promised, in the way it was promised. This chapter
applies the [redesign method](../framework/05-redesign-method.md) to the pillar: it lists the pillar's recurring
workflows, redesigns the periodic portfolio manager review so that it runs on the risk function's agenda with an
evidence-based challenge pack, and sets out the thresholds, limits, controls and measures that make the redesign work.
The shift is from receiving the portfolio manager's account of performance to challenging it with independent evidence.

## The outcome
The pillar's outcome, as defined in [investment risk](../framework/01-investment-risk.md#performance-risk):

> The risk manager can show, with evidence, whether each portfolio is meeting its objective and whether its returns come
> from the sources its mandate describes.

The second half of the sentence matters as much as the first. A portfolio that beats its benchmark through an exposure
its mandate does not describe is not delivering what was promised, and the success may not last. The pillar tests both
the outcome and the way it was achieved. It reads what has happened: realised outcomes, and whether holdings match the
promised style. What could happen next, including ex-ante tracking error and the risk budget, belongs to [market
risk](market-risk.md).

## Workflows in this pillar

| Workflow | Cadence | Output | Used by | For which decision |
|---|---|---|---|---|
| Portfolio manager review | Quarterly | Challenge pack, minutes, actions | Risk manager | What must be explained |
| Attribution reporting | Monthly | Return by source | Risk manager | Whether returns come from intended sources |
| Realised risk and drawdown | Daily | Ex-post tracking error; drawdown, absolute and relative | Risk manager | Whether the portfolio runs beyond its promise |
| Peer comparison | Monthly | Position against peers | Investment oversight | Whether the outcome is competitive |
| Style and mandate consistency | Daily | Exposures against mandate terms | Risk manager | Whether the portfolio drifts |
| Watch list management | Monthly | Portfolios under watch, with actions | Investment oversight | Whether to escalate |

The portfolio manager review is the flagship, because it is where the pillar's evidence meets the person who can act on
it. The other workflows feed it: attribution, realised risk, peer comparison and consistency checks supply the evidence,
and market risk's risk budget review adds its exceptions. Attribution separates the two [sources of
return](../framework/02-sources-of-return.md), using the [alpha and beta method](alpha-and-beta-method.md). The watch
list holds the portfolios whose issues have not been resolved; it is a single list for the firm, owned by the risk
function, to which this pillar and the [integrated view](integrated-view.md) both add portfolios, and which investment
oversight uses to decide escalation.

**Ex-post tracking error** is the standard deviation of the portfolio's realised return relative to its benchmark over a
stated window. Its forecast counterpart, ex-ante tracking error, belongs to [market risk](market-risk.md), which
compares the two. **Realised drawdown** is the fall from the portfolio's peak value, measured in absolute terms and
relative to its benchmark; market risk reads the headroom it leaves before the drawdown tolerance. The risk budget
review is also market risk's, and its exceptions come into the challenge pack here.

Relative return and drawdown are computed every day over a rolling window, a governed parameter illustrated here as 12
months, so that a shortfall reaches watch as soon as it forms rather than at the end of a quarter. Persistence is still
counted in whole periods.

## Flagship redesign: the periodic portfolio manager review
The example below follows the review of one portfolio. **The steps, hours and elapsed times are illustrative.**

**Current state.** Before each review, the risk function prepares material; in the meeting, the portfolio manager
presents their own account of performance.

| # | Step | Tag | Hours | Elapsed |
|---|---|---|---|---|
| 1 | Pull attribution reports and performance data | Gather | 2 | 1 day |
| 2 | Build charts and tables for the meeting | Communicate | 3 | 2 days |
| 3 | Read the reports to find points to raise | Interpret | 2 | 1 day |
| 4 | Hold the meeting; the portfolio manager presents their account | Judge | 1.5 | 1 day |
| 5 | Write the minutes | Communicate | 2 | 3 days |
| 6 | Circulate the minutes for agreement | Approve / Wait | 0.5 | 5 days |
| 7 | Chase follow-up actions by email | Communicate | 1.5 | Ongoing |

Each review takes 12.5 hours, and 13 working days pass from the start of preparation to agreed minutes, followed by
open-ended chasing. The meeting runs on the portfolio manager's agenda, because the material describes performance
without pointing to the questions it raises. Follow-up is loose: actions live in minutes and emails, and nothing
escalates an action that has stalled.

**Owner assignment.**

- Step 1 moves to the risk engine, which tracks the pillar's measures continuously rather than pulling them before each
  review.
- Step 2 is eliminated, because the risk engine produces the pack in its final format.
- Step 3 is split. The risk engine tests the portfolio against its mandate terms and ranks the issues, which is
  computation; the AI drafts the evidence and the questions for each issue, which is interpretation.
- Step 4 stays with the risk manager, who now runs the meeting on the risk function's agenda.
- Step 5 becomes an AI draft of the minutes and the action log, edited by the risk manager.
- Step 6 stays as an approval, shortened because the risk manager edits a draft rather than writing from notes.
- Step 7 exists only because nothing tracked the actions, and is eliminated: the risk engine tracks follow-ups and
  escalates overdue actions to the watch list.

**Mandate terms, set up once.** Testing a portfolio against what it promised needs the promise in a form the risk engine
can test. The AI extracts the portfolio's stated objective, style and limits from its documents into structured terms,
each linked to the passage it came from. The risk manager confirms the terms once, and again whenever the documents
change. The risk engine then tests holdings and exposures against the confirmed terms and flags style drift and
unintended bets. The AI reads the documents, the risk engine makes the comparison, and the risk function owns what the
terms say once the risk manager has confirmed them.

**Redesigned flow.**

| # | Step | Owner | Hours | Elapsed |
|---|---|---|---|---|
| 1 | Track realised return, ex-post tracking error, drawdown, active share, information ratio, factors and peer position | Risk engine | 0 | Continuous |
| 2 | Test exposures against the mandate terms; flag drift and unintended bets | Risk engine | 0 | Continuous |
| 3 | Rank the portfolio's issues, with market risk's tracking error and risk budget exceptions | Risk engine | 0 | Minutes |
| 4 | Draft the challenge pack: evidence and questions for each issue | AI assistant | 0 | Minutes |
| 5 | Grounding check on the pack | Risk engine | 0 | Minutes |
| 6 | Review and edit the pack; set the agenda | Risk manager | 1.5 | 1 day |
| 7 | Run the meeting on the risk function's agenda | Risk manager | 1.5 | 1 day |
| 8 | Draft the minutes and the action log | AI assistant | 0 | Same day |
| 9 | Edit and agree the minutes and actions | Risk manager | 0.5 | 2 days |
| 10 | Track follow-ups; escalate overdue actions to the watch list | Risk engine | 0 | Ongoing |

Each review falls to 3.5 hours, and agreed minutes follow 4 working days after preparation starts instead of 13. The
meeting itself takes the same time as before; what changes is whose agenda it follows and what happens afterwards.

**The shift.** In the current state, the risk function receives the portfolio manager's account and asks what it can. In
the redesigned state, it arrives with the top issues for the portfolio, the evidence for each and the questions to ask,
prepared from data that is independent of the portfolio manager. The risk manager challenges; the portfolio manager
explains; and the actions agreed are tracked until they are closed.

## Materiality and exceptions
An **exception** in this pillar is a rule that has fired: a sign that the portfolio is not delivering its promise, or
not in the way it promised. A **watch item** is an early sign that has not yet persisted. Each rule is a [governed
parameter](../framework/06-controls.md#materiality-thresholds-as-governed-parameters). **The example values below are
illustrative and are not recommendations;** each risk function sets its own.

| Kind of rule | Example (illustrative) | What it catches |
|---|---|---|
| Relative return | Shortfall net of fees against benchmark or objective over the rolling window, beyond a set level | Missing the promise |
| Persistence | Shortfall in several consecutive periods | Shortfall that is not noise |
| Ex-post tracking error | Outside the range the mandate terms imply | Too much or too little active risk taken |
| Drawdown | Realised drawdown, absolute or relative, beyond its tolerance | Losses that end mandates |
| Active share | Falling for several consecutive quarters | A portfolio moving towards its benchmark |
| Source of return | A large share of gross excess return from unintended beta, over several periods | Returns from the wrong sources |
| Style consistency | Exposures outside the confirmed mandate terms | Style drift |
| Overdue action | An agreed action past its due date | Follow-up that has stalled |

A shortfall over the rolling window, or a single period of the source-of-return reading, is a watch item; every other
rule in the table, including persistent shortfall, gives an exception when it fires. The risk engine ranks issues for
each portfolio, exceptions before watch items. Persistent issues rank above single-period ones, because short periods
are noisy and persistence carries more information than size. Issues where the outcome and the way it was achieved both
depart from the promise rank highest. Overdue actions are always shown, so that the review starts from what was agreed
last time.

## What the AI drafts
The AI drafts each item of the challenge pack from the facts that the risk engine produced and from nothing else. Every
number in each draft appears in the facts beside it, so the [grounding
check](../framework/06-controls.md#the-grounding-check) would pass. The questions are proposals; the risk manager
decides which to ask. **The funds and figures are illustrative.**

**Outperformance from unintended beta.**

| Fact | Value |
|---|---|
| Fund | Fund G |
| Excess return over benchmark before fees, last 12 months | 2.1% |
| Split of the excess: unintended beta from currency / alpha | 1.6% / 0.5% |
| Currency in confirmed mandate terms | Not part of the stated strategy |
| Currency tilt on record | None |
| Average unhedged US dollar exposure | 14% of net assets |

> Fund G returned 2.1% above its benchmark before fees over the last 12 months. Of that, 1.6% was unintended beta from
> currency, which is not part of its stated strategy and has no tilt on record; alpha was 0.5%. The fund held an
> average of 14% of net assets in unhedged US dollar exposure. *Question: Is the currency exposure intended, and if so,
> how is it managed?*

**Active share falling while the fee is unchanged.**

| Fact | Value |
|---|---|
| Fund | Fund H |
| Active share, last four quarters | 71% / 64% / 58% / 52% |
| Consecutive quarters of decline | 3 |
| Management fee over the period | Unchanged |

> Fund H's active share has fallen for 3 consecutive quarters, from 71% to 52%, while its fee is unchanged. *Question:
> What has changed in how the portfolio is managed, and does its positioning still reflect an active mandate?*

**Returns inconsistent with the stated style.**

| Fact | Value |
|---|---|
| Fund | Fund J |
| Confirmed style | Large-company value |
| Value factor exposure, today / 12 months ago | -0.10 / +0.40 |
| Share of net assets in small companies, today / 12 months ago | 22% / 6% |

> Fund J's confirmed style is large-company value, but its value factor exposure has moved from +0.40 to -0.10 over 12
> months, and its holdings in small companies have risen from 6% to 22% of net assets. *Question: Is the portfolio still
> managed to its stated style, and if not, should its positioning or its documents change?*

## Limits of the measures
The risk function owns the model risk in its own performance measures; independent validation of the models sits
elsewhere, as set out in [investment risk](../framework/01-investment-risk.md#scope-and-boundaries).

| Measure | Where it is weak | How the function tests it |
|---|---|---|
| Attribution | Depends on the model and benchmark chosen | Comparing methods; reviewing benchmark fit |
| Relative return | Short periods are noisy | Persistence over several periods |
| Ex-post tracking error | Depends on the window; noisy over short ones | Several windows; comparison with ex-ante from market risk |
| Peer comparison | Peer groups can be poorly matched | Reviewing peer-group membership |
| Factor exposures | Depend on the baskets and the estimated betas | Comparing with a regression on portfolio returns |
| Extracted mandate terms | The AI can miss or misread a term | Confirmation by the risk manager |

Attribution answers the question it is set up to answer: a different model or benchmark can tell a different story, so
the function checks that its choices fit each portfolio. Short periods are noisy, so persistence matters more than any
single period, which is why the ranking rule weighs it heavily. Peer groups can be poorly matched, which makes a
portfolio look better or worse than it is. The extracted mandate terms are the AI step's main limit in this pillar: an
error there would make every later test wrong, which is why the terms are confirmed by the risk manager before they are
used.

## Controls specific to this pillar
The general controls in [controls](../framework/06-controls.md) apply in full. This pillar adds five.

- **Mandate terms are confirmed before use.** Extracted terms are not tested against until the risk manager confirms
  them, each term links to its source passage, and a change to the documents triggers re-extraction with the
  differences shown.
- **Evidence is independent.** The challenge pack is built from the risk function's own data, not from material the
  portfolio manager supplies.
- **Questions are chosen by the risk manager.** Drafted questions are proposals; the risk manager decides what to ask.
- **Watch list exits are decided.** A portfolio leaves the watch list only by a recorded decision, not because its
  actions were closed automatically, whichever workflow added it.
- **The split reconciles before drafting.** The lines of the [alpha and beta](alpha-and-beta-method.md) split
  must sum to the gross return, and alpha must show no exposure to a declared factor, within stated tolerances, before
  the AI drafts from them. A split that fails is an exception in its own right. A missing-factor flag goes to the risk
  manager.

## Measuring value
The measures from [measuring value](../framework/07-measuring-value.md) that matter most for this pillar are
influence measures, because the purpose of the review is to change what happens.

| Dimension | Measure for this pillar |
|---|---|
| Influence | Issues raised in reviews, and actions completed |
| Influence | Share of review time spent on the risk function's agenda |
| Speed | Working days from preparation to agreed minutes and actions |
| Quality | Drift or underperformance first identified outside the risk function |
| Capacity | Reviews held per quarter at full depth |
| Pillar-specific | Share of agreed actions closed by their due date; time on the watch list before an outcome |

In the flagship example, preparation and follow-up fall from 12.5 hours to 3.5 hours per review, and agreed minutes
follow in 4 working days instead of 13. The freed time is directed in advance, for example to reviewing portfolios more
often when they are on the watch list. (The figures are illustrative.)

## Connections
Performance risk signals often come first. Underperformance prompts redemptions, which is why [liquidity
risk](liquidity-risk.md) watches flows more closely in portfolios flagged here. Style drift and unintended bets change a
portfolio's exposures and can raise concentration and volatility in [market risk](market-risk.md), while that pillar's
ex-ante tracking error and risk budget exceptions feed the challenge pack here, and the drawdown measured here sets the
headroom it reads. The [integrated view](integrated-view.md) brings these signals together for each portfolio.

## Sources
- Grinold, R. and Kahn, R. (2000). *Active Portfolio Management*, 2nd edition. McGraw-Hill. Ex-post tracking error,
  the information ratio and persistence as evidence of skill.
- Brinson, G., Hood, L. and Beebower, G. (1986). Determinants of Portfolio Performance. *Financial Analysts Journal*.
  Attribution by decision into allocation and selection.
- Cremers, M. and Petajisto, A. (2009). How Active Is Your Fund Manager? A New Measure That Predicts Performance.
  *Review of Financial Studies*. Active share as a measure of how far holdings depart from the benchmark.
