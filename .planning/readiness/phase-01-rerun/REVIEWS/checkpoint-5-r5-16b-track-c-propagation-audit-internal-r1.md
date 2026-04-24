# Checkpoint 5 R5.16b Track C Propagation Audit Internal R1

## Research Frame

- Mode: `synthesis` plus `gap exposure / completeness challenge`
- Question: whether the current Track C bundle propagates honest launch-truth, closure-status, and debt-carrying-completion semantics into the consumers that actually decide completion and forward motion
- Scope: the Track C candidate surfaces, the listed downstream consumers, and narrowly expanded chain-tail consumers when the listed read set proved inadequate to judge locality honestly
- Non-goals: patch design, final `R5.16c` adjudication, or broader portability/provenance hardening
- Stop condition: determine whether the current Track C bundle is closure-ready evidence and classify the strongest surviving propagation gaps

## Path Of Inquiry

- Entry point: `WORKFLOW.md`, `AI-GUARDRAILS.md`, `capture_launch_truth.py`, the executor/verifier overlays, and the listed `execute-phase` / `verify-work` / `progress` consumers
- Branches pursued: requested-versus-effective launch capture; `human_needed` completion routing; override-backed completion; progress/current-phase routing; debt-audit surfaces
- Branches followed-and-marked: `transition.md`, `ship.md`, and `autonomous.md` after the listed consumer chain proved insufficient to test non-promotion honestly
- Branches deferred: broader wrapper-family reread beyond directly contradictory surfaces, and non-Track-C portability/provenance lanes

## Verdict

- [e:c+r:i] `Track C is not closure-ready.` The launch-truth doctrine itself is materially stronger, but the surviving propagation failures are still blocking on completion semantics: unresolved human verification, override-backed deviations, and acknowledged debt still collapse into ordinary phase completion or ordinary next-step routing in live consumers. Non-promotion to a wider chain-tail lane is not yet defensible on the current evidence. Sources: `.planning/readiness/phase-01-rerun/GATES/checkpoint-5.md:82-91`; `.planning/readiness/phase-01-rerun/STATUS.md:92-114`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md:98-100,114-130`; `.codex/get-shit-done/workflows/execute-phase.md:1263-1375`; `.codex/get-shit-done/workflows/progress.md:168-203,342-440`; `.codex/get-shit-done/references/verification-overrides.md:95-123`.
- [d:r:i] Disposition: `reopen-current` for Track C and carry these findings into `R5.16c` as blocking anti-regret evidence rather than treating the current patch set as closure-ready.

## Blocking Propagation Gaps

1. [e:c+r:i] The `human_needed` path in `execute-phase` still converts unresolved manual verification into formal phase completion. The workflow writes `*-HUMAN-UAT.md` with `status: partial`, tells the user that the debt will remain visible later, and then on a bare `"approved"` response proceeds directly to `update_roadmap`; the `phase complete` command then records the debt only as non-blocking warnings while still writing `Complete` into ROADMAP state. This directly contradicts the active Checkpoint 5 requirement that clean completion and debt-carrying completion stay distinct where rerun quality depends on that distinction. Sources: `.codex/get-shit-done/workflows/execute-phase.md:1263-1321,1347-1375`; `.codex/get-shit-done/bin/lib/phase.cjs:771-789,792-824`; `.planning/readiness/phase-01-rerun/GATES/checkpoint-5.md:82-91`; `.planning/readiness/phase-01-rerun/STATUS.md:92-114`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md:98-100`.

2. [e:c+r:i] Override-backed deviations still collapse into clean verified closure instead of a debt-bearing completion state. The override reference and verifier instructions explicitly say `PASSED (override)` counts toward the passing score and can still yield frontmatter `status: passed`; downstream status and audit consumers then treat `passed` as `Complete` while only `human_needed` and `gaps_found` are surfaced as open debt. That means intentional but still debt-carrying deviations disappear from the phase-status, progress, and audit trail that real consumers use. Sources: `.codex/get-shit-done/references/verification-overrides.md:95-123,204-226`; `tooling/portable-gsd/overlay/agents/gsd-verifier.toml:176-179,486-500,582-585,697-718`; `.codex/get-shit-done/bin/lib/commands.cjs:12-35`; `.codex/get-shit-done/bin/lib/phase.cjs:785-789`; `.codex/get-shit-done/bin/lib/audit.cjs:463-466`; `.codex/get-shit-done/bin/lib/uat.cjs:53-70,211-251`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md:98-100,114`.

3. [e:c+r:i] The primary progress/status consumer still routes debt-carrying phases as complete and next-step ready. `progress.md` treats cross-phase verification debt as a warning only, then routes `summaries = plans` to "Phase complete"; `roadmap.cjs` separately treats `summaryCount >= planCount` as `complete` and even trusts a roadmap checkbox over disk evidence. Once any completion path checks the roadmap box, the main progress surface will push toward the next phase or milestone while the previous phase's debt is relegated to a warning banner. Sources: `.codex/get-shit-done/workflows/progress.md:168-203,342-440`; `.codex/get-shit-done/bin/lib/roadmap.cjs:176-195,223-229`; `.codex/get-shit-done/bin/lib/phase.cjs:771-789,792-824`; `.planning/readiness/phase-01-rerun/GATES/checkpoint-5.md:84-91`.

4. [e:c+r:i] `verify-work` still preserves a cheap acknowledge-and-continue completion path instead of a closure-resistant one. When issues are zero it auto-transitions to phase completion; when open artifacts remain it asks only "Proceed anyway?" and records acknowledged gaps rather than enforcing a stronger closure category. The actual downstream `transition.md` consumer then states that outstanding verification items "do NOT block transition" and in yolo mode auto-approves completion anyway. Sources: `.codex/get-shit-done/workflows/verify-work.md:413-459,461-483`; `.codex/get-shit-done/workflows/transition.md:77-99,101-110,161-176`; `.planning/readiness/phase-01-rerun/POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md:115-120,150-156`.

## Local But Important Gaps

- [e:c+r:i] The launch-truth helper is still boundary-scoped rather than launch-identity-scoped. `capture_launch_truth.py` selects all worker rows after a `--since` boundary, compares requested model/reasoning/approval/sandbox across that whole set, and explicitly admits that `requested_agent` is operator intent only. That is honest and much better than the old ambient-memory rule, but it still supports "rows after this boundary matched" more strongly than "this exact requested worker definitely launched." Sources: `tooling/codex/capture_launch_truth.py:159-193,204-232,328-368`; `WORKFLOW.md:71-82`; `AI-GUARDRAILS.md:89-91`.

- [e:c+r:i] The chosen representation boundary for debt-carrying completion is still not mechanically visible in the executor/summary/reference contract. Executor and summary surfaces still speak in plain completion language, and the agent-contract reference still requires summary completeness/self-check rather than any explicit debt-bearing marker. That leaves downstream consumers reconstructing debt from warnings and side-channel artifacts instead of from a first-class contract field. Sources: `tooling/portable-gsd/overlay/agents/gsd-executor.toml:361-399,432-489,494-520`; `.codex/get-shit-done/templates/summary.md:1-50,65-76`; `.codex/get-shit-done/references/agent-contracts.md:70-78`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md:98-100`.

## Signals That The Problem May Already Be Wider

- [e:c+r:i] The listed Track C read set was not enough to judge locality responsibly. The audit had to expand into `transition.md`, where outstanding verification debt is explicitly non-blocking and yolo mode auto-approves completion. That is already a load-bearing chain-tail consumer outside the original list. Sources: `.codex/get-shit-done/workflows/transition.md:77-99,101-110,161-176`.

- [e:c+r:i] Adjacent orchestration/ship surfaces already preserve the same cheap-closure semantics. `ship.md` accepts `status: human_needed` with human approval as ship-ready, and `autonomous.md` allows "Continue without validation" for `human_needed` and "Continue anyway" for `gaps_found`, then proceeds onward. This is evidence of propagation beyond the narrow `execute-phase` / `verify-work` / `progress` trio. Sources: `.codex/get-shit-done/workflows/ship.md:41-46`; `.codex/get-shit-done/workflows/autonomous.md:411-429,461-478`.

- [e:c+r:i] The status/debt semantics are already distributed across multiple command libraries rather than living in one local workflow file. `phase.cjs`, `roadmap.cjs`, `commands.cjs`, `audit.cjs`, and `uat.cjs` all encode part of the closure/debt story. That spread makes the "keep it local" judgment a positive claim that now needs stronger justification than the current candidate bundle provides. Sources: `.codex/get-shit-done/bin/lib/phase.cjs:771-789,792-824`; `.codex/get-shit-done/bin/lib/roadmap.cjs:176-195,223-229`; `.codex/get-shit-done/bin/lib/commands.cjs:12-35`; `.codex/get-shit-done/bin/lib/audit.cjs:463-466`; `.codex/get-shit-done/bin/lib/uat.cjs:53-70,211-251`.

## What Is Already Strong

- [e:c:i] The launch-truth doctrine is materially better than the pre-rerun baseline. The governing docs now explicitly distinguish requested settings, effective sqlite truth, and unresolved runtime fields, and the helper script preserves that distinction in its rendered assessment instead of pretending to prove more than it can. Sources: `WORKFLOW.md:71-82`; `AI-GUARDRAILS.md:89-91`; `tooling/codex/capture_launch_truth.py:204-232,328-368`.

- [e:c+r:i] Some downstream machinery already has the beginnings of the right vocabulary. `commands.cjs` distinguishes `Complete`, `Needs Review`, and `Executed`; `phase.cjs` emits explicit warning arrays; and `progress.md` can surface cross-phase verification debt visibly. The core failure is incomplete propagation and non-blocking treatment, not total absence of status language. Sources: `.codex/get-shit-done/bin/lib/commands.cjs:12-35`; `.codex/get-shit-done/bin/lib/phase.cjs:771-789,1038-1040`; `.codex/get-shit-done/workflows/progress.md:168-192`.

- [g:c:i] The Track C spec is asking the right anti-regret question by requiring chain-tail scrutiny, read-set adequacy testing, and explicit locality/non-promotion challenge rather than assuming the current patch is local by default. Sources: `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-16b-track-c-propagation-audit-spec.md:52-65`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-16-propagation-audit-bundle-spec.md:68-77`.

## What Must Change Before Track C Can Count As Closure-Ready

- A `human_needed`, partial-UAT, acknowledged-open-artifact, or comparable debt-bearing phase must not call `phase complete`, `transition`, or ordinary "Phase complete" / next-phase routing unless that debt-bearing state is first-class and preserved downstream.

- Override-backed acceptance must stop collapsing into frontmatter `status: passed`. A distinct phase-level debt carrier is needed so `audit-uat`, `audit-open`, progress routing, shipping, and autonomous flows can still see the difference between clean verified closure and accepted deviation.

- Progress/current-phase/milestone routing must key on verification/debt semantics rather than plan/summary counts or roadmap checkbox trust alone.

- `verify-work`, `transition`, `ship`, and `autonomous` need reread-and-patch or an explicit contradiction note that keeps Track C open. Right now they are active chain-tail consumers, not optional future cleanup.

- If launch-truth capture remains boundary-based, mixed captures must stay non-certifying and the workflow must require explicit human interpretation of which rows belong to the intended launch.

## What Can Remain Local

- `capture_launch_truth.py` can remain a reviewable capture aid rather than a full provenance subsystem. The current requested/effective/unresolved framing is acceptable if downstream artifacts do not overclaim from it.

- Broader portability/provenance hardening can stay deferred. This audit did not need install pinning or archive/provenance changes to expose the current contradiction set.

- Wrapper alignment can remain secondary once the actual completion consumers are fixed. The strongest surviving Track C blockers are not primarily caused by skill-wrapper prose.

## Change Summary

- The launch-truth layer is directionally strong and mostly honest about its own limits.

- The blocking failures are downstream completion consumers: the `human_needed` completion shortcut, override flattening into `passed`, and progress/status routing that treats debt as warning-only carry-forward.

- Because omitted chain-tail consumers such as `transition`, `ship`, and `autonomous` already repeat the same cheap-closure logic, `R5.16c` should not accept a locality or non-promotion claim cheaply.
