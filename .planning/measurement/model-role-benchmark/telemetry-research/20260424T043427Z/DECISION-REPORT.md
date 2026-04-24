# Decision Report

Status: synthesis complete, implementation not started.
Evidence boundary: provider/runtime claims are based on lane artifacts, independent design review, and architecture resolution. They are not live re-verifications unless the cited lane explicitly performed read-only local inspection or official-doc retrieval.

## Recommended Architecture

Adopt a harness-agnostic telemetry substrate with:

- JSONL/raw artifacts as durable evidence.
- SQLite as a rebuildable query cache.
- Entity/edge/observation relational core.
- Static YAML plugin manifests validated into canonical JSON registries.
- Provider/runtime/harness/domain details emitted as namespaced observations and payloads.
- Mandatory semantic missingness, reliability, content contract, cost evidence mode, and comparability fields.
- Multidimensional rubric observations as canonical quality storage.

This architecture passes with conditions because the load-bearing choices were separately reviewed and resolved in:

- `audits/20260424T045822Z-independent-design-review/DESIGN-REVIEW.md`
- `audits/20260424T045822Z-independent-design-review/ARCHITECTURE-RESOLUTION.md`

## Accepted Invariants

| Invariant | Why |
| --- | --- |
| Provider-neutral core | Prevents Codex, Claude, OpenAI, Anthropic, OTel, or GSD-specific fields from foreclosing future adapters. |
| Raw evidence separate from query cache | Preserves auditability, rebuildability, and privacy boundaries. |
| Registry/store/query/report parity | Avoids Reflect's registry drift failure mode. |
| Semantic missingness | Prevents missing-as-zero and makes deferred/redacted/unavailable states visible. |
| Cost evidence modes | Avoids conflating API-equivalent cost, provider-reported cost, subscription quota, and manual estimates. |
| Runtime items distinct from model calls | Prevents false one-to-one mapping between CLI/runtime records and provider inference calls. |
| Rubric observations over `score.overall` | Keeps benchmark quality multidimensional and auditable. |

## Resolved Load-Bearing Decisions

| Decision | Resolution |
| --- | --- |
| `runtime_response_items` | Core generic runtime-item concept, distinct from `model_calls`, with correlation status and namespaced payloads. |
| `telemetry_events` | Optional replay/debug/import support; not required first-slice infrastructure. |
| Canonical enums | Use `ARCHITECTURE-RESOLUTION.md` vocabularies for status, evidence, reliability, content, cost, and comparability. |
| Manifest/registry | Static YAML source, canonical JSON hash, SQLite registry cache, strict parity at manifest/rebuild/query/report. |
| Provider-neutrality gate | Codex-first allowed, but neutrality claim requires manual, Claude-shaped, and provider-denominator fixtures. |
| `score.overall` | Legacy/view-only as `legacy.score.overall`; canonical quality is `rubric_observations`. |

## What To Inherit From Reflect

Adopt or adapt:

- source adapter -> extractor registry -> query/report layering
- registry/store/query parity as a hard invariant
- semantic availability/missingness statuses
- privacy/content contracts
- provenance split between about-work, detected-by, and written-by style claims
- uncertainty-preserving reports

Reject or defer:

- Reflect loop taxonomy as core ontology
- GSD source families as core source kinds
- signal lifecycle automation as core benchmark behavior
- thinking/facet/session summaries as quality truth
- `score.overall` as benchmark anchor

## What To Change From Current Benchmark Ingest

Current benchmark ingest can remain v0 compatibility, but the next design must change:

- Move extensibility out of ad hoc run-record fields into declared observations.
- Keep `score.overall` importable only as `legacy.score.overall`.
- Add multidimensional rubric observations with evaluator and rubric-version provenance.
- Add cost evidence mode and token category preservation.
- Add registry manifests and rebuild/query/report hash parity.
- Add provider-neutral fixture gate before claiming neutrality.

## What Not To Build Yet

- Live OTel capture adapters.
- Live OpenAI/Anthropic API capture.
- Billing/quota truth integration.
- Raw API body capture.
- Full generic telemetry event store.
- GSD phase/milestone domain plugin.
- Broad dashboard/reporting layer.

These remain deferred until fixtures, consent boundaries, or implementation needs justify them.

## Research Confidence Summary

| Area | Confidence | Basis |
| --- | --- | --- |
| Reflect inheritance lessons | high | Lane 01 and memory-backed Reflect precedent, treated as repo precedent. |
| Codex SQLite/JSONL structure | high for observed structure, medium for stability | Lane 02 read-only local structural inspection. |
| Codex OTel emitted payload | low | Docs/config only; no capture. |
| Claude local structures | medium | Lane 03 structural inspection; schema unofficial and drift-prone. |
| Claude OTel/hooks/plugins/skills | medium | Official docs; no local capture. |
| OpenAI/Anthropic API and Agents surfaces | medium-high for docs, low for live values | Lane 04 official-doc research; no live calls. |
| Ontology/storage direction | medium-high | Lane 05 plus independent high-reasoning review. |
| Plugin protocol direction | medium-high | Lane 06 plus independent high-reasoning review. |

## Decision On Next Step

Proceed to implementation planning, not another broad research pass.

The first implementation plan must be bounded to schema/registry/fixture foundations and must not implement live provider capture. Provider-specific live research remains deferred until fixture-backed adapters prove the base contract.

## Conditions Carried Into Implementation Planning

- Use `ARCHITECTURE-RESOLUTION.md` as the authoritative load-bearing decision source.
- Build only enough schema to prove registry/rebuild/query parity and observation/rubric storage.
- Include provider-neutrality fixtures in the first slice.
- Keep raw content out of default fixtures and observations.
- Treat all live OTel/API/billing questions as deferred.
