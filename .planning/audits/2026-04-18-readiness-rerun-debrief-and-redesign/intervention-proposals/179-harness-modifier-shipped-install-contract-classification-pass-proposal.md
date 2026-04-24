Date: 2026-04-23
Status: revised proposal

# Harness Modifier Shipped/Install Contract Classification Pass Proposal

## Role

- [d:r:i] This proposal is the next bounded release-readiness object after the first actual observe-only host-evidence slice in `178`.
- [d:r:i] Its job is to classify the current shipped/install contract surface from real repo evidence rather than from package-only intuition or packet-only preparation.
- [g:r:i] It does not declare the modifier broadly deployable.

## Why This Proposal Is Active Now

- [d:r:i] `177` and responsible-closure lane `07` already sharpened the need to classify the shipped/install contract surface, not just `harness_modifier/` in isolation.
- [d:r:i] `178` now adds the first real host-evidence boundary:
  - observed-basis compatibility window: inside
  - modifier-side pristine/materialization marker: absent
  - full `verify_materialized`: intentionally deferred
  - resulting posture: read-side `shift-mode`
- [d:r:i] That means the modifier now has enough real evidence to stop speaking only in provisional productization abstractions, but not enough to widen into second-host, mixed-runtime, or write-side deployment claims.

## Review Consequence

- [d:r:i] Responsible-closure lane `08` returned `revise`, not reject.
- [d:r:i] Three load-bearing corrections are now accepted into this proposal:
  - widen the live shipped/install surface beyond `workflows/skills` to the fuller manifest-installed runtime carrier field
  - widen the install/materialization entrypoint inventory to include installer-executed helper and compact-prompt selection/body surfaces
  - split `tooling/codex/*` into typed shim-authority classes rather than treating it as one flat transitional bucket

## Primary Question

- [g:r:i] What is the cleanest current classification of the shipped/install contract surface across:
  - runtime-core
  - runtime-support
  - transitional shipped/install support
  - pre-run experimental
  - development-program-only
- [g:r:i] The answer should be grounded in actual invocation, install/materialization ownership, and audience posture rather than in family names alone.

## Scope

- [d:r:i] Classify the current shipped/install contract surface across:
  - `harness_modifier/` families
  - installer entrypoints
  - manifest-installed runtime carriers
  - live overlay exposure and invoked helper paths
  - remaining typed shim-authority paths still in the live contract
- [d:r:i] Preserve audience posture while classifying:
  - runtime user
  - contributing user
  - harness developer
- [d:r:i] Preserve install-profile pressure where it already exists, but do not implement feature-profile selection in this slice.

## Required Surface Inventory

- [d:r:i] Package families:
  - `harness_modifier/overlay/`
  - `harness_modifier/contract/`
  - `harness_modifier/compatibility/`
  - `harness_modifier/uplift/`
  - `harness_modifier/capture/`
  - `harness_modifier/closure/`
- [d:r:i] Install/materialization entrypoints:
  - `scripts/setup-portable-gsd.sh`
  - `tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json`
  - `harness_modifier/contract/portable_gsd_contract.py`
  - `harness_modifier/contract/ensure_gsd_sdk_runtime.py`
  - compact-prompt selection and body surfaces now chosen and materialized during install
- [d:r:i] Manifest-installed runtime carriers:
  - runtime config
  - agent carriers
  - patched CLI library surfaces
  - references
  - templates
  - workflows
  - skills
  - compact prompts
- [d:r:i] Live route exposure and helper/shim paths:
  - overlay routes that surface modifier-owned behavior or modifier-aware continuity
  - typed `tooling/codex/*` bridge classes that remain live:
    - modifier-facing transitional bridge
    - derivative/downstream bridge
    - stable repo-local tooling boundary

## Classification Outputs This Pass Must Produce

- [d:r:i] One explicit classification ledger for the current shipped/install contract surface.
- [d:r:i] One explicit audience-and-install-profile view showing:
  - what should travel in `core`
  - what likely belongs to optional later profiles such as `review-and-capture`, `uplift-and-propagation`, or `development-program`
  - what remains transitional and should not silently become permanent shipped shape
- [d:r:i] One explicit unresolved list for:
  - naming/reclassification pressure
  - still-blurred pre-run experimental surfaces
  - still-unsettled package versus installer ownership seams
- [d:r:i] One explicit rule for `installed but host-local / non-portable` surfaces so later classification can tell the truth about currently installed bodies that should not be treated as generic modifier-owned shipped carry.
- [d:r:i] One explicit evidence shape for each later ledger row:
  - current install/runtime relation
  - installer executes it
  - manifest materializes it
  - live route invokes it
  - authoritative home
  - current portability posture
  - audience pressure
  - later profile / rename / rehome pressure

## Required Judgment Constraints

- [g:r:i] Do not classify a surface as shipped merely because it sits in `harness_modifier/`.
- [g:r:i] Do not classify a surface as development-only merely because it is currently used mainly by this workspace.
- [g:r:i] Distinguish:
  - currently shipped by live install/materialization contract
  - currently reachable but transitional
  - currently present but not yet part of active runtime-facing behavior
- [g:r:i] Do not collapse all `tooling/codex/*` paths into one lifetime class when current authority maps already distinguish modifier-facing transitional bridges, downstream derivative bridges, and stable repo-local tooling boundaries.
- [g:r:i] Keep possible or virtual future surfaces explicit, but do not let them contaminate the classification of what actually ships now.

## Potential/Virtual Surface Handling

- [d:r:i] This pass should name possible or virtual later surfaces only in one bounded section:
  - likely future optional install profiles
  - likely future contributor-facing feedback/closure routes
  - likely later extracted standalone-repo product surfaces
- [d:r:i] Those surfaces should be marked as projected, not current shipped/install truth.

## Likely Pressure Points

- [d:r:i] `closure/` remains the clearest pre-run experimental family and should be judged from actual current invocation rather than from the word `closure`.
- [d:r:i] `capture/` may stay mixed across runtime-support and development-program-only postures.
- [d:r:i] Manifest-installed compact prompts are installed runtime bodies, but the current roster already marks them as host-local rather than generic modifier-owned carry; the classification pass must be able to say both parts at once.
- [d:r:i] Overlay workflows that mention modifier-owned support may pull some non-materialized helpers into the live shipped/install contract even if they are not themselves materialized into `.codex/get-shit-done`.
- [d:r:i] Compatibility shims do not share one authority lifetime; the pass must keep repo-local audit tooling, downstream derivative bridges, and modifier-facing transitional bridges distinct.

## Deliberate Boundaries

- [d:r:i] This slice does not implement install profiles.
- [d:r:i] This slice does not create CI.
- [d:r:i] This slice does not widen to second-host or mixed-runtime exercises.
- [d:r:i] This slice does not reopen `167`.
- [d:r:i] This slice does not extract to a standalone repo yet.
- [d:r:i] This slice does not decide final product-facing names for every pre-run or transitional family.

## Required Review Front

- [d:r:i] Run one bounded internal review over this proposal before implementation.
- [d:r:i] The review should test:
  - whether the object is scoped to the real shipped/install surface
  - whether audience and install-profile distinctions are carried cleanly
  - whether actual versus projected surfaces remain separate
  - whether current installed-but-host-local and typed shim-authority distinctions are preserved

## Primary Inputs

- [d:r:i] [166-harness-modifier-development-program-plan.md](166-harness-modifier-development-program-plan.md)
- [d:r:i] [177-harness-modifier-release-readiness-extraction-and-audience-split-plan.md](177-harness-modifier-release-readiness-extraction-and-audience-split-plan.md)
- [d:r:i] [178-harness-modifier-first-observe-only-host-exercise-implementation.md](178-harness-modifier-first-observe-only-host-exercise-implementation.md)
- [d:r:i] [../responsible-closure-audit/dispositions/10-harness-modifier-release-readiness-and-audience-split-plan-review-inheritance.md](../responsible-closure-audit/dispositions/10-harness-modifier-release-readiness-and-audience-split-plan-review-inheritance.md)
- [d:r:i] [../responsible-closure-audit/outputs/08-harness-modifier-shipped-install-contract-classification-pass-review-gpt54-xhigh-r1.md](../responsible-closure-audit/outputs/08-harness-modifier-shipped-install-contract-classification-pass-review-gpt54-xhigh-r1.md)
- [d:r:i] [../../../../harness_modifier/README.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/README.md)
- [d:r:i] [../../../../harness_modifier/overlay/ROSTER.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/ROSTER.md)
- [d:r:i] [../../../../scripts/setup-portable-gsd.sh](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh)
- [d:r:i] [../../../../tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json)
- [d:r:i] [../../../../harness_modifier/overlay/helpers/AUTHORITY-MAP.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/helpers/AUTHORITY-MAP.md)
- [d:r:i] [../../../../tooling/codex/README.md](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/README.md)

## Exact Next Move

1. [d:r:i] Audit this proposal on a bounded internal review basis.
2. [d:r:i] Land the first shipped/install-contract classification artifact from the reviewed object.
3. [d:r:i] Use that classified baseline to cut the next CI/install-profile/extraction tranche rather than reopening the classification question ambiently.
