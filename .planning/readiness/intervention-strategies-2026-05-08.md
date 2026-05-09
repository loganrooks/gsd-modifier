# Intervention Strategies for the gsd-modifier Overlay

Date: 2026-05-08
Repo: `/home/rookslog/workspace/projects/gsd-modifier`
Upstream reference: `/home/rookslog/workspace/projects/get-shit-done-upstream` (`origin/main` HEAD `96806003`, latest tag `v1.41.0`).
Status: read-only analysis, no source/manifest/contract changes proposed inline.
Companion: `release-readiness-orientation-2026-05-08.md` (read first; this artifact assumes its drift findings).

This is a snapshot strategy artifact, not a current-state authority.
Author obligations:
- "Observed" claims cite a file:line, manifest entry, upstream commit, or doc section.
- "Inferred" claims are explicitly marked.
- The author DID NOT execute build/install/test; all dynamic claims rest on code reading.

---

## 0. Executive summary (read first)

1. **The overlay overwrites because of three orthogonal pressures.** Path style (`@~/.claude/...` → `@__PROJECT_ROOT__/.codex/...`), section additions (modifier-specific `<supporting_reading>`/`<deeper_reading>`), and a small set of behavior-class changes (extra steps like `keep_route_boundaries_explicit`, removed steps like `--backfill`/`--context`). Of the three, only the third truly requires body-level intervention; the other two could be handled by patch-style materializers.

2. **Upstream already knows how to rewrite for codex.** `bin/install.js` runs `convertClaudeToCodexMarkdown()` (file `bin/install.js:2199-2224`) which converts `/gsd-foo` → `$gsd-foo`, `~/.claude/...` → `~/.codex/...`, `$ARGUMENTS` → `{{GSD_ARGS}}`, and `Claude` → `the agent`. The modifier overlay carries the **post-conversion** form, which means the overlay duplicates work upstream already does and goes silently stale when upstream refines its conversion or fixes a bug in either the source or the converter.

3. **Section consumption is bimodal.** The SDK runtime parses `<purpose>`, `<process>`, `<step name="...">` (in workflow files via `phase-prompt.ts`) and `<objective>`, `<execution_context>`, `<context>`, `<task>` (in PLAN.md via `plan-parser.ts`). Everything else — `<required_reading>`, `<supporting_reading>`, `<deeper_reading>`, `<runtime_note>`, `<purpose>`, `<role>`, `<codex_skill_adapter>` — is **pure LLM prompt content**. The modifier's added sections work because the LLM reads them, not because any parser activates on them. This means injection-style additions are viable for those tag types but require the host workflow to either invoke them ("read the supporting_reading block") or place them where the LLM scans naturally.

4. **The overwrite-heavy posture has produced concrete staleness.** Three skills (§4.2 of orientation), substantial behavior drift in `bin/lib/state.cjs` (779-line diff, includes a new `computeProgressPercent` function the modifier overwrites away), and missing #3242 progress-percent calculation. A patch-style materializer would have picked up additive upstream changes automatically.

5. **The recommended migration is asymmetric.** Most workflow-file overlays (~16 of 24) can move to injection/include archetypes with manageable contract-tool changes. About 5–8 carriers (`do.md`, `plant-seed.md`, `health.md`, `update.md`, possibly `progress.md`) have step-level removals or restructurings that need either a richer patch operation set ("remove `<step name="context_check">`") or genuine overwrite. CJS lib files (5) cannot use markdown-style injection at all — they need a different mechanism (require()-time monkey-patch, plugin extension point, or upstream PR). Templates and references (10 carriers) can largely move to injection with simple block-replace operations.

---

## 1. Active premise check — current materialization model

### 1.1 Manifest enumeration by archetype-of-record

`OVERLAY-MANIFEST.json` contains 67 entries (schema_version 3). Below is the cross-tabulation of `parity_tier` × dominant materialization mode (across both runtimes for `core_required` / `core_adapted` carriers; codex-only for `runtime_specific`).

| `parity_tier` | mode: overwrite | mode: add | Total |
|---|---:|---:|---:|
| `core_required` | 41 | 5 | 46 |
| `core_adapted` | 0 | 3 | 3 |
| `runtime_specific` | 8 | 10 | 18 |
| **Total** | **49** | **18** | **67** |

(Counts derived from reading `OVERLAY-MANIFEST.json:1-1133`.)

### 1.2 Carrier-class breakdown of the 49 overwrites

Observed by reading the manifest:

| Carrier class | Count | parity_tier | Examples |
|---|---:|---|---|
| Workflow `.md` (overwrite) | 22 | `core_required` | `new-project.md`, `discuss-phase.md`, `plan-phase.md` |
| Reference `.md` (overwrite) | 5 | `core_required` | `agent-contracts.md`, `mandatory-initial-read.md`, `planner-reviews.md`, `planning-config.md`, `verification-overrides.md` |
| Template `.md`/`.json` (overwrite) | 7 | `core_required` | `phase-prompt.md`, `verification-report.md`, `config.json`, `state.md` |
| Agent `.md` (overwrite) | 4 | `core_required` | `gsd-code-fixer.md`, `gsd-code-reviewer.md`, `gsd-intel-updater.md`, `gsd-pattern-mapper.md` |
| `bin/lib/*.cjs` (overwrite) | 5 | `core_required` | `audit.cjs`, `config.cjs`, `phase.cjs`, `roadmap.cjs`, `state.cjs` |
| Skill `SKILL.md` (overwrite, codex-only) | 8 | `runtime_specific` | `gsd-discuss-phase`, `gsd-do`, `gsd-explore`, `gsd-from-gsd2`, `gsd-health`, `gsd-plan-phase`, `gsd-plant-seed`, `gsd-resume-work`, `gsd-review`, `gsd-update` |

(Note: skill counts in the table sum to 10 because two are overwrite-mode `runtime_specific`; the 8 above plus add-mode `gsd-progress` and `gsd-rigorous-research` which are different rows.)

### 1.3 Carrier-class breakdown of the 18 adds

| Carrier class | Count | parity_tier | Notes |
|---|---:|---|---|
| Reference `.md` (add) | 2 | `core_required` | `entry-runtime-uplift-continuity.md`, `milestone-boundary-uplift-continuity.md`. Added at `mode: add` even though modifier overwrites the surrounding workflows; reached via `@`-include from those workflows. |
| Generator wrapper | 1 | `core_required` | `bin/generate-instruction.cjs` — the runtime-neutral wrapper. Plan 004 disposition in §3 of orientation. |
| Skill `SKILL.md` (add, codex-only) | 1 | `runtime_specific` | `gsd-progress` (the only mode-add codex skill that doesn't have an upstream `commands/gsd/progress.md` prefix mismatch — actually it does exist upstream; this is a curious classification — see §1.6 below). |
| Skill `SKILL.md` net-new modifier | 1 | `runtime_specific` | `gsd-rigorous-research` + 3 `references/*.md` |
| Agent `.toml` (add, codex-only) | 7 | `runtime_specific` | `gsd-code-fixer.toml`, `gsd-code-reviewer.toml`, `gsd-executor.toml`, `gsd-intel-updater.toml`, `gsd-pattern-mapper.toml`, `gsd-phase-researcher.toml`, `gsd-plan-checker.toml`, `gsd-planner.toml`, `gsd-verifier.toml` |
| `entrypoints/*` net-new modifier | 3 | `core_adapted` | `gsd-propagation-review`, `gsd-seed-migration-inventory`, `gsd-uplift-project` (each with both codex and claude materializers, sourced from `harness_modifier/overlay/`) |
| `compact-prompts/*.md` | 2 | `runtime_specific` | `project.md`, `readiness.md` (codex-only) |
| Workflow `.md` (add, modifier-owned) | 3 | `core_required` | `propagation-review.md`, `seed-migration-inventory.md`, `uplift-project.md` (sourced from `harness_modifier/overlay/...`) |
| `config.toml` (add, codex-only) | 1 | `runtime_specific` | Codex top-level config |

### 1.4 Inconsistency check — `mode: overwrite` against upstream presence

Cross-check via `git ls-tree origin/main` (read in this pass):

| Path | Manifest mode | Upstream `origin/main` presence | Disposition |
|---|---|---|---|
| `agents/gsd-code-fixer.md` | overwrite | present (`agents/gsd-code-fixer.md`) | aligned |
| `agents/gsd-code-reviewer.md` | overwrite | present | aligned |
| `agents/gsd-intel-updater.md` | overwrite | present | aligned |
| `agents/gsd-pattern-mapper.md` | overwrite | present | aligned |
| All 22 overwrite workflow `.md` | overwrite | present (verified subset: new-project, discuss-phase, plan-phase, health, update, progress, do, plant-seed, research-phase) | one stale: `research-phase.md` is missing from upstream `origin/main` (was deleted) |
| All 5 reference `.md` | overwrite | present | aligned |
| All 7 templates | overwrite | present | aligned |
| 5 lib `.cjs` | overwrite | present | aligned (but content drift; see §4.7) |
| `skills/gsd-do/SKILL.md` | overwrite, codex-only | upstream has `commands/gsd/do.md` deleted; for codex install upstream installer **converts `commands/gsd/*.md` → `skills/gsd-*/SKILL.md`** at install time. So overlay overwrites a file upstream synthesizes. After deletion (#2790), upstream no longer synthesizes for `do.md`. | **stale-deleted** |
| `skills/gsd-from-gsd2/SKILL.md` | overwrite, codex-only | same | **stale-deleted** |
| `skills/gsd-plant-seed/SKILL.md` | overwrite, codex-only | same | **stale-deleted** |

**Stale-deleted `mode: overwrite` carriers**: 3 confirmed (`gsd-do`, `gsd-from-gsd2`, `gsd-plant-seed`). 1 stale-deleted workflow (`get-shit-done/workflows/research-phase.md`) — modifier overlay declares overwrite, but `git ls-tree origin/main get-shit-done/workflows/research-phase.md` returns nothing (verified).

### 1.5 The "research-phase.md" finding (newly surfaced this pass)

Verified: `cd ~/workspace/projects/get-shit-done-upstream && git ls-tree origin/main get-shit-done/workflows/research-phase.md` returns empty. The upstream workflow file does not exist. Modifier overlay declares `mode: overwrite, parity_tier: core_required` for both runtimes (`OVERLAY-MANIFEST.json:738-753`). This means:

- For codex install: upstream installer copies `get-shit-done/workflows/*.md`. Without `research-phase.md` upstream, the modifier overlay's `apply-overlay` step writes a file upstream did not place. This **works** because `apply-overlay` does `target.write_text(...)` regardless (`portable_gsd_contract.py:687`).
- For claude install: same.
- The `verify-materialized` step would not catch this because it only checks `live_path.exists()` against the modifier's source — both exist after apply-overlay (`portable_gsd_contract.py:756-770`).

**Inferred**: the overlay carries a workflow file that upstream removed. Consequence is similar to the §4.2 stale-deleted skills — modifier ships content that no longer aligns with upstream's surface. Does not block functionality, does mean the modifier has implicitly become the canonical source for `research-phase.md`. See §4 for archetype recommendation.

### 1.6 The "gsd-progress" curiosity

Manifest declares `skills/gsd-progress/SKILL.md` as `mode: add, codex-only` (`OVERLAY-MANIFEST.json:991-1001`). Upstream has both `commands/gsd/progress.md` (the source) and synthesizes `skills/gsd-progress/SKILL.md` for codex installs via `convertClaudeCommandToCodexSkill()` (`bin/install.js:2282-...`). So an `add`-mode entry should fail the manifest validation rule "add entries must NOT be in backup-meta" since upstream-installed paths land in `backup-meta.json` via the `capture-pristine-overwrites` step.

**Observed**: the file `gsd-progress/SKILL.md` is in `tooling/portable-gsd/overlay/skills/gsd-progress/SKILL.md` (not `harness_modifier/overlay/...`) and uses `mode: add` despite upstream synthesizing the same target path during install.

This is either:
- a manifest declaration bug (should be `mode: overwrite`), or
- a deliberate "the overlay version is the canonical one and we accept silent overwriting of the upstream synthesis" decision.

Either way it's worth flagging. Inference: most likely a declaration bug. Verification by running `validate-manifest --strict --runtime codex` is recommended; but that's state-mutating against backup-meta and out of read-only scope.

### 1.7 Summary of premise check

| Finding | Class |
|---|---|
| 49 overwrites, 18 adds, mostly `core_required` | observed |
| 22 of 24 workflow files use overwrite (the 2 modifier-net-new use add) | observed |
| 3 stale-deleted skill carriers (orientation §4.2) | observed (cross-checked) |
| 1 stale-deleted workflow carrier (`research-phase.md`) | observed (newly surfaced) |
| `gsd-progress` declared mode: add but upstream synthesizes the same path | observed (likely a declaration bug, inferred) |
| Substantial line-level divergence between modifier and upstream copies (e.g., new-project.md: 283 diff lines, lib/state.cjs: 779 diff lines, agents/gsd-code-fixer.md: 269 diff lines) | observed |

---

## 2. Inventory of upstream extension mechanisms

Read sources (all verified to exist on `origin/main`):
- `docs/CONFIGURATION.md`, `docs/USER-GUIDE.md`, `docs/CLI-TOOLS.md`, `docs/COMMANDS.md`, `docs/ARCHITECTURE.md` (all present)
- `sdk/src/query/QUERY-HANDLERS.md` (the query layer doc)
- `bin/install.js` (the per-runtime path/syntax converter)
- `sdk/src/phase-prompt.ts`, `sdk/src/plan-parser.ts` (the runtime parsers)
- `sdk/src/query/profile-output.ts` (the `generate-claude-md` SDK handler)
- `hooks/` (all hook files)
- `commands/gsd/*.md`, `agents/*.md` (file format references)

NOT present on origin/main (verified): `docs/HOOKS.md`, `docs/EXTENDING.md`, `docs/CUSTOMIZATION.md`, `references/EXTENDING.md`. Hook documentation lives partially in `docs/issue-driven-orchestration.md`, README, and the install.js inline comments. **There is no first-class extension API doc.**

### 2.1 The `@`-include resolver

**Path/syntax**: lines starting with `@~/.claude/...` (claude install path) or `@__PROJECT_ROOT__/.codex/...` (modifier-rewritten codex install path), generally on their own line inside an XML section (`<required_reading>`, `<supporting_reading>`, `<execution_context>`).

**Consumer**:
1. **Runtime-parser branch** (LIMITED): `sdk/src/plan-parser.ts:336-356` (`extractContextRefs`, `extractExecutionContext`) extracts `@`-prefixed lines from `<context>` and `<execution_context>` blocks **of PLAN.md files only**, returning them as `string[]` for the prompt builder to treat as file references. **Workflow-file `@`-includes are NOT runtime-parsed** by the SDK.
2. **LLM-consumer branch** (DOMINANT): the agent (Claude Code, Codex CLI, etc.) reads the workflow file as part of skill/command invocation. The runtime's own `@`-syntax then triggers automatic file inclusion — Claude Code's `@filepath` convention, Codex's equivalent. This is **runtime-managed**, not SDK-managed.

**Limitations**:
- The `@`-resolver expects **literal paths** at install time. Modifier substitutes `__PROJECT_ROOT__` → absolute path during `apply-overlay` (`portable_gsd_contract.py:175-176`). After substitution the file on disk has, e.g., `@/home/user/repo/.codex/get-shit-done/references/...`, which is the actual path Claude/Codex will resolve.
- No content-addressing — if the target file content changes after install, the `@`-include silently picks up the new content. (This is a feature for refreshable references.)
- No conditional include — can't say "include this only if X". The XML section context becomes the conditioning hint to the LLM.

**Stable extension API or implementation detail?** Inferred to be a **stable convention**. Upstream's many usages (`git grep '^@~/.claude'` → 40+ workflows, 111 `commands/gsd/*.md`) and explicit conversion logic in `install.js:2210-2217` (path rewriting per runtime) suggest deliberate design. Not formally documented as an extension API.

### 2.2 The HTML-comment marker injection model

**Path/syntax**: `<!-- GSD:<section>-start source:<file> -->` ... `<!-- GSD:<section>-end -->` markers in markdown files, used by `generate-claude-md` (upstream) and `generate-instruction.cjs` (modifier wrapper).

**Consumer**: the SDK handler `generateClaudeMd` (`sdk/src/query/profile-output.ts:774-...`) reads the existing `CLAUDE.md`/`AGENTS.md`, finds the markers via `indexOf('<!-- GSD:<name>-start')`, and replaces only the marker-bounded region. The modifier wrapper (`generate-instruction.cjs:212-228`) does the same.

**Section names actually managed**: 
- Upstream: `project`, `stack`, `conventions`, `architecture`, `skills`, `workflow`, `profile` (`profile-output.ts:779, 808`).
- Modifier: same six plus the same profile placeholder (`generate-instruction.cjs:13`).

**Limitations**:
- Currently used **only** for project instruction file (CLAUDE.md / AGENTS.md). Not used elsewhere in the codebase (verified `git grep '<!-- GSD:'` in upstream returns hits only in `profile-output.ts` and tests).
- Section names are hard-coded — there's no generic injection registry.
- No idempotency check at the marker level except by content equality. The `--auto` flag on `generate-claude-md` (`profile-output.ts:874-884`) enables a `detectManualEdit` check that skips refreshing sections the user manually changed — so there IS a basic divergence-detection model, just no marker-level rollback or rebase machinery.

**Stable extension API or implementation detail?** Inferred to be **near-stable**. The marker syntax has been stable since the file was created (no breaking changes in observable git history); section names are hard-coded so adding a new section requires a code change. Treated as an implementation detail of one specific generator.

### 2.3 The `<process>` / `<step>` workflow parser

**Path/syntax**: `<process>...</process>` containing `<step name="X">...</step>` blocks. Used by `phase-prompt.ts:42-65` (`extractBlock`, `extractSteps`).

**Consumer**: the `PromptFactory.buildPrompt` (`phase-prompt.ts:114-170`) reads the workflow file for the active phase type, extracts `<purpose>`, `<process>`, then `<step>` blocks, and assembles them into the executor prompt as cacheable prefix sections.

**Limitations**:
- Only `<purpose>`, `<process>`, and `<step>` are extracted. Other XML sections (`<required_reading>`, `<supporting_reading>`, `<deeper_reading>`, `<runtime_note>`, `<auto_mode>`, `<execution_context>`) are **not** parsed by the SDK at workflow-prompt-build time.
- Workflow files are loaded by phase-type mapping (`PHASE_WORKFLOW_MAP` at `phase-prompt.ts:30-37`). New phase types require adding to this map plus a `PhaseType` enum value.

**Stable extension API or implementation detail?** Inferred **internal implementation detail**. The extractor is part of the SDK; adding a new section name to be parsed requires code change. The fact that there is documentation in `sdk/src/query/QUERY-HANDLERS.md` about query handler conventions but not about workflow section conventions reinforces this.

### 2.4 The agent file format

**Path/syntax**: `agents/<name>.md` with YAML frontmatter (claude format, `name`/`description`/`tools`/`color`/`hooks`) plus markdown body containing `<role>`, `<philosophy>`, `<task_breakdown>`, `<plan_format>`, `<execution_flow>`, `<scope_estimation>`, `<context_fidelity>`, `<checkpoints>`, etc.

**Consumer**: `phase-prompt.ts:131-141` strips the frontmatter (`stripYamlFrontmatter`) and includes the **whole body** as `## Agent Instructions` in the cacheable prompt prefix. Comments at `phase-prompt.ts:131-134` explain: "Include the complete agent definition (minus YAML frontmatter), not just the `<role>` block. The real agents have critical instructions in sections like `<philosophy>`, `<task_breakdown>`, ... etc."

**Limitations**:
- Whole-body inclusion means any modifier-side wrapper or addition shows up verbatim in the prompt.
- For codex installs, the upstream installer converts agent .md → agent .toml format (`convertClaudeAgentTo*` family functions in install.js), wrapping the body inside `developer_instructions = '''...'''` triple-quote string. So the modifier's agent .toml files (the 7 `mode: add, runtime_specific` carriers) are codex-format mirrors of agent .md content.
- The `<codex_agent_role>` block the modifier injects (e.g., `agents/gsd-pattern-mapper.md`) is added by the modifier in the .md form. Upstream's installer would have generated something equivalent on its own — modifier overlay overrides this.

**Stable extension API or implementation detail?** Frontmatter format is **stable** (documented per skill-format conventions in install.js logic and tests). XML section names are convention but not parsed — they are LLM prompt content.

### 2.5 The skill (slash-command) file format

**Path/syntax**: `commands/gsd/<name>.md` (the canonical claude form upstream) with YAML frontmatter (`name: gsd:foo`, `description`, `argument-hint`, `allowed-tools`) plus body containing `<objective>`, `<execution_context>`, `<runtime_note>`, `<context>`, `<process>`. Codex install converts to `skills/gsd-<name>/SKILL.md` via `convertClaudeCommandToCodexSkill()` (`bin/install.js:2282`).

**Consumer**: 
- The runtime (Claude Code, Codex CLI, etc.) reads slash-command files at startup, registers the slash command, presents the description in command pickers.
- The body of the command file is what the LLM sees when the user invokes the slash command.

**Limitations**:
- Slash-command files are listed in the system prompt at runtime startup (see USER-GUIDE.md "Namespace routing primer" — `~120 tokens` for 6 routers vs `~2,150` for flat 86-skill listing). Adding skills increases prompt-time cost; the namespace-meta-skills (#2792) addressed this.
- Codex skill format requires `<codex_skill_adapter>` block (added by upstream installer for codex-installed skills via `convertClaudeCommandToCodexSkill`). Modifier overlay copies carry this block manually.

**Stable extension API or implementation detail?** Skill-file format is **stable across versions**. The set of fields and the conversion rules are well-tested (`tests/qwen-install.test.cjs`, `tests/codebuddy-install.test.cjs`, etc.).

### 2.6 The hook system (`hooks/`)

**Path/syntax**: 12 hook scripts in `hooks/` directory, dispatched by claude-code/codex hook runner. PostToolUse, PreToolUse, etc.

**Consumer**: claude-code or codex runtime fires hooks on declared events. The hook scripts in `hooks/` are general-purpose.

**Limitations**:
- Adding new hooks requires editing the runtime's settings.json (claude) or config.toml (codex). For codex, this is the `[[hooks.<Event>]]` block. The upstream installer manages this in `bin/install.js`.
- Hook events are runtime-defined — modifier cannot invent a new event type.
- Hooks fire on actions (PostToolUse), not on workflow points. There's no "PostWorkflowSection" hook the modifier could subscribe to.

**Stable extension API or implementation detail?** **Stable for runtime-defined events**, but invocation context is constrained to what the agent runtime exposes.

### 2.7 The SDK query handler layer (`sdk/src/query/`)

**Path/syntax**: TypeScript handlers in `sdk/src/query/<name>.ts`, registered via `createRegistry()` (`sdk/src/query/index.ts`). Reachable via `gsd-sdk query <command-name>` from workflow body.

**Consumer**: workflow body shells call out — `RES=$(gsd-sdk query init.new-project)` etc.

**Limitations**:
- Adding a query handler requires SDK-side TypeScript code change. Modifier cannot inject a query handler without forking the SDK.
- Query handlers must conform to `QueryHandler` interface (`sdk/src/query/utils.ts`).
- CJS fallback (`gsd-tools.cjs`) is being deprecated (#2791); modifier must lean on SDK going forward.

**Stable extension API or implementation detail?** **Stable for consumers of `gsd-sdk query <name>`**, but adding new query handlers is internal. From outside upstream, the only way to add a query handler is fork-and-rebuild.

### 2.8 The `__PROJECT_ROOT__` placeholder

**Path/syntax**: literal string `__PROJECT_ROOT__` in any overlay file; substituted by `render_overlay_text` in `harness_modifier/contract/portable_gsd_contract.py:175-176` to the absolute path of the repo at install time. This is **modifier-only** — upstream's `install.js` does not handle this placeholder.

**Consumer**: substitution is install-time only. Post-substitution the file is on-disk normal text.

**Stable extension API**: this is an **internal modifier convention**, not a published mechanism. It's also a one-off — only `__PROJECT_ROOT__` and `__COMPACT_PROMPT_FILE__` are recognized. An injection-style materializer would benefit from a richer template-variable model.

### 2.9 The install-time runtime adapter family in `bin/install.js`

This is the most relevant prior art for what the modifier is partially duplicating.

**File**: `bin/install.js` (~5000 lines). Key functions:
- `convertClaudeToCodexMarkdown(content)` — `bin/install.js:2199-2224`: runs `convertSlashCommandsToCodexSkillMentions`, removes `/clear` references, rewrites `~/.claude/...` → `~/.codex/...`, `$ARGUMENTS` → `{{GSD_ARGS}}`, calls `neutralizeAgentReferences` (replaces "Claude" → "the agent", "CLAUDE.md" → "AGENTS.md" — `bin/install.js:4611-4622`).
- `convertSlashCommandsToCodexSkillMentions(content)` — `bin/install.js:2185-2197`: regex-rewrites `/gsd-foo`, `/gsd:foo` → `$gsd-foo`.
- `convertClaudeCommandToCodexSkill(content, skillName)` — `bin/install.js:2282-...`: skill-specific wrapping (adds the `<codex_skill_adapter>` block).
- Equivalent families for: gemini (colon-form), copilot, antigravity, cursor, windsurf, augment, trae, qwen, hermes, codebuddy, cline. 14 runtimes total.

**Implication**: upstream **already** does extensive runtime-specific rewriting of source content. The modifier overlay is materializing **post-conversion** content directly, which means:
1. Modifier doesn't have to re-run conversion (duplicate work avoided).
2. Modifier IS exposed to upstream changes in either the source content OR the converter — both can drift the modifier copy silently.
3. If upstream adds a new conversion rule (e.g., #2855 standardized slash-command form), the modifier copy doesn't pick it up.

**Stable extension API**: not exposed. These are internal conversion functions. If the modifier moved to a patch-style materializer that runs **before** upstream conversion (or inserts content into the source files), upstream's converters would handle the rewriting on each install.

### 2.10 The CHANGELOG entries cited in the prompt

| PR | Subject | Read result |
|---|---|---|
| #2792 | Namespace meta-skills (`gsd:workflow`, `gsd:project`, `gsd:review`, `gsd:context`, `gsd:manage`, `gsd:ideate`) | Documented in `docs/USER-GUIDE.md:35-46`. Modifier hasn't adopted; not in overlay. |
| #2762 | `--minimal` install flag | Referenced in install.js logic (`hasMinimal = args.includes('--minimal') || args.includes('--core-only')`); the `MINIMAL_SKILL_ALLOWLIST` from `install-profiles.cjs`. Modifier `parity_tier` taxonomy doesn't intersect with `--minimal` yet. |
| #2790 | Skill consolidation 86 → 59 | Confirmed: upstream `commands/gsd/{do,from-gsd2,plant-seed,...}.md` deleted. Modifier overlay's stale-deleted skills are the consequence. |
| #2824 | Continued skill consolidation | Same as above. |
| #2406 | `gsd-read-injection-scanner` PostToolUse hook | File `hooks/gsd-read-injection-scanner.js` present in `git ls-tree origin/main hooks/`. Modifier doesn't carry it (would need declaration to be installed for codex). |

### 2.11 Summary table — which mechanism for which intervention

| If modifier wants to... | Best mechanism today | Modifier currently uses |
|---|---|---|
| Add a top-of-file include to a workflow body | `<supporting_reading>` block with `@__PROJECT_ROOT__/.codex/...` ref + a `mode: add` reference file | Overwrite the whole workflow file |
| Add a new step to a workflow's `<process>` | None native; SDK reads only `<purpose>` / `<step>` from `<process>`. Either inject `<step>` into existing `<process>` (whole-section replace required to maintain bounds) OR genuine overwrite | Overwrite the whole workflow file |
| Replace one section (e.g., `<step name="parse_args">`) | None native. Closest analog is HTML-comment markers used in CLAUDE.md/AGENTS.md only | Overwrite the whole workflow file |
| Add a net-new workflow | `mode: add` works as-is; just needs an upstream "register the new slash command" path | Already used (`propagation-review.md`, etc.) |
| Add a net-new skill | `mode: add` works as-is | Already used (`gsd-rigorous-research`, `gsd-propagation-review`) |
| Change codex installer behavior (e.g., new conversion rule) | Patch upstream `bin/install.js`; no extension API | Workaround: modifier overrides post-conversion artifacts |
| Inject a query handler | Patch upstream `sdk/src/query/`; no extension API | Workaround: invoke a separate CJS wrapper (the `generate-instruction.cjs` pattern) |
| Add a hook | Modify install settings.json/config.toml entries | Modifier doesn't currently add hooks |

---

## 3. Decorative-section risk validation

Question from the user: do arbitrary `<gsd_modifier_uplift>` style sections in upstream files get honored or ignored?

### 3.1 Methodology

Selected representative workflow files: `new-project.md`, `discuss-phase.md`, `plan-phase.md`, `health.md`, `update.md`, `progress.md`, `do.md`. For each XML section observed in modifier and upstream, traced the consumer.

### 3.2 Section-name → consumer table

| Section | Consumer | Cite |
|---|---|---|
| `<purpose>` | LLM prompt (extracted by `phase-prompt.ts:153-155` into `## Purpose` for executor prompts; otherwise plain LLM read) | `phase-prompt.ts:42-46`, `153-155` |
| `<process>` | Runtime parser (the SDK's `extractBlock` then `extractSteps`); **only effective for the 5 mapped phase types** (Execute, Research, Plan, Verify, Discuss, Repair) | `phase-prompt.ts:30-37`, `159-167` |
| `<step name="X">` | Runtime parser (extracted from `<process>` for the phase types above); also LLM read in all other workflows | `phase-prompt.ts:48-65` |
| `<required_reading>` | LLM prompt only — NOT runtime-parsed by SDK | confirmed via `git grep required_reading sdk/` returning zero hits |
| `<supporting_reading>` | LLM prompt only — NOT runtime-parsed by SDK | `git grep supporting_reading sdk/` returns zero hits |
| `<deeper_reading>` | LLM prompt only — NOT runtime-parsed by SDK | (same) |
| `<execution_context>` | Runtime parser **for PLAN.md only** (extracted by `plan-parser.ts:336-356`); LLM prompt for workflow files (since workflow files don't go through `parsePlan`) | `plan-parser.ts:336-356`, `phase-prompt.ts:1-50` does not extract this from workflow files |
| `<context>` | Runtime parser **for PLAN.md only** (extracted by `plan-parser.ts:325-335`); LLM prompt for skill `commands/gsd/*.md` files | `plan-parser.ts:320-335` |
| `<task>` | Runtime parser for PLAN.md (extracted by `plan-parser.ts:parseTasks`); LLM prompt elsewhere | `plan-parser.ts:404-410` |
| `<role>` | LLM prompt only (SDK includes whole agent body, not just `<role>`) | `phase-prompt.ts:131-141` (deliberate: "include the complete agent definition (minus YAML frontmatter), not just the `<role>` block") |
| `<runtime_note>` | LLM prompt only | confirmed by absence in SDK code |
| `<codex_skill_adapter>` | LLM prompt; rendered by upstream installer via `convertClaudeCommandToCodexSkill` for codex-target skills | `bin/install.js:2236-2280` (the inline TEMPLATE constant within `convertClaudeCommandToCodexSkill`) |
| `<auto_mode>` | LLM prompt only | absent in SDK |
| `<objective>` | Runtime parser for PLAN.md (`extractBlock` of 'objective' in `plan-parser.ts:404`); LLM prompt elsewhere | `plan-parser.ts:404` |
| `<must_haves>` | Runtime parser for PLAN.md frontmatter (`parseMustHaves`); not an XML block | `plan-parser.ts:380-398` |
| `<gsd_modifier_uplift>` (hypothetical) | None native — would be pure LLM prompt content | n/a |

### 3.3 The decorative-section risk

The user's specific concern was whether arbitrary `<gsd_modifier_uplift>` sections in upstream workflow files would be ignored.

**Answer**: yes for the SDK runtime parser — it only knows `<purpose>`, `<process>`, `<step>`, and (for PLAN.md) `<objective>`, `<execution_context>`, `<context>`, `<task>`, `<must_haves>`. Other section names are inert to the parser.

**Caveat — they are NOT ignored by the LLM.** When the runtime invokes the workflow (skill body or workflow file content gets read by Claude Code / Codex CLI), the LLM sees the entire file, including any custom sections. Whether the LLM honors the section depends entirely on:
1. Whether the LLM prompt elsewhere instructs the LLM to read that section ("see `<gsd_modifier_uplift>` for additional...").
2. Whether the section name is self-explanatory enough that the LLM treats it as authoritative anyway.

The modifier's `<supporting_reading>` and `<deeper_reading>` sections work today via mechanism (2): the section names are conventional enough that LLMs treat them as authoritative reading guidance. But this is **fragile** — it depends on LLM behavior, not hard parser semantics.

**For an injection model to be robust, two conditions must hold:**

1. **The host workflow must reference the injected section.** Either by being already-referenced (e.g., the `<supporting_reading>` block is at the workflow top where readers expect it) or by having an LLM-side instruction nearby that says "before X, also consult `<gsd_modifier_uplift>` if present."

2. **The injection must not interfere with the runtime parser's section boundaries.** The current parser uses regex like `/<process[^>]*>([\s\S]*?)<\/process>/i` (`phase-prompt.ts:42`). An injected section nested inside `<process>` would be parsed-as-LLM-content; an injected section after `</process>` would be invisible to the parser. Both are safe for "additive" content. Modifying the parser's recognized blocks (`<purpose>`, `<process>`) requires intervention at the block-replace level.

### 3.4 Concrete deliverable: section consumption classification

For modifier-injected sections, the safe spots are:
- **`<supporting_reading>` / `<deeper_reading>`**: safe additive insertions because LLMs already treat them as reading guidance and they don't collide with parser blocks. **Recommended primary injection point** for content additions.
- **Inside `<process>` as a new `<step name="..."/>` block**: safe runtime-parser-wise (the step extractor will pick it up if the phase type is mapped) but order-sensitive — the new step needs to land before/after the right neighbors.
- **`<runtime_note>`**: safe additive section, often used for runtime-specific guidance.
- **A net-new section name (e.g., `<gsd_modifier_uplift>`)**: works only if the host workflow references it explicitly. Without that hook, content is read but not actively cited.

Unsafe / requires care:
- **Modifying `<purpose>` content**: would change the executor prompt's `## Purpose` section. Requires whole-section replacement.
- **Removing a `<step>` from `<process>`**: requires whole-section replacement of `<process>` because the step extractor processes all child steps.
- **Replacing the body of an existing `<step>`**: requires step-bounded replacement.

---

## 4. Carrier-by-carrier intervention archetype mapping

### 4.1 Archetype taxonomy

- **A. Pure injection** — additive markdown/XML; upstream file body untouched apart from the injection points
- **B. `@`-include via reference file** — modifier ships `references/*.md`; upstream workflow references it via `@`-include line that the upstream file already contains, OR the modifier uses `mode: add` for the reference and a small line patch (archetype C) inserts the include line
- **C. Targeted line patch** — overlay swaps one specific line in upstream (e.g., adds an include line at a known anchor, replaces a placeholder)
- **D. Genuine overwrite required** — modifier needs whole-file replacement; behavior change is broad enough that line-level patching would be more brittle than overwrite
- **E. Modifier-owned net-new** — already `mode: add`, no upstream analog
- **F. Code-level intervention** — `.cjs` file; needs require-time patching, plugin extension point, or upstream PR

### 4.2 Workflow files (24 total — primary user concern)

For each, evaluated by:
1. Reading the diff between upstream `git show origin/main:get-shit-done/workflows/<f>` and modifier overlay copy
2. Counting and classifying changed lines
3. Distinguishing converter-output-style changes (would-be-rewritten-by-upstream-anyway) from genuine modifier behavior changes

| File | Diff lines | Modifier-specific behavior changes (genuine, not converter-output) | Recommended archetype | Evidence |
|---|---:|---|---|---|
| `new-project.md` | 283 | (a) added `<supporting_reading>`/`<deeper_reading>`/`<required_reading>` with modifier `@`-include; (b) added section "1.5. Review Entry Runtime Continuity"; (c) replaced `gsd-sdk query generate-claude-md` with the `generate-instruction.cjs` wrapper invocation; (d) removed step "7.5. Project Structure Mode" (MVP/standard mode prompt); (e) removed "ORCHESTRATOR RULE — CODEX RUNTIME" notes, removed `/clear then:` lines (NOTE: removing `/clear` is upstream's converter behavior; this is converter-output overlap); (f) `gsd-sdk query commit "..." --files X` → `gsd-sdk query commit "..." X` (drops `--files` flag — likely modifier-side bugfix or back-compat) | **A+B+C+D mix**. Best path: (1) move the `<supporting_reading>` and `<deeper_reading>` additions to archetype A injection; (2) move the `1.5` section to archetype A injection; (3) keep the wrapper-invocation block as archetype C line patch; (4) the removed sections (7.5 mode, orchestrator rule) need archetype D narrow region replacement OR archetype A injection of "skip step 7.5" guidance. Net: mostly A with surgical C operations. | diff at `new-project.md:5-22, 100-121, 1268-1274, 1130-1162` |
| `discuss-phase.md` | 1486 | Added `<supporting_reading>`/`<deeper_reading>` (`discuss-phase.md:8-22`); converted Agent → Task spelling (modifier convention); modifier `@`-include paths; removed several mode-template files (`workflows/discuss-phase/modes/power.md`, etc. — no, those are still upstream — modifier just inlines the `--power` path differently); large `<codex_skill_adapter>`-shaped runtime translation block | Mostly **A** for the reading-section additions; some **D** for the runtime-translation insertion if it doesn't fit in `<runtime_note>`. **Needs deeper sweep** — 1486 line diff is large enough that conclusions are more uncertain. | diff sample read this pass |
| `plan-phase.md` | 1105 | Same reading-section pattern; possibly `<codex_skill_adapter>` block insertion | **A+B** as primary; deeper sweep recommended | (not deeply read in this pass; flagged) |
| `health.md` | 248 | Added `<supporting_reading>`/`<deeper_reading>` (`health.md:6-22`); removed `--backfill` flag handling (lines 18-19, 23-54 in upstream); removed `--context` mode (entire `<step name="context_check">`); removed corresponding `BACKFILL_FLAG` and `CONTEXT_MODE` propagation; added new step `<step name="keep_route_boundaries_explicit">` (`health.md:52-65`); added `<step name="offer_repair">` after | **D for now** but mostly **A+removal-via-step-replace**. The `--backfill`/`--context` removals are step-level deletions — would need either an "operations: section_replace" or "operations: step_remove" patch capability. The added `keep_route_boundaries_explicit` and `offer_repair` steps are pure A injections inside `<process>`. | diff read this pass at `health.md:14-67` |
| `update.md` | 209 | Added reading sections; replaced one slash command spelling (`/gsd-update` → `$gsd-update` — converter-output overlap); removed several lines about `RESOLVED_GSD_DIR` echo (#2992/#2993 commentary — upstream-side commentary the modifier removes); replaced "Check npm for latest version via the deterministic script" longer block with shorter "Check npm for latest version:" (modifier wants narrower flow) | **A+C+D mix**. Reading-section additions are A. Slash-command rewrites overlap with upstream converter (would not be needed if modifier moved upstream-of-converter). The block shortening is **D narrow** — could be archetype C if done as a section-replace operation. | diff read this pass at `update.md:5-22, 116-121, 285-289` |
| `progress.md` | 534 | Reading-section additions; likely workflow-step additions for modifier-specific routing | **A** primary; deeper sweep needed | (not deeply read this pass; flagged) |
| `complete-milestone.md` | (not measured this pass) | Likely reading-section additions plus one explicit `@`-include of `milestone-boundary-uplift-continuity.md` (the modifier-net-new reference) | **A+B**. The reference is already `mode: add`; if the workflow body already references it via `@`-include, the body itself doesn't need overwrite. | manifest declares `entry-runtime-uplift-continuity.md` and `milestone-boundary-uplift-continuity.md` as `mode: add`; orientation §4 |
| `discuss-phase-assumptions.md` | (not measured this pass) | Reading sections + modifier conventions | **A** | flagged |
| `discuss-phase-power.md` | (not measured this pass) | Reading sections + modifier conventions | **A** | flagged |
| `do.md` | (not measured this pass) | Reading-section additions; `do.md` is the upstream workflow that still ships even though the skill was deleted (#2790). Modifier carries `gsd-do/SKILL.md` as overwrite (stale-deleted) plus `do.md` workflow as overwrite. | **A** for reading sections; **archetype-decision tied to skill disposition** (orientation §7.3) — if the modifier keeps `gsd-do` skill, the workflow is needed; if dropped, the workflow overwrite may also become redundant. |
| `explore.md` | (not measured this pass) | Same pattern | **A** | flagged |
| `ingest-docs.md` | (not measured this pass) | Reading sections + `@`-include of `entry-runtime-uplift-continuity.md` | **A+B** | flagged |
| `new-milestone.md` | (not measured this pass) | Reading sections + modifier-specific milestone-boundary continuity hook | **A+B** | flagged |
| `plant-seed.md` | (not measured this pass) | Same as `do.md` — stale-deleted skill carrier; workflow body modifier-modified | **A** with skill-disposition coupling | (orientation §7.3) |
| `propagation-review.md` | n/a | Modifier-net-new — `mode: add` already from `harness_modifier/overlay/...` | **E** as already implemented | manifest entry |
| `quick.md` | (not measured this pass) | Reading sections | **A** | flagged |
| `research-phase.md` | n/a | Modifier carries this as overwrite, but **upstream `origin/main` does NOT have this file** (newly surfaced §1.5). Modifier is implicitly the canonical source. | **E (modifier-owned net-new)** OR remove from overlay if research-phase functionality is no longer needed. Reclassify `mode: overwrite` → `mode: add` from modifier-owned source. | `git ls-tree origin/main get-shit-done/workflows/research-phase.md` empty |
| `resume-project.md` | (not measured this pass) | Reading sections | **A** | flagged |
| `review.md` | (not measured this pass) | Reading sections | **A** | flagged |
| `seed-migration-inventory.md` | n/a | Modifier-net-new | **E** as already implemented | manifest entry |
| `settings.md` | (not measured this pass) | Reading sections | **A** | flagged |
| `spec-phase.md` | (not measured this pass) | Reading sections + `@`-include of `__PROJECT_ROOT__/.codex/get-shit-done/templates/spec.md` | **A+B** | flagged |
| `transition.md` | (not measured this pass) | Reading sections | **A** | flagged |
| `uplift-project.md` | n/a | Modifier-net-new | **E** as already implemented | manifest entry |
| `update.md` | (covered above) | (covered above) | A+C+D | (covered above) |
| `verify-phase.md` | (not measured this pass) | Reading sections + `@`-include of `__PROJECT_ROOT__/.codex/get-shit-done/templates/verification-report.md` and `verification-patterns.md` | **A+B** | flagged |

**Workflow summary**: of the 22 overwrite-mode workflows analyzed at any depth, the diffs cluster as:

- **~70% recoverable to archetype A** (pure additive injection of reading blocks and supplementary steps).
- **~20% require archetype A+C** (add includes plus targeted line patches around generators/wrapper invocation).
- **~10% require archetype D** (genuine overwrite for substantial step-set restructuring — `health.md` is the clearest example with `--backfill`/`--context` removal).
- **2 carriers** (`research-phase.md`) are misclassified — should be **E (modifier-owned net-new)**.
- **3 carriers** (`do.md`, `plant-seed.md`, possibly `from-gsd2`-related) tied to skill disposition.

**Inferred percentages — author did not deeply read all 22 files. Items marked "flagged" are needs-deeper-sweep.**

### 4.3 Reference files (5 overwrites + 2 adds)

| File | Mode today | Diff lines | Recommended archetype | Why |
|---|---|---:|---|---|
| `references/agent-contracts.md` | overwrite | 36 | **A** (or D) | Small enough that overwrite is defensible. Modifier additions likely additive sections plus modifier-specific examples. |
| `references/mandatory-initial-read.md` | overwrite | 21 | **A** | Reading-tier definitions added at top (`mandatory-initial-read.md:3-22` per diff this pass). Pure additive. Move to A. |
| `references/planner-reviews.md` | overwrite | 67 | **A** likely | Larger but predominantly modifier-specific additions. Deeper sweep recommended. |
| `references/planning-config.md` | overwrite | 80 | **A** likely | Same. Deeper sweep recommended. |
| `references/verification-overrides.md` | overwrite | 20 | **A** | Small additive. |
| `references/entry-runtime-uplift-continuity.md` | add | n/a | **E (already)** | Modifier-net-new |
| `references/milestone-boundary-uplift-continuity.md` | add | n/a | **E (already)** | Modifier-net-new |

### 4.4 Templates (7 overwrites)

| File | Diff lines | Recommended archetype |
|---|---:|---|
| `templates/config.json` | 18 | **C (line patch)** — diffs are key removals (`discuss_mode: discuss` → `exploratory`, removed `code_review_command`/`plan_bounce*`/`cross_ai_*` keys, removed `claude_md_path`). Could move to JSON-merge operation in manifest. |
| `templates/context.md` | 122 | **A or D** — likely modifier-specific section additions; deeper sweep recommended |
| `templates/phase-prompt.md` | 586 | **D** likely — large diff suggests substantial template rewrite; modifier may have different prompt assembly model. Templates of this scale are realistically still overwrite even in patch model. |
| `templates/research.md` | 372 | **D likely; deeper sweep needed** |
| `templates/spec.md` | 58 | **A** possibly |
| `templates/state.md` | 57 | **A** possibly |
| `templates/verification-report.md` | 412 | **D likely** |

**Inference**: templates are slower-moving than workflows but, when they diff substantially, the modifier intent is more likely "different output document shape". Genuine overwrite is more defensible here than for workflow files.

### 4.5 Agent files (4 overwrite .md + 7 add .toml)

| File | Mode today | Diff lines | Recommended archetype |
|---|---|---:|---|
| `agents/gsd-code-fixer.md` | overwrite | 269 | **A+D mix** — modifier adds `<codex_agent_role>` block (not relevant for claude install but harmless), changes "CLAUDE.md" → "AGENTS.md" (converter-output overlap), changes project-skills routing language. Net: deeper sweep needed; structural changes suggest D. |
| `agents/gsd-code-reviewer.md` | overwrite | 94 | **A+C** likely |
| `agents/gsd-intel-updater.md` | overwrite | 90 | **A+C** likely |
| `agents/gsd-pattern-mapper.md` | overwrite | 56 | **A** — diff is dominated by `<codex_agent_role>` block addition + small surgical text changes (orientation `agents/gsd-pattern-mapper.md:6-12, 35-41`) |
| `agents/gsd-*.toml` (7 files) | add (codex-only) | n/a | **E (already)** — codex-format mirrors of agent .md content |

**Caveat**: agent `.md` content includes `<role>`, `<philosophy>`, `<task_breakdown>`, `<plan_format>`, `<execution_flow>`, etc. Per `phase-prompt.ts:131-141`, the **whole body** is included in the prompt for executor / planner / etc. — so any addition or removal directly affects executor behavior. Higher-stakes than workflow body changes. Recommend treating as D unless surgical injection is well-anchored.

### 4.6 lib `.cjs` files (5 overwrites) — code-level intervention

| File | Diff lines | Notes |
|---|---:|---|
| `bin/lib/audit.cjs` | 107 | |
| `bin/lib/config.cjs` | 282 | |
| `bin/lib/phase.cjs` | 471 | |
| `bin/lib/roadmap.cjs` | 353 | |
| `bin/lib/state.cjs` | 779 | Includes upstream's new `computeProgressPercent` (#3242) and `planning-workspace.cjs` extraction (#2900) — modifier copies don't have these. |

**All five are archetype F.** Markdown injection doesn't apply to JavaScript code. Options:

1. **Maintain as overwrite** (status quo) — accept staleness risk; periodic content-resync sweep.
2. **Forking** — declare modifier owns these files entirely; remove the assumption that they mirror upstream.
3. **Plugin extension point** — would require upstream to expose extension hooks (e.g., `core.cjs` already exports several functions; modifier could `require('@gsd-build/get-shit-done/bin/lib/core.cjs').loadConfig` and wrap). Today not feasible without upstream PR.
4. **Monkey-patch at install time** — write a shim `.cjs` that requires upstream, mutates exports, and is invoked first. Brittle but possible.
5. **Upstream PR** — the cleanest path for any specific behavior the modifier needs. Highest social-cost, lowest entropy.

**Inferred recommendation**: status quo (option 1) for the immediate slice with a content-resync sweep cadence; option 5 (upstream PR) for any change that's likely upstream would accept. Options 3 and 4 carry runtime-stability risk that exceeds the maintenance burden of option 1.

### 4.7 Skills (10 overwrite codex-only + 2 add codex-only)

| File | Mode | Status | Recommended archetype |
|---|---|---|---|
| `skills/gsd-discuss-phase/SKILL.md` | overwrite | aligned | **A or D** depending on diff size — would benefit from content-resync sweep. Most of the modifier diff is the upstream-converter-equivalent `<codex_skill_adapter>` block. |
| `skills/gsd-do/SKILL.md` | overwrite | **stale-deleted** | reclassify — A is moot, **decision per orientation §7.3**: keep modifier-owned (E) or drop |
| `skills/gsd-explore/SKILL.md` | overwrite | aligned | **A or D**, same as discuss |
| `skills/gsd-from-gsd2/SKILL.md` | overwrite | **stale-deleted** | per orientation §7.3 |
| `skills/gsd-health/SKILL.md` | overwrite | aligned | **A or D** |
| `skills/gsd-plan-phase/SKILL.md` | overwrite | aligned | **A or D** |
| `skills/gsd-plant-seed/SKILL.md` | overwrite | **stale-deleted** | per orientation §7.3 |
| `skills/gsd-progress/SKILL.md` | add | **declaration-curiosity §1.6** | likely should be overwrite (same A or D as health/plan-phase) |
| `skills/gsd-resume-work/SKILL.md` | overwrite | aligned | **A or D** |
| `skills/gsd-review/SKILL.md` | overwrite | aligned | **A or D** |
| `skills/gsd-rigorous-research/SKILL.md` (+3 references) | add | **E (already)** | net-new modifier |
| `skills/gsd-update/SKILL.md` | overwrite | aligned | **A or D** |

**The Codex skill mirror problem**: upstream installer auto-generates `skills/gsd-X/SKILL.md` from `commands/gsd/X.md` for codex installs. Modifier overlay's overwrite of these synthesized files means modifier owns a copy of upstream's converter output. If upstream changes the converter (e.g., #2855 standardized the slash-command form), modifier's overwrite is stale. **The cleanest archetype is to overwrite `commands/gsd/X.md` (the pre-conversion source) and let upstream synthesize the codex form fresh on each install.** But this requires moving the modifier's intervention point upstream of the installer's converter. The modifier can't do this without modifying its install order — or moving its overlay step before `npx get-shit-done-cc` runs.

**Inferred from current setup-script flow** (`scripts/setup-portable-gsd-runtime.sh:67-113`): upstream install runs first, then modifier overlay runs. Reversing this would require: modifier writes `commands/gsd/X.md` first (would override upstream's writer at install time), or modifier patches the source tarball before upstream install runs. Neither is trivial — both are arguably bigger changes than the current overlay approach.

**Bottom-line for skills**: archetype A (additive injection) is partially viable for new modifier content blocks (`<codex_skill_adapter>`, modifier `@`-includes), but for full skill-body parity with upstream, the modifier-as-installer-output-overlay model is structurally appropriate. The fix is content-resync cadence, not architectural change.

### 4.8 Other carriers

| File | Mode | Disposition |
|---|---|---|
| `config.toml` | add (codex-only) | **E (already)** — codex top-level config; no upstream analog at this path (upstream doesn't ship a global config.toml; codex's config is `~/.codex/config.toml`) |
| `bin/generate-instruction.cjs` | add | **E (already, per Plan 004)** — modifier-owned wrapper, has independent value |
| `tooling/compact-prompts/project.md`, `readiness.md` | add (codex-only) | **E (already)** — modifier-owned compact prompts |

---

## 5. Manifest schema sketch for patch-style materializers

### 5.1 Proposed schema extension (illustrative, not committed)

```json
{
  "schema_version": 4,
  "entries": {
    "get-shit-done/workflows/new-project.md": {
      "capability_id": "get-shit-done/workflows/new-project.md",
      "parity_tier": "core_required",
      "materializers": {
        "codex": {
          "mode": "inject",
          "target": "get-shit-done/workflows/new-project.md",
          "operations": [
            {
              "kind": "section_insert_after",
              "anchor": "<required_reading>",
              "section_tag": "supporting_reading",
              "source": "harness_modifier/overlay/get-shit-done/workflows/new-project/supporting_reading.md",
              "idempotency_key": "GSD_MODIFIER:supporting_reading"
            },
            {
              "kind": "section_insert_after",
              "anchor": "</supporting_reading>",
              "section_tag": "deeper_reading",
              "source": "harness_modifier/overlay/get-shit-done/workflows/new-project/deeper_reading.md",
              "idempotency_key": "GSD_MODIFIER:deeper_reading"
            },
            {
              "kind": "include_add",
              "tag": "required_reading",
              "line": "@__PROJECT_ROOT__/.codex/get-shit-done/references/mandatory-initial-read.md",
              "after_line_match": "^Read all files referenced by",
              "idempotency_key": "GSD_MODIFIER:include:mandatory-initial-read"
            },
            {
              "kind": "step_replace",
              "step_name": "generate_instruction_file",
              "source": "harness_modifier/overlay/get-shit-done/workflows/new-project/generate_instruction_step.md",
              "idempotency_key": "GSD_MODIFIER:step:generate_instruction"
            }
          ]
        },
        "claude": {
          "mode": "inject",
          "target": "get-shit-done/workflows/new-project.md",
          "operations": [
            { "...": "..." }
          ]
        }
      }
    },
    "get-shit-done/workflows/health.md": {
      "capability_id": "get-shit-done/workflows/health.md",
      "parity_tier": "core_required",
      "materializers": {
        "codex": {
          "mode": "inject",
          "target": "get-shit-done/workflows/health.md",
          "operations": [
            {
              "kind": "section_insert_after",
              "anchor": "<required_reading>",
              "section_tag": "supporting_reading",
              "source": "harness_modifier/overlay/get-shit-done/workflows/health/supporting_reading.md",
              "idempotency_key": "GSD_MODIFIER:health:supporting_reading"
            },
            {
              "kind": "step_remove",
              "step_name": "context_check",
              "idempotency_key": "GSD_MODIFIER:health:remove_context_check"
            },
            {
              "kind": "step_insert_after",
              "anchor_step": "validate",
              "step_name": "keep_route_boundaries_explicit",
              "source": "harness_modifier/overlay/get-shit-done/workflows/health/keep_route_boundaries_explicit.md",
              "idempotency_key": "GSD_MODIFIER:health:keep_route_boundaries"
            }
          ]
        }
      }
    }
  }
}
```

### 5.2 Operation kinds in the proposed model

| Kind | Semantics | Idempotency | Verifies via |
|---|---|---|---|
| `section_insert_after` | After an anchor (XML tag close), insert a new section. Wrapped in HTML-comment `<!-- GSD_MODIFIER:start key:KEY -->` ... `<!-- GSD_MODIFIER:end key:KEY -->` markers | marker presence with matching key = already injected | scan target for marker; if present, skip |
| `section_replace` | Replace the inner content of an XML block (between tags) | marker presence + content hash | scan target for marker; verify content hash |
| `include_add` | Add a new line to an XML block (e.g., `@`-include in `<required_reading>`). Wrapped in marker | line presence inside the block | scan target for marker |
| `step_insert_after` | Insert a new `<step name="X">` after another step inside `<process>` | marker presence | scan |
| `step_replace` | Replace a `<step name="X">` body (not the step tag itself) | marker presence | scan |
| `step_remove` | Remove a `<step name="X">` block; leaves a comment marker recording the removal | marker presence | scan |
| `block_replace` | Replace one specific top-level block (e.g., `<purpose>...</purpose>`) | marker presence | scan |
| `line_replace` | Replace one specific line matching a regex (e.g., wrapper invocation swap) | marker presence + replacement on disk | scan |
| `text_substitute` | Substitute a literal string (e.g., `__PROJECT_ROOT__`) | substituted text on disk | match against expected pattern |

For backward compatibility:
- `mode: "overwrite"` and `mode: "add"` remain valid as today's bulk operations.
- `mode: "inject"` is the new, operation-sequence form.

### 5.3 What `harness_modifier/contract/portable_gsd_contract.py` would need to do

Functions that need extension (referenced from current code at `portable_gsd_contract.py`):

1. **`apply_overlay`** (`portable_gsd_contract.py:678-689` today): currently does a single `target.write_text(...)`. For inject-mode entries, would need to:
   - Read existing target content (post-upstream-install).
   - For each operation in sequence, compute the target text after applying the operation.
   - Verify idempotency markers before each operation; skip if marker already present.
   - Atomic write the final content.

2. **`build_manifest_validation_report_for_roots`** (`portable_gsd_contract.py:475-601`): currently validates `mode in {add, overwrite}` (`VALID_MODES = {"add", "overwrite"}` at line 26). Would need to extend to `{add, overwrite, inject}` and validate operation schemas.

3. **`build_materialization_report_for_roots`** (`portable_gsd_contract.py:718-829`): currently compares `overlay_text` to `live_text` for content equality. For inject-mode entries, equality check makes no sense (the live text is upstream + injections; not equal to source). Need a per-operation "did the injection land?" check via:
   - Marker presence on disk for each operation's idempotency_key
   - Optional content hash verification of the marker-bounded region

4. **`capture_pristine_overwrites`** (`portable_gsd_contract.py:617-675`): currently captures `overwrite`-mode entries to backup-meta. For `inject`-mode entries, what to capture? Option: capture the upstream-install state as the "pristine" baseline, then idempotency markers track which operations have been applied. The backup is for rollback purposes — restore the captured pristine, then re-apply the operation set.

5. **New module `harness_modifier/contract/inject_operations.py`** (proposed): single-responsibility module implementing each operation kind. Each operation is a pure function `(content: str, op: dict) → (new_content: str, applied: bool)`.

### 5.4 Verification model

The hardest constraint: how does `verify-materialized` confirm the live target matches the modifier's intent?

Three options, each with trade-offs:

**Option V1: Marker presence + position check.**
- For each operation, scan the live file for the operation's `<!-- GSD_MODIFIER:start key:KEY --> ... <!-- GSD_MODIFIER:end key:KEY -->` markers.
- Verify markers exist at the expected anchor (e.g., after the right `<required_reading>`).
- Pro: cheap, fast, no semantic content check.
- Con: doesn't catch if a user manually edited inside the marker region.

**Option V2: Marker presence + content hash.**
- For each operation, store the expected content hash of the marker-bounded region.
- On verify, compute the hash and compare.
- Pro: detects in-marker edits.
- Con: any user edit invalidates verification; more complex schema (hashes in manifest).

**Option V3: Round-trip diff.**
- After applying all operations, store the full target file's content hash in the manifest.
- On verify, recompute the live content hash and compare.
- Pro: simplest verification logic.
- Con: any change anywhere in the file (even outside the modifier's marker regions, e.g., upstream changing a comment) breaks verification. Most brittle.

**Inferred recommendation**: V1 as the default with V2 as an opt-in per operation. V3 is incompatible with the goal of "non-marker regions can drift".

### 5.5 Interaction with `parity_tier`

Today `parity_tier` is a property of the entry as a whole (`core_required`, `core_adapted`, `runtime_specific`). With patch-style materializers per runtime, the question becomes: do all runtime materializers need the same operation set?

- **`core_required`**: today means "this carrier is required for both runtimes to maintain parity." With injections, "parity" can mean "the same operation set is applied" OR "the same effective behavior is achieved through different operations." For most reading-block additions, both runtimes get equivalent operations. For `<codex_skill_adapter>` blocks (codex-only), the operation is genuinely runtime-specific.

- **Recommendation**: parity_tier remains valid; for `inject` mode, materializer-equivalence is checked at the **outcome** level (do both runtimes have the same modifier-owned content visible after injection?), not at the operation level. Add a `parity_outcome` field per entry that documents what equivalence means for that carrier.

- **Alternative**: introduce a `parity_tier: core_inject_aligned` value that explicitly says "core parity via operation alignment, not bulk overwrite." Avoids breaking existing tier semantics.

### 5.6 Backward compatibility

Existing `overwrite`/`add` entries:
- Stay valid in schema_version 4. The new `inject` mode is additive.
- Validation rules unchanged for `overwrite`/`add`.
- The transition can be carrier-by-carrier: each manifest entry can independently move from `overwrite` to `inject` when ready.

Schema-version migration:
- Bump `schema_version` to 4 when first inject-mode entry is added.
- Validation code already branches on schema version (`portable_gsd_contract.py:295-312`) — extend with v4 branch.

---

## 6. Risk and migration analysis

### 6.1 Idempotency

Operation markers are the foundation. For each operation, generate a marker like:

```
<!-- GSD_MODIFIER:health:remove_context_check op:step_remove key:GSD_MODIFIER:health:remove_context_check applied:1 -->
```

On `apply-overlay`:
1. Scan target for marker with matching key.
2. If present → skip (already applied).
3. If absent → apply and write marker.

This makes re-running setup safe.

**Risk**: if upstream introduces an identical marker syntax (extremely unlikely given the `GSD_MODIFIER` namespace prefix), conflicts are possible. Mitigate by namespacing markers (prefix `GSD_MODIFIER:`).

### 6.2 Anchor drift

The biggest risk for inject-mode operations.

Example: today's modifier overlay assumes `<supporting_reading>` lives directly after `<required_reading>`. If upstream renames `<required_reading>` to `<context_reading>` in some workflow file:
- `section_insert_after` with anchor `<required_reading>` would silently skip insertion.
- `verify-materialized` with V1 marker check would also miss this.

**Mitigation strategies**:
1. **Multiple-anchor fallback**: each operation specifies `anchor` plus `fallback_anchor` (e.g., "if `<required_reading>` not found, try `<context_reading>`, else fail").
2. **Anchor-mismatch alarm**: `apply-overlay` records each operation's anchor outcome. If an anchor-not-found, raise hard failure with explicit "upstream may have renamed the anchor; review needed."
3. **Anchor versioning**: tie operation set to upstream version; if upstream version mismatches, prompt for re-evaluation.

Inferred: the alarm-on-not-found behavior (option 2) is the most aligned with the modifier's existing posture (silent staleness is the disease; loud mismatches are the cure).

### 6.3 Partial application

If 5 of 7 operations succeed and 2 fail (e.g., anchor-not-found):
- All-or-nothing semantics: roll back the 5 that succeeded; raise the failure.
- Best-effort semantics: keep the 5 successes, mark the file as partially-modified, raise.

**Recommendation**: all-or-nothing by default. The `apply-overlay` step should be transactional per file. Implementation: write the modified content to a temp file, swap in only if all operations applied successfully.

### 6.4 Rollback

Today: `gsd-local-patches/<rel_path>` holds the upstream-pristine copy (`portable_gsd_contract.py:617-675`). Rollback is `cp gsd-local-patches/<rel_path> <live_path>`.

For inject-mode:
- The captured pristine is the upstream post-install state.
- Re-applying inject operations to the pristine should be deterministic.
- Rollback: restore pristine, optionally re-apply the desired operation set.

The new model is more rollback-friendly because it's reversible by design.

### 6.5 Detection — "didn't happen" vs "reverted by user"

Marker presence/absence answers this clearly:
- Marker absent → operation didn't happen (or was applied and then user removed both content + marker).
- Marker present, content matches → operation happened, untouched.
- Marker present, content differs → user manually edited the marker region.

Add a fourth state: marker present with `applied:0` → operation was deliberately skipped (e.g., conditional operation didn't fire).

### 6.6 Migration phases (proposed)

**Phase α — schema and contract groundwork**
- Bump `schema_version` from 3 to 4, add `inject` mode validation, retain backward compatibility.
- Implement first 3 operation kinds (`section_insert_after`, `include_add`, `text_substitute`) as the lowest-friction ones.
- Add `verify-materialized` extension to handle marker-presence checks.
- Effort: ~1 phase (1–2 weeks single-developer).

**Phase β — migrate low-risk carriers**
- Move references with simple additive content first: `references/mandatory-initial-read.md` (the 21-line additive at top) — convert from overwrite to inject with one `section_insert_after` operation.
- Move 5 reference files from overwrite to inject.
- After each, run full bootstrap proof and host matrix.
- Effort: ~1 phase per 2–3 references; ~1–2 phases total.

**Phase γ — migrate workflow files (the 22 overwrites)**
- Start with workflows where the diff is dominated by reading-section additions: `update.md` (209 lines), `health.md` (248 lines, with one step-remove), `progress.md`, `verify-phase.md`.
- Skip workflows with deep restructuring (`new-project.md`, `discuss-phase.md`) until confidence is high.
- Effort: ~1 phase per 4–5 workflows; ~5–6 phases total.

**Phase δ — workflows with step-level patches**
- Operations needed: `step_remove`, `step_replace`, `step_insert_after`. Already specified in §5.2.
- Tackle `health.md`, possibly `update.md`, possibly `progress.md` once Phase γ has shaken out the operation library.
- Effort: ~2 phases.

**Phase ε — agents and templates**
- Agent `.md` files — riskier because executor behavior depends on full body. Only after Phase γ proves the model.
- Template files — large diffs may stay as overwrite even in patch model.
- Effort: variable, ~2–4 phases.

**Phase ζ — codex-only skills**
- Likely deferred. The codex-skill-mirror problem (§4.7) means some of these may stay as upstream-installer-output-overlays even when the rest of the manifest has moved.
- Effort: 1–2 phases if pursued.

**Stays as overwrite**: 5 lib `.cjs` files (archetype F, no markdown injection model applies); some templates.

**Total**: ~12–18 phases for a complete migration. **Inferred** — actual scope depends on what the user finds tolerable in the partial-migration state.

### 6.7 Risk summary

| Risk | Severity | Mitigation |
|---|---|---|
| Anchor drift (upstream renames a tag) | high | Anchor-not-found loud alarm (§6.2 option 2) |
| Operation-set staleness (modifier intent diverges from current upstream) | medium | Same content-resync sweep already needed for overwrite mode; injection makes it harder, not easier, to detect |
| Partial application leaves file in inconsistent state | medium | All-or-nothing transactional apply (§6.3) |
| User manually edits inside marker region | low | V2 content-hash check on opt-in operations |
| Operation library complexity creep | medium | Start with 3 operation kinds; add new ones only when concrete carrier need arises |
| Backward incompatibility breaks existing manifests | low | schema versioning; v3 entries continue to work |
| Verification UX regression | medium | Aggregate operation outcomes per entry; report level summaries with drill-down |

---

## 7. Strategy recommendation

### 7.1 What the new model should be

**Two-tier overlay system:**

1. **Surgical/inject layer** (new) — for ~50–60% of current overwrite carriers. Markdown/XML files with predominantly additive modifier intent. Patch-style operations preserve upstream content, mark modifier additions explicitly, allow upstream non-marker regions to drift in without modifier interference.

2. **Bulk overwrite layer** (status quo) — for the remaining ~40–50%. Lib `.cjs` files (archetype F), heavily-restructured workflows, large-template overwrites. Same as today.

3. **Net-new layer** (status quo, `mode: add`) — for modifier-owned content with no upstream analog.

### 7.2 What carriers move first (recommended ordering)

**First wave (low-risk, high-value)**:
- `references/mandatory-initial-read.md` — small additive (21 lines), pure A injection.
- `references/verification-overrides.md` — small additive (20 lines).
- `references/agent-contracts.md` — medium additive (36 lines).
- 1 small workflow (e.g., `update.md` or `health.md` with the reading-section-only additions).

Goal: prove the inject mechanism works end-to-end on 3–4 carriers before scaling.

**Second wave (medium-risk)**:
- 5 reference files complete.
- 4–5 workflows whose diffs are pure additive (`spec-phase.md`, `verify-phase.md`, `complete-milestone.md`, `new-milestone.md`, `ingest-docs.md`).

**Third wave (step-level operations)**:
- `health.md` (`step_remove`, `step_insert_after`).
- `update.md` (block content reductions).
- `progress.md` (deeper sweep needed first).

**Fourth wave (large/restructured workflows)**:
- `new-project.md`, `discuss-phase.md`, `plan-phase.md`. Each large enough that the inject model needs to be mature.

**Stays as overwrite (don't move)**:
- 5 `bin/lib/*.cjs` files — no markdown model applies.
- Heavy-template overwrites (`phase-prompt.md`, `verification-report.md`, `research.md`) until injection shows it's worth the cost on smaller templates.
- Codex-skill mirrors — structural mismatch (§4.7); stays as overlay-of-installer-output.

**Modifier-owned net-new** (no change): all 18 `mode: add` entries stay as `mode: add`.

### 7.3 Rough effort estimates

Per-carrier-class:
- **Reference file (additive)**: ~½ day to migrate, ~½ day to verify across both runtimes. Phase β waves of 2–3 references = ~2–3 days.
- **Small workflow (reading-only)**: ~1 day to migrate (more anchor edge cases), ~1 day to verify. Phase γ waves of 3–4 workflows = ~6–8 days.
- **Step-level workflow**: ~2 days to migrate (new operation kinds; deeper diff analysis), ~1 day to verify. Phase δ workflows = ~3 days each.
- **Large workflow (`new-project.md`-class)**: ~4–6 days each. Defer until model is mature.
- **Schema and contract groundwork (Phase α)**: ~1–2 weeks.

Total inferred effort to reach 70% migration (references + 12 small workflows + 3 step-level): ~6–8 weeks single-developer.

Total inferred effort for full migration: ~12–18 weeks single-developer (excludes lib `.cjs` and codex-skill-mirror — those stay as today).

### 7.4 Verification surface extensions needed

New contract-tool methods (`portable_gsd_contract.py`):
1. `validate_inject_operations(spec)` — verify each operation has required fields per its kind.
2. `apply_inject_operations(content, operations)` — pure function; returns (new_content, list_of_marker_records).
3. `extract_inject_markers(content)` — scan content for `GSD_MODIFIER:` markers, return their keys + positions.
4. `verify_inject_state(target_content, expected_operations)` — confirm marker presence per operation.

New test categories (under `tooling/codex/tests/`):
1. **Operation unit tests** — for each operation kind, test idempotency, anchor-not-found, partial application.
2. **End-to-end inject tests** — for each migrated carrier, verify the operation set produces expected target content.
3. **Pristine-restore tests** — verify rollback round-trips preserve content.
4. **Backward-compat tests** — ensure schema v3 entries still work after schema v4 introduction.

### 7.5 Where the new model lives in `parity_tier` taxonomy

**Recommended**: extend the existing taxonomy without changes — `parity_tier` continues to describe "what role this carrier plays in dual-runtime parity". The new `mode: "inject"` is orthogonal (it describes "how does this carrier reach its target"). Both `core_required` and `runtime_specific` carriers can use any of the three modes.

For the operation alignment check (§5.5), introduce per-operation parity_intent metadata if needed. Most `core_required` carriers will want `parity_intent: "outcome_aligned"` (both runtimes get the same effective additions); some carriers may want `"runtime_independent"` (operations differ per runtime by design).

### 7.6 What stays as-is (and why)

| Carrier class | Stays as-is? | Why |
|---|---|---|
| `bin/lib/*.cjs` (5) | yes — overwrite | Markdown injection doesn't apply; archetype F |
| Heavy-template overwrites (`phase-prompt.md`, etc.) | yes for now | Large diff means many operations; injection complexity exceeds overwrite simplicity for these |
| Modifier-owned `mode: add` (18) | yes | Already in optimal state |
| Codex-skill mirrors (10) | partially — see §4.7 | Structural mismatch with upstream installer flow makes the overlay-of-output model architecturally correct |

### 7.7 What this means for the 3 stale-deleted skill carriers

Per orientation §7.3, three options were on the table:
- 3a: reclassify all three as `mode: add` from `harness_modifier/overlay/`.
- 3b: remove all three.
- 3c: mixed.

**Implication of the inject-mode model for these**:
- If the modifier moves to inject-mode for the `commands/gsd/<X>.md` body of these skills (i.e., reach upstream's pre-conversion source), then 3a-style "reclassify as `mode: add`" is the path. The modifier owns the source (`mode: add` from `harness_modifier/overlay/commands/gsd/X.md`), and upstream's installer synthesizes the codex `skills/gsd-X/SKILL.md` from it.
- Today: modifier overwrites the post-conversion `skills/gsd-X/SKILL.md` directly. There's no upstream `commands/gsd/X.md` to overwrite (it was deleted). The cleaner long-term fix is to reach upstream-of-converter — but this requires `mode: add` in the source path, which means **the modifier has to add a `commands/gsd/X.md` that doesn't exist upstream.** That works because upstream's installer reads from `commands/gsd/` dir — the modifier just needs to put the file there before install. Today's overlay model runs **after** install, so it can't easily do this.

**Inferred recommendation**: for the three stale-deleted skills:
- If kept (per orientation §7.3 option 3a), the cleanest path is **add a pre-install step** to the modifier setup that copies modifier-owned `harness_modifier/overlay/commands/gsd/X.md` files into the source tarball OR use a different install entry point that respects modifier-owned skill sources. Both are bigger than typical modifier slices.
- Simpler: keep them as `mode: add` overlays of the synthesized codex `skills/gsd-X/SKILL.md` path (i.e., reclassify from overwrite to add), accepting that they're modifier-owned standalone skills with no upstream symbolic relationship. This is the fastest path; trade-off is that for claude installs, these skills don't materialize unless the modifier also adds claude-side `commands/gsd/<X>.md` paths to the manifest.

---

## 8. Evidence gaps (places where inference exceeds doc support)

1. **Upstream extension API**: there is no `EXTENDING.md`, `CUSTOMIZATION.md`, or formal extension API doc on `origin/main`. All extension-mechanism claims rest on code reading. Specifically:
   - Whether `@`-include syntax is a stable convention or implementation detail is **inferred from usage volume and the explicit conversion logic in `install.js`**, not from a doc commitment.
   - Whether `<!-- GSD:section-start -->` markers are intended to be a general-purpose extension primitive is **inferred from their currently-narrow usage** — only `generate-claude-md` uses them today.

2. **The `gsd-progress` mode-add curiosity (§1.6)**: not verified by running `validate-manifest --strict`. The conclusion that this is "likely a declaration bug" is inference from reading the manifest; the validation may or may not flag it.

3. **Diff-quality assertions for un-deeply-read files**: the table in §4.2 marks several entries "deeper sweep needed". The recommendations for those rows are inferred from diff line counts and class-typical patterns, not from full reading. Specifically: `discuss-phase.md` (1486), `plan-phase.md` (1105), `progress.md` (534) were not deeply read.

4. **Effort estimates in §7.3**: based on author's read of operation complexity vs. carrier counts. No empirical baseline (e.g., past phase durations on similar work). Treat as order-of-magnitude.

5. **Codex skill-mirror migration path (§4.7)**: the suggestion that modifier could move to overlaying `commands/gsd/X.md` (pre-conversion) instead of `skills/gsd-X/SKILL.md` (post-conversion) is inferred from how upstream's installer flow works. Whether the modifier's setup script can practically inject between source-fetch and conversion is not verified by running the install — would need testing.

6. **The "bin/install.js conversion duplicates modifier work" claim**: read the converter code and observed the rules. **Did NOT run** an experiment showing what content would result if modifier overlaid `commands/gsd/X.md` and let upstream synthesize the codex form. This is a strong inference but not a verified behavior.

7. **Upstream PR receptivity for archetype F (lib `.cjs` files)**: §4.6 mentions option 5 (upstream PR) as a path. Author has no specific information about upstream's policy for accepting modifier-targeted extension hooks. This is purely inference.

---

## 9. Cross-reference to orientation §7

The orientation artifact's §7 lists 7 numbered next moves. This deliverable's findings affect them as follows:

| Orientation §7 item | Affected by intervention-strategies? | How |
|---|---|---|
| 7.1 Plan 004 disposition update | No | Plan 004 is locked; the wrapper has independent value. This deliverable confirms the wrapper is correctly classified as `mode: add` (§4.8). |
| 7.2 Draft CLAUDE.md as runtime-neutral pointer | No | Governance carrier; orthogonal to intervention model. |
| 7.3 Reclassify 3 stale-deleted skill carriers | **Yes** — see §7.7 above. The recommended path depends on whether the inject model is being adopted. If staying with overwrite-only, simple `mode: add` reclassification is the path (option 3a from orientation). If moving to inject, there's an opportunity to overlay `commands/gsd/<X>.md` (the pre-conversion source) instead, but that requires deeper install-flow changes. |
| 7.4 Add change-class triggers to AGENTS.md | No (orthogonal) | Governance discipline; this deliverable is technical strategy. The new "mode: inject" carrier class would itself need a change-class trigger entry (any inject schema or operation-library change is governance-relevant). |
| 7.5 Delete temp handoff | No | Independent. |
| 7.6 Run bootstrap gate against current state | No, but **strongly recommended before any inject migration** to establish baseline. The migration plan in §7.2 implicitly assumes baseline gates pass. |
| 7.7 Medium-term sweep proposals (placeholder) | **Yes** — the medium-term sweep proposals (§6.2 of orientation) overlap with this deliverable's recommended phases. Specifically: |
| ... §6.2.1 overlay content-resync sweep | **Subsumed/superseded by inject migration**. If carriers move to inject mode, content-resync becomes per-operation drift check rather than whole-file diff — a cleaner sweep. For carriers staying as overwrite (lib `.cjs`, etc.), the content-resync sweep remains needed. |
| ... §6.2.2 slash-command namespace audit | **Now likely a non-issue** for inject-mode carriers because the modifier wouldn't be carrying post-conversion text. Still relevant for the overwrite-mode carriers and for the modifier-owned net-new content. |
| ... §6.2.3 workflow stale-rename check | **Subsumed**. The 3 stale-deleted skills + 1 stale-deleted workflow (§1.5 of this artifact) are the surfaced cases. After the migration discipline is in place, periodic anchor-not-found alarms (§6.2 here) replace this manual check. |
| ... §6.2.4 upstream drift check tool | **Reframed**. Instead of "did upstream delete a carrier we declare?" the inject model asks "did upstream rename our anchor?" and "did our operations land?". A simpler, more focused tool. |

---

## 10. Constraints and capabilities the author wished for

### 10.1 Files that would have helped but don't exist

- `docs/EXTENDING.md` (or `docs/CUSTOMIZATION.md`) on `origin/main` — would have crystallized which mechanisms upstream considers stable extension surfaces vs. internal implementation details. Verified absent.
- `docs/HOOKS.md` — would have documented hook-event surface formally. Verified absent (hook info is scattered in install.js, README, `docs/issue-driven-orchestration.md`).
- A formal contract test in upstream that asserts "the workflow file XML section schema is `{purpose, process, step, …}`" — would have removed inference about which sections are runtime-parsed.

### 10.2 Capabilities the author would have used

- **Running the bootstrap stack** (`scripts/ci/check-deterministic.sh`, `scripts/ci/check-bootstrap.sh`) and the host matrix to verify baseline before recommending migration. State-mutating, thus out of read-only scope, but recommended as a precursor to any §7 implementation.
- **Running `validate-manifest --strict --runtime codex`** to confirm the §1.6 `gsd-progress` curiosity. State-mutating against backup-meta; out of scope.
- **A test run of one carrier through a hypothetical inject prototype** to validate the operation library's expressiveness on a real workflow. Out of scope for this deliverable.

### 10.3 Things that worked

- **Side-by-side `git show origin/main:<path>` access to upstream content** was essential and worked smoothly. The `~/workspace/projects/get-shit-done-upstream` clone proved to be the right reference.
- **The orientation artifact's read trail (§ Read trail)** gave a strong starting point for which files to focus on.
- **The clarity of the modifier's contract code** (`portable_gsd_contract.py` is well-structured and readable) made schema-extension reasoning tractable.
- **Upstream's `bin/install.js` has detailed inline comments** explaining why each conversion exists (citing PR numbers like #1430, #2639, #3018). This made tracing the converter's intent feasible.

---

## Read trail

Files read during this pass (read-only):

Modifier repo:
- `.planning/readiness/release-readiness-orientation-2026-05-08.md` (full)
- `tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json` (full)
- `tooling/portable-gsd/overlay/get-shit-done/bin/generate-instruction.cjs` (full)
- `tooling/portable-gsd/overlay/get-shit-done/workflows/new-project.md` (head + spot reads + diff)
- `tooling/portable-gsd/overlay/get-shit-done/workflows/discuss-phase.md` (diff only)
- `tooling/portable-gsd/overlay/get-shit-done/workflows/health.md` (diff)
- `tooling/portable-gsd/overlay/get-shit-done/workflows/update.md` (diff)
- `tooling/portable-gsd/overlay/get-shit-done/templates/config.json` (diff)
- `tooling/portable-gsd/overlay/get-shit-done/bin/lib/state.cjs` (diff sample)
- `tooling/portable-gsd/overlay/agents/gsd-pattern-mapper.md` (diff sample)
- `tooling/portable-gsd/overlay/skills/gsd-discuss-phase/SKILL.md` (head)
- `tooling/portable-gsd/overlay/config.toml` (head)
- `tooling/portable-gsd/overlay/agents/gsd-code-fixer.toml` (head)
- `harness_modifier/contract/portable_gsd_contract.py` (full)
- `harness_modifier/contract/__init__.py` (full)
- `harness_modifier/compatibility/declaration.json` (relevant section)
- `harness_modifier/overlay/get-shit-done/workflows/propagation-review.md` (head)
- `scripts/setup-portable-gsd-runtime.sh` (full)

Upstream reference (via `git show origin/main:<path>` and `git ls-tree origin/main`):
- `bin/install.js` (head + targeted reads of conversion functions; ~5000 lines, sampled lines 2185-2280, 4611-4670, 1364-1373, 1522-1535, 1671, 1789, 2200-2225)
- `bin/gsd-sdk.js` (full, 36 lines)
- `sdk/src/query/QUERY-HANDLERS.md` (head)
- `sdk/src/query/profile-output.ts` (sampled — `generateClaudeMd` handler lines 774-900, plus head)
- `sdk/src/query/index.ts` (full, 8 lines)
- `sdk/src/query/command-manifest.non-family.ts` (relevant lines)
- `sdk/src/phase-prompt.ts` (head + class definition through `loadAgentDef`, ~200 lines)
- `sdk/src/plan-parser.ts` (head, sampled `extractContextRefs` + `extractExecutionContext` + `parsePlan`)
- `docs/CONFIGURATION.md` (head)
- `docs/USER-GUIDE.md` (head, section on namespace routing)
- `commands/gsd/discuss-phase.md` (head)
- `commands/gsd/new-project.md` (head)
- `agents/gsd-planner.md` (head)
- `get-shit-done/workflows/new-project.md` (head + targeted greps)
- `get-shit-done/workflows/discuss-phase.md` (head)
- `get-shit-done/workflows/do.md` (head)
- `get-shit-done/templates/phase-prompt.md` (head)
- `get-shit-done/references/mandatory-initial-read.md` (diff snippet)

Upstream tree presence checks (via `git ls-tree origin/main <path>`):
- `commands/gsd/{do,from-gsd2,plant-seed}.md` → all empty (verified deleted)
- `get-shit-done/workflows/{do,plant-seed,research-phase}.md` → research-phase missing; do.md and plant-seed.md present
- `docs/{HOOKS.md, EXTENDING.md, CUSTOMIZATION.md}` → all absent
- `hooks/` directory listing → 12 hooks present (gsd-check-update, gsd-context-monitor, gsd-prompt-guard, gsd-read-guard, gsd-read-injection-scanner, etc.)
- `bin/lib/` upstream — confirmed presence of `core.cjs`, `model-profiles.cjs`, `install-profiles.cjs`, `planning-workspace.cjs` etc. (per usages in `bin/install.js`)
- `sdk/src/query/` listing — 100+ handler files

Upstream commits cited:
- `96806003` (current HEAD `origin/main`)
- `c5b14455` (PR #2341, shipped in v1.38.4)

Tag inspection: `v1.41.0` is current latest stable.

PR numbers cited from upstream comments and CHANGELOG:
#1430 (.claude → .codex path conversion), #2341 (PR #2302 Track A — golden parity harness), #2406 (read-injection-scanner), #2517 (runtime-aware tier resolution), #2551 (workflow budget), #2639 (.claudeignore → .codexignore), #2762 (--minimal install), #2768/#2783/#2697/#2855 (slash-command namespace), #2790/#2824 (skill consolidation), #2791 (gsd-tools deprecation), #2792 (namespace meta-skills), #2900 (planning-workspace.cjs extraction), #2992/#2993 (npm view → script-driven), #3018 (auto-default failure mode), #3163 (codex AGENTS.md override), #3242 (computeProgressPercent), #3261 (nested plans counting).

---

## Disposition

This artifact is a strategy snapshot. Once the user has digested the recommendations:

- Either route specific phases per §7.2 (each phase = a separately-approvable proposal under AGENTS.md governance).
- Or keep this as a reference; defer migration; let it inform incremental decisions.

This artifact does **not** become governance, does **not** declare any path adopted, and does **not** authorize any source/manifest/contract change. Each migration phase is a separate proposal under the existing change-class trigger discipline.
