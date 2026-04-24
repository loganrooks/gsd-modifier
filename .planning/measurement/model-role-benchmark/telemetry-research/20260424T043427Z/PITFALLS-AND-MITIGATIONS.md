# Pitfalls And Mitigations

## Research Pitfalls

| Pitfall | Observed risk | Mitigation | Verification method |
| --- | --- | --- | --- |
| Treating Reflect as authority | Reflect telemetry work is rich but GSD-specific | Use Reflect as `repo_precedent`; inherit invariants, adapt seams, reject workflow ontology | `01-REFLECT-INHERITANCE-REVIEW.md`; synthesis keeps GSD phases as domain plugin |
| Designing around Codex only | Codex has strongest local evidence and could shape schema | Provider-neutral core; Codex fields in namespaces; mandatory non-Codex fixture gate | `ARCHITECTURE-RESOLUTION.md`; first-slice fixtures include Claude-shaped and provider-denominator cases |
| Flattening provider/auth/billing | API cost, subscription quota, rate limits, and auth are different axes | Separate token, cost evidence mode, quota, rate, auth, provider, billing observations | Manifest enum validation and cost-mode tests |
| Over-trusting local logs | Codex/Claude local schemas are internal and drift-prone | Treat as local structural evidence; adapters are versioned/tolerant and fixture-backed | Golden fixtures and malformed-line diagnostics |
| Mutating config for OTel | OTel capture may require setup and config overrides | Keep OTel deferred unless explicit local fixture capture is approved | No OTel adapter until fixture and capture metadata exist |
| Persisting sensitive content | Local logs can contain prompts, assistant text, tool args/results | Default content contracts are structural/metadata/redacted; raw modes require consent | Fixture review and manifest raw-content policy checks |
| Treating missing as zero | Missing reasoning/cache/cost can be misread as zero | Canonical missingness enum and report rendering | Validator rejects absent status for observations |
| Treating thinking summaries as quality | Claude facets/summaries are substitute signals | Store as substitute observations only; rubric observations are separate | Rubric tests reject summary-as-score paths |
| Reintroducing `score.overall` | Current tests still use scalar score | Legacy import only as `legacy.score.overall`; canonical rubric observations | Compatibility test plus no canonical aggregate metric validation |
| Sanitized reports hiding uncertainty | Summaries can erase evidence/missingness | Reports must include evidence class, reliability, status, and confidence | Report snapshot tests include gaps/deferred rows |

## Implementation Pitfalls

| Pitfall | Risk | Mitigation | Verification method |
| --- | --- | --- | --- |
| Overbuilding a generic telemetry platform | Too many tables/adapters before source facts are proved | First slice: manifest registry, rebuild cache, fixtures, Codex fixture adapters, rubric path | Scope checklist in `NEXT-IMPLEMENTATION-PLAN.md` |
| Under-specifying plugin boundaries | Adapters, extractors, and reports drift | Static YAML manifests and canonical JSON registry | Manifest validator tests |
| Query/rebuild registry drift | Rebuild, query, and report disagree on declarations | Store registry hash/source-set hash in rebuilds, queries, and reports | Rebuild/query/report parity tests |
| Codex `response_item` becomes core shape | Future providers fake Codex concepts | Generic `runtime_response_items` with correlation status and payload namespaces | Claude-shaped fixture must not fake Codex fields |
| Mandatory event table too early | Duplicates raw/private sources in SQLite | `telemetry_events` optional until adapter proves replay need | First-slice schema excludes required events table |
| Provider neutrality claimed too early | Codex-only implementation marketed as neutral | Require manual, Claude-shaped, and provider-denominator fixtures | Docs/checklist gate neutrality language |
| Enum drift | Plugins invent local names for missingness/reliability/cost | Canonical enum vocabulary and strict validation | Validator rejects undeclared enum values |
| Raw-content leakage through fixtures | Test data accidentally embeds private transcript text | Synthetic fixtures only; structural fields; content hashes/lengths | Fixture linter checks forbidden fields |
| Cost precision overclaim | API-equivalent estimates look like actual bill/quota burn | Mandatory cost evidence mode and caveat fields | Report tests render cost mode and caveat |
| GSD overfit | Phases/milestones become core telemetry entities | GSD is domain plugin, not core ontology | Schema review checks no GSD-only core columns |
