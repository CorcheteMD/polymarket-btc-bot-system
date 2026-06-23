---
name: order-execution-compliance
description: Skill bloqueante para ejecutar o auditar ordenes Polymarket solo cuando existe aprobacion estructurada de risk-management-gate y confirmacion humana. Usar para revisar placement, cancel, heartbeat, audit log, auth L1/L2 y receipt. No genera senales ni decide riesgo.
---

# Order Execution Compliance

## Mision

Ejecutar o auditar una accion de orden solo si existe aprobacion previa, limites claros y audit log.

## Requisitos De Entrada

- Decision `APPROVED_FOR_LIVE_GATE` o `APPROVED_FOR_PAPER` de `risk-management-gate`.
- Confirmacion humana explicita si mueve capital real.
- Market/token IDs.
- Side, price, size, order type, expiry.
- Motivo de la orden y condiciones de cancelacion.

## Workflow

1. Verificar que la orden no nace de esta skill.
2. Verificar limites y aprobacion.
3. Revisar auth boundary: no imprimir secrets, no exponer private key.
4. Preparar accion o auditoria de ejecucion.
5. Registrar receipt y resultado.

## Output

- Execution readiness.
- Order receipt o audit finding.
- Log fields requeridos.
- Errores y fallback.

## Fuera De Scope

- No genera edge.
- No hace market research.
- No ajusta risk.
- No opera sin gate humano en live.

