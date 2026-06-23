# Sanitized System Map

This map captures the public-safe shape of the private BTC/Polymarket bot workspace. It is intentionally descriptive, not operational: no hosts, process IDs, credentials, private config values, or live commands are included.

## Runtime Shape

```text
Polymarket Gamma / CLOB / WebSocket
  -> market discovery
  -> active-market scanner
  -> dry-run evaluator
  -> signal and microstructure features
  -> risk gate
  -> trade lifecycle manager
  -> operator dashboard
```

The private system also had a live execution path. That path is excluded from this public repository because safe publication should show the design discipline without exposing runnable trading code.

## Module Responsibilities

| Module family | Public responsibility |
|---|---|
| Market scanner | Finds active BTC markets, filters stale/future markets, deduplicates condition IDs. |
| WebSocket/feed layer | Collects price and order-book observations for downstream research. |
| Signal layer | Produces market context and rejects neutral or stale conditions. |
| Dry-run engine | Evaluates candidates without placing orders and records outcomes. |
| Microstructure layer | Separates implied price from executable bid/ask reality. |
| Risk gate | Blocks promotion when evidence, cash truth, or runtime safety is incomplete. |
| Trade lifecycle manager | Owns open/closed trade state, idempotent closes, restart recovery, and stats. |
| Dashboard/operator layer | Reads state and reports it; it should not own trade truth. |

## Single Sources Of Truth

| Truth | Owner |
|---|---|
| Open/closed trade state | Trade lifecycle manager |
| Market candidate evidence | Evidence artifact / research tape |
| Runtime safety state | Risk and safety gate |
| Market-data schema | Data contract |
| Operator-facing stats | Read model derived from trade lifecycle state |

The original workspace showed why this matters: once CSV files, dashboards, runtime memory, and ledgers all become partial truth sources, the bot can look healthy while important state is missing.

## Shared-State Rules

- Timeframe must be explicit at module boundaries.
- A signal module must not place orders.
- A dashboard must not infer trade truth from an incomplete export.
- Closing a trade must always release exposure and deduplication locks.
- Restart recovery must rebuild active monitors from persisted open state.
- Live execution must be downstream of evidence, risk, and human review.

