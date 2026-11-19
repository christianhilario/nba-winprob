"""How models use features (prof feedback).  (Both)

- LR: standardized coefficients (+ bootstrap CI)
- GBM: gain importance + permutation importance on val
- LSTM/transformer: permute one feature GROUP across games on val -> Δ log loss
  (optional: retrain without the group)
- One combined figure ranking feature groups across all models -> reports/figures/

Note: sklearn.inspection.permutation_importance works for LR/GBM; for the LSTM you'll need
your own loop since inputs are 3D (batch, seq, features).
"""

# TODO(both): implement
