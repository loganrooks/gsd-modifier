Date: 2026-04-21
Status: landed first slice

# Initialization And Ingest Read-Packet First Slice Implementation

## Purpose

- [g:r:i] This note records the landed first slice opened in `67`.
- [g:r:i] The target stayed bounded: initialization and ingest now inherit the shared read-packet doctrine without widening yet into the broader repair/migration family.

## What Landed

- [e:r:i] The tracked overlay now owns the current initialization and ingest carriers:
  - [tooling/portable-gsd/overlay/get-shit-done/workflows/new-project.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/new-project.md)
  - [tooling/portable-gsd/overlay/get-shit-done/workflows/new-milestone.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/new-milestone.md)
  - [tooling/portable-gsd/overlay/get-shit-done/workflows/ingest-docs.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/ingest-docs.md)
  - [tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json)
- [e:r:i] Those three workflows now carry the shared mandatory-read doctrine explicitly:
  - `required_reading`
  - `supporting_reading`
  - `deeper_reading`
- [e:r:i] The route split is now stated where initialization/onboarding pressure actually lives:
  - `new-project` now starts from init plus idea context, keeps brownfield widening deliberate, and routes existing-project refresh pressure toward `$gsd-progress` plus `$gsd-uplift-project --write`
  - `new-milestone` now keeps milestone-open project/state/long-arc context primary, with seeds and research widening only when those routes activate
  - `ingest-docs` now keeps parse/init/manifest primary, keeps classifications/conflict/merge widening staged, and routes repo-local uplift separately instead of blending it into doc ingest

## Verification And Recovery Path

- [e:r:i] Focused contract proof now exists in [tooling/codex/tests/test_initialization_read_packet_contract.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/tests/test_initialization_read_packet_contract.py), covering:
  - overlay ownership for the three initialization/ingest workflows
  - layered packet doctrine presence
  - explicit uplift-routing visibility where this slice makes that route real
- [e:r:i] The slice became real overlay/materialization carry, not a live-only patch:
  - `python3 tooling/codex/portable_gsd_contract.py capture-pristine-overwrites . --strict`
  - `python3 tooling/codex/portable_gsd_contract.py validate-manifest . --strict`
  - `python3 tooling/codex/portable_gsd_contract.py apply-overlay . --compact-prompt-file tooling/compact-prompts/project.md`
  - `python3 tooling/codex/portable_gsd_contract.py apply-reasoning-defaults .`
  - `python3 tooling/codex/portable_gsd_contract.py verify-materialized . --compact-prompt-file tooling/compact-prompts/project.md --strict`

## What This Slice Still Holds

- [d:r:i] This slice does not yet widen into `health` or `from-gsd2`.
- [d:r:i] It does not yet add automatic relevance ranking or packet synthesis.
- [d:r:i] It does not yet widen the same doctrine across every remaining entry skill wrapper.

## Current Consequence

- [d:r:i] The harness now carries layered read-packet control across both re-entry and the primary initialization/doc-ingest workflows instead of leaving initialization as a flatter older pocket.
- [d:r:i] The next narrower question is which adjacent onboarding family should inherit after this:
  - `health` / repair
  - `from-gsd2` / migration
  - seed-consumer carry
  - or a later wider packet retrofit
