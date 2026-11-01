# Risk

A framework for redesigning investment risk management around AI: principles, a definition of investment risk and its
three workflow pillars (market, liquidity, performance risk), a method for redesigning each workflow, the controls that
make it safe, and how to measure the value. Reference implementations on synthetic data show the core pattern:
**code computes, AI narrates, a human judges.**

The framework's map is in `README.md`. Read it, and the chapters a change touches, before making the change.

## This is a public repository
- **Synthetic data only.** No real holdings, prices, flows, investor data or exports from any system.
- **Generic content only.** No firm names, fund names, internal system names, real limits, thresholds or internal policy
  text. Write about "a fund manager" or "a risk function"; use illustrative numbers.
- **No secrets.** No API keys, tokens, connection strings or local paths. Read keys from environment variables.
- **No dependency on private code.** Do not import from, vendor or copy code out of any other repository. Examples must
  run for anyone who clones this repo.
- **Commit messages and pull request descriptions say what changed**, not why it matters to anyone's employer.
- If a request would put something identifying into the repo, stop and say so.

## Voice
The repo presents a framework, not the history of how it was designed. Write in a normative voice ("a risk function
should...", "each workflow is redesigned by..."). No decision logs, status markers, roadmaps or open questions in the
content.

## Design rules for the reference implementations
- **The LLM never produces a number.** Every figure is computed by code from data. The narrative layer only writes text
  around figures it is given, and a grounding check verifies that every number in generated text matches a computed
  value; text that fails is rejected.
- **Exceptions over everything.** Workflows rank what needs a human's attention rather than handing over everything.
- **Every AI step has a human sign-off point and an audit trail** of what was generated and what the human changed.
- **Examples run without an LLM.** The narrative layer has a deterministic template backend so tests and demos run
  offline; an LLM backend is optional and configured by environment variable.
- Calculations stay simple and transparent. The examples demonstrate workflows, not risk models.

## Ask, don't decide
If a change involves a risk-methodology choice the framework doesn't already settle (a measure, an estimator, a
default, a threshold convention, how a pillar is scoped), stop and ask rather than choosing.

## Keeping the framework consistent
- A change to a chapter's scope updates every chapter that refers to it, and the map in `README.md`, in the same commit.
- `framework/` holds the cross-cutting chapters; `pillars/` holds one chapter per pillar plus the integrated view;
  `reference/` holds runnable code.

## Working conventions
- One change per branch, merged by pull request; keep each diff small enough to review.
- Python, managed with `uv`. Tests sit next to the code they cover; add tests with every code change.
- Lines up to 120 characters.
- Earlier code is preserved under the git tag `legacy-2020`. Do not restore it to the main branch.
