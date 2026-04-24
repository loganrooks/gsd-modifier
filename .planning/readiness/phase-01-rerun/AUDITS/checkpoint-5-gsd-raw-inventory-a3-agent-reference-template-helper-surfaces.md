# Checkpoint 5 GSD Raw Inventory A3: Agent, Reference, Template, And Helper Surfaces

## Incomplete State

Complete. The durability placeholder was created first and then cleared after the scoped inventory pass.

## Research Frame

- [g:c:i] This lane inventories the contract-carrying and helper/control surfaces that sit below the workflow-wrapper picture: agent role files under `.codex/agents/`, doctrine and contract refs under `.codex/get-shit-done/references/`, artifact and prompt templates under `.codex/get-shit-done/templates/`, and the helper/runtime-control code under `.codex/get-shit-done/bin/` and `bin/lib/`. Sources: `AGENTS.md:39-45`; `.planning/AGENTS.md:42-82`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-a3-agent-reference-template-helper-surfaces-spec.md:3-20,31-77`.
- [s:c:i] I kept three visibly separate buckets throughout: `agents`, `references/templates`, and `helper/runtime-control surfaces`. I preserved cross-cutting and ambiguous items rather than collapsing them into one support bucket. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-bundle-spec.md:23-37,66-90,112-127`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-a3-agent-reference-template-helper-surfaces-spec.md:15-20,70-77`.
- [d:r:i] For comparison against the current picture, I used the current local-topology schema plus prior agent/runtime audits as governing baselines, because this lane is about omission detection rather than rebuilding ontology from zero. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-local-topology-schema.md:144-200`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-agent-doctrine-and-role-contracts.md:18-76`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-runtime-config-overlay-truth.md:46-76`.

## Path Of Inquiry

1. [e:c:i] I read root governance, planning-local governance, the lane spec, and the bundle spec first, then created this artifact immediately with the required headings and an `Incomplete State` note per the durability protocol. Sources: `AGENTS.md:39-45,96-124`; `.planning/AGENTS.md:42-82,114-121`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-a3-agent-reference-template-helper-surfaces-spec.md:21-82`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-bundle-spec.md:38-64,121-127`.
2. [e:r:i] I mapped the scoped runtime directories with `rg --files` and then sampled only the load-bearing files using narrow `nl -ba` windows: core phase-chain agents, selected auxiliary agents, contract references, artifact/prompt templates, and the helper code that reads or enforces them. Basis: direct targeted reads under `.codex/agents/`, `.codex/get-shit-done/references/`, `.codex/get-shit-done/templates/`, `.codex/get-shit-done/bin/`, and `.codex/get-shit-done/bin/lib/`.
3. [e:c+i] I used prior readiness artifacts only where classification required comparison with the existing high-level map: the current local topology schema for what is already represented, the Checkpoint 3 agent-doctrine lane for core-role focus and explicit open inquiry debt, and the runtime/config lane for the `.md`/`.toml` authority split and template-vs-loader seams. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-local-topology-schema.md:152,159,178-180,194-200`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-agent-doctrine-and-role-contracts.md:24-76`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-runtime-config-overlay-truth.md:48-76`.
4. [s:r:i] I did not widen into general repo code, home-level Reflect paths, or unrelated workflow trees. I also did not open the repo-local `gsd-rigorous-research` skill body because the lane’s explicit read-set constraint was narrower; I followed the same scoped, evidence-first discipline directly inside the allowed surface set. Basis: lane constraint plus observed inquiry path.

## Agent Surface Ledger

### A1. Core phase-chain `.md` worker contracts

`surface`: Core human-readable phase-chain agent prompts for researcher, planner, checker, executor, and verifier.

`path`: `.codex/agents/gsd-phase-researcher.md:1-34,59-103`; `.codex/agents/gsd-planner.md:1-35,47-124`; `.codex/agents/gsd-plan-checker.md:1-39,55-90`; `.codex/agents/gsd-executor.md:1-22,51-140`; `.codex/agents/gsd-verifier.md:1-30,60-109`.

`repo-local role as stated by source`: [e:c:i] These files declare the actual role narratives for the phase-critical chain: research before planning, executable prompt-plan creation, pre-execution skepticism, bounded execution with deviation rules, and post-execution goal-backward verification. Sources: `.codex/agents/gsd-phase-researcher.md:13-34,88-103`; `.codex/agents/gsd-planner.md:13-35,62-124`; `.codex/agents/gsd-plan-checker.md:13-31,70-90`; `.codex/agents/gsd-executor.md:13-22,68-140`; `.codex/agents/gsd-verifier.md:13-30,46-58,88-109`.

`reads/expects`: `required_reading` / repo governance via `AGENTS.md` and often `.planning/AGENTS.md`; phase artifacts such as `CONTEXT.md`, `RESEARCH.md`, `PLAN.md`, `SUMMARY.md`, roadmap-derived must-haves, and shared doctrine refs such as `gates.md`, `checkpoints.md`, and the thinking-model files. Sources: `.codex/agents/gsd-phase-researcher.md:18-20,59-86`; `.codex/agents/gsd-planner.md:24-35,47-91`; `.codex/agents/gsd-plan-checker.md:20-39,55-68,94-99`; `.codex/agents/gsd-executor.md:20-22,70-95,116-140`; `.codex/agents/gsd-verifier.md:18-30,62-109`.

`emits/returns`: `RESEARCH.md`, `PLAN.md`, `SUMMARY.md`, `VERIFICATION.md`, plus completion or escalation markers consumed by orchestration. Sources: `.codex/agents/gsd-phase-researcher.md:21-33,88-103`; `.codex/agents/gsd-planner.md:22-35`; `.codex/get-shit-done/references/agent-contracts.md:11-24,47-91`.

`downstream consumers`: `plan-phase`, `execute-phase`, `verify-work`, adjacent workers in the phase chain, and helper code that reads artifact fields or completion status. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-agent-doctrine-and-role-contracts.md:27-31,60-62`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-local-topology-schema.md:154-155,194-200`.

`obvious relations`: `agent-contracts.md`, `gates.md`, `checkpoints.md`, `thinking-models-{planning,execution,verification}.md`, `phase-prompt.md`, `context.md`, and the helper control path in `gsd-tools.cjs` plus `init.cjs`.

`candidate loose tags`: `core-phase-chain`, `prompt-contract`, `AGENTS-aware`, `artifact-producer`, `workflow-consumed`.

`intervention status`: `tracked overlay / live runtime for the phase-critical chain`, with later runtime truth still dependent on launch authority evidence rather than prompt text alone. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-local-topology-schema.md:159,198-200`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-runtime-config-overlay-truth.md:48-53`.

`classification status`: `placed provisionally`

`confidence`: `high`

`unresolved classification`: These files are clearly contract-carrying, but they are not proved to be the sole launch-authoritative worker surface because `.toml` siblings remain active in the runtime registry.

### A2. Core phase-chain `.toml` registry prompts

`surface`: Codex-registered worker prompt/config surfaces for the same core phase chain.

`path`: `.codex/agents/gsd-phase-researcher.toml:1-27,29-79`; `.codex/agents/gsd-planner.toml:1-35,37-96`; `.codex/agents/gsd-executor.toml:1-39,41-110`.

`repo-local role as stated by source`: [e:c+r:i] These files duplicate the worker roles as `developer_instructions` and also carry per-agent `model_reasoning_effort`, but they still preserve older doctrine in places, including `CLAUDE.md` and legacy skill-location assumptions, rather than the repo’s newer `AGENTS.md` / `.codex/skills/` framing. Sources: `.codex/agents/gsd-phase-researcher.toml:29-44`; `.codex/agents/gsd-planner.toml:37-50,52-96`; `.codex/agents/gsd-executor.toml:24-39`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-runtime-config-overlay-truth.md:50-53`.

`reads/expects`: `<files_to_read>` blocks, repo instructions, model-selection inputs, and the same phase artifacts the `.md` chain expects. Sources: `.codex/agents/gsd-phase-researcher.toml:11-19,29-61`; `.codex/agents/gsd-planner.toml:17-35,37-96`; `.codex/agents/gsd-executor.toml:13-22,24-68`.

`emits/returns`: The same core phase artifacts and structured completion returns the `.md` family claims to produce. Sources: `.codex/agents/gsd-phase-researcher.toml:14-27,63-79`; `.codex/agents/gsd-planner.toml:20-28`; `.codex/agents/gsd-executor.toml:7-15,43-108`.

`downstream consumers`: Named subagent launches, model-resolution logic, and any install/post-install mutation path that rewrites reasoning defaults. Sources: `.codex/get-shit-done/bin/lib/core.cjs:1343-1373`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-runtime-config-overlay-truth.md:48-59`.

`obvious relations`: `.md` siblings, `model-profiles.cjs`, `references/model-profiles.md`, and the `checkAgentsInstalled()` vs runtime-registry split surfaced earlier.

`candidate loose tags`: `worker-registry`, `prompt-config`, `reasoning-policy`, `dual-authority`, `stale-doctrine-risk`.

`intervention status`: `mixed live runtime / tracked overlay for core five; broader family status unresolved in this lane`. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-local-topology-schema.md:159`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-runtime-config-overlay-truth.md:48-59,73`.

`classification status`: `ambiguous`

`confidence`: `medium-high`

`unresolved classification`: The main open question is not whether these are real surfaces, but whether they are the dominant worker authority at launch versus the `.md` family.

### A3. Advisor / discuss helper seam

`surface`: Single-gray-area advisor researcher used by discuss-phase advisor mode.

`path`: `.codex/agents/gsd-advisor-researcher.toml:1-25,40-124`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-agent-doctrine-and-role-contracts.md:26,46,53,75`.

`repo-local role as stated by source`: [e:c:i] This worker is scoped tightly: research one gray area, produce one comparison table, return it to the main orchestrator, and avoid user-facing synthesis. Sources: `.codex/agents/gsd-advisor-researcher.toml:5-15,69-97`.

`reads/expects`: `<gray_area>`, `<phase_context>`, `<project_context>`, and a calibration tier controlling output shape; library docs via Context7/WebFetch/WebSearch if needed. Sources: `.codex/agents/gsd-advisor-researcher.toml:17-47,49-67,99-114`.

`emits/returns`: Exactly one comparison table plus rationale paragraph in a fixed 5-column format. Sources: `.codex/agents/gsd-advisor-researcher.toml:69-88`.

`downstream consumers`: `discuss-phase` advisor orchestration, not the end user directly. Sources: `.codex/agents/gsd-advisor-researcher.toml:6-15`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-agent-doctrine-and-role-contracts.md:26,46,53`.

`obvious relations`: `discuss-phase` advisor path, `universal-anti-patterns.md`, and the broader `general-purpose` seam from prior audits.

`candidate loose tags`: `optional-discuss-helper`, `single-question-research`, `structured-comparison`, `adapter-seam`.

`intervention status`: `mostly upstream/base live surface; invocation path remains a repo-local seam rather than a settled named-agent flow`. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-agent-doctrine-and-role-contracts.md:38,46,53`.

`classification status`: `ambiguous`

`confidence`: `medium`

`unresolved classification`: This surface is real, but its actual launch path appears adapter-mediated rather than cleanly `subagent_type="gsd-advisor-researcher"`.

### A4. Design-contract specialist lane

`surface`: UI-design contract worker family represented here by `gsd-ui-researcher`.

`path`: `.codex/agents/gsd-ui-researcher.md:13-27,67-104,108-136,140-220`; `.codex/get-shit-done/templates/UI-SPEC.md:1-100`.

`repo-local role as stated by source`: [e:c:i] This worker turns upstream product/phase artifacts plus existing design-system state into a prescriptive `UI-SPEC.md` contract, asks only unanswered questions, and adds a third-party registry safety gate before contract acceptance. Sources: `.codex/agents/gsd-ui-researcher.md:13-27,67-104,140-220`.

`reads/expects`: `CONTEXT.md`, `RESEARCH.md`, `REQUIREMENTS.md`, local design-system files, component inventory, and optionally shadcn state. Sources: `.codex/agents/gsd-ui-researcher.md:67-91,120-159`.

`emits/returns`: `UI-SPEC.md` plus structured `UI-SPEC COMPLETE` / `UI-SPEC BLOCKED` returns. Sources: `.codex/agents/gsd-ui-researcher.md:226-352`; `.codex/get-shit-done/templates/UI-SPEC.md:1-100`.

`downstream consumers`: `gsd-ui-checker`, `gsd-planner`, `gsd-executor`, and `gsd-ui-auditor`. Sources: `.codex/agents/gsd-ui-researcher.md:93-104`.

`obvious relations`: `UI-SPEC.md`, design-system scanning patterns, shadcn registry safety checks, and the broader specialist-agent family that Checkpoint 3 deliberately left secondary.

`candidate loose tags`: `specialist-agent`, `design-contract`, `frontend-gate`, `spec-producer`.

`intervention status`: `mostly upstream/base live surface from this lane’s evidence`

`classification status`: `placed provisionally`

`confidence`: `high`

`unresolved classification`: This row only samples the research side of the UI family; the checker/auditor siblings remain implied rather than exhaustively inventoried here.

### A5. Secondary review, debug, and intel workers

`surface`: Specialist lanes outside the core phase chain: review, debugging, and codebase intelligence.

`path`: `.codex/agents/gsd-code-reviewer.md:13-20,37-82,84-156`; `.codex/agents/gsd-debugger.md:13-33,48-123,125-205`; `.codex/agents/gsd-intel-updater.md:32-80,94-220`.

`repo-local role as stated by source`: [e:c:i] These workers are not generic helpers. They carry distinct contracts: severity-classified `REVIEW.md`, persistent hypothesis-driven debug state with checkpointed conclusions, and machine-parseable `.planning/intel/` outputs that later commands and agents query instead of rereading the codebase. Sources: `.codex/agents/gsd-code-reviewer.md:13-20,37-82`; `.codex/agents/gsd-debugger.md:13-33,48-123`; `.codex/agents/gsd-intel-updater.md:34-46,94-193`.

`reads/expects`: Changed-file lists or diff bases for review, user symptoms and debug state for debugging, and canonical project code locations for intel refresh. Sources: `.codex/agents/gsd-code-reviewer.md:84-156`; `.codex/agents/gsd-debugger.md:23-33,125-205`; `.codex/agents/gsd-intel-updater.md:48-80,195-220`.

`emits/returns`: `REVIEW.md`, debug markers / debug files, and JSON+Markdown intel corpus files (`stack.json`, `files.json`, `apis.json`, `deps.json`, `arch.md`). Sources: `.codex/agents/gsd-code-reviewer.md:16-20`; `.codex/agents/gsd-debugger.md:21-33`; `.codex/agents/gsd-intel-updater.md:94-193`.

`downstream consumers`: code-review workflows, UAT diagnosis / debug continuation, and `intel query/status/diff/snapshot/validate` helpers plus any later agent that consumes the intel store. Sources: `.codex/agents/gsd-intel-updater.md:34-46,48-60`; `.codex/get-shit-done/bin/lib/intel.cjs:328-387`.

`obvious relations`: `debug-subagent-prompt.md`, `common-bug-patterns.md`, `intel.cjs`, `audit.cjs`, and summary/verification follow-through lanes.

`candidate loose tags`: `secondary-specialist-family`, `review-lane`, `debug-lane`, `intel-control-plane`.

`intervention status`: `mostly upstream/base live surfaces`

`classification status`: `cross-cutting`

`confidence`: `medium-high`

`unresolved classification`: Checkpoint 3 already flagged these broader optional families as secondary rather than fully mapped; this row preserves them as real surfaces without pretending they form one stable ontology branch. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-agent-doctrine-and-role-contracts.md:54,76`.

## Reference And Template Surface Ledger

### R1. `agent-contracts.md`

`surface`: Shared marker and handoff contract for agent outputs.

`path`: `.codex/get-shit-done/references/agent-contracts.md:1-108`.

`repo-local role as stated by source`: [e:c+i] This file is not passive documentation; it defines completion markers, the meaning of `PLAN COMPLETE`, and the handoff schemas for `RESEARCH.md`, `PLAN.md`, `SUMMARY.md`, and `VERIFICATION.md`. Sources: `.codex/get-shit-done/references/agent-contracts.md:3-8,11-18,45-91,92-108`.

`reads/expects`: Exact agent names, completion headings, and frontmatter/body field names.

`emits/returns`: A coupled protocol description that later workflows and helper code consume.

`downstream consumers`: planner/executor/verifier, `phase.cjs`, `roadmap.cjs`, and any workflow routing on completion or debt-bearing status. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-local-topology-schema.md:179-180,194-200`.

`obvious relations`: `summary.md`, `verification-report.md`, `phase-prompt.md`, `phase.cjs`, `roadmap.cjs`.

`candidate loose tags`: `handoff-contract`, `marker-protocol`, `completion-semantics`, `cross-cutting`.

`intervention status`: `live .codex-only drift surface`; current local topology already marks debt-aware completion semantics here as a live runtime distinction. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-local-topology-schema.md:171,179-180,200`.

`classification status`: `cross-cutting`

`confidence`: `high`

`unresolved classification`: None about its contract role; only its relative authority versus helper code interpretations can drift.

### R2. `gates.md`

`surface`: Canonical gate taxonomy.

`path`: `.codex/get-shit-done/references/gates.md:1-70`.

`repo-local role as stated by source`: [e:c:i] Defines pre-flight, revision, escalation, and abort gates and tells later workflow or audit design how each should behave. Sources: `.codex/get-shit-done/references/gates.md:1-4,7-42,61-70`.

`reads/expects`: Workflow stage names, artifact checkpoints, and failure modes needing gate classification.

`emits/returns`: The gate categories that plan-checker, verifier, and workflows concretize.

`downstream consumers`: `gsd-plan-checker`, `gsd-verifier`, planning/execution workflows, and prior audits that map gate semantics. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-agent-doctrine-and-role-contracts.md:18`.

`obvious relations`: `gsd-plan-checker.md`, `gsd-verifier.md`, `revision-loop.md`.

`candidate loose tags`: `reference-doctrine`, `gate-taxonomy`, `routing-contract`.

`intervention status`: `mostly upstream/base live surface`

`classification status`: `placed provisionally`

`confidence`: `high`

`unresolved classification`: None material.

### R3. `checkpoints.md`

`surface`: Human interaction contract for checkpoint tasks.

`path`: `.codex/get-shit-done/references/checkpoints.md:1-12,16-38,94-215`.

`repo-local role as stated by source`: [e:c:i] Sets the automation-first rule, defines `checkpoint:human-verify`, `checkpoint:decision`, and `checkpoint:human-action`, and explicitly constrains what should or should not be delegated to humans. Sources: `.codex/get-shit-done/references/checkpoints.md:1-12,16-38,94-215`.

`reads/expects`: Task XML structures, auto-mode flags, and the boundary between automatable work and human judgment.

`emits/returns`: Canonical checkpoint task shapes and resume-signal expectations.

`downstream consumers`: planner task design, executor checkpoint handling, `phase-prompt.md`, and any review of verification/decision gates. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-agent-doctrine-and-role-contracts.md:19`.

`obvious relations`: `phase-prompt.md`, `gsd-planner.md`, `gsd-executor.md`.

`candidate loose tags`: `reference-doctrine`, `checkpoint-contract`, `human-in-the-loop`.

`intervention status`: `mostly upstream/base live surface`

`classification status`: `placed provisionally`

`confidence`: `high`

`unresolved classification`: None material.

### R4. Planner-side review and authority references

`surface`: `planner-source-audit.md` and `planner-reviews.md`.

`path`: `.codex/get-shit-done/references/planner-source-audit.md:1-73`; `.codex/get-shit-done/references/planner-reviews.md:1-69`.

`repo-local role as stated by source`: [e:c+i] These refs sharpen planner obligations beyond generic planning text: source-audit forces GOAL/REQ/RESEARCH/CONTEXT coverage accounting, and reviews-mode forces explicit address/defer/reject accounting for review feedback rather than silent carry-forward. Sources: `.codex/get-shit-done/references/planner-source-audit.md:1-55,59-73`; `.codex/get-shit-done/references/planner-reviews.md:1-22,23-69`.

`reads/expects`: Phase goal, requirement IDs, RESEARCH/CONTEXT artifacts, `REVIEWS.md`, and review-consumer buckets.

`emits/returns`: Required coverage matrices and review-disposition sections the planner should produce.

`downstream consumers`: `gsd-planner`, `plan-phase` review mode, readiness review follow-through. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-local-topology-schema.md:157,180,200`.

`obvious relations`: `gsd-planner.md`, `plan-phase.md`, `review.md`.

`candidate loose tags`: `planner-doctrine`, `review-consumer-contract`, `coverage-discipline`.

`intervention status`: `mixed tracked overlay / live runtime`; the current topology already treats review surfaces as materially stronger in live runtime than in the tracked overlay copy. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-local-topology-schema.md:157,170,180`.

`classification status`: `cross-cutting`

`confidence`: `high`

`unresolved classification`: These are clearly contracts, but their exact strength depends on the live planner workflow and prompt injection path, not the markdown alone.

### R5. `verification-overrides.md`

`surface`: Intentional-deviation acceptance contract for verifier output.

`path`: `.codex/get-shit-done/references/verification-overrides.md:1-205`.

`repo-local role as stated by source`: [e:c:i] Defines when a must-have failure can become `PASSED (override)`, how fuzzy matching works, and how override use changes `completion_mode`, `debt_bearing`, and frontmatter score semantics. Sources: `.codex/get-shit-done/references/verification-overrides.md:1-48,63-136,138-205`.

`reads/expects`: `VERIFICATION.md` frontmatter, must-have text, accepted-by metadata, and verifier failure cases.

`emits/returns`: Override schema and verifier behavior rules for debt-bearing completion.

`downstream consumers`: `gsd-verifier`, milestone audits, and any helper reading verification frontmatter. Sources: `.codex/get-shit-done/references/verification-overrides.md:91-136,176-205`.

`obvious relations`: `agent-contracts.md`, `verification-report.md`, `phase.cjs`.

`candidate loose tags`: `verification-doctrine`, `debt-carrying-completion`, `override-contract`.

`intervention status`: `mostly upstream/base live surface`

`classification status`: `cross-cutting`

`confidence`: `high`

`unresolved classification`: None material.

### R6. Thinking-model references

`surface`: `thinking-models-planning.md`, `thinking-models-execution.md`, and `thinking-models-verification.md`.

`path`: `.codex/get-shit-done/references/thinking-models-planning.md:1-62`; `.codex/get-shit-done/references/thinking-models-execution.md:1-50`; `.codex/get-shit-done/references/thinking-models-verification.md:1-55`.

`repo-local role as stated by source`: [e:c:i] These are structured reasoning overlays for planner, executor, checker, and verifier agents. They are selective doctrine, not generic philosophy: each file names failure modes and when not to invoke the model suite. Sources: `.codex/get-shit-done/references/thinking-models-planning.md:1-16,23-46,55-62`; `.codex/get-shit-done/references/thinking-models-execution.md:1-39,43-50`; `.codex/get-shit-done/references/thinking-models-verification.md:1-45,48-55`.

`reads/expects`: Decision points during planning, execution, or verification; already-known agent scope and artifact context.

`emits/returns`: Reasoning heuristics and anti-failure checks rather than artifacts.

`downstream consumers`: planner, executor, checker, verifier, and any audit evaluating whether those roles apply skepticism or scope discipline. Sources: `.codex/agents/gsd-plan-checker.md:94-99`; `.codex/agents/gsd-executor.md:116-122`; `.codex/agents/gsd-verifier.md:62-67`.

`obvious relations`: Phase-chain worker contracts, review/verification doctrine.

`candidate loose tags`: `reasoning-doctrine`, `anti-failure-guidance`, `agent-consumed`.

`intervention status`: `mostly upstream/base live surface`

`classification status`: `placed provisionally`

`confidence`: `high`

`unresolved classification`: None material.

### R7. Steering-brief template

`surface`: `context.md`.

`path`: `.codex/get-shit-done/templates/context.md:1-12,15-158`.

`repo-local role as stated by source`: [e:c+i] This template is a steering-brief contract, not just a document skeleton. It fixes the sections downstream agents must read, especially `canonical_refs` and the four-part `future_awareness` structure. Sources: `.codex/get-shit-done/templates/context.md:3-12,30-152,162-162`.

`reads/expects`: Phase boundary, implementation decisions, assumptions, derived constraints, open questions, canonical references, existing code insights, future-awareness categories, and deferred ideas.

`emits/returns`: The `CONTEXT.md` shape that research and planning treat as high-authority input.

`downstream consumers`: `gsd-phase-researcher`, `gsd-planner`, discuss/plan workflows, and later audits about preserved seams. Sources: `.codex/get-shit-done/templates/context.md:9-12,93-152`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-agent-doctrine-and-role-contracts.md:22,27-29,58-59`.

`obvious relations`: `phase-researcher`, `planner`, `phase-prompt.md`, `planner-source-audit.md`.

`candidate loose tags`: `template`, `steering-brief`, `future-awareness`, `canonical-refs`.

`intervention status`: `tracked overlay / live runtime steering contract` in the repo-local GSD stack. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-runtime-config-overlay-truth.md:27`.

`classification status`: `placed provisionally`

`confidence`: `high`

`unresolved classification`: None material.

### R8. Phase artifact templates

`surface`: `phase-prompt.md`, `summary.md`, `verification-report.md`, and `research.md`.

`path`: `.codex/get-shit-done/templates/phase-prompt.md:1-179`; `.codex/get-shit-done/templates/summary.md:1-148`; `.codex/get-shit-done/templates/verification-report.md:1-186`; `.codex/get-shit-done/templates/research.md:1-220`.

`repo-local role as stated by source`: [e:c+i] These templates collectively define the core artifact contracts the phase chain works through: plan frontmatter including `future_preservation` and `must_haves`, summary frontmatter for dependency graph and requirements completion, verification tables and gap structure, and research disposition sections carrying resolved vs preserved uncertainty. Sources: `.codex/get-shit-done/templates/phase-prompt.md:14-49,64-179`; `.codex/get-shit-done/templates/summary.md:9-46,132-148`; `.codex/get-shit-done/templates/verification-report.md:7-180`; `.codex/get-shit-done/templates/research.md:9-66,98-220`.

`reads/expects`: Phase ID/name, must-haves, requirements, dependencies, decisions, completion metadata, and research evidence/disposition fields.

`emits/returns`: The concrete file shapes for `PLAN.md`, `SUMMARY.md`, `VERIFICATION.md`, and `RESEARCH.md`.

`downstream consumers`: core phase-chain agents, `frontmatter.cjs`, `verify.cjs`, `template.cjs`, `summary-extract`, `phase.cjs`, and `roadmap.cjs`.

`obvious relations`: `agent-contracts.md`, `checkpoints.md`, `template.cjs`, `frontmatter.cjs`, `verify.cjs`.

`candidate loose tags`: `artifact-template-family`, `machine-readable-frontmatter`, `goal-backward`.

`intervention status`: `mixed`; `phase-prompt.md` is explicitly described as an overlay-backed repo-local plan contract, while the rest behave as live runtime templates from this lane’s evidence. Sources: `.codex/get-shit-done/templates/phase-prompt.md:1-5,14-34,130-149`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-runtime-config-overlay-truth.md:28`.

`classification status`: `cross-cutting`

`confidence`: `high`

`unresolved classification`: These are templates, but helper code and live refs can harden or reinterpret their meaning after generation.

### R9. Specialized contract templates

`surface`: `UI-SPEC.md` and `AI-SPEC.md`.

`path`: `.codex/get-shit-done/templates/UI-SPEC.md:1-100`; `.codex/get-shit-done/templates/AI-SPEC.md:1-219`.

`repo-local role as stated by source`: [e:c:i] These are specialist design contracts, not optional prose. `UI-SPEC.md` locks design system, copy, spacing, and registry safety for frontend phases, while `AI-SPEC.md` locks framework choice, implementation guidance, guardrails, and eval strategy before planning AI system phases. Sources: `.codex/get-shit-done/templates/UI-SPEC.md:10-100`; `.codex/get-shit-done/templates/AI-SPEC.md:1-5,8-219`.

`reads/expects`: Phase metadata, selected tool/preset/framework, domain or design decisions, and guardrail/eval structure.

`emits/returns`: Specialized contract files consumed before or during planning.

`downstream consumers`: `gsd-ui-researcher`, `gsd-ui-checker`, `gsd-planner`, `gsd-executor`, `gsd-ui-auditor`, `gsd-ai-researcher`, and `gsd-eval-auditor`. Sources: `.codex/get-shit-done/templates/UI-SPEC.md:10-12,82-100`; `.codex/get-shit-done/templates/AI-SPEC.md:3-5,25,77,135`.

`obvious relations`: Specialist agent families and their checker/auditor companions.

`candidate loose tags`: `specialist-template`, `design-contract`, `AI-contract`, `pre-plan-lock`.

`intervention status`: `mostly upstream/base live surfaces`

`classification status`: `placed provisionally`

`confidence`: `high`

`unresolved classification`: These are clearly contract carriers, but they are only activated for particular phase types rather than the default phase chain.

### R10. Helper prompt templates and baseline config template

`surface`: `planner-subagent-prompt.md`, `debug-subagent-prompt.md`, and `templates/config.json`.

`path`: `.codex/get-shit-done/templates/planner-subagent-prompt.md:1-117`; `.codex/get-shit-done/templates/debug-subagent-prompt.md:1-91`; `.codex/get-shit-done/templates/config.json:1-48`.

`repo-local role as stated by source`: [e:c+r:i] The prompt templates are orchestration helpers that bridge workflows into specialist agents without being end-user artifacts; `templates/config.json` looks like runtime truth but is only a baseline/default comparison surface in the current loader architecture, not the effective config source. Sources: `.codex/get-shit-done/templates/planner-subagent-prompt.md:1-54,69-117`; `.codex/get-shit-done/templates/debug-subagent-prompt.md:1-32,52-91`; `.codex/get-shit-done/templates/config.json:1-48`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-runtime-config-overlay-truth.md:34-36,66`.

`reads/expects`: Placeholder values or user choices; in the config template’s case, default workflow and gate settings.

`emits/returns`: Filled planner/debug prompts and a config baseline shape.

`downstream consumers`: Workflow prompt assembly, developer comparison against default config, and audits trying to distinguish baseline from effective runtime.

`obvious relations`: `template.cjs`, `init.cjs`, `config.cjs`, `core.loadConfig()`.

`candidate loose tags`: `helper-template`, `orchestration-bridge`, `baseline-not-loader`, `ambiguous`.

`intervention status`: `mixed baseline / helper surface`

`classification status`: `ambiguous`

`confidence`: `medium-high`

`unresolved classification`: The prompt templates are clearly helpers; the main ambiguity is whether the map should place them under templates or under orchestration helpers because they are not generated phase artifacts.

## Helper And Runtime-Control Surface Ledger

### H1. `gsd-tools.cjs`

`surface`: Top-level CLI router and command surface.

`path`: `.codex/get-shit-done/bin/gsd-tools.cjs:1-164,166-185,226-240`.

`repo-local role as stated by source`: [e:c:i] This file centralizes and names the control surface that workflows use instead of re-embedding shell snippets: config parsing, model resolution, phase lookup, commits, summary verification, init payloads, verification suite calls, scaffolding, intel operations, and open-artifact audit entry points. Sources: `.codex/get-shit-done/bin/gsd-tools.cjs:4-8,9-164,166-185`.

`reads/expects`: CLI args, cwd/project root, and all helper libraries under `bin/lib/`.

`emits/returns`: JSON or raw strings for workflow consumption; command dispatch into the helper layer.

`downstream consumers`: Main workflows and any agent invoking `node .../gsd-tools.cjs ...` for structured answers. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-local-topology-schema.md:152,199`.

`obvious relations`: `init.cjs`, `config.cjs`, `phase.cjs`, `roadmap.cjs`, `verify.cjs`, `template.cjs`, `intel.cjs`, `audit.cjs`.

`candidate loose tags`: `router`, `control-plane-entry`, `helper-cli`, `workflow-bridge`.

`intervention status`: `mostly upstream/base live helper surface`

`classification status`: `placed provisionally`

`confidence`: `high`

`unresolved classification`: None material.

### H2. Core config, model, and install-validation layer

`surface`: `core.cjs`, `config.cjs`, and `model-profiles.cjs`.

`path`: `.codex/get-shit-done/bin/lib/core.cjs:239-266,268-420,1269-1325,1343-1373`; `.codex/get-shit-done/bin/lib/config.cjs:14-55,76-187,189-235`; `.codex/get-shit-done/bin/lib/model-profiles.cjs:1-70`.

`repo-local role as stated by source`: [e:c+r:i] This layer carries the effective runtime truth for defaults, config normalization, valid config-key API, agent-install detection, and model resolution. It is also where doc-vs-code seams become real, because `model-profiles.cjs` and `references/model-profiles.md` are parallel sources and `loadConfig()` normalizes behavior beyond what `templates/config.json` suggests. Sources: `.codex/get-shit-done/bin/lib/core.cjs:239-266,268-391,1269-1325,1343-1373`; `.codex/get-shit-done/bin/lib/config.cjs:14-55,76-187`; `.codex/get-shit-done/bin/lib/model-profiles.cjs:1-28`; `.codex/get-shit-done/references/model-profiles.md:1-50,89-145`.

`reads/expects`: `.planning/config.json`, global defaults, env vars/API-key files, model profile names, and agent-type names.

`emits/returns`: Normalized config objects, created config files, agent-install status, and resolved model strings.

`downstream consumers`: All workflow init payloads, settings/config commands, agent launch selection, health checks, and any audit of runtime truth. Sources: `.codex/get-shit-done/bin/lib/init.cjs:43-47,55-110,189-240`; `.codex/get-shit-done/bin/lib/commands.cjs:234-247`.

`obvious relations`: `templates/config.json`, `references/model-profiles.md`, agent `.md` / `.toml` families, `verify.cjs`.

`candidate loose tags`: `runtime-truth`, `config-loader`, `model-resolution`, `install-validation`, `doc-code-drift-risk`.

`intervention status`: `mixed live runtime / tracked overlay`; prior audits already identified config normalization and `.md` vs `.toml` install/registry seams here. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-runtime-config-overlay-truth.md:34-44,48-59,61-73`.

`classification status`: `cross-cutting`

`confidence`: `high`

`unresolved classification`: The code’s role is clear; the unresolved part is how much surrounding human-facing markdown a later reader can safely treat as equal authority.

### H3. Workflow bootstrap layer

`surface`: `init.cjs`.

`path`: `.codex/get-shit-done/bin/lib/init.cjs:27-48,50-181,184-260`.

`repo-local role as stated by source`: [e:c:i] Builds compound init payloads for workflows, injects `project_root`, agent-install status, response language, resolved models, config flags, artifact availability, phase identity, and roadmap-derived requirement IDs. Sources: `.codex/get-shit-done/bin/lib/init.cjs:27-48,50-181,184-260`.

`reads/expects`: Config state, roadmap, phase directories, milestone info, agent-install state, and current filesystem facts.

`emits/returns`: Structured init JSON consumed by execute/plan/new-project/new-milestone/quick/progress and related workflows.

`downstream consumers`: Main workflows and any runtime path that depends on bootstrapped context instead of ad hoc file reads. Sources: `.codex/get-shit-done/bin/gsd-tools.cjs:137-150`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-local-topology-schema.md:152`.

`obvious relations`: `core.cjs`, `config.cjs`, `phase.cjs`, `roadmap.cjs`, agent launch settings.

`candidate loose tags`: `bootstrap-helper`, `workflow-init`, `context-assembler`.

`intervention status`: `mostly upstream/base live helper surface`

`classification status`: `placed provisionally`

`confidence`: `high`

`unresolved classification`: None material.

### H4. Status, routing, commit, and summary extraction layer

`surface`: `phase.cjs`, `roadmap.cjs`, and the status/commit portions of `commands.cjs`.

`path`: `.codex/get-shit-done/bin/lib/phase.cjs:11-37,37-113`; `.codex/get-shit-done/bin/lib/roadmap.cjs:10-74,116-175,182-275,277-320`; `.codex/get-shit-done/bin/lib/commands.cjs:11-36,234-355,425-479`.

`repo-local role as stated by source`: [e:c+i] This layer is where artifact state becomes routing truth. `inspectPhaseCompletion()` turns verification files, overrides, warnings, and debt into `clean_completion` or `debt_carrying_completion`; `roadmap analyze` and `update-plan-progress` translate that into roadmap/disk status; `commands.cjs` adds commit gating, branch handling, summary extraction, and the user-facing resolve-model surface. Sources: `.codex/get-shit-done/bin/lib/phase.cjs:11-31,37-113`; `.codex/get-shit-done/bin/lib/roadmap.cjs:159-223,237-275,289-320`; `.codex/get-shit-done/bin/lib/commands.cjs:11-36,234-355,425-479`.

`reads/expects`: SUMMARY/VERIFICATION/UAT files, roadmap sections, git state, config flags, and frontmatter.

`emits/returns`: Derived phase status, roadmap updates, commits, extracted summary facts, and model answers.

`downstream consumers`: `progress`, `transition`, `ship`, phase completion routing, milestone closeout, and human/operator inspection. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-local-topology-schema.md:158,179,194-200`.

`obvious relations`: `agent-contracts.md`, `summary.md`, `verification-report.md`, `verify.cjs`.

`candidate loose tags`: `status-router`, `completion-semantics`, `git-control`, `artifact-reader`.

`intervention status`: `mostly live runtime helper surface`

`classification status`: `cross-cutting`

`confidence`: `high`

`unresolved classification`: None material.

### H5. Template fill and frontmatter parser layer

`surface`: `template.cjs` and `frontmatter.cjs`.

`path`: `.codex/get-shit-done/bin/lib/template.cjs:1-224`; `.codex/get-shit-done/bin/lib/frontmatter.cjs:1-182,193-260`.

`repo-local role as stated by source`: [e:c+i] These are the code surfaces that translate template markdown into live artifacts and then parse or reconstruct their machine-readable frontmatter. `template.cjs` chooses summary variants and fills plan/summary/verification files; `frontmatter.cjs` parses nested YAML, reconstructs frontmatter, and contains special logic for `must_haves` blocks plus warnings when they silently parse empty. Sources: `.codex/get-shit-done/bin/lib/template.cjs:10-53,56-224`; `.codex/get-shit-done/bin/lib/frontmatter.cjs:43-118,120-182,193-260`.

`reads/expects`: Existing plan or phase directory, template type, frontmatter conventions, nested `must_haves` structure.

`emits/returns`: Filled artifact files, parsed frontmatter objects, reconstructed YAML, and must-have block extraction.

`downstream consumers`: planner/executor/verifier workflows, `verify.cjs`, summary extraction, and any code depending on structured artifact fields.

`obvious relations`: `phase-prompt.md`, `summary.md`, `verification-report.md`, `research.md`, `verify.cjs`.

`candidate loose tags`: `artifact-filler`, `frontmatter-parser`, `machine-contract-enforcer`.

`intervention status`: `mostly upstream/base live helper surface`

`classification status`: `cross-cutting`

`confidence`: `high`

`unresolved classification`: None material.

### H6. Verification and health suite

`surface`: `verify.cjs`.

`path`: `.codex/get-shit-done/bin/lib/verify.cjs:1-167,169-259,283-380,658-724,993-1009`.

`repo-local role as stated by source`: [e:c+i] This file converts artifact contracts into machine checks: summary spot-checking, plan-structure validation, phase completeness, path/reference verification, `must_haves.artifacts` and `must_haves.key_links` checks, health warnings, and named-agent installation validation. Sources: `.codex/get-shit-done/bin/lib/verify.cjs:12-105,108-167,169-214,216-259,283-380,658-724,993-1009`.

`reads/expects`: SUMMARY/PLAN files, frontmatter, must-have blocks, phase directories, config state, and agent-install expectations.

`emits/returns`: Structured pass/fail JSON, warning/error lists, verified artifact/key-link results, and health/agent validation reports.

`downstream consumers`: verifier workflow, plan-checker support, health checks, runtime-truth audits, and human inspection. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-runtime-config-overlay-truth.md:48,53`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-local-topology-schema.md:152,194-200`.

`obvious relations`: `frontmatter.cjs`, `agent-contracts.md`, `verification-overrides.md`, agent-install split in `core.cjs`.

`candidate loose tags`: `machine-verification`, `health-check`, `agent-validation`, `artifact-semantics`.

`intervention status`: `mostly live runtime helper surface`

`classification status`: `cross-cutting`

`confidence`: `high`

`unresolved classification`: None material.

### H7. Open-artifact audit helper

`surface`: `audit.cjs`.

`path`: `.codex/get-shit-done/bin/lib/audit.cjs:1-17,18-77,79-149,151-220,223-240`.

`repo-local role as stated by source`: [e:c:i] This helper is a control surface for cross-type unresolved state, not a passive utility. It scans `.planning/debug/`, `.planning/quick/`, `.planning/threads/`, and `.planning/todos/pending/` for still-open items and returns structured results for pre-close gating. Sources: `.codex/get-shit-done/bin/lib/audit.cjs:1-17,18-77,79-149,151-220,223-240`.

`reads/expects`: Planning-root directories, frontmatter status fields, thread/debug summary sections, and safe-path constraints.

`emits/returns`: Structured unresolved-state inventory for `audit-open`.

`downstream consumers`: milestone-close and artifact-governance workflows; any audit trying to understand open state across artifact classes.

`obvious relations`: `gsd-tools.cjs audit-open`, `frontmatter.cjs`, artifact retention/governance lanes.

`candidate loose tags`: `open-state-scanner`, `artifact-audit`, `control-plane-secondary`.

`intervention status`: `mostly upstream/base live helper surface`

`classification status`: `placed provisionally`

`confidence`: `medium-high`

`unresolved classification`: None material.

### H8. Intel control plane

`surface`: `intel.cjs`.

`path`: `.codex/get-shit-done/bin/lib/intel.cjs:2-8,19-42,46-70,194-207,234-340,344-387`.

`repo-local role as stated by source`: [e:c+i] This is not just storage plumbing. It defines the persistent intel store under `.planning/intel/`, gates it on config, supports query/status/diff/snapshot/validate/patch-meta/extract-exports operations, and explicitly treats `intel update` as a spawn-agent handoff to `gsd-intel-updater`. Sources: `.codex/get-shit-done/bin/lib/intel.cjs:2-8,19-42,46-70,194-207,234-340,344-387`.

`reads/expects`: Intel-enabled config, intel file schemas, planning root, search terms, and file paths for metadata or export extraction.

`emits/returns`: Intel query answers, freshness reports, diff/snapshot artifacts, validation results, and `spawn_agent` update instructions.

`downstream consumers`: `gsd-tools intel *`, `gsd-intel-updater`, and later agents that query intel instead of rereading the full codebase. Sources: `.codex/get-shit-done/bin/gsd-tools.cjs:77-84,1038-1078`; `.codex/agents/gsd-intel-updater.md:34-46,48-60`.

`obvious relations`: `gsd-intel-updater.md`, `audit.cjs`, `frontmatter.cjs`, `gsd-tools.cjs`.

`candidate loose tags`: `knowledge-base-helper`, `spawn-handoff`, `secondary-control-plane`.

`intervention status`: `mostly upstream/base live helper surface`

`classification status`: `cross-cutting`

`confidence`: `high`

`unresolved classification`: None material.

## Cross-Cutting Contract Carriers

1. [e:c+r:i] The `.md` / `.toml` agent pair is itself a cross-cutting contract carrier. The `.md` files carry much of the repo-local worker doctrine and AGENTS-aware behavior, while the `.toml` siblings carry registry-facing prompt/config surfaces and reasoning settings. Install validation and model resolution touch different halves of that pair, so any honest map has to show both together and still leave launch authority unresolved. Sources: `.codex/agents/gsd-planner.md:47-57`; `.codex/agents/gsd-planner.toml:37-50`; `.codex/get-shit-done/bin/lib/core.cjs:1269-1325,1343-1373`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-runtime-config-overlay-truth.md:48-53,73`.
2. [e:c+i] `agent-contracts.md` plus `phase.cjs` / `roadmap.cjs` form a doc-plus-code completion contract. The reference says `PLAN COMPLETE` is not clean completion, and the helper layer operationalizes that by deriving debt-bearing vs clean completion from verification artifacts and warnings. Sources: `.codex/get-shit-done/references/agent-contracts.md:45-91`; `.codex/get-shit-done/bin/lib/phase.cjs:21-31,37-113`; `.codex/get-shit-done/bin/lib/roadmap.cjs:182-223,237-275`.
3. [e:c+i] `checkpoints.md`, `phase-prompt.md`, `frontmatter.cjs`, and `verify.cjs` jointly carry the plan-interaction contract. One file defines checkpoint semantics, one defines how they should appear in plans, one parses the nested frontmatter blocks, and one validates whether the resulting plan structure is coherent enough for execution or verification. Sources: `.codex/get-shit-done/references/checkpoints.md:1-12,16-38,185-214`; `.codex/get-shit-done/templates/phase-prompt.md:14-49,91-121,130-179`; `.codex/get-shit-done/bin/lib/frontmatter.cjs:193-260`; `.codex/get-shit-done/bin/lib/verify.cjs:108-167,283-380`.
4. [e:c+r:i] `templates/config.json`, `references/model-profiles.md`, and the `core/config/model-profiles` helper trio are a cross-cutting doc-code seam rather than one clean family. The template and reference make runtime shape legible to humans, but the effective behavior comes from `loadConfig()`, `VALID_CONFIG_KEYS`, and `resolveModelInternal()`. Sources: `.codex/get-shit-done/templates/config.json:1-48`; `.codex/get-shit-done/references/model-profiles.md:89-145`; `.codex/get-shit-done/bin/lib/core.cjs:268-391,1343-1373`; `.codex/get-shit-done/bin/lib/config.cjs:14-55,76-187`; `.codex/get-shit-done/bin/lib/model-profiles.cjs:1-28`.
5. [e:c+i] `planner-subagent-prompt.md` and `debug-subagent-prompt.md` are helper prompt surfaces that bridge workflows to agents without being end-user artifacts or runtime helper code. They should stay visible as cross-cutting adapters rather than disappear into either the template bucket or the helper-code bucket. Sources: `.codex/get-shit-done/templates/planner-subagent-prompt.md:1-54,69-117`; `.codex/get-shit-done/templates/debug-subagent-prompt.md:1-32,52-91`.
6. [e:c+i] The intel lane is both an agent family and a helper/control plane. `gsd-intel-updater` writes the intel corpus, while `intel.cjs` queries, snapshots, validates, and instructs the operator/runtime to spawn that updater again when refresh is needed. Sources: `.codex/agents/gsd-intel-updater.md:34-46,94-193`; `.codex/get-shit-done/bin/lib/intel.cjs:194-207,234-340,344-387`.

## What The Current High-Level Picture Misses

1. [e:c+r:i] The current topology schema already names `.codex/get-shit-done/bin/gsd-tools.cjs` plus a few major helpers and it already includes `.codex/agents/*.toml` as `core role contracts`, but it still does not carve out the sibling `.md` worker contracts as their own high-level surface family. That omission matters because prior audits already showed that install validation and repo-local doctrine lean on the `.md` side while registry/model control leans on `.toml`. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-local-topology-schema.md:152,159`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-runtime-config-overlay-truth.md:48-53,73`.
2. [e:c+i] The current picture still treats most references and templates as subordinate attachments to workflows instead of a distinct contract layer. In practice, `agent-contracts.md`, `gates.md`, `checkpoints.md`, `planner-source-audit.md`, `planner-reviews.md`, and `verification-overrides.md` each encode operational semantics that later agents or helper code must honor. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-local-topology-schema.md:157,179-180,199-200`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-agent-doctrine-and-role-contracts.md:18-21,60-62`; `.codex/get-shit-done/references/planner-source-audit.md:1-55`; `.codex/get-shit-done/references/verification-overrides.md:91-136`.
3. [e:c+i] The helper/control picture is still too coarse. The present schema calls out `init`, `config`, `roadmap`, and `phase`, but it does not visibly preserve `template.cjs`, `frontmatter.cjs`, `verify.cjs`, `audit.cjs`, `intel.cjs`, and the utility portions of `commands.cjs`, even though those smaller files are where plan structure, must-have parsing, agent installation checks, open-artifact scans, intel refresh handoffs, and summary extraction actually happen. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-local-topology-schema.md:152,194-200`; `.codex/get-shit-done/bin/lib/template.cjs:56-224`; `.codex/get-shit-done/bin/lib/frontmatter.cjs:193-260`; `.codex/get-shit-done/bin/lib/verify.cjs:108-167,283-380,993-1009`; `.codex/get-shit-done/bin/lib/audit.cjs:1-17`; `.codex/get-shit-done/bin/lib/intel.cjs:328-340`.
4. [e:c+r:i] The current map underrepresents specialist secondary families by leaving them implicit or previously secondary. Checkpoint 3 explicitly deferred broader UI/docs/review/security/intel families; for raw inventory, they now need to remain visible as real surfaces rather than later surprises. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-agent-doctrine-and-role-contracts.md:54,76`; `.codex/agents/gsd-ui-researcher.md:93-104`; `.codex/agents/gsd-code-reviewer.md:13-20,84-156`; `.codex/agents/gsd-debugger.md:21-33`; `.codex/agents/gsd-intel-updater.md:34-46`.
5. [e:c+r:i] The current picture still misses a clear representation of ambiguous or weakly placed surfaces. `templates/config.json` is baseline but not loader truth; `model-profiles.md` has a code twin; planner/debug prompt templates are orchestration bridges rather than ordinary output templates; the advisor helper exists as a named surface but is routed through a `general-purpose` seam in prior audits. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-runtime-config-overlay-truth.md:66-67,71-73`; `.codex/get-shit-done/bin/lib/model-profiles.cjs:1-8`; `.codex/get-shit-done/templates/planner-subagent-prompt.md:1-54`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-agent-doctrine-and-role-contracts.md:38-39,44-46,53,75`.

## Recommended Additions To The Next Map

1. [d:r:i] Add a dedicated `Worker Contract Layer` with at least three visible families: core phase-chain `.md` prompts, core phase-chain `.toml` registry prompts, and specialist/secondary worker families (`UI`, `review`, `debug`, `intel`, and optional advisor lanes). The `.md` / `.toml` split should be annotated as an unresolved authority seam, not hidden inside one node.
2. [d:r:i] Add a distinct `Reference Doctrine Layer` separate from workflows. At minimum, show `gates`, `checkpoints`, `agent-contracts`, `planner-source-audit`, `planner-reviews`, `verification-overrides`, and the `thinking-models` cluster as shared contracts consumed across multiple workflows and helpers.
3. [d:r:i] Add a distinct `Template Contract Layer` separate from references. Split it into `phase artifact templates` (`context`, `phase-prompt`, `research`, `summary`, `verification`) and `specialist contract templates` (`UI-SPEC`, `AI-SPEC`), then keep `planner-subagent-prompt` / `debug-subagent-prompt` visible as helper-prompt adapters rather than burying them.
4. [d:r:i] Expand the helper/control band into sublanes instead of one generic helper node: `router/bootstrap` (`gsd-tools`, `init`), `runtime truth` (`core`, `config`, `model-profiles`), `artifact parsing/fill` (`template`, `frontmatter`), `verification/status` (`verify`, `phase`, `roadmap`, summary/commit utilities), and `secondary control planes` (`audit`, `intel`).
5. [d:r:i] Mark three specific ambiguous surfaces directly on the next map: `templates/config.json` as `baseline only / not effective loader`, `references/model-profiles.md` as `human-facing twin of code table`, and `gsd-advisor-researcher` as `named surface with adapter-mediated launch path`.
6. [d:r:i] Preserve cross-cutting surfaces explicitly instead of forcing exclusivity. In particular: `agent-contracts.md` should connect both to workers and to helper status code; `checkpoints.md` should connect both to planner template shape and to executor behavior; the intel lane should connect both to its agent writer and to its helper query/snapshot code.
