# Checkpoint 5 R5.18 Versus 2026-04-15 Governance Audit Comparison Internal R1

## Research Frame

- Mode: `synthesis`.
- Question: are the concern families exposed by the 2026-04-15 multilayer harness governance audit actually being addressed by the current Checkpoint 5 / `R5.18` boundary, launch bundle, and active readiness state?
- Scope: compare the historical bundle's exposed weak-side families against current Checkpoint 5 status, gate, split `R5.18` specs, `R5.19d4/e` consequence layer, and the current governing repo docs that now shape that frontier.
- Non-goals: no code-patch review, no rerun of the 2026-04-15 audit, no fresh whole-repo governance audit, no closure claims about `R5.18a/b/c/d` implementation that has not started.
- Stop condition: each major historical concern family is classified against current state as `addressed_in_r5_18`, `partially_addressed_boundary_only`, `deferred_with_owner`, `still_missing`, or `superseded`.
Assumptions surfaced:
- `addressed` means either `inside current governing doctrine` or `inside the live `R5.18` corrective frontier`; it does not mean `implemented and reviewed`.
- `current state` means what is ratified by `STATUS.md`, `TASKS.md`, `GATES/checkpoint-5.md`, `R5.18` boundary/launch artifacts, `R5.19d4/e`, and current governing docs, not hypothetical later cleanups.
- `major concern family` means the historical bundle's explicit weak-side families and externally pressured subfamilies, not every individual file recommendation.

## Path Of Inquiry

- Entry point: extract the historical weak-side map from `01`-`06` plus `08`, then compare that map against current `R5.18` boundary truth rather than against imagined future patches.
- Branches considered: lane-by-lane restatement; current-task-board restatement; file-overlap comparison; concern-family synthesis.
- Branches pursued: concern-family synthesis from the historical bundle, then mapping against current `STATUS` / `TASKS` / checkpoint gate / `R5.18a-d` / `R5.19d4/e` / governing-doc surfaces.
- Branches deferred or abandoned: raw `R5.19a/b/c` reread; code-level implementation-quality review; broader repo audit outside current Checkpoint 5.
- Unexpected branches / reframings: the live comparison is not `old recommendation versus completed fix`; it is `old concern family versus current bounded corrective frontier`, because `R5.18` execution has not started yet (`.planning/readiness/phase-01-rerun/STATUS.md:91-95,157-163,204-206`; `.planning/readiness/phase-01-rerun/TASKS.md:24`; `.planning/readiness/phase-01-rerun/GATES/checkpoint-5.md:45-72`).

## Artifacts Read

### Historical Concern Bundle
- `.planning/research/2026-04-15-multilayer-harness-governance-audit/00-launch-bundle-spec.md`
- `.planning/research/2026-04-15-multilayer-harness-governance-audit/01-codex-orchestration-layer-audit.md`
- `.planning/research/2026-04-15-multilayer-harness-governance-audit/02-gsd-lifecycle-and-long-arc-layer-audit.md`
- `.planning/research/2026-04-15-multilayer-harness-governance-audit/03-git-repo-operations-layer-audit.md`
- `.planning/research/2026-04-15-multilayer-harness-governance-audit/04-ci-release-and-deployment-layer-audit.md`
- `.planning/research/2026-04-15-multilayer-harness-governance-audit/05-cross-layer-integration-and-escalation-audit.md`
- `.planning/research/2026-04-15-multilayer-harness-governance-audit/06-converged-synthesis.md`
- `.planning/research/2026-04-15-multilayer-harness-governance-audit/08-external-comparative-governance-research.md`

### Current Readiness / Corrective Frontier
- `AGENTS.md`
- `.planning/AGENTS.md`
- `.planning/readiness/phase-01-rerun/STATUS.md`
- `.planning/readiness/phase-01-rerun/TASKS.md`
- `.planning/readiness/phase-01-rerun/GATES/checkpoint-5.md`
- `.planning/readiness/phase-01-rerun/PROTOCOL.md`
- `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18-bounded-promoted-corrective-scope-spec.md`
- `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18-launch-bundle-spec.md`
- `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18a-boundary-and-ledger-launch-spec.md`
- `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18b-review-planning-chain-launch-spec.md`
- `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18c-completion-routing-chain-launch-spec.md`
- `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18d-integration-and-review-prep-launch-spec.md`
- `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-19d4-operational-consequences-adjudication-internal-r1.md`
- `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-19e-adjudication-reread-internal-r1.md`

### Current Governing / Method Docs
- `WORKFLOW.md`
- `AI-GUARDRAILS.md`
- `ARTIFACT-GOVERNANCE.md`
- `.codex/skills/gsd-rigorous-research/SKILL.md`
- `.codex/skills/gsd-rigorous-research/references/method.md`
- `.codex/skills/gsd-rigorous-research/references/output-template.md`
- `~/.gsd/knowledge/index.md`

## Concern Map From 2026-04-15 Bundle

- [e:c:i] `Returned-work disposition and closure auditability` was a major historical concern. The bundle explicitly said launch auditability was stronger than closure auditability, returned work lacked mandatory disposition, and `runtime-valid` was not cleanly separated from `actually closed` (`.planning/research/2026-04-15-multilayer-harness-governance-audit/01-codex-orchestration-layer-audit.md:186-206,225-230`; `.planning/research/2026-04-15-multilayer-harness-governance-audit/06-converged-synthesis.md:301-305,331-337,391-405`).
- [e:c:i] `Worker-first exploration and explicit active-task structure` was also a distinct historical concern. The bundle wanted exploratory work to be worker-first by default and wanted one declared active substantive task rather than ambient multi-bucket drift (`.planning/research/2026-04-15-multilayer-harness-governance-audit/01-codex-orchestration-layer-audit.md:183-185,211-212,226-229,241-246`; `.planning/research/2026-04-15-multilayer-harness-governance-audit/06-converged-synthesis.md:332-334,391-399`).
- [e:c:i] `GSD lifecycle doctrine carry-forward` was a major historical concern. The bundle said `LONG-ARC.md` was strong inside phase planning but weak at `new-project`, `new-milestone`, `progress`, `transition`, `complete-milestone`, auto paths, and lifecycle metadata (`.planning/research/2026-04-15-multilayer-harness-governance-audit/02-gsd-lifecycle-and-long-arc-layer-audit.md:175-190,233-289`; `.planning/research/2026-04-15-multilayer-harness-governance-audit/06-converged-synthesis.md:257,339-349,406-417`).
- [e:c:i] `Git / repo-ops boundary materialization` was a major historical concern. The bundle wanted explicit same-checkout versus branch versus worktree rules, explicit park/accept/revise/reject materialization, branch-diff review, and a cleaner distinction between recovery tactics and normal posture (`.planning/research/2026-04-15-multilayer-harness-governance-audit/03-git-repo-operations-layer-audit.md:167-201,213-329`; `.planning/research/2026-04-15-multilayer-harness-governance-audit/06-converged-synthesis.md:258,303-305,351-360,418-425`).
- [e:c:i] `Config/default posture alignment with the repo's rigor bar` was a distinct historical concern. The bundle explicitly called out `mode: "yolo"`, `workflow.auto_advance: true`, and `git.branching_strategy: "none"` as misaligned with doctrine-sensitive work and recommended live config alignment rather than commentary-only safety (`.planning/research/2026-04-15-multilayer-harness-governance-audit/01-codex-orchestration-layer-audit.md:208-209,225-231`; `.planning/research/2026-04-15-multilayer-harness-governance-audit/02-gsd-lifecycle-and-long-arc-layer-audit.md:184-189,272-275`; `.planning/research/2026-04-15-multilayer-harness-governance-audit/03-git-repo-operations-layer-audit.md:168-171`; `.planning/research/2026-04-15-multilayer-harness-governance-audit/06-converged-synthesis.md:374,426-432`).
- [e:c:i+d] `CI / release / deploy staged mechanical enforcement` was a major historical concern. The bundle wanted one narrow repo-integrity CI lane after a canonical local verify contract, manual and human-visible release/deploy approval until a real runtime exists, and risk-shaped escalation instead of size-shaped automation (`.planning/research/2026-04-15-multilayer-harness-governance-audit/04-ci-release-and-deployment-layer-audit.md:148-195`; `.planning/research/2026-04-15-multilayer-harness-governance-audit/06-converged-synthesis.md:304,362-368,434-466`; `.planning/research/2026-04-15-multilayer-harness-governance-audit/08-external-comparative-governance-research.md:116-128,150-158,193-205`).
- [e:c:i+d] `Cross-layer handoff contracts and layer ownership` was a major historical concern. The bundle's strongest synthesis claim was that the main weakness was under-specified handoffs between Codex, GSD, Git, and CI, and that the correct answer was a progressive control chain with explicit ownership by layer (`.planning/research/2026-04-15-multilayer-harness-governance-audit/05-cross-layer-integration-and-escalation-audit.md:148-175,217-267,388-417`; `.planning/research/2026-04-15-multilayer-harness-governance-audit/06-converged-synthesis.md:263-287,370-386`; `.planning/research/2026-04-15-multilayer-harness-governance-audit/00-launch-bundle-spec.md:188-193`).
- [e:c:i+d] `Governance-semantic uptake and explicit review/handoff machinery` was an externally pressured historical subfamily. `08` argued that issue/PR/MR templates, review-owner routing, and linked review artifacts were underweighted, and that authority docs should not be mistaken for sufficient downstream uptake (`.planning/research/2026-04-15-multilayer-harness-governance-audit/08-external-comparative-governance-research.md:85-95,140-148,197-203`; `.planning/research/2026-04-15-multilayer-harness-governance-audit/06-converged-synthesis.md:267-271,359,456-460`).

## Comparison Against Current R5.18 / Checkpoint 5 State

### Direct Evidence

- [e:c:i] Checkpoint 5 is still active, the repo is still `not ready to rerun`, and the split `R5.18a/b/c/d` bundle exists only as boundary and launch truth; execution has not started (`.planning/readiness/phase-01-rerun/STATUS.md:7-10,91-95,157-163,204-206`; `.planning/readiness/phase-01-rerun/TASKS.md:24`).
- [e:c:i] Current Checkpoint 5 owns rerun-blocking harness follow-through: runtime-authoritative worker alignment, review/closure-pressure hardening, launch/model-truth capture, workflow-chain follow-through, and wrapper alignment after workflow changes (`.planning/readiness/phase-01-rerun/STATUS.md:28-33,142-149`; `.planning/readiness/phase-01-rerun/TASKS.md:9-15`; `.planning/readiness/phase-01-rerun/GATES/checkpoint-5.md:96-107`).
- [e:c:i] Current `R5.18` explicitly keeps `Bucket 1` narrow, widens `Bucket 2` and `Bucket 3`, requires contradiction-ledger entries for non-first-wave live items, rejects authority-shelter as a cheap keep-out move, and forbids promoting the new exclusion heuristics into standing doctrine (`.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18-bounded-promoted-corrective-scope-spec.md:62-69,111-181,183-233,278-307`; `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-19d4-operational-consequences-adjudication-internal-r1.md:5-16,17-70,91-106`; `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-19e-adjudication-reread-internal-r1.md:25-33`).
- [e:c:i] Current governing docs outside the readiness package already absorb some historical concerns into doctrine: root `AGENTS.md` now requires auditable baselines and explicit `accept / revise / park / reject`; `.planning/AGENTS.md` now requires visible path-of-inquiry plus evidence/inference/unknown separation; `WORKFLOW.md` now encodes branch discipline, branch-level review, and launch-truth capture as standing policy (`AGENTS.md:96-124`; `.planning/AGENTS.md:42-112`; `WORKFLOW.md:30-41,56-82,84-99,115-124,153-158`).

### Inference and Interpretation

- [d:c+r:i] Current `R5.18` is not a re-execution of the full 2026-04-15 multi-layer roadmap. It is a narrower rerun-critical corrective frontier that most directly absorbs the old `closure / disposition / handoff-explicitness` concerns and only partially carries the old `full lifecycle`, `repo-ops materialization`, and `CI staging` agenda.
- [d:c+r:i] A historical concern can now be inside current truth in three materially different ways: `patch-now trunk`, `mandatory explicit-disposition surface`, or `conditional / contradiction-ledger item`. Flattening those into one generic `addressed` would recreate the failure mode the split `R5.18` bundle was designed to prevent (`.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18-launch-bundle-spec.md:7-18`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18-bounded-promoted-corrective-scope-spec.md:70-76`; `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-19e-adjudication-reread-internal-r1.md:27-33`).
- [d:c+r:i] Several current `R5.18` items are clearly responsive to the historical bundle but are doing later, narrower work: runtime-authoritative overlay/live pairing, stronger post-verificationist review-consumer semantics, and wrapper-alignment follow-through are rerun-critical concretizations of the older handoff and closure concerns, not one-for-one 2026-04-15 prescriptions (`.planning/readiness/phase-01-rerun/STATUS.md:29-33,67-69`; `.planning/readiness/phase-01-rerun/TASKS.md:9-15`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18c-completion-routing-chain-launch-spec.md:31-35`).

### Unknowns

- [o:c:i] Because `R5.18a/b/c/d` execution has not started, this comparison cannot claim actual correction of the live surfaces; it can only classify current governing scope honestly (`.planning/readiness/phase-01-rerun/STATUS.md:91-95,157-163`; `.planning/readiness/phase-01-rerun/TASKS.md:24`).
- [o:c:i] Final owner naming for several deferred contradictions is not yet on disk as completed `R5.18a` output, so some current deferrals remain `boundary truth` rather than `executed ownership truth` (`.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18a-boundary-and-ledger-launch-spec.md:24-31`; `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-19d4-operational-consequences-adjudication-internal-r1.md:91-106`).
- [o:c+r:i] If `R5.18` execution touches config behavior, worktree behavior, or wider governance machinery, currently partial or deferred historical families may need reclassification.

## Integrated Decision Structure

- [d:c+r:i] The historical bundle's concerns now fall into three live classes: directly absorbed into current `R5.18` scope, preserved only as boundary / contradiction / conditional truth, or not presently owned despite historical force.
- [d:c+r:i] The strongest current uptake is on `closure discipline`, `handoff explicitness`, and `semantic non-silence`. The weakest current uptake is on `live config posture`, `full lifecycle doctrine carry-forward`, and `concrete CI/local-verify activation`.
- [d:c+r:i] No major historical concern family is actually superseded. Some are narrowed or deferred by current stage, but none are replaced by a better framing that makes the old concern obsolete.

| historical concern family | where exposed in 2026-04-15 bundle | current treatment | status | evidence quality | note |
| --- | --- | --- | --- | --- | --- |
| returned-work disposition / closure auditability | `01`: 186-206, 225-230; `06`: 301-305, 331-337, 391-405 | current Checkpoint 5 actively owns review/closure-pressure, launch/model-truth capture, and workflow-chain follow-through; root `AGENTS.md` and `WORKFLOW.md` now require explicit review/disposition and launch-truth handling | addressed_in_r5_18 | high | directly responsive, but still not implemented |
| worker-first exploration / explicit active substantive task model | `01`: 183-185, 211-212, 226-229, 241-246; `06`: 332-334, 391-399 | split launch-spec discipline exists, and delegation boundaries are stricter, but current `R5.18` does not yet introduce the explicit `one active substantive task` or `worker-first exploration` machinery the old bundle asked for | partially_addressed_boundary_only | medium | launch discipline improved; active-task structure remains under-owned |
| GSD lifecycle doctrine / `LONG-ARC` carry-forward | `02`: 175-190, 233-289; `06`: 339-349, 406-417 | current doctrine strengthens future-awareness, and `R5.18c` touches `progress.md` and `transition.md`, but `new-project`, `new-milestone`, `complete-milestone`, and lifecycle doctrine metadata are not current `R5.18` owners | partially_addressed_boundary_only | medium | historical family was lifecycle-wide; current uptake is rerun-critical only |
| Git / repo-ops boundary materialization | `03`: 167-201, 213-329; `06`: 351-360, 418-425 | branch/review/disposition doctrine is now stronger in `WORKFLOW.md` and root `AGENTS.md`, but Checkpoint 5 still treats branch/worktree materialization as accepted bounded risk and leaves `R5.8` conditional | deferred_with_owner | medium | explicit trigger exists, but full materialization is not in first-wave `R5.18` |
| config/default posture alignment with rigor bar | `01`: 208-209, 225-231; `02`: 184-189, 272-275; `03`: 168-171; `06`: 374, 426-432 | current doctrine is stricter, but no current `R5.18` bucket, task, or launch lane owns live config/default changes | still_missing | high | clearest quiet drop from the historical near-term changes |
| CI / local verify / manual deploy staging | `04`: 148-195; `06`: 434-466; `08`: 116-128, 193-205 | current checkpoint preserves narrow-scope/no-omnibus-hardening logic, but no active `R5.18` lane owns a canonical local verify contract or narrow repo-integrity CI | partially_addressed_boundary_only | medium | stage-aware defer survives; concrete near-term controls remain unowned |
| cross-layer handoff contracts / explicit layer ownership | `05`: 148-175, 217-267, 388-417; `06`: 263-287, 370-386 | split `R5.18a/b/c/d`, widened `Bucket 2/3`, contradiction-ledger requirement, and `R5.18d` integration checks directly target no-silence handoff ownership | addressed_in_r5_18 | high | strongest direct response to the historical bundle |
| governance-semantic uptake / explicit review-handoff machinery | `08`: 85-95, 140-148, 197-203; `06`: 267-271, 359, 456-460 | `Bucket 2C` now names reviewer-prompt tightening, review/debt vocabulary, protocol alignment, review-template/policy uptake, and explicit statusing for `WORKFLOW.md`, `AI-GUARDRAILS.md`, and `ARTIFACT-GOVERNANCE.md`; remote issue/PR/review-owner machinery is still absent | partially_addressed_boundary_only | medium | repo-local semantic uptake is in scope; fuller remote review machinery is not |

## What Is Clearly Being Addressed

- [d:c+r:i] `Cross-layer handoff explicitness` is directly in current scope. The split `R5.18a/b/c/d` design, widened `Bucket 2` and `Bucket 3`, contradiction-ledger requirement, anti-authority-shelter rule, and no-heuristics-as-standing-doctrine rule are a direct answer to the historical complaint that layer handoffs were too implicit (`.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18-launch-bundle-spec.md:7-18,21-63`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18d-integration-and-review-prep-launch-spec.md:5-18`; `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-19d4-operational-consequences-adjudication-internal-r1.md:5-16,17-58,91-106`).
- [d:c+r:i] `Closure/disposition auditability` is directly in current scope. Current Checkpoint 5 owns review/closure-pressure follow-through, launch/model-truth capture, and workflow-chain follow-through, while current doctrine already requires auditable baselines and returned-work disposition (`.planning/readiness/phase-01-rerun/STATUS.md:28-33,142-149`; `.planning/readiness/phase-01-rerun/TASKS.md:10-15`; `AGENTS.md:111-124`; `WORKFLOW.md:56-82`).
- [d:c+r:i] `Governance semantic uptake` is no longer allowed to hide behind source authority alone. `Bucket 2C` and `R5.18d` explicitly keep reviewer-prompt tightening, vocabulary disposition, protocol alignment, review-policy/template uptake, and governance-doc statusing inside active consequence handling (`.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18-bounded-promoted-corrective-scope-spec.md:167-181`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18d-integration-and-review-prep-launch-spec.md:7-12`; `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-19d4-operational-consequences-adjudication-internal-r1.md:14,50-58`).
- [d:c+r:i] Some current `R5.18` work is clearly responsive to the older bundle but is doing newer rerun-critical work rather than literal old-roadmap execution: runtime-authoritative worker alignment, stronger review-consumer semantics, and wrapper follow-through belong in that category (`.planning/readiness/phase-01-rerun/TASKS.md:9-15`; `.planning/readiness/phase-01-rerun/GATES/checkpoint-5.md:96-107`).

## What Is Only Partially Addressed

- [d:c+r:i] The old `LONG-ARC` carry-forward concern has been narrowed to rerun-critical routing and stronger governing doctrine. That is not the same as the historical recommendation to patch the lifecycle set `new-project` / `new-milestone` / `progress` / `transition` / `complete-milestone` plus doctrine metadata (`.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18c-completion-routing-chain-launch-spec.md:11-14`; `.planning/AGENTS.md:100-112`; contrast with `.planning/research/2026-04-15-multilayer-harness-governance-audit/02-gsd-lifecycle-and-long-arc-layer-audit.md:175-190,233-289`).
- [d:c+r:i] The old CI/deploy staging concern survives mainly as stage-aware doctrine. Current Checkpoint 5 does not own the historical near-term pair `canonical local verify entrypoint` plus `narrow repo-integrity CI`, even though the old bundle explicitly framed those as the right current-stage CI move (`.planning/readiness/phase-01-rerun/GATES/checkpoint-5.md:8-12,96-113`; `WORKFLOW.md:134-143`; contrast with `.planning/research/2026-04-15-multilayer-harness-governance-audit/04-ci-release-and-deployment-layer-audit.md:159-173`).
- [d:c+r:i] The old governance-handoff concern is only partially answered on the remote-review side. Current `Bucket 2C` handles repo-local semantic uptake, but `08`'s pressure about issue/PR/MR templates and review-owner routing is not represented in the current split bundle (`.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18-bounded-promoted-corrective-scope-spec.md:167-181`; contrast with `.planning/research/2026-04-15-multilayer-harness-governance-audit/08-external-comparative-governance-research.md:85-95,141-147,197-203`).
- [d:c+r:i] Historical `worker-first exploration / active-task model` is only partly answered. Current doctrine is stricter about delegation boundaries and unresolved returned work, but the explicit `one active substantive task` and default `worker lanes first` machinery remain absent from the current live bundle (`AGENTS.md:111-124`; `WORKFLOW.md:58-67`; contrast with `.planning/research/2026-04-15-multilayer-harness-governance-audit/01-codex-orchestration-layer-audit.md:225-246`).

## What Is Still Missing Or Quietly Dropped

- [d:c+r:i] Historical `config/default posture alignment` is the clearest quiet drop. The old bundle explicitly called for revisiting permissive live defaults, but the current `R5.18` boundary, launch bundle, and active task board do not include config surfaces as current targets (`.planning/research/2026-04-15-multilayer-harness-governance-audit/06-converged-synthesis.md:426-432`; contrast with `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18-bounded-promoted-corrective-scope-spec.md:78-177`; `.planning/readiness/phase-01-rerun/TASKS.md:5-24`; `.planning/readiness/phase-01-rerun/GATES/checkpoint-5.md:82-113`).
- [o:c+r:i] Full lifecycle doctrine carry-forward beyond `progress` / `transition` remains under-owned. The current frontier shows no active treatment for `new-project`, `new-milestone`, `complete-milestone`, or `long_arc_*` init metadata (`.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18c-completion-routing-chain-launch-spec.md:5-15`; `.planning/readiness/phase-01-rerun/TASKS.md:5-24`; contrast with `.planning/research/2026-04-15-multilayer-harness-governance-audit/02-gsd-lifecycle-and-long-arc-layer-audit.md:235-286`).
- [o:c+r:i] The stronger remote-review governance surfaces highlighted by `08` remain effectively absent from current `R5.18` truth. They may be stage-inappropriate for pre-rerun work, but the current bundle does not record them as named later-lane consequences; they are simply not in the active frontier (`.planning/research/2026-04-15-multilayer-harness-governance-audit/08-external-comparative-governance-research.md:85-95,141-147,197-203`; contrast with `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18-launch-bundle-spec.md:21-63`).

## What Can Close Now

- [d:c+r:i] It can now close that current `R5.18` does not absorb the 2026-04-15 governance audit wholesale. It absorbs only the rerun-critical subset, chiefly `closure/disposition`, `handoff explicitness`, and `governance semantic non-silence`.
- [d:c+r:i] It can now close that `cross-layer handoff contracts` and `closure/disposition auditability` are genuinely inside current governing `R5.18` scope.
- [d:c+r:i] It can now close that `config/default alignment` is not presently owned by current `R5.18`, and that `full lifecycle carry-forward` plus `CI/local-verify activation` remain only partial.
- [d:c+r:i] It can now close that no major historical concern family is `superseded`; the current package narrows and defers, but does not obsolete them.

## What Must Stay Open

- [o:c:i] Whether `R5.18a` will actually assign owner and reopen-trigger truth to all contested or deferred items rather than merely preserving the contradiction-ledger requirement on paper.
- [o:c+r:i] Whether the Git/worktree concern stays safely deferred once the patch wave touches real runtime/config or parallel-lane behavior.
- [o:c+r:i] Whether the repo reactivates the historical config-alignment concern after `R5.18` execution or continues to rely on stronger doctrine outpacing live defaults.
- [o:c+r:i] Whether the remote-review / PR-template / review-owner machinery highlighted by `08` becomes a named post-rerun lane or remains ambient.
- [o:c+r:i] Whether the historical lifecycle-wide `LONG-ARC` gap should reopen after rerun once the repo returns to normal phase execution rather than readiness repair.

## Planning Handoff

### Direct Doctrine
- Treat current `R5.18` as a bounded rerun-critical follow-through bundle, not as execution of the full 2026-04-15 multi-layer roadmap.
- Treat `patch-now`, `explicit-disposition`, `conditional contradiction`, and `governing authority` as different closure states. Do not flatten them.

### Bounded-Open Branches
- lifecycle-wide `LONG-ARC` carry-forward outside `progress` / `transition`
- canonical local verify plus narrow repo-integrity CI
- remote review-template / review-owner routing machinery
- historical `worker-first exploration / active-task model` beyond current disposition doctrine

### Preserve-Only Seams
- `AI-GUARDRAILS.md`, `ARTIFACT-GOVERNANCE.md`, `R5.9`, and `R5.10` remain preserve-only or later-lane surfaces under current consequence logic (`.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-19d4-operational-consequences-adjudication-internal-r1.md:72-80`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18-bounded-promoted-corrective-scope-spec.md:266-275`).

### Reversal-Sensitive Boundaries
- do not let `R5.19` heuristics become standing doctrine
- do not treat `R5.8` accepted bounded risk as proof that Git/worktree boundary materialization is closed
- do not treat governance-doc strengthening as a substitute for config or lifecycle implementation

### Inquiry Debt
- explicit live config/default posture alignment
- full non-phase lifecycle doctrine metadata and carry-forward handling
- named later-lane treatment for remote review / routing surfaces highlighted by `08`
- Use this comparison as a challenge surface for `R5.18a`: if a historical concern family remains outside first-wave, current boundary artifacts should either record the defer/trigger plainly or admit that the family is being dropped.

## Sources

### Historical Bundle
- `.planning/research/2026-04-15-multilayer-harness-governance-audit/00-launch-bundle-spec.md`
- `.planning/research/2026-04-15-multilayer-harness-governance-audit/01-codex-orchestration-layer-audit.md`
- `.planning/research/2026-04-15-multilayer-harness-governance-audit/02-gsd-lifecycle-and-long-arc-layer-audit.md`
- `.planning/research/2026-04-15-multilayer-harness-governance-audit/03-git-repo-operations-layer-audit.md`
- `.planning/research/2026-04-15-multilayer-harness-governance-audit/04-ci-release-and-deployment-layer-audit.md`
- `.planning/research/2026-04-15-multilayer-harness-governance-audit/05-cross-layer-integration-and-escalation-audit.md`
- `.planning/research/2026-04-15-multilayer-harness-governance-audit/06-converged-synthesis.md`
- `.planning/research/2026-04-15-multilayer-harness-governance-audit/08-external-comparative-governance-research.md`

### Current Frontier
- `AGENTS.md`
- `.planning/AGENTS.md`
- `WORKFLOW.md`
- `AI-GUARDRAILS.md`
- `ARTIFACT-GOVERNANCE.md`
- `.planning/readiness/phase-01-rerun/STATUS.md`
- `.planning/readiness/phase-01-rerun/TASKS.md`
- `.planning/readiness/phase-01-rerun/GATES/checkpoint-5.md`
- `.planning/readiness/phase-01-rerun/PROTOCOL.md`
- `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18-bounded-promoted-corrective-scope-spec.md`
- `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18-launch-bundle-spec.md`
- `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18a-boundary-and-ledger-launch-spec.md`
- `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18b-review-planning-chain-launch-spec.md`
- `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18c-completion-routing-chain-launch-spec.md`
- `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18d-integration-and-review-prep-launch-spec.md`
- `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-19d4-operational-consequences-adjudication-internal-r1.md`
- `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-19e-adjudication-reread-internal-r1.md`
