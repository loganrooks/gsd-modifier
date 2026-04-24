Date: 2026-04-23
Status: completed implementation

# Harness Modifier Shipped/Install Contract Classification First Slice

## Role

- [d:r:i] This slice lands the first durable shipped/install-contract classification artifact after revised `179` and responsible-closure lane `08`.
- [d:r:i] Its job is to turn the release-readiness classification question into an explicit ledger rather than leaving it in review prose alone.

## What Landed

- [d:r:i] The first durable ledger now exists at:
  - [../responsible-closure-audit/artifacts/02-shipped-install-contract-classification-v1.json](../responsible-closure-audit/artifacts/02-shipped-install-contract-classification-v1.json)
- [d:r:i] [../../../../harness_modifier/README.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/README.md) now exposes the current shipped/install posture in package-facing form instead of leaving that distinction only inside the audit tree.

## Current Classification Result

- [d:r:i] `runtime-core`
  - installer entrypoint
  - installer-executed runtime verifier
  - manifest/materialization contract
  - installed runtime config, agents, patched CLI libs, references, templates, overwrite workflows and overwrite skills
  - package `contract/` and `compatibility/`
- [d:r:i] `runtime-support`
  - additive modifier workflows and skills
  - package `uplift/`
  - package `capture/`
- [d:r:i] `transitional-shipped-install-support`
  - installed compact prompts that are still host-local / non-portable
  - `project_uplift.py` modifier-facing transitional bridge
  - `seed_migration_inventory.py` downstream derivative bridge
  - thin `tooling/codex/` compatibility shims whose authoritative homes now live under `harness_modifier/`
- [d:r:i] `pre-run-experimental`
  - package `closure/`
- [d:r:i] `development-program-only`
  - repo-local audit-tooling boundary such as `audit_refmap.py`

## Design Consequence

- [d:r:i] The shipped/install question is no longer only `what lives in harness_modifier/`.
- [d:r:i] The future extracted-project boundary is therefore no longer blurred either:
  - do not extract `harness_modifier/` alone
  - move the modifier package together with the live overlay/install-materialization contract and installer entrypoints when the extraction tranche opens
- [d:r:i] The artifact now distinguishes:
  - installed runtime carriers
  - package homes
  - helper bridges
  - host-local installed doctrine bodies
  - repo-local development tooling boundaries
- [d:r:i] The compact-prompt case is now explicit rather than blurred:
  - installed now
  - but host-local / non-portable
- [d:r:i] The `tooling/codex/` question is also now typed:
  - modifier-facing transitional bridge
  - derivative/downstream bridge
  - thin compatibility shims
  - stable repo-local tooling boundary

## Deliberate Boundaries

- [d:r:i] This slice does not implement install-profile selection.
- [d:r:i] This slice does not create CI.
- [d:r:i] This slice does not reopen second-host or mixed-runtime exercise widening.
- [d:r:i] This slice does not reopen `167`.
- [d:r:i] This slice does not yet move the modifier into its own repo.

## Verification

- [d:r:i] `python3 tooling/codex/audit_refmap.py verify .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign`
- [d:r:i] `python3 -m json.tool .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/responsible-closure-audit/artifacts/02-shipped-install-contract-classification-v1.json && python3 -m json.tool .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/propagation-audit/artifacts/05-propagation-registry-v2-evidence-index.json && python3 -m json.tool .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/propagation-audit/artifacts/06-propagation-registry-v2-coverage-and-refresh.json`
- [d:r:i] `python3 tooling/codex/scan_threshold_language.py --ignore-meta-instruction-lines .planning/HARNESS-IMPROVEMENT-REGISTER.md .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/CURRENT-STATE.md .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/STATUS.md .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/INDEX.md .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/166-harness-modifier-development-program-plan.md .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/177-harness-modifier-release-readiness-extraction-and-audience-split-plan.md .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/180-harness-modifier-shipped-install-contract-classification-first-slice-implementation.md .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/181-harness-modifier-route-vs-own-harness-strategy-deferral-note.md .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/README.md .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/responsible-closure-audit/README.md .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/propagation-audit/README.md .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/propagation-audit/65-responsible-closure-shipped-install-contract-classification-first-slice-change-triggered-refresh.md harness_modifier/README.md`
- [d:r:i] `git diff --check`

## Exact Next Move

1. [d:r:i] Use the classified baseline to cut the next CI/install-profile/extraction sequencing object rather than reopening the classification question.
   - current bounded object: [182-harness-modifier-first-ci-install-profile-and-extraction-sequencing-proposal.md](182-harness-modifier-first-ci-install-profile-and-extraction-sequencing-proposal.md)
2. [d:r:i] Keep `167` sequential and explicit.
3. [d:r:i] Keep the later `modifier route versus own harness` strategic question explicit through [181-harness-modifier-route-vs-own-harness-strategy-deferral-note.md](181-harness-modifier-route-vs-own-harness-strategy-deferral-note.md), but do not let it consume the current responsible-closure queue.
4. [d:r:i] Keep second-host and mixed-runtime exercises later until the classified baseline has first been used on the release-readiness side.
