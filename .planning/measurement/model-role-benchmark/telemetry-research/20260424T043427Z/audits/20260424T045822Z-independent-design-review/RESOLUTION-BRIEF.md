# Load-Bearing Resolution Brief

Write target for reviewer recommendation: `LOAD-BEARING-RESOLUTION-RECOMMENDATION.md`
Coordinator final target after review: `ARCHITECTURE-RESOLUTION.md`

## Purpose

Resolve the load-bearing decisions called out by `DESIGN-REVIEW.md` before coordinator synthesis. This is not implementation. It is an architecture-resolution step that must preserve future provider and harness options while giving the next synthesis a concrete decision basis.

## Inputs

- `DESIGN-REVIEW.md`
- `05-ONTOLOGY-STORAGE-OPTIONS.md`
- `06-PLUGIN-PROTOCOL-METRICS.md`
- `01-REFLECT-INHERITANCE-REVIEW.md`
- `02-CODEX-EXPOSURE.md`
- `03-CLAUDE-EXPOSURE.md`
- `04-API-AGENTS-TRACE-SURFACES.md`
- `ORCHESTRATION.md`
- `LANE-SPECS-AND-PROMPTS.md`

## Decisions To Resolve

1. `runtime_response_items`
   - Decide whether this is a core table/concept in the first architecture, an adapter-owned observation family, or a deferred fixture-derived concept.
   - Justify against Codex, Claude local JSONL, OpenAI Agents/API, Anthropic API, OTel, manual import, and future harness support.

2. `telemetry_events`
   - Decide whether event storage is required infrastructure, optional replay/debug support, adapter-owned raw evidence, or deferred.
   - Preserve JSONL/raw artifacts as durable evidence and SQLite as rebuildable cache.

3. Canonical enums
   - Propose concrete enum vocabularies for:
     - missingness
     - evidence class
     - reliability mode
     - content contract
     - cost evidence mode
     - comparability
   - Keep names implementation-ready but not overfit to Codex, Claude, GSD, or one benchmark.

4. Manifest and registry enforcement
   - Decide first-slice manifest format and validation strictness.
   - Decide where registry hash/version/source-set hash must appear.
   - Preserve Reflect registry/store/query parity lesson without importing Reflect workflow ontology.

5. First-slice provider-neutrality gate
   - Decide what non-Codex fixture or provider-neutral fixture gate is mandatory before claiming harness neutrality.
   - Keep first implementation bounded, but prevent Codex-shaped core schema.

6. `score.overall` migration
   - Decide how legacy `score.overall` records are accepted, stored, rendered, and prevented from becoming canonical quality truth.
   - Preserve multidimensional rubric observations as canonical.

## Required Recommendation Format

For each decision, provide:

- verdict: `resolve-now`, `resolve-with-condition`, `defer`, or `reject`
- recommended decision
- rationale
- future-option preservation check
- risk if wrong
- implementation implication
- evidence basis by artifact
- confidence

Then provide:

- `Synthesis Instructions`: exact constraints the coordinator should carry into `DECISION-REPORT.md`
- `Do Not Do`: decisions that would overfit, overbuild, or hide uncertainty
- `Open Questions`: what remains legitimately deferred

## Constraints

- Do not edit lane artifacts.
- Do not perform new provider research or live calls.
- Do not mutate provider configs.
- This is architectural deliberation from existing artifacts.
- Mark artifact-derived claims as such; do not imply independent provider verification.
