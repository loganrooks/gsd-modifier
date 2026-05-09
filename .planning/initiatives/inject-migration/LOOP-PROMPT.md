# Loop Invocation Prompts

Use one of these prompts to invoke an iteration of the inject migration loop.

## Standard Iteration (most common)

Paste this into a fresh Claude Code session in the `gsd-modifier` repo, or use it with the `/loop` skill for periodic auto-advance.

```text
You are advancing the inject migration initiative by exactly one bounded slice.

Repo: /home/rookslog/workspace/projects/gsd-modifier

Read these in order:
1. .planning/initiatives/inject-migration/STATE.md
2. .planning/initiatives/inject-migration/GUARDRAILS.md
3. .planning/initiatives/inject-migration/PROTOCOL.md
4. The active phase plan named in STATE.md, e.g., .planning/initiatives/inject-migration/phases/00-surface-cleanup.md

Then:
- Run Cold Start steps from PROTOCOL.md
- Identify the next pending slice
- Execute exactly one slice per the slice spec
- Run all gates (slice-specific + baseline)
- Commit if green; checkpoint; update STATE.md; exit
- Stop and surface if any GUARDRAILS hard-stop or paused-for-approval condition fires

Do not advance more than one slice. Do not edit governance carriers, contract code, or files outside the slice's declared write set without explicit operator approval. Do not run state-mutating bootstrap scripts unless the phase plan authorizes it for the slice.

End the iteration cleanly when one of these is true:
- A slice's commit is in place AND STATE.md is updated AND a checkpoint is written
- A hard-stop or paused-for-approval condition has been written to STATE.md and a checkpoint
- The Sentinel in STATE.md is INITIATIVE-COMPLETE or ABORTED (do nothing; report and exit)
```

## With `/loop` Skill (auto-pacing)

Use the `loop` skill in dynamic-pacing mode (no interval — the agent self-paces between iterations):

```text
/loop

You are advancing the inject migration initiative by exactly one bounded slice each iteration.

Repo: /home/rookslog/workspace/projects/gsd-modifier

(rest of standard iteration prompt above)

After completing one slice, schedule the next iteration via ScheduleWakeup with delaySeconds based on the type of work just completed:
- After a small additive slice: 60–120s (cache-warm, fast follow-up)
- After a verification-heavy slice: 270s (cache-warm, lets bootstrap gate writes settle if any)
- After a paused-for-approval or blocked checkpoint: do NOT schedule; the operator decides
- After Sentinel becomes INITIATIVE-COMPLETE: do NOT schedule; exit cleanly

The loop terminates when STATE.md → Sentinel is INITIATIVE-COMPLETE or ABORTED.
```

## Cold-Start From a Cleared Context

If you are uncertain whether the previous iteration completed cleanly, use this prompt instead. It runs all reconciliation steps before any work.

```text
You are resuming the inject migration initiative after a context clear or new session.

Repo: /home/rookslog/workspace/projects/gsd-modifier

Step 1 — Reconciliation (no edits):
1. cd /home/rookslog/workspace/projects/gsd-modifier
2. git rev-parse HEAD
3. git status --short --branch
4. ls .planning/initiatives/inject-migration/checkpoints/ | tail -5
5. Read the most recent checkpoint file
6. Read .planning/initiatives/inject-migration/STATE.md
7. Confirm STATE.md → Last commit equals git rev-parse HEAD
8. Confirm STATE.md → Status, Phase, Slice within phase, and Sentinel
9. Confirm worktree dirtiness matches STATE.md → Dirty-Worktree Pre-Conditions

If reconciliation surfaces ANY divergence (commit mismatch, unexpected uncommitted files, contradictory checkpoint), STOP and surface a diagnosis without edits.

Step 2 — Decide:
- If most-recent checkpoint outcome is `success` AND STATE.md is consistent: proceed to standard iteration with the next pending slice
- If most-recent checkpoint outcome is `paused-for-approval`: surface the question recorded in that checkpoint to the operator and exit
- If most-recent checkpoint outcome is `blocked`: surface the blocker and exit; do not retry
- If most-recent checkpoint outcome is `aborted` OR Sentinel is INITIATIVE-COMPLETE: exit cleanly with a status report
- If checkpoints/ is empty (initiative not started yet): proceed to Phase 0 Slice 0 per Cold Start

Step 3 — Execute (only if reconciliation passed and decision is to proceed):
Run one bounded slice per PROTOCOL.md. End cleanly.
```

## Operator Status Query (read-only)

Use this to see initiative status without advancing.

```text
Read .planning/initiatives/inject-migration/STATE.md and .planning/initiatives/inject-migration/checkpoints/ (most recent 3 files). Produce a short status report:
- Current phase / slice / status
- Phase Progress checklist
- Last 3 checkpoints (timestamp, phase/slice, outcome, brief)
- Any active blockers
- Whether the loop is currently safe to advance (per GUARDRAILS preconditions)

Do not edit any files. Do not advance the loop.
```

## Operator Halt Signal

Use this to mark the initiative as aborted. Only the operator should invoke this.

```text
Set the inject migration initiative to ABORTED.

Steps:
1. Read .planning/initiatives/inject-migration/STATE.md
2. Edit STATE.md → Current Status → Status to `aborted`, Sentinel to `ABORTED`
3. Append an entry to Recent Checkpoints noting operator-initiated abort
4. Write a final checkpoint at checkpoints/<timestamp>-abort.md with reason: <fill in>
5. Commit the STATE.md change with subject: chore(initiative): mark inject-migration aborted

After this commit, no further iterations should proceed. The loop is terminated.
```

## Operator Resume Signal (after abort or pause)

To resume after an `aborted` state, the operator must reset the sentinel:

```text
Resume the inject migration initiative.

Steps:
1. Read .planning/initiatives/inject-migration/STATE.md
2. Confirm with operator (this prompt, by being invoked, IS the confirmation): change Sentinel from ABORTED back to NOT-STARTED or to the phase-appropriate value
3. Confirm any blockers in STATE.md → Blockers have been resolved (operator acknowledges)
4. Update Last updated, Last updated by, etc. as per the standard state-update protocol
5. Commit STATE.md change with subject: chore(initiative): resume inject-migration from <reason>

Then exit the iteration. The next standard iteration prompt will pick up from the new state.
```

## Tips For The Operator

- **Use the standard iteration prompt 80% of the time.** It's the simplest path.
- **Run a status query before sleep.** Use the read-only query to see where the loop ended without re-engaging.
- **Cold-start prompt after a long break.** If more than a day has passed since the last iteration, use the cold-start prompt to ensure reconciliation runs.
- **Never paste two prompts in a row.** Each prompt advances at most one slice; chaining them risks losing the iteration boundary that makes recovery work.
