# Performance risk

## In short
**The question:** is a portfolio delivering what was promised, in the way it was promised?

**The outcome:**

> The risk manager can show, with evidence, whether each portfolio is meeting its objective and whether its returns come
> from the sources its mandate describes.

**How the work is done:** the risk engine tracks every portfolio's realised measures and tests its exposures against the
confirmed mandate terms. The AI drafts a challenge pack: the top issues for the portfolio, the evidence for each and the
questions to ask. The risk manager runs the portfolio manager review on the risk function's agenda, with evidence that
is independent of the portfolio manager, and the agreed actions are tracked until they are closed.

| # | Step | Owner |
|---|---|---|
| 1 | Track realised return, ex-post tracking error, drawdown, active share, information ratio, factors and peer position | Risk engine |
| 2 | Test exposures against the mandate terms; flag drift and unintended bets | Risk engine |
| 3 | Rank the portfolio's issues, with market risk's tracking error and risk budget exceptions | Risk engine |
| 4 | Draft the challenge pack: evidence and questions for each issue | AI assistant |
| 5 | Grounding check on the pack | Risk engine |
| 6 | Review and edit the pack; set the agenda | Risk manager |
| 7 | Run the meeting on the risk function's agenda | Risk manager |
| 8 | Draft the minutes and the action log | AI assistant |
| 9 | Edit and agree the minutes and actions | Risk manager |
| 10 | Track follow-ups; escalate overdue actions to the watch list | Risk engine |

**Both halves of the outcome count:** a portfolio that beats its benchmark through an exposure its mandate does not
describe is not delivering what was promised, and the success may not last. The pillar reads what has happened. What
could happen next, including ex-ante tracking error and the risk budget, belongs to [market risk](market-risk.md).

**Where it connects:** underperformance often comes before redemptions, so [liquidity risk](liquidity-risk.md) watches
flows more closely in portfolios flagged here. Style drift and unintended bets can raise concentration and volatility in
market risk, whose tracking error and risk budget exceptions feed the challenge pack. The [integrated
view](integrated-view.md) reads these signals together.

The rest of this chapter is the detail behind these points.

## Workflows in this pillar

| Workflow | Cadence | Output | Used by | For which decision |
|---|---|---|---|---|
| Portfolio manager review | Quarterly | Challenge pack, minutes, actions | Risk manager | What must be explained |
| Attribution reporting | Monthly | Return by source | Risk manager | Whether returns come from intended sources |
| Realised risk and drawdown | Daily | Ex-post tracking error; drawdown, absolute and relative | Risk manager | Whether the portfolio runs beyond its promise |
| Peer comparison | Monthly | Position against peers | Investment oversight | Whether the outcome is competitive |
| Style and mandate consistency | Daily | Exposures against mandate terms | Risk manager | Whether the portfolio drifts |
| Watch list management | Monthly | Portfolios under watch, with actions | Investment oversight | Whether to escalate |

The portfolio manager review is the flagship, shown in the table at the top: it is where the pillar's evidence meets the
person who can act on it. The other workflows feed it.

- **Attribution** separates the two [sources of return](../framework/02-sources-of-return.md), using the [alpha and beta
  method](alpha-and-beta-method.md), and shows each beta line by the [return
  generator](../framework/02-sources-of-return.md#what-generates-return) that paid it: market risk premia or style
  premia, with alpha read as skill. The generator tells the risk manager [how the return could
  stop](../framework/02-sources-of-return.md#how-does-each-generator-fail), which sets the question to put to the
  portfolio manager.
- **The watch list** holds the portfolios whose issues have not been resolved. It is a single list for the firm, owned
  by the risk function, to which this pillar and the [integrated view](integrated-view.md) both add portfolios.
  Investment oversight uses it to decide escalation, and an escalated portfolio goes to the risk committee, as [limits
  and escalation](../framework/04-limits-and-escalation.md#escalation) sets out.
- **Challenge.** When a portfolio manager explains an issue, the AI tests the explanation against the risk function's
  data and reports what supports it and what contradicts it, in the challenge mode of [working with
  AI](../framework/06-working-with-ai.md#three-modes-of-working). The risk manager weighs that evidence; the AI does not
  judge the explanation.

**Ex-post tracking error** and **realised drawdown**, absolute and relative, belong to this pillar. Their
forward-looking counterparts belong to [market risk](market-risk.md), which also reads the headroom the drawdown leaves
before the drawdown tolerance.

Relative return and drawdown are computed every day over a rolling window, a governed parameter illustrated here as 12
months, so that a shortfall reaches watch as soon as it forms rather than at the end of a quarter. A run of losing
periods is counted in whole periods. The windows, and the significance shown beside each figure, are set out under
[design choices](performance-risk.md#windows-and-significance).

## Mandate terms
Testing a portfolio against what it promised needs the promise in a form the risk engine can test. The AI extracts the
portfolio's stated objective, benchmark, style, limits and dealing terms from its documents into structured terms, each
linked to the passage it came from. The risk manager confirms the terms once, and again whenever the documents change.
The risk engine then tests holdings and exposures against the confirmed terms and flags style drift and unintended bets.
The AI reads the documents and the risk engine makes the comparison. For a hard limit, compliance's coded rule is the
master reading: the extracted limit is reconciled to it, and a difference is routed to compliance, not settled by the
risk manager. The risk function owns the objective and style terms, which compliance does not code, once the risk
manager has confirmed them. For a new portfolio, the terms are first extracted and confirmed in the [new portfolio
review](new-portfolio-review.md).

## Materiality and exceptions
An **exception** in this pillar is a reading that has crossed a rule's threshold: a sign that the portfolio is not
delivering its promise, or not in the way it promised. A **watch item** is an early sign that has not crossed one: a
shortfall that is not yet significant, or a reading seen in one period only. Each rule is a [governed
parameter](../framework/08-controls.md#materiality-thresholds-as-governed-parameters). **The example values below are
illustrative and are not recommendations;** each risk function sets its own.

| Kind of rule | Example (illustrative) | What it catches |
|---|---|---|
| Significant shortfall | Cumulative shortfall net of fees against benchmark or objective that is large against tracking error: a t-statistic below a set level, such as -2 | Missing the promise by more than noise |
| Shortfall not yet significant | A shortfall over the rolling window, on both short windows, or in several consecutive periods | A shortfall that may become significant |
| Ex-post tracking error | Outside the range the mandate terms imply | Too much or too little active risk taken |
| Drawdown | Realised drawdown, absolute or relative, beyond its tolerance | Losses that end mandates |
| Active share | Falling for several consecutive quarters | A portfolio moving towards its benchmark |
| Source of return | A large share of gross excess return from unintended beta, over several periods | Returns from the wrong sources |
| Style consistency | Exposures outside the confirmed mandate terms | Style drift |
| Overdue action | An agreed action past its due date | Follow-up that has stalled |

A shortfall that is not yet significant is a watch item, whether it shows over the rolling window, on both the 1-month
and 3-month windows, or as a run of consecutive periods. So is a single period of the source-of-return reading. Every
other rule in the table, including a significant shortfall, gives an exception when it fires. The risk engine ranks
issues for each portfolio, exceptions before watch items. Significant issues rank above those that are not, because
short periods are noisy, and significance weighs both the size of a shortfall and how long it has lasted. Issues where
the outcome and the way it was achieved both depart from the promise rank highest. Overdue actions are always shown, so
that the review starts from what was agreed last time.

## What the AI drafts
The AI drafts each item of the challenge pack from the facts that the risk engine produced and from nothing else. Every
number in the draft appears in the facts beside it, so the [grounding
check](../framework/08-controls.md#the-grounding-check) would pass. The questions are proposals; the risk manager
decides which to ask. **The fund and figures are illustrative.**

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

## Design choices
A risk function chooses how each of its performance measures is computed, records the choice and tests it. Independent
validation of the models sits outside the risk function, as set out in [investment
risk](../framework/01-investment-risk.md#scope-and-boundaries).

### Risk-adjusted measures
Each measure misleads in a known way.

| Measure | Use it for | Where it misleads |
|---|---|---|
| Information ratio | Benchmarked portfolios; the core measure of the pillar | Over short windows it is mostly noise, and a portfolio hugging its benchmark can show a high ratio on very little |
| Sharpe ratio | Absolute return and objective-based portfolios | Treats gains and losses alike, and flatters strategies whose losses are rare and large |
| Sortino ratio | Absolute return portfolios where losses matter more than gains | Needs a long history, because downside observations are few |
| Realised drawdown | Every portfolio, against its drawdown tolerance | Depends on the window, and says nothing about how long recovery takes |
| Up-market and down-market capture | Showing whether returns come from the way the portfolio behaves in rising or in falling markets | Few observations in each state make it unstable over short periods |

A portfolio is not judged on one measure. The measures shown for each portfolio follow its mandate: a benchmarked
portfolio leads with the information ratio and relative drawdown, an absolute return portfolio with the Sharpe or
Sortino ratio and absolute drawdown.

### Windows and significance
Every measure is shown over several windows, because each answers a different question. **The set below is an
illustrative setup;** each risk function chooses its own and holds it as a governed parameter.

| Window | What it is for | Where it is weak |
|---|---|---|
| 1 and 3 months | An early sign that something has changed | Mostly noise on its own |
| 12 months | The rolling window for relative return and drawdown | Still short against the time skill takes to show |
| 36 months | A fuller view of how the portfolio is run | Slow to show a change, and may span a change of manager or style |
| The mandate's own stated period | The period over which the promise was made, such as a rolling five years | May be longer than the portfolio's record |
| Since inception | The whole record, and the most data | Dominated by early periods, when the portfolio may have been small |

A shortfall that shows on both the 1-month and the 3-month windows is an earlier watch, because the shorter windows
agreeing is less likely to be noise than either alone. A run of losing periods is counted in whole periods.

Beside every information ratio, the **t-statistic** shows how much of it could be noise: the ratio times the square root
of the number of years measured. At an information ratio of 0.5 it takes about 16 years to reach a t-statistic of 2, as
[sources of return](../framework/02-sources-of-return.md#where-do-the-labels-mislead) sets out. Showing it on every
report keeps one good period from being read as skill.

The same statistic tests a shortfall: the cumulative shortfall over a window, divided by the tracking error scaled to
the window's length. A shortfall is **significant** when the statistic falls below a set level, illustrated here as -2,
on the rolling window or any longer one. A count of losing periods throws away the size of each shortfall, and a manager
with real skill still loses in many periods, so a run of periods gives a watch item and only significance gives an
exception. For a portfolio with an objective and no benchmark, the shortfall is set against the volatility of its return
over the objective.

### Benchmarks and peer groups
A benchmark decides every relative figure, so it is tested before it is used and reviewed while it is used. A sound
benchmark is:

- **Specified in advance,** before the period it judges.
- **Investable,** so the portfolio could have tracked it instead, at a known cost.
- **Unambiguous,** with its constituents and weights known.
- **Measurable,** with its return computable as often as the portfolio's.
- **Appropriate to the style** the mandate describes.
- **Owned,** with the portfolio manager accepting it as the measure of the mandate.

A benchmark that cannot be held, such as inflation plus a margin, still judges the promise, and the [alpha and beta
method](alpha-and-beta-method.md#scope-and-basis) sets out how an investable stand-in serves for the split.

A peer group is tested in the same spirit: its members are chosen by stated criteria of strategy and vehicle, the
comparison includes portfolios that closed or merged during the period so that the survivors do not flatter the group,
and membership is reviewed on a set cycle.

### Linking attribution over time
Published linking methods give slightly different answers, so the method is stated, held as a [governed
parameter](../framework/08-controls.md#materiality-thresholds-as-governed-parameters), and changed only from a recorded
effective date. The same applies to linking the lines of the [alpha and beta
split](alpha-and-beta-method.md#the-test-and-its-limits) over longer periods.

### Where the measures are weak
| Measure | Where it is weak | How the function tests it |
|---|---|---|
| Attribution | Depends on the model and benchmark chosen | Comparing methods; testing the benchmark as above |
| Relative return | Short periods are noisy | Several windows; significance by the t-statistic; runs of periods as a watch only |
| Ex-post tracking error | Depends on the window; noisy over short ones | Several windows; comparison with ex-ante from market risk |
| Risk-adjusted ratios | Rare large losses are understated until they happen | Reading them beside drawdown and stress |
| Peer comparison | Peer groups can be poorly matched or flattered by survivors | Membership criteria and a survivorship check |
| Factor exposures | Depend on the baskets and the estimated betas | Comparing with a regression on portfolio returns |
| Extracted mandate terms | The AI can miss or misread a term, which would make every later test wrong | Confirmation by the risk manager before the terms are used |

## Controls and measures specific to this pillar
The general [controls](../framework/08-controls.md) apply in full. This pillar adds five.

- **Mandate terms are confirmed before use.** Extracted terms are not tested against until the risk manager confirms
  them, each term links to its source passage, and a change to the documents triggers re-extraction with the differences
  shown.
- **Evidence is independent.** The challenge pack is built from the risk function's own data, not from material the
  portfolio manager supplies.
- **Questions are chosen by the risk manager.** Drafted questions are proposals; the risk manager decides what to ask.
- **Watch list exits are decided.** A portfolio leaves the watch list only by a recorded decision, not because its
  actions were closed automatically, whichever workflow added it.
- **The split reconciles before drafting.** The lines of the [alpha and beta](alpha-and-beta-method.md) split must sum
  to the gross return, and alpha must show no exposure to a declared factor, within stated tolerances, before the AI
  drafts from them. A split that fails is an exception in its own right. A missing-factor flag goes to the risk manager.

Of the measures in [measuring value](../framework/09-measuring-value.md), influence matters most here, because the
purpose of the review is to change what happens.

| Dimension | Measure for this pillar |
|---|---|
| Influence | Issues raised in reviews, and actions completed |
| Influence | Share of review time spent on the risk function's agenda |
| Speed | Working days from preparation to agreed minutes and actions |
| Quality | Drift or underperformance first identified outside the risk function |
| Capacity | Reviews held per quarter at full depth |
| Pillar-specific | Share of agreed actions closed by their due date; time on the watch list before an outcome |

## Sources
- Grinold, R. and Kahn, R. (2000). *Active Portfolio Management*, 2nd edition. McGraw-Hill. Ex-post tracking error, the
  information ratio and persistence as evidence of skill.
- Brinson, G., Hood, L. and Beebower, G. (1986). Determinants of Portfolio Performance. *Financial Analysts Journal*.
  Attribution by decision into allocation and selection.
- Cremers, M. and Petajisto, A. (2009). How Active Is Your Fund Manager? A New Measure That Predicts Performance.
  *Review of Financial Studies*. Active share as a measure of how far holdings depart from the benchmark.
- Sharpe, W. (1994). The Sharpe Ratio. *Journal of Portfolio Management*. Return per unit of total risk.
- Sortino, F. and Price, L. (1994). Performance Measurement in a Downside Risk Framework. *Journal of Investing*. Return
  per unit of downside risk against a target.
- Bailey, J. (1992). Evaluating Benchmark Quality. *Financial Analysts Journal*. The properties of a sound benchmark.
- Brown, S., Goetzmann, W., Ibbotson, R. and Ross, S. (1992). Survivorship Bias in Performance Studies. *Review of
  Financial Studies*. How dropping closed portfolios flatters a peer group.
- Carino, D. (1999). Combining Attribution Effects Over Time. *Journal of Performance Measurement*. Linking
  single-period attribution so that it sums over longer periods.
- Menchero, J. (2000). An Optimized Approach to Linking Attribution Effects Over Time. *Journal of Performance
  Measurement*. An alternative linking method, and why methods differ.
