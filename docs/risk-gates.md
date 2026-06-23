# Risk Gates

The source bot used a strict operating rule: read-only first, dry-run before live, and human approval before any action that can move capital.

## Gate Contract

Every decision artifact should include:

- `decision`
- `confidence`
- `blocking_gates`
- `evidence_layer`
- `next_action`
- `do_not_do`

## Evidence Layers

| Evidence layer | Meaning |
|---|---|
| `REPLAY_ONLY` | Historical replay only; never enough for live promotion |
| `SHADOW_WOULD_BUY` | Candidate would have entered, but no real fill confirmed |
| `LIVE_NO_FILL` | Runtime observed, but fills are not proven |
| `LIVE_FILL` | Real fill evidence exists |
| `CASH_TRUTH` | Real cash/ledger truth reconciled |

## Blocking Examples

- Missing heartbeat or stale runtime evidence.
- Replay, shadow, live, and cash-truth disagree.
- Fillability-adjusted PnL is not positive.
- Candidate depends on stale limit assumptions.
- Kill switch is active.
- Human approval is missing.

## Rule

`PROMOTE_REVIEW` means review-ready. It does not mean "trade live automatically."

