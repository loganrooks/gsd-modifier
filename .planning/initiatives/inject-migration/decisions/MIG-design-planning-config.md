# Migration Design: planning-config.md

Date: 2026-05-16
Phase: 4 (`04-first-wave-references`)
Slice: 7 (`design migration of references/planning-config.md`)
Status: design-only; no manifest, overlay, runtime, bootstrap, or contract behavior changed

## Decision

Do not treat `get-shit-done/references/planning-config.md` as a routine full-fidelity apply candidate.

This carrier is mostly an overwrite-staleness case, not a clean additive-reference case. The current modifier file carries a few local runtime/path deltas that are plausible modifier-owned content:

1. `gsd-sdk query ...` examples are rewritten to repo-local `node "__PROJECT_ROOT__/.codex/get-shit-done/bin/gsd-tools.cjs" ...` examples.
2. `/gsd:discuss-phase` examples are rewritten to `/gsd-discuss-phase`.
3. The team-project example and field reference use `workflow.discuss_mode: "exploratory"` instead of upstream `"discuss"`.

The current modifier file also drops several upstream config fields and sections that now appear to be upstream drift, not intentional modifier ownership: `git.create_tag`, `workflow.inline_plan_threshold`, `workflow.auto_prune_state`, `workflow.ai_integration_phase`, `workflow.code_review*`, `workflow.security_*`, `workflow.post_planning_gaps`, `ship.pr_body_sections`, `features.global_learnings`, `learnings.max_inject`, and `intel.enabled`.

Recommendation for Slice 8: run Plan/slice-ambiguity review before applying. The safest candidate is a **source-freshening inject migration**: preserve the local runtime/path and `discuss_mode` deltas with seven existing `block_replace` operations, while letting upstream-added field documentation flow through. This is marker-clean and preflights under the current catalog, but it is not byte-for-byte equivalent to the stale overwrite.

## Current State

Upstream source read from:

```text
/home/rookslog/workspace/projects/get-shit-done-upstream/get-shit-done/references/planning-config.md
```

Upstream checkout: `a7f0af2c`.

Upstream relevant ranges:

- `:27-43` - top config-schema option table.
- `:46-83` - commit-docs behavior examples using `gsd-sdk query`.
- `:164-178` - branching config examples using `gsd-sdk query`.
- `:223-346` - complete field reference, including several newer upstream fields absent from the current modifier overwrite.
- `:407-435` - team project example with `workflow.discuss_mode: "discuss"`.

Current modifier overwrite source:

```text
tooling/portable-gsd/overlay/get-shit-done/references/planning-config.md
```

Modifier relevant ranges:

- `:27-41` - top option table, with `/gsd-discuss-phase` spelling and missing upstream `git.create_tag` / `workflow.inline_plan_threshold` rows.
- `:44-81` - commit-docs behavior examples using repo-local `gsd-tools.cjs`.
- `:162-176` - branching config examples using repo-local `gsd-tools.cjs`.
- `:219-307` - complete field reference, with `workflow.discuss_mode: "exploratory"` but missing several upstream field families.
- `:368-396` - team project example with `workflow.discuss_mode: "exploratory"`.

Current manifest entry:

```json
{
  "capability_id": "get-shit-done/references/planning-config.md",
  "parity_tier": "core_required",
  "materializers": {
    "codex": {
      "mode": "overwrite",
      "target": "get-shit-done/references/planning-config.md",
      "source": "tooling/portable-gsd/overlay/get-shit-done/references/planning-config.md"
    },
    "claude": {
      "mode": "overwrite",
      "target": "get-shit-done/references/planning-config.md",
      "source": "tooling/portable-gsd/overlay/get-shit-done/references/planning-config.md"
    }
  }
}
```

Manifest location: `tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json:461-476`.

Precise diff from upstream to current modifier source:

```diff
@@ -30,14 +30,12 @@
 | `search_gitignored` | `false` | Add `--no-ignore` to broad rg searches |
 | `git.branching_strategy` | `"none"` | Git branching approach: `"none"`, `"phase"`, or `"milestone"` |
 | `git.base_branch` | `null` (auto-detect) | Target branch for PRs and merges (e.g. `"master"`, `"develop"`). When `null`, auto-detects from `git symbolic-ref refs/remotes/origin/HEAD`, falling back to `"main"`. |
-| `git.create_tag` | `true` | Create git tags on milestone completion |
 | `git.phase_branch_template` | `"gsd/phase-{phase}-{slug}"` | Branch template for phase strategy |
 | `git.milestone_branch_template` | `"gsd/{milestone}-{slug}"` | Branch template for milestone strategy |
 | `git.quick_branch_template` | `null` | Optional branch template for quick-task runs |
 | `workflow.use_worktrees` | `true` | Whether executor agents run in isolated git worktrees. Set to `false` to disable worktrees — agents execute sequentially on the main working tree instead. Recommended for solo developers or when worktree merges cause issues. |
 | `workflow.subagent_timeout` | `300000` | Timeout in milliseconds for parallel subagent tasks (e.g. codebase mapping). Increase for large codebases or slower models. Default: 300000 (5 minutes). |
-| `workflow.inline_plan_threshold` | `2` | Plans with this many tasks or fewer execute inline (Pattern C) instead of spawning a subagent. Avoids ~14K token spawn overhead for small plans. Set to `0` to always spawn subagents. |
-| `manager.flags.discuss` | `""` | Flags passed to `/gsd:discuss-phase` when dispatched from manager (e.g. `"--auto --analyze"`) |
+| `manager.flags.discuss` | `""` | Flags passed to `/gsd-discuss-phase` when dispatched from manager (e.g. `"--auto --analyze"`) |
 | `manager.flags.plan` | `""` | Flags passed to plan workflow when dispatched from manager |
 | `manager.flags.execute` | `""` | Flags passed to execute workflow when dispatched from manager |
 | `response_language` | `null` | Language for user-facing questions and prompts across all phases/subagents (e.g. `"Portuguese"`, `"Japanese"`, `"Spanish"`). When set, all spawned agents include a directive to respond in this language. |
@@ -55,19 +53,19 @@
 - User must add `.planning/` to `.gitignore`
 - Useful for: OSS contributions, client projects, keeping planning private
 
-**Using `gsd-sdk query` (preferred):**
+**Using gsd-tools.cjs (preferred):**
 
 ```bash
 # Commit with automatic commit_docs + gitignore checks:
-gsd-sdk query commit "docs: update state" --files .planning/STATE.md
+node "__PROJECT_ROOT__/.codex/get-shit-done/bin/gsd-tools.cjs" commit "docs: update state" --files .planning/STATE.md
 
 # Load config via state load (returns JSON):
-INIT=$(gsd-sdk query state.load)
+INIT=$(node "__PROJECT_ROOT__/.codex/get-shit-done/bin/gsd-tools.cjs" state load)
 if [[ "$INIT" == @file:* ]]; then INIT=$(cat "${INIT#@file:}"); fi
 # commit_docs is available in the JSON output
 
 # Or use init commands which include commit_docs:
-INIT=$(gsd-sdk query init.execute-phase "1")
+INIT=$(node "__PROJECT_ROOT__/.codex/get-shit-done/bin/gsd-tools.cjs" init execute-phase "1")
 if [[ "$INIT" == @file:* ]]; then INIT=$(cat "${INIT#@file:}"); fi
 # commit_docs is included in all init command outputs
 ```
@@ -77,7 +75,7 @@
 **Commit via CLI (handles checks automatically):**
 
 ```bash
-gsd-sdk query commit "docs: update state" --files .planning/STATE.md
+node "__PROJECT_ROOT__/.codex/get-shit-done/bin/gsd-tools.cjs" commit "docs: update state" --files .planning/STATE.md
 ```
 
 The CLI checks `commit_docs` config and gitignore status internally — no manual conditionals needed.
@@ -165,14 +163,14 @@
 
 Use `init execute-phase` which returns all config as JSON:
 ```bash
-INIT=$(gsd-sdk query init.execute-phase "1")
+INIT=$(node "__PROJECT_ROOT__/.codex/get-shit-done/bin/gsd-tools.cjs" init execute-phase "1")
 if [[ "$INIT" == @file:* ]]; then INIT=$(cat "${INIT#@file:}"); fi
 # JSON output includes: branching_strategy, phase_branch_template, milestone_branch_template
 ```
 
 Or use `state load` for the config values:
 ```bash
-INIT=$(gsd-sdk query state.load)
+INIT=$(node "__PROJECT_ROOT__/.codex/get-shit-done/bin/gsd-tools.cjs" state load)
 if [[ "$INIT" == @file:* ]]; then INIT=$(cat "${INIT#@file:}"); fi
 # Parse branching_strategy, phase_branch_template, milestone_branch_template from JSON
 ```
@@ -227,7 +225,7 @@
 | Key | Type | Default | Allowed Values | Description |
 |-----|------|---------|----------------|-------------|
 | `model_profile` | string | `"balanced"` | `"quality"`, `"balanced"`, `"budget"`, `"inherit"` | Model selection preset for subagents |
-| `mode` | string | `"interactive"` | `"interactive"`, `"yolo"` | Operation mode: `"interactive"` shows gates and confirmations; `"yolo"` runs autonomously without prompts |
+| `mode` | string | (none) | `"code-first"`, `"plan-first"`, `"hybrid"` | Per-phase workflow mode controlling discuss/plan/execute flow |
 | `granularity` | string | (none) | `"coarse"`, `"standard"`, `"fine"` | Planning depth for phase plans (migrated from deprecated `depth`) |
 | `commit_docs` | boolean | `true` | `true`, `false` | Commit .planning/ artifacts to git (auto-false if .planning/ is gitignored) |
 | `search_gitignored` | boolean | `false` | `true`, `false` | Include gitignored paths in broad rg searches via `--no-ignore` |
@@ -235,9 +233,7 @@
 | `project_code` | string\|null | `null` | Any short string | Prefix for phase dirs (e.g. `"CK"` produces `CK-01-foundation`) |
 | `response_language` | string\|null | `null` | Any language name | Language for user-facing prompts (e.g., `"Portuguese"`, `"Japanese"`) |
 | `context_window` | number | `200000` | `200000`, `1000000` | Context window size; set `1000000` for 1M-context models |
-| `resolve_model_ids` | boolean\|string | `false` | `false`, `true`, `"omit"` | Map model aliases to full Claude IDs; `"omit"` returns empty string |
-| `context` | string\|null | `null` | `"dev"`, `"research"`, `"review"` | Execution context profile that adjusts agent behavior: `"dev"` for development tasks, `"research"` for investigation/exploration, `"review"` for code review workflows |
-| `review.models.<cli>` | string\|null | `null` | Any model ID string | Per-CLI model override for /gsd:review (e.g., `review.models.gemini`). Falls back to CLI default when null. |
+| `resolve_model_ids` | boolean\|string | `false` | `false`, `true`, `"omit"` | Map model aliases to full the agent IDs; `"omit"` returns empty string |
 
 ### Workflow Fields
 
@@ -249,35 +245,18 @@
 | `workflow.plan_check` | boolean | `true` | `true`, `false` | Run plan-checker agent to validate plans. _Alias:_ `plan_checker` is the flat-key form used in `CONFIG_DEFAULTS`; `workflow.plan_check` is the canonical namespaced form. |
 | `workflow.verifier` | boolean | `true` | `true`, `false` | Run verifier agent after execution |
 | `workflow.nyquist_validation` | boolean | `true` | `true`, `false` | Enable Nyquist-inspired validation gates |
-| `workflow.auto_prune_state` | boolean | `false` | `true`, `false` | Automatically prune old STATE.md entries on phase completion (keeps 3 most recent phases) |
 | `workflow.auto_advance` | boolean | `false` | `true`, `false` | Auto-advance to next phase after completion |
 | `workflow.node_repair` | boolean | `true` | `true`, `false` | Attempt automatic repair of failed plan nodes |
 | `workflow.node_repair_budget` | number | `2` | Any positive integer | Max repair retries per failed node |
-| `workflow.ai_integration_phase` | boolean | `true` | `true`, `false` | Run /gsd:ai-integration-phase before planning AI system phases |
 | `workflow.ui_phase` | boolean | `true` | `true`, `false` | Generate UI-SPEC.md for frontend phases |
 | `workflow.ui_safety_gate` | boolean | `true` | `true`, `false` | Require safety gate approval for UI changes |
 | `workflow.text_mode` | boolean | `false` | `true`, `false` | Use plain-text numbered lists instead of AskUserQuestion menus |
 | `workflow.research_before_questions` | boolean | `false` | `true`, `false` | Run research before interactive questions in discuss phase |
-| `workflow.discuss_mode` | string | `"discuss"` | `"discuss"`, `"assumptions"` | Default mode for discuss-phase: `"discuss"` runs interactive questioning; `"assumptions"` analyzes codebase and surfaces assumptions instead |
+| `workflow.discuss_mode` | string | `"exploratory"` | `"exploratory"`, `"discuss"`, `"assumptions"` | Default mode for discuss-phase steering behavior |
 | `workflow.skip_discuss` | boolean | `false` | `true`, `false` | Skip discuss phase entirely |
 | `workflow.use_worktrees` | boolean | `true` | `true`, `false` | Run executor agents in isolated git worktrees |
 | `workflow.subagent_timeout` | number | `300000` | Any positive integer (ms) | Timeout for parallel subagent tasks (default: 5 minutes) |
-| `workflow.inline_plan_threshold` | number | `2` | `0`-`10` | Plans with <=N tasks execute inline instead of spawning a subagent |
-| `workflow.code_review` | boolean | `true` | `true`, `false` | Enable built-in code review step in the ship workflow |
-| `workflow.code_review_depth` | string | `"standard"` | `"light"`, `"standard"`, `"deep"` | Depth level for code review analysis in the ship workflow |
 | `workflow._auto_chain_active` | boolean | `false` | `true`, `false` | Internal: tracks whether autonomous chaining is active |
-| `workflow.security_enforcement` | boolean | `true` | `true`, `false` | Enable threat-model-anchored security verification via `/gsd:secure-phase`. When `false`, security checks are skipped entirely |
-| `workflow.security_asvs_level` | number | `1` | `1`, `2`, `3` | OWASP ASVS verification level. Level 1 = opportunistic, Level 2 = standard, Level 3 = comprehensive |
-| `workflow.security_block_on` | string | `"high"` | `"high"`, `"medium"`, `"low"` | Minimum severity that blocks phase advancement |
-| `workflow.post_planning_gaps` | boolean | `true` | `true`, `false` | Post-planning gap report (#2493). After plans are generated, scans REQUIREMENTS.md and CONTEXT.md `<decisions>` against all PLAN.md files and emits a unified `Source \| Item \| Status` table. Non-blocking. Set to `false` to skip Step 13e of plan-phase. _Alias:_ `post_planning_gaps` is the flat-key form used in `CONFIG_DEFAULTS`; `workflow.post_planning_gaps` is the canonical namespaced form. |
-
-### Ship Fields
-
-Set via `ship.*` namespace in config.json. These fields affect `/gsd:ship` PRD-style pull request body composition only.
-
-| Key | Type | Default | Allowed Values | Description |
-|-----|------|---------|----------------|-------------|
-| `ship.pr_body_sections` | array | `[]` | Array of section objects | Append-only project-specific PR body sections. Each entry has `heading`, optional `enabled`, and one or more of `source`, `template`, or `fallback`. Disabled entries remain in onboarding config but do not render. Core sections remain required and cannot be removed or replaced. |
 
 ### Git Fields
 
@@ -287,7 +266,6 @@
 |-----|------|---------|----------------|-------------|
 | `git.branching_strategy` | string | `"none"` | `"none"`, `"phase"`, `"milestone"` | Git branching approach for phase/milestone isolation |
 | `git.base_branch` | string\|null | `null` (auto-detect) | Any branch name | Target branch for PRs and merges; auto-detects from `origin/HEAD` when `null` |
-| `git.create_tag` | boolean | `true` | `true`, `false` | Create git tags on milestone completion |
 | `git.phase_branch_template` | string | `"gsd/phase-{phase}-{slug}"` | Template with `{phase}`, `{slug}` | Branch naming template for `phase` strategy |
 | `git.milestone_branch_template` | string | `"gsd/{milestone}-{slug}"` | Template with `{milestone}`, `{slug}` | Branch naming template for `milestone` strategy |
 | `git.quick_branch_template` | string\|null | `null` | Template with `{slug}` | Optional branch template for quick-task runs |
@@ -309,7 +287,6 @@
 | Key | Type | Default | Allowed Values | Description |
 |-----|------|---------|----------------|-------------|
 | `features.thinking_partner` | boolean | `false` | `true`, `false` | Enable conditional extended thinking at workflow decision points (used by discuss-phase and plan-phase for architectural tradeoff analysis) |
-| `features.global_learnings` | boolean | `false` | `true`, `false` | Enable injection of global learnings from `~/.gsd/learnings/` into agent prompts |
 
 ### Hook Fields
 
@@ -319,29 +296,13 @@
 |-----|------|---------|----------------|
 | `hooks.context_warnings` | boolean | `true` | `true`, `false` | Show warnings when context budget is exceeded |
 
-### Learnings Fields
-
-Set via `learnings.*` namespace (e.g., `"learnings": { "max_inject": 5 }`). Used together with `features.global_learnings`.
-
-| Key | Type | Default | Allowed Values | Description |
-|-----|------|---------|----------------|-------------|
-| `learnings.max_inject` | number | `10` | Any positive integer | Maximum number of global learning entries to inject into agent prompts per session |
-
-### Intel Fields
-
-Set via `intel.*` namespace (e.g., `"intel": { "enabled": true }`). Controls the queryable codebase intelligence system consumed by `/gsd:map-codebase --query`.
-
-| Key | Type | Default | Allowed Values | Description |
-|-----|------|---------|----------------|-------------|
-| `intel.enabled` | boolean | `false` | `true`, `false` | Enable queryable codebase intelligence system. When `true`, `/gsd:map-codebase --query` builds and queries a JSON index in `.planning/intel/`. |
-
 ### Manager Fields
 
 Set via `manager.*` namespace (e.g., `"manager": { "flags": { "discuss": "--auto" } }`).
 
 | Key | Type | Default | Allowed Values | Description |
 |-----|------|---------|----------------|-------------|
-| `manager.flags.discuss` | string | `""` | Any CLI flags string | Flags passed to `/gsd:discuss-phase` from manager (e.g., `"--auto --analyze"`) |
+| `manager.flags.discuss` | string | `""` | Any CLI flags string | Flags passed to `/gsd-discuss-phase` from manager (e.g., `"--auto --analyze"`) |
 | `manager.flags.plan` | string | `""` | Any CLI flags string | Flags passed to plan workflow from manager |
 | `manager.flags.execute` | string | `""` | Any CLI flags string | Flags passed to execute workflow from manager |
 
@@ -422,7 +383,7 @@
     "verifier": true,
     "nyquist_validation": true,
     "use_worktrees": true,
-    "discuss_mode": "discuss"
+    "discuss_mode": "exploratory"
   },
   "manager": {
     "flags": {
```

## Proposed Manifest Entry (Candidate, Reviewer-Mediated)

This candidate intentionally does **not** preserve every deletion in the current overwrite. It preserves the local runtime/path and `discuss_mode` deltas while letting upstream-added field docs remain in the materialized file.

```json
"get-shit-done/references/planning-config.md": {
  "capability_id": "get-shit-done/references/planning-config.md",
  "parity_tier": "core_required",
  "parity_intent": "outcome_aligned",
  "materializers": {
    "codex": {
      "mode": "inject",
      "target": "get-shit-done/references/planning-config.md",
      "operations": [
        {
          "kind": "block_replace",
          "start_anchor": "- Useful for: OSS contributions, client projects, keeping planning private\n",
          "end_anchor": "**Auto-detection:** If `.planning/` is gitignored, `commit_docs` is automatically `false` regardless of config.json. This prevents git errors when users have `.planning/` in `.gitignore`.\n",
          "source": "harness_modifier/overlay/inject-sources/get-shit-done/references/planning-config/commit-docs-gsd-tools-body.md",
          "marker_key": "GSD_MODIFIER:references-planning-config:commit-docs-gsd-tools"
        },
        {
          "kind": "block_replace",
          "start_anchor": "**Commit via CLI (handles checks automatically):**\n",
          "end_anchor": "The CLI checks `commit_docs` config and gitignore status internally — no manual conditionals needed.\n",
          "source": "harness_modifier/overlay/inject-sources/get-shit-done/references/planning-config/commit-via-cli-body.md",
          "marker_key": "GSD_MODIFIER:references-planning-config:commit-via-cli"
        },
        {
          "kind": "block_replace",
          "start_anchor": "Use `init execute-phase` which returns all config as JSON:\n",
          "end_anchor": "Or use `state load` for the config values:\n",
          "source": "harness_modifier/overlay/inject-sources/get-shit-done/references/planning-config/init-execute-phase-command.md",
          "marker_key": "GSD_MODIFIER:references-planning-config:init-execute-phase-command"
        },
        {
          "kind": "block_replace",
          "start_anchor": "Or use `state load` for the config values:\n",
          "end_anchor": "**Branch creation:**\n",
          "source": "harness_modifier/overlay/inject-sources/get-shit-done/references/planning-config/state-load-command.md",
          "marker_key": "GSD_MODIFIER:references-planning-config:state-load-command"
        },
        {
          "kind": "block_replace",
          "start_anchor": "| `workflow.subagent_timeout` | `300000` | Timeout in milliseconds for parallel subagent tasks (e.g. codebase mapping). Increase for large codebases or slower models. Default: 300000 (5 minutes). |\n",
          "end_anchor": "| `manager.flags.plan` | `\"\"` | Flags passed to plan workflow when dispatched from manager |\n",
          "source": "harness_modifier/overlay/inject-sources/get-shit-done/references/planning-config/top-manager-discuss-row.md",
          "marker_key": "GSD_MODIFIER:references-planning-config:top-manager-discuss-row"
        },
        {
          "kind": "block_replace",
          "start_anchor": "Set via `manager.*` namespace (e.g., `\"manager\": { \"flags\": { \"discuss\": \"--auto\" } }`).\n",
          "end_anchor": "| `manager.flags.plan` | string | `\"\"` | Any CLI flags string | Flags passed to plan workflow from manager |\n",
          "source": "harness_modifier/overlay/inject-sources/get-shit-done/references/planning-config/manager-fields-discuss-row.md",
          "marker_key": "GSD_MODIFIER:references-planning-config:manager-fields-discuss-row"
        },
        {
          "kind": "block_replace",
          "start_anchor": "    \"use_worktrees\": true,\n",
          "end_anchor": "  },\n  \"manager\": {\n",
          "source": "harness_modifier/overlay/inject-sources/get-shit-done/references/planning-config/team-example-discuss-mode.md",
          "marker_key": "GSD_MODIFIER:references-planning-config:team-example-discuss-mode"
        }
      ]
    },
    "claude": {
      "mode": "inject",
      "target": "get-shit-done/references/planning-config.md",
      "operations": [
        {
          "kind": "block_replace",
          "start_anchor": "- Useful for: OSS contributions, client projects, keeping planning private\n",
          "end_anchor": "**Auto-detection:** If `.planning/` is gitignored, `commit_docs` is automatically `false` regardless of config.json. This prevents git errors when users have `.planning/` in `.gitignore`.\n",
          "source": "harness_modifier/overlay/inject-sources/get-shit-done/references/planning-config/commit-docs-gsd-tools-body.md",
          "marker_key": "GSD_MODIFIER:references-planning-config:commit-docs-gsd-tools"
        },
        {
          "kind": "block_replace",
          "start_anchor": "**Commit via CLI (handles checks automatically):**\n",
          "end_anchor": "The CLI checks `commit_docs` config and gitignore status internally — no manual conditionals needed.\n",
          "source": "harness_modifier/overlay/inject-sources/get-shit-done/references/planning-config/commit-via-cli-body.md",
          "marker_key": "GSD_MODIFIER:references-planning-config:commit-via-cli"
        },
        {
          "kind": "block_replace",
          "start_anchor": "Use `init execute-phase` which returns all config as JSON:\n",
          "end_anchor": "Or use `state load` for the config values:\n",
          "source": "harness_modifier/overlay/inject-sources/get-shit-done/references/planning-config/init-execute-phase-command.md",
          "marker_key": "GSD_MODIFIER:references-planning-config:init-execute-phase-command"
        },
        {
          "kind": "block_replace",
          "start_anchor": "Or use `state load` for the config values:\n",
          "end_anchor": "**Branch creation:**\n",
          "source": "harness_modifier/overlay/inject-sources/get-shit-done/references/planning-config/state-load-command.md",
          "marker_key": "GSD_MODIFIER:references-planning-config:state-load-command"
        },
        {
          "kind": "block_replace",
          "start_anchor": "| `workflow.subagent_timeout` | `300000` | Timeout in milliseconds for parallel subagent tasks (e.g. codebase mapping). Increase for large codebases or slower models. Default: 300000 (5 minutes). |\n",
          "end_anchor": "| `manager.flags.plan` | `\"\"` | Flags passed to plan workflow when dispatched from manager |\n",
          "source": "harness_modifier/overlay/inject-sources/get-shit-done/references/planning-config/top-manager-discuss-row.md",
          "marker_key": "GSD_MODIFIER:references-planning-config:top-manager-discuss-row"
        },
        {
          "kind": "block_replace",
          "start_anchor": "Set via `manager.*` namespace (e.g., `\"manager\": { \"flags\": { \"discuss\": \"--auto\" } }`).\n",
          "end_anchor": "| `manager.flags.plan` | string | `\"\"` | Any CLI flags string | Flags passed to plan workflow from manager |\n",
          "source": "harness_modifier/overlay/inject-sources/get-shit-done/references/planning-config/manager-fields-discuss-row.md",
          "marker_key": "GSD_MODIFIER:references-planning-config:manager-fields-discuss-row"
        },
        {
          "kind": "block_replace",
          "start_anchor": "    \"use_worktrees\": true,\n",
          "end_anchor": "  },\n  \"manager\": {\n",
          "source": "harness_modifier/overlay/inject-sources/get-shit-done/references/planning-config/team-example-discuss-mode.md",
          "marker_key": "GSD_MODIFIER:references-planning-config:team-example-discuss-mode"
        }
      ]
    }
  }
}
```

## Modifier Source Files

Candidate files:

- `harness_modifier/overlay/inject-sources/get-shit-done/references/planning-config/commit-docs-gsd-tools-body.md`
  - Body between the `commit_docs: false` use-case list and the auto-detection paragraph, replacing the upstream `gsd-sdk query` examples with repo-local `gsd-tools.cjs` examples.
- `harness_modifier/overlay/inject-sources/get-shit-done/references/planning-config/commit-via-cli-body.md`
  - Body under the "Commit via CLI" heading, replacing the single `gsd-sdk query commit` example.
- `harness_modifier/overlay/inject-sources/get-shit-done/references/planning-config/init-execute-phase-command.md`
  - Body under "Use `init execute-phase`", replacing the `gsd-sdk query init.execute-phase` example.
- `harness_modifier/overlay/inject-sources/get-shit-done/references/planning-config/state-load-command.md`
  - Body under "Or use `state load`", replacing the `gsd-sdk query state.load` example.
- `harness_modifier/overlay/inject-sources/get-shit-done/references/planning-config/top-manager-discuss-row.md`
  - Body preserving the upstream `workflow.inline_plan_threshold` row and replacing the top-table `manager.flags.discuss` row with `/gsd-discuss-phase`.
- `harness_modifier/overlay/inject-sources/get-shit-done/references/planning-config/manager-fields-discuss-row.md`
  - Body preserving the Manager Fields table header and replacing the `manager.flags.discuss` row with `/gsd-discuss-phase`.
- `harness_modifier/overlay/inject-sources/get-shit-done/references/planning-config/team-example-discuss-mode.md`
  - Body replacing the team-project example's `"discuss_mode": "discuss"` with `"discuss_mode": "exploratory"`.

No candidate source file is listed for the current modifier's broad omissions of upstream fields. The candidate deliberately lets those upstream rows and sections remain.

## Expected Materialized Content Sketch

With the seven-operation candidate, the materialized file would:

- Preserve upstream-added field documentation for `git.create_tag`, `workflow.inline_plan_threshold`, `workflow.auto_prune_state`, `workflow.ai_integration_phase`, `workflow.code_review*`, `workflow.security_*`, `workflow.post_planning_gaps`, `ship.pr_body_sections`, `features.global_learnings`, `learnings.max_inject`, and `intel.enabled`.
- Preserve upstream's `mode` row (`interactive` / `yolo`) rather than the current modifier's older `code-first` / `plan-first` / `hybrid` row.
- Replace the command examples that currently use `gsd-sdk query` with repo-local `gsd-tools.cjs` examples under marker regions.
- Replace both `/gsd:discuss-phase` manager-flag references with `/gsd-discuss-phase`.
- Replace the team-project example's `workflow.discuss_mode` value with `"exploratory"`.
- Add seven marker regions around the modifier-owned replacements.

Therefore the candidate is marker-clean and upstream-freshening, but not byte-for-byte equivalent to the existing overwrite.

## Preflight

Pure-function preflight against the real upstream content and the seven candidate operation bodies:

```text
records=[('block_replace', 'GSD_MODIFIER:references-planning-config:commit-docs-gsd-tools', 'applied'), ('block_replace', 'GSD_MODIFIER:references-planning-config:commit-via-cli', 'applied'), ('block_replace', 'GSD_MODIFIER:references-planning-config:init-execute-phase-command', 'applied'), ('block_replace', 'GSD_MODIFIER:references-planning-config:state-load-command', 'applied'), ('block_replace', 'GSD_MODIFIER:references-planning-config:top-manager-discuss-row', 'applied'), ('block_replace', 'GSD_MODIFIER:references-planning-config:manager-fields-discuss-row', 'applied'), ('block_replace', 'GSD_MODIFIER:references-planning-config:team-example-discuss-mode', 'applied')]
verify_passed=True
statuses=[('GSD_MODIFIER:references-planning-config:commit-docs-gsd-tools', 'verified'), ('GSD_MODIFIER:references-planning-config:commit-via-cli', 'verified'), ('GSD_MODIFIER:references-planning-config:init-execute-phase-command', 'verified'), ('GSD_MODIFIER:references-planning-config:state-load-command', 'verified'), ('GSD_MODIFIER:references-planning-config:top-manager-discuss-row', 'verified'), ('GSD_MODIFIER:references-planning-config:manager-fields-discuss-row', 'verified'), ('GSD_MODIFIER:references-planning-config:team-example-discuss-mode', 'verified')]
has_gsd_tools=True
has_upstream_security=True
has_upstream_ship=True
has_current_mode_row=False
has_upstream_mode_row=True
```

## Verification Approach

Slice 8 should not apply this carrier until the open questions below are resolved by Plan/slice-ambiguity review.

If a reviewer approves the upstream-freshening candidate, Slice 8 should run:

```bash
git diff --check
python3 tooling/codex/audit_refmap.py verify .
python3 harness_modifier/contract/portable_gsd_contract.py validate-manifest . --all-supported --source-only --strict
python3 -m unittest discover -s tooling/codex/tests -p 'test_inject*.py'
python3 -m unittest discover -s tooling/codex/tests
```

The full discover gate is expected to continue hitting the known non-carrier baseline until OOS #5 is addressed; if its failure shape changes or names `planning-config.md`, route through `gsd-debugger`.

## Rollback Plan

If Slice 8 proceeds and fails before commit:

1. Restore `tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json`.
2. Restore `tooling/portable-gsd/overlay/get-shit-done/references/planning-config.md`.
3. Remove the newly created `harness_modifier/overlay/inject-sources/get-shit-done/references/planning-config/` directory.
4. Rerun the failed Slice 8 gates.

If Slice 8 fails after commit, revert the single Slice 8 commit before writing the Phase 4 debrief.

## Open Questions

1. Should Slice 8 preserve the current overwrite byte-for-byte, including removal of upstream-added config fields, or should it intentionally use inject migration as the point where upstream-added field docs flow through?
2. Are the `gsd-tools.cjs` examples still the desired planning-config reference, given upstream's 2026-05-08 readiness note that `gsd-sdk query` is the canonical consumer surface but this repo still carries many repo-local `gsd-tools.cjs` workflow calls?
3. Should the current modifier's `mode` row (`code-first` / `plan-first` / `hybrid`) be treated as stale and dropped in favor of upstream (`interactive` / `yolo`), as the candidate does, or should it be preserved through a separate operation?
