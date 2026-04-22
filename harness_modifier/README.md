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

During the in-repo rehome step, the old `tooling/codex/*.py` paths remain as thin compatibility shims.
Active scripts, docs, and tests should prefer `harness_modifier/...` paths.
