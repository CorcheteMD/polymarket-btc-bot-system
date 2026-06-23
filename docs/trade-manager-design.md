# Trade Manager Design

The private audit converged on one central architectural need: trade lifecycle state needs a single owner.

## Purpose

The Trade Manager should own:

- open trade creation
- close idempotency
- exposure release
- restart recovery
- dashboard statistics
- export/read-model generation

It should not own:

- signal generation
- market discovery
- private-key handling
- live order placement
- Telegram command parsing

## State Machine

```text
PENDING
  -> OPEN
  -> CLOSING
  -> CLOSED
  -> RECOVERED_OPEN
```

`CLOSED` is terminal. A second close request should return the existing closed record rather than double-counting PnL or releasing exposure twice.

## Recovery Contract

On startup:

1. Acquire a single-instance lock.
2. Load persisted trades whose state is not terminal.
3. Rebuild monitoring intent for each active trade.
4. Rebuild deduplication state from persisted open trades.
5. Emit a structured recovery report.

## Integration Order

1. Add Trade Manager as a standalone module with tests.
2. Route dry-run writes through it.
3. Route dashboard stats through it.
4. Add restart recovery.
5. Only then consider live execution integration.

## Invariants

- A trade can be opened once per unique market/outcome intent.
- A trade can be closed many times safely, but only the first close mutates state.
- Closing a trade always releases exposure.
- Dashboard numbers are derived from the trade owner, not from an incidental CSV.
- Export files are views, not sources of truth.

