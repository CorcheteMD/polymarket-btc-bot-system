---
name: bot-harness-architect
description: Use when designing or upgrading the local AI harness for the Polymarket bot: skill roots, context loading, gates, command surfaces, subagent handoffs, memory, evals, and safety boundaries. Does not edit trading code or execute remote/live actions.
---

# Bot Harness Architect

## Mission

Design the control plane around the bot so agents work with context, gates, evidence, and repeatable workflows instead of improvising.

## When To Use

- You want to upgrade the AI system, not a single strategy.
- You need to decide where a new skill, command, memory file, eval, or hook belongs.
- You are adapting external systems like ECC into this bot.
- You need a blueprint before building automation.

## Inputs

- `CLAUDE.md`
- `vault/SKILLS_MANUAL.md`
- `vault/context/OPEN_WORK.md`
- `vault/architecture/*.md`
- Existing skills under `vault/skills` and `.claude/skills`
- Existing scripts such as `eval_pipeline.py`, `agent_brain.py`, and `scripts/hb_profit_orchestrator.py`

## Workflow

1. Classify the requested upgrade: context, skill, command, eval, memory, security, or orchestration.
2. Identify the owner: docs, skill, script, vault data, or runtime module.
3. Define the handoff contract: input, output, evidence, forbidden actions.
4. Add a gate if the workflow can affect capital, VPS, credentials, or live runtime.
5. Propose the smallest implementation that improves repeatability.

## Output

- Harness component map.
- Ownership boundaries.
- Handoff contracts.
- Safety gates.
- Implementation order.

## Hard Rules

- Do not create global hooks before a local read-only harness exists.
- Do not connect research directly to execution.
- Do not modify `.env`, private keys, API secrets, or VPS state.
- Do not promote a system unless eval and risk gates exist.

