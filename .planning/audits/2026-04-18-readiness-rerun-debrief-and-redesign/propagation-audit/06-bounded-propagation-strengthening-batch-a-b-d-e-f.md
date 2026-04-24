Date: 2026-04-21
Status: landed bounded strengthening batch

# Bounded Propagation Strengthening Batch A B D E F

## Purpose

- [g:r:i] This note records the first bounded strengthening batch inherited from the Opus propagation reread.
- [g:r:i] The job of this batch is not to widen the family into additive install or whole-network challenge. The job is to intensify the current two-consumer baseline where the reread exposed under-carried edges.

## What Landed

- [e:r:i] Route A landed as a regressible producer-to-consumer contract test:
  - `tooling/codex/project_uplift.py` now exposes a small render-contract vocabulary
  - `test_project_uplift.py` now verifies the producer note keys and the prose labels carried by both overlay workflows stay in tune
- [e:r:i] Route B landed as typed held-later carry:
  - [UPLIFT-HELD-LATER.md](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/UPLIFT-HELD-LATER.md) now records `held` vs `partially landed`
  - `project_uplift.py` now parses and writes structured held-later objects
  - `.planning/UPLIFT-MANIFEST.json` now carries `schema_version: 3`
  - `.planning/UPLIFT-REPORT.md` now renders typed held-later entries
- [e:r:i] Route D landed as tracked overlay ownership for the read-only consumer skills:
  - [gsd-progress/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/skills/gsd-progress/SKILL.md)
  - [gsd-resume-work/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/skills/gsd-resume-work/SKILL.md)
- [e:r:i] Route E landed as a dedicated chain-flow disclosure artifact:
  - [05-project-uplift-chain-map.md](05-project-uplift-chain-map.md)
- [e:r:i] Route F landed as stronger governance/discovery routing:
  - [tooling/codex/README.md](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/README.md) now names the live consumers, durable outputs, and audit lineage for `project_uplift.py`
  - [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md) now points the contract-propagation rule at the worked-example `propagation-audit/` family

## Materialization And Output Consequence

- [e:r:i] `python3 tooling/codex/project_uplift.py detect . --write --json` was rerun after the helper and held-later changes landed.
- [e:r:i] `./scripts/setup-portable-gsd.sh` was rerun after the new overlay skill owners landed.
- [e:r:i] The live `.codex` runtime now carries the tracked `gsd-progress` and `gsd-resume-work` skill owners as well as the earlier workflow owners.

## Review And Verification Gates

### Tooling Gates

- [e:r:i] `python3 -m py_compile tooling/codex/project_uplift.py`
- [e:r:i] `python3 -m unittest tooling.codex.tests.test_project_uplift`

### Materialization And Output Gates

- [e:r:i] real repo write refresh of uplift outputs
- [e:r:i] installer rerun for overlay -> live materialization
- [e:r:i] typed held-later entries now appear in manifest/report outputs

### Governance Gates

- [e:r:i] threshold scan on the touched request/governance/tooling surfaces
- [e:r:i] `audit_refmap.py verify` on the audit root
- [e:r:i] `git diff --check`

## What This Batch Still Holds

- [d:r:i] Route C stays next rather than absorbed here:
  - overlay add-vs-overwrite manifest
- [d:r:i] Route G stays dependent on C:
  - post-materialization coherence gate
- [d:r:i] Later families remain later:
  - third consumer
  - additive install routing
  - cross-runtime reconciliation
  - broader whole-network challenge

## Current Consequence

- [d:r:i] The current propagation chain is now stronger at five concrete edges:
  - helper JSON contract
  - held-later registry semantics
  - read-only consumer skill ownership
  - chain-flow disclosure
  - governance/discovery routing
- [d:r:i] The next bounded move is Route C, then Route G on top of it, unless a still-stronger local need emerges first.
