---
name: polymarket-system-orchestrator
description: Orquesta el sistema local de skills para el bot BTC/Polymarket. Usar cuando se quiera decidir que skill activar, en que orden, con que gates y que evidencia pedir antes de tocar datos, senales, riesgo o ejecucion. No investiga mercados, no genera senales y no ejecuta ordenes.
---

# Polymarket System Orchestrator

## Mision

Convertir una peticion del operador en una ruta segura de skills para el bot de trading. Esta skill decide capas, handoffs y gates; no ejecuta el trabajo de dominio.

## Principios

1. Read-only primero. Toda mejora nueva empieza sin trading real.
2. Separacion estricta. Discovery, streaming, archivo, analisis, research, senales, riesgo y ejecucion no se mezclan.
3. R3 por defecto. Cualquier cambio que pueda mover capital, credenciales, ordenes, VPS o reputacion requiere gate humano.
4. No tocar `.env`, claves, wallet, API secrets ni VPS sin solicitud explicita.
5. Una orden real solo puede venir de `order-execution-compliance` y solo si existe aprobacion de `risk-management-gate`.

## Intake

Clasifica la peticion:

- `OBSERVE`: descubrir mercados, leer orderbook, revisar datos.
- `DIAGNOSE`: investigar bug, gap de datos, calidad de senal.
- `RESEARCH`: tesis de mercado, fuentes, forecast humano/LLM.
- `BACKTEST`: replay, calibracion, OOS, PBO.
- `SIGNAL`: edge candidato, anomaly detection, decision doc.
- `RISK`: sizing, drawdown, limites, kill switch.
- `EXECUTION`: orden, cancelacion, heartbeat, audit log.

## Ruta Recomendada

| Caso | Ruta |
|---|---|
| Quiero listar mercados | `polymarket-market-discovery` |
| Quiero leer book/WS | `polymarket-ws-streaming` |
| Quiero dataset o replay | `polymarket-historical-archive` -> `clob-microstructure-analysis` |
| Quiero saber si una tesis tiene edge | `market-research-intelligence` -> `forecast-calibration-engine` -> `signal-generation-anomaly` |
| Quiero pasar de senal a accion | `signal-generation-anomaly` -> `risk-management-gate` -> gate humano |
| Quiero ejecutar/cancelar | `order-execution-compliance` solo con aprobacion estructurada |

## Output

Entrega siempre:

- Clasificacion de la peticion.
- Skill primaria.
- Skills secundarias.
- Handoff esperado.
- Evidencia minima.
- Gate requerido.
- Accion prohibida en esta corrida.

