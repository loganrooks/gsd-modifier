# Checkpoint 5 R5.17b Chain-Tail Exclusion Audit Internal R1

## Research Frame

- Mode: `synthesis` plus `gap exposure / completeness challenge`
- Question: whether prior exclusions of chain-tail, representation, routing, and downstream-consumer surfaces survive direct reread of the candidate files themselves
- Scope: the 11 candidate targets in `checkpoint-5-r5-17b-chain-tail-exclusion-audit-spec.md`, plus follow-and-mark spot checks of `execute-phase.md`, `verify-work.md`, `commands.cjs`, and `templates/summary.md` only where candidate authority or read-set adequacy could not otherwise be judged honestly
- Non-goals: patch design, final `R5.17d` adjudication, wrapper-lane resolution, or governance-lane resolution
- Stop condition: classify which exclusions fail, which remain contested, and which can still be defended without violating the package's anti-regret rule

## Path Of Inquiry

- Entry point: reread the lane spec, `GATES/checkpoint-5.md`, `checkpoint-5-workflow-follow-through-implementation-spec.md`, and the completed `R5.16b` / `R5.16c` / `R5.16d` artifacts before touching the candidate files.
- Branches considered: producer contract surfaces; verifier/override status surfaces; routing-authority surfaces; later chain-tail consumers.
- Branches pursued: all 11 candidate files in the `R5.17b` spec.
- Branches followed-and-marked: `execute-phase.md`, `verify-work.md`, `commands.cjs`, and `templates/summary.md`, because the candidate-file meaning could not be judged honestly without them.
- Branches deferred: wrapper-family questions belong to `R5.17a`; governance/naming questions belong to `R5.17c`.
- Unexpected branches / reframings: `checkpoints.md` is loaded by `execute-phase.md`, so it is not a free-floating reference file; `commands.cjs` already contains debt-aware vocabulary, which sharpens the problem from "missing concept" to "non-authoritative concept."

## Assumptions Surfaced

- [a:r:i] This lane is judging exclusion survivability, not selecting the final patch ordering. A file can therefore fail exclusion without automatically becoming a same-wave edit.
- [a:r:i] Read-set adequacy is part of the lane's job, so bounded follow-and-mark expansion is warranted when a candidate file delegates or depends on omitted authority surfaces.
- [g:c:i] Non-promotion is not a neutral default; continued exclusion has to explain why it does not knowingly export cheap-closure semantics downstream. Sources: `.planning/readiness/phase-01-rerun/POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md:134-140`; `.planning/readiness/phase-01-rerun/AUDIT-COMPARISON-POLICY.md:89-95`.

## Invalid Exclusions

1. [e:c+r:i] Excluding `agent-contracts.md` and `gsd-executor.toml` as `representation-only` or `not the primary seam` fails on direct reread. `plan-phase.md` and `execute-phase.md` both load `agent-contracts.md`; the Planner -> Executor contract has no review-feedback carrier; the Executor -> Verifier contract frontmatter has no `status`, `completion_mode`, or debt-bearing field; `gsd-executor.toml` instructs the executor to write SUMMARY metadata plus only a `PASSED` / `FAILED` self-check; and `templates/summary.md` has no structured debt-bearing carrier either. These are producer-authority surfaces, not passive tail docs. Sources: `.codex/get-shit-done/workflows/plan-phase.md:5-13`; `.codex/get-shit-done/workflows/execute-phase.md:26-32`; `.codex/get-shit-done/references/agent-contracts.md:59-77`; `tooling/portable-gsd/overlay/agents/gsd-executor.toml:360-399,414-430`; `.codex/get-shit-done/templates/summary.md:10-46`.

2. [e:c+r:i] Excluding `verification-overrides.md` and `gsd-verifier.toml` as `only reference` or `not runtime-authoritative` also fails. The override reference explicitly makes `PASSED (override)` count toward the passing score and permits overall `status: passed`; the verifier TOML hardcodes only `gaps_found | human_needed | passed` as terminal states and emits the same limited frontmatter schema. That pair is not a downstream restatement of status logic. It is the status logic. Sources: `.codex/get-shit-done/references/verification-overrides.md:106-121,204-226`; `tooling/portable-gsd/overlay/agents/gsd-verifier.toml:165-179,486-500,576-585`.

3. [e:c+r:i] Excluding `phase.cjs`, `roadmap.cjs`, `progress.md`, and `transition.md` as `downstream only`, `secondary surface`, or `can remain deferred` fails most strongly. `phase.cjs` scans for unresolved verification debt but converts it into non-blocking warnings before writing complete state; `roadmap.cjs` declares a phase `complete` when `summaryCount >= planCount` and then trusts the ROADMAP checkbox over disk evidence; `progress.md` says verification debt is `a WARNING, not a blocker` and routes `summaries = plans` to `Phase complete`; `transition.md` says outstanding verification items do not block transition and also contains an explicit `mark complete anyway` partial-completion path. Those are routing and closure authorities, not decorative chain tails. Sources: `.codex/get-shit-done/bin/lib/phase.cjs:771-824`; `.codex/get-shit-done/bin/lib/roadmap.cjs:176-195,223-229`; `.codex/get-shit-done/workflows/progress.md:168-203,342-440`; `.codex/get-shit-done/workflows/transition.md:77-99,161-178,629-649`.

4. [e:c+r:i] The direct reread also satisfies the implementation-spec condition that was previously left contested. The spec said chain-tail completion surfaces should widen if the chosen debt-carrying representation left them contradictory; the files above are contradictory on their face. This means the older `not yet forced by evidence` exclusion cannot stand unchanged. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md:89-101,112-115`; `.planning/readiness/phase-01-rerun/GATES/checkpoint-5.md:67-78,95-100`; sources in items 1-3 above.

## Under-Justified Exclusions

- [o:c+r:i] `checkpoints.md` whole-file exclusion is contested, not defensible. `execute-phase.md` loads it in the execution context and `execute-plan.md` explicitly routes checkpoint handling to it, so `just reference` is false. But the directly contradictory material is not uniform across the whole file: the main `checkpoint:human-verify` doctrine is blocking, while the generic auto-mode bypass rule and the TDD-specific `checkpoint:tdd-review` subsection are where the cheap-closure pressure appears. That means whole-file immediate promotion is too blunt, but whole-file exclusion is too cheap. Sources: `.codex/get-shit-done/workflows/execute-phase.md:481-485`; `.codex/get-shit-done/workflows/execute-plan.md:271-281`; `.codex/get-shit-done/references/checkpoints.md:1-11,16-37,762-789`.

- [o:c+r:i] `autonomous.md` exclusion is also contested rather than cleanly defensible. The file filters future work by `disk_status !== "complete" || roadmap_complete === false`, then offers `Continue without validation`, `Continue without fixing`, and `Continue anyway`. That is real downstream closure authority, not inert later documentation. The only thing stopping it from becoming an automatic first-wave edit target is checkpoint boundedness: `Checkpoint 5` is framed around rerun-critical discuss/plan/execute follow-through rather than autonomous milestone driving. If parked, it must be parked explicitly as live downstream debt. Sources: `.codex/get-shit-done/workflows/autonomous.md:90-92,411-472,821-823`; `.planning/readiness/phase-01-rerun/GATES/checkpoint-5.md:53-78`.

- [o:c+r:i] `ship.md` exclusion is under-justified for the same reason, though the case is narrower. `ship.md` is farther downstream than the rerun itself, but it still treats `status: passed` or `status: human_needed` with human approval as ship-ready. That means the file can be deferred only as a named downstream contradiction if Checkpoint 5 remains rerun-bound; it cannot be waved away as `not the primary seam`. Sources: `.codex/get-shit-done/workflows/ship.md:1-3,41-46`; `.planning/readiness/phase-01-rerun/GATES/checkpoint-5.md:65-78`.

## Defensible Exclusions

- [d:c+r:i] No whole-file exclusion survives among the 11 candidate targets. Every candidate file either defines a producer contract, defines terminal verifier states, determines phase or milestone routing, or continues execution after debt is visible. Sources: `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-17b-chain-tail-exclusion-audit-spec.md:41-64`; direct spot checks below.

- [d:c+r:i] Only narrow deferrals survive, and they survive as downstream-wave deferrals rather than as read exclusions:
  - `ship.md` can stay out of the first corrective patch wave only if Checkpoint 5 records it as a known downstream contradiction to revisit before any shipping lane relies on current status semantics. Sources: `.codex/get-shit-done/workflows/ship.md:41-46`; `.planning/readiness/phase-01-rerun/GATES/checkpoint-5.md:65-78`.
  - The TDD-only `checkpoint:tdd-review` subsection inside `checkpoints.md` can stay out of the first corrective patch wave if `workflow.tdd_mode` is not active in the rerun path, but the file itself cannot be treated as irrelevant because the generic checkpoint doctrine and auto-mode bypass rules are already loaded by execution surfaces. Sources: `.codex/get-shit-done/references/checkpoints.md:1-11,762-789`; `.codex/get-shit-done/workflows/execute-phase.md:481-485`.

## Presumptive Edit Targets

- [d:c+r:i] If `R5.17` promotes corrective follow-through, the presumptive first-wave chain-tail set is:
  - `tooling/portable-gsd/overlay/agents/gsd-verifier.toml`
  - `.codex/get-shit-done/references/verification-overrides.md`
  - `.codex/get-shit-done/references/agent-contracts.md`
  - `tooling/portable-gsd/overlay/agents/gsd-executor.toml`
  - `.codex/get-shit-done/bin/lib/phase.cjs`
  - `.codex/get-shit-done/bin/lib/roadmap.cjs`
  - `.codex/get-shit-done/workflows/progress.md`
  - `.codex/get-shit-done/workflows/transition.md`

  These are the minimum surfaces where exclusion would knowingly export cheap-closure semantics after direct reread. The first four own signal production; the latter four own routing and completion authority. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md:89-101,112-115`; `.planning/readiness/phase-01-rerun/GATES/checkpoint-5.md:67-78,95-100`; direct spot checks in this artifact.

## Mandatory Disposition Targets

- [d:c+r:i] `checkpoints.md`, `ship.md`, and `autonomous.md` must not silently disappear again in `R5.17d` or any later `R5.18` scope note. Each now needs one of two explicit dispositions: patch now, or park as a bounded-risk contradiction with a named trigger for reopening. `secondary surface` is no longer an adequate disposition for any of the three. Sources: direct spot checks in this artifact; `.planning/readiness/phase-01-rerun/POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md:134-140`; `.planning/readiness/phase-01-rerun/AUDIT-COMPARISON-POLICY.md:89-95`.

- [d:c+r:i] The lane also exposed missing-but-material surfaces that future adjudication should treat as mandatory spot checks, even though the `R5.17b` candidate list did not enumerate them:
  - `.codex/get-shit-done/workflows/verify-work.md` auto-runs the transition path when issues are zero and offers `Proceed anyway?` when open artifacts remain, so `transition.md` cannot be judged honestly without it. Sources: `.codex/get-shit-done/workflows/verify-work.md:415-459,473-483`.
  - `.codex/get-shit-done/bin/lib/commands.cjs` already distinguishes `Complete`, `Needs Review`, and `Executed`, which proves the harness has better status vocabulary but has not made it authoritative in routing. Sources: `.codex/get-shit-done/bin/lib/commands.cjs:12-35`.
  - `.codex/get-shit-done/workflows/execute-phase.md` sends `human_needed` to `update_roadmap` on bare approval, so downstream consumers cannot be judged apart from that producer handoff. Sources: `.codex/get-shit-done/workflows/execute-phase.md:1263-1375`.
  - `.codex/get-shit-done/templates/summary.md` is the concrete payload carrier paired with `agent-contracts.md` and `gsd-executor.toml`; omitting it reintroduces the false split between contract and representation. Sources: `.codex/get-shit-done/templates/summary.md:10-46`.

## Direct Spot Checks

- [e:c:i] `agent-contracts.md` defines the Planner -> Executor and Executor -> Verifier contracts, but the latter still requires only `phase, plan, subsystem, tags, key-files, metrics`, `Deviations`, and `Self-Check`, with no structured debt-bearing field. Sources: `.codex/get-shit-done/references/agent-contracts.md:59-77`.

- [e:c:i] `verification-overrides.md` explicitly states that `PASSED (override)` counts toward passing and that a phase with only `VERIFIED` / `PASSED (override)` items can still have `status: passed`; `gsd-verifier.toml` then hardcodes only `gaps_found | human_needed | passed` as terminal states. Sources: `.codex/get-shit-done/references/verification-overrides.md:106-121,204-226`; `tooling/portable-gsd/overlay/agents/gsd-verifier.toml:486-500,576-585`.

- [e:c:i] `phase.cjs` detects partial UAT, `human_needed`, and `gaps_found`, but records them only as warnings before updating the ROADMAP checkbox and progress row to `Complete`. Sources: `.codex/get-shit-done/bin/lib/phase.cjs:771-824`.

- [e:c:i] `roadmap.cjs` derives `disk_status = 'complete'` from `summaryCount >= planCount` and then explicitly trusts the ROADMAP checkbox over disk evidence when they disagree. Sources: `.codex/get-shit-done/bin/lib/roadmap.cjs:176-195`.

- [e:c:i] `progress.md` warns about verification debt but says routing proceeds normally, then routes `summaries = plans` to `Phase complete` and next-phase or milestone-complete suggestions. Sources: `.codex/get-shit-done/workflows/progress.md:168-203,342-440`.

- [e:c:i] `transition.md` says outstanding verification items do not block transition, auto-approves in yolo mode, and separately offers a `mark complete anyway` path when plans are incomplete. Sources: `.codex/get-shit-done/workflows/transition.md:77-99,101-112,629-649`.

- [e:c:i] `ship.md` closes the plan -> execute -> verify -> ship loop and treats `status: human_needed` with human approval as ship-ready. Sources: `.codex/get-shit-done/workflows/ship.md:1-3,41-46`.

- [e:c:i] `autonomous.md` filters phases by `disk_status !== "complete" || roadmap_complete === false` and offers `Continue without validation`, `Continue without fixing`, and `Continue anyway` branches, so it compounds any earlier cheap-completion state rather than merely echoing it. Sources: `.codex/get-shit-done/workflows/autonomous.md:90-92,411-472,821-823`.

- [e:c+i] `checkpoints.md` is mixed rather than uniformly bad: it still presents `checkpoint:human-verify` as blocking, but it also contains a generic auto-mode checkpoint bypass rule and an advisory/auto-approving `checkpoint:tdd-review` subsection. Sources: `.codex/get-shit-done/references/checkpoints.md:1-11,16-37,762-789`.

## Dependencies And Relations

| Item | Depends on | Constrains or affects | Vulnerability |
| --- | --- | --- | --- |
| Producer contract cluster (`agent-contracts.md`, `gsd-executor.toml`, `summary.md`) | planner / executor handoff rules | whether debt can be emitted mechanically at all | high |
| Verifier status cluster (`verification-overrides.md`, `gsd-verifier.toml`) | override semantics, terminal-state vocabulary | whether accepted deviation collapses into `passed` | high |
| Routing authority cluster (`phase.cjs`, `roadmap.cjs`, `progress.md`, `transition.md`) | emitted completion state plus roadmap updates | whether debt is blocking, warning-only, or invisible in forward motion | high |
| Late chain-tail cluster (`checkpoints.md`, `ship.md`, `autonomous.md`) | earlier status/routing decisions | whether cheap closure keeps propagating after the first authority surfaces | medium-high |

## Scope Expansions And Deferrals

- Follow-and-mark: `execute-phase.md`, `verify-work.md`, `commands.cjs`, and `templates/summary.md` had to be read because the candidate-file set alone could not answer the lane's own read-set adequacy question honestly.
- Defer: wrapper-family questions remain with `R5.17a`; doctrine-vocabulary questions remain with `R5.17c`; broad portability / provenance / branch-worktree concerns remain deferred because this pass did not need them to surface the contradiction set.
- Revisit later: exact ordering for `ship.md`, `autonomous.md`, and the contested parts of `checkpoints.md` should be decided in `R5.17d`, not silently assumed here.

## Package Consequences

- [d:c+r:i] `R5.17d` should treat the core contract/routing exclusions as failed, not merely pressured. The direct reread now satisfies the implementation-spec condition for widening: the chosen debt-carrying boundary leaves downstream consumers contradictory on their face. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md:98-101,112-115`; direct spot checks above.

- [d:c+r:i] `R5.17d` and `R5.17e` should not let `checkpoints.md`, `ship.md`, or `autonomous.md` drop out through distance-based deferral language. If any of them stays out of the first corrective patch wave, the exclusion must be recorded as an accepted bounded-risk contradiction, not as absence of evidence. Sources: `.planning/readiness/phase-01-rerun/POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md:134-140`; `.planning/readiness/phase-01-rerun/AUDIT-COMPARISON-POLICY.md:89-95`; direct spot checks above.

- [d:c+r:i] The `R5.17b` candidate list was useful but not sufficient by itself. Future adjudication should treat `execute-phase.md`, `verify-work.md`, `commands.cjs`, and `templates/summary.md` as required spot-check surfaces whenever chain-tail exclusion is being judged. Otherwise the package will still under-read authority distribution. Sources: `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-17b-chain-tail-exclusion-audit-spec.md:63-64`; `.planning/readiness/phase-01-rerun/POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md:93-99`; direct spot checks above.

- [d:c+r:i] No evidence from this pass forces broader portability, provenance, or branch/worktree expansion. The exclusion failure is specific to contract, status, and routing authority. That matters because it preserves the checkpoint's bounded-scope discipline while still rejecting cheap locality claims. Sources: `.planning/readiness/phase-01-rerun/GATES/checkpoint-5.md:79-83`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md:118-121`.

## What Can Close Now

- [d:c+r:i] The earlier exclusion heuristics fail for the core chain-tail cluster. `not the primary seam`, `secondary surface`, and `can remain deferred` do not survive direct reread of `agent-contracts.md`, `verification-overrides.md`, `gsd-executor.toml`, `gsd-verifier.toml`, `phase.cjs`, `roadmap.cjs`, `progress.md`, and `transition.md`.

- [d:c+r:i] The implementation-spec's older contested chain-tail boundary should now be treated as reactivated, not hypothetical. The direct contradiction evidence is strong enough that `R5.17d` can no longer leave those files in a generic "only if later forced" bucket.

## What Must Stay Open

- [o:c+r:i] Whether `ship.md` and `autonomous.md` land in the first corrective wave or survive as explicitly parked bounded-risk contradictions.

- [o:c+r:i] Whether the problematic parts of `checkpoints.md` are best handled through a file-level update or a narrower subsection-level TDD / auto-mode disposition.

- [o:c+r:i] The exact debt-bearing representation mechanism remains a design choice. This pass establishes that the mechanism must become authoritative somewhere in the producer -> verifier -> routing chain; it does not decide the final field name or carrier. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md:98-101`.

## Sources

- Governing package doctrine:
  - `.planning/readiness/phase-01-rerun/GATES/checkpoint-5.md`
  - `.planning/readiness/phase-01-rerun/POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md`
  - `.planning/readiness/phase-01-rerun/AUDIT-COMPARISON-POLICY.md`
  - `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md`
- Prior comparison artifacts:
  - `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-16b-track-c-propagation-audit-internal-r1.md`
  - `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-16b-track-c-propagation-cross-vendor-opus-r1.md`
  - `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-16c-anti-regret-adjudication-r1.md`
  - `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-16c-anti-regret-adjudication-cross-vendor-opus-r1.md`
  - `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-16d-adjudication-reread-internal-r1.md`
  - `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-16d-adjudication-reread-cross-vendor-opus-r1.md`
- Direct candidate surfaces and read-set-expansion spot checks:
  - `.codex/get-shit-done/references/agent-contracts.md`
  - `.codex/get-shit-done/references/verification-overrides.md`
  - `.codex/get-shit-done/references/checkpoints.md`
  - `.codex/get-shit-done/bin/lib/phase.cjs`
  - `.codex/get-shit-done/bin/lib/roadmap.cjs`
  - `.codex/get-shit-done/workflows/progress.md`
  - `.codex/get-shit-done/workflows/transition.md`
  - `.codex/get-shit-done/workflows/ship.md`
  - `.codex/get-shit-done/workflows/autonomous.md`
  - `tooling/portable-gsd/overlay/agents/gsd-executor.toml`
  - `tooling/portable-gsd/overlay/agents/gsd-verifier.toml`
  - `.codex/get-shit-done/workflows/execute-phase.md`
  - `.codex/get-shit-done/workflows/verify-work.md`
  - `.codex/get-shit-done/bin/lib/commands.cjs`
  - `.codex/get-shit-done/templates/summary.md`
