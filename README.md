# nba-winprob

DS340 final project (Fall '26) — Chris & David.

We train and compare **logistic regression**, **gradient boosting**, and an **LSTM** (stretch: small transformer) that predict the home team's win probability after every play-by-play event, then freeze them and test prospectively on 2026-27 games.

## Repo layout

```
nba-winprob/
├── CLAUDE.md              # context + rules for Claude Code (read this, Claude)
├── SETUP.md               # git + Claude Code setup for both of us
├── docs/
│   ├── PLAN.md            # timeline, milestones, who owns what
│   └── EVALUATION.md      # eval protocol incl. prof feedback (nontrivial preds, interpretability)
├── configs/default.yaml   # seasons, split years, hyperparams
├── data/                  # NOT committed (see data/README.md)
├── notebooks/             # exploration only — real code lives in src/
├── src/nbawp/
│   ├── data/              # download.py, clean.py            (Chris)
│   ├── features/          # elo.py, snapshot.py (Chris), sequences.py (David)
│   ├── models/            # baselines.py (Chris), lstm.py (David), transformer.py (stretch)
│   └── eval/              # splits.py, metrics.py, interpretability.py (both)
├── reports/               # figures/ and tables/ that go in the paper
└── tests/                 # leakage + metric sanity tests
```

## Quickstart

```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pip install -e .
pytest
```

## Pipeline (target)

```bash
python -m nbawp.data.download  --config configs/default.yaml   # raw PBP -> data/raw/
python -m nbawp.data.clean     --config configs/default.yaml   # -> data/processed/events.parquet
python -m nbawp.features.elo   --config configs/default.yaml   # -> data/processed/elo.parquet
python -m nbawp.models.baselines --config configs/default.yaml
python -m nbawp.models.lstm      --config configs/default.yaml
```

## AI use

Per our proposal, Claude/other AI is used as a **tutor and debugger**. Pipeline, features, models, and eval code are written by us. See `CLAUDE.md`.
