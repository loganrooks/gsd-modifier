Date: 2026-04-21
Status: active companion artifact

# Runtime Materialization And Authority

## Purpose

- [g:r:i] This companion artifact maps the repo-local harness as a materialization chain rather than a flat doc set, so future intervention work can distinguish declared authority from effective runtime authority before choosing where to intervene.
- [d:r:i] It exists because the submitted PR docs, the older C3/C4/C5 mapping work, and the later intervention audit all converged on the same pressure: contributor/reference docs alone do not carry runtime mutation order, authority drift, or intervention leverage strongly enough for harness-wide modification planning.

## Governing Split

- [g:c+i] This repo explicitly treats repo-local regular GSD as the live runtime, with `.codex/get-shit-done` as the active harness and `./scripts/setup-portable-gsd.sh` as the local install/materialization command. Sources: [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:5), [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:7), [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:8).
- [d:r:i] That means runtime truth here is not reducible to any one of:
  - upstream package files alone
  - tracked overlay files alone
  - frozen docs PR snapshot alone
  - readiness audit package alone
- [d:r:i] Runtime truth has to be read as a composition chain whose later stages can override or narrow the authority of earlier ones.

## Materialization Chain

### 1. Upstream Base Install

- [e:c+i] The installer begins by running `npx get-shit-done-cc --codex --local`, so the first layer is the current upstream/npm-installed regular GSD payload, not a repo-authored scaffold. Source: [scripts/setup-portable-gsd.sh](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh:20).
- [e:c+i] The currently materialized base version in this repo is `1.38.3`. Sources: [.codex/get-shit-done/VERSION](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/VERSION:1), [.codex/gsd-file-manifest.json](/home/rookslog/workspace/projects/prix-guesser/.codex/gsd-file-manifest.json:2).

### 2. Tracked Overlay Copy

- [e:c+i] After the upstream install, the script copies every file from `tooling/portable-gsd/overlay/` into `.codex/`, substituting `__PROJECT_ROOT__` and the selected compact prompt path as it writes. Sources: [scripts/setup-portable-gsd.sh](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh:23), [scripts/setup-portable-gsd.sh](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh:26), [scripts/setup-portable-gsd.sh](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh:38), [scripts/setup-portable-gsd.sh](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh:41).
- [e:c+i] The overlay therefore acts as the tracked repo-local intervention canon for any file it covers, but only for the subset of the runtime tree it actually ships. Sources: [scripts/setup-portable-gsd.sh](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh:26), [tooling/portable-gsd/overlay/config.toml](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/config.toml:1).

### 3. Post-Copy Mutation Pass

- [e:c+i] The installer then mutates the freshly materialized `.codex/` tree again: it rewrites top-level `model_reasoning_effort` and selected agent `.toml` files after overlay copy completes. Sources: [scripts/setup-portable-gsd.sh](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh:46), [scripts/setup-portable-gsd.sh](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh:55), [scripts/setup-portable-gsd.sh](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh:66), [scripts/setup-portable-gsd.sh](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh:86).
- [d:r:i] This matters because the tracked overlay is not the last writer. Effective runtime truth can move one step beyond overlay canon in the installer’s mutation stage.

### 4. Live Materialized Runtime

- [e:c+i] The active runtime registry sits in `.codex/config.toml`, which points agent entries at repo-local `.codex/agents/*.toml` contracts and carries the live model/reasoning defaults for this repo. Sources: [.codex/config.toml](/home/rookslog/workspace/projects/prix-guesser/.codex/config.toml:1), [.codex/config.toml](/home/rookslog/workspace/projects/prix-guesser/.codex/config.toml:2), [.codex/config.toml](/home/rookslog/workspace/projects/prix-guesser/.codex/config.toml:20), [.codex/config.toml](/home/rookslog/workspace/projects/prix-guesser/.codex/config.toml:76).
- [e:c+i] The live `.codex/config.toml` already differs from overlay+installer expectation on the top-level reasoning line: the overlay declares `high`, the installer rewrites to `high`, and the current live file says `xhigh`. Sources: [tooling/portable-gsd/overlay/config.toml](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/config.toml:2), [scripts/setup-portable-gsd.sh](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh:57), [.codex/config.toml](/home/rookslog/workspace/projects/prix-guesser/.codex/config.toml:2).
- [d:r:i] So the live `.codex/` tree is the effective runtime surface, but it is not safely inferable from a single earlier layer without checking for later drift or repo-local intentional overrides.

### 5. Planning / Output Layer

- [e:c+i] `.planning/config.json` is a live runtime input even though it lives outside `.codex/`: workflow flags such as `auto_advance`, `discuss_mode`, `code_review`, and model overrides are read downstream by the harness. Sources: [.planning/config.json](/home/rookslog/workspace/projects/prix-guesser/.planning/config.json:15), [.planning/config.json](/home/rookslog/workspace/projects/prix-guesser/.planning/config.json:20), [.planning/config.json](/home/rookslog/workspace/projects/prix-guesser/.planning/config.json:27), [.planning/config.json](/home/rookslog/workspace/projects/prix-guesser/.planning/config.json:38).
- [d:r:i] `.planning/` is therefore not just audit residue; some of it is runtime-consumed steering state, while other parts remain review/control surfaces only. Future intervention work has to distinguish those subfamilies instead of treating `.planning/` as one undifferentiated layer.

## Declared Vs Effective Authority Register

| Surface family | Declared authority | Effective authority now | Intervention consequence |
| --- | --- | --- | --- |
| Submitted PR docs / frozen snapshot | stable docs-governance and contributor-reference pressure | not current runtime truth | preserve as stable reference/governance pressure, not runtime canon |
| Upstream install payload | baseline package truth for this install cycle | first writer only | useful for diff/probe work, not final local truth |
| `tooling/portable-gsd/overlay/` | tracked repo-local intervention canon | authoritative for covered files until later mutation/drift intervenes | primary intervention surface, but not exhaustive |
| `scripts/setup-portable-gsd.sh` | install helper | load-bearing composition and mutation seam | primary intervention surface |
| live `.codex/config.toml` + `.codex/agents/*.toml` | runtime registry and worker contracts | effective spawn/runtime authority | primary intervention surface |
| live `.codex/get-shit-done/bin/lib/*` + workflows/references/templates | shipped/overlayed workflow and helper chain | effective routing/state semantics | primary intervention surface |
| `.codex/gsd-file-manifest.json` | materialization inventory record | version evidence, but not fully trustworthy semantic parity proof after local carry | verification aid with explicit limits |
| `.planning/config.json` | planning config | live runtime input | intervention surface when changing behavior/routing |
| `.planning/readiness/...` and this audit workspace | review/control/package truth | not runtime canon | use for diagnosis, proposals, and inheritance only |

- [e:c+i] The repo already distinguishes runtime canon from review/control surfaces: root instructions anchor runtime authority in repo-local `.codex/*`, while readiness packages are explicitly review/control surfaces. Sources: [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:39), [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:47), [checkpoint-5-gsd-local-topology-schema.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-local-topology-schema.md:5), [checkpoint-5-gsd-local-topology-schema.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-gsd-local-topology-schema.md:20).

## Backup And Manifest Limits

- [e:c+i] `.codex/gsd-local-patches/backup-meta.json` records only the backed-up replaced subset from the pre-overlay runtime, not the full overlay inventory or the full live intervention set. Sources: [.codex/gsd-local-patches/backup-meta.json](/home/rookslog/workspace/projects/prix-guesser/.codex/gsd-local-patches/backup-meta.json:2), [.codex/gsd-local-patches/backup-meta.json](/home/rookslog/workspace/projects/prix-guesser/.codex/gsd-local-patches/backup-meta.json:5), [.codex/gsd-local-patches/backup-meta.json](/home/rookslog/workspace/projects/prix-guesser/.codex/gsd-local-patches/backup-meta.json:17).
- [e:c+i] The manifest records the active version as `1.38.3` and a file hash inventory, but the earlier update lane already established that manifest hashes had gone stale relative to the actual post-overlay state even when live surfaces were semantically aligned with a fresh reinstall at the then-current `1.38.1` probe boundary. Sources: [.codex/gsd-file-manifest.json](/home/rookslog/workspace/projects/prix-guesser/.codex/gsd-file-manifest.json:2), [.codex/gsd-file-manifest.json](/home/rookslog/workspace/projects/prix-guesser/.codex/gsd-file-manifest.json:3), [HARNESS-INTERVENTION-UPDATE-LANE.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/harness-interventions/HARNESS-INTERVENTION-UPDATE-LANE.md:31), [HARNESS-INTERVENTION-UPDATE-LANE.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/harness-interventions/HARNESS-INTERVENTION-UPDATE-LANE.md:32).
- [d:r:i] Practical consequence: backup metadata and manifest state are both useful, but neither should be treated as a sovereign proof of current effective runtime truth without cross-checking the actual live files.

## First-Rank Intervention Surfaces

### 1. Installer Composition And Mutation

- [d:r:i] Any intervention that changes how repo-local runtime truth is materialized should start with `scripts/setup-portable-gsd.sh`, because that is the seam where upstream base, overlay carry, compact prompt selection, and post-copy mutations are composed.

### 2. Agent Runtime Authority

- [d:r:i] Any intervention that aims to change actual spawned-worker behavior should privilege `.codex/agents/*.toml` and the registry entries in `.codex/config.toml` over nicer wrapper prose, because those surfaces are what the runtime actually points at during spawn.

### 3. Live Workflow / Helper Semantics

- [d:r:i] Any intervention that aims to change routing, completion semantics, transition semantics, or helper-chain behavior should privilege live `.codex/get-shit-done/bin/lib/*`, workflows, references, and templates rather than assuming skills wrappers are the main seam.

### 4. Manifest / Drift Visibility

- [d:r:i] Any intervention that aims to make the harness easier to trust over time should address manifest/install coherence and live-vs-overlay drift visibility explicitly, because current runtime truth can outrun both overlay canon and recorded manifest state.

## Consequences For The Remaining Companion Artifacts

- [d:r:i] `../indexes/GOAL-TO-SURFACE-INTERVENTION-INDEX.md` should route desired changes through the materialization chain above rather than by doc family alone.
- [d:r:i] `../indexes/SURFACE-STATUS-AND-DELTA.md` should distinguish at least four states:
  - frozen PR-doc governance/reference snapshot
  - current upstream/base runtime line
  - tracked overlay canon
  - live repo-local effective runtime
- [d:r:i] The bounded proposal artifacts should start from the first-rank intervention surfaces named here rather than reopening generic “docs vs runtime” comparison as if the authority chain were still unclear.

## Bottom Line

- [g:r:i] The strongest current reading is: runtime truth in this repo is a composed, driftable chain. The best intervention planning will come from acting on that chain explicitly, not from treating any single layer as the whole harness.
