Date: 2026-04-22
Status: active change-triggered refresh

# Harness Modifier Project Uplift Host-Planning-Shape Neutralization Change-Triggered Refresh

## Trigger

- [e:c+i] The third neutralization tranche is now landed through [../intervention-proposals/159-harness-modifier-project-uplift-host-planning-shape-neutralization-implementation.md](../intervention-proposals/159-harness-modifier-project-uplift-host-planning-shape-neutralization-implementation.md).

## Carriers Refreshed

- [d:r:i] new typed state-section carrier:
  - `harness_modifier/uplift/state_section.json`
  - `harness_modifier/uplift/state_section.py`
- [d:r:i] new typed phase-layout carrier:
  - `harness_modifier/uplift/phase_layout.json`
  - `harness_modifier/uplift/phase_layout.py`
- [d:r:i] new narrow writer:
  - `harness_modifier/uplift/state_writer.py`
- [d:r:i] rewired helper:
  - `tooling/codex/project_uplift.py`
- [d:r:i] refreshed parity frontier:
  - `tooling/codex/tests/test_project_uplift.py`

## Propagation Meaning

- [d:r:i] The `Project Uplift` slot no longer depends on helper-local label order, sibling markers, or direct state-file edit logic embedded inside `project_uplift.py`.
- [d:r:i] Phase discovery for `context`, `plan`, and `summary` no longer depends on helper-local root/glob/prefix literals embedded inside `project_uplift.py`.
- [d:r:i] The helper now produces state-section values and phase activity, but the host planning-shape grammar itself has a typed home outside the helper.
- [d:r:i] The next payload-home judgment can now ask a still-sharper question: what remains materially host/shared-boundary after policy-data, host-doctrine/vocabulary, and host-planning-shape neutralization have all landed.

## Held Later

- [d:r:i] no relocation judgment inside this refresh itself
- [d:r:i] no install-contract pointer neutralization here
- [d:r:i] no second overlay tranche here
- [d:r:i] no standalone repo or npm/`npx` distribution move here
