# Agent A Brief: Runtime Carriers And Operator Surfaces

## Role

Read-only evidence collector for runtime-facing carriers and operator guidance surfaces.

## Write Scope

Write only:

- `.planning/implementation-plans/20260424T082720Z/concrete-plans/002-runtime-intervention-surface-inventory/evidence/runtime-carriers.md`

Do not edit source, docs outside this evidence file, generated runtime output, overlay files, or planning registries.

## Task

Inventory files that carry runtime behavior, operator instructions, or runtime-specific guidance.

Start with:

- `AGENTS.md`
- `WORKFLOW.md`
- `docs/development.md`
- `docs/onboarding/codex.md`
- `docs/onboarding/claude.md`
- `docs/install-profiles.md`
- `docs/host-exercise-matrix.md`
- `tooling/portable-gsd/overlay/`
- `harness_modifier/overlay/`
- `harness_modifier/uplift/carrier_catalog.json`

Also inspect repo-local runtime config directories if present:

- `.codex/`
- `.claude/`

## Output Format

Write a Markdown report with:

1. Summary
2. Surface inventory table
3. Runtime-specific surfaces
4. Shared/operator surfaces
5. Generated or materialized surfaces
6. Unknowns and risks

Inventory table columns:

- Surface
- Path
- Runtime relevance
- Codex posture
- Claude posture
- Generated or maintained
- Evidence
- Open concern

## Evidence Rules

- Every claim must cite a local path.
- Mark inferred relationships as `Inference:` and explain the basis briefly.
- If a file is absent, record `absent` rather than inventing a role.
- Do not recommend implementation changes except as open questions.

## Completion Criteria

- The report is self-contained enough for the main thread to synthesize without re-running the whole scan.
- No files outside the write scope are modified.
