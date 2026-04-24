Date: 2026-04-21
Status: lane-01 widening output (opus47-max-r1)

# Entry Surface And Project Uplift Field Mapping — Opus 4.7 Max R1

## Purpose

- [g:r:i] This output widens the local scaffold laid down in `37-entry-surface-and-project-uplift-map.md` so a later project-uplift workflow can inherit the full entry-surface field rather than a top-few ranking.
- [g:r:i] The task is not to confirm or refuse the local map. The task is to expose what the local map already carries strongly, where its naming still compresses distinct jobs, what surfaces or scenarios it leaves outside, how the surfaces propagate into each other, and where a dedicated uplift workflow opens stronger carry that the current surface set leaves scattered.
- [g:r:i] The project-uplift question is kept bounded to repo-local harness, runtime, planning, and governing carry. Broader operational families (workstream reconciliation, post-mortem, audit-subtree aging) are named where they touch the entry field but are routed out of the first uplift slice.

## 1. What The Current Map Already Exposes Strongly

- [e:c+i] The scenario map in `37` already carries nine distinct jobs as first-class entries, routes each to a current primary owner, and keeps the ninth (existing vanilla or older GSD project that should inherit stronger repo-local doctrine) visible as ownerless rather than silently folded into `update` or `health`. Source: `.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/37-entry-surface-and-project-uplift-map.md:24-42`.
- [e:c+i] The per-surface passages give each owner two layers explicitly: a strongest-carry line naming what the surface holds well, and a thinner-edge line naming where its carry does not reach for the uplift family. That two-layer framing already refuses the single-sentence threshold summary style and opens the stronger question of ownership shape. Source: `.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/37-entry-surface-and-project-uplift-map.md:46-92`.
- [e:c+i] The governing/onboarding-carriers section already separates `mandatory-initial-read` as a discipline carrier from its use as an uplift owner, which opens room for later carriers (claim-type convention, anti-threshold posture, long-horizon doctrine) to land alongside it without being collapsed into it. Source: `.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/37-entry-surface-and-project-uplift-map.md:94-97`.
- [e:c+i] The "Where Carry Is Currently Scattered" section already splits four distinct seams (governing-doc refresh, long-horizon/strengthening install, vanilla-project uplift, uplift output record) rather than naming one generic "we need an uplift workflow" catch-all. That split is the map's strongest first handle for a later workflow design. Source: `.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/37-entry-surface-and-project-uplift-map.md:115-131`.
- [e:c+i] The candidate ownership split in `37` already names what each existing surface should keep and what a later uplift workflow should newly compose, so the later workflow inherits a positive division of labor rather than an undifferentiated "absorb everything else" mandate. Source: `.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/37-entry-surface-and-project-uplift-map.md:133-144`.
- [e:c+i] The parent plan in `36` already opens the family with creation / milestone / docs-ingest as primary entries and `health` / `progress` / `resume-project` / `update` / `from-gsd2` as uplift/continuity surfaces — so the uplift question starts from a layered surface set rather than a flat onboarding label. Source: `.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/36-initialization-onboarding-and-project-uplift-strengthening-plan.md:33-56`.
- [e:c+i] The harness-intervention companion set already ties the entry field to declared-vs-effective authority, a composed materialization chain, and a goal-to-surface routing index, so uplift planning can route intent to real authority seams rather than treating every entry surface as flat documentation. Sources: `.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/governance/RUNTIME-MATERIALIZATION-AND-AUTHORITY.md:50-62`, `.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/indexes/GOAL-TO-SURFACE-INTERVENTION-INDEX.md:20-30`.

## 2. Missing Surfaces Or Scenario Families

The current map carries nine scenarios and eight surface families. The following surfaces or scenarios materially affect the uplift field and open stronger carry when named.

### 2a. Workspace And Worktree Entry Surfaces

- [e:c+i] `gsd-new-workspace`, `gsd-list-workspaces`, and `gsd-remove-workspace` are live skills in this repo. Source: listing at `.codex/skills/`.
- [d:r:i] These create a distinct entry family: isolated parallel workstreams each with their own `.planning/` tree. They behave like `new-project` in miniature but inherit posture from the parent repo at clone time; that clone boundary is its own uplift seam because the child workstream can then drift from the parent without a current surface owning the reconciliation.
- [d:r:i] The map in `37` does not carry workspace/worktree as a scenario, but any later uplift workflow run inside a workstream has to know whether it is uplifting the workspace or routing the uplift back to the parent repo.

### 2b. Phase-Injection Entry Surfaces

- [e:c+i] `gsd-add-phase`, `gsd-insert-phase`, `gsd-remove-phase`, and `gsd-plan-milestone-gaps` are live skills for mid-milestone scope entry rather than new-project or new-milestone boundaries. Source: listing at `.codex/skills/`.
- [d:r:i] These are entry-shaped moves because they bring new phase objects into an already-shaped milestone, but they sit outside the nine scenarios in `37`. A later uplift workflow has to decide whether newly inserted phases inherit current doctrine or older posture captured when the milestone was first roadmapped.

### 2c. Installer As Its Own Entry Surface

- [e:c+i] `scripts/setup-portable-gsd.sh` composes three mutation layers (upstream install, overlay copy, post-copy rewrite). Sources: `.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/governance/RUNTIME-MATERIALIZATION-AND-AUTHORITY.md:23-36`, `scripts/setup-portable-gsd.sh:20`, `scripts/setup-portable-gsd.sh:23`, `scripts/setup-portable-gsd.sh:46`.
- [d:r:i] The map in `37` routes runtime entry only through `update`, but re-running the installer is itself an entry event: it re-materializes `.codex/`, replaces live files, and can surface drift the project has carried locally. Uplift detection should be able to ask "when was the installer last run against this live state" rather than conflating installer execution with `$gsd-update`.

### 2d. Upstream Template / Contract Drift Entry

- [e:c+i] Checkpoint 5 recorded that important behavior can drift into live `.codex/` workflow / reference / helper surfaces beyond the tracked overlay. Source: `.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/harness-interventions/HARNESS-INTERVENTION-ONBOARDING.md:16`.
- [d:r:i] Upstream template / shared-contract drift is its own entry class: the package version may be current, live `.codex/` may still be aligned with overlay, and yet a newly shipped workflow (`spec-phase`, `ingest-docs`) may not yet be expressed in the project's own audit, phase, or governing surfaces. `update` and `health` both miss this because they do not compare repo-local posture to current runtime capability; they compare install state to package state. An uplift workflow opens stronger carry by routing this gap explicitly.

### 2e. Required-Reading Posture Install

- [e:c+i] `mandatory-initial-read.md` activates `<required_reading>` only when a prompt already lists files. Source: `.codex/get-shit-done/references/mandatory-initial-read.md:1`.
- [d:r:i] The harness ships the protocol but does not install the practice of adding `<required_reading>` blocks to the project's own spec / prompt / packet surfaces. The current repo does this by hand inside audit lanes. Uplift should know whether a project carries the practice and open a path to install it where it thins.

### 2f. Discovery-Seed / `discovery/` Boundary

- [e:c+i] Root `AGENTS.md` points operators to `discovery/14-gsd-seed.md` when `.planning/` is absent, and treats `discovery/` as upstream context rather than live operational state. Sources: `AGENTS.md:21-29`, `AGENTS.md:42`.
- [d:r:i] `new-project --auto` consumes a specific seed document, but the broader `discovery/` subtree is a durable pre-planning corpus whose uplift relationship (what gets lifted into `.planning/`, what stays as upstream context, how it ages) is scattered rather than owned by one surface. This matters for brownfield uplift in repos that carry a long discovery trail before `.planning/` exists.

### 2g. Claim-Type Convention And Anti-Threshold Posture Install

- [e:c+i] Root `AGENTS.md` defines the `[type:support:basis]` claim notation and the anti-threshold language posture; `.planning/AGENTS.md` adds the scanning tool and the planning-side anti-threshold discipline. Sources: `AGENTS.md:92-106`, `.planning/AGENTS.md:117-132`.
- [d:r:i] These are repo-local doctrine carriers that a fresh `new-project` run does not install. A vanilla project that gets "uplifted" without them will continue to produce load-bearing artifacts without claim typing or anti-threshold pressure, which is the main posture gap the harness-intervention audit was opened to address. Uplift opens stronger carry by bringing them into alignment deliberately.

### 2h. `LONG-ARC.md` Install / Resurface

- [e:c+i] `.planning/AGENTS.md` names `LONG-ARC.md` as part of the primary planning canon. Source: `.planning/AGENTS.md:16`.
- [d:r:i] Neither `new-project` nor `new-milestone` mentions `LONG-ARC.md` today. It is a repo-local carrier that projects pick up only when an operator or audit adds it. Uplift should check whether a project already carries long-horizon doctrine distinct from `ROADMAP.md` and, when it thins there, seed the file with a durable future-horizon section.

### 2i. Phase-Boundary / Pre-Rerun Recovery

- [e:c+i] Root `AGENTS.md` and `.planning/AGENTS.md` both explicitly carry the rule that Phase 01 is at a pre-rerun boundary and older `01-*` artifacts are not execution-approved. Sources: `AGENTS.md:43`, `.planning/AGENTS.md:208-213`.
- [d:r:i] `progress`, `resume-project`, and `health` do not model pre-rerun boundaries at all. A project that crosses doctrine versions mid-phase needs an entry surface that says "this phase requires a fresh discuss + planning pass before execution" rather than silently resuming against older artifacts. Uplift opens the natural owner for this signal, since rerun boundaries are usually created by doctrine moves that an uplift pass already touched.

### 2j. Audit-Subtree And Companion-Carrier Aging

- [e:c+i] `.planning/AGENTS.md` keeps `canon`, `phase work`, `audit trail`, `exploration`, and `generated corpus` as distinct artifact classes. Source: `.planning/AGENTS.md:33-40`.
- [d:r:i] Large audit workspaces (e.g., the `2026-04-18-readiness-rerun-debrief-and-redesign/` tree) become durable companion carriers whose uplift is unlike phase-work or canon uplift: they age, they reference live runtime surfaces, they spawn onboarding artifacts of their own. The map in `37` does not name this as a surface; the later uplift workflow should know whether an audit tree is currently active, durable, or a candidate for tombstone.

### 2k. Steering-Brief (`CONTEXT.md`) Refresh

- [e:c+i] `CONTEXT.md` files are steering briefs written during `discuss-phase` and carried through planning. Source: `AGENTS.md:45`.
- [d:r:i] No current surface owns mid-phase steering-brief refresh when doctrine, posture, or scope shifts during execution. This interacts with uplift because doctrine uplift during an active phase raises the question of whether the phase's `CONTEXT.md` still steers correctly. Uplift should route this seam to `discuss-phase` follow-up rather than silently invalidate in-progress steering.

### 2l. Forensics / Post-Mortem Entry

- [e:c+i] `gsd-forensics` is a live skill in this repo. Source: listing at `.codex/skills/`.
- [d:r:i] Post-mortem / forensic entry is its own scenario: the project state is coherent on paper, execution failed, and the operator needs a structured way back in that is neither `resume-project` nor `health`. `37` does not name it. Uplift should be aware of it because a forensics finding can trigger uplift when the failure points at doctrine drift rather than code bugs.

### 2m. Archived Milestone Re-Entry

- [e:c+i] `gsd-cleanup`, `gsd-complete-milestone`, and `gsd-milestone-summary` handle outbound archival and summarization. Source: listing at `.codex/skills/`.
- [d:r:i] There is no named surface for re-entering an archived milestone's artifacts when a later question makes them load-bearing again. This is rare but real, and uplift should record enough posture context that a later reader can tell whether a re-entered milestone was produced under current doctrine.

### 2n. Cross-Runtime Posture Uplift

- [e:c+i] `new-project` detects the invoking runtime and writes an instruction file named accordingly, and the update/install surfaces route through runtime-specific paths. Sources: `.codex/get-shit-done/workflows/new-project.md:69-90`, `.codex/get-shit-done/workflows/update.md:14-24`.
- [d:r:i] A project may have been initialized under one runtime (Claude, Gemini, OpenCode) and later add a second runtime without re-running `new-project`. Uplift opens the natural place to bring governing-doc wrappers, required-reading posture, and runtime-specific conventions into alignment across runtimes rather than letting the first-runtime install quietly own the whole project.

### 2o. Repo-Local Tooling Install

- [e:c+i] Repo-local tooling includes `audit_refmap.py`, `scan_threshold_language.py`, `runtime_visibility.py`, `capture_launch_truth.py`, `manifest_install_coherence.py`, and related scripts. Sources: `.planning/AGENTS.md:44-74`, `AGENTS.md:149-152`.
- [d:r:i] These are governing tools, not governing docs. They are currently assumed by audit and intervention work but do not have a home in `new-project` output. Uplift should know whether a project already carries the tools that doctrine assumes and open a path to install them when they thin.

### 2p. `gsd-rigorous-research` Install And Research-Skill Posture

- [e:c+i] Root `AGENTS.md` names the repo-local `gsd-rigorous-research` skill as the preferred structure for non-phase-bound research lanes. Source: `AGENTS.md:44`.
- [d:r:i] The skill is a doctrine carrier that a vanilla project does not receive. Uplift should know whether the project carries it and whether recent strengthening-carry changes to the method (proposal `33`) are expressed in the project's own research artifacts.

## 3. Where The Current Ownership Split Still Overcompresses Distinct Jobs

- [d:r:i] "Re-entry" is one label in `37`, but it already carries at least three distinct sub-jobs: short-break resumption (minutes to hours), long-gap return (weeks to months with possible doctrine drift between), and new-operator cold start (someone else picking up work). `resume-project` + `progress` cover the first well; the second needs uplift detection alongside resumption, and the third needs a stronger read of governing docs before routing. Ownership is scattered here across `resume-project`, `progress`, and operator memory.
- [d:r:i] "Repair" currently means structural integrity repair in `health`. It overcompresses at least three sub-jobs: structural repair (missing files, invalid phase refs), posture repair (governing docs or doctrine drift), and runtime drift repair (overlay vs live vs manifest). `health` owns only the first; the rest need a dedicated owner.
- [d:r:i] "Migration" in `37` means `from-gsd2` format migration. It overcompresses at least four sub-jobs: format migration (gsd2 → gsd1), cross-runtime migration (Claude ↔ Codex ↔ Gemini ↔ OpenCode), vanilla-to-repo-local-doctrine uplift, and upstream-drift uplift. Only the first has an explicit owner.
- [d:r:i] "Uplift" itself — even as named in `36` / `37` — overcompresses: vanilla-project uplift, aged-bespoke-project uplift, cross-runtime uplift, and upstream-drift uplift all sit under one label. A later workflow should carry these distinctions rather than flatten them into "refresh everything."
- [d:r:i] "Initialization" overcompresses at least four sub-jobs in the current map: true greenfield (no code, no docs, no discovery), greenfield-with-discovery-seeds (no code, but durable pre-planning corpus in `discovery/`), brownfield-with-code (existing codebase, no `.planning/`), and brownfield-with-docs (existing docs, no `.planning/`). `new-project` and `ingest-docs` split this along a code-vs-docs axis but not along the discovery-seed axis cleanly.
- [d:r:i] "Milestone opening" overcompresses at least three sub-jobs: first milestone after initialization, milestone opening after prior milestone archive, and milestone opening with planted seeds that predate current strengthening-carry doctrine. `new-milestone` covers the first two and carries seed selection, but does not handle doctrine-vintage of the seeds themselves.
- [d:r:i] "Docs merge" overcompresses: docs that straightforwardly extend `.planning/`, docs that propose to change canon, and docs that should trigger milestone recomputation rather than quiet merge. `ingest-docs` merge-mode handles the first well and blocks on conflicts, but it does not route the second or third into a separate owner.
- [d:r:i] "Governing / onboarding" overcompresses in `37`: the section names `mandatory-initial-read` plus audit-subtree companions, but the governing carry actually active in this repo is at least five-fold — `AGENTS.md` + `.planning/AGENTS.md` + `CLAUDE.md` wrappers + `CLAIM-TYPES.md` + `LONG-ARC.md` + repo-local tooling + anti-threshold scan. Treating them as one bucket hides which of them a vanilla project lacks.

## 4. Interaction And Propagation Map

- [e:c+i] `new-project` generates the initial `INSTRUCTION_FILE` and commits `.planning/PROJECT.md`, `REQUIREMENTS.md`, `ROADMAP.md`, `STATE.md`. Source: `.codex/get-shit-done/workflows/new-project.md:1236-1247`, `.codex/get-shit-done/workflows/new-project.md:1335-1346`.
- [d:r:i] `new-project` → first-generation governing / instruction doc → does not connect to any later refresh or re-generation path. A project whose instruction file was written at version N will not re-receive a version-N+1 instruction file except by running `new-project` again (error — project already exists) or by hand edits. That is where uplift opens stronger carry.
- [e:c+i] `update` rewrites runtime via `scripts/setup-portable-gsd.sh`, which composes upstream install → overlay copy → post-copy mutation and preserves user files via the `gsd-user-files-backup` pass. Sources: `.codex/get-shit-done/workflows/update.md:382-462`, `.codex/get-shit-done/workflows/update.md:464-487`, `.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/governance/RUNTIME-MATERIALIZATION-AND-AUTHORITY.md:33-42`.
- [d:r:i] `update` → runtime rewrite → propagates into spawn-time agent behavior and live workflow semantics → which `progress` and `resume-project` read → without surfacing a parallel seam for "project-level governing posture also needs refresh." That seam is where uplift opens stronger carry.
- [e:c+i] `ingest-docs` (merge) writes new requirements and decisions through the intel directory and conflict gate. Source: `.codex/get-shit-done/workflows/ingest-docs.md:264-277`.
- [d:r:i] `ingest-docs` (merge) → new requirements / decisions / roadmap additions → does not propagate into governing-doc stack, runtime posture, or long-horizon carry. A project whose docs merge adds scope that should also force a governing-doc refresh will see the scope land and the governing carry stay untouched.
- [e:c+i] `new-milestone` reads `PROJECT.md`, `MILESTONES.md`, `STATE.md`, can archive phase directories, scans `.planning/seeds/`, and writes a new roadmap. Source: `.codex/get-shit-done/workflows/new-milestone.md:22-96`, `.codex/get-shit-done/workflows/new-milestone.md:186-231`.
- [d:r:i] `new-milestone` → new milestone roadmap → does not check whether existing posture (claim-type convention, long-horizon carry, anti-threshold framing, required-reading install) is current doctrine. A milestone can open cleanly while governing-doc posture quietly ages underneath.
- [e:c+i] `resume-project` reads STATE / HANDOFF / `.continue-here` and routes to next action. Source: `.codex/get-shit-done/workflows/resume-project.md:30-111`.
- [d:r:i] `resume-project` → next-step routing → carries no concept of doctrine vintage. A project that was left sitting during a doctrine uplift will resume as if nothing changed between the pause and the resume.
- [e:c+i] `progress` reads roadmap + state, detects UAT/verification debt, and routes to the correct next-step command. Source: `.codex/get-shit-done/workflows/progress.md:141-516`.
- [d:r:i] `progress` → situational routing → has no "project is stale on doctrine even though current on milestone execution" branch. Its debt model is verification debt, not posture debt.
- [e:c+i] `health` validates structural files, repairs low-risk issues (missing config, missing STATE.md), and explicitly draws a hard boundary around deeper content change. Source: `.codex/get-shit-done/workflows/health.md:123-159`.
- [d:r:i] `health` → structural repair only → cannot touch governing posture, by design. Uplift opens the natural place to handle what `health` correctly refuses.
- [e:c+i] `from-gsd2` migrates hierarchy format; makes no content changes to governing docs or runtime posture. Source: `.codex/skills/gsd-from-gsd2/SKILL.md:48-82`.
- [d:r:i] `from-gsd2` → migrated `.planning/` tree → does not propagate into current repo-local doctrine.
- [e:c+i] `gsd-docs-update` refreshes project documentation; distinct from governing-doc refresh. Source: listing at `.codex/skills/gsd-docs-update/SKILL.md`.
- [d:r:i] `gsd-docs-update` → project-facing docs → propagation into governing / uplift is thin; these live in parallel layers.
- [e:c+i] `capture_launch_truth.py`, `runtime_visibility.py`, `audit_refmap.py`, `scan_threshold_language.py`, `manifest_install_coherence.py` are called from specific audit / intervention lanes rather than installed as project-level posture at entry. Source: `.planning/AGENTS.md:44-74`, `AGENTS.md:149-152`.
- [d:r:i] Repo-local tooling → audit / lane use → no entry surface currently installs these as standing project discipline; uplift opens the natural owner.
- [e:c+i] Workspace creation in `new-workspace` clones repo state into an isolated tree with its own `.planning/`. Source: listing at `.codex/skills/gsd-new-workspace/SKILL.md`.
- [d:r:i] `new-workspace` → isolated tree → posture inherits at clone time → child and parent can then drift. Uplift opens the cross-workspace alignment seam that the workstream family currently solves by hand.
- [d:r:i] Cumulatively, the propagation field has one recurring pattern: near-term execution surfaces (`new-project`, `new-milestone`, `ingest-docs`) generate or refresh a narrow slice of posture at entry; continuity surfaces (`resume-project`, `progress`, `health`, `update`, `from-gsd2`) preserve near-term state and integrity but leave the governing / long-horizon / required-reading / claim-type / repo-local-tooling layers without a refresh path. A dedicated uplift workflow is where these outer layers come into alignment; the interaction map shows exactly why every other surface thins there.

## 5. What A Later Project-Uplift Workflow Should Own

A later `gsd-uplift-project` / `gsd-upgrade-project` workflow opens stronger carry when it owns the composition layer below, which no current surface owns end-to-end.

- [d:r:i] **Uplift detection.** Decide whether an uplift pass is worth opening, using signals such as: installed runtime version vs last overlay / manifest snapshot, governing-doc vintage vs current doctrine version, presence vs absence of claim-type convention, presence vs absence of `LONG-ARC.md`, presence vs absence of `.planning/CLAIM-TYPES.md`, repo-local tooling presence, cross-runtime instruction-file coherence.
- [d:r:i] **Runtime / install posture check.** Consume (not redo) `update`'s install-truth, `runtime_visibility.py`'s overlay-vs-live picture, and `manifest_install_coherence.py`'s comparison against a frozen snapshot. Produce a single classified view of install posture for this project.
- [d:r:i] **Planning structural health.** Consume (not redo) `health`'s integrity view. Flag any structural issue as upstream-of-uplift and route to `health --repair` where appropriate.
- [d:r:i] **Governing-doc install or refresh.** Bring root `AGENTS.md`, `.planning/AGENTS.md`, thin `CLAUDE.md` wrappers, and the generated runtime `INSTRUCTION_FILE` into alignment with current doctrine, preserving project-specific content and routing conflicts to the operator. This is the clearest ownerless seam in `37` and the clearest place the workflow opens stronger carry.
- [d:r:i] **Required-reading posture install.** Install or refresh the project-local practice of adding `<required_reading>` blocks in spec / prompt / packet / launch artifacts. This is install discipline, not prompt-time enforcement (which stays with `mandatory-initial-read`).
- [d:r:i] **Long-horizon carry install.** Install or refresh `LONG-ARC.md`, the strengthening-routes contract in the discuss / plan / research chain (if the project carries current discuss/plan templates), and the anti-threshold scan surfaces.
- [d:r:i] **Claim-type convention install.** Install or refresh `.planning/CLAIM-TYPES.md` and name the notation expectation in load-bearing artifacts. This is a governing-doc carry, not a runtime change.
- [d:r:i] **Discovery / `discovery/` boundary install.** Where a project carries a durable `discovery/` tree, install or refresh the convention line in root `AGENTS.md` that distinguishes upstream context from live operational state, and surface any seed documents that should be promoted into `.planning/` as future-milestone inputs.
- [d:r:i] **Repo-local tooling install.** Install or refresh the repo-local Python / shell tooling that current doctrine assumes (`audit_refmap.py`, `scan_threshold_language.py`, `runtime_visibility.py`, `capture_launch_truth.py`, `manifest_install_coherence.py`). These are governing tools, not runtime surfaces.
- [d:r:i] **Audit-subtree convention install.** Where a project carries (or should carry) durable audit workspaces, install or refresh the audit / wave / lane tuple convention, and the packet / spec / prompt / launch-truth / outputs / inheritance-note shape named in `entry-uplift-audit/README.md`.
- [d:r:i] **Uplift disposition output.** Write a durable `UPLIFT-REPORT.md` (or analogous artifact) recording before-state, what changed, what stayed local, what still requires later reread, what was routed out of this slice, and where the next uplift pass should begin. This is the output record seam that `37` named as scattered.
- [d:r:i] **Routing to downstream surfaces.** Close the pass by routing the operator to the correct next command (`$gsd-new-milestone`, `$gsd-discuss-phase N`, `$gsd-progress`, `$gsd-health`, or a marked rerun boundary for older phase artifacts).

## 6. What Existing Surfaces Should Continue To Own

- [d:r:i] **`new-project`** already carries creation coherence strongly: brownfield detection, deep questioning, spike / sketch discovery, research chain, requirements, roadmap, state initialization, instruction file generation. Uplift should consume its outputs, not re-do its creation flow.
- [d:r:i] **`new-milestone`** already carries milestone continuation strongly: seed scanning, milestone research, requirement scoping, phase-dir archival under reset-phase numbering, new roadmap. Uplift should route to it when the real need is a new milestone rather than doctrine refresh.
- [d:r:i] **`ingest-docs`** already carries docs bootstrap and docs merge strongly: classifier / synthesizer chain, conflict gating with BLOCKER safety, new-mode vs merge-mode routing. Uplift should route docs-origin work into it rather than re-do synthesis.
- [d:r:i] **`resume-project`** already carries session resumption strongly: STATE / HANDOFF / `.continue-here` detection, incomplete-work flagging, next-step routing. Uplift should compose with it when a long-gap return coincides with doctrine age.
- [d:r:i] **`progress`** already carries situational routing strongly: roadmap / state analysis, UAT and verification debt detection, phase-state distinction, route into execute / discuss / plan / verify / audit / milestone close. Uplift should surface posture debt into `progress` as a neighboring signal rather than absorb progress routing.
- [d:r:i] **`health`** already carries structural integrity strongly: missing files, invalid config, naming mismatch, orphaned state. Its hard boundary around doctrine change is correct; uplift should consume its output, not dissolve its boundary.
- [d:r:i] **`update`** already carries runtime install / version change strongly: local vs global detection, preferred-runtime routing, custom-file backup, cache clearing, patch-reapply pointer. Uplift should consume its install truth, not re-run the installer itself.
- [d:r:i] **`from-gsd2`** already carries format migration strongly: hierarchy mapping, completion-state preservation. Uplift should route a post-migration project into uplift, not collapse migration into uplift.
- [d:r:i] **`mandatory-initial-read`** already carries prompt-time required-reading discipline strongly. Uplift should install the project-local practice of writing required-reading blocks; the reference itself keeps owning enforcement once files are named.
- [d:r:i] **`gsd-docs-update`** already carries project-facing documentation refresh strongly. Uplift should stay distinct from it: governing-doc refresh and project-facing doc refresh are sibling layers, not one task.
- [d:r:i] **Repo-local tooling (`audit_refmap.py`, `scan_threshold_language.py`, `runtime_visibility.py`, `capture_launch_truth.py`, `manifest_install_coherence.py`)** should continue as individual, invokable tools with their current contracts. Uplift should install their presence and, where useful, run a first pass — not absorb their behavior.
- [d:r:i] **`gsd-rigorous-research` skill** already carries non-phase-bound research posture strongly. Uplift should install its presence where it thins and consume its outputs where active.

## 7. Report And Governing Carriers The Uplift Family Should Create Or Refresh

### 7a. Create

- [d:r:i] **`UPLIFT-REPORT.md`** — durable per-run disposition artifact. Records: before-state fingerprint (runtime version, governing-doc vintage, tooling presence), pass type (vanilla / aged-bespoke / cross-runtime / upstream-drift), refreshed carriers, preserved local content, remaining later reread, routing target.
- [d:r:i] **`UPLIFT-STATE.md`** (or a dedicated section inside `STATE.md`) — persistent uplift history. Records last-uplift date, last-uplift pass type, and a terse signal for whether doctrine has moved since the last uplift. `progress` and `resume-project` can then surface posture age alongside their normal output.
- [d:r:i] **Project doctrine manifest.** A small index (under `.planning/` or alongside `AGENTS.md`) naming the governing carriers installed and their posture version, so operators and later passes can tell at a glance what the project currently inherits.
- [d:r:i] **Uplift-origin seed convention.** Where uplift detects a carrier that should exist but would create too much scope inside this pass (e.g., install `LONG-ARC.md` with populated content), plant an explicit seed under `.planning/seeds/` so `new-milestone` can surface it later rather than leave it as ambient operator memory.

### 7b. Refresh

- [d:r:i] **Root `AGENTS.md`** — bring current anti-threshold, claim-type, delegation, maintenance, and governance lines into alignment with current doctrine while preserving project-specific product posture sections.
- [d:r:i] **`.planning/AGENTS.md`** — align artifact-class discipline, reference-graph hygiene, launch-truth discipline, research and audit quality lines, and future-flexibility statusing with current doctrine; preserve project-specific canon pointers.
- [d:r:i] **Thin `CLAUDE.md` wrappers (`CLAUDE.md`, `.planning/CLAUDE.md`)** — keep them as cross-vendor wrappers pointing back to `AGENTS.md`, refresh claude-specific translation sections where current doctrine has moved, and do not duplicate subtree doctrine.
- [d:r:i] **`.planning/CLAIM-TYPES.md`** — install where absent; refresh claim-notation definition where posture has moved.
- [d:r:i] **`.planning/LONG-ARC.md`** — install where absent; add a durable future-horizon section where stale; never overwrite project-specific long-arc content without operator confirmation.
- [d:r:i] **Generated runtime instruction file (`INSTRUCTION_FILE` from `new-project`)** — refresh to current template, preserving project-specific inserted sections, and route ambiguity to operator confirmation rather than silent rewrite.
- [d:r:i] **Required-reading blocks in load-bearing artifacts.** Where a project carries specs, prompts, packets, or launch-truth artifacts, install the practice of naming `<required_reading>` files explicitly; do not rewrite the artifacts' content.
- [d:r:i] **Anti-threshold scan surfaces.** Ensure `scan_threshold_language.py` is present and that current request / spec / prompt surfaces are clean; surface debt rather than mutate it.

## 8. What Should Stay Outside The First Uplift Slice

- [d:r:i] **Full cross-generation migration.** `from-gsd2` keeps owning format migration. The first uplift slice should route post-migration projects forward, not absorb migration itself.
- [d:r:i] **Full milestone recomputation.** Uplift should plant seeds and route to `new-milestone` where a milestone move is warranted; it should not silently start one.
- [d:r:i] **Full runtime reinstall.** Uplift should read install truth (`update`, manifest, overlay) and flag drift, not run the installer itself. Runtime install stays with `update` and `scripts/setup-portable-gsd.sh`.
- [d:r:i] **Cross-project orchestration.** First slice is one project at a time. A later family can consider cross-project uplift batching.
- [d:r:i] **Deeper structural repair.** Repairs past `health`'s low-risk set (missing config, missing STATE.md) stay with `health` or with the operator. Uplift names them, does not perform them.
- [d:r:i] **Full audit-subtree aging.** Durable audit workspaces age on their own timeline. Uplift can install the audit-convention carry for future work and can name aging audits as an inquiry signal, but it should not re-tombstone or restructure existing audit trees inside the first slice.
- [d:r:i] **Workstream / worktree reconciliation.** Reconciling state across parallel workstreams stays with the workstream family. Uplift can note workspace posture drift; it should not merge or reconcile across workstreams in the first slice.
- [d:r:i] **Upstream template churn response.** The first slice should install awareness of upstream template drift (detection, reporting) rather than re-expressing every newly shipped template inside every project's artifacts. Template-expression work is a later slice.
- [d:r:i] **Aged-bespoke-project uplift.** Projects that carry bespoke but aging governing docs deserve their own uplift shape; the first slice should stay focused on the vanilla / younger-project case to keep the blast radius small, and then widen.
- [d:r:i] **Cross-runtime posture uplift.** Projects installed under one runtime that later add a second runtime should get their own uplift pass; first slice can route a single-runtime project into alignment and name cross-runtime as deferred.
- [d:r:i] **Forensics / post-mortem entry.** Forensics stays its own surface. Uplift can consume forensic findings as one input; it should not absorb the forensic protocol.
- [d:r:i] **Archived milestone re-entry.** Re-entering archived milestones is a rare, bounded scenario that stays with milestone-archive tooling rather than uplift.
- [d:r:i] **Narrative project-facing docs.** `gsd-docs-update` continues to own those; uplift stays inside governing / planning / runtime carry.

## 9. How The Current Map Should Be Inherited

### Carry Forward

- [d:r:i] The nine-scenario map and its scenario-to-owner routing in `37` stays the first decoder ring for any later uplift workflow, widened (not replaced) by the additions in Section 2.
- [d:r:i] The two-layer per-surface shape (strongest carry + thinner edge) in `37` stays the template for how the uplift workflow should describe every surface it consumes or routes to.
- [d:r:i] The four-part "where carry is scattered" split (governing-doc refresh, long-horizon install, vanilla-project uplift, output record) stays the main seam inventory; the workflow should widen the governing-doc bucket to name `CLAIM-TYPES.md`, `LONG-ARC.md`, repo-local tooling, required-reading posture, and audit-subtree convention alongside the currently named `AGENTS.md` / `CLAUDE.md` stack.
- [d:r:i] The candidate ownership split in `37` stays the first division of labor: `new-project` / `new-milestone` / `ingest-docs` / `health` / `update` / `progress` / `resume-project` / `from-gsd2` stay as specialist owners; uplift is the composition layer.
- [d:r:i] The parent plan in `36` keeps the right sequencing posture: entry-surface audit → uplift path design → first live slice → widening after live use.
- [d:r:i] The runtime-authority companion artifacts (`../../governance/RUNTIME-MATERIALIZATION-AND-AUTHORITY.md`, `../../indexes/GOAL-TO-SURFACE-INTERVENTION-INDEX.md`) stay as the authority lens the uplift workflow uses when it has to decide where an install vs an edit vs a detect-only move should land.

### Revise Before Workflow Design

- [d:r:i] The "Governing / Onboarding Carriers" section in `37` is currently one paragraph anchored on `mandatory-initial-read`. Before workflow design, widen it to enumerate at least: root `AGENTS.md`, `.planning/AGENTS.md`, `CLAUDE.md` wrappers, `CLAIM-TYPES.md`, `LONG-ARC.md`, required-reading posture, claim-type notation, anti-threshold scan, repo-local tooling, audit-subtree convention, `gsd-rigorous-research` skill.
- [d:r:i] The "Vanilla-Project Uplift" label in `37` should split into at least four children before workflow design: vanilla uplift, aged-bespoke uplift, cross-runtime uplift, upstream-drift uplift. Otherwise the first slice will overpack, since these four have different blast radius and different detection signals.
- [d:r:i] The scenario map in `37` should add (before workflow design): workspace / worktree entry, phase-injection entry, installer re-run entry, upstream-template-drift entry, forensics entry, archived-milestone re-entry. Not all need new surfaces, but all need an explicit seat at the table so the workflow can route them rather than quietly miss them.
- [d:r:i] The "Re-entry" and "Repair" labels in `37` should each split into the sub-jobs named in Section 3 so the uplift detection layer has real signals to read.
- [d:r:i] The output record seam in `37` should be rewritten before workflow design to name the specific artifacts Section 7a names (`UPLIFT-REPORT.md`, `UPLIFT-STATE.md`, project doctrine manifest, uplift-origin seed convention). "An output record is missing" is weaker than the stronger positive shape now available.
- [d:r:i] The per-surface passages in `37` should be read as reference rather than as final architectural claims. They describe live surface behavior; the workflow design will need to check them against any runtime movement between now and design time, using `runtime_visibility.py` and fresh reads of `.codex/get-shit-done/`.

### Keep Seeded

- [d:r:i] The working name `gsd-uplift-project` or `gsd-upgrade-project` in `36` should stay seeded; pick the final handle at design time rather than freezing it here.
- [d:r:i] The direction "one explicit owner for the uplift composition layer" stays seeded.
- [d:r:i] The requirement "durable disposition output" stays seeded; `UPLIFT-REPORT.md` is a candidate shape, not a committed name.
- [d:r:i] The pairing of runtime-visibility tooling with uplift detection stays seeded; the first slice should read visibility rather than mutate it.
- [d:r:i] The compactness constraint in `36` — the first slice must be testable on fresh and existing projects without widening into a full harness rewrite — stays seeded as a standing scope brake for any later uplift design.
- [d:r:i] The later widening order proposed in `36` (milestone-opening, docs-ingest merge, resume / re-entry, upgrade / migration families) stays seeded for use only after the first slice produces real examples.
- [d:r:i] The strengthening-carry surfaces already live in discuss / context / plan / research / seed (per proposals `32` and `33`) stay seeded as upstream producers for any uplift that later needs to check whether a project has actually inherited strengthening-route carry.

## Internal Coherence Notes

- [d:r:i] This output widens, rather than replaces, `37`. Where `37` and this output differ, the repo should treat `37` as the earlier local map and this output as the wider inheritance map.
- [d:r:i] Claim typing follows the notation in `AGENTS.md:92-106` and `.planning/CLAIM-TYPES.md`. Load-bearing positive claims use `[e:c+i]` with in-line sources; downstream architectural moves use `[d:r:i]`; governing / framing lines use `[g:r:i]`.
- [d:r:i] The threshold-language ban and deficit-oriented-pseudo-positive ban in both `AGENTS.md` and `.planning/AGENTS.md` shape this output's language. Where a threshold reading would be natural, the surface is reframed as carry, thinning, scattering, or opening — not as pass / fail against a bar.
