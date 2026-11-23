# Data integrity

## The essentials
**Data integrity** asks whether every figure the framework shows, for risk, performance or liquidity, can be trusted,
and reproduced later.

**What every figure rests on:** data the risk function did not create, from positions and prices to returns, flows and
the terms of each mandate. The same data serves the risk function, performance measurement and the investment team, so
one set of numbers starts from one set of data. It is checked before anything is computed, versioned as it was known,
filled with flagged proxies where it has gaps, and corrected at its source, never patched.

**How the work is done:** on every run the analytics engine checks every domain for every portfolio and triages the
breaks by what they could change. The AI drafts a notice to the owner of each break's source. The risk manager
prioritises the breaks and decides whether the day's measures run, wait or run marked.

**Who owns what:** the risk function owns fitness for use: the checks, the proxy policy and whether a run goes ahead.
Each domain has a named owner responsible for its quality and for correcting it at source; in a larger firm this is
often a dedicated data team.

The rest of this chapter is the detail behind these points.

## What the analytics engine reads
The analytics engine computes from the same domains for every portfolio, whatever its vehicle or strategy. Documents,
the last domain, are read by the AI.

| Domain | What it holds | Used by |
|---|---|---|
| Positions | Each portfolio's holdings, cash and derivative positions, with collateral posted and received | Every pillar |
| Prices | The price of each holding, with its source and the date it last changed | Every pillar |
| Market data | Index and basket returns, the prices and holding costs of the ETFs and futures in top-down portfolios, rates, spreads, volatilities and trading volumes | Market and liquidity risk, alpha and beta |
| Reference data | What each security is: issuer, type, sector, country, currency, rating, maturity | Every pillar |
| Benchmarks | Each benchmark's constituents and weights | Market and performance risk, alpha and beta |
| Returns and valuations | Net asset values, accounting values, fees and the cash flows behind time-weighted returns, gross and net | Performance risk, alpha and beta |
| Flows and investors | Subscriptions, redemptions, withdrawals and the shares held by the largest investors and distributors, including redemptions notified in dealing notices, read by the AI and confirmed by the risk manager, and matched to the dealing record when it arrives | Liquidity risk |
| Margin and financing | Margin and collateral calls, borrowing and its maturity, commitments, currency hedges and their roll dates, securities on loan and their collateral | Liquidity risk |
| Mandate terms | The objective, benchmark, style, limits and dealing terms, confirmed by the risk manager, with hard limits reconciled to compliance's rules | Every pillar |
| Records of decisions | Tilts and timing calls as recorded, including those the AI extracted from minutes and the risk manager confirmed, and trades with their tags | Performance risk, alpha and beta |
| Documents | Governing documents, committee minutes and dealing notices, kept as received with the date they were received and their source | Read by the AI, which extracts from them; only confirmed extractions enter the other domains |

A portfolio that invests in other funds is read through to their holdings, which carry their as-of date.

In the domains the analytics engine computes from, personal data about investors is kept to what the measures need:
shares and flows, not identities. Documents kept as received can name investors and people. They are read only by an AI
service approved for that data, and a record extracted from one carries no more personal data than the domain it
enters. The rules on what may be sent to an AI service are set out under [data handling](08-controls.md#data-handling).

## From source to computed figure
The analytics engine takes each item from its domain's **golden source** and nowhere else, so two outputs never disagree
because they read different copies of the same number.

The analytics engine keeps what it reads in a **data store**: the golden source's data as received, with the date it
became known, never edited. It is a record of the one copy, not a second copy, so nothing in it can drift from the
source. Every run follows the same order.

| Step | What happens |
|---|---|
| Take in | Each domain is loaded from its golden source, with the time it arrived |
| Check | The quality checks below run on every domain, and breaks are recorded |
| Enrich | Classification is added, proxies are applied under the policy, and look-through holdings are joined |
| Snapshot | The checked and enriched data is fixed as the version the run will use |
| Compute | Every measure is computed from the snapshot, and only from the snapshot |

The order matters. Nothing is computed from data that has not been checked, and every computed figure points to the
snapshot it came from, so that it can be traced back to the records and sources behind it.

## Versioned as known
Each record in the data store carries two dates: the date it describes and the date it became known.

- **Reproducing a past output** uses the data as it was known on the day the output was produced, so the figure that was
  shown, and acted on, can be shown again exactly.
- **Measuring history**, such as a backtest or a volatility, uses the data as it is known today, corrections included.

A correction never overwrites what was known before. Both versions stay, and the audit trail records which one each
output used. The same applies to thresholds and other governed parameters, which are
[versioned](08-controls.md#materiality-thresholds-as-governed-parameters) with the dates they took effect.

## Quality before computation
Every domain passes checks in five dimensions before the snapshot is fixed. **The examples below are illustrative;**
each risk function sets its own checks and tolerances.

| Dimension | Example checks (illustrative) |
|---|---|
| Completeness | Every holding priced and classified; every portfolio's file arrived |
| Accuracy | Positions reconcile to the portfolio's accounting value within a tolerance; price jumps outside a security's usual range; a portfolio's return consistent with its change in net asset value after flows and fees |
| Timeliness | Files arrived by their deadline; prices that have not changed for a set number of days |
| Consistency | The same security described the same way in every domain; benchmark weights summing to the whole |
| Validity | Values inside their allowed ranges, such as weights between limits and dates in order |

A failed check is a **data break**. Each break is recorded with the portfolios and measures it affects, and the run
follows a rule set in advance: it waits for the correction, or it runs with the affected portfolios marked. A portfolio
whose data has a break it cannot run past is shown as not assessed, never as clean.

Stale prices are both a data check and a measure of valuation risk. The check finds them; [liquidity
risk](../pillars/liquidity-risk.md#materiality-and-exceptions) flags the holdings to the owner of pricing and shows
which measures rest on them.

The check runs in nine steps:

| # | Step | Owner |
|---|---|---|
| 1 | Take in every domain; check completeness, timeliness and validity | Analytics engine |
| 2 | Reconcile positions to accounting values; check prices against each security's history | Analytics engine |
| 3 | Apply proxies under the policy and flag them | Analytics engine |
| 4 | Triage breaks by the portfolios and measures they affect | Analytics engine |
| 5 | Draft a notice for each break to the owner of its source | AI |
| 6 | Grounding check on every notice | Analytics engine |
| 7 | Prioritise and judge each break; decide whether to run, wait or run marked | Risk manager |
| 8 | Edit and send the notices | Risk manager |
| 9 | Track each break to closure | Analytics engine |

A break affecting a large share of a portfolio, or a measure close to its limit, comes above one that could not move any
reading the risk manager would see.

## Proxies
A **proxy** fills a gap with something close enough to compute from, such as a sector's beta for a new security or the
last known holdings of an underlying fund.

The risk function sets one proxy policy for all domains.

- **Every proxy is flagged.** A figure computed partly from a proxy says so, wherever it appears.
- **Every proxy is governed.** The choice of proxy for each kind of gap is a [governed
  parameter](08-controls.md#materiality-thresholds-as-governed-parameters), owned by the risk function.
- **Proxies are measured.** The share of each portfolio, by value, that rests on proxies is reported beside its
  measures, and a share above a set level is a data break in its own right.
- **Proxies are temporary.** A proxy is replaced as soon as the real data arrives, and a proxy that has stayed beyond a
  set age is a data break.

Each pillar chooses the proxies for its own measures within this policy, in its design choices.

## Who owns what
The risk function owns **fitness for use**: the checks, their tolerances, the proxy policy and the decision whether a
run can go ahead. Each domain has a named owner responsible for its quality and for **correcting** it at source; in a
larger firm this is often a dedicated data team, which works on the underlying data continuously rather than as a side
task. The risk function does not patch data in the data store; where it cannot wait for a correction, it runs with the
affected portfolios marked or uses a proxy under the policy. A break is routed to the source's owner with the evidence
and tracked until it is closed.

## What the AI drafts
Every number in the draft appears in the facts beside it, so the [grounding check](08-controls.md#the-grounding-check)
would pass. **The fund and figures are illustrative.**

| Fact | Value |
|---|---|
| Fund | Fund M |
| Check | Position total against accounting value |
| Difference | 0.6% of net assets |
| Tolerance | 0.1% of net assets |
| Holding in accounting records, missing from the position file | 45,000 units of one bond |
| Source | Position file |

> Fund M's position total differs from its accounting value by 0.6% of net assets, above the 0.1% tolerance. The
> difference matches one holding of 45,000 units of a bond that appears in the accounting records but not in the
> position file.

## Controls and measures specific to data integrity
The rules above (a checked snapshot, breaks shown, corrections at source, a reproducible past) are this chapter's
controls; the general [controls](08-controls.md) apply in full.

Of the measures in [measuring value](09-measuring-value.md), speed and quality matter most here: how soon the day's
measures can be trusted, and whether a break reaches an output unseen.

| Dimension | Measure for data integrity |
|---|---|
| Speed | Time from data arrival to a checked snapshot |
| Capacity | Portfolios and domains checked in full each day |
| Quality | Breaks found after an output was released |
| Influence | Breaks corrected at source by their due date; breaks that recur |
| Data integrity specific | Share of each portfolio resting on proxies; age of the oldest open break |

## Sources
- Basel Committee on Banking Supervision (2013). *Principles for Effective Risk Data Aggregation and Risk Reporting.*
  Accuracy, completeness, timeliness and adaptability of the data behind risk reporting, and its governance.
- DAMA International (2017). *DAMA-DMBOK: Data Management Body of Knowledge*, 2nd edition. Technics Publications. Data
  quality dimensions, ownership of data and golden sources.
- Snodgrass, R. (1999). *Developing Time-Oriented Database Applications in SQL.* Morgan Kaufmann. Recording both the
  date a fact describes and the date it became known, so that past states can be reproduced.
