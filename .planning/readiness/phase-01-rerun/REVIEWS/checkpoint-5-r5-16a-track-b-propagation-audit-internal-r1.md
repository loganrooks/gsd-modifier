# Checkpoint 5 R5.16a Track B Propagation Audit — Internal R1

## Verdict

- [e:c:i] `Disposition: revise-current`. Track B is directionally stronger on the producer side, but it is not closure-ready against the current Checkpoint 5 standard because the promoted review doctrine still weakens at two real handoff points: the `--reviews` replanning consumer is not explicitly bound to the stronger review-consumption contract, and the human-facing review completion summary still recenters consensus at the moment lone high-signal criticism was supposed to survive. Sources: `.planning/readiness/phase-01-rerun/STATUS.md:93-99`; `.planning/readiness/phase-01-rerun/GATES/checkpoint-5.md:107-114`; `.codex/get-shit-done/references/planner-reviews.md:7-36`; `.codex/get-shit-done/workflows/plan-phase.md:5-13,668-705`; `.codex/get-shit-done/workflows/review.md:237-295`.
- [e:c+r:i] The surviving blockers are still primarily local to the review/replanning chain. This lane does surface wider closure-pressure signals, but not yet enough on its own to promote `R5.17` before adjudication. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md:79-87`; `.codex/get-shit-done/references/checkpoints.md:4-12`; `.codex/get-shit-done/workflows/plan-phase.md:1094-1127`.

## Blocking Propagation Gaps

1. `High` — Reviews-mode replanning is still an orphaned contract.
Evidence: the strongest consumer contract exists in `.codex/get-shit-done/references/planner-reviews.md:7-56`, where the planner is told to preserve lone high-signal criticism, treat merely-adequate areas as `should address`, and emit explicit addressed/deferred/rejected review accounting. But the `plan-phase` workflow does not list that file in `required_reading` (`.codex/get-shit-done/workflows/plan-phase.md:5-13`), the `gsd-plan-phase` wrapper does not include it in its `execution_context` (`.codex/skills/gsd-plan-phase/SKILL.md:56-59`), and the planner prompt itself only passes `reviews_path` as another file in `<files_to_read>` without any mode-specific review-consumer instructions (`.codex/get-shit-done/workflows/plan-phase.md:668-705`).
Why it matters: Track B is supposed to prove that the stronger review posture reaches real replanning consumers, not merely that a good reference doc exists. Right now the key doctrine is present as adjacent text, not clearly load-bearing in the actual `--reviews` planning path.

2. `High` — The human-facing review handoff still collapses the stronger synthesis back into consensus.
Evidence: `review.md` now asks reviewers for `Strongest Justified Criticism`, `What Is Merely Adequate`, and `Later Audit Failures` (`tooling/portable-gsd/overlay/get-shit-done/workflows/review.md:117-141`; `.codex/get-shit-done/workflows/review.md:117-141`) and writes a synthesis with `Lone High-Signal Concerns`, `Merely Adequate Areas`, `Later Audit Risks`, and `Divergent Views` (`tooling/portable-gsd/overlay/get-shit-done/workflows/review.md:237-257`; `.codex/get-shit-done/workflows/review.md:237-257`). But the very next handoff surface tells the user only `Consensus concerns:` and the success criteria still require a `Consensus summary synthesized from multiple reviewers` (`.codex/get-shit-done/workflows/review.md:266-295`). That is in direct tension with the planner-side rule that lack of consensus does not automatically downgrade a criticism (`.codex/get-shit-done/references/planner-reviews.md:16,20-36`).
Why it matters: the first real consumer after review generation is the operator. If that surface re-centers shared overlap and omits lone high-signal / later-audit categories, the stronger doctrine is already being flattened before replanning even begins.

## Local But Important Gaps

1. `Medium` — Wrapper-level propagation is still partial rather than explicit.
Evidence: `gsd-review` loads only the review workflow in its execution context (`.codex/skills/gsd-review/SKILL.md:48-75`), while `gsd-plan-phase` exposes `--reviews` but loads only `plan-phase.md` and `ui-brand.md` (`.codex/skills/gsd-plan-phase/SKILL.md:48-83`).
Why it matters: the first-invoked skill surfaces do not themselves expose the stronger review-consumer doctrine. That does not block a deeper workflow fix, but it leaves the lane more dependent on ambient knowledge than the current checkpoint standard should tolerate.

2. `Medium` — The portable source-of-truth side of the Track B pair is not yet provenance-safe enough to count as closure-ready.
Evidence: the implementation spec makes tracked overlay/materialization ownership mandatory for touched runtime surfaces (`.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md:29-37,123-131`). In the current repo state, `git status --short -- tooling/portable-gsd/overlay/get-shit-done/workflows/review.md tooling/portable-gsd/overlay/get-shit-done/references/planner-reviews.md` reports both overlay Track B files as untracked.
Why it matters: the live `.codex` copies may already carry the stronger language, but Track B still cannot honestly present the overlay pair as a tracked, auditable portable source of truth yet.

## Signals That The Problem May Already Be Wider

1. [e:c+r:i] The auto/default pressure chain is still permissive outside the dedicated review files. `checkpoints.md` says auto mode bypasses `human-verify` and `decision` checkpoints by auto-approving them (`.codex/get-shit-done/references/checkpoints.md:4-12`), and the implementation spec already treats this chain as active Checkpoint 5 scope rather than a `review.md`-only concern (`.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md:79-87`).
2. [e:c+r:i] `plan-phase` still points the user primarily toward execution, with review kept in the optional `Also available` bucket (`.codex/get-shit-done/workflows/plan-phase.md:1094-1127`). That suggests closure pressure is not confined to Track B producer/consumer files.

## What Is Already Strong

1. [e:c:i] The producer-side review artifact shape is materially better. Both the overlay candidate and the live installed `review.md` now demand strongest-criticism, merely-adequate, and later-audit framing, then preserve those distinctions in the written synthesis (`tooling/portable-gsd/overlay/get-shit-done/workflows/review.md:117-141,237-257`; `.codex/get-shit-done/workflows/review.md:117-141,237-257`).
2. [e:c:i] `planner-reviews.md` is a strong downstream contract on paper. It explicitly refuses false-consensus dismissal, requires lone high-signal criticism to be answered on the merits, and requires addressed/deferred/rejected accounting in planner output (`tooling/portable-gsd/overlay/get-shit-done/references/planner-reviews.md:7-56`; `.codex/get-shit-done/references/planner-reviews.md:7-56`).
3. [e:c+r:i] There is no substantive overlay/live semantic split inside the two Track B text surfaces themselves. The same stronger review instructions and the same stronger planner-consumption rules are already present in both the overlay candidate and the live installed copies, so the current propagation failure is downstream consumption and handoff rather than a content contradiction between those paired files. Sources: `tooling/portable-gsd/overlay/get-shit-done/workflows/review.md:117-141,237-257`; `.codex/get-shit-done/workflows/review.md:117-141,237-257`; `tooling/portable-gsd/overlay/get-shit-done/references/planner-reviews.md:7-56`; `.codex/get-shit-done/references/planner-reviews.md:7-56`.

## What Must Change Before Track B Can Count As Closure-Ready

1. Make the `--reviews` plan-phase path explicitly load-bearing on the stronger consumer contract. That can happen by loading `planner-reviews.md` as required reading, inlining its obligations into the planner prompt, or both, but the current ambient arrangement is not enough.
2. Replace the consensus-only `present_results` handoff in `review.md` with a summary that also surfaces `Lone High-Signal Concerns`, `Merely Adequate Areas`, `Later Audit Risks`, and `Divergent Views`.
3. Decide whether wrapper-level skill surfaces should explicitly carry the stronger doctrine. If not, make the deeper workflow enforcement strong enough that wrapper omission is clearly non-load-bearing.
4. If the Track B pair is part of the candidate patch set, make the overlay side actually tracked so the portable source-of-truth claim is auditably true.

## What Can Remain Local

1. [e:r:i] The main repair path can still remain inside the review/replanning chain: `review.md`, `planner-reviews.md`, `gsd-plan-phase`, and `plan-phase.md`. This audit does not yet prove that a broader `R5.17` premature-closure trace lane is already mandatory.
2. [e:r:i] The wider signals should be carried into `R5.16c`/`R5.16d` as explicit adjudication pressure, not silently promoted from this lane alone. The right next move is a tighter local repair plus later anti-regret judgment, not immediate omnibus widening.

## Change Summary

- [e:r:i] Track B has already improved the review producer surfaces substantially, but the surviving weakness is still consumer-side: stronger review categories are generated, then weakened at the operator handoff and left under-bound in the `--reviews` replanning path.
- [e:r:i] The narrowest scrutiny-resistant next disposition is `revise-current`: fix the local review/replanning propagation chain first, then let adjudication decide whether the wider closure-pressure signals still justify `R5.17`.
