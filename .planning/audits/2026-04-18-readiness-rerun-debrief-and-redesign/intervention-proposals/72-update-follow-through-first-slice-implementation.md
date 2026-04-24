Date: 2026-04-21
Status: landed first slice

# Update Follow-Through First Slice Implementation

## Purpose

- [g:r:i] This note records the landed first slice opened in `71`.
- [g:r:i] The target stayed bounded: runtime/package update now carries stronger route separation without widening into broader reinstall or seed-consumer work.

## What Landed

- [e:r:i] The tracked overlay now owns the current update carriers:
  - [tooling/portable-gsd/overlay/get-shit-done/workflows/update.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/update.md)
  - [tooling/portable-gsd/overlay/skills/gsd-update/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/skills/gsd-update/SKILL.md)
  - [tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json)
- [e:r:i] `update` now inherits the shared mandatory-read doctrine explicitly:
  - `required_reading`
  - `supporting_reading`
  - `deeper_reading`
- [e:r:i] The route split is now stated where runtime/package movement actually lives:
  - `update` keeps runtime/package change, installer rerun, custom-file backup, and patch recovery reminders as its owned boundary
  - structural planning repair now routes explicitly to `$gsd-health`
  - broader repo-local posture refresh now routes explicitly to `$gsd-uplift-project --write`
  - the current-runtime branch no longer implies that no later project-level follow-through could still be relevant

## Verification And Recovery Path

- [e:r:i] Focused contract proof now exists in [tooling/codex/tests/test_update_follow_through_contract.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/tests/test_update_follow_through_contract.py), covering:
  - overlay ownership for `update.md` and `gsd-update`
  - layered packet doctrine plus explicit health/uplift route separation in `update.md`
  - explicit runtime/package ownership plus separate repair/uplift follow-through in the skill wrapper
- [e:r:i] The slice became real overlay/materialization carry, not a live-only patch:
  - `python3 tooling/codex/portable_gsd_contract.py capture-pristine-overwrites . --strict`
  - `python3 tooling/codex/portable_gsd_contract.py validate-manifest . --strict`
  - `python3 tooling/codex/portable_gsd_contract.py apply-overlay . --compact-prompt-file tooling/compact-prompts/project.md`
  - `python3 tooling/codex/portable_gsd_contract.py apply-reasoning-defaults .`
  - `python3 tooling/codex/portable_gsd_contract.py verify-materialized . --compact-prompt-file tooling/compact-prompts/project.md --strict`

## What This Slice Still Holds

- [d:r:i] This slice does not yet widen into repeated-reinstall or standalone compatibility-carrier work.
- [d:r:i] It does not yet widen into seed-consumer carry.
- [d:r:i] It does not auto-launch repair or uplift from `update`; it keeps those routes explicit and separate.

## Current Consequence

- [d:r:i] The harness now carries stronger update-side follow-through instead of letting runtime/package movement stand in for structural repair or broader repo-local posture refresh.
- [d:r:i] The next narrower question is which adjacent onboarding family should inherit after this:
  - seed consumers
  - a later wider entry-wrapper retrofit
  - or a broader repeated-reinstall / compatibility carrier

