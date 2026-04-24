# Checkpoint 5 GSD Raw Inventory A2: Workflow And Subworkflow Surfaces

## Incomplete State

[e:c:i] Completed on 2026-04-16 after the required early scaffold pass. This file was created first, then revised in place; no known required section remains placeholder-only. Sources: [checkpoint-5-gsd-raw-inventory-a2-workflow-and-subworkflow-surfaces-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-a2-workflow-and-subworkflow-surfaces-spec.md:52), [checkpoint-5-gsd-raw-inventory-bundle-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-bundle-spec.md:121), [checkpoint-5-gsd-raw-inventory-bundle-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-bundle-spec.md:123).

## Research Frame

- [g:c:i] This lane is a high-level workflow-topology inventory, not a deep contract zoom. The pressure is to inventory workflow families plus the sub-workflows and internal bridges that make the current mainline picture too simple. Sources: [checkpoint-5-gsd-raw-inventory-a2-workflow-and-subworkflow-surfaces-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-a2-workflow-and-subworkflow-surfaces-spec.md:3), [checkpoint-5-gsd-raw-inventory-a2-workflow-and-subworkflow-surfaces-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-a2-workflow-and-subworkflow-surfaces-spec.md:37), [checkpoint-5-gsd-raw-inventory-a2-workflow-and-subworkflow-surfaces-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-a2-workflow-and-subworkflow-surfaces-spec.md:65).
- [g:c:i] The bundle contract explicitly rejects premature neatness: cross-cutting, ambiguous, and unplaced surfaces should stay visible rather than being forced into a stable family too early. Sources: [checkpoint-5-gsd-raw-inventory-bundle-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-bundle-spec.md:31), [checkpoint-5-gsd-raw-inventory-bundle-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-bundle-spec.md:66), [checkpoint-5-gsd-raw-inventory-bundle-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-bundle-spec.md:112).
- [d:r:i] I treated the working unit here as `workflow family + bridge flow + emitted artifact carrier`, because the current repo-local topology schema already captures a simplified main chain and this checkpoint is supposed to broaden that picture rather than redraw the same spine. Sources: [checkpoint-5-gsd-local-topology-schema.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-local-topology-schema.md:76), [checkpoint-5-gsd-local-topology-schema.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-local-topology-schema.md:144), [checkpoint-3-gsd-surface-map.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-surface-map.md:87).

## Path Of Inquiry

- [e:c:i] I started with the required governing inputs, created the target file immediately, then used the workflow directory itself as the primary evidence surface. Sources: [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:17), [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md:42), [checkpoint-5-gsd-raw-inventory-a2-workflow-and-subworkflow-surfaces-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-a2-workflow-and-subworkflow-surfaces-spec.md:21), [checkpoint-5-gsd-raw-inventory-bundle-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-bundle-spec.md:121).
- [e:c:i] The main read set was `.codex/get-shit-done/workflows/`, using purpose blocks, narrow routing windows, and artifact-emission lines rather than broad full-file rereads. Sources: [checkpoint-5-gsd-raw-inventory-a2-workflow-and-subworkflow-surfaces-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-a2-workflow-and-subworkflow-surfaces-spec.md:30), [checkpoint-5-gsd-raw-inventory-a2-workflow-and-subworkflow-surfaces-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-a2-workflow-and-subworkflow-surfaces-spec.md:67), [checkpoint-5-gsd-raw-inventory-bundle-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-bundle-spec.md:123).
- [e:r:i] I widened to a small set of skill-wrapper references only when needed to prove that wrapper summaries are not the authoritative surface and that some entrypoints fan into multiple workflow files. Sources: [gsd-discuss-phase/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/.codex/skills/gsd-discuss-phase/SKILL.md:69), [gsd-discuss-phase/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/.codex/skills/gsd-discuss-phase/SKILL.md:92), [gsd-do/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/.codex/skills/gsd-do/SKILL.md:67).
- [e:r:i] I widened to the readiness protocol, current schema docs, and Checkpoint 3/4 synthesis artifacts because this lane is explicitly about what the current high-level picture underrepresents; without those comparison surfaces, “misses” would be hand-wavy. Sources: [checkpoint-5-gsd-raw-inventory-bundle-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-bundle-spec.md:42), [PROTOCOL.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/PROTOCOL.md:35), [checkpoint-5-gsd-local-topology-schema.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-local-topology-schema.md:76), [checkpoint-4-converged-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-converged-synthesis.md:79).
- [e:r:i] I also widened briefly to the governance docs named by root `AGENTS.md` to confirm artifact-handling posture for audit outputs; that widening did not materially alter workflow-family classification. Sources: [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:11), [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:101), [ARTIFACT-GOVERNANCE.md](/home/rookslog/workspace/projects/prix-guesser/ARTIFACT-GOVERNANCE.md:33), [AI-GUARDRAILS.md](/home/rookslog/workspace/projects/prix-guesser/AI-GUARDRAILS.md:56).

## Workflow Surface Ledger

### `Discuss family`
- `surface`: `discuss-phase` main mode plus `assumptions` and `power` subflows behind the same skill entry.
- `path`: [gsd-discuss-phase/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/.codex/skills/gsd-discuss-phase/SKILL.md:69), [discuss-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/discuss-phase.md:1), [discuss-phase-assumptions.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/discuss-phase-assumptions.md:1), [discuss-phase-power.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/discuss-phase-power.md:1)
- `repo-local role as stated by source`: Create `CONTEXT.md` as the steering brief; assumptions mode does codebase-first inference; power mode externalizes the question set into JSON/HTML before generating the same steering artifact.
- `reads/expects`: Phase args, canon/state, prior contexts, `workflow.discuss_mode`, and gray-area analysis inputs.
- `emits/returns`: `CONTEXT.md`, `DISCUSSION-LOG.md`, `DISCUSS-CHECKPOINT.json`, optionally `QUESTIONS.json` and `QUESTIONS.html`; may flat-launch `gsd-plan-phase`.
- `downstream consumers`: `gsd-phase-researcher`, `gsd-planner`, `progress`, `autonomous`.
- `obvious relations`: Skill wrapper mode-routes into separate workflow files; standard and assumptions variants both preserve a flat auto-chain into planning.
- `candidate loose tags`: `steering`, `phase-entry`, `mode-router`, `artifact-writer`
- `intervention status`: `core mainline`
- `classification status`: `placed provisionally`
- `confidence`: `high`
- `unresolved classification`: The next map should show this as a family node with internal branches, not a single “discuss” box. Sources: [discuss-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/discuss-phase.md:1237), [discuss-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/discuss-phase.md:1311), [discuss-phase-assumptions.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/discuss-phase-assumptions.md:652), [discuss-phase-power.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/discuss-phase-power.md:31).

### `Research and discovery family`
- `surface`: Standalone `research-phase` plus the narrower `discovery-phase` subworkflow used for verified dependency/library investigation.
- `path`: [research-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/research-phase.md:1), [discovery-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/discovery-phase.md:1)
- `repo-local role as stated by source`: `research-phase` writes `RESEARCH.md`; `discovery-phase` chooses a depth level and may emit `DISCOVERY.md` or only a verbal verification result.
- `reads/expects`: Phase context, requirements, state, resolved `canonical_refs`, and current external documentation.
- `emits/returns`: `RESEARCH.md`, `DISCOVERY.md`, or a no-file “verified enough to proceed” result.
- `downstream consumers`: `plan-phase`, planner/checker prompts, later verification/validation work.
- `obvious relations`: `plan-phase` already integrates research and separately relies on discovery-style verification for current-library/API truth.
- `candidate loose tags`: `research`, `planning-support`, `external-doc-check`, `depth-router`
- `intervention status`: `optional or embedded support lane`
- `classification status`: `placed provisionally`
- `confidence`: `high`
- `unresolved classification`: `discovery-phase` behaves more like an internal planning-support subworkflow than a user-facing peer of `research-phase`, so the next map should not flatten them together too aggressively. Sources: [research-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/research-phase.md:48), [discovery-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/discovery-phase.md:10), [discovery-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/discovery-phase.md:45), [discovery-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/discovery-phase.md:79).

### `Plan family`
- `surface`: `plan-phase`
- `path`: [plan-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/plan-phase.md:1)
- `repo-local role as stated by source`: Create executable `PLAN.md` files through integrated research, planning, and plan-checking with a revision loop.
- `reads/expects`: `CONTEXT.md`, resolved `canonical_refs`, `RESEARCH.md`, optional `REVIEWS.md`, optional `UI-SPEC.md`, current config, prior phase context at larger context windows.
- `emits/returns`: `PLAN.md`, sometimes `VALIDATION.md`, sometimes a PRD-derived `CONTEXT.md`, `STATE.md` planned-phase updates, and optional auto-launch of execution.
- `downstream consumers`: `execute-phase`, verifier, review-driven replanning, gap-closure execution.
- `obvious relations`: Auto-generates or prompts for `UI-SPEC` when UI indicators exist; reads review-consumer doctrine; flat-chains to execute-phase.
- `candidate loose tags`: `planning`, `gatekeeper`, `review-consumer`, `auto-chain`
- `intervention status`: `core mainline`
- `classification status`: `placed provisionally`
- `confidence`: `high`
- `unresolved classification`: The family boundary is wider than a simple “planner node” because it also owns PRD-express steering generation and optional validation/design-contract insertion points. Sources: [plan-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/plan-phase.md:27), [plan-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/plan-phase.md:501), [plan-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/plan-phase.md:1029), [plan-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/plan-phase.md:1078).

### `Inserted design-contract family`
- `surface`: `ui-phase` and `ai-integration-phase`
- `path`: [ui-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/ui-phase.md:1), [ai-integration-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/ai-integration-phase.md:1)
- `repo-local role as stated by source`: Insert design-contract lanes between steering and planning so the planner inherits a locked `UI-SPEC.md` or `AI-SPEC.md` rather than improvising those decisions during execution.
- `reads/expects`: Phase context, roadmap, requirements, and sometimes prior research.
- `emits/returns`: `UI-SPEC.md` or `AI-SPEC.md`.
- `downstream consumers`: `plan-phase`, later UI/AI audit lanes, execution.
- `obvious relations`: `plan-phase` explicitly checks for missing `UI-SPEC.md` and can auto-run `gsd-ui-phase`; the AI workflow describes itself as an inserted lifecycle lane rather than a post-hoc audit.
- `candidate loose tags`: `design-contract`, `pre-plan-branch`, `specialized-prep`
- `intervention status`: `optional inserted branch`
- `classification status`: `placed provisionally`
- `confidence`: `medium-high`
- `unresolved classification`: The UI insertion edge is directly evidenced in `plan-phase`; the AI insertion posture is explicit in its own purpose block but its exact auto-routing point was not reread in the planner body during this lane. Sources: [plan-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/plan-phase.md:501), [plan-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/plan-phase.md:510), [ui-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/ui-phase.md:121), [ai-integration-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/ai-integration-phase.md:2).

### `Execution orchestration family`
- `surface`: `execute-phase`
- `path`: [execute-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/execute-phase.md:1)
- `repo-local role as stated by source`: Execute a phase via wave-based orchestration while keeping the orchestrator lean and delegating plan work to executors.
- `reads/expects`: `PLAN.md`, state/config, prior summaries, context/research, overlap/worktree safety data.
- `emits/returns`: `SUMMARY.md`, `VERIFICATION.md`, `HUMAN-UAT.md`, shared-doc updates (`STATE.md`, `ROADMAP.md`, `REQUIREMENTS.md`, `PROJECT.md`), optional next-step routing.
- `downstream consumers`: `verify-work`, `ship`, `progress`, milestone audits, next-phase routing.
- `obvious relations`: Can execute `execute-plan.md` inline; spawns verifier logic; invokes internal `transition.md`; routes gaps back to `plan-phase --gaps`.
- `candidate loose tags`: `execution`, `wave-orchestrator`, `debt-router`, `state-writer`
- `intervention status`: `core mainline`
- `classification status`: `placed provisionally`
- `confidence`: `high`
- `unresolved classification`: The current high-level map should split “execute” into orchestration, actual plan execution, and verification-routing subflows instead of keeping one opaque execution node. Sources: [execute-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/execute-phase.md:5), [execute-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/execute-phase.md:189), [execute-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/execute-phase.md:1218), [execute-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/execute-phase.md:1468).

### `Inline execution subworkflow`
- `surface`: `execute-plan`
- `path`: [execute-plan.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/execute-plan.md:1)
- `repo-local role as stated by source`: Execute a single `PLAN.md` and create the corresponding `SUMMARY.md`.
- `reads/expects`: `STATE.md`, config, phase/plan init context, task-level execution instructions.
- `emits/returns`: `SUMMARY.md`, requirement completion updates, session continuity updates, and sometimes shared `STATE.md` / `ROADMAP.md` writes.
- `downstream consumers`: `execute-phase`, verifier, `add-tests`, shipping/audit surfaces.
- `obvious relations`: Inline child of `execute-phase`; worktree mode pushes some shared-doc writes back to the orchestrator.
- `candidate loose tags`: `internal-bridge`, `plan-runner`, `summary-writer`
- `intervention status`: `internal bridge`
- `classification status`: `placed provisionally`
- `confidence`: `high`
- `unresolved classification`: None at this level; the main need is visibility, not a different bucket. Sources: [execute-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/execute-phase.md:189), [execute-plan.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/execute-plan.md:340), [execute-plan.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/execute-plan.md:351), [execute-plan.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/execute-plan.md:434).

### `Goal-backward verification subworkflow`
- `surface`: `verify-phase` plus the execute-phase verifier handoff that spawns verification after execution.
- `path`: [verify-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/verify-phase.md:1), [execute-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/execute-phase.md:1218)
- `repo-local role as stated by source`: Verify goal achievement rather than task completion, then classify the phase into `passed`, `human_needed`, or `gaps_found`.
- `reads/expects`: All phase plans, summaries, requirement traceability, and sometimes context/research/prior verification.
- `emits/returns`: `VERIFICATION.md` plus a status the execution orchestrator branches on.
- `downstream consumers`: `execute-phase`, `verify-work`, `audit-milestone`, gap-closure replanning.
- `obvious relations`: This is distinct from `verify-work`; it is codebase/goal-backward verification first, human UAT second.
- `candidate loose tags`: `internal-bridge`, `goal-backward-verification`, `status-router`
- `intervention status`: `internal bridge`
- `classification status`: `ambiguous`
- `confidence`: `medium`
- `unresolved classification`: The repo shows both a dedicated `verify-phase.md` workflow and a direct execute-phase prompt for `gsd-verifier`; this lane confirms the split exists but does not settle which text is the stricter operative source in practice. Sources: [verify-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/verify-phase.md:4), [verify-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/verify-phase.md:28), [execute-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/execute-phase.md:1225), [execute-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/execute-phase.md:1257).

### `Persistent UAT and gap-closure family`
- `surface`: `verify-work` plus the `diagnose-issues` bridge it can invoke
- `path`: [verify-work.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/verify-work.md:1), [diagnose-issues.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/diagnose-issues.md:1)
- `repo-local role as stated by source`: Persist human testing state in `UAT.md`, diagnose failures before fix planning, and feed targeted gap plans back into execution.
- `reads/expects`: Phase summaries, verification state, existing UAT files, diagnosed or undiagnosed gaps.
- `emits/returns`: `UAT.md`, acknowledged gaps, root-cause-enriched gap entries, `DEBUG-*.md`, transition on clean pass, or fix-plan readiness.
- `downstream consumers`: `plan-phase --gaps`, `execute-phase --gaps-only`, `progress`, `audit-uat`, milestone audits.
- `obvious relations`: Inline-calls `transition.md` on clean completion and calls `diagnose-issues.md` before replanning fixes.
- `candidate loose tags`: `manual-verification`, `persistent-state`, `debug-bridge`, `gap-closure`
- `intervention status`: `post-execution core`
- `classification status`: `placed provisionally`
- `confidence`: `high`
- `unresolved classification`: The family probably needs its own box in the next map rather than being treated as a thin epilogue to execute-phase. Sources: [verify-work.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/verify-work.md:29), [verify-work.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/verify-work.md:445), [verify-work.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/verify-work.md:488), [diagnose-issues.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/diagnose-issues.md:21), [diagnose-issues.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/diagnose-issues.md:94).

### `Plan review family`
- `surface`: `review`
- `path`: [review.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/review.md:1)
- `repo-local role as stated by source`: Run cross-AI plan review and synthesize feedback into a consumer contract rather than a soft consensus summary.
- `reads/expects`: Plans, project context, requirements, optional context/research, available external AI CLIs.
- `emits/returns`: `REVIEWS.md` with explicit “must address”, rebuttal-required, and deferable buckets.
- `downstream consumers`: `plan-phase --reviews`, human replanning judgment, later audit.
- `obvious relations`: The planner’s reviews mode is a real bridge, not just an optional comment layer.
- `candidate loose tags`: `adversarial-review`, `plan-pressure`, `consumer-contract`
- `intervention status`: `cross-cutting review lane`
- `classification status`: `placed provisionally`
- `confidence`: `high`
- `unresolved classification`: None at this level; the main issue is that the current high-level picture underplays how explicit the review-consumer contract is. Sources: [review.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/review.md:2), [review.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/review.md:242), [review.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/review.md:246), [review.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/review.md:300).

### `Implementation review and auto-fix family`
- `surface`: `code-review`, `code-review-fix`, and `audit-fix`
- `path`: [code-review.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/code-review.md:1), [code-review-fix.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/code-review-fix.md:1), [audit-fix.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/audit-fix.md:1)
- `repo-local role as stated by source`: Review changed implementation surfaces, auto-fix review findings, or run an end-to-end audit-to-fix loop for UAT-derived findings.
- `reads/expects`: Changed-file scope, `REVIEW.md`, UAT/verification findings, fixability classification.
- `emits/returns`: `REVIEW.md`, `REVIEW-FIX.md`, atomic fix commits, audit-fix summary status.
- `downstream consumers`: Developers, shipping, follow-up verification, human review.
- `obvious relations`: These are not part of the main phase spine, but they materially change how “complete” execution can become before shipping.
- `candidate loose tags`: `implementation-review`, `repair-loop`, `auto-fix`, `post-phase`
- `intervention status`: `cross-cutting fix lane`
- `classification status`: `cross-cutting`
- `confidence`: `medium-high`
- `unresolved classification`: The family spans both phase-local review and broader audit-driven repair, so the next map should show it as a side-lane cluster rather than one box tied to a single mainline stage.

### `Routing and state-detection family`
- `surface`: `do`, `progress`, and `next`
- `path`: [do.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/do.md:1), [progress.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/progress.md:1), [next.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/next.md:1)
- `repo-local role as stated by source`: Route freeform requests or current project state to the right next workflow step.
- `reads/expects`: `.planning` existence, init/state snapshots, roadmap counts, current phase disk status, verification/UAT debt.
- `emits/returns`: Recommendations or direct routing into discuss/plan/execute/verify/complete flows.
- `downstream consumers`: User/operator and every major lifecycle lane.
- `obvious relations`: These are control surfaces, not lifecycle stages; `progress` and `next` especially encode stateful routing logic that depends on completion/debt distinctions.
- `candidate loose tags`: `router`, `state-detector`, `operator-control`
- `intervention status`: `operator router`
- `classification status`: `cross-cutting`
- `confidence`: `high`
- `unresolved classification`: None; the current picture simply needs to stop treating routing as a thin UI nicety. Sources: [do.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/do.md:1), [progress.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/progress.md:197), [next.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/next.md:140).

### `Session continuity family`
- `surface`: `pause-work` and `resume-project`
- `path`: [pause-work.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/pause-work.md:1), [resume-project.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/resume-project.md:1)
- `repo-local role as stated by source`: Preserve and restore work state across sessions via machine-readable and human-readable handoff artifacts.
- `reads/expects`: Current phase/spike/deliberation context, `STATE.md`, summaries, handoff files, interrupted-agent state.
- `emits/returns`: `.planning/HANDOFF.json`, context-local `.continue-here.md`, updated session continuity in `STATE.md`, reconstructed `STATE.md` when missing.
- `downstream consumers`: `resume-project`, humans resuming work, and `execute-phase`, which reads `.continue-here.md` for blocking anti-patterns.
- `obvious relations`: Continuity is not only a human convenience layer; execution itself consults the continuation artifact when present.
- `candidate loose tags`: `handoff`, `resume`, `continuity`, `anti-pattern-memory`
- `intervention status`: `cross-cutting support lane`
- `classification status`: `cross-cutting`
- `confidence`: `high`
- `unresolved classification`: The next map should show both the write side (`pause-work`) and the read side (`resume-project` and `execute-phase`) or it will understate how load-bearing continuity artifacts already are. Sources: [pause-work.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/pause-work.md:27), [pause-work.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/pause-work.md:62), [resume-project.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/resume-project.md:29), [resume-project.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/resume-project.md:284), [execute-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/execute-phase.md:139).

### `Top-level multi-phase orchestration family`
- `surface`: `manager` and `autonomous`
- `path`: [manager.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/manager.md:1), [autonomous.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/autonomous.md:1)
- `repo-local role as stated by source`: Orchestrate multiple phases from above the ordinary single-phase chain.
- `reads/expects`: Milestone context, recommended actions, dashboard state, phase ranges, UI flags, audit status.
- `emits/returns`: Background dispatch, chained skill invocations, dashboard routing, milestone-close progression.
- `downstream consumers`: Core lifecycle skills, milestone audit/cleanup, user operator.
- `obvious relations`: `manager` mixes inline discuss with background plan/execute dispatch; `autonomous` walks phase after phase and can invoke UI phase, gap closure, milestone audit, completion, and cleanup.
- `candidate loose tags`: `meta-orchestrator`, `milestone-control`, `parallel-dispatch`
- `intervention status`: `top-level control surface`
- `classification status`: `cross-cutting`
- `confidence`: `high`
- `unresolved classification`: These surfaces are not just routers; they are macro-workflows that recompose several other families. The next map should give them a separate control layer. Sources: [manager.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/manager.md:19), [manager.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/manager.md:201), [autonomous.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/autonomous.md:3), [autonomous.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/autonomous.md:303), [autonomous.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/autonomous.md:883).

### `Quick and fast alternative execution family`
- `surface`: `quick` and `fast`
- `path`: [quick.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/quick.md:1), [fast.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/fast.md:1)
- `repo-local role as stated by source`: Offer reduced-overhead alternatives to the main phase chain: `quick` keeps GSD guarantees while shrinking scope; `fast` rejects planning/research entirely for trivial inline work.
- `reads/expects`: Ad hoc task description, planner/executor/checker/verifier availability for quick mode, current `STATE.md`.
- `emits/returns`: Quick-task `PLAN.md` / `SUMMARY.md` under `.planning/quick/` or, for `fast`, only commits plus optional `STATE.md` logging.
- `downstream consumers`: Developers needing non-phase work, shipping/review if those quick tasks become material.
- `obvious relations`: `quick --full` partially recreates the core chain; `fast` is an explicit escape hatch that refuses the chain.
- `candidate loose tags`: `alternative-lane`, `ad-hoc`, `trivial-inline`, `mini-pipeline`
- `intervention status`: `alternative execution lane`
- `classification status`: `cross-cutting`
- `confidence`: `high`
- `unresolved classification`: The next map should keep these visible but separate from the main phase lifecycle, because they intentionally change the chain contract. Sources: [quick.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/quick.md:1), [quick.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/quick.md:444), [fast.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/fast.md:24), [fast.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/fast.md:92).

### `Lifecycle mutation and archive family`
- `surface`: `new-project`, `new-milestone`, `add-phase`, `insert-phase`, `remove-phase`, `plan-milestone-gaps`, `analyze-dependencies`, `complete-milestone`, and `cleanup`
- `path`: [new-project.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/new-project.md:1), [new-milestone.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/new-milestone.md:1), [add-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/add-phase.md:1), [insert-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/insert-phase.md:1), [remove-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/remove-phase.md:1), [plan-milestone-gaps.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/plan-milestone-gaps.md:1), [analyze-dependencies.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/analyze-dependencies.md:1), [complete-milestone.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/complete-milestone.md:1), [cleanup.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/cleanup.md:1)
- `repo-local role as stated by source`: Create, reshape, or archive the project’s phase/milestone topology rather than executing the existing topology.
- `reads/expects`: Project context, roadmap, requirements, milestone audit outputs, milestone archive directories, dependency heuristics.
- `emits/returns`: New roadmap structure, milestone archives, `MILESTONES.md`, gap-closure phases, phase renumbering, cleaned phase directories.
- `downstream consumers`: Every mainline lifecycle lane, future milestones, archival browsing.
- `obvious relations`: `plan-milestone-gaps` consumes `MILESTONE-AUDIT.md`; `autonomous` later calls `audit-milestone`, `complete-milestone`, and `cleanup`.
- `candidate loose tags`: `topology-mutation`, `archive`, `milestone-control`, `roadmap-reshape`
- `intervention status`: `lifecycle mutation`
- `classification status`: `placed provisionally`
- `confidence`: `high`
- `unresolved classification`: The current high-level picture barely represents roadmap/milestone mutation even though these surfaces materially change what the core chain will run next.

### `Operational admin, shipping, and workspace family`
- `surface`: `settings`, `health`, `update`, `help`, `stats`, `ship`, `pr-branch`, `new-workspace`, `list-workspaces`, and `remove-workspace`
- `path`: [settings.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/settings.md:1), [health.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/health.md:1), [update.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/update.md:1), [help.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/help.md:1), [stats.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/stats.md:1), [ship.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/ship.md:1), [pr-branch.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/pr-branch.md:1), [new-workspace.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/new-workspace.md:1), [list-workspaces.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/list-workspaces.md:1), [remove-workspace.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/remove-workspace.md:1)
- `repo-local role as stated by source`: Configure the runtime, validate planning integrity, update GSD, expose operator reference/status, prepare PR-ready history, ship completed work, and manage isolated workspaces.
- `reads/expects`: `.planning/config.json`, runtime install state, git state, planning artifacts, workspace manifests.
- `emits/returns`: Config changes, health findings, update/install actions, status/reference outputs, PRs/branches, workspace directories.
- `downstream consumers`: Human operators and later execution/review/shipping work.
- `obvious relations`: These are not “mainline stages,” but they materially shape the environment and exit surfaces the mainline depends on.
- `candidate loose tags`: `admin`, `shipping`, `workspace`, `runtime-hygiene`
- `intervention status`: `operator support lane`
- `classification status`: `cross-cutting`
- `confidence`: `high`
- `unresolved classification`: `ship` is already present in the current simplified map, but `pr-branch` and workspace control show that shipping/isolation is really a larger family than one terminal “ship” node.

### `Auxiliary documentation, mapping, and capture family`
- `surface`: `map-codebase`, `scan`, `docs-update`, `add-todo`, `check-todos`, `note`, `plant-seed`, `session-report`, `inbox`, `profile-user`
- `path`: [map-codebase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/map-codebase.md:1), [scan.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/scan.md:1), [docs-update.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/docs-update.md:1), [add-todo.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/add-todo.md:1), [check-todos.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/check-todos.md:1), [note.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/note.md:1), [plant-seed.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/plant-seed.md:1), [session-report.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/session-report.md:1), [inbox.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/inbox.md:1), [profile-user.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/profile-user.md:1)
- `repo-local role as stated by source`: Generate side-car knowledge artifacts, maintain documentation/codebase intelligence, and capture future work or developer/operator context.
- `reads/expects`: Codebase, planning state, docs inventories, GitHub contribution templates, session state.
- `emits/returns`: `.planning/codebase/*`, docs work manifests, todos/notes/seeds, session reports, inbox review outputs, profiling artifacts.
- `downstream consumers`: Humans, later planning lanes, milestone and onboarding work.
- `obvious relations`: These surfaces can influence later planning, but they are not cleanly embedded in the core phase chain.
- `candidate loose tags`: `auxiliary-artifact`, `knowledge-capture`, `docs`, `intelligence`
- `intervention status`: `auxiliary cross-cutting`
- `classification status`: `unplaced`
- `confidence`: `medium`
- `unresolved classification`: This is the loosest cluster in the inventory; the safest next-map move is to keep it as an auxiliary strip/legend rather than pretend it is one coherent lifecycle family.

## Internal-Only And Bridge Flows

- [e:c:i] `execute-plan.md` is a real internal execution surface, not just an implementation detail hidden inside execute-phase. `execute-phase` explicitly tells interactive mode to read and follow it inline, and the file itself owns `SUMMARY.md`, `STATE.md`, `ROADMAP.md`, and `REQUIREMENTS.md` writes or deferrals. Sources: [execute-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/execute-phase.md:189), [execute-plan.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/execute-plan.md:351), [execute-plan.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/execute-plan.md:408), [execute-plan.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/execute-plan.md:424).
- [e:c:i] `transition.md` is explicitly internal-only, but it is load-bearing because both `execute-phase` and `verify-work` use it to mark phases complete and route toward the next phase. Sources: [transition.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/transition.md:3), [execute-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/execute-phase.md:1470), [verify-work.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/verify-work.md:445).
- [e:c:i] `diagnose-issues.md` is the key bridge between human/UAT symptom capture and targeted gap planning. Without it, the map falsely suggests `verify-work` goes straight from “issue found” to “plan fixes,” when the documented flow is “diagnose root cause first.” Sources: [verify-work.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/verify-work.md:488), [diagnose-issues.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/diagnose-issues.md:21), [diagnose-issues.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/diagnose-issues.md:94).
- [e:c:i] `discuss-phase-assumptions.md` and `discuss-phase-power.md` are bridge-like subflows inside the same entry family, because the wrapper can route to them while still presenting one visible command name to the user. Sources: [gsd-discuss-phase/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/.codex/skills/gsd-discuss-phase/SKILL.md:86), [discuss-phase-assumptions.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/discuss-phase-assumptions.md:1), [discuss-phase-power.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/discuss-phase-power.md:7).
- [e:c:i] `verify-phase.md` is a bridge surface between execution and user-facing verification. Its existence means the workflow topology distinguishes automated goal-backward verification from later conversational UAT, even though a simplified picture could mistakenly merge them. Sources: [verify-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/verify-phase.md:1), [execute-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/execute-phase.md:1225), [verify-work.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/verify-work.md:1).
- [e:c:i] `discovery-phase.md` behaves as a planning support bridge rather than a top-level peer of `plan-phase`; its own purpose says it is called from `plan-phase`’s mandatory discovery step with a depth parameter. Sources: [discovery-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/discovery-phase.md:1), [discovery-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/discovery-phase.md:19).

## Emitted Artifact Carriers

- [e:c:i] The current simplified artifact spine already shows `CONTEXT -> RESEARCH -> PLAN -> SUMMARY -> VERIFICATION / UAT / REVIEWS`, but the workflow corpus emits materially more carriers than that backbone alone suggests. Sources: [checkpoint-5-gsd-local-topology-schema.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-local-topology-schema.md:46), [checkpoint-5-gsd-local-topology-schema.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-local-topology-schema.md:146).
- [e:c:i] Steering capture is not only `CONTEXT.md`. `discuss-phase` also writes `DISCUSSION-LOG.md` and a resumable `DISCUSS-CHECKPOINT.json`, while power mode writes `QUESTIONS.json` and `QUESTIONS.html` before final context generation. Sources: [discuss-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/discuss-phase.md:893), [discuss-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/discuss-phase.md:941), [discuss-phase-power.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/discuss-phase-power.md:31), [discuss-phase-power.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/discuss-phase-power.md:97).
- [e:c:i] Planning-side carriers go beyond `RESEARCH.md` and `PLAN.md`: `discovery-phase` can emit `DISCOVERY.md`, `plan-phase` can emit `VALIDATION.md`, `ui-phase` emits `UI-SPEC.md`, and `ai-integration-phase` emits `AI-SPEC.md`. Sources: [discovery-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/discovery-phase.md:3), [plan-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/plan-phase.md:431), [ui-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/ui-phase.md:132), [ai-integration-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/ai-integration-phase.md:153), [ai-integration-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/ai-integration-phase.md:183).
- [e:c:i] Execution and verification also emit more than `SUMMARY.md` and `VERIFICATION.md`: `execute-phase` persists `HUMAN-UAT.md`, `verify-work` maintains `UAT.md`, `diagnose-issues` creates `DEBUG-*.md`, and `execute-phase` can write regression/debt follow-through that later audits consume. Sources: [execute-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/execute-phase.md:1267), [verify-work.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/verify-work.md:1), [diagnose-issues.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/diagnose-issues.md:78), [execute-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/execute-phase.md:1085).
- [e:c:i] Review and post-implementation audit carriers are also broader than the current picture: `REVIEW.md`, `REVIEW-FIX.md`, `UI-REVIEW.md`, `EVAL-REVIEW.md`, `VALIDATION.md`, `SECURITY.md`, and `MILESTONE-AUDIT.md` all have dedicated workflows or follow-through lanes. Sources: [code-review.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/code-review.md:2), [code-review-fix.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/code-review-fix.md:2), [ui-review.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/ui-review.md:1), [eval-review.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/eval-review.md:1), [validate-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/validate-phase.md:1), [secure-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/secure-phase.md:1), [audit-milestone.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/audit-milestone.md:2).
- [e:c:i] Continuity and operator-side carriers matter too: `pause-work` writes `HANDOFF.json` and `.continue-here.md`; `session-report` writes `SESSION_REPORT.md`; `complete-milestone` and `cleanup` emit archive surfaces that change what remains on the active planning surface. Sources: [pause-work.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/pause-work.md:1), [pause-work.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/pause-work.md:104), [session-report.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/session-report.md:1), [complete-milestone.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/complete-milestone.md:21), [cleanup.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/cleanup.md:3).

## Unplaced Or Cross-Cutting Workflow Surfaces

- [e:c:i] `do`, `progress`, and `next` are cross-cutting control surfaces, not lifecycle stages. They read state and decide which lifecycle surface should run next. Sources: [do.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/do.md:2), [progress.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/progress.md:2), [next.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/next.md:2).
- [e:c:i] `manager` and `autonomous` are also cross-cutting, but at a different scale: they recompose multiple lifecycle steps across many phases or an entire milestone. Sources: [manager.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/manager.md:3), [autonomous.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/autonomous.md:3).
- [e:c:i] `quick` and `fast` are alternative execution lanes that intentionally modify or bypass the standard chain contract. They should stay visible as alternatives, not be tucked under ordinary phase execution. Sources: [quick.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/quick.md:2), [fast.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/fast.md:2).
- [e:c:i] Admin/runtime hygiene surfaces remain cross-cutting: `settings`, `health`, `update`, `help`, and `stats` shape or inspect the environment rather than executing project work. Sources: [settings.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/settings.md:2), [health.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/health.md:2), [update.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/update.md:2), [help.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/help.md:2), [stats.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/stats.md:2).
- [e:c:i] Workspace isolation surfaces (`new-workspace`, `list-workspaces`, `remove-workspace`) and shipping surfaces (`ship`, `pr-branch`) are similarly cross-cutting: they change where or how work is managed rather than belonging to one lifecycle stage. Sources: [new-workspace.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/new-workspace.md:2), [list-workspaces.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/list-workspaces.md:2), [remove-workspace.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/remove-workspace.md:2), [ship.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/ship.md:2), [pr-branch.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/pr-branch.md:2).
- [e:c:i] Knowledge/documentation/capture surfaces (`map-codebase`, `scan`, `docs-update`, `add-todo`, `check-todos`, `note`, `plant-seed`, `session-report`, `inbox`, `profile-user`) are best preserved as an auxiliary strip for now. They emit durable artifacts, but they do not yet belong cleanly to one mainline workflow family. Sources: [map-codebase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/map-codebase.md:2), [docs-update.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/docs-update.md:2), [add-todo.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/add-todo.md:2), [note.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/note.md:2), [plant-seed.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/plant-seed.md:2), [session-report.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/session-report.md:2), [inbox.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/inbox.md:2), [profile-user.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/profile-user.md:2).

## What The Current High-Level Picture Misses

- [e:r:i] The current local topology schema already models the core chain, but it compresses the entire discuss family into one node. That hides the fact that one visible entrypoint fans into standard, assumptions, and power workflows with different artifact behavior (`DISCUSS-CHECKPOINT.json` versus `QUESTIONS.json/html`) and different information-gathering posture. Sources: [checkpoint-5-gsd-local-topology-schema.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-local-topology-schema.md:82), [checkpoint-5-gsd-local-topology-schema.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-local-topology-schema.md:138), [gsd-discuss-phase/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/.codex/skills/gsd-discuss-phase/SKILL.md:69), [discuss-phase-power.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/discuss-phase-power.md:31).
- [e:r:i] The current picture underrepresents planning-side subflows. `plan-phase` is not only “research -> planner -> checker”; it also owns PRD-express context creation, validation output, and explicit inserted contract branches like `ui-phase`, while `discovery-phase` exists as a narrower planning-support lane. Sources: [checkpoint-5-gsd-local-topology-schema.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-local-topology-schema.md:109), [plan-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/plan-phase.md:501), [ui-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/ui-phase.md:2), [discovery-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/discovery-phase.md:5).
- [e:r:i] The current picture treats execution as a single box plus an internal `transition`, but the workflow corpus shows at least three distinct internal surfaces: `execute-phase` orchestration, `execute-plan` actual plan execution, and a separate goal-backward verification subworkflow before human UAT. Sources: [checkpoint-5-gsd-local-topology-schema.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-local-topology-schema.md:114), [execute-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/execute-phase.md:189), [execute-plan.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/execute-plan.md:2), [verify-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/verify-phase.md:2).
- [e:r:i] The current picture underplays the explicit UAT-diagnosis-gap-closure loop. It shows `verify-work` and `transition`, but it does not expose `diagnose-issues.md` or the fact that UAT issues are supposed to become root-caused findings before `plan-phase --gaps` reruns. Sources: [checkpoint-5-gsd-local-topology-schema.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-local-topology-schema.md:119), [verify-work.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/verify-work.md:488), [diagnose-issues.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/diagnose-issues.md:23).
- [e:r:i] The current picture treats routing lightly. In practice, `do`, `progress`, `next`, `manager`, and `autonomous` are their own control layer that determines how often the mainline is entered, skipped, recomposed, or resumed. Sources: [checkpoint-5-gsd-local-topology-schema.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-local-topology-schema.md:86), [progress.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/progress.md:2), [next.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/next.md:2), [manager.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/manager.md:3), [autonomous.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/autonomous.md:3).
- [e:r:i] The current picture barely acknowledges continuity and archive/mutation surfaces. `pause-work`/`resume-project` and the milestone/phase mutation family change how the chain restarts, what topology exists, and what remains on the active planning surface. Sources: [pause-work.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/pause-work.md:2), [resume-project.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/resume-project.md:10), [new-milestone.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/new-milestone.md:3), [complete-milestone.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/complete-milestone.md:3), [cleanup.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/cleanup.md:3).
- [e:r:i] Checkpoint 3 explicitly kept many peripheral workflows out of the excellence envelope on purpose; Checkpoint 5’s raw inventory job is precisely to surface those broader families before later ontology synthesis. Sources: [checkpoint-3-gsd-surface-map.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-surface-map.md:61), [checkpoint-5-gsd-raw-inventory-bundle-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-bundle-spec.md:5), [checkpoint-5-gsd-raw-inventory-bundle-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-bundle-spec.md:92).

## Recommended Additions To The Next Map

- [p:r:i] Add a `Discuss family` node with internal branches for `standard`, `assumptions`, and `power` rather than a single flat discuss box. Show the extra artifact carriers (`DISCUSS-CHECKPOINT.json`, `QUESTIONS.json`, `QUESTIONS.html`) on that branch.
- [p:r:i] Split planning support into at least three visible nodes: `research/discovery`, `plan-phase`, and `inserted design contracts` (`UI-SPEC`, optionally `AI-SPEC`). Do not imply that the planner always operates on only `CONTEXT + RESEARCH + PLAN`.
- [p:r:i] Split execution into `execute-phase` orchestration, `execute-plan` internal execution, `goal-backward verification`, and `persistent UAT / diagnosis / gap-closure`. This is the most important anti-simple-picture addition.
- [p:r:i] Add a separate `router/control` layer containing `do`, `progress`, `next`, `manager`, and `autonomous`. The current picture is too lifecycle-centric to explain how work is actually entered and resumed.
- [p:r:i] Add a `continuity` layer with `pause-work`, `resume-project`, `.continue-here.md`, and `HANDOFF.json`, and draw the read edge from execution back into those continuity artifacts.
- [p:r:i] Add a `topology mutation / archive` layer for `new-project`, `new-milestone`, phase insertion/removal, `plan-milestone-gaps`, `analyze-dependencies`, `complete-milestone`, and `cleanup`.
- [p:r:i] Keep `quick` and `fast` visible as explicit alternative lanes, not footnotes under the normal phase chain.
- [p:r:i] Represent the broader artifact surface explicitly, either as a side legend or an “emitted carrier” strip, so the next synthesis does not silently forget `UI-SPEC`, `AI-SPEC`, `DISCOVERY`, `REVIEW`, `REVIEW-FIX`, `VALIDATION`, `SECURITY`, `UI-REVIEW`, `EVAL-REVIEW`, `MILESTONE-AUDIT`, `HANDOFF`, and `SESSION_REPORT`.
- [p:r:i] Preserve auxiliary cross-cutting families (`docs-update`, `map-codebase`, todo/note/seed capture, workspaces, shipping/pr-branch) in a separate auxiliary band or appendix node group. They are real workflow surfaces, but the repo evidence is not yet strong enough to force them into the same ontology as the core phase chain.
