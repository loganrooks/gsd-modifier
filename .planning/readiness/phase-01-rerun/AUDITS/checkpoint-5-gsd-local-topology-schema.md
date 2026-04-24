# Checkpoint 5: Repo-Local GSD Topology Schema

This is a structure map of the repo-local regular GSD runtime as it exists in this workspace today. It is not a product doc and it is not a generic GSD overview.

Claim marker legend:
- `[e:c:i]` evidenced, cited, internal repo file
- `[e:r:i]` evidenced with a short reasoned step from cited internal files
- `[g:c:i]` governing repo/package instruction, cited, internal repo file

## Orientation

- `[g:c:i]` This repository is explicitly on regular repo-local GSD for Codex, not Reflect; the live runtime anchor is `.codex/get-shit-done`, and the intended local install path is `./scripts/setup-portable-gsd.sh`. ([AGENTS.md:5](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:5), [AGENTS.md:7](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:7), [AGENTS.md:8](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:8))
- `[e:c:i]` The base layer is upstream/npm-installed: the installer starts by running `npx get-shit-done-cc --codex --local`. ([setup-portable-gsd.sh:11](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh:11))
- `[e:c:i]` The tracked canon for repo-local intervention is `tooling/portable-gsd/overlay/`; the installer copies every overlay file into `.codex/`, substituting `__PROJECT_ROOT__` on the way in. ([setup-portable-gsd.sh:6](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh:6), [setup-portable-gsd.sh:15](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh:15), [setup-portable-gsd.sh:27](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh:27), [overlay-config.toml:1](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/config.toml:1), [overlay-plan-phase.md:1](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/plan-phase.md:1), [overlay-agent-contracts.md:1](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/references/agent-contracts.md:1), [overlay-template-config.json:1](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/templates/config.json:1))
- `[e:c:i]` The live materialized runtime is the `.codex/*` tree: `.codex/config.toml` is the runtime registry, `.codex/get-shit-done/` holds workflows/references/templates/helpers, `.codex/skills/` holds Codex wrappers, `.codex/agents/` holds role contracts, and `.codex/gsd-file-manifest.json` records the materialized file set and version. ([.codex/config.toml:1](/home/rookslog/workspace/projects/prix-guesser/.codex/config.toml:1), [.codex/config.toml:20](/home/rookslog/workspace/projects/prix-guesser/.codex/config.toml:20), [.codex/gsd-file-manifest.json:2](/home/rookslog/workspace/projects/prix-guesser/.codex/gsd-file-manifest.json:2), [.codex/gsd-file-manifest.json:4](/home/rookslog/workspace/projects/prix-guesser/.codex/gsd-file-manifest.json:4))
- `[e:c:i]` The installer also performs a post-materialization mutation pass: it rewrites top-level `model_reasoning_effort` and selected agent TOMLs after the overlay copy completes. ([setup-portable-gsd.sh:33](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh:33), [setup-portable-gsd.sh:42](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh:42), [setup-portable-gsd.sh:73](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh:73))
- `[g:c:i]` The readiness package is a review/control surface, not runtime canon: this subtree exists to track checkpoint readiness work, and `AUDITS/` stores readiness-local audit/scoping artifacts rather than runtime authority. ([phase-01-rerun/AGENTS.md:10](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AGENTS.md:10), [phase-01-rerun/AGENTS.md:45](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AGENTS.md:45), [AUDITS/README.md:3](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/README.md:3))

## Architecture / Topology

```mermaid
flowchart LR
    A["Upstream/npm base<br/>`npx get-shit-done-cc --codex --local`"]
    B["Tracked overlay canon<br/>`tooling/portable-gsd/overlay/`<br/>config / workflows / refs / templates / agents / skills"]
    I["`scripts/setup-portable-gsd.sh`<br/>install -> copy overlay -> rewrite reasoning defaults"]

    A --> I
    B --> I

    subgraph L["Live materialized runtime (`.codex/`)"]
      C1["`config.toml`<br/>runtime registry + model settings"]
      C2["`get-shit-done/`<br/>workflows / references / templates / bin/lib helpers"]
      C3["`skills/`<br/>Codex skill wrappers"]
      C4["`agents/`<br/>role contracts"]
      C5["`gsd-file-manifest.json`<br/>materialized file set"]
      C6["`gsd-local-patches/backup-meta.json`<br/>backed-up replaced subset"]
    end

    I --> C1
    I --> C2
    I --> C3
    I --> C4
    I --> C5
    I --> C6

    subgraph P["Planning/runtime outputs (`.planning/`)"]
      O1["`config.json`<br/>workflow flags + model overrides"]
      O2["phase artifacts<br/>`CONTEXT -> RESEARCH -> PLAN -> SUMMARY -> VERIFICATION / UAT / REVIEWS`"]
      O3["project state<br/>`PROJECT / ROADMAP / REQUIREMENTS / STATE`"]
    end

    C1 --> C2
    C1 --> C3
    C1 --> C4
    C2 --> O1
    C2 --> O2
    C2 --> O3
    C3 --> C2
    C4 --> O2

    subgraph R["Readiness package (`.planning/readiness/phase-01-rerun/`)"]
      R1["`AGENTS.md`<br/>package/control rules"]
      R2["`AUDITS/` `REVIEWS/` `GATES/`<br/>checkpoint review surfaces"]
    end

    R1 -. audits / constrains readiness work .-> R2
    R2 -. reviews runtime, does not govern runtime .-> C2
    R2 -. packages findings about outputs .-> O2
```

Topology reading:
- `[e:c:i]` Skills are thin Codex adapters that point into repo-local workflow files; the workflow files, not the wrapper summaries, are the real execution surface. ([gsd-discuss-phase/SKILL.md:69](/home/rookslog/workspace/projects/prix-guesser/.codex/skills/gsd-discuss-phase/SKILL.md:69), [gsd-discuss-phase/SKILL.md:96](/home/rookslog/workspace/projects/prix-guesser/.codex/skills/gsd-discuss-phase/SKILL.md:96))
- `[e:c:i]` `gsd-tools.cjs` plus its `lib/*` helpers are the runtime helper chain that turns file-heavy planning state into structured init/config/roadmap/phase answers for workflows. ([gsd-tools.cjs:6](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/bin/gsd-tools.cjs:6), [gsd-tools.cjs:137](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/bin/gsd-tools.cjs:137), [init.cjs:32](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/bin/lib/init.cjs:32), [config.cjs:14](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/bin/lib/config.cjs:14), [roadmap.cjs:116](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/bin/lib/roadmap.cjs:116), [phase.cjs:37](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/bin/lib/phase.cjs:37))
- `[e:c:i]` `.planning/config.json` is not part of `.codex`, but it is a live runtime input: workflow flags such as `auto_advance`, `discuss_mode`, `code_review`, and model overrides are read from there by workflows and init helpers. ([.planning/config.json:15](/home/rookslog/workspace/projects/prix-guesser/.planning/config.json:15), [.planning/config.json:20](/home/rookslog/workspace/projects/prix-guesser/.planning/config.json:20), [.planning/config.json:27](/home/rookslog/workspace/projects/prix-guesser/.planning/config.json:27), [.planning/config.json:38](/home/rookslog/workspace/projects/prix-guesser/.planning/config.json:38))

## Main Family Flow / Call Graph

```mermaid
flowchart TD
    U["User or orchestrator"]

    D["`$gsd-discuss-phase`<br/>skill -> `discuss-phase.md`"]
    P["`$gsd-plan-phase`<br/>skill -> `plan-phase.md`"]
    E["`$gsd-execute-phase`<br/>skill -> `execute-phase.md`"]
    V["`$gsd-verify-work`<br/>skill -> `verify-work.md`"]
    R["`$gsd-review`<br/>skill -> `review.md`"]
    G["`$gsd-progress`<br/>skill -> `progress.md`"]
    T["`transition.md`<br/>internal only"]
    S["`$gsd-ship`<br/>skill -> `ship.md`"]
    A["`$gsd-autonomous`<br/>skill -> `autonomous.md`"]

    PR["`gsd-phase-researcher`<br/>writes `RESEARCH.md`"]
    PL["`gsd-planner`<br/>writes `PLAN.md`"]
    PC["`gsd-plan-checker`<br/>returns pass/issues"]
    EX["`gsd-executor`<br/>writes `SUMMARY.md`"]
    VF["`gsd-verifier`<br/>writes `VERIFICATION.md`"]
    RV["writes `REVIEWS.md`"]
    UAT["writes `UAT.md` / `HUMAN-UAT.md`"]

    U --> D
    U --> P
    U --> E
    U --> V
    U --> R
    U --> G
    U --> S
    U --> A

    D -->|"auto / chain / auto_advance"| P
    P --> PR --> PL --> PC
    PC -->|"verification passed"| E
    PC -->|"issues found"| P

    E --> EX --> VF
    VF -->|"passed"| T
    VF -->|"gaps_found"| P
    VF -->|"human_needed"| UAT

    V --> UAT
    UAT -->|"issues found"| P
    UAT -->|"clean manual pass"| T

    R --> RV -->|"consume via `--reviews`"| P
    G -. routes to .-> D
    G -. routes to .-> P
    G -. routes to .-> E
    G -. routes to .-> V

    T -->|"next phase routing"| D
    T -->|"context already exists"| P

    VF -->|"verified phase ready to ship"| S
    A --> D
    A --> P
    A --> E
```

Flow reading:
- `[e:c:i]` Discuss owns `CONTEXT.md`, and in auto/chain paths it launches plan-phase using a flat skill call rather than deeper nested task chains. ([discuss-phase.md:228](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/discuss-phase.md:228), [discuss-phase.md:230](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/discuss-phase.md:230), [discuss-phase.md:1269](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/discuss-phase.md:1269))
- `[e:c:i]` Plan-phase orchestrates the research -> planner -> checker loop, and the live runtime has an explicit reviews-mode contract layered into the planner prompt. ([plan-phase.md:2](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/plan-phase.md:2), [plan-phase.md:13](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/plan-phase.md:13), [plan-phase.md:682](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/plan-phase.md:682), [plan-phase.md:705](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/plan-phase.md:705), [plan-phase.md:723](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/plan-phase.md:723))
- `[e:c:i]` Execute-phase is debt-aware: it delegates execution, then uses verifier output to branch into clean completion, human verification capture, or gap-closure replanning; `transition.md` is internal only. ([execute-phase.md:2](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/execute-phase.md:2), [execute-phase.md:1218](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/execute-phase.md:1218), [execute-phase.md:1257](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/execute-phase.md:1257), [execute-phase.md:1476](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/execute-phase.md:1476), [transition.md:3](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/transition.md:3))
- `[e:c:i]` Review is not closure by itself; it emits `REVIEWS.md` as a consumer contract that the live planner is expected to ingest via `--reviews`. ([review.md:2](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/review.md:2), [review.md:5](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/review.md:5), [review.md:200](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/review.md:200), [review.md:246](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/review.md:246), [review.md:300](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/review.md:300))

## Contract Matrix

| Surface | Role | Reads / expects | Emits / returns | Downstream consumers | Intervention status |
|---|---|---|---|---|---|
| `scripts/setup-portable-gsd.sh` | Materializes repo-local GSD into `.codex/` and applies post-install mutations. ([setup-portable-gsd.sh:11](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh:11), [setup-portable-gsd.sh:15](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh:15), [setup-portable-gsd.sh:33](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh:33)) | Repo root, tracked overlay tree, writable `.codex/`. | Materialized live runtime plus reasoning rewrites and status output. ([setup-portable-gsd.sh:51](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh:51), [setup-portable-gsd.sh:81](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh:81), [setup-portable-gsd.sh:85](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh:85)) | Every `.codex/*` runtime surface. | `tracked overlay` |
| `tooling/portable-gsd/overlay/` | Repo-tracked intervention canon layered over upstream base. Representative files: config, workflow, reference, template. ([overlay-config.toml:1](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/config.toml:1), [overlay-plan-phase.md:1](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/plan-phase.md:1), [overlay-agent-contracts.md:1](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/references/agent-contracts.md:1), [overlay-template-config.json:1](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/templates/config.json:1)) | Installer copy pass with `__PROJECT_ROOT__` substitution. | Overlay-backed live files under `.codex/`. | `.codex/config.toml`, `.codex/get-shit-done/*`, overlay-added skills/agents. | `tracked overlay` |
| `.codex/config.toml` + `.planning/config.json` | Runtime registry plus per-project workflow settings. ([.codex/config.toml:20](/home/rookslog/workspace/projects/prix-guesser/.codex/config.toml:20), [.planning/config.json:15](/home/rookslog/workspace/projects/prix-guesser/.planning/config.json:15), [.planning/config.json:38](/home/rookslog/workspace/projects/prix-guesser/.planning/config.json:38)) | Registered agent config files, workflow keys, model overrides, flags such as `auto_advance` and `discuss_mode`. ([config.cjs:14](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/bin/lib/config.cjs:14), [config.cjs:136](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/bin/lib/config.cjs:136)) | Runtime configuration answers consumed by workflows and init commands. | Skill wrappers, workflows, init helpers, agents. | `tracked overlay` for shape; current live file also has `live-only local change` drift at top-level reasoning setting |
| `.codex/skills/*.md` wrappers | Codex entry adapters from `$gsd-*` invocations into repo-local workflow files. ([gsd-discuss-phase/SKILL.md:8](/home/rookslog/workspace/projects/prix-guesser/.codex/skills/gsd-discuss-phase/SKILL.md:8), [gsd-discuss-phase/SKILL.md:69](/home/rookslog/workspace/projects/prix-guesser/.codex/skills/gsd-discuss-phase/SKILL.md:69), [gsd-rigorous-research/SKILL.md:22](/home/rookslog/workspace/projects/prix-guesser/.codex/skills/gsd-rigorous-research/SKILL.md:22)) | User args; workflow files in `<execution_context>`. | Codex-native skill behavior; user interaction/task mapping; workflow dispatch. | Workflow markdown files. | Mostly `upstream/base`; some repo-local additions/overrides are `tracked overlay` |
| `.codex/get-shit-done/bin/gsd-tools.cjs` + `bin/lib/{init,config,roadmap,phase}.cjs` | Structured helper/inspection layer for workflows. ([gsd-tools.cjs:6](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/bin/gsd-tools.cjs:6), [gsd-tools.cjs:137](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/bin/gsd-tools.cjs:137), [init.cjs:32](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/bin/lib/init.cjs:32), [roadmap.cjs:116](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/bin/lib/roadmap.cjs:116), [phase.cjs:37](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/bin/lib/phase.cjs:37)) | `.planning/*`, config, filesystem state, phase artifacts. | JSON/raw answers for init, config, roadmap analysis, phase completion/debt inspection. | All main workflows. | Mostly `upstream/base`; `config.cjs` is `tracked overlay` via backup metadata |
| `discuss-phase.md` | Builds `CONTEXT.md`, reads mode flags, may auto-chain into planning. ([discuss-phase.md:194](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/discuss-phase.md:194), [discuss-phase.md:216](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/discuss-phase.md:216), [discuss-phase.md:1237](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/discuss-phase.md:1237)) | Phase state, config, prior context, roadmap/state. | `*-CONTEXT.md`; optional flat `gsd-plan-phase` launch. | `gsd-phase-researcher`, `gsd-planner`, `gsd-progress`, autonomous flow. | `tracked overlay` |
| `plan-phase.md` | Research-plan-check orchestration; review-aware replanning in live runtime. ([plan-phase.md:2](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/plan-phase.md:2), [plan-phase.md:13](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/plan-phase.md:13), [plan-phase.md:673](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/plan-phase.md:673), [plan-phase.md:716](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/plan-phase.md:716)) | CONTEXT, roadmap, requirements, research, review feedback, UI-SPEC, config. | `*-PLAN.md`; may trigger execute-phase in auto-chain. | `gsd-executor`, `gsd-progress`, `verify-work` gap closure, `review` follow-through. | Overlay-backed, with important `live-only local change` additions on the live file |
| `execute-phase.md` | Wave orchestration across plans, then verifier-driven routing. ([execute-phase.md:2](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/execute-phase.md:2), [execute-phase.md:70](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/execute-phase.md:70), [execute-phase.md:1218](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/execute-phase.md:1218), [execute-phase.md:1351](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/execute-phase.md:1351)) | Init payload, plans, config, prior phase artifacts. | `*-SUMMARY.md`, `*-VERIFICATION.md`, `*-HUMAN-UAT.md`, roadmap/state updates, optional internal transition. | `progress`, `verify-work`, `ship`, next-phase routing. | `upstream/base` in this map |
| `verify-work.md` | Conversational/manual verification lane and gap-closure planner/checker loop. ([verify-work.md:2](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/verify-work.md:2), [verify-work.md:171](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/verify-work.md:171), [verify-work.md:488](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/verify-work.md:488), [verify-work.md:660](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/verify-work.md:660)) | Phase summaries, current UAT state, verification outputs. | `*-UAT.md`; optionally gap plans verified by checker. | `execute-phase --gaps-only`, `transition`, `progress`. | `upstream/base` |
| `review.md` + `planner-reviews.md` | Adversarial review lane plus planner-side review consumption contract. ([review.md:2](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/review.md:2), [review.md:200](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/review.md:200), [planner-reviews.md:7](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/references/planner-reviews.md:7), [planner-reviews.md:50](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/references/planner-reviews.md:50)) | PLANs, CONTEXT, RESEARCH, REQUIREMENTS, external CLI availability, `REVIEWS.md`. | `*-REVIEWS.md`; review-consumer buckets; planner output sections for addressed/deferred/rejected feedback. | `gsd-plan-phase --reviews`, readiness review follow-through. | `tracked overlay` for review surfaces; live planner consumption is partly `live-only local change` |
| `progress.md`, `transition.md`, `ship.md`, `autonomous.md` | Routing, internal phase transition, PR closure, and multi-phase autopilot. ([progress.md:15](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/progress.md:15), [progress.md:199](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/progress.md:199), [transition.md:3](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/transition.md:3), [ship.md:2](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/ship.md:2), [autonomous.md:3](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/autonomous.md:3)) | ROADMAP/STATE/project status, phase artifacts, verification state, branch/PR tooling. | Next-action routing, internal transition, PR creation/update, repeated discuss-plan-execute loops. | User/operator, later phases, GitHub shipping path. | `upstream/base` |
| `.codex/agents/*.toml` core role contracts | Subagent behavior contracts for researcher, planner, checker, executor, verifier, plus many auxiliary lanes. ([.codex/config.toml:68](/home/rookslog/workspace/projects/prix-guesser/.codex/config.toml:68), [gsd-phase-researcher.toml:2](/home/rookslog/workspace/projects/prix-guesser/.codex/agents/gsd-phase-researcher.toml:2), [gsd-planner.toml:9](/home/rookslog/workspace/projects/prix-guesser/.codex/agents/gsd-planner.toml:9), [gsd-executor.toml:7](/home/rookslog/workspace/projects/prix-guesser/.codex/agents/gsd-executor.toml:7), [gsd-verifier.toml:7](/home/rookslog/workspace/projects/prix-guesser/.codex/agents/gsd-verifier.toml:7), [gsd-plan-checker.toml:7](/home/rookslog/workspace/projects/prix-guesser/.codex/agents/gsd-plan-checker.toml:7)) | `<files_to_read>` blocks, AGENTS surfaces, repo-local workflow/reference docs. | `RESEARCH.md`, `PLAN.md`, `SUMMARY.md`, `VERIFICATION.md`, verification/checkpoint markers, auxiliary outputs. | Main workflow family and auxiliary audit/review lanes. | Core five planning agents are `tracked overlay`; many auxiliary agents are `upstream/base` materialized live surfaces |
| `.planning/readiness/phase-01-rerun/` package | Checkpoint control, audit packaging, review policy surfaces. ([phase-01-rerun/AGENTS.md:10](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AGENTS.md:10), [phase-01-rerun/AGENTS.md:49](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AGENTS.md:49), [AUDITS/README.md:3](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/README.md:3)) | Runtime facts, checkpoint reviews, governance/routing docs. | Audit artifacts, reviews, gate-ready findings. | Humans and readiness follow-through work, not runtime execution. | `readiness intervention` |

## Intervention Map

| Surface | Why it matters | Class |
|---|---|---|
| `tooling/portable-gsd/overlay/config.toml` -> `.codex/config.toml` | Repo-owned runtime registry, model defaults, and agent registration are overlay-backed rather than purely upstream. ([overlay-config.toml:1](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/config.toml:1), [.codex/config.toml:20](/home/rookslog/workspace/projects/prix-guesser/.codex/config.toml:20)) | `tracked overlay-backed` |
| Overlay workflow/reference/template overrides listed in `.codex/gsd-local-patches/backup-meta.json` | These are the replaced upstream files the installer explicitly preserves metadata for; they are the most obvious overlay-owned behavioral surfaces. ([backup-meta.json:5](/home/rookslog/workspace/projects/prix-guesser/.codex/gsd-local-patches/backup-meta.json:5), [backup-meta.json:22](/home/rookslog/workspace/projects/prix-guesser/.codex/gsd-local-patches/backup-meta.json:22)) | `tracked overlay-backed` |
| Overlay-added repo-local skill `gsd-rigorous-research` | This repo-specific research lane is part of the materialized local skill surface and is meant for standalone rigorous analysis outside normal phase flow. ([gsd-rigorous-research/SKILL.md:2](/home/rookslog/workspace/projects/prix-guesser/.codex/skills/gsd-rigorous-research/SKILL.md:2), [gsd-rigorous-research/SKILL.md:13](/home/rookslog/workspace/projects/prix-guesser/.codex/skills/gsd-rigorous-research/SKILL.md:13)) | `tracked overlay-backed` |
| Live `.codex/config.toml` top-level reasoning setting | Current live runtime says `model_reasoning_effort = "xhigh"`, while both overlay canon and installer rewrite logic target `"high"`. This is real live drift, not just hypothetical. ([overlay-config.toml:2](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/config.toml:2), [setup-portable-gsd.sh:45](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh:45), [.codex/config.toml:2](/home/rookslog/workspace/projects/prix-guesser/.codex/config.toml:2)) | `live .codex-only` |
| Live `plan-phase.md` review-mode additions | The live planner workflow reads `planner-reviews.md` and requires explicit review-disposition output sections that are not present in the tracked overlay copy shown here. ([plan-phase.md:13](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/plan-phase.md:13), [plan-phase.md:683](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/plan-phase.md:683), [plan-phase.md:705](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/plan-phase.md:705), [plan-phase.md:723](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/plan-phase.md:723), [overlay-plan-phase.md:11](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/plan-phase.md:11), [overlay-plan-phase.md:681](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/plan-phase.md:681)) | `live .codex-only` |
| Live `agent-contracts.md` debt-aware completion semantics | The live reference now treats `PLAN COMPLETE` as insufficient for clean completion and defines `completion_mode` / debt-bearing handoffs; the overlay copy is weaker. ([agent-contracts.md:45](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/references/agent-contracts.md:45), [agent-contracts.md:71](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/references/agent-contracts.md:71), [agent-contracts.md:82](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/references/agent-contracts.md:82), [overlay-agent-contracts.md:45](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/references/agent-contracts.md:45), [overlay-agent-contracts.md:70](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/references/agent-contracts.md:70)) | `live .codex-only` |
| `.planning/readiness/phase-01-rerun/{AGENTS,AUDITS,REVIEWS,GATES}` | These surfaces package findings and gate decisions about runtime quality, but they are explicitly not runtime canon. ([phase-01-rerun/AGENTS.md:10](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AGENTS.md:10), [phase-01-rerun/AGENTS.md:45](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AGENTS.md:45), [AUDITS/README.md:3](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/README.md:3)) | `package-truth / review-only` |

## Failure-Relevant Seams

### Semantic / Runtime Contract Seams

- `[e:c:i]` Wrapper-vs-workflow seam: the skill wrappers are intentionally thin, and they explicitly say the workflow files are the real instructions. If wrapper summary text and workflow body ever diverge, runtime truth is in the workflow body. ([gsd-discuss-phase/SKILL.md:69](/home/rookslog/workspace/projects/prix-guesser/.codex/skills/gsd-discuss-phase/SKILL.md:69), [gsd-discuss-phase/SKILL.md:96](/home/rookslog/workspace/projects/prix-guesser/.codex/skills/gsd-discuss-phase/SKILL.md:96))
- `[e:c:i]` Completion-semantics seam: executor completion is not equivalent to clean phase closure. Live runtime depends on `completion_mode`, debt metadata, verification status, and `inspectPhaseCompletion()` rather than the presence of `## PLAN COMPLETE` or a SUMMARY alone. ([agent-contracts.md:45](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/references/agent-contracts.md:45), [agent-contracts.md:86](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/references/agent-contracts.md:86), [phase.cjs:77](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/bin/lib/phase.cjs:77), [phase.cjs:105](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/bin/lib/phase.cjs:105), [roadmap.cjs:182](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/bin/lib/roadmap.cjs:182))
- `[e:c:i]` Review-consumer seam: `review.md` produces a strong consumer contract, but clean follow-through depends on the live planner reading `planner-reviews.md` and emitting addressed/deferred/rejected review dispositions. That contract is stronger in the live runtime than in the tracked overlay copy. ([review.md:246](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/review.md:246), [planner-reviews.md:21](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/references/planner-reviews.md:21), [planner-reviews.md:50](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/references/planner-reviews.md:50), [plan-phase.md:705](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/plan-phase.md:705), [overlay-plan-phase.md:694](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/plan-phase.md:694))
- `[e:c:i]` Transition authority seam: `transition.md` is internal only, and execute/verify routes are responsible for invoking it inline without teaching the user a nonexistent `$gsd-transition` command. ([transition.md:3](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/transition.md:3), [transition.md:31](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/transition.md:31), [execute-phase.md:1470](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/execute-phase.md:1470), [execute-phase.md:1476](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/execute-phase.md:1476))

### Materialization / Reinstall Seams

- `[e:c:i]` Reinstall is a three-stage composition: upstream install, overlay copy, then post-copy mutation. Any of the three can move independently, so materialized runtime truth is not reducible to a single source file. ([setup-portable-gsd.sh:11](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh:11), [setup-portable-gsd.sh:15](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh:15), [setup-portable-gsd.sh:33](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh:33))
- `[e:r:i]` Backup metadata is a seam, not a full manifest of interventions: the installer copies all overlay files, but `.codex/gsd-local-patches/backup-meta.json` records only the backed-up replaced subset. Treating `backup-meta.json` as the full overlay inventory would miss additive repo-local surfaces. ([setup-portable-gsd.sh:15](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh:15), [backup-meta.json:5](/home/rookslog/workspace/projects/prix-guesser/.codex/gsd-local-patches/backup-meta.json:5), [backup-meta.json:22](/home/rookslog/workspace/projects/prix-guesser/.codex/gsd-local-patches/backup-meta.json:22))
- `[e:c:i]` Current live runtime already demonstrates drift after materialization: overlay canon and installer rewrite target top-level `model_reasoning_effort = "high"`, but the live file currently says `xhigh`. ([overlay-config.toml:2](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/config.toml:2), [setup-portable-gsd.sh:46](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh:46), [.codex/config.toml:2](/home/rookslog/workspace/projects/prix-guesser/.codex/config.toml:2))
- `[e:c:i]` Manifest and live file hashes are useful for “what was materialized,” but they do not replace semantic inspection of workflow/contract drift. ([.codex/gsd-file-manifest.json:2](/home/rookslog/workspace/projects/prix-guesser/.codex/gsd-file-manifest.json:2), [.codex/gsd-file-manifest.json:4](/home/rookslog/workspace/projects/prix-guesser/.codex/gsd-file-manifest.json:4))

### Authority / Package-Truth Seams

- `[g:c:i]` Runtime authority for this repo is live repo-local `.codex/*` plus `.planning/config.json`, not home-level Reflect paths and not generic upstream assumptions. ([AGENTS.md:5](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:5), [AGENTS.md:7](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:7), [AGENTS.md:9](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:9), [.planning/config.json:15](/home/rookslog/workspace/projects/prix-guesser/.planning/config.json:15))
- `[g:c:i]` The readiness package is explicitly package truth for checkpoint control, not canon for runtime or product behavior. Audit findings can steer follow-through, but they do not directly rewrite runtime semantics unless that follow-through lands in overlay/live runtime files. ([phase-01-rerun/AGENTS.md:10](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AGENTS.md:10), [phase-01-rerun/AGENTS.md:45](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AGENTS.md:45), [AUDITS/README.md:3](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/README.md:3))
- `[e:c:i]` The planning/runtime helper chain itself is live authority for routing and state classification. For example, `roadmap analyze` and `inspectPhaseCompletion()` decide whether a phase is `complete`, `complete_with_debt`, or merely `executed`, and `progress.md` routes based on those statuses. ([phase.cjs:11](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/bin/lib/phase.cjs:11), [roadmap.cjs:189](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/bin/lib/roadmap.cjs:189), [roadmap.cjs:237](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/bin/lib/roadmap.cjs:237), [progress.md:199](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/progress.md:199), [progress.md:211](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/progress.md:211))

## Bottom Line

- `[e:c:i]` Designed topology here is not “upstream package only.” It is: upstream base -> tracked overlay -> installer post-pass -> live materialized `.codex` runtime -> `.planning` artifacts/state. ([setup-portable-gsd.sh:11](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh:11), [setup-portable-gsd.sh:15](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh:15), [setup-portable-gsd.sh:33](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh:33))
- `[e:c:i]` The main workflow family is coherent only if the live repo-local contracts are read together: skill wrapper -> workflow -> helper CLI/init -> agent contract -> phase artifact -> routing helper. ([gsd-discuss-phase/SKILL.md:96](/home/rookslog/workspace/projects/prix-guesser/.codex/skills/gsd-discuss-phase/SKILL.md:96), [gsd-tools.cjs:137](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/bin/gsd-tools.cjs:137), [agent-contracts.md:47](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/references/agent-contracts.md:47))
- `[e:c:i]` For checkpoint-5 readiness work, the most failure-relevant fact is that important behavior now lives in live runtime drift surfaces, not only in the tracked overlay canon. The review-aware planner contract and debt-aware completion semantics are the clearest examples. ([plan-phase.md:13](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/plan-phase.md:13), [plan-phase.md:705](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/plan-phase.md:705), [agent-contracts.md:45](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/references/agent-contracts.md:45), [agent-contracts.md:82](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/references/agent-contracts.md:82))
