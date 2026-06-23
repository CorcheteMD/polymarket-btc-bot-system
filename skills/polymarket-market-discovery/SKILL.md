---
name: polymarket-market-discovery
description: Descubre y filtra mercados Polymarket en modo read-only usando Gamma/Data/CLOB publicos. Usar para listar mercados activos, encontrar BTC/ETH/SOL/XRP 5m/15m, mapear condition_id/token_id, tags, liquidez, volumen y fechas. No usa auth, no genera senales y no ejecuta trading.
---

# Polymarket Market Discovery

## Mision

Construir un catalogo verificable de mercados Polymarket relevantes para el bot, especialmente mercados binarios crypto Up/Down.

## Inputs

- Asset: BTC, ETH, SOL, XRP u otro.
- Timeframe: 5m, 15m u otro.
- Filtros: activo/cerrado, liquidez minima, volumen, fecha, tag, slug.
- Codigo local opcional: `market/market_scanner.py`, `core/clob_client.py`, `seen_conditions.json`.

## Workflow

1. Declarar filtros y alcance.
2. Consultar metadata publica o revisar codigo/local data disponible.
3. Distinguir `condition_id`, outcome token IDs, slug, close time y timeframe.
4. Marcar cobertura incompleta entre Gamma y CLOB si aparece mismatch.
5. Entregar tabla de mercados y gaps de datos.

## Output

- Tabla de mercados candidatos.
- IDs requeridos por downstream.
- Fuente usada: Gamma, Data, CLOB publico o archivo local.
- Riesgos de mapping.
- Handoff a `polymarket-ws-streaming` o `polymarket-historical-archive`.

## Fuera De Scope

- No calcula edge.
- No decide direccion.
- No usa endpoints autenticados.
- No modifica `seen_conditions.json` salvo peticion explicita y plan aprobado.

