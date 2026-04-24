# Checkpoint 5 Spec Stack Gap-Exposure Cross-Vendor Review (Claude Opus R1)

Reviewer: Claude Opus 4.6 (cross-vendor)
Date: 2026-04-15
Governing spec: [checkpoint-5-spec-stack-gap-exposure-audit-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-spec-stack-gap-exposure-audit-spec.md)

## Verdict

**The candidate stack is directionally strong but under-propagated.** It correctly identifies the four primary workflow defects and proposes appropriate fixes. However, it treats the four named workflow files as if they were the complete semantic surface of each proposed change, when in fact each change creates propagation obligations on at least 2-4 additional files that the spec does not name or own.

The spec is strong enough to guide implementation of the workflow file edits themselves. It is not strong enough to guide a complete Checkpoint 5 follow-through that will survive later audit, because the propagation surfaces that would still carry stale semantics are neither owned nor explicitly deferred.

**Classification: CONDITIONAL PASS -- must address propagation ownership before implementation completes, may begin implementation of the four workflow edits now.**

---

## Blocking Gaps

### BG-1: Research completion contract lacks template propagation (Severity: blocking)

[d:c+r:i] The spec requests a research adequacy/disposition patch to `research-phase.md` (implementation-spec:25-27). The proposed change adds an explicit disposition surface for open questions before planning can consume the research output.

But `templates/research.md` (lines 1-60) is the artifact contract that defines what RESEARCH.md looks like. It currently has `<user_constraints>`, `<research_summary>`, `<standard_stack>`, etc. -- no disposition section. If the workflow changes the completion contract but the template stays unchanged, researchers will produce RESEARCH.md files in the old format because the template is what they actually follow for structure. Sources: [templates/research.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/templates/research.md:1), [research-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/research-phase.md:90).

The researcher `.toml` overlay (`gsd-phase-researcher.toml:660-686`) defines structured return markers (`## RESEARCH COMPLETE`, `## RESEARCH BLOCKED`). If the workflow now requires an explicit disposition accounting, the structured return should carry or reference that disposition so downstream consumers can parse it mechanically. Sources: [gsd-phase-researcher.toml](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/agents/gsd-phase-researcher.toml:660).

**What must happen:** `templates/research.md` and the researcher's structured return format must be named as propagation targets of the S1 change, either as active in-scope edits or as explicitly deferred with a named consequence.

### BG-2: Planner does not consume rich CONTEXT.md steering (Severity: blocking)

[d:c+r:i] The spec proposes to reinforce `discuss-phase.md` (S4, implementation-spec:41) so doctrine-sensitive reruns don't flatten open items. The discuss workflow already produces `<working_model>`, `<derived_constraints>`, `<open_questions>`, `<epistemic_guardrails>`, and `<future_awareness>` sections in CONTEXT.md. Sources: [templates/context.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/templates/context.md:47), [discuss-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/discuss-phase.md:64).

But the planner's CONTEXT.md consumption contract (`gsd-planner.toml:52-81`, `<context_fidelity>` section) only mandates explicit fidelity to three sections:
- `## Decisions` (locked -- NON-NEGOTIABLE)
- `## Deferred Ideas` (MUST NOT appear)
- `## Claude's Discretion` (planner's judgment)

The planner has no explicit obligation to account for, preserve, or disposition the richer steering sections. Even if discuss-phase stops flattening them, the planner can simply ignore them because nothing in its contract says otherwise. Sources: [gsd-planner.toml](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/agents/gsd-planner.toml:52).

The spec names a planning obligation (S2, implementation-spec:33) to "preserve material `CONTEXT.md` decisions, open questions, and protected seams in the produced plan or in an explicit defer/escalate path." But this obligation targets `plan-phase.md` (the orchestrator), not the planner agent's own contract. The orchestrator feeds the planner a prompt, but if the planner's own `<context_fidelity>` block doesn't enforce fidelity to the richer sections, the obligation is prose-only.

**What must happen:** The spec must explicitly state whether the planner's `<context_fidelity>` contract needs widening, or whether the orchestrator-level obligation in `plan-phase.md` is deemed sufficient. If the latter, that is a defensible but weaker choice that should be named as accepted residual risk.

### BG-3: Execution completion semantics change without downstream consumer alignment (Severity: blocking)

[d:c+r:i] The spec proposes to patch `execute-phase.md` (S3, implementation-spec:37) so debt-carrying completion states are labeled rather than reading like ordinary closure. But the spec does not name any downstream propagation obligation:

1. The executor `.toml` (`gsd-executor.toml:494-510`) returns `## PLAN COMPLETE` as the only successful completion marker. There is no debt-carrying variant. Source: [gsd-executor.toml](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/agents/gsd-executor.toml:494), [agent-contracts.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/references/agent-contracts.md:14).
2. The verifier `.toml` (`gsd-verifier.toml:489-501`) determines status based on must-haves verification, not based on execution completion quality. If the executor says PLAN COMPLETE with debt, the verifier has no mechanism to detect that distinction. Source: [gsd-verifier.toml](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/agents/gsd-verifier.toml:489).
3. The `agent-contracts.md` reference (lines 1-60) documents all completion markers and handoff contracts. If completion semantics change, this reference would still describe the old undifferentiated markers. Source: [agent-contracts.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/references/agent-contracts.md:1).
4. The `templates/summary.md` (referenced by executor at line 365) is consumed by the verifier -- if debt-carrying completion should be visible in SUMMARY.md, this template needs a section for it.

**What must happen:** The spec must name whether the debt-carrying distinction propagates into the executor's `.toml` completion format, the agent contracts reference, and/or the summary template -- or whether the distinction lives only at the orchestrator workflow level and downstream consumers do not need to mechanically parse it. Either answer is defensible, but the spec currently does not make the choice.

---

## Propagation Gaps

### PG-1: `agent-contracts.md` not named as a propagation surface

[e:c+r:i] `references/agent-contracts.md` (lines 1-60) is the canonical reference for completion markers and handoff schemas. The spec proposes changes to completion semantics (S1 research disposition, S3 debt-carrying completion) but does not name this file as needing review or update. If later audit reads `agent-contracts.md` and finds it still describes only the pre-change markers, that will read as incomplete follow-through. Source: [agent-contracts.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/references/agent-contracts.md:1).

### PG-2: Plan checker Dimension 11 interaction with research adequacy not analyzed

[e:c+r:i] `gsd-plan-checker.toml` Dimension 11 (lines 491-526) already checks whether RESEARCH.md has unresolved open questions. If the research workflow now requires explicit disposition of open questions (S1), the plan checker's check may become redundant, insufficient, or semantically misaligned with the new contract. The spec should name whether Dimension 11 needs adjustment. Source: [gsd-plan-checker.toml](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/agents/gsd-plan-checker.toml:491).

### PG-3: `phase-prompt.md` template has `future_preservation` not consumed by planner

[e:c+r:i] The repo-local `templates/phase-prompt.md` (lines 25-29) includes a `future_preservation` frontmatter block with `protected_seams`, `non_decisions`, and `posture_assumptions`. This is exactly the kind of steering-to-plan traceability mechanism the spec wants at S2 (implementation-spec:33). But the planner `.toml` plan format specification does not include `future_preservation` in its frontmatter. The template and the planner are out of sync. This is not a defect introduced by the spec, but the spec's S2 change would benefit from acknowledging this existing mechanism rather than inventing a parallel one. Source: [phase-prompt.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/templates/phase-prompt.md:25).

### PG-4: Plan-phase.md stale skill reference identified but not explicitly listed as a patch item

[e:c:i] The spec's Current Workflow Facts (implementation-spec:18) correctly notes that `plan-phase.md:393` still points at `.claude/skills/` or `.agents/skills/`. The Requested Changes S2 (implementation-spec:31) says "remove stale Claude/agents skill guidance." But the specific patch item for lines 393-394 is buried inside a section about steering-to-plan traceability. It should be a distinct, separately auditable patch item since it is a factual correction, not a judgment call. Source: [plan-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/plan-phase.md:393).

### PG-5: Discuss-phase -> planner -> plan checker -> verifier chain not traced

[a:r:i] The spec proposes to reinforce disposition expectations through the chain, but only names two files in the chain: `discuss-phase.md` and `plan-phase.md`. The full chain is:
1. `discuss-phase.md` produces CONTEXT.md
2. `research-phase.md` consumes CONTEXT.md and produces RESEARCH.md
3. `plan-phase.md` orchestrates the planner which consumes both
4. `gsd-plan-checker.toml` verifies the plan
5. `execute-phase.md` orchestrates the executor
6. `gsd-verifier.toml` verifies the result

If steering items are preserved by discuss-phase and research-phase but the plan checker has no dimension to verify their preservation in the plan, the chain breaks silently. This is not necessarily blocking (the orchestrator-level obligation may be sufficient), but the spec does not trace the chain to identify where the disposition expectation stops being mechanically enforceable.

---

## Misclassified Deferrals / Scope Decisions

### MD-1: Template propagation is neither active nor deferred -- it is absent

[e:c+r:i] The spec names `templates/research.md` nowhere. It names `templates/context.md` nowhere. It names `templates/phase-prompt.md` nowhere. These are not deferred -- they are simply not considered. At minimum, the spec should state whether template files are in-scope propagation targets or explicitly out of scope with a named rationale.

### MD-2: Wrapper alignment scope may be over-stated

[e:c+r:i] Reading all four skill wrappers (docs #32-35), they are thin Codex adapters that contain only:
- A `codex_skill_adapter` mapping section
- A re-statement of the workflow `<objective>`
- An `@`-reference that loads the actual workflow file

Since the workflows are loaded at runtime via `@`-reference, the wrappers should automatically pick up workflow changes. The only wrapper content that could lag is the YAML `description` field in the frontmatter, which is a display string, not a semantic contract. This suggests the wrapper alignment pass (S5) may be lighter than the spec implies -- mostly verifying that `description` fields don't actively contradict the new workflow expectations. Sources: [gsd-discuss-phase SKILL.md](/home/rookslog/workspace/projects/prix-guesser/.codex/skills/gsd-discuss-phase/SKILL.md:1), [gsd-plan-phase SKILL.md](/home/rookslog/workspace/projects/prix-guesser/.codex/skills/gsd-plan-phase/SKILL.md:1), [gsd-review SKILL.md](/home/rookslog/workspace/projects/prix-guesser/.codex/skills/gsd-review/SKILL.md:1), [gsd-execute-phase SKILL.md](/home/rookslog/workspace/projects/prix-guesser/.codex/skills/gsd-execute-phase/SKILL.md:1).

### MD-3: R5.9 (compact prompt design) should remain conditional, not promoted

[d:c:i] R5.9 is correctly marked conditional in TASKS.md. This review confirms it should stay conditional -- the current spec has enough work without pulling compaction design into the pre-rerun path.

---

## What Is Already Strong

1. **Citation discipline.** The implementation spec cites specific file:line references for every factual claim and every proposed change. A later auditor can trace each change to its Checkpoint 4 justification without guesswork. This is above the typical spec quality bar.

2. **Scope boundaries are clear.** The explicit non-goals (implementation-spec:47-50) correctly fence off broad hardening, and the deferred hardening set is carried forward from the reactivated launch spec without silent widening. The four requested changes are well-motivated from accepted Checkpoint 4 findings.

3. **Historical correction trail.** The reactivated launch spec preserves the full correction history: why the first Checkpoint 5 was too narrow, why the anti-enumeration rule was misapplied, why the pre-reactivation Track A/B/C work remains valid but insufficient. This makes the widened scope auditable rather than arbitrary. Sources: [checkpoint-5-reactivated-launch-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-reactivated-launch-spec.md:8).

4. **Track A/B/C preservation and materialization.** The implementation note correctly records that runtime-surface changes were materialized into tracked overlay files, explains why, and preserves the launch-truth evidence even though it is fallback-grade. The `.toml` overlay files are well-structured and correctly reject stale runtime surfaces. Sources: [checkpoint-5-bounded-follow-through-implementation-note.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-bounded-follow-through-implementation-note.md:24).

5. **Existing Track B review hardening.** The overlay `review.md` and `planner-reviews.md` already carry stronger review expectations (strongest justified criticism, merely adequate areas, later audit failures, lone high-signal concern preservation). These are real improvements over upstream GSD defaults. Sources: [review.md overlay](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/review.md:122), [planner-reviews.md overlay](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/references/planner-reviews.md:10).

6. **The launch-truth helper** is well-implemented: it captures requested vs. effective settings, normalizes sandbox policies, handles missing fields as unresolved rather than inferred, and explicitly labels `--latest` as weaker evidence. Sources: [capture_launch_truth.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/capture_launch_truth.py:52).

---

## What Must Change Before Implementation

1. **Name template propagation targets explicitly.** The spec must state whether `templates/research.md`, `templates/context.md`, and `references/agent-contracts.md` are in-scope or explicitly deferred with consequence. The current silence reads as oversight, not as a deliberate scope decision.

2. **Resolve the planner CONTEXT.md consumption gap.** The spec proposes to strengthen both `discuss-phase.md` and `plan-phase.md`, but the planner's own `<context_fidelity>` contract only mandates three-section fidelity. The spec must either widen the planner's contract or name this as accepted residual risk.

3. **Decide the debt-carrying completion propagation boundary.** The spec must state whether the execution debt-carrying distinction lives only in the orchestrator workflow or whether it propagates into the executor `.toml`, agent contracts, and/or summary template. The current spec proposes the change but does not trace its propagation.

4. **Separate the plan-phase.md stale skill reference fix from the steering-to-plan traceability change.** These are different kinds of edits -- one is a factual correction, the other is a judgment-laden workflow obligation. Bundling them makes the stale reference fix harder to audit independently.

---

## What Can Remain Deferred

1. **Full plan checker dimension adjustment for research adequacy.** Dimension 11 may need future adjustment, but the current checker is not broken -- it checks for unresolved open questions, which is compatible with a richer disposition requirement. This can wait until the research changes land and are verified.

2. **`future_preservation` template-planner alignment.** The template has it; the planner doesn't consume it. This is a pre-existing gap, not one introduced by the spec. It can remain deferred if the spec acknowledges it as context for S2.

3. **Compact prompt design (R5.9).** Correctly conditional.

4. **Broader skill enumeration.** The spec correctly resists this.

5. **Branch/worktree boundary materialization.** Correctly accepted as bounded risk.

6. **Agent contract marker evolution.** If the debt-carrying distinction is explicitly scoped to the orchestrator level only, then agent contracts do not need updating and can remain deferred.

---

## Shared Contract Consequences

### If CONTEXT.md semantics change (S4):

| Downstream consumer | Current state | Consequence if not updated |
|---|---|---|
| `templates/context.md` | Already supports rich sections | Low risk -- template is ahead of workflow |
| `gsd-phase-researcher.toml` | Consumes `## Decisions`, `## Claude's Discretion`, `## Deferred Ideas` | May ignore new disposition expectations in `<working_model>` or `<open_questions>` |
| `gsd-planner.toml` `<context_fidelity>` | Only mandates three-section fidelity | **Will silently drop richer steering** -- this is the primary propagation failure point |
| `gsd-plan-checker.toml` | No dimension for CONTEXT.md steering preservation | Planning can pass checker while dropping steering |

### If RESEARCH.md semantics change (S1):

| Downstream consumer | Current state | Consequence if not updated |
|---|---|---|
| `templates/research.md` | No disposition section | **Researchers will produce old-format output** |
| `gsd-planner.toml` | Consumes `## User Constraints`, `## Standard Stack`, etc. | May ignore new disposition section |
| `gsd-plan-checker.toml` Dimension 11 | Checks for `## Open Questions (RESOLVED)` | Compatible but may become semantically misaligned |
| `references/agent-contracts.md` | Lists `## RESEARCH COMPLETE` / `## RESEARCH BLOCKED` | Incomplete if new disposition marker is added |

### If planning closure pressure changes (S2):

| Downstream consumer | Current state | Consequence if not updated |
|---|---|---|
| `references/checkpoints.md` | Describes checkpoint protocols, not planning closure | No direct conflict |
| `gsd-plan-checker.toml` | Strong gates already | Compatible -- checker raises issues, plan-phase decides what to do with them |
| Stale skill reference at `plan-phase.md:393` | Points to `.claude/skills/` | **Researcher spawn prompt will carry stale hint contradicting repo doctrine** |

### If execution completion semantics change (S3):

| Downstream consumer | Current state | Consequence if not updated |
|---|---|---|
| `gsd-executor.toml` completion format | Only `## PLAN COMPLETE` | **Cannot express debt-carrying state** |
| `references/agent-contracts.md` | Only lists `## PLAN COMPLETE`, `## CHECKPOINT REACHED` | Would not document new distinction |
| `gsd-verifier.toml` | Classifies on must-haves, not completion quality | **Would misclassify debt-carrying as clean if must-haves technically pass** |
| `templates/summary.md` | No debt-carrying section | Debt would not be visible in summary |

---

## Change Summary

| Item | Status | Action Required |
|---|---|---|
| S1 Research adequacy (workflow) | Strong | Proceed with named template propagation |
| S1 Research adequacy (template) | Gap | Name `templates/research.md` as target |
| S1 Research adequacy (agent contracts) | Gap | Name or explicitly defer |
| S2 Stale skill reference | Strong but bundled | Separate into distinct patch item |
| S2 Anti-permissive closure | Strong | Proceed |
| S2 Steering-to-plan traceability | Strong at orchestrator level | Resolve planner contract gap |
| S3 Debt-carrying completion (workflow) | Strong | Proceed |
| S3 Debt-carrying completion (propagation) | Gap | Decide propagation boundary |
| S4 Auto/default pressure | Strong | Proceed |
| S5 Wrapper alignment | Probably lighter than expected | Verify thin-adapter assumption |
| Template propagation (overall) | Absent | Must be explicitly owned or deferred |
| Agent contracts reference | Absent | Must be explicitly owned or deferred |
| Planner CONTEXT.md consumption | Gap | Must be resolved before implementation completes |

---

**Bottom line:** The spec is directionally right and well-cited. The four workflow edits can begin now. But the spec under-owns the propagation consequences of its own proposed changes. Before the widened Checkpoint 5 can close, the spec must either own the propagation targets or explicitly defer them with named consequences. The most likely later audit failure from this stack unchanged is: "The workflows say the right things but the templates, agent contracts, and planner consumption contract still carry the old semantics, so the actual rerun will produce artifacts in the old shape."
