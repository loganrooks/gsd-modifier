# Open Questions Register

Status: post-resolution register for coordinator synthesis.

## Implementation-Blocking Before Code

| Question | Owner | Blocker | Next experiment or decision | Risk if unanswered | Can implementation proceed? |
| --- | --- | --- | --- | --- | --- |
| Exact first-slice table names and Python API shape | Coordinator/planner | Architecture resolved concepts but not code API | Specify in implementation plan before coding | Ambiguous ownership and churn | No, not for schema code |
| Whether evaluator/rubric logic is extractor subtype or fourth plugin class | Coordinator/planner | Lane 06 left both viable | Decide during implementation planning | Hidden evaluator boundary, report drift | No for rubric plugin implementation; yes for schema docs |
| Manifest schema details beyond resolved fields | Coordinator/planner | YAML source and canonical JSON decided, exact fields need spec | Draft `telemetry-plugin-manifest/v1` schema | Plugins may drift | No for adapter work; yes for planning |
| Legacy `score.overall` test migration sequence | Coordinator/planner | Current tests still use scalar score | Plan compatibility test plus rubric observation tests | New schema could break current benchmark helpers | No for test update; yes for docs |

## Provider Evidence Deferred

| Question | Owner | Blocker | Next experiment or decision | Risk if unanswered | Can implementation proceed? |
| --- | --- | --- | --- | --- | --- |
| Exact Codex OTel emitted payload schema | Future provider adapter lane | Requires local collector and controlled Codex run/config override | Fixture-gated local capture with explicit approval | OTel adapter may be speculative | Yes; keep OTel deferred |
| Exact Claude Code OTel emitted payload schema | Future provider adapter lane | Requires configured export/capture | Fixture-gated capture with explicit approval | Claude OTel adapter may overclaim | Yes; keep OTel deferred |
| Live OpenAI/Anthropic API headers and retry behavior | Future API adapter lane | Requires live API calls/credentials/quota | Controlled fixture capture or documented mock | Rate/retry observations incomplete | Yes; use synthetic fixtures first |
| Provider billing truth and subscription/quota burn | Future cost/billing lane | Requires account/billing data or official cost API | Separate cost evidence research | Reports may overstate cost precision | Yes if cost modes remain explicit |
| Local Codex/Claude schema drift over time | Adapter maintenance | Requires multiple versions/samples | Versioned golden fixtures and tolerant parsers | Adapters break on runtime updates | Yes with drift-tolerant design |

## Governance And Claims

| Question | Owner | Blocker | Next experiment or decision | Risk if unanswered | Can implementation proceed? |
| --- | --- | --- | --- | --- | --- |
| When can docs claim provider-neutral substrate? | Coordinator | Requires provider-neutrality gate | Require manual, Claude-shaped, and provider-denominator fixtures | Codex-shaped API masquerades as neutral | Yes, but claims restricted |
| Raw API body/content consent UX | Future privacy/design lane | Out of scope for default no-content path | Separate retention/consent design | Privacy breach or unusable raw-body adapter | Yes; raw content disabled |
| How GSD phases/milestones attach | Future GSD domain plugin | Core must avoid GSD overfit | Domain plugin design after core substrate | GSD leaks into core ontology | Yes; defer as domain plugin |

## Resolved And Carried Forward

| Item | Resolution artifact | Carry-forward rule |
| --- | --- | --- |
| `runtime_response_items` | `ARCHITECTURE-RESOLUTION.md` | Core generic runtime-item concept, distinct from `model_calls`. |
| `telemetry_events` | `ARCHITECTURE-RESOLUTION.md` | Optional replay/debug/import support, not first-slice required infrastructure. |
| Canonical enums | `ARCHITECTURE-RESOLUTION.md` | Use resolved vocabularies; strict validators reject undeclared values. |
| Registry enforcement | `ARCHITECTURE-RESOLUTION.md` | Static YAML source, canonical JSON hash, SQLite cache, rebuild/query/report parity. |
| Provider-neutrality gate | `ARCHITECTURE-RESOLUTION.md` | No neutrality claim from Codex-only fixtures. |
| `score.overall` | `ARCHITECTURE-RESOLUTION.md` | Legacy/view-only as `legacy.score.overall`; rubric observations are canonical. |
