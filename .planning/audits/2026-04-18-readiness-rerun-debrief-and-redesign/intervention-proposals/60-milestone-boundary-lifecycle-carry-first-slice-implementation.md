Date: 2026-04-21
Status: landed first slice

# Milestone Boundary Lifecycle Carry First Slice Implementation

## Purpose

- [g:r:i] This note records the first landed milestone-boundary lifecycle-carry slice opened in `59`.
- [g:r:i] The target stayed bounded: make milestone opening and milestone close reread long-arc doctrine and future-carry continuity explicitly instead of leaving that bridge to operator memory after the verifier and transition slices.

## What Landed

- [e:r:i] The tracked overlay now owns the milestone-boundary lifecycle carriers that were previously outside repo-local carry:
  - [tooling/portable-gsd/overlay/get-shit-done/workflows/new-milestone.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/new-milestone.md)
  - [tooling/portable-gsd/overlay/get-shit-done/workflows/complete-milestone.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/complete-milestone.md)
  - [tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json)
- [e:r:i] `new-milestone.md` now rereads `.planning/LONG-ARC.md` when present and treats `STATE.md` `Future Carry Forward` as explicit milestone-opening input instead of leaving preserved seams, keep-open decisions, posture assumptions, and seeded strengthening routes ambient.
- [e:r:i] The milestone-opening summary, requirements shaping, research handoff, and roadmapper handoff now keep future-carry pressure explicit when it remains relevant at milestone open.
- [e:r:i] `complete-milestone.md` now rereads `.planning/STATE.md` and `.planning/LONG-ARC.md` before archival/project evolution cleanup and performs a bounded milestone-close review over:
  - still-live preserved seams
  - keep-open non-decisions
  - posture assumptions that should remain explicit
  - seeded strengthening routes that should remain explicit rather than dissolving into retrospective prose
- [e:r:i] The milestone-close success criteria and state-update guidance now require still-live future carry to remain explicit after milestone close rather than being silently cleared by the boundary itself.

## Verification And Recovery Path

- [e:r:i] Manifest validation surfaced the real carry boundary clearly: both milestone workflows are upstream-shipped carriers, so the overlay now owns them as tracked `overwrite` entries rather than ambient live-only drift.
- [e:r:i] The landed slice passed:
  - `python3 -m json.tool tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json`
  - `python3 tooling/codex/portable_gsd_contract.py capture-pristine-overwrites . --strict`
  - `python3 tooling/codex/portable_gsd_contract.py validate-manifest . --strict`
  - `python3 tooling/codex/portable_gsd_contract.py apply-overlay . --compact-prompt-file tooling/compact-prompts/project.md`
  - `python3 tooling/codex/portable_gsd_contract.py apply-reasoning-defaults .`
  - `python3 tooling/codex/portable_gsd_contract.py verify-materialized . --compact-prompt-file tooling/compact-prompts/project.md --strict`
  - `python3 tooling/codex/harness_canary.py report . --strict`
- [e:r:i] Post-materialization verification proved the new milestone-boundary carriers survive repo-local reinstall/materialization rather than existing only as local overlay prose.

## What This Slice Still Holds

- [d:r:i] This slice does not yet widen into:
  - `SPEC` carry
  - broader `STATE/progress` or `resume-project` consumer redesign for future-carry summaries
  - seed-consumer redesign beyond keeping seeded routes explicit at milestone boundaries
- [d:r:i] This slice does not try to settle every long-horizon tension at milestone boundaries; it keeps the milestone-open and milestone-close reread/continuity bridge explicit and bounded.

## Current Consequence

- [d:r:i] Lifecycle carry now has three landed later-boundary bridges:
  - verifier-side follow-through in `54`
  - transition-side carry and state-digest upkeep in `58`
  - milestone-boundary long-arc and future-carry reread plus continuity review in `60`
- [d:r:i] The next narrower lifecycle question is no longer whether later boundaries should inherit at all. It is which adjacent later surface should inherit next:
  - `SPEC`
  - `STATE/progress` consumer readout
  - or seed-consumer carry beyond explicit boundary rereads
