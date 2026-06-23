---
name: quality-evidence-mapper
description: Mapeador de evidencia para auditorias universales de calidad. Usar despues de `quality-rubric-builder` para vincular artefactos, logs, metricas, muestras, documentos y referencias con cada criterio de la rubrica, declarar calidad de evidencia y marcar gaps. No puntua calidad, no diagnostica causas y no propone mejoras.
---

# Quality Evidence Mapper

## Mision

Construir la matriz de evidencia que permite puntuar sin improvisar. Esta skill responde: que evidencia existe, que criterio cubre, que tan confiable es y que falta.

## Inputs

- Rubrica de `quality-rubric-builder`.
- Contexto de `quality-context-reader`.
- Artefactos disponibles.
- Referencias de dominio, benchmarks o fuentes.

## Workflow

1. **Listar artefactos**
   - Nombre.
   - Tipo.
   - Fecha/version si existe.
   - Fuente.
   - Relacion con el objeto auditado.

2. **Mapear evidencia por criterio**
   - Cada criterio debe tener evidencia directa, indirecta, faltante o no aplicable.
   - Si una evidencia sirve para varias dimensiones, repetirla con nota de uso.
   - Si no hay evidencia, marcar `FALTANTE`.

3. **Calificar confianza de evidencia**
   - Alta: directa, verificable, actual, suficiente y trazable.
   - Media: parcial, indirecta, muestra pequena o sin trazabilidad completa.
   - Baja: anecdota, opinion, output aislado, supuesto o fuente no verificable.
   - Faltante: necesaria pero ausente.

4. **Declarar gaps criticos**
   - Gaps que impiden score.
   - Gaps que permiten score con baja confianza.
   - Gaps que exigen gate humano.

## Output

```markdown
## Matriz De Evidencia

| Dimension | Criterio | Evidencia | Tipo | Fuente/artefacto | Calidad | Estado | Nota |
|---|---|---|---|---|---|---|---|
| ... | ... | ... | directa/indirecta/faltante | ... | alta/media/baja/faltante | disponible/faltante/N-E | ... |

## Cobertura

- Criterios cubiertos:
- Criterios con evidencia parcial:
- Criterios sin evidencia:
- Dimensiones no evaluables:
- Confianza global de evidencia: alta/media/baja

## Gaps Criticos

1. ...
```

## Reglas Duras

- No puntuar la calidad del sistema.
- No convertir evidencia faltante en score cero salvo que la rubrica lo diga.
- No tratar opiniones como evidencia directa.
- No usar evidencia fuera de fecha sin marcarlo.
- No ocultar que una dimension clave no es evaluable.
