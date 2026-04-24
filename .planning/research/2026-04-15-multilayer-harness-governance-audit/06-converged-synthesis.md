# 06 Converged Synthesis

## Research Frame
- Mode: `synthesis`
- Question:
  Given the narrower orchestration/framework synthesis plus the five multi-layer audit lanes, what is the correct broader answer about this repo's harness/governance stack, what should change now, what should be deferred, and how should stronger controls escalate as risk, parallelism, and operational burden rise?
- Scope:
  - `.planning/research/2026-04-15-multilayer-harness-governance-audit/00-launch-bundle-spec.md`
  - `.planning/research/2026-04-15-multilayer-harness-governance-audit/01-codex-orchestration-layer-audit.md`
  - `.planning/research/2026-04-15-multilayer-harness-governance-audit/02-gsd-lifecycle-and-long-arc-layer-audit.md`
  - `.planning/research/2026-04-15-multilayer-harness-governance-audit/03-git-repo-operations-layer-audit.md`
  - `.planning/research/2026-04-15-multilayer-harness-governance-audit/04-ci-release-and-deployment-layer-audit.md`
  - `.planning/research/2026-04-15-multilayer-harness-governance-audit/05-cross-layer-integration-and-escalation-audit.md`
  - `.planning/research/2026-04-15-multilayer-harness-governance-audit/08-external-comparative-governance-research.md`
  - `.planning/research/2026-04-15-orchestration-framework-audit/04-converged-synthesis.md`
  - repo governance and canon needed to interpret those artifacts:
    - `AGENTS.md`
    - `.planning/AGENTS.md`
    - `WORKFLOW.md`
    - `AI-GUARDRAILS.md`
    - `ARTIFACT-GOVERNANCE.md`
    - `.planning/PROJECT.md`
    - `.planning/LONG-ARC.md`
    - `.planning/ROADMAP.md`
    - `.planning/REQUIREMENTS.md`
    - `.planning/STATE.md`
    - `.planning/knowledge/index.md`
- Non-goals:
  - patching the framework or repo in this artifact
  - replacing Codex or repo-local GSD
  - finalizing a production DevOps stack before the repo has a runnable product
  - relitigating Prix Guesser product doctrine beyond the current canon
- Stop condition:
  - answer the broader ask directly
  - preserve the distinction between the narrower orchestration audit and the larger multi-layer audit
  - identify current-need changes, deferred-but-important work, and later escalation by risk / blast radius / complexity

## Artifacts Read
- `.planning/research/2026-04-15-multilayer-harness-governance-audit/00-launch-bundle-spec.md`
- `.planning/research/2026-04-15-multilayer-harness-governance-audit/01-codex-orchestration-layer-audit.md`
- `.planning/research/2026-04-15-multilayer-harness-governance-audit/02-gsd-lifecycle-and-long-arc-layer-audit.md`
- `.planning/research/2026-04-15-multilayer-harness-governance-audit/03-git-repo-operations-layer-audit.md`
- `.planning/research/2026-04-15-multilayer-harness-governance-audit/04-ci-release-and-deployment-layer-audit.md`
- `.planning/research/2026-04-15-multilayer-harness-governance-audit/05-cross-layer-integration-and-escalation-audit.md`
- `.planning/research/2026-04-15-multilayer-harness-governance-audit/08-external-comparative-governance-research.md`
- `.planning/research/2026-04-15-multilayer-harness-governance-audit/06-converged-synthesis-task-spec.md`
- `.planning/research/2026-04-15-orchestration-framework-audit/04-converged-synthesis.md`
- `AGENTS.md`
- `.planning/AGENTS.md`
- `WORKFLOW.md`
- `AI-GUARDRAILS.md`
- `ARTIFACT-GOVERNANCE.md`
- `.planning/PROJECT.md`
- `.planning/LONG-ARC.md`
- `.planning/ROADMAP.md`
- `.planning/REQUIREMENTS.md`
- `.planning/STATE.md`
- `.planning/knowledge/index.md`
- `.planning/knowledge/signals/prix-guesser/2026-04-15-dirty-task-transitions-mixed-worktree.md`
- `.planning/knowledge/signals/prix-guesser/2026-04-15-underdelegated-exploration-orchestrator-role-drift.md`

## Path Of Inquiry
- Entry point:
  - The narrower orchestration/framework audit had already closed the immediate "what failed and what kind of guardrails are justified?" question, but explicitly deferred the broader stack question across Codex, GSD, Git/repo-ops, and CI/release/deployment.
- Branches considered:
  - whether the broader answer would mostly collapse into repo-ops recommendations
  - whether the main unresolved problem was still mainly orchestration
  - whether the right next move was stronger CI/release automation now
  - whether `LONG-ARC.md` carry-forward is mainly a GSD concern or a full-stack responsibility chain
  - whether the repo is already strong enough to reduce expert supervision without further structure
- Branches pursued:
  - what the narrower audit truly settled
  - what each new lane adds beyond that narrower result
  - where current control should live by layer
  - which controls require shared ownership rather than a single owner
  - how escalation should stage by actual risk rather than by "project gets bigger"
- Branches deferred or abandoned:
  - exact implementation placement of every helper command
  - final config patch sequence
  - final CI command surface once executable product code exists
  - final deploy bundle and runtime topology
- Unexpected branches / reframings:
  - the repo is not weak everywhere; it is strongest at doctrine definition and phase-local steering, but weaker at lifecycle carry-forward and boundary materialization
  - repo-operations is necessary but not a complete answer because many current failures occur before Git merge boundaries even exist
  - the immediate governance gap is not "more automation" but "clearer handoffs between layers"

## Assumptions Surfaced
- `[a:c+r:i]` The repo remains `solo-developer`, `agent-heavy`, `planning-heavy`, and `Phase 01 pre-rerun` in the near term ([WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:12), [AI-GUARDRAILS.md](/home/rookslog/workspace/projects/prix-guesser/AI-GUARDRAILS.md:102), [.planning/STATE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/STATE.md:63)).
  - Why it matters: near-term controls should emphasize visible workflow gates and reviewable boundaries over heavy production bureaucracy.
  - What could weaken it: a shift to frequent multi-human contribution or a runnable product with real operator burden.
- `[d:c:i]` `LONG-ARC.md` is doctrine, not a second roadmap ([.planning/LONG-ARC.md](/home/rookslog/workspace/projects/prix-guesser/.planning/LONG-ARC.md:20), [.planning/LONG-ARC.md](/home/rookslog/workspace/projects/prix-guesser/.planning/LONG-ARC.md:22), [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md:183), [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md:189)).
  - Why it matters: lifecycle and release controls must preserve doctrine translation without widening current milestone scope.
- `[a:c+r:i]` The most expensive current failures are still pre-merge and pre-deploy ([01-codex-orchestration-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/01-codex-orchestration-layer-audit.md:148), [03-git-repo-operations-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/03-git-repo-operations-layer-audit.md:145), [05-cross-layer-integration-and-escalation-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/05-cross-layer-integration-and-escalation-audit.md:431)).
  - Why it matters: upper layers should carry more of the immediate control burden than CI or release machinery.
  - What could weaken it: repeated failures that begin appearing mainly at merge or deployment boundaries once a runnable app exists.
- `[a:c+r:i+d]` Stronger controls should escalate by blast radius, parallelism, environment complexity, and obligation profile, not by repo age alone ([05-cross-layer-integration-and-escalation-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/05-cross-layer-integration-and-escalation-audit.md:434)).[^github-rulesets][^google-sre-release]
  - Why it matters: it keeps this audit from silently importing production-grade release automation before the repo has earned it.
  - What could weaken it: evidence that supposedly low-risk stages are already causing materially expensive failures.

## Motivating grounds
This synthesis exists because the broader question remained open after the narrower orchestration/framework audit closed.

The strongest grounds are:

- `00-launch-bundle-spec.md`
  - explicitly framed this as a multi-layer control problem rather than a repo-ops replacement for orchestration analysis
- `04-converged-synthesis.md` from the narrower audit
  - concluded that workflow and Git discipline were the immediate remedies, but explicitly deferred repo-operations / production-governance and broader layer assignment
- `01-codex-orchestration-layer-audit.md`
  - showed the Codex-layer problem is weak closure and task-transition control, not lack of worker capability
- `02-gsd-lifecycle-and-long-arc-layer-audit.md`
  - showed the GSD-layer problem is lifecycle carry-forward of doctrine, not weak phase-level planning intelligence
- `03-git-repo-operations-layer-audit.md`
  - showed the Git-layer problem is mixed concern buckets and oversized integration boundaries, not merely a cosmetically dirty tree
- `04-ci-release-and-deployment-layer-audit.md`
  - showed the CI/release lane is real, but its immediate value is narrow repo-integrity reinforcement because the repo has no deployable runtime yet
- `05-cross-layer-integration-and-escalation-audit.md`
  - showed the larger answer depends on explicit handoffs between layers rather than on nominating one universal harness
- `08-external-comparative-governance-research.md`
  - externally strengthened the risk-shaped escalation and explicit-handoff parts of this synthesis, while adding pressure to name issue/PR/MR templates, review routing, and hybrid automation-plus-approval release surfaces more explicitly ([08-external-comparative-governance-research.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/08-external-comparative-governance-research.md:86), [08-external-comparative-governance-research.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/08-external-comparative-governance-research.md:141))
- repo canon and governance
  - `AGENTS.md`, `.planning/AGENTS.md`, `WORKFLOW.md`, and `AI-GUARDRAILS.md` already distinguish doctrine, workflow, Git, CI, and human-signoff boundaries, so the broader answer must respect those distinctions

## Evidence Base
### Direct evidence
- `[e:c:i]` The narrower orchestration/framework synthesis already closed three points ([04-converged-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-orchestration-framework-audit/04-converged-synthesis.md:125), [04-converged-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-orchestration-framework-audit/04-converged-synthesis.md:138), [04-converged-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-orchestration-framework-audit/04-converged-synthesis.md:188)):
  - progressive guardrails are justified by risk and coordination complexity, not by repo size alone
  - immediate remedy should focus on workflow and Git discipline rather than production automation
  - a later broader repo-operations / production-governance pass was still needed
- `[e:c:i]` The Codex lane found ([01-codex-orchestration-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/01-codex-orchestration-layer-audit.md:140), [01-codex-orchestration-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/01-codex-orchestration-layer-audit.md:148)):
  - real launch discipline already exists
  - returned-task disposition, active-task modeling, and closure reporting are still weak
  - narrow hooks remain the correct hook posture
- `[e:c:i]` The GSD lane found ([02-gsd-lifecycle-and-long-arc-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/02-gsd-lifecycle-and-long-arc-layer-audit.md:133), [02-gsd-lifecycle-and-long-arc-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/02-gsd-lifecycle-and-long-arc-layer-audit.md:140)):
  - `LONG-ARC.md` is first-class in discuss/research/plan flow
  - lifecycle workflows remain mostly `LONG-ARC`-blind
  - live config and auto paths can bypass doctrine-sensitive review
- `[e:c:i]` The Git lane found ([03-git-repo-operations-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/03-git-repo-operations-layer-audit.md:132), [03-git-repo-operations-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/03-git-repo-operations-layer-audit.md:146)):
  - the repo already has meaningful Git doctrine and recovery capacity
  - policy/config mismatch and missing branch/worktree decision rules remain active gaps
  - branch-level reviewability must be treated separately from commit-level tidiness
- `[e:c:i]` The CI/release lane found ([04-ci-release-and-deployment-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/04-ci-release-and-deployment-layer-audit.md:104), [04-ci-release-and-deployment-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/04-ci-release-and-deployment-layer-audit.md:122)):
  - there is no `.github/` workflow surface and no runnable app/deploy bundle yet
  - the near-term win is narrow repo-integrity CI plus a canonical local verify entrypoint in the repo's current pre-runtime stage
  - deployment and release should remain manual and human-approved for now, while later automation should grow once a runnable surface exists
- `[e:c:i+t]` The external comparative pass found that risk-shaped escalation, explicit handoff artifacts, and hybrid automation-plus-approval release boundaries are stronger than the earlier draft made explicit, and that issue/PR/MR templates plus review routing are governance surfaces rather than optional polish ([08-external-comparative-governance-research.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/08-external-comparative-governance-research.md:86), [08-external-comparative-governance-research.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/08-external-comparative-governance-research.md:97), [08-external-comparative-governance-research.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/08-external-comparative-governance-research.md:117), [08-external-comparative-governance-research.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/08-external-comparative-governance-research.md:141)).
- `[e:c:d]` Mature workflow systems do treat issue/PR/MR templates, review-owner routing, and explicit deployment approval as first-class governance surfaces.[^github-issue-pr-templates][^github-codeowners][^gitlab-flow][^github-deployment-reviews]
- `[e:c:d]` Comparative practice also supports stronger CI/build/test enforcement once executable code and a stable local verify path exist, rather than treating CI minimalism as a durable norm.[^gitlab-flow][^github-rulesets][^google-sre-release]
- `[e:c:i]` The integration lane found ([05-cross-layer-integration-and-escalation-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/05-cross-layer-integration-and-escalation-audit.md:120), [05-cross-layer-integration-and-escalation-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/05-cross-layer-integration-and-escalation-audit.md:149), [05-cross-layer-integration-and-escalation-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/05-cross-layer-integration-and-escalation-audit.md:430)):
  - upper layers should own nuanced judgment and workflow visibility
  - lower layers should own durable boundary materialization and mechanical enforcement
  - the immediate problem is missing ownership transfer between layers
- `[e:c:i]` Current canon confirms ([AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:41), [AI-GUARDRAILS.md](/home/rookslog/workspace/projects/prix-guesser/AI-GUARDRAILS.md:15), [.planning/STATE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/STATE.md:63)):
  - `LONG-ARC.md` is live doctrine
  - human signoff remains required for legal, branding, monetization, hosting, infrastructure, and other obligation-changing decisions
  - the repo is still at a Phase 01 pre-rerun boundary and remains planning-heavy

### Inference and interpretation
- `[e:c+r:i]` The narrower audit was right but incomplete ([04-converged-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-orchestration-framework-audit/04-converged-synthesis.md:183), [05-cross-layer-integration-and-escalation-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/05-cross-layer-integration-and-escalation-audit.md:430)).
  - It correctly identified the immediate failure surface, but the broader audit shows that failure sits inside a larger chain of weak handoffs rather than inside the Codex layer alone.
- `[e:c+r:i]` The repo's strongest existing surface is doctrine definition plus phase-local translation ([02-gsd-lifecycle-and-long-arc-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/02-gsd-lifecycle-and-long-arc-layer-audit.md:133), [02-gsd-lifecycle-and-long-arc-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/02-gsd-lifecycle-and-long-arc-layer-audit.md:165), [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:51)).
  - The weakest existing surface is what happens between "doctrine exists" and "merge/release automation can honestly enforce anything."
- `[e:c+r:i]` Repo-operations is a middle boundary layer, not the whole answer ([03-git-repo-operations-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/03-git-repo-operations-layer-audit.md:145), [05-cross-layer-integration-and-escalation-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/05-cross-layer-integration-and-escalation-audit.md:174)).
  - Git can materialize branches, worktrees, and review units, but it cannot decide active task ownership or doctrine correctness by itself.
- `[a:c+r:i+t]` Current immediate controls belong mostly in `Codex + GSD + Git` for this repo's present stage, while the CI claim should be read narrowly as `pre-runtime and pre-stable-verify` rather than as a broader anti-CI rule ([05-cross-layer-integration-and-escalation-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/05-cross-layer-integration-and-escalation-audit.md:431), [08-external-comparative-governance-research.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/08-external-comparative-governance-research.md:124), [08-external-comparative-governance-research.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/08-external-comparative-governance-research.md:165)).
  - CI and release automation become valuable later, but they are not the cheapest or most honest place to catch today's failures.
- `[e:c+r:i+d]` Long-horizon quality depends on explicit handoff contracts, including explicit review artifacts and routing surfaces once remote review becomes real ([05-cross-layer-integration-and-escalation-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/05-cross-layer-integration-and-escalation-audit.md:127), [08-external-comparative-governance-research.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/08-external-comparative-governance-research.md:92)).[^github-issue-pr-templates][^github-codeowners]
  - Codex keeps the work bounded and reviewable while fluid
  - GSD translates doctrine into lifecycle-visible constraints
  - Git turns that into reviewable and reversible boundaries
  - CI verifies only what has become mechanically checkable
  - issue / PR / MR templates, review-owner routing, and linked issue-to-review artifacts become part of that handoff chain once those boundaries exist

### Unknowns
- `[o:c:i]` The exact packaging and placement of new disposition, doctrine-delta, or status helpers remain open ([01-codex-orchestration-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/01-codex-orchestration-layer-audit.md:156), [02-gsd-lifecycle-and-long-arc-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/02-gsd-lifecycle-and-long-arc-layer-audit.md:143)).
- `[o:c:i]` The exact sequence for tightening `.planning/config.json` versus patching workflows remains open ([01-codex-orchestration-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/01-codex-orchestration-layer-audit.md:160), [05-cross-layer-integration-and-escalation-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/05-cross-layer-integration-and-escalation-audit.md:132)).
- `[o:c:i]` The first canonical local verify command and later CI command surface remain open because executable product code does not yet exist ([04-ci-release-and-deployment-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/04-ci-release-and-deployment-layer-audit.md:126), [05-cross-layer-integration-and-escalation-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/05-cross-layer-integration-and-escalation-audit.md:133)).
- `[o:c:i]` The first real deploy bundle and rollback unit remain open because the repo still has no runnable runtime surface ([04-ci-release-and-deployment-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/04-ci-release-and-deployment-layer-audit.md:125), [04-ci-release-and-deployment-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/04-ci-release-and-deployment-layer-audit.md:128)).
- `[o:c:i]` The remote host's current branch-protection state was not verified in this synthesis ([WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:77), [05-cross-layer-integration-and-escalation-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/05-cross-layer-integration-and-escalation-audit.md:134)).

## Source-basis and epistemic limits

`[e:c:i+t]` This synthesis is materially stronger on repo-state diagnosis than on externally validated universal governance prescription, but it is no longer purely internal after the comparative pass in `08` ([08-external-comparative-governance-research.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/08-external-comparative-governance-research.md:194), [AI-GUARDRAILS.md](/home/rookslog/workspace/projects/prix-guesser/AI-GUARDRAILS.md:94)).

### Claims that are mostly `internal/cited`

`[e:c:i]` These hold up well because they are grounded in repo-local artifacts about the current stack ([01-codex-orchestration-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/01-codex-orchestration-layer-audit.md:140), [02-gsd-lifecycle-and-long-arc-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/02-gsd-lifecycle-and-long-arc-layer-audit.md:133), [03-git-repo-operations-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/03-git-repo-operations-layer-audit.md:132), [04-ci-release-and-deployment-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/04-ci-release-and-deployment-layer-audit.md:104)):

- the repo is strong at doctrine definition and phase-local steering
- `LONG-ARC.md` is phase-strong but lifecycle-weak
- Codex launch discipline exists but task disposition/closure handling is weak
- Git recovery capacity exists but explicit branch/worktree operating rules are still thin
- CI/release/deployment governance is currently intentionally thin

Those are primarily claims about the repo as it currently exists, and the supporting evidence is overwhelmingly internal and directly inspectable.

### Claims that are now `internal + externally strengthened`

`[e:c:i+d]` These are materially stronger after `08`, but they still should not be overstated as universal best practice ([08-external-comparative-governance-research.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/08-external-comparative-governance-research.md:151), [08-external-comparative-governance-research.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/08-external-comparative-governance-research.md:204)).[^github-rulesets][^github-deployment-reviews][^google-sre-release]

- risk-shaped escalation is the right broad pattern
- explicit handoff artifacts beat ambient memory
- lower layers should verify mechanical truth rather than decide doctrine
- manual approval and automation are compatible rather than mutually exclusive
- issue / PR / MR templates and review routing deserve to be treated as governance surfaces once remote review flow exists

### Claims that remain mostly `repo-specific reasoned guidance`

`[a:c+r:i+t]` These remain useful, but they are still local staging judgment rather than externally proven optimal weighting ([05-cross-layer-integration-and-escalation-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/05-cross-layer-integration-and-escalation-audit.md:431), [08-external-comparative-governance-research.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/08-external-comparative-governance-research.md:163)).

- immediate controls should live mostly in `Codex + GSD + Git`
- CI should stay narrow only while this repo remains pre-runtime and lacks a stable local verify contract
- release/deploy approval should remain manual and human-visible until there is a real deploy surface
- stronger controls should escalate by risk, blast radius, parallelism, and environment complexity
- the main near-term problem is under-specified handoff between layers

These recommendations are defensible from the repo's current state and failure history, and `08` strengthens some adjacent governance principles, but this bundle still did not prove that the repo's exact local weighting is generally optimal across other repos.

### Claims that are `not externally grounded in this bundle`

`[o:c:i+t]` This bundle still does not provide direct external grounding for several broader claims, even after `08` ([08-external-comparative-governance-research.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/08-external-comparative-governance-research.md:180)).

- universal best-practice claims about optimal CI or deployment governance
- broad industry claims about how all large agent-assisted repos should stage controls
- strong comparative claims that this repo's current staged approach is better than other viable governance models in general

`[e:c+r:i+t]` So this artifact should be treated as strong internal synthesis plus partially externally strengthened governance guidance, not as a fully externally validated general theory ([08-external-comparative-governance-research.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/08-external-comparative-governance-research.md:204)).

That does not invalidate the recommendations, but it does limit how confidently they should be treated beyond this repo's current circumstances.

## Integrated diagnosis

### 1. What the narrower orchestration audit settled
The narrower audit can now be treated as having closed the following:

- the recent failure was not merely "bad delegation" or "dirty tree" in isolation
- the real pattern was:
  - meaningful delegation succeeded
  - returned work was not dispositioned
  - the main thread resumed exploratory work locally
  - the working tree accumulated multiple unresolved logical buckets
- the right immediate remedy was not broad hook expansion or production automation
- the right immediate remedy was stronger workflow and Git discipline
- the next unanswered question was how that remedy should distribute across the larger stack

What it left open:

- what belongs primarily at Codex versus GSD versus Git versus CI
- how `LONG-ARC.md` should move across day-to-day lifecycle boundaries
- how repo-operations fits without becoming the whole answer
- what stronger controls should wait for later runtime and deployment maturity

### 2. What the broader multi-layer audit adds
The broader audit adds four important conclusions the narrower audit could not settle by itself:

- `Codex` is not missing worker capability; it is missing active-task, disposition, and closure structure.
- `Repo-local GSD` is not weak at phase-local steering; it is weak at lifecycle carry-forward of doctrine.
- `Git / repo-ops` is not merely a cleanliness layer; it is the durable boundary layer for reviewability, rollback, and parked work.
- `CI / release / deployment` is a real governance lane, but its immediate role is narrow because there is no runnable product surface yet.

The integration lane then adds the controlling synthesis:

- the repo's main problem is under-specified handoffs between layers
- the highest-value near-term controls belong in the upper layers because current failures happen while work is still fluid
- lower-layer automation should harden only after upper-layer ambiguity is reduced and the runtime surface becomes real

`08` then sharpens that synthesis in three places:

- issue / PR / MR templates, review-owner routing, and linked issue-to-review artifacts should be named as governance surfaces rather than left implicit
- `CI should stay narrow` is valid only for the repo's current pre-runtime stage, not as a broader claim against early branch/PR CI once executable code exists
- manual approval should be distinguished from `lack of automation`; the later healthy shape is a hybrid of mechanical checks plus explicit human approval where deploy or environment risk justifies it

### 3. Broader stack diagnosis
The broader stack is best understood as:

- `strong` at doctrine definition and phase-level future-aware steering
- `partially strong` at orchestration launch discipline and Git recovery capacity
- `weak` at lifecycle carry-forward, task closure, explicit branch/worktree operating rules, and merge-boundary automation
- `intentionally thin` at release/deploy automation because the repo has not yet earned production-style controls

That means the repo's current harness stack is not a governance failure overall. It is an uneven stack:

- some upper-layer doctrine is already unusually good
- some middle-layer boundary materialization is only partially formalized
- some lower-layer automation is deliberately absent for good reasons

The wrong response would be to flatten that unevenness into "just add repo-ops rules" or "just add CI." The right response is to close the handoff gaps in sequence.

## Answer to the original broader ask
The current harness stack is `partially sufficient` for the repo's present posture, but `insufficient if left unchanged` for the larger vision of long-horizon, future-aware, lower-supervision work.

Why `partially sufficient` now:

- the repo already has real doctrine in `LONG-ARC.md`
- the repo already has strong phase-local steering through discuss / research / plan
- the repo already has meaningful orchestration doctrine, narrow hook discipline, and explicit human-signoff boundaries
- the repo already has enough Git awareness to recover from mixed work and to treat artifact classes seriously

Why it is still `insufficient` as a durable broader stack unless it changes:

- Codex still lacks first-class task disposition and closure reporting
- GSD still does not carry doctrine cleanly through milestone, progress, transition, and completion workflows
- Git/repo-ops still lacks explicit one-branch-one-objective and same-checkout-versus-worktree rules
- CI/release/deployment still has almost no mechanical enforcement surface, even for narrow repo-integrity checks
- the stack still depends too much on expert memory to transfer responsibility cleanly between layers

So the direct answer to the broader ask is:

- do not replace the answer with only repo-ops recommendations
- do not jump straight to production automation
- strengthen `Codex + GSD + Git` now so the repo can behave rigorously while work is fluid
- add narrow repo-integrity CI next for the repo's current pre-runtime stage, then add branch/PR build-test CI as soon as executable code and a stable local verify contract exist
- keep release/deploy approval manual and human-visible until a real deploy surface exists, then layer automation under that approval posture rather than treating approval and automation as opposites

## What is already strong
- `Doctrine exists and is explicit.`
  - `LONG-ARC.md`, `PROJECT.md`, `ROADMAP.md`, `REQUIREMENTS.md`, and the AGENTS/governance docs already form a real doctrine surface rather than ambient lore.
- `Phase-level doctrine translation is already strong.`
  - `discuss-phase`, `CONTEXT.md`, `research-phase`, and `plan-phase` already preserve `canonical_refs`, `future_awareness`, and future-preservation thinking.
- `Codex launch discipline is meaningful.`
  - spawn classification, runtime verification, anti-recursive orchestration doctrine, and narrow hooks already exist.
- `The repo already has Git doctrine and recovery capacity.`
  - short-lived-branch guidance, archive-branch posture, bounded recovery commits, and worktree-capable workflows already exist.
- `Human signoff boundaries are correctly explicit.`
  - legal, branding, monetization, infra, hosting, and obligation-changing decisions remain human-owned.
- `The repo is already future-aware about deployment and obligation ladders.`
  - canon already distinguishes private-host capability, later hosted convenience, and broader public obligations instead of flattening them into one deploy story.

## What is weak or missing by layer

### Codex orchestration
- Exploratory and scope-shaping work is not yet operationally worker-first enough.
- Returned worker output still lacks a mandatory `accept / revise / park / reject` gate.
- There is no explicit `active substantive task` model.
- Launch auditability is stronger than closure auditability.
- `runtime-valid` and `artifact-delivered / dispositioned` are not yet separated clearly enough.
- Current autonomy posture still pulls against the repo's rigor bar on doctrine-sensitive work.

### Repo-local GSD lifecycle and long-arc carry-forward
- `LONG-ARC.md` is strong inside phase workflows but weak at:
  - `new-project`
  - `new-milestone`
  - `progress`
  - `transition`
  - `complete-milestone`
- generic `project` and `roadmap` templates do not treat durable doctrine as first-class
- lifecycle init plumbing does not expose doctrine metadata consistently
- current auto paths can bypass doctrine-sensitive review too easily
- `quick` and other speed paths still need clearer doctrine-sensitive boundaries

### Git / repo-operations
- policy and config remain internally inconsistent
- there is no explicit rule set for:
  - when same-checkout path-based work is acceptable
  - when a new branch is mandatory
  - when a separate worktree is mandatory
- parked work is not yet materialized as an explicit repo object by default
- branch-level diff review is not yet formalized as a standing control surface
- issue / PR / MR templates, branch-intent notes, and review-owner routing are not yet formalized as standing governance surfaces for future remote review flow
- docs/canon/audit-heavy work can still hide mixed objectives under "it is all in `.planning/`"

### CI / release / deployment
- there is still no `.github/` workflow surface
- there is still no canonical root-level local verify command
- there is still no build/test/package/deploy surface for the product
- there is still no release artifact shape, deploy runbook, or rollback note
- there is still no narrow merge-boundary repo-integrity CI even though that is now justified
- the current absence of automation should not be confused with a preferred long-term absence of manual approval plus automation at later deploy boundaries

### Cross-layer integration
- handoff rules between layers are still too implicit
- `LONG-ARC.md` still depends too much on human memory outside phase workflows
- task transition, merge readiness, and release readiness each require layered support, but the support chain is not yet explicit enough
- config defaults still advertise more permissive behavior than the doctrine and governance docs justify

## How `LONG-ARC.md` should integrate day-to-day across layers
- `Canon` should keep the doctrine itself.
  - `LONG-ARC.md` remains the durable doctrine file and should not be replaced by workflow lore, branch naming, or CI policy.
- `GSD` should translate doctrine into lifecycle-visible constraints.
  - milestone start, progress routing, transition, and completion should surface current posture, protected seams, explicit non-decisions, and reversal-sensitive boundaries.
- `Codex` should keep doctrine from being bypassed conversationally.
  - relevant doctrine must be named in launch specs and returned research must be dispositioned before it starts acting like accepted steering.
- `Git` should keep doctrine changes reviewable and reversible.
  - doctrine/canon changes should stay separately inspectable from unrelated implementation or cleanup where review timing differs.
- `CI` should later verify only the mechanical part.
  - required files, references, and delta artifacts can be checked; doctrine quality itself remains outside CI's authority.

## Near-term changes
These are the current-need changes. They are the most justified now, given actual repo maturity and current failure surfaces.

### 1. Close the Codex-layer task-boundary gap
- Make exploratory, ambiguity-heavy, and scope-shaping work worker-first by default.
- Add a mandatory disposition gate for every returned worker:
  - `accept`
  - `revise`
  - `park`
  - `reject`
- Require one declared active substantive task unless a persisted bundle explicitly defines parallel lanes.
- Persist launch bundles before workers launch, with:
  - requested runtime
  - effective runtime
  - owned output path
  - stop condition
- Treat `runtime-valid but output-missing` as blocked work, not acceptable ambiguity.

### 2. Patch GSD lifecycle carry-forward of doctrine
- Add `LONG-ARC`-aware steps to:
  - `new-milestone`
  - `progress`
  - `transition`
  - `complete-milestone`
- Add lifecycle init metadata such as:
  - `long_arc_exists`
  - `long_arc_path`
- Stop hardcoding doctrine-blind permissive behavior in lifecycle auto paths where possible.
- Clarify that doctrine-sensitive quick work should not use the bare no-discuss path by default.

### 3. Formalize repo-ops boundary rules now
- Adopt one-branch-one-objective as a standing rule.
- Treat `git diff <base>...HEAD` as a first-class review surface.
- Define when same-checkout work is acceptable versus when separate branch or worktree isolation is required.
- Treat parked work as an explicit repo boundary, not ambient dirty files.
- Require explicit disposition of subagent-returned work before merge-back is considered semantically accepted.
- When remote review flow becomes real, add branch-intent / issue / PR template conventions and review-owner routing as explicit handoff machinery rather than optional polish.

### 4. Align live config posture with the repo's stated rigor bar
- Revisit:
  - `workflow.auto_advance: true`
  - `mode: "yolo"`
  - `git.branching_strategy: "none"`
- Do not let safer behavior depend only on commentary discipline.
- Stage config changes with workflow and command support so the repo does not trade one silent bypass for another.

### 5. Add one narrow merge-boundary CI lane after the local verify contract is clear
- Define one canonical local verify entrypoint first.
- Then add narrow `repo-integrity` CI when remote PR flow is active:
  - required file/reference checks
  - selected planning/governance artifact integrity checks
  - mechanically checkable verification-surface claims
- Do not add auto-deploy or doctrine judgment here.
- Treat this as a current-stage claim only. Once runnable code exists, expand to branch/PR build-test CI earlier than deploy automation.

## Deferred but important changes
These matter, but they should not outrun the repo's current stage.

### Codex and status visibility
- a lightweight orchestration-status view that combines runtime state, artifact existence, and disposition state
- investigation of whether open child-thread reporting is a runtime bug, a polling gap, or a missing closeout convention
- possible first-class repo-local command support for recurring multi-lane audit bundles

### GSD lifecycle maturity
- a first-class optional durable-doctrine artifact type, not only repo-specific `LONG-ARC.md`
- milestone-level doctrine-delta reporting
- progress surfaces that report doctrine-grounding health, not just whether context exists

### Git/repo-ops maturity
- helper commands for transition gating, checkpointing, parking, and subagent disposition
- branch intent or PR body conventions for mergeable branches
- issue / PR templates and review-owner routing once remote review flow exists
- verified remote branch-protection posture rather than relying only on local doctrine
- formalized archive-branch rules when bulky retained corpora start dominating active branches

### CI / release / deployment maturity
- build/test CI once executable product code and a stable local verify path exist
- deploy-bundle smoke checks, secret-boundary documentation, and rollback notes once a private-host runtime surface exists
- stronger release approval, backup validation, migration gates, and environment promotion only when multiple environments/operators or real remote-host burden exist

## Escalation model by risk / blast radius / complexity

| Stage | Trigger | Primary control emphasis | Justified controls |
| --- | --- | --- | --- |
| `Stage 0: current repo posture` | planning-heavy repo, Phase 01 pre-rerun, solo + agent-heavy, no runnable product | upper-layer visibility and local boundary discipline | Codex disposition gates, GSD doctrine carry-forward patches, branch/worktree rules by convention, narrow repo-integrity CI only once PR flow is active |
| `Stage 1: first sustained implementation and parallel work` | real code verification exists, multiple write streams, growing diffs to base | stronger local boundary materialization plus merge-boundary checks | mandatory separate worktrees for parallel or parked write streams, branch protection and required status checks, build/test CI once local verify is stable |
| `Stage 2: first private-host deployable runtime used by real players` | operator flow exists and failures affect real game-night sessions | deploy-bundle correctness and operator safety | documented start/stop flow checks, deploy smoke tests, secret-boundary docs, rollback note, release checklist, stronger separation of deploy/runtime changes from canon/planning changes |
| `Stage 3: multiple environments, multiple operators, or frequent remote use` | staging/prod differ meaningfully, more than one operator, remote use becomes routine | promotion and recovery discipline | approval gates, backup/export validation, migration gates, post-deploy verification, tighter release approvals |
| `Stage 4: public or paid obligation profile` | public discovery, stronger uptime/moderation expectations, payment or guaranteed access | service-grade operational governance | stronger secret handling and scanning, incident/runbook discipline, auditable release provenance, explicit operational ownership boundaries |

The governing rule across these stages is:

- escalate controls when blast radius, reversibility cost, coordination complexity, or obligation profile rises
- do not escalate simply because the repo has existed longer

## How repo-operations fits into the larger stack
Repo-operations is the durable boundary layer in the middle of the stack.

It is not the first owner of every failure, and it is not the final owner of every control.

Its role is:

- to materialize the results of upper-layer judgment into reviewable and reversible objects
- to turn active work into:
  - one coherent branch objective
  - a separate worktree
  - a parked stream
  - an accepted merge boundary
- to keep canon, audit/history, archive/corpus, and implementation changes attributable and separable when review timing differs

What repo-ops should not try to do alone:

- decide whether exploratory work should have been delegated
- decide doctrine correctness
- substitute for lifecycle carry-forward of `LONG-ARC.md`
- pretend that a clean tree proves semantic closure
- pretend that CI can repair mixed local change sets after the fact

So repo-operations fits as:

- downstream of Codex and GSD judgment
- upstream of CI enforcement
- central to reviewability, rollback, and non-ambient parked work
- insufficient by itself if the upper-layer judgment and lifecycle inputs stay ambiguous

## Recommended implementation sequence
1. Land the Codex-layer active-task and returned-work disposition contract first.
   - This directly addresses the most recent failure pattern while work is still fluid.
2. Patch the GSD lifecycle gap around `LONG-ARC.md`.
   - This keeps doctrine from depending on memory outside phase workflows.
3. Formalize Git/repo-ops branch/worktree/parking rules.
   - This turns upper-layer judgment into durable review and rollback boundaries.
4. Align the live repo config with the repo's actual rigor bar.
   - Do this with workflow/command support, not as an isolated config-only gesture.
5. Define one canonical local verify entrypoint.
   - CI should consume a real local contract, not invent its own.
6. Add one narrow repo-integrity CI lane when remote PR flow is active.
   - This should reinforce merge-boundary truth, not replace local judgment.
7. Defer build/test/deploy automation until a runnable product and private-host runtime surface exist.
   - Then escalate by actual operator burden and obligation profile.

## What can close now
- `[e:c+r:i]` The broader answer is genuinely multi-layer. No single layer should become the catch-all harness ([05-cross-layer-integration-and-escalation-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/05-cross-layer-integration-and-escalation-audit.md:430), [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:5)).
- `[e:c+r:i]` The narrower orchestration audit was correct but incomplete; the broader audit shows that the main weakness is the handoff chain across layers ([04-converged-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-orchestration-framework-audit/04-converged-synthesis.md:183), [05-cross-layer-integration-and-escalation-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/05-cross-layer-integration-and-escalation-audit.md:430)).
- `[a:c+r:i+t]` The repo's highest-value immediate changes still belong mainly in `Codex + GSD + Git`, but the CI claim is now explicitly narrowed to the current pre-runtime stage rather than treated as a durable anti-CI posture ([05-cross-layer-integration-and-escalation-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/05-cross-layer-integration-and-escalation-audit.md:431), [08-external-comparative-governance-research.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/08-external-comparative-governance-research.md:143)).
- `[e:c+r:i]` `Repo-ops` is necessary but not sufficient. It is the durable boundary layer, not the whole governance story ([03-git-repo-operations-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/03-git-repo-operations-layer-audit.md:145), [05-cross-layer-integration-and-escalation-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/05-cross-layer-integration-and-escalation-audit.md:174)).
- `[e:c+r:i+d]` Issue / PR / MR templates, review-owner routing, and linked issue-to-review artifacts should be treated as governance surfaces once remote review flow exists, not as optional process polish ([08-external-comparative-governance-research.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/08-external-comparative-governance-research.md:94)).[^github-issue-pr-templates][^github-codeowners][^gitlab-flow]
- `[e:c+r:i+d]` Manual approval and automation should be distinguished. For later deploy boundaries, the healthy shape is automated mechanical checks plus explicit human approval where environment risk justifies it ([08-external-comparative-governance-research.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/08-external-comparative-governance-research.md:146)).[^github-deployment-reviews][^google-sre-release]
- `[e:c+r:i]` `LONG-ARC.md` should move through the stack as doctrine translation plus reviewable canon diffs, not as ambient memory and not as CI policy ([02-gsd-lifecycle-and-long-arc-layer-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/02-gsd-lifecycle-and-long-arc-layer-audit.md:192), [05-cross-layer-integration-and-escalation-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/05-cross-layer-integration-and-escalation-audit.md:433)).
- `[e:c+r:i+d]` Progressive enforcement is justified here only by blast radius, parallelism, environment count, operator burden, and obligation profile, not repo age alone ([05-cross-layer-integration-and-escalation-audit.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/05-cross-layer-integration-and-escalation-audit.md:434)).[^github-rulesets][^google-sre-release]

## What must stay open
- The exact packaging and placement of new disposition/status/doctrine-delta helpers
- The exact sequence for config hardening versus workflow patching
- The exact first canonical local verify command and later CI command set
- The first real deploy bundle, release unit, and rollback boundary
- The verified remote branch-protection state

## Sources
- `.planning/research/2026-04-15-multilayer-harness-governance-audit/00-launch-bundle-spec.md`
- `.planning/research/2026-04-15-multilayer-harness-governance-audit/01-codex-orchestration-layer-audit.md`
- `.planning/research/2026-04-15-multilayer-harness-governance-audit/02-gsd-lifecycle-and-long-arc-layer-audit.md`
- `.planning/research/2026-04-15-multilayer-harness-governance-audit/03-git-repo-operations-layer-audit.md`
- `.planning/research/2026-04-15-multilayer-harness-governance-audit/04-ci-release-and-deployment-layer-audit.md`
- `.planning/research/2026-04-15-multilayer-harness-governance-audit/05-cross-layer-integration-and-escalation-audit.md`
- `.planning/research/2026-04-15-multilayer-harness-governance-audit/08-external-comparative-governance-research.md`
- `.planning/research/2026-04-15-multilayer-harness-governance-audit/06-converged-synthesis-task-spec.md`
- `.planning/research/2026-04-15-orchestration-framework-audit/04-converged-synthesis.md`
- `AGENTS.md`
- `.planning/AGENTS.md`
- `WORKFLOW.md`
- `AI-GUARDRAILS.md`
- `ARTIFACT-GOVERNANCE.md`
- `.planning/PROJECT.md`
- `.planning/LONG-ARC.md`
- `.planning/ROADMAP.md`
- `.planning/REQUIREMENTS.md`
- `.planning/STATE.md`
- `.planning/knowledge/index.md`
- `.planning/knowledge/signals/prix-guesser/2026-04-15-dirty-task-transitions-mixed-worktree.md`
- `.planning/knowledge/signals/prix-guesser/2026-04-15-underdelegated-exploration-orchestrator-role-drift.md`

## External Works Cited

[^github-issue-pr-templates]: GitHub Docs, "About issue and pull request templates", https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/about-issue-and-pull-request-templates
[^github-codeowners]: GitHub Docs, "About code owners", https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners
[^github-rulesets]: GitHub Docs, "Available rules for rulesets", https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets
[^github-deployment-reviews]: GitHub Docs, "Review deployments", https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/review-deployments
[^google-sre-release]: Google SRE Book, "Release Engineering", https://sre.google/sre-book/release-engineering/
[^gitlab-flow]: GitLab Blog, "GitLab Flow", https://about.gitlab.com/blog/gitlab-flow-duo/
