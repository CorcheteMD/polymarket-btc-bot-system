---
name: hb-dataset-contract-freezer
description: Use when freezing, auditing, or selecting HB datasets for Polymarket replay, shadow validation, or live truth. It prevents mixing canonical bars, HB context, outcomes, and derived artifacts dishonestly.
---

# HB Dataset Contract Freezer

Mission: define what each dataset is allowed to prove.

## Inputs

- root paths or artifact paths
- row counts, time window, schema, hashes
- known bad Parquet fragments
- evidence purpose: discovery, replay, shadow truth, execution truth

## Output

- `DATASET_OK`, `DATASET_PARTIAL`, or `DATASET_BLOCKED`
- manifest path
- allowed use
- forbidden use
- missing fields

## Rules

- Canonical/HORAS_BUENAS is discovery/replay, not live execution truth.
- HB context is forward shadow/live event truth, not arbitrary alpha discovery.
- Derived CSV/JSON reports are hypothesis catalog only.
- Bad Parquet fragments must be named and excluded.
- Native timing fields beat reconstructed timing.
