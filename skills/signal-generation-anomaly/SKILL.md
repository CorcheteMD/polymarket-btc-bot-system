---
name: signal-generation-anomaly
description: Combina research, calibracion y microestructura para producir un Signal Doc con edge, incertidumbre, anomalias y criterios de invalidacion. Usar solo despues de datos/research suficientes. No ejecuta, no aprueba y no ajusta riesgo.
---

# Signal Generation Anomaly

## Mision

Crear una propuesta de senal auditable, falsable y separada de ejecucion.

## Inputs

- Dossier de `market-research-intelligence`.
- Calibration report.
- Microstructure scorecard.
- Datos locales del bot.
- Estrategia candidata.

## Workflow

1. Declarar hipotesis.
2. Calcular edge estimado y rango de confianza.
3. Evaluar anomalias y fallos de datos.
4. Definir invalidation criteria.
5. Emitir Signal Doc para risk review.

## Output

- Signal Doc.
- Edge estimado.
- Confidence level.
- Evidence links.
- PBO/overfit flag.
- Handoff obligatorio a `risk-management-gate`.

## Fuera De Scope

- No hace sizing final.
- No cambia `config.json`.
- No llama `order-execution-compliance`.

