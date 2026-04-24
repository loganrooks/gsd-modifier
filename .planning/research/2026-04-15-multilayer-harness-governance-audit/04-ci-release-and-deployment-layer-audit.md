# 04 CI, Release, And Deployment Layer Audit

## Research Frame
- Mode: `synthesis`
- Question:
  What CI, release, and deployment controls should this repo eventually adopt, and which of them are worth introducing now versus later, if the goal is to support a long-lived, agent-assisted, doctrine-sensitive project without pretending it is already a production service?
- Scope:
  - current repo governance and planning canon
  - current automation surface in this repo
  - prior repo-local findings about hosting, distribution, and orchestration
  - staged CI / release / deployment governance for this repo's actual maturity
- Non-goals:
  - designing a full production DevOps stack now
  - choosing the final room runtime or final hosting vendor
  - treating private-host, official-hosted convenience, provider-hosted, and unsupported private-operator futures as already decided
  - moving Git/task-boundary governance out of the adjacent Git lane
- Stop condition:
  - identify what this layer should do now
  - identify what should wait for actual runtime and hosting risk
  - make the boundary between automation and human judgment explicit

## Motivating grounds

This lane exists because the broader audit explicitly opened a fourth control surface beyond Codex, GSD, and Git:

- the user asked about proper DevOps, GitHub Actions, progressive enforcement, deployment posture, and how stronger controls should evolve as the repo grows
- the narrower orchestration audit explicitly deferred CI / release / deployment into a later governance layer rather than treating it as solved
- the repo already recognizes deployment and operator-flow questions as real product constraints through `DEPLOY-01` through `DEPLOY-05`, but the current workspace still has almost no actual CI / release / deployment machinery

Primary grounds:

- `.planning/research/2026-04-15-orchestration-framework-audit/04-converged-synthesis.md`
- `WORKFLOW.md`
- `AI-GUARDRAILS.md`
- `.planning/ROADMAP.md`
- `.planning/REQUIREMENTS.md`
- `.planning/audits/2026-04-08-pre-execution-review/lane-3-stakeholder-distribution.md`
- `.planning/research/2026-04-10-vision-hosting-wave/findings/02-hosting-transition.md`

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
- `.planning/knowledge/index.md`
- `.planning/research/2026-04-15-orchestration-framework-audit/03-guardrails-mechanisms-and-command-proposals.md`
- `.planning/research/2026-04-15-orchestration-framework-audit/04-converged-synthesis.md`
- `.planning/audits/2026-04-08-pre-execution-review/lane-3-stakeholder-distribution.md`
- `.planning/audits/2026-04-08-pre-execution-review/CONVERGENCE.md`
- `.planning/research/2026-04-10-vision-hosting-wave/findings/02-hosting-transition.md`
- `.planning/research/2026-04-10-vision-hosting-wave/findings/03-precedents-and-trajectories.md`
- `.codex/hooks.json`
- `scripts/setup-portable-gsd.sh`
- `.codex/get-shit-done/workflows/ship.md`
- `.codex/get-shit-done/bin/lib/verify.cjs`
- `README.md`

## Path Of Inquiry
- Entry point:
  The lane started from a mismatch: the repo's governance docs already talk about branch protection, status checks, rollback posture, deployment requirements, and operator-hosted play, but the actual repo surface is still mostly planning artifacts with no `.github/` workflows, no app manifest in the root, and no deployable runtime bundle.
- Branches considered:
  - current CI and GitHub Actions absence
  - verification and release controls that would already help now
  - deployment controls that should wait for an actual runtime
  - anti-hallucination and anti-shortcut checks that belong here versus in other layers
  - how this layer should interact with GSD and Codex rather than replacing them
- Branches pursued:
  - current automation surface and repo maturity
  - prior distribution/hosting findings because this repo already elevated deployment into product requirements
  - release-safety and rollback posture in proportion to private-hosted early stages
  - staged escalation thresholds by actual blast radius
- Branches deferred or abandoned:
  - enterprise-style CI/CD blueprints
  - full secrets/compliance/security automation design
  - final production hosting topology
- Unexpected branches / reframings:
  - the highest-value near-term CI for this repo is not app deployment CI; it is repo-integrity and verification-surface CI for a doctrine-heavy planning/codebase
  - the most important deployment question is still product-shaping and operator-flow shaping, not throughput or cloud scale
  - release governance here must avoid silently choosing a future host identity or public-obligation profile

## Assumptions Surfaced
- `[e:c:i]` The repo is still pre-execution and planning-heavy, not a functioning app with build/test/deploy pipelines ([README.md](/home/rookslog/workspace/projects/prix-guesser/README.md:62), [.planning/STATE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/STATE.md:5), [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:41), [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:12)).
  - Why it matters: the right immediate controls are narrower than a normal application repo's CI/CD stack.
  - Support: `README.md`, `.planning/STATE.md`, and the Phase 01 pre-rerun boundary in `AGENTS.md` and `WORKFLOW.md`.
- `[e:c:i]` Deployment and operator flow are real product constraints, not only later infra concerns ([.planning/REQUIREMENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/REQUIREMENTS.md:60), [.planning/ROADMAP.md](/home/rookslog/workspace/projects/prix-guesser/.planning/ROADMAP.md:84), [lane-3-stakeholder-distribution.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-08-pre-execution-review/lane-3-stakeholder-distribution.md:5)).
  - Why it matters: this lane cannot dismiss deployment until "after launch."
  - Support: `DEPLOY-01` through `DEPLOY-05` in `.planning/REQUIREMENTS.md`, Phase 3 through 5 posture in `.planning/ROADMAP.md`, and the 2026-04-08 distribution audit.
- `[a:c+r:i]` The repo will continue to prefer self-hostable authoritative rooms as the primary preserved branch for early hosted play ([.planning/LONG-ARC.md](/home/rookslog/workspace/projects/prix-guesser/.planning/LONG-ARC.md:118), [.planning/PROJECT.md](/home/rookslog/workspace/projects/prix-guesser/.planning/PROJECT.md:138)).
  - Why it matters: release/deploy controls should support private-host parity first.
  - What could weaken it: a later deliberate move to a public-managed-first runtime.
- `[e:c:i]` This repo explicitly does not want automation to replace doctrine-sensitive judgment ([AI-GUARDRAILS.md](/home/rookslog/workspace/projects/prix-guesser/AI-GUARDRAILS.md:15), [AI-GUARDRAILS.md](/home/rookslog/workspace/projects/prix-guesser/AI-GUARDRAILS.md:89), [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md:68), [.planning/LONG-ARC.md](/home/rookslog/workspace/projects/prix-guesser/.planning/LONG-ARC.md:177)).
  - Why it matters: CI here should verify claims and artifacts, not adjudicate canon or product direction.
  - Support: `AI-GUARDRAILS.md`, `WORKFLOW.md`, `.planning/AGENTS.md`, `.planning/LONG-ARC.md`.

## Evidence Base
### Direct evidence
- `[e:c+r:i]` There is currently no `.github/` workflow content in the repo. This is direct repo observation from 2026-04-15, consistent with the repo still presenting itself as planning-first rather than app-runtime-first ([README.md](/home/rookslog/workspace/projects/prix-guesser/README.md:62)).
- `[e:c+r:i]` The root repo has no application `package.json`, no lockfile, no Dockerfile, no `docker-compose.yml`, and no deploy manifest; the only root script is `scripts/setup-portable-gsd.sh`. This is direct repo observation from 2026-04-15 and matches the current planning-only posture described in [README.md](/home/rookslog/workspace/projects/prix-guesser/README.md:62).
- `[e:c:i]` `README.md` says this repo is currently "a browser-first project plan, not a finished app" ([README.md](/home/rookslog/workspace/projects/prix-guesser/README.md:62)).
- `[e:c:i]` `WORKFLOW.md` already recommends remote-host branch protection and status checks before merge, and names a "simple rollback posture" plus explicit secret handling as DevOps minimums before the project grows much further ([WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:77), [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:83), [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:123), [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:125), [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:126)).
- `[e:c:i]` `WORKFLOW.md` also says hooks are not the primary enforcement layer and should not substitute for branch protection, CI, or explicit review boundaries ([WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:117)).
- `[e:c:i]` `AI-GUARDRAILS.md` reserves infrastructure, hosting, and secrets-management changes for explicit human signoff ([AI-GUARDRAILS.md](/home/rookslog/workspace/projects/prix-guesser/AI-GUARDRAILS.md:15)).
- `[e:c:i]` `.planning/REQUIREMENTS.md` includes `DEPLOY-01` through `DEPLOY-05`, which already formalize operator start/stop flow, remote HTTPS/WebSocket ingress, and join/distribution concerns ([.planning/REQUIREMENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/REQUIREMENTS.md:60)).
- `[e:c:i]` `.planning/ROADMAP.md` ties deployment/access obligations directly to milestone work, especially Phase 3, Phase 4, and Phase 5 ([.planning/ROADMAP.md](/home/rookslog/workspace/projects/prix-guesser/.planning/ROADMAP.md:84), [.planning/ROADMAP.md](/home/rookslog/workspace/projects/prix-guesser/.planning/ROADMAP.md:109), [.planning/ROADMAP.md](/home/rookslog/workspace/projects/prix-guesser/.planning/ROADMAP.md:132), [.planning/ROADMAP.md](/home/rookslog/workspace/projects/prix-guesser/.planning/ROADMAP.md:154)).
- `[e:c:i]` `.codex/get-shit-done/workflows/ship.md` assumes a future where PRs merge "when CI passes," but the repo has no actual CI surface yet ([.codex/get-shit-done/workflows/ship.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/ship.md:39), [.codex/get-shit-done/workflows/ship.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/ship.md:213)).
- `[e:c:i]` `.codex/get-shit-done/bin/lib/verify.cjs` already contains repo-structure and artifact verification utilities that could later be surfaced as CI entrypoints ([.codex/get-shit-done/bin/lib/verify.cjs](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/bin/lib/verify.cjs:118), [.codex/get-shit-done/bin/lib/verify.cjs](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/bin/lib/verify.cjs:216), [.codex/get-shit-done/bin/lib/verify.cjs](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/bin/lib/verify.cjs:557)).
- `[e:c:i]` The 2026-04-08 stakeholder/distribution audit and convergence artifact both describe deployment/distribution as a critical gap and elevate `DEPLOY-*` requirements plus Docker/Compose-style operator flow as future needs ([lane-3-stakeholder-distribution.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-08-pre-execution-review/lane-3-stakeholder-distribution.md:5), [lane-3-stakeholder-distribution.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-08-pre-execution-review/lane-3-stakeholder-distribution.md:26), [CONVERGENCE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-08-pre-execution-review/CONVERGENCE.md:118)).
- `[e:c:i]` The 2026-04-10 hosting-transition research already treats the likely ladder as local/LAN -> private remote host -> small public hosted operation, with Cloudflare Tunnel or similar as a bridge and with actual operational breakpoints around HTTPS, WebSocket ingress, reconnect, and operator burden ([02-hosting-transition.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-10-vision-hosting-wave/findings/02-hosting-transition.md:58), [02-hosting-transition.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-10-vision-hosting-wave/findings/02-hosting-transition.md:68)).

### Inference and interpretation
- `[e:c+r:i]` The repo's near-term CI need is mostly structural and epistemic: catch broken references, missing required artifacts, or false claims of verification before merge ([README.md](/home/rookslog/workspace/projects/prix-guesser/README.md:62), [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:90), [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:105), [.codex/get-shit-done/bin/lib/verify.cjs](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/bin/lib/verify.cjs:216)).
- `[e:c+r:i]` Full deployment automation would currently be premature because there is nothing real to package, release, or promote across environments yet ([README.md](/home/rookslog/workspace/projects/prix-guesser/README.md:62), [.planning/STATE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/STATE.md:28), [.planning/ROADMAP.md](/home/rookslog/workspace/projects/prix-guesser/.planning/ROADMAP.md:84)).
- `[p:c+r:i]` Release safety for this repo should emerge in the same sequence as product-hosting maturity: first reproducible operator startup, then reversible private-host deployment, then environment separation, then stronger public-service controls if the project ever accepts that burden ([.planning/REQUIREMENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/REQUIREMENTS.md:60), [.planning/ROADMAP.md](/home/rookslog/workspace/projects/prix-guesser/.planning/ROADMAP.md:84), [02-hosting-transition.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-10-vision-hosting-wave/findings/02-hosting-transition.md:68)).
- `[e:c+r:i]` Anti-hallucination checks in this layer should focus on mechanically checkable claims such as "the deploy bundle exists," "the join/build/test entrypoint exists," or "the cited verification artifact exists," not on trying to decide whether the underlying product or doctrine choice is good ([AI-GUARDRAILS.md](/home/rookslog/workspace/projects/prix-guesser/AI-GUARDRAILS.md:89), [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md:132), [.codex/get-shit-done/bin/lib/verify.cjs](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/bin/lib/verify.cjs:289)).
- `[e:c+r:i]` CI should remain downstream of Codex/GSD/Git governance. It can reinforce explicit contracts, but it cannot repair underdelegation, bad task boundaries, or doctrine drift by itself ([WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:52), [2026-04-15-dirty-task-transitions-mixed-worktree.md](/home/rookslog/workspace/projects/prix-guesser/.planning/knowledge/signals/prix-guesser/2026-04-15-dirty-task-transitions-mixed-worktree.md:50), [2026-04-15-underdelegated-exploration-orchestrator-role-drift.md](/home/rookslog/workspace/projects/prix-guesser/.planning/knowledge/signals/prix-guesser/2026-04-15-underdelegated-exploration-orchestrator-role-drift.md:51)).

### Unknowns
- `[o:c:i]` The final room runtime, deploy topology, and packaging format are not chosen yet ([.planning/PROJECT.md](/home/rookslog/workspace/projects/prix-guesser/.planning/PROJECT.md:167), [.planning/ROADMAP.md](/home/rookslog/workspace/projects/prix-guesser/.planning/ROADMAP.md:106)).
- `[o:c:i]` The repo does not yet have an executable app surface, so exact test/build/deploy commands remain unknown ([README.md](/home/rookslog/workspace/projects/prix-guesser/README.md:62), [.planning/STATE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/STATE.md:28)).
- `[o:c:i]` The eventual publicness level and host-identity ladder remain deliberately unresolved in `.planning/LONG-ARC.md` ([.planning/LONG-ARC.md](/home/rookslog/workspace/projects/prix-guesser/.planning/LONG-ARC.md:101), [.planning/LONG-ARC.md](/home/rookslog/workspace/projects/prix-guesser/.planning/LONG-ARC.md:118)).
- `[o:c:i]` There is no current evidence for what the first practical rollback unit should be: git revision only, container image, database snapshot, content bundle version, or some combination ([WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:92), [02-hosting-transition.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-10-vision-hosting-wave/findings/02-hosting-transition.md:232)).

## Dependencies And Relations

| Item | Depends on | Constrains or affects | Vulnerability |
| --- | --- | --- | --- |
| Narrow CI now | a canonical local verify entrypoint, repo-structure checks worth enforcing | PR safety, planning-artifact integrity, trust in automated green checks | medium |
| First real release gate | executable app, reproducible build/test path, explicit packaging format | whether "ship" means merge only or actual deployable bundle | high |
| Private-host deployment posture | room runtime choice, HTTPS/WebSocket ingress path, operator-flow design | start/stop scripts, remote-host smoke tests, rollback design | high |
| Stronger environment promotion | more than one deploy environment, more than one operator, real hosted uptime expectations | staging/prod separation, approval gates, backup and migration controls | high |
| Doctrine-safe automation | explicit source-of-truth docs and review boundaries | prevents CI from being over-read as product or canon authority | medium |

## Current State And Gaps

### What is already strong
- The repo already treats deployment as part of the product surface rather than a post-hoc ops problem.
- The canon is explicit that browser-first guest access, private-host parity, and later hosted/public obligation are different layers.
- The repo already rejects hooks-as-magic and already reserves infra/hosting decisions for explicit human signoff.
- The GSD surface already contains verification and shipping concepts that can later be connected to CI rather than replaced by it.

### What is currently weak or missing
- No GitHub Actions or equivalent CI workflows exist.
- No single root-level "verify the repo/app" command exists yet.
- No build, test, package, or deploy entrypoints exist for the product itself.
- No release artifact shape exists yet: no container image, compose file, binary, bundle manifest, or tagged release process.
- No deployment runbook exists for local/LAN, private remote host, or "hosted only when we want to play."
- No environment separation exists because no environment surface exists yet.
- No secret-loading contract, backup/export posture, or rollback procedure exists beyond high-level governance language.

## Near-Term Recommended CI, Release, And Deployment Controls

### 1. Add one narrow `repo-integrity` CI workflow once remote PR flow is active
- Purpose: catch broken references, missing required planning files, malformed governance artifacts, and false "this is verified" claims that are mechanically checkable.
- Best fit now:
  - markdown/link/path validation for local file references in canonical docs
  - existence checks for required repo-governance files
  - selected `.planning/` artifact integrity checks using existing `verify.cjs`-style primitives
- Why now:
  - the repo is currently more vulnerable to broken doc/process surfaces than to broken app deploys
  - this is the one CI lane that matches actual repo maturity today

### 2. Define one canonical local verification entrypoint before broad CI expansion
- CI should not invent its own check set.
- The repo should converge on one documented local command that future CI runs verbatim.
- Near-term scope for that command should stay narrow: repo structure, references, and any minimal validation that actually exists.

### 3. Keep release and deploy actions manual, explicit, and human-approved for now
- No auto-deploy on merge.
- No "green CI means publish" rule.
- No scheduled release automation.
- For the current maturity, release safety should mean:
  - explicit branch/PR boundary
  - explicit verification artifact
  - explicit human decision to merge or publish later

### 4. Treat deployment-readiness as a phase deliverable, not as ambient infrastructure work
- Phase 3 through 5 should own the first real operator-flow and private-host deploy surface.
- CI can later enforce that those deliverables exist once the roadmap phase earns them.
- Until then, the right posture is "deployment obligations are planned," not "deployment pipeline should already exist."

### 5. Add only lightweight anti-shortcut checks in this layer
- Good fit for CI:
  - claimed files exist
  - required docs or manifests exist
  - known verification entrypoints succeed
- Bad fit for CI:
  - trying to judge whether a doctrine-sensitive planning choice is wise
  - trying to infer that a release is socially or legally safe because checks are green

## Later-Stage Recommended Controls

These become justified only when the repo crosses from planning-heavy into runnable and then hosted software.

### When first executable product code exists
- required install/build/test checks on PRs
- lockfile and toolchain consistency checks
- smoke validation that the documented local bootstrap path actually works
- failure on broken test/build status before merge to protected branches

### When first private-host deploy bundle exists
- smoke test of the documented operator start/stop flow
- validation that join URL / QR generation works in the intended deployment mode
- explicit `.env.example` or equivalent secret-boundary documentation
- manual release checklist tied to one reproducible deploy unit
- rollback note defining the first safe reversal path

### When real remote-host use by friends becomes normal
- packaging verification for the chosen runtime bundle
- backup/export path for durable content and any state that matters
- post-deploy smoke checks for the live room flow
- deploy logs or minimal observability sufficient to diagnose failed game-night sessions

### When multiple environments or broader service obligations exist
- staging vs production separation
- approval gate before production deploy
- migration guardrails and rollback rehearsals
- periodic backup validation, not only backup creation
- status/incident communication posture if the repo accepts ongoing service expectations

### When public discovery, payment, or stronger support promises exist
- stronger secret handling and scanning
- auditable release notes and change provenance
- tighter deployment approvals and operational runbooks
- more formal observability and incident response

## Escalation Thresholds For Stronger Automation

1. `Threshold 0: planning-heavy repo, no runnable product`
   - Keep automation narrow and structural.
   - Valuable now: repo-integrity CI, explicit verify entrypoint, protected-branch/status-check posture when remote PR flow is active.

2. `Threshold 1: runnable app with repeatable local verification`
   - Add required build/test checks.
   - Still keep deployment manual.

3. `Threshold 2: first trusted private-host deployment used by real players`
   - Add deploy-bundle smoke tests, secret-boundary docs, start/stop validation, and rollback notes.
   - Release remains human-triggered.

4. `Threshold 3: more than one environment, more than one operator, or frequent remote use`
   - Add promotion rules, backup validation, migration gates, and stronger post-deploy verification.

5. `Threshold 4: public or paid obligation profile`
   - Add service-grade release governance, operational visibility, and incident discipline.
   - This is a product-obligation transition, not just a repo-size transition.

## How This Layer Should Interact With Git, GSD, And Codex
- Git discipline should define the reviewable change set and merge boundary first; CI should validate the resulting branch state, not substitute for task-boundary or concern-bucket discipline.
- GSD should remain the place where verification artifacts, plan status, and shipping intent are produced; CI should consume those artifacts once they exist instead of creating a second shadow workflow.
- Codex and subagents should still own bounded research, implementation, and verification work; CI should not be asked to disposition whether a worker result is `accept`, `revise`, or `park`.
- Doctrine-sensitive planning changes should continue to rely on explicit human review and source-of-truth docs; CI can check for missing references or malformed structure, but not for correctness of the doctrine itself.
- Release automation should sit after those layers, as a final reproducibility and safety check, not as the primary source of project judgment.

## What automation should not pretend to decide
- Whether a change to `PROJECT.md`, `LONG-ARC.md`, `ROADMAP.md`, or requirements is doctrinally sound.
- Whether a later wrapper, visibility state, or host identity has been safely narrowed.
- Whether a green check means the product is actually watchable, legible at couch distance, or socially fun.
- Whether public-hosted convenience, provider-hosting, or unsupported private-host operation has become the preferred future.
- Whether a release is legally safe, branding-safe, or support-obligation-safe.
- Whether a successful private-host deploy implies the repo should accept stronger uptime or moderation promises.

## What should never be left only to CI
- Infrastructure, hosting, or secrets-management decisions that change the repo's obligation profile.
- Canon changes that materially alter project scope or long-arc doctrine.
- Release approval for a first deploy surface or a materially changed operator flow.
- Data/content migrations that would make rollback expensive.
- Human assessment that rollback is actually acceptable for the current host and player context.
- Any decision that changes who is allowed to host, who is supported, or what service level is being implicitly promised.

## Scope Expansions And Deferrals
- Defer final deployment topology choice until the room-runtime and operator-flow work is real.
- Defer environment-promotion automation until more than one environment actually exists.
- Defer public-service DevOps controls until the project accepts public-service obligations.
- Follow-and-mark:
  - CI should eventually consume GSD verification outputs and deploy/runbook artifacts once those exist, rather than inventing parallel truth surfaces.

## What Can Close Now
- `[e:c+r:i]` The repo does need a CI/release/deployment governance lane; it is not premature as a research question ([.planning/REQUIREMENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/REQUIREMENTS.md:60), [.planning/ROADMAP.md](/home/rookslog/workspace/projects/prix-guesser/.planning/ROADMAP.md:84), [lane-3-stakeholder-distribution.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-08-pre-execution-review/lane-3-stakeholder-distribution.md:5)).
- `[e:c+r:i]` The most useful immediate CI for this repo is narrow repo-integrity and verification-surface enforcement, not auto-deploy ([WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:90), [WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:105), [.codex/get-shit-done/bin/lib/verify.cjs](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/bin/lib/verify.cjs:216), [README.md](/home/rookslog/workspace/projects/prix-guesser/README.md:62)).
- `[e:c+r:i]` Release and deployment should remain manual and human-approved until the project has a real runtime and real operator flow ([AI-GUARDRAILS.md](/home/rookslog/workspace/projects/prix-guesser/AI-GUARDRAILS.md:15), [.planning/ROADMAP.md](/home/rookslog/workspace/projects/prix-guesser/.planning/ROADMAP.md:84), [02-hosting-transition.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-10-vision-hosting-wave/findings/02-hosting-transition.md:232)).
- `[e:c+r:i]` Progressive enforcement is justified here, but only by blast radius, environment count, operator count, and obligation level, not by repo age alone ([WORKFLOW.md](/home/rookslog/workspace/projects/prix-guesser/WORKFLOW.md:121), [.planning/LONG-ARC.md](/home/rookslog/workspace/projects/prix-guesser/.planning/LONG-ARC.md:89), [02-hosting-transition.md](/home/rookslog/workspace/projects/prix-guesser/.planning/research/2026-04-10-vision-hosting-wave/findings/02-hosting-transition.md:68)).
- `[e:c+r:i]` Anti-hallucination enforcement in this layer should be mechanical and bounded: existence, traceability, reproducibility, and declared entrypoints ([AI-GUARDRAILS.md](/home/rookslog/workspace/projects/prix-guesser/AI-GUARDRAILS.md:89), [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md:132), [.codex/get-shit-done/bin/lib/verify.cjs](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/bin/lib/verify.cjs:289)).

## What Must Stay Open
- The eventual package/deploy unit: compose bundle, service script, image, or some other form.
- The first real rollback unit and backup boundary.
- The exact CI surface once executable code exists.
- The exact relationship between private-host parity, later hosted convenience, and any future public or paid surface.

## How This Layer Should Support Long-Horizon Project Quality
- It should make claims harder to fake, not decisions easier to fake.
- It should reinforce explicit source-of-truth artifacts and verification contracts already established in the repo.
- It should preserve the long-arc distinction between private-host capability, later hosted convenience, and broader public obligation rather than collapsing them into one `deploy` story.
- It should stage stronger controls only when the project has actually earned stronger operational burden.
- It should keep merge, release, and deploy boundaries inspectable enough that later growth does not depend on hidden operator memory.

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
- `.planning/knowledge/index.md`
- `.planning/research/2026-04-15-orchestration-framework-audit/03-guardrails-mechanisms-and-command-proposals.md`
- `.planning/research/2026-04-15-orchestration-framework-audit/04-converged-synthesis.md`
- `.planning/audits/2026-04-08-pre-execution-review/lane-3-stakeholder-distribution.md`
- `.planning/audits/2026-04-08-pre-execution-review/CONVERGENCE.md`
- `.planning/research/2026-04-10-vision-hosting-wave/findings/02-hosting-transition.md`
- `.planning/research/2026-04-10-vision-hosting-wave/findings/03-precedents-and-trajectories.md`
- `.codex/hooks.json`
- `scripts/setup-portable-gsd.sh`
- `.codex/get-shit-done/workflows/ship.md`
- `.codex/get-shit-done/bin/lib/verify.cjs`
- `README.md`
