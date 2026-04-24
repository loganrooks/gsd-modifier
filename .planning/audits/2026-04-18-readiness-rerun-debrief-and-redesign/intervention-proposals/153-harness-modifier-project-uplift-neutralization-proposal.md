Date: 2026-04-22
Status: proposed

# Harness Modifier Project Uplift Neutralization Proposal

## Role

- [g:r:i] This proposal defines the next bounded extraction move after the helper authority map in `152`.
- [g:r:i] Its job is not to relocate `project_uplift.py` yet.
- [g:r:i] Its job is to neutralize the remaining helper-local policy and path assumptions that would otherwise make later payload movement blur authority, routing, or provider posture.

## Why This Slice Now

- [d:r:i] `harness_modifier/overlay/helpers/AUTHORITY-MAP.md` now freezes the helper split explicitly:
  - `project_uplift.py` is the modifier-facing payload candidate
  - `seed_migration_inventory.py` remains downstream of it
  - `audit_refmap.py` is outside the later payload-movement family
- [d:r:i] The lane-04 Opus reread kept the next move bounded: land a neutralization precondition slice for `project_uplift.py` before any relocation, second overlay tranche, overwrite-family widening, or standalone-project design.
- [d:r:i] The helper still carries three kinds of embedded assumptions that should travel as data or declaration rather than as helper-local constants:
  - runtime discovery posture
  - uplift output / planning path posture
  - compatibility-anchor routing posture

## Neutralization Targets

### 1. Runtime Discovery Policy

- [d:r:i] `project_uplift.py` still hard-codes `RUNTIME_DIRS` as a helper-local list.
- [d:r:i] The neutralization move is to shift runtime discovery posture into a typed carrier rather than leaving it as a module constant.
- [d:r:i] That carrier should preserve the current `.codex` observed basis and `.claude` held annotation discipline while avoiding a fresh provider-widening argument inside this slice.
- [d:r:i] This slice should not decide a broader multi-provider future. It should only stop helper-local constants from silently owning that policy.

### 2. Uplift Output And Planning Path Policy

- [d:r:i] `project_uplift.py` still owns `REPORT_REL_PATH`, `MANIFEST_REL_PATH`, `HELD_LATER_REL_PATH`, `SEED_DIR_REL_PATH`, and `STATE_HEADING` directly.
- [d:r:i] Some of these are ordinary output locations, but together they still make the helper itself the implicit owner of uplift-memory topology.
- [d:r:i] The neutralization move is to gather these into a typed output/path policy carrier so later payload movement does not also have to move hidden path doctrine.
- [d:r:i] This slice should keep the current output topology stable; it should only re-home the policy expression.

### 3. Compatibility-Anchor Routing

- [d:r:i] The helper now reads `harness_modifier/compatibility/declaration.json`, but it still copies many declaration fields into helper-local globals and helper-local routing assumptions.
- [d:r:i] The neutralization move is to reduce helper-local compatibility posture copying so the declaration remains the authority and the helper becomes a consumer with thinner local policy.
- [d:r:i] This slice should preserve:
  - `.codex` as the observed runtime basis
  - `.claude` as the held annotation
  - the current parity-baseline semantics
- [d:r:i] This slice should not reopen compatibility-family widening or standalone compatibility-carrier design.

## Proposed Carrying Surfaces

- [d:r:i] live helper:
  - `tooling/codex/project_uplift.py`
- [d:r:i] helper-adjacent typed carriers, if earned:
  - `harness_modifier/compatibility/declaration.json`
  - a new adjacent typed uplift-path/runtime-policy carrier under `harness_modifier/`
- [d:r:i] tests:
  - focused `project_uplift` contract coverage
  - any new carrier loader tests if a new typed carrier is introduced
- [d:r:i] governance / extraction carry:
  - `harness_modifier/overlay/helpers/AUTHORITY-MAP.md`
  - `harness_modifier/overlay/ROSTER.md`
  - `CURRENT-STATE.md`
  - `STATUS.md`
  - `intervention-proposals/README.md`

## Explicitly Not This Slice

- [d:r:i] No payload relocation of `project_uplift.py`.
- [d:r:i] No movement of `seed_migration_inventory.py`.
- [d:r:i] No reopening of `audit_refmap.py` movement.
- [d:r:i] No second overlay filesystem tranche.
- [d:r:i] No overwrite-family source-indirection widening.
- [d:r:i] No standalone repo or npm/`npx` packaging move.
- [d:r:i] No broader `.codex` / `.claude` parity redesign beyond preserving the current compatibility declaration posture.

## Exact Next Move

1. [d:r:i] Land one implementation slice that moves runtime discovery posture, uplift output/path posture, and compatibility-anchor routing posture out of helper-local constants as far as is justified without relocating the helper.
2. [d:r:i] Refresh the helper authority map and extraction/governance surfaces so later payload movement, if still earned afterward, starts from the neutralized boundary rather than from helper-local hidden policy.
3. [d:r:i] Only after that neutralization slice lands, decide whether later `project_uplift.py` movement is still the sharper extraction move or whether the cleaner boundary has changed.
