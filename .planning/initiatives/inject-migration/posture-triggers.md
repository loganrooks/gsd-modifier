# Change-Class Triggers — Operational Checklist

Companion to AGENTS.md "Workflow Rules → Change-Class Triggers" for inject-migration loop operators and reviewers. AGENTS.md is authoritative; this file is a quick-reference restating of the five classes with concrete repo examples.

## Five Trigger Classes

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
