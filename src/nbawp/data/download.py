"""Download raw play-by-play + game results from NBA.com via nba_api.  (Chris)

Writes one cached file per game to data/raw/<season>/<game_id>.json so reruns skip
what's already downloaded. Sleep `data.request_sleep_sec` between calls.

Useful nba_api endpoints to look at:
- nba_api.stats.endpoints.leaguegamefinder  -> list of games + results per season
- nba_api.stats.endpoints.playbyplayv3      -> event log for one game_id

Run: python -m nbawp.data.download --config configs/default.yaml
"""

# TODO(Chris): implement


if __name__ == "__main__":
    from nbawp.config import cli_config
    cfg = cli_config()
    raise NotImplementedError("download.py not written yet")
