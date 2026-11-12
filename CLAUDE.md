# Risk

Asset management from an investment risk perspective, and how to redesign that work around AI: a philosophy, a
definition of investment risk and its three workflow pillars (market, liquidity, performance risk), the two sources of
return, the risk data the work rests on, the limits that apply each mandate, principles, a method for redesigning each
workflow, the controls that make it safe and how to measure the value. Its core pattern: **the risk engine computes, AI
analyses and narrates, a human judges.**

The framework's map is in `README.md`. Read it, and the chapters a change touches, before making the change.

## This is a public repository
- **Synthetic data only.** No real holdings, prices, flows, investor data or exports from any system.
- **Generic content only.** No firm names, fund names, internal system names, real limits, thresholds or internal policy
  text. Write about "an asset manager" or "a risk function"; use illustrative numbers.
- **No secrets.** No API keys, tokens, connection strings or local paths. Read keys from environment variables.
- **No dependency on private code.** Do not import from, vendor or copy code out of any other repository. Examples must
  run for anyone who clones this repo.
- **Commit messages and pull request descriptions say what changed**, not why it matters to anyone's employer.
- If a request would put something identifying into the repo, stop and say so.

## Voice
The repo presents a framework, not the history of how it was designed. Write in a normative voice ("a risk function
should...", "each workflow is redesigned by..."). No decision logs, status markers, roadmaps or open questions in the
content.

"Portfolio" is the general term for a fund or a segregated mandate; say fund or mandate only where the type matters.
The text stays jurisdiction-neutral, and each chapter ends with a Sources section listing the public standards and
literature it draws on.

## Design rules for the reference implementations
- **The AI never fabricates a number.** Every figure is computed by code from data, in the daily run or in an analysis
  the AI layer runs through the risk engine (an aggregation, an attribution, a what-if), with the run recorded. Beyond
  that the AI layer at most combines figures in simple ways (a sum, difference, ratio or percentage change), and a
  grounding check verifies that every number in generated text traces to a computed value or is recomputed from
  computed values; text that fails is rejected.
- **Exceptions over everything.** Workflows rank what needs a human's attention rather than handing over everything.
- **Every AI step has a human sign-off point and an audit trail** of what was generated and what the human changed.
- **Examples run without an AI service.** The narrative layer has a deterministic template backend so tests and demos
  run offline; an AI backend is optional and configured by environment variable.
- Calculations stay simple and transparent. The examples demonstrate workflows, not risk models.

## Ask, don't assume
This repo is built collaboratively. When anything is unclear (what a request means, its scope, what a chapter should
say, how code should be structured, what to do next), ask for clarification rather than inferring an answer and acting
on it. A short, specific question, with options where they help, is better than a confident guess.

In particular, if a change involves a risk-methodology choice the framework doesn't already settle (a measure, an
estimator, a default, a threshold convention, how a pillar is scoped), stop and ask rather than choosing.

## Keeping the framework consistent
- A change to a chapter's scope updates every chapter that refers to it, the map in `README.md` and the concept map in
  `framework/concept-map.md`, in the same commit.
- `framework/` holds the cross-cutting chapters; `pillars/` holds one chapter per pillar plus the integrated view,
  the alpha and beta method and the new portfolio review;
  `reference/` is for runnable code.

## Working conventions
- One coherent piece of work per branch, merged by pull request as one commit. Small fixes cluster into one branch and
  pull request; a substantial change gets its own. Keep each diff reviewable.
- Python, managed with `uv`. Tests sit next to the code they cover; add tests with every code change.
- Lines up to 120 characters; Markdown table rows that cannot wrap are exempt.
- Earlier code is preserved under the git tag `legacy-2020`. Do not restore it to the main branch.
