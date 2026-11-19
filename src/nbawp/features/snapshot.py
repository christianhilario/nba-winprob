"""Per-event snapshot features for LR + GBM.  (Chris)

Input: events.parquet + elo.parquet. Output: feature matrix X + label y + game_id + season.

Ideas:
- config features.snapshot columns
- recent-trend features over last `features.trend_window_events` events
  (e.g. points run, change in score_diff) — rolling must be grouped by game_id!
- interaction: score_diff / sqrt(seconds_remaining + 1)  (makes LR less handicapped)

Keep a flag to DROP score_diff-derived features for the ablation the prof asked about.
"""

# TODO(Chris): implement
