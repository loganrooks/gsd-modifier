# Inject Migration Loop Protocol

The loop is **`/goal`-driven**: the operator invokes `/goal <condition>` once; the runtime fires a new turn after each turn ends until the condition is met or a hard-stop fires. Each turn advances the initiative by exactly one bounded slice and ends with a parseable `[GOAL-EVAL]` line that the `/goal` evaluator (a small fast model) reads.

This document defines: read order, cold-start reconciliation, the per-turn flow, reviewer integration, auto-recovery, turn-end discipline, and resume mechanics after context clears.

## Read Order (every turn, in this order)

1. `STATE.md` — where we are
2. `GUARDRAILS.md` — what's safe
3. `REVIEWERS.md` — which reviewer at which gate; verdict format
4. The active phase plan: `phases/<NN>-<slug>.md` (where `<NN>` is `STATE.md → Current Status → Phase`)
5. `INITIATIVE.md` — only if the phase plan references it (mostly for cross-phase context)

You do **not** need to read other phase files unless the active phase plan references them or you are escalating a cross-phase concern.

## Cold Start (first turn after context clear or new session)

1. **Verify the repo location**: working directory is `/home/rookslog/workspace/projects/gsd-modifier`. If not, hard-stop.
2. **Verify branch**: `git rev-parse --abbrev-ref HEAD` should return `main` unless `STATE.md → Current Status` says otherwise. If not on `main`, hard-stop.
3. **Read the five files** in the order above.
4. **Reconcile STATE.md against `git log`**: `git rev-parse HEAD` must equal `STATE.md → Last commit`. If they diverge, treat `git log` as ground truth and update STATE.md before proceeding.
5. **Verify clean worktree**: `git status --short` should show only items listed in `STATE.md → Dirty-Worktree Pre-Conditions`. Any other untracked or modified files trigger the worktree-drift auto-recovery pattern (see GUARDRAILS.md).
6. **Check the sentinel**: if `STATE.md → Sentinel` is `INITIATIVE-COMPLETE` or `ABORTED`, output `[GOAL-EVAL] Sentinel: <value>` and end the turn. The `/goal` evaluator will terminate the goal.
7. **Check the most-recent checkpoint outcome**:
   - `success` → proceed to Per-Turn Flow
   - `paused-for-operator` → hard-stop with the prior reason; end the turn
   - `blocked` → re-attempt the same slice via auto-recovery (this is what the 3-consecutive-failure rule counts)
   - `aborted` → end the turn

## Per-Turn Flow

```text
┌────────────────────────────────────────────────────────────────────────────┐
│ 1. Cold Start / Reconciliation                                             │
├────────────────────────────────────────────────────────────────────────────┤
│ 2. Identify the next pending slice                                         │
│    Read phase plan; find slice marked `[ ]` with no unmet dependencies.    │
├────────────────────────────────────────────────────────────────────────────┤
│ 3. Pre-execute checks                                                      │
│    - Worktree clean (or matches declared pre-conditions)                   │
│    - Slice's preconditions (per phase plan) satisfied                      │
│    - No incompatible STATE.md flags                                        │
├────────────────────────────────────────────────────────────────────────────┤
│ 4. Reviewer-required-before-execute? (some slices)                         │
│    e.g., ADR slices: spawn adversarial-auditor BEFORE writing the ADR      │
│    e.g., contract slices: spawn auditor on the proposed diff first         │
├────────────────────────────────────────────────────────────────────────────┤
│ 5. Execute slice                                                           │
│    - Follow slice spec exactly                                             │
│    - Stay within the slice's declared write set                            │
│    - If a needed write is outside spec → spawn Plan reviewer for           │
│      surface-change evaluation (auto-recovery pattern)                     │
├────────────────────────────────────────────────────────────────────────────┤
│ 6. Run verification gates                                                  │
│    - Per slice spec (specific to the slice)                                │
│    - Plus baseline gates (audit_refmap; git diff --check)                  │
│    - If green → step 7                                                     │
│    - If red → invoke Verification-Gate-Fail auto-recovery (GUARDRAILS.md)  │
├────────────────────────────────────────────────────────────────────────────┤
│ 7. Reviewer (per slice / per phase boundary)                               │
│    - Per-slice review is OPTIONAL (only if slice spec mandates)            │
│    - At phase boundary (last slice of phase): spawn trajectory-verifier    │
│    - At phase debrief slice: spawn adversarial-auditor-xhigh               │
│    - Capture verdict per REVIEWERS.md; act on it                           │
├────────────────────────────────────────────────────────────────────────────┤
│ 8. Commit                                                                  │
│    - Conventional subject; Why/Verification/Boundary body                  │
│    - Initiative: trailer                                                   │
│    - Reviewer: trailer if a reviewer's verdict influenced the commit       │
├────────────────────────────────────────────────────────────────────────────┤
│ 9. Update STATE.md                                                         │
│    - Last commit, Last checkpoint, Slice within phase                      │
│    - Status, Counters                                                      │
│    - Reviewer Decisions Log (append row if a reviewer was invoked)         │
│    - Auto-Recovery Counters (increment if relevant)                        │
│    - Phase Progress (mark [x] if phase just completed)                     │
├────────────────────────────────────────────────────────────────────────────┤
│ 10. Write checkpoint                                                       │
│    checkpoints/<UTC-timestamp>-phase<NN>-slice<MM>.md per template         │
├────────────────────────────────────────────────────────────────────────────┤
│ 11. Output [GOAL-EVAL] line (Turn-End Discipline below)                    │
│     End the turn. /goal evaluator decides whether to fire next turn.       │
└────────────────────────────────────────────────────────────────────────────┘
```

## Slice Execution Discipline

For each slice the agent must:

1. **Re-read the slice spec** from the phase plan before any edit
2. **Compute the proposed write set** and confirm it is fully contained in the spec's `Write Set` section
3. **Apply edits** using `Edit` / `Write` tools as appropriate
4. **Run the slice's `Verification` gates** in the order specified
5. **If gates pass, optionally spawn slice-level reviewer** (only when slice spec mandates)
6. **Commit** with the slice's specified `Commit message`
7. **Update STATE.md** with the new `Last commit`, `Last checkpoint`, advance `Slice within phase`
8. **Write checkpoint** to `checkpoints/<UTC-timestamp>-phase<NN>-slice<MM>.md`
9. **Print `[GOAL-EVAL]` line**
10. **End the turn** — do not start the next slice in the same turn.

The one-slice-per-turn discipline is what makes the loop resumable and bounded. The `/goal` evaluator fires the next turn automatically; the agent does not.

## Reviewer Spawning (when, how, what)

Reviewers are mediated through the `Agent` tool. The main agent never edits files based on a reviewer's claim alone — only based on a parsed verdict block.

### Per-slice mandate

Most slices do not require a slice-level reviewer (the slice's automated gates + the phase-boundary reviewer are sufficient).

Slices that DO mandate a slice-level reviewer:

- Any slice that produces an ADR file (Phase 1 ADR-001, Phase 9 ADR-002): pre-execute reviewer on the planned content; post-execute reviewer on the committed content
- Phase 2 contract code slices: pre-commit reviewer on the proposed diff
- Phase 3 pilot slice: post-commit reviewer on the pilot result
- Phase 6 first new operation kind: post-commit reviewer on the first use
- Phase 10 closeout: per-slice reviewers as defined in `phases/10-closeout.md`

The phase plan's slice spec authoritatively says whether a slice requires a reviewer. If silent, no reviewer is required at slice level.

### Phase-boundary mandate

After the LAST slice of a phase commits, BEFORE marking the phase `[x]` in STATE.md, the agent MUST spawn `trajectory-verifier` per the REVIEWERS.md "Phase Boundary Verification" template. The verdict determines whether STATE.md advances:

- PASS: mark phase `[x]`, advance to next phase
- FAIL: do not advance; the verifier's RECOMMENDATION points at the unmet criterion; treat as a new slice (revise the phase plan if needed via operator, or re-attempt the unmet criterion)
- ESCALATE: triangulate with `adversarial-auditor-xhigh` per REVIEWERS.md
- HALT: hard-stop

This is a SEPARATE turn from the last slice's commit turn. The last slice commits in turn N; the phase-boundary verification runs in turn N+1.

### Invocation mechanics

```text
1. Compose input per REVIEWERS.md template (substitute placeholders)
2. Call: Agent({subagent_type: '<reviewer>', description: '<short>', prompt: '<composed input>'})
3. Parse VERDICT/REASONING/RECOMMENDATION/EVIDENCE from the agent's returned message
4. Act per REVIEWERS.md verdict semantics
5. Record:
   - STATE.md → Reviewer Decisions Log (append row)
   - The next checkpoint's "## Reviewer Verdict" section
   - The commit body (Reviewer: trailer)
```

If the reviewer's response cannot be parsed into a verdict block, treat as ESCALATE and triangulate.

## Auto-Recovery Protocol

Failures that do NOT hard-stop are recovered as follows (full table in GUARDRAILS.md → "Auto-Recovery Patterns"):

```text
Verification gate fail
  → retry once
  → spawn gsd-debugger
  → if debugger PASS: apply fix, re-run gate
  → if debugger FAIL outside scope: spawn Plan reviewer for scope review
  → if Plan PASS: expand scope, log expansion, apply, re-run
  → if Plan FAIL: hard-stop
  → if debugger ESCALATE: triangulate
  → if debugger HALT: hard-stop
```

The 3-consecutive-failure rule fires when STATE.md shows the same slice has been retried 3 times (across 3 turns). At that point, the next failure is an automatic hard-stop without retry.

## Hard-Stop Protocol

When a hard-stop condition fires (see GUARDRAILS.md "Hard Stops"):

1. Do NOT commit any pending changes; restore worktree
2. Update STATE.md → Status to `paused-for-operator`
3. Write checkpoint with outcome `paused-for-operator` and a `## Question for operator` section detailing what's needed
4. Output `HARD-STOP: <reason>` on its own line
5. Output the `[GOAL-EVAL]` line indicating Turn-end: hard-stop
6. End the turn

The `/goal` evaluator detects `HARD-STOP:` in the turn output (per the condition string in LOOP-PROMPT.md) and terminates the goal.

## Turn-End Discipline

Every turn — successful or not — must output a single parseable `[GOAL-EVAL]` line as the last meaningful content. The `/goal` evaluator (a small fast model) reads the transcript and decides whether to fire the next turn.

Format (exact; one line; placeholders filled):

```text
[GOAL-EVAL] Sentinel: <NOT-STARTED|IN-PROGRESS|INITIATIVE-COMPLETE|ABORTED> | Status: <pending|in-progress|paused-for-operator|blocked|complete> | Phase: <NN> | Slice: <MM> | Turn-end: <slice-complete|phase-complete|hard-stop-{reason}|initiative-complete|aborted>
```

Examples:

- After Phase 0 Slice 0 (sanity check, no commit): `[GOAL-EVAL] Sentinel: IN-PROGRESS | Status: in-progress | Phase: 0 | Slice: 1 | Turn-end: slice-complete`
- After Phase 0 last slice + phase complete: `[GOAL-EVAL] Sentinel: IN-PROGRESS | Status: in-progress | Phase: 1 | Slice: 0 | Turn-end: phase-complete`
- At hard-stop: `[GOAL-EVAL] Sentinel: IN-PROGRESS | Status: paused-for-operator | Phase: 3 | Slice: 4 | Turn-end: hard-stop-reviewer-deadlock`
- At initiative completion: `[GOAL-EVAL] Sentinel: INITIATIVE-COMPLETE | Status: complete | Phase: 10 | Slice: 6 | Turn-end: initiative-complete`

The `/goal` condition (per LOOP-PROMPT.md) is constructed so that the evaluator detects these terminal markers in the line:

- `Sentinel: INITIATIVE-COMPLETE` → goal met
- `Sentinel: ABORTED` → goal met
- `Turn-end: hard-stop-*` → goal met
- Anything else → fire next turn

If the agent forgets to output `[GOAL-EVAL]`, the evaluator cannot ground its decision. As a safety floor, the `/goal` condition also includes a turn cap ("or stop after 300 turns") so runaway loops terminate.

## Checkpoint Template

Each turn writes one file at `checkpoints/<UTC-timestamp>-phase<NN>-slice<MM>.md` in this format:

```markdown
# Checkpoint phase <NN> slice <MM>

Timestamp: <ISO-8601 UTC>
Phase: <NN>-<slug>
Slice: <MM>-<slug>
Outcome: <success | blocked | aborted | paused-for-operator>
Commit: <SHA or "(no commit)">

## What was done
- <bullet>

## Files touched
- <path> (added | modified | deleted)

## Verification gates run
- <gate name>: <result> (<exit code or notes>)

## Reviewer Verdict
- (if no reviewer invoked: "n/a — slice did not require reviewer")
- (if reviewer invoked: reviewer type, full verdict block from REVIEWERS.md format, action taken)

## Auto-Recovery
- (if none: "none")
- (if any: which pattern fired, how many retries, outcome)

## Observations
- <any non-trivial notes the next turn should know>

## Question for operator
(only present if Outcome is paused-for-operator)
- <what the agent needs to know>

## Next expected slice
- <NN>-<slug> slice <MM+1> (or "phase complete; advance to phase <NN+1>")
```

## State-Update Protocol

The agent updates `STATE.md` at the end of each turn. Update is **atomic** — either all fields update or none do. If a write fails partway, the next turn's reconciliation step (Cold Start step 4) will detect the divergence.

Fields to update at turn end:

- `Last updated` (timestamp)
- `Last updated by` (use the literal string `inject-migration /goal agent`)
- `Current Status → Slice within phase` (advance by 1, or move to next phase if last slice complete)
- `Current Status → Status` (one of the enum values)
- `Current Status → Last checkpoint` (path to checkpoint file just written)
- `Current Status → Last commit` (`git rev-parse HEAD`)
- `Phase Progress` (mark `[x]` if a phase just completed)
- `Active Work` (next task description; or `(none — paused)` etc.)
- `Counters` (increment relevant counters)
- `Reviewer Decisions Log` (append row if reviewer was invoked)
- `Auto-Recovery Counters` (increment if relevant)
- `Recent Checkpoints` (append new checkpoint summary line; keep last 10 entries)

## When To Spawn Subagents (general — not reviewers)

Reviewers are spawned per REVIEWERS.md. The main agent MAY spawn other subagents for bounded research or evidence-gathering, but **never** for code changes. Code changes happen in the main loop only.

Use cases for non-reviewer subagents:

- Reading large upstream files to confirm a hypothesis (use `Explore` with read-only intent)
- Cross-referencing many overlay carriers in parallel (single `Explore` agent with batched targets)

Subagent constraints:

- Strictly read-only
- Bounded (single deliverable; clear exit criteria)
- Returned within one turn

Spawning a subagent is a state-mutating decision (it appears in the transcript). Log it in the checkpoint's Observations.

## Failure Recovery (in-turn)

When a verification gate fails, the agent attempts recovery per the auto-recovery pattern. The hard-stop triggers are:

- 3-consecutive-failure rule fires (next failure halts without retry)
- Reviewer triangulation deadlocks
- A failure exposes a corrupted initiative file (self-diagnosis)
- A failure requires forbidden actions to fix

## Resume After Context Clear

A context clear means the agent's working memory is gone but `STATE.md`, `git log`, and the filesystem persist. The `/goal` invocation also clears in this case unless the session was resumed via `--resume` or `--continue`. The operator may re-invoke `/goal` with the same condition string.

Resume flow:

1. Operator invokes `/goal <condition>` (or resumes the session)
2. First turn fires
3. Agent runs Cold Start steps (the discipline above)
4. Reconciliation against `git log` catches any STATE.md drift
5. Check most-recent checkpoint outcome:
   - `success` → proceed to Per-Turn Flow with next slice
   - `paused-for-operator` → re-emit HARD-STOP marker; end turn; operator must address before resuming
   - `blocked` → 3-consecutive-failure counter consulted; retry or hard-stop accordingly
   - `aborted` → emit ABORTED sentinel; end turn; operator must reset to resume
6. If `checkpoints/` is empty (initiative just started), proceed to Phase 0 Slice 0

## Verification Stack (per-turn)

Baseline gates that every turn runs in addition to slice-specific gates:

```bash
git diff --check
python3 tooling/codex/audit_refmap.py verify .
```

These are fast (seconds), so they run on every commit. Exit must be 0.

**Per-phase gates** are documented in each phase plan's `Exit Criteria` section. They run at phase boundaries.

**Initiative-level gates** are documented in `INITIATIVE.md → Completion Criteria`. They run at Phase 10 closeout.

**State-mutating bootstrap gates** (`bash scripts/ci/check-deterministic.sh`, `bash scripts/ci/check-bootstrap.sh`) run only at phase boundaries when the phase plan explicitly authorizes it. Running them mid-phase risks materialization-side-effects polluting the worktree mid-slice.

## Commit Discipline

Every slice produces exactly one commit. Commit message format follows AGENTS.md "Commit Hygiene":

```text
<type>(<scope>): <imperative summary>

Why: <one paragraph>

Verification: <commands run + results>

Boundary: <what's intentionally held out of this commit>

Reviewer: <reviewer-type VERDICT @ context — if applicable>

Initiative: inject-migration phase <NN> slice <MM>
```

The `Reviewer:` trailer is REQUIRED when a reviewer's verdict influenced the commit (any per-slice reviewer; any phase-boundary reviewer; any auto-recovery reviewer). It is OMITTED for slices that did not invoke a reviewer.

The `Initiative:` trailer is REQUIRED for all initiative slices. It enables `git log --grep "Initiative: inject-migration"` to enumerate all slice commits cleanly.

## Loop Termination

The loop terminates when one of these is true:

- `STATE.md → Sentinel` is set to `INITIATIVE-COMPLETE` (after Phase 10 closeout)
- `STATE.md → Sentinel` is set to `ABORTED` (operator-decided early termination)
- A `HARD-STOP: <reason>` is emitted (operator must address before resuming)
- `/goal` evaluator hits the turn cap (runaway safety floor; operator must inspect)

The agent should not advance from these terminal states.

## Common Pitfalls

- **Editing STATE.md mid-turn**: don't. Update only at turn end.
- **Skipping checkpoints**: don't. Each turn must produce a checkpoint or the resume protocol can't function.
- **Running bootstrap gates mid-phase**: don't, unless the phase plan authorizes it for that specific slice.
- **Spawning more than 2 reviewers per gate event**: forbidden per GUARDRAILS.md.
- **Acting on a reviewer FAIL by silently expanding scope**: forbidden. Surface-change requests go through `Plan` reviewer per REVIEWERS.md.
- **Doing two slices in one turn**: forbidden. The one-slice-per-turn bound is what makes recovery work.
- **Skipping the `[GOAL-EVAL]` line**: forbidden. Without it, the `/goal` evaluator may misjudge state.
- **Skipping the slice spec re-read**: the spec is what defines the safe write set. Always re-read.
