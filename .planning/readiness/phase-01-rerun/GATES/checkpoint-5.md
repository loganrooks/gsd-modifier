# Checkpoint 5: Conditional Harness / GSD Follow-Through

Status: in progress
Last updated: 2026-04-16

## Objective

- execute the reactivated harness follow-through that Checkpoint 4 proved is warranted before rerun-readiness verification
- preserve the already-completed Track A/B/C work, but do not let that partial bundle stand in for the full checkpoint
- keep the checkpoint centered on rerun-blocking harness quality, not on omnibus hardening
- keep spec revision and implementation ownership auditable as separate moves rather than collapsing them into one patch wave

## Governing inputs

- [AUDITS/checkpoint-5-bounded-follow-through-launch-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-bounded-follow-through-launch-spec.md)
- [AUDITS/checkpoint-5-reactivated-launch-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-reactivated-launch-spec.md)
- [AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md)
- [AUDITS/checkpoint-5-r5-16-propagation-audit-bundle-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-16-propagation-audit-bundle-spec.md)
- [AUDITS/checkpoint-5-r5-17-exclusion-judgment-audit-bundle-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-17-exclusion-judgment-audit-bundle-spec.md)
- [POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md)
- [AUDITS/checkpoint-4-gsd-workflow-chain-and-artifact-contracts-excellence.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-gsd-workflow-chain-and-artifact-contracts-excellence.md)
- [AUDIT-COMPARISON-POLICY.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDIT-COMPARISON-POLICY.md)
- [REVIEWS/checkpoint-5-spec-stack-audit-comparison-ledger.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-spec-stack-audit-comparison-ledger.md)

## Current subphase

- complete: pre-implementation audit comparison and claim qualification
- complete: revise the governing implementation spec from convergent and supported claims, keeping contested and pressure-only claims explicit
- complete: fresh internal and cross-vendor reread of the revised implementation spec
- complete: `R5.16a` / `R5.16b` / `R5.16c` / `R5.16d`
  - the Track B / Track C propagation audits, anti-regret adjudication, and reread all exist as completed bundle evidence
- complete now: the package no longer treats `R5.17` as the old wider lane label
  - `R5.17` now means the exclusion-judgment audit bundle
  - `R5.18` now means the provisional promoted corrective boundary that must later govern the patch wave
  - `R5.19` now means the broader exclusion / modification-consideration challenge lane that runs before or alongside final `R5.18`, not downstream of it
- complete now: the full `R5.17` exclusion-judgment bundle exists on disk, including the split `d1/d2/d3/d4` adjudications and the internal plus cross-vendor rereads
- complete now: the split `R5.18` execution bundle exists from boundary-setting through review prep
  - use the clean cross-vendor `claude-opus-4-6[1m]` reread as the clean cross-vendor `R5.17e` artifact
  - treat the earlier non-`[1m]` Opus reread as preserved partial/overflowed evidence, not as the clean governing reread
  - the broader `R5.19` bundle was run because `R5.18` is itself the current modification frontier, so the package could not leave the broader exclusion question downstream of it
  - the `R5.19d/e` consequence layer is now carried forward as implemented truth:
    - `Bucket 1` stayed unchanged
    - non-first-wave live items now carry contradiction-ledger rows instead of ambient omission
    - broader remainder ownership is explicit under `R8.1` through `R8.4`
    - the exclusion heuristics remain barred from standing-doctrine status
  - execution artifacts now exist at:
    - [REVIEWS/checkpoint-5-r5-18a1-current-wave-boundary-and-ledger-decision-internal-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-18a1-current-wave-boundary-and-ledger-decision-internal-r1.md)
    - [REVIEWS/checkpoint-5-r5-18a2-later-lane-and-quiet-drop-adjudication-internal-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-18a2-later-lane-and-quiet-drop-adjudication-internal-r1.md)
    - [REVIEWS/checkpoint-5-r5-18b-review-planning-chain-launch-internal-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-18b-review-planning-chain-launch-internal-r1.md)
    - [REVIEWS/checkpoint-5-r5-18c-completion-routing-chain-launch-internal-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-18c-completion-routing-chain-launch-internal-r1.md)
    - [REVIEWS/checkpoint-5-r5-18d-integration-and-review-prep-launch-internal-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-18d-integration-and-review-prep-launch-internal-r1.md)
  - launch-spec governance remains preserved at:
    - [AUDITS/checkpoint-5-r5-18-launch-bundle-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18-launch-bundle-spec.md)
    - [AUDITS/checkpoint-5-r5-18d-integration-and-review-prep-launch-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18d-integration-and-review-prep-launch-spec.md)
- active now: run the internal and cross-vendor checkpoint review on the coherent `R5.18` patch bundle rather than treating `18b` and `18c` as isolated slices

## Activation Criteria

- Checkpoint 4 concluded that:
  - the phase-critical runtime-authoritative worker surface still carries stale doctrine
  - review / closure pressure is still too soft for the rerun standard
  - launch/model-truth capture remains too implicit for later audit
  - workflow-chain follow-through is still needed on steering translation, research adequacy, permissive closure, and clean-versus-debt-carrying completion

## Likely Targets

- phase-critical registered `.toml` worker prompts under [.codex/agents](/home/rookslog/workspace/projects/prix-guesser/.codex/agents)
- repo-local GSD workflow / review / completion surfaces under [.codex/get-shit-done](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done), especially:
  - [.codex/get-shit-done/workflows/discuss-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/discuss-phase.md)
  - [.codex/get-shit-done/workflows/research-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/research-phase.md)
  - [.codex/get-shit-done/workflows/plan-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/plan-phase.md)
  - [.codex/get-shit-done/workflows/execute-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/execute-phase.md)
- repo-local overlay under `tooling/portable-gsd/overlay/` only where the bounded follow-through truly requires it
- rerun-critical wrappers under [.codex/skills](/home/rookslog/workspace/projects/prix-guesser/.codex/skills) only as a secondary alignment surface after workflow changes land
- [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md) only where a doc-level policy needs explicit machinery-backed protocol

## Bounded Scope

- required:
  - align the phase-critical runtime-authoritative `.toml` worker prompts with the repo’s actual instruction and skill surfaces
  - tighten review / closure-pressure harness surfaces so lone strong criticism and debt-carrying completion are handled more explicitly
  - make the repo-local GSD review/audit consumption surfaces encode the stronger readiness posture:
    - strongest justified criticism
    - merely adequate but not strong enough
    - later-audit risk
    - lone high-signal criticism that must be answered on the merits rather than ignored for lack of consensus
    - synthesis that does not flatten disagreement into false consensus
  - define the durable rule for launch/model-truth capture on doctrine-sensitive worker launches
  - add workflow-chain follow-through on steering-to-plan traceability, research adequacy/disposition, doctrine-sensitive closure pressure, and clean-versus-debt-carrying completion
  - align rerun-critical wrappers where the invocation surface would otherwise lag the corrected workflow doctrine
- explicitly deferred unless the active work reaches those surfaces directly:
  - broad install pinning
  - archival provenance replacement
  - full path-portability hardening
  - broader branch/worktree redesign

## Exit Criteria

- the revised Checkpoint 5 implementation spec passes fresh internal and cross-vendor reread under the audit comparison policy
- the completed `R5.16` propagation bundle is treated as settled checkpoint evidence, not as still-pending work
- the current `R5.17` exclusion-judgment bundle then completes and passes review:
  - `R5.17a` wrapper-exclusion audit
  - `R5.17b` chain-tail / downstream-consumer exclusion audit
  - `R5.17c` governance / doctrine exclusion audit
  - `R5.17d` adjudication of those exclusion lanes
  - `R5.17e` reread of that adjudication
- the executed `R5.18` patch bundle must pass fresh internal and cross-vendor review against the accepted spec
- review must confirm that `R5.18a1` contradiction-ledger rows actually governed `R5.18b/c` scope and that no kept-out live item is still governing by silence
- review must confirm that `R8.1` through `R8.4` remain explicit later-lane ownership rather than implied closure from adjacent current-wave fixes
- review must confirm that router-pair asymmetry is either paired or explicitly defended, authority-shelter did not suppress downstream semantic-uptake obligations, and the exclusion heuristics did not re-enter as standing doctrine
- the phase-critical worker authority surface, review/closure posture, and debt-aware completion routing remain aligned for the rerun paths the checkpoint actually exercises
- broader portability/provenance hardening and branch/worktree redesign remain either explicitly deferred or reactivated only by their stated triggers

## Quality Questions

- are these real harness defects with clean ownership stories?
- are we moving only the controls that genuinely improve reliability?
- are we keeping broader hardening explicit instead of smuggling it into the pre-rerun checkpoint?
- are we carrying forward the accepted Checkpoint 4 workflow findings rather than silently dropping them because the initial Checkpoint 5 launch spec was narrower?
- are we treating exclusion as a burden-bearing claim rather than a neutral default?
- are we letting `thin wrapper`, `secondary surface`, or `not runtime-authoritative` do scope work they have not earned?

## Review Note

- the existing Checkpoint 5 internal and cross-vendor reviews apply only to the pre-reactivation partial bundle
- the spec-stack audit bundle also showed that the widened implementation spec itself required revision before implementation
- closure of the reactivated checkpoint therefore now requires:
  - the already-satisfied revised-spec rereads
  - the already-completed `R5.16` propagation bundle
  - the already-completed `R5.17` exclusion-judgment bundle
  - the executed `R5.18a1/a2/b/c/d` corrective bundle
  - then fresh internal and cross-vendor review of the resulting implementation patch set against the accepted spec, using `R5.18d` as the integration entrypoint
- the fresh reread requirement for the revised implementation spec is now satisfied by:
  - [REVIEWS/checkpoint-5-revised-implementation-spec-internal-review-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-revised-implementation-spec-internal-review-r1.md)
  - [REVIEWS/checkpoint-5-revised-implementation-spec-cross-vendor-opus-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-revised-implementation-spec-cross-vendor-opus-r1.md)
- the clean cross-vendor reread for `R5.17e` is now:
  - [REVIEWS/checkpoint-5-r5-17e-exclusion-adjudication-reread-cross-vendor-opus-1m-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-17e-exclusion-adjudication-reread-cross-vendor-opus-1m-r1.md)
- because much of the `.codex/*` runtime surface is repo-ignored or otherwise not available as a normal tracked diff here, review should use direct file-content inspection plus the recorded verification commands rather than tracked-path expectations alone

## Commit Rule

- keep harness changes separate from governance wording unless inseparable
