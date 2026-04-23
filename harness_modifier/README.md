# Harness Modifier

This package is the authoritative in-repo home for generic harness-modifier carriers.

Current shipped/install contract posture:
- `runtime-core`
  - installer entrypoint and install/materialization contract
  - installed runtime config, agent, patched CLI-lib, reference, template, overwrite workflow, and overwrite skill carriers
  - package `contract/` and `compatibility/`
- `runtime-support`
  - additive modifier workflows/skills
  - package `uplift/`
  - package `capture/`
- `transitional shipped/install support`
  - installed compact prompts that are still host-local / non-portable
  - current bridge paths such as `project_uplift.py`, `seed_migration_inventory.py`, and thin `tooling/codex/` compatibility shims
- `pre-run experimental`
  - package `closure/`
- `development-program-only`
  - repo-local audit-tooling boundaries such as `audit_refmap.py`

Current durable ledger:
- [.planning/.../02-shipped-install-contract-classification-v1.json](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/responsible-closure-audit/artifacts/02-shipped-install-contract-classification-v1.json)

Future extracted-project boundary:
- the later standalone modifier repo should not extract `harness_modifier/` alone
- it should carry the modifier package together with the live overlay/install-materialization contract and installer entrypoints
- repo-local audit/governance tooling and installed-but-host-local compact-prompt bodies still require explicit classification before they travel

Current first-slice split:
- `contract/`
  - portable install/materialization contract helpers
  - runtime/install visibility and coherence helpers
  - bounded canary surfaces
- `closure/`
  - responsible-closure observation-record carrier and writer
  - responsible-closure host-exercise packet contract and writer
  - first observe-only host-exercise runner plus frozen host-evidence bundle support
  - shared exercise vocabulary owned at the packet layer and consumed by the observation writer
  - current posture: pre-run experimental / observe-only support, not a default materialized overlay family
- `capture/`
  - launch-truth capture
  - runtime snapshot capture
  - external CLI probe helpers
  - stream extraction helpers
- `compatibility/`
  - typed portable compatibility declaration
  - parity-baseline rules and held-annotation posture
  - first extraction artifact intended to travel unchanged into a later standalone project
- `overlay/`
  - authoritative first extraction tranche for specialist workflow and skill carriers
  - package-owned helper shims for moved workflow shells
  - current roster of generic, shared-boundary, and host-local overlay carriers

During the in-repo rehome step, the old `tooling/codex/*.py` paths remain as thin compatibility shims.
Active scripts, docs, and tests should prefer `harness_modifier/...` paths.
