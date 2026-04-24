# 01 Codex Orchestration Layer Audit

## Research Frame
- Mode: `synthesis`
- Question: At the Codex orchestration layer, what is already working, what is structurally weak, and what should change so the main thread behaves like a strong orchestrator rather than a shallow do-everything worker?
- Scope: Codex-layer control surfaces in this repo: subagent delegation defaults, task-boundary handling, context pressure, runtime verification discipline, hooks, and visible orchestration guardrails.
- Non-goals:
  - redesigning repo-local GSD as a general product
  - deep Git/worktree/branch policy design beyond Codex-layer handoff points
  - CI, release, or deployment design beyond stating what should be handed off
  - relitigating Prix Guesser product doctrine
- Stop condition: identify Codex-layer strengths, weaknesses, near-term changes, later changes, and the right split between prompt/policy, hooks, commands/skills, and runtime verification/reporting.

## Motivating grounds
- `.planning/knowledge/signals/prix-guesser/2026-04-15-underdelegated-exploration-orchestrator-role-drift.md`
  - The main thread retained exploratory and scope-shaping work that should have moved into bounded worker lanes.
- `.planning/knowledge/signals/prix-guesser/2026-04-15-dirty-task-transitions-mixed-worktree.md`
  - The orchestrator crossed substantive task boundaries without clean disposition of the previous bucket.
- `.planning/research/2026-04-15-orchestration-framework-audit/01-orchestration-and-task-transition-failure-audit.md`
  - The prior audit already showed that the failure was not "no delegation" but "delegation without closure and transition control."
- `.planning/research/2026-04-15-orchestration-framework-audit/04-converged-synthesis.md`
  - The converged result already identified subagent-first exploration and task-transition gating as immediate needs.
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-worktree-stabilization-note.md`
  - The repo had to recover concern buckets after the fact because the Codex layer did not stop sooner.
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-git-cleanup-checkpoint-plan.md`
  - The cleanup plan makes clear that Codex-layer ambiguity was not just cosmetic; it degraded reviewable change-set control.
- `AGENTS.md`
  - The repo already formalizes top-level orchestration, spawn classification, and runtime verification, so this lane is evaluating a real doctrine surface, not an empty one.

## Artifacts Read
- `AGENTS.md`
- `.planning/AGENTS.md`
- `WORKFLOW.md`
- `AI-GUARDRAILS.md`
- `.codex/hooks.json`
- `.codex/hooks/session_start_guardrail.py`
- `.codex/hooks/pre_tool_use_guardrail.py`
- `.codex/config.toml`
- `.planning/config.json`
- `.planning/LONG-ARC.md`
- `.planning/PROJECT.md`
- `.planning/STATE.md`
- `.planning/knowledge/index.md`
- `.planning/knowledge/signals/prix-guesser/2026-04-08-recursive-gsd-orchestration.md`
- `.planning/knowledge/signals/prix-guesser/2026-04-08-manual-substitute-planning.md`
- `.planning/knowledge/signals/prix-guesser/2026-04-08-premature-stall-diagnosis.md`
- `.planning/knowledge/signals/prix-guesser/2026-04-15-dirty-task-transitions-mixed-worktree.md`
- `.planning/knowledge/signals/prix-guesser/2026-04-15-underdelegated-exploration-orchestrator-role-drift.md`
- `.planning/research/2026-04-15-orchestration-framework-audit/00-launch-bundle-spec.md`
- `.planning/research/2026-04-15-orchestration-framework-audit/01-orchestration-and-task-transition-failure-audit.md`
- `.planning/research/2026-04-15-orchestration-framework-audit/03-guardrails-mechanisms-and-command-proposals.md`
- `.planning/research/2026-04-15-orchestration-framework-audit/04-converged-synthesis.md`
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-worktree-stabilization-note.md`
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-git-cleanup-checkpoint-plan.md`
- `.planning/research/2026-04-15-multilayer-harness-governance-audit/00-launch-bundle-spec.md`
- local runtime verification state required by repo policy: `~/.codex/state_5.sqlite`

## Path Of Inquiry
- Entry point:
  - The user's complaint that the orchestrator kept exploratory work in the main thread, moved across buckets with a messy tree, and relied too much on conversational discipline.
- Branches considered:
  - whether the Codex problem was mainly launch settings
  - whether it was mainly weak hooks
  - whether it was mainly missing task-disposition structure
  - whether it was mainly a GSD-layer lifecycle problem rather than Codex itself
  - whether current failures included output-delivery and child-thread closure gaps
- Branches pursued:
  - launch discipline versus closure discipline
  - subagent-default behavior
  - task-transition and concern-bucket control
  - hook posture versus command/skill posture
  - runtime verification and reporting gaps
- Branches deferred or abandoned:
  - deep branch/worktree policy design
  - CI/release/deployment enforcement design
  - product-doctrine ratification questions
- Unexpected branches / reframings:
  - the repo already has stronger Codex orchestration doctrine than a generic setup
  - the biggest remaining Codex-layer weakness is not spawn configuration alone; it is the missing lifecycle object between `launched` and `safely closed`
  - the current multi-layer bundle itself exposed a second-order weakness: runtime-valid launches can still remain operationally `open` without output closure

## Assumptions Surfaced
- `[a:c+r:i]` Exploratory, ambiguity-heavy, and scope-shaping work should default to dedicated worker lanes rather than main-thread local exploration ([2026-04-15-underdelegated-exploration-orchestrator-role-drift.md](/home/rookslog/workspace/projects/prix-guesser/.planning/knowledge/signals/prix-guesser/2026-04-15-underdelegated-exploration-orchestrator-role-drift.md:25), [01-orchestration-and-task-transition-failure-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-orchestration-framework-audit/01-orchestration-and-task-transition-failure-audit.md:196)).
  - Why it matters: this is the load-bearing distinction between "strong orchestrator" and "do-everything worker."
  - Current status: strongly supported by the 2026-04-15 underdelegation signal and the prior orchestration audit.
  - What could weaken it: a bounded case where local exploration is only a short prelude to a worker spec and no unresolved task bucket exists.
- `[a:c+r:i]` Mid-session task transitions are too nuanced for broad blocking hooks and too important to leave as ambient habit ([WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:113), [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:116), [.codex/hooks.json](/home/rookslog/workspace/projects/prix-guesser/.codex/hooks.json:2), [.codex/hooks/session_start_guardrail.py](/home/rookslog/workspace/projects/prix-guesser/.codex/hooks/session_start_guardrail.py:46), [.codex/hooks/pre_tool_use_guardrail.py](/home/rookslog/workspace/projects/prix-guesser/.codex/hooks/pre_tool_use_guardrail.py:8)).
  - Why it matters: it pushes the solution toward visible commands/workflow gates rather than opaque denials.
  - Current status: supported by `WORKFLOW.md` hook posture and by the repo's repeated dislike of hidden control.
  - What could weaken it: much richer hook capabilities with clear operator-facing explanations, which the repo does not have now.
- `[a:c+r:i]` Runtime-valid launch settings are necessary but insufficient evidence that orchestration is working correctly ([AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:136), [AI-GUARDRAILS.md](/home/rookslog/workspace/projects/prix-guesser/AI-GUARDRAILS.md:89), [.codex/get-shit-done/workflows/execute-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/execute-phase.md:20)).
  - Why it matters: this distinguishes `requested/effective runtime` from `artifact delivered/dispositioned`.
  - Current status: supported by the earlier reasoning-effort mismatch signal and by the current bundle's open-child-thread state.
  - What could weaken it: evidence that open thread status always self-resolves promptly and the missing artifacts were only a temporary observation.

## Evidence Base
### Direct evidence
- `AGENTS.md` already requires:
  - top-level Codex orchestration
  - explicit task classification before spawn
  - requested model/reasoning mapping
  - effective runtime verification against `~/.codex/state_5.sqlite`
- The repo already formalized three prior Codex-layer failures into standing signals:
  - recursive orchestration (`2026-04-08-recursive-gsd-orchestration.md`)
  - premature stall diagnosis (`2026-04-08-premature-stall-diagnosis.md`)
  - manual substitute planning (`2026-04-08-manual-substitute-planning.md`)
- The 2026-04-15 signals add two more Codex-specific failures:
  - underdelegated exploration / orchestrator role drift
  - dirty task transitions / mixed worktree hygiene
- `.codex/get-shit-done/workflows/execute-phase.md` explicitly says:
  - "Orchestrator stays lean"
  - "Orchestrator coordinates, not executes"
  - spawned-agent completion should be checked via artifacts and git state, not only by waiting for signals
- `.codex/get-shit-done/workflows/plan-phase.md`, `progress.md`, and `map-codebase.md` all contain explicit context-minimization and subagent-oriented language rather than assuming a monolithic main thread.
- `.codex/hooks.json` currently limits hooks to:
  - a `SessionStart` reminder hook
  - a `PreToolUse` destructive-Bash deny hook
- `.codex/hooks/session_start_guardrail.py` checks:
  - `main` branch
  - dirty tree
  - Phase 01 pre-rerun boundary
  - it does not classify concern buckets or block mid-session drift
- `.codex/hooks/pre_tool_use_guardrail.py` denies only obviously destructive commands.
- `.codex/config.toml` sets:
  - `model = "gpt-5.4"`
  - `model_reasoning_effort = "high"`
  - `plan_mode_reasoning_effort = "xhigh"`
- `.planning/config.json` sets:
  - `mode = "yolo"`
  - `workflow.auto_advance = true`
  - `git.branching_strategy = "none"`
  - `workflow.discuss_mode = "exploratory"`
- `.planning/research/2026-04-15-orchestration-framework-audit/00-launch-bundle-spec.md` records that the earlier orchestration-framework bundle spec was written after workers had already launched; the repo itself marked that as an auditability failure.
- Current runtime verification for the multi-layer bundle showed four lane workers with effective `model = gpt-5.4` and `reasoning_effort = xhigh`, but before this file was closed the bundle still had:
  - `thread_spawn_edges.status = open` for all four lanes
  - missing lane output files under `.planning/research/2026-04-15-multilayer-harness-governance-audit/`
  This is direct evidence that launch verification exists, but closure reporting remains weak.

### Inference and interpretation
- `[e:c+r:i]` The repo is already stronger on `launch discipline` than on `task closure discipline` ([AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:111), [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:117), [.codex/config.toml](/home/rookslog/workspace/projects/prix-guesser/.codex/config.toml:1), [00-launch-bundle-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-orchestration-framework-audit/00-launch-bundle-spec.md:135)).
  - It knows how to classify spawns, verify runtime settings, and avoid recursive call graphs.
  - It does not yet have a first-class `disposition` object that governs what must happen after a worker returns or while a worker remains open.
- `[e:c+r:i]` The missing Codex-layer mechanism is not "more hooks everywhere." It is visible structure around ([WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:113), [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:116), [.codex/hooks.json](/home/rookslog/workspace/projects/prix-guesser/.codex/hooks.json:2), [.codex/hooks/session_start_guardrail.py](/home/rookslog/workspace/projects/prix-guesser/.codex/hooks/session_start_guardrail.py:46), [.codex/hooks/pre_tool_use_guardrail.py](/home/rookslog/workspace/projects/prix-guesser/.codex/hooks/pre_tool_use_guardrail.py:8)):
  - active task ownership
  - returned-task disposition
  - multi-lane bundle auditability
  - child-thread closure reporting
- `[e:c+r:i]` Subagent capability is not the main problem. The repo already has the ability to launch strong workers. The main problem is that the main thread can still drift back into local exploration or forward into a new bucket without closing the previous one ([.codex/get-shit-done/workflows/execute-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/execute-phase.md:1), [2026-04-15-underdelegated-exploration-orchestrator-role-drift.md](/home/rookslog/workspace/projects/prix-guesser/.planning/knowledge/signals/prix-guesser/2026-04-15-underdelegated-exploration-orchestrator-role-drift.md:51), [2026-04-15-dirty-task-transitions-mixed-worktree.md](/home/rookslog/workspace/projects/prix-guesser/.planning/knowledge/signals/prix-guesser/2026-04-15-dirty-task-transitions-mixed-worktree.md:50)).
- `[e:c+r:i]` The current autonomy defaults pull against the repo's stated rigor bar. `mode: yolo` and `workflow.auto_advance: true` increase the chance that missing checkpoints are treated as acceptable momentum ([AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:49), [.planning/config.json](/home/rookslog/workspace/projects/prix-guesser/.planning/config.json:9), [03-guardrails-mechanisms-and-command-proposals.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-orchestration-framework-audit/03-guardrails-mechanisms-and-command-proposals.md:154)).

### Unknowns
- Whether `thread_spawn_edges.status = open` during the current bundle reflects:
  - a real child-thread lifecycle bug
  - delayed status propagation
  - or missing output-closeout conventions
- Whether the best Codex-layer solution should live primarily as:
  - repo doctrine in `AGENTS.md`
  - repo-local orchestration commands/skills
  - or local runtime helper scripts
- How aggressively to tighten autonomy defaults now, versus after the broader multi-layer bundle finishes and the Git/CI lanes add their own constraints

## Current Codex-Layer Strengths
### 1. The repo already has real top-level orchestration doctrine
`AGENTS.md` is not vague here. It explicitly prohibits recursive GSD call graphs, requires classification before spawn, and requires runtime verification after spawn. That is stronger than a generic "use subagents when helpful" posture.

### 2. Prior Codex failures have been converted into standing lessons
The repo did not merely complain about recursive delegation, manual substitute planning, or premature stall diagnosis. It recorded them as signals and translated them into live constraints. That means the Codex layer already supports learning, not just improvisation.

### 3. Lean-orchestrator patterns already exist in concrete workflows
`execute-phase.md`, `plan-phase.md`, `progress.md`, and `map-codebase.md` all explicitly try to minimize orchestrator context load and push work into specialized agents or targeted extraction calls. This is the right architectural direction for a repo that cares about long-horizon clarity.

### 4. The current hook posture is appropriately narrow
The hook pilot does useful low-ambiguity work:
- destructive-command denial
- startup reminders about branch, dirty tree, and rerun boundary

It does not pretend that hooks should solve nuanced doctrine or task-boundary judgment.

### 5. Runtime verification is treated as evidence, not as a cosmetic request
The repo already learned from the reasoning-effort mismatch signal that requested runtime settings are not proof. That is a meaningful Codex-layer strength, especially for a harness that depends on specific reasoning levels for architecture-setting work.

## Current Codex-Layer Weaknesses
### 1. Subagent-first behavior is still too optional for exploratory work
The repo now believes exploratory and scope-shaping work belongs in worker lanes, but that belief is still only partially operationalized. The 2026-04-15 underdelegation signal exists precisely because the main thread could still resume open-ended exploration locally.

### 2. Task disposition is not a first-class Codex control surface
There is still no durable Codex-layer object or command that forces:
- `accept`
- `revise`
- `park`
- `reject`

before a new substantive task begins. The prior orchestration audit identified this gap, and the cleanup artifacts had to reconstruct it afterward.

### 3. Mid-session task-transition hygiene is too reliant on self-discipline
The startup reminder hook can say the tree is dirty, but once the session is underway there is no visible, persistent Codex-layer guardrail that says:
- what the active substantive task is
- whether a returned worker has been dispositioned
- whether the next task is authorized to begin

### 4. Launch auditability is better than closure auditability
The repo can record launch bundles, runtime settings, and lane specs. It is still weaker at proving:
- which lanes are actually closed
- which worker outputs exist
- which returned tasks are accepted versus provisionally parked
- which "open" threads are real blockers versus stale bookkeeping

### 5. Current autonomy defaults are misaligned with doctrine-sensitive work
`mode: yolo` plus `workflow.auto_advance: true` is a throughput-friendly posture. This repo is explicitly not optimizing for throughput at any cost. On doctrine-heavy research and audit work, those defaults make quiet bypass of decision checkpoints more likely.

### 6. The Codex layer has no explicit active-task model
The cleanup artifacts had to invent `concern buckets` after the fact because the orchestration layer itself did not expose one active substantive task boundary that later work could violate visibly.

## Dependencies And Relations
| Item | Depends on | Constrains or affects | Vulnerability |
| --- | --- | --- | --- |
| Subagent-first exploration | clear task classification and bounded specs | research depth, main-thread focus, context hygiene | medium |
| Returned-task disposition | completed worker output plus orchestrator review | whether new substantive work may begin | high |
| Active substantive task model | visible concern-bucket ownership | transition hygiene, rollback clarity, review boundaries | high |
| Launch-bundle persistence | pre-spawn discipline and owned output paths | auditability and replayability of multi-lane work | medium |
| Runtime verification | `state_5.sqlite`, dispatch logging, artifact checks | requested/effective runtime honesty | medium |
| Child-thread closure reporting | runtime state plus filesystem/git evidence | ambiguous acceptance state, stalled-lane detection | high |
| Narrow hook posture | deterministic scripts and operator trust | low-noise safety automation | low |

## Recommended Near-Term Changes
- Make `exploratory / scope-shaping / audit-shaping` work subagent-first by default at the Codex layer, with the main thread limited to spec writing and integration.
- Add a mandatory task-disposition gate before any new substantive task: every returned worker must be marked `accept`, `revise`, `park`, or `reject`.
- Add an explicit `active substantive task` declaration to orchestration-sensitive work so the main thread cannot silently carry two unresolved buckets at once.
- Persist launch bundles before workers launch, not after, and include requested runtime, verified runtime, owned output path, and stop condition.
- Add runtime reporting that separates `requested`, `effective`, `artifact present`, and `dispositioned` so `open` does not masquerade as acceptable ambiguity.
- Tighten Codex-facing autonomy defaults for doctrine-heavy work, especially where `workflow.auto_advance` currently bypasses checkpoints.

## Recommended Later Changes
- Integrate task-transition awareness into `progress`, `resume`, and next-step routing so unresolved returned work is visible before more orchestration begins.
- Build a lightweight repo-local child-thread status view that combines runtime state with artifact presence and git evidence.
- Investigate whether open-child-thread status is a runtime bug, a polling gap, or a missing closeout convention, and then harden the reporting path accordingly.
- Consider whether certain research/audit bundle shapes deserve a first-class repo-local orchestration command rather than repeated manual launch-bundle authoring.

## Mechanisms By Control Surface
### Prompt / policy
- Adopt a standing rule: if work is exploratory, ambiguity-heavy, or scope-shaping, the default is `worker lanes first`, not main-thread exploration.
- Restrict main-thread local exploration to two cases:
  - preparing a bounded worker spec
  - integrating already returned outputs
- Require one declared `active substantive task` at a time unless a persisted launch bundle explicitly defines parallel lanes under one parent task.
- Require explicit disposition of every returned worker before a new substantive task begins.
- Preserve the distinction between:
  - main-thread orchestration discipline
  - worker capability
  - later Git/CI enforcement

Why prompt/policy, not hooks:
- These rules are doctrine-heavy and context-sensitive.
- They need to remain inspectable and explainable to the operator.

### Hook
- Keep the destructive-Bash deny hook exactly in the narrow, low-ambiguity lane it already occupies.
- Keep startup reminders for:
  - dirty tree
  - `main` branch
  - pre-rerun boundary
- If hook expansion happens at all, prefer non-blocking reminders for clearly detectable orchestration facts, such as:
  - an undispositioned active task artifact
  - a persisted launch bundle with missing owned outputs

What should not move into hooks:
- doctrinal nuance
- concern-bucket classification
- "should this task be delegated?" judgments
- "is this output good enough to accept?" judgments

### Command / skill
- Add a task-transition or disposition command that records:
  - active task
  - returned output(s)
  - `accept / revise / park / reject`
  - whether a new task is authorized
- Add a launch-bundle helper that writes `00-launch-bundle-spec.md` before the first worker launch and requires owned output paths and stop conditions.
- Add an agent-status or orchestration-status command that summarizes:
  - active worker threads
  - verified runtime settings
  - expected output files
  - whether outputs are present
  - whether each output has been dispositioned
- Extend `progress`/`next`-style routing so it can warn when the repo is about to cross a task boundary with unresolved Codex-layer work, not only when a roadmap phase is next.

Why command/skill is the right layer:
- These are reusable procedures.
- They benefit from visible outputs and explicit operator review.
- They are too nuanced for hooks and too structured to leave as ambient habit.

### Runtime verification / reporting
- Keep mandatory post-spawn verification against `~/.codex/state_5.sqlite`.
- Persist requested and effective runtime in repo artifacts, not only in commentary.
- Add a required closure check for spawned work:
  - output file exists
  - output file is non-empty and in the owned path
  - disposition recorded
  - if applicable, related git/artifact evidence exists
- Treat `runtime-valid but output-missing` as a blocked orchestration state, not as an ignorable pending state.
- Treat `thread still open` as a reporting input, not as the only truth source.

Why reporting matters:
- This repo already proved that launch settings can mismatch.
- The current bundle shows the dual problem: launch settings can match while closure remains ambiguous.

## What should not be solved at the Codex layer
- Branch protection, PR requirements, merge rules, and repository review policy
  - those belong mainly to the Git/repo-operations lane
- CI required checks, release promotion, deploy gates, rollback posture, and environment policy
  - those belong mainly to the CI/release/deployment lane
- Artifact retention and archive-branch policy
  - those belong to artifact governance plus Git operations, not Codex hooks
- Human-owned signoff on legal posture, branding, monetization, roadmap restructuring, or canon doctrine changes
  - `AI-GUARDRAILS.md` keeps those human-owned
- Nuanced product-doctrine decisions
  - the Codex layer should protect the path of inquiry and closure discipline, not auto-ratify doctrine

## How These Changes Preserve `LONG-ARC.md` And Future-Aware Rigor
The main long-arc risk at the Codex layer is not only hallucination. It is context flattening. When the main thread mixes unfinished integration duties with live exploration, open future branches get narrowed implicitly by convenience. That is exactly how wrapper order, identity seams, memory layers, and hosting distinctions can be quietly collapsed without any explicit decision artifact.

Subagent-first exploration helps because it gives open terrain enough depth to remain plural instead of being compressed into a quick main-thread answer. Task disposition helps because returned outputs cannot silently become canon-adjacent assumptions while still unreviewed. Active-task and closure reporting help because they keep long-arc doctrine, current execution scope, and deferred follow-up lanes from bleeding into one ambient "current work" blob.

In short:
- stronger Codex-layer orchestration preserves separation between exploration and ratification
- visible closure rules reduce hidden assumption carry-over
- better runtime reporting makes future-aware research auditable instead of memory-dependent
- narrow hooks avoid replacing doctrine with opaque denials

## What Can Close Now
- `[e:c+r:i]` The repo already has meaningful Codex-layer strengths around launch discipline, anti-recursion, and runtime honesty ([AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:111), [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:136), [.codex/config.toml](/home/rookslog/workspace/projects/prix-guesser/.codex/config.toml:1), [.codex/get-shit-done/workflows/execute-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/execute-phase.md:1)).
- `[e:c+r:i]` The main remaining Codex-layer defect is weak task closure and transition control, not lack of subagent capability ([2026-04-15-underdelegated-exploration-orchestrator-role-drift.md](/home/rookslog/workspace/projects/prix-guesser/.planning/knowledge/signals/prix-guesser/2026-04-15-underdelegated-exploration-orchestrator-role-drift.md:38), [2026-04-15-dirty-task-transitions-mixed-worktree.md](/home/rookslog/workspace/projects/prix-guesser/.planning/knowledge/signals/prix-guesser/2026-04-15-dirty-task-transitions-mixed-worktree.md:38), [01-orchestration-and-task-transition-failure-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-orchestration-framework-audit/01-orchestration-and-task-transition-failure-audit.md:180)).
- `[e:c+r:i]` The right immediate fixes are mostly policy, command/skill, and runtime-reporting changes, not broader blocking hooks ([WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:113), [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:116), [.codex/hooks.json](/home/rookslog/workspace/projects/prix-guesser/.codex/hooks.json:2), [03-guardrails-mechanisms-and-command-proposals.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-orchestration-framework-audit/03-guardrails-mechanisms-and-command-proposals.md:111)).
- `[e:c+r:i]` Deep Git/CI/deploy enforcement should be handed off to later lanes rather than absorbed here ([04-converged-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-orchestration-framework-audit/04-converged-synthesis.md:150)).

## What Must Stay Open
- `[o:i]` Whether child-thread `open` status reflects a true runtime bug or only incomplete closeout reporting
- `[o:i]` Exactly where new orchestration commands should live:
  - repo-local skill layer
  - `.codex/get-shit-done` overlay
  - or a thinner repo helper script layer
- `[o:i]` How much to tighten `workflow.auto_advance` and related defaults immediately versus after the broader multi-layer audit converges

## Planning Handoff
### What can now be treated as decided
- Codex-layer orchestration in this repo should become explicitly subagent-first for exploratory and scope-shaping work.
- Returned-task disposition is missing and should become first-class.
- Launch verification and closure verification are distinct responsibilities and both must be explicit.
- Narrow hooks remain the correct hook posture.

### What remains assumed or open
- exact command names and overlay placement
- whether open-child-thread reporting needs runtime debugging or only workflow hardening
- how hard the autonomy-default tightening should land in the short term

### Derived constraints
- Do not rely on startup reminders to solve mid-session drift.
- Do not let runtime-valid launch settings stand in for closure evidence.
- Do not use hooks as a substitute for active-task, disposition, or doctrine-sensitive judgment.

### Future-awareness seams to preserve
- `LONG-ARC.md` must remain a doctrine layer, not ambient memory carried informally by the current thread.
- exploratory bundle outputs must remain reviewable before they influence canon or roadmap work
- long-arc seams should be protected by orchestration clarity, not by silent main-thread convenience

### Deferred follow-up lanes
- `03-git-repo-operations-layer-audit.md`
  - branch/worktree/change-set discipline beyond Codex warnings
- `04-ci-release-and-deployment-layer-audit.md`
  - CI, release, deployment, rollback, and environment controls
- `05-cross-layer-integration-and-escalation-audit.md`
  - final assignment of which mechanism belongs to which layer

## Sources
- `AGENTS.md`
- `.planning/AGENTS.md`
- `WORKFLOW.md`
- `AI-GUARDRAILS.md`
- `.codex/config.toml`
- `.planning/config.json`
- `.codex/hooks.json`
- `.codex/hooks/session_start_guardrail.py`
- `.codex/hooks/pre_tool_use_guardrail.py`
- `.codex/get-shit-done/workflows/execute-phase.md`
- `.codex/get-shit-done/workflows/plan-phase.md`
- `.codex/get-shit-done/workflows/progress.md`
- `.codex/get-shit-done/workflows/map-codebase.md`
- `.planning/LONG-ARC.md`
- `.planning/PROJECT.md`
- `.planning/STATE.md`
- `.planning/knowledge/index.md`
- `.planning/knowledge/signals/prix-guesser/2026-04-08-recursive-gsd-orchestration.md`
- `.planning/knowledge/signals/prix-guesser/2026-04-08-manual-substitute-planning.md`
- `.planning/knowledge/signals/prix-guesser/2026-04-08-premature-stall-diagnosis.md`
- `.planning/knowledge/signals/prix-guesser/2026-04-15-dirty-task-transitions-mixed-worktree.md`
- `.planning/knowledge/signals/prix-guesser/2026-04-15-underdelegated-exploration-orchestrator-role-drift.md`
- `.planning/research/2026-04-15-orchestration-framework-audit/00-launch-bundle-spec.md`
- `.planning/research/2026-04-15-orchestration-framework-audit/01-orchestration-and-task-transition-failure-audit.md`
- `.planning/research/2026-04-15-orchestration-framework-audit/03-guardrails-mechanisms-and-command-proposals.md`
- `.planning/research/2026-04-15-orchestration-framework-audit/04-converged-synthesis.md`
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-worktree-stabilization-note.md`
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-git-cleanup-checkpoint-plan.md`
- `.planning/research/2026-04-15-multilayer-harness-governance-audit/00-launch-bundle-spec.md`
- `~/.codex/state_5.sqlite` as the runtime-verification artifact explicitly required by repo orchestration policy
