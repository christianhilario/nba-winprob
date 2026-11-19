"""Metrics + subsets.  (Both)  See docs/EVALUATION.md.

Suggested API (tests in tests/test_metrics.py expect these names):

    log_loss(y, p, weights=None) -> float
    brier(y, p, weights=None) -> float
    game_weights(game_ids) -> np.ndarray          # each game sums to 1
    skill_vs_baseline(ll_model, ll_baseline) -> float   # 1 - ll_model / ll_baseline
    contested_mask(df, p_baseline, band) -> bool array
    close_late_mask(df, margin) -> bool array
    bootstrap_ci(df, metric_fn, reps, seed) -> (lo, hi)   # resample GAMES, not events
    calibration_table(y, p, bins) -> DataFrame
"""

# TODO(both): implement
