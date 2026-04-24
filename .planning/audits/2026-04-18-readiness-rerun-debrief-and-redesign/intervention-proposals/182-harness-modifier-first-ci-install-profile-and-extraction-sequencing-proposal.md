Date: 2026-04-23
Status: active proposal

# Harness Modifier Extracted-Repo Bootstrap, Onboarding, And CI Sequencing Proposal

## Role

- [d:r:i] This proposal is the next bounded release-readiness object after the landed shipped/install classification slice in `180`.
- [d:r:i] Its job is to turn the newly durable classification baseline into one sequenced answer for:
  - extracted-repo bootstrap
  - developer onboarding for Codex and Claude
  - CI sequencing
  - install-profile sequencing
  - extracted-project sequencing
- [g:r:i] It does not implement CI in this slice.
- [g:r:i] It does not create the standalone repo in this slice either.
- [g:r:i] It does not reopen `modifier route versus own harness` as the active decision front.
- [d:r:i] The accepted route answer now lands through [183-harness-modifier-filtered-history-bootstrap-and-onboarding-route.md](183-harness-modifier-filtered-history-bootstrap-and-onboarding-route.md).

## Why This Proposal Is Active Now

- [d:r:i] `177` already made CI, optionality, and extraction pressure explicit as the next productization cluster.
- [d:r:i] `180` now supplies the first durable baseline for that cluster:
  - runtime-core
  - runtime-support
  - transitional shipped/install support
  - pre-run experimental
  - development-program-only
- [d:r:i] `181` now keeps two strategic boundary conditions explicit:
  - the later standalone project should carry the modifier package plus the live overlay/install-materialization contract
  - the later `modifier route versus own harness` question stays deferred until responsible closure sharpens farther

## Primary Question

- [g:r:i] What is the strongest first sequencing answer for extracted-repo bootstrap, developer onboarding, CI, install profiles, and repo extraction once the shipped/install contract surface is classified but not yet broadly deployed?

## Scope

- [d:r:i] Shape the first extracted-repo bootstrap answer:
  - what moves into the first standalone repo cut
  - what stays behind as host-local or development-program-only
  - what repo skeleton and top-level layout the extracted project needs
  - what Codex and Claude developer onboarding surfaces should exist on day one so development can continue there cleanly
- [d:r:i] Shape CI sequencing across three tiers rather than treating it as the first implementation move:
  - deterministic/package-owned gates
  - slower integration/materialization smoke
  - later release-packaging checks
- [d:r:i] Shape install-profile sequencing across the currently visible profile pressure:
  - `core`
  - `uplift-and-propagation`
  - `review-and-capture`
  - `development-program`
  - host-local-only or non-portable carveouts where needed
- [d:r:i] Shape the extraction sequence into a standalone project that carries:
  - `harness_modifier/`
  - the live overlay/install-materialization contract
  - installer entrypoints
  - tests / fixtures / release-readiness carriers that belong to the modifier product rather than to one host repo

## Required Inputs

- [d:r:i] [177-harness-modifier-release-readiness-extraction-and-audience-split-plan.md](177-harness-modifier-release-readiness-extraction-and-audience-split-plan.md)
- [d:r:i] [179-harness-modifier-shipped-install-contract-classification-pass-proposal.md](179-harness-modifier-shipped-install-contract-classification-pass-proposal.md)
- [d:r:i] [180-harness-modifier-shipped-install-contract-classification-first-slice-implementation.md](180-harness-modifier-shipped-install-contract-classification-first-slice-implementation.md)
- [d:r:i] [181-harness-modifier-route-vs-own-harness-strategy-deferral-note.md](181-harness-modifier-route-vs-own-harness-strategy-deferral-note.md)
- [d:r:i] [../responsible-closure-audit/artifacts/02-shipped-install-contract-classification-v1.json](../responsible-closure-audit/artifacts/02-shipped-install-contract-classification-v1.json)
- [d:r:i] [../../../../harness_modifier/README.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/README.md)
- [d:r:i] [../../../../scripts/setup-portable-gsd.sh](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh)
- [d:r:i] [../../../../tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json)

## Required Outputs

- [d:r:i] One explicit recommendation for what belongs in the first extracted-repo bootstrap tranche.
- [d:r:i] One explicit recommendation for what onboarding surfaces the extracted repo must carry before development shifts there:
  - Codex startup/onboarding
  - Claude startup/onboarding
  - local verify/test/install commands
  - runtime-vs-development-surface explanation
- [d:r:i] One explicit recommendation for what belongs in the first CI tranche after bootstrap exists.
- [d:r:i] One explicit recommendation for what remains later CI rather than being forced into the first tranche.
- [d:r:i] One explicit install-profile sequencing answer:
  - what should remain one default bundle for now
  - what should first be documented as pressure before implementation
  - what should stay explicitly later because the dependency graph still needs sharper stabilization first
- [d:r:i] One explicit extraction sequence that says:
  - what moves together into the standalone project
  - what stays behind as host-local or development-program-only
  - what transitional bridges must remain visible during migration

## Judgment Constraints

- [g:r:i] Do not treat CI as one flat yes/no question.
- [g:r:i] Do not let CI implementation outrun extracted-repo bootstrap and developer onboarding.
- [g:r:i] Do not treat install profiles as if they must all be implemented at once.
- [g:r:i] Do not let extracted-project planning collapse back into `move harness_modifier/`.
- [g:r:i] Do not let the later `modifier route versus own harness` question reconsume this bounded object.
- [g:r:i] Keep second-host and mixed-runtime exercise widening explicitly later unless this proposal can justify a narrow prerequisite with real evidence.

## Deliberate Boundaries

- [d:r:i] This slice does not implement GitHub Actions or other CI yet.
- [d:r:i] This slice does not implement install-profile selection.
- [d:r:i] This slice does not reopen `167`.
- [d:r:i] This slice does not broaden `.claude` materialization claims.
- [d:r:i] This slice does not settle the later `modifier route versus own harness` strategy question.

## Exact Next Move

1. [d:r:i] Review this proposal against the classified baseline in `180`.
2. [d:r:i] Land one bounded sequencing answer for:
   - extracted-repo bootstrap
   - Codex/Claude developer onboarding
   - first CI tranche after bootstrap exists
   - install-profile staging
   - extracted-project migration order
3. [d:r:i] Only after that, decide whether the next boundary is:
   - extraction scaffolding
   - developer-onboarding/bootstrap implementation inside the new repo
   - actual CI implementation
   - or a narrower optionality/profile contract slice
