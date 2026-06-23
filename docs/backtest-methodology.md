# Backtest Methodology

This document captures the public-safe backtesting method from the private workspace.

## Principle

A backtest is only useful if it models the thing that would have been executable.

```text
price path != fill path
```

## Required Separations

Separate these concepts in every simulation:

- implied price
- last trade price
- best bid
- best ask
- actual fill evidence
- target/stop evaluation
- fees
- slippage
- stale data
- partial/missing book state
- resolution labels

## Minimum Honest Backtest Loop

```text
for each market epoch:
  load ordered events
  validate schema and freshness
  derive features only from data available at that timestamp
  evaluate candidate
  check fillability from executable book
  simulate bounded limit intent
  cancel stale intent if not filled
  manage only real/simulated fills
  close via target, stop, expiry, or resolution
  record cash-truth PnL
```

## Anti-Leakage Rules

- Do not use future resolution labels for entry decisions.
- Do not compute rolling features from future rows.
- Do not assume fills at implied price.
- Do not use the best price after the decision timestamp.
- Do not compare a polling bot to a tick-perfect hindsight fill.
- Do not mix dry-run assumptions with live execution assumptions.

## Metrics To Report

| Metric | Why it matters |
|---|---|
| Trades attempted | Shows opportunity frequency. |
| Trades filled | Separates signals from executable entries. |
| Fill rate | Measures whether the edge is reachable. |
| Win rate | Useful only after fillability is modeled. |
| Average PnL | More important than win rate alone. |
| Profit factor | Identifies asymmetric payoff. |
| Max drawdown | Capital survival. |
| Average duration | Operational feasibility. |
| Stale-data rejects | Dataset quality. |
| Unresolved/open count | Recovery and accounting health. |

## Dry-Run vs Live Diff

Always maintain a table comparing:

- fee model
- fill price
- slippage model
- order-book freshness
- latency
- cancel/replace behavior
- emergency exit behavior
- dashboard accounting

If dry-run skips freshness checks or assumes instant fills, its PnL is not promotion evidence.

## Promotion Rule

Backtest results can justify more research. They do not authorize live trading.

Promotion requires:

- validated data contract
- execution-aware simulation
- out-of-sample review
- cash-truth reconciliation
- risk gate
- human approval

