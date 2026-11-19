"""Season- and game-based splits.  (Both)

Suggested API (tests in tests/test_leakage.py expect this):

    split_by_season(df, cfg) -> dict[str, pd.DataFrame]   # keys: train, val, holdout, test

Uses cfg["splits"]. Every game_id must land in exactly one split.
Test split must also respect cfg["splits"]["freeze_date"].
"""

# TODO(both): implement
