# Checkpoint 4 GSD Runtime / Config / Overlay Truth Excellence

## Research Frame

- Mode: `synthesis`.
- Question: does the repo-local GSD install/config/overlay surface materially support excellent planning and execution work, or does it still hide enough drift and authority ambiguity to silently degrade quality?
- Scope: `.planning/config.json`, tracked `.codex/config.toml`, live `.codex/get-shit-done/`, live `.codex/agents/`, tracked overlay under `tooling/portable-gsd/overlay/`, ignored archival patch tree under `.codex/gsd-local-patches/`, and the install path in `scripts/setup-portable-gsd.sh`.
- Non-goals: full workflow-chain excellence, governance-doc ownership beyond runtime overlap, or patching the harness.
- Stop condition: enough direct evidence to say where runtime truth is strong, where it is weak, and whether the weakness is doctrine, protocol, or machinery.

## Path Of Inquiry

1. Read the governing repo docs plus the Checkpoint 4 lane spec and prior Checkpoint 3 runtime/Codex maps to inherit the accepted envelope instead of re-litigating scope.
2. Inspected the live install/config surfaces: `scripts/setup-portable-gsd.sh`, `.planning/config.json`, `.codex/config.toml`, `.codex/get-shit-done/bin/lib/{config,core,init,state,verify}.cjs`, representative workflows, and representative agent `.toml` / `.md` pairs.
3. Compared the tracked overlay against both the live `.codex/` runtime and the archival `.codex/gsd-local-patches/` tree to separate active install truth from provenance claims.
4. Ran read-only runtime spot checks:
   - `config-get workflow.discuss_mode --raw` returned `exploratory`
   - `config-get workflow.security_enforcement --raw` returned `Error: Key not found`
   - `init plan-phase 1 --raw` returned `researcher_model`, `planner_model`, and `checker_model` as `gpt-5.4`
   - `init execute-phase 1 --raw` returned `executor_model: "gpt-5.4"` and `verifier_model: ""`
   - `resolve-model gsd-planner --raw` returned `gpt-5.4`
   - `resolve-model gsd-verifier --raw` returned an empty string
   - `git ls-files` showed `.codex/config.toml` is tracked while `.codex/agents/`, `.codex/get-shit-done/`, and `.codex/gsd-local-patches/` are ignored surfaces in practice
5. Deferred: direct spawned-worker payload verification through live Codex launch logs or `~/.codex/state_5.sqlite`. This artifact therefore closes local runtime/config truth strongly, but not full live-launch inheritance proof.

## Current Strengths

- [e:c:i] The install path is concrete rather than folkloric: the repo installs local regular GSD, applies a tracked overlay from `tooling/portable-gsd/overlay`, then rewrites repo-specific reasoning defaults in `.codex/config.toml` and agent `.toml` files. Sources: `scripts/setup-portable-gsd.sh:10-31,33-82`.
- [e:r:i] In sampled comparisons, the live `.codex/get-shit-done/` runtime matched the tracked overlay, which means the current checkout is not running a mysterious untracked fork of the overlayed files. Basis: direct file comparison of live `.codex/get-shit-done/*` against `tooling/portable-gsd/overlay/*`.
- [e:c:i] The overlay does real quality work, not cosmetic patching: it makes `exploratory` discuss a first-class runtime mode, requires canonical references and four-bucket future-awareness in `CONTEXT.md`, and carries `future_preservation` into the plan contract. Sources: `tooling/portable-gsd/overlay/get-shit-done/workflows/discuss-phase.md:190-226`; `tooling/portable-gsd/overlay/get-shit-done/templates/context.md:93-143`; `tooling/portable-gsd/overlay/get-shit-done/templates/phase-prompt.md:14-29,143-149,165`.
- [e:c+r:i] Core planning/execution model policy is materially encoded for the most important roles: `.codex/config.toml` defaults the repo to `gpt-5.4` with `high` reasoning and `xhigh` plan-mode reasoning, `.planning/config.json` pins the four core GSD roles to `gpt-5.4`, and runtime spot checks confirmed that planner/researcher/checker/executor resolve that way. Sources: `.codex/config.toml:1-4`; `.planning/config.json:38-47`; `.codex/get-shit-done/bin/lib/core.cjs:1300-1330`; `.codex/get-shit-done/bin/lib/init.cjs:85-99,207-218`.
- [e:c:i] The runtime already contains one useful anti-drift check on agent availability: `init` injects `agents_installed` / `missing_agents`, and `verify.cjs` warns that missing agents cause `Task(subagent_type="gsd-*")` fallback to general-purpose behavior. Sources: `.codex/get-shit-done/bin/lib/init.cjs:32-47`; `.codex/get-shit-done/bin/lib/verify.cjs:702-718`.

## Where Runtime Truth Reliably Supports Quality

- [e:c+r:i] The repo has made uncertainty-preserving discuss behavior runtime-real, not merely doctrinal. `workflow.discuss_mode` is both set in live config and consumed by the overlayed discuss workflow, and the current runtime reports `exploratory` directly. Sources: `.planning/config.json:15-32`; `tooling/portable-gsd/overlay/get-shit-done/workflows/discuss-phase.md:190-226`.
- [e:c:i] The steering brief and plan artifact contracts now materially protect future-aware work quality. Downstream agents are told to read canonical refs before acting, and plans are expected to preserve seams/non-decisions instead of silently flattening them. Sources: `tooling/portable-gsd/overlay/get-shit-done/templates/context.md:93-143`; `tooling/portable-gsd/overlay/get-shit-done/templates/phase-prompt.md:123-179`.
- [e:c+r:i] Core planning and execution truth is strong enough to trust in this checkout: the important agents do not merely inherit a vague profile table; they resolve to `gpt-5.4` in direct init/resolve-model checks. Sources: `.planning/config.json:38-47`; `.codex/get-shit-done/bin/lib/core.cjs:1300-1330`; direct runtime spot checks listed in `Path Of Inquiry`.
- [e:c:i] The runtime tries to prevent one of the worst silent degradations, namely missing specialized agents. That does not solve all authority problems, but it is a real quality support surface rather than a doc-only reminder. Sources: `.codex/get-shit-done/bin/lib/init.cjs:32-47`; `.codex/get-shit-done/bin/lib/verify.cjs:702-718`.

## Where Runtime Truth Leaves Quality Exposed

- [e:c+r:i] Install reproducibility is weaker than the repo’s current portability story. The installer pulls `npx get-shit-done-cc --codex --local` without a version pin, while the live vendored runtime and archival patch manifest are explicitly tied to `1.34.2`. That means a future reinstall can apply the current overlay against a newer upstream base without any first-class compatibility guard. Sources: `scripts/setup-portable-gsd.sh:10-14`; `.codex/get-shit-done/VERSION:1`; `.codex/gsd-local-patches/backup-meta.json:2-4`.
- [e:c+r:i] Overlay provenance is split and already stale. The tracked overlay is the active install source, but the archival `.codex/gsd-local-patches` tree has already diverged substantively from it, and that archival tree lives under an ignored path. The result is that the repo has a live truth path and a provenance-looking path that no longer cleanly agree. Sources: `scripts/setup-portable-gsd.sh:13-31`; `.codex/gsd-local-patches/backup-meta.json:2-19`; `.codex/gsd-local-patches/get-shit-done/templates/context.md:96-99`; `tooling/portable-gsd/overlay/get-shit-done/templates/context.md:96-99`; `.gitignore:1`.
- [e:c+r:i] Portability is partial, not clean. The overlay README says checkout-specific paths are templated as `__PROJECT_ROOT__`, but at least two tracked overlay workflows still hardcode `/home/rookslog/workspace/projects/prix-guesser`, and tracked `.codex/config.toml` also carries absolute repo-path references into an otherwise ignored runtime tree. A fresh checkout therefore depends on rerunning install, not on committed files being self-portable. Sources: `tooling/portable-gsd/README.md:7-17`; `tooling/portable-gsd/overlay/get-shit-done/workflows/discuss-phase-assumptions.md:556-575,627-639`; `tooling/portable-gsd/overlay/get-shit-done/workflows/quick.md:132-144,671-673,832-839`; `.codex/config.toml:20-114`.
- [e:c+r:i] Config ownership is uneven enough to mislead reviewers. `workflow.use_worktrees`, `workflow.discuss_mode`, and `_auto_chain_active` are supported and documented, but `loadConfig()` still does not normalize `use_worktrees`, so workflows read it through raw `config-get`. Separately, the security trio is template-real and workflow-real, but not in `VALID_CONFIG_KEYS`, not available via `config-set`, and not present in the planning-config/settings field references. `workflow.code_review` is valid and live in config, yet omitted from those same docs. Sources: `.codex/get-shit-done/templates/config.json:1-15`; `.codex/get-shit-done/bin/lib/config.cjs:14-39,122-159,335-397`; `.codex/get-shit-done/bin/lib/core.cjs:331-366`; `.codex/get-shit-done/workflows/plan-phase.md:446-470`; `.codex/get-shit-done/workflows/quick.md:665-673`; `.codex/get-shit-done/references/planning-config.md:225-260`; `.codex/get-shit-done/workflows/settings.md:28-38,159-165,174-199`; `.planning/config.json:15-32`.
- [e:c+r:i] Agent and model authority are only partially stabilized. Runtime registry authority lives in tracked `.codex/config.toml` pointing at ignored agent `.toml` files, install/verification logic still checks `.md` presence, and `.md` / `.toml` content has already drifted materially. On top of that, verifier and other non-overridden roles resolve to an empty model string and therefore rely on ambient Codex defaults rather than an explicit GSD-side model choice. Sources: `.gitignore:1`; `.codex/config.toml:20-114`; `.codex/get-shit-done/bin/lib/core.cjs:1236-1284,1300-1330`; `.codex/get-shit-done/bin/lib/init.cjs:85-99`; `.codex/agents/gsd-planner.md:44-57`; `.codex/agents/gsd-planner.toml:37-50`; `.planning/config.json:38-47`; direct runtime spot checks listed in `Path Of Inquiry`.

## Authority / Config / Overlay Risk Assessment

- `Install source drift` — `high`.
  [e:c+r:i] Current live state happens to be aligned around `1.34.2`, but the installer does not pin that upstream version. The repo is therefore one reinstall away from exercising the overlay against a different upstream basis. Sources: `scripts/setup-portable-gsd.sh:10-14`; `.codex/get-shit-done/VERSION:1`; `.codex/gsd-local-patches/backup-meta.json:2-4`.
- `Overlay provenance drift` — `high`.
  [e:c+r:i] The tracked overlay is authoritative for install, while the archival backup tree looks authoritative enough to mislead later readers but has already drifted and sits in an ignored path. Sources: `scripts/setup-portable-gsd.sh:13-31`; `.codex/gsd-local-patches/backup-meta.json:2-19`; `.gitignore:1`; `.codex/gsd-local-patches/get-shit-done/templates/context.md:96-99`; `tooling/portable-gsd/overlay/get-shit-done/templates/context.md:96-99`.
- `Path portability truth` — `high`.
  [e:c+r:i] The overlay portability claim is incomplete because some tracked overlay files and tracked `.codex/config.toml` still embed checkout-specific absolute paths. Sources: `tooling/portable-gsd/README.md:7-17`; `tooling/portable-gsd/overlay/get-shit-done/workflows/discuss-phase-assumptions.md:556-575,627-639`; `tooling/portable-gsd/overlay/get-shit-done/workflows/quick.md:132-144,671-673,832-839`; `.codex/config.toml:20-114`.
- `Config API truth` — `medium-high`.
  [e:c+r:i] Reviewers cannot safely infer “supported config” from one surface. The template, raw workflow probes, `VALID_CONFIG_KEYS`, `loadConfig()`, `planning-config.md`, and `settings.md` do not currently expose one clean contract. Sources: `.codex/get-shit-done/templates/config.json:1-15`; `.codex/get-shit-done/bin/lib/config.cjs:14-39,122-159,335-397`; `.codex/get-shit-done/bin/lib/core.cjs:331-366`; `.codex/get-shit-done/references/planning-config.md:225-260`; `.codex/get-shit-done/workflows/settings.md:28-38,159-165,174-199`.
- `Agent / model authority truth` — `medium-high`.
  [e:c+r:i] Core four roles are pinned strongly enough for current use, but verifier/auxiliary roles still depend on ambient model defaults, and human-facing `.md` files are no longer a trustworthy proxy for runtime instructions. Sources: `.planning/config.json:38-47`; `.codex/config.toml:1-4,20-114`; `.codex/get-shit-done/bin/lib/core.cjs:1236-1330`; `.codex/agents/gsd-planner.md:44-57`; `.codex/agents/gsd-planner.toml:37-50`.

## Strongest Justified Criticisms

1. [e:c+r:i] The repo’s current “portable local GSD” story overstates actual reproducibility. A version-specific overlay is being installed on top of an unpinned upstream `npx` install. That is the clearest way to believe runtime truth is governed while still letting upstream drift silently change the machinery. Sources: `scripts/setup-portable-gsd.sh:10-14`; `.codex/get-shit-done/VERSION:1`; `.codex/gsd-local-patches/backup-meta.json:2-4`; `tooling/portable-gsd/README.md:3-17`.
2. [e:c+r:i] Git-visible review does not currently expose the whole runtime authority chain. Tracked `.codex/config.toml` points to ignored agent `.toml` files, the vendored runtime is ignored, and the archival provenance tree is also ignored and already stale. That means a clean repo diff can still hide materially relevant runtime drift. Sources: `.gitignore:1`; `.codex/config.toml:20-114`; `.codex/gsd-local-patches/backup-meta.json:2-19`.
3. [e:c+r:i] The repo still relies on behaviorally real but weakly governed config seams. Security, worktree, auto-chain, and code-review behavior are spread across template defaults, raw `config-get` probes, partially documented references, and partially normalized loader code. That is not a clean “config contract”; it is an accretion of real behaviors. Sources: `.codex/get-shit-done/templates/config.json:1-15`; `.codex/get-shit-done/bin/lib/config.cjs:14-39,122-159,335-397`; `.codex/get-shit-done/bin/lib/core.cjs:331-366`; `.codex/get-shit-done/workflows/plan-phase.md:446-470`; `.codex/get-shit-done/workflows/quick.md:665-673`; `.codex/get-shit-done/references/planning-config.md:225-260`.
4. [e:c+r:i] Model/reasoning truth is only partially explicit. The strongest current work lanes are pinned well enough, but verifier and other non-overridden roles fall through to ambient defaults, and `.md` files are already inaccurate enough that humans can inspect the wrong authority surface. Sources: `.planning/config.json:38-47`; `.codex/config.toml:1-4`; `.codex/get-shit-done/bin/lib/core.cjs:1300-1330`; `.codex/agents/gsd-planner.md:44-57`; `.codex/agents/gsd-planner.toml:37-50`.

## Strategic Opportunities

- [p:r:i] Pin the install source to an explicit upstream GSD version and record overlay compatibility against that version. This is the cleanest way to turn “current live state happens to be 1.34.2” into actual install truth.
- [p:r:i] Replace the ignored archival patch tree as the repo’s provenance witness with one tracked manifest that states: upstream base version, tracked overlay file list, and whether live runtime matched overlay at the last regeneration checkpoint.
- [p:r:i] Decide whether the security trio, `use_worktrees`, `code_review`, and `_auto_chain_active` belong in the normalized config API. If yes, give them one supported path. If no, stop implying they are governed like ordinary settings.
- [p:r:i] Make agent authority single-source or generated. Either runtime should trust `.toml` and human docs should be generated from it, or the repo should stop treating `.md` files as meaningful runtime-adjacent references.
- [p:r:i] Finish the portability job: template the remaining absolute-path overlays and decide whether tracked `.codex/config.toml` should remain a checkout-specific committed file or become a generated install artifact.

## Ownership Assessment

| Material finding | Classification | Why |
| --- | --- | --- |
| Unpinned upstream install against a `1.34.2` overlay/base | `machinery-owned` | Doctrine cannot pin package resolution; the installer or install manifest must do it. |
| Live overlay is authoritative, but archival `.codex/gsd-local-patches` provenance is stale and ignored | `split/ambiguous` | The weakness is partly machinery/provenance design and partly workflow discipline around regeneration/checkpointing. Docs alone are insufficient, but machinery alone would still need protocol. |
| Remaining absolute-path portability holes in tracked overlay files and tracked `.codex/config.toml` | `machinery-owned` | This is a concrete install/materialization problem, not a policy wording issue. |
| Config contract split across template defaults, raw probes, loader normalization, and partial docs | `split/ambiguous` | The runtime API needs cleanup, but workflow/config-reference ownership also needs a deliberate contract decision. |
| Core four model truth is strong; verifier/auxiliary truth still depends on ambient defaults | `split/ambiguous` | Repo doctrine already says what it wants, but machinery does not encode the whole policy explicitly. |
| Runtime registry authority in `.toml` while install/check/human review still lean on `.md` surfaces | `machinery-owned` | This is an authority-surface mismatch inside the harness itself. |

## Conditional Follow-Through Candidates

- If Checkpoint 5 opens on runtime reproducibility, make `setup-portable-gsd.sh` version-aware before any broader harness redesign.
- If rerun readiness requires git-reviewable runtime truth, replace or retire `.codex/gsd-local-patches` as an ignored provenance surface.
- If the repo wants config audits to mean anything stronger than “the key exists somewhere,” decide which workflow keys are first-class supported settings and normalize/document them end-to-end.
- If the repo wants agent launch truth to survive later scrutiny, run one bounded live-spawn verification lane that checks actual worker payload authority against `.codex/config.toml`, agent `.toml`, and current runtime overrides.
- If the repo wants the portability claim to be literal rather than procedural, remove the remaining absolute-path residues and stop relying on reinstall as the only path-normalization step.

## Sources

- Local files inspected:
  `scripts/setup-portable-gsd.sh`, `.planning/config.json`, `.gitignore`, `.codex/config.toml`, `.codex/get-shit-done/VERSION`, `.codex/get-shit-done/bin/lib/{config,core,init,state,verify}.cjs`, `.codex/get-shit-done/templates/config.json`, `.codex/get-shit-done/references/planning-config.md`, `.codex/get-shit-done/workflows/{discuss-phase,plan-phase,quick,settings}.md`, `.codex/agents/{gsd-planner,gsd-verifier}.{md,toml}`, `.codex/gsd-local-patches/backup-meta.json`, `.codex/gsd-local-patches/get-shit-done/templates/context.md`, `tooling/portable-gsd/README.md`, `tooling/portable-gsd/overlay/get-shit-done/{templates,workflows}/*`, `tooling/portable-gsd/overlay/skills/gsd-discuss-phase/SKILL.md`.
- Runtime spot checks executed:
  `node .codex/get-shit-done/bin/gsd-tools.cjs config-get workflow.discuss_mode --raw`
  `node .codex/get-shit-done/bin/gsd-tools.cjs config-get workflow.security_enforcement --raw`
  `node .codex/get-shit-done/bin/gsd-tools.cjs init plan-phase 1 --raw`
  `node .codex/get-shit-done/bin/gsd-tools.cjs init execute-phase 1 --raw`
  `node .codex/get-shit-done/bin/gsd-tools.cjs resolve-model gsd-planner --raw`
  `node .codex/get-shit-done/bin/gsd-tools.cjs resolve-model gsd-verifier --raw`
  `git ls-files ...`
  `git status --short --ignored ...`
  `diff -rq` and targeted `diff -u` comparisons between live `.codex/`, tracked overlay, and archival `.codex/gsd-local-patches/`.
