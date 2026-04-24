# 00 Multi-Layer Harness Governance Audit - Launch Bundle Spec

## Purpose

Persist the broader audit bundle needed to answer the larger question left open by the narrower 2026-04-15 orchestration/framework audit:

- can the full stack of harness layers around this repo actually sustain long-horizon, future-aware, high-rigor project development
- with enough protection against drift, shortcuts, hallucinations, dirty transitions, weak Git discipline, and poor deployment/release hygiene
- without requiring constant human expert supervision

This audit treats `repo operations / production governance` as one lane inside a larger multi-layer control problem, not as a replacement for it.

## Trigger

The user explicitly pushed beyond the narrower orchestration audit and asked for a broader audit of:

- Codex orchestration and harness behavior
- the repo-local GSD layer in `.codex`
- Git discipline and task-boundary hygiene
- GitHub Actions / CI / release / deployment controls
- the relationship of those layers to `LONG-ARC.md`, long-term vision, future-aware design, and day-to-day execution quality

The user also made two governance requirements explicit:

- the audit should be delegated in lanes rather than flattened into shallow main-thread exploration
- auditability matters, so the launch shape and lane scopes should be persisted as repo artifacts

## Motivating Grounds Map

This bundle is justified by a mix of:

- explicit user asks in the current session
- recent failure signals
- the narrower 2026-04-15 orchestration/framework audit
- the repo's long-horizon canon and governance docs

The lane motivations are:

1. `Codex orchestration layer`
   - grounded in the user's complaint about shallow main-thread exploration, poor orchestration, and failure to delegate
   - supported by:
     - `.planning/knowledge/signals/prix-guesser/2026-04-15-underdelegated-exploration-orchestrator-role-drift.md`
     - `.planning/research/2026-04-15-orchestration-framework-audit/01-orchestration-and-task-transition-failure-audit.md`
2. `GSD lifecycle and LONG-ARC layer`
   - grounded in the user's earlier request to audit how the framework carries long-term vision and future-aware design into day-to-day work
   - supported by:
     - `.planning/LONG-ARC.md`
     - `.planning/research/2026-04-15-orchestration-framework-audit/02-long-arc-lifecycle-integration-audit.md`
3. `Git / repo-operations layer`
   - grounded in the dirty-worktree and task-transition failure, plus the user's explicit concern about proper Git/version-control discipline for a large project
   - supported by:
     - `.planning/knowledge/signals/prix-guesser/2026-04-15-dirty-task-transitions-mixed-worktree.md`
     - `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-git-cleanup-checkpoint-plan.md`
     - `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-git-cleanup-execution-report.md`
4. `CI / release / deployment layer`
   - grounded in the user's explicit question about proper devops, deployment, guardrails, and progressive enforcement for a project that will grow substantially
   - supported by:
     - `.planning/research/2026-04-15-orchestration-framework-audit/04-converged-synthesis.md`
     - current governance docs and any present repo automation surface
5. `Cross-layer integration`
   - grounded in the user's clarification that this is not only a GSD harness question, but a different-levels-and-levers question across Codex, GSD, Git, and GitHub Actions
   - supported by the need to decide what belongs at each layer rather than overloading one

## Question

Across the repo's harness and governance stack, what mechanisms already exist, what is missing, and what should be changed so the repo can better support:

- long-horizon doctrine carry-forward
- future-aware and non-foreclosing design
- strong Git and task-transition discipline
- lower hallucination / shortcut / fake-closure risk
- progressive controls as risk, scale, parallelism, and operational complexity rise
- high-quality autonomous or semi-autonomous work with less constant expert supervision

## Scope

This bundle should treat at least these layers as distinct but interacting:

1. `Codex orchestration layer`
2. `repo-local GSD / overlay / skill layer`
3. `Git / worktree / review / repo-operations layer`
4. `CI / GitHub Actions / release / deployment governance layer`
5. `cross-layer integration and escalation logic`

## Non-Goals

- redesigning Prix Guesser product doctrine
- replacing Codex or GSD entirely
- finalizing production infrastructure for all future milestones in one pass
- recommending blanket blocking hooks for every nuanced decision
- widening current product implementation scope

## Authority Stack

### Prior audit and process sources

- `.planning/research/2026-04-15-orchestration-framework-audit/00-launch-bundle-spec.md`
- `.planning/research/2026-04-15-orchestration-framework-audit/01-orchestration-and-task-transition-failure-audit.md`
- `.planning/research/2026-04-15-orchestration-framework-audit/02-long-arc-lifecycle-integration-audit.md`
- `.planning/research/2026-04-15-orchestration-framework-audit/03-guardrails-mechanisms-and-command-proposals.md`
- `.planning/research/2026-04-15-orchestration-framework-audit/04-converged-synthesis.md`
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-worktree-stabilization-note.md`
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-git-cleanup-checkpoint-plan.md`
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-git-cleanup-execution-report.md`

### Repo governance and instruction sources

- `AGENTS.md`
- `.planning/AGENTS.md`
- `WORKFLOW.md`
- `AI-GUARDRAILS.md`
- `ARTIFACT-GOVERNANCE.md`
- `.planning/LONG-ARC.md`
- `.planning/PROJECT.md`
- `.planning/ROADMAP.md`
- `.planning/STATE.md`

### Runtime and harness sources

- `.codex/get-shit-done/`
- `tooling/portable-gsd/overlay/`
- `.codex/hooks.json`
- `.planning/config.json`
- relevant repo scripts and GitHub config as needed

### Signal sources

- `.planning/knowledge/index.md`
- `.planning/knowledge/signals/prix-guesser/2026-04-15-dirty-task-transitions-mixed-worktree.md`
- `.planning/knowledge/signals/prix-guesser/2026-04-15-underdelegated-exploration-orchestrator-role-drift.md`
- earlier process signals that remain relevant

## Bundle Shape

The audit should be split into five lane artifacts plus one converged synthesis:

1. Codex orchestration and task-boundary control
2. Repo-local GSD lifecycle, long-arc, and skill/command support
3. Git / worktree / branch / review / repo-operations discipline
4. CI / GitHub Actions / release / deployment governance
5. Cross-layer control-surface integration and escalation
6. Converged synthesis and recommended roadmap

## Recommended Execution Order

This bundle should not be launched as six parallel lanes.

Preferred order:

1. launch lanes `01` through `04` first
2. review whether any of those lanes expose a major framing defect
3. launch lane `05` after the first four outputs exist, because it is an integration lane rather than a first-pass terrain lane
4. launch lane `06` only after lanes `01` through `05` are complete

Reason:

- lanes `01` through `04` are substantive terrain lanes
- lane `05` is responsible for assigning responsibilities across layers and should read the earlier lane outputs, not only speculate from their specs
- lane `06` is the final answer layer

## Shared Constraints

- classify this bundle as `initial architecture research/planning`
- keep the work repo-grounded rather than generic best-practice dumping
- distinguish:
  - what exists now
  - what is missing
  - what should change soon
  - what should wait for later scale/risk
- require every lane output to include a `Motivating grounds` section that cites the specific artifacts or session concerns that justify that lane
- require every lane output to include a `Source-basis and epistemic limits` section for its load-bearing conclusions
- do not let internal repo support read like external validation; if a recommendation is mainly internal/cited or internal/reasoned, say so
- make `LONG-ARC.md` treatment explicit throughout
- do not silently flatten different control levers into one governance blob
- do not recommend heavier automation where visible workflow gates would be better

## Expected Outputs

- `01-codex-orchestration-layer-audit.md`
- `02-gsd-lifecycle-and-long-arc-layer-audit.md`
- `03-git-repo-operations-layer-audit.md`
- `04-ci-release-and-deployment-layer-audit.md`
- `05-cross-layer-integration-and-escalation-audit.md`
- `06-converged-synthesis.md`

## Key Distinction To Preserve

This bundle should preserve the distinction between:

- `what the repo needs now to improve rigor and future-awareness`
- `what should become stronger only as risk, blast radius, contributor count, environment count, or deployment stakes increase`

The audit should not assume that "bigger project" automatically means "more blocking automation." It should reason in terms of risk, parallelism, reversibility, and operational cost.
