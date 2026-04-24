# Opus Cross-Review Spec

Status: drafted, not launched

## Purpose

Run an external `Opus 4.7 xhigh` review of this audit setup before the main audit wave starts.

The job is not to redo the whole readiness package yet. The job is to pressure-test:

- the framing
- the question set
- the plan proposals
- the evidence architecture
- the burden-of-proof rules for tame recommendations

## Review Target

Primary review target:
- this entire directory

Required external read set in addition to this directory:
- `.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/planning-notes/SESSION-FRAMING-BRIEF.md`
- `.planning/readiness/phase-01-rerun/PLAN.md`
- `.planning/readiness/phase-01-rerun/POST-FALSIFICATIONIST-REVIEW-DOCTRINE.md`
- `.planning/audits/2026-04-17-gsd-upstream-docs-readiness-comparative-audit/SYNTHESIS.md`
- `.planning/audits/2026-04-17-gsd-upstream-docs-readiness-comparative-audit/lane-03-reseed-judgment.md`
- `.planning/audits/2026-04-17-gsd-upstream-docs-readiness-comparative-audit/lane-12-opus47-courageous-docs-refresh-recommendation.md`

Use repo-local paths, not `/tmp` wrapper files.
Do not read raw Codex logs unless the task spec is later amended with a narrow dispute that actually requires them.
Treat `../planning-notes/SESSION-FRAMING-BRIEF.md` as a situated briefing artifact, not as an impartial surrogate for the full conversation.

## Core Questions

1. Is the main framing strong enough, or is it still too tame, too narrow, too binary, or too attached to the old readiness package's own closure logic?
2. Is the session briefing itself skewing the audit frame in a way that should be corrected or supplemented?
3. Are the current plan proposals actually the right option set, or is a missing proposal shape needed?
4. Is the current question set missing any critical line of inquiry?
5. Is the evidence architecture packeted well enough to support later serious lanes?
6. Does the current burden-of-proof rule for `no change` / `no new lane` / `leave it local` go far enough?
7. Is the current role assigned to the `04-17` bridge audit correct?
8. What is still most likely to cause this second attempt to underreach?

## Required Posture

- do not optimize for the easiest viable setup
- do not praise the suite for being organized unless that organization actually improves audit quality
- do not accept `no further prep needed` or `current framing is sufficient` without explicit burden of proof
- explicitly call out any remaining human-timeline bias, prestige-model bias, or quiet minimal-change bias
- if a stronger program shape is warranted, name it concretely
- when challenging framing claims, do not assume strict falsifiability is the only acceptable standard; post-falsificationist pressure can also take the form of rival explanation, anomaly pressure, comparative weakness, or explicit weakening conditions

## Required Output

Produce a markdown artifact in this directory named:

- `../lane-reviews/lane-01-opus47-audit-setup-cross-review.md`

Required sections:

1. `Overall Judgment`
2. `Framing Strengths`
3. `Framing Weaknesses`
4. `Session-Brief Distortions Or Limits`
5. `Missing Questions`
6. `Plan-Proposal Critique`
7. `Evidence-Architecture Critique`
8. `Tame-Recommendation Failure Modes`
9. `Recommended Revisions Before Main Wave`
10. `Whether Launch Is Justified Yet`

## If Recommending No Major Revision

That recommendation must explicitly justify:

- why the current frame is strong enough
- why the current question set is not leaving material gains on the table
- why the current plan architecture is not prematurely narrowing the rerun
- why a stronger preparatory phase is unlikely to materially improve the second attempt

## Launch Notes

- use `--dangerously-skip-permissions`
- use repo-local spec paths
- record requested-versus-effective launch truth if the review is actually launched
- update [LAUNCH-LEDGER.md](../root-support/LAUNCH-LEDGER.md) after launch
