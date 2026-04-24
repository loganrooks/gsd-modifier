Date: 2026-04-22
Status: landed first-slice implementation

# Uplift Compatibility Annotation First Slice Implementation

## Purpose

- [g:r:i] Land the first bounded implementation slice cleared by the revised compatibility-family widening-shape proposal in `114`.
- [g:r:i] Keep the uplift compatibility anchor rooted in the observed `.codex` basis while making the currently held `.claude` runtime difference durable inside the same family.

## Landed Shape

- [d:r:i] The landed sub-shape is the narrower `held-scalar` annotation route, not the `structural-row` route.
- [d:r:i] `compatibility_posture` remains `observed_basis_only`.
- [d:r:i] The new compatibility detail is carried as a held runtime annotation:
  - runtime: `.claude`
  - version: `1.34.2`
  - source: `.claude/get-shit-done/VERSION`
  - annotation posture: `held_annotation`

## Carrier Follow-Through

- [d:r:i] Helper-side carry now lives in [tooling/codex/project_uplift.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/project_uplift.py):
  - read the canonical observed `.codex` runtime basis
  - read the held `.claude` runtime annotation separately
  - preserve the top-level observed-basis posture
  - route held-runtime movement into the progress-note write recommendation path
- [d:r:i] The landed helper-side implementation choice is the narrower `.claude`-specific constant route, not a runtime-dir walker:
  - `HELD_CLAUDE_RUNTIME_VERSION_REL_PATH`
  - the observed-basis anchor stays narrow while the held runtime is read through one explicitly named secondary path
- [d:r:i] Durable uplift outputs now carry the annotation:
  - [UPLIFT-REPORT.md](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-REPORT.md)
  - [UPLIFT-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-MANIFEST.json)
  - `Project Uplift` section in [STATE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/STATE.md)
- [d:r:i] Read-only current-runtime consumers now surface the annotation when present:
  - [progress.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/progress.md)
  - [resume-project.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/resume-project.md)
  - [uplift-project.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/get-shit-done/workflows/uplift-project.md)
  - [gsd-uplift-project/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/skills/gsd-uplift-project/SKILL.md)

## What This Slice Preserves

- [d:r:i] The observed runtime basis remains `.codex` only.
- [d:r:i] The slice keeps one explicit asymmetry visible rather than hiding it:
  - the wider runtime detection list still includes `.gemini`, `.opencode`, and `.kilo`
  - the held-runtime annotation reader only reads `.claude`
  - this keeps later third-runtime widening named as later instead of quietly implying it already travels today
- [d:r:i] The slice does not claim a version-window compatibility matrix.
- [d:r:i] The slice does not claim `.claude` route translation parity.
- [d:r:i] The slice does not open a standalone multi-runtime compatibility carrier.

## Real Repo Result

- [e:c+i] The refreshed durable uplift memory now records:
  - observed runtime basis: `.codex 1.38.3`
  - held runtime annotation: `.claude 1.34.2 (held_annotation)`
  Sources:
  - [UPLIFT-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-MANIFEST.json)
  - [UPLIFT-REPORT.md](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-REPORT.md)
  - [STATE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/STATE.md)
- [e:c+i] The project still classifies as `cross-runtime uplift`, with recommendation `Continue with current routing.` Source:
  - [UPLIFT-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-MANIFEST.json)

## Verification

- [e:c+i] Focused helper coverage passed:
  - `python3 -m unittest tooling.codex.tests.test_project_uplift`
- [e:c+i] Overlay was re-materialized into live `.codex`:
  - `./scripts/setup-portable-gsd.sh`
- [e:c+i] Durable uplift memory was refreshed against the real repo:
  - `python3 tooling/codex/project_uplift.py detect . --write --json`
- [e:c+i] The refreshed report/state now show the held runtime annotation explicitly. Sources:
  - [UPLIFT-REPORT.md](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-REPORT.md)
  - [STATE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/STATE.md)

## Current Consequence

- [d:r:i] The compatibility family now carries a narrower widening shape in live code and live operator-facing outputs, not only in proposal prose.
- [d:r:i] The next adjacent move can now ask a cleaner question:
  - whether later cross-runtime widening should intensify consumer-chain asymmetry carry
  - or whether a later structural-row shape is earned inside the same family
  - without losing the observed-basis discipline the current slice preserves
