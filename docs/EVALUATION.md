# Evaluation protocol

## Splits (leak-free)
| Split | Seasons | Use |
|---|---|---|
| train | e.g. 2018-19 → 2023-24 | fit models |
| val | 2024-25 | tuning, early stopping, model selection |
| holdout | 2025-26 | final retrospective comparison |
| prospective test | 2026-27 games played after freeze | the real test, touched once |

Split by game and season, never by event. Elo computed strictly from games before each game date.

## Metrics
- Log loss, Brier score (primary)
- Calibration curves (10 bins) + ECE
- Accuracy at checkpoints: end of Q1, Q2, Q3, 5:00 left in Q4
- Bootstrap 95% CIs **resampling games** (not events), 1000 reps; paired bootstrap for model-vs-model differences

## Prof feedback #1 — nontrivial predictions
Score diff makes late-game prediction trivial. So every metric is reported on:
1. **All events** (for completeness)
2. **Contested states:** events where the score+time-only LR baseline predicts between 0.25 and 0.75
3. **Close-late:** Q4 / OT with |score diff| ≤ 5
4. **Early game:** Q1–Q2 only
5. **Exclude garbage time:** drop events with < 2:00 left and |diff| ≥ 10

And:
- Report **skill relative to the score+time baseline**: `1 - LogLoss(model) / LogLoss(score_time_LR)`, not just vs. 50/50.
- **Weight per game, not per event** (each game contributes equally), so games with many late events don't dominate.
- Ablation: retrain each model **without score diff** to show how much it leans on it.

## Prof feedback #2 — how models use features
- **Logistic regression:** standardize features (fit scaler on train), report coefficients ± bootstrap CI as a table/bar chart.
- **Gradient boosting:** gain-based importance + **permutation importance on val** (gain is biased toward high-cardinality features). Optional: SHAP summary plot.
- **LSTM / transformer:** feature-group ablation on val
  - Groups: score diff, time/period, event type, possession/team, fouls/timeouts, pregame Elo
  - Method A (cheap): permute that group's values *across games* in val, measure Δ log loss
  - Method B (stronger, if time): retrain without the group, measure Δ log loss
  - Also: Δ log loss vs. sequence length (20 / 35 / 50 events) to show whether history matters at all
- Compare importance rankings across all three models in one figure.

## Variations to try
- Sequence window length (20/35/50)
- With/without pregame Elo
- With/without score diff
- GBM depth / n_estimators; LSTM hidden size, dropout
- Stretch: transformer encoder vs LSTM

## Freeze checklist (before prospective test)
- [ ] Final weights saved to `models/frozen/`
- [ ] Config + git commit hash saved alongside
- [ ] Test-game pull script only fetches games after the freeze date
