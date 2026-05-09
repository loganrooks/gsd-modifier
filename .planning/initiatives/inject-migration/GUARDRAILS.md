# Inject Migration Guardrails

These rules apply on every iteration without exception. They override anything else if a conflict appears (including operator preference unless the operator explicitly overrides a specific rule with reasoning).

## Hard Stops — Halt Iteration Immediately, Surface To Operator

A hard stop means: do not commit, write a `paused-for-approval` checkpoint, set `STATE.md → Status` to `paused-for-approval`, exit the iteration. Wait for operator input.

1. **Verification gate fails twice on the same slice in the same iteration**
2. **Worktree contains uncommitted, untracked, or staged files outside the slice's declared write set** — do not auto-clean; investigate
3. **Manifest schema validation fails** under `validate-manifest --strict --source-only` after a slice's edits
4. **An ambiguity in the slice spec requires interpretation** that could plausibly be resolved more than one way
5. **Surface change is required outside the slice's declared write set** to make verification pass — never expand the write set silently
6. **The slice's commit body cannot be filled out honestly** under AGENTS.md §123 (e.g., the `Why:` is unclear because the slice's purpose has shifted)
7. **A subagent returns evidence that contradicts the phase plan's premise** — pause; do not proceed on a falsified premise
8. **The orientation artifact's premise check or the intervention-strategies analysis would change** if the new evidence were applied — surface to operator before continuing
9. **The operator interrupts the loop** with any signal (text, question, or stop)
10. **A previously-passing test now fails in a region unrelated to the slice** — likely a regression introduced earlier; stop and investigate
11. **The 3-consecutive-failure rule fires** (STATE.md shows the same slice failed 3 separate iterations)

## Soft Stops — Note And Continue If Possible

A soft stop means: log the issue to STATE.md `Blockers` or to the checkpoint, continue if the slice can still complete cleanly, surface in the next operator-visible report.

1. **Network timeout or transient error** during a tool call — retry once; if still failing, escalate to hard stop
2. **A cross-reference link in a doc points at a moved file** — note in checkpoint; do not auto-fix unless the slice spec authorizes it
3. **A non-essential CI gate produces a warning** — note; continue; raise to phase-boundary review
4. **Subagent timeout** — retry the subagent once with the same prompt; if still failing, hard-stop

## Forbidden Actions — Never, Under Any Circumstance

These are forbidden regardless of operator request unless the operator explicitly overrides each one in writing in the same iteration's prompt.

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

## Required Discipline

Every iteration must satisfy these or the iteration's commit is invalid (revert and retry):

1. **Single commit per slice** — exactly one. Multiple slices in one commit is forbidden.
2. **Conventional commit subject** — `<type>(<scope>): <imperative>`, no trailing period, ≤72 chars
3. **Body has Why/Verification/Boundary sections** per AGENTS.md §123
4. **`Initiative: inject-migration phase <NN> slice <MM>` trailer** is present
5. **Files staged exactly match the slice's declared write set** — no surprises
6. **`git diff --check` is clean** before commit
7. **`audit_refmap.py verify .` is clean** (exit 0) before commit
8. **STATE.md updated AFTER commit, in a SEPARATE commit** if STATE.md edit is non-trivial; in the SAME commit only if the slice spec explicitly says so

## Approval-Required Actions (Stop, Surface To Operator)

These actions require explicit operator approval at the time. The phase plan may pre-authorize them; if so, that's noted in the slice spec.

1. **Modifying any file under `harness_modifier/contract/`** — contract surface; high-risk
2. **Modifying any file under `tooling/codex/audit_refmap.py`** — verification carrier
3. **Modifying `OVERLAY-MANIFEST.json`** with a `parity_tier` or `mode` change for a carrier whose disposition is not pre-spec'd in the phase plan
4. **Adding or removing entries to `OVERLAY-MANIFEST.json`** without phase-plan authorization
5. **Modifying any `agents/*.toml` or `agents/*.md` file** — agent prompts; behavior-affecting
6. **Modifying any `commands/gsd/*.md` overlay** — modifier-owned but operator-visible
7. **Editing `AGENTS.md`, `CLAUDE.md`, `WORKFLOW.md`** — governance carriers
8. **Editing `docs/handoff/current.md`** — live-state carrier (only allowed in initiative phases that specifically address handoff state)
9. **Running `bash scripts/ci/check-bootstrap.sh`** — state-mutating; only at phase boundaries when the phase plan authorizes
10. **Running `bash scripts/ci/check-deterministic.sh`** — generally safer; still log the run
11. **Running the host matrix** (`harness_modifier/closure/host_exercise_matrix.py`) — state-mutating; phase-boundary only

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
4. **DO NOT force-push** — origin is unaware of the unpublished commit; reset is local-only
5. If the commit was already pushed (rare in this initiative), STOP — operator decides whether to revert or roll forward

When the agent detects an inconsistency between STATE.md and `git log`:

1. Log the inconsistency in the next iteration's checkpoint
2. Treat `git log` as ground truth
3. Update STATE.md to match `git log`'s actual state
4. Do not assume the inconsistency is benign; surface it to the operator on next visible report

## Worktree Hygiene

Before every iteration:

- `git status --short` should show:
  - Either an empty list (all changes from prior iterations committed)
  - Or only items pre-declared in `STATE.md → Dirty-Worktree Pre-Conditions`
- `git rev-parse HEAD` must equal `STATE.md → Last commit`
- The active branch must be `main` (or whatever `STATE.md` declares)

If any of these fails, hard-stop and ask.

## Cross-Runtime Coherence

The migration model has implications for how Codex and Claude experience each carrier. The agent must maintain:

1. **Both runtimes verify under bootstrap gate** for any carrier that's `parity_tier: core_required`
2. **Carrier output content matches expected for each runtime** — `core_required` means same effective outcome
3. **Modifier-owned net-new** stays modifier-owned; do not let upstream conventions push the modifier carriers into shared paths inadvertently

The bootstrap gate is the empirical check. If it surfaces a divergence after a slice, that's a hard stop.

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

## Operator-Override Mechanism

If the operator wants to override a guardrail for one iteration, they must say so explicitly with the rule number, e.g., "Override guardrail F.7 for this slice: I authorize amending the previous commit to fix the typo in its Why line."

The agent records the override in the checkpoint's `Observations` section. The override applies only to that iteration. It does not modify this file.

## Self-Diagnosis (read-only)

If the agent suspects this guardrails file or any other initiative file has been corrupted (malformed, contradictory, partial):

1. Do not attempt to repair
2. Hard-stop
3. Surface to operator with diagnosis details

The agent does not edit `GUARDRAILS.md`, `PROTOCOL.md`, `INITIATIVE.md`, or phase plans during normal iteration. These are operator-edited only. The only files the loop writes are `STATE.md`, `checkpoints/*`, and the slice's declared write set.
