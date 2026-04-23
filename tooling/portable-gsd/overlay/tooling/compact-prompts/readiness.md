Preserve continuity for an engineering planning/workflow session.

Produce a compact replacement history that is concise but operationally faithful.

Prioritize, in order:

1. the active control surface and its entrypoint path
2. the exact control files that must be reopened first
3. current checkpoint or current task
4. immediate next action
5. current blockers, open findings, unresolved questions, and open opportunities
6. latest meaningful commit/checkpoint boundary if relevant to current work
7. review/closure requirements that must survive compaction
8. user corrections or policy changes that changed how the work must proceed
9. distinctions that must not flatten in summary:
   - decided vs open
   - preserve-only vs active
   - milestone scope vs long-arc doctrine
   - current task vs deferred follow-up
10. if the work is on harness improvement rather than host-product delivery:
   - keep harness-program horizons separate from host-product horizons
   - name whether `uplift` refers to harness-contract, host-artifact, harness-agential, harness-operational, harness-adaptive, or distribution/deployability change
11. if a live external lane exists:
   - preserve the lane id, frozen basis commit, estimated runtime window, and whether it is still running or completed
   - preserve what companion work is safe while it runs and what must wait for inheritance
12. preserve the intended carrier for open findings when that has been made explicit:
   - active bounded slice
   - held later
   - seed
   - deferred residue
   - doctrine / protected seam
   - audit-family memory
13. if the work is inside a harness-program tranche rather than host-product delivery:
   - preserve the active tranche id and its adjacent proposal/implementation carrier
   - preserve lifecycle-loop state:
     - intended effects
     - propagation obligations
     - monitor target
     - current disposition verb
   - preserve the paired propagation companion id and state when one exists
   - preserve any scheduled bounded verification/review work that was explicitly earned by the slice
   - preserve the explicit Phase 01 rerun hold across that tranche

Prefer exact repo file paths over vague prose.

If the active control surface is the Phase 01 readiness package, preserve explicitly:

- package entrypoint:
  - `.planning/readiness/phase-01-rerun/INDEX.md`
- minimum read order:
  - `PLAN.md`
  - `STATUS.md`
  - `STATE.yaml`
  - active gate under `GATES/`
- current checkpoint id, name, and state
- current task and immediate next action
- current blockers and open findings from `STATUS.md` / `STATE.yaml`
- whether the worktree is expected to be clean
- latest relevant readiness checkpoint commits if they are load-bearing to the next move
- active review constraints from:
  - `.planning/readiness/phase-01-rerun/REVIEW-POLICY.yaml`
  - `.planning/readiness/phase-01-rerun/CHECKPOINT-REVIEW-MATRIX.md`
- whether major checkpoint closure requires an independent reviewer
- whether cross-vendor review is required, preferred, conditional, or not required
- any package files that must be updated after the next meaningful action:
  - `STATUS.md`
  - `STATE.yaml`
  - active gate file
  - `CHECKPOINT-LEDGER.md` when a checkpoint boundary is committed
  - `RESEARCH-INTAKE.md`, `TASKS.md`, `DEVIATIONS.md`, or `OPPORTUNITIES.md` if the next action changes them

Do not waste space on:

- pleasantries
- repetitive restatement
- broad transcript retelling
- stale alternatives already rejected

If the current work references a control package, preserve that package and its live state explicitly.

If the session is at a checkpoint boundary, preserve:

- what has already been committed
- what remains uncommitted
- what must happen before the next delegation or rerun
- whether a session re-entry check should be rerun from `.planning/SESSION-REENTRY-CHECKLIST.md`

If there is uncertainty, preserve it as uncertainty. Do not make open questions sound settled.
