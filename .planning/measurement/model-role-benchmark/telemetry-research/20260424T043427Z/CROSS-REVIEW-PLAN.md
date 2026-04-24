# Cross-Review Plan

This plan operationalizes the cross-review map from `ORCHESTRATION.md` after all lane self-audits and dependency repairs completed.

## Rules

- Reviewers write separate files under `cross-reviews/` to avoid write conflicts.
- Reviews are critiques of lane artifacts, not new primary research.
- Reviews must identify:
  - accepted claims
  - overreach or unsupported claims
  - missing evidence or missingness semantics
  - ontology/plugin/schema implications
  - questions the coordinator must carry into synthesis
- Load-bearing schema/protocol decisions remain provisional until coordinator critique and high-reasoning architecture review.

## Assignments

| Reviewer | Input artifacts | Write target |
| --- | --- | --- |
| Lane 02 | `03-CLAUDE-EXPOSURE.md` | `cross-reviews/02-REVIEWS-03.md` |
| Lane 03 | `02-CODEX-EXPOSURE.md` | `cross-reviews/03-REVIEWS-02.md` |
| Lane 04 | `02-CODEX-EXPOSURE.md`, `03-CLAUDE-EXPOSURE.md` | `cross-reviews/04-REVIEWS-02-03.md` |
| Lane 05 | `01-REFLECT-INHERITANCE-REVIEW.md` through `06-PLUGIN-PROTOCOL-METRICS.md` | `cross-reviews/05-REVIEWS-ALL.md` |
| Lane 06 | `01-REFLECT-INHERITANCE-REVIEW.md` through `05-ONTOLOGY-STORAGE-OPTIONS.md` | `cross-reviews/06-REVIEWS-ALL.md` |
| Lane 01 | Final synthesis draft, once created | `cross-reviews/01-REVIEWS-FINAL-SYNTHESIS.md` |

## High-Reasoning Gate

Before `DECISION-REPORT.md` is final, a high-reasoning reviewer must critique load-bearing architecture choices, especially:

- minimum SQLite schema and whether it forecloses future harnesses
- event-first versus entity/edge/observation recommendation
- `runtime_response_items` / `telemetry_events` boundaries
- registry/rebuild/query parity contract
- plugin manifest and metric namespace contract
- rubric observation model and avoidance of `score.overall`
- first implementation slice
