# Harness Modifier

This package is the authoritative in-repo home for generic harness-modifier carriers.

Current first-slice split:
- `contract/`
  - portable install/materialization contract helpers
  - runtime/install visibility and coherence helpers
  - bounded canary surfaces
- `capture/`
  - launch-truth capture
  - runtime snapshot capture
  - external CLI probe helpers
  - stream extraction helpers
- `compatibility/`
  - typed portable compatibility declaration
  - parity-baseline rules and held-annotation posture
  - first extraction artifact intended to travel unchanged into a later standalone project

During the in-repo rehome step, the old `tooling/codex/*.py` paths remain as thin compatibility shims.
Active scripts, docs, and tests should prefer `harness_modifier/...` paths.
