# Checkpoint 5 R5.18 Versus 2026-04-15 Governance Audit Split Comparison Bundle Spec

Purpose: replace the monolithic comparison lane with narrower concern-family lanes so the historical 2026-04-15 governance audit can be reread against the current Checkpoint 5 / `R5.18` frontier without collapsing distinct concern families into one overloaded synthesis pass.

This split bundle does not supersede the completed monolithic artifact. It complements it and gives us finer-grained challenge surfaces before we trust the monolithic comparison as governing.

## Bundle Shape

1. `L1` orchestration / returned-work / config-posture comparison
2. `L2` lifecycle / `LONG-ARC` / non-phase carry-forward comparison
3. `L3` git / repo-ops / CI / release / local-verify comparison
4. `L4` cross-layer handoff / escalation / external-governance comparison
5. `L5` synthesis of `L1`-`L4` against the already-completed monolithic comparison artifact

## Bundle Goals

- test whether the completed monolithic comparison undercalled or overcalled any historical concern family
- surface which historical concerns are:
  - directly inside current `R5.18`
  - only partially addressed or boundary-only
  - explicitly deferred with owner/trigger
  - still missing
  - no longer active but only because they were consciously preserved for later
- preserve concern-family distinctions instead of flattening them into one generic `mostly addressed` judgment

## Governing Inputs

- [checkpoint-5-r5-18-vs-2026-04-15-governance-audit-comparison-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18-vs-2026-04-15-governance-audit-comparison-spec.md)
- [checkpoint-5-r5-18-vs-2026-04-15-governance-audit-comparison-internal-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-18-vs-2026-04-15-governance-audit-comparison-internal-r1.md)
- [checkpoint-5-r5-18-bounded-promoted-corrective-scope-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18-bounded-promoted-corrective-scope-spec.md)
- [checkpoint-5-r5-18-launch-bundle-spec.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/AUDITS/checkpoint-5-r5-18-launch-bundle-spec.md)
- [checkpoint-5-r5-19d4-operational-consequences-adjudication-internal-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-19d4-operational-consequences-adjudication-internal-r1.md)
- [checkpoint-5-r5-19e-adjudication-reread-internal-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/readiness/phase-01-rerun/REVIEWS/checkpoint-5-r5-19e-adjudication-reread-internal-r1.md)

## Anti-Misread Rules

- Do not treat the split bundle as a replacement for the monolithic artifact unless the split synthesis explicitly says the monolithic comparison materially failed.
- Do not treat `present in current docs` as equivalent to `owned by current corrective frontier`.
- Do not over-credit `R5.18` for concerns that are only carried as explicit-disposition or contradiction-ledger entries.
- Do not silently drop historical concern families just because they are less rerun-critical than the current first-wave patch set.

## Required Output Discipline

- `L1`-`L4` should be independent concern-family comparisons.
- `L5` should compare `L1`-`L4` against the monolithic comparison and produce a reconciled consequence map.
