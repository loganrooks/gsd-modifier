Date: 2026-04-22
Status: landed bounded classification pass

# Harness Modifier First Overlay Residue Classification Pass Implementation

## What Landed

- [d:r:i] The first specialist skill adapters now use source-side `__PROJECT_ROOT__` token abstraction in their `execution_context` and route text:
  - `harness_modifier/overlay/skills/gsd-uplift-project/SKILL.md`
  - `harness_modifier/overlay/skills/gsd-propagation-review/SKILL.md`
  - `harness_modifier/overlay/skills/gsd-seed-migration-inventory/SKILL.md`
- [d:r:i] Focused contract coverage now proves that explicit manifest source entries still render `__PROJECT_ROOT__` correctly through the materialization contract:
  - [../../../../tooling/codex/tests/test_portable_gsd_contract.py](../../../../tooling/codex/tests/test_portable_gsd_contract.py)

## Residue Classifications

### 1. Skill-adapter `execution_context` policy

- [d:r:i] Classification: `source-side token abstraction is the right posture now`.
- [d:r:i] Reason:
  - the authoritative source files now live under `harness_modifier/overlay/`
  - hard host-absolute paths in those sources were unnecessary residue from the host repo
  - the existing materialization contract already renders `__PROJECT_ROOT__` for explicit source entries
- [d:r:i] Result:
  - this residue is no longer held open
  - the moved skill adapters now carry the same source/install split more cleanly

### 2. Helper-shim versus helper-payload authority

- [d:r:i] Classification: `keep the current shim bridge explicit; helper-payload promotion remains later`.
- [d:r:i] Reason:
  - the first filesystem-rehome slice proved source/install separation for workflow shells and skill adapters
  - it did not yet prove that helper payloads should move out of `tooling/codex/`
  - the shims under `harness_modifier/overlay/helpers/` are currently a stable bridge, not yet the final helper-authority frontier
- [d:r:i] Result:
  - no helper-payload relocation lands in this slice
  - later extraction work should treat helper-payload promotion as its own bounded object

### 3. Default-source-root policy

- [d:r:i] Classification: `keep the current default root anchored at tooling/portable-gsd/overlay for now`.
- [d:r:i] Reason:
  - most tracked entries still live under the install-target mirror
  - explicit `source` indirection is now a typed exception, not yet a general migration posture
  - changing the default root now would widen the extraction family before more carriers have earned separate source homes
- [d:r:i] Result:
  - no root migration lands in this slice
  - external source entries remain deliberate, explicit, and sparse

### 4. Overwrite-mode source-indirection readiness

- [d:r:i] Classification: `not yet ready for a live exercise`.
- [d:r:i] Reason:
  - the first split only exercised `add`-mode entries
  - overwrite-mode carriers still carry backup-meta and pristine-frontier obligations that were not exercised by `148`
  - widening into overwrite-mode source indirection now would blend residue classification with a second live migration family
- [d:r:i] Result:
  - overwrite-family source indirection remains later
  - any later overwrite exercise should arrive only after a separate bounded readiness object

## Propagation Consequence

- [d:r:i] The first specialist source split now carries a cleaner source/install/materialization grammar:
  - source-side skill adapters no longer hardcode one host path
  - helper-payload promotion remains explicitly later rather than ambiently implied
  - the manifest default root remains stable while explicit source indirection stays the bounded widening mechanism
  - overwrite-family source indirection remains held until its own readiness slice exists

## Exact Next Move

- [d:r:i] Do not widen into a second filesystem tranche from this classification pass alone.
- [d:r:i] The next extraction object should come from one of the remaining explicit later pressures:
  - helper-payload authority
  - default-source-root migration pressure
  - overwrite-family source-indirection readiness
