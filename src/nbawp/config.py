"""Config + seeding plumbing (shared helper, OK for AI to write per CLAUDE.md)."""
import argparse
import os
import random
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
