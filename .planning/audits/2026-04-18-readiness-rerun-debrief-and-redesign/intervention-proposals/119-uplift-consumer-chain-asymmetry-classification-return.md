Date: 2026-04-22
Status: active bounded classification return

# Uplift Consumer-Chain Asymmetry Classification Return

## Purpose

- [g:r:i] Convert the accepted `118` proposal into a per-carrier classification return before any ≤2-carrier implementation slice opens.
- [g:r:i] The target is not to implement consumer carry yet.
- [g:r:i] The target is to make the silent-carrier field explicit enough that the first implementation slice can be chosen deliberately instead of from prose memory.

## Classification Frame

- [d:r:i] Each carrier or carrier-group receives:
  - one primary classification:
    - `deepen in place`
    - `attach through a shared reference`
    - `explicitly held`
  - one surfacing direction when materially relevant:
    - `read-only`
    - `write-recommending`

## Carrier Returns

- [d:r:i] `transition.md` + `templates/state.md`
  - classification: `deepen in place`
  - surfacing direction: `read-only`
  - reason: the transition/state-continuity pair already carries compact continuity structure parallel to the scalar uplift summary, so held-runtime awareness can deepen without first inventing a shared external carrier

- [d:r:i] `new-milestone.md` + `complete-milestone.md`
  - classification: `attach through a shared reference`
  - surfacing direction: `read-only`
  - reason: milestone-boundary carry already depends on shared reading doctrine and can inherit held-runtime posture through one common reference surface rather than through two separate boundary-specific expansions

- [d:r:i] `health.md`
  - classification: `deepen in place`
  - surfacing direction: `read-only`
  - reason: the repair route already distinguishes structural repair, validation, and later uplift posture, so held-runtime awareness can travel as bounded additional carry rather than as a new reference regime

- [d:r:i] read-packet doctrine + initialization / ingest + repair / migration + update carriers
  - classification: `attach through a shared reference`
  - surfacing direction: `read-only`
  - reason: these carriers already cluster around `mandatory-initial-read.md`, so widening them through a shared reference keeps the field coherent and avoids a spray of per-route prose edits

- [d:r:i] verifier lifecycle carriers
  - classification: `explicitly held`
  - reason: held-runtime awareness at verification time would widen the question from surfacing posture into compatibility judgment under future-preservation review, which this family is not yet answering

- [d:r:i] discuss / plan / execute entry points
  - classification: `explicitly held`
  - reason: these routes share the same inventory as family-6 wider route mapping, so classifying them for held-runtime surfacing must not silently pre-answer the registry-versus-translation-versus-doctrine split that family-6 still owns

- [d:r:i] `propagation-review` route
  - classification: `deepen in place`
  - surfacing direction: `read-only`
  - reason: the route already carries durable-note placement and explicit tool-result-to-disposition logic, so bounded held-runtime disclosure can deepen there without broadening into a new reference family

- [d:r:i] setup / materialization bridge (`propagation 20`)
  - classification: `explicitly held`
  - reason: the installer entry, `gsd-sdk` helper, and pristine-capture stage sit at the install/runtime frontier rather than the current consumer frontier; they stay visible in the inventory, but the first consumer slice should not widen install semantics and consumer semantics together

- [d:r:i] helper-side `RUNTIME_DIRS` versus `HELD_CLAUDE_RUNTIME_VERSION_REL_PATH` asymmetry
  - classification: `explicitly held`
  - reason: this is a helper-clarity widening and later third-runtime frontier, not the first consumer-carry slice

- [d:r:i] write-recommending drift path in `project_uplift.py`
  - classification: `explicitly held`
  - surfacing direction: `write-recommending`
  - reason: `compatibility_drift_reasons` should remain a bounded drift detector for now rather than widening into a generic write-side dispatcher during the first consumer-carry tranche

## Immediate Priority Order

- [d:r:i] first candidate pair:
  - `transition.md` + `templates/state.md`
- [d:r:i] second candidate pair:
  - `new-milestone.md` + `complete-milestone.md` through a shared reference
- [d:r:i] third candidate single carrier:
  - `health.md`

## What Stays Explicitly Later

- [d:r:i] structural-row promotion
- [d:r:i] dual-basis relabel
- [d:r:i] typed standalone carrier
- [d:r:i] live `.claude` translation or parity
- [d:r:i] compatibility matrix / version-window claims
- [d:r:i] third-runtime annotation
- [d:r:i] extraction implementation
- [d:r:i] widening `compatibility_drift_reasons` beyond held-runtime drift

## Current Consequence

- [d:r:i] The cross-runtime family now has the missing intermediate object between proposal and implementation.
- [d:r:i] The next bounded move after `119` should be one ≤2-carrier implementation-slice proposal chosen from the priority order above, not a full-field implementation sweep.
