Date: 2026-04-22
Status: active audit spec

# Codex Claude Installation Parity Audit Spec

## Framing

- [g:r:i] Audit the `.codex` / `.claude` installation-parity field immediately after the landed `update + gsd-update` continuity consumer branch.
- [g:r:i] The governing task is not to ask whether the repo is merely `compatible` in the abstract and not to widen into all-provider parity.
- [g:r:i] The governing task is to map the current two-runtime field:
  - what upstream already separates explicitly at install/materialization time
  - where repo-local carry stays aligned with that split
  - where repo-local carry still blurs or compresses runtime-specific responsibilities
  - which surfaced `.claude` hits are real defects versus contextual warnings
  - what bounded next intervention would most sharpen the field
- [g:r:i] Keep the audit away from pass/fail or minimum-bar framing. `.codex` and `.claude` are the whole provider horizon here.

## Primary Questions

1. What does upstream already separate explicitly between `.codex` and `.claude` at install/materialization time?
2. Where does the repo-local modifier layer already stay in tune with that upstream split?
3. Where do repo-local install/update/materialization surfaces still blur runtime-specific responsibilities, install shapes, or references?
4. Which currently surfaced `.claude` references in repo-local surfaces are real current defects, and which are contextual warnings inside runtime-detection or installer examples?
5. What should remain explicitly later-family work instead of being folded into one parity-cleanup pass?
6. What is the strongest bounded next route after this audit?

## Required Output Shape

Use these exact section headings:

1. `What Upstream Already Separates Explicitly`
2. `Where Repo-Local Carry Already Travels In Tune`
3. `Where Repo-Local Carry Still Blurs Runtime-Specific Responsibilities`
4. `Which Surfaced Claude References Are Real Defects Versus Contextual Warnings`
5. `What To Keep Explicitly Later`
6. `Strongest Next Route`
7. `How This Audit Should Be Inherited`

Inside section `7`, separate:
- `Carry Forward`
- `Revise`
- `Hold For Later`

## Audit Discipline

- [d:r:i] Judge the actual current repo-local installer/materialization layer and the actual upstream runtime-specific installer logic, not a simplified verbal summary of either.
- [d:r:i] Keep runtime-specific install shape distinct from generic wording cleanup.
- [d:r:i] Keep overlay source, live materialized state, and upstream pristine installer behavior distinct instead of flattening them into one blended install story.
- [d:r:i] Treat leak-style `.claude` warnings contextually:
  - a literal `.claude` path in a codex-targeted runtime-only instruction may be a defect
  - a `.claude` path inside runtime-detection arrays, upstream examples, or explanatory install comments may be a contextual warning rather than a defect
- [d:r:i] If you think a surfaced issue belongs in a later bounded slice, name the boundary explicitly and explain why.

## Output Path

- Opus output:
  - [entry-uplift-audit/outputs/23-codex-claude-installation-parity-audit-opus47-max-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/entry-uplift-audit/outputs/23-codex-claude-installation-parity-audit-opus47-max-r1.md)
