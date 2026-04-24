# Agent B Brief: Instruction Generation And Uplift Paths

## Role

Read-only evidence collector for producers and update paths that create or alter instruction surfaces.

## Write Scope

Write only:

- `.planning/implementation-plans/20260424T082720Z/concrete-plans/002-runtime-intervention-surface-inventory/evidence/instruction-generation.md`

Do not edit source, docs outside this evidence file, generated runtime output, overlay files, or planning registries.

## Task

Trace how instruction and onboarding surfaces are produced, updated, or carried.

Search for producer and consumer references to:

- `AGENTS.md`
- `.planning/AGENTS.md`
- `CLAUDE.md`
- `.planning/CLAUDE.md`
- `experimental_compact_prompt_file`
- `new-project`
- `project_uplift`
- `carrier_catalog`
- onboarding docs
- runtime instruction templates

Likely areas:

- `tooling/codex/`
- `harness_modifier/uplift/`
- `harness_modifier/overlay/`
- `tooling/portable-gsd/overlay/`
- `.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign`

## Output Format

Write a Markdown report with:

1. Summary
2. Producer inventory
3. Consumer inventory
4. Generation/update flow map
5. Parity-relevant findings
6. Unknowns and risks

Flow map rows:

- Source producer
- Output surface
- Trigger or command
- Runtime affected
- Evidence
- Verification currently available
- Gap or open question

## Evidence Rules

- Prefer `rg` results tied to exact files over broad prose.
- Every claim must cite a local path.
- Mark inferred relationships as `Inference:`.
- Do not change any generation logic in this plan.

## Completion Criteria

- The report identifies current producers and consumers well enough to decide whether a later parity plan should edit generation logic, docs, contracts, or all three.
- No files outside the write scope are modified.
