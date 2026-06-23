# Architecture

This public architecture is derived from a private BTC/Polymarket bot workspace and redacted for publication.

## Layers

| Layer | Responsibility | Public-safe signal |
|---|---|---|
| Market discovery | Find active prediction markets and normalize identifiers | Demonstrates API/workflow design |
| Streaming archive | Capture order book and price events | Demonstrates data engineering |
| Microstructure analysis | Estimate spreads, depth, fillability, slippage, and timing | Demonstrates quantitative rigor |
| Forecast calibration | Compare signal candidates against out-of-sample evidence | Demonstrates research discipline |
| Risk gate | Decide whether a candidate is blocked, killed, held, scouted, or review-ready | Demonstrates safety |
| Execution compliance | Only execute after risk approval and explicit human approval | Demonstrates governance |

## Design Principle

No layer gets to be judge, jury, and executioner. A signal generator can propose a candidate, but it cannot promote itself to live execution. A risk gate can approve review, but it cannot place orders. Execution requires a separate compliance path and human approval.

## Data Flow

```text
Polymarket / external market data
  -> collector
  -> archive
  -> feature builder
  -> replay and shadow evaluation
  -> cash-truth reconciliation
  -> risk gate
  -> human review
```

## Private Components Excluded

- Live CLOB client configuration.
- VPS deployment details.
- Credentials and wallet materials.
- Raw datasets, logs, ledgers, model artifacts, and strategy thresholds.
- Any code path that can submit or cancel an order.

