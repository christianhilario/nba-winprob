"""Metric sanity tests. Each skips until the function exists in nbawp.eval.metrics."""
import importlib

import numpy as np
import pytest


def _get(name):
    fn = getattr(importlib.import_module("nbawp.eval.metrics"), name, None)
    if fn is None:
        pytest.skip(f"metrics.{name} not implemented yet")
    return fn


def test_log_loss_coin_flip():
    log_loss = _get("log_loss")
    y = np.array([0, 1, 0, 1])
    assert np.isclose(log_loss(y, np.full(4, 0.5)), np.log(2))


def test_log_loss_matches_sklearn():
    log_loss = _get("log_loss")
    from sklearn.metrics import log_loss as sk
    rng = np.random.default_rng(0)
    y, p = rng.integers(0, 2, 200), rng.uniform(0.01, 0.99, 200)
    assert np.isclose(log_loss(y, p), sk(y, p))


def test_brier_bounds():
    brier = _get("brier")
    y = np.array([0, 1])
    assert np.isclose(brier(y, np.array([0.0, 1.0])), 0.0)
    assert np.isclose(brier(y, np.array([1.0, 0.0])), 1.0)
    assert np.isclose(brier(y, np.array([0.5, 0.5])), 0.25)


def test_game_weights_sum_to_one_per_game():
    game_weights = _get("game_weights")
    gids = np.array(["a", "a", "a", "b"])
    w = game_weights(gids)
    assert np.isclose(w[gids == "a"].sum(), 1.0)
    assert np.isclose(w[gids == "b"].sum(), 1.0)


def test_skill_vs_baseline():
    skill = _get("skill_vs_baseline")
    assert np.isclose(skill(0.5, 0.5), 0.0)
    assert skill(0.4, 0.5) > 0
