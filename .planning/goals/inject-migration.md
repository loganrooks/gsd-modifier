# Goal: Inject Migration Initiative

Drives the autonomous initiative at [`.planning/initiatives/inject-migration/`](../initiatives/inject-migration/INITIATIVE.md). Migrates the modifier's overlay model from overwrite-heavy (~49 carriers) to surgical injection (`mode: inject` operations against known anchors).

## Context

| Field | Value |
|---|---|
| Workstream | Inject migration initiative |
| Workstream home | [`.planning/initiatives/inject-migration/`](../initiatives/inject-migration/) |
| Starting state (at goal invocation) | `STATE.md → Sentinel: NOT-STARTED`, Phase 0 Slice 0 |
| Terminates on | `Sentinel: INITIATIVE-COMPLETE`, `Sentinel: ABORTED`, any `HARD-STOP: <reason>` in turn output, or 300-turn safety cap |
| Operator presence required at | initial invocation (below), manual interrupt, hard-stop responses, final retrospective review |
| Required Claude Code version | v2.1.139 or later |

## Read order before invocation (optional — the agent reads these per turn anyway)

1. [`STATE.md`](../initiatives/inject-migration/STATE.md) — current state (sentinel + phase + slice + counters)
2. [`GUARDRAILS.md`](../initiatives/inject-migration/GUARDRAILS.md) — 5 hard stops + reviewer-mediated continuation
3. [`REVIEWERS.md`](../initiatives/inject-migration/REVIEWERS.md) — reviewer roster + prompt templates + verdict semantics
4. [`PROTOCOL.md`](../initiatives/inject-migration/PROTOCOL.md) — turn-end discipline + reviewer spawning
5. [`INITIATIVE.md`](../initiatives/inject-migration/INITIATIVE.md) — mission, phase catalog, completion criteria

## /goal invocation (canonical)

Paste verbatim into a fresh Claude Code session at `/home/rookslog/workspace/projects/gsd-modifier`:

```text
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
```

## Status check (read-only, no advancement)

While the goal is running:

```text
/goal
```

Returns the condition, elapsed time, turn count, token spend, and evaluator's most recent reasoning.

## Manual interrupt

```text
/goal clear
```

Aliases: `stop`, `off`, `reset`, `none`, `cancel`. Or Ctrl+C in interactive mode.

After interrupt, the most-recent checkpoint records where the loop stopped; re-pasting the `/goal` block above will resume from that state via Cold Start reconciliation.

## Resume after hard-stop

If the goal terminated due to a `HARD-STOP:` line:

1. Read `STATE.md → Status` (should be `paused-for-operator`)
2. Read the most-recent checkpoint's `## Question for operator` section
3. Address the question — edit the slice spec / phase plan / governance carrier as needed (operator-only); or accept the diagnosis and approve a recovery action
4. Update `STATE.md → Status` from `paused-for-operator` back to `pending`
5. Re-invoke `/goal` with the same block above
6. Next turn fires Cold Start, sees `success` checkpoint status, proceeds

Full recovery flow: [`LOOP-PROMPT.md → Resume After Hard-Stop`](../initiatives/inject-migration/LOOP-PROMPT.md).

## Resume after abort

To resume from `Sentinel: ABORTED`, edit STATE.md → Sentinel back to a non-terminal value (operator-only), then re-invoke `/goal` above. See [`LOOP-PROMPT.md → Resume After Abort`](../initiatives/inject-migration/LOOP-PROMPT.md) for the full procedure.

## See also

- [`LOOP-PROMPT.md`](../initiatives/inject-migration/LOOP-PROMPT.md) — initiative's operator-facing invocation surface (status check, manual interrupt, halt, fallback manual single-turn prompt)
- [`README.md`](README.md) — goal prompts registry convention
