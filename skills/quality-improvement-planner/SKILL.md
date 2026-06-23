---
name: quality-improvement-planner
description: Planificador de mejora y rediseno para auditorias universales de calidad. Usar despues del veredicto y causa raiz para proponer correcciones, controles, rediseno de skill, rediseno de pipeline, cambios de rubrica, evidencia faltante y backlog priorizado. No declara que la mejora funciona; eso corresponde a `quality-rescore-validator`.
---

# Quality Improvement Planner

## Mision

Convertir el diagnostico en un plan de mejora accionable. Puede proponer rediseno completo cuando la causa raiz esta en el sistema, no solo en el output.

## Inputs

- Veredicto final.
- Causas raiz.
- Scorecard.
- Hallazgos red team.
- Contexto y restricciones.
- Pipeline actual si existe.

## Workflow

1. **Priorizar causas**
   - Criticas primero.
   - Luego alto impacto/bajo esfuerzo.
   - Separar deuda estructural de mejoras cosmeticas.

2. **Elegir tipo de accion**
   - Corregir output.
   - Reescribir prompt/skill.
   - Cambiar handoff.
   - Agregar gate.
   - Agregar evidencia.
   - Redisenar pipeline.
   - Crear nueva skill o referencia.

3. **Disenar controles**
   - Gate antes de score.
   - Gate humano.
   - Checklists.
   - Rubrica actualizada.
   - Pruebas red team.
   - Re-score posterior.

4. **Definir aceptacion**
   - Que cambia.
   - Como se verifica.
   - Que evidencia demostrara mejora real.

## Output

```markdown
## Plan De Mejora

| Prioridad | Accion | Causa raiz que ataca | Tipo | Owner sugerido | Evidencia de exito | Re-score |
|---:|---|---|---|---|---|---|
| 1 | ... | ... | output/prompt/pipeline/evidencia/gate | ... | ... | requerido |

## Rediseno De Pipeline

- Pipeline actual:
- Falla estructural:
- Pipeline propuesto:
- Handoffs nuevos:
- Gates nuevos:
- Skills/referencias faltantes:

## Cambios Que No Cuentan Como Mejora

- ...
```

## Reglas Duras

- No declarar aprobacion final.
- No llamar mejora a cambios esteticos si no atacan causa raiz.
- No crear nuevas responsabilidades dentro de una skill que ya tiene ownership claro.
- No eliminar gates R3 por velocidad.
- Todo plan debe terminar en condicion de re-score.
