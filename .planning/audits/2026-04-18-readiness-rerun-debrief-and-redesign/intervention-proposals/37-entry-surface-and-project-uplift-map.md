Date: 2026-04-21
Status: active map artifact

# Entry Surface And Project Uplift Map

## Purpose

- [g:r:i] This artifact maps the full entry-surface family opened in `36` so later uplift design can build from the real harness terrain rather than from a generic “improve onboarding” slogan.
- [g:r:i] The target is broader than first-run setup. The target is the whole family of moments where a project enters, re-enters, changes milestone, is bootstrapped from docs, is repaired, is updated, or is migrated into the repo-local harness posture.

## Framing

- [d:r:i] The current family contains a wider set of distinct jobs:
  - initial creation
  - milestone opening
  - docs bootstrap / docs merge
  - session re-entry and planning recovery
  - runtime / install refresh
  - structural or posture repair
  - migration across generations or runtimes
  - vanilla-project uplift into current repo-local posture
  - lightly aged project uplift with limited bespoke carry
  - aged-bespoke project uplift with selective refresh
  - cross-runtime posture uplift
  - upstream-template-drift uplift
  - mid-phase uplift when doctrine has moved during active execution
- [d:r:i] Several of these jobs already have specialist owners. The composition-layer uplift job still spreads across several surfaces and lacks one explicit owner.
- [d:r:i] This map therefore asks not only what each surface already carries, but also where ownership thins, where carry becomes scattered across multiple commands, and where a dedicated uplift workflow should later gather the work into one auditable path.

## Scenario Map

- [d:r:i] `Fresh greenfield repo`
  - current primary owner: `new-project`
- [d:r:i] `Greenfield repo with durable discovery corpus but no .planning/`
  - current primary owner: `new-project`
  - thinner edge: the `discovery/` to live-planning boundary still needs manual carry
- [d:r:i] `Brownfield repo with code but no .planning/`
  - current primary owner: `new-project`, with optional `map-codebase` detour first
- [d:r:i] `Existing project opening a new milestone`
  - current primary owner: `new-milestone`
- [d:r:i] `Docs-heavy repo bootstrapping or merging planning state`
  - current primary owner: `ingest-docs`
- [d:r:i] `Workspace / worktree entry`
  - current primary owners: `gsd-new-workspace`, `gsd-list-workspaces`, `gsd-remove-workspace`
- [d:r:i] `Phase-injection entry inside an existing milestone`
  - current primary owners: `gsd-add-phase`, `gsd-insert-phase`, `gsd-plan-milestone-gaps`
- [d:r:i] `Existing project returning after time away`
  - current primary owners: `resume-project` and `progress`
- [d:r:i] `Existing active phase whose doctrine posture has moved mid-stream`
  - current primary owners: no single explicit owner yet
  - strongest current adjacent carriers: phase `CONTEXT.md`, `progress`, `discuss-phase`
- [d:r:i] `Existing project with damaged or thin planning state`
  - current primary owner: `health`
- [d:r:i] `Existing project updating runtime install/version`
  - current primary owner: `update`
- [d:r:i] `Installer re-run / materialization refresh without broader project uplift`
  - current primary owner: `scripts/setup-portable-gsd.sh`
  - strongest supporting owner: `update`
- [d:r:i] `Project migrating from GSD2 back to .planning/`
  - current primary owner: `from-gsd2`
- [d:r:i] `Required-reading posture install`
  - current primary carrier: `mandatory-initial-read`
  - current owner for wider project install: no single explicit owner yet
- [d:r:i] `Claim-type / long-horizon / anti-threshold doctrine install on an existing project`
  - current primary carriers: root/planning `AGENTS.md`, `CLAIM-TYPES.md`, `LONG-ARC.md`
  - current owner for project-wide install: no single explicit owner yet
- [d:r:i] `Existing vanilla project that should inherit stronger repo-local doctrine, governing docs, long-horizon carry, and runtime posture`
  - current owner: no single explicit owner yet
- [d:r:i] `Existing lightly aged project whose current posture is thinner than current repo-local carry but whose bespoke local content is still limited`
  - current owner: no single explicit owner yet
- [d:r:i] `Existing aged-bespoke project that already has custom local carriers and needs selective rather than blanket refresh`
  - current owner: no single explicit owner yet
- [d:r:i] `Cross-runtime posture uplift`
  - current owner: no single explicit owner yet
- [d:r:i] `Upstream-template-drift uplift`
  - current owner: no single explicit owner yet
- [d:r:i] `Forensics / post-mortem entry`
  - current primary owner: `gsd-forensics`
- [d:r:i] `Archived-milestone re-entry`
  - current primary owners: milestone archive / summary surfaces
- [d:r:i] `Audit-subtree aging and companion-carrier refresh`
  - current owner: no single explicit owner yet

## Current Surface Map

### 1. `new-project`

- [e:c+i] `new-project` already owns a thick creation path: init checks, git/bootstrap decisions, brownfield codebase-map offer, config creation, prior spike/sketch discovery, project synthesis, requirements, roadmap, state initialization, and instruction-file generation. Sources: .codex/get-shit-done/workflows/new-project.md:57-67, .codex/get-shit-done/workflows/new-project.md:104-124, .codex/get-shit-done/workflows/new-project.md:212-231, .codex/get-shit-done/workflows/new-project.md:242-261, .codex/get-shit-done/workflows/new-project.md:332-436, .codex/get-shit-done/workflows/new-project.md:1046-1247, .codex/get-shit-done/workflows/new-project.md:1335-1368.
- [d:r:i] Its strongest carry is creation-time coherence: it can move from idea or brownfield discovery into `PROJECT.md`, `REQUIREMENTS.md`, `ROADMAP.md`, `STATE.md`, config, research, and runtime instruction file in one owned flow.
- [d:r:i] Its thinner edge for the current family is that it assumes the project is crossing into planning for the first time. It does not own “take an already-initialized vanilla project and bring it into stronger repo-local posture” as a separate governed action.

### 2. `new-milestone`

- [e:c+i] `new-milestone` already owns a thick existing-project entry: it loads `PROJECT.md`, `MILESTONES.md`, and `STATE.md`, scans planted seeds, refreshes milestone summary, keeps the evolution section alive, can archive old phase directories before numbering reset, optionally runs fresh milestone research, defines requirements, and roadmaps the next milestone. Sources: .codex/get-shit-done/workflows/new-milestone.md:30-33, .codex/get-shit-done/workflows/new-milestone.md:49-96, .codex/get-shit-done/workflows/new-milestone.md:153-172, .codex/get-shit-done/workflows/new-milestone.md:174-198, .codex/get-shit-done/workflows/new-milestone.md:218-231, .codex/get-shit-done/workflows/new-milestone.md:235-249, .codex/get-shit-done/workflows/new-milestone.md:350-377, .codex/get-shit-done/workflows/new-milestone.md:431-496.
- [d:r:i] Its strongest carry is milestone-shaped continuation plus seed resurfacing.
- [d:r:i] Its thinner edge is posture inheritance. It assumes the project already has a meaningful `PROJECT.md` / `STATE.md` / roadmap baseline. It can widen scope intelligently, but it does not own a deeper refresh of runtime posture, governing-doc stack, or repo-local doctrine when the existing project is older or thinner than the current harness.

### 3. `ingest-docs`

- [e:c+i] `ingest-docs` already owns docs bootstrap and docs merge: it auto-detects `new` vs `merge`, classifies mixed doc sets, writes intel and conflict reports, blocks on blockers, routes clean new-mode synthesis through `gsd-roadmapper`, and in merge mode plans requirement / decision / roadmap additions against existing `.planning/` state. Sources: .codex/get-shit-done/workflows/ingest-docs.md:48-77, .codex/get-shit-done/workflows/ingest-docs.md:128-149, .codex/get-shit-done/workflows/ingest-docs.md:173-199, .codex/get-shit-done/workflows/ingest-docs.md:205-230, .codex/get-shit-done/workflows/ingest-docs.md:238-258, .codex/get-shit-done/workflows/ingest-docs.md:268-277, .codex/get-shit-done/workflows/ingest-docs.md:287-310.
- [d:r:i] Its strongest carry is document-origin reconciliation with conflict gating.
- [d:r:i] Its thinner edge is repo-local uplift beyond document synthesis. It can build or merge planning state from docs, but it does not install a stronger governing-doc stack, does not refresh runtime/local doctrine, and does not own the “older project to stronger repo-local posture” move once the docs merge itself is complete.

### 4. `resume-project` / `gsd-resume-work`

- [e:c+i] `resume-project` already owns session re-entry and recovery: it can restore from `STATE.md`, reconstruct `STATE.md` when absent, detect `HANDOFF.json`, `.continue-here`, incomplete plans, interrupted agents, and route toward the next appropriate discuss / plan / execute step. Sources: .codex/get-shit-done/workflows/resume-project.md:19-31, .codex/get-shit-done/workflows/resume-project.md:36-58, .codex/get-shit-done/workflows/resume-project.md:62-111, .codex/get-shit-done/workflows/resume-project.md:156-192, .codex/get-shit-done/workflows/resume-project.md:227-316; .codex/skills/gsd-resume-work/SKILL.md:48-75.
- [d:r:i] Its strongest carry is context restoration and resumption routing.
- [d:r:i] Its thinner edge is posture uplift. It restores where the project is, but it does not ask whether the project’s runtime, governing docs, required-reading posture, or long-horizon carry should be refreshed before continuing.

### 5. `progress`

- [e:c+i] `progress` already owns situational awareness and next-step routing: it detects missing planning state, analyzes the roadmap/state snapshot, surfaces verification debt, distinguishes phase states, and routes to execution, discuss, plan, verify, audit, milestone close, or new milestone start. Sources: .codex/get-shit-done/workflows/progress.md:25-41, .codex/get-shit-done/workflows/progress.md:45-69, .codex/get-shit-done/workflows/progress.md:83-137, .codex/get-shit-done/workflows/progress.md:141-207, .codex/get-shit-done/workflows/progress.md:403-516.
- [d:r:i] Its strongest carry is routing the operator through current project state.
- [d:r:i] Its thinner edge is structural uplift detection. It knows whether a project is missing planning state or carries verification debt, but it does not currently own a richer “this project exists, but it still deserves repo-local harness uplift” branch.

### 6. `health`

- [e:c+i] `health` already owns structural planning validation and narrow repair: it can detect missing core files, invalid config, naming mismatch, invalid phase references, absent nyquist key, and stale task directories, and it can repair specific low-risk structural issues such as missing config or missing `STATE.md`. Sources: .codex/get-shit-done/workflows/health.md:25-38, .codex/get-shit-done/workflows/health.md:60-94, .codex/get-shit-done/workflows/health.md:123-159, .codex/get-shit-done/workflows/health.md:161-180.
- [d:r:i] Its strongest carry is integrity checking plus low-risk repair.
- [d:r:i] Its thinner edge is that it draws a hard boundary around deeper content/doctrine change. That is good for safety, but it means `health` cannot by itself carry a richer uplift path involving governing docs, required-reading posture, long-horizon installation, or doctrine refresh.

### 7. `update`

- [e:c+i] `update` already owns runtime/version posture: it detects local vs global install, resolves preferred runtime/config-dir, checks npm release state, warns about clean install boundaries, preserves custom files, runs the install, clears update cache, and points to local patch reapplication. Sources: .codex/get-shit-done/workflows/update.md:12-23, .codex/get-shit-done/workflows/update.md:76-116, .codex/get-shit-done/workflows/update.md:288-320, .codex/get-shit-done/workflows/update.md:353-368, .codex/get-shit-done/workflows/update.md:464-487, .codex/get-shit-done/workflows/update.md:558-567.
- [d:r:i] Its strongest carry is runtime-install truth and safe update execution.
- [d:r:i] Its thinner edge is project-level onboarding. It updates the harness install and protects user files, but it does not bring a repo’s governing docs, `.planning/` posture, seeds, long-horizon carry, or instruction surfaces into current local doctrine by itself.

### 8. `from-gsd2`

- [e:c+i] `from-gsd2` already owns hierarchy migration from `.gsd/` into `.planning/`, preserving slices/tasks as phases/plans and carrying completion state where possible. Sources: .codex/skills/gsd-from-gsd2/SKILL.md:48-82.
- [d:r:i] Its strongest carry is structural migration across generations.
- [d:r:i] Its thinner edge is that it stops at format migration. It does not then run a richer repo-local uplift pass over the migrated project.

### 9. Governing / Onboarding Carriers

- [e:c+i] `mandatory-initial-read` enforces `<required_reading>` when a workflow has already named files to load. Source: .codex/get-shit-done/references/mandatory-initial-read.md:1.
- [d:r:i] That makes it an important discipline carrier, but not an uplift owner. It does not decide what a vanilla or older project should newly inherit; it only ensures required files are read once they have already been named.
- [e:c+i] Root/planning `AGENTS.md`, thin `CLAUDE.md` wrappers, `.planning/CLAIM-TYPES.md`, and `.planning/LONG-ARC.md` already carry repo-local doctrine, claim notation, long-horizon posture, and anti-threshold framing. Sources: AGENTS.md:13-20, AGENTS.md:60-106, .planning/AGENTS.md:13-24, .planning/AGENTS.md:117-132.
- [d:r:i] These are not merely background reading. They are current posture carriers that many older or vanilla projects will not yet have inherited in their stronger form.
- [e:c+i] Repo-local tooling now also carries doctrine in executable form: `audit_refmap.py`, `scan_threshold_language.py`, `runtime_visibility.py`, `capture_launch_truth.py`, and `manifest_install_coherence.py` are named directly in root/planning guidance for audit, runtime, and request-surface discipline. Sources: AGENTS.md:149-152, .planning/AGENTS.md:44-74.
- [d:r:i] That means governing posture now has both document carriers and tooling carriers. A later uplift workflow should check both rather than treating onboarding as only a markdown-doc problem.
- [e:c+i] The repo-local `gsd-rigorous-research` skill is also a standing posture carrier for non-phase-bound research lanes. Source: AGENTS.md:44.

### 10. Adjacent Entry And Carrier Families

- [d:r:i] `Workspace / worktree entry`, `phase-injection entry`, `forensics entry`, and `archived-milestone re-entry` are real entry families even though they should stay specialist-owned rather than absorbed into a first uplift slice.
- [d:r:i] `Required-reading posture install`, `claim-type / long-horizon install`, `repo-local tooling install`, and `audit-subtree aging` are not standalone workflows today, but they already function as entry-sensitive posture families and should be treated as such in later uplift design.
- [d:r:i] The main current gain from naming them here is not to widen the first slice recklessly. It is to stop them from disappearing into a generic onboarding bucket.

## Interaction Map

- [d:r:i] `new-project` and `new-milestone` are the thickest creation/continuation surfaces.
- [d:r:i] `ingest-docs` is the thickest document-origin bridge.
- [d:r:i] `resume-project` and `progress` are the thickest situational/re-entry surfaces.
- [d:r:i] `health` is the thickest structural repair surface.
- [d:r:i] `update` is the thickest runtime-version surface.
- [d:r:i] `from-gsd2` is the thickest format migration surface.
- [d:r:i] `mandatory-initial-read`, root/planning `AGENTS.md`, `CLAUDE.md` wrappers, `CLAIM-TYPES.md`, `LONG-ARC.md`, and the repo-local tooling stack are the thickest governing/posture carriers.
- [d:r:i] None of these currently owns the full cross-surface move:
  - detect older/vanilla posture
  - check runtime/install state
  - check `.planning/` structural health
  - install or refresh repo-local governing docs, tooling, and instruction carriers
  - ensure required-reading and long-horizon carry are active
  - ensure claim-type and anti-threshold posture are active in load-bearing surfaces
  - output an explicit uplift disposition showing what was refreshed, what stayed local, and what still needs later work

## Where Carry Is Currently Scattered

### Governing-Doc Refresh

- [d:r:i] The current harness can generate an instruction file during `new-project`, and local audit work has its own onboarding companions, but there is no single follow-through path for refreshing root/planning `AGENTS.md`, thin `CLAUDE.md` wrappers, `.planning/CLAIM-TYPES.md`, `.planning/LONG-ARC.md`, or related governance documents on an already-existing project. Sources: .codex/get-shit-done/workflows/new-project.md:1247, .codex/get-shit-done/workflows/new-project.md:1346, AGENTS.md:92-106, .planning/AGENTS.md:16.

### Long-Horizon And Strengthening Carry Install

- [d:r:i] The strengthening family is now live in discuss/context/plan/research/seed surfaces, but there is no owned entry/uplift surface that checks whether an existing project has actually inherited those newer carriers before ordinary planning continues. Sources: intervention-proposals/32-strengthening-opportunity-first-slice-implementation.md:1, intervention-proposals/33-research-and-planner-strengthening-carry-follow-through.md:1.

### Vanilla-Project Uplift

- [d:r:i] An existing vanilla project can currently be updated, repaired, resumed, or progressed, but it still lacks one explicit route that says: detect thinner posture, refresh runtime/governing/planning carriers, and write a durable report of the uplift. This is the family’s clearest ownerless seam.

### Lightly Aged Project Uplift

- [d:r:i] A lightly aged project is not equivalent to a vanilla project. It may already carry some repo-local doctrine and planning posture, but not the newer carrier set now assumed by the repo. This family needs selective refresh, not blanket reinstall.

### Aged-Bespoke Uplift

- [d:r:i] A project that already carries custom local governance or planning doctrine can be stronger than vanilla and still drift from current repo-local posture. That refresh is different from vanilla uplift because the task is not first install, but selective refresh without flattening bespoke local value.

### Cross-Runtime Uplift

- [d:r:i] A project may have been initialized under one runtime and later used under another. The current surface family can update the runtime install and generate runtime-specific instruction files during first init, but it does not own later cross-runtime posture alignment.

### Upstream-Template-Drift Uplift

- [d:r:i] A project may be current on package version and still thinner than current shipped template posture. This is not the same problem as runtime update or structural health, and it needs its own seat in the uplift family rather than disappearing into generic “update”.

### Mid-Phase Uplift

- [d:r:i] A project can also need uplift while a phase is already active. That is its own interaction family, because the strongest carry surface is the live `CONTEXT.md` boundary and any resulting routing back into `discuss-phase` or `progress`, not a generic onboarding pass.

### Output Record

- [d:r:i] The current entry surfaces each produce their own local outputs (`PROJECT.md`, `STATE.md`, roadmap, conflicts, repair results, resume status), but there is no single uplift report surface that records the before/after of a project-wide repo-local refresh.
- [d:r:i] The stronger candidate carrier set is now visible:
  - `UPLIFT-REPORT.md`
  - uplift section inside `STATE.md`
  - a thin project doctrine manifest such as `UPLIFT-MANIFEST.json`
  - uplift-origin seed routing for what should be deferred rather than silently dropped

## Candidate Ownership Split For A Later Uplift Workflow

- [d:r:i] `new-project`, `new-milestone`, and `ingest-docs` should stay the primary owners of creation / milestone / docs merge.
- [d:r:i] `health` should stay the owner of low-risk structural repair.
- [d:r:i] `update` should stay the owner of runtime install/version change.
- [d:r:i] `progress` and `resume-project` should stay the owners of situational routing and session restoration.
- [d:r:i] A later uplift workflow should own the composition layer:
  - detect whether uplift is worth opening
  - gather runtime/install, planning-health, and governing-posture evidence
  - refresh repo-local carriers that belong together
  - install or refresh required-reading, claim-type, long-horizon, and anti-threshold posture where it thins
  - install or refresh the repo-local tooling carriers that current doctrine now assumes
  - write a durable uplift report, `STATE.md` uplift section, and thin doctrine manifest
  - route any remainder into later work instead of mutating silently
- [d:r:i] The first slice of that workflow should stay compact:
  - no full reinstall
  - no full migration
  - no cross-project batching
  - no workstream reconciliation
  - no audit-tree restructuring
  - no full upstream-template expression pass

## Current Consequence

- [d:r:i] The family terrain now carries the widened field directly rather than only through the raw Opus output.
- [d:r:i] This map now carries the four-way uplift split, the mid-phase uplift case, and the installer/materialization distinction directly rather than leaving them only in the cross-vendor lane output.
- [d:r:i] The next workflow pass should therefore use this revised terrain as the active local field map rather than the earlier narrower shape.
