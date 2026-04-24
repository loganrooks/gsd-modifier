# Checkpoint 5 GSD Raw Inventory A1: Entry And Router Surfaces

## Incomplete State

[e:b:i] Completed. No known placeholder sections remain. Residual uncertainty is preserved in each ledger entry's `unresolved classification` field instead of being hidden.

## Research Frame

- [g:c:i] This lane inventories the visible entry, wrapper, router, and control surfaces that introduce a user or orchestrator into repo-local GSD. It is intentionally high-level and anti-leftover-bucket: the point is to stop treating awkward entry surfaces as irrelevant just because they do not fit the existing simple picture. Sources: `AGENTS.md:43-45`; `.planning/AGENTS.md:44-60`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-a1-entry-and-router-surfaces-spec.md:5-9,31-46,66-73`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-bundle-spec.md:5-22,66-90,112-127`.
- [g:c:i] The bundle explicitly requires `cross-cutting`, `ambiguous`, and `unplaced` classification states to remain visible. I therefore treat neat exclusivity as a bias risk, not as a cleanliness goal. Sources: `.planning/AGENTS.md:84-96`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-bundle-spec.md:31-37,83-90,114-119`.
- [d:r:i] The honest unit here is not "every skill file equally." The more defensible unit is: direct phase wrappers, discovery surfaces, routers/meta-entrypoints, ad hoc execution shells, continuity/capture shells, and namespace/workspace control shells. That keeps the inventory high-level without flattening obviously different intervention shapes. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-surface-map.md:13-20,24-39,58-61`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-local-topology-schema.md:84-90,151-158`.

## Path Of Inquiry

- [e:c:i] Entry point: I read the required repo/planning governance and the two A1 bundle specs first, then created the output file immediately per durability protocol before widening into the rest of the governing checkpoint materials. Sources: `AGENTS.md:39-45,70-83,96-124`; `.planning/AGENTS.md:42-82,98-121`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-a1-entry-and-router-surfaces-spec.md:23-29,48-77`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-bundle-spec.md:38-64,121-127`.
- [e:c:i] Governing-input reread: I then pulled the required current-map and baseline materials so the inventory could compare real entry surfaces against the existing simplified picture instead of pretending the current topology graph was already complete. Sources: `.planning/readiness/phase-01-rerun/PROTOCOL.md:35-47,159-177`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-local-topology-schema.md:84-90,150-158,194-199`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-upstream-baseline-schema.md:146-169,193-201`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-surface-map.md:12-20,32-39,56-61`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-4-converged-synthesis.md:79-87`.
- [e:r:i] Focused widening inside the allowed surface set: I inspected only the skill/workflow/control surfaces whose descriptions or current-map gaps made them plausible entry or router candidates: `help`, `do`, `progress`, `next`, `manager`, `autonomous`, `quick`, `fast`, `resume-work`, `pause-work`, `settings`, `note`, `check-todos`, `workstreams`, `thread`, and workspace commands. I did not widen into agent internals or deep workflow execution logic unless a surface's role could not be classified without seeing its direct read/dispatch behavior. Sources: `.codex/skills/gsd-help/SKILL.md:48-64`; `.codex/skills/gsd-do/SKILL.md:48-69`; `.codex/skills/gsd-progress/SKILL.md:48-60`; `.codex/skills/gsd-next/SKILL.md:48-64`; `.codex/skills/gsd-manager/SKILL.md:48-74`; `.codex/skills/gsd-autonomous/SKILL.md:48-79`; `.codex/skills/gsd-quick/SKILL.md:48-72,84-99`; `.codex/skills/gsd-fast/SKILL.md:48-64`; `.codex/skills/gsd-resume-work/SKILL.md:48-76`; `.codex/skills/gsd-pause-work/SKILL.md:48-76`; `.codex/skills/gsd-settings/SKILL.md:48-72`; `.codex/skills/gsd-note/SKILL.md:48-70`; `.codex/skills/gsd-check-todos/SKILL.md:48-80`; `.codex/skills/gsd-workstreams/SKILL.md:48-108`; `.codex/skills/gsd-thread/SKILL.md:48-64,164-244`; `.codex/skills/gsd-new-workspace/SKILL.md:58-80`; `.codex/skills/gsd-list-workspaces/SKILL.md:48-58`; `.codex/skills/gsd-remove-workspace/SKILL.md:53-64`.
- [e:r:i] Explicit reason for widening into helper code: `progress`, `manager`, `list-workspaces`, and `workstreams` are helper-backed shells, and `workstreams`/workspace operations are not ordinary skill -> workflow wrappers. I therefore inspected `gsd-tools.cjs` and `bin/lib/workstream.cjs` only where necessary to establish that part of the visible entry plane is a CLI/helper control surface, not just markdown workflows. Sources: `.codex/get-shit-done/bin/gsd-tools.cjs:4-9,12-34,871-887,1009-1031`; `.codex/get-shit-done/bin/lib/workstream.cjs:1-9,19-24,69-120`.
- [e:r:i] Deliberate non-widening: I did not reopen deep phase-internal tracing. Checkpoint 3 and the current topology schema already establish the phase-critical lifecycle, and A1 only needs that family separated from routers and management shells, not re-audited internally. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-surface-map.md:24-39,41-55`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-local-topology-schema.md:151-158`.

## Entry Surface Ledger

### `Direct Phase Workflow Wrapper Family`
- `surface`: `$gsd-discuss-phase`, `$gsd-research-phase`, `$gsd-plan-phase`, `$gsd-execute-phase`, `$gsd-verify-work`, `$gsd-review`
- `path`: `.codex/skills/gsd-discuss-phase/SKILL.md`; `.codex/skills/gsd-plan-phase/SKILL.md`; `.codex/skills/gsd-execute-phase/SKILL.md`; `.codex/skills/gsd-verify-work/SKILL.md`; `.codex/skills/gsd-review/SKILL.md`; `.codex/get-shit-done/workflows/{discuss-phase,research-phase,plan-phase,execute-phase,verify-work,review}.md` as summarized in `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-local-topology-schema.md:151-158` and `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-surface-map.md:24-39`
- `repo-local role as stated by source`: Thin Codex entry adapters into the main phase lifecycle and its review lane; these are the commands the current high-level map already centers.
- `reads/expects`: Phase arguments plus the stage-specific planning artifacts and config described by the underlying lifecycle workflows.
- `emits/returns`: `CONTEXT.md`, `RESEARCH.md`, `PLAN.md`, `SUMMARY.md`, `VERIFICATION.md`, `UAT.md`, and `REVIEWS.md`, depending on stage.
- `downstream consumers`: Later lifecycle stages, users, and helper-backed routers such as `progress`.
- `obvious relations`: This family is already relatively well represented by the current topology graph and Checkpoint 3 surface map; A1 mainly needs it held apart from routers and control shells.
- `candidate loose tags`: `direct-wrapper`, `phase-lifecycle`, `artifact-producing`
- `intervention status`: Mixed. The wrapper layer is mostly `upstream/base` with some repo-local overrides, and current topology schema already marks `discuss-phase` and `plan-phase` as locally intervened surfaces.
- `classification status`: `placed provisionally`
- `confidence`: high
- `unresolved classification`: Exact subfamily splits belong to A2; A1 only needs this family distinguished from discovery/router/control surfaces.

### `$gsd-help`
- `surface`: `$gsd-help`
- `path`: `.codex/skills/gsd-help/SKILL.md:48-64`; `.codex/get-shit-done/workflows/help.md:1-6,121-171,231-318,414-459`
- `repo-local role as stated by source`: Static discovery/reference surface. The skill says to output the command reference only, with no project analysis or next-step commentary.
- `reads/expects`: No project artifact state; it just reads the help workflow's reference content.
- `emits/returns`: A command reference document; no planning artifact and no dispatch.
- `downstream consumers`: Humans deciding which command to run next.
- `obvious relations`: This is discovery, not routing. It is also not a full inventory of live entry surfaces: the reference covers `quick`, `fast`, `progress`, `resume-work`, `pause-work`, `note`, `check-todos`, `settings`, and `help`, but not `manager`, `next`, `workstreams`, `thread`, or workspace commands that still exist as live skills. Compare `.codex/skills/gsd-manager/SKILL.md:48-74`; `.codex/skills/gsd-next/SKILL.md:48-64`; `.codex/skills/gsd-workstreams/SKILL.md:48-108`; `.codex/skills/gsd-thread/SKILL.md:48-64`; `.codex/skills/gsd-list-workspaces/SKILL.md:48-58`; `.codex/skills/gsd-new-workspace/SKILL.md:58-80`; `.codex/skills/gsd-remove-workspace/SKILL.md:53-64`.
- `candidate loose tags`: `discovery`, `reference`, `wrapper`
- `intervention status`: Not assessed in this lane beyond it being a live repo-local skill -> workflow pair.
- `classification status`: `placed provisionally`
- `confidence`: high
- `unresolved classification`: Whether `help` should ever be treated as the canonical visible inventory is open; current evidence says no.

### `$gsd-do`
- `surface`: `$gsd-do`
- `path`: `.codex/skills/gsd-do/SKILL.md:48-69`; `.codex/get-shit-done/workflows/do.md:1-109`
- `repo-local role as stated by source`: Smart dispatcher that never does the work itself; it matches natural-language intent to a command, resolves ambiguity, displays the routing decision, and dispatches.
- `reads/expects`: `{{GSD_ARGS}}`, project existence via `gsd-tools.cjs state load`, and text-mode/AskUserQuestion handling.
- `emits/returns`: A routing banner and immediate invocation of the selected `$gsd-*`; no primary artifact of its own.
- `downstream consumers`: The routed command and its underlying workflow.
- `obvious relations`: Real router/meta-entry surface, but narrower than the total live entry set. Its first-match route table covers a subset of commands and does not expose `manager`, `next`, `settings`, `note`, `thread`, `workstreams`, or workspace commands.
- `candidate loose tags`: `router`, `dispatcher`, `meta-entry`
- `intervention status`: Not assessed in this lane beyond it being a live repo-local skill -> workflow pair.
- `classification status`: `cross-cutting`
- `confidence`: high
- `unresolved classification`: It is a router, but not a universal router; next-map treatment should show it as a partial dispatcher rather than "the" single entrance.

### `$gsd-progress`
- `surface`: `$gsd-progress`
- `path`: `.codex/skills/gsd-progress/SKILL.md:48-60`; `.codex/get-shit-done/workflows/progress.md:11-70,93-139,141-279`; `.codex/get-shit-done/bin/gsd-tools.cjs:871-887`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-local-topology-schema.md:158,194-199`
- `repo-local role as stated by source`: State-aware status board plus next-step router. It summarizes recent work, current position, outstanding debt, and then routes toward discuss/plan/execute/verify/audit actions.
- `reads/expects`: `init progress`, `config-get`, `roadmap analyze`, `state-snapshot`, `summary-extract`, and `audit-uat` helper calls.
- `emits/returns`: Rich status report, route suggestions, and verification-debt warnings; no primary artifact file of its own.
- `downstream consumers`: User/operator, `execute-phase`, `plan-phase`, `discuss-phase`, `verify-work`, and `audit-uat`.
- `obvious relations`: More than passive status. It sits between discovery and routing and depends on the helper CLI as part of its operative control plane.
- `candidate loose tags`: `router`, `status`, `helper-backed`, `control-shell`
- `intervention status`: The current topology schema groups `progress.md` with `transition.md`, `ship.md`, and `autonomous.md` as an `upstream/base` routing/control cluster.
- `classification status`: `cross-cutting`
- `confidence`: high
- `unresolved classification`: Keep it distinct from `next`; `progress` suggests and reports, while `next` auto-advances and can record deferrals.

### `$gsd-next`
- `surface`: `$gsd-next`
- `path`: `.codex/skills/gsd-next/SKILL.md:48-65`; `.codex/get-shit-done/workflows/next.md:12-35,37-135,137-188`
- `repo-local role as stated by source`: Zero-friction auto-advance surface. It determines the next logical GSD step, runs safety gates, scans prior phases for incomplete work, and then immediately invokes the chosen command.
- `reads/expects`: `state json`, `STATE.md`, `ROADMAP.md`, `.continue-here`, verification state, prior phase completeness, and optional `--force`.
- `emits/returns`: Hard-stop messages, completeness reports, optional backlog deferral writes/commits, and direct command invocation.
- `downstream consumers`: `discuss-phase`, `plan-phase`, `execute-phase`, `verify-work`, `complete-milestone`, `resume-work`, and `ROADMAP.md` when it records deferrals.
- `obvious relations`: Router/meta-entry surface adjacent to `progress`, but materially stronger: it owns hard stops, prior-phase completeness handling, and direct no-confirmation dispatch.
- `candidate loose tags`: `router`, `auto-advance`, `safety-gated`, `meta-entry`
- `intervention status`: Not assessed in this lane beyond it being a live repo-local skill -> workflow pair.
- `classification status`: `cross-cutting`
- `confidence`: high
- `unresolved classification`: It partly behaves like a control policy surface because it can mutate backlog state during advancement, not just suggest a command.

### `$gsd-manager`
- `surface`: `$gsd-manager`
- `path`: `.codex/skills/gsd-manager/SKILL.md:48-74`; `.codex/get-shit-done/workflows/manager.md:15-33,56-83,106-181,197-280`
- `repo-local role as stated by source`: Interactive milestone dashboard and command center. It refreshes state, shows recommended actions, dispatches discuss inline, and spawns plan/execute as background agents.
- `reads/expects`: `init manager`, per-phase `recommended_actions`, manager flags from config, phase status, and background activity state.
- `emits/returns`: Dashboard display, AskUserQuestion menus, background Task spawns, and inline dispatch into other skills.
- `downstream consumers`: `gsd-discuss-phase`, `gsd-plan-phase`, `gsd-execute-phase`, `gsd-verify-work`, and `gsd-complete-milestone`.
- `obvious relations`: This is a real orchestration shell, not just another wrapper. It is also one of the clearest omissions from both the current topology graph and the static help reference.
- `candidate loose tags`: `manager`, `dashboard`, `router`, `background-orchestrator`
- `intervention status`: Not assessed in this lane beyond it being a live repo-local skill -> workflow pair.
- `classification status`: `cross-cutting`
- `confidence`: high
- `unresolved classification`: Next map should keep it separate from `autonomous`; both orchestrate, but `manager` remains human-in-the-loop and dashboard-driven.

### `$gsd-autonomous`
- `surface`: `$gsd-autonomous`
- `path`: `.codex/skills/gsd-autonomous/SKILL.md:48-79`; `.codex/get-shit-done/workflows/autonomous.md:1-5,15-75,78-149,151-260`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-local-topology-schema.md:158`
- `repo-local role as stated by source`: Multi-phase autopilot. It discovers incomplete phases, then runs discuss -> plan -> execute per phase, optionally with inline discuss and background plan/execute.
- `reads/expects`: Milestone init, `roadmap analyze`, per-phase details, skip-discuss/config flags, and optional range flags.
- `emits/returns`: Repeated phase artifacts and roadmap/state advancement across a run, followed by milestone closeout suggestions.
- `downstream consumers`: The full phase lifecycle, later milestone closure surfaces, and users overseeing long runs.
- `obvious relations`: Router/meta-entry surface already partially represented in the current topology graph, but still different from ordinary wrappers because it sequences several commands across multiple phases.
- `candidate loose tags`: `orchestrator`, `autopilot`, `meta-entry`
- `intervention status`: The current topology schema groups `autonomous.md` with `progress.md`, `transition.md`, and `ship.md` as a routing/control cluster marked `upstream/base`.
- `classification status`: `cross-cutting`
- `confidence`: high
- `unresolved classification`: Keep it separate from `manager`; both orchestrate, but one is dashboard/manual and the other is milestone-autopilot.

### `Ad Hoc Task Family`
- `surface`: `$gsd-quick` and `$gsd-fast`
- `path`: `.codex/get-shit-done/workflows/help.md:135-171`; `.codex/skills/gsd-quick/SKILL.md:48-99`; `.codex/get-shit-done/workflows/quick.md:1-13,129-190`; `.codex/skills/gsd-fast/SKILL.md:48-64`; `.codex/get-shit-done/workflows/fast.md:1-9,24-42,44-88`
- `repo-local role as stated by source`: Alternate non-phase task entry lane. `quick` is a shortened but still structured mini-pipeline living in `.planning/quick/`; `fast` is the inline escape hatch that refuses non-trivial work and redirects it back to `quick`.
- `reads/expects`: Task description, active project/roadmap for `quick`, subcommand parsing (`list/status/resume`) in `quick`, and triviality heuristics in `fast`.
- `emits/returns`: `quick` creates `.planning/quick/*/PLAN.md` and `SUMMARY.md`; `fast` emits direct code changes, a commit, and optional `STATE.md` logging without plan artifacts.
- `downstream consumers`: Users, `STATE.md`, later quick-task resumption, and any follow-on verification done outside the fast lane.
- `obvious relations`: This family is visible in the help reference but absent from the current topology graph. It is not just a utility footnote; it is an alternate execution entry that bypasses the roadmap-backed phase lifecycle.
- `candidate loose tags`: `ad-hoc`, `alternate-entry`, `quick-exec`, `inline-exec`
- `intervention status`: Not assessed in this lane beyond these being live repo-local skill/workflow surfaces.
- `classification status`: `ambiguous`
- `confidence`: high
- `unresolved classification`: `quick` is richer than a wrapper because it owns subcommands and a separate artifact chain; `fast` is closer to a control escape hatch than to ordinary workflow routing.

### `Session Continuity Family`
- `surface`: `$gsd-resume-work` and `$gsd-pause-work`
- `path`: `.codex/skills/gsd-resume-work/SKILL.md:48-76`; `.codex/get-shit-done/workflows/resume-project.md:1-15,19-32,62-112,156-192,227-260`; `.codex/skills/gsd-pause-work/SKILL.md:48-76`; `.codex/get-shit-done/workflows/pause-work.md:1-7,11-33,37-59,61-107,204-227`
- `repo-local role as stated by source`: Preserve and restore working state across sessions. `pause-work` writes structured and human-readable handoff state; `resume-work` reloads that state and routes the user toward the most plausible next action.
- `reads/expects`: Current phase/spike/deliberation/research context, `STATE.md`, `PROJECT.md`, `HANDOFF.json`, `.continue-here`, interrupted-agent state, and incomplete-plan detection.
- `emits/returns`: `.planning/HANDOFF.json`, `.continue-here.md`, WIP commit, project-status display, and next-action options.
- `downstream consumers`: Users, `resume-work`, later routers such as `progress`/`next`, and any workflow resuming from the preserved state.
- `obvious relations`: These are cross-cutting continuity shells, not phase-lifecycle stages. They connect directly to router surfaces and to planning artifacts without being ordinary lifecycle wrappers.
- `candidate loose tags`: `continuity`, `pause-resume`, `handoff`, `checkpoint`
- `intervention status`: Not assessed in this lane beyond these being live repo-local skill/workflow surfaces.
- `classification status`: `cross-cutting`
- `confidence`: high
- `unresolved classification`: `resume-work` partly overlaps `progress` and `next`, but it remains a different surface because it reconstructs continuity rather than just routing fresh work.

### `$gsd-settings`
- `surface`: `$gsd-settings`
- `path`: `.codex/skills/gsd-settings/SKILL.md:48-72`; `.codex/get-shit-done/workflows/settings.md:1-2,11-38,40-204,206-250`; `.codex/get-shit-done/workflows/help.md:414-433`
- `repo-local role as stated by source`: Interactive control-plane configuration for workflow toggles and model profile selection.
- `reads/expects`: `config-ensure-section`, current `.planning/config.json`, current model/workflow/git settings, and an interactive question set.
- `emits/returns`: Updated `.planning/config.json` and optionally `~/.gsd/defaults.json`.
- `downstream consumers`: Nearly every helper-backed workflow and init path that reads workflow flags or model profile.
- `obvious relations`: Control surface, not lifecycle stage. It also has a nearby quick-switch companion in `$gsd-set-profile`, which reinforces that config/profile administration is its own visible entry family.
- `candidate loose tags`: `control-surface`, `config`, `model-profile`
- `intervention status`: Not assessed in this lane beyond it being a live repo-local skill -> workflow pair.
- `classification status`: `cross-cutting`
- `confidence`: high
- `unresolved classification`: It belongs in the map even though it produces no phase artifact, because it materially changes how most other entry surfaces behave.

### `Capture And Backlog Bridge Family`
- `surface`: `$gsd-note` and `$gsd-check-todos`
- `path`: `.codex/skills/gsd-note/SKILL.md:48-70`; `.codex/get-shit-done/workflows/note.md:1-6,14-36,38-67,69-135`; `.codex/skills/gsd-check-todos/SKILL.md:48-80`; `.codex/get-shit-done/workflows/check-todos.md:1-3,11-36,44-61,73-166`; `.codex/get-shit-done/workflows/help.md:279-318`
- `repo-local role as stated by source`: Side-entry capture and re-entry bridge. `note` captures ideas instantly, supports global fallback, and can promote notes into todos; `check-todos` loads pending todos and routes them into "work now", "add to phase", "brainstorm", or "create a phase".
- `reads/expects`: Note text or subcommands; `.planning/notes`, `.codex/notes`, `.planning/todos`, `init todos`, todo files, and roadmap correlation.
- `emits/returns`: Note files, promoted todo files, todo moves to completed, `STATE.md` todo updates, commits, and routing suggestions.
- `downstream consumers`: Users, future planning work, `add-phase`, `progress`, and any follow-on execution started from a selected todo.
- `obvious relations`: These surfaces sit between idea capture and active roadmap work. They are not cleanly "just utility" because they can feed or reopen planned work.
- `candidate loose tags`: `capture`, `backlog-bridge`, `global-local-bridge`, `routing`
- `intervention status`: Not assessed in this lane beyond these being live repo-local skill/workflow surfaces.
- `classification status`: `ambiguous`
- `confidence`: high
- `unresolved classification`: Keep `note` and `check-todos` related but distinct in the next map; one captures/promotes, the other loads/routes backlog state.

### `$gsd-workstreams`
- `surface`: `$gsd-workstreams`
- `path`: `.codex/skills/gsd-workstreams/SKILL.md:48-108`; `.codex/get-shit-done/bin/gsd-tools.cjs:1009-1031`; `.codex/get-shit-done/bin/lib/workstream.cjs:1-9,19-24,69-120`
- `repo-local role as stated by source`: Direct management shell for internal workstream namespacing. It lists, creates, switches, resumes, completes, and summarizes parallel milestone workstreams by calling helper CLI subcommands directly.
- `reads/expects`: Workstream subcommand plus `.planning/workstreams` state through `gsd-tools workstream`.
- `emits/returns`: Workstream namespace creation/completion, active-workstream switching, and human-readable status/progress output.
- `downstream consumers`: All workflows that honor `--ws` or active-workstream path resolution.
- `obvious relations`: This is not an ordinary skill -> workflow wrapper. It is a direct skill -> helper control shell that changes where the rest of the planning system resolves its files.
- `candidate loose tags`: `namespace-control`, `management-shell`, `helper-direct`
- `intervention status`: Not assessed in this lane beyond it being a live repo-local skill + helper-chain surface.
- `classification status`: `ambiguous`
- `confidence`: high
- `unresolved classification`: The next map should show it as a namespace/control-plane surface, not bury it under generic "utility" or force it into the phase lifecycle.

### `Workspace Family`
- `surface`: `$gsd-new-workspace`, `$gsd-list-workspaces`, `$gsd-remove-workspace`
- `path`: `.codex/skills/gsd-new-workspace/SKILL.md:58-80`; `.codex/skills/gsd-list-workspaces/SKILL.md:48-58`; `.codex/get-shit-done/workflows/list-workspaces.md:1-18,20-55`; `.codex/skills/gsd-remove-workspace/SKILL.md:53-64`; `.codex/get-shit-done/bin/gsd-tools.cjs:877-887`
- `repo-local role as stated by source`: External workspace-perimeter administration. These surfaces create isolated workspace directories with independent `.planning/`, list existing workspaces under `~$gsd-workspaces/`, and remove them cleanly.
- `reads/expects`: Workspace args and `init {new-workspace,list-workspaces,remove-workspace}` helper state, plus `WORKSPACE.md` and workspace filesystem structure.
- `emits/returns`: Workspace directories, `WORKSPACE.md`, independent `.planning/` roots, status tables, and removal actions.
- `downstream consumers`: Humans entering workspaces, `gsd-new-project` inside a new workspace, and later workspace cleanup.
- `obvious relations`: Adjacent to `workstreams`, but not the same thing. Workspaces are external multi-repo or multi-copy entry surfaces, not internal `.planning/workstreams` namespacing.
- `candidate loose tags`: `external-entry`, `workspace-admin`, `multi-repo`
- `intervention status`: Not assessed in this lane beyond these being live repo-local skill/workflow/helper surfaces.
- `classification status`: `ambiguous`
- `confidence`: medium-high
- `unresolved classification`: Keep workspace administration visibly separate from workstream namespacing; the two are related but operate at different boundaries.

### `$gsd-thread`
- `surface`: `$gsd-thread`
- `path`: `.codex/skills/gsd-thread/SKILL.md:48-64,68-133,135-244,248-264`
- `repo-local role as stated by source`: Direct persistent-context shell for cross-session work that does not belong to a specific phase. It can create, list, resume, inspect, and resolve thread files under `.planning/threads/`.
- `reads/expects`: Thread slug or description, `.planning/threads/*.md`, frontmatter helpers, and direct file existence checks.
- `emits/returns`: Thread files, status changes, commit records, and plain-text resumption context.
- `downstream consumers`: Future sessions, humans, and later promotion into `add-phase` or `add-backlog`.
- `obvious relations`: Another non-ordinary surface: no separate workflow file, direct skill-owned logic, and an artifact family outside the roadmap/phase chain. It is also omitted from the help reference and current topology graph.
- `candidate loose tags`: `context-shell`, `continuity`, `direct-skill`, `non-phase`
- `intervention status`: Not assessed in this lane beyond it being a live repo-local skill-owned surface.
- `classification status`: `unplaced`
- `confidence`: high
- `unresolved classification`: It likely belongs near continuity/capture surfaces, but next-map synthesis should keep that provisional rather than pretending its final family is settled.

## Router And Meta-Entry Surfaces

- [e:c:i] The clearest router/meta-entry set is: `gsd-do`, `gsd-progress`, `gsd-next`, `gsd-manager`, and `gsd-autonomous`. All five select, sequence, or dispatch other commands rather than simply carrying one fixed workflow contract end-to-end. Sources: `.codex/get-shit-done/workflows/do.md:35-97`; `.codex/get-shit-done/workflows/progress.md:141-279`; `.codex/get-shit-done/workflows/next.md:37-188`; `.codex/get-shit-done/workflows/manager.md:131-181,197-280`; `.codex/get-shit-done/workflows/autonomous.md:78-149,151-260`.
- [e:c:i] `gsd-help` is discovery-only, not a router. Its skill explicitly says to output the reference content only, and the workflow is just the reference body. Sources: `.codex/skills/gsd-help/SKILL.md:48-64`; `.codex/get-shit-done/workflows/help.md:1-6`.
- [e:c+r:i] `gsd-progress` and `gsd-next` should not be flattened into one "status/continue" bucket. `progress` reports plus suggests; `next` owns hard stops, prior-phase completeness scanning, optional backlog deferral writes, and no-confirmation dispatch. Sources: `.codex/get-shit-done/workflows/progress.md:141-279`; `.codex/get-shit-done/workflows/next.md:37-135,173-188`.
- [e:c+r:i] `gsd-manager` and `gsd-autonomous` are both orchestration shells, but they are different kinds. `manager` is human-in-the-loop, dashboard-driven, and background-agent aware; `autonomous` is milestone-autopilot with only bounded pauses for user decisions. Sources: `.codex/get-shit-done/workflows/manager.md:56-83,131-181,197-280`; `.codex/get-shit-done/workflows/autonomous.md:1-5,46-47,78-149,151-260`.
- [e:c+r:i] `gsd-settings`, `gsd-workstreams`, workspace commands, and `gsd-thread` are better treated as control shells than as ordinary wrappers. They either change the planning namespace/control plane, create external work contexts, or manage their own non-phase artifact family. Sources: `.codex/get-shit-done/workflows/settings.md:171-250`; `.codex/skills/gsd-workstreams/SKILL.md:68-108`; `.codex/get-shit-done/bin/lib/workstream.cjs:1-9,19-24`; `.codex/skills/gsd-new-workspace/SKILL.md:58-71`; `.codex/skills/gsd-thread/SKILL.md:48-64,180-244`.

## Unplaced Or Weakly Placed Entry Surfaces

- [e:c+r:i] `gsd-thread` is the clearest currently `unplaced` entry surface. It is a live skill-owned shell with no separate workflow file, its own `.planning/threads/` artifact family, and promotion edges into later phase/backlog work, but it is neither phase lifecycle nor simple continuity handoff. Sources: `.codex/skills/gsd-thread/SKILL.md:48-64,167-244,248-264`.
- [e:c+r:i] `gsd-workstreams` is still `ambiguous`. It is visibly user-facing, but its operative role is namespace mutation through helper CLI calls, not standard workflow orchestration. Sources: `.codex/skills/gsd-workstreams/SKILL.md:48-108`; `.codex/get-shit-done/bin/gsd-tools.cjs:1009-1031`; `.codex/get-shit-done/bin/lib/workstream.cjs:1-9,19-24`.
- [e:c+r:i] Workspace administration is `ambiguous` for a different reason: it lives at the external workspace perimeter (`~$gsd-workspaces/`, repo copies, independent `.planning/`) rather than inside the current project's ordinary runtime. It belongs on the map, but not as if it were just another in-project phase command. Sources: `.codex/skills/gsd-new-workspace/SKILL.md:58-71`; `.codex/get-shit-done/workflows/list-workspaces.md:1-18,20-55`; `.codex/skills/gsd-remove-workspace/SKILL.md:53-64`.
- [e:c+r:i] `gsd-quick` is `ambiguous` rather than neatly placeable. It is not part of the roadmap-backed phase chain, but it is also not a trivial utility: it owns an alternate artifact lifecycle under `.planning/quick/` and its own `list/status/resume` entry behavior. Sources: `.codex/skills/gsd-quick/SKILL.md:48-72,86-99`; `.codex/get-shit-done/workflows/quick.md:1-13,129-190`.
- [e:c+r:i] `gsd-note` is weakly placed because it spans project-local capture, global capture, and note-to-todo promotion. That bridge role is real and should stay explicit rather than being collapsed into generic "todo tooling." Sources: `.codex/get-shit-done/workflows/note.md:14-36,38-67,69-135,139-158`; `.codex/get-shit-done/workflows/help.md:279-292`.

## What The Current High-Level Picture Misses

- [e:c+r:i] The current topology picture is still too simple at the visible-entry layer. Its graph shows the main lifecycle plus `review`, `progress`, `ship`, and `autonomous`, but it does not draw `help`, `do`, `next`, `manager`, `quick`, `fast`, `resume-work`, `pause-work`, `note`, `check-todos`, `settings`, `workstreams`, `thread`, or workspace administration as first-class entry surfaces. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-local-topology-schema.md:84-90`; `.codex/skills/gsd-do/SKILL.md:48-69`; `.codex/skills/gsd-manager/SKILL.md:48-74`; `.codex/skills/gsd-next/SKILL.md:48-64`; `.codex/skills/gsd-quick/SKILL.md:48-72`; `.codex/skills/gsd-fast/SKILL.md:48-64`; `.codex/skills/gsd-resume-work/SKILL.md:48-76`; `.codex/skills/gsd-pause-work/SKILL.md:48-76`; `.codex/skills/gsd-note/SKILL.md:48-70`; `.codex/skills/gsd-check-todos/SKILL.md:48-80`; `.codex/skills/gsd-settings/SKILL.md:48-72`; `.codex/skills/gsd-workstreams/SKILL.md:48-108`; `.codex/skills/gsd-thread/SKILL.md:48-64`; `.codex/skills/gsd-list-workspaces/SKILL.md:48-58`.
- [e:c+r:i] The static help reference is a partial discovery surface, not a full inventory. It covers quick/fast/progress/resume/pause/note/check-todos/settings/help, but omits live management/router surfaces such as `manager`, `next`, `workstreams`, `thread`, and workspace administration. Sources: `.codex/get-shit-done/workflows/help.md:135-171,231-318,414-459`; `.codex/skills/gsd-manager/SKILL.md:48-74`; `.codex/skills/gsd-next/SKILL.md:48-64`; `.codex/skills/gsd-workstreams/SKILL.md:48-108`; `.codex/skills/gsd-thread/SKILL.md:48-64`; `.codex/skills/gsd-new-workspace/SKILL.md:58-80`; `.codex/skills/gsd-list-workspaces/SKILL.md:48-58`; `.codex/skills/gsd-remove-workspace/SKILL.md:53-64`.
- [e:c+r:i] `gsd-do` is also a partial router, not a universal one. Its route table is useful, but it only spans a constrained subset of the real entry set and therefore cannot stand in for the whole visible control surface. Sources: `.codex/get-shit-done/workflows/do.md:35-60`; `.codex/skills/gsd-settings/SKILL.md:48-72`; `.codex/skills/gsd-workstreams/SKILL.md:48-108`; `.codex/skills/gsd-thread/SKILL.md:48-64`.
- [e:c+r:i] Checkpoint 3's broad claim that most of `.codex/skills/` is lower leverage than it looks is directionally right for the core phase chain, but it is too coarse for A1. Several live entry surfaces own meaningful logic themselves: `manager` owns dashboard orchestration, `next` owns safety-gated advancement, `workstreams` and `thread` are direct shells, and `quick` owns an alternate artifact family. Sources: `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-3-gsd-surface-map.md:56-61`; `.codex/get-shit-done/workflows/manager.md:131-181,197-280`; `.codex/get-shit-done/workflows/next.md:37-188`; `.codex/skills/gsd-workstreams/SKILL.md:48-108`; `.codex/skills/gsd-thread/SKILL.md:48-64,180-244`; `.codex/skills/gsd-quick/SKILL.md:48-72,86-99`.
- [e:c+r:i] The helper CLI is part of the entry plane, not just backstage plumbing. `progress`, `manager`, `list-workspaces`, `workstreams`, `resume`, `pause`, and `settings` all rely on `gsd-tools` init/config/workstream helpers to classify state and route work. A next map that only shows skill -> workflow arrows will miss that helper-backed control seam. Sources: `.codex/get-shit-done/workflows/progress.md:11-23,44-59`; `.codex/get-shit-done/workflows/manager.md:19-34,60-67`; `.codex/get-shit-done/workflows/list-workspaces.md:11-18`; `.codex/get-shit-done/workflows/settings.md:11-20`; `.codex/get-shit-done/workflows/resume-project.md:19-32`; `.codex/get-shit-done/workflows/pause-work.md:61-66`; `.codex/get-shit-done/bin/gsd-tools.cjs:4-9,12-34,871-887,1009-1031`.

## Recommended Additions To The Next Map

1. Add an explicit `Entry / Discovery / Routing` family with at least `help`, `do`, `progress`, `next`, `manager`, and `autonomous`, and distinguish `discovery` from `routing` from `multi-step orchestration`. Sources: `.codex/get-shit-done/workflows/help.md:1-6`; `.codex/get-shit-done/workflows/do.md:35-97`; `.codex/get-shit-done/workflows/progress.md:141-279`; `.codex/get-shit-done/workflows/next.md:37-188`; `.codex/get-shit-done/workflows/manager.md:131-181`; `.codex/get-shit-done/workflows/autonomous.md:78-149`.
2. Add an `Alternate Execution` family for `quick` and `fast` so the map no longer implies phase lifecycle is the only serious work-entry lane. Sources: `.codex/get-shit-done/workflows/help.md:135-171`; `.codex/get-shit-done/workflows/quick.md:1-13,129-190`; `.codex/get-shit-done/workflows/fast.md:24-42,44-88`.
3. Add a `Continuity / Capture / Backlog Bridge` family for `resume-work`, `pause-work`, `note`, `check-todos`, and keep `thread` visible as a still-unplaced neighbor rather than burying it. Sources: `.codex/get-shit-done/workflows/resume-project.md:62-112,156-192`; `.codex/get-shit-done/workflows/pause-work.md:61-107,204-227`; `.codex/get-shit-done/workflows/note.md:14-36,69-135`; `.codex/get-shit-done/workflows/check-todos.md:44-166`; `.codex/skills/gsd-thread/SKILL.md:48-64,180-244`.
4. Add a `Namespace / Workspace Control` family and keep `workstreams` separate from workspace administration. `workstreams` is internal `.planning` namespacing; workspace commands create or manage external workspace roots with their own `.planning/`. Sources: `.codex/get-shit-done/bin/lib/workstream.cjs:1-9,19-24`; `.codex/skills/gsd-new-workspace/SKILL.md:58-71`; `.codex/get-shit-done/workflows/list-workspaces.md:1-18,20-55`; `.codex/skills/gsd-remove-workspace/SKILL.md:53-64`.
5. Draw `gsd-tools.cjs` as an explicit helper/control substrate under the router/control-shell families. That will make it harder for later maps to pretend every meaningful entry surface is "just a skill wrapper." Sources: `.codex/get-shit-done/bin/gsd-tools.cjs:4-9,12-34,871-887,1009-1031`; `.codex/get-shit-done/workflows/progress.md:15-23,48-59`; `.codex/get-shit-done/workflows/manager.md:21-33,62-67`; `.codex/get-shit-done/workflows/list-workspaces.md:13-18`.
6. Tag future map entries with dual classification when needed: `direct wrapper`, `router`, `management shell`, `control-plane backed`, `non-phase artifact family`, and `external workspace perimeter`. This repo has already earned a richer vocabulary than one flat "skills" bucket. Sources: `.planning/AGENTS.md:84-96`; `.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-raw-inventory-bundle-spec.md:31-37,66-90,112-119`.
