# Checkpoint 5 R5.19a2 Workflow Disposition Inventory Audit Internal R1

## Summary

- [e:c:i] Current explicit Checkpoint 5 workflow consideration is concentrated in ten files: seven workflows are already inside current first-wave `R5.18` / implementation scope (`discuss-phase.md`, `research-phase.md`, `plan-phase.md`, `execute-phase.md`, `review.md`, `progress.md`, `transition.md`), two are mandatory explicit-disposition severity-boundary files (`ship.md`, `autonomous.md`), and `verify-work.md` remains scope-gated rather than cleanly excluded. Sources: `.planning/readiness/phase-01-rerun/GATES/checkpoint-5.md:30-31,45-57,67-92,109-121`; `.planning/readiness/phase-01-rerun/TASKS.md:12-15,21-22`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md:41-116`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18-bounded-promoted-corrective-scope-spec.md:74-145,158-192`.
- [e:c+r:i] Twelve additional workflow files are not cleanly outside Checkpoint 5. Two already carry qualified pressure (`code-review.md`, `execute-plan.md`), and ten more are better described as `not_yet_meaningfully_considered` than as defended exclusions because they are alternate carriers, routers, or adjacent variants of the active workflow chain. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-workflow-chain-and-artifact-contracts.md:19,37-38,44,82,90,96`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-gsd-agent-doctrine-and-role-contracts-excellence.md:16,27,43`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-gsd-workflow-chain-and-artifact-contracts-excellence.md:17,27,44,86`.
- [d:r:i] The current `outside_checkpoint_5` bucket is operationally real but not file-level proven. Most of the 49 workflows currently treated as outside are excluded by family-level inference plus omission from current scope artifacts, not by direct `R5.17` / `R5.18` workflow-level adjudication. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-workflow-harness-scope-audit.md:70-72,103-106`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18-bounded-promoted-corrective-scope-spec.md:210-241`; `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-17e-exclusion-adjudication-reread-internal-r1.md:17-32`; `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-17e-exclusion-adjudication-reread-cross-vendor-opus-1m-r1.md:74-104`.

## Method And Read Coverage

- Read the required governance/spec stack named in the lane request, then the current checkpoint-state stack actually governing workflow status: `STATUS.md`, `TASKS.md`, `GATES/checkpoint-5.md`, `PROTOCOL.md`, `POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md`, `AUDIT-COMPARISON-POLICY.md`, `checkpoint-3-gsd-surface-map.md`, `checkpoint-3-workflow-harness-scope-audit.md`, `checkpoint-5-workflow-follow-through-implementation-spec.md`, `checkpoint-5-r5-18-bounded-promoted-corrective-scope-spec.md`, and both `R5.17e` rereads.
- Enumerated all 71 files under `.codex/get-shit-done/workflows/`.
- Spot-read ambiguous workflow surfaces that are adjacent to the active chain but not explicitly dispositioned in current Checkpoint 5 scope: `discuss-phase-power.md`, `discovery-phase.md`, `execute-plan.md`, `verify-phase.md`, `manager.md`, `next.md`, `quick.md`, `resume-project.md`, `discuss-phase-assumptions.md`, `list-phase-assumptions.md`, `do.md`, `pause-work.md`, and `settings.md`.
- Classification rule used:
  - explicit current scope beats older broad scoping
  - explicit `R5.18` bucketing beats generic adjacency
  - if a workflow is adjacent to an active carrier but current Checkpoint 5 artifacts do not actually disposition it, prefer `qualified_pressure_only` or `not_yet_meaningfully_considered` over a cleaner exclusion label
  - do not call workflow-level exclusions `preserved_exclusion` unless file-level proof exists

Reference key used in the inventory table:

- `G5` = `.planning/readiness/phase-01-rerun/GATES/checkpoint-5.md:25-31,45-57,67-92,109-121`
- `T5` = `.planning/readiness/phase-01-rerun/TASKS.md:9-22`
- `I5` = `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md:21-25,31-37,41-116`
- `R518` = `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18-bounded-promoted-corrective-scope-spec.md:62-72,74-145,158-258`
- `R517Ei` = `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-17e-exclusion-adjudication-reread-internal-r1.md:5-7,17-32`
- `R517Ex` = `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-17e-exclusion-adjudication-reread-cross-vendor-opus-1m-r1.md:13-16,34-43,74-104`
- `C3Scope` = `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-workflow-harness-scope-audit.md:70-72,103-106`
- `C3Map` = `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-surface-map.md:58-61`
- `C3Chain` = `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-workflow-chain-and-artifact-contracts.md:19,37-38,44,82,90,96`
- `C4Role` = `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-gsd-agent-doctrine-and-role-contracts-excellence.md:16,27,43`
- `C4WF` = `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-gsd-workflow-chain-and-artifact-contracts-excellence.md:17,27,44,86`
- `R517Bcp` = `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-17b-chain-tail-exclusion-audit-internal-r1.md:38`
- `WFDISC` = `.codex/get-shit-done/workflows/discovery-phase.md:1-40`
- `WFDPP` = `.codex/get-shit-done/workflows/discuss-phase-power.md:1-28`
- `WFASSUME` = `.codex/get-shit-done/workflows/discuss-phase-assumptions.md:1-34`
- `WFDO` = `.codex/get-shit-done/workflows/do.md:1-40`
- `WFLASSUME` = `.codex/get-shit-done/workflows/list-phase-assumptions.md:1-24`
- `WFMGR` = `.codex/get-shit-done/workflows/manager.md:1-33`
- `WFNEXT` = `.codex/get-shit-done/workflows/next.md:1-29`
- `WFQUICK` = `.codex/get-shit-done/workflows/quick.md:1-37`
- `WFRESUME` = `.codex/get-shit-done/workflows/resume-project.md:1-31`
- `WFVERIFY` = `.codex/get-shit-done/workflows/verify-phase.md:1-38`
- `WFEXECPLAN` = `.codex/get-shit-done/workflows/execute-plan.md:1-50`

## Disposition Counts

| disposition | count | note |
| --- | ---: | --- |
| `first_wave_r5_18` | 7 | explicit current first-wave / active-scope workflow set |
| `mandatory_explicit_disposition` | 2 | severity-boundary workflows that cannot disappear by silence |
| `scope_gating_only` | 1 | workflow explicitly kept behind an unresolved boundary choice |
| `governing_authority_not_edit_now` | 0 | no workflow currently holds this status |
| `preserved_exclusion` | 0 | no workflow currently has file-level proof strong enough for this label |
| `qualified_pressure_only` | 2 | adjacent workflows already carrying real pressure but not yet current scope |
| `outside_checkpoint_5` | 49 | current outside bucket; mostly family-level / inferred, not file-level proven |
| `not_yet_meaningfully_considered` | 10 | alternate carriers, routers, and variants left outside current scope without a clean file-level disposition |

## Full Disposition Inventory

| path | family | current disposition | basis | explicit_or_inferred | directly_challenged_in_r5_17 | relevance_mode | exclusion_proven | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `workflows/discuss-phase.md` | `core_phase_chain` | `first_wave_r5_18` | `G5+T5+I5` | `explicit` | `yes` | `both` | `n/a` | `high` |
| `workflows/execute-phase.md` | `core_phase_chain` | `first_wave_r5_18` | `G5+T5+I5+R517Ei` | `explicit` | `yes` | `both` | `n/a` | `high` |
| `workflows/plan-phase.md` | `core_phase_chain` | `first_wave_r5_18` | `G5+R518+R517Ex` | `explicit` | `yes` | `both` | `n/a` | `high` |
| `workflows/research-phase.md` | `core_phase_chain` | `first_wave_r5_18` | `G5+T5+I5+R517Ex` | `explicit` | `yes` | `both` | `n/a` | `high` |
| `workflows/review.md` | `review_and_closure` | `first_wave_r5_18` | `T5+R518+R517Ex` | `explicit` | `yes` | `both` | `n/a` | `high` |
| `workflows/progress.md` | `chain_tail_and_completion` | `first_wave_r5_18` | `R518+R517Ei+R517Ex` | `explicit` | `yes` | `both` | `n/a` | `high` |
| `workflows/transition.md` | `chain_tail_and_completion` | `first_wave_r5_18` | `R518+R517Ei+R517Ex` | `explicit` | `yes` | `both` | `n/a` | `high` |
| `workflows/autonomous.md` | `chain_tail_and_completion` | `mandatory_explicit_disposition` | `R518+R517Ex` | `explicit` | `yes` | `both` | `no` | `high` |
| `workflows/ship.md` | `chain_tail_and_completion` | `mandatory_explicit_disposition` | `R518+R517Ex` | `explicit` | `yes` | `both` | `no` | `high` |
| `workflows/verify-work.md` | `chain_tail_and_completion` | `scope_gating_only` | `I5+R517Ei+R517Ex` | `explicit` | `yes` | `both` | `no` | `medium` |
| `workflows/code-review.md` | `review_and_closure` | `qualified_pressure_only` | `C4Role+C4WF+absent from G5/T5/I5/R518` | `inferred` | `no` | `both` | `no` | `medium` |
| `workflows/execute-plan.md` | `adjacent_phase_variant` | `qualified_pressure_only` | `C3Chain+R517Bcp+absent from G5/T5/I5/R518` | `inferred` | `yes` | `both` | `no` | `medium` |
| `workflows/discovery-phase.md` | `adjacent_phase_variant` | `not_yet_meaningfully_considered` | `WFDISC+absent from G5/T5/I5/R518` | `inferred` | `no` | `propagation_linked` | `no` | `medium` |
| `workflows/discuss-phase-assumptions.md` | `adjacent_phase_variant` | `not_yet_meaningfully_considered` | `WFASSUME+absent from G5/T5/I5/R518` | `inferred` | `no` | `propagation_linked` | `no` | `low` |
| `workflows/discuss-phase-power.md` | `adjacent_phase_variant` | `not_yet_meaningfully_considered` | `WFDPP+absent from G5/T5/I5/R518` | `inferred` | `no` | `propagation_linked` | `no` | `medium` |
| `workflows/do.md` | `router_or_orchestrator` | `not_yet_meaningfully_considered` | `WFDO+absent from G5/T5/I5/R518` | `inferred` | `no` | `propagation_linked` | `no` | `medium` |
| `workflows/list-phase-assumptions.md` | `adjacent_phase_variant` | `not_yet_meaningfully_considered` | `WFLASSUME+absent from G5/T5/I5/R518` | `inferred` | `no` | `propagation_linked` | `no` | `low` |
| `workflows/manager.md` | `router_or_orchestrator` | `not_yet_meaningfully_considered` | `WFMGR+absent from G5/T5/I5/R518` | `inferred` | `no` | `propagation_linked` | `no` | `medium` |
| `workflows/next.md` | `router_or_orchestrator` | `not_yet_meaningfully_considered` | `WFNEXT+absent from G5/T5/I5/R518` | `inferred` | `no` | `propagation_linked` | `no` | `medium` |
| `workflows/quick.md` | `router_or_orchestrator` | `not_yet_meaningfully_considered` | `WFQUICK+absent from G5/T5/I5/R518` | `inferred` | `no` | `both` | `no` | `low` |
| `workflows/resume-project.md` | `router_or_orchestrator` | `not_yet_meaningfully_considered` | `WFRESUME+absent from G5/T5/I5/R518` | `inferred` | `no` | `propagation_linked` | `no` | `medium` |
| `workflows/verify-phase.md` | `adjacent_phase_variant` | `not_yet_meaningfully_considered` | `WFVERIFY+absent from G5/T5/I5/R518` | `inferred` | `no` | `propagation_linked` | `no` | `medium` |
| `workflows/add-phase.md` | `project_or_milestone_admin` | `outside_checkpoint_5` | `C3Scope+C3Map+absent from G5/T5/I5/R518` | `inferred` | `no` | `independent_surface` | `partial` | `medium` |
| `workflows/add-tests.md` | `audit_or_validation_utility` | `outside_checkpoint_5` | `C3Scope+C3Map+absent from G5/T5/I5/R518` | `inferred` | `no` | `independent_surface` | `partial` | `medium` |
| `workflows/add-todo.md` | `notes_or_session_utility` | `outside_checkpoint_5` | `C3Scope+C3Map+absent from G5/T5/I5/R518` | `inferred` | `no` | `independent_surface` | `partial` | `medium` |
| `workflows/ai-integration-phase.md` | `planning_or_research_utility` | `outside_checkpoint_5` | `C3Scope+C3Map+absent from G5/T5/I5/R518` | `inferred` | `no` | `independent_surface` | `partial` | `medium` |
| `workflows/analyze-dependencies.md` | `planning_or_research_utility` | `outside_checkpoint_5` | `C3Scope+C3Map+absent from G5/T5/I5/R518` | `inferred` | `no` | `independent_surface` | `partial` | `medium` |
| `workflows/audit-fix.md` | `audit_or_validation_utility` | `outside_checkpoint_5` | `C3Scope+C3Map+absent from G5/T5/I5/R518` | `inferred` | `no` | `independent_surface` | `partial` | `medium` |
| `workflows/audit-milestone.md` | `audit_or_validation_utility` | `outside_checkpoint_5` | `C3Scope+C3Map+absent from G5/T5/I5/R518` | `inferred` | `no` | `independent_surface` | `partial` | `medium` |
| `workflows/audit-uat.md` | `audit_or_validation_utility` | `outside_checkpoint_5` | `C3Scope+C3Map+absent from G5/T5/I5/R518` | `inferred` | `no` | `independent_surface` | `partial` | `medium` |
| `workflows/check-todos.md` | `notes_or_session_utility` | `outside_checkpoint_5` | `C3Scope+C3Map+absent from G5/T5/I5/R518` | `inferred` | `no` | `independent_surface` | `partial` | `medium` |
| `workflows/cleanup.md` | `project_or_milestone_admin` | `outside_checkpoint_5` | `C3Scope+C3Map+absent from G5/T5/I5/R518` | `inferred` | `no` | `independent_surface` | `partial` | `medium` |
| `workflows/code-review-fix.md` | `audit_or_validation_utility` | `outside_checkpoint_5` | `C3Scope+C3Map+absent from G5/T5/I5/R518` | `inferred` | `no` | `independent_surface` | `partial` | `medium` |
| `workflows/complete-milestone.md` | `project_or_milestone_admin` | `outside_checkpoint_5` | `C3Scope+C3Map+absent from G5/T5/I5/R518` | `inferred` | `no` | `independent_surface` | `partial` | `medium` |
| `workflows/diagnose-issues.md` | `audit_or_validation_utility` | `outside_checkpoint_5` | `C3Scope+C3Map+absent from G5/T5/I5/R518` | `inferred` | `no` | `independent_surface` | `partial` | `medium` |
| `workflows/docs-update.md` | `planning_or_research_utility` | `outside_checkpoint_5` | `C3Scope+C3Map+absent from G5/T5/I5/R518` | `inferred` | `no` | `independent_surface` | `partial` | `medium` |
| `workflows/eval-review.md` | `audit_or_validation_utility` | `outside_checkpoint_5` | `C3Scope+C3Map+absent from G5/T5/I5/R518` | `inferred` | `no` | `independent_surface` | `partial` | `medium` |
| `workflows/explore.md` | `planning_or_research_utility` | `outside_checkpoint_5` | `C3Scope+C3Map+absent from G5/T5/I5/R518` | `inferred` | `no` | `independent_surface` | `partial` | `medium` |
| `workflows/extract_learnings.md` | `planning_or_research_utility` | `outside_checkpoint_5` | `C3Scope+C3Map+absent from G5/T5/I5/R518` | `inferred` | `no` | `independent_surface` | `partial` | `medium` |
| `workflows/fast.md` | `planning_or_research_utility` | `outside_checkpoint_5` | `C3Scope+C3Map+absent from G5/T5/I5/R518` | `inferred` | `no` | `independent_surface` | `partial` | `medium` |
| `workflows/forensics.md` | `audit_or_validation_utility` | `outside_checkpoint_5` | `C3Scope+C3Map+absent from G5/T5/I5/R518` | `inferred` | `no` | `independent_surface` | `partial` | `medium` |
| `workflows/health.md` | `planning_or_research_utility` | `outside_checkpoint_5` | `C3Scope+C3Map+absent from G5/T5/I5/R518` | `inferred` | `no` | `independent_surface` | `partial` | `medium` |
| `workflows/help.md` | `router_or_orchestrator` | `outside_checkpoint_5` | `C3Scope+C3Map+absent from G5/T5/I5/R518` | `inferred` | `no` | `independent_surface` | `partial` | `medium` |
| `workflows/import.md` | `router_or_orchestrator` | `outside_checkpoint_5` | `C3Scope+C3Map+absent from G5/T5/I5/R518` | `inferred` | `no` | `independent_surface` | `partial` | `medium` |
| `workflows/inbox.md` | `notes_or_session_utility` | `outside_checkpoint_5` | `C3Scope+C3Map+absent from G5/T5/I5/R518` | `inferred` | `no` | `independent_surface` | `partial` | `medium` |
| `workflows/insert-phase.md` | `project_or_milestone_admin` | `outside_checkpoint_5` | `C3Scope+C3Map+absent from G5/T5/I5/R518` | `inferred` | `no` | `independent_surface` | `partial` | `medium` |
| `workflows/list-workspaces.md` | `project_or_milestone_admin` | `outside_checkpoint_5` | `C3Scope+C3Map+absent from G5/T5/I5/R518` | `inferred` | `no` | `independent_surface` | `partial` | `medium` |
| `workflows/map-codebase.md` | `planning_or_research_utility` | `outside_checkpoint_5` | `C3Scope+C3Map+absent from G5/T5/I5/R518` | `inferred` | `no` | `independent_surface` | `partial` | `medium` |
| `workflows/milestone-summary.md` | `project_or_milestone_admin` | `outside_checkpoint_5` | `C3Scope+C3Map+absent from G5/T5/I5/R518` | `inferred` | `no` | `independent_surface` | `partial` | `medium` |
| `workflows/new-milestone.md` | `project_or_milestone_admin` | `outside_checkpoint_5` | `C3Scope+C3Map+absent from G5/T5/I5/R518` | `inferred` | `no` | `independent_surface` | `partial` | `medium` |
| `workflows/new-project.md` | `project_or_milestone_admin` | `outside_checkpoint_5` | `C3Scope+C3Map+absent from G5/T5/I5/R518` | `inferred` | `no` | `independent_surface` | `partial` | `medium` |
| `workflows/new-workspace.md` | `project_or_milestone_admin` | `outside_checkpoint_5` | `C3Scope+C3Map+absent from G5/T5/I5/R518` | `inferred` | `no` | `independent_surface` | `partial` | `medium` |
| `workflows/node-repair.md` | `router_or_orchestrator` | `outside_checkpoint_5` | `C3Scope+C3Map+absent from G5/T5/I5/R518` | `inferred` | `no` | `independent_surface` | `partial` | `medium` |
| `workflows/note.md` | `notes_or_session_utility` | `outside_checkpoint_5` | `C3Scope+C3Map+absent from G5/T5/I5/R518` | `inferred` | `no` | `independent_surface` | `partial` | `medium` |
| `workflows/pause-work.md` | `notes_or_session_utility` | `outside_checkpoint_5` | `C3Scope+C3Map+absent from G5/T5/I5/R518` | `inferred` | `no` | `independent_surface` | `partial` | `medium` |
| `workflows/plan-milestone-gaps.md` | `project_or_milestone_admin` | `outside_checkpoint_5` | `C3Scope+C3Map+absent from G5/T5/I5/R518` | `inferred` | `no` | `independent_surface` | `partial` | `medium` |
| `workflows/plant-seed.md` | `project_or_milestone_admin` | `outside_checkpoint_5` | `C3Scope+C3Map+absent from G5/T5/I5/R518` | `inferred` | `no` | `independent_surface` | `partial` | `medium` |
| `workflows/pr-branch.md` | `project_or_milestone_admin` | `outside_checkpoint_5` | `C3Scope+C3Map+absent from G5/T5/I5/R518` | `inferred` | `no` | `independent_surface` | `partial` | `medium` |
| `workflows/profile-user.md` | `planning_or_research_utility` | `outside_checkpoint_5` | `C3Scope+C3Map+absent from G5/T5/I5/R518` | `inferred` | `no` | `independent_surface` | `partial` | `medium` |
| `workflows/remove-phase.md` | `project_or_milestone_admin` | `outside_checkpoint_5` | `C3Scope+C3Map+absent from G5/T5/I5/R518` | `inferred` | `no` | `independent_surface` | `partial` | `medium` |
| `workflows/remove-workspace.md` | `project_or_milestone_admin` | `outside_checkpoint_5` | `C3Scope+C3Map+absent from G5/T5/I5/R518` | `inferred` | `no` | `independent_surface` | `partial` | `medium` |
| `workflows/scan.md` | `planning_or_research_utility` | `outside_checkpoint_5` | `C3Scope+C3Map+absent from G5/T5/I5/R518` | `inferred` | `no` | `independent_surface` | `partial` | `medium` |
| `workflows/secure-phase.md` | `audit_or_validation_utility` | `outside_checkpoint_5` | `C3Scope+C3Map+absent from G5/T5/I5/R518` | `inferred` | `no` | `independent_surface` | `partial` | `medium` |
| `workflows/session-report.md` | `notes_or_session_utility` | `outside_checkpoint_5` | `C3Scope+C3Map+absent from G5/T5/I5/R518` | `inferred` | `no` | `independent_surface` | `partial` | `medium` |
| `workflows/settings.md` | `router_or_orchestrator` | `outside_checkpoint_5` | `C3Scope+C3Map+absent from G5/T5/I5/R518` | `inferred` | `no` | `independent_surface` | `partial` | `medium` |
| `workflows/stats.md` | `project_or_milestone_admin` | `outside_checkpoint_5` | `C3Scope+C3Map+absent from G5/T5/I5/R518` | `inferred` | `no` | `independent_surface` | `partial` | `medium` |
| `workflows/ui-phase.md` | `planning_or_research_utility` | `outside_checkpoint_5` | `C3Scope+C3Map+absent from G5/T5/I5/R518` | `inferred` | `no` | `independent_surface` | `partial` | `medium` |
| `workflows/ui-review.md` | `audit_or_validation_utility` | `outside_checkpoint_5` | `C3Scope+C3Map+absent from G5/T5/I5/R518` | `inferred` | `no` | `independent_surface` | `partial` | `medium` |
| `workflows/undo.md` | `project_or_milestone_admin` | `outside_checkpoint_5` | `C3Scope+C3Map+absent from G5/T5/I5/R518` | `inferred` | `no` | `independent_surface` | `partial` | `medium` |
| `workflows/update.md` | `project_or_milestone_admin` | `outside_checkpoint_5` | `C3Scope+C3Map+absent from G5/T5/I5/R518` | `inferred` | `no` | `independent_surface` | `partial` | `medium` |
| `workflows/validate-phase.md` | `audit_or_validation_utility` | `outside_checkpoint_5` | `C3Scope+C3Map+absent from G5/T5/I5/R518` | `inferred` | `no` | `independent_surface` | `partial` | `medium` |

## Files Currently Excluded From Modification Consideration

No workflow file currently earns a defended `preserved_exclusion` label on file-level proof. The currently excluded workflow set is instead a mixture of `qualified_pressure_only`, `not_yet_meaningfully_considered`, and `outside_checkpoint_5`.

`qualified_pressure_only`:
`workflows/code-review.md`, `workflows/execute-plan.md`

`not_yet_meaningfully_considered`:
`workflows/discovery-phase.md`, `workflows/discuss-phase-assumptions.md`, `workflows/discuss-phase-power.md`, `workflows/do.md`, `workflows/list-phase-assumptions.md`, `workflows/manager.md`, `workflows/next.md`, `workflows/quick.md`, `workflows/resume-project.md`, `workflows/verify-phase.md`

`outside_checkpoint_5` by current family-level treatment:

- `planning_or_research_utility`: `workflows/ai-integration-phase.md`, `workflows/analyze-dependencies.md`, `workflows/docs-update.md`, `workflows/explore.md`, `workflows/extract_learnings.md`, `workflows/fast.md`, `workflows/health.md`, `workflows/map-codebase.md`, `workflows/profile-user.md`, `workflows/scan.md`, `workflows/ui-phase.md`
- `project_or_milestone_admin`: `workflows/add-phase.md`, `workflows/cleanup.md`, `workflows/complete-milestone.md`, `workflows/insert-phase.md`, `workflows/list-workspaces.md`, `workflows/milestone-summary.md`, `workflows/new-milestone.md`, `workflows/new-project.md`, `workflows/new-workspace.md`, `workflows/plan-milestone-gaps.md`, `workflows/plant-seed.md`, `workflows/pr-branch.md`, `workflows/remove-phase.md`, `workflows/remove-workspace.md`, `workflows/stats.md`, `workflows/undo.md`, `workflows/update.md`
- `audit_or_validation_utility`: `workflows/add-tests.md`, `workflows/audit-fix.md`, `workflows/audit-milestone.md`, `workflows/audit-uat.md`, `workflows/code-review-fix.md`, `workflows/diagnose-issues.md`, `workflows/eval-review.md`, `workflows/forensics.md`, `workflows/secure-phase.md`, `workflows/ui-review.md`, `workflows/validate-phase.md`
- `notes_or_session_utility`: `workflows/add-todo.md`, `workflows/check-todos.md`, `workflows/inbox.md`, `workflows/note.md`, `workflows/pause-work.md`, `workflows/session-report.md`
- `router_or_orchestrator`: `workflows/help.md`, `workflows/import.md`, `workflows/node-repair.md`, `workflows/settings.md`

## Files Not Yet Meaningfully Considered

- `workflows/discovery-phase.md`: called from `plan-phase.md` for mandatory discovery depth routing, but current Checkpoint 5 scope names `research-phase.md` / `plan-phase.md` and never dispositions the delegated discovery carrier.
- `workflows/discuss-phase-assumptions.md`: assumption-surfacing variant that still feeds `CONTEXT.md`-level planning inputs but is absent from current discuss-chain follow-through.
- `workflows/discuss-phase-power.md`: explicit `--power` mode variant of `discuss-phase.md` that still generates `CONTEXT.md`, yet current scope only names the standard discuss workflow.
- `workflows/do.md`: freeform dispatcher that can become a first-read surface for active Checkpoint 5 commands, but current scope artifacts never classify it.
- `workflows/list-phase-assumptions.md`: conversational assumptions surface adjacent to discuss/plan flow; current scope does not say whether stronger steering doctrine should reach it.
- `workflows/manager.md`: dashboard/orchestration surface that dispatches `discuss`, `plan`, and `execute`; current scope does not say whether it must reflect corrected workflow doctrine.
- `workflows/next.md`: automatic progression router over `discuss -> plan -> execute -> verify -> complete`; current scope patches `progress.md` / `transition.md` but does not disposition this adjacent routing surface.
- `workflows/quick.md`: alternate mini-pipeline with `discuss`, `research`, `plan-check`, `verification`, and code-review toggles; current Checkpoint 5 work is phase-chain-specific, but no artifact actually proves quick mode lies outside the same doctrine changes.
- `workflows/resume-project.md`: `continue` / `what's next` continuity surface that can present current-state truth after `progress.md` / `transition.md` changes, yet it is not presently in scope.
- `workflows/verify-phase.md`: goal-backward verifier executed from `execute-phase.md`; current debt-carrying completion work is changing execution/verification semantics without an explicit disposition for this verifier carrier.

## Strongest Misclassification Risks

1. `workflows/execute-plan.md` may be undercalled. `checkpoint-3-gsd-workflow-chain-and-artifact-contracts.md` treats execution authority as `execute-phase + execute-plan`, and `R5.17b` uses `execute-plan.md` as checkpoint-routing evidence. Leaving it at `qualified_pressure_only` is more honest than calling it outside, but it may still deserve promotion to `scope_gating_only` or stronger.
2. `workflows/code-review.md` may be undercalled. Checkpoint 4 already identified it as a real but deliberately non-blocking review surface, while current Track B scope narrows to `review.md` / `planner-reviews.md`. If closure-pressure hardening is meant to survive later reread, this omission may not hold.
3. `workflows/verify-phase.md` is a plausible propagation miss. It is the verification subagent surface that `execute-phase.md` actually spawns, yet current Checkpoint 5 wording concentrates on `execute-phase.md` and `verify-work.md` without saying whether goal-backward verification doctrine changes must land here.
4. `workflows/discuss-phase-power.md` is a plausible propagation miss. It is not a peripheral command; it is an alternate `discuss-phase` mode that still generates `CONTEXT.md`. Treating only standard `discuss-phase.md` as in-scope may be too narrow.
5. The router/orchestrator cluster (`do.md`, `manager.md`, `next.md`, `quick.md`, `resume-project.md`) is not proven outside the relevant sphere of influence. These files are first-read or alternate-entry surfaces for the same active lifecycle, so current omission is better read as under-consideration than as a defended exclusion.
6. The 49-file `outside_checkpoint_5` bucket is current practice, not fully earned proof. Most of those files were not directly reread under `R5.17` / `R5.18` conditions, so the bucket should be read as “currently outside the active frontier” rather than “file-level exclusion proven.”

## Read-Set Adequacy

- [d:c+r:i] Adequate for the narrow question this lane actually owes: what the current workflow-level modification-consideration map is, which workflows are explicitly in current first-wave scope, which remain mandatory or scope-gated, and which adjacent surfaces are being left outside by omission rather than by earned proof. Sources: `.planning/readiness/phase-01-rerun/GATES/checkpoint-5.md:45-57,67-92,109-121`; `.planning/readiness/phase-01-rerun/TASKS.md:12-22`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md:21-25,41-116`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18-bounded-promoted-corrective-scope-spec.md:62-72,74-145,158-258`.
- [d:c+r:i] Not adequate to claim that the full 49-file `outside_checkpoint_5` bucket is file-level proven. That would require direct rereads of many more peripheral workflows under the same anti-regret burden used on the currently active core. Current evidence supports the outside bucket as a truthful map of present treatment, not as a completed proof of non-implication. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-workflow-harness-scope-audit.md:70-72,103-106`; `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-17e-exclusion-adjudication-reread-internal-r1.md:17-32`; `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-17e-exclusion-adjudication-reread-cross-vendor-opus-1m-r1.md:74-104`.
