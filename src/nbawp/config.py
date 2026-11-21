"""Config + seeding plumbing (shared helper, OK for AI to write per CLAUDE.md)."""
import argparse
import os
import random
import re
from pathlib import Path

import numpy as np
import yaml


def load_config(path: str | Path = "configs/default.yaml") -> dict:
    with open(path) as f:
        return yaml.safe_load(f)


def cli_config() -> dict:
    """Parse `--config` from the command line and return the loaded config."""
    p = argparse.ArgumentParser()
    p.add_argument("--config", default="configs/default.yaml")
    return load_config(p.parse_args().config)


_SEASON_RE = re.compile(r"^(\d{4})-(\d{2})$")


def season_start_year(season: str) -> int:
    """'2018-19' -> 2018. shufinskiy/nba_data names files by start year."""
    m = _SEASON_RE.match(season)
    if not m or (int(m.group(1)) + 1) % 100 != int(m.group(2)):
        raise ValueError(f"bad season string {season!r}, expected like '2018-19'")
    return int(m.group(1))


def season_from_start_year(year: int) -> str:
    """2018 -> '2018-19' (nba_api / config format)."""
    return f"{year}-{(year + 1) % 100:02d}"


def season_source(cfg: dict, season: str) -> str:
    """Which raw source a season comes from: 'file' (shufinskiy) or 'api' (nba_api)."""
    season_start_year(season)  # validates format
    data = cfg["data"]
    file_seasons = data.get("file_source_seasons", [])
    if data["test_season"] in file_seasons:
        raise ValueError("test_season must come from nba_api, not file_source_seasons")
    return "file" if season in file_seasons else "api"


def set_seed(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)
    try:
        import torch
        torch.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)
    except ImportError:
        pass
