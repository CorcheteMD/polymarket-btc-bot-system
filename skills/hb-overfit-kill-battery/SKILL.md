---
name: hb-overfit-kill-battery
description: Use when testing HB replay or shadow strategy candidates for overfit, threshold fragility, small-N, temporal dependence, and remove-best failure before promotion.
---

# HB Overfit Kill Battery

Mission: kill pretty candidates before they touch live.

## Inputs

- strategy_id, rule_text, rule_hash
- replay/shadow trades
- market_id and time block identifiers
- costs, stake, entry price model

## Required Checks

- resolved trades >= 30 for normal candidates
- cash-truth estimated PnL > 0
- max loss streak <= 7
- remove-best-trade PnL > 0
- remove-best-market PnL > 0 when market grouping exists
- at least 3 of 4 time blocks positive
- threshold sensitivity has a stable neighborhood

## Output

`SCOUT`, `LOW_N_SCOUT`, `KILL_OVERFIT`, `KILL_SMALL_N`, or `BLOCKED_MISSING_TRUTH`.

Never rescue a candidate by changing more than one primary dimension after seeing forward results.
