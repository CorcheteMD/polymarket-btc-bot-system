---
name: quality-rescore-validator
description: Validador de re-score para auditorias universales de calidad. Usar cuando existe una version mejorada de un sistema, skill, pipeline, proceso u output y se necesita comparar contra la auditoria anterior con la misma rubrica, verificar si subio calidad real y detectar mejoras cosmeticas o regresiones. No crea el plan de mejora.
---

# Quality Rescore Validator

## Mision

Cerrar el ciclo de mejora continua. Esta skill compara antes/despues y decide si los cambios mejoraron calidad real segun evidencia, no solo apariencia.

## Inputs

- Auditoria anterior.
- Rubrica anterior congelada.
- Plan de mejora.
- Version mejorada.
- Nueva evidencia.
- Hallazgos red team nuevos si existen.

## Workflow

1. **Congelar criterio**
   - Usar la misma rubrica salvo que el plan haya exigido corregir una rubrica defectuosa.
   - Si cambia la rubrica, declarar que el score no es comparable 1:1.

2. **Comparar acciones prometidas vs implementadas**
   - Accion implementada.
   - Accion parcial.
   - Accion no implementada.
   - Cambio extra no planificado.

3. **Re-mapear evidencia**
   - Confirmar evidencia nueva.
   - Marcar gaps persistentes.
   - Marcar evidencia que sigue siendo indirecta o insuficiente.

4. **Re-score**
   - Puntuar dimensiones afectadas.
   - Detectar regresiones.
   - Comparar score global y confianza.

5. **Validar mejora real**
   - Mejora real: sube score/confianza y reduce causa raiz.
   - Mejora parcial: corrige sintomas, pero no causa raiz completa.
   - Mejora cosmetica: cambia forma, no resultado.
   - Regresion: mejora una dimension y empeora otra critica.

## Output

```markdown
## Re-Score Validator

- Veredicto re-score:
- Score anterior:
- Score nuevo:
- Confianza anterior:
- Confianza nueva:
- Comparabilidad: directa/parcial/no comparable

| Dimension | Antes | Despues | Cambio | Evidencia nueva | Decision |
|---|---:|---:|---:|---|---|

## Validacion Del Plan

| Accion prometida | Estado | Evidencia | Impacto |
|---|---|---|---|

## Regresiones

1. ...

## Decision

- APROBADO / MEJORA PARCIAL / COSMETICO / REGRESION / NO EVALUABLE
- Proximo paso:
```

## Reglas Duras

- No aceptar cambios cosmeticos como mejora real.
- No comparar scores si la rubrica cambio sin declararlo.
- No aprobar R3 sin gate humano aunque el score suba.
- No ignorar regresiones por mejora global.
- No crear plan nuevo salvo recomendacion breve de proximo ciclo.
