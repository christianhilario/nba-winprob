"""Raw PBP -> cleaned game-level event table.  (Chris)

THIS DOCSTRING IS THE SOURCE OF TRUTH FOR THE EVENT TABLE SCHEMA. Update it when columns change.

Output: data/processed/events.parquet, one row per event, sorted by (game_id, event_idx).

Columns (proposed — edit as you build it):
    game_id            str    NBA.com game id
    season             str    e.g. "2023-24"
    game_date          date
    event_idx          int    0..n-1 order within game
    period             int    1-4, 5+ = OT
    seconds_remaining  float  seconds left in regulation (OT: define + document!)
    home_score         int    AFTER this event
    away_score         int    AFTER this event
    score_diff         int    home_score - away_score
    event_type         str    shot_made, shot_missed, ft, rebound, turnover, foul, timeout, sub, ...
    team_side          str    "home" / "away" / "none"
    points             int    points scored on this event
    possession_home    int    1 if home has ball after event (best effort)
    home_fouls, away_fouls, home_timeouts, away_timeouts   int   running counts
    home_win           int    LABEL: 1 if home won the game (same for every event in a game)

Leakage notes: home_win and final scores must NEVER be used as features.

Run: python -m nbawp.data.clean --config configs/default.yaml
"""

# TODO(Chris): implement


if __name__ == "__main__":
    from nbawp.config import cli_config
    cfg = cli_config()
    raise NotImplementedError("clean.py not written yet")
