Date: 2026-04-21
Status: landed bounded implementation

# Resume-Project Second-Consumer Implementation

## Purpose

- [g:r:i] This note records the accepted implementation of the bounded second-consumer slice proposed in `03`.
- [g:r:i] The job of this slice is not to widen the whole entry family. The job is to make project re-entry carry the existing uplift signal cleanly, through tracked overlay ownership and explicit materialization proof.

## What Landed

- [e:r:i] A new tracked overlay owner now exists at [tooling/portable-gsd/overlay/get-shit-done/workflows/resume-project.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/resume-project.md).
- [e:r:i] The new owner adds one bounded read-only bridge inside `present_status`:
  - load `UPLIFT_NOTE` through `python3 "__PROJECT_ROOT__/tooling/codex/project_uplift.py" progress-note "__PROJECT_ROOT__" --json`
  - render an `Uplift Posture` block only when `UPLIFT_NOTE.show` is `true`
- [e:r:i] The bridge reuses the existing helper contract instead of inventing a second parsing path for `STATE.md` or `UPLIFT-MANIFEST.json`.
- [e:r:i] The route remains non-absorptive:
  - no auto-write
  - no auto-refresh
  - no route takeover
  - no new dedicated uplift action inserted into option routing

## Materialization Boundary

- [e:r:i] `./scripts/setup-portable-gsd.sh` was rerun after the overlay owner landed.
- [e:r:i] The live runtime now carries the same bounded insertion at [.codex/get-shit-done/workflows/resume-project.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/resume-project.md).
- [e:r:i] This means the second-consumer slice is not an unmaterialized local patch; it is now real tracked overlay carry with installer-backed live proof.

## Propagation Consequence

- [d:r:i] The uplift chain now has two live routed consumers:
  - `progress`
  - `resume-project`
- [d:r:i] That strengthens ordinary project re-entry because uplift posture can now surface both during explicit progress checks and during direct session resumption.
- [d:r:i] This slice still does not widen into:
  - broader entry-family redesign
  - additive install routes
  - cross-runtime reconciliation
  - a third routed consumer family

## Review And Verification Gates

### Workflow And Language Gates

- [e:r:i] `python3 tooling/codex/scan_threshold_language.py tooling/portable-gsd/overlay/get-shit-done/workflows/resume-project.md`
- [e:r:i] `git diff --check`

### Materialization And Behavior Gates

- [e:r:i] `python3 tooling/codex/project_uplift.py progress-note . --json`
- [e:r:i] `./scripts/setup-portable-gsd.sh`
- [e:r:i] live reread confirmed the `UPLIFT_NOTE` load and `Uplift Posture` rendering block in `.codex/get-shit-done/workflows/resume-project.md`

### Workspace Gates

- [e:r:i] `python3 tooling/codex/audit_refmap.py verify .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign`
- [e:r:i] `git diff --check`

## What This Slice Holds For Later

- [d:r:i] Keep later follow-through explicit rather than absorbing it here:
  - whether `resume-project` should ever route into a dedicated uplift action
  - whether another entry surface should become a third routed consumer
  - whether a broader external propagation challenge should now test the strengthened producer / consumer chain
  - whether later additive-install and cross-runtime families should inherit from this cleaner two-consumer baseline

## Current Consequence

- [d:r:i] The propagation family now includes one concrete follow-through implementation, not only a seed, opening note, map, and proposal.
- [d:r:i] The next stronger question is no longer whether a second consumer is warranted in the abstract.
- [d:r:i] The next stronger question is what external or wider local scrutiny should test this now-strengthened chain before later family widening.
