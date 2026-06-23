# Testing Strategy

The private workspace contained a broad set of tests around collectors, heartbeat behavior, fair-value logic, profitability review, schema contracts, and live-safety promotion. This public repository preserves the testing philosophy without publishing private datasets or edge parameters.

## Test Layers

| Layer | Goal |
|---|---|
| Contract tests | Freeze schema expectations for ticks, features, fillability, and decisions. |
| Fixture tests | Use small synthetic market snapshots that can be reviewed by humans. |
| Lifecycle tests | Prove idempotent close, restart recovery, and terminal state behavior. |
| Gate tests | Confirm missing evidence blocks promotion. |
| Microstructure tests | Prove implied price is never treated as executable ask. |
| Regression tests | Encode previously found audit failures as deterministic checks. |

## Synthetic First

Public tests should prefer synthetic fixtures because they are:

- small enough to inspect
- safe to publish
- deterministic
- free of wallet/user data
- easy for contributors to modify

Raw datasets, logs, ledgers, private wallet studies, and model artifacts belong outside this repo.

## Minimum Bar For A New Feature

Every new public feature should include:

1. A contract or dataclass update.
2. A small fixture.
3. A deterministic unit test.
4. A note in the relevant doc explaining the invariant it protects.

## Promotion Gate

Passing tests do not authorize live trading. They only prove that the public scaffold behaves consistently. Promotion to live systems requires private operational review, cash truth, risk review, and human approval.

