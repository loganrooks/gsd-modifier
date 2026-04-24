Date: 2026-04-22
Status: active reread spec

# Health Uplift Deepen-In-Place First Slice Proposal Reread Spec

## Framing

- [g:r:i] Reread the next adjacent single-carrier route after the landed milestone-boundary shared-reference slice in `123`.
- [g:r:i] The governing task is not to ask whether `124` clears a minimum bar.
- [g:r:i] The governing task is to judge whether `health.md` should deepen in place next, what that route should read first, how it should keep structural repair distinct from later uplift follow-through, and what it must keep out.
- [g:r:i] Keep the review away from binary-gate framing, minimum-bar vocabulary, another generic “just run uplift after health” answer, and premature widening back into whole-family implementation.

## Primary Questions

1. What does `124` choose well as the next bounded route after `123`?
2. Should this carry deepen in place inside `health.md`, or is another carrier shape better?
3. What should the health route read first, when should it widen, and what should stay route-local?
4. How should `health.md` and `gsd-health` divide structural repair, read-only uplift continuity, and later write-side refresh?
5. What must stay out of scope for this slice?
6. How should this proposal be inherited now?

## Required Output Shape

Use these exact section headings:

1. `What The Proposal Chooses Well`
2. `Whether Health Should Deepen In Place`
3. `What The Health Route Should Read And When`
4. `How Workflow And Wrapper Should Divide The Route`
5. `What Must Stay Out Of Scope`
6. `How This Proposal Should Be Inherited`

Inside section `6`, separate:
- `Carry Forward`
- `Revise Locally`
- `Keep Later`
- `Next Bounded Move`

## Review Discipline

- [d:r:i] Keep the slice bounded to `health.md` plus `gsd-health`.
- [d:r:i] Preserve health as the structural-repair owner.
- [d:r:i] Preserve `compatibility_posture: observed_basis_only`.
- [d:r:i] Preserve held runtime annotation as annotation, not as dual-basis relabel.
- [d:r:i] Do not let the health route become a write-side compatibility dispatcher.
- [d:r:i] Do not widen into parity, translation, matrix claims, structural-row promotion, or extraction work.
- [d:r:i] Judge the proposal against the live `STATE.md` `Project Uplift` digest plus the current uplift report/manifest surfaces, not only against the health workflow text.

## Output Path

- Opus output:
  - [entry-uplift-audit/outputs/18-health-uplift-deepen-in-place-first-slice-proposal-reread-opus47-max-r1.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/entry-uplift-audit/outputs/18-health-uplift-deepen-in-place-first-slice-proposal-reread-opus47-max-r1.md)
