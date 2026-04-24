Date: 2026-04-22
Status: active doctrine note

# Harness Program Horizons And Future-Carry Doctrine

## Role

- [d:r:i] This note defines the horizon stack for the harness-improvement program itself.
- [d:r:i] Its job is to stop harness horizons from being silently borrowed from host-product planning docs or from one active local slice.

## Scope Rule

- [g:r:i] Harness-program horizons are separate from host-product horizons.
- [d:r:i] Host-product docs such as `.planning/LONG-ARC.md`, `.planning/ROADMAP.md`, and host `.planning/STATE.md` can still matter when a slice explicitly crosses into:
  - product planning
  - rerun coupling
  - entry / re-entry integration
- [d:r:i] But they are contextual inputs, not the default sovereign future surface for the harness-improvement program.

## Horizon Stack

### Near Horizon

- [d:r:i] The near horizon is the current bounded slice and its required neighboring carry.
- [d:r:i] Typical carriers:
  - `CURRENT-STATE.md`
  - `STATUS.md`
  - the live proposal / implementation note
  - change-triggered refresh notes
  - focused verification surfaces

### Medium Horizon

- [d:r:i] The medium horizon is the active family field:
  - current extraction branch
  - propagation branch
  - responsible-closure branch
  - parallelization branch
  - held-later adjacent routes
- [d:r:i] Typical carriers:
  - `.planning/HARNESS-IMPROVEMENT-REGISTER.md`
  - `intervention-proposals/README.md`
  - family `README.md` notes
  - bounded next proposals and inheritance notes

### Far Horizon

- [d:r:i] The far horizon is not a fixed roadmap promise.
- [d:r:i] It is the harness program's orienting future:
  - cleaner extraction into its own repo
  - deployability across host contexts
  - adaptive post-deploy feedback
  - stronger agential capacity under uncertainty
  - better management of long-horizon futures without premature closure
- [d:r:i] Typical carriers:
  - extraction route notes like `115`
  - responsible-closure route notes like `161`
  - this note
  - the harness-improvement register

## Horizon Tensions

- [d:r:i] Long-horizon orientation should not collapse into vague aspiration only.
- [d:r:i] Near-horizon execution should not flatten medium/far futures into whatever is locally convenient.
- [d:r:i] Revision pressure from later reviews should not be treated as failure of the horizon stack; it is part of how the stack stays alive under new evidence.
- [d:r:i] The practical task is not to eliminate tension but to route it cleanly.

## Reopen And Revision Rules

- [d:r:i] When a review or audit materially changes the path, do not rewrite every horizon layer at once.
- [d:r:i] Instead:
  1. update the near-horizon slice and governance carry
  2. revise the medium-horizon family routing if the family shape changed
  3. revise far-horizon orientation only if the result actually changes the protected future or extraction/deployability direction
- [d:r:i] Do not let a local change silently reset far-horizon ambition.
- [d:r:i] Do not let far-horizon desire force immediate implementation when the bounded next slice has not earned it.

## Protected Futures

- [d:r:i] Some futures should remain open by explicit policy:
  - standalone harness-modifier repo
  - installer/distribution travel
  - richer adaptive telemetry/feedback
  - stronger parallelization frameworks
  - broader host-context deployability
- [d:r:i] Keeping these open does not mean importing them wholesale into every current slice.
- [d:r:i] It means later local convenience should not quietly foreclose them.

## Current Consequence

- [d:r:i] When a later note names `short`, `medium`, or `long` horizon, interpret that first against the harness-improvement program unless the note explicitly says it is talking about the host product.
- [d:r:i] If a later audit starts reading host-product future docs as if they were automatically the harness's sovereign future surface, that is a scope error that should be corrected explicitly.
