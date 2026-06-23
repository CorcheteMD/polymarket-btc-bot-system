---
name: shadow-informativeness-auditor
description: Use when deciding whether a Polymarket HB shadow challenger adds information beyond the baseline or is a clone, redundant variant, or noisy overfit.
---

# Shadow Informativeness Auditor

Mission: keep only shadows that teach us something.

## Inputs

- baseline strategy rows
- challenger strategy rows
- strategy_id, rule_hash, timestamps, market_id, side
- outcomes and estimated PnL

## Checks

- Jaccard overlap by market_id + side
- unique wins and unique losses
- marginal PnL vs baseline
- max loss streak and drawdown
- blocked/unresolved dependence
- rule difference is one primary dimension unless marked interaction test

## Output

`KEEP`, `KILL_CLONE`, `KILL_WORSE`, `EXTEND_SAMPLE`, or `PROMOTE_REVIEW_INPUT`.
