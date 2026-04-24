# Consumer Authority Map

Date: 2026-04-24
Plan: `003-instruction-surface-generation-parity`

## Authority Categories

| Category | Meaning |
| --- | --- |
| Governing runtime instruction | A surface a runtime agent or workflow is told to obey as project authority. |
| Tracked doctrine carrier | A surface fingerprinted or reported for drift/proposal purposes, without necessarily being governing truth for every runtime. |
| Generated project output | A file that an initialization or generator command is supposed to create or refresh. |
| Human onboarding guidance | A source-maintained guide for operators and reviewers. |
| Materialized runtime entrypoint | Generated `.codex` or `.claude` runtime file produced from overlay source. |
| Stale or absent surface | A named carrier that is not present in this worktree or whose generation path is unproven. |

## Root And Planning Instruction Files

| Surface | Current worktree state | Consumer family | Authority classification | Notes |
| --- | --- | --- | --- | --- |
| `AGENTS.md` | Present | Operators, Codex agents, repo workflows by convention, onboarding docs | Governing runtime instruction and human operator guidance | The repo's live `AGENTS.md` defines source-of-truth, runtime surface, propagation, commit, and verification rules. Codex agents explicitly read repo-root `AGENTS.md`. Claude onboarding also starts from `AGENTS.md` in this repo. |
| `.planning/AGENTS.md` | Absent | Codex agents when work touches `.planning/`; uplift catalog | Governing instruction when present; tracked doctrine carrier | Multiple Codex agent prompts say to read it when phase context or artifacts live under `.planning/`. Absence is tolerated by those prompts, but it remains catalogued for host/project uplift. |
| `CLAUDE.md` | Absent | Uplift catalog; installed upstream new-project workflow for non-Codex hosts | Tracked doctrine carrier; generated upstream default for non-Codex | Codex agents explicitly reject `./CLAUDE.md` as governing truth for Codex. The modifier overlay currently does not generate it in `new-project.md`. |
| `.planning/CLAUDE.md` | Absent | Uplift catalog | Tracked doctrine carrier | No observed runtime agent in this repo treats it as Codex authority. Its catalog role appears to be drift/proposal tracking for hosts that carry Claude doctrine. |

## Codex Agent Consumers

Codex agent prompts in `tooling/portable-gsd/overlay/agents/` consistently treat `AGENTS.md` and, when relevant, `.planning/AGENTS.md` as the governing project instruction surface.

Examples:

- `gsd-executor.toml` tells the executor to read repo-root `AGENTS.md`, read `.planning/AGENTS.md` when phase context or artifacts live under `.planning/`, and not treat `./CLAUDE.md` as governing truth for the repo.
- `gsd-code-reviewer.md` and `gsd-code-reviewer.toml` use the same instruction model for reviews.
- `gsd-phase-researcher.toml`, `gsd-planner.toml`, `gsd-plan-checker.toml`, and `gsd-verifier.toml` all use the same `AGENTS.md` / `.planning/AGENTS.md` authority pattern.

Authority conclusion: for Codex agents, `AGENTS.md` is governing and `CLAUDE.md` is explicitly non-governing.

## Shared Workflow Consumers

Shared workflow source under `tooling/portable-gsd/overlay/get-shit-done/workflows/` uses a mixed model:

- `new-project.md` is a producer of the root instruction file and currently names `AGENTS.md` for all runtimes in the modifier overlay.
- `plan-phase.md`, `quick.md`, and related flows tell agents to read `./AGENTS.md` if present for project-specific guidelines.
- `progress.md` and `transition.md` consume uplift progress information from `project_uplift.py`, not root instruction body text directly.
- `update.md` says update does not itself refresh governing docs or repo-local instruction surfaces and routes later posture refresh to `$gsd-uplift-project --write`.

Authority conclusion: shared workflows use `AGENTS.md` as the project instruction read surface, while uplift/reporting flows treat instruction files as drift-sensitive carriers.

## Claude-Facing Consumers

Claude-facing source in this repo is primarily:

- `harness_modifier/overlay/commands/gsd/`
- shared workflow bodies mapped to Claude runtime targets by the overlay manifest
- `docs/onboarding/claude.md`

Observed authority:

- `docs/onboarding/claude.md` starts from `AGENTS.md`, then `WORKFLOW.md`, `docs/development.md`, and `docs/migration-origin.md`.
- Claude command wrappers route into `.claude/get-shit-done/workflows/...` for specialist workflows.
- The installed upstream new-project workflow would generate `CLAUDE.md` for non-Codex runtimes, but the modifier overlay changed that filename policy to `AGENTS.md` for all runtimes.

Authority conclusion: this repo's maintained Claude onboarding uses `AGENTS.md` as the source instruction guide, but installed upstream GSD still carries a `CLAUDE.md` generation model. The modifier needs an explicit decision before claiming those are equivalent.

## Uplift And Reporting Consumers

`harness_modifier/uplift/carrier_catalog.json` and `tooling/codex/project_uplift.py` treat instruction surfaces as reportable carriers.

Tracked file carriers include:

- `.planning/AGENTS.md`
- `.planning/CLAUDE.md`
- `AGENTS.md`
- `CLAUDE.md`
- `.codex/config.toml`
- `tooling/codex/README.md`

The runtime agent registry additionally tracks `.codex/agents/*.toml`.

Authority conclusion: uplift tracking is broader than Codex runtime authority. It can track `CLAUDE.md` as doctrine-sensitive without making `CLAUDE.md` governing for Codex.

## Materialization Consumers

The overlay manifest and contract tools are the materialization authority:

- `tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json`
- `scripts/setup-portable-gsd-runtime.sh`
- `harness_modifier/contract/portable_gsd_contract.py`
- `harness_modifier/contract/runtime_visibility.py`
- `harness_modifier/contract/harness_canary.py`

These tools materialize and verify runtime roots, but they do not currently generate project-root `AGENTS.md` or `CLAUDE.md` for host projects. That remains an initialization workflow and generator-command concern.

Authority conclusion: materialization checks prove overlay-to-runtime coherence after setup; they do not by themselves prove host project instruction file generation.

## Onboarding And Operator Docs

| Surface | Role |
| --- | --- |
| `WORKFLOW.md` | Short operator sequence for this extracted repo. |
| `docs/development.md` | Runtime/source/provenance layer split and typical verification. |
| `docs/install-profiles.md` | Active `codex-core`, `claude-core`, and `dual-runtime-core` claims. |
| `docs/onboarding/codex.md` | Codex bootstrap route. |
| `docs/onboarding/claude.md` | Claude bootstrap route and current Claude posture. |
| `docs/runtime-intervention-surfaces.md` | Prior intervention surface map and deferred questions. |

Authority conclusion: these are maintained source docs and should stay aligned with any future instruction-generation posture change.

## Consumer Risk Summary

- Changing `new-project.md` to generate `CLAUDE.md` again would affect Claude-facing host initialization and would need docs, catalog, and tests to explain why this repo's Claude onboarding still starts from `AGENTS.md`.
- Keeping single generated `AGENTS.md` without fixing the generator command leaves the workflow claiming a file write that the installed SDK handler does not perform.
- Replacing the SDK query with the CJS generator would need a runtime-root-safe command path and an explicit decision about whether a `CLAUDE.md`-templated body is acceptable as generated `AGENTS.md`.
- Removing `CLAUDE.md` from the carrier catalog would be a reporting-contract change and is not justified by Codex agent non-authority alone.
