---
name: hb-live-cash-truth-pnl
description: Use when converting HB live, paper, shadow, ledger, Polymarket Data API, fills, fees, outcomes, and no-fills into honest cash-truth PnL.
---

# HB Live Cash Truth PnL

Mission: measure money, not vibes.

## Inputs

- context events
- ledger rows
- Polymarket/Data API activity
- fills/effective prices/sizes
- fees/tax model
- outcomes and redeem/settlement status

## Rules

- Ledger/API activity wins over context when measuring real money.
- Shadow rows are never real fills.
- Blocked rows are never PnL.
- Limit cap is not fill price.
- Direct shadow price is observed signal ask, not stale `limit_price=1.0`.
- Keep unresolved separate.

## Output

Per-trade and aggregate:

- `paper_expected`
- `live_effective`
- `cash_truth_delta`
- `realized_pnl`
- `unresolved`
- `promotion_blockers`
