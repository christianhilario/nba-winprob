---
description: Audit a file for train/test leakage
argument-hint: [path/to/file.py]
---
Read $ARGUMENTS and audit it for leakage only. Check specifically:

- Any split by event/row instead of by game_id + season
- `fit` / `fit_transform` called on data that includes val/holdout/test
- Pregame Elo or any rolling stat that includes the current game or later games (look for missing `.shift(1)` or `<` vs `<=` on dates)
- Features computed from the final score/outcome (e.g. final margin, total points)
- Sequence windows that cross game boundaries
- Anything reading 2026-27 data outside the frozen-test path

For each issue: line number, what leaks, how bad (fatal / minor), and a guiding question. If clean, say so in one line.
