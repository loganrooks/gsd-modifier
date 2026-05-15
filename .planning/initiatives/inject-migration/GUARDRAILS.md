# Inject Migration Guardrails

Rules that apply on every iteration without exception. They override anything else if a conflict appears.

This initiative is **reviewer-mediated**, not operator-gated, between hard stops. The operator is involved only at:

1. Initial `/goal` invocation
2. Manual interrupt (`/goal clear` or Ctrl+C)
3. Hard-stop conditions (5 only, listed below)
4. Final retrospective review

Reviewer agents handle every other checkpoint. See [REVIEWERS.md](REVIEWERS.md).

## Hard Stops (5) — Halt And Surface To Operator

A hard stop means: do not commit, do not continue, emit `HARD-STOP: <reason>` in the turn's output, write a `paused-for-operator` checkpoint, set `STATE.md → Status: paused-for-operator`, end the turn. The `/goal` evaluator detects the HARD-STOP line and terminates the goal.

1. **Manifest schema validation fails** under `validate-manifest --strict --source-only` after a slice's edits, AND a `gsd-debugger` reviewer cannot identify a fix within the slice's declared write set
2. **Commit body cannot be filled out honestly** under AGENTS.md §123 — the `Why:` is unclear because the slice's purpose has shifted away from the phase plan's intent
3. **Premise change detected** — an `adversarial-auditor-xhigh` reviewer running the premise-change template returns `HALT`, meaning the orientation or intervention-strategies premise has been falsified
4. **3-consecutive-failure rule** fires — STATE.md shows the same slice failed verification 3 separate times across 3 separate turns
5. **Self-detected initiative-file corruption** — INITIATIVE.md, GUARDRAILS.md, PROTOCOL.md, REVIEWERS.md, or any active phase plan is malformed (unparseable markdown, contradictory directives, missing required sections)

Other former hard-stop conditions are now reviewer-mediated (see "Reviewer-Mediated Continuation" below).

## Soft Stops — Log And Continue

A soft stop means: log to STATE.md `Blockers` or the checkpoint, continue if the slice can still complete cleanly, surface in the next operator-visible report.

1. **Network timeout or transient tool error** during a non-gate tool call — retry once; if still failing, treat as a gate failure and invoke `gsd-debugger`
2. **A cross-reference link in a doc points at a moved file** — note in checkpoint; do not auto-fix unless the slice spec authorizes it
3. **A non-essential CI gate produces a warning** (not a failure) — note; continue; surface at phase boundary
4. **Reviewer agent timeout** — retry the reviewer once with the same prompt; if still timing out, hard-stop with `HARD-STOP: reviewer-tool-failure`

## Forbidden Actions — Never, Under Any Circumstance

These are agent constraints. They cannot be reviewer-overridden. The only override mechanism is operator instruction in writing in the same turn (see "Operator Override" below).

1. **Force-pushing to any branch** — `git push --force` / `--force-with-lease`
2. **Resetting `main` to a non-descendant commit** — `git reset --hard <ref>` where `<ref>` is not an ancestor of HEAD
3. **Skipping git hooks** — `--no-verify`, `--no-gpg-sign`
4. **Amending a published commit** — `git commit --amend` after the commit has been pushed
5. **Bypassing verification gates** — running `git commit` without first running the slice's gates and confirming pass
6. **Running `setup-portable-gsd-runtime.sh` mid-slice** without phase-plan authorization (state-mutating; pollutes worktree)
7. **Modifying historical initiative-related commits** via rebase
8. **Storing secrets in any committed file** (`.env`, credentials, API keys, signed tokens)
9. **Auto-creating new top-level repo directories** (e.g., `tools/`, `vendor/`) — only directories listed in this initiative's phase plans may be created
10. **Editing `gsd-build/get-shit-done` upstream clone or its working tree** from this loop — read-only access only
11. **Disabling, removing, or weakening any guardrail in this file** without operator approval
12. **Deleting or reordering existing checkpoints** in `checkpoints/`
13. **Publishing modifier changes to any external system** (npm, PyPI, GitHub Releases) — this initiative is repo-local until explicit operator authorization
14. **Spawning more than 2 reviewers per gate event** — triangulation pairs only; beyond 2 = hard-stop with `HARD-STOP: reviewer-deadlock`
15. **Acting on a reviewer's recommendation outside the slice's declared write set** — surface-change requests go through `Plan` reviewer first (see REVIEWERS.md)

## Required Discipline

Every iteration must satisfy these or the iteration's commit is invalid (revert and retry):

1. **Single commit per slice** — exactly one. Multiple slices in one commit is forbidden.
2. **Conventional commit subject** — `<type>(<scope>): <imperative>`, no trailing period, ≤72 chars
3. **Body has Why/Verification/Boundary sections** per AGENTS.md §123
4. **`Initiative: inject-migration phase <NN> slice <MM>` trailer** is present
5. **`Reviewer:` trailer** is present when a reviewer's verdict influenced the commit (e.g., `Reviewer: adversarial-auditor-xhigh PASS @ phase-boundary-04`)
6. **Files staged exactly match the slice's declared write set** — no surprises
7. **`git diff --check` is clean** before commit
8. **`audit_refmap.py verify .` is clean** (exit 0) before commit
9. **STATE.md updated AFTER commit, in a SEPARATE commit** if STATE.md edit is non-trivial; in the SAME commit only if the slice spec explicitly says so
10. **`[GOAL-EVAL]` line printed at end of each turn** — see PROTOCOL.md "Turn-End Discipline"

## Reviewer-Mediated Continuation (replaces former Approval-Required Actions)

These actions formerly required operator approval. They now route through reviewer agents per REVIEWERS.md.

| Action | Reviewer | Triangulation if ESCALATE |
|---|---|---|
| Modify any file under `harness_modifier/contract/` | `adversarial-auditor-xhigh` (contract review) | second auditor with steel-man prompt |
| Modify `tooling/codex/audit_refmap.py` | `adversarial-auditor-xhigh` | second auditor |
| Modify `OVERLAY-MANIFEST.json` with parity_tier or mode change not pre-spec'd | `adversarial-auditor-xhigh` | `Explore` for manifest grammar check |
| Add or remove `OVERLAY-MANIFEST.json` entries not pre-authorized in phase plan | `adversarial-auditor-xhigh` | `Explore` |
| Modify any `agents/*.toml` or `agents/*.md` file | `adversarial-auditor-xhigh` | second auditor |
| Modify any `commands/gsd/*.md` overlay | `adversarial-auditor-xhigh` | second auditor |
| Edit `AGENTS.md`, `CLAUDE.md`, `WORKFLOW.md` outside a governance-slice | `adversarial-auditor-xhigh` | second auditor |
| Edit `docs/handoff/current.md` outside a handoff-state slice | `adversarial-auditor-xhigh` | second auditor |
| Run `bash scripts/ci/check-bootstrap.sh` mid-phase | `Plan` (scope review) | `adversarial-auditor-xhigh` |
| Run host matrix (`harness_modifier/closure/host_exercise_matrix.py`) outside phase boundary | `Plan` | `adversarial-auditor-xhigh` |
| Expand a slice's declared write set | `Plan` (surface-change review) | `adversarial-auditor-xhigh` |
| Skip a phase declared as deferrable (Phase 7) | `adversarial-auditor-xhigh` (cost-benefit review) | second auditor |

If a reviewer returns FAIL or the triangulation deadlocks, the action does not proceed — the main agent either re-attempts within original scope or hard-stops.

## Auto-Recovery Patterns (replaces former Verification-Fail Halt)

These are recovery paths the main agent takes BEFORE escalating to hard-stop. They preserve autonomy for transient or fixable failures.

### Verification gate fails

1. Retry once (gates can flake on filesystem / network)
2. If still failing: spawn `gsd-debugger` per REVIEWERS.md
3. If debugger returns PASS with a fix in the slice's write set: apply the fix, re-run the gate
4. If debugger returns FAIL (fix needs scope expansion): spawn `Plan` reviewer; if Plan PASS: expand scope and apply; if Plan FAIL: hard-stop
5. If debugger returns ESCALATE: triangulate per REVIEWERS.md table
6. If debugger returns HALT: hard-stop with the debugger's stated reason

### Worktree drift detected before slice execution

1. `git status --short` shows files outside `STATE.md → Dirty-Worktree Pre-Conditions`
2. Spawn `Explore` to identify the source of the drift (recent commit? unfinished prior slice?)
3. If Explore identifies a recoverable cause (e.g., prior iteration's STATE.md edit not committed): `git restore` the unstaged drift, reconcile STATE.md
4. If Explore cannot identify: hard-stop with `HARD-STOP: unknown-worktree-drift`

### Slice ambiguity prevents safe execution

1. Spawn `Plan` reviewer with the ambiguity context (see REVIEWERS.md template)
2. If Plan returns a single recommended interpretation with PASS: execute that interpretation; log the decision in the checkpoint
3. If Plan returns FAIL (slice spec is broken): hard-stop
4. If Plan returns ESCALATE: triangulate with `adversarial-auditor-xhigh`

### Subagent returns evidence contradicting the slice's premise

1. Spawn `Explore` to verify the subagent's cited evidence
2. If Explore PASS (no real contradiction): continue with original plan
3. If Explore FAIL (subagent was wrong): re-run subagent with corrected input
4. If Explore ESCALATE or evidence genuinely contradicts: invoke premise-change template via `adversarial-auditor-xhigh`; if HALT, hard-stop

### Previously-passing test fails in region unrelated to the slice

1. Spawn `gsd-debugger` per REVIEWERS.md
2. Per debugger verdict: apply fix in-scope, expand scope via `Plan`, or hard-stop

### Same slice has failed 2 times in this and prior iterations

1. Treat next failure as automatic hard-stop (3-consecutive-failure rule)
2. Surface to operator with the failure log

## Rollback Procedures

When a slice fails after edits but before commit:

1. `git status` to confirm nothing is staged or has been committed
2. `git restore <files-touched>` for unstaged changes
3. `git restore --staged <files-touched>` for staged changes
4. `git status` to confirm clean
5. Update STATE.md with `Blockers` entry; do not advance slice counter

When a slice fails after commit (rare; gates should run before commit):

1. `git reset --hard HEAD~1` — revert the commit (only if the commit is the most recent one, no later commits depend on it)
2. Verify worktree clean
3. Update STATE.md with `Blockers` entry; do not advance slice counter
4. **Do not force-push** — origin is unaware of the unpublished commit; reset is local-only
5. If the commit was already pushed (rare), hard-stop with `HARD-STOP: published-commit-revert-needed`

When the agent detects an inconsistency between STATE.md and `git log`:

1. Log the inconsistency in the next iteration's checkpoint
2. Treat `git log` as ground truth
3. Update STATE.md to match `git log`'s actual state
4. Continue if the inconsistency is small (e.g., a counter off by one). Hard-stop if structural (sentinel disagrees, phase progress disagrees with file existence).

## Worktree Hygiene

Before every iteration:

- `git status --short` should show:
  - Either an empty list (all changes from prior iterations committed)
  - Or only items pre-declared in `STATE.md → Dirty-Worktree Pre-Conditions`
- `git rev-parse HEAD` must equal `STATE.md → Last commit`
- The active branch must be `main` (or whatever `STATE.md` declares)

If any of these fails, follow the "Worktree drift detected" auto-recovery pattern.

## Cross-Runtime Coherence

The migration model has implications for how Codex and Claude experience each carrier. The agent must maintain:

1. **Both runtimes verify under bootstrap gate** for any carrier that's `parity_tier: core_required`
2. **Carrier output content matches expected for each runtime** — `core_required` means same effective outcome
3. **Modifier-owned net-new** stays modifier-owned; do not let upstream conventions push the modifier carriers into shared paths inadvertently

The bootstrap gate is the empirical check. If it surfaces a divergence after a slice, that's a `gsd-debugger` invocation (recoverable) or a hard-stop (irrecoverable).

## Sub-Initiative Isolation

This loop is for the inject migration only. Concerns surfaced during iteration that do not belong to this initiative must be:

1. Logged in `STATE.md → Notes For The Agent` (or a new `Out-Of-Scope Surfaces` section if many accumulate)
2. NOT acted on inside the loop
3. Surfaced to the operator at phase-boundary report or end-of-initiative retrospective

Examples of out-of-scope concerns:

- A bug in a non-overlay file you happened to read
- An opportunity to refactor unrelated tooling
- A drift item not on the inject-migration phase catalog
- A spec ambiguity in unrelated planning artifacts

## Operator Override Mechanism

If the operator wants to override a guardrail for one turn, they must say so explicitly with the rule number in the `/goal` invocation or in a follow-up message. Example: "Override Forbidden #7 for this turn: I authorize amending the previous commit to fix the typo in its Why line."

The agent records the override in the checkpoint's `Observations` section. The override applies only to that turn. It does not modify this file.

## Self-Diagnosis (read-only)

If the agent suspects this guardrails file or any other initiative file has been corrupted (malformed, contradictory, partial):

1. Do not attempt to repair
2. Hard-stop with `HARD-STOP: initiative-file-corruption` and cite the file + suspected issue
3. End the turn

The agent does not edit `GUARDRAILS.md`, `PROTOCOL.md`, `INITIATIVE.md`, `REVIEWERS.md`, or phase plans during normal iteration. These are operator-edited only. The only files the loop writes are `STATE.md`, `checkpoints/*`, and the slice's declared write set.
