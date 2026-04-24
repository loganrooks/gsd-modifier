Date: 2026-04-21
Status: active bounded reread spec

# Historical Scanner-Influenced Reread Spec

## Objective

- [g:r:i] Produce a contextual historical reread over the bounded scanner-influenced commit family so the workspace can distinguish useful widening from harmful wording control or governance drift.

## Scope

- [d:r:i] The reread must stay inside the packeted historical commit set and the explicitly named high-priority surfaces.
- [d:r:i] It may inspect surrounding file context and commit diffs when needed, but it should not widen into unrelated threshold residue across the whole repo.

## Required Method

1. [d:r:i] Reread each historical commit in context, not only by commit message.
2. [d:r:i] Check whether touched files are:
   - doctrine / instruction surfaces
   - live governance surfaces
   - historical audit/research outputs
   - tooling / heuristic surfaces
3. [d:r:i] Judge edits against file role:
   - explicit prohibition naming is often desirable in doctrine files
   - heuristic cleanliness is not a valid reason by itself to weaken direct anti-pattern naming
   - live governance should not treat the scanner as a gate
4. [d:r:i] Name specific artifacts that now deserve:
   - `keep`
   - `patch`
   - `contextual reinterpretation`
   - `revisit the earlier judgment`

## Anti-Misread Rules

- [g:r:i] Do not collapse this into “was the scanner good or bad?”
- [g:r:i] Do not treat the current internal audit as automatically complete.
- [g:r:i] Do not reward euphemism merely because it avoids flagged words.
- [g:r:i] Do not flatten historical quoted evidence and live governance carry into one contamination bucket.

## Output Path

- [d:r:i] Write the review to:
  - `.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/threshold-audit/outputs/05-historical-scanner-influenced-reread-gpt54-xhigh-r1.md`

