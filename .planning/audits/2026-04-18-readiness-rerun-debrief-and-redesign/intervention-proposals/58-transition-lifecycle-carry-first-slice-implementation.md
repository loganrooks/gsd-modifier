Date: 2026-04-21
Status: landed first slice

# Transition Lifecycle Carry First Slice Implementation

## Purpose

- [g:r:i] This note records the first landed transition-side lifecycle-carry slice opened in `57`.
- [g:r:i] The target stayed bounded: make phase closure carry forward preserved seams, explicit non-decisions, posture assumptions, and strengthening routes instead of letting them thin between verifier follow-through and the next planning round.

## What Landed

- [e:r:i] The tracked overlay now owns the transition-side lifecycle carriers that were previously outside repo-local carry:
  - [tooling/portable-gsd/overlay/get-shit-done/workflows/transition.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/transition.md)
  - [tooling/portable-gsd/overlay/get-shit-done/templates/state.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/templates/state.md)
  - [tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json)
- [e:r:i] The transition workflow now loads plan `future_preservation` before marking a phase complete and explicitly reviews four carry buckets when present:
  - `protected_seams`
  - `non_decisions`
  - `posture_assumptions`
  - `strengthening_routes`
- [e:r:i] The landed transition slice now requires an explicit close-boundary judgment for each carry item:
  - stay live into the next immediate phase
  - remain explicit at project/state level even when not next-phase execution
  - close with an explicit note
  - move to explicit seed handoff when it is a strengthening route outside the next immediate phase
- [e:r:i] The state template now has a bounded `Future Carry Forward` digest under `Accumulated Context` with a compact four-line shape:
  - `Preserve:`
  - `Keep open:`
  - `Posture:`
  - `Seeded:`
- [e:r:i] The transition workflow success criteria now require the `Future Carry Forward` digest to remain explicit when future-preservation carry is still live, instead of treating roadmap/state updates as only requirement/decision evolution.

## Verification And Recovery Path

- [e:r:i] Manifest validation surfaced one real ownership correction during landing: `get-shit-done/templates/state.md` is an upstream-shipped carrier, so the overlay needed tracked `overwrite` ownership rather than ambient live-only drift.
- [e:r:i] The landed slice passed:
  - `python3 tooling/codex/portable_gsd_contract.py capture-pristine-overwrites . --strict`
  - `python3 -m json.tool tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json`
  - `python3 tooling/codex/portable_gsd_contract.py validate-manifest . --strict`
  - `python3 tooling/codex/portable_gsd_contract.py apply-overlay . --compact-prompt-file tooling/compact-prompts/project.md`
  - `python3 tooling/codex/portable_gsd_contract.py apply-reasoning-defaults .`
  - `python3 tooling/codex/portable_gsd_contract.py verify-materialized . --compact-prompt-file tooling/compact-prompts/project.md --strict`
  - `python3 tooling/codex/harness_canary.py report . --strict`
- [e:r:i] Post-materialization verification proved the new transition/state-template carriers survive repo-local reinstall/materialization rather than existing only as local overlay prose.

## What This Slice Still Holds

- [d:r:i] This slice does not yet widen into:
  - milestone-boundary carry
  - `SPEC` carry
  - broader `progress` / `resume-project` consumer redesign for future-carry summaries
  - seed-consumer redesign beyond explicit transition-time routing to seed handoff
- [d:r:i] This slice does not try to settle every activation-pressure or long-arc doctrine question at phase close; it keeps the first durable close-boundary bridge explicit and bounded.

## Current Consequence

- [d:r:i] Planning-side `future_preservation` no longer disappears by default between verifier review and phase transition.
- [d:r:i] The lifecycle-carry family now has two landed bridges:
  - verifier-side follow-through in `54`
  - transition-side carry and state-digest upkeep in `58`
- [d:r:i] The next narrower lifecycle question is no longer whether transition should inherit at all. It is which adjacent later surface should inherit next:
  - milestone boundaries
  - `STATE/progress` consumer readout
  - `SPEC`
  - or seed-consumer carry beyond the first transition-time route
