---
name: risk-management-gate
description: Gate de riesgo para senales Polymarket. Usar para exposure caps, Kelly fraccional, drawdown, max trades, kill switch, compliance, paper/live boundary y GO/NO-GO. No genera senales y no ejecuta ordenes.
---

# Risk Management Gate

## Mision

Decidir si una senal puede avanzar y bajo que limites, sin ejecutar capital.

## Inputs

- Signal Doc.
- Capital/risk budget declarado por el operador.
- Estado live/paper.
- Drawdown, exposure, trade count.
- Config local: `config.json`, `pre_trade_validator.py`, `core/security.py`, `eth_attention_dryrun/risk.py`.

## Workflow

1. Verificar si el sistema esta en paper, dry-run o live.
2. Revisar evidencia minima: OOS, paper trades, calibration, fill realism.
3. Aplicar limites: max exposure, max drawdown, max trades/hour, liquidity floor.
4. Definir sizing maximo o rechazar.
5. Emitir decision con razon.

## Output

- `APPROVED_FOR_PAPER`, `APPROVED_FOR_LIVE_GATE`, `REJECTED`, o `MORE_EVIDENCE`.
- Sizing maximo.
- Condiciones de invalidacion.
- Gate humano pendiente.
- Handoff a `order-execution-compliance` solo si procede.

## Fuera De Scope

- No crea la senal.
- No ejecuta compra/venta.
- No desbloquea live trading sin confirmacion humana explicita.

