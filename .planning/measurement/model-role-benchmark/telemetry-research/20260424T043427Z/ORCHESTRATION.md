# Telemetry Exposure Research Orchestration

Run timestamp: `20260424T043427Z`
Research folder: `.planning/measurement/model-role-benchmark/telemetry-research/20260424T043427Z/`
Baseline command: `git status --short`
Baseline result: clean worktree before this folder was created.

## Scope

This is a research-only pass for redesigning model benchmark telemetry into a harness-agnostic substrate with provider adapters and domain plugins. It does not implement the telemetry platform, mutate provider configuration, run paid/provider calls, or change home-level telemetry settings.

## Evidence Taxonomy

| Label | Meaning |
| --- | --- |
| `verified-doc` | Confirmed in current official docs with URL and retrieval date. |
| `local-observed` | Confirmed by read-only local inspection with command/path. |
| `repo-precedent` | Found in prior Reflect artifacts or source; not automatically accepted. |
| `inferred` | Reasoned from evidence, not directly observed. |
| `unverified` | Plausible but not yet confirmed. |
| `deferred` | Requires live credentials, config mutation, paid/quota-consuming run, or external setup. |
| `rejected` | Considered and rejected with rationale. |

## Coordination Rules

- Every material claim needs evidence class, source path or URL, command or citation, confidence, and uncertainty.
- Provider capability claims should use official docs and read-only local inspection. Community sources are not primary evidence.
- Local samples may describe schema and field names but must not copy private prompts, assistant text, tool arguments, tool outputs, or raw transcript content.
- Reflect telemetry work is `repo-precedent` until verified or adapted. No prior Reflect decision may be treated as automatically authoritative.
- Core ontology may not contain provider-only field names. Provider-specific details belong in adapter payloads, observations, or namespaced metrics.
- Missing values are semantic states, not zeroes.
- Claude thinking summaries, facets, and session meta are substitute or derived signals, not raw reasoning tokens or quality truth.
- The model benchmark target stores multidimensional rubric observations. It must not depend on `score.overall`.

## Lane Assignments

| Lane | Write target | Focus |
| --- | --- | --- |
| 01 | `01-REFLECT-INHERITANCE-REVIEW.md` | Critical inheritance from Reflect Phase 57, 57.5, 57.6, 57.7, 60.1, and measurement source. |
| 02 | `02-CODEX-EXPOSURE.md` | Codex SQLite, rollout JSONL, OTel, config, provider, auth, rate, model/reasoning, and local capture feasibility. |
| 03 | `03-CLAUDE-EXPOSURE.md` | Claude local session-meta/JSONL, OTel, monitoring, hooks, plugins, skills, raw API body refs, compaction, and privacy controls. |
| 04 | `04-API-AGENTS-TRACE-SURFACES.md` | OpenAI Agents traces/evals, OpenAI API usage fields, Anthropic API differences, and OTel GenAI conventions. |
| 05 | `05-ONTOLOGY-STORAGE-OPTIONS.md` | Ontology/storage options, minimum SQLite schema, IDs, edges, observations, rebuild behavior. |
| 06 | `06-PLUGIN-PROTOCOL-METRICS.md` | Source adapters, extractors, view/report plugins, privacy contracts, metrics, fixtures, rubric observations. |

## Cross-Review Map

| Reviewer | Review responsibility |
| --- | --- |
| Lane 02 | Review Lane 03 for symmetry assumptions. |
| Lane 03 | Review Lane 02 for provider-specific overfitting. |
| Lane 04 | Review Lanes 02 and 03 for API/trace compatibility. |
| Lane 05 | Review all lanes for ontology implications. |
| Lane 06 | Review all lanes for plugin extensibility gaps. |
| Lane 01 | Review final synthesis for naive inheritance from Reflect. |

## No-Mutation Policy

Allowed:
- read-only local file and SQLite schema inspection
- official documentation retrieval
- structural field sampling without content extraction
- repo-local Markdown artifact creation in this timestamped folder

Forbidden:
- live provider calls
- paid or quota-consuming model/API runs
- persistent provider config edits
- enabling telemetry exporters in user config
- copying private transcript content into artifacts
- implementation changes outside this research folder

## Spawned Agents And Disposition

| Agent | Lane | Disposition | Notes |
| --- | --- | --- | --- |
| `019dbdc5-9ea2-7193-9454-4a1d3cfd74a4` (`Kant`) | 01 | accept | Self-audited Reflect inheritance artifact accepted as `repo_precedent` input; final synthesis still treats Reflect as precedent, not authority. |
| `019dbdc5-9f23-7751-8f92-5b48b918ede4` (`James`) | 02 | accept | Self-audited Codex exposure artifact accepted; OTel payload schema, billing truth, and schema stability remain deferred. |
| `019dbdc5-9f92-75a2-81f7-f36beea876f7` (`Turing`) | 03 | accept | Self-audited Claude exposure artifact accepted; local schema stability and live OTel capture remain deferred. |
| `019dbdc5-a053-7691-9da7-b75b189abb12` (`Kuhn`) | 04 | accept | Self-audited API/Agents trace artifact accepted; live API headers and billing truth remain deferred. |
| `019dbdc9-f337-7391-9b22-e4efe0722ca3` (`Helmholtz`) | 05 | accept-with-conditions | Ontology/storage artifact accepted after dependency repair; load-bearing decisions resolved in `ARCHITECTURE-RESOLUTION.md`. |
| `019dbdc9-f3ab-7372-a642-3e3e817c7848` (`Zeno`) | 06 | accept-with-conditions | Plugin/protocol artifact accepted after dependency repair; manifest, registry, enum, provider-neutrality, and `score.overall` decisions resolved in `ARCHITECTURE-RESOLUTION.md`. |
| `019dbddb-16c0-7ff3-b24d-e40d665f6de7` (`Faraday`) | independent design review | accept | Produced `audits/20260424T045822Z-independent-design-review/DESIGN-REVIEW.md`; verdict `pass-with-conditions`. |
| `019dbe11-54ea-7a73-8453-824d80f60954` (`Nietzsche`) | load-bearing resolution recommendation | accept | Produced `LOAD-BEARING-RESOLUTION-RECOMMENDATION.md`; coordinator accepted core recommendations in `ARCHITECTURE-RESOLUTION.md`. |

## Cross-Review Disposition

The original lane cross-review map was not completed as separate `cross-reviews/*.md` files. It was superseded by an independent high-reasoning design review plus a separate high-reasoning load-bearing architecture recommendation. The remaining synthesis conditions from that review are carried into `ARCHITECTURE-RESOLUTION.md`, `DECISION-REPORT.md`, and `NEXT-IMPLEMENTATION-PLAN.md`.

## Coordinator Deliverables

- `EXPOSURE-MATRIX.md`
- `OPEN-QUESTIONS-REGISTER.md`
- `PITFALLS-AND-MITIGATIONS.md`
- `DECISION-REPORT.md`
- `NEXT-IMPLEMENTATION-PLAN.md`

## Verification Plan

- `git status --short` before and after
- `git diff --check -- .planning/measurement/model-role-benchmark`
- `python3 -m unittest tooling.codex.tests.test_model_benchmark`
- Manual checks:
  - no provider configs changed
  - no home-level telemetry settings changed
  - no live/paid/quota-consuming runs performed
  - no raw private transcript content copied into research artifacts
  - material provider capability claims carry evidence class and source
  - open questions are captured in `OPEN-QUESTIONS-REGISTER.md`
  - `DECISION-REPORT.md` separates implementation-ready decisions from unresolved research
