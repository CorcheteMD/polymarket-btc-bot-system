---
name: botctl-control-plane
description: Use when designing or using a local command surface for the bot such as status, doctor, skills, recommend, snapshot, risk, and eval. Commands must be read-only by default and never execute live trading without explicit gates.
---

# Botctl Control Plane

## Mission

Create a safe local command surface that lets agents and humans inspect the bot without touching live runtime.

## Commands

- `status`: summarize current open work and architecture files.
- `skills`: list project skills and Claude skills.
- `doctor`: check required files and harness presence.
- `recommend`: point to the current orchestrator path.
- `snapshot`: print a compact status snapshot.

## Inputs

- Project root.
- Vault files.
- Skills.
- Optional latest reports.

## Output

- Human-readable status.
- Missing files.
- Skill list.
- Recommended next command or skill.

## Hard Rules

- Default commands are read-only.
- No command places orders, deploys, restarts PM2, edits `.env`, or touches VPS.
- Any write mode must be explicit and local-only.

