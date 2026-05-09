# Phase 4 — First Wave: Small References

ID: `04-first-wave-references`
Status: `pending`
Dependencies: Phase 3 pilot debrief recommends proceeding
Approval gates: none at slice level (per-slice gates only)

## Objective

Migrate four additional small reference files to `mode: inject`. Build per-iteration cadence and surface any not-pilot-evident issues before larger-scale migration.

Targets:
- `references/verification-overrides.md`
- `references/agent-contracts.md`
- `references/planner-reviews.md`
- `references/planning-config.md`

(`references/mandatory-initial-read.md` was the pilot in Phase 3.)

## Rationale

References are smaller and simpler than workflows. They typically need only one or two operations (a section_insert_after for a modifier-specific block, plus possibly an include_add). They build the agent's per-carrier migration muscle memory, surface any pilot-only edge cases that didn't generalize, and produce 4 datapoints on per-carrier effort and risk.

The phase intentionally moves multiple carriers because each is small. If carriers were large, one-per-phase would be appropriate; for small references, one-per-slice is right.

## Approach

Eight slices: per carrier, one design slice + one apply slice. Plus one phase-boundary verification slice at the end.

The slice-pair pattern per carrier mirrors Phase 3:
- Design slice: write the focused design doc
- Apply slice: execute migration, run gates, commit

The design doc per carrier is shorter than Phase 3's pilot design (10–30 lines) since the pattern is established.

## Slice Catalog

### Slice 1 — Design migration of `references/verification-overrides.md`

- **Status**: `[ ]`
- **Write set**:
  - `.planning/initiatives/inject-migration/decisions/MIG-design-verification-overrides.md` → CREATE
- **Required content** (lighter than pilot):
  - Cite upstream content (path + line range); cite modifier overlay (path + line range); produce diff
  - Proposed `mode: inject` manifest entry (full JSON)
  - List of new modifier source files under `harness_modifier/overlay/inject-sources/`
  - Expected materialized content sketch
  - Open questions (if any)
- **Verification**: per-slice gates
- **Commit**: `docs(initiative): design migration of verification-overrides.md`

### Slice 2 — Apply migration of `references/verification-overrides.md`

- **Status**: `[ ]`
- **Type**: overlay carrier change (per AGENTS.md; pre-authorized)
- **Write set**:
  - Move/delete `tooling/portable-gsd/overlay/get-shit-done/references/verification-overrides.md`
  - Create new modifier source files under `harness_modifier/overlay/inject-sources/get-shit-done/references/verification-overrides/`
  - Edit `OVERLAY-MANIFEST.json` entry
- **Approach**: per Slice 1 design
- **Verification**:
  - per-slice gates
  - `validate-manifest --source-only --strict` exit 0
  - inject unit tests still pass
  - existing tests still pass
- **Commit**: `feat(overlay): migrate verification-overrides.md to mode: inject`

### Slice 3 — Design migration of `references/agent-contracts.md`

Same shape as Slice 1, target `agent-contracts.md`.

- **Status**: `[ ]`
- **Write set**: `.planning/initiatives/inject-migration/decisions/MIG-design-agent-contracts.md`
- **Commit**: `docs(initiative): design migration of agent-contracts.md`

### Slice 4 — Apply migration of `references/agent-contracts.md`

Same shape as Slice 2.

- **Status**: `[ ]`
- **Commit**: `feat(overlay): migrate agent-contracts.md to mode: inject`

### Slice 5 — Design migration of `references/planner-reviews.md`

- **Status**: `[ ]`
- **Commit**: `docs(initiative): design migration of planner-reviews.md`

### Slice 6 — Apply migration of `references/planner-reviews.md`

- **Status**: `[ ]`
- **Commit**: `feat(overlay): migrate planner-reviews.md to mode: inject`

### Slice 7 — Design migration of `references/planning-config.md`

- **Status**: `[ ]`
- **Commit**: `docs(initiative): design migration of planning-config.md`

### Slice 8 — Apply migration of `references/planning-config.md`

- **Status**: `[ ]`
- **Commit**: `feat(overlay): migrate planning-config.md to mode: inject`

## Phase-Boundary Slice (Slice 9 — phase debrief)

- **Status**: `[ ]`
- **Write set**:
  - `.planning/initiatives/inject-migration/decisions/PHASE-04-debrief.md` → CREATE
- **Approach**:
  1. Run state-mutating gates (`check-deterministic`, `check-bootstrap`, `verify-materialized`, `harness_canary`)
  2. Confirm all 5 references (4 from this phase + 1 from Phase 3) materialize correctly under both runtimes
  3. Write debrief: per-carrier effort spent, surprises, schema feedback, recommendations
- **Verification**:
  - All gates exit 0
  - bootstrap `hard_failures: []`
  - All 5 reference carriers verified
- **Commit**: `docs(initiative): phase 04 debrief and migration metrics`

## Exit Criteria (phase boundary)

1. All 9 slices marked `[x]`
2. 5 references total (1 pilot + 4 phase-04) materialize correctly under both runtimes
3. Bootstrap gate green; `hard_failures: []`
4. Existing tests still pass
5. STATE.md → Phase 4 marked `[x]`; advance to Phase 5
6. Counters: `Carriers migrated to mode: inject: 5 / target` (target depends on later phases)

## Boundary

- This phase migrates 4 references; no workflows, no agents, no templates, no lib files.
- Each carrier's design doc is lighter than the pilot's; the pilot established the pattern.
- This phase does NOT add new operation kinds. If a target requires a kind not in the pilot, that's a hard-stop event triggering an ADR amendment.

## Risks (phase-level)

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| One of the 4 references requires a new operation kind | medium (intervention-strategies §4.3 says all 5 references are simple additive) | high (Phase 4 stalls) | hard-stop and amend ADR; do not invent operation kinds in-flight |
| Migration of one reference exposes a bug in apply_inject_operations | medium (more real content; more edge cases) | medium | each carrier's apply slice runs the test suite; bugs surface and route through a fix slice within Phase 4 |
| The 5 references collectively duplicate marker keys (different ops, same KEY) | medium | low | the marker key convention should namespace by carrier; design docs in odd-numbered slices verify this |
| Worktree accumulates many `harness_modifier/overlay/inject-sources/` files; directory structure becomes unclear | low | low | establish convention: `inject-sources/<full-path-to-target>/<op-N>.md` |
| Phase-boundary verification reveals one carrier didn't actually migrate cleanly (manifest entry has typo, etc.) | medium | low | Slice 9's verification catches and surfaces; revert + fix in a follow-up slice |

## Notes For Future Iterations

- After Phase 4, the per-carrier effort is well-known. Phase 5+ can plan slice durations more accurately.
- The debrief's metrics (lines per design doc, lines per carrier, time per slice) inform later phase plans.
- If a slice in this phase pauses for approval (e.g., a slice spec ambiguity), the operator handles via standard PROTOCOL paused-for-approval flow.
