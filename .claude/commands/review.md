---
description: Review the current diff for bugs, leakage, and project-rule violations
---
Run `git diff main...HEAD` (and `git diff` for uncommitted changes) and review it like a teammate doing a PR review.

Check, in order:
1. **Leakage** (CLAUDE.md rule 1): random/event-level splits, scalers fit on all data, Elo using same-day or future games, test-season data touched before freeze.
2. **Prof feedback** (rules 2–3): are new metrics also computed on contested subsets? Is interpretability output (coefs / importances / ablations) being preserved?
3. Correctness bugs (off-by-one in clock/period, home/away flips, label alignment).
4. Readability: unclear names, missing docstrings on public functions.

Output a short list: must fix / should fix / nit, each with file:line and *why*. Don't rewrite the code for us — point and explain.
