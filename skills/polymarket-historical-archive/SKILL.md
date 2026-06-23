---
name: polymarket-historical-archive
description: Disena archivo historico reproducible para ticks, orderbook, trades, outcomes y joins on-chain. Usar para CSV/Parquet, replay, schemas, snapshots, calidad de datos, reorg buffer y lineage. No genera senales ni decide trading.
---

# Polymarket Historical Archive

## Mision

Convertir datos crudos del bot en datasets reproducibles para backtest, replay y auditoria.

## Inputs

- CSVs: `btc_ticks_*`, `btc_market_summary_*`, `all_ticks_*`, `live_ledger_*`.
- Codigo: `scripts/build_epoch_chain.py`, `scripts/wfo_backtest_engine.py`, `core/persistence.py`.
- Reportes en `vault/data` y `vault/research`.

## Workflow

1. Inventariar fuentes, escritor y lector.
2. Declarar schema canonico por dataset.
3. Separar raw, normalized, enriched y derived.
4. Definir checks: timestamps, duplicate IDs, missing close, stale book, impossible price.
5. Proponer archivo incremental y reproducible.

## Output

- Data lineage.
- Schema canonico.
- Checks de calidad.
- Handoff a `clob-microstructure-analysis` o `forecast-calibration-engine`.

## Fuera De Scope

- No optimiza estrategia.
- No promueve variantes.
- No modifica archivos grandes sin plan de migracion.

