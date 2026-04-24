# Checkpoint 4 Converged Synthesis

## Research Frame

- [g:c:i] This synthesis decides whether the current workflow/harness stack is already strong enough to carry forward, whether the remaining deficits are mainly doctrine/protocol cleanup, or whether a bounded Checkpoint 5 must open before rerun-readiness verification. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-converged-synthesis-spec.md:1-49`; `.planning/readiness/phase-01-rerun/PLAN.md:409-435,579-585`.
- [g:c:i] The decision standard is the repo’s current excellence bar, not “can the system probably make progress.” The question is whether the stack can support the best planning, review, verification, and rerun work this repo can reasonably produce, and whether that verdict would survive later adversarial reread. Sources: `AGENTS.md:47-83`; `.planning/AGENTS.md:42-58,98-112`; `.planning/readiness/phase-01-rerun/GATES/checkpoint-4.md:26-47`.
- [s:c:i] I treat the four lane outputs plus the seam synthesis as the full evidence set for Checkpoint 4. I do not reopen Checkpoint 3 scope, and I do not bluff a cleaner answer than the evidence supports. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-cross-lane-seam-synthesis.md:1-48`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-workflow-harness-excellence-launch-spec.md:40-57,100-119`.

## Path Of Inquiry

1. Re-read the Checkpoint 4 gate and the plan’s branching logic so the verdict would map cleanly onto the accepted `record result / avoid overbuilding` versus `open bounded Checkpoint 5` branches. Sources: `.planning/readiness/phase-01-rerun/GATES/checkpoint-4.md:34-57`; `.planning/readiness/phase-01-rerun/PLAN.md:409-435,579-585`.
2. Compared the lane-local verdicts against the seam synthesis instead of simply counting findings. The key question was whether the stack’s weaknesses are mostly wording/protocol thinness or whether at least some of them are now demonstrably carried by runtime-authoritative machinery surfaces. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-cross-lane-seam-synthesis.md:13-47`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-codex-load-bearing-surfaces-and-seams.md:44-48,69-83`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-gsd-runtime-config-overlay-truth-excellence.md:43-47,64-86`.
3. Tested the emerging verdict against the repo’s own anti-regression logic: do not overbuild the harness when docs and protocol would suffice, but also do not treat real runtime-authority drift as if clearer prose alone could fix it. Sources: `.planning/readiness/phase-01-rerun/PLAN.md:143-145,426-432,498-597`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-cross-lane-seam-synthesis.md:32-47`.

## What Is Already Strong

- [e:c+r:i] The upstream steering and planning surfaces are genuinely stronger than “passable workflow.” `CONTEXT.md`, `canonical_refs`, `future_awareness`, and `future_preservation` create a serious steering contract, while `gsd-plan-checker` and `gsd-verifier` bring real skepticism rather than merely confirming that artifacts exist. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-gsd-workflow-chain-and-artifact-contracts-excellence.md:24-28,32-35,58-59`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-gsd-agent-doctrine-and-role-contracts-excellence.md:22-27,31-35`.
- [e:c+r:i+d] The repo’s continuity posture for readiness work is materially strong. The current package uses durable artifacts, a readiness-specific compact prompt, a re-entry checklist, and explicit fresh-thread doctrine rather than trusting compaction or resumed context. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-codex-load-bearing-surfaces-and-seams.md:26,38-39,52-56`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-cross-lane-seam-synthesis.md:19-21`.
- [e:c+r:i] Core planning/execution model policy is already better than ambient defaulting. The Codex and runtime lanes independently found the main `gpt-5.4` / `xhigh` planning / `high` execution doctrine materially encoded for the most important roles. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-codex-load-bearing-surfaces-and-seams.md:27,60-66`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-gsd-runtime-config-overlay-truth-excellence.md:31,38,59-60`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-gsd-agent-doctrine-and-role-contracts-excellence.md:78`.
- [e:c+r:i] The stack is not missing review or verification machinery. It already has cross-AI review surfaces, code review, schema/regression checks, and goal-backward verifier logic. The problem is not absence of machinery; it is the softness and unevenness of the pressure those surfaces apply. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-gsd-workflow-chain-and-artifact-contracts-excellence.md:27-28,58-61`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-gsd-agent-doctrine-and-role-contracts-excellence.md:27,42-43,49-50`.

## Where The Stack Is Still Pass/Fail-Thin

- [e:c+r:i+d] The operative worker-authority seam is still thinner than the human-facing docs imply. The registered `.toml` worker prompts and the home-level Codex instruction layer still carry stale doctrine, so the current stack can look more aligned than the runtime-authoritative surfaces actually are. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-codex-load-bearing-surfaces-and-seams.md:33-36,44-48,69-73`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-gsd-agent-doctrine-and-role-contracts-excellence.md:39,56`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-gsd-runtime-config-overlay-truth-excellence.md:47,65-67,86`.
- [e:c+r:i] The workflow chain is excellence-capable but not excellence-demanding. It preserves epistemic richness early, then reintroduces closure-biased exits through advisory review, auto-approved checkpoints, `Proceed anyway` branches, and approval-based advancement with partial verification debt. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-gsd-workflow-chain-and-artifact-contracts-excellence.md:40-45,60-67`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-gsd-agent-doctrine-and-role-contracts-excellence.md:42-43,49-50,57`.
- [e:c+r:i] Claim discipline still collapses downstream from research. The repo now expects load-bearing planning/process artifacts to expose claim status and source basis, but that discipline is mostly absent from planner, checker, reviewer, and verifier outputs. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-gsd-agent-doctrine-and-role-contracts-excellence.md:40,51,58`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-gsd-workflow-chain-and-artifact-contracts-excellence.md:49-52,66`.
- [e:c+r:i] Runtime reproducibility and config truth are still too weak for a repo now auditing its harness seriously. Unpinned upstream install, stale ignored provenance, absolute-path portability holes, and a split config contract mean the runtime story is not yet as reviewable as the doctrine story. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-gsd-runtime-config-overlay-truth-excellence.md:43-47,51-67,71-75`.
- [e:r:i] Not all of those runtime/config weaknesses carry the same pre-rerun weight. The current live install is coherent enough to audit, so broader reinstall/provenance hardening reads more like important follow-on hardening unless Checkpoint 5 ends up touching materialization surfaces directly. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-gsd-runtime-config-overlay-truth-excellence.md:29-31,43-47,71-75`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-cross-lane-seam-synthesis.md:59-64`.
- [e:c+r:i] Branch/worktree materialization remains a real but under-evidenced seam. There is enough evidence to keep it visible, but not enough to make it the center of Checkpoint 5. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-cross-lane-seam-synthesis.md:24-31`.

## Strongest Justified Criticisms

- [e:c+r:i+d] The stack still requires too much operator compensation at the exact seams where runtime truth should already be reliable: operative worker doctrine, launch truth, and reproducible local harness state. That is not a documentation-only problem anymore. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-cross-lane-seam-synthesis.md:32-35,43`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-codex-load-bearing-surfaces-and-seams.md:44-48,69-83`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-gsd-runtime-config-overlay-truth-excellence.md:64-67`.
- [e:c+r:i] The phase workflow still makes it too easy to look complete before the strongest criticism has really been preserved or answered. That is clearest in advisory/non-blocking review, auto-approved checkpoints, partial human-verification closure, and consensus-biased reread synthesis. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-gsd-workflow-chain-and-artifact-contracts-excellence.md:41-45,60-67`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-gsd-agent-doctrine-and-role-contracts-excellence.md:42-43,49-50,57`.
- [e:c+r:i] The harness front-loads nuance and then only partially translates it. The strongest steering artifacts (`CONTEXT.md`, canonical refs, future-awareness) are better than the downstream traceability and evidence-basis contracts they feed. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-gsd-workflow-chain-and-artifact-contracts-excellence.md:24,32-33,49-52,65-66`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-gsd-agent-doctrine-and-role-contracts-excellence.md:40,58`.
- [e:c+r:i] The repo’s portable-GSD story is not yet strong enough to survive a hard scrutiny pass without qualification. It is useful and partly real, but still too dependent on local coincidence and reinstall discipline. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-gsd-runtime-config-overlay-truth-excellence.md:43-47,64-67`.

## Strategic Opportunities

- [p:r:i+d] Unify runtime-authoritative worker prompts with the repo’s actual instruction and skill surfaces so the best doctrine stops losing to legacy launch-facing overlays.
- [p:r:i] Strengthen review and completion pressure so lone strong criticism, research adequacy, and debt-carrying closure are preserved explicitly instead of being procedurally softened.
- [p:r:i] Extend lightweight claim-discipline into downstream planning/review/verification artifacts where later rereads need to know what is cited, what is inferred, and what remains assumption or projection.
- [p:r:i] Make the portable local GSD story genuinely reproducible: pin upstream version, track provenance in reviewable form, and finish the remaining path-normalization work.
- [p:r:i+d] Turn launch-truth verification into a durable review boundary rather than an orchestrator memory task whenever high-stakes worker launches materially steer doctrine or rerun readiness.

## Doc vs Protocol vs Machinery Ownership Verdict

- [e:r:i] `Doc-level doctrine only` is not enough. There are still doc-local opportunities, especially around claim-discipline propagation and stale home-level instructions, but the audit found runtime-authoritative worker drift and reproducibility seams that clearer wording alone cannot fix. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-codex-load-bearing-surfaces-and-seams.md:44-48,69-73`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-gsd-runtime-config-overlay-truth-excellence.md:43-47,64-67`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-gsd-agent-doctrine-and-role-contracts-excellence.md:56`.
- [e:r:i] `Workflow-protocol` owns a large share of the quality gap. The biggest non-machinery deficits are review sharpness, research adequacy/disposition, debt-carrying completion semantics, and better translation of steering richness into later obligations. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-gsd-workflow-chain-and-artifact-contracts-excellence.md:40-45,49-53,60-75`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-gsd-agent-doctrine-and-role-contracts-excellence.md:40-43,49-59`.
- [e:r:i] `Machinery-owned` follow-through is now justified, but only in a bounded way. The cleanest machinery-owned problems are:
  - runtime-authoritative `.toml` worker drift
  - unpinned install / stale provenance / portability truth
  - incomplete explicit model truth for some roles
  Those are real harness ownership problems, not just governance prose dissatisfaction. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-codex-load-bearing-surfaces-and-seams.md:44-48,60-66,69-83`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-gsd-runtime-config-overlay-truth-excellence.md:43-47,64-67,81-86`.
- [e:r:i] Overall verdict: the stack is `mixed-strong but not yet strong enough to carry forward untouched`. It does materially support better work than a generic default stack, but it still leans too hard on strong operators at several load-bearing seams.

## Branching-Logic Alignment

- [e:c:i] The relevant plan branch is the Checkpoint 4 split between:
  - `record the result and avoid overbuilding the harness` when findings are mostly process/doctrine
  - `run Checkpoint 5 before rerun` when the audit finds real harness ownership problems. Sources: `.planning/readiness/phase-01-rerun/PLAN.md:579-585`.
- [e:r:i] Counter-hypothesis tested: `could the rerun proceed if we skipped Checkpoint 5 and limited ourselves to doctrine/protocol cleanup plus opportunistic core-chain `.toml` fixes?` My answer is no. That path would still leave two rerun-distorting harness truths unresolved:
  - the runtime-authoritative phase-critical worker surface would remain partly stale until treated explicitly as a harness task rather than incidental wording cleanup
  - the current review/closure machinery would still encode advisory or debt-carrying progression semantics at precisely the stage where the rerun needs stronger quality pressure, not just stronger governance prose
  Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-codex-load-bearing-surfaces-and-seams.md:44-48`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-gsd-agent-doctrine-and-role-contracts-excellence.md:42-43,49-50,56-57`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-gsd-workflow-chain-and-artifact-contracts-excellence.md:44-45,60-67`.
- [e:r:i] This audit does not justify `reopen-current` or `reactivate-earlier`. The evidence is already strong enough to classify the main weaknesses cleanly, and no earlier checkpoint was invalidated by the findings.
- [e:r:i] It also does not justify the “mostly process/doctrine, avoid Checkpoint 5” branch. The runtime-authoritative `.toml` worker drift and the portable-GSD reproducibility defects are too concrete to be waved away as mere wording or review-practice cleanup.
- [e:r:i] The portable-GSD defects need one more qualification: they do not all belong inside the bounded pre-rerun checkpoint. The branch only justifies Checkpoint 5 because some harness ownership problems are real now; it does not justify silently importing every later hardening opportunity into that checkpoint.
- [e:r:i] So the branching logic points to: `open a bounded Checkpoint 5`.

## Regression Pressure Check

- [e:r:i] `Governance-doc regressions`: this verdict does not reopen the old trap of trying to solve everything with more docs. It explicitly says docs alone are insufficient at the current runtime-authority seams. Sources: `.planning/readiness/phase-01-rerun/PLAN.md:516-527`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-cross-lane-seam-synthesis.md:32-35`.
- [e:r:i] `Delegation / orchestration regressions`: this verdict reinforces, rather than weakens, the repo’s launch-truth discipline. It treats requested runtime settings and human-facing shadow docs as insufficient proof of actual worker behavior. Sources: `.planning/readiness/phase-01-rerun/PLAN.md:537-547`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-codex-load-bearing-surfaces-and-seams.md:48,62-66`.
- [e:r:i] `Git / checkpoint regressions`: the checkpoint should still be committed before any harness modifications. The audit bundle is now a coherent reviewable unit, and the plan explicitly requires that boundary. Sources: `.planning/readiness/phase-01-rerun/GATES/checkpoint-4.md:49-51`; `.planning/readiness/phase-01-rerun/PLAN.md:406-407,551-554`.
- [e:r:i] `Phase 01 rerun regressions`: proceeding straight to Checkpoint 6 or 7 would risk rerunning Phase 01 on top of unresolved runtime-authority and closure-pressure weaknesses that this audit has now made explicit. That would violate the plan’s rule against starting the rerun while unresolved governance/process cleanup can materially distort planning quality. Sources: `.planning/readiness/phase-01-rerun/PLAN.md:132-145,437-470,556-562`.
- [e:r:i] `Branch/worktree seam`: current disposition is `accepted bounded risk`, not silent closure. If Checkpoint 5 changes worktree/config behavior or Checkpoint 6 finds rerun-prep ambiguity there, reactivate the seam explicitly rather than pretending this audit settled it. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-cross-lane-seam-synthesis.md:24-31,49`.

## Checkpoint 5 Decision

- [d:r:i] `open a bounded Checkpoint 5`
- [e:r:i] The bounded scope should center on the cleanest ownership stories already proved here:
  - align the phase-critical runtime-authoritative `.toml` worker prompts with the repo’s actual instruction and skill surfaces
  - add a bounded review/closure-pressure follow-through on the harness surfaces that currently encode advisory or debt-carrying progression semantics
  - decide which launch-truth and model-truth surfaces need explicit durable capture versus protocol-only discipline
- [e:r:i] The bounded scope should explicitly defer broader install pinning, provenance cleanup, and path-portability hardening unless Checkpoint 5 touches reinstall/materialization surfaces directly or proves those issues are still rerun-blocking in the current live checkout.
- [e:r:i] It should not widen into a full harness redesign, a broad product rethink, or indiscriminate automation of judgment-heavy review semantics. Many remaining weaknesses are still better handled as protocol/doctrine improvements rather than machinery.
- [e:r:i] Stopping rule for Checkpoint 5:
  - the phase-critical worker authority surface is aligned for the roles the rerun will actually exercise
  - review/closure protocol changes explicitly preserve lone strong criticism and distinguish clean completion from debt-carrying completion where the rerun depends on that distinction
  - launch/model-truth capture has a clear, reviewable rule for doctrine-sensitive worker launches
  - broader portability/provenance hardening is either completed because the checkpoint touched those surfaces directly, or explicitly deferred as later hardening
- [e:r:i] The under-evidenced branch/worktree seam should remain visible as an accepted bounded risk, but it is not strong enough to become the centerpiece of Checkpoint 5 unless a narrower follow-up proves it materially defective.

## Readiness Handoff

- [e:r:i] Checkpoint 4 is ready for review. The artifact set now supports a defensible statement of both what is already strong and why a bounded Checkpoint 5 is still justified.
- [e:r:i] The correct next sequence is:
  1. rereview the revised Checkpoint 4 bundle under the strengthened readiness review policy
  2. if review accepts the bounded-Checkpoint-5 verdict, checkpoint the audit bundle
  3. then open Checkpoint 5 as a narrowly scoped harness follow-through rather than an omnibus redesign
