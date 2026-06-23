---
name: ecc-extraction-lab
description: Use to evaluate ECC or other external agent systems before adapting them into this bot. Separates reusable patterns from unsafe installs, identifies harness ideas, and produces an extraction plan.
---

# ECC Extraction Lab

## Mission

Extract useful frontier patterns from ECC without blindly installing external automation into a trading system.

## Inputs

- ECC repository docs or files.
- Local bot harness map.
- Target use case.
- Security constraints.

## Workflow

1. Classify ECC component: skill, rule, hook, MCP, dashboard, installer, command, or daemon.
2. Decide if it is pattern-only, copyable, adaptable, or blocked.
3. Identify local owner: skill, doc, script, eval, memory, or security.
4. Run `bot-agent-shield` for anything that can execute commands or touch secrets.
5. Produce extraction plan.

## Output

- `PATTERN_ONLY`
- `ADAPT_AS_SKILL`
- `ADAPT_AS_DOC`
- `ADAPT_AS_SCRIPT_READ_ONLY`
- `BLOCKED_UNSAFE`

## Hard Rules

- Do not install hooks globally.
- Do not run external installers on the bot by default.
- Do not import MCP configs without reviewing permissions.
- Prefer local minimal adaptation over broad install.

