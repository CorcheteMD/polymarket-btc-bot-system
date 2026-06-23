---
name: market-research-intelligence
description: Investiga contexto de un mercado/evento Polymarket y sintetiza tesis YES/NO con fuentes trazables. Usar para preguntas abiertas, noticias, resolucion, datos oficiales, crowd vs LLM y forecast rationale. No ejecuta trades ni usa informacion privada.
---

# Market Research Intelligence

## Mision

Producir contexto verificable para una tesis de mercado sin convertirlo automaticamente en senal de trading.

## Inputs

- Pregunta del mercado.
- Slug, condition_id, close time.
- Fuentes publicas.
- Precio de mercado opcional.

## Workflow

1. Reescribir la pregunta en terminos resolubles.
2. Identificar fuente de resolucion y ambiguedades.
3. Buscar evidencia publica y actual.
4. Separar hechos, inferencias y opinion.
5. Entregar tesis YES/NO con incertidumbre.

## Output

- Dossier de mercado.
- Tesis YES/NO.
- Fuentes y calidad.
- Riesgo de resolucion.
- Handoff a `signal-generation-anomaly`.

## Fuera De Scope

- No usa MNPI ni fuentes privadas.
- No ejecuta ordenes.
- No ignora reglas de resolucion.

