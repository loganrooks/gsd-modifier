# 05 Cross-Layer Integration And Escalation Audit

## Research Frame
- Mode: `synthesis`
- Question:
  given the repo's actual state and the first four lane outputs, what responsibilities belong primarily at the Codex, repo-local GSD, Git/repo-operations, and CI/release/deployment layers; which controls need layered support; and how should those controls escalate as risk, parallelism, and operational burden rise?
- Scope:
  - the first four lane outputs in this audit bundle
  - the narrower orchestration/framework synthesis
  - repo governance and canon docs that define current posture
  - current repo maturity, not a hypothetical production service
- Non-goals:
  - writing the final converged synthesis for the whole bundle
  - proposing "full automation now"
  - relitigating Prix Guesser product doctrine
  - replacing repo-local GSD or collapsing all control into one harness layer
- Stop condition:
  - assign primary responsibilities by layer
  - name shared-control cases explicitly
  - define a staged escalation model
  - recommend a near-term integrated roadmap without drifting into lane `06`

## Artifacts Read
- `AGENTS.md`
- `.planning/AGENTS.md`
- `WORKFLOW.md`
- `AI-GUARDRAILS.md`
- `ARTIFACT-GOVERNANCE.md`
- `.planning/LONG-ARC.md`
- `.planning/PROJECT.md`
- `.planning/ROADMAP.md`
- `.planning/REQUIREMENTS.md`
- `.planning/STATE.md`
- `.planning/research/2026-04-15-orchestration-framework-audit/04-converged-synthesis.md`
- `.planning/research/2026-04-15-multilayer-harness-governance-audit/00-launch-bundle-spec.md`
- `.planning/research/2026-04-15-multilayer-harness-governance-audit/01-codex-orchestration-layer-audit.md`
- `.planning/research/2026-04-15-multilayer-harness-governance-audit/02-gsd-lifecycle-and-long-arc-layer-audit.md`
- `.planning/research/2026-04-15-multilayer-harness-governance-audit/03-git-repo-operations-layer-audit.md`
- `.planning/research/2026-04-15-multilayer-harness-governance-audit/04-ci-release-and-deployment-layer-audit.md`
- current repo/runtime observations from:
  - `.planning/config.json`
  - `.codex/config.toml`
  - `.codex/hooks.json`
  - `git status --short --branch`
  - `~/.codex/state_5.sqlite`

## Motivating grounds
This lane exists because the user explicitly rejected a single-layer answer. The broader question is not only "what should GSD do?" but "what should happen at Codex level, what should happen at GSD/workflow level, what should happen at Git/repo-operations level, and what should happen at CI/release/deployment level."

The strongest local grounds are:

- `.planning/research/2026-04-15-orchestration-framework-audit/04-converged-synthesis.md`
  - This already closed the narrower audit by saying the next pass must separate workflow/Git/CI concerns instead of absorbing them into one orchestration answer.
- `.planning/research/2026-04-15-multilayer-harness-governance-audit/01-codex-orchestration-layer-audit.md`
  - This showed the Codex problem is task closure and transition control, not lack of subagent capability.
- `.planning/research/2026-04-15-multilayer-harness-governance-audit/02-gsd-lifecycle-and-long-arc-layer-audit.md`
  - This showed the GSD problem is lifecycle carry-forward of `LONG-ARC.md`, not phase-local planning intelligence.
- `.planning/research/2026-04-15-multilayer-harness-governance-audit/03-git-repo-operations-layer-audit.md`
  - This showed the Git problem is mixed concern buckets and oversized integration boundaries, not just a cosmetically dirty tree.
- `.planning/research/2026-04-15-multilayer-harness-governance-audit/04-ci-release-and-deployment-layer-audit.md`
  - This showed the CI/deploy problem is staged mechanical verification and later release safety, not "implement production DevOps immediately."
- `AGENTS.md`, `.planning/AGENTS.md`, `WORKFLOW.md`, and `AI-GUARDRAILS.md`
  - These docs already distinguish doctrine, workflow, Git, and human signoff boundaries, so the integration task here is assigning real ownership, not inventing layers from scratch.

## Path Of Inquiry
- Entry point:
  - the lane 05 task spec plus the user's clarification that the broader audit should stay anti-collapse across multiple harness levels
- Branches considered:
  - whether one layer should become the default owner for most controls
  - whether the right answer is mostly staged automation
  - whether the key distinction is "now versus later" only
  - whether `LONG-ARC.md` propagation is mainly a GSD concern or a full-stack responsibility chain
- Branches pursued:
  - primary ownership by layer
  - shared-control cases where no single layer is sufficient
  - escalation thresholds tied to repo maturity and blast radius
  - long-arc doctrine movement through all four layers
- Branches deferred or abandoned:
  - exact implementation placement of every helper command
  - final branch/phase packaging of the recommended changes
  - final release/deploy topology choice
- Unexpected branches / reframings:
  - the repo is not under-instrumented everywhere; it is misallocated in a few specific places
  - the highest-value immediate controls belong in upper layers because current failures are contextual and pre-merge
  - lower-layer automation becomes valuable only after upper-layer ambiguity is reduced and the runtime surface becomes real

## Assumptions Surfaced
- `[a:c+r:i]` The repo remains solo-developer, agent-heavy, and planning-sensitive in the near term ([WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:12), [AI-GUARDRAILS.md](/home/rookslog/workspace/projects/prix-guesser/AI-GUARDRAILS.md:102), [.planning/STATE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/STATE.md:63)).
  - Why it matters:
    the right controls now are visible and reviewable gates, not multi-team bureaucracy.
  - What could weaken it:
    a shift to multiple frequent human contributors or a public contribution model.
- `[a:c+r:i]` Stronger controls should escalate by blast radius and coordination complexity, not by repo age alone ([03-git-repo-operations-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/03-git-repo-operations-layer-audit.md:284), [04-ci-release-and-deployment-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/04-ci-release-and-deployment-layer-audit.md:288)).
  - Why it matters:
    it stops lane `04` from pulling deploy/release machinery forward before the repo has an executable product.
  - What could weaken it:
    evidence that a supposedly low-risk stage is already causing materially expensive failures.
- `[d:c:i]` `LONG-ARC.md` is doctrine, not a second roadmap ([.planning/LONG-ARC.md](/home/rookslog/workspace/projects/prix-guesser/.planning/LONG-ARC.md:20), [.planning/LONG-ARC.md](/home/rookslog/workspace/projects/prix-guesser/.planning/LONG-ARC.md:22), [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md:183), [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md:189)).
  - Why it matters:
    cross-layer integration has to preserve doctrine translation without turning long-arc material into ambient scope widening.
- `[a:c+r:i]` Most current failure modes are cheapest to catch before merge and before automation, not after ([01-codex-orchestration-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/01-codex-orchestration-layer-audit.md:140), [03-git-repo-operations-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/03-git-repo-operations-layer-audit.md:132), [04-ci-release-and-deployment-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/04-ci-release-and-deployment-layer-audit.md:118)).
  - Why it matters:
    Codex/GSD/Git need to carry more of the immediate control burden than CI does today.
  - What could weaken it:
    if repeated failures start appearing mainly at merge or deploy boundaries instead of during active work.

## Evidence Base
### Direct evidence
- `[e:c:i]` The Codex lane found the primary defect to be missing task disposition and closure discipline, not missing worker capability ([01-codex-orchestration-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/01-codex-orchestration-layer-audit.md:143), [01-codex-orchestration-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/01-codex-orchestration-layer-audit.md:148)).
- `[e:c:i]` The GSD lane found `LONG-ARC.md` to be phase-strong but lifecycle-weak ([02-gsd-lifecycle-and-long-arc-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/02-gsd-lifecycle-and-long-arc-layer-audit.md:133), [02-gsd-lifecycle-and-long-arc-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/02-gsd-lifecycle-and-long-arc-layer-audit.md:135)).
- `[e:c:i]` The Git lane found the core repo-ops failure to be mixed concern buckets and oversized integration boundaries ([03-git-repo-operations-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/03-git-repo-operations-layer-audit.md:132), [03-git-repo-operations-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/03-git-repo-operations-layer-audit.md:146)).
- `[e:c:i]` The CI/deploy lane found the repo has no real CI surface or deployable runtime yet, so near-term automation should stay narrow and structural ([04-ci-release-and-deployment-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/04-ci-release-and-deployment-layer-audit.md:104), [04-ci-release-and-deployment-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/04-ci-release-and-deployment-layer-audit.md:118)).
- `[e:c:i]` `AGENTS.md`, `.planning/AGENTS.md`, and `AI-GUARDRAILS.md` already treat `LONG-ARC.md` as live doctrine and explicitly distinguish orchestration, planning canon, and human-signoff domains ([AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:41), [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:111), [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md:183), [AI-GUARDRAILS.md](/home/rookslog/workspace/projects/prix-guesser/AI-GUARDRAILS.md:15)).
- `[e:c:i]` `WORKFLOW.md` already distinguishes local workflow discipline from remote branch protection and later CI checks ([WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:30), [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:77), [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:90)).
- `[e:c:i]` `AI-GUARDRAILS.md` explicitly withholds legal, branding, monetization, infra, hosting, and other obligation-changing decisions from autonomous closure ([AI-GUARDRAILS.md](/home/rookslog/workspace/projects/prix-guesser/AI-GUARDRAILS.md:15), [AI-GUARDRAILS.md](/home/rookslog/workspace/projects/prix-guesser/AI-GUARDRAILS.md:24), [AI-GUARDRAILS.md](/home/rookslog/workspace/projects/prix-guesser/AI-GUARDRAILS.md:27)).
- `[e:c:i]` `.planning/config.json` still shows `workflow.auto_advance: true`, `mode: "yolo"`, and `git.branching_strategy: "none"`, which means the active stack still contains settings that can bypass the repo's stated rigor posture ([.planning/config.json](/home/rookslog/workspace/projects/prix-guesser/.planning/config.json:9), [03-git-repo-operations-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/03-git-repo-operations-layer-audit.md:133), [01-codex-orchestration-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/01-codex-orchestration-layer-audit.md:149)).
- `[e:c:i]` `.planning/STATE.md` and `AGENTS.md` still place the repo at a Phase 01 pre-rerun boundary, so the current maturity is planning-heavy and doctrine-sensitive rather than deploy-heavy ([.planning/STATE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/STATE.md:63), [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:43)).

### Inference and interpretation
- `[e:c+r:i]` The correct integration pattern is ([01-codex-orchestration-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/01-codex-orchestration-layer-audit.md:140), [02-gsd-lifecycle-and-long-arc-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/02-gsd-lifecycle-and-long-arc-layer-audit.md:133), [03-git-repo-operations-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/03-git-repo-operations-layer-audit.md:132), [04-ci-release-and-deployment-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/04-ci-release-and-deployment-layer-audit.md:118)):
  - upper layers own nuanced judgment and workflow visibility
  - lower layers own durable boundary materialization and mechanical checks
- `[e:c+r:i]` The repo should resist making GSD or CI the "universal harness" ([01-codex-orchestration-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/01-codex-orchestration-layer-audit.md:143), [02-gsd-lifecycle-and-long-arc-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/02-gsd-lifecycle-and-long-arc-layer-audit.md:135), [04-ci-release-and-deployment-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/04-ci-release-and-deployment-layer-audit.md:122)).
  - GSD is best at doctrine translation and lifecycle structure.
  - CI is best at mechanical verification once a merge or release boundary exists.
  - neither should absorb Codex orchestration judgment or Git change-set reality.
- `[e:c+r:i]` Task transition, doctrine carry-forward, and release safety each require different layer combinations rather than one owner ([01-codex-orchestration-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/01-codex-orchestration-layer-audit.md:142), [02-gsd-lifecycle-and-long-arc-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/02-gsd-lifecycle-and-long-arc-layer-audit.md:136), [03-git-repo-operations-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/03-git-repo-operations-layer-audit.md:145), [04-ci-release-and-deployment-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/04-ci-release-and-deployment-layer-audit.md:121)).
- `[e:c+r:i]` The near-term gap is not missing automation everywhere; it is missing explicit ownership transfer between layers ([01-codex-orchestration-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/01-codex-orchestration-layer-audit.md:148), [02-gsd-lifecycle-and-long-arc-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/02-gsd-lifecycle-and-long-arc-layer-audit.md:135), [03-git-repo-operations-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/03-git-repo-operations-layer-audit.md:137)).

### Unknowns
- `[o:c:i]` The exact command/skill packaging for task-disposition and doctrine-delta review remains undecided ([01-codex-orchestration-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/01-codex-orchestration-layer-audit.md:156), [02-gsd-lifecycle-and-long-arc-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/02-gsd-lifecycle-and-long-arc-layer-audit.md:143)).
- `[o:c:i]` The exact timing for changing `.planning/config.json` defaults versus patching workflows first remains open ([01-codex-orchestration-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/01-codex-orchestration-layer-audit.md:160), [02-gsd-lifecycle-and-long-arc-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/02-gsd-lifecycle-and-long-arc-layer-audit.md:143), [03-git-repo-operations-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/03-git-repo-operations-layer-audit.md:150)).
- `[o:c:i]` The exact first deploy unit and rollback unit remain unknown because the repo has no runnable app surface yet ([04-ci-release-and-deployment-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/04-ci-release-and-deployment-layer-audit.md:125), [04-ci-release-and-deployment-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/04-ci-release-and-deployment-layer-audit.md:128)).
- `[o:c:i]` The remote-host branch protection state is not verified from this lane ([WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:77), [03-git-repo-operations-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/03-git-repo-operations-layer-audit.md:149)).

## Dependencies And Relations
| Item | Depends on | Constrains or affects | Vulnerability |
| --- | --- | --- | --- |
| Active-task and returned-work disposition | Codex orchestration discipline, visible task ownership | task transitions, mixed-tree avoidance, worker closure trust | high |
| `LONG-ARC.md` lifecycle carry-forward | GSD lifecycle workflows, doctrine metadata, canon refs | future-seam preservation, milestone continuity, scope control | high |
| Branch/worktree boundary discipline | Git norms, branch objective clarity, parking rules | reviewability, rollback clarity, parallel stream safety | high |
| Repo-integrity CI | canonical local verify entrypoint, required artifact contracts | merge-boundary trust, false-verification resistance | medium |
| Release/deploy controls | executable runtime, operator flow, deploy bundle, rollback note | real-player safety, environment promotion, later service burden | high |
| Canon/doctrine reviewability | scoped doc diffs, human signoff, artifact statusing | long-arc reversibility, roadmap clarity, anti-drift quality | high |

## Integrated Decision Structure

### 1. Primary integration principle
`[e:c+r:i]` The stack should be treated as a progressive control chain, not as four competing automation venues ([01-codex-orchestration-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/01-codex-orchestration-layer-audit.md:143), [02-gsd-lifecycle-and-long-arc-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/02-gsd-lifecycle-and-long-arc-layer-audit.md:135), [03-git-repo-operations-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/03-git-repo-operations-layer-audit.md:137), [04-ci-release-and-deployment-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/04-ci-release-and-deployment-layer-audit.md:122)).

- Codex should catch contextual drift while work is still fluid.
- GSD should translate doctrine and lifecycle obligations into explicit workflow artifacts.
- Git should materialize coherent review and rollback boundaries.
- CI/release/deployment should verify only what has become mechanically checkable and operationally worth enforcing.

That means escalation should usually move downward through the stack:

1. visible warning or workflow gate
2. required artifact or declared status
3. branch/worktree or review-boundary separation
4. CI enforcement at merge
5. release/deploy gate once runtime risk exists

The repo should not jump straight to layer `4` or `5` when a layer `1` or `2` control would catch the same failure earlier and more honestly.

## What should live where

### Control-surface map by layer

| Layer | Primary ownership now | Best-fit mechanisms now | What should not live here |
| --- | --- | --- | --- |
| `Codex orchestration` | active task ownership, worker-first exploration, launch/closure discipline, runtime verification honesty | prompt/policy, visible task-disposition gates, launch bundle specs, narrow hooks, runtime reporting | branch protection, CI policy, deploy approval, doctrine ratification |
| `Repo-local GSD` | `LONG-ARC.md` carry-forward, lifecycle doctrine review, steering-brief quality, future-awareness translation | workflow patches, template/init changes, progress/transition checks, doctrine-delta review support | deciding doctrine content, absorbing Git review policy, hiding human signoff |
| `Git / repo-operations` | coherent change sets, branch/worktree isolation, parking and review boundaries, archive/corpus branch posture | branch rules, worktree rules, branch-level diff review, explicit park/accept/reject materialization | deciding task intent alone, deciding doctrine correctness, pretending clean tree equals resolved work |
| `CI / release / deployment` | mechanical integrity checks, merge-boundary verification, later build/test/release/deploy safety | local verify entrypoint in CI, status checks, build/test gates later, deploy smoke later, release approvals later | fixing mixed local work, `accept/revise/park` semantics, product/doctrine judgment |

### Layer-by-layer responsibility detail

#### `Codex orchestration` should primarily own
- subagent-first handling for exploratory, ambiguity-heavy, or scope-shaping work
- one declared active substantive task unless a persisted bundle explicitly defines parallel lanes
- returned worker disposition:
  - `accept`
  - `revise`
  - `park`
  - `reject`
- launch-time and closeout-time runtime truth:
  - requested runtime
  - effective runtime
  - owned output path
  - artifact-present versus thread-open ambiguity
- early warnings when the main thread is about to cross into a new concern bucket

#### `Repo-local GSD` should primarily own
- doctrine translation from `.planning/LONG-ARC.md` into:
  - lifecycle review prompts
  - `canonical_refs`
  - `future_awareness`
  - milestone and transition doctrine-delta checks
- steering-brief quality for discuss/research/plan/progress/transition flows
- lifecycle visibility for whether a phase is merely "present" versus actually canon-grounded and future-aware
- alignment between config defaults and doctrine-sensitive repos

#### `Git / repo-operations` should primarily own
- whether a change set is one coherent review/rollback unit
- when same-checkout work is still acceptable versus when a separate branch or worktree is required
- how parked, accepted, rejected, or deferred work is materialized
- branch-level reviewability relative to base
- explicit handling of audit trail, canon diffs, and archive/corpus movements

#### `CI / release / deployment` should primarily own
- narrow repo-integrity enforcement once remote PR flow is active
- later build/test enforcement once runnable code exists
- later deploy-bundle and operator-flow smoke checks once a private-host surface exists
- release/deploy approvals and promotion controls only when environment and obligation boundaries justify them

### Shared-control cases that should not be collapsed

#### `Task transition hygiene`
- Primary owner: `Codex orchestration`
- Supporting layers:
  - `Git` materializes the result as branch/worktree/parked state
  - `GSD` can later surface the state in progress/transition helpers
- Why it is shared:
  - Codex knows the intent boundary first.
  - Git is where unresolved mixed work becomes a real repo problem.

#### `LONG-ARC.md` carry-forward
- Primary owner: `Repo-local GSD`
- Supporting layers:
  - `Codex` ensures relevant tasks actually read the doctrine when it materially constrains the work
  - `Git` keeps doctrine changes separately reviewable and reversible
  - `CI` later checks only presence/reference contracts, not doctrine correctness
- Why it is shared:
  - doctrine must move through the lifecycle, not only live in a file
  - but the doctrine file itself must stay reviewable canon, not hidden workflow memory

#### `Merge readiness`
- Primary owner: `Git / repo-operations`
- Supporting layers:
  - `Codex` should not advance new work while disposition is unresolved
  - `GSD` should provide verification artifacts and workflow status
  - `CI` should verify mechanical claims at merge time
- Why it is shared:
  - no single layer can honestly answer "is this ready" by itself

#### `Release and deployment readiness`
- Primary owner: `CI / release / deployment`
- Supporting layers:
  - `GSD` should define required runbooks, verification artifacts, and roadmap-owned deploy deliverables
  - `Git` should isolate deploy/runtime changes cleanly
  - `Codex` should handle only bounded preparation work, not autonomous obligation decisions
- Why it is shared:
  - release safety is partly mechanical, partly artifact-based, and partly human-signoff-bound

## Responsibility matrix

| Problem or control | Primary layer | Supporting layers | Escalate to next layer when | Why |
| --- | --- | --- | --- | --- |
| Exploratory work staying in the main thread | `Codex` | `GSD` for lane spec templates | exploration affects more than one concern bucket or needs durable outputs | this is an orchestration-shape problem first |
| Returned worker output not clearly closed | `Codex` | `Git` | returned work is modifying files or needs to persist beyond the current turn | closure meaning must exist before Git can safely carry it |
| `LONG-ARC.md` not reaching milestone/progress/transition flows | `GSD` | `Codex`, `Git` | doctrine drift begins crossing canon boundaries or milestone turnover | lifecycle structure belongs in workflow, not in Git or CI |
| Mixed concern buckets in one tree | `Git` | `Codex` | more than one active write stream or branch diff stops being one coherent objective | local repo state is now the controlling risk surface |
| Need to preserve parked work without ambient dirty files | `Git` | `Codex`, `GSD` | parked work survives beyond a short local pause | parking must become a durable repo boundary |
| Broken local references / false "verified" claims | `CI` once PR flow exists | `GSD`, `Git` | the checks are mechanically defined and worth enforcing on every merge | this is a merge-boundary integrity question |
| Build/test regression risk | `CI` | `Git`, `GSD` | runnable app and stable local verify commands exist | before that, automation would mostly be theater |
| Deploy-bundle correctness | `CI / release` | `GSD`, `Git` | a private-host deploy bundle actually exists and real players depend on it | release/deploy gates are only honest once a deploy surface is real |
| Legal/branding/obligation shifts | human signoff outside all four layers | `Codex`, `GSD`, `Git`, `CI` may prepare artifacts | never delegated as autonomous closure | repo guardrails explicitly reserve these decisions |

## How `LONG-ARC.md` should move through all four layers

### 1. Canon doctrine should live in the canon
`LONG-ARC.md` should remain the durable doctrine file. It should not be rewritten as:
- Codex memory
- GSD ambient lore
- Git branch naming
- CI policy

### 2. GSD should translate doctrine into workflow-visible constraints
The GSD layer should make doctrine present at:
- `new-project`
- `new-milestone`
- `progress`
- `transition`
- `complete-milestone`
- `discuss-phase`
- `quick` when doctrine materially constrains the task

That translation should stay about:
- current posture
- protected seams
- explicit non-decisions
- reversal-sensitive boundaries

It should not widen current milestone scope.

### 3. Codex should keep doctrine from being bypassed conversationally
The Codex layer should ensure:
- relevant doctrine is named in launch specs and required reading
- exploratory work is delegated deeply enough that open branches remain explicit
- returned research outputs are dispositioned before they start acting like accepted doctrine

### 4. Git should preserve doctrine changes as reviewable and reversible
Doctrine and canon changes should remain easy to:
- inspect
- compare against the prior state
- separate from implementation when they deserve different review timing
- reverse without archaeology

### 5. CI should verify only the mechanical part of doctrine handling
Later CI can check:
- required doctrine files exist
- referenced files resolve
- required review artifacts or delta notes exist

CI should not decide whether the doctrine itself is good.

## Escalation guidance by risk, scale, and complexity

### Stage 0: Current repo posture
`planning-heavy`, `solo-developer`, `agent-heavy`, `Phase 01 pre-rerun`, `no runnable product`, `no CI surface`

Use:
- Codex warnings and visible disposition gates
- GSD lifecycle and doctrine carry-forward patches
- Git branch/worktree rules by convention
- narrow repo-integrity CI only when remote PR flow is active

Do not use:
- deploy automation
- production-style release gating
- opaque blocking hooks for nuanced judgment

### Stage 1: First sustained implementation and parallel work
Trigger:
- multiple active write streams
- sustained subagent execution
- growing branch diffs to `main`
- real code verification entrypoints exist

Escalate to:
- mandatory separate worktrees for parallel or parked write streams
- GSD progress/transition surfaces that report unresolved disposition and doctrine-grounding state
- branch protection plus required status checks when PR flow is active
- build/test CI once local verification is stable

### Stage 2: First private-host deployable runtime used by real players
Trigger:
- operator flow is real
- private-host sessions are used beyond pure local experimentation
- failure now affects a real game night

Escalate to:
- deploy-bundle smoke checks
- documented start/stop flow checks
- secret-boundary docs
- rollback note and explicit release checklist
- stronger separation between runtime/deploy changes and canon/planning changes

### Stage 3: Multiple environments, multiple operators, or frequent remote use
Trigger:
- staging and production become meaningfully different
- more than one person may operate the runtime
- remote use becomes routine rather than occasional

Escalate to:
- promotion rules
- backup/export validation
- migration gates
- stronger post-deploy verification
- tighter release approval posture

### Stage 4: Public or paid obligation profile
Trigger:
- public discovery
- stronger uptime/moderation expectations
- payment or guaranteed access
- materially larger blast radius for bad releases

Escalate to:
- service-grade release governance
- stronger secret handling and scanning
- incident/runbook discipline
- explicit operational ownership boundaries

At this stage the controlling constraint is not repo complexity. It is obligation profile.

## Recommended near-term integrated roadmap

1. `[e:c+r:i]` Strengthen the upper layers before adding more lower-layer automation ([01-codex-orchestration-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/01-codex-orchestration-layer-audit.md:148), [02-gsd-lifecycle-and-long-arc-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/02-gsd-lifecycle-and-long-arc-layer-audit.md:135), [04-ci-release-and-deployment-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/04-ci-release-and-deployment-layer-audit.md:118)).
   - Add Codex-level active-task, disposition, and launch/closure evidence expectations.
   - Treat `runtime-valid but output-missing` as blocked work rather than acceptable ambiguity.

2. `[e:c+r:i]` Patch the GSD lifecycle gap around `LONG-ARC.md` ([02-gsd-lifecycle-and-long-arc-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/02-gsd-lifecycle-and-long-arc-layer-audit.md:135), [02-gsd-lifecycle-and-long-arc-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/02-gsd-lifecycle-and-long-arc-layer-audit.md:180)).
   - Add doctrine-aware steps to `new-milestone`, `progress`, `transition`, and `complete-milestone`.
   - Expose `long_arc_exists` / `long_arc_path` style init metadata.
   - Stop relying on ambient memory or optional pauses for doctrine carry-forward.

3. `[e:c+r:i]` Formalize repo-ops boundary rules now ([03-git-repo-operations-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/03-git-repo-operations-layer-audit.md:132), [03-git-repo-operations-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/03-git-repo-operations-layer-audit.md:185)).
   - Make branch-level diff review a standing habit.
   - Define when same-checkout work is acceptable and when separate worktrees are required.
   - Treat parked work as an explicit repo object, not as ambient modified files.

4. `[e:c+r:i]` Align config posture with the repo's stated rigor bar ([AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:49), [.planning/config.json](/home/rookslog/workspace/projects/prix-guesser/.planning/config.json:9), [01-codex-orchestration-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/01-codex-orchestration-layer-audit.md:149), [03-git-repo-operations-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/03-git-repo-operations-layer-audit.md:133)).
   - Revisit `workflow.auto_advance: true`, `mode: "yolo"`, and `git.branching_strategy: "none"` in light of the audit results.
   - Do not let safer behavior depend entirely on commentary discipline.

5. `[e:c+r:i]` Add one narrow merge-boundary CI lane only after the local verify contract is clear ([04-ci-release-and-deployment-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/04-ci-release-and-deployment-layer-audit.md:118), [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:64), [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:96)).
   - repo-integrity checks
   - path/reference validation
   - required artifact existence checks
   - no auto-deploy and no doctrine judgment

6. `[p:c+r:i]` Defer real release/deploy controls until a runnable private-host surface exists ([04-ci-release-and-deployment-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/04-ci-release-and-deployment-layer-audit.md:119), [.planning/ROADMAP.md](/home/rookslog/workspace/projects/prix-guesser/.planning/ROADMAP.md:84), [.planning/REQUIREMENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/REQUIREMENTS.md:60)).
   - build/test CI after executable app exists
   - deploy-bundle smoke and release checklist after deploy surface exists
   - promotion controls only after multiple environments/operators exist

## Anti-patterns to avoid
- Treating GSD as the universal harness that should absorb orchestration, Git, and CI responsibilities.
- Treating CI as the place to solve mixed local change sets, doctrine drift, or worker-disposition ambiguity.
- Treating a clean working tree as proof that substantive task-transition discipline exists.
- Treating `LONG-ARC.md` as ambient memory instead of a doctrine file that needs workflow translation and reviewable canon changes.
- Treating all future stronger controls as "more automation" instead of matching the mechanism to the failure surface.
- Escalating to deploy/release automation before the repo has one canonical local verify path or one real deploy unit.
- Hiding human-signoff territory behind green checks, successful worker runs, or workflow auto-advance.
- Letting lower-layer enforcement choose winners among live long-arc branches such as wrapper order, host identity, or visibility ladder.

## What can close now
- `[e:c+r:i]` The broader answer should stay multi-layer. No single layer should become the catch-all harness ([01-codex-orchestration-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/01-codex-orchestration-layer-audit.md:143), [02-gsd-lifecycle-and-long-arc-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/02-gsd-lifecycle-and-long-arc-layer-audit.md:135), [04-ci-release-and-deployment-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/04-ci-release-and-deployment-layer-audit.md:122)).
- `[e:c+r:i]` The highest-value immediate controls belong mainly in `Codex + GSD + Git`, because the repo's current failures are contextual, lifecycle-sensitive, and pre-merge ([01-codex-orchestration-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/01-codex-orchestration-layer-audit.md:148), [02-gsd-lifecycle-and-long-arc-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/02-gsd-lifecycle-and-long-arc-layer-audit.md:135), [03-git-repo-operations-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/03-git-repo-operations-layer-audit.md:145)).
- `[e:c+r:i]` `CI / release / deployment` is a real lane, but its immediate role is narrow repo-integrity reinforcement, not deployment automation ([04-ci-release-and-deployment-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/04-ci-release-and-deployment-layer-audit.md:118), [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:92)).
- `[e:c+r:i]` `LONG-ARC.md` should move through the stack as doctrine translation plus reviewable canon diffs, not as ambient memory and not as CI policy ([.planning/LONG-ARC.md](/home/rookslog/workspace/projects/prix-guesser/.planning/LONG-ARC.md:20), [02-gsd-lifecycle-and-long-arc-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/02-gsd-lifecycle-and-long-arc-layer-audit.md:192), [03-git-repo-operations-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/03-git-repo-operations-layer-audit.md:195)).
- `[e:c+r:i]` Progressive enforcement is justified here only by rising blast radius, parallelism, operator burden, and obligation level ([04-ci-release-and-deployment-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/04-ci-release-and-deployment-layer-audit.md:120), [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:92), [AI-GUARDRAILS.md](/home/rookslog/workspace/projects/prix-guesser/AI-GUARDRAILS.md:15)).

## What must stay open
- The exact packaging of new helper commands or skills for disposition and doctrine-delta review
- The exact sequence for config hardening versus workflow patching
- The exact first local verify entrypoint and later CI command set
- The first real deploy bundle and rollback boundary
- The remote host's current branch-protection state

## Planning Handoff
### What can now be treated as decided
- Codex owns early contextual control.
- GSD owns doctrine/lifecycle translation.
- Git owns durable review and rollback boundaries.
- CI/release owns mechanical enforcement only after those boundaries become real and worth enforcing.
- Long-arc quality depends on handoffs between those layers being explicit.

### What remains assumed or open
- exact implementation placement of task-disposition and doctrine-delta helpers
- exact config/default changes and whether they should land together
- exact timing for the first repo-integrity CI rollout

### Derived constraints
- Do not use lower-layer automation to paper over upper-layer ambiguity.
- Do not let doctrine-sensitive work bypass GSD lifecycle structure through "quick" or conversational shortcuts.
- Do not let Git review boundaries become oversized just because commit history is tidy.
- Do not let CI imply operational or doctrinal closure beyond what it can mechanically check.

### Future-awareness seams to preserve
- `LONG-ARC.md` stays doctrine, not a shadow roadmap.
- branch/worktree policy should preserve separate reviewability for canon uplift, code, archive moves, and deploy/runtime changes.
- the later distinction between private-host capability, hosted convenience, and public obligation must remain explicit across workflow and release controls.

### Deferred follow-up lane
- `06-converged-synthesis.md`
  - consolidate this responsibility map with the four substantive lanes into the final recommended governance posture

## Sources
- `AGENTS.md`
- `.planning/AGENTS.md`
- `WORKFLOW.md`
- `AI-GUARDRAILS.md`
- `ARTIFACT-GOVERNANCE.md`
- `.planning/LONG-ARC.md`
- `.planning/PROJECT.md`
- `.planning/ROADMAP.md`
- `.planning/REQUIREMENTS.md`
- `.planning/STATE.md`
- `.planning/config.json`
- `.codex/config.toml`
- `.codex/hooks.json`
- `.planning/research/2026-04-15-orchestration-framework-audit/04-converged-synthesis.md`
- `.planning/research/2026-04-15-multilayer-harness-governance-audit/00-launch-bundle-spec.md`
- `.planning/research/2026-04-15-multilayer-harness-governance-audit/01-codex-orchestration-layer-audit.md`
- `.planning/research/2026-04-15-multilayer-harness-governance-audit/02-gsd-lifecycle-and-long-arc-layer-audit.md`
- `.planning/research/2026-04-15-multilayer-harness-governance-audit/03-git-repo-operations-layer-audit.md`
- `.planning/research/2026-04-15-multilayer-harness-governance-audit/04-ci-release-and-deployment-layer-audit.md`
- `~/.codex/state_5.sqlite`
- live repo observation on 2026-04-15 from `git status --short --branch`
