Date: 2026-04-22
Status: active audit output

# Codex Claude Installation Parity Audit — Opus 4.7 r1

## Framing

- [g:r:i] Audit horizon is `.codex` and `.claude` only.
- [g:r:i] The audit maps the two-runtime install/materialization field: what upstream already separates explicitly, where repo-local carry stays in tune with that split, where repo-local carry still blurs runtime-specific responsibilities, how each currently surfaced `.claude` reference should be classified, what should travel explicitly later, and what the strongest next bounded route is.
- [g:r:i] The audit is not a pass/fail check. `.codex` and `.claude` are the whole provider horizon here, and the governing task is field disclosure and stronger carry, not threshold clearance.

## What Upstream Already Separates Explicitly

Upstream's `bin/install.js` already treats `.codex` and `.claude` as distinct install paths at several layers, not as plain reference substitution. Each layer separates explicitly.

### Install Shape

- [e:c+i] Upstream dispatches install shape per runtime flag and never shares a single carrier between Codex and Claude. Source: [install.js:4104-4192](/home/rookslog/.npm/_npx/a2a7266cd903ec8b/node_modules/get-shit-done-cc/bin/install.js).
  - `isCodex` branch writes to `skills/gsd-*/SKILL.md` via `copyCommandsAsCodexSkills` (install.js:4119-4128).
  - Claude path (the `else` default on install.js:4179-4192) writes to nested `commands/gsd/` via `copyWithPathReplacement`.
  - These are different directory layouts, different file name shapes, and different frontmatter contracts.
- [e:c+i] Upstream README makes the Codex-side shape explicit rather than leaving it inferred: "Codex installation uses skills (`skills/gsd-*/SKILL.md`) rather than custom prompts." Source: [README.md:96](/home/rookslog/.npm/_npx/a2a7266cd903ec8b/node_modules/get-shit-done-cc/README.md).

### Agent Conversion

- [e:c+i] Upstream does not ship one agent shape and hope every runtime reads it. Each runtime gets a distinct frontmatter/body conversion path. Source: [install.js:4230-4248](/home/rookslog/.npm/_npx/a2a7266cd903ec8b/node_modules/get-shit-done-cc/bin/install.js).
  - `isCodex` → `convertClaudeAgentToCodexAgent` (install.js:4237-4238).
  - Claude (default): no conversion applied; upstream source is already Claude-shape.
  - `~/.claude/` and `$HOME/.claude/` in agent bodies are substituted to the runtime-specific `pathPrefix` for every non-Claude, non-Copilot, non-Antigravity runtime (install.js:4227-4230).

### Runtime Config

- [e:c+i] Upstream then generates runtime-specific config artifacts after the shared content is written. The Codex branch writes a `config.toml` plus per-agent `.toml` files through `installCodexConfig`. Source: [install.js:4388-4421](/home/rookslog/.npm/_npx/a2a7266cd903ec8b/node_modules/get-shit-done-cc/bin/install.js).
- [e:c+i] Claude path instead writes a `settings.json`. Source: [install.js:4446-4450](/home/rookslog/.npm/_npx/a2a7266cd903ec8b/node_modules/get-shit-done-cc/bin/install.js).
- [d:r:i] Those are two different config grammars entirely. Upstream does not pretend that one file shape carries both.

### Hook Carrier

- [e:c+i] Upstream's hook layer also splits per runtime at install time. Source: [install.js:4280-4320](/home/rookslog/.npm/_npx/a2a7266cd903ec8b/node_modules/get-shit-done-cc/bin/install.js).
  - The shared copy path `if (!isCodex && !isCopilot && !isCursor && !isWindsurf)` writes a CommonJS shim `package.json` and copies `hooks/dist/*` .js files with `.claude` substituted to the runtime-specific config dir via `configDirReplacement` (install.js:4295, 4304).
  - Codex skips that copy entirely. Instead, Codex adds a `[[hooks]]` stanza directly into `config.toml` gated on the `codex_hooks` feature flag. Source: [install.js:4394-4415](/home/rookslog/.npm/_npx/a2a7266cd903ec8b/node_modules/get-shit-done-cc/bin/install.js).
  - Claude adds hook entries into `settings.json.hooks.SessionStart` and `.PostToolUse` arrays. Source: [install.js:4475-4520](/home/rookslog/.npm/_npx/a2a7266cd903ec8b/node_modules/get-shit-done-cc/bin/install.js).
- [d:r:i] Codex hook ownership is config-driven inside the runtime-native config format. Claude hook ownership is settings-driven inside a Claude-native JSON file. Upstream carries both separately; neither would read the other.

### Leak Scanner Layer

- [e:c+i] Upstream also carries a post-install verification layer that explicitly recognizes `.claude` references as runtime-specific and runs only against non-Claude runtimes. Source: [install.js:4339-4386](/home/rookslog/.npm/_npx/a2a7266cd903ec8b/node_modules/get-shit-done-cc/bin/install.js).
  - Scanner regex: `(?:~|\$HOME)\/\.claude\b` (install.js:4367).
  - The scanner is warning-level, not exit-level: `console.warn` plus a note that "these paths may not resolve correctly for {runtimeLabel}" (install.js:4377-4384).
  - The scanner is a blunt regex over `.md` and `.toml` content, with no semantic awareness of runtime-detection arrays or comment examples.

### Separation Shape Summary

- [d:r:i] The separation upstream already carries between `.codex` and `.claude` is not decorative. It covers install directory shape, agent conversion, runtime config format, hook carrier, and the verification scanner itself. Any repo-local layer that claims to stay in tune with that split has to recognize all five.

## Where Repo-Local Carry Already Travels In Tune

The repo-local modifier layer stays aligned with the upstream split across the Codex runtime, and it carries that alignment through several surfaces.

### Installer Entry Surface

- [e:c+i] `scripts/setup-portable-gsd.sh:21` invokes upstream as `npx get-shit-done-cc --codex --local`, then hands control to the repo-local overlay chain. Source: [scripts/setup-portable-gsd.sh](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh).
- [d:r:i] The repo-local entry surface commits to a single active runtime at install time rather than attempting to drive both runtimes from one script. That matches the repo's stated posture in [AGENTS.md:7](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md): `Active local runtime: .codex/get-shit-done`.

### Overlay Manifest Shape

- [e:c+i] The overlay manifest at [tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json) declares entries in Codex-shape directories: `agents/*.toml`, `config.toml`, `skills/gsd-*/SKILL.md`, plus the shared-across-runtimes `get-shit-done/` subtree (references/, templates/, workflows/, bin/lib/).
- [d:r:i] Every runtime-specific entry in the manifest is Codex-shape. The manifest does not claim to mutate Claude-shape paths (`commands/gsd/*.md`, `settings.json`, Claude agent `.md` without `.toml` companion). That is a clean separation rather than a blended contract.
- [e:c+i] The `overwrite` vs `add` mode typing distinguishes repo-local supplementation (`add`) from upstream-pristine overwriting (`overwrite`). Source: [tooling/codex/portable_gsd_contract.py:159-218](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/portable_gsd_contract.py). The contract refuses overlay drift (`missing_from_manifest`, `missing_from_overlay`, `overwrite_missing_in_backup`, `add_present_in_backup`, `backup_overlay_not_overwrite`). That policing is Codex-runtime-local and does not spill into Claude-runtime state.

### Reasoning-Defaults Application

- [e:c+i] `apply_reasoning_defaults` operates only on Codex-grammar config keys (`model_reasoning_effort` in `config.toml` and per-agent `.toml` files). Source: [tooling/codex/portable_gsd_contract.py:296-317](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/portable_gsd_contract.py).
- [e:c+i] The `QUALITY_REASONING` dict at [portable_gsd_contract.py:19-37](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/portable_gsd_contract.py) names 17 agents with effort levels that only apply to Codex agent `.toml` files; Claude has no equivalent carrier for this key.
- [d:r:i] Keeping this Codex-only is in tune with upstream's separation. A Claude-side reasoning-effort layer would need a different carrier entirely (Claude agents do not carry `model_reasoning_effort` TOML keys), so leaving this Codex-only rather than forcing a shared abstraction matches the upstream split.

### Update Workflow Provider Gate

- [e:c+i] The repo-local overlay `update.md` narrows the repo-local continuity gate to two runtimes explicitly. Source: [tooling/portable-gsd/overlay/get-shit-done/workflows/update.md:15](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/update.md):
  - Continuity reference surfaces only when `PREFERRED_RUNTIME` is `codex` or `claude` and repo-local `.codex/` or `.claude/` state is present.
- [e:c+i] The same gate is repeated at the step boundary at `update.md:352-362`, where the clean-install rematerialization asymmetry is named directly: `update` reads the continuity reference before the later clean-install step rewrites the runtime copy via overlay rematerialization.
- [d:r:i] The gate shape keeps repo-local continuity narrower than the broader seven-runtime detection block that surrounds it. That is stronger carry than a symmetric all-runtimes widening would have produced, because continuity only matters where the repo-local chain actually maintains contract.

### Update Wrapper Boundary

- [e:c+i] The wrapper at [tooling/portable-gsd/overlay/skills/gsd-update/SKILL.md:60-61](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/skills/gsd-update/SKILL.md) states the continuity boundary explicitly at `<objective>`: "This skill may surface repo-local entry/runtime continuity only when the active runtime is `.codex` or `.claude`. It does not translate that continuity into broader parity, matrix, or version-window claims."
- [d:r:i] That wrapper-side boundary keeps the continuity family narrow rather than letting it leak into provider-general parity pressure.

### Continuity Reference Posture

- [e:c+i] The continuity reference itself carries an asymmetric posture: "Repo-local entry continuity here is about observed `.codex` basis plus held `.claude` annotation." Source: [.codex/get-shit-done/references/entry-runtime-uplift-continuity.md:30](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/references/entry-runtime-uplift-continuity.md).
- [d:r:i] The reference spells out that `.codex` is observed-basis and `.claude` is held-annotation. That keeps the two-runtime horizon present without implying symmetric live carry across both.

### Codex Skill Adapter

- [e:c+i] The repo-local wrapper `skills/gsd-update/SKILL.md` carries a `<codex_skill_adapter>` block that translates Claude-syntax calls (`AskUserQuestion`, `Task(...)`) into Codex equivalents (`request_user_input`, `spawn_agent`). Source: [tooling/portable-gsd/overlay/skills/gsd-update/SKILL.md:8-46](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/skills/gsd-update/SKILL.md).
- [d:r:i] The adapter carries the Codex-native translation explicitly rather than assuming Claude syntax can run as-is under Codex. That is stronger carry than leaving the mismatch latent at execution time.

### Post-Materialization Verification

- [e:c+i] `verify-materialized` compares the rendered overlay text against live `.codex/` content per-entry and refuses any drift, with `normalize_reasoning_defaults` abstracting over the single Codex-only mutation that the installer reliably reapplies. Source: [tooling/codex/portable_gsd_contract.py:106-113, 320-368](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/portable_gsd_contract.py).
- [d:r:i] The verification path stays Codex-targeted and does not pretend to verify Claude-runtime state. That is in tune with the installer's single-runtime scope.

## Where Repo-Local Carry Still Blurs Runtime-Specific Responsibilities

These are the surfaces where repo-local layering carries weaker runtime disclosure than it could, or where it couples responsibilities that upstream already separates.

### Install Shape: Single-Runtime Anchor Without Disclosure

- [e:c+i] `scripts/setup-portable-gsd.sh:21` hardcodes `--codex --local` with no runtime-aware branch and no operator-visible statement that the repo's materialization chain targets Codex exclusively. Source: [scripts/setup-portable-gsd.sh](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh).
- [d:r:i] The single-runtime anchor is correct for the repo's current posture. The blur is that the caller sees `Installing repo-local regular GSD for Codex...` (line 19) once, but the governing doctrine carry about `.codex` being observed-basis while `.claude` is held-annotation lives inside `.codex/get-shit-done/references/entry-runtime-uplift-continuity.md:30`, not at the installer boundary itself. The installer output does not say "this installer does not materialize `.claude/` carriers; see continuity reference for held-annotation posture."
- [a:r:i] An operator who runs the installer and then finds a pre-existing `.claude/` directory on disk does not get told whether the repo-local chain touches it or intentionally leaves it. The actual live state shows this ambiguity concretely: `.codex/` was last rematerialized on Apr 22 while `.claude/` was last modified Apr 10 and is not in the overlay manifest at all.

### Hooks Carrier Versus Config Carrier: Silent In Installer

- [e:c+i] `scripts/setup-portable-gsd.sh` calls `apply-reasoning-defaults` (line 52-53) and `verify-materialized` (line 55-59), both of which operate on `config.toml` and `agents/*.toml` — the Codex-native config grammar. Source: [tooling/codex/portable_gsd_contract.py:98-99, 296-317](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/portable_gsd_contract.py) (`install_mutation_targets` returns `{config.toml, agents/<name>.toml for each quality-reasoning agent}`).
- [d:r:i] The repo-local mutation surface is Codex-grammar-only, but it is not named as Codex-grammar-only at the installer boundary or in the contract helper's CLI help text. A reader who arrives at `portable_gsd_contract.py` could infer that `apply-reasoning-defaults` is a general repo-local mutation, when in fact it only applies to Codex runtime state.
- [o:r:i] A later narrow uplift could carry that Codex-grammar scope as a docstring or CLI `--help` hint on `apply-reasoning-defaults` without widening the mutation itself. That would sharpen disclosure without changing behavior.

### Agent Carrier Asymmetry In Overlay Manifest

- [e:c+i] The overlay manifest declares paired `agents/<name>.md` (mode `overwrite`) and `agents/<name>.toml` (mode `add`) entries for `gsd-code-fixer`, `gsd-code-reviewer`, `gsd-intel-updater`, `gsd-pattern-mapper`, plus `.toml`-only `add` entries for `gsd-executor`, `gsd-phase-researcher`, `gsd-plan-checker`, `gsd-planner`, `gsd-verifier`. Source: [tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json).
- [d:r:i] The `.md` + `.toml` pairing is a Codex-specific convention: Codex reads agent `developer_instructions` from the `.toml` and optionally uses `.md` for companion content. Claude would use `.md` alone. The manifest silently encodes Codex assumptions here — a Claude-shape overlay would pair differently, and there is no manifest-side discipline that says so.
- [d:r:i] This is not a defect in current flow; it is a cost that becomes load-bearing only if a later parity slice wants Claude-shape overlay carriers. At that point the manifest schema itself would need to either fork per-runtime or learn a per-entry runtime tag.

### Runtime Detection Array As Implicit Contract

- [e:c+i] `update.md` inside the overlay keeps the upstream seven-runtime detection block verbatim at lines 53, 112, and 574. Source: [tooling/portable-gsd/overlay/get-shit-done/workflows/update.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/update.md).
- [d:r:i] Retaining upstream's full runtime-detection block is the right move for upstream parity (the workflow must still correctly identify whichever runtime invoked it). The blur is not that `.claude` appears in those arrays — that is mandatory — but that the overlay carries the full seven-runtime detection machinery inside a workflow whose repo-local continuity gate only honors two of them. Operators arriving at the workflow could read `RUNTIME_DIRS=( "claude:.claude" ...)` and infer that the repo-local maintenance chain also considers those seven paths.
- [o:r:i] The sharpest repo-local disclosure would be a one-line comment near the runtime-detection array naming the difference: detection covers all upstream-supported runtimes; repo-local continuity surface only covers `codex` and `claude`. That sharpens without re-authoring the upstream logic.

### Leak Scanner Warning Classification Is Ambient

- [e:c+i] The repo-local installer does not classify the upstream leak-scanner warnings after materialization. Live scan reproduces upstream's regex and surfaces three hits: `agents/gsd-debugger.toml:424`, `get-shit-done/workflows/update.md:438`, and the pristine backup copy at `gsd-local-patches/get-shit-done/workflows/update.md:438`. Source: reproduction via the same regex as [install.js:4367](/home/rookslog/.npm/_npx/a2a7266cd903ec8b/node_modules/get-shit-done-cc/bin/install.js) against the current `.codex/` materialization.
- [d:r:i] Every one of those hits is contextual rather than defect-class (see next section), but the repo-local chain does not record that classification anywhere durable. A later repo-local install run prints the same warning text upstream emits without any repo-local sharpening, and a future upstream bump that introduces new runtime-detection examples would be blended with any real active-pointer drift at the same warning count.
- [d:r:i] The blur here is not that warnings exist. The blur is that `contextual scanner hit` and `active runtime-pointer defect` travel under one warning signal, and the repo-local layer does not currently split them.

### Update Workflow Comment Example

- [e:c+i] `update.md:438` in the overlay reads `# RUNTIME_DIR is the resolved config directory (e.g. ~/.claude, ~/.config/opencode)`. Source: [tooling/portable-gsd/overlay/get-shit-done/workflows/update.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/update.md).
- [d:r:i] This specific hit is the only scanner-matched line inside the overlay source (all other `.claude` strings in the file use bare `.claude` without the `~/` or `$HOME` prefix and are invisible to the scanner regex). Rewriting this one comment example would quiet the scanner warning for the overlay-owned update.md, but only that one line.
- [d:r:i] The blur class here is example-centric: the comment carries Claude as the primary runtime example even though the repo-local chain targets Codex. A rewrite to use `~/.codex` (or to pair `~/.codex` and `~/.claude`) would stay inside the same example role while better matching the repo's active runtime. But doing this merely to silence the upstream scanner would be threshold-quieting residue — `.planning/AGENTS.md:212-213` explicitly names "do not rewrite explicit prohibitions, quoted examples, or historical evidence solely to quiet a scanner hit" as discipline. Any rewrite should therefore be justified by repo-local-posture alignment, not by the scanner signal alone.

### Two-Runtime Gate Without Live-Freshness Discipline

- [e:c+i] The `review_entry_runtime_continuity` gate in `update.md:351-362` surfaces the continuity reference when `PREFERRED_RUNTIME` is `codex` or `claude` AND repo-local `.codex/` or `.claude/` runtime state is present.
- [e:c+i] Live state: `.codex/` is currently maintained by the overlay chain (last rematerialized Apr 22), while `.claude/` is a pre-existing older install (last modified Apr 10) that the overlay chain does not touch. Source: directory listings under `ls -la` of the two runtime roots.
- [d:r:i] Semantically the gate is consistent with the continuity reference's own posture (`.codex` observed-basis, `.claude` held-annotation), so a `.claude/`-only presence still correctly routes to held-annotation carry. The blur is narrower: the gate condition does not distinguish between an actively-maintained `.claude/` (which the repo does not have a path for today) and a stale `.claude/` left over from an earlier install. Today, both states route to the same continuity read.
- [p:r:i] A repo that later accrues a maintained `.claude/` carrier (for example via a second repo-local installer branch) would pressure this gate into needing an additional freshness predicate. Holding that as projected rather than current work matches the audit's bounded scope.

## Which Surfaced Claude References Are Real Defects Versus Contextual Warnings

The deferred note at [intervention-proposals/132](../../intervention-proposals/132-codex-claude-installation-parity-audit-deferred-note.md) cited multiple `.claude` lines inside `update.md`. This audit reran upstream's scanner regex against the live `.codex/` tree and against the overlay source to separate what the scanner actually flags, what the deferred note listed as surrounding context, and how each hit should be classified.

### Upstream Scanner Regex

- [e:c+i] Upstream scanner pattern: `(?:~|\$HOME)\/\.claude\b`, matched against `.md` and `.toml` files (excluding `CHANGELOG.md`). Source: [install.js:4357-4373](/home/rookslog/.npm/_npx/a2a7266cd903ec8b/node_modules/get-shit-done-cc/bin/install.js).
- [d:r:i] The regex does not match bare `.claude` (it requires a `~/` or `$HOME/` prefix). That narrows the actual flag set significantly compared to the broader set of `.claude` mentions listed in the deferred note.

### Full Scanner Hit Classification

- [e:c+i] Live `.codex/` tree scan returns three hits (reproduced by running the upstream regex against the current `.codex/` materialization):

| File | Line | Text | Overlay-owned? | Class |
|------|------|------|----------------|-------|
| `agents/gsd-debugger.toml` | 424 | `configDir = ~/.claude` | No (not in manifest) | Contextual upstream carry — debugging example illustrating a path-indirection bug |
| `get-shit-done/workflows/update.md` | 438 | `# RUNTIME_DIR is the resolved config directory (e.g. ~/.claude, ~/.config/opencode)` | Yes (overwrite mode) | Contextual comment example inside runtime-detection logic |
| `gsd-local-patches/get-shit-done/workflows/update.md` | 438 | Same content | No (pristine backup) | Contextual — frozen pristine copy captured before overlay applies |

- [d:r:i] None of these hits is a broken active-pointer. All three are descriptive: a debugging-example snippet inside an agent contract, a comment example illustrating what `RUNTIME_DIR` looks like, and a pristine backup preserving the upstream-shipped example text. The scanner's blunt regex flags them because it has no notion of "comment example" versus "active pointer."

### Deferred Note Lines Not Flagged By Scanner

- [e:c+i] The deferred note listed additional `update.md` lines: 53, 112, 352, 574. Live reading of [tooling/portable-gsd/overlay/get-shit-done/workflows/update.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/update.md) shows:
  - Line 53: `RUNTIME_DIRS=( "claude:.claude" ... )` — bare `.claude`, no `~/` prefix, scanner does not match.
  - Line 112: `for dir in .claude .config/opencode ...` — bare `.claude`, scanner does not match.
  - Line 352: `If PREFERRED_RUNTIME is codex or claude ...` — plain word, no path, scanner does not match.
  - Line 574: `for dir in .claude .config/opencode ...` — bare `.claude`, scanner does not match.
- [d:r:i] Those lines are contextual-by-construction: they live inside runtime-detection arrays, iteration loops, or prose mentions of runtime names. They would each be a real defect only if the workflow attempted to anchor the repo-local continuity or mutation chain at those `.claude` entries, which it does not.

### Real-Defect Criteria

- [g:r:i] A hit would qualify as a real current defect if it met all of these:
  1. The path is addressed literally (not via runtime detection) from inside code the repo-local overlay owns as `overwrite`.
  2. The path would be read or mutated at execution time for the Codex runtime.
  3. There is no fallback or branch that translates the path to the Codex-native equivalent.
- [d:r:i] None of the current scanner hits or deferred-note lines meet all three criteria. Every `.claude` reference in repo-owned overlay code sits inside runtime-detection arrays (line 53, 112, 574), comment examples (line 438), or prose that names `claude` as a runtime label without using it as a path (line 352). The upstream-owned `agents/gsd-debugger.toml:424` reference sits inside a debugging-example block illustrating a path-indirection bug and is not a runtime pointer at all.

### Three-Class Split For Later Carriers

- [d:r:i] The field currently carries three distinguishable classes. Future scanner hits or deferred-note additions should be classified into one of these before being acted on:
  1. **Runtime-detection carriers** — arrays and loops that must list all upstream-supported runtimes for correct detection; bare `.claude` is mandatory here.
  2. **Comment and debugging examples** — illustrative text that picks one concrete example value; Claude-flavored examples are inherited from upstream and can be repo-locally re-flavored for Codex when that sharpens posture alignment.
  3. **Active pointers** — paths that would actually be read or mutated; the repo currently has none in Codex-targeted code, and the scanner would correctly flag any regression here.
- [d:r:i] The audit finds zero class-3 hits in the current state. All surfaced hits are class-1 or class-2. Treating them under one "unreplaced `.claude` path" warning compresses the distinction.

### Later-Family Improvement Pressure

- [o:r:i] The fact that upstream's scanner and upstream's own source each carry class-2 hits that remain after install (the `agents/gsd-debugger.toml:424` hit is upstream-only) raises a later-family question: should upstream's own pristine output be able to leak class-2 hits into every non-Claude install, and if so, what is the operator-facing disclosure path? That is upstream-scoped pressure and belongs outside this audit's bounded scope.
- [o:r:i] A narrower repo-local improvement route — classifying hits rather than silencing them — stays inside this audit's scope and is taken up under the next section.

## What To Keep Explicitly Later

These pressures sit adjacent to the audit but do not belong inside this bounded slice. Each is named with its boundary and rationale.

### Claude-Side Parity Install

- [o:r:i] Boundary: any repo-local materialization path that writes `commands/gsd/*.md`, `settings.json`, Claude agent `.md` without `.toml` companion, or templated hook .js files.
- [d:r:i] Rationale: the repo currently maintains Codex-shape overlay carriers only, and AGENTS.md:7 declares Codex the active local runtime. Building a second Claude-shape materialization chain would require extending `OVERLAY-MANIFEST.json` with Claude-shape entries, extending `setup-portable-gsd.sh` with runtime-aware dispatch, adding Claude-native conversion/verification in `portable_gsd_contract.py`, and resolving how the two runtime states should be maintained in lockstep or diverge intentionally. That is a much larger slice than this audit should subsume.

### Runtime-Aware Dispatch In `setup-portable-gsd.sh`

- [o:r:i] Boundary: any branching in the installer that would take a runtime argument, CLI flag, or env var and dispatch to Codex vs Claude materialization chains.
- [d:r:i] Rationale: depends on Claude-side parity install existing first. Without a Claude-shape overlay chain to dispatch to, the runtime branch has nothing to dispatch.

### Agent Conversion Carriers Beyond Codex

- [o:r:i] Boundary: any repo-local conversion functions analogous to upstream's `convertClaudeAgentToCodexAgent` for additional runtimes.
- [d:r:i] Rationale: the repo does not use upstream's other runtimes and has no evidence of needing them. Carrying conversion logic the repo would not exercise would be avoidable surface without present yield.

### Hook Carrier Parity

- [o:r:i] Boundary: repo-local hook-file templates, Claude-side `settings.json` hook entries, or a hook-dispatch abstraction that unifies Codex `[[hooks]]` stanzas and Claude `settings.json.hooks` arrays.
- [d:r:i] Rationale: hooks on Codex route through `config.toml` `[[hooks]]` blocks directly; hooks on Claude route through `settings.json` arrays. Upstream already carries both separately. The repo-local chain relies on upstream's Codex hook carrier and does not need to widen into Claude's until Claude-side parity install is on the table.

### Upstream Leak-Scanner Discipline

- [o:r:i] Boundary: any proposal that upstream's scanner should classify hits rather than count them, or that upstream's own `agents/gsd-debugger.toml` should adjust its path-indirection example.
- [d:r:i] Rationale: upstream-scoped. The repo-local audit can recognize the three classes of hits but has no standing to re-architect upstream's scanner or re-author upstream's pristine agent contracts.

### Comment-Example Re-Flavoring

- [o:r:i] Boundary: any rewrite of `update.md:438`'s example comment from `~/.claude` to `~/.codex`, or any other runtime-example edits inside overlay workflows aimed at silencing scanner warnings.
- [d:r:i] Rationale: `.planning/AGENTS.md:212-213` explicitly cautions against rewriting comment examples solely to quiet a scanner hit. A repo-local re-flavoring that also earns its place on posture grounds (the active runtime is Codex; Claude is held-annotation) could be defensible later, but only if the justification stands on posture alignment rather than on scanner-quieting. Keeping this explicitly later prevents residue-chasing from blending into the current parity audit.

### Live-Freshness Predicate On `.claude/` Gate

- [o:r:i] Boundary: any refinement of the `review_entry_runtime_continuity` gate that distinguishes stale pre-existing `.claude/` directories from actively-maintained ones.
- [d:r:i] Rationale: today there is no repo-local path that maintains `.claude/` actively. The gate's current behavior (surface continuity reference whenever `.claude/` exists) is harmless because the continuity reference itself carries held-annotation posture. A freshness predicate would become load-bearing only after a Claude-side maintenance path exists.

## Strongest Next Route

The strongest next bounded route sharpens the disclosure layer rather than adding or rewriting runtime-specific install carriers.

### Route Shape

- [d:r:i] A bounded classification carrier that distinguishes contextual `.claude` scanner hits (runtime-detection arrays, comment examples, upstream-pristine carry) from active-pointer defects, and freezes the current three-hit baseline with explicit per-hit classification.
- [d:r:i] Specifically, the route should:
  - Record the current scanner-hit inventory inside the repo-local contract layer (not inside an audit note alone) so any net-new class-3 hit or newly appearing class-1/2 hit surfaces in repo-local signal rather than being diluted by upstream warning noise.
  - Classify each of the three current hits explicitly: `agents/gsd-debugger.toml:424` as upstream-only contextual carry, `get-shit-done/workflows/update.md:438` as overlay-owned comment example, `gsd-local-patches/.../update.md:438` as pristine-backup mirror.
  - Leave comment-example rewriting, Claude-side parity, runtime-aware installer dispatch, and scanner re-architecture explicitly later.

### Why This Route

- [d:r:i] Compared to a comment-example rewrite: this route preserves the distinction between example wording and runtime contract. Rewriting one comment to quiet the scanner would narrow the scanner-hit count but would not sharpen future disclosure when upstream bumps a new example text into the overlay.
- [d:r:i] Compared to a Claude-side parity install: this route is two or three orders of magnitude smaller in carrier and verification surface, earns its value inside the current active-runtime posture, and does not lock the later parity family into a particular shape.
- [d:r:i] Compared to leaving the field as-is: this route converts ambient scanner-warning text into durable repo-local contract so later runs do not have to reconstruct the classification from memory. That matches the `.planning/AGENTS.md:58-59` contract-propagation carry rule: "If the propagation path is already clear, update those neighbors in the same slice rather than leaving the carry implicit."

### Carriers The Route Would Touch

- [p:r:i] Candidate carriers (for a later proposal to decide among, not for this audit to prescribe):
  - A small helper under `tooling/codex/` that runs the upstream regex plus a classification layer and prints a typed report.
  - An extension of `portable_gsd_contract.py verify-materialized` to surface scanner hits alongside content-mismatch and backup-missing checks, classified rather than counted.
  - A focused contract test under `tooling/codex/tests/` that freezes the three-hit baseline with class tags and refuses net-new class-3 hits.
- [d:r:i] Any of those carriers would keep the surface narrow. The choice among them is a later proposal question.

### What This Route Does Not Claim To Solve

- [d:r:i] The route does not solve the upstream leak-scanner's bluntness.
- [d:r:i] The route does not solve Claude-side carrier absence.
- [d:r:i] The route does not solve the `update.md:438` comment example's Claude-flavor bias. If posture-aligned re-flavoring is later pursued, the classification carrier would make that change legible rather than scanner-chasing.
- [d:r:i] The route does not extend to live-freshness discipline on the `.claude/` gate.

## How This Audit Should Be Inherited

### Carry Forward

- [d:r:i] The five-layer upstream separation (install shape, agent conversion, runtime config, hook carrier, leak scanner) is the frame a later parity slice should use. Treat it as the structure, not the conclusion.
- [d:r:i] The three-class `.claude` reference split (runtime-detection carriers / comment-and-debugging examples / active pointers) should travel into any later discussion of scanner hits, rather than letting new hits be counted under one blended "unreplaced `.claude` path" bucket.
- [d:r:i] The posture asymmetry from the continuity reference — `.codex` observed-basis, `.claude` held-annotation — should remain the governing posture for any later audit or slice. Parity in this repo is not symmetric live carry; it is active-plus-annotated.
- [d:r:i] The current live-state snapshot (`.codex/` Apr 22 rematerialization vs `.claude/` Apr 10 pre-existing install, with only `.codex/` in the overlay manifest) should be named explicitly at the boundary of any later slice so that the single-runtime-active posture is not lost in later reasoning.
- [d:r:i] The strongest-next-route framing (classification layer as the sharpest sharpening, not comment-example rewriting) should guide how any follow-through intervention proposal is scoped.

### Revise

- [d:r:i] If a later slice earns a Codex-flavor re-flavoring of `update.md:438` on posture grounds — not on scanner-quieting grounds — the audit output should be revised to name that justification explicitly so the residue-chasing concern does not re-emerge.
- [d:r:i] If a later upstream bump introduces a new class-3 (active-pointer) hit in overlay-owned content, this audit's claim that "the audit finds zero class-3 hits in the current state" should be narrowed explicitly to the 2026-04-22 commit `a75cfe7` snapshot, and the follow-through route should sharpen to the new hit rather than assuming continued absence.
- [d:r:i] If `AGENTS.md` or the continuity reference ever moves `.claude` posture off held-annotation and toward observed basis, the gate discipline and the live-freshness concern become load-bearing rather than projected. The audit's "explicitly later" entries for freshness and runtime-aware dispatch should then move into the active slice list.

### Hold For Later

- [d:r:i] Claude-side parity install, runtime-aware dispatch in `setup-portable-gsd.sh`, agent-conversion carriers beyond Codex, and hook-carrier parity all stay explicitly later per the earlier section. None of them is a current-slice concern even after the classification route lands.
- [d:r:i] Upstream-scoped disciplines (the scanner's bluntness, upstream's `gsd-debugger.toml` example, upstream's own multi-runtime example re-flavoring) stay outside the repo-local horizon.
- [d:r:i] The live-freshness predicate on the `.claude/` gate stays projected. It becomes current-slice work only after a maintained `.claude/` carrier path exists.
- [d:r:i] Broader multi-provider parity (opencode, gemini, kilo, cursor, windsurf, copilot, antigravity) stays outside the two-runtime horizon this audit was bounded to. The audit's horizon split should not be widened just because upstream supports more runtimes; the repo's actual surface today does not exercise them.
