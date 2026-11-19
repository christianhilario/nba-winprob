"""Pregame Elo-style team ratings.  (Chris)

Output: data/processed/elo.parquet with columns
    game_id, home_elo_pre, away_elo_pre, elo_diff_pre

Rules:
- Process games in date order. A game's pregame rating uses ONLY games completed
  before that game's date (same-day games must not see each other's results).
- Between seasons, regress toward the mean (config: elo.season_carryover).
- Params in config: elo.k, elo.home_adv.

There's a test for this in tests/test_leakage.py (test_elo_uses_only_past_games).

Run: python -m nbawp.features.elo --config configs/default.yaml
"""

# TODO(Chris): implement
