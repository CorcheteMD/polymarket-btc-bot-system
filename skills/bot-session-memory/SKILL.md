---
name: bot-session-memory
description: Use to create, update, or read durable session memory for the bot: decision logs, incident logs, open work summaries, and lessons converted into rules or skills. Does not rewrite history or change runtime state.
---

# Bot Session Memory

## Mission

Keep the bot's learning durable without polluting future sessions with stale or false context.

## Inputs

- Session summary.
- Decisions made.
- Evidence used.
- Bugs found.
- Incidents.
- New rules or skill candidates.

## Workflow

1. Separate fact, inference, decision, and open question.
2. Mark whether evidence is historical, current, shadow, paper, or live.
3. Append decision or incident in machine-readable form when applicable.
4. Update open work only if it changes the active owner of progress.
5. Convert repeated lessons into skill or prevention-rule candidates.

## Output

- Session memory entry.
- Decision log entry.
- Incident log entry.
- Skill candidate.
- Stale-context warning.

## Hard Rules

- Do not overwrite old evidence to make it cleaner.
- Do not promote a lesson into a rule after one anecdote.
- Do not mix old bundle evidence with current bundle readiness.

