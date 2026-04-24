Date: 2026-04-21
Status: accepted bounded proposal

# Transition Lifecycle Carry First Slice Proposal

## Purpose

- [g:r:i] This proposal opens the next bounded lifecycle-carry slice after verifier follow-through.
- [g:r:i] The target is not a whole-lifecycle rewrite. The target is the phase-closure boundary where `transition.md` currently evolves roadmap/state/project surfaces without a normalized carry path for preserved seams, explicit non-decisions, posture assumptions, and strengthening routes.

## Trigger

- [e:c+i] The long-horizon carry register already marked `transition.md` as the next lifecycle surface where future-aware carry can still thin after planning and verification. Sources: [29-long-horizon-carry-gap-register.md](29-long-horizon-carry-gap-register.md:27), [29-long-horizon-carry-gap-register.md](29-long-horizon-carry-gap-register.md:44), [29-long-horizon-carry-gap-register.md](29-long-horizon-carry-gap-register.md:182).
- [e:r:i] The verifier slice in `53` and `54` closed the planning-to-verification bridge, which makes the phase-close bridge the next narrower pressure instead of leaving lifecycle carry as one undifferentiated field.

## Bounded First Slice

- [d:r:i] Teach `transition.md` to load plan `future_preservation` when present instead of treating phase completion as requirement/decision evolution only.
- [d:r:i] Add a bounded `Future Carry Forward` digest shape to the state template and require transition-time upkeep of that digest.
- [d:r:i] Distinguish four carry buckets at phase close:
  - `protected_seams`
  - `non_decisions`
  - `posture_assumptions`
  - `strengthening_routes`
- [d:r:i] Route strengthening items that do not belong in the next immediate phase toward explicit seed handoff rather than leaving them ambient in state prose.

## Verification Gates

- [d:r:i] Overlay ownership for any new transition/state-template carriers must be explicit and strict-manifest clean.
- [d:r:i] Post-materialization verification must prove the new carriers survive repo-local reinstall/materialization.
- [d:r:i] The landed slice should leave a concrete governance and propagation trail instead of only mutating live workflow prose.

## Held Later

- [d:r:i] This slice does not yet widen into milestone-close, `SPEC`, or broad `progress`/`resume` consumer redesign.
- [d:r:i] This slice does not try to settle every activation-pressure or long-arc doctrine question at once.
