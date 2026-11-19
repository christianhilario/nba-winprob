# data/

Nothing in here is committed except this README (see `.gitignore`).

```
data/
├── raw/         # nba_api responses, one file per game (from download.py)
├── interim/     # scratch
└── processed/
    ├── events.parquet   # cleaned event table (schema: src/nbawp/data/clean.py docstring)
    └── elo.parquet      # pregame Elo per game_id
```

Sharing: whoever runs the download first uploads `data/processed/*.parquet` to a shared Google Drive folder. The other person drops them in `data/processed/`.

nba_api tips: sleep between requests (`request_sleep_sec` in config), cache every raw response to disk so a crash doesn't mean re-downloading, and download season by season.
