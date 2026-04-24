# Checkpoint 5 Internal Review R1

- checkpoint: `5`
- artifact(s) under review:
  - `WORKFLOW.md`
  - `AI-GUARDRAILS.md`
  - `tooling/codex/capture_launch_truth.py`
  - `tooling/portable-gsd/overlay/agents/gsd-phase-researcher.toml`
  - `tooling/portable-gsd/overlay/agents/gsd-planner.toml`
  - `tooling/portable-gsd/overlay/agents/gsd-plan-checker.toml`
  - `tooling/portable-gsd/overlay/agents/gsd-executor.toml`
  - `tooling/portable-gsd/overlay/agents/gsd-verifier.toml`
  - `tooling/portable-gsd/overlay/get-shit-done/workflows/review.md`
  - `tooling/portable-gsd/overlay/get-shit-done/references/planner-reviews.md`
  - `AUDITS/checkpoint-5-bounded-follow-through-implementation-note.md`
  - `AUDITS/checkpoint-5-launch-truth-capture-fallback.md`
- review mode: `internal-verification-agent`
- authoring lane: `checkpoint-5 bounded follow-through`
- reviewer: `Codex`
- model / reasoning or vendor: `gpt-5.4 high`
- baseline commit / artifact snapshot: `7f24b1d` plus current uncommitted Checkpoint 5 candidate state as of `2026-04-15`
- independence relationship: `independent`

## Historical Status

- [d:c:i] This review applies only to the pre-reactivation partial Checkpoint 5 bundle. It remains valid as audit evidence, but it is not closure authority for the reactivated Checkpoint 5 scope now governed by [checkpoint-5-reactivated-launch-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-reactivated-launch-spec.md:1).

## Verdict

- status: `revise-current`
- explanation:
  - [e:c+r:i] Checkpoint 5 is not yet closure-ready. Track A is strong and the live-versus-tracked worker-alignment seam is materially better handled, but Track B and Track C each leave one load-bearing gap in the current candidate:
    - the review workflow still collapses its own handoff summary back to `consensus concerns`, which undercuts the claimed lone-high-signal preservation at the exact surface a human is most likely to skim first ([review.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/review.md:237), [review.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/review.md:276), [review.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/review.md:293))
    - the launch-truth helper still treats `--requested-agent` as operator-declared only and emits no effective agent-identity field in the artifact, so doctrine-sensitive launches cannot be tied back to the intended worker wave with the same requested-versus-effective discipline now required elsewhere ([WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:77), [capture_launch_truth.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/capture_launch_truth.py:93), [capture_launch_truth.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/capture_launch_truth.py:296), [capture_launch_truth.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/capture_launch_truth.py:328))
- before Checkpoint 5 can close:
  - [d:r:i] Extend the launch-truth helper and the recorded artifact so requested agent identity can be compared against an effective runtime field when available, then regenerate the Checkpoint 5 launch-truth capture on that stronger basis.
  - [d:r:i] Update the review workflow's completion/output contract so lone high-signal concerns stay visible in the workflow summary and success criteria rather than only inside the full `REVIEWS.md` body.

## Findings

1. [e:c+r:i] The launch-truth helper still leaves requested agent identity effectively unverified, which is too weak for a checkpoint whose Track C claim is durable doctrine-sensitive launch capture. The workflow now explicitly says to use `--requested-agent` and `--requested-agent-path` when named-worker identity matters, but the helper's output table only records `agent_role` and `agent_path`, and its assessment text says `requested_agent` is operator-declared intent only. The recorded fallback artifact then omits both `requested_agent` and any effective agent-identity column, so the current evidence can show generic worker settings but not which intended workers those rows actually were ([WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:77), [capture_launch_truth.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/capture_launch_truth.py:93), [capture_launch_truth.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/capture_launch_truth.py:179), [capture_launch_truth.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/capture_launch_truth.py:296), [capture_launch_truth.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/capture_launch_truth.py:328), [checkpoint-5-launch-truth-capture-fallback.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-launch-truth-capture-fallback.md:8), [checkpoint-5-launch-truth-capture-fallback.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-launch-truth-capture-fallback.md:16), [checkpoint-5-bounded-follow-through-implementation-note.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-bounded-follow-through-implementation-note.md:21)).

2. [e:c+r:i] Track B is materially stronger inside `REVIEWS.md`, but the workflow still re-centers consensus bias at its own handoff boundary. The new synthesis body explicitly preserves lone high-signal concerns and merely-adequate areas, and the planner reread reference no longer auto-downgrades non-consensus criticism. But the workflow's `present_results` step still shows only `Consensus concerns`, and the success criteria still define success as a `Consensus summary synthesized from multiple reviewers`. That keeps reviewer overlap as the user-facing headline even after the checkpoint claimed to fix that exact bias ([review.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/review.md:237), [review.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/review.md:247), [review.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/review.md:276), [review.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/review.md:293), [planner-reviews.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/references/planner-reviews.md:20), [planner-reviews.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/references/planner-reviews.md:29), [checkpoint-5-bounded-follow-through-implementation-note.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-bounded-follow-through-implementation-note.md:20)).

## What Is Already Strong

- [e:c+r:i] Track A is the strongest part of the candidate. The phase-critical worker prompts now point at repo-root `AGENTS.md`, conditionally route into `.planning/AGENTS.md`, reject stale `CLAUDE.md` and legacy skill-path doctrine, and the tracked overlay mirrors the live `.codex` state rather than leaving the repo dependent on ignored local edits alone ([gsd-phase-researcher.toml](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/agents/gsd-phase-researcher.toml:32), [gsd-planner.toml](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/agents/gsd-planner.toml:40), [gsd-plan-checker.toml](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/agents/gsd-plan-checker.toml:36), [gsd-executor.toml](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/agents/gsd-executor.toml:27), [gsd-verifier.toml](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/agents/gsd-verifier.toml:27), [setup-portable-gsd.sh](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh:15)).

- [e:c+r:i] The core review prompt and planner reread protocol are substantively better than before. The review request now asks for strongest justified criticism, merely adequate areas, and later audit failures, while the planner reread guidance now treats lone high-signal criticism as potentially must-address even without reviewer overlap ([review.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/review.md:121), [review.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/review.md:137), [review.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/review.md:247), [planner-reviews.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/references/planner-reviews.md:20), [planner-reviews.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/references/planner-reviews.md:29), [planner-reviews.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/references/planner-reviews.md:33)).

- [e:c+r:i] Track C is epistemically cleaner than the pre-checkpoint state even though it is not finished. The helper distinguishes requested from effective settings, the workflow explicitly prefers `--since` over `--latest`, and the artifact correctly labels fallback capture as weaker evidence while leaving unresolved fields unresolved instead of inventing confidence ([WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:71), [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:78), [AI-GUARDRAILS.md](/home/rookslog/workspace/projects/prix-guesser/AI-GUARDRAILS.md:89), [capture_launch_truth.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/capture_launch_truth.py:358), [capture_launch_truth.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/capture_launch_truth.py:366), [checkpoint-5-launch-truth-capture-fallback.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-launch-truth-capture-fallback.md:27)).

## Open Questions / Assumptions

- [a:r:i] I am assuming the intended durable identity comparison for `--requested-agent` can be grounded in an effective sqlite field that is already present at launch time, rather than requiring a heavier new launch-management subsystem. If that assumption is wrong, the checkpoint needs to say so explicitly instead of implying that `--requested-agent` is already meaningfully captured.

- [o:r:i] If the repo wants the review workflow's top-level CLI summary to remain consensus-oriented for brevity, it still needs a parallel explicit slot for `lone high-signal concern` in that same summary. Otherwise the checkpoint should stop claiming that lone strong criticism is preserved at the handoff boundary rather than only inside the full artifact.

## Change Summary

- [e:c:i] The candidate made three real moves:
  - aligned the phase-critical live/overlay worker prompts with the repo's actual instruction and skill surfaces
  - strengthened the cross-AI review prompt plus planner reread protocol
  - added a repo-local launch-truth helper plus standing requested-versus-effective doctrine

- [e:r:i] The remaining work is bounded, not a checkpoint reset:
  - finish requested-agent truth capture so Track C can substantiate named doctrine-sensitive launches
  - finish the review handoff contract so Track B does not reintroduce consensus bias in its own completion surface
