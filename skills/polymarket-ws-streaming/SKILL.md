---
name: polymarket-ws-streaming
description: Disena y audita ingesta WebSocket de Polymarket en modo read-only. Usar para book, price_change, best_bid_ask, heartbeat, reconnect, gaps, latencia y normalizacion de eventos. No almacena historico definitivo, no infiere direccion de trade y no ejecuta ordenes.
---

# Polymarket WS Streaming

## Mision

Mantener una lectura estable y auditable de eventos WebSocket sin mezclar feed, storage, analisis y ejecucion.

## Inputs

- Asset IDs / token IDs.
- Canal: market, user, sports o RTDS.
- Codigo local: `core/ws_feed.py`, `collector_v5/ws/client.py`, `btc_data_collector_v3.py`.
- Logs o muestras de eventos.

## Workflow

1. Revisar canal y payload esperado.
2. Verificar heartbeat, reconnect, backoff y deduplicacion.
3. Normalizar eventos sin cambiar semantica.
4. Medir gaps, stale data y latencia observable.
5. Entregar contrato de evento para archivo o analisis.

## Regla Critica

`change_side` no debe usarse como verdad de aggressor side. Para metricas direction-dependent, pasar a `clob-microstructure-analysis` con join on-chain.

## Output

- Event contract.
- Riesgos de stale/gap.
- Checklist de reconnect.
- Handoff a `polymarket-historical-archive`.

## Fuera De Scope

- No escribe ordenes.
- No decide entradas.
- No calcula PnL.
- No toca credenciales.

