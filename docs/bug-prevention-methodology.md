# Bug Prevention Methodology

This is the public-safe development discipline extracted from the private bot audits.

## Rule 1: Explicit Data Ownership

Before writing any persistent or shared data, answer:

```text
Who is the canonical owner of this data?
```

If the answer is not obvious, stop and fix the design first.

Examples:

- Trades belong to the Trade Manager.
- Signal state belongs to the signal module.
- Runtime exposure belongs to the safety/risk state.
- Dashboard stats are read models, not write targets.

## Rule 2: Contracts At Module Boundaries

Any function crossing module boundaries should have:

- type hints
- a docstring describing guarantees
- explicit validation for critical inputs
- tests for invalid inputs

Boundary functions should fail loudly before side effects.

## Rule 3: One Writer Per Data Source

If two modules need to write the same file, table, or state object, create a single owner module. Do not let two modules coordinate by convention.

Bad:

```text
dry-run writes trades
live runner writes trades
dashboard infers trades
ledger partially writes trades
```

Better:

```text
all paths call TradeManager
exports are generated views
dashboard reads TradeManager stats
```

## Rule 4: Shared State Requires Owner, Lock, Cleanup

Every mutable object shared across threads/processes needs:

- owner
- lock or concurrency protocol
- cleanup rule
- recovery rule
- test coverage

## Rule 5: Every Code Change Needs A Test

If a change affects trade lifecycle, data contracts, fillability, risk gates, or dashboard stats, add a regression test before promotion.

## Rule 6: Observability Is Designed, Not Patched Later

Lifecycle events should be structured from the beginning:

- `TRADE_ENTERED`
- `TRADE_CLOSED`
- `TRADE_SKIPPED`
- `ORDER_INTENT_CREATED`
- `ORDER_INTENT_CANCELLED`
- `RECOVERY`
- `RISK_BLOCKED`
- `DATA_STALE`
- `ERROR`

The event should include enough context to debug without exposing secrets.

## Pre-Code Checklist

- Who owns this data?
- Is the boundary typed and validated?
- Is there exactly one writer?
- Does shared state have lock and cleanup?
- Is there a regression test?
- Will the dashboard read canonical truth?
- Will failure be visible?

