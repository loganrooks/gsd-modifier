Date: 2026-04-23
Status: revised after lane-05 audit

# Harness Modifier Responsible Closure First Bundle Field Map

## Role

- [d:r:i] This artifact defines the first bounded responsible-closure bundle that follows the landed development-side protocol slice.
- [d:r:i] Its job is to keep the next deployability and adaptive-feedback work split into clean carriers instead of flattening it into one vague `telemetry` or `deployment readiness` object.

## Why This Bundle Is Next

- [d:r:i] The current baseline is now cleaner:
  - [169-harness-modifier-development-parallelization-and-intervention-lifecycle-protocol-consolidation-proposal.md](169-harness-modifier-development-parallelization-and-intervention-lifecycle-protocol-consolidation-proposal.md) is no longer the active next object because its first slice already landed through [171-harness-modifier-development-protocol-first-slice-implementation.md](171-harness-modifier-development-protocol-first-slice-implementation.md).
  - [167-harness-modifier-project-uplift-install-contract-pointer-neutralization-proposal.md](167-harness-modifier-project-uplift-install-contract-pointer-neutralization-proposal.md) remains explicit and sequential, but it is not the immediate next family according to [166-harness-modifier-development-program-plan.md](166-harness-modifier-development-program-plan.md) and [CURRENT-STATE.md](../CURRENT-STATE.md).
- [d:r:i] The next stronger gain is to make the responsible-closure bundle concrete enough that it can be challenged, implemented, and later exercised without reconstructing the field from route note [161-harness-modifier-responsible-closure-deployability-and-adaptive-feedback-route.md](161-harness-modifier-responsible-closure-deployability-and-adaptive-feedback-route.md) or from chat memory.

## Bundle Split

### 1. Observation Carrier Proposal

- [d:r:i] This carrier owns the durable observe-only record for one host exercise.
- [d:r:i] It owns observation-record shape, not packet vocabulary.
- [d:r:i] It should carry the five-family partition inherited from responsible-closure lane `01`:
  - `deployment-context`
  - `expectation-vs-observation`
  - `semantic-deviation`
  - `positive-gain`
  - `measurement-provenance`
- [d:r:i] It should stay:
  - observe-only
  - operator-triggered
  - single-writer
  - keyed to one host exercise
  - split-provenance rather than flat runtime memory
- [d:r:i] It should absorb the bounded transfer now fixed in [../responsible-closure-audit/dispositions/05-reflect-reference-sidecar-inheritance.md](../responsible-closure-audit/dispositions/05-reflect-reference-sidecar-inheritance.md):
  - `provenance_schema: v2_split`
  - `detected_by`
  - `written_by`
  - `about_work`
  - `signal_subtype`
  - `evidence_family`
  - `disposition`
  - `automation_level`
  - `automation_skip_reasons`
- [d:r:i] First physical form is now explicitly JSON-only, with only an optional in-record `narrative_summary` if later quick interpretation proves necessary.

### 2. Host-Exercise Packet Proposal

- [d:r:i] This carrier owns the first disjoint-host exercise shape.
- [d:r:i] It owns shared exercise vocabulary and packet-side scope rules; the observation carrier should reference those fields rather than redeclare them.
- [d:r:i] It should define:
  - target host class
  - preconditions
  - exact reads/checks to run
  - what outputs must be captured
  - what must not be written into the host's own planning tree
  - abort / hold conditions if the host posture falls outside the current compatibility declaration
- [d:r:i] It should remain a packet/proposal first, not a run claim.
- [d:r:i] It should now carry a tighter packet vocabulary rather than leaving these fields ambient:
  - `exercise_id`
  - `host_shape`
  - `declaration_posture`
  - `observed_basis_runtime`
  - `held_annotation_runtime`
  - `compatibility_window_state`
  - `skip_reason`
  - `check_outcome`
  - `runtime_visibility_snapshot_path`
  - `verify_materialized_summary`
- [d:r:i] The first host target is now narrower than `disjoint .codex host` in the abstract:
  - disjoint `.codex`-only
  - regular GSD already installed
  - no Reflect artifacts
  - clean worktree
  - known basis commit
  - no coupling to `prix-guesser`

### 3. Later Exercise Run

- [d:r:i] The actual observe-only host run remains the third step, not the second.
- [d:r:i] This keeps the dependency chain explicit:
  - field map
  - observation carrier proposal
  - host-exercise packet proposal
  - later observe-only run

## Ownership Direction

- [g:r:i] `172` is an index-plus-sequencing carrier only.
- [g:r:i] `174` owns exercise vocabulary and packet-side scope.
- [g:r:i] `173` owns observation-record shape and durable carry.
- [d:r:i] Shared fields should be declared once in `174` and then referenced from `173`, not redeclared as a second competing vocabulary layer.
- [d:r:i] `172` should not grow a second vocabulary list, a second transfer-now table, or a second held-later table beyond what already lives in `173`, `174`, and the responsible-closure dispositions.

## Target Split

- [d:r:i] This bundle is mainly a combined `distribution/deployability` plus `harness-adaptive` move.
- [d:r:i] It also touches:
  - `harness-operational`, because observation writing needs provenance, disposition, and run-home discipline
  - `harness-agential`, because later review should be able to read what broadened or narrowed without collapsing the work into readiness-gate thinking
- [d:r:i] It is not:
  - a harness-in-action workflow parallelization rewrite
  - a standalone repo extraction move
  - a full GSD Reflect telemetry import

## First Host Target

- [d:r:i] The first packet should prefer a disjoint `.codex` host because it exercises travel without simultaneously widening `.claude` materialization claims.
- [d:r:i] A mixed `.codex` + held-annotation `.claude` host remains the stronger second exercise when earned, because it tests the held parity posture carried in [141-harness-modifier-compatibility-declaration-carrier-implementation.md](141-harness-modifier-compatibility-declaration-carrier-implementation.md).

## Parallelization Stance

- [d:r:i] Development-side overlap can still help this bundle, but it should stay inside the classes already diagnosed by `parallelization-audit/`:
  - safe earned:
    - read-only reference mapping while the parent thread drafts the bundle
    - later cross-vendor reread while unrelated non-single-writer governance carry proceeds
  - promising but not-yet-governed:
    - fan-out verification/review scheduling against the first landed observation or host-exercise slice
  - likely coherence/quality risk:
    - concurrent writes to single-writer governance surfaces
    - installer/materialization rewrites during a frozen-basis external lane
- [d:r:i] This bundle should therefore inherit the development-side protocol and not reopen the broader harness parallelization field.

## Explicitly Later

- [d:r:i] The actual observe-only run
- [d:r:i] Mixed-host `.codex` + `.claude` exercise
- [d:r:i] `durability` ladder and recurrence fields
- [d:r:i] severity fields
- [d:r:i] full `runtime/derived/modifier` lineage doctrine
- [d:r:i] reflection/pattern loop
- [d:r:i] automation-level behavior beyond explicit operator-triggered posture
- [d:r:i] Auto-collection
- [d:r:i] Sensor / synthesizer / reflector machinery
- [d:r:i] Lifecycle state machine
- [d:r:i] Cross-project aggregation
- [d:r:i] Standalone repo extraction widening
- [d:r:i] `167` install-contract pointer neutralization

## Exact Next Move

1. [d:r:i] Treat responsible-closure lane `05` as the completed audit over `172 + 173 + 174`.
2. [d:r:i] Keep the bundle at three proposals with the ownership split above.
3. [d:r:i] Open the observation-carrier writer as the first implementation slice.
4. [d:r:i] Open the host-exercise packet contract as the second implementation slice.
5. [d:r:i] Keep the actual observe-only host run later, after both preceding slices are landed and reread.
