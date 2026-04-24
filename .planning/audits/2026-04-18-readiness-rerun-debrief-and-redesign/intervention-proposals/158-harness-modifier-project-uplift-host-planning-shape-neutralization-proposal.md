Date: 2026-04-22
Status: proposed

# Harness Modifier Project Uplift Host-Planning-Shape Neutralization Proposal

## Role

- [g:r:i] This proposal defines the next bounded extraction move after the reopened payload-home judgment in lane `08`.
- [g:r:i] Its job is not to relocate `project_uplift.py` yet.
- [g:r:i] Its job is to neutralize the remaining host-planning-shape surface still embedded inside `project_uplift.py` so a later payload-home judgment can be reopened on a further-thinned helper.

## Why This Slice Now

- [d:r:i] `154` landed the policy-data neutralization tranche.
- [d:r:i] `157` landed the host-doctrine and operator-facing vocabulary neutralization tranche.
- [d:r:i] Lane `08` then reopened the payload-home question on top of both landed tranches and found one materially remaining host-coupling surface:
  - `.planning/STATE.md` writer reach
  - `.planning/phases/*/*-CONTEXT.md` scanner reach
  - phase-directory shape assumptions
  - the line-label schema inside `state_section_text`
- [d:r:i] Relocation still remains later because moving `project_uplift.py` now would re-host that planning-shape writer/scanner blur instead of dissolving it.

## Judgment Questions

### 1. What Planning-Shape Surface Should Move Out Of The Helper?

- [d:r:i] The slice should neutralize the host-planning-shape surface only:
  - state-section anchor and sibling-marker knowledge
  - state-section line-label schema
  - phase-layout and scan-shape knowledge
- [d:r:i] It should not widen into install-contract wiring, standalone extraction, or packaging.

### 2. What Should The Helper Keep?

- [d:r:i] `project_uplift.py` should keep:
  - classification
  - fingerprinting
  - drift-reason composition
  - report/progress-note rendering
  - CLI plumbing
- [d:r:i] The helper should call a narrower writer/scanner surface rather than editing host planning files directly.

### 3. What Is The Cleaner Neutralization Shape?

- [d:r:i] The slice should judge the cleanest bounded split across:
  - a typed writer-side state-section carrier
  - a typed analysis-side phase-layout carrier
  - a narrow writer module with distinct render and update entries
- [d:r:i] It should keep `OVERLAY_MANIFEST_REL_PATH` explicitly out of this tranche and hold that as a later install-contract slice.

## Proposed Carrying Surfaces

- [d:r:i] current helper:
  - `tooling/codex/project_uplift.py`
- [d:r:i] already landed typed carriers:
  - `harness_modifier/compatibility/declaration.json`
  - `harness_modifier/compatibility/observation.json`
  - `harness_modifier/compatibility/seed_contract.json`
  - `harness_modifier/uplift/output_policy.json`
  - `harness_modifier/uplift/carrier_catalog.json`
  - `harness_modifier/uplift/vocabulary.json`
- [d:r:i] proposed new bounded carrier/writer pair:
  - `harness_modifier/uplift/state_section.json`
  - `harness_modifier/uplift/phase_layout.json`
  - `harness_modifier/uplift/state_writer.py`
- [d:r:i] extraction/governance carry:
  - `harness_modifier/overlay/helpers/AUTHORITY-MAP.md`
  - `harness_modifier/overlay/ROSTER.md`
  - `CURRENT-STATE.md`
  - `STATUS.md`
  - `extraction-audit/README.md`

## Explicitly Not This Slice

- [d:r:i] No `project_uplift.py` relocation yet.
- [d:r:i] No `seed_migration_inventory.py` relocation.
- [d:r:i] No `audit_refmap.py` movement.
- [d:r:i] No second overlay filesystem tranche.
- [d:r:i] No overwrite-family source-indirection widening.
- [d:r:i] No standalone repo or npm/`npx` packaging move.
- [d:r:i] No broader `.codex` / `.claude` parity redesign.
- [d:r:i] No `OVERLAY_MANIFEST_REL_PATH` neutralization inside this tranche.
- [d:r:i] No `seed_migration_inventory.py` or `harness_canary.py` changes inside this tranche.
- [d:r:i] No `tooling/codex/UPLIFT-HELD-LATER.md` artifact-home move inside this tranche.

## Sharpened Shape

- [d:r:i] `state_heading` remains owned by `harness_modifier/uplift/output_policy.json`; the new state-section carrier references that heading rather than re-declaring `"## Project Uplift"`.
- [d:r:i] `harness_modifier/uplift/state_section.json` should carry:
  - `.planning/STATE.md` path anchor
  - sibling-marker names
  - ordered label tuple
  - typed selector vocabulary
- [d:r:i] `harness_modifier/uplift/phase_layout.json` should carry:
  - `.planning/phases` root anchor
  - phase-prefix grammar
  - discovery globs for `*-CONTEXT.md`, `*-PLAN.md`, and `*-SUMMARY.md`
- [d:r:i] `harness_modifier/uplift/state_writer.py` should expose distinct render and update entries so parity tests can judge each boundary separately.
- [d:r:i] Selector dispatch stays in writer code; do not pull rendering logic into carrier data as `(label, field_selector)` tuples.

## Focused Parity Frontier

- [d:r:i] The tranche should name and hold:
  - rendered state-section byte equivalence on a representative analysis fixture
  - emitted uplift manifest field equivalence
  - `update_state_section` byte equivalence across anchor-match, sibling-marker-insert, and trailing-append paths
  - `latest_phase_context_path`, `count_phase_files`, and `phase_sort_key` equivalence after the phase-layout carrier replaces embedded literals

## Governance Carry

- [d:r:i] The landed tranche should refresh:
  - `harness_modifier/overlay/helpers/AUTHORITY-MAP.md`
  - `harness_modifier/overlay/ROSTER.md`
  - `.planning/HARNESS-IMPROVEMENT-REGISTER.md`
  - `CURRENT-STATE.md`
  - `STATUS.md`
  - `extraction-audit/README.md`
- [d:r:i] The landed tranche should also open a propagation-audit entry modeled on `57` and `58`.

## Exact Next Move

1. [d:r:i] Run one bounded reread on this host-planning-shape neutralization proposal.
2. [d:r:i] Use that reread to judge the cleanest carrier/writer/layout split.
3. [d:r:i] Only after that third neutralization tranche lands, reopen the payload-home judgment again on the further-thinned helper.
