---
name: vps-live-safety-ops
description: Use before any remote VPS operation for the HB live bot, especially exports, scans, PM2 restarts, heartbeat checks, or research jobs that might affect live runtime.
---

# VPS Live Safety Ops

Mission: protect the live VPS and hot path from research work.

## Inputs

- intended remote command or operation
- target paths
- PM2 status
- heartbeat freshness
- CPU/memory/load
- file/root size

## Rules

- Block full-root Parquet scans on live VPS.
- Prefer local snapshots or bounded partition exports.
- Check `hb-dedicated-collector` and `hb-fairprice-microlive` before and after.
- Verify wrapper exports are before final `exec`.
- `pm2 online` is not enough; heartbeat and mtimes must be fresh.

## Output

`REMOTE_SAFE`, `REMOTE_BLOCKED`, or `REMOTE_SAFE_WITH_BOUNDS`, with exact allowed command shape and rollback/check steps.
