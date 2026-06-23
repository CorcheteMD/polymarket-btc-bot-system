---
name: clob-microstructure-analysis
description: Analiza microestructura CLOB: spreads, depth, imbalance, maker concentration, stale book, slippage, fill realism y wash-risk. Usar despues de tener archivo historico o muestras. No genera ordenes ni aprueba senales.
---

# CLOB Microstructure Analysis

## Mision

Separar edge real de artefactos de book, latencia, liquidez, spread, fill assumptions y datos mal interpretados.

## Inputs

- Archivo historico validado.
- Orderbook snapshots.
- Trades/replay/paper trades.
- Codigo: `analisis_orderbook_real.py`, `liquidity_auditor.py`, `exec_feasibility*.py`.

## Workflow

1. Validar fuente y granularidad.
2. Medir spread, depth, imbalance, stale rate y slippage.
3. Comparar backtest fill vs fill plausible.
4. Marcar sesgos: longshot, close-to-resolution, low-liquidity, stale book.
5. Entregar diagnosis microestructural.

## Output

- Microstructure scorecard.
- Riesgos de ejecucion.
- Ajustes recomendados para backtest/replay.
- Handoff a `signal-generation-anomaly` o `risk-management-gate`.

## Fuera De Scope

- No produce senal final.
- No decide sizing.
- No llama CLOB autenticado.

