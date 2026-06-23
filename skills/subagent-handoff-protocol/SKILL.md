---
name: subagent-handoff-protocol
description: Use before delegating work to another agent or model. Defines objective, context, allowed files, forbidden actions, output contract, evidence standard, and return format so subagents do not lose the real purpose.
---

# Subagent Handoff Protocol

## Mission

Make delegation precise. A subagent should know why the task matters, what evidence counts, and what it must not touch.

## Handoff Template

```text
Objective:
Why it matters:
Allowed files:
Forbidden files/actions:
Evidence required:
Output format:
Decision labels:
Stop conditions:
Return to:
```

## Workflow

1. State the real objective, not only the literal command.
2. Include the current owner of progress from `OPEN_WORK`.
3. Declare allowed sources.
4. Declare forbidden actions.
5. Define the exact output contract.
6. Require uncertainty and gaps.

## Hard Rules

- No subagent gets access to live execution unless the parent task already passed risk and human gates.
- No subagent should infer secrets or ask to print them.
- Do not ask a subagent to both build and audit the same artifact.

