# Checkpoint 5 R5.19a4 Bin / Agent / Overlay / Runtime-Control Disposition Inventory Audit Internal R1

## Summary

- [d:c+r:i] The current bin / agent / overlay surface does not support an overlay-only modification frontier. The explicit `R5.18` Bucket 1 set inside this family is still only four files, but the stronger `R5.19b4` exclusion audit shows that leaving the live `.codex/agents/gsd-executor.toml` and `.codex/agents/gsd-verifier.toml` copies ambient is not a defensible non-modification story once their overlay counterparts are active. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18-bounded-promoted-corrective-scope-spec.md:92-100`; `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-19b4-bin-agent-overlay-exclusion-justification-audit-internal-r1.md:5-8,58-82`.
- [d:r:i] Across 92 inventoried files (24 `bin/lib` files, 62 live `.codex/agents` files, 5 tracked overlay agent files, and 1 `tooling/codex` helper), the current disposition map is: 4 `first_wave_r5_18`, 5 `mandatory_explicit_disposition`, 6 `scope_gating_only`, 0 `governing_authority_not_edit_now`, 1 `preserved_exclusion`, 9 `qualified_pressure_only`, 0 `not_yet_meaningfully_considered`, and 67 `outside_checkpoint_5`.
- [d:c+r:i] The only clean preserved exclusion in this lane remains `tooling/codex/capture_launch_truth.py`. `commands.cjs`, `uat.cjs`, and `audit.cjs` can stay out of Bucket 1 only as explicit-disposition files already inside active consideration, while the non-phase-critical agent remainder stays outside current Checkpoint 5 only as a bounded off-path judgment rather than as directory-wide per-file proof. Sources: `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-19b4-bin-agent-overlay-exclusion-justification-audit-internal-r1.md:9-16,18-52,43,106`.
- [o:c+r:i] The sharpest unresolved runtime-control boundary is the research / steering agent pair problem: the implementation spec still keeps `gsd-phase-researcher`, `gsd-planner`, and `gsd-plan-checker` overlay `.toml` files inside active ownership sets, while `R5.19b4` says the live `.codex/agents/*.toml` counterparts must move into explicit paired consideration if those tracks stay active. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md:41-71`; `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-19b4-bin-agent-overlay-exclusion-justification-audit-internal-r1.md:70-88`.
- [d:c+r:i] No file in this family currently earns `governing_authority_not_edit_now`. In the current package, authority-not-edit-now is carried by governance and readiness-control docs, not by runtime binaries or agent contracts. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18-bounded-promoted-corrective-scope-spec.md:194-208`; `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-19a-full-surface-disposition-inventory-audit-spec.md:82-105`.

## Method And Read Coverage

- [e:c:i] Governing read set covered the requested instruction/spec stack plus the readiness subtree requirements and the strongest already-written same-family comparison artifact: root `AGENTS.md`, `.planning/AGENTS.md`, `.planning/readiness/phase-01-rerun/AGENTS.md`, `INDEX.md`, `PLAN.md`, `STATUS.md`, `STATE.yaml`, `GATES/checkpoint-5.md`, `CHECKPOINT-REVIEW-MATRIX.md`, `REVIEW-POLICY.yaml`, `PROTOCOL.md`, the `R5.19` bundle spec, the `R5.19a` umbrella spec, the `R5.19a4` lane spec, `TASKS.md`, the revised Checkpoint 5 implementation spec, the provisional `R5.18` boundary artifact, the Checkpoint 3/4 runtime and agent-doctrine audits, the `R5.17d2` / `R5.17e` chain-tail rereads, and the existing `R5.19b4` exclusion-justification audit. Sources: `.planning/readiness/phase-01-rerun/AGENTS.md:11-38`; `.planning/readiness/phase-01-rerun/PROTOCOL.md:3-29`; `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-19a4-bin-agent-overlay-disposition-inventory-audit-spec.md:5-26`.
- [e:r:i] This lane used the same anti-misread rule as `R5.19a1`: classify current status from the strongest surviving scope sources, not from filename familiarity. Where `R5.18` already gave a file an explicit bucket, I kept that bucket. Where `R5.19b4` proved that current non-modification was under-justified, I did not clean the file back up into `preserved_exclusion`. Where current off-path status is only family-level bounded judgment, I kept the confidence at `medium` and marked the proof as bounded/family-level rather than per-file sovereign. Sources: `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-19a-full-surface-disposition-inventory-audit-spec.md:25-27,109-118`; `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-19b4-bin-agent-overlay-exclusion-justification-audit-internal-r1.md:106`.
- [e:r:i] Full coverage rule for this lane was: enumerate every file under `.codex/get-shit-done/bin/lib/`, `.codex/agents/`, `tooling/portable-gsd/overlay/agents/`, and `tooling/codex/`; apply explicit file-level `R5.18` / `R5.19b4` status where present; then use the Checkpoint 3/4 runtime and agent-doctrine maps to bound the remainder without inventing cleaner exclusion proof than the read set actually earned.

Basis legend:

- `B1`: explicit `first_wave_r5_18` chain-tail trunk for `.codex/get-shit-done/bin/lib/{phase,roadmap}.cjs` and `tooling/portable-gsd/overlay/agents/{gsd-executor,gsd-verifier}.toml`. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18-bounded-promoted-corrective-scope-spec.md:92-100`; `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-17d2-chain-tail-exclusion-adjudication-internal-r1.md:29`.
- `B2`: explicit `mandatory_explicit_disposition` for `commands.cjs`, `uat.cjs`, and `audit.cjs` because they can stay out of Bucket 1 only as named explicit-disposition files already inside active consideration. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18-bounded-promoted-corrective-scope-spec.md:132-145,162-178`; `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-19b4-bin-agent-overlay-exclusion-justification-audit-internal-r1.md:13-16,28-42`.
- `B3`: current omission of live `.codex/agents/gsd-executor.toml` and `.codex/agents/gsd-verifier.toml` is invalid; they must move into explicit `R5.18` consideration as live pairs of promoted overlay files. Sources: `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-19b4-bin-agent-overlay-exclusion-justification-audit-internal-r1.md:58-82`.
- `B4`: `scope_gating_only` for overlay/live `gsd-phase-researcher.toml`, `gsd-planner.toml`, and `gsd-plan-checker.toml` because the implementation spec keeps research/steering contract work active, while `R5.19b4` says paired live-agent consideration becomes mandatory if those tracks stay open. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md:41-71`; `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-19b4-bin-agent-overlay-exclusion-justification-audit-internal-r1.md:70-88`.
- `B5`: explicit `preserved_exclusion` for `tooling/codex/capture_launch_truth.py` as bounded launch-truth rendering cleanup outside the current debt/completion wave. Sources: `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-19b4-bin-agent-overlay-exclusion-justification-audit-internal-r1.md:18-24`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18-bounded-promoted-corrective-scope-spec.md:218-228`.
- `B6`: inferred `qualified_pressure_only` for current runtime/model-truth surfaces with real open findings but no current promotion into `R5.18`: `.codex/get-shit-done/bin/lib/{config,core,init,verify}.cjs` and the five phase-critical `.md` agent contracts. These files are materially implicated by Checkpoint 3/4 authority-drift findings, but the current implementation slice still keeps broader runtime reproducibility / launch-authority hardening out of first-wave scope. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-gsd-runtime-config-overlay-truth-excellence.md:46-47,66-67`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-gsd-agent-doctrine-and-role-contracts-excellence.md:39-41,56-60`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md:118-120`; `.planning/readiness/phase-01-rerun/STATUS.md:118-123`.
- `B7`: inferred `outside_checkpoint_5` for low-relevance `bin/lib` helpers and the non-phase-critical `.codex/agents` remainder. This is a bounded current-status judgment grounded in Checkpoint 3's phase-critical chain scoping plus `R5.19b4`'s surviving exclusion for the non-phase-critical `.codex/agents/*.toml` remainder, not a permanent per-file exemption certificate. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-agent-doctrine-and-role-contracts.md:32,51-53`; `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-19b4-bin-agent-overlay-exclusion-justification-audit-internal-r1.md:43,53-57,106`.

## Disposition Counts

| disposition | count |
| --- | ---: |
| `first_wave_r5_18` | 4 |
| `mandatory_explicit_disposition` | 5 |
| `scope_gating_only` | 6 |
| `governing_authority_not_edit_now` | 0 |
| `preserved_exclusion` | 1 |
| `qualified_pressure_only` | 9 |
| `not_yet_meaningfully_considered` | 0 |
| `outside_checkpoint_5` | 67 |

## Full Disposition Inventory

| path | family | current disposition | basis | explicit_or_inferred | directly_challenged_in_r5_17 | relevance_mode | exclusion_proven | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `.codex/get-shit-done/bin/lib/audit.cjs` | `bin_lib` | `mandatory_explicit_disposition` | `B2` | explicit | `yes (qualified widening only)` | `both` | `n/a` | medium |
| `.codex/get-shit-done/bin/lib/commands.cjs` | `bin_lib` | `mandatory_explicit_disposition` | `B2` | explicit | `yes` | `both` | `n/a` | medium |
| `.codex/get-shit-done/bin/lib/config.cjs` | `bin_lib` | `qualified_pressure_only` | `B6` | inferred | `no` | `both` | `no` | medium |
| `.codex/get-shit-done/bin/lib/core.cjs` | `bin_lib` | `qualified_pressure_only` | `B6` | inferred | `no` | `both` | `no` | medium |
| `.codex/get-shit-done/bin/lib/docs.cjs` | `bin_lib` | `outside_checkpoint_5` | `B7` | inferred | `no` | `independent_surface` | `yes` | medium |
| `.codex/get-shit-done/bin/lib/frontmatter.cjs` | `bin_lib` | `outside_checkpoint_5` | `B7` | inferred | `no` | `independent_surface` | `yes` | medium |
| `.codex/get-shit-done/bin/lib/graphify.cjs` | `bin_lib` | `outside_checkpoint_5` | `B7` | inferred | `no` | `independent_surface` | `yes` | medium |
| `.codex/get-shit-done/bin/lib/gsd2-import.cjs` | `bin_lib` | `outside_checkpoint_5` | `B7` | inferred | `no` | `independent_surface` | `yes` | medium |
| `.codex/get-shit-done/bin/lib/init.cjs` | `bin_lib` | `qualified_pressure_only` | `B6` | inferred | `no` | `both` | `no` | medium |
| `.codex/get-shit-done/bin/lib/intel.cjs` | `bin_lib` | `outside_checkpoint_5` | `B7` | inferred | `no` | `independent_surface` | `yes` | medium |
| `.codex/get-shit-done/bin/lib/learnings.cjs` | `bin_lib` | `outside_checkpoint_5` | `B7` | inferred | `no` | `independent_surface` | `yes` | medium |
| `.codex/get-shit-done/bin/lib/milestone.cjs` | `bin_lib` | `outside_checkpoint_5` | `B7` | inferred | `no` | `independent_surface` | `yes` | medium |
| `.codex/get-shit-done/bin/lib/model-profiles.cjs` | `bin_lib` | `outside_checkpoint_5` | `B7` | inferred | `no` | `independent_surface` | `yes` | medium |
| `.codex/get-shit-done/bin/lib/phase.cjs` | `bin_lib` | `first_wave_r5_18` | `B1` | explicit | `yes` | `both` | `n/a` | high |
| `.codex/get-shit-done/bin/lib/profile-output.cjs` | `bin_lib` | `outside_checkpoint_5` | `B7` | inferred | `no` | `independent_surface` | `yes` | medium |
| `.codex/get-shit-done/bin/lib/profile-pipeline.cjs` | `bin_lib` | `outside_checkpoint_5` | `B7` | inferred | `no` | `independent_surface` | `yes` | medium |
| `.codex/get-shit-done/bin/lib/roadmap.cjs` | `bin_lib` | `first_wave_r5_18` | `B1` | explicit | `yes` | `both` | `n/a` | high |
| `.codex/get-shit-done/bin/lib/schema-detect.cjs` | `bin_lib` | `outside_checkpoint_5` | `B7` | inferred | `no` | `independent_surface` | `yes` | medium |
| `.codex/get-shit-done/bin/lib/security.cjs` | `bin_lib` | `outside_checkpoint_5` | `B7` | inferred | `no` | `independent_surface` | `yes` | medium |
| `.codex/get-shit-done/bin/lib/state.cjs` | `bin_lib` | `outside_checkpoint_5` | `B7` | inferred | `no` | `independent_surface` | `yes` | medium |
| `.codex/get-shit-done/bin/lib/template.cjs` | `bin_lib` | `outside_checkpoint_5` | `B7` | inferred | `no` | `independent_surface` | `yes` | medium |
| `.codex/get-shit-done/bin/lib/uat.cjs` | `bin_lib` | `mandatory_explicit_disposition` | `B2` | explicit | `yes (qualified widening only)` | `both` | `n/a` | medium |
| `.codex/get-shit-done/bin/lib/verify.cjs` | `bin_lib` | `qualified_pressure_only` | `B6` | inferred | `no` | `both` | `no` | medium |
| `.codex/get-shit-done/bin/lib/workstream.cjs` | `bin_lib` | `outside_checkpoint_5` | `B7` | inferred | `no` | `independent_surface` | `yes` | medium |
| `.codex/agents/gsd-advisor-researcher.md` | `live_agent_md` | `outside_checkpoint_5` | `B7` | inferred | `no` | `independent_surface` | `yes (family-level)` | medium |
| `.codex/agents/gsd-advisor-researcher.toml` | `live_agent_toml` | `outside_checkpoint_5` | `B7` | inferred | `no` | `independent_surface` | `yes (family-level)` | medium |
| `.codex/agents/gsd-ai-researcher.md` | `live_agent_md` | `outside_checkpoint_5` | `B7` | inferred | `no` | `independent_surface` | `yes (family-level)` | medium |
| `.codex/agents/gsd-ai-researcher.toml` | `live_agent_toml` | `outside_checkpoint_5` | `B7` | inferred | `no` | `independent_surface` | `yes (family-level)` | medium |
| `.codex/agents/gsd-assumptions-analyzer.md` | `live_agent_md` | `outside_checkpoint_5` | `B7` | inferred | `no` | `independent_surface` | `yes (family-level)` | medium |
| `.codex/agents/gsd-assumptions-analyzer.toml` | `live_agent_toml` | `outside_checkpoint_5` | `B7` | inferred | `no` | `independent_surface` | `yes (family-level)` | medium |
| `.codex/agents/gsd-code-fixer.md` | `live_agent_md` | `outside_checkpoint_5` | `B7` | inferred | `no` | `independent_surface` | `yes (family-level)` | medium |
| `.codex/agents/gsd-code-fixer.toml` | `live_agent_toml` | `outside_checkpoint_5` | `B7` | inferred | `no` | `independent_surface` | `yes (family-level)` | medium |
| `.codex/agents/gsd-code-reviewer.md` | `live_agent_md` | `outside_checkpoint_5` | `B7` | inferred | `no` | `independent_surface` | `yes (family-level)` | medium |
| `.codex/agents/gsd-code-reviewer.toml` | `live_agent_toml` | `outside_checkpoint_5` | `B7` | inferred | `no` | `independent_surface` | `yes (family-level)` | medium |
| `.codex/agents/gsd-codebase-mapper.md` | `live_agent_md` | `outside_checkpoint_5` | `B7` | inferred | `no` | `independent_surface` | `yes (family-level)` | medium |
| `.codex/agents/gsd-codebase-mapper.toml` | `live_agent_toml` | `outside_checkpoint_5` | `B7` | inferred | `no` | `independent_surface` | `yes (family-level)` | medium |
| `.codex/agents/gsd-debug-session-manager.md` | `live_agent_md` | `outside_checkpoint_5` | `B7` | inferred | `no` | `independent_surface` | `yes (family-level)` | medium |
| `.codex/agents/gsd-debug-session-manager.toml` | `live_agent_toml` | `outside_checkpoint_5` | `B7` | inferred | `no` | `independent_surface` | `yes (family-level)` | medium |
| `.codex/agents/gsd-debugger.md` | `live_agent_md` | `outside_checkpoint_5` | `B7` | inferred | `no` | `independent_surface` | `yes (family-level)` | medium |
| `.codex/agents/gsd-debugger.toml` | `live_agent_toml` | `outside_checkpoint_5` | `B7` | inferred | `no` | `independent_surface` | `yes (family-level)` | medium |
| `.codex/agents/gsd-doc-verifier.md` | `live_agent_md` | `outside_checkpoint_5` | `B7` | inferred | `no` | `independent_surface` | `yes (family-level)` | medium |
| `.codex/agents/gsd-doc-verifier.toml` | `live_agent_toml` | `outside_checkpoint_5` | `B7` | inferred | `no` | `independent_surface` | `yes (family-level)` | medium |
| `.codex/agents/gsd-doc-writer.md` | `live_agent_md` | `outside_checkpoint_5` | `B7` | inferred | `no` | `independent_surface` | `yes (family-level)` | medium |
| `.codex/agents/gsd-doc-writer.toml` | `live_agent_toml` | `outside_checkpoint_5` | `B7` | inferred | `no` | `independent_surface` | `yes (family-level)` | medium |
| `.codex/agents/gsd-domain-researcher.md` | `live_agent_md` | `outside_checkpoint_5` | `B7` | inferred | `no` | `independent_surface` | `yes (family-level)` | medium |
| `.codex/agents/gsd-domain-researcher.toml` | `live_agent_toml` | `outside_checkpoint_5` | `B7` | inferred | `no` | `independent_surface` | `yes (family-level)` | medium |
| `.codex/agents/gsd-eval-auditor.md` | `live_agent_md` | `outside_checkpoint_5` | `B7` | inferred | `no` | `independent_surface` | `yes (family-level)` | medium |
| `.codex/agents/gsd-eval-auditor.toml` | `live_agent_toml` | `outside_checkpoint_5` | `B7` | inferred | `no` | `independent_surface` | `yes (family-level)` | medium |
| `.codex/agents/gsd-eval-planner.md` | `live_agent_md` | `outside_checkpoint_5` | `B7` | inferred | `no` | `independent_surface` | `yes (family-level)` | medium |
| `.codex/agents/gsd-eval-planner.toml` | `live_agent_toml` | `outside_checkpoint_5` | `B7` | inferred | `no` | `independent_surface` | `yes (family-level)` | medium |
| `.codex/agents/gsd-executor.md` | `live_agent_md` | `qualified_pressure_only` | `B6` | inferred | `no` | `both` | `no` | medium |
| `.codex/agents/gsd-executor.toml` | `live_agent_toml` | `mandatory_explicit_disposition` | `B3` | inferred | `no` | `both` | `n/a` | high |
| `.codex/agents/gsd-framework-selector.md` | `live_agent_md` | `outside_checkpoint_5` | `B7` | inferred | `no` | `independent_surface` | `yes (family-level)` | medium |
| `.codex/agents/gsd-framework-selector.toml` | `live_agent_toml` | `outside_checkpoint_5` | `B7` | inferred | `no` | `independent_surface` | `yes (family-level)` | medium |
| `.codex/agents/gsd-integration-checker.md` | `live_agent_md` | `outside_checkpoint_5` | `B7` | inferred | `no` | `independent_surface` | `yes (family-level)` | medium |
| `.codex/agents/gsd-integration-checker.toml` | `live_agent_toml` | `outside_checkpoint_5` | `B7` | inferred | `no` | `independent_surface` | `yes (family-level)` | medium |
| `.codex/agents/gsd-intel-updater.md` | `live_agent_md` | `outside_checkpoint_5` | `B7` | inferred | `no` | `independent_surface` | `yes (family-level)` | medium |
| `.codex/agents/gsd-intel-updater.toml` | `live_agent_toml` | `outside_checkpoint_5` | `B7` | inferred | `no` | `independent_surface` | `yes (family-level)` | medium |
| `.codex/agents/gsd-nyquist-auditor.md` | `live_agent_md` | `outside_checkpoint_5` | `B7` | inferred | `no` | `independent_surface` | `yes (family-level)` | medium |
| `.codex/agents/gsd-nyquist-auditor.toml` | `live_agent_toml` | `outside_checkpoint_5` | `B7` | inferred | `no` | `independent_surface` | `yes (family-level)` | medium |
| `.codex/agents/gsd-pattern-mapper.md` | `live_agent_md` | `outside_checkpoint_5` | `B7` | inferred | `no` | `independent_surface` | `yes (family-level)` | medium |
| `.codex/agents/gsd-pattern-mapper.toml` | `live_agent_toml` | `outside_checkpoint_5` | `B7` | inferred | `no` | `independent_surface` | `yes (family-level)` | medium |
| `.codex/agents/gsd-phase-researcher.md` | `live_agent_md` | `qualified_pressure_only` | `B6` | inferred | `no` | `both` | `no` | medium |
| `.codex/agents/gsd-phase-researcher.toml` | `live_agent_toml` | `scope_gating_only` | `B4` | inferred | `no` | `both` | `n/a` | medium |
| `.codex/agents/gsd-plan-checker.md` | `live_agent_md` | `qualified_pressure_only` | `B6` | inferred | `no` | `both` | `no` | medium |
| `.codex/agents/gsd-plan-checker.toml` | `live_agent_toml` | `scope_gating_only` | `B4` | inferred | `no` | `both` | `n/a` | medium |
| `.codex/agents/gsd-planner.md` | `live_agent_md` | `qualified_pressure_only` | `B6` | inferred | `no` | `both` | `no` | medium |
| `.codex/agents/gsd-planner.toml` | `live_agent_toml` | `scope_gating_only` | `B4` | inferred | `no` | `both` | `n/a` | medium |
| `.codex/agents/gsd-project-researcher.md` | `live_agent_md` | `outside_checkpoint_5` | `B7` | inferred | `no` | `independent_surface` | `yes (family-level)` | medium |
| `.codex/agents/gsd-project-researcher.toml` | `live_agent_toml` | `outside_checkpoint_5` | `B7` | inferred | `no` | `independent_surface` | `yes (family-level)` | medium |
| `.codex/agents/gsd-research-synthesizer.md` | `live_agent_md` | `outside_checkpoint_5` | `B7` | inferred | `no` | `independent_surface` | `yes (family-level)` | medium |
| `.codex/agents/gsd-research-synthesizer.toml` | `live_agent_toml` | `outside_checkpoint_5` | `B7` | inferred | `no` | `independent_surface` | `yes (family-level)` | medium |
| `.codex/agents/gsd-roadmapper.md` | `live_agent_md` | `outside_checkpoint_5` | `B7` | inferred | `no` | `independent_surface` | `yes (family-level)` | medium |
| `.codex/agents/gsd-roadmapper.toml` | `live_agent_toml` | `outside_checkpoint_5` | `B7` | inferred | `no` | `independent_surface` | `yes (family-level)` | medium |
| `.codex/agents/gsd-security-auditor.md` | `live_agent_md` | `outside_checkpoint_5` | `B7` | inferred | `no` | `independent_surface` | `yes (family-level)` | medium |
| `.codex/agents/gsd-security-auditor.toml` | `live_agent_toml` | `outside_checkpoint_5` | `B7` | inferred | `no` | `independent_surface` | `yes (family-level)` | medium |
| `.codex/agents/gsd-ui-auditor.md` | `live_agent_md` | `outside_checkpoint_5` | `B7` | inferred | `no` | `independent_surface` | `yes (family-level)` | medium |
| `.codex/agents/gsd-ui-auditor.toml` | `live_agent_toml` | `outside_checkpoint_5` | `B7` | inferred | `no` | `independent_surface` | `yes (family-level)` | medium |
| `.codex/agents/gsd-ui-checker.md` | `live_agent_md` | `outside_checkpoint_5` | `B7` | inferred | `no` | `independent_surface` | `yes (family-level)` | medium |
| `.codex/agents/gsd-ui-checker.toml` | `live_agent_toml` | `outside_checkpoint_5` | `B7` | inferred | `no` | `independent_surface` | `yes (family-level)` | medium |
| `.codex/agents/gsd-ui-researcher.md` | `live_agent_md` | `outside_checkpoint_5` | `B7` | inferred | `no` | `independent_surface` | `yes (family-level)` | medium |
| `.codex/agents/gsd-ui-researcher.toml` | `live_agent_toml` | `outside_checkpoint_5` | `B7` | inferred | `no` | `independent_surface` | `yes (family-level)` | medium |
| `.codex/agents/gsd-user-profiler.md` | `live_agent_md` | `outside_checkpoint_5` | `B7` | inferred | `no` | `independent_surface` | `yes (family-level)` | medium |
| `.codex/agents/gsd-user-profiler.toml` | `live_agent_toml` | `outside_checkpoint_5` | `B7` | inferred | `no` | `independent_surface` | `yes (family-level)` | medium |
| `.codex/agents/gsd-verifier.md` | `live_agent_md` | `qualified_pressure_only` | `B6` | inferred | `no` | `both` | `no` | medium |
| `.codex/agents/gsd-verifier.toml` | `live_agent_toml` | `mandatory_explicit_disposition` | `B3` | inferred | `no` | `both` | `n/a` | high |
| `tooling/portable-gsd/overlay/agents/gsd-executor.toml` | `overlay_agent_toml` | `first_wave_r5_18` | `B1` | explicit | `yes` | `both` | `n/a` | high |
| `tooling/portable-gsd/overlay/agents/gsd-phase-researcher.toml` | `overlay_agent_toml` | `scope_gating_only` | `B4` | inferred | `no` | `both` | `n/a` | medium |
| `tooling/portable-gsd/overlay/agents/gsd-plan-checker.toml` | `overlay_agent_toml` | `scope_gating_only` | `B4` | inferred | `no` | `both` | `n/a` | medium |
| `tooling/portable-gsd/overlay/agents/gsd-planner.toml` | `overlay_agent_toml` | `scope_gating_only` | `B4` | inferred | `no` | `both` | `n/a` | medium |
| `tooling/portable-gsd/overlay/agents/gsd-verifier.toml` | `overlay_agent_toml` | `first_wave_r5_18` | `B1` | explicit | `yes` | `both` | `n/a` | high |
| `tooling/codex/capture_launch_truth.py` | `tooling_codex` | `preserved_exclusion` | `B5` | explicit | `yes (qualified chain-tail widening)` | `independent_surface` | `yes` | high |

## Files Currently Excluded From Modification Consideration

- [d:r:i] `preserved_exclusion` (1): `tooling/codex/capture_launch_truth.py`.
- [d:r:i] `qualified_pressure_only` (9): `.codex/get-shit-done/bin/lib/{config,core,init,verify}.cjs`; `.codex/agents/{gsd-phase-researcher,gsd-planner,gsd-plan-checker,gsd-executor,gsd-verifier}.md`.
- [d:r:i] `outside_checkpoint_5` (67): all remaining non-phase-critical `.codex/agents/*` files plus the low-relevance `bin/lib` helper remainder (`docs`, `frontmatter`, `graphify`, `gsd2-import`, `intel`, `learnings`, `milestone`, `model-profiles`, `profile-output`, `profile-pipeline`, `schema-detect`, `security`, `state`, `template`, `workstream`). The full per-file list is in the inventory table.
- [d:c+r:i] These 77 currently excluded files are not one evidential bucket. `capture_launch_truth.py` is a clean preserved exclusion; the 9 `qualified_pressure_only` files carry live relevance without proven non-modification; and the 67 `outside_checkpoint_5` calls are bounded current-status judgments, especially for the non-phase-critical agent remainder. Sources: `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-19b4-bin-agent-overlay-exclusion-justification-audit-internal-r1.md:18-24,43,106`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-gsd-runtime-config-overlay-truth-excellence.md:46-47,66-67`.

## Files Not Yet Meaningfully Considered

- [d:r:i] None currently carry the `not_yet_meaningfully_considered` label in this lane.
- [d:c+r:i] That is not a claim of perfect per-file proof. It means the current read set was strong enough to place the remainder either into active consideration, bounded off-path exclusion, or qualified pressure, especially after incorporating the stronger `R5.19b4` exclusion audit. Sources: `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-19b4-bin-agent-overlay-exclusion-justification-audit-internal-r1.md:106`; `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-19a-full-surface-disposition-inventory-audit-spec.md:25-27`.

## Strongest Misclassification Risks

- [o:c+r:i] `.codex/agents/gsd-executor.toml` and `.codex/agents/gsd-verifier.toml` may already deserve `first_wave_r5_18`, not merely `mandatory_explicit_disposition`. `R5.19b4` says current non-modification is invalid, and the only reason not to mark them first-wave already is that the live `R5.18` artifact has not yet absorbed the paired-agent correction. Sources: `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-19b4-bin-agent-overlay-exclusion-justification-audit-internal-r1.md:58-82`.
- [o:c+r:i] The six `scope_gating_only` research / steering `.toml` files may need to move to `mandatory_explicit_disposition` or even active patch-now treatment if `R5.18` keeps the research-disposition and wider steering-consumer branches active rather than narrowing them. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-workflow-follow-through-implementation-spec.md:41-71`; `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-19b4-bin-agent-overlay-exclusion-justification-audit-internal-r1.md:70-88`.
- [o:c+r:i] The five phase-critical `.md` agent contracts may be undercalled at `qualified_pressure_only`. Checkpoint 3/4 repeatedly identified the `.md` versus `.toml` split as unresolved and reversal-sensitive; if the repo later decides human-facing agent docs must stop lagging runtime contract truth, these five files would likely need explicit paired disposition rather than pressure-only status. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-agent-doctrine-and-role-contracts.md:44-45,74`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-gsd-agent-doctrine-and-role-contracts-excellence.md:39,56-60`.
- [o:c+r:i] `.codex/get-shit-done/bin/lib/{config,core,init,verify}.cjs` may also be undercalled at `qualified_pressure_only` if Track C reopens broader launch/model-truth capture into runtime model-authority or install-truth hardening. The runtime/config lane already showed these surfaces are where loader truth, model resolution, and agent-install warnings actually live. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-runtime-config-overlay-truth.md:34-49`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-gsd-runtime-config-overlay-truth-excellence.md:46-47,66-67`.
- [o:c+r:i] Some non-phase-critical agent exclusions could later reopen if Checkpoint 5 widens from the rerun-critical path into off-path review or audit machinery. `R5.19b4` itself warns that the current surviving exclusion for that remainder is family-level bounded judgment, not directory-wide per-file certification. Sources: `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-19b4-bin-agent-overlay-exclusion-justification-audit-internal-r1.md:43,106`.

## Read-Set Adequacy

- [d:c+r:i] Adequate for current-status inventory: every file in the requested family was inventoried, the explicit `R5.18` frontier inside this family was carried through unchanged where it already exists, and the stronger `R5.19b4` audit was used to prevent false preserved-exclusion calls on live `.codex/agents` executor/verifier pairs. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18-bounded-promoted-corrective-scope-spec.md:92-100,132-145,218-228`; `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-19b4-bin-agent-overlay-exclusion-justification-audit-internal-r1.md:5-16,58-88`.
- [d:c+r:i] Also adequate to distinguish three different kinds of "currently excluded" outcome in this family: a clean preserved exclusion (`capture_launch_truth.py`), real-but-unpromoted qualified pressure on runtime truth surfaces, and bounded off-path exclusion for the non-phase-critical remainder. That is the main epistemic job of this lane. Sources: `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-19a-full-surface-disposition-inventory-audit-spec.md:25-27,109-118`; `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-19b4-bin-agent-overlay-exclusion-justification-audit-internal-r1.md:18-24,43,106`.
- [o:c+r:i] Not adequate for permanent per-file proof of every one of the 67 `outside_checkpoint_5` rows. For the non-phase-critical `.codex/agents` remainder especially, current status is a bounded rerun-path judgment, not a forever exemption. If Track B/C later widens into code-review, doc, UI, or other off-path agent consumers, those rows should be reread directly rather than treated as settled by inheritance. Sources: `.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-19b4-bin-agent-overlay-exclusion-justification-audit-internal-r1.md:43,106`.
