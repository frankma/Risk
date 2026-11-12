# Performance risk

Performance risk asks whether a portfolio is delivering what was promised, in the way it was promised. This chapter
applies the [redesign method](../framework/07-redesign-method.md) to the pillar: it lists the pillar's recurring
workflows, redesigns the periodic portfolio manager review so that it runs on the risk function's agenda with an
evidence-based challenge pack, and sets out the thresholds, limits, controls and measures that make the redesign work,
and the design choices behind the pillar's measures. The shift is from receiving the portfolio manager's account of
performance to challenging it with independent evidence.

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
return](../framework/02-sources-of-return.md), using the [alpha and beta method](alpha-and-beta-method.md), and shows
each beta line by the [return generator](../framework/02-sources-of-return.md#what-generates-return) that paid it:
market risk premia or style premia, with alpha read as skill. The generator tells the risk manager
[how the return could stop](../framework/02-sources-of-return.md#how-does-each-generator-fail), which sets the question
to put to the portfolio manager. The watch
list holds the portfolios whose issues have not been resolved; it is a single list for the firm, owned by the risk
function, to which this pillar and the [integrated view](integrated-view.md) both add portfolios, and which investment
oversight uses to decide escalation. An escalated portfolio goes to the risk committee, as
[limits and escalation](../framework/04-limits-and-escalation.md#escalation) sets out.

The review also uses the challenge mode set out in
[working with AI](../framework/06-working-with-ai.md#three-modes-of-working). When a portfolio manager explains an
issue, the AI tests the explanation against the risk function's data and reports what supports it and what contradicts
it. The risk manager weighs that evidence; the AI does not judge the explanation.

**Ex-post tracking error** is the standard deviation of the portfolio's realised return relative to its benchmark over a
stated window. Its forecast counterpart, ex-ante tracking error, belongs to [market risk](market-risk.md), which
compares the two. **Realised drawdown** is the fall from the portfolio's peak value, measured in absolute terms and
relative to its benchmark; market risk reads the headroom it leaves before the drawdown tolerance. The risk budget
review is also market risk's, and its exceptions come into the challenge pack here.

Relative return and drawdown are computed every day over a rolling window, a governed parameter illustrated here as 12
months, so that a shortfall reaches watch as soon as it forms rather than at the end of a quarter. Persistence is
counted in whole periods. The windows, and the significance shown beside each figure, are set out under
[design choices](performance-risk.md#windows-and-significance).

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
can test. The AI extracts the portfolio's stated objective, benchmark, style, limits and dealing terms from its
documents into structured terms, each linked to the passage it came from. The risk manager confirms the terms once, and
again whenever the documents change. The risk engine then tests holdings and exposures against the confirmed terms and
flags style drift and unintended bets. The AI reads the documents and the risk engine makes the comparison. For a hard
limit, compliance's coded rule is the master reading: the extracted limit is reconciled to it, and a difference is
routed to compliance, not settled by the risk manager. The risk function owns the objective and style terms, which
compliance does not code, once the risk manager has confirmed them. For a new portfolio, the terms are first extracted
and confirmed in the [new portfolio review](new-portfolio-review.md).

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
An **exception** in this pillar is a reading that has crossed a rule's threshold: a sign that the portfolio is not
delivering its promise, or not in the way it promised. A **watch item** is an early sign that has not yet persisted.
Each rule is a [governed
parameter](../framework/08-controls.md#materiality-thresholds-as-governed-parameters). **The example values below are
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

A shortfall over the rolling window, a shortfall on both the 1-month and 3-month windows, or a single period of the
source-of-return reading, is a watch item; every other rule in the table, including persistent shortfall, gives an
exception when it fires. The risk engine ranks issues for each portfolio, exceptions before watch items. Persistent
issues rank above single-period ones, because short periods are noisy and persistence carries more information than
size. Issues where the outcome and the way it was achieved both depart from the promise rank highest. Overdue actions
are always shown, so that the review starts from what was agreed last time.

## What the AI drafts
The AI drafts each item of the challenge pack from the facts that the risk engine produced and from nothing else. Every
number in each draft appears in the facts beside it, so the [grounding
check](../framework/08-controls.md#the-grounding-check) would pass. The questions are proposals; the risk manager
decides which to ask. **The funds and figures are illustrative.**

**Outperformance from unintended beta.**

| Fact | Value |
|---|---|
| Fund | Fund G |
| Excess return over benchmark before fees, last 12 months | 2.1% |
| Split of the excess: unintended beta from currency, after its holding cost / alpha | 1.6% / 0.5% |
| Return generator of the currency exposure | Market risk premium |
| Currency in confirmed mandate terms | Not part of the stated strategy |
| Currency tilt on record | None |
| Average unhedged US dollar exposure | 14% of net assets |

> Fund G returned 2.1% above its benchmark before fees over the last 12 months. Of that, 1.6% was unintended beta from
> currency, which is not part of its stated strategy and has no tilt on record; alpha was 0.5%. The currency return is a
> market risk premium, not skill. The fund held an average of 14% of net assets in unhedged US dollar exposure.
> *Question: Is the currency exposure intended, and if so, how is it managed?*

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

## Design choices
A risk function chooses how each of its performance measures is computed, and records the choice. This section sets
out the choices for this pillar, what each trades off, and how the function tests what it chose. The risk function owns
the model risk in its own performance measures; independent validation of the models sits elsewhere, as set out in
[investment risk](../framework/01-investment-risk.md#scope-and-boundaries).

### Risk-adjusted measures
Each measure answers one question, and each misleads in a known way.

| Measure | What it answers | Use it for | Where it misleads |
|---|---|---|---|
| Information ratio | Active return per unit of active risk | Benchmarked portfolios; the core measure of the pillar | Over short windows it is mostly noise, and a portfolio hugging its benchmark can show a high ratio on very little |
| Sharpe ratio | Return above cash per unit of total volatility | Absolute return and objective-based portfolios | Treats gains and losses alike, and flatters strategies whose losses are rare and large |
| Sortino ratio | Return above a target per unit of downside volatility | Absolute return portfolios where losses matter more than gains | Needs a long history, because downside observations are few |
| Realised drawdown | The fall from the portfolio's peak, absolute and relative to the benchmark | Every portfolio, against its drawdown tolerance | Depends on the window, and says nothing about how long recovery takes |
| Up-market and down-market capture | How much of the benchmark's rises and falls the portfolio takes part in | Showing whether returns come from the way the portfolio behaves in rising or in falling markets | Few observations in each state make it unstable over short periods |

A portfolio is not judged on one measure. The measures shown for each portfolio follow its mandate: a benchmarked
portfolio leads with the information ratio and relative drawdown, an absolute return portfolio with the Sharpe or
Sortino ratio and absolute drawdown.

### Windows and significance
Every measure is shown over **1, 3, 12 and 36 months**. The 12-month window is the default for the relative return
rule; a shortfall that shows on both the 1-month and the 3-month windows is an earlier watch, because the shorter
windows agreeing is less likely to be noise than either alone. Persistence is counted in whole periods.

Beside every information ratio, the **t-statistic** shows how much of it could be noise: the ratio times the square root
of the number of years measured. At an information ratio of 0.5 it takes about 16 years to reach a t-statistic of 2, as
[sources of return](../framework/02-sources-of-return.md#where-do-the-labels-mislead) sets out. Showing it on every
report keeps one good period from being read as skill.

### Benchmarks and peer groups
A benchmark decides every relative figure, so it is tested before it is used and reviewed while it is used. A sound
benchmark is:

- **Specified in advance,** before the period it judges.
- **Investable,** so the portfolio could have tracked it instead, at a known cost.
- **Unambiguous,** with its constituents and weights known.
- **Measurable,** with its return computable as often as the portfolio's.
- **Appropriate to the style** the mandate describes.
- **Owned,** with the portfolio manager accepting it as the measure of the mandate.

A benchmark that cannot be held, such as inflation plus a margin, still judges the promise, and the
[alpha and beta method](alpha-and-beta-method.md#scope-and-basis) sets out how an investable stand-in serves for the
split.

A peer group is tested in the same spirit: its members are chosen by stated criteria of strategy and vehicle, the
comparison includes portfolios that closed or merged during the period so that the survivors do not flatter the
group, and membership is reviewed on a set cycle.

### Linking attribution over time
Attribution effects measured period by period do not add up over longer periods, because returns compound. A linking
method spreads the difference across the periods so that the effects sum to the return over the whole period. Several
published methods exist, and they give slightly different answers, so the method is stated, held as a
[governed parameter](../framework/08-controls.md#materiality-thresholds-as-governed-parameters), and changed only from a
recorded effective date. The same applies to linking the lines of the
[alpha and beta split](alpha-and-beta-method.md#the-test-and-its-limits) over longer periods.

### Where the measures are weak
| Measure | Where it is weak | How the function tests it |
|---|---|---|
| Attribution | Depends on the model and benchmark chosen | Comparing methods; testing the benchmark as above |
| Relative return | Short periods are noisy | Several windows; persistence over several periods; the t-statistic |
| Ex-post tracking error | Depends on the window; noisy over short ones | Several windows; comparison with ex-ante from market risk |
| Risk-adjusted ratios | Rare large losses are understated until they happen | Reading them beside drawdown and stress |
| Peer comparison | Peer groups can be poorly matched or flattered by survivors | Membership criteria and a survivorship check |
| Factor exposures | Depend on the baskets and the estimated betas | Comparing with a regression on portfolio returns |
| Extracted mandate terms | The AI can miss or misread a term | Confirmation by the risk manager |

Attribution answers the question it is set up to answer: a different model or benchmark can tell a different story, so
the function checks that its choices fit each portfolio. Short periods are noisy, so persistence matters more than any
single period, which is why the ranking rule weighs it heavily. Peer groups can be poorly matched, which makes a
portfolio look better or worse than it is. The extracted mandate terms are the AI step's main limit in this pillar: an
error there would make every later test wrong, which is why the terms are confirmed by the risk manager before they are
used.

## Controls specific to this pillar
The general controls in [controls](../framework/08-controls.md) apply in full. This pillar adds five.

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
The measures from [measuring value](../framework/09-measuring-value.md) that matter most for this pillar are
influence measures, because the purpose of the review is to change what happens.

| Dimension | Measure for this pillar |
|---|---|
| Influence | Issues raised in reviews, and actions completed |
| Influence | Share of review time spent on the risk function's agenda |
| Speed | Working days from preparation to agreed minutes and actions |
| Quality | Drift or underperformance first identified outside the risk function |
| Capacity | Reviews held per quarter at full depth |
| Pillar-specific | Share of agreed actions closed by their due date; time on the watch list before an outcome |

In the flagship example, each review falls from 12.5 hours to 3.5 hours, and agreed minutes
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
- Sharpe, W. (1994). The Sharpe Ratio. *Journal of Portfolio Management*. Return per unit of total risk.
- Sortino, F. and Price, L. (1994). Performance Measurement in a Downside Risk Framework. *Journal of Investing*.
  Return per unit of downside risk against a target.
- Bailey, J. (1992). Evaluating Benchmark Quality. *Financial Analysts Journal*. The properties of a sound benchmark.
- Brown, S., Goetzmann, W., Ibbotson, R. and Ross, S. (1992). Survivorship Bias in Performance Studies. *Review of
  Financial Studies*. How dropping closed portfolios flatters a peer group.
- Carino, D. (1999). Combining Attribution Effects Over Time. *Journal of Performance Measurement*. Linking
  single-period attribution so that it sums over longer periods.
- Menchero, J. (2000). An Optimized Approach to Linking Attribution Effects Over Time. *Journal of Performance
  Measurement*. An alternative linking method, and why methods differ.
