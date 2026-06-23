# Forensic Audit Playbook

This playbook preserves the audit method from the private workspace without publishing private code paths, hosts, process IDs, or strategy thresholds.

## Audit Goal

Find the bugs that make a trading bot look alive while silently losing money, lying about performance, or skipping the very trades it was built to evaluate.

## Severity Ladder

| Level | Meaning |
|---|---|
| Level 1 | Guaranteed financial loss if path is reached. |
| Level 2 | Probable financial loss under normal stress. |
| Level 3 | Invalid data or misleading metrics. |
| Level 4 | Silent failure. |
| Level 5 | Delayed failure / restart / recovery hazard. |
| Level 6+ | Inefficiency, maintainability, or cosmetic debt. |

## Audit Phases

1. **Map state owners.** Identify who owns trades, open exposure, market candidates, dashboard stats, and runtime locks.
2. **Trace money paths.** Follow entry, fill, exit, cancel, failover, expiration, and post-resolution behavior.
3. **Compare dry-run vs live assumptions.** Look for different fee, freshness, slippage, fill, timing, and exit logic.
4. **Attack dashboards.** Verify that reported wins, losses, unresolved positions, and PnL come from the same canonical truth.
5. **Search for shared mutable state.** Every shared dict/list/cache needs an owner, lock, and cleanup protocol.
6. **Run devil's advocate last.** Ask which upstream assumption could make all tactical fixes irrelevant.

## Questions That Found The Most Value

- Does dry-run use the same executable price as live execution?
- Does any path confuse implied price with executable bid/ask?
- Can a cancel succeed while the replacement order fails?
- Does a restart leave open positions without monitors?
- Does the dashboard count every terminal state?
- Can two modules write the same trade state?
- Can an old signal suppress a valid opportunity later in the epoch?
- Does a missing timestamp bypass freshness checks?

## Public Regression Targets

Turn each audit finding into one of these tests:

- `test_implied_price_is_not_executable`
- `test_close_trade_is_idempotent`
- `test_dashboard_uses_trade_manager`
- `test_recovery_marks_open_trades`
- `test_stale_book_blocks_cross_side_features`
- `test_missing_required_dataset_fields_fail_validation`
- `test_dry_run_requires_fillability_evidence`

## Red Flags

- "CSV is the source of truth."
- "Dashboard parses whatever file exists."
- "Live and dry-run are almost the same."
- "This dict is only used in two places."
- "If the API fails, we notify the operator and return."
- "The price moved there, so we could have filled there."

