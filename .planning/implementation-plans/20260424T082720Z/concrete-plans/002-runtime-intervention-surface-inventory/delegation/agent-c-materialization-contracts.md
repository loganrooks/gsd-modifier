# Agent C Brief: Materialization Contracts And Verification Hooks

## Role

Read-only evidence collector for install/materialization paths and contract checks.

## Write Scope

Write only:

- `.planning/implementation-plans/20260424T082720Z/concrete-plans/002-runtime-intervention-surface-inventory/evidence/materialization-contracts.md`

Do not edit source, docs outside this evidence file, generated runtime output, overlay files, or planning registries.

## Task

Map how runtime-facing source surfaces become materialized runtime behavior, and how this repo verifies that relationship.

Start with:

- `scripts/setup-portable-gsd.sh`
- `scripts/setup-portable-gsd-runtime.sh`
- `tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json`
- `harness_modifier/contract/portable_gsd_contract.py`
- `harness_modifier/contract/runtime_visibility.py`
- `harness_modifier/contract/manifest_install_coherence.py`
- `harness_modifier/contract/harness_canary.py`
- `harness_modifier/contract/runtime_adapters/`
- `harness_modifier/closure/host_exercise_matrix.py`
- `scripts/ci/check-deterministic.sh`
- `scripts/ci/check-bootstrap.sh`

## Output Format

Write a Markdown report with:

1. Summary
2. Materialization path map
3. Contract checker inventory
4. CI and host-matrix gates
5. Surface-to-verification table
6. Unknowns and risks

Surface-to-verification table columns:

- Source surface
- Materialized destination
- Runtime profile
- Contract or script that checks it
- Command
- Evidence
- Gap or open question

## Evidence Rules

- Every claim must cite a local path.
- Mark inferred relationships as `Inference:`.
- Distinguish source verification from materialized-runtime verification.
- Do not broaden host-matrix semantics in this plan.

## Completion Criteria

- The report makes clear which future runtime-surface changes would require source-only checks, materialized checks, CI gates, or host matrix proof.
- No files outside the write scope are modified.
