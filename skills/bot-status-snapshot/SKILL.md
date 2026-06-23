---
name: bot-status-snapshot
description: Use to produce a compact current-state snapshot for the bot from OPEN_WORK, skills manual, architecture docs, latest research, data registries, and harness checks. Does not change runtime state.
---

# Bot Status Snapshot

## Mission

Create one honest state document that tells the next agent what is active, blocked, risky, stale, and safe to do next.

## Inputs

- `vault/context/OPEN_WORK.md`
- `vault/context/CURRENT_STATE.md`
- `vault/research/CURRENT_RESEARCH.md`
- `vault/data/DATA_REGISTRY.md`
- `vault/SKILLS_MANUAL.md`
- latest decision and incident logs if present

## Workflow

1. Read current owner of progress.
2. Separate active path from stale campaigns.
3. Identify readiness gates and blocked items.
4. List canonical skills to use first.
5. Produce a short snapshot with timestamp and confidence.

## Output

- Current owner.
- Open stage.
- Active path.
- Do not touch list.
- Required skills.
- Next best action.
- Evidence gaps.

## Hard Rules

- Do not mix historical evidence into current readiness.
- Do not infer live readiness from old paper/replay artifacts.
- If source files conflict, mark `CONFLICT` instead of choosing silently.

