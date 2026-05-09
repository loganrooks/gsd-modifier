# Inject Migration Loop Protocol

This document defines exactly how an agent advances the inject migration by one bounded slice per iteration, persists state between iterations, and resumes correctly after a context clear.

## Read Order (every iteration, in this order)

1. `STATE.md` — where we are
2. `GUARDRAILS.md` — what's safe
3. The active phase plan: `phases/<NN>-<slug>.md` (where `<NN>` is `STATE.md → Current Status → Phase`)
4. `INITIATIVE.md` — only if the phase plan references it (mostly for cross-phase context)

You do **not** need to read other phase files unless the active phase plan references them or you are escalating a cross-phase concern.

## Cold Start (first iteration after context clear or new session)

1. **Verify the repo location**: working directory is `/home/rookslog/workspace/projects/gsd-modifier`. If not, fail and ask the operator.
2. **Verify branch**: `git rev-parse --abbrev-ref HEAD` should return `main` unless `STATE.md → Current Status` says otherwise. If not on `main`, stop and ask.
3. **Read the four files** in the order above.
4. **Reconcile STATE.md against `git log`**: `git rev-parse HEAD` must equal `STATE.md → Last commit`. If they diverge, treat `git log` as ground truth and update STATE.md before proceeding.
5. **Verify clean worktree**: `git status --short` should show only items listed in `STATE.md → Dirty-Worktree Pre-Conditions`. Any other untracked or modified files mean the previous iteration was interrupted; investigate before continuing.
6. **Check the sentinel**: if `STATE.md → Sentinel` is `INITIATIVE-COMPLETE` or `ABORTED`, exit immediately and report status to the operator. Do not attempt further work.
7. **Otherwise, proceed to Per-Iteration Flow** with the active phase and slice from `STATE.md`.

## Per-Iteration Flow

The flow per iteration is one bounded slice. Slices are defined in each phase plan. A slice is complete when it produces a single commit with passing verification.

```
┌─────────────────────────────────────────────────────────────┐
│ 1. Identify the next pending slice                          │
│    Read phase plan; find slice marked `[ ]` with no deps.   │
├─────────────────────────────────────────────────────────────┤
│ 2. Pre-execute checks                                       │
│    - Worktree clean                                         │
│    - Slice's preconditions (per phase plan) satisfied       │
│    - No incompatible STATE.md flags (e.g., paused-for-approval)│
├─────────────────────────────────────────────────────────────┤
│ 3. Execute slice                                            │
│    - Follow slice spec exactly                              │
│    - Stay within the slice's declared write set             │
│    - If a needed write is outside the spec → STOP, ask      │
├─────────────────────────────────────────────────────────────┤
│ 4. Run verification gates                                   │
│    - Per slice spec (specific to the slice)                 │
│    - Plus per-phase gates (per phase plan exit criteria)    │
│    - Plus baseline gates (audit_refmap; git diff --check)   │
├─────────────────────────────────────────────────────────────┤
│ 5. Decision branch:                                         │
│    - All gates green:                                       │
│      → commit; update STATE.md; write checkpoint; iter end  │
│    - Any gate red:                                          │
│      → invoke Failure Recovery (below)                      │
│    - Approval-required action surfaced:                     │
│      → set STATE.md status=paused-for-approval; stop        │
└─────────────────────────────────────────────────────────────┘
```

## Slice Execution Discipline

For each slice the agent must:

1. **Re-read the slice spec** from the phase plan before any edit
2. **Compute the proposed write set** and confirm it is fully contained in the spec's `Write Set` section
3. **Apply edits** using `Edit` / `Write` tools as appropriate
4. **Run the slice's `Verification` gates** in the order specified
5. **If gates pass, commit** with the slice's specified `Commit message`
6. **Update STATE.md** with the new `Last commit`, `Last checkpoint`, advance `Slice within phase`
7. **Write checkpoint** to `checkpoints/<UTC-timestamp>-phase<NN>-slice<MM>.md` per the checkpoint template (below)
8. **Iteration ends** — exit cleanly. Do not start the next slice in the same iteration.

The exit-after-one-slice discipline is what makes the loop resumable and bounded. Two slices in one iteration creates a context-bloat risk and complicates rollback.

## Checkpoint Template

Each iteration writes one file at `checkpoints/<UTC-timestamp>-phase<NN>-slice<MM>.md` in this format:

```markdown
# Checkpoint phase <NN> slice <MM>

Timestamp: <ISO-8601 UTC>
Phase: <NN>-<slug>
Slice: <MM>-<slug>
Outcome: <success | blocked | aborted | paused-for-approval>
Commit: <SHA or "(no commit)">

## What was done
- <bullet>

## Files touched
- <path> (added | modified | deleted)

## Verification gates run
- <gate name>: <result> (<exit code or notes>)

## Observations
- <any non-trivial notes the next iteration should know>

## Next expected slice
- <NN>-<slug> slice <MM+1> (or "phase complete; advance to phase <NN+1>")
```

## State-Update Protocol

The agent updates `STATE.md` at the end of each iteration. Update is **atomic** — either all fields update or none do. If a write fails partway, the next iteration's reconciliation step (Cold Start step 4) will detect the divergence.

Fields to update at iteration end:

- `Last updated` (timestamp)
- `Last updated by` (use the literal string `inject-migration loop agent`)
- `Current Status → Slice within phase` (advance by 1, or move to next phase if last slice complete)
- `Current Status → Status` (one of the enum values)
- `Current Status → Last checkpoint` (path to checkpoint file just written)
- `Current Status → Last commit` (`git rev-parse HEAD`)
- `Phase Progress` (mark `[x]` if a phase just completed)
- `Active Work` (next task description; or `(none — paused)` etc.)
- `Counters` (increment relevant counters)
- `Recent Checkpoints` (append new checkpoint summary line; keep last 10 entries; older entries archived to `checkpoints/`)

## When To Stop And Ask (paused-for-approval)

The agent must stop and surface to the operator (via `AskUserQuestion` or by setting status and exiting) when any of the following occur. These are NOT failures; they are deliberate human-gate points.

- The slice spec calls for a write outside its declared `Write Set`
- A governance carrier (`AGENTS.md`, `CLAUDE.md`, `WORKFLOW.md`, `STATUS.md`, `CURRENT-STATE.md`, `current.md`) is about to be edited and the slice is not specifically a governance slice
- A change to `OVERLAY-MANIFEST.json` produces a parity_tier or mode change not pre-approved in the phase plan
- A subagent returns evidence that contradicts the phase plan's premise
- A verification gate exposes a regression in a previously-passing area unrelated to the current slice
- The operator typed an explicit stop signal (e.g., interrupted the loop, asked a question)
- More than 3 consecutive iterations have failed verification on the same slice
- A new file with side-effects on shared infrastructure (e.g., new CI script, new top-level dir) is about to be created without prior phase-plan authorization

When stopping, the agent writes a `paused-for-approval` checkpoint with a `## Question for operator` section detailing what's needed.

## When To Spawn Subagents

The agent may spawn subagents for bounded research or evidence-gathering, but **never** for code changes. Code changes happen in the main loop only.

Use cases for subagents:
- Reading large upstream files to confirm a hypothesis
- Cross-referencing many overlay carriers in parallel
- Adversarial review of a slice's design before write

Subagents must be:
- Strictly read-only
- Bounded (single deliverable; clear exit criteria)
- Returned within one iteration (no inter-iteration handoff)

Spawning a subagent is a state-mutating decision that should be logged in the checkpoint.

## Failure Recovery

When a verification gate fails, the agent attempts:

1. **Re-run once** — gates can be flaky, especially anything that touches the network, runtime materialization, or filesystem locks
2. **If still failing, classify the failure**:
   - **Test regression** in code the slice did not touch → likely an upstream change exposed; stop and ask
   - **Test regression** in code the slice touched → revert the slice's changes (`git restore` for unstaged; `git reset --hard HEAD` if no commit yet); analyze; either retry the slice with corrections OR stop and ask
   - **Verification tooling itself errors** → stop and ask; do not attempt to fix verification tooling in the same slice
3. **Update STATE.md** to `blocked` with a `Blockers` entry describing the failure
4. **Write a `blocked` checkpoint** with full failure detail
5. **Exit the iteration** — do not retry the same slice without operator input

The 3-consecutive-failures rule applies across iterations: if STATE.md shows the same slice has been retried 3 times across 3 separate iterations, the next iteration must stop without retry.

## Resume After Context Clear

A context clear means the agent's working memory is gone but `STATE.md`, `git log`, and the filesystem persist. The Cold Start steps cover this case.

Specifically, after a clear:

1. Run all Cold Start steps
2. Look at the most recent checkpoint in `checkpoints/`. Its `Outcome` field tells you whether the previous iteration completed (`success`) or didn't (`blocked` / `aborted` / `paused-for-approval`).
3. If the most recent outcome was `success`, the previous iteration completed cleanly and STATE.md is authoritative. Proceed to the next slice.
4. If the most recent outcome was `paused-for-approval`, do not proceed; surface the question to the operator (via the operator's first message in the new session).
5. If the most recent outcome was `blocked`, do not retry; surface the blocker.
6. If the most recent outcome was `aborted`, the entire initiative was halted; do not proceed.

If `checkpoints/` is empty (initiative just started), Cold Start step 6 catches this via the sentinel.

## Verification Stack (per-iteration)

These are the **baseline gates** that every iteration runs in addition to slice-specific gates:

```bash
git diff --check
python3 tooling/codex/audit_refmap.py verify .
```

These do not cost much, run in seconds, and catch many integration issues. Their exit must be 0.

The **per-phase gates** are documented in each phase plan's `Exit Criteria` section. Run them at phase boundaries (after the last slice of a phase commits, before marking the phase complete).

The **initiative-level gates** are documented in `INITIATIVE.md → Completion Criteria`. Run them only when the operator asks or when reaching the closeout phase.

The **state-mutating bootstrap gates** (`bash scripts/ci/check-deterministic.sh`, `bash scripts/ci/check-bootstrap.sh`) are run only at phase boundaries when the phase plan explicitly authorizes it. Running them mid-phase risks materialization-side-effects polluting the worktree mid-slice.

## Commit Discipline

Every slice produces exactly one commit. Commit message format follows AGENTS.md "Commit Hygiene":

```
<type>(<scope>): <imperative summary>

Why: <one paragraph>

Verification: <commands run + results>

Boundary: <what's intentionally held out of this commit>

Initiative: inject-migration phase <NN> slice <MM>
```

The `Initiative:` trailer is required for all initiative slices. It enables `git log --grep "Initiative: inject-migration"` to enumerate all slice commits cleanly.

## Loop Termination

The loop terminates when `STATE.md → Sentinel` is set to `INITIATIVE-COMPLETE` (after Phase 10 closeout) or `ABORTED` (operator-decided early termination). The agent should not advance from these terminal states.

## Common Pitfalls

- **Editing STATE.md mid-iteration**: don't. Update only at iteration end.
- **Skipping checkpoints**: don't. Each iteration must produce a checkpoint or the resume protocol can't function.
- **Running bootstrap gates mid-phase**: don't, unless the phase plan authorizes it for that specific slice.
- **Spawning more than one subagent per iteration**: avoid; each subagent costs context. If you genuinely need parallel research, batch in a single subagent prompt.
- **Optimistic "I'll commit two slices together"**: don't. One slice per iteration. The bound is what makes recovery work.
- **Skipping the slice spec re-read**: the spec is what defines the safe write set. Always re-read.
