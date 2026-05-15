# CLAUDE.md

## Scope

This is the Claude-side governance carrier for `gsd-modifier`.

The runtime-neutral source of truth is [AGENTS.md](AGENTS.md). Everything in AGENTS.md — Source Of Truth, Live Control Surface, Working Rules, Workflow Rules, Contract Propagation, Auditability And Review, Delegation And Review, Commit Hygiene, Verification — applies in full to Claude work in this repo. This file does not duplicate that content. It captures only the Claude-specific surface that AGENTS.md cannot cleanly express in runtime-neutral terms.

If a runtime-facing claim here ever conflicts with AGENTS.md, AGENTS.md governs.

## Read Order

1. [AGENTS.md](AGENTS.md) — runtime-neutral governance (read in full)
2. This file — Claude-specific addenda only
3. [WORKFLOW.md](WORKFLOW.md) — primary operator surface
4. [docs/development.md](docs/development.md)
5. [docs/handoff/current.md](docs/handoff/current.md) — live operational state

## Claude-Specific Runtime Surface

- Install root: `~/.claude/get-shit-done/`
- Materialized runtime root in this repo: `.claude/get-shit-done/`
- Skill routing: `commands/gsd/<cmd>.md` for user-invoked slash commands; subagent prompts under `agents/`
- `CLAUDE.md` files (this file at the repo root, plus any `~/.claude/CLAUDE.md` and `<runtime-root>/CLAUDE.md`) are auto-loaded into the system prompt at Claude Code session start; `AGENTS.md` is not

## Cross-Runtime Parity Carrier

`gsd-modifier` declares three install profiles: `codex-core`, `claude-core`, `dual-runtime-core`. Parity means shared core outcomes per `parity_tier` in `tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json`, not byte-identical files. See AGENTS.md "Working Rules" for the parity definition.

## Modifier-Owned Capabilities On Claude Side

Net-new modifier capabilities materialize for Claude under `commands/gsd/`:

- `commands/gsd/uplift-project.md`
- `commands/gsd/propagation-review.md`
- `commands/gsd/seed-migration-inventory.md`

These are declared `parity_tier: core_adapted` in the overlay manifest — the same capability has different shape per runtime (Codex consumes a `skills/gsd-<cap>/SKILL.md` for each).

## Workflow Discipline

The propose-evidence-approve discipline in AGENTS.md "Workflow Rules" applies under Claude without modification:

- For ambiguous, architectural, policy-bearing, or contract-carrying changes: state the observed problem, proposed change, why it's appropriate, alternatives considered, expected write set, and verification plan; wait for explicit user approval before editing or committing.
- Read-only investigation is allowed before approval.
- Small mechanical fixes may proceed only when the user's request is already explicit and the change is low-risk.
- If the user challenges the premise of a change, pause implementation and reconcile before touching files.

The change-class trigger taxonomy in AGENTS.md "Workflow Rules → Change-Class Triggers" applies under Claude. The five classes (overlay carrier, contract surface, install/bootstrap, governance, plan disposition) are runtime-neutral.

## Verification (Claude-side anchors)

The verification stack in AGENTS.md "Verification" is runtime-neutral and runs identically here. Claude-side notes:

- Materialized verification (`portable_gsd_contract.py verify-materialized`) reads the `.claude/` runtime root for Claude profiles; same tool, different roots.
- Hooks live under `~/.claude/hooks/` for Claude versus `~/.codex/hooks/` for Codex; the overlay manifest does not currently declare hooks under `parity_tier: core_required`.

## Auditability

Same as AGENTS.md "Auditability And Review". A senior reviewer or external AI auditor reading this file together with AGENTS.md should be able to follow modifier governance without any prior conversation context.
