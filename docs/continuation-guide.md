# Continuation Guide

This repo is designed so another engineer can continue the public-safe system without receiving private credentials or raw trading data.

## Where To Start

1. Read `README.md`.
2. Read `docs/architecture.md`.
3. Read `docs/risk-gates.md`.
4. Run the tests.
5. Extend `src/polymarket_decision_orchestrator.py` only through explicit contracts and tests.

## Recommended Next Build Order

| Step | Build | Why |
|---:|---|---|
| 1 | `src/contracts.py` data contracts | Make inputs explicit before adding adapters |
| 2 | Synthetic fixtures | Test behavior without private datasets |
| 3 | Market discovery interface | Keep discovery read-only |
| 4 | Archive interface | Separate capture from signal logic |
| 5 | Microstructure feature functions | Make fillability assumptions visible |
| 6 | Risk gate expansion | Prevent replay-only promotion |
| 7 | Human review artifact | Keep execution separate from research |

## Public-Safe Development Rule

Work from interfaces inward:

```text
contract -> synthetic fixture -> deterministic test -> implementation
```

Do not start from private logs, live clients, or a copied production module.

## Open Questions For A Future Private Build

These questions require private data and should not be answered in this public repo:

- Which exact strategy thresholds survived out-of-sample validation?
- Which markets had real fills versus implied-price movement only?
- Which VPS/runtime settings were used in production?
- Which wallet or counterparty behavior was analyzed?
- Which live orders, if any, affected real cash PnL?

