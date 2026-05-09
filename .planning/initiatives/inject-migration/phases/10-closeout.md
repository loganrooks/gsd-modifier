# Phase 10 — Closeout

ID: `10-closeout`
Status: `pending`
Dependencies: all prior phases complete (Phase 7 may be deferred; that's a valid completion)
Approval gates: operator final review

## Objective

Close the initiative cleanly. Run full initiative-level verification. Write a comprehensive retrospective. Update governance carriers (`AGENTS.md`, `CLAUDE.md`) to document `mode: inject` as a stable extension class. Update repo-level state (`docs/handoff/current.md`, `.planning/STATUS.md`, `.planning/CURRENT-STATE.md`) to reflect the new model. Mark the initiative `INITIATIVE-COMPLETE`.

## Rationale

The closeout phase is more than a checklist. It transforms the initiative from "in-flight work" to "documented stable posture". Without closeout:

- The new `mode: inject` carriers exist but aren't documented as a stable extension surface
- Future modifier work won't know which carriers are inject vs overwrite without re-reading the manifest
- `docs/handoff/current.md` will still describe the pre-migration model
- Future drift around inject carriers won't trigger the change-class trigger discipline cleanly

Closeout makes the new model the canonical posture.

## Approach

Six slices.

- Slice 1: full initiative-level verification (state-mutating; phase-boundary authorized)
- Slice 2: write the retrospective
- Slice 3: update AGENTS.md and CLAUDE.md to document `mode: inject` as a stable extension surface
- Slice 4: update `docs/handoff/current.md`, `.planning/STATUS.md`, `.planning/CURRENT-STATE.md` to reflect the new posture
- Slice 5: archive initiative artifacts (move `decisions/*` and `checkpoints/*` to a frozen subfolder; update STATE.md to terminal state)
- Slice 6: final commit + sentinel set + operator review

## Slice Catalog

### Slice 1 — Full initiative-level verification

- **Status**: `[ ]`
- **Type**: state-mutating verification (phase-boundary authorized)
- **Write set**:
  - `.planning/initiatives/inject-migration/decisions/CLOSEOUT-verification-results.md` → CREATE (records the outcomes of all gates and tests run)
- **Approach**:
  1. `bash scripts/ci/check-deterministic.sh`
  2. `bash scripts/ci/check-bootstrap.sh`
  3. `./scripts/setup-portable-gsd-runtime.sh --runtime both`
  4. `python3 harness_modifier/contract/portable_gsd_contract.py validate-manifest . --all-supported --strict`
  5. `python3 harness_modifier/contract/portable_gsd_contract.py verify-materialized . --all-supported --strict`
  6. `python3 harness_modifier/contract/harness_canary.py report . --all-supported --strict`
  7. `python3 harness_modifier/closure/host_exercise_matrix.py . --profile all --output-dir .planning/measurement/host-exercise-matrix --strict`
  8. `python3 -m unittest discover -s tooling/codex/tests`
  9. Cross-check: total carriers in each mode (count `mode: inject`, `mode: overwrite`, `mode: add` from manifest)
  10. Cross-check: bootstrap gate `hard_failures: []`
- **Verification**: all gates exit 0; counts match expected
- **Commit**: `verify(initiative): closeout verification results`

### Slice 2 — Retrospective

- **Status**: `[ ]`
- **Write set**: `.planning/initiatives/inject-migration/RETROSPECTIVE.md` → CREATE
- **Required content**:
  - **Goal recap**: per INITIATIVE.md
  - **Phase-by-phase outcome**: which phases entered, which deferred, key debriefs
  - **Quantitative**:
    - Carriers migrated to `mode: inject`: count + breakdown by carrier class
    - Carriers staying `mode: overwrite`: count + per-carrier rationale
    - Carriers in `mode: add`: count (Phase 0 reclassifications + net-new modifier-owned)
    - Inject operations exercised: which kinds, count of uses each
    - Calendar time: from initiative start to closeout
    - Slices completed: total
    - Hard-stops encountered: count + nature
    - Operator approval gates fired: count
  - **Qualitative**:
    - What worked well
    - What surprised us
    - What we'd do differently next time
    - Recommendations for follow-on initiatives
  - **Open issues**: any deferred items that need explicit follow-up tracking (e.g., `gsd-progress` declaration anomaly if not resolved; Phase 7 deferred carriers)
  - **Cross-references**: to all phase debriefs, the orientation artifact, intervention-strategies analysis
- **Verification**: per-slice gates
- **Commit**: `docs(initiative): inject migration retrospective`

### Slice 3 — Update governance for stable inject posture

- **Status**: `[ ]`
- **Type**: governance carrier change (per AGENTS.md change-class triggers; pre-authorized)
- **Write set**:
  - `AGENTS.md` → EDIT (extend "Source Of Truth" or add a new "Carrier Modes" section that documents `mode: inject` as a stable extension class with brief examples)
  - `CLAUDE.md` → EDIT (parallel update)
  - `.planning/initiatives/inject-migration/posture-triggers.md` → EDIT (mark `mode: inject` carrier class as stable surface, not just a migration class)
- **Required content for AGENTS.md** (sketch; refine in Slice 3):

```markdown

### Carrier Modes (stable surface as of closeout)

The overlay manifest at `tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json` declares each carrier's materialization mode:

- `mode: overwrite` — modifier ships a full file replacement; appropriate for code files (`bin/lib/*.cjs`) and rare body-replacing carriers
- `mode: add` — modifier ships net-new content with no upstream analog (modifier-owned workflows, references, the runtime-neutral generator wrapper)
- `mode: inject` — modifier ships operations applied to upstream's content at known anchors (the post-2026-05-08 default for additive intent)

Operation kinds, marker conventions, and parity_intent semantics are documented in `.planning/initiatives/inject-migration/decisions/ADR-001-manifest-schema-v4.md`.
```

- **Verification**: per-slice gates; `audit_refmap verify .`; `scan_threshold_language --ignore-meta-instruction-lines`
- **Commit**: `docs(governance): document mode: inject as stable carrier mode`

### Slice 4 — Update repo-level state

- **Status**: `[ ]`
- **Type**: governance / state carrier change (pre-authorized by this slice)
- **Write set**:
  - `docs/handoff/current.md` → EDIT (update sections describing carrier modes; reference the new model)
  - `.planning/STATUS.md` → EDIT (add a "Inject migration complete" line; reference RETROSPECTIVE.md)
  - `.planning/CURRENT-STATE.md` → EDIT (similar)
- **Verification**: per-slice gates; ensure cross-references all valid
- **Commit**: `docs(state): update repo state to reflect inject migration completion`

### Slice 5 — Archive initiative artifacts

- **Status**: `[ ]`
- **Approach**:
  1. Create `.planning/initiatives/inject-migration/archive/` directory
  2. Move `decisions/*` to `archive/decisions/`
  3. Move `checkpoints/*` to `archive/checkpoints/`
  4. Keep `INITIATIVE.md`, `STATE.md`, `RETROSPECTIVE.md`, `README.md`, and the phase plans in place (they remain readable for future reference)
  5. Add a top-level `ARCHIVED.md` or note in README explaining the archive structure
- **Verification**: per-slice gates; archived files retain content
- **Commit**: `chore(initiative): archive initiative working artifacts`

### Slice 6 — Final sentinel + STATE.md terminal update

- **Status**: `[ ]`
- **Write set**:
  - `.planning/initiatives/inject-migration/STATE.md` → EDIT (`Sentinel: INITIATIVE-COMPLETE`; `Status: complete`; `Last updated: <timestamp>`; `Phase Progress: all [x]` or `[~]` for Phase 7 deferred; `Active Work: (initiative complete)`)
  - `.planning/initiatives/inject-migration/checkpoints/<final-timestamp>-INITIATIVE-COMPLETE.md` → CREATE (final checkpoint; sentinel transition record)
- **Approach**:
  1. Final read of STATE.md
  2. Update sentinel
  3. Write final checkpoint
  4. Commit
- **Verification**:
  - `git rev-parse HEAD` matches updated STATE.md
  - `git log --oneline --grep "Initiative: inject-migration"` enumerates all initiative slice commits
- **Commit**: `chore(initiative): mark inject-migration INITIATIVE-COMPLETE`
- **After this commit**: the loop is terminated. Future iterations of the loop prompt should detect `Sentinel: INITIATIVE-COMPLETE` and exit cleanly per PROTOCOL.

## Exit Criteria (initiative-level, not just phase-level)

After Slice 6:

1. All initiative completion criteria from INITIATIVE.md "Completion Criteria" met
2. STATE.md → Sentinel: `INITIATIVE-COMPLETE`
3. RETROSPECTIVE.md exists and operator-reviewed
4. AGENTS.md and CLAUDE.md document `mode: inject` as a stable surface
5. Repo-level state (`current.md`, `STATUS.md`, `CURRENT-STATE.md`) reflects the post-migration model
6. Initiative artifacts archived
7. Final commit landed; loop terminator engaged

**Operator final review gate**: the operator reviews the RETROSPECTIVE.md and confirms the initiative's outcomes match what was promised. The operator's confirmation is the final commit (the operator may invoke Slice 6 themselves, or approve the agent's invocation).

## Boundary

- This phase does NOT migrate any new carriers.
- This phase does NOT extend the inject schema.
- This phase does NOT add new operation kinds.
- This phase does NOT modify upstream files.

## Risks (phase-level)

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Closeout verification surfaces a regression in a carrier from earlier phases | medium | high (could re-open prior phases) | per-phase verification was meant to catch this; if it appears in closeout, treat as a P0 issue and revert/fix before proceeding |
| Retrospective reveals the initiative didn't achieve its core goal | low | high (need to revisit completion criteria) | per-phase debriefs surface progress; final retrospective should be a confirmation, not a discovery |
| Governance updates in Slices 3–4 introduce contradictions with AGENTS.md / CLAUDE.md | low | medium | use `audit_refmap` and `scan_threshold_language` per-slice; visual review of the diffs |
| Archive step accidentally moves content the agent will read in future sessions | low | low | INITIATIVE.md, RETROSPECTIVE.md, README.md, STATE.md, and phase plans stay in place; only `decisions/` and `checkpoints/` move |
| Operator wants to defer closeout indefinitely; initiative stays in-flight | low | low | the loop is paused-for-approval at Slice 6; operator can resume at their pace |

## Notes For Future Iterations

- The retrospective is the most important closeout artifact. It informs future initiatives.
- The archive structure means initiative artifacts remain accessible for forensics or precedent without cluttering the active planning surface.
- Once Sentinel is `INITIATIVE-COMPLETE`, the LOOP-PROMPT operator-resume signal is the only way to re-engage the initiative — typically not needed unless a defect is discovered post-closeout.
