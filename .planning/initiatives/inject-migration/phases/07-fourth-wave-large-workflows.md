# Phase 7 — Fourth Wave: Large Workflows (DEFERRABLE)

ID: `07-fourth-wave-large-workflows`
Status: `pending`
Dependencies: Phase 6 complete
Approval gates: operator decides whether to enter the phase at all (entry gate)

## Objective

Migrate three large workflow files to `mode: inject`:

- `workflows/new-project.md` — 1300+ lines, 283-line modifier diff
- `workflows/discuss-phase.md` — 1486 lines (per intervention-strategies §8)
- `workflows/plan-phase.md` — 1105 lines

These are the largest carriers and the most expensive to migrate. The intervention-strategies analysis explicitly classified Phase 7 as DEFERRABLE — the operator may decide the cost-benefit no longer favors migration after Phase 6 lands.

## Rationale

Large workflows are where the inject model's leverage is highest (because every line of upstream content modifier doesn't have to carry is leverage) AND where the per-carrier risk is also highest (because one carrier touches many anchors and many operations).

By Phase 7, the inject mechanism has been exercised on:
- 5 references (Phases 3 + 4)
- 5 additive workflows (Phase 5)
- 2–3 step-level workflows (Phase 6)

That's enough operational data to know whether a 4th-wave migration is worth the effort or whether the remaining carriers should stay overwrite. The decision is the operator's at the entry gate.

## Entry Gate

Before any slice in this phase runs, the operator must explicitly authorize entry. The agent stops at Phase 6's exit and presents:

- Per-carrier estimated effort (extrapolated from Phase 5 and 6 metrics)
- Cumulative per-runtime carrier count if Phase 7 lands (~13 inject carriers post-Phase 7)
- Estimated calendar time
- Risk: large carriers can fail mid-migration; partial state is harder to recover

The operator either says "enter Phase 7" or "skip Phase 7; mark Phase 7 deferred and proceed to Phase 8". A "deferred" decision is recorded in STATE.md and reflected in INITIATIVE.md.

## Approach (if entering)

Eight slices: per workflow, two slices (deep-sweep design + apply, since each is so large; the design slice IS the deep sweep). Plus a phase-boundary verification.

The deep-sweep design slice for these large workflows is more substantial than Phase 6's progress.md sweep. Expect 100–200 line design docs.

## Slice Catalog (if entering)

### Slice 1 — Deep-sweep design for `workflows/new-project.md`

- **Status**: `[ ]`
- **Write set**: `.planning/initiatives/inject-migration/decisions/MIG-design-new-project.md`
- **Required content**:
  - Read entire upstream `new-project.md` and entire modifier overlay `new-project.md`
  - Clause-by-clause diff
  - Classify each modifier deviation by operation kind required
  - **Special concern**: confirm the `INSTRUCTION_FILE` runtime branching (lines 101 and 1273-1274 per the orientation read) survives migration without regression
  - Confirm `generate-instruction.cjs` wrapper interactions are preserved
  - Operations list: 10–30 operations expected (it's a large file)
  - Edge cases (multiple `<supporting_reading>` blocks; nested `@`-includes; conditional sections)
  - Decision: migrate vs keep overwrite (the `progress.md` precedent applies — keep-overwrite is a valid decision per design)
- **Verification**: per-slice gates
- **Commit**: `docs(initiative): deep sweep design for new-project.md migration`

### Slice 2 — Apply migration of `workflows/new-project.md` OR record overwrite-stay decision

Same two-path structure as Phase 6 Slice 6.

- **Status**: `[ ]`

### Slice 3–4 — `workflows/discuss-phase.md`

Same shape (deep-sweep design + apply-or-stay).

- **Status**: `[ ]` `[ ]`

### Slice 5–6 — `workflows/plan-phase.md`

Same shape.

- **Status**: `[ ]` `[ ]`

### Slice 7 — Phase debrief and verification

- **Status**: `[ ]`
- **Write set**: `.planning/initiatives/inject-migration/decisions/PHASE-07-debrief.md`
- **Required**: per-carrier outcome (migrated / kept overwrite); aggregate metrics; recommendations for Phase 8
- **Commit**: `docs(initiative): phase 07 debrief and large-workflow migration outcomes`

## Exit Criteria (phase boundary, IF entered)

1. All 7 slices marked `[x]` (regardless of migrate-vs-stay decisions)
2. Each large workflow either migrated and verified, or documented as intentional overwrite
3. Bootstrap gate green
4. STATE.md → Phase 7 `[x]`; advance to Phase 8

## Exit Criteria (IF NOT entered — operator deferred)

1. STATE.md → Phase 7 marked `[~]` (deferred)
2. INITIATIVE.md updated with deferral note
3. Brief deferral artifact at `.planning/initiatives/inject-migration/decisions/PHASE-07-deferred.md` with rationale
4. STATE.md advances to Phase 8

## Boundary

- This phase migrates AT MOST 3 large workflows. The set is fixed (`new-project.md`, `discuss-phase.md`, `plan-phase.md`). Other large workflows would be a follow-on initiative.
- This phase does NOT introduce new operation kinds. If a target requires one, hard-stop and amend ADR.
- Per-carrier deferral is allowed: if `new-project.md` is migrated but `plan-phase.md` is decided to stay overwrite, that's a valid Phase 7 outcome.

## Risks (phase-level)

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Large file's deep sweep takes >1 week per carrier | high | medium (initiative slips) | each design doc is itself a slice; if a sweep takes 2+ weeks, surface to operator for re-scope |
| One of the 3 large workflows interacts subtly with the runtime parser (e.g., the `<step>`-name-parsing in `phase-prompt.ts`) | medium | high (silent regression) | per-slice gates plus harness_canary at phase boundary; visual inspection of materialized content |
| Mid-migration of a large workflow gets interrupted (context clear, operator pause) | medium (large = long) | medium | each slice is one commit; partial migrations don't land; resume from last commit |
| The cumulative manifest grows large enough that JSON parsing / validation becomes slow | low | low | manifest is human-edited; even 100+ entries are fast |
| Operator decides to defer the entire phase | medium | low | this is an explicit option; defer is fine |

## Notes For Future Iterations

- After Phase 7 (whether entered or deferred), the remaining inject-targetable surface is small. Phase 8 handles templates and agents.
- If the operator defers Phase 7, the migration is "done enough" — references and most workflows are on inject; only large workflows and code files stay overwrite. That's a defensible end-state.
