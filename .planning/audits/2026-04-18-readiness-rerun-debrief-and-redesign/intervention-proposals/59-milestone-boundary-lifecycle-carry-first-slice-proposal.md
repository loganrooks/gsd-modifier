Date: 2026-04-21
Status: accepted bounded proposal

# Milestone Boundary Lifecycle Carry First Slice Proposal

## Purpose

- [g:r:i] This proposal opens the next bounded lifecycle-carry slice after the verifier and transition bridges.
- [g:r:i] The target is not a full milestone-workflow rewrite. The target is the milestone-open and milestone-close boundary where long-arc doctrine and future-carry continuity can still thin if they are left to operator memory.

## Trigger

- [e:c+i] The long-horizon carry register already marked milestone boundaries as one of the next lifecycle surfaces where long-horizon carry can weaken after discuss/plan entry. Sources: [29-long-horizon-carry-gap-register.md](29-long-horizon-carry-gap-register.md:26), [29-long-horizon-carry-gap-register.md](29-long-horizon-carry-gap-register.md:34), [29-long-horizon-carry-gap-register.md](29-long-horizon-carry-gap-register.md:183).
- [e:c+i] `new-milestone.md` currently loads `PROJECT.md`, `MILESTONES.md`, and `STATE.md`, but does not explicitly reread `.planning/LONG-ARC.md` or normalize `Future Carry Forward` as a milestone-opening input. Sources: [/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/new-milestone.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/new-milestone.md:30), [/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/new-milestone.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/new-milestone.md:32), [/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/new-milestone.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/new-milestone.md:425).
- [e:c+i] `complete-milestone.md` currently requires `ROADMAP.md`, `REQUIREMENTS.md`, and `PROJECT.md`, but not `STATE.md` or `.planning/LONG-ARC.md`, and it lacks an explicit milestone-close future-carry review. Sources: [/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/complete-milestone.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/complete-milestone.md:7), [/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/complete-milestone.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/complete-milestone.md:229), [/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/complete-milestone.md](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/workflows/complete-milestone.md:573).
- [e:r:i] The transition slice in `57` and `58` now keeps phase-close carry explicit, which makes the milestone boundary the next narrower lifecycle seam instead of leaving lifecycle carry as one blended field.

## Bounded First Slice

- [d:r:i] Teach `new-milestone.md` to reread `.planning/LONG-ARC.md` when present and treat `STATE.md` `Future Carry Forward` as an explicit milestone-opening input rather than operator memory.
- [d:r:i] Teach the milestone-opening summary, requirements shaping, and roadmapper handoff to keep preserved seams, keep-open non-decisions, posture assumptions, and seeded strengthening routes explicit when they still matter.
- [d:r:i] Teach `complete-milestone.md` to reread `.planning/LONG-ARC.md` and `STATE.md` `Future Carry Forward` before archival/project-evolution cleanup.
- [d:r:i] Add a bounded milestone-close review that decides what future carry remains explicit after milestone closure instead of letting milestone archival silently clear it.

## Verification Gates

- [d:r:i] Overlay ownership for the milestone workflow carriers must become explicit and strict-manifest clean.
- [d:r:i] Post-materialization verification must prove the new milestone-boundary carriers survive repo-local reinstall/materialization.
- [d:r:i] The landed slice should leave a concrete propagation and governance trail rather than only mutating live workflow prose.

## Held Later

- [d:r:i] This slice does not yet widen into `SPEC`, broader `STATE/progress` consumer redesign, or seed-consumer redesign beyond keeping seeded routes explicit at milestone boundaries.
- [d:r:i] This slice does not try to turn milestone boundaries into a full horizon-tension engine; it keeps the boundary reread and continuity judgments explicit and bounded.
