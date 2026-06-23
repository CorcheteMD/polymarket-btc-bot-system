---
name: quality-context-reader
description: Lector de contexto para auditorias universales de calidad. Usar dentro de `universal-quality-orchestrator` cuando se necesite estructurar el caso antes de evaluar: sistema auditado, objetivo declarado, objetivo real, stakeholders, dominio, riesgo, evidencia disponible, artefactos, historial, constraints y gaps de contexto. No puntua, no crea rubricas, no propone mejoras.
---

# Quality Context Reader

## Mision

Convertir una entrada ambigua o dispersa en un contexto auditable. Esta skill crea la base factual que consumen rubrica, evidencia, scoring y red team.

## Inputs

- Descripcion del sistema, skill, pipeline, proceso u output.
- Objetivo esperado o decision que se busca tomar.
- Artefactos disponibles: prompts, codigo, documentos, outputs, logs, metricas, screenshots, versiones.
- Dominio declarado o inferido.
- Usuarios, destinatarios, stakeholders o afectados.
- Riesgo declarado o inferido.

## Workflow

1. **Identificar objeto auditado**
   - Sistema/pipeline.
   - Skill/agente.
   - Output/artefacto.
   - Proceso organizacional.
   - Comparacion entre versiones.

2. **Separar objetivo declarado y objetivo real**
   - Objetivo declarado: lo que el sistema dice perseguir.
   - Objetivo real: lo que el usuario necesita decidir o proteger.
   - Si divergen, marcarlo como riesgo de evaluacion.

3. **Mapear contexto operacional**
   - Donde se usa.
   - Quien lo usa.
   - Quien recibe el output.
   - Que pasa si falla.
   - Que restricciones hay: tiempo, costo, politica, regulacion, marca, privacidad.

4. **Inventariar evidencia**
   - Evidencia directa: artefactos, logs, resultados, metricas, muestras.
   - Evidencia indirecta: opiniones, supuestos, benchmarks no verificables.
   - Evidencia faltante: lo que seria necesario para juzgar con confianza.

5. **Clasificar riesgo**
   - R1: interno, reversible, bajo impacto.
   - R2: afecta usuarios, clientes, reputacion o decisiones operativas.
   - R3: legal, medico, financiero, seguridad, datos sensibles, reputacion severa o dano irreversible.

## Output

```markdown
## Contexto Auditable

- Objeto auditado:
- Tipo de objeto:
- Objetivo declarado:
- Objetivo real inferido:
- Dominio:
- Stakeholders:
- Usuario/destinatario final:
- Decision buscada:
- Riesgo: R1/R2/R3
- Consecuencia de fallo:
- Artefactos disponibles:
- Evidencia directa:
- Evidencia indirecta:
- Evidencia faltante:
- Gaps de contexto:
- Supuestos declarados:
- Bloqueos para auditar:
```

## Reglas Duras

- No evaluar calidad.
- No crear criterios de rubrica.
- No proponer soluciones.
- No transformar ausencia de evidencia en conclusion.
- Si falta objetivo u objeto auditado, devolver `NO EVALUABLE POR CONTEXTO`.
- Si el riesgo puede ser R3, clasificar como R3 hasta que evidencia lo baje.
