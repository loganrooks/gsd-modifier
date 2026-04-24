Date: 2026-04-21
Status: landed first slice

# Project-Uplift First-Slice Implementation

## Purpose

- [g:r:i] This note records the first live implementation slice for the `37 + 38 + 39` project-uplift family after the widening lanes, bundle challenge, reread, and harmonization pass.
- [g:r:i] The slice stays detect-only by default and keeps additive refresh / doctrine-sensitive rewrite routes for later bounded follow-through.

## What Landed

- [e:r:i] A new repo-local helper now exists at `tooling/codex/project_uplift.py`.
- [e:r:i] The helper now:
  - classifies current uplift posture
  - fingerprints the bounded first-slice carrier set
  - writes `.planning/UPLIFT-REPORT.md`
  - writes `.planning/UPLIFT-MANIFEST.json`
  - refreshes a dedicated `## Project Uplift` section inside `.planning/STATE.md`
  - emits a read-only `progress-note` view so `progress` can read structured uplift memory instead of prose
- [e:r:i] A new tracked overlay workflow now exists at `tooling/portable-gsd/overlay/get-shit-done/workflows/uplift-project.md`.
- [e:r:i] A new tracked overlay skill now exists at `tooling/portable-gsd/overlay/skills/gsd-uplift-project/SKILL.md`.
- [e:r:i] The tracked overlay `progress.md` now carries a bounded `Uplift Posture` note that reads `UPLIFT-MANIFEST.json` through the helper rather than parsing prose.
- [e:r:i] The live `.codex/` runtime was re-materialized through `./scripts/setup-portable-gsd.sh`, so the new workflow, skill, and progress hook now carry through tracked overlay rather than a live-only patch.

## Verification Set

### Synthetic Verification

- [e:r:i] `tooling/codex/tests/test_project_uplift.py` now covers:
  - vanilla uplift classification
  - lightly aged uplift classification
  - output writing plus later doctrine-movement detection for `progress-note`

### Repo-Local Negative / Safety Verification

- [e:r:i] The helper was first run on `prix-guesser` in read-only form before any durable output write.
- [e:r:i] That read-only pass stayed non-destructive and surfaced the repo’s mixed `.codex` / `.claude` runtime posture as `cross-runtime uplift` instead of flattening it into a generic aging class.

### Live Output Verification

- [e:r:i] After the helper wrote the first durable outputs for this repo, `progress-note` reread the resulting manifest and now recommends ordinary routing rather than immediately demanding another detect-only pass.
- [e:r:i] The first write surfaced one real integration bug: the report/state section initially preserved the transient pre-write `no uplift manifest recorded yet` recommendation.
- [e:r:i] That bug is now fixed, and the durable outputs now reflect post-write posture rather than the transient pre-write condition.

## Current Repo Result

- [e:r:i] The current repo now carries:
  - `.planning/UPLIFT-REPORT.md`
  - `.planning/UPLIFT-MANIFEST.json`
  - a `STATE.md` uplift section
- [e:r:i] The current repo’s first recorded class is `cross-runtime uplift`.
- [d:r:i] That result is appropriate for the current repo because `.codex` and `.claude` both still exist, which means the later cross-runtime uplift family remains real even though the first detect-only pass does not yet widen into that follow-through.

## What This Slice Deliberately Holds

- [d:r:i] No additive carrier installs landed from this workflow.
- [d:r:i] No doctrine-sensitive AGENTS / CLAUDE refresh landed from this workflow.
- [d:r:i] No broad wrapper rewrite, cross-runtime reconciliation, upstream-template-drift machinery, or audit-aging machinery landed from this workflow.
- [d:r:i] The first slice is composition, posture recording, and routing only.

## Current Consequence

- [d:r:i] The project-uplift family now has real runtime carry, real durable outputs, and a real `progress` consumer.
- [d:r:i] The next honest move is no longer “can this family be implemented at all?”
- [d:r:i] The next honest move is to decide whether the stronger adjacent step is:
  - challenged reread of the landed first slice
  - additive install-route implementation
  - or later cross-runtime uplift follow-through
