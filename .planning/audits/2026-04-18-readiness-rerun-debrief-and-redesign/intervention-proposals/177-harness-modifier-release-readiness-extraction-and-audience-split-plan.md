Date: 2026-04-23
Status: active proposed plan

# Harness Modifier Release Readiness, Extraction, And Audience-Split Plan

## Role

- [g:r:i] This artifact is the bounded plan for moving the harness-modifier program toward responsible deployment pressure without collapsing that question into `ship now`.
- [g:r:i] It is not a declaration that the modifier is already ready for broad deployment.
- [g:r:i] It is also not a substitute for the current responsible-closure sequence.
- [d:r:i] Its job is to gather one newly sharpened cluster into a single governed object:
  - startup-grade predeployment review/testing expectations
  - CI expectations
  - repo extraction pressure
  - shipped-surface versus development-program-surface separation
  - audience split between harness users and harness developers
  - optionality and install-profile discipline

## Current Baseline

- [d:r:i] No GitHub Actions or other repo-local CI pipeline exists yet under `.github/workflows/`.
- [d:r:i] The modifier package now has a real package home under [../../../../harness_modifier/README.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/README.md), but it still lives inside the `prix-guesser` host repo.
- [d:r:i] The overlay manifest in [../../../../tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json) is currently the clearest declared answer to `what ships into the live runtime`.
- [d:r:i] The package tree under `harness_modifier/` is broader than the overlay surface:
  - `overlay/` contains product-facing workflow/skill carriers and helper shims
  - `contract/`, `compatibility/`, and `uplift/` contain runtime/install/support logic that materially affects shipped behavior
  - `capture/` and `closure/` contain a mixture of support machinery and pre-run responsible-closure machinery that is not yet fully classified as user-facing, developer-facing, or internal-only
- [d:r:i] The current responsible-closure sequence now has first real host evidence:
  - `175` landed the observation carrier/writer
  - `176` landed the host-exercise packet contract/writer
  - `178` landed the first actual observe-only host exercise
  - the first host run was inside the observed-basis compatibility window, but full modifier-side `verify_materialized` stayed deferred because the host did not yet carry `.codex/gsd-local-patches/backup-meta.json`
- [g:r:i] Harness-program horizons remain separate from `prix-guesser` product horizons.

## Why A Separate Plan Is Earned

- [d:r:i] The current field is now carrying two different improvement programs at once:
  - improving the harness as a deployable modifier product
  - improving the harness-development program itself
- [d:r:i] Those programs overlap, but they do not have the same audience, the same install surface, or the same review criteria.
- [d:r:i] Repo extraction pressure is no longer only a future packaging appetite. It is also a semantic-boundary and governance-boundary pressure.

## Inheritance And Adjacency

- [d:r:i] This plan inherits the active sequence already carried in [166](166-harness-modifier-development-program-plan.md), responsible-closure lane `06`, and the still-separate extraction object [167](167-harness-modifier-project-uplift-install-contract-pointer-neutralization-proposal.md).
- [d:r:i] It does not replace that sequence.
- [d:r:i] The current adjacency stays:
  - [179-harness-modifier-shipped-install-contract-classification-pass-proposal.md](179-harness-modifier-shipped-install-contract-classification-pass-proposal.md) next
  - `167` still sequential
  - second-host and mixed-runtime exercise widening only after the first real host-evidence slice is inherited

## Audience Split

- [g:r:i] Future productization should not assume one undifferentiated `user`.
- [d:r:i] The field now wants at least three audience postures:
  - `runtime user`
    - installs the modifier to improve a host harness locally
    - may use uplift/diagnostic routes
    - should not be forced to install development-program governance or pre-run experimental machinery by default
  - `contributing user`
    - installs the modifier in a host repo
    - can generate local uplift/diagnostic/adaptive artifacts
    - may propose improvements upstream, but is still not necessarily developing the modifier itself
  - `harness developer`
    - is developing the modifier itself
    - needs the full governance, audit, propagation, review, verifier, and release-program surfaces
- [d:r:i] Dogfooding belongs primarily to the `harness developer` posture, and becomes cleaner once the modifier has its own repo.
- [d:r:i] This split implies that some current package surfaces likely belong to different eventual install profiles rather than one default bundle.

## Shipped/Install Contract Classification Draft

- [d:r:i] The current field now wants a stricter classification pass than `ships` versus `meta`.
- [d:r:i] That pass should not stop at `harness_modifier/` alone.
- [d:r:i] It should classify the current shipped/install contract surface across:
  - `harness_modifier/` families
  - installer entrypoints
  - overlay workflows/skills that expose modifier behavior
  - remaining compatibility-shim paths still invoked from live routes
- [d:r:i] The current provisional classes should be:
  - `runtime-core`
    - overlay carriers materialized into `.codex/get-shit-done`
    - install/materialization contract helpers
    - compatibility declaration and runtime-support carriers required by live modifier behavior
  - `runtime-support`
    - non-materialized helper logic that supports runtime-facing workflows, verification, or updates
  - `pre-run experimental`
    - package-owned carriers that are real but not yet wired into active shipped workflow behavior
    - current leading example: `harness_modifier/closure/`
  - `development-program-only`
    - governance-program support for developing, reviewing, auditing, and releasing the modifier itself
- [d:r:i] The current `closure/` naming is best treated as a provisional program-family name, not yet a settled product-facing family classification.
- [d:r:i] The present evidence supports `pre-run experimental / not-default-shipped` more strongly than `developer-only forever`.
- [d:r:i] If `closure/` later becomes contributor-facing or runtime-adjacent, it should be reclassified or renamed around its actual product function rather than the current program-phase naming.

## Provisional Mapping Table

| Current family or entrypoint | Provisional tier | Likely audience posture | Likely install profile | Rename / reclassification pressure |
| --- | --- | --- | --- | --- |
| `harness_modifier/overlay/` | runtime-core | runtime user, contributing user | core | low |
| `harness_modifier/contract/` | runtime-core | runtime user, harness developer | core | low |
| `harness_modifier/compatibility/` | runtime-core | runtime user, harness developer | core | low |
| `harness_modifier/uplift/` | runtime-support | contributing user, harness developer | uplift-and-propagation | medium |
| `harness_modifier/capture/` | mixed runtime-support / development-only | contributing user, harness developer | review-and-capture or development-program | medium |
| `harness_modifier/closure/` | pre-run experimental | contributing user or harness developer, still unresolved | review-and-capture or development-program later | high |
| `scripts/setup-portable-gsd.sh` | install entrypoint | runtime user, contributing user, harness developer | core | low |
| `tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json` | install/materialization contract | harness developer, runtime support operators | core | low |
| live overlay workflows/skills exposing modifier behavior | runtime-core or runtime-support depending on route | runtime user, contributing user | core or uplift-and-propagation | medium |
| `tooling/codex/*` compatibility shims | transitional shipped/install support | harness developer, contributing user | transitional only | high |

## Product Review Requirements Before Broader Deployment Pressure

- [g:r:i] If this were a startup product, broader deployment pressure would require more than unit tests and ad hoc audit memory.
- [d:r:i] The required review families would be:
  - `release architecture review`
    - package boundary
    - shipped surface classification
    - optionality model
    - install/upgrade/remove semantics
  - `runtime safety and non-destructive behavior review`
    - observe-only versus write-side guarantees
    - clean-worktree assumptions
    - path targeting
    - host disjointness rules
  - `installer/materialization review`
    - manifest correctness
    - overwrite/add semantics
    - pristine capture semantics
    - post-materialization verification
  - `host-context test review`
    - fresh host
    - upgraded host
    - drifted host
    - codex-only first
    - claude-specific later, when the parity family earns it
  - `observability/recovery review`
    - launch truth
    - timing capture
    - failure salvage
    - output-path traceability
  - `release governance review`
    - versioning
    - compatibility declaration
    - changelog and release notes discipline
    - support posture and rollback story

## Testing Requirements Before Broader Deployment Pressure

- [d:r:i] The testing stack should be layered:
  - `package/unit`
    - compile
    - unit tests for each carrier/writer/contract helper
  - `contract`
    - manifest validation
    - install/materialization strict verification
    - route contract tests
  - `fixture host integration`
    - synthetic fixture repos for:
      - fresh regular-GSD codex host
      - aged/drifted codex host
      - later claude host
      - later mixed-runtime host if earned
  - `observe-only exercise`
    - first real disjoint host run
    - packet + observation + output-target verification
  - `upgrade/regression`
    - reinstall after upstream movement
    - compatibility declaration still respected
    - overlay manifest still coherent
- [g:r:i] The first actual host exercise is still a prerequisite to claiming stronger deployability knowledge.

## CI Matrix

- [d:r:i] The current repo has no CI, so the first serious CI should be explicit and tiered rather than one undifferentiated matrix.
- [d:r:i] Tier `A` should be deterministic and package-owned:
  - `python3 tooling/codex/audit_refmap.py verify ...`
  - `git diff --check`
  - JSON validation over carrier files
  - `python3 -m py_compile` for package helpers
  - focused unittest suites
  - `portable_gsd_contract.py validate-manifest`
  - `portable_gsd_contract.py verify-materialized --strict` when it can run from already-materialized local state
- [d:r:i] Tier `B` should be slower integration/materialization smoke:
  - [../../../../scripts/setup-portable-gsd.sh](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh)
  - fresh local materialization smoke
  - synthetic host install/materialization checks
  - later observe-only host packet exercise in CI-compatible form if that becomes reproducible
- [d:r:i] Tier `C` should remain later and extraction-facing:
  - standalone package build/install smoke
  - compatibility declaration validation in the extracted repo
  - release packaging checks
- [d:r:i] Threshold-language scanning should remain intake-oriented, not a release gate by itself.

## Optionality Model

- [g:r:i] Optionality should not mean `present in the repo but hopefully harmless if unused`.
- [d:r:i] The modifier now wants explicit install profiles, at least later:
  - `core`
  - `review-and-capture`
  - `uplift-and-propagation`
  - `development-program`
- [d:r:i] A robust optionality model would require:
  - declared feature/profile manifest
  - install-time selection
  - dependency rules between profiles
  - smoke tests proving core still works when higher profiles are absent
  - route-level documentation of what each profile adds

## Extraction Pressure

- [g:r:i] Extraction to a dedicated repo is now an earned near-term direction, not a speculative long-later appetite.
- [d:r:i] The likely eventual target remains a repo like `~/workspace/projects/gsd-modifier`.
- [d:r:i] That extracted project should not be modeled as `harness_modifier/` alone.
- [d:r:i] The future extracted project currently wants at least:
  - the modifier package families under `harness_modifier/`
  - the live overlay/install-materialization contract that still routes through `tooling/portable-gsd/overlay/`
  - installer entrypoints such as `scripts/setup-portable-gsd.sh`
  - tests, fixtures, and release/readiness surfaces that belong to the modifier product rather than to one host repo
- [d:r:i] Host-local and repo-local-only surfaces should remain distinct during that extraction:
  - compact-prompt bodies that are installed but host-local / non-portable
  - repo-local audit/governance tooling that supports modifier development but is not part of the runtime product contract
- [d:r:i] The extraction sequence should stay bounded:
  1. classify the current shipped/install contract surface by audience and shipping tier
  2. keep finishing the current responsible-closure first-host sequence
  3. separate shipped runtime surfaces from development-program-only surfaces
  4. create the standalone repo once the first shipping-tier map is explicit and durable enough to avoid immediate re-splitting, and use that map to move the package plus overlay/install contract as one project rather than repeating the current transitional split
  5. add first-class Codex and Claude developer onboarding there so ongoing harness-modifier development can actually relocate cleanly
  6. add package CI and fixture hosts there
- [d:r:i] Repo extraction should not wait for every possible improvement to end.
- [d:r:i] It should wait for enough classification and first-host closure that the extracted project does not immediately need a second semantic split.
- [d:r:i] The later strategic question of `modifier route versus own harness` should remain explicit, but it is not part of the current extraction gate. The active route remains the modifier path until responsible closure and first deployable extraction boundaries are materially sharper.

## What This Plan Does Not Claim

- [d:r:i] It does not claim that the current package boundary is already correct.
- [d:r:i] It does not claim that extracting `harness_modifier/` by itself would produce the right standalone project boundary.
- [d:r:i] It does not claim that `closure/` should definitely remain a shipped product family name.
- [d:r:i] It does not claim that all current package helpers should be user-installable.
- [d:r:i] It does not claim that the modifier is already ready for broad deployment in internal repos.
- [d:r:i] It does not collapse harness users and harness developers into the same install/use posture.
- [d:r:i] It does not settle the later strategic question of `modifier route versus own harness`.

## Short Horizon

- [d:r:i] Use the first responsible-closure host-evidence slice as the entry proof:
  - one actual observe-only host exercise is now frozen
  - no write-side widening was taken
  - no mixed-host widening was taken
- [d:r:i] Open one bounded `shipped/install contract classification` pass across:
  - `harness_modifier/` families
  - installer entrypoints
  - live overlay workflows/skills that expose modifier behavior
  - remaining compatibility-shim paths still in the live contract
- [d:r:i] Open one bounded release-readiness / CI / install-profile proposal after that classification pass.

## Medium Horizon

- [d:r:i] Stand up extracted-repo bootstrap and developer onboarding before real CI implementation becomes the main focus.
- [d:r:i] Classify which current development-program surfaces should never ship by default.
- [d:r:i] Open the dedicated extraction tranche into a standalone repo once the audience/profile map is explicit.

## Long Horizon

- [d:r:i] Standalone repo
- [d:r:i] package / `npx` distribution
- [d:r:i] multiple host-context deployment exercises
- [d:r:i] stronger adaptive feedback and discrepancy capture after real host usage begins

## Exact Next Moves

1. [d:r:i] Keep the first actual observe-only host evidence slice as the accepted boundary; do not reinterpret it as write-side deployment proof.
2. [d:r:i] Open one bounded `shipping-tier + audience-split classification` proposal across the current shipped/install contract surface rather than `harness_modifier/` alone.
3. [d:r:i] Use that classification proposal to decide:
   - what ships by default
   - what stays optional
   - what is development-program-only
   - whether `closure/` keeps its current name or gets reclassified
4. [d:r:i] Then open one bounded `release-readiness and CI tranche` proposal.
5. [d:r:i] Keep standalone repo extraction as the next adjacent structural move once the classification pass and first host run are both in hand.
