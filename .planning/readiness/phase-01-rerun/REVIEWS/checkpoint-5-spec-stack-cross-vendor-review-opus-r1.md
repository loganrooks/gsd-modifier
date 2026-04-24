# Checkpoint 5 Spec Stack Cross-Vendor Review — Opus R1

**Reviewer:** Claude Opus 4.6 (cross-vendor)  
**Date:** 2026-04-15  
**Scope:** Pre-implementation audit of the widened Checkpoint 5 candidate spec stack  
**Governing prompt:** [checkpoint-5-spec-stack-cross-vendor-review-prompt.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-spec-stack-cross-vendor-review-prompt.md)

---

## Verdict

**The candidate spec stack is not yet strong enough to guide implementation.**

The implementation spec correctly identifies the four workflow seams that Checkpoint 4 proved belong on the pre-rerun path. The claim typing is rigorous, the provenance trail to Checkpoint 4 findings is solid, and the scope/deferral boundaries are honest.

However, the spec has several propagation gaps — three of which are blocking — that would cause it to fail later stringent audit. The most critical is that the spec proposes edits to four gitignored runtime workflow files without any materialization plan for making those edits tracked, auditable, or reinstallable. This contradicts the repo's own governance principles and the precedent set by Track A/B in the pre-reactivation implementation.

Fix the three blocking findings below. The remaining findings are real but can be addressed during implementation rather than requiring spec revision.

---

## Findings

### F-1 [BLOCKING]: No materialization plan for workflow edits into tracked overlay truth

**Severity:** Blocking  
**Surfaces:** [checkpoint-5-workflow-follow-through-implementation-spec.md:23-41](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md:23), [checkpoint-5-bounded-follow-through-implementation-note.md:30-31](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-bounded-follow-through-implementation-note.md:30)

The implementation spec proposes editing four workflow files:
- `.codex/get-shit-done/workflows/discuss-phase.md`
- `.codex/get-shit-done/workflows/research-phase.md`
- `.codex/get-shit-done/workflows/plan-phase.md`
- `.codex/get-shit-done/workflows/execute-phase.md`

These files live under `.codex/`, which is gitignored ([.gitignore](/home/rookslog/workspace/projects/prix-guesser/.gitignore:1)). The portable setup path installs from tracked overlay truth under `tooling/portable-gsd/overlay/` ([scripts/setup-portable-gsd.sh](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh)).

The pre-reactivation implementation already identified and solved this exact problem for Track A (agent `.toml` files) and Track B (`review.md`, `planner-reviews.md`) by materializing changes into overlay files with `__PROJECT_ROOT__` placeholders ([checkpoint-5-bounded-follow-through-implementation-note.md:30-31](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-bounded-follow-through-implementation-note.md:30)). Current tracked overlay evidence under `tooling/portable-gsd/overlay/` confirms that pattern is already established.

The widened spec does not mention materialization at all. Without it:
1. The edits are not version-controlled and cannot be committed
2. The edits are not auditable by later review
3. The edits will not survive a `setup-portable-gsd.sh` reinstall
4. The checkpoint produces changes that contradict the repo's own tracking discipline

This is not a deferred hardening item. It is a precondition for any workflow edit to be a meaningful checkpoint output. The spec must explicitly state whether the implementation will:
- Create overlay copies of all four workflow files (significant surface expansion but consistent with established Track A/B pattern)
- Create partial overlay patches (smaller but breaks the whole-file overlay pattern)
- Or address this via a different mechanism

**Required fix:** Add an explicit materialization section to the implementation spec that follows the Track A/B precedent, or document a justified alternative.

### F-2 [BLOCKING]: Research adequacy change does not propagate to the researcher agent prompt

**Severity:** Blocking  
**Surfaces:** [checkpoint-5-workflow-follow-through-implementation-spec.md:25-27](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md:25), [gsd-phase-researcher.toml:656-706](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/agents/gsd-phase-researcher.toml:656)

Change 1 in the spec patches `research-phase.md` so the completion contract requires explicit disposition of material open questions — resolved, preserved, escalated, or inconclusive with named consequence.

But the researcher agent prompt (`gsd-phase-researcher.toml`) is the surface that actually produces `RESEARCH.md`. Its structured returns section (lines 660-706) defines `RESEARCH COMPLETE`, `CHECKPOINT REACHED`, and `RESEARCH BLOCKED` return formats. None of these currently include an explicit disposition accounting for material open questions.

The orchestrator workflow (`research-phase.md`) spawns the researcher and handles its return. If the workflow adds a new completion contract, but the agent prompt doesn't know to produce the new required output, the agent will continue returning the old format. The orchestrator could reject incomplete returns, but that is a brittle enforcement mechanism that depends on the orchestrator parsing for a section that the agent was never told to produce.

The researcher `.toml` overlay already exists from Track A and would be the natural place for this change.

**Required fix:** The spec must explicitly address whether `gsd-phase-researcher.toml` needs an updated structured return format to produce the new disposition accounting, or document why the orchestrator-only change is sufficient.

### F-3 [BLOCKING]: Stale researcher guidance in plan-phase.md contradicts existing Track A overlay

**Severity:** Blocking  
**Surfaces:** [plan-phase.md:393-394](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/plan-phase.md:393), [gsd-phase-researcher.toml:38](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/agents/gsd-phase-researcher.toml:38)

The implementation spec correctly identifies that `plan-phase.md:393` still carries stale guidance pointing research at `.claude/skills/` or `.agents/skills/`. The spec marks this for correction under change 2.

However, this creates a dual-surface contradiction with the already-materialized Track A overlay. The researcher `.toml` (overlay line 38) now explicitly says: "Do NOT treat `.claude/skills/`, `.agents/skills/`, `./CLAUDE.md`, or home-level Reflect directories as governing truth for this repo." Meanwhile, the `plan-phase.md` orchestrator spawn prompt at line 393-394 tells the same researcher: "Check .claude/skills/ or .agents/skills/ directory (if either exists)."

This is not merely a future fix. It is an active contradiction between an already-landed Track A change and the runtime orchestrator. When the plan-phase orchestrator spawns a researcher, the researcher receives both instructions — its own `.toml` prompt (saying "don't look there") and the orchestrator's spawn prompt (saying "look there"). The `.toml` should take precedence, but the contradiction is a governance defect that exists right now.

The spec correctly identifies this fix but classifies it as one item within change 2. Given that it creates a live contradiction with already-committed work, it should be recognized as a blocking cleanup rather than merely a part of a broader improvement.

**Required fix:** Acknowledge this as a live contradiction that must be fixed regardless of whether the broader change 2 closure-pressure improvements land. It is already a regression from the Track A commit.

### F-4 [SIGNIFICANT]: Debt-carrying completion change does not propagate to the verifier

**Severity:** Significant (not blocking, but would fail later audit)  
**Surfaces:** [checkpoint-5-workflow-follow-through-implementation-spec.md:35-37](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md:35), [gsd-verifier.toml:40-50](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/agents/gsd-verifier.toml:40)

Change 3 patches `execute-phase.md` so human-approval continuation and advisory review outcomes are labeled as debt-carrying completion states rather than reading like ordinary closure.

If the executor starts marking completion states as debt-carrying, the verifier should know to check for that marker. Currently the verifier (`gsd-verifier.toml`) checks must-haves, artifacts, key links, anti-patterns, and behavioral spot-checks. It has no concept of "debt-carrying completion" as a verification dimension.

Without verifier-side awareness, the executor can honestly mark a phase as debt-carrying — but the verifier's `passed` verdict will then re-legitimize it as clean completion because the verifier has no debt-carrying dimension to check. The debt becomes invisible again at verification.

**Recommended fix:** The spec should note that the verifier `.toml` overlay may need a narrow update to check for debt-carrying markers when they exist in executor output. This can be addressed during implementation rather than requiring a spec revision, but it should be named as an expected propagation consequence.

### F-5 [SIGNIFICANT]: Context.md template not addressed for disposition-expectation reinforcement

**Severity:** Significant  
**Surfaces:** [checkpoint-5-workflow-follow-through-implementation-spec.md:39-41](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md:39), [templates/context.md:68-80](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/templates/context.md:68)

Change 4 patches `discuss-phase.md` so doctrine-sensitive reruns treat auto/default throughput as explicit convenience rather than as the ambient excellence lane, and reinforces downstream disposition expectations for open questions.

The `context.md` template is the structural contract for `CONTEXT.md` output. It defines the sections downstream agents consume. Currently the template includes `<open_questions>` and `<future_awareness>` sections, but these do not carry any disposition-expectation language. The template's guidelines (line 386-419) do not mention that open questions should include downstream disposition expectations.

If the discuss-phase workflow is strengthened but the template that structures its output is not, the reinforcement depends entirely on the discuss-phase workflow including the right prose at generation time. That is fragile. The template should carry the expectation structurally.

**Recommended fix:** During implementation, add brief downstream-disposition guidance to the `<open_questions>` section of the context.md template. This can be handled during implementation without a spec revision.

### F-6 [MODERATE]: Summary.md template not addressed for completion-status metadata

**Severity:** Moderate  
**Surfaces:** [gsd-executor.toml:362-412](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/agents/gsd-executor.toml:362), [WORKFLOW.md:94](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:94)

If execute-phase starts distinguishing clean from debt-carrying completion, the SUMMARY.md artifact should carry that distinction. Currently the executor's summary creation section includes `Self-Check`, `Deviations`, `Auth Gates`, `Stubs`, and `Threat Flags` sections, but no explicit completion-status metadata field.

The state updates section (`gsd-executor.toml:436-484`) updates STATE.md via `state advance-plan` and `state record-metric`, but neither of these tools currently distinguishes clean from debt-carrying completion.

**Recommended fix:** During implementation, add a completion-status field to the summary template and/or state update logic. This is downstream of change 3 and can be handled in the same implementation pass.

### F-7 [MODERATE]: Shared references may need tandem updates

**Severity:** Moderate  
**Surfaces:** `.codex/get-shit-done/references/gates.md`, `.codex/get-shit-done/references/revision-loop.md`, `.codex/get-shit-done/references/agent-contracts.md`

The spec targets the four workflow files and names wrapper alignment as secondary scope. But several shared reference files are consumed by multiple workflows:

- `references/gates.md` — consumed by plan-checker and verifier; if closure pressure semantics change, gate patterns may need alignment
- `references/revision-loop.md` — consumed by plan-phase; if `Proceed anyway` is demoted, the revision loop reference may need awareness
- `references/agent-contracts.md` — consumed by execute-phase and plan-phase; if the research completion contract changes, the agent contract reference may need updating

These are not blocking, but the spec should acknowledge them as likely tandem update surfaces during implementation rather than discovering them mid-edit.

### F-8 [INFO]: Overlay surface expansion implications

**Severity:** Info  
**Surfaces:** [scripts/setup-portable-gsd.sh](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh), `tooling/portable-gsd/overlay/`

If F-1 is resolved by creating overlay copies of all four workflow files, this is a significant expansion of the tracked overlay surface. Currently `tooling/portable-gsd/overlay/` contains:
- 5 agent `.toml` files (Track A)
- 2 workflow/reference files (Track B)

Adding 4 full workflow files (each several hundred lines) would more than double the overlay surface. This may trigger the conditional task R5.7 (Portable GSD reproducibility/provenance hardening) from the readiness TASKS.md, since the overlay materialization is now becoming the primary auditability mechanism for a growing number of GSD surfaces.

The spec should note this implication even if it does not widen to include R5.7.

---

## What Is Already Strong

1. **Claim typing and provenance trail.** The implementation spec's `[d:c+r:i]` markers with concrete file-line citations back to Checkpoint 4 findings are exemplary. Every requested change traces to accepted audit output. This is the strongest aspect of the candidate stack.

2. **Scope and deferral boundaries.** The explicit non-goals section honestly names what the spec does not reopen (broad install pinning, archival provenance, branch/worktree redesign, exhaustive skill audit). The deferral language is specific enough to distinguish genuine later work from scope avoidance.

3. **The five-change decomposition.** The mapping of Checkpoint 4 workflow-chain findings into five concrete implementation changes is well-structured. Each change has a named defect, a named target surface, and a stated intent. The ordering (research adequacy → plan traceability → completion semantics → discuss-phase → wrappers) is the right dependency order.

4. **Track A/B pre-reactivation work.** The `.toml` alignment, review-surface hardening, and launch-truth helper from the pre-reactivation tracks are solid. The materialization of those changes into tracked overlay truth was the right move and established a pattern that the widened scope should follow.

5. **Reactivation governance.** The correction trail from the initially too-narrow Checkpoint 5 scope to the reactivated scope is well-documented. The reactivated launch spec honestly names why the initial scope was insufficient and correctly identifies the checkpoint audit provenance for each added obligation.

6. **Review-surface improvements.** The review.md and planner-reviews.md overlay changes (Track B) — asking for strongest justified criticism, merely adequate areas, later audit failures, and preserving lone high-signal concerns — are genuine improvements to the review harness that will serve the rerun.

---

## What Must Change Before Implementation

1. **F-1: Add an explicit materialization section** to the implementation spec explaining how the four workflow file edits will be tracked as overlay truth. Follow the Track A/B precedent. Without this, the implementation cannot produce auditable, committable results.

2. **F-2: Address researcher `.toml` propagation** for the new research adequacy/disposition contract. State whether the researcher agent prompt needs to be updated to produce the new disposition output, or explain why the orchestrator-only change is sufficient.

3. **F-3: Acknowledge and prioritize the stale-guidance fix** in `plan-phase.md:393-394` as a live contradiction with the already-committed Track A overlay, not merely one bullet in a broader improvement set.

---

## What Can Remain Deferred

1. **F-4 (verifier propagation)** — can be addressed during implementation; the spec should name it as an expected consequence but does not need to block on it.

2. **F-5 (context.md template)** — can be addressed during implementation as a natural companion to the discuss-phase change.

3. **F-6 (summary.md template / state updates)** — can be addressed during implementation alongside change 3.

4. **F-7 (shared references)** — can be addressed during implementation; the spec should acknowledge them as likely tandem surfaces.

5. **F-8 (overlay expansion implications)** — informational; the spec should note the implication for conditional task R5.7.

6. **Broader provenance hardening, install pinning, branch/worktree redesign** — correctly deferred and not active dependencies of this candidate stack.

---

## Propagation Consequences

If the spec's five changes are implemented, the following propagation chains must be respected:

| Change | Primary target | Must also touch | May also touch |
|--------|---------------|-----------------|----------------|
| 1. Research adequacy | research-phase.md | gsd-phase-researcher.toml (structured returns) | references/agent-contracts.md |
| 2. Plan traceability / closure | plan-phase.md | (stale guidance fix is self-contained) | references/revision-loop.md, references/gates.md |
| 3. Debt-carrying completion | execute-phase.md | gsd-verifier.toml (debt dimension) | summary.md template, state update logic |
| 4. Discuss auto/default | discuss-phase.md | context.md template (disposition expectations) | — |
| 5. Wrapper alignment | SKILL.md wrappers | — | — |
| ALL | overlay materialization | tooling/portable-gsd/overlay/ | setup-portable-gsd.sh |

The overlay materialization row is the cross-cutting propagation requirement: every workflow edit must land in tracked overlay truth, not only in gitignored runtime space.

---

## Change Summary

| Item | Action Required | Before Implementation? |
|------|----------------|----------------------|
| Materialization plan for workflow edits | Add to spec | Yes — blocking |
| Researcher .toml propagation | Add to spec | Yes — blocking |
| Stale guidance contradiction | Acknowledge priority in spec | Yes — blocking |
| Verifier debt-carrying dimension | Name as expected consequence | No — during implementation |
| Context.md template update | Name as expected consequence | No — during implementation |
| Summary template / state updates | Name as expected consequence | No — during implementation |
| Shared references awareness | Name as likely tandem surfaces | No — during implementation |
| Overlay expansion implications | Note for R5.7 monitoring | No — informational |
