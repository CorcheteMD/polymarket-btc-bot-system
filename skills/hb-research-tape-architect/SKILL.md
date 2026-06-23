---
name: hb-research-tape-architect
description: Use when designing a lightweight HB live-era research tape that captures candidate rows before narrow strategy filters without increasing VPS CPU/I/O or touching the order hot path.
---

# HB Research Tape Architect

Mission: create replayable live-era data without hurting live execution.

## Inputs

- required fields
- HB time window
- CPU/I/O budget
- producer/consumer topology
- retention and snapshot policy

## Output

- schema proposal
- writer location
- forbidden hot-path writes
- heartbeat/health metrics
- replay compatibility contract

## Rules

- Append-only and slim.
- No CLOB calls.
- No model/probability computation unless already available.
- Must run before narrow strategy gates but after enough state exists for truthful deltas.
