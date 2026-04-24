# 02 GSD Lifecycle And Long-Arc Layer Audit

## Research Frame
- Mode: `solution evaluation`
- Question:
  can the repo-local GSD layer, as it currently exists in `.codex/get-shit-done/`, `tooling/portable-gsd/overlay/`, and the live repo config/canon, carry `LONG-ARC.md` through the project lifecycle rather than only through phase-local discuss and planning?
- Scope:
  - root `AGENTS.md`
  - `.planning/AGENTS.md`
  - `.planning/LONG-ARC.md`
  - `.planning/PROJECT.md`
  - `.planning/ROADMAP.md`
  - `.planning/STATE.md`
  - `.planning/REQUIREMENTS.md`
  - `.planning/config.json`
  - `.codex/get-shit-done/workflows/discuss-phase.md`
  - `.codex/get-shit-done/workflows/plan-phase.md`
  - `.codex/get-shit-done/workflows/research-phase.md`
  - `.codex/get-shit-done/workflows/new-project.md`
  - `.codex/get-shit-done/workflows/new-milestone.md`
  - `.codex/get-shit-done/workflows/progress.md`
  - `.codex/get-shit-done/workflows/transition.md`
  - `.codex/get-shit-done/workflows/complete-milestone.md`
  - `.codex/get-shit-done/workflows/quick.md`
  - `.codex/get-shit-done/templates/context.md`
  - `.codex/get-shit-done/templates/project.md`
  - `.codex/get-shit-done/templates/roadmap.md`
  - `.codex/get-shit-done/bin/lib/init.cjs`
  - `tooling/portable-gsd/overlay/get-shit-done/...` overlay variants and config helpers
  - `tooling/portable-gsd/overlay/skills/gsd-discuss-phase/SKILL.md`
  - prior audit artifacts named by the task spec
- Non-goals:
  - redesigning GSD generically for every repo
  - deciding Prix Guesser product doctrine beyond what the canon already says
  - patching the framework in this lane
  - auditing execution quality or Git/CI/release layers except where they directly affect long-arc carry-forward
- Stop condition:
  - identify where `LONG-ARC.md` is already first-class
  - identify where it is still phase-strong but lifecycle-weak
  - name concrete patch points in workflows, templates, skills, commands, and config
  - distinguish what belongs in GSD from what should stay repo policy

## Motivating grounds
This lane exists because the repo now explicitly expects `LONG-ARC.md` to be durable steering doctrine, not ambient memory:

- root `AGENTS.md` treats `.planning/LONG-ARC.md` as part of live operational state and tells agents to think across the current phase, next milestone, and farther doctrine surfaces
- `.planning/AGENTS.md` says `LONG-ARC.md` carries farther doctrine that current planning must preserve without widening current scope
- `.planning/PROJECT.md` and `.planning/ROADMAP.md` already cite `LONG-ARC.md` as the long-range doctrine current work should preserve
- `.planning/STATE.md` explicitly says replanning should consume `LONG-ARC.md` before fresh planning artifacts are treated as authoritative

The narrower orchestration audit already established the core suspicion this lane is testing:

- `.planning/research/2026-04-15-orchestration-framework-audit/02-long-arc-lifecycle-integration-audit.md` found `LONG-ARC.md` to be phase-strong but lifecycle-weak
- `.planning/research/2026-04-15-orchestration-framework-audit/03-guardrails-mechanisms-and-command-proposals.md` argued that lifecycle workflows, not just phase workflows, need doctrine-sensitive carry-forward
- `.planning/research/2026-04-15-orchestration-framework-audit/04-converged-synthesis.md` concluded that the local stack is capable of long-horizon design but not yet robustly lifecycle-aware

So the live question here is not whether long-arc doctrine exists. It is whether repo-local GSD actually carries it across initialization, milestone turnover, progress routing, transition, completion, and speed-path command usage.

## Anti-Misread Note
`carry-forward awareness` is not the same thing as `scope widening`.

- `carry-forward awareness` means current workflows preserve present-tense doctrine, protected seams, explicit non-decisions, and obligation boundaries so later milestones stay possible without being silently chosen now.
- `scope widening` means importing later wrapper families, visibility states, identity layers, or support obligations into current requirements and phase goals just because they appear in `LONG-ARC.md`.

The right GSD behavior for this repo is:

- strengthen `carry-forward awareness`
- avoid automated `scope widening`

That means the lifecycle layer should translate doctrine into present constraints and review prompts, not turn `LONG-ARC.md` into a second roadmap or inject it indiscriminately into every task.

## Path Of Inquiry
- Entry point:
  - the lane spec and the repo's current expectation that `.planning/LONG-ARC.md` should shape day-to-day work without widening Milestone 01 scope
- Branches considered:
  - the repo-local overlay may already have closed the lifecycle gap
  - the framework may be phase-strong and lifecycle-weak
  - the repo may currently depend mostly on canon docs and human discipline rather than workflow support
  - the relevant gap may be config and speed-path usage rather than templates
- Branches pursued:
  - inspect the live canon to understand the repo's actual long-arc standard
  - inspect lifecycle workflows and init payloads for first-class long-arc support
  - inspect phase workflows, context templates, and quick-task paths for carry-forward mechanisms
  - inspect overlay coverage to see which parts the repo has already chosen to preserve across reinstalls
  - inspect current config and auto-mode defaults for doctrine-sensitive lifecycle risk
- Branches deferred:
  - full end-to-end execution tracing of every lifecycle command
  - generic upstream product design for GSD beyond repo-relevant patch points

## Assumptions Surfaced
- `[a:c+r:i]` If `LONG-ARC.md` is only phase-local input, milestone and project evolution can still drift even when phase planning is good ([AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:41), [.planning/STATE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/STATE.md:63), [.planning/LONG-ARC.md](/home/rookslog/workspace/projects/prix-guesser/.planning/LONG-ARC.md:20)).
  - Why it matters:
    this repo's doctrine is wider than any one phase.
  - What would weaken it:
    evidence that lifecycle workflows already read or translate equivalent doctrine elsewhere.
- `[a:c+r:i]` A repo with `workflow.auto_advance: true` cannot depend on humans remembering to insert doctrine review pauses at every lifecycle boundary ([.planning/config.json](/home/rookslog/workspace/projects/prix-guesser/.planning/config.json:15), [.codex/get-shit-done/workflows/new-project.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/new-project.md:214), [.codex/get-shit-done/workflows/transition.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/transition.md:103), [.codex/get-shit-done/workflows/complete-milestone.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/complete-milestone.md:98)).
  - Why it matters:
    doctrine-sensitive checks need to be structural if auto progression is allowed.
  - What would weaken it:
    explicit lifecycle gates that run even under auto paths.
- `[a:c+r:i]` Quick or speed-path command usage matters here because Prix Guesser uses GSD outside strict phase execution as well as inside it ([.codex/get-shit-done/workflows/quick.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/quick.md:1), [.codex/get-shit-done/workflows/quick.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/quick.md:193), [.codex/get-shit-done/workflows/quick.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/quick.md:309)).
  - Why it matters:
    doctrine can still be bypassed through "small task" lanes if those lanes ignore it by default.
  - What would weaken it:
    a clear repo policy that speed paths are never used for doctrine-sensitive work and a workflow that enforces that boundary.

## Evidence Base
### Direct evidence
- root `AGENTS.md` elevates `.planning/LONG-ARC.md` into live operational state and explicitly instructs agents to think across current, next-milestone, and farther-doctrine horizons
- `.planning/AGENTS.md` requires future-flexibility work to distinguish `direct doctrine`, `bounded-open branches`, `preserve-only seams`, `reversal-sensitive boundaries`, and `inquiry debt`
- `.planning/LONG-ARC.md` explicitly says downstream discuss, research, and planning should treat it as durable doctrine rather than re-litigating it phase by phase
- `.planning/PROJECT.md`, `.planning/ROADMAP.md`, and `.planning/STATE.md` already manually reference `LONG-ARC.md` as a current steering source
- `discuss-phase.md`, `discuss-phase-assumptions.md`, and `discuss-phase-power.md` explicitly:
  - read `.planning/LONG-ARC.md` when present
  - add it to `canonical_refs` when it materially constrains the phase
  - derive normalized `future_awareness` buckets including `Protected Seams` and `Explicit Non-Decisions`
- `templates/context.md` makes `<canonical_refs>` mandatory and keeps `<future_awareness>` first-class
- `research-phase.md` and `plan-phase.md` explicitly consume `context_canonical_refs`, `derived_constraints`, and `future_awareness`
- `tooling/portable-gsd/overlay/get-shit-done/templates/phase-prompt.md` adds `future_preservation` as a reviewable plan frontmatter field when future-awareness exists
- `quick.md` includes a conditional path where quick-task `CONTEXT.md` can cite `.planning/LONG-ARC.md` when `--discuss` is used and doctrine materially constrains the task
- repo-local `gsd-rigorous-research` is the preferred non-phase research lane in repo instructions and does strengthen evidence/inference discipline for doctrine-sensitive research, but it does not itself patch lifecycle carry-forward
- `new-project.md`, `new-milestone.md`, `progress.md`, `transition.md`, and `complete-milestone.md` do not mention `LONG-ARC.md`
- `templates/project.md` and `templates/roadmap.md` do not include first-class long-arc or carry-forward sections
- `bin/lib/init.cjs` init payloads for `new-project`, `new-milestone`, and `progress` expose no `long_arc_exists`, `long_arc_path`, or doctrine freshness fields
- overlay coverage under `tooling/portable-gsd/overlay/get-shit-done/` preserves the phase-layer files, not the lifecycle workflows or generic `project` / `roadmap` templates
- overlay `bin/lib/config.cjs` now defaults new projects to `workflow.auto_advance: false` and `workflow.discuss_mode: 'exploratory'`
- live `.planning/config.json` in this repo still has `mode: "yolo"` and `workflow.auto_advance: true`
- `new-project.md` auto mode still hardcodes `"workflow":{"...","auto_advance":true}` when creating config
- `transition.md` auto-approves transition in yolo mode once summaries match plans
- `complete-milestone.md` auto-approves milestone scope verification in yolo mode

### Inference and interpretation
- The repo-local GSD layer is already strong where it has a steering brief to work from.
  - `LONG-ARC.md` becomes real when it is translated into `CONTEXT.md`, `canonical_refs`, `future_awareness`, and then into `future_preservation`.
- The repo-local GSD layer is weak where lifecycle workflows are expected to create or refresh that steering brief.
  - initialization, milestone rollover, transition, and completion do not make doctrine review first-class
- The repo is compensating manually through canon patches and AGENTS rules.
  - that compensation is useful, but it is not the same thing as framework support
- The current live config means lifecycle rigor cannot rely on optional pauses alone.
  - if auto-advance remains enabled in a repo like this, doctrine checks have to be part of the workflow machinery or clearly excluded from auto paths

### Unknowns
- I did not run a full fresh lifecycle through every command, so this lane is based on workflow definitions, init payloads, and live canon rather than a full replay trace
- I did not audit every speed-path command, so the command-usage conclusions are strongest for `quick`, `progress`, and the main lifecycle workflows rather than the entire command catalog

## Current lifecycle integration map

| Lifecycle surface | Current long-arc mechanism | Status | Why it matters |
| --- | --- | --- | --- |
| Repo canon and instruction layer | `AGENTS.md`, `.planning/AGENTS.md`, `PROJECT.md`, `ROADMAP.md`, `STATE.md` all manually elevate `LONG-ARC.md` | `Strong repo-policy compensation` | The repo has already done the doctrinal work, so the framework is not starting from zero |
| `discuss-phase` family | Explicitly reads `.planning/LONG-ARC.md`, adds it to `canonical_refs`, derives normalized `future_awareness` | `First-class` | This is the strongest current carrier of doctrine into actual phase work |
| `templates/context.md` | Makes `canonical_refs` and `future_awareness` mandatory | `First-class` | This is the main bridge from doctrine into downstream planning and research |
| `research-phase` | Treats `context_canonical_refs`, `derived_constraints`, and `future_awareness` as research guardrails | `First-class downstream consumer` | Preserves doctrine during research rather than after-the-fact review |
| `plan-phase` + `phase-prompt` | Preserves `future_awareness`, flags violations, records `future_preservation` | `First-class downstream consumer` | Makes seam-preservation auditable in plans, not just conversational |
| `quick` with `--discuss` | Can cite `.planning/LONG-ARC.md` in quick-task context and preserve its refs downstream | `Conditional / opt-in` | Shows the stack can carry doctrine into non-phase work, but only when used deliberately |
| `new-project` | No long-arc scaffold, no template, no durable-doctrine prompt; auto mode hardcodes `auto_advance: true` | `Lifecycle-blind` | The first lifecycle moment does not create a doctrine artifact or carry-forward slot by default |
| `templates/project.md` / `roadmap.md` | No first-class long-arc or carry-forward section | `Lifecycle-blind` | Generic project scaffolds do not preserve doctrine unless the repo patches them manually later |
| `new-milestone` | Updates `PROJECT.md` and `STATE.md`, then researches/roadmaps, but never reviews `LONG-ARC.md` | `Lifecycle-blind` | The exact milestone carry-forward point has no doctrine step |
| `progress` | Knows whether `CONTEXT.md` exists, but not whether that context is long-arc-grounded or stale | `Indirect / weak` | It can overstate readiness by treating "has context" as sufficient |
| `transition` | Evolves `PROJECT.md` and `STATE.md` from summaries without reading `LONG-ARC.md` | `Lifecycle-blind` | Phase learnings can change canon without any doctrine triage |
| `complete-milestone` | Full `PROJECT.md` review and archive behavior, but no `LONG-ARC.md` review | `Lifecycle-blind` | Durable milestone learnings can be archived without touching doctrine |
| `init` payloads and config helpers | No first-class long-arc metadata in lifecycle init payloads | `Mechanism gap` | Workflows would have to rediscover doctrine ad hoc every time |

## Strongest existing leverage points
1. `CONTEXT.md` is a real doctrine carrier, not just a decision memo. The combination of `canonical_refs`, `future_awareness`, and downstream consumption already gives the repo a high-quality phase-level long-arc pipeline.
2. The overlay preserved the right layer first. The repo chose to harden `discuss`, `plan`, `research`, `context`, and `phase-prompt`, which are the highest-value places for seam preservation once a phase has been framed correctly.
3. The repo canon already compensates for lifecycle gaps. `PROJECT.md`, `ROADMAP.md`, and `STATE.md` explicitly keep `LONG-ARC.md` visible, so current planning quality is higher than the generic lifecycle machinery deserves.
4. `quick` is not entirely blind. The workflow already contains a doctrine-aware path for ad hoc tasks when discussion/context is used.
5. The repo-local `gsd-rigorous-research` skill is already a good epistemic lane for non-phase doctrine work.
   - that helps the repo avoid mushy research, but it is not a substitute for lifecycle-aware workflow steps
6. The overlay config defaults now lean in the right direction for future projects at the phase layer.
  - `workflow.discuss_mode: exploratory`
  - `workflow.auto_advance: false`

## Weakest lifecycle gaps
1. `LONG-ARC.md` is not a first-class artifact of project creation.
   - `new-project.md` and the generic templates do not scaffold durable doctrine, so doctrine enters only through repo-specific retrofits.
2. Milestone start has no explicit carry-forward translation step.
   - `new-milestone.md` can produce a new milestone without asking what long-arc doctrine still governs, what seams remain live, or whether doctrine changed.
3. Progress routing conflates `has context` with `is doctrine-grounded`.
   - `progress.md` can say a phase is ready to plan while remaining blind to whether `LONG-ARC.md` is cited when relevant or whether `future_awareness` exists at all.
4. Phase transition and milestone completion do not triage learnings into the doctrine layer.
   - `transition.md` and `complete-milestone.md` evolve `PROJECT.md` and archive milestone artifacts, but neither requires a `LONG-ARC.md` review.
5. Auto paths amplify the lifecycle blind spot.
   - the live project config still has `workflow.auto_advance: true`
   - `transition.md` and `complete-milestone.md` both have yolo auto-approval branches
   - `new-project.md` auto mode still hardcodes `auto_advance: true`
6. Lifecycle workflows lack cheap doctrine metadata.
   - because init payloads do not expose `long_arc_exists` or `long_arc_path`, long-arc awareness is not a reusable part of lifecycle tooling

## How LONG-ARC should flow through the lifecycle
`LONG-ARC.md` should move through the lifecycle as doctrine translation, not doctrine duplication.

### 1. Project creation
- Ask whether this project has durable doctrine that should outlive the first milestone.
- If yes, scaffold a doctrine artifact and seed `PROJECT.md` / `ROADMAP.md` with an explicit reference to it.
- Do not force doctrine scaffolding for every repo; make it a first-class optional artifact.

### 2. Milestone start
- Read the current doctrine file.
- Translate it into a short carry-forward record for the new milestone:
  - current posture that must still hold
  - preserve-only seams that current work must not close
  - explicit non-decisions that must stay open
  - reversal-sensitive boundaries that should not be crossed casually
- Do not import later wrapper families into the milestone just because the doctrine mentions them.

### 3. Phase discuss and planning
- This is the current strong path and should stay the main doctrine-to-work translator.
- `LONG-ARC.md` should enter the phase only when it materially constrains the phase.
- The phase should carry forward the doctrine as `future_awareness`, not as future feature scope.

### 4. Progress and next-step routing
- Show whether the current phase has a doctrine-grounded steering brief, not just whether a `CONTEXT.md` file exists.
- Surface a warning when planning is about to continue without relevant long-arc grounding.

### 5. Transition after phase completion
- Review completed-phase learnings and triage them:
  - `PROJECT.md` compact product identity update
  - `ROADMAP.md` sequencing or requirement update
  - `LONG-ARC.md` doctrine update
  - `preserve-only seam` note with no canon change
- This is the key boundary where carry-forward awareness should be refreshed without widening current scope.

### 6. Milestone completion
- Run a doctrine delta review:
  - what still governs unchanged
  - what was validated strongly enough to harden
  - what was invalidated
  - what must remain open
- Archive milestone learnings only after deciding whether they belong in doctrine, roadmap, or historical trail only.

## Concrete patch points in workflows, templates, skills, and config
### Workflow changes
- `new-project.md`
  - add a durable-doctrine decision step
  - stop hardcoding `workflow.auto_advance: true` in auto mode without an explicit choice
- `new-milestone.md`
  - add a `long-arc carry-forward review` before research/requirements/roadmap generation
- `progress.md`
  - add doctrine-grounding visibility:
    - relevant `LONG-ARC.md` exists
    - current phase context cites it when relevant
    - `future_awareness` is present
- `transition.md`
  - add a `doctrine triage` step after summary review
- `complete-milestone.md`
  - add a `long-arc delta` or `doctrine review` step before archive finalization
- `quick.md`
  - keep the existing doctrine-aware `--discuss` path
  - add clearer guidance that doctrine-sensitive quick tasks should not use the bare no-discuss path

### Template changes
- add a `templates/long-arc.md` or other first-class durable-doctrine template
- patch `templates/project.md` to include a compact `Long-Arc Reference` or `Carry-Forward Doctrine` pointer
- patch `templates/roadmap.md` to include a lightweight `carry-forward constraints` field or guidance note rather than treating long-arc doctrine as ambient lore

### CLI / init changes
- patch `bin/lib/init.cjs` outputs for lifecycle workflows to expose:
  - `long_arc_exists`
  - `long_arc_path`
  - optionally `long_arc_updated_at`
- this is a small mechanism change that would let multiple workflows surface doctrine status consistently instead of each reimplementing file checks

### Repo-local skill / command additions
- Near-term bridge, not permanent substitute:
  - add a repo-local `gsd-long-arc-review` or `gsd-doctrine-delta` skill for milestone start, transition, and completion if workflow patching will take longer
- Preferred steady state:
  - patch lifecycle workflows directly
  - use the skill as a deliberate review lane for major doctrine revisions, not as the only way doctrine survives the lifecycle

### Config changes
- For this repo specifically, doctrine-sensitive lifecycle health should not depend on `workflow.auto_advance: true`
- if auto-advance remains allowed, lifecycle commands need built-in doctrine checkpoints that still run under auto paths
- otherwise, set the live repo config to match the safer overlay default and keep doctrine review human-visible at task boundaries

## Recommended near-term GSD changes
1. Add first-class lifecycle awareness for `LONG-ARC.md` without redesigning the whole system.
   - patch `new-project`, `new-milestone`, `progress`, `transition`, and `complete-milestone`
2. Add init payload support for doctrine metadata.
   - this is low-cost and unlocks cleaner workflow patches everywhere else
3. Stop treating "has context" as sufficient in progress routing.
   - progress should surface whether the steering brief is canon-grounded and future-aware
4. Align auto-mode behavior with doctrine-sensitive repos.
   - at minimum, stop hardcoding `auto_advance: true` in `new-project` auto mode
   - ideally, ensure doctrine reviews cannot be silently skipped by auto paths
5. Keep phase-level mechanisms intact and build from them.
   - do not replace `canonical_refs`, `future_awareness`, or `future_preservation`
   - extend their lifecycle inputs upstream instead

## Recommended later GSD changes
1. Make durable doctrine a first-class optional artifact type in repo-local GSD.
   - not only `LONG-ARC.md` for this repo, but a general lifecycle-aware doctrine slot for projects that need it
2. Add milestone-level doctrine status and delta reporting.
   - enough to show whether doctrine is unchanged, refined, or contradicted by recent milestone work
3. Add lightweight doctrine-health reporting to `progress` and manager-style routing surfaces.
   - not just "phase planned?" but "steering substrate complete enough?"
4. Consider a formal doctrine-delta artifact on milestone completion.
   - useful when a repo wants an audit trail of what moved from exploratory or milestone-local learning into durable doctrine

## What should remain repo policy rather than be pushed into GSD
1. The actual Prix Guesser doctrine.
   - wrapper families
   - visibility ladder
   - host-identity distinctions
   - layered memory and cadence doctrine
   - obligation thresholds
2. Human signoff for doctrine changes that materially alter scope or posture.
   - GSD should surface the review, not autonomously ratify the doctrine shift
3. The repo-specific judgment of when `LONG-ARC.md` materially constrains a phase or quick task.
   - GSD can prompt for this; it should not universally assume it
4. The repo's broader governance rules around legal posture, branding, monetization, and publicness.
   - those belong in canon and governance docs, not hidden inside workflow internals

## Bottom line
`[e:c+r:i]` The repo-local GSD layer is already good at long-arc-aware phase steering once a phase has been framed correctly. Its weakness is lifecycle continuity, not phase intelligence ([.codex/get-shit-done/workflows/discuss-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/discuss-phase.md:331), [.codex/get-shit-done/templates/context.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/templates/context.md:93), [.codex/get-shit-done/workflows/research-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/research-phase.md:48), [.codex/get-shit-done/workflows/plan-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/plan-phase.md:295), [phase-prompt.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/templates/phase-prompt.md:25)).

Right now the stack is:

- `[e:c+r:i]` `strong` at discuss/research/plan carry-forward ([.codex/get-shit-done/workflows/discuss-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/discuss-phase.md:472), [.codex/get-shit-done/templates/context.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/templates/context.md:126), [.codex/get-shit-done/workflows/research-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/research-phase.md:74), [.codex/get-shit-done/workflows/plan-phase.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/plan-phase.md:698))
- `[a:c+r:i]` `conditional` for quick-task usage ([.codex/get-shit-done/workflows/quick.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/quick.md:8), [.codex/get-shit-done/workflows/quick.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/quick.md:309), [.codex/get-shit-done/workflows/quick.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/quick.md:316))
- `[e:c+r:i]` `weak` at project creation, milestone turnover, transition, completion, and progress visibility ([.codex/get-shit-done/workflows/new-project.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/new-project.md:214), [.codex/get-shit-done/workflows/new-project.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/new-project.md:1089), [.codex/get-shit-done/workflows/new-milestone.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/new-milestone.md:33), [.codex/get-shit-done/workflows/progress.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/progress.md:22), [.codex/get-shit-done/workflows/transition.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/transition.md:103), [.codex/get-shit-done/workflows/complete-milestone.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/complete-milestone.md:98), [.codex/get-shit-done/templates/project.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/templates/project.md:3), [.codex/get-shit-done/templates/roadmap.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/templates/roadmap.md:3), [.codex/get-shit-done/bin/lib/init.cjs](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/bin/lib/init.cjs:85))

So the right next move is not a generic GSD redesign. It is a targeted lifecycle uplift:

- make `LONG-ARC.md` a first-class optional lifecycle artifact
- translate it at milestone and transition boundaries
- expose doctrine status in progress/init plumbing
- keep carry-forward awareness strong without turning it into scope widening

## Sources
- `AGENTS.md`
- `.planning/AGENTS.md`
- `.planning/LONG-ARC.md`
- `.planning/PROJECT.md`
- `.planning/ROADMAP.md`
- `.planning/STATE.md`
- `.planning/REQUIREMENTS.md`
- `.planning/config.json`
- `.codex/get-shit-done/workflows/discuss-phase.md`
- `.codex/get-shit-done/workflows/discuss-phase-assumptions.md`
- `.codex/get-shit-done/workflows/discuss-phase-power.md`
- `.codex/get-shit-done/workflows/plan-phase.md`
- `.codex/get-shit-done/workflows/research-phase.md`
- `.codex/get-shit-done/workflows/new-project.md`
- `.codex/get-shit-done/workflows/new-milestone.md`
- `.codex/get-shit-done/workflows/progress.md`
- `.codex/get-shit-done/workflows/transition.md`
- `.codex/get-shit-done/workflows/complete-milestone.md`
- `.codex/get-shit-done/workflows/quick.md`
- `.codex/get-shit-done/templates/context.md`
- `.codex/get-shit-done/templates/project.md`
- `.codex/get-shit-done/templates/roadmap.md`
- `.codex/get-shit-done/bin/lib/init.cjs`
- `tooling/portable-gsd/overlay/get-shit-done/templates/context.md`
- `tooling/portable-gsd/overlay/get-shit-done/templates/phase-prompt.md`
- `tooling/portable-gsd/overlay/get-shit-done/workflows/discuss-phase.md`
- `tooling/portable-gsd/overlay/get-shit-done/workflows/plan-phase.md`
- `tooling/portable-gsd/overlay/get-shit-done/workflows/research-phase.md`
- `tooling/portable-gsd/overlay/get-shit-done/workflows/settings.md`
- `tooling/portable-gsd/overlay/get-shit-done/bin/lib/config.cjs`
- `tooling/portable-gsd/overlay/skills/gsd-discuss-phase/SKILL.md`
- `.planning/research/2026-04-15-orchestration-framework-audit/02-long-arc-lifecycle-integration-audit.md`
- `.planning/research/2026-04-15-orchestration-framework-audit/03-guardrails-mechanisms-and-command-proposals.md`
- `.planning/research/2026-04-15-orchestration-framework-audit/04-converged-synthesis.md`
- `.planning/research/2026-04-14-agents-md-audit/01-agents-md-audit-and-improvement-proposal.md`
