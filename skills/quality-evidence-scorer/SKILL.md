---
name: quality-evidence-scorer
description: Scorer de evidencia para auditorias universales de calidad. Usar cuando ya existen rubrica y matriz de evidencia para aplicar criterios, calcular score ponderado, declarar confianza, dimensiones no evaluables y veredicto preliminar. No crea rubricas, no busca causas raiz, no hace red team y no propone mejoras.
---

# Quality Evidence Scorer

## Mision

Aplicar la rubrica congelada sobre la evidencia mapeada. Esta skill produce el scorecard preliminar y declara cuanta confianza merece.

## Inputs

- Rubrica de `quality-rubric-builder`.
- Matriz de evidencia de `quality-evidence-mapper`.
- Contexto de riesgo.

## Workflow

1. **Verificar prerequisitos**
   - Rubrica existe.
   - Pesos suman 1.0 o 100%.
   - Evidencia esta mapeada por criterio.
   - Criterios criticos tienen evidencia o estan marcados como no evaluables.

2. **Aplicar escala**
   - Puntuar 0-4 segun indicadores de la rubrica.
   - Usar `N/E` cuando falta evidencia.
   - No usar juicio libre fuera de la rubrica.

3. **Calcular score**
   - Score ponderado por dimension.
   - Score global solo si hay suficiente cobertura.
   - Si falta una dimension critica, el veredicto maximo permitido baja.

4. **Declarar confianza**
   - Alta: evidencia suficiente en dimensiones criticas.
   - Media: algunos gaps no criticos.
   - Baja: gaps relevantes, muestra pequena o inferencia excesiva.
   - No evaluable: falta base minima.

## Output

```markdown
## Scorecard Preliminar

- Caso:
- Riesgo:
- Confianza del score: alta/media/baja/no evaluable
- Score global:
- Veredicto preliminar:

| Dimension | Peso | Puntaje | Score ponderado | Evidencia usada | Confianza | Nota |
|---|---:|---:|---:|---|---|---|
| ... | ... | ... | ... | ... | ... | ... |

## Dimensiones No Evaluables

| Dimension | Motivo | Evidencia faltante |
|---|---|---|

## Limites Del Score

- ...
```

## Reglas Duras

- No crear nuevos criterios durante el scoring.
- No proponer soluciones.
- No diagnosticar causa raiz.
- No emitir `APROBADO` si hay dimension critica `N/E`.
- No emitir confianza alta con evidencia media o baja en criterios criticos.
- Si el scorer produjo el output auditado, declarar riesgo de self-judge bias.
