---
name: hb-promotion-war-room
description: Use as the final pre-live HB promotion gate. It combines dataset, overfit, shadow, latency, cash-truth, risk, and open incident verdicts before any real order change.
---

# HB Promotion War Room

Mission: decide if a candidate may be proposed for micro-live.

## Inputs

- dataset verdict
- replay/overfit battery
- forward shadow report
- cash-truth PnL report
- latency/no-fill report
- bankroll and risk limits
- open incidents

## Decisions

- `PROMOTE_MICRO_REVIEW`: ready for explicit human approval.
- `HOLD`: promising but missing evidence.
- `KILL`: failed a hard gate.
- `BLOCKED`: truth/runtime unavailable.

## Non-Negotiables

- No automatic halt lift.
- No automatic stake increase.
- No automatic real-orders enable.
- Require rollback checklist, stake cap, kill switch, and live-paper parallel plan.
