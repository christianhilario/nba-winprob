"""Spec for Chris's game-list function in nbawp.data.download.

Expected: build_game_list(raw) takes the LeagueGameFinder dataframe (2 rows per game,
one per team) and returns ONE row per game with at least these columns:
    game_id (str, 10 chars with leading zeros), game_date, home_team_id, away_team_id,
    home_pts, away_pts, home_win (0/1), neutral_site (bool)
It must raise (ValueError or AssertionError) on malformed games.
Rename freely; just update the import below. Tests skip until the function exists.
"""
import pandas as pd
import pytest

download = pytest.importorskip("nbawp.data.download")
build_game_list = getattr(download, "build_game_list", None)
pytestmark = pytest.mark.skipif(build_game_list is None, reason="build_game_list not written yet")

COLS = ["SEASON_ID", "TEAM_ID", "TEAM_ABBREVIATION", "GAME_ID", "GAME_DATE", "MATCHUP", "WL", "PTS"]


def _raw(rows):
    return pd.DataFrame(rows, columns=COLS)


# Normal game: BOS hosts NYK, NYK wins.
NORMAL = [
    ("22023", 1610612738, "BOS", "0022300010", "2023-10-25", "BOS vs. NYK", "L", 104),
    ("22023", 1610612752, "NYK", "0022300010", "2023-10-25", "NYK @ BOS", "W", 108),
]
# International game, real 2024-25 format: BOTH rows say "IND @ SAS" -> SAS is designated home.
PARIS = [
    ("22024", 1610612754, "IND", "0022400633", "2025-01-25", "IND @ SAS", "W", 136),
    ("22024", 1610612759, "SAS", "0022400633", "2025-01-25", "IND @ SAS", "L", 98),
]


def _one(out, game_id):
    row = out[out["game_id"] == game_id]
    assert len(row) == 1, f"expected exactly one row for {game_id}"
    return row.iloc[0]


def test_one_row_per_game():
    out = build_game_list(_raw(NORMAL + PARIS))
    assert len(out) == 2
    assert out["game_id"].is_unique


def test_normal_game_home_away_and_label():
    g = _one(build_game_list(_raw(NORMAL)), "0022300010")
    assert g["home_team_id"] == 1610612738  # BOS
    assert g["away_team_id"] == 1610612752  # NYK
    assert (g["home_pts"], g["away_pts"]) == (104, 108)
    assert g["home_win"] == 0
    assert not g["neutral_site"]


def test_international_game_uses_team_after_at():
    g = _one(build_game_list(_raw(PARIS)), "0022400633")
    assert g["home_team_id"] == 1610612759  # SAS
    assert g["away_team_id"] == 1610612754  # IND
    assert (g["home_pts"], g["away_pts"]) == (98, 136)
    assert g["home_win"] == 0
    assert g["neutral_site"]


def test_game_id_keeps_leading_zeros_even_if_int():
    raw = _raw(NORMAL)
    raw["GAME_ID"] = raw["GAME_ID"].astype(int)  # how a CSV round-trip can mangle it
    out = build_game_list(raw)
    assert out["game_id"].tolist() == ["0022300010"]


def test_order_of_rows_does_not_matter():
    a = build_game_list(_raw(NORMAL))
    b = build_game_list(_raw(NORMAL[::-1]))
    assert a.iloc[0]["home_team_id"] == b.iloc[0]["home_team_id"]


@pytest.mark.parametrize(
    "rows",
    [
        NORMAL[:1],                                          # only one team row
        [NORMAL[0], NORMAL[1][:6] + ("L", 108)],             # nobody won
        [NORMAL[0], NORMAL[0][:1] + NORMAL[1][1:3] + NORMAL[0][3:5] + ("NYK vs. BOS", "W", 108)],  # two home teams
    ],
    ids=["single_row", "no_winner", "two_home_teams"],
)
def test_malformed_games_raise(rows):
    with pytest.raises((ValueError, AssertionError)):
        build_game_list(_raw(rows))
