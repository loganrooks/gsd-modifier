# `/goal` Invocation

This initiative runs under `/goal`. The operator invokes `/goal` once with the condition string below; the runtime fires turns automatically until the condition is met or a hard-stop terminates the goal.

The operator's only obligations: initial GO, manual interrupt if needed, hard-stop responses, final retrospective review.

## Primary: `/goal` Invocation

Paste this into a Claude Code session at `/home/rookslog/workspace/projects/gsd-modifier` (v2.1.139 or later required):

````text
/goal The inject-migration initiative has reached a terminal or operator-required state. Specifically, the most recent agent turn output contains a [GOAL-EVAL] line whose `Sentinel:` field is INITIATIVE-COMPLETE or ABORTED, OR whose `Turn-end:` field begins with `hard-stop-`. The condition is also met if the turn cap of 300 turns is exceeded (runaway safety floor).

For each turn, the agent must:

1. Set working directory to /home/rookslog/workspace/projects/gsd-modifier
2. Read in order: .planning/initiatives/inject-migration/STATE.md, GUARDRAILS.md, REVIEWERS.md, PROTOCOL.md, the active phase plan in phases/
3. Run Cold Start reconciliation per PROTOCOL.md "Cold Start"
4. If Sentinel is INITIATIVE-COMPLETE or ABORTED: output [GOAL-EVAL] line and end turn
5. Otherwise identify the next pending slice from the active phase plan
6. Execute exactly one bounded slice per its slice spec
7. Run slice's verification gates; if fail, invoke auto-recovery per GUARDRAILS.md
8. If slice spec mandates a reviewer, spawn it via Agent tool per REVIEWERS.md
9. At phase boundary (last slice of phase commits), spawn trajectory-verifier in a separate turn
10. Commit with Why/Verification/Boundary body, Initiative: trailer, and Reviewer: trailer if applicable
11. Update STATE.md atomically per PROTOCOL.md "State-Update Protocol"
12. Write checkpoint to checkpoints/<UTC-timestamp>-phase<NN>-slice<MM>.md per template
13. Output the [GOAL-EVAL] line on its own; end the turn

Discipline:
- Exactly one slice per turn
- Reviewer verdicts are mandatory at the gates declared in REVIEWERS.md
- Hard-stops (5 conditions in GUARDRAILS.md) emit HARD-STOP: <reason> and end the turn
- Forbidden actions (15 in GUARDRAILS.md) are never taken regardless of reviewer recommendation

Or stop after 300 turns.
````

That's it. Hit enter, then walk away. The `◎ /goal active` indicator shows the loop running.

## Status Check (read-only, no advancement)

While `/goal` is running, you can check status at any time without disturbing it:

````text
/goal
````

Returns the condition, elapsed time, turn count, token spend, and the evaluator's most recent reasoning.

## Manual Interrupt

Stop the goal before completion:

````text
/goal clear
````

Or `/goal stop` / `off` / `reset` / `none` / `cancel` (aliases).

Or Ctrl+C if in interactive mode.

After an interrupt, the most-recent checkpoint records where the loop stopped; the next `/goal` invocation will resume from that state via Cold Start reconciliation.

## Resume After Hard-Stop

If the goal terminated due to a `HARD-STOP:` line:

1. Read `STATE.md → Status` (should be `paused-for-operator`)
2. Read the most-recent checkpoint's `## Question for operator` section
3. Address the question:
   - Edit slice spec / phase plan / governance carrier if the question requires it (operator-only)
   - Or accept the diagnosis and approve a recovery action
4. Update STATE.md → Status from `paused-for-operator` back to `pending` (or appropriate value)
5. Re-invoke `/goal` with the same condition string above
6. The next turn fires Cold Start, sees `success` checkpoint status (after your edit), and proceeds

## Resume After Abort

To resume from `Sentinel: ABORTED`:

````text
# Operator-only — say this in a fresh session:
Resume the inject migration initiative.

Steps:
1. Read .planning/initiatives/inject-migration/STATE.md
2. Change Sentinel from ABORTED to NOT-STARTED (or to the phase-appropriate value)
3. Confirm any Blockers have been resolved
4. Update Last updated, Last updated by, etc. per the standard state-update protocol
5. Commit STATE.md change with subject: chore(initiative): resume inject-migration from <reason>

Then exit. Re-invoke /goal with the standard condition string from LOOP-PROMPT.md.
````

## Operator Halt (force abort mid-run)

If you need to force-abort instead of just pause:

````text
# Operator-only — say this in a fresh session:
Set the inject migration initiative to ABORTED.

Steps:
1. Read .planning/initiatives/inject-migration/STATE.md
2. Edit STATE.md → Current Status → Status to `aborted`, Sentinel to `ABORTED`
3. Append an entry to Recent Checkpoints noting operator-initiated abort
4. Write a final checkpoint at checkpoints/<timestamp>-abort.md with reason: <fill in>
5. Commit the STATE.md change with subject: chore(initiative): mark inject-migration aborted

After this commit, no further turns proceed. /goal will detect ABORTED on next invocation and exit cleanly.
````

## Fallback: Manual Single-Turn Invocation

For debugging or recovery scenarios where `/goal` is unavailable or where you want to advance exactly one turn manually:

````text
You are advancing the inject migration initiative by exactly one bounded slice.

Repo: /home/rookslog/workspace/projects/gsd-modifier

Read in order:
1. .planning/initiatives/inject-migration/STATE.md
2. .planning/initiatives/inject-migration/GUARDRAILS.md
3. .planning/initiatives/inject-migration/REVIEWERS.md
4. .planning/initiatives/inject-migration/PROTOCOL.md
5. The active phase plan named in STATE.md

Then run the Per-Turn Flow from PROTOCOL.md exactly once. End with the [GOAL-EVAL] line per Turn-End Discipline.

Do not advance more than one slice. Do not edit governance carriers, contract code, or files outside the slice's declared write set without spawning the required reviewer per REVIEWERS.md.
````

This prompt does what one `/goal` turn would do, but only once. Useful when you want to step through manually.

## Tips

- **Use `/goal` for normal operation.** The `/goal` model is the supported autonomous-run path.
- **The 300-turn cap is a safety floor**, not a target. The initiative is sized at roughly 80–120 slices total, so 300 turns gives plenty of headroom even with reviewer-mediated retries.
- **Reviewer invocations consume tokens.** Each phase-boundary trajectory-verifier + each ADR adversarial-auditor costs more than a regular slice. Expect 2–4x the per-slice spend for reviewer-heavy slices (Phase 1, 2, 3, 9, 10).
- **Hard-stop responses are the only synchronous operator work.** If the loop runs for 12 hours without a hard-stop, the operator was rightfully absent for 12 hours.
- **Adversarial verdicts going FAIL are not the same as hard-stops.** A FAIL is auto-recovered through the patterns in GUARDRAILS.md. A hard-stop is when even recovery isn't safe. Watch the loop's recovery counters in STATE.md for early signal that things are wobbling.
