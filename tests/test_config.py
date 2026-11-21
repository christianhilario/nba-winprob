import pytest

from nbawp.config import load_config, season_from_start_year, season_source, season_start_year


@pytest.mark.parametrize("season,year", [("2018-19", 2018), ("2023-24", 2023), ("1999-00", 1999)])
def test_season_round_trip(season, year):
    assert season_start_year(season) == year
    assert season_from_start_year(year) == season


@pytest.mark.parametrize("bad", ["2018", "2018-2019", "2018-20", "18-19", "2018/19"])
def test_bad_season_strings(bad):
    with pytest.raises(ValueError):
        season_start_year(bad)


def test_default_config_sources():
    cfg = load_config()
    d = cfg["data"]
    assert set(d["file_source_seasons"]) <= set(d["seasons"])
    assert season_source(cfg, "2018-19") == "file"
    assert season_source(cfg, "2024-25") == "api"
    assert season_source(cfg, d["test_season"]) == "api"


def test_test_season_cannot_be_file_sourced():
    cfg = load_config()
    cfg["data"]["file_source_seasons"].append(cfg["data"]["test_season"])
    with pytest.raises(ValueError):
        season_source(cfg, "2018-19")
