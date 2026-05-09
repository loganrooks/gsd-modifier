# Phase 6 — Third Wave: Step-Level Workflows

ID: `06-third-wave-step-level`
Status: `pending`
Dependencies: Phase 5 complete; Phase 5 debrief recommends proceeding
Approval gates: operator review when a new operation kind is first exercised in a real carrier

## Objective

Migrate three workflows that require step-level operations (`step_remove`, `step_insert_after`) to `mode: inject`:

- `workflows/health.md` — has `step_remove` and `step_insert_after` per intervention-strategies §4.2
- `workflows/update.md` — has block content reductions
- `workflows/progress.md` — needs deeper sweep first; complex

These are the first carriers that exercise step-level operations in production. The implementation in Phase 2 covered them in unit tests; Phase 6 is their first real-content trial.

## Rationale

Step-level operations are the next-level expressiveness beyond pure additive injection. They handle the case where modifier needs to *remove* an upstream step (because modifier doesn't want it for its users) or *insert* a modifier-specific step at a precise point in the workflow's process.

If step-level operations work cleanly in Phase 6, the inject mechanism is essentially fully validated for everything except large-restructure workflows (Phase 7) and code files (Phase 9). If they don't work cleanly, the ADR may need amendment.

The deeper-sweep requirement on `progress.md` means its design slice is more involved than the others — possibly two design slices for that one carrier.

## Approach

Eight slices: per workflow, one design slice + one apply slice (6 slices). Plus a deep-sweep slice for `progress.md` and a phase-boundary verification.

Per the PROTOCOL approval gate: when an operation kind is first exercised on real content (e.g., `step_remove` on `health.md`), the agent stops after the first slice that uses it for operator review. Subsequent uses of the same kind do not require the gate.

## Slice Catalog

### Slice 1 — Design migration of `workflows/health.md`

- **Status**: `[ ]`
- **Write set**: `.planning/initiatives/inject-migration/decisions/MIG-design-health.md`
- **Required content**: as Phase 5 design docs, plus:
  - **Step-removal list**: each upstream step that modifier removes — name, line range, why
  - **Step-insertion list**: each modifier-added step — name, anchor (after which step), payload source, why
  - **Step-ordering verification**: the resulting `<process>` section's step order — confirmed correct
- **Critical check**: confirm `step_remove` and `step_insert_after` in the ADR cover all of `health.md`'s needs. If a new kind is needed (e.g., `step_replace`), hard-stop and request ADR amendment.
- **Verification**: per-slice gates
- **Commit**: `docs(initiative): design migration of health.md workflow`

### Slice 2 — Apply migration of `workflows/health.md`

This is the FIRST real-content use of `step_remove` and `step_insert_after`. Per the approval gate, the agent stops after this slice's commit for operator review before proceeding to Slice 3.

- **Status**: `[ ]`
- **Write set**: per design
- **Verification**:
  - per-slice gates
  - inject unit tests still pass
  - existing tests still pass
  - validate-manifest --source-only --strict exit 0
  - Visual sanity check: confirm the materialized `health.md` has the expected step order. (Read the file; verify against design's expected ordering.)
- **Commit**: `feat(overlay): migrate health.md to mode: inject (first step-level operations)`
- **After commit**: STATE.md → Status = `paused-for-approval`. Operator confirms step-level operations look correct on real content before proceeding.

### Slice 3 — Design migration of `workflows/update.md`

- **Status**: `[ ]`
- **Commit**: `docs(initiative): design migration of update.md workflow`

### Slice 4 — Apply migration of `workflows/update.md`

- **Status**: `[ ]`
- **Commit**: `feat(overlay): migrate update.md to mode: inject`

### Slice 5 — Deep-sweep design for `workflows/progress.md`

`progress.md` is 534 lines (per intervention-strategies §4.2) and was flagged "deeper sweep needed". This slice is the deeper sweep.

- **Status**: `[ ]`
- **Write set**: `.planning/initiatives/inject-migration/decisions/MIG-progress-deep-sweep.md`
- **Required content**:
  - Read the entire upstream `progress.md` and the entire modifier-overlay `progress.md` (no skimming)
  - Produce a clause-by-clause diff: every modifier deviation gets an entry
  - Classify each deviation: pure-additive / step-level / block_replace / requires-overwrite
  - If any deviation requires overwrite, document why; the carrier may stay `mode: overwrite` with the rest migrated, OR may stay overwrite entirely
  - Decision: migrate to `mode: inject` (in Slice 6) or keep as `mode: overwrite` (Slice 6 records that decision instead)
- **Verification**: per-slice gates
- **Commit**: `docs(initiative): deep sweep design for progress.md migration`

### Slice 6 — Apply migration of `workflows/progress.md` OR record overwrite-stay decision

- **Status**: `[ ]`
- **Two paths**:
  - **Path A** (deeper sweep recommends migration): apply per design; manifest entry; commit `feat(overlay): migrate progress.md to mode: inject`
  - **Path B** (deeper sweep recommends keeping overwrite): no manifest change; commit a planning note to `.planning/initiatives/inject-migration/decisions/PROGRESS-stays-overwrite.md` with the rationale; commit `docs(initiative): record progress.md as intentional mode: overwrite`
- The phase plan does NOT pre-commit which path. Slice 5's deep sweep is genuinely informational.

### Slice 7 — Phase debrief and verification

- **Status**: `[ ]`
- **Write set**: `.planning/initiatives/inject-migration/decisions/PHASE-06-debrief.md`
- **Approach**:
  1. Run state-mutating gates
  2. Confirm `health.md`, `update.md`, and (if migrated) `progress.md` materialize correctly under both runtimes
  3. Run `harness_canary.py report` to confirm runtime-facing behavior is preserved
  4. Write debrief: did step-level operations work? any surprise edge cases? new operation kinds needed?
- **Verification**: gates green; debrief written
- **Commit**: `docs(initiative): phase 06 debrief and step-level operation metrics`

## Exit Criteria (phase boundary)

1. All 7 slices marked `[x]`
2. `health.md` and `update.md` migrated successfully (`progress.md` migrated OR documented as intentional overwrite)
3. Bootstrap gate green; `hard_failures: []`
4. `harness_canary.py report --all-supported --strict` exit 0
5. STATE.md → Phase 6 `[x]`; advance to Phase 7 (or Phase 8 if Phase 7 deferred)
6. Operator approval recorded after Slice 2 (first step-level operation)

## Phase Boundary Verification

Standard state-mutating gates plus the harness canary, which exercises the runtime-facing surface more thoroughly than the bootstrap gate alone:

```bash
bash scripts/ci/check-deterministic.sh
bash scripts/ci/check-bootstrap.sh
./scripts/setup-portable-gsd-runtime.sh --runtime both
python3 harness_modifier/contract/harness_canary.py report . --all-supported --strict
python3 harness_modifier/contract/portable_gsd_contract.py verify-materialized . --all-supported --strict
```

## Boundary

- This phase migrates 2 or 3 workflows. The exact count depends on Slice 5's deep-sweep result.
- Step-level operations are exercised first on `health.md`. The operator reviews before scaling.
- This phase does NOT touch large workflows (`new-project`, `discuss-phase`, `plan-phase`). They're Phase 7.
- This phase does NOT touch agents, templates, or lib files. They're Phase 8 / kept-overwrite respectively.

## Risks (phase-level)

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Step-level operations on real content reveal an apply/verify bug not caught by Phase 2 unit tests | medium | medium | the operator review after Slice 2 specifically looks for this; if found, hard-stop and route to a fix slice |
| `progress.md` deeper sweep takes substantially longer than estimated | medium | low | the slice has flexible scope; longer sweep is acceptable; the alternative (rushing to migration) is worse |
| `update.md` has subtle interactions between block content reductions and the `<process>` parser | low | medium | Slice 4's verification includes `harness_canary` which exercises the parser |
| Operator approval after Slice 2 takes long enough to delay the loop | low | low | the operator can review at their pace; loop is paused, not blocked |
| A step-level operation works in apply but verifies wrong (e.g., `verify_inject_state` misreports a removed step as still present) | medium | high (silent regression) | per-slice gates re-run verify after apply; visual inspection of materialized content; harness canary at phase boundary |

## Notes For Future Iterations

- The decision in Slice 6 sets a precedent for future "deep-sweep" carriers: when a carrier's diff is large, the decision to migrate is made AFTER the sweep, not before.
- If `progress.md` stays overwrite, the manifest entry is unchanged but a planning artifact records the rationale. This is the canonical way to mark intentional `mode: overwrite` going forward.
