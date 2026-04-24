# Checkpoint 5 Pre-Reactivation Partial Follow-Through Cross-Vendor Review Prompt

Review the authored pre-reactivation partial Checkpoint 5 follow-through candidate before closure.

This is a cross-vendor reread of the executed partial follow-through, not a replacement implementation pass.

Historical note:

- this prompt applies only to the pre-reactivation partial bundle
- after Checkpoint 5 scope reactivation, it remains part of the audit trail but no longer defines closure review for the widened checkpoint

## Review Stance

- Review against a high bar, not a minimal pass bar.
- Be firm, specific, and justified when the candidate is settling for adequacy.
- Do not be rude or arbitrarily harsh.
- Try seriously to falsify closure-readiness before declaring the checkpoint strong.
- Do not treat `technically passes` as sufficient if a stronger bounded follow-through was reasonably achievable.
- Criticism should be justified in terms of rigor, auditability, future viability, architectural soundness, or quality of judgment.

## Governing Inputs

Read these first:

1. [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md)
2. [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md)
3. [PLAN.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PLAN.md)
4. [STATUS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/STATUS.md)
5. [TASKS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/TASKS.md)
6. [GATES/checkpoint-5.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/GATES/checkpoint-5.md)
7. [AUDITS/checkpoint-5-bounded-follow-through-launch-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-bounded-follow-through-launch-spec.md)
8. [AUDITS/checkpoint-5-reactivated-launch-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-reactivated-launch-spec.md)
9. [AUDITS/checkpoint-5-bounded-follow-through-implementation-note.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-bounded-follow-through-implementation-note.md)
10. [AUDITS/checkpoint-5-launch-truth-capture-fallback.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-launch-truth-capture-fallback.md)

Then review these changed surfaces:

- [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md)
- [AI-GUARDRAILS.md](/home/rookslog/workspace/projects/prix-guesser/AI-GUARDRAILS.md)
- [tooling/codex/capture_launch_truth.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/capture_launch_truth.py)
- [tooling/portable-gsd/overlay/agents/gsd-phase-researcher.toml](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/agents/gsd-phase-researcher.toml)
- [tooling/portable-gsd/overlay/agents/gsd-planner.toml](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/agents/gsd-planner.toml)
- [tooling/portable-gsd/overlay/agents/gsd-plan-checker.toml](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/agents/gsd-plan-checker.toml)
- [tooling/portable-gsd/overlay/agents/gsd-executor.toml](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/agents/gsd-executor.toml)
- [tooling/portable-gsd/overlay/agents/gsd-verifier.toml](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/agents/gsd-verifier.toml)
- [tooling/portable-gsd/overlay/get-shit-done/workflows/review.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/review.md)
- [tooling/portable-gsd/overlay/get-shit-done/references/planner-reviews.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/references/planner-reviews.md)

## Review Questions

- did the pass actually solve the rerun-blocking seams that Checkpoint 4 assigned to Checkpoint 5?
- are the runtime-authoritative worker surfaces now aligned on both live and tracked truth, or is the repo still depending on ignored local state?
- are the review / closure-pressure changes genuinely stronger, or only cosmetically more demanding?
- is the launch-truth helper honest about effective-versus-requested capture, fallback weakness, and unresolved runtime fields?
- did this pass stay bounded, or did it quietly smuggle in deferred hardening?
- what is the strongest justified criticism of this candidate?
- what is merely acceptable here but should be stronger?
- what would fail later stringent audit by strong engineers, designers, or researchers?
- what meaningful quality opportunity is being left unused?

## Output Requirements

Write a review artifact with:

- `Verdict`
- `Findings`
- `What Is Already Strong`
- `What Must Change Before Closure`
- `What Can Wait Until Later`

Findings should be ordered by severity and cite concrete file lines.

If the candidate is closure-ready, say so explicitly.
If not, say exactly what must change before Checkpoint 5 can close.
