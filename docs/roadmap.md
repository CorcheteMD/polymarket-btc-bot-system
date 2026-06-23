# Roadmap

This is the public-safe continuation roadmap.

## Phase 0: Public Contracts

- Add typed data contracts.
- Add synthetic fixtures.
- Add tests for stale heartbeat, negative fillability, missing approval, and evidence disagreement.
- Document excluded private components.

## Phase 1: Research Harness

- Add read-only market discovery interfaces.
- Add archive/replay interfaces that accept synthetic data.
- Add microstructure feature functions.
- Add tests that distinguish implied price from executable price.

## Phase 2: Trade Lifecycle Design

- Add a public `TradeLifecycle` state machine.
- Add recovery-from-restart design docs.
- Add idempotent close tests.
- Keep execution disabled.

## Phase 3: Review Artifacts

- Generate review-ready Markdown reports from candidate evidence.
- Include `do_not_do` guardrails in every report.
- Require human approval before any promote-review state.

## Phase 4: Private Integration

Private only. This is where live data adapters, credentials, VPS runtime, and strategy parameters would be connected.

