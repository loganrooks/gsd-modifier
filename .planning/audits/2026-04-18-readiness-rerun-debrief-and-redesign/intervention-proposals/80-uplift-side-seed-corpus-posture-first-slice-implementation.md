Date: 2026-04-22
Status: landed first slice

# Uplift-Side Seed Corpus Posture First Slice Implementation

## Purpose

- [g:r:i] This note records the landed first slice opened in `79`.
- [g:r:i] The target stayed bounded: uplift now sees seed corpus posture and preserves it in durable uplift memory without absorbing seed migration.

## What Landed

- [e:r:i] The uplift helper now scans `.planning/seeds/SEED-*.md` and records seed corpus posture in:
  - [tooling/codex/project_uplift.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/project_uplift.py)
  - [UPLIFT-REPORT.md](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-REPORT.md)
  - [UPLIFT-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-MANIFEST.json)
  - [STATE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/STATE.md)
- [e:r:i] The posture now distinguishes:
  - no seed corpus
  - current-contract-only corpus
  - legacy-unversioned presence
  - noncurrent version presence
- [e:r:i] The helper now treats seed corpus movement like another durable-memory refresh trigger, so live progress/resume routing can push toward `--write` after seed posture changes instead of leaving stored uplift memory stale.
- [e:r:i] The uplift workflow and wrapper now keep that posture visible while still holding migration as a later route:
  - [uplift-project.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/get-shit-done/workflows/uplift-project.md)
  - [gsd-uplift-project/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/skills/gsd-uplift-project/SKILL.md)
- [e:r:i] The held-later uplift register now keeps seed migration explicit rather than silent:
  - [tooling/codex/UPLIFT-HELD-LATER.md](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/UPLIFT-HELD-LATER.md)

## Verification And Recovery Path

- [e:r:i] Focused uplift proof now lives in [tooling/codex/tests/test_project_uplift.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/tests/test_project_uplift.py), widened to cover:
  - mixed current-plus-legacy seed corpus classification
  - schema/versioned uplift-memory carry
  - refresh routing after seed corpus movement
- [e:r:i] The helper and current repo uplift outputs were refreshed with:
  - `python3 tooling/codex/project_uplift.py detect . --write --json`

## What This Slice Still Holds

- [d:r:i] This slice does not migrate or rewrite legacy seeds.
- [d:r:i] It does not widen broader seed consumers.
- [d:r:i] It does not widen `audit.cjs`.
- [d:r:i] It does not create a standalone seed migration helper.

## Current Consequence

- [d:r:i] Project-wide onboarding and re-entry now keep seed corpus compatibility more visible instead of leaving that distinction only at milestone-open.
- [d:r:i] The next narrower seed-family question is now cleaner:
  - broader seed consumers beyond milestone opening
  - later `audit.cjs` widening
  - any later wider entry-wrapper retrofit
