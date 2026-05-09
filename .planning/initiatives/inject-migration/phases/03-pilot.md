# Phase 3 — Pilot

ID: `03-pilot`
Status: `pending`
Dependencies: Phase 2 contract code merged and approved
Approval gates: operator review of pilot result before phase exit

## Objective

Migrate exactly one carrier — `references/mandatory-initial-read.md` — to `mode: inject` end-to-end through both runtimes. Use the migration to stress-test the schema, the contract code, the marker conventions, and the verification model on a real file. Surface any issues before scaling to multiple carriers.

## Rationale

The pilot is a single high-fidelity migration. The carrier was selected because:

- Small (21 lines per intervention-strategies §7.2)
- Pure additive intent (modifier prepends a `<required_reading>`-style block; upstream content otherwise unchanged)
- Both runtimes consume the file (`parity_tier: core_required`)
- The diff against upstream is mostly the `@`-include line — a clean test of `include_add` operation
- A failure in the pilot is contained — a single carrier, easy to revert, no downstream pressure

If the pilot reveals fundamental issues (e.g., the schema is missing an operation kind, marker conventions don't survive a real upstream file's content, verify-materialized produces false positives or negatives), Phase 3 stops cleanly and Phase 1 reopens for ADR amendment.

## Approach

Three slices.

- Slice 1: design the migration of `mandatory-initial-read.md` — write the proposed manifest entry and modifier source files; do not apply yet
- Slice 2: apply the migration — bump schema_version to 4, swap the manifest entry, move the source files, run gates
- Slice 3: post-migration verification — run state-mutating gates, verify both runtimes, write a pilot debrief

## Slice Catalog

### Slice 1 — Design the migration

- **Status**: `[ ]`
- **Type**: planning artifact (still no behavior change)
- **Write set**:
  - `.planning/initiatives/inject-migration/decisions/PILOT-DESIGN-mandatory-initial-read.md` → CREATE (a focused design doc for this carrier's migration)
- **Required content**:
  - **Current state**: cite upstream `commands/gsd/references/mandatory-initial-read.md` content; cite modifier overlay's current overwritten content; produce a precise diff
  - **Proposed manifest entry**: full JSON for the `mode: inject` form with operations array
  - **Modifier source files**: list each new file under `harness_modifier/overlay/inject-sources/...` that the operations reference; sketch their content
  - **Materialization preview**: the expected output content after applying operations to upstream
  - **Verification approach**: which gates to run; what each confirms
  - **Rollback plan**: the exact sequence to revert if Slice 2 fails verification
  - **Open questions** (if any): document them; do not proceed if any open question is unanswered
- **Verification**: per-slice gates; `audit_refmap verify .` exit 0
- **Commit**: `docs(initiative): design pilot migration of mandatory-initial-read.md`
- **Boundary**: design doc only. No manifest changes; no source-file moves; no contract-code changes (Phase 2's code is what processes the entry; Phase 3 only uses it).

### Slice 2 — Apply the pilot migration

- **Status**: `[ ]`
- **Type**: overlay carrier change + manifest schema_version bump (per AGENTS.md change-class triggers; pre-authorized by this slice spec)
- **Write set**:
  - `tooling/portable-gsd/overlay/get-shit-done/references/mandatory-initial-read.md` → DELETE (no longer needed; modifier no longer overwrites)
  - `harness_modifier/overlay/inject-sources/get-shit-done/references/mandatory-initial-read/<operation>.md` → CREATE (one or more source files per the design)
  - `tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json` → EDIT:
    - Bump `schema_version` from 3 to 4
    - Change entry `get-shit-done/references/mandatory-initial-read.md` from `mode: overwrite` to `mode: inject` with operations array
- **Approach** per Slice 1's design:
  1. Move/delete files per Slice 1's plan
  2. Update manifest entry per Slice 1's spec
  3. Run validate-manifest with the new schema; confirm parses cleanly
- **Verification**:
  - `git diff --check` clean
  - `python3 tooling/codex/audit_refmap.py verify .` exit 0
  - `python3 harness_modifier/contract/portable_gsd_contract.py validate-manifest . --all-supported --source-only --strict` exit 0 (source-only, not state-mutating)
  - `python3 -m unittest discover -s tooling/codex/tests` exit 0 (existing tests still pass)
  - `python3 -m unittest tooling.codex.tests.test_inject_*` exit 0 (inject tests pass)
- **Commit**: `feat(overlay): pilot mode: inject migration for mandatory-initial-read.md`
- **Boundary**: only the pilot carrier migrates. Other entries unchanged. The `schema_version: 4` bump is one-time; subsequent inject entries don't re-bump.

### Slice 3 — Post-migration verification + pilot debrief

- **Status**: `[ ]`
- **Type**: state-mutating verification + planning artifact
- **Write set**:
  - `.planning/initiatives/inject-migration/decisions/PILOT-DEBRIEF-mandatory-initial-read.md` → CREATE (the debrief)
- **Approach**:
  1. Run the state-mutating bootstrap gate (authorized at phase boundary): `bash scripts/ci/check-deterministic.sh`
  2. Run `bash scripts/ci/check-bootstrap.sh`
  3. Materialize via `./scripts/setup-portable-gsd-runtime.sh --runtime both`
  4. Inspect the materialized files for both runtimes; confirm modifier's `@`-include line is present and the rest of the upstream content is preserved
  5. Run `python3 harness_modifier/contract/portable_gsd_contract.py verify-materialized . --all-supported --strict` exit 0
  6. Write the debrief: what worked, what surprised us, what should change before Phase 4
- **Required debrief sections**:
  - **Worked as designed**: list of design assumptions confirmed
  - **Surprised by**: anything not anticipated in Slice 1
  - **Operator-visible risks**: any concerns to surface before Phase 4
  - **Schema feedback**: should the ADR be amended? (if yes, Phase 3 stops; an ADR-002 is drafted before Phase 4)
  - **Operation-kind feedback**: did any operation kind feel unwieldy? Any new kind needed?
  - **Marker convention feedback**: any issues with the `<!-- GSD_MODIFIER:start key:KEY -->` markers in real content?
  - **Verification feedback**: did `verify_inject_state` surface false positives or negatives?
  - **Recommendation**: enter Phase 4, or revise design first
- **Verification**:
  - The state-mutating gates pass (logged in debrief)
  - The materialized files for both runtimes contain the expected modifier content + the upstream content
  - `git diff --check` clean (the debrief is the only new file)
- **Commit**: `docs(initiative): pilot debrief for mandatory-initial-read.md migration`
- **Boundary**: the debrief is informational. If it recommends design changes, those happen in a fresh Phase 1 amendment, not as post-hoc edits to the pilot.

## Exit Criteria (phase boundary)

After Slice 3:

1. All three slices marked `[x]`
2. The pilot carrier is materialized correctly under both runtimes (visual inspection + `verify-materialized` exit 0)
3. Bootstrap gate exit 0 with `hard_failures: []` (the surface cleanup from Phase 0 should still hold)
4. Pilot debrief recommends entering Phase 4 (if not, the initiative pauses for design revision)

**Operator review gate**: operator reads the debrief; signals approval to enter Phase 4 by invoking next iteration. Without approval, Phase 4 does not start.

## Phase Boundary Verification

Run all of the following (state-mutating; phase-boundary authorized):

```bash
bash scripts/ci/check-deterministic.sh
bash scripts/ci/check-bootstrap.sh
./scripts/setup-portable-gsd-runtime.sh --runtime both
python3 harness_modifier/contract/portable_gsd_contract.py verify-materialized . --all-supported --strict
python3 harness_modifier/contract/harness_canary.py report . --all-supported --strict
```

## Boundary

- Only `mandatory-initial-read.md` is migrated in Phase 3. Other carriers wait for Phase 4+.
- The pilot does NOT inform decisions about `bin/lib/*.cjs` (those stay overwrite per ADR-001).
- The pilot does NOT migrate the codex skill mirrors (Phase 9).
- The pilot does NOT update the host matrix (Phase 6+ if needed).

## Risks (phase-level)

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| `apply_inject_operations` works on synthetic content (Phase 2 tests) but fails on the real upstream file (e.g., unexpected whitespace, BOM) | medium | medium | the pilot is the first real-content test; failures here are expected to surface and inform fixes |
| `verify_inject_state` confirms the operation landed but the materialized content is subtly wrong (e.g., wrong indentation in the inserted block) | medium | medium | Slice 3's visual inspection of materialized output catches this |
| The marker key naming convention (`KEY` field) collides with content already in upstream | low | high | the marker uses an explicit prefix `GSD_MODIFIER:`; collision requires upstream to use the same prefix (very unlikely) |
| Operator review of the debrief reveals a fundamental design issue requiring ADR amendment | medium (this is the pilot's purpose) | high (delays initiative) | the pilot is small; iteration cost is low; an ADR amendment phase can be added between Phase 3 and Phase 4 |
| The `schema_version` bump to 4 breaks the existing test suite | medium (Phase 2 backward-compat test should catch) | high | Slice 2 verification includes the full test discover; Slice 6 of Phase 2 specifically tests mixed-mode manifests |
| Rollback after a failed pilot is hard (multiple commits to revert) | medium | low | each slice is one commit; revert is simple `git revert` if needed |

## Notes For Future Iterations

- The pilot establishes the pattern that Phase 4+ uses: design slice → apply slice → debrief slice. Subsequent waves combine multiple carriers per phase but follow the same per-carrier rhythm.
- The debrief's "Recommendation" field is the gate: if it says "do not enter Phase 4", the initiative stops cleanly.
- The pilot creates `harness_modifier/overlay/inject-sources/` as a new subtree. This convention persists for all future inject sources.
