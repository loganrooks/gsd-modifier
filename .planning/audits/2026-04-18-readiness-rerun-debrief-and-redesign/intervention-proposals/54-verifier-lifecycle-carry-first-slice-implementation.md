Date: 2026-04-21
Status: landed first slice

# Verifier Lifecycle Carry First Slice Implementation

## Purpose

- [g:r:i] This note records the first landed lifecycle-carry slice opened in `53`.
- [g:r:i] The target was bounded: make verifier-side workflow, template, registry, and reference carriers answer back to the planning-side `future_preservation` contract instead of letting that carry thin after plan creation.

## What Landed

- [e:r:i] The tracked overlay now owns the verifier-side lifecycle carriers that were previously outside repo-local carry:
  - [tooling/portable-gsd/overlay/get-shit-done/workflows/verify-phase.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/verify-phase.md)
  - [tooling/portable-gsd/overlay/get-shit-done/templates/verification-report.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/templates/verification-report.md)
  - [tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json)
- [e:r:i] The verifier registry contract now loads and routes `future_preservation` explicitly:
  - [tooling/portable-gsd/overlay/agents/gsd-verifier.toml](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/agents/gsd-verifier.toml)
  - [tooling/portable-gsd/overlay/get-shit-done/references/agent-contracts.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/references/agent-contracts.md)
- [e:r:i] The landed verifier slice now reviews four planning-carry buckets when present:
  - `protected_seams`
  - `non_decisions`
  - `posture_assumptions`
  - `strengthening_routes`
- [e:r:i] The verifier-side statuses are now explicit and narrower than a flat pass:
  - item-level `carried`
  - item-level `thinned`
  - item-level `uncertain`
  - phase-level `gaps_found` when any carry item is `thinned`
  - phase-level `human_needed` when any carry item is `uncertain`
- [e:r:i] [tooling/codex/project_uplift.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/project_uplift.py) now samples the new verifier-side doctrine carriers, so uplift memory and later propagation refreshes can see that this lifecycle slice moved.

## Verification And Recovery Path

- [e:r:i] Manifest validation surfaced one real ownership correction during landing: the new verifier workflow/template carriers are upstream-shipped surfaces, so they belong under tracked `overwrite` ownership rather than `add`.
- [e:r:i] The landed slice passed:
  - `python3 -m json.tool tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json`
  - `python3 -m py_compile tooling/codex/project_uplift.py`
  - `python3 -m unittest tooling.codex.tests.test_project_uplift`
  - `python3 tooling/codex/portable_gsd_contract.py validate-manifest . --strict`
  - `python3 tooling/codex/portable_gsd_contract.py verify-materialized . --compact-prompt-file tooling/compact-prompts/project.md --strict`
  - `python3 tooling/codex/harness_canary.py report . --strict`
- [e:r:i] The direct local rerun of [scripts/setup-portable-gsd.sh](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh) still exits non-zero here because the upstream installer self-check cannot resolve `gsd-sdk` on `PATH`.
- [d:r:i] That fragility is not treated as fixed in this slice.
- [d:r:i] The verified local recovery path remains:
  - `portable_gsd_contract.py apply-overlay`
  - `portable_gsd_contract.py apply-reasoning-defaults`
  - `portable_gsd_contract.py verify-materialized`

## What This Slice Still Holds

- [d:r:i] This slice does not yet widen into:
  - `transition` carry
  - milestone-boundary carry
  - `SPEC` carry
  - `STATE.md` / `progress` lifecycle carry
  - seed-consumer carry
- [d:r:i] This slice does not claim setup-script robustness. It keeps that fragility explicit as a later maintainability / reinstall-truth family instead of quietly folding it into lifecycle carry.

## Current Consequence

- [d:r:i] Planning-side `future_preservation` no longer disappears before verification by default.
- [d:r:i] The current lifecycle question is narrower now:
  - which later lifecycle surface should inherit next
  - and how the repo-local setup / reinstall path should become more durable so runtime restoration is less brittle under repeated local use
