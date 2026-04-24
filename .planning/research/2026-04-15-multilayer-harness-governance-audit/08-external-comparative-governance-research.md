# 08 External Comparative Governance Research

## Research frame
- Mode:
  - primary: `hypothesis testing`
  - secondary: `solution evaluation` where alternative governance shapes matter
- Question:
  - Which broader prescriptive claims from `06-converged-synthesis.md` are materially strengthened, qualified, or weakened by direct outside evidence?
- Scope:
  - test the broader governance recommendations in `06`
  - use direct external comparison on agentic-workflow structure, Git/review boundaries, CI/deploy staging, and explicit handoff practices
  - keep the repo's current-state diagnosis situated by the required canon and lane outputs
- Non-goals:
  - redo the multi-layer audit
  - reopen Prix Guesser product doctrine
  - choose a final runtime, deployment topology, or host identity
  - pretend official docs alone prove optimal governance
- Stop condition:
  - a reader can tell which `06` claims are now externally strengthened, which remain mainly repo-specific judgment, and whether `06` needs revision or only clearer source-basis labeling

## Motivating grounds
- This pass exists because `06` is already strong on repo-state diagnosis but materially weaker on broader external grounding for some prescriptive claims.
- The source-basis drift signal explicitly names the problem: the newer bundle stopped exposing whether support was internal-only, external-direct, or only externally traceable through prior artifacts.
- The practical question is therefore narrower than a full re-audit:
  - Which `06` recommendations survive comparative pressure?
  - Which should remain framed as repo-specific reasoned guidance?
  - Which need sharper qualification so internal support does not read like general best practice?

## Source strategy and exclusions
- Preferred external source classes:
  - official OpenAI/Codex docs and OpenAI's own Codex workflow writeup
  - official GitHub docs for branch protection, rulesets, issue/PR templates, CODEOWNERS, manual workflow runs, and deployment reviews
  - official Git docs for worktree mechanics relevant to parallel isolation
  - Google's SRE book for release-engineering, rollout, and explicit-handoff doctrine
  - official GitLab workflow writeups where they expose issue/MR/release-evidence process
- Exclusions:
  - SEO-style "best practice" blogs
  - generic AI productivity advice
  - non-analogous enterprise governance material with little operational detail
  - sources that only restate secondhand claims without a primary operational basis
- Comparison rule used in this pass:
  - capability docs count as direct evidence for what a layer is designed to enforce
  - they do not, by themselves, prove that every repo should enforce that mechanism immediately

## Path of inquiry
- Entry point:
  - `06` already argued for a multi-layer, risk-staged governance stack, but its broader prescriptions were still mostly internal/reasoned.
- Branches considered:
  - whether outside evidence mainly confirms the "explicit handoff" thesis
  - whether comparative evidence pushes more control downward into CI earlier than `06` suggests
  - whether external practice supports risk-based escalation over age/size heuristics
  - whether remote issue/PR/MR workflow surfaces are underweighted in `06`
- Branches pursued:
  - official agentic-workflow guidance
  - official Git/GitHub review and protection surfaces
  - release/deployment and incident-handling material from Google SRE
  - official GitLab workflow material where issues, merge requests, templates, and release evidence are part of the operating model
- Branches deferred or abandoned:
  - deep comparative study of large public AI-code repos as a separate lane
  - platform-specific deployment topology comparisons
  - generalized "what all AI-heavy repos should do" claims where analogy quality was weak
- Reframing that emerged:
  - the strongest external confirmation is not "use CI more" or "use CI less"
  - it is that mature workflows encode handoffs, reviewers, environments, and release boundaries explicitly, while fitting stronger controls to actual risk surfaces

## Claims under test from 06
1. Near-term controls should live mostly in `Codex + GSD + Git`.
2. CI should stay narrow for now and release/deploy should remain manual until a real runtime exists.
3. Stronger controls should escalate by risk, blast radius, parallelism, and environment complexity rather than repo age or size alone.
4. Long-horizon quality depends on explicit handoff contracts between layers.
5. The repo's strongest surface is doctrine definition plus phase-local translation, while its weakest surface is lifecycle carry-forward and boundary materialization.
6. Lower-layer automation should verify mechanical truth, not replace upper-layer judgment on doctrine or scope.

## External findings

### 1. Explicit task shaping and persistent repo context are strongly supported [e:c:d]
Direct evidence:
- OpenAI's Codex docs describe Codex as a background coding agent that can run tasks in parallel and turn results into PRs.[^openai-codex-cloud]
- OpenAI's own Codex writeup says Codex performs best on well-scoped tasks, works better when prompts are structured like GitHub issues, benefits from a task queue used as a lightweight backlog, and benefits from a persistent `AGENTS.md`.[^openai-codex-workflow]

Inference:
- This materially strengthens the upper-layer part of `06` that emphasizes explicit task framing, persistent operating context, and bounded delegation before lower-layer enforcement enters.
- It does not prove the exact repo-local split between `Codex` and `GSD`, but it does directly support the idea that agentic work needs workflow-visible structure before merge-time automation can help much.

### 2. Explicit workflow artifacts and review ownership are strongly supported [e:c:d]
Direct evidence:
- GitHub documents issue and pull-request templates as a way to customize and standardize the information contributors provide, including structured required fields in issue forms.[^github-issue-pr-templates] [^github-issue-forms]
- GitHub documents `CODEOWNERS` as an automatic review-routing surface and supports requiring code-owner approval before merge.[^github-codeowners]
- GitHub protected branches and rulesets enforce pull-request, review, status-check, deployment, and path/file restrictions at selected branches and tags.[^github-protected-branches] [^github-rulesets]
- GitLab's own workflow writeups describe issues as the place where links, information, and participants are gathered, with merge requests linked back to those issues; GitLab Flow also treats merge requests as the collaboration boundary where comments, reviews, and pipelines happen.[^gitlab-build-gitlab] [^gitlab-flow]

Inference:
- This strongly supports `06`'s claim that long-horizon quality depends on explicit handoff contracts rather than memory or culture alone.
- It also adds pressure `06` did not emphasize enough: issue/PR/MR templates, review-owner routing, and linked issue-to-merge artifacts are not optional niceties in mature workflow systems; they are first-class governance surfaces.

### 3. Risk-shaped escalation is strongly supported [e:c:d]
Direct evidence:
- Google's SRE book says deployment processes should fit the risk profile of the service, with materially different rollout patterns for pre-production, large user-facing services, and sensitive infrastructure.[^google-sre-release]
- GitHub rulesets let a repo target selected branches or tags and apply requirements such as pull requests, required reviews, required status checks, required deployments, code scanning, and file-path restrictions.[^github-rulesets]
- GitHub deployment environments allow required reviewers and explicit approve/reject decisions before a job proceeds.[^github-deployment-reviews]

Inference:
- This is the strongest external confirmation in the whole pass.
- `06` is well supported when it argues for stronger controls by blast radius, parallelism, environment count, and obligation profile rather than age/size alone.
- Outside evidence supports not only the principle, but also the specific idea of different control sets at different boundaries.

### 4. Parallelism-sensitive isolation is supported, but mainly as a mechanism claim [e:c:d]
Direct evidence:
- Official Git documentation describes `git worktree` as support for multiple working trees attached to the same repository, allowing more than one branch to be checked out at a time.[^git-worktree]
- The same docs explicitly describe creating a new worktree for a new topic branch or a throwaway experimental/testing worktree.[^git-worktree]

Inference:
- This supports the Git-lane recommendation that parallel or interruption-prone work should materialize as separate branches/worktrees rather than as one ambient mixed tree.
- The external evidence is strongest on mechanism availability and intended use, not on one universal threshold for when every repo must switch to worktrees.

### 5. CI/release/deploy staging is supported only in a narrower form than `06` sometimes implies [e:c:i+d]
Direct evidence:
- GitHub supports manual workflow runs via `workflow_dispatch`.[^github-workflow-dispatch]
- GitHub deployment environments support explicit approve/reject review before deployment jobs proceed.[^github-deployment-reviews]
- Google's SRE book treats reproducible, automated release processes as core to reliable running services and argues that teams should define release processes early rather than retrofit them later.[^google-sre-release]
- GitLab Flow assumes pipelines on feature-branch / merge-request updates and uses them to build, test, and verify changes before they merge.[^gitlab-flow]

Inference:
- External comparison supports a hybrid model:
  - strong automation for mechanical checks once a runnable software surface exists
  - manual approval where deployment or environment risk justifies it
- This supports the `release/deploy stays manual until a real runtime exists` part of `06`.
- It weakens any broader reading of `CI should stay narrow` beyond the current no-runtime stage. Comparative practice pushes CI/build/test checks earlier once executable code exists, even before a repo becomes large.

### 6. Lower layers as mechanical-verification layers are well supported, but not sufficient alone [e:c:d]
Direct evidence:
- GitHub's protected branches, rulesets, required status checks, required deployments, and required reviewers all operate on merge or environment boundaries.[^github-protected-branches] [^github-rulesets] [^github-deployment-reviews]
- GitLab Flow similarly places pipelines and verification on merge-request/branch boundaries.[^gitlab-flow]
- Google SRE incident guidance emphasizes live docs, explicit roles, and explicit handoffs in addition to tooling.[^google-sre-incidents]

Inference:
- This supports `06`'s split where lower layers verify mechanical truth while upper layers own contextual shaping and handoff intent.
- It also confirms that lower-layer automation cannot substitute for explicit task ownership and handoff state; external operational practice adds those artifacts rather than expecting automation to infer them.

## Pressure against 06
- `06` underweights issue/PR/MR templates and review-routing surfaces.
  - External workflow systems make these explicit, repository-resident handoff mechanisms first-class rather than incidental.
- `06` needs sharper wording on the CI claim.
  - External practice supports narrow CI only because the repo is still planning-heavy and pre-runtime.
  - Once there is executable code and a stable local verify path, comparative practice shifts toward early branch/MR CI, not prolonged CI minimalism.
- `06` should distinguish manual approval from lack of automation more clearly.
  - GitHub environments show that automated checks plus explicit deployment approval is a standard hybrid, not a contradiction.
- `06` is strongest where it speaks about this repo's current internal state; it is weaker where it sounds like a generally optimal theory of agentic-governance staging across repos.

## What survives strongly
- `Risk-shaped escalation over age-shaped escalation` [e:c:d]
  - This is directly strengthened by Google SRE and GitHub ruleset/environment design.
- `Explicit handoff artifacts beat ambient memory` [e:c:d]
  - OpenAI, GitHub, GitLab, and Google SRE all encode work via explicit task, review, issue, template, environment, or handoff artifacts.
- `Lower layers should verify mechanical truth rather than decide doctrine` [e:c:d]
  - Protected branches, required reviews, status checks, deployments, and release tooling all reinforce explicit boundaries; none of them solve doctrinal judgment on their own.
- `Release/deploy approval should stay explicit and human-visible for real environments` [e:c:d]
  - GitHub deployment reviews and Google SRE release policy both support this, though the exact form depends on runtime maturity.
- `The repo's internal diagnosis mostly survives` [e:c:i]
  - External comparison mostly confirms the direction of the weak-side diagnosis rather than overturning it ([06-converged-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/06-converged-synthesis.md:253), [06-converged-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/06-converged-synthesis.md:261)).

## What weakens or remains only repo-specific judgment
- `Near-term controls should live mostly in Codex + GSD + Git` [a:r:i+d]
  - External evidence supports the direction, but not the exact weighting. The exact "mostly" remains a repo-stage judgment tied to this repo's failure pattern and no-runtime posture.
- `CI should stay narrow for now` [a:r:i+d]
  - Valid as a current repo-stage prescription, not as a broader norm. Comparative practice pushes earlier CI once executable code and a stable local verify contract exist.
- `The repo's strongest surface is doctrine definition plus phase-local translation, and its weakest surface is lifecycle carry-forward and boundary materialization` [e:c:i]
  - This remains a strong internal diagnosis, but outside sources cannot directly validate that ranking for this repo ([06-converged-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/06-converged-synthesis.md:256), [06-converged-synthesis.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/06-converged-synthesis.md:258)).
- `Upper-layer controls alone are the main answer` [o:r:i+d]
  - External comparison does not support that flattening. The comparative evidence favors explicit upper-layer shaping plus explicit remote review/pipeline surfaces as soon as those boundaries are real.

## Source-basis and epistemic limits
- Marker note:
  - examples used here follow `.planning/AGENTS.md`, e.g. `[e:c:d]`, `[e:c:i+d]`, `[a:r:i+d]`, `[e:c:i]`
- This pass is strongest where external sources directly describe:
  - agent-task structuring
  - explicit review/handoff artifacts
  - branch/ruleset/deployment boundary controls
  - risk-shaped release and incident practice
- It is weaker where it would need a near-perfect analogue to:
  - a solo-developer, planning-heavy, multi-agent repo with no runnable app yet
- Official platform docs mostly prove:
  - what a mechanism is designed to do
  - where it sits in the workflow
- They do not automatically prove:
  - the best activation point for every repo
  - the optimal local weighting between orchestration, workflow, Git, and CI
- So the source-basis outcome is:
  - repo-state diagnosis from `06`: still mainly `internal/cited`
  - some broader governance principles: now materially `external-direct`
  - exact near-term staging for this repo: still partly `internal + external-direct` and reasoned

## Implication for whether 06 needs revision
- `06` does not need a full rewrite. It does need either a light revision or this artifact attached as an explicit supplement.
- Minimum needed change:
  - mark which conclusions are repo-internal diagnosis versus externally strengthened governance guidance
- Recommended substantive revisions:
  1. Split the CI/deploy claim into two parts:
     - `narrow CI is appropriate only while the repo is pre-runtime and lacks a stable local verify contract`
     - `manual deploy/release approval remains appropriate until a real deploy surface exists`
  2. Add issue/PR/MR templates, review-owner routing, and linked issue-to-review artifacts as underweighted handoff machinery.
  3. Keep the risk/blast-radius escalation model; that part is the most externally strengthened part of `06`.
  4. Keep the handoff-chain thesis, but state more plainly that lower-layer remote review/pipeline surfaces should become part of that chain as soon as there is real code and real PR flow.
- Bottom line:
  - `06` should be treated as `strong internal synthesis plus partially externally strengthened governance guidance`, not as a fully externally validated general theory.

## Sources

### Local grounding
- `/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/06-converged-synthesis.md`
- `/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/01-codex-orchestration-layer-audit.md`
- `/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/02-gsd-lifecycle-and-long-arc-layer-audit.md`
- `/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/03-git-repo-operations-layer-audit.md`
- `/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/04-ci-release-and-deployment-layer-audit.md`
- `/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-multilayer-harness-governance-audit/05-cross-layer-integration-and-escalation-audit.md`
- `/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-15-orchestration-framework-audit/04-converged-synthesis.md`
- `/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-12-game-modes-r1-exploratory-audit/00-governance/review-trail-framework.md`
- `/home/rookslog/workspace/projects/prix-guesser/.codex/skills/gsd-rigorous-research/references/method.md`
- `/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md`
- `/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md`
- `/home/rookslog/workspace/projects/prix-guesser/AI-GUARDRAILS.md`
- `/home/rookslog/workspace/projects/prix-guesser/.planning/LONG-ARC.md`
- `/home/rookslog/workspace/projects/prix-guesser/.planning/PROJECT.md`
- `/home/rookslog/workspace/projects/prix-guesser/.planning/ROADMAP.md`
- `/home/rookslog/workspace/projects/prix-guesser/.planning/STATE.md`
- `/home/rookslog/workspace/projects/prix-guesser/.planning/knowledge/signals/prix-guesser/2026-04-15-citation-source-basis-enforcement-drift.md`

## External Works Cited

[^openai-codex-cloud]: OpenAI Docs, "Codex cloud", https://developers.openai.com/codex/cloud
[^openai-codex-workflow]: OpenAI, "How OpenAI uses Codex", https://cdn.openai.com/pdf/6a2631dc-783e-479b-b1a4-af0cfbd38630/how-openai-uses-codex.pdf
[^github-protected-branches]: GitHub Docs, "About protected branches", https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches
[^github-rulesets]: GitHub Docs, "Available rules for rulesets", https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets
[^github-issue-pr-templates]: GitHub Docs, "About issue and pull request templates", https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/about-issue-and-pull-request-templates
[^github-issue-forms]: GitHub Docs, "Syntax for issue forms", https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-issue-forms
[^github-codeowners]: GitHub Docs, "About code owners", https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners
[^github-workflow-dispatch]: GitHub Docs, "Manually run a workflow", https://docs.github.com/en/actions/how-tos/manage-workflow-runs/manually-run-a-workflow
[^github-deployment-reviews]: GitHub Docs, "Review deployments", https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/review-deployments
[^git-worktree]: Git documentation, "`git-worktree`", https://git-scm.com/docs/git-worktree
[^google-sre-release]: Google SRE Book, "Release Engineering", https://sre.google/sre-book/release-engineering/
[^google-sre-incidents]: Google SRE Book, "Managing Incidents", https://sre.google/sre-book/managing-incidents/
[^gitlab-build-gitlab]: GitLab Blog, "How we use GitLab to build GitLab", https://about.gitlab.com/blog/how-we-use-gitlab-to-build-gitlab/
[^gitlab-flow]: GitLab Blog, "GitLab Flow", https://about.gitlab.com/blog/gitlab-flow-duo/
