"""Event table -> fixed-length sequences for the LSTM/transformer.  (David)

For each event t in a game, the input is the last `models.lstm.seq_len` events up to and
including t (left-padded + mask at game start); target is home_win.

Rules:
- Windows NEVER cross game boundaries.
- Categorical encoders (event_type, team_side) and numeric scalers fit on TRAIN seasons only.
- Keep feature groups addressable (score, time, event, possession, fouls/timeouts, elo)
  so eval/interpretability.py can permute one group at a time.
"""

# TODO(David): implement
