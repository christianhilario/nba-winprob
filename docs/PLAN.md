# Plan (Nov 19 → Dec 8)

~19 days. Tight, so the LSTM can't wait on a perfect pipeline: David starts on a tiny sample of events as soon as one season is cleaned.

| Dates | Chris | David | Both |
|---|---|---|---|
| Nov 19–21 | `download.py` for 1 season, start `clean.py` | read PBP sample, sketch `sequences.py` on it | repo + Claude Code setup |
| Nov 22–25 | finish `clean.py` all seasons, `elo.py` | `sequences.py` done, first LSTM training run | `eval/splits.py` + `metrics.py` |
| **Nov 26 — TA milestone** | LR + GBM trained, val log loss/Brier | LSTM val log loss | **deliverable:** val table (3 models, all events + contested subset) + one calibration plot |
| Nov 27–30 | interpretability for LR/GBM, no-score-diff ablation | LSTM tuning, feature-group permutation | **Nov 30: freeze models** (weights + config + git hash) |
| Dec 1–4 | pull 2026-27 games after freeze, run prospective test | transformer (stretch, only if LSTM is done) | bootstrap CIs, figures into `reports/` |
| Dec 5–8 | paper sections | paper sections | lightning talk slides, final paper **Dec 8** |

## Cut list if behind (in order)
1. Transformer
2. Retrain-based ablation (keep permutation-based)
3. Fewer seasons (4 instead of 6–8)
4. SHAP

Never cut: contested-subset metrics, interpretability tables (prof asked for both).
