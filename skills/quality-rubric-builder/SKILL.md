---
name: quality-rubric-builder
description: Constructor de rubricas adaptativas para auditorias universales de calidad. Usar cuando ya existe contexto estructurado y se necesita definir dimensiones, criterios, pesos, umbrales, evidencia requerida e indicadores antes de puntuar un sistema, skill, pipeline, proceso u output. No aplica la rubrica, no puntua y no propone mejoras.
---

# Quality Rubric Builder

## Mision

Construir el instrumento de medicion del caso. La rubrica adapta dimensiones universales a un dominio y objetivo concretos sin convertir la skill en experta fija de ese dominio.

## Inputs

- Output de `quality-context-reader`.
- Referencias externas de dominio, si existen.
- Nivel de riesgo.
- Decision buscada: aprobar, comparar, diagnosticar, redisenar o mejorar.

## Referencias

Si estan disponibles, leer desde `../universal-quality-orchestrator/references/`:

- `universal-quality-dimensions.md`
- `evidence-confidence-model.md`
- `risk-levels-and-human-gates.md`

## Workflow

1. **Elegir dimensiones relevantes**
   - Partir de dimensiones universales: adecuacion funcional, fiabilidad, veracidad, relevancia, seguridad, usabilidad, mantenibilidad, portabilidad, transparencia, supervisabilidad, evidencia y riesgo.
   - Eliminar dimensiones irrelevantes solo con razon explicita.
   - Agregar dimensiones de dominio solo si hay referencia o contexto que las justifique.

2. **Definir criterios observables**
   - Cada criterio debe poder evaluarse con evidencia.
   - Evitar criterios vagos como "bueno", "premium", "robusto" sin indicador.
   - Incluir indicadores negativos cuando una metrica pueda ser jugada.

3. **Asignar pesos**
   - La suma debe ser 1.0 o 100%.
   - R3 debe dar peso alto a seguridad, evidencia, supervisabilidad y riesgo.
   - No sobreponderar estetica, estilo o facilidad si el objetivo real es seguridad, exactitud o decision.

4. **Definir escala**
   - Default 0-4:
     - 0 = ausente/no cumple.
     - 1 = insuficiente.
     - 2 = parcial.
     - 3 = adecuado.
     - 4 = excelente.
   - `N/E` se usa cuando falta evidencia, no como cero automatico.

5. **Definir evidencia requerida**
   - Para cada criterio, indicar que evidencia cuenta.
   - Separar evidencia directa, indirecta y faltante.

## Output

```markdown
## Rubrica De Auditoria

- Caso:
- Objeto auditado:
- Decision buscada:
- Riesgo:
- Escala:
- Umbrales:

| Dimension | Peso | Criterio | Evidencia requerida | 0 | 1 | 2 | 3 | 4 |
|---|---:|---|---|---|---|---|---|---|
| ... | ... | ... | ... | ... | ... | ... | ... | ... |

## Dimensiones Excluidas

| Dimension | Motivo |
|---|---|

## Riesgos De La Rubrica

- Criterios potencialmente manipulables:
- Evidencia critica faltante:
- Supuestos:
```

## Reglas Duras

- No puntuar.
- No inventar normas de dominio.
- No usar pesos que no sumen 1.0.
- No permitir una rubrica sin evidencia requerida.
- No mezclar output quality con process quality sin separar dimensiones.
- No usar una sola metrica global para decidir casos R3.
