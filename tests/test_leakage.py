"""Leakage tests. Each skips until the function it checks exists."""
import importlib

import numpy as np
import pandas as pd
import pytest

from nbawp.config import load_config


def _get(module, name):
    mod = importlib.import_module(module)
    fn = getattr(mod, name, None)
    if fn is None:
        pytest.skip(f"{module}.{name} not implemented yet")
    return fn


@pytest.fixture
def cfg():
    return load_config("configs/default.yaml")


@pytest.fixture
def toy_events():
    """3 events per game, 2 games per season."""
    rows = []
    for s_i, season in enumerate(["2022-23", "2023-24", "2024-25", "2025-26", "2026-27"]):
        for g in range(2):
            gid = f"{s_i}{g}"
            for e in range(3):
                rows.append(dict(game_id=gid, season=season,
                                 game_date=pd.Timestamp(f"{2022 + s_i}-12-0{g + 1}"),
                                 event_idx=e, score_diff=e, home_win=g % 2))
    return pd.DataFrame(rows)


def test_config_splits_disjoint(cfg):
    s = cfg["splits"]
    groups = [set(s[k]) for k in ("train", "val", "holdout", "test")]
    for i in range(len(groups)):
        for j in range(i + 1, len(groups)):
            assert not groups[i] & groups[j], "a season appears in two splits"


def test_config_train_before_val_before_test(cfg):
    s = cfg["splits"]
    assert max(s["train"]) < min(s["val"]) <= max(s["val"]) < min(s["holdout"]) < min(s["test"])


def test_split_keeps_games_whole(cfg, toy_events):
    split_by_season = _get("nbawp.eval.splits", "split_by_season")
    cfg = {**cfg, "splits": {**cfg["splits"], "train": ["2022-23", "2023-24"],
                             "freeze_date": "2026-01-01"}}
    parts = split_by_season(toy_events, cfg)
    seen = {}
    for name, df in parts.items():
        for gid in df["game_id"].unique():
            assert gid not in seen, f"game {gid} in both {seen.get(gid)} and {name}"
            seen[gid] = name


def test_elo_uses_only_past_games():
    """Changing a game's result must not change that game's (or same-day games') pregame Elo."""
    compute_elo = _get("nbawp.features.elo", "compute_elo")
    games = pd.DataFrame({
        "game_id": ["a", "b", "c"],
        "game_date": pd.to_datetime(["2023-01-01", "2023-01-01", "2023-01-02"]),
        "season": ["2022-23"] * 3,
        "home_team": ["BOS", "NYK", "BOS"],
        "away_team": ["MIA", "LAL", "NYK"],
        "home_win": [1, 1, 0],
    })
    flipped = games.assign(home_win=[0, 1, 0])
    e1 = compute_elo(games).set_index("game_id")
    e2 = compute_elo(flipped).set_index("game_id")
    # game a's own result can't affect its pregame rating, nor same-day game b
    assert np.isclose(e1.loc["a", "elo_diff_pre"], e2.loc["a", "elo_diff_pre"])
    assert np.isclose(e1.loc["b", "elo_diff_pre"], e2.loc["b", "elo_diff_pre"])
    # but it SHOULD affect the next day's BOS game
    assert not np.isclose(e1.loc["c", "elo_diff_pre"], e2.loc["c", "elo_diff_pre"])
