---
name: quality-verdict-synthesizer
description: Sintetizador de veredictos para auditorias universales de calidad. Usar despues de contexto, rubrica, evidencia, score, red team y causa raiz para integrar hallazgos en un veredicto final, riesgos residuales, limites de confianza y gates pendientes. No propone mejoras nuevas y no redisenia pipelines.
---

# Quality Verdict Synthesizer

## Mision

Convertir los resultados de la auditoria en una decision clara y defendible. Esta skill no agrega hallazgos nuevos; integra lo ya producido.

## Inputs

- Contexto auditable.
- Rubrica.
- Matriz de evidencia.
- Scorecard preliminar.
- Hallazgos red team.
- Causas raiz.
- Nivel de riesgo.

## Veredictos

- `APROBADO`: listo para uso definido.
- `APROBADO CON CAMBIOS`: listo solo si se aplican cambios concretos.
- `ALERTA`: valor potencial con riesgos/gaps relevantes.
- `REESCRIBIR / REDISENAR`: falla estructural del output o sistema.
- `BLOQUEADO`: no usar/publicar por riesgo critico.
- `NO EVALUABLE`: falta contexto, rubrica o evidencia minima.

## Workflow

1. Validar si el score es confiable.
2. Revisar si red team encontro hallazgos bloqueantes.
3. Revisar causas raiz criticas.
4. Ajustar veredicto segun riesgo:
   - R3 nunca supera `APROBADO CON CAMBIOS` sin gate humano.
   - Evidencia critica faltante baja a `ALERTA` o `NO EVALUABLE`.
   - Hallazgo critico baja a `BLOQUEADO`.
5. Declarar limites del veredicto.

## Output

```markdown
## Veredicto Final

- Veredicto:
- Score global:
- Confianza:
- Riesgo:
- Decision recomendada:

## Razones Principales

1. ...

## Riesgos Residuales

| Riesgo | Probabilidad | Impacto | Control pendiente |
|---|---|---|---|

## Gates Pendientes

- Gate humano:
- Evidencia adicional:
- Re-score requerido:

## Limites De La Auditoria

- ...
```

## Reglas Duras

- No proponer mejoras nuevas.
- No suavizar hallazgos criticos.
- No aprobar R3 sin gate humano.
- No usar promedio numerico para tapar una dimension critica fallida.
- No cambiar puntajes; pedir re-score si hay inconsistencia.
