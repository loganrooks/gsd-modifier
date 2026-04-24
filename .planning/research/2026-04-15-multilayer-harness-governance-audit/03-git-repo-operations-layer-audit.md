# 03 Git And Repo-Operations Layer Audit

## Research Frame
- Mode: `synthesis`
- Question: What Git and repo-operations discipline should this repo adopt so planning, canon, research, implementation, and subagent work stay reviewable, revertible, and long-horizon-safe as the repo grows?
- Scope:
  - repo Git posture and current branch/worktree state
  - repo governance docs: `AGENTS.md`, `.planning/AGENTS.md`, `WORKFLOW.md`, `AI-GUARDRAILS.md`, `ARTIFACT-GOVERNANCE.md`
  - recent dirty-transition and cleanup artifacts
  - current repo-local GSD Git/worktree workflows and config where they materially affect repo discipline
- Non-goals:
  - full CI/CD, release engineering, or deployment design
  - generic DevOps best-practice dumping
  - replacing repo-local GSD or redesigning the full harness
- Stop condition:
  - identify current Git/repo-ops strengths and weak points
  - define near-term and later-stage Git governance rules
  - state what belongs in norms/docs, helper commands, branch/worktree policy, and CI checks

## Artifacts Read
- `AGENTS.md`
- `.planning/AGENTS.md`
- `WORKFLOW.md`
- `AI-GUARDRAILS.md`
- `ARTIFACT-GOVERNANCE.md`
- `.planning/PROJECT.md`
- `.planning/LONG-ARC.md`
- `.planning/ROADMAP.md`
- `.planning/STATE.md`
- `.planning/research/2026-04-15-orchestration-framework-audit/01-orchestration-and-task-transition-failure-audit.md`
- `.planning/research/2026-04-15-orchestration-framework-audit/03-guardrails-mechanisms-and-command-proposals.md`
- `.planning/research/2026-04-15-orchestration-framework-audit/04-converged-synthesis.md`
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-worktree-stabilization-note.md`
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-git-cleanup-checkpoint-plan.md`
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-git-cleanup-execution-report.md`
- `.planning/knowledge/signals/prix-guesser/2026-04-15-dirty-task-transitions-mixed-worktree.md`
- `.planning/knowledge/index.md`
- `.planning/config.json`
- `.codex/hooks.json`
- `.codex/get-shit-done/workflows/execute-phase.md`
- `.codex/get-shit-done/workflows/quick.md`
- `.codex/get-shit-done/workflows/ship.md`
- `.codex/get-shit-done/workflows/new-workspace.md`
- live repo observation from:
  - `git status --short --branch`
  - `git branch --all`
  - `git worktree list`
  - `git log --oneline main..HEAD`
  - `git diff --stat main...HEAD`

## Motivating grounds
This lane exists because the recent failure was version-control-deep, not just orchestration-deep.

- `.planning/knowledge/signals/prix-guesser/2026-04-15-dirty-task-transitions-mixed-worktree.md` formalizes the core failure as unresolved concern buckets crossing task boundaries in one working tree.
- `05-worktree-stabilization-note.md` and `05-git-cleanup-checkpoint-plan.md` explicitly reframe the problem as recovering logical Git change sets, not merely cleaning files.
- `05-git-cleanup-execution-report.md` shows the repo already had to reconstruct a mixed tree into multiple explicit commits, which is evidence of both recovery capacity and prior discipline failure.
- `WORKFLOW.md` already asks for short-lived branches, PR-style boundaries, and reviewable commits, while `.planning/config.json` still says `git.branching_strategy: "none"`. That mismatch is itself a governance problem.
- The current repo state is cleaner than the failure moment, but the branch posture is still a warning sign:
  - `git status --short --branch` shows only the new multi-layer audit bundle as untracked work
  - `git log main..HEAD` shows a bounded seven-commit recovery/history on `phase-01-guardrails-rerun-boundary`
  - `git diff --stat main...HEAD` still shows a large branch-level delta to `main`, which means commit discipline alone is not enough if branch scope remains too broad

## Path Of Inquiry
- Entry point:
  - the user's explicit reframing of the problem as Git working-tree / version-control discipline for a large, long-lived, agent-assisted repo
- Branches considered:
  - same-checkout path-based commit discipline
  - branch scope and branch lifetime
  - worktree isolation for subagents and parallel streams
  - subagent-return acceptance/disposition rules
  - PR/review/merge posture
  - whether local hygiene should live mainly in docs, commands, hooks, branch policy, or CI
- Branches pursued:
  - branch/worktree decision rules
  - change-set and checkpoint discipline
  - review and merge boundaries
  - what this repo should enforce now versus later
- Branches deferred or abandoned:
  - CI/deployment implementation detail beyond merge-boundary enforcement
  - generic hosted-release policy
  - full redesign of repo-local GSD
- Unexpected branches / reframings:
  - the repo already has more Git-aware machinery than the governance docs alone suggest
  - the deeper gap is not lack of Git features, but lack of explicit policy for when to use path staging, branches, worktrees, auto-merge cleanup, and PR boundaries
  - the current repo can produce clean commits and still carry an oversized branch-level diff, so `clean commit history` and `reviewable integration boundary` must be treated separately

## Assumptions Surfaced
- `[a:c+r:i]` The repo will remain solo-developer but agent-heavy in the near term ([WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:12), [AI-GUARDRAILS.md](/home/rookslog/workspace/projects/prix-guesser/AI-GUARDRAILS.md:102)).
  - Why it matters: near-term governance should strengthen reviewability and rollback without jumping straight to heavy multi-team bureaucracy.
  - What could weaken it: a shift to multiple frequent human contributors or public open-source contribution.
- `[a:c+r:i]` Same-checkout path-based commits remain a necessary recovery and low-overhead tool for this repo ([05-git-cleanup-checkpoint-plan.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-git-cleanup-checkpoint-plan.md:150), [05-git-cleanup-execution-report.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-git-cleanup-execution-report.md:49)).
  - Why it matters: the right answer is not `always use worktrees`.
  - What could weaken it: if the repo moves to sustained parallel code and canon streams where same-checkout work becomes more dangerous than helpful.
- `[a:c+r:i]` Long-horizon quality in this repo depends on decision traceability and reversibility as much as on source cleanliness ([AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:57), [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:45), [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:49), [05-worktree-stabilization-note.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-worktree-stabilization-note.md:135)).
  - Why it matters: this repo carries canon, doctrine, audit history, and future-seam protection in Git, not only source code.
  - What could weaken it: if the repo later externalizes most audit/canon history away from the main code repository.

## Evidence Base
### Direct evidence
- `WORKFLOW.md` already says:
  - do not work directly on `main` for substantive code or canon changes
  - prefer short-lived branches with explicit scope
  - prefer PR-style review boundaries even when working solo
  - prefer squash merge for most branches unless preserving a multi-commit audit trail matters
- `AI-GUARDRAILS.md` and `AGENTS.md` treat canon, roadmap, legal, infra, destructive cleanup, and other high-stakes changes as human-boundary territory.
- `ARTIFACT-GOVERNANCE.md` already distinguishes canon, audit trail, exploration, and generated corpus, and explicitly describes an `archive/` or `research-archive/` branch strategy for bulky retained material.
- `05-worktree-stabilization-note.md`, `05-git-cleanup-checkpoint-plan.md`, and `05-git-cleanup-execution-report.md` already encode the repo's most concrete Git lesson:
  - mixed concern buckets are the real failure
  - same-checkout path staging was the right recovery tool for that already-mixed tree
  - the recovery outcome was five bounded commits plus a final report
- `.planning/knowledge/signals/prix-guesser/2026-04-15-dirty-task-transitions-mixed-worktree.md` explicitly says unresolved concern buckets should block new substantive work.
- `.planning/config.json` still sets:
  - `git.branching_strategy: "none"`
  - `mode: "yolo"`
  - `workflow.auto_advance: true`
- `.codex/get-shit-done/workflows/execute-phase.md` and `quick.md` already support worktree-isolated execution and cleanup, including:
  - sequential worktree creation for parallel agents
  - merge-back of worktree branches
  - orchestrator-owned-file protection for `.planning/STATE.md` and `.planning/ROADMAP.md`
- `.codex/get-shit-done/workflows/ship.md` assumes a clean tree and prefers shipping from a feature branch, not from `main`.
- `.codex/get-shit-done/workflows/new-workspace.md` already supports `worktree` and `clone` strategies, which means isolation mechanisms exist locally.
- `.codex/hooks.json` is deliberately narrow:
  - startup guardrail reminder
  - destructive Bash denial only
- Current repo observation:
  - `git status --short --branch` shows the repo is on `phase-01-guardrails-rerun-boundary` with only the new audit bundle untracked
  - `git worktree list` shows only the main checkout is active right now
  - `git log main..HEAD` shows seven bounded commits on the current branch
  - `git diff --stat main...HEAD` shows a large branch-level integration delta relative to `main`

### Inference and interpretation
- The repo is already capable of disciplined Git recovery and explicit change-set reconstruction. The problem is not ignorance of Git; it is inconsistent governance around when to switch from one change-set strategy to another.
- Branch policy is currently misaligned across layers:
  - repo workflow doctrine wants scoped feature branches and review boundaries
  - runtime config still advertises `branching_strategy: none`
  - execution workflows can silently rely on worktree isolation and merge-back behavior anyway
- This means the repo's Git surface is not underpowered. It is under-explicit.
- Path-based commits in one checkout are a valid technique here, but they are being asked to do two different jobs:
  - disciplined single-bucket work
  - emergency recovery of already-mixed work
  Those must be distinguished or the repo will normalize recovery tactics as daily operating posture.
- The current branch history is a mixed signal in an important way:
  - positive: the commits are much more reviewable than the earlier mixed tree
  - negative: the branch as a whole is still large enough that `merge to main` reviewability becomes its own risk
- Local hooks are correctly narrow. Mixed concern-bucket classification, accept/revise/park decisions, and branch/worktree choice are too contextual to live mainly in blocking hooks.
- CI can help at merge boundaries, but it cannot solve the core local problem of deciding whether the current working tree still represents one coherent objective.

### Unknowns
- Whether the remote host actually enforces the branch protection recommendations documented in `WORKFLOW.md`
- Whether `workflow.use_worktrees` is intentionally configured elsewhere or is currently riding on workflow defaults
- Whether the current long-lived branch posture is a temporary artifact of the recent recovery burst or a recurring repo habit

## Current Git/repo-ops strengths
- The repo already has explicit Git doctrine in `WORKFLOW.md` instead of leaving all discipline to habit.
- The repo has a real concept of artifact classes and archive branches, which matters because this repo stores canon, audits, and generated corpus alongside code.
- The recent cleanup artifacts show the repo can recover from a mixed tree by turning one pile into bounded logical commits without destructive resets.
- The current feature-branch history shows change-set thinking is achievable here; the repo is not trapped in one giant undifferentiated commit style.
- The local GSD workflows already know how to:
  - create/use feature branches
  - isolate work in worktrees
  - merge worktree outputs back
  - protect orchestrator-owned planning files from stale worktree overwrites
- The repo's current hook posture is disciplined:
  - hooks warn or block only at obviously appropriate layers
  - they do not pretend to solve nuanced repo-governance questions

## Current weak points
- The repo's policy/config stack is internally inconsistent:
  - `WORKFLOW.md` prefers short-lived scoped branches
  - `.planning/config.json` still says `git.branching_strategy: "none"`
- There is no explicit repo rule yet for when same-checkout path-based commits are acceptable versus when separate branch or worktree isolation is mandatory.
- The repo has a task-transition lesson, but not yet a full repo-ops rule set that ties:
  - concern bucket
  - branch scope
  - worktree choice
  - subagent disposition
  - merge boundary
  into one operating model.
- Current workflows can merge worktree results back automatically, but repo governance does not yet require an explicit `accept / revise / park / reject` disposition before moving on.
- The current branch-to-main delta is large enough that branch-level reviewability is weaker than commit-level reviewability.
- The repo does not yet have a cheap helper command for day-to-day change-set classification, checkpointing, or parking, which means operators have to reconstruct discipline manually.
- Because this repo is docs-, canon-, and audit-heavy, there is a special risk that unrelated work gets mislabeled as one acceptable bucket simply because it all lives under `.planning/` or "is only docs."

## Recommended near-term rules
- `Rule 1`: No new substantive task may begin while the working tree still contains unresolved files from more than one substantive concern bucket.
- `Rule 2`: Do not do substantive work directly on `main`. Use a scoped objective branch even for canon and governance changes.
- `Rule 3`: One branch should correspond to one coherent objective that can be explained in one short paragraph relative to its base branch.
- `Rule 4`: Treat `git diff <base>...HEAD` as a first-class review surface. If the whole branch diff is no longer one coherent review unit, the branch is too broad even if the commits are individually tidy.
- `Rule 5`: Same-checkout path-based commits are acceptable only when:
  - the work belongs to one coherent concern bucket
  - there is only one active write stream
  - the branch will remain reviewable as one objective
  - or the repo is intentionally recovering an already-mixed tree
- `Rule 6`: A returned subagent write result is provisional until the orchestrator explicitly marks it `accept`, `revise`, `park`, or `reject`.
- `Rule 7`: Canon/governance changes and implementation changes should not remain unresolved in the same branch once they need independent review, rollback, or continuation timing.
- `Rule 8`: Audit corpus imports, archive moves, and generated-corpus retention work must be treated as explicit repo-operations change sets, not ambient cleanup.
- `Rule 9`: Merge readiness is not `working tree clean`. Merge readiness is:
  - one coherent branch objective
  - clear motivating artifact or reason
  - reviewable diff
  - explicit disposition of any subagent-returned work

## Recommended later rules as repo complexity rises
- When parallel human or subagent streams become normal, require separate worktrees or child branches for every concurrent write stream by default.
- When code, canon, and deploy/runtime changes begin landing together more often, require separate PR boundaries for:
  - doctrine/canon changes
  - code/runtime changes
  - release/deploy or repo-infrastructure changes
- When branch count and review pressure rise, standardize branch naming beyond loose prefixes and require a short branch intent note or PR body template for every mergeable branch.
- When the repo begins carrying more public-facing or operationally costly changes, protect `main` on the remote with required PRs, required checks, and up-to-date-with-base enforcement.
- If large historical corpora continue to accumulate, formalize an integration rule that keeps active development branches focused while moving bulky retained material to explicit archive branches or curated subsets.

## Branch/worktree strategy guidance
### Same-checkout path-based commits are acceptable when
- the repo is already in one checkout and the correct move is to recover or checkpoint coherent path groups without inventing retroactive parallelism
- the task is one bounded concern bucket with tightly coupled support artifacts
- there is one active writer and no need for another lane to continue independently
- the expected lifetime is short enough that the branch-level diff will remain reviewable as one unit

### Separate branch is mandatory when
- starting any new substantive objective from a clean or stabilized base
- the work would be unsafe or awkward to merge with the current branch objective
- the work needs a separate rollback unit from the existing branch
- the diff to base can no longer be explained as one objective in one short paragraph
- the work materially changes canon/governance and code in ways that deserve separate review timing

### Separate worktree is mandatory when
- two write streams need to proceed in parallel
- a subagent is expected to modify files for more than a quick bounded task while the main branch continues
- one stream is risky cleanup, archive/corpus movement, or broad refactoring that should not destabilize active work
- a long-running research/governance lane and an implementation lane both need live write scopes
- a paused or waiting-for-review stream must remain intact while another objective advances

### Read-only or low-risk cases
- Read-only research does not need a new worktree just for ceremony.
- Tiny, tightly scoped fixups on the current objective branch do not need a new worktree if they do not create a second unresolved concern bucket.
- Path-based staging should remain available as a surgical tool, but it should not be the default answer to sustained parallelism.

## Checkpoint/park/accept/revise guidance
- `Accept`
  - review the diff as one concern bucket
  - confirm it still matches the branch objective
  - confirm validation is proportionate to the risk
  - keep it on the branch or merge the worktree back
- `Revise`
  - do not start a new substantive task
  - send the same branch/worktree back for revision or create a tightly related follow-up branch
  - keep the original objective and acceptance state explicit
- `Park`
  - never leave parked work as ambient modified files
  - park it as an explicit branch, worktree, or clearly labeled stash only when truly necessary
  - record why it is parked, what owns it, and what would resume it
- `Reject`
  - do not let rejected work sit in the tree
  - drop the worktree/branch or revert the bounded change set before moving on

For subagent-returned work specifically:
- The orchestrator should review:
  - affected paths
  - whether the output stayed inside its declared concern bucket
  - whether the result belongs on the current branch at all
- Auto-merge of worktree results may remain a mechanical convenience, but it must not be mistaken for semantic acceptance.

## Review/merge expectations
- Keep PR-style review boundaries even when working solo.
- Require every mergeable branch to answer, in one short note or PR body:
  - what objective this branch serves
  - what artifact or decision motivated it
  - what changed class it contains:
    - canon
    - audit/history
    - governance
    - code/runtime
    - archive/corpus
  - what remains open
- Prefer squash merge when the branch is one coherent objective and the commit chronology is not itself evidence.
- Preserve multi-commit history when the commit sequence is part of the audit/recovery trail.
- Do not merge a branch to `main` just because its working tree is clean if the branch still contains multiple objectives relative to base.
- Before merge, review the branch as the reviewer will see it:
  - `git diff base...HEAD`
  - not only `git log`

## Progressive governance by risk and blast radius
`[e:c+r:i]` The right escalation model is not `bigger repo -> more ceremony`. It is `higher risk / larger blast radius / more parallel write activity -> stronger repo-ops controls` ([WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:30), [05-git-cleanup-checkpoint-plan.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-git-cleanup-checkpoint-plan.md:187), [04-converged-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-orchestration-framework-audit/04-converged-synthesis.md:117)).

| Risk / blast radius | Typical repo shape | Appropriate Git discipline now | Stronger discipline later |
| --- | --- | --- | --- |
| Low | one writer, one concern bucket, short-lived docs/code fix | scoped feature branch, same-checkout path staging allowed, local review against base | PR template consistency if these become frequent |
| Medium | canon or governance change, multi-commit audit bundle, moderate rollback cost | explicit branch objective, accept/revise/park rule, review whole branch diff before merge | separate worktree if the stream will sit open while other work continues |
| High | parallel subagents, code plus canon, archive moves, broad refactors | separate branches and usually separate worktrees, explicit disposition before merge-back, no new bucket until one closes | required PR checks and stricter branch freshness on remote |
| Very high | public-facing or operationally expensive changes, multiple active environments, multiple contributors | protected `main`, PR-only merges, required checks, up-to-date-with-base enforcement | richer release/integration policy handled in the CI/release lane |

What should not scale mainly with repo size:
- blocking hooks for nuanced local branch-choice decisions
- blanket worktree creation for every tiny task
- automatic treatment of all `.planning/` changes as one acceptable bucket

## What should be enforced by norms/docs, helper commands, branch/worktree policy, and CI checks
### Norms/docs
- concern-bucket language
- one-branch-one-objective rule
- branch-level reviewability rule
- accept/revise/park/reject requirement for returned work
- explicit distinction between recovery tactics and normal operating posture
- artifact-class separation for canon, audit/history, archive/corpus, and code

### Helper commands
- a bucket-aware `status` or `transition gate` command that groups modified paths by likely concern bucket
- a `checkpoint` command that records branch objective, current disposition, and paths owned by the current change set
- a lightweight `park` command that turns ambient work into an explicit parked branch/worktree or labeled stash with a note
- a `subagent disposition` command or template that makes `accept / revise / park / reject` cheap and routine

### Branch/worktree policy
- branch required for every substantive objective
- worktree required for concurrent write streams and long-lived isolated lanes
- no advancing one branch with multiple unresolved objectives just because path staging could theoretically separate them later
- explicit archive-branch use when bulky retained corpus would otherwise dominate active development branches

### CI checks
- protect `main`
- require PRs to merge to `main`
- require status checks before merge
- require branch to be up to date before merge
- optionally require a small PR template or branch description field that states objective and affected change class

What CI should not try to own:
- local concern-bucket classification
- same-checkout versus worktree choice
- subagent acceptance semantics before the branch reaches merge boundary

## How this layer supports long-horizon quality, not just cleanliness
In this repo, Git is carrying more than code delivery. It is also carrying:
- doctrine changes in `PROJECT.md` and `LONG-ARC.md`
- roadmap and requirement shifts
- audit trail and historical challenge artifacts
- archive/corpus retention decisions
- governance and agent-operating rules

That means repo-ops quality has to protect:
- reversibility of doctrine
- reviewability of canon uplift
- traceability of why a seam was preserved or closed
- recoverability from experiments, audit bursts, and archive moves

`Clean tree` is only the surface signal. The deeper quality bar is:
- later rereaders can understand why a change landed
- future rollback does not require archaeology across mixed objectives
- long-arc seam protection is not silently changed inside a broad unrelated branch
- historical audit material stays attributable without dominating active development

## Dependencies And Relations
| Item | Depends on | Constrains or affects | Vulnerability |
| --- | --- | --- | --- |
| Concern-bucket classification | path visibility, explicit task ownership, operator honesty | task transitions, path-based commits, park/reject decisions | high |
| Branch objective discipline | base-branch choice, review habit, small-scope planning | merge readability, rollback clarity, PR quality | high |
| Worktree isolation | Git worktree support, lane parallelism, cleanup discipline | concurrent write safety, subagent containment | medium |
| Subagent disposition | explicit return checkpoint, review boundary, owned output | whether merge-back means anything semantically | high |
| Archive-branch strategy | artifact classification, retention intent | workspace readiness, audit/corpus sprawl | medium |
| CI merge gates | remote branch protection, status checks | final integration safety | medium |

## Scope Expansions And Deferrals
- Defer:
  - full CI/release/deployment control design to lane `04`
  - remote-host configuration details beyond merge-boundary protection
- Follow-and-mark:
  - whether `.planning/config.json` should stop advertising `git.branching_strategy: "none"`
  - whether `workflow.auto_advance` and related autonomy defaults should be tightened at the same time
- Revisit later:
  - whether the repo needs a more formal integration-branch model instead of only short-lived objective branches
  - whether archive-branch use should become default for certain large retained corpora

## What can close now
- The repo's Git problem is not merely `dirty tree`; it is unresolved mixed concern buckets and oversized integration boundaries.
- Same-checkout path-based commits should remain a valid recovery and single-bucket tool.
- Separate branch/worktree policy needs to become explicit now, not later.
- Most of the important discipline belongs in norms, helper commands, and branch/worktree policy, not in heavy hooks.
- Branch-level reviewability must be treated as a separate control surface from commit-level tidiness.

## What must stay open
- The exact config change sequence for `branching_strategy`, `workflow.use_worktrees`, and autonomy defaults
- Whether the current long-lived branch posture is transitional or structural
- The exact helper command surface that should implement transition gates and parking
- The actual remote enforcement state of branch protections

## Planning Handoff
### What can now be treated as decided
- Git governance for this repo must reason in terms of logical change sets and concern buckets, not just file cleanliness.
- Path-based same-checkout work is acceptable, but only inside explicit limits.
- Parallel or long-lived independent streams should use separate worktrees or branches.
- Returned subagent work must be dispositioned explicitly before new substantive work begins.
- Branch-level diff review should become a standing repo habit.

### What remains assumed or open
- How much of this should land as repo docs versus repo-local GSD command support
- Whether config changes should be bundled with broader harness changes or staged separately

### Derived constraints
- Do not let `.planning/` become an excuse for mixed branches.
- Do not rely on CI to solve local change-set classification.
- Do not treat auto-merged worktree results as already accepted.
- Keep archive/corpus moves explicit so long-horizon history remains reviewable instead of ambient.

### Future-awareness seams to preserve
- canon uplift should stay separately reviewable from implementation and cleanup work
- historical audit trail should remain attributable without bloating active branches unnecessarily
- preserve the ability to move bulky retained material to archive branches without silent deletion
- long-arc doctrine updates should stay easy to trace and easy to reverse

### Deferred follow-up lanes
- lane `04`: CI / release / deployment governance
- lane `05`: cross-layer integration and escalation
- lane `06`: converged synthesis

## Sources
- `AGENTS.md`
- `.planning/AGENTS.md`
- `WORKFLOW.md`
- `AI-GUARDRAILS.md`
- `ARTIFACT-GOVERNANCE.md`
- `.planning/PROJECT.md`
- `.planning/LONG-ARC.md`
- `.planning/ROADMAP.md`
- `.planning/STATE.md`
- `.planning/research/2026-04-15-orchestration-framework-audit/01-orchestration-and-task-transition-failure-audit.md`
- `.planning/research/2026-04-15-orchestration-framework-audit/03-guardrails-mechanisms-and-command-proposals.md`
- `.planning/research/2026-04-15-orchestration-framework-audit/04-converged-synthesis.md`
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-worktree-stabilization-note.md`
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-git-cleanup-checkpoint-plan.md`
- `.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/05-gap-closure/05-git-cleanup-execution-report.md`
- `.planning/knowledge/signals/prix-guesser/2026-04-15-dirty-task-transitions-mixed-worktree.md`
- `.planning/knowledge/index.md`
- `.planning/config.json`
- `.codex/hooks.json`
- `.codex/get-shit-done/workflows/execute-phase.md`
- `.codex/get-shit-done/workflows/quick.md`
- `.codex/get-shit-done/workflows/ship.md`
- `.codex/get-shit-done/workflows/new-workspace.md`
- live repo Git observations captured on 2026-04-15 from `git status`, `git branch`, `git worktree list`, `git log main..HEAD`, and `git diff --stat main...HEAD`
