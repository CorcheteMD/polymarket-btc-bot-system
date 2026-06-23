---
name: universal-quality-orchestrator
description: Orquestador universal de auditoria de calidad para IA, sistemas, skills, orquestadores, pipelines, procesos y outputs. Usar cuando el usuario pida medir calidad, auditar un sistema, evaluar resultados de un orquestador, comparar versiones, detectar fallas, proponer mejoras, redisenar un pipeline, crear un scorecard o decidir si un artefacto/sistema esta listo para uso, publicacion o entrega. Coordina subskills de contexto, rubrica, evidencia, scoring, red team, causa raiz, veredicto, mejora y re-score; no evalua ni mejora directamente.
---

# Universal Quality Orchestrator

## Mision

Coordinar una auditoria profunda y portable de calidad sin depender de un rubro especifico. Esta skill lee el caso, activa `skill-pipeline-architect` para ordenar el pipeline, delega a las subskills de calidad y ensambla el reporte final.

No puntua, no construye rubricas, no hace red team, no diagnostica causas raiz y no propone mejoras por cuenta propia. Su trabajo es gobernar el flujo y proteger la separacion de responsabilidades.

## Principios

1. **Separacion estricta.** Ninguna skill evalua lo que ella misma construyo.
2. **Rigor profundo por defecto.** Si falta evidencia, declarar baja confianza en vez de inventar certeza.
3. **Dominio externo.** Las normas o referencias de salud, codigo, legal, finanzas, marketing u otro rubro se cargan como insumos, no viven en esta skill.
4. **Gate antes del score.** Un caso sin contexto, objetivo o evidencia minima no debe recibir nota fuerte.
5. **R3 exige humano.** Legal, medico, financiero, seguridad, datos sensibles o reputacion no se aprueban sin gate humano.
6. **Mejora verificable.** Un rediseno no cuenta como mejora hasta pasar por `quality-rescore-validator`.
7. **Pipeline architect conserva ownership.** Usar `skill-pipeline-architect` para decidir orden, capas, profundidad y handoffs.

## Inputs Esperados

- Sistema, skill, orquestador, pipeline, proceso u output a auditar.
- Objetivo declarado y objetivo real si existe.
- Contexto de uso, audiencia, stakeholders y dominio.
- Artefactos: prompts, codigo, documentos, logs, metricas, outputs, versiones anteriores.
- Riesgo declarado o inferido: R1, R2 o R3.
- Referencias de dominio o criterios externos si existen.
- Para contenido NeuroMatrona V4.1 historico: ICP Attention Brief, Extreme Hook Ranking Matrix, ICP Hook Fit Matrix, Human Selection Gate, Final Reveal Ledger, material conversacional, guion/brief, limites clinicos y fuentes o auditoria local.
- Para contenido NeuroMatrona V5: Scroll Stopper Inspector, Visible Hook Ranking, Internal Hook Scorecard, ICP Scroll Simulation Panel, Story Retention Reality Gate, Commentability/Shareability Gate, guion con oratoria, limites clinicos y re-score si hubo mejora.
- Para contenido NeuroMatrona V5.1: Visual Event Bank, Marketing Brutality Red Team, prueba sin texto/audio, Curiosity Debt Ledger, Comment Trigger Lab y re-score despues de cambios.
- Para contenido NeuroMatrona V5.2: Shoot Feasibility Reality Gate, Prototype Test, Conversation Continuation Lab, version casera si hubo idea impracticable y re-score despues de cambios.
- Para contenido NeuroMatrona V6: Docu-Real Cold Open Bank, Boringness Blacklist Report, Feed Collision Score, Hook Kill Room Verdict, V6 Hook Dossier y re-score despues de cambios.
- Para contenido NeuroMatrona V6.2: Unspoken Insecurity Map, Ethical Recognition Gate, Assumed Truth / Contrarian Line Set si aplica, Reversal Ledger, V6.2 Hook Dossier y re-score despues de cambios.

## Referencias

Lee solo lo necesario:

- Dimensiones base: `references/universal-quality-dimensions.md`.
- Confianza y suficiencia de evidencia: `references/evidence-confidence-model.md`.
- Riesgos y gates humanos: `references/risk-levels-and-human-gates.md`.
- Formato final: `references/final-report-template.md`.
- Fronteras entre subskills: `references/anti-overlap-boundaries.md`.

## Pipeline Canonico

1. `skill-pipeline-architect`: clasifica tipo, riesgo, etapa, entregable, profundidad y orden de capas.
2. `quality-context-reader`: estructura el caso y declara gaps de contexto.
3. `quality-rubric-builder`: crea la rubrica especifica del caso.
4. `quality-evidence-mapper`: mapea evidencia contra criterios y marca faltantes.
5. `quality-evidence-scorer`: puntua solo con evidencia disponible.
6. `quality-red-team-auditor`: ataca puntos fuertes, riesgos y edge cases.
7. `quality-root-cause-analyst`: separa sintomas de causas raiz.
8. `quality-verdict-synthesizer`: integra hallazgos y emite veredicto.
9. `quality-improvement-planner`: propone plan de mejora y rediseno si corresponde.
10. `quality-rescore-validator`: solo se activa cuando existe version mejorada.

## Workflow

### 1. Intake y clasificacion

Completar:

- Objeto auditado: sistema, skill, pipeline, proceso, output o version comparativa.
- Objetivo esperado.
- Contexto de uso.
- Dominio.
- Riesgo inicial.
- Evidencia disponible.
- Decision buscada: medir, aprobar, bloquear, mejorar, redisenar o comparar.

Si el caso es ambiguo pero no bloqueante, declarar supuestos. Si falta el objeto auditado o el objetivo esperado, pedirlo antes de continuar.

### 2. Llamar a `skill-pipeline-architect`

Solicitarle:

- Clasificacion en 5 dimensiones.
- Score de profundidad.
- Capas requeridas.
- Skills existentes a usar.
- Handoffs.
- Gaps u overlap.

No crear una skill nueva de pipeline dentro de este sistema.

### 3. Ejecutar subskills por handoff

Cada subskill debe recibir solo el output necesario de la anterior:

- Context reader entrega contexto estructurado.
- Rubric builder recibe contexto y referencias.
- Evidence mapper recibe rubrica y artefactos.
- Scorer recibe rubrica + matriz de evidencia.
- Red team recibe scorecard + sistema auditado.
- Root cause recibe scorecard + red team + contexto.
- Verdict recibe todos los hallazgos, pero no crea mejoras nuevas.
- Improvement planner recibe veredicto + causas raiz.
- Rescore validator recibe version anterior + version mejorada + rubrica congelada.

### 4. Ensamblar reporte final

Usar `references/final-report-template.md` y completar:

- Veredicto.
- Score global y confianza.
- Scorecard por dimension.
- Matriz de evidencia.
- Hallazgos red team.
- Causas raiz.
- Riesgos residuales.
- Plan de mejora.
- Rediseno de pipeline si aplica.
- Gates humanos pendientes.
- Re-score pendiente o comparativo.

### 5. Modo NeuroMatrona V4.1 Pre-Shoot

Activar cuando se audite una pieza de contenido NeuroMatrona antes de `reel-shoot-director`.

Evidencia minima:

- `ICP Attention Brief`.
- `Extreme Hook Ranking Matrix` completa.
- `ICP Hook Fit Matrix`.
- `Human Selection Gate` si hay contenders.
- `Final Reveal Ledger` con regla practica.
- Material conversacional si el objetivo es comentario.
- Claims bloqueados y limites clinicos.
- Guion o estructura narrativa.
- Score de `neuro-content-performance-lab` si existe.

Bloquear o marcar `APROBADO CON CAMBIOS` si:

- El sistema eligio el hook final sin decision humana cuando habia contenders.
- Falta una matriz o tiene columnas incompletas.
- El reveal no contiene criterio, contraste o decision rule.
- El recurso de comentarios es solo una palabra, sin promesa ni estructura.
- Las red flags clinicas quedan fuera del caption/limite.
- Hay opcion ROJO/NEGRO sin reemplazo prudente.

Si el output se mejora despues de esta auditoria, activar `quality-rescore-validator` antes de grabar.

### 6. Modo V5 / V5.1 / V5.2 / V6 / V6.2 Viral Reality Audit

Activar cuando se audite una pieza NeuroMatrona V5 antes de guion final, shot list o publicacion.

Evidencia minima:

- `Scroll Stopper Inspector`.
- `Visible Hook Ranking`.
- `Internal Hook Scorecard`.
- `ICP Scroll Simulation Panel` con 17 ICPs.
- `Story Retention Reality Gate`.
- `Commentability / Shareability Gate`.
- Guion con beats de oratoria.
- Riesgos clinicos y claims bloqueados.
- Re-score si hubo cambios despues de auditoria.

Evidencia minima adicional para V5.1:

- `Visual Event Bank`.
- `Marketing Brutality Red Team`.
- Prueba sin texto y sin audio.
- `Curiosity Debt Ledger`.
- `Comment Trigger Lab` si el objetivo es comentario/share.

Evidencia minima adicional para V5.2:

- `Shoot Feasibility Reality Gate`.
- `Prototype Test`.
- Version casera de reemplazo para toda idea impracticable.
- `Conversation Continuation Lab` si el objetivo es comentario/DM conversacional.

Evidencia minima adicional para V6:

- `Docu-Real Cold Open Bank`.
- `Boringness Blacklist Report`.
- `Feed Collision Score`.
- `Hook Kill Room Verdict`.
- `V6 Hook Dossier`.
- Decision humana si hay contenders o opciones ROJO/NEGRO.

Evidencia minima adicional para V6.2:

- `Unspoken Insecurity Map`.
- `Ethical Recognition Gate`.
- `Assumed Truth / Contrarian Line Set` si se usa verdad asumida o contradiccion.
- `Reversal Ledger` si se usa contradiccion.
- `V6.2 Hook Dossier`.

Auditar:

- Creatividad no generica: no obvia, no vista, no IA-like.
- Simulacion ICP: contexto de scroll, feed previo, keep/skip y accion probable.
- Retencion narrativa: que esperaba recibir y si se le pago mejor de lo esperado.
- Commentability/shareability: comentario simple, material claro o razon de compartir.
- Riesgo clinico: sin cura, miedo, body shame, diagnostico o promesa.
- Originalidad de plataforma: no copia tendencia ni repost mental.
- Fuerza de evento: hay accion fisica, contradiccion, consecuencia o interrupcion; no solo objeto mostrado.
- Marketing brutality: el hook compite en feed saturado y no es correcto pero invisible.
- Curiosity debt: la rareza abre una deuda que el reveal paga proporcionalmente.
- Factibilidad real: el hook se puede grabar hoy sin IA, VFX, montaje complejo, caos visual ni actuacion falsa.
- Continuidad conversacional: el comentario abre ramas que Ayleen puede responder sin diagnosticar en publico.
- Docu-realidad: el hook parece una escena humana interrumpida, no una metafora de objeto.
- Blacklist: no usa patrones gastados salvo como apoyo secundario a conflicto humano.
- Feed collision: gana contra al menos 3 de 5 contextos de feed.
- Kill room: recibe PASS antes de ranking.
- Reconocimiento etico: toca inseguridad no dicha sin humillar, diagnosticar, asustar ni sonar superior.
- Verdad asumida: "como ya sabes" funciona como complicidad, no como arrogancia.
- Contradiccion segura: el giro no es un claim absoluto y vuelve a una explicacion prudente.

Bloquear o marcar `REESCRIBIR / REDISENAR` si:

- En V5.1 falta `Visual Event Bank` o `Marketing Brutality Red Team`.
- En V5.2 falta `Shoot Feasibility Reality Gate`.
- En V6 falta `Docu-Real Cold Open Bank`, `Boringness Blacklist Report`, `Feed Collision Score` o `Hook Kill Room Verdict`.
- En V6.2 falta `Unspoken Insecurity Map` o `Ethical Recognition Gate`.
- En V6.2 se usa verdad asumida/contradiccion sin `Assumed Truth / Contrarian Line Set`.
- En V6.2 se usa contradiccion sin `Reversal Ledger`.
- El hook es props-first, educativo disfrazado o patron gastado.
- El cold open no gana 3 de 5 en feed collision.
- El cold open no recibe `PASS` en hook kill room.
- El hook parece IA/VFX, no se puede grabar plano por plano o requiere montaje no declarado.
- El hook no funciona sin texto y sin audio.
- El hook falla inspector o no puede explicar por que detiene scroll.
- Menos de 70% del panel queda en keep.
- Menos de 50% llega al final con accion probable.
- La tabla publica muestra calculos gigantes en vez de formato compacto.
- El CTA es complejo, minoritario o no nace del video.
- El video explica despues del hook sin sostener tension.
- La deuda de curiosidad no se paga con un reveal proporcional.
- El CTA no paso `comment-trigger-lab` cuando el objetivo era comentario/share.
- El CTA no paso `conversation-continuation-lab` cuando el objetivo era conversacion o DM.
- La pieza usa inseguridad como insulto, body shame, miedo clinico, superioridad o lectura mental.
- La frase "sabemos mas de ti que tu" aparece literal o implicita.
- "Como ya sabes" aparece como primer estimulo o invalida a la mujer.
- La contradiccion no se paga con una vuelta segura en el reveal.

Si falla, devolver a iteracion creativa/story/performance segun causa raiz. Si se modifica, activar `quality-rescore-validator`.

## Veredictos Permitidos

- `APROBADO`: evidencia suficiente, riesgo controlado, score alto y sin hallazgos bloqueantes.
- `APROBADO CON CAMBIOS`: base valida con ajustes obligatorios antes de uso amplio.
- `ALERTA`: valor potencial, pero evidencia incompleta, riesgos abiertos o fallas relevantes.
- `REESCRIBIR / REDISENAR`: el output o pipeline tiene fallas estructurales.
- `BLOQUEADO`: riesgo R3, dano probable, evidencia critica faltante o contradiccion grave.
- `NO EVALUABLE`: falta contexto, objetivo o evidencia minima.

## Reglas Duras

- No aprobar un caso R3 sin gate humano.
- No emitir score numerico si la rubrica no existe.
- No emitir confianza alta con evidencia incompleta en dimensiones criticas.
- No permitir que `quality-improvement-planner` declare que sus mejoras ya funcionaron.
- No mezclar criterios de un dominio con otro sin evidencia de relevancia.
- No optimizar por metrica visible si contradice el objetivo real del sistema.
- No ocultar gaps: un buen reporte puede terminar en `NO EVALUABLE`.

## Smoke Tests

1. Skill de contenido NeuroMatrona: debe separar calidad del output, calidad del pipeline y riesgo clinico/comercial.
2. Pipeline tecnico/codigo: no debe usar criterios de salud, marketing o premiumidad si no aplican.
3. Evidencia incompleta: debe bajar confianza y bloquear conclusiones fuertes.
4. Caso R3: debe exigir gate humano.
5. Version mejorada: debe activar re-score y rechazar cambios solo cosmeticos.
6. Contenido NeuroMatrona V4.1 pre-shoot: debe bloquear shot list si faltan matrices, seleccion humana, regla practica, recurso conversacional o re-score pendiente.
7. Contenido NeuroMatrona V5: debe bloquear si falta inspector, simulacion 17 ICPs, story retention, comment/share gate o tabla compacta.
8. Contenido NeuroMatrona V5.1: debe bloquear si falta Visual Event Bank, Marketing Brutality Red Team, prueba sin texto/audio, Curiosity Debt Ledger o Comment Trigger Lab cuando aplique.
9. Contenido NeuroMatrona V5.2: debe bloquear si falta Shoot Feasibility Reality Gate, Prototype Test, version casera de reemplazo o Conversation Continuation Lab cuando aplique.
10. Contenido NeuroMatrona V6: debe bloquear si faltan cold open docu-real, blacklist, feed collision, kill room o si el hook nace de props.
