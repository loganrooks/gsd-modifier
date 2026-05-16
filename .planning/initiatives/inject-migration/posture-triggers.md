# Change-Class Triggers — Operational Checklist

Companion to AGENTS.md "Workflow Rules → Change-Class Triggers" for inject-migration loop operators and reviewers. AGENTS.md is authoritative; this file is a quick-reference restating of the six classes with concrete repo examples.

## Six Trigger Classes

### 1. Overlay carrier add/remove

Triggering paths:

- `tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json` (entry add/remove or `mode`/`source` change)
- `tooling/portable-gsd/overlay/**/*` (file add/remove/move)
- `harness_modifier/overlay/**/*` (file add/remove/move)

Examples in this initiative: Phase 0 Slices 1–4 (gsd-do, gsd-from-gsd2, gsd-plant-seed, research-phase) flipping `mode: overwrite → add` and moving sources.

### 2. Contract surface change

Triggering paths:

- `harness_modifier/contract/**/*.py`
- `tooling/codex/audit_refmap.py`
- `tooling/codex/scan_threshold_language.py`

Examples in this initiative: Phase 2 will modify `portable_gsd_contract.py` to implement validate/apply/extract/verify for `mode: inject`.

### 3. Install/bootstrap script change

Triggering paths:

- `scripts/setup-portable-gsd*.sh`
- `scripts/ci/check-*.sh`

Examples in this initiative: deferred; no current slice modifies these. If a slice needs to, surface to the operator first.

### 4. Governance carrier change

Triggering paths:

- `AGENTS.md`
- `CLAUDE.md`
- `WORKFLOW.md`
- `docs/handoff/current.md`
- `.planning/STATUS.md`
- `.planning/CURRENT-STATE.md`

Examples in this initiative: Phase 0 Slice 5 (this slice — adds the Change-Class Triggers subsection itself).

### 5. Plan disposition or premise change

Triggering paths:

- `evidence/decision.md`
- `evidence/implementation-disposition.md`
- Any other decision artifact under `.planning/` describing why an earlier plan was adjusted or abandoned

Examples in this initiative: the orientation artifact (release-readiness-orientation-2026-05-08.md) and intervention-strategies (intervention-strategies-2026-05-08.md) are the load-bearing premise inputs; any future ADR or premise revision under `.planning/initiatives/inject-migration/` falls here.

### 6. Inject mechanism change

Triggering paths:

- `.planning/initiatives/inject-migration/decisions/ADR-001-manifest-schema-v4.md` (operation kind catalog, marker conventions, `parity_intent` semantics, backward-compat shims)
- Future ADRs under `.planning/initiatives/inject-migration/decisions/` that extend the inject mechanism (e.g., the `append_after_text` or non-XML markdown anchor amendments surfaced in ADR-001 Appendix A "Patterns surfaced")
- Files in `harness_modifier/contract/` that implement inject operations (overlap with class #2 contract surface; this class adds the spec-design dimension)

Distinction from class #2 (contract surface change): class #2 covers code that VALIDATES manifests and applies materialization; class #6 covers the DESIGN of the inject mechanism (schema-version 4 spec, operation semantics, marker conventions, `parity_intent` semantics). New operation kinds count as inject mechanism changes; new USES of existing operation kinds do not.

Examples in this initiative: ADR-001 (Phase 1 Slices 1 and 2) is itself an inject mechanism change — it introduces the v4 schema. Future amendments to ADR-001's catalog (e.g., adding `append_after_text` per the schema gap surfaced in Appendix A) would also fall in this class.

## When In Doubt

- The slice spec authoritatively pre-authorizes specific changes within a class. If your change matches a slice's declared write set, the trigger is already addressed.
- If your change is outside the slice spec but inside a trigger class: route through the matching reviewer in [REVIEWERS.md](REVIEWERS.md) "Reviewer-Mediated Continuation" table.
- If unsure which class your change falls under: read AGENTS.md "Workflow Rules → Change-Class Triggers" and the parallel CLAUDE.md acknowledgement; the canonical list lives there.

## Out Of Scope (No Trigger)

- Documentation typos with no semantic change
- Test additions confirming existing behavior
- Comment-only changes
- Whitespace/formatting confined to one file

These proceed under the "small mechanical fixes" carve-out in AGENTS.md "Workflow Rules".
