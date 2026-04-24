Date: 2026-04-21
Status: accepted bounded proposal

# Read-Packet And Relevance-Control First Slice Proposal

## Purpose

- [g:r:i] This proposal opens the next bounded lifecycle / operator-control slice after the spec-boundary bridge.
- [g:r:i] The target is not a whole harness-wide reread redesign. The target is the flatter entry and re-entry reading posture that still makes operators and workflows widen context too early or too indiscriminately.

## Why This Slice Is Real

- [e:r:i] The repo-local governance set already pushes progressive disclosure inside the audit workspace, but the live harness entry surfaces still flatten reading into one broad startup block too often.
- [e:r:i] The current `mandatory-initial-read` reference only says `read every file in <required_reading>` and does not distinguish:
  - irreducible startup context
  - route-local supporting context
  - deeper context that should wait until the route actually points there
- [e:r:i] The current re-entry surfaces reflect that flatter posture:
  - `progress.md`
  - `resume-project.md`
  - `uplift-project.md`
- [e:r:i] That matters because these are the exact operator-facing surfaces that should give better control over what gets read first, what becomes relevant later, and when deeper family rereads are earned.

## Bounded First Slice

- [d:r:i] Bring `references/mandatory-initial-read.md` into tracked overlay ownership so repo-local reading doctrine becomes durable instead of staying a one-line upstream default.
- [d:r:i] Expand that reference into a three-tier packet doctrine:
  - `required_reading`
  - `supporting_reading`
  - `deeper_reading`
- [d:r:i] Keep contextual reread sovereign:
  - packet tiers widen attention
  - they do not replace route-specific judgment
  - they do not justify laundering explicit anti-patterns, prohibitions, or historical evidence just to keep a packet narrow
- [d:r:i] Teach the current re-entry surfaces to use that layered packet explicitly:
  - `progress.md`
  - `resume-project.md`
  - `uplift-project.md`
- [d:r:i] Keep the slice bounded:
  - no harness-wide retrofit of every workflow or agent contract
  - no new-project / new-milestone widening yet
  - no automatic relevance ranking engine
  - no broad packet-generation machinery

## Runtime / Contract Surfaces To Move Together

1. [d:r:i] `tooling/portable-gsd/overlay/get-shit-done/references/mandatory-initial-read.md`
2. [d:r:i] `tooling/portable-gsd/overlay/get-shit-done/workflows/progress.md`
3. [d:r:i] `tooling/portable-gsd/overlay/get-shit-done/workflows/resume-project.md`
4. [d:r:i] `tooling/portable-gsd/overlay/get-shit-done/workflows/uplift-project.md`
5. [d:r:i] `tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json`

## Verification Gates

- [d:r:i] Add a focused contract test that checks:
  - tracked overlay ownership for the mandatory-read reference
  - the three reading tiers exist
  - the current entry/re-entry surfaces actually carry the layered packet doctrine
- [d:r:i] Re-materialize the overlay so the live `.codex` frontier carries the same reading-control contract.
- [d:r:i] Refresh the propagation carriers because this slice changes a shared reference contract plus three operator-facing workflow consumers.

## Held Later

- [d:r:i] This slice does not yet widen into `new-project`, `new-milestone`, or other initialization surfaces.
- [d:r:i] It does not yet add packet tiers across spawned agent definitions.
- [d:r:i] It does not yet build automatic relevance scoring or route synthesis.

## Current Consequence

- [d:r:i] If this slice lands, the harness no longer treats entry and re-entry reading as one flat startup burden in the current operator-facing surfaces.
- [d:r:i] The next narrower question becomes which adjacent entry family should inherit next:
  - initialization / onboarding surfaces
  - seed-consumer carry
  - or a later wider packet retrofit
