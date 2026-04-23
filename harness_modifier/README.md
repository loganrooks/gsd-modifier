# Harness Modifier

This package is the in-repo home for modifier-owned carriers and helpers inside `gsd-modifier`.

Current posture:
- `runtime-core`
  - `contract/`
  - `compatibility/`
  - shipped/install contract helpers used by local materialization
- `runtime-support`
  - `uplift/`
  - `capture/`
  - additive modifier workflows/skills and related support logic
- `pre-run experimental`
  - `closure/`
- `transitional support`
  - selected `tooling/codex/` helpers and compatibility shims that still participate in the extracted repo's executable development surface

For the carried migration/provenance context, see:
- [../docs/migration-origin.md](../docs/migration-origin.md)
- [../docs/origin-audit](../docs/origin-audit)

Current first-slice split:
- `contract/`
  - install/materialization helpers
  - runtime/install visibility and coherence helpers
  - bounded canary surfaces
- `closure/`
  - observe-only host-exercise packet and observation carriers
  - current posture: pre-run experimental / observe-only support
- `capture/`
  - launch-truth and runtime snapshot capture
  - external CLI probe helpers
- `compatibility/`
  - portable compatibility declaration and related typed carriers
- `overlay/`
  - modifier-owned workflow/skill source tranche
  - helper shims for moved workflow shells

Active scripts, docs, and tests should prefer `harness_modifier/...` paths where the authoritative home already lives.
