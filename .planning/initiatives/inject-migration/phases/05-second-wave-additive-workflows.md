# Phase 5 — Second Wave: Additive Workflows

ID: `05-second-wave-additive-workflows`
Status: `pending`
Dependencies: Phase 4 complete; Phase 4 debrief recommends proceeding
Approval gates: none at slice level (per-slice gates only)

## Objective

Migrate five additive-pattern workflow files to `mode: inject`. These workflows have predominantly additive modifier intent (modifier adds `<supporting_reading>` / `<deeper_reading>` sections + `@`-include lines for modifier-owned references) without restructuring upstream's existing content.

Targets:
- `workflows/spec-phase.md`
- `workflows/verify-phase.md`
- `workflows/complete-milestone.md`
- `workflows/new-milestone.md`
- `workflows/ingest-docs.md`

## Rationale

Workflows are larger and more complex than references but the additive pattern is the same. Phase 5 scales the pattern from references (Phase 3 + 4) to workflow files. Each workflow is large enough (300–800 lines typically) that a per-carrier design doc is more involved, but the operations themselves should still be the same kinds used in Phase 3 and 4 (`section_insert_after`, `include_add`, possibly `section_replace` with markers).

If a target turns out to require step-level operations (`step_remove`, `step_insert_after`), it doesn't belong in Phase 5; reclassify to Phase 6. This phase is specifically the additive-only workflow wave.

## Approach

Eleven slices: per workflow, one design slice + one apply slice (10 slices). Plus one phase-boundary verification (Slice 11).

The per-carrier design doc is more substantial than Phase 4's because workflows have more content to consider. Aim for 30–60 lines per design doc — enough to be unambiguous about what each operation does, but not redundant with the upstream file content (cite by path, don't inline).

## Slice Catalog

### Slice 1 — Design migration of `workflows/spec-phase.md`

- **Status**: `[ ]`
- **Write set**: `.planning/initiatives/inject-migration/decisions/MIG-design-spec-phase.md` → CREATE
- **Required content**:
  - Diff summary: cite upstream and modifier-overlay content; identify the modifier-only sections (e.g., specific `<supporting_reading>` blocks; specific `@`-include lines)
  - Operation list: per modifier addition, propose the operation kind + anchor + payload source
  - Manifest entry: full JSON
  - Modifier source files: list under `harness_modifier/overlay/inject-sources/`
  - Edge cases (anchors in nested sections, multiple matches for the same anchor, etc.)
- **Critical check**: confirm the workflow does NOT need step-level operations (`step_remove`, `step_insert_after`). If it does, hard-stop; reclassify to Phase 6.
- **Verification**: per-slice gates
- **Commit**: `docs(initiative): design migration of spec-phase.md workflow`

### Slice 2 — Apply migration of `workflows/spec-phase.md`

- **Status**: `[ ]`
- **Write set**: per design; new modifier source files; manifest entry update
- **Verification**:
  - per-slice gates
  - `validate-manifest --source-only --strict` exit 0
  - inject unit tests pass
  - existing tests pass
- **Commit**: `feat(overlay): migrate spec-phase.md workflow to mode: inject`

### Slice 3–4 — `workflows/verify-phase.md`

Same shape as Slice 1–2.

- **Status**: `[ ]` `[ ]`
- **Commits**: `docs(initiative): design migration of verify-phase.md` ; `feat(overlay): migrate verify-phase.md to mode: inject`

### Slice 5–6 — `workflows/complete-milestone.md`

- **Status**: `[ ]` `[ ]`
- **Commits**: `docs(initiative): design migration of complete-milestone.md` ; `feat(overlay): migrate complete-milestone.md to mode: inject`

### Slice 7–8 — `workflows/new-milestone.md`

- **Status**: `[ ]` `[ ]`
- **Commits**: `docs(initiative): design migration of new-milestone.md` ; `feat(overlay): migrate new-milestone.md to mode: inject`

### Slice 9–10 — `workflows/ingest-docs.md`

- **Status**: `[ ]` `[ ]`
- **Commits**: `docs(initiative): design migration of ingest-docs.md` ; `feat(overlay): migrate ingest-docs.md to mode: inject`

### Slice 11 — Phase debrief and verification

- **Status**: `[ ]`
- **Write set**: `.planning/initiatives/inject-migration/decisions/PHASE-05-debrief.md` → CREATE
- **Approach**:
  1. Run state-mutating gates (`check-deterministic`, `check-bootstrap`, `verify-materialized`)
  2. Confirm all 5 workflows in this phase, plus all 5 references from Phase 3+4, materialize correctly under both runtimes
  3. Write debrief
- **Required debrief sections**:
  - Per-workflow effort (slice durations; design-doc complexity)
  - Operation kinds used per workflow (any kind unused so far?)
  - Surprises
  - Recommendations for Phase 6 (step-level workflows)
  - Whether `block_replace` was needed (it shouldn't be in this phase's pure-additive workload)
- **Verification**: all gates exit 0; both runtimes verify all 10 migrated carriers
- **Commit**: `docs(initiative): phase 05 debrief and migration metrics`

## Exit Criteria (phase boundary)

1. All 11 slices marked `[x]`
2. 10 carriers total (5 references + 5 workflows) materialize correctly under both runtimes
3. Bootstrap gate green; `hard_failures: []`
4. Existing tests still pass
5. STATE.md → Phase 5 marked `[x]`; advance to Phase 6

## Boundary

- This phase migrates 5 workflows that follow the additive pattern. Step-level workflows are Phase 6.
- This phase does NOT introduce new operation kinds. If a target requires a kind not yet in the catalog, hard-stop and amend ADR.
- This phase does NOT touch any references. References were Phase 3 and 4.

## Risks (phase-level)

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| A target workflow that intervention-strategies classified as additive turns out to need step-level operations | medium | medium (slice slips to Phase 6) | each design slice's "Critical check" catches; reclassify to Phase 6 |
| Per-workflow design doc explosion (hundreds of lines each) | medium | low | hold design docs to 30–60 lines; cite upstream rather than inline; reuse pattern from Phase 4 |
| Marker key namespace collisions across multiple workflows | medium | low | establish convention: marker keys include the carrier path: `<workflow_name>:<purpose>`, e.g., `spec-phase:supporting-reading` |
| The `<supporting_reading>` anchor format varies subtly across workflows | medium | medium | each design slice verifies the anchor format upstream uses; if a workflow uses a different convention (e.g., `<context_reading>`), document and add operation accordingly |
| One workflow has a bug in upstream (e.g., #2787-style fenced-code-block boundary issue) that interacts with operation anchors | low | medium | per-slice verification catches; if surfaced, hard-stop and operator reviews |

## Notes For Future Iterations

- After Phase 5, the major remaining workload is step-level (Phase 6) and large workflows (Phase 7, deferrable).
- The 10-carrier baseline should be cross-runtime verified at every subsequent phase boundary, not just within the migrating phase.
- If Phase 5 takes substantially longer than estimated (>2 weeks per carrier average), the initiative may benefit from operator review before Phase 6 — surface that in the Phase 5 debrief.
