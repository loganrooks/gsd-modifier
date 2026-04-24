Date: 2026-04-21
Status: accepted bounded proposal

# Initialization And Ingest Read-Packet First Slice Proposal

## Purpose

- [g:r:i] This proposal opens the next bounded inheritance step after the landed operator-facing read-packet slice in `65` and `66`.
- [g:r:i] The target is not every remaining onboarding or repair surface at once. The target is the initialization and ingest trio that still shapes first-read burden too bluntly:
  - `new-project.md`
  - `new-milestone.md`
  - `ingest-docs.md`

## Why This Slice Is Real

- [e:r:i] The previous slice already made `progress`, `resume-project`, and `uplift-project` more deliberate about primary packet, route-local support, and deeper widening.
- [e:r:i] The initialization family still starts from flatter reading posture:
  - `new-project` still opens with one flat mandatory-read block and a blunt `project_exists -> use progress` line
  - `new-milestone` still names the right milestone-open files, but not as an explicit layered packet
  - `ingest-docs` still treats doc discovery, merge review, and later repo-local uplift as one blended startup space
- [e:r:i] These surfaces matter disproportionately because they shape onboarding, bootstrap, milestone opening, and document-driven re-entry.

## Bounded First Slice

- [d:r:i] Bring `new-project.md` and `ingest-docs.md` into tracked overlay ownership alongside the already-carried `new-milestone.md`.
- [d:r:i] Teach all three workflows to use the shared mandatory-read doctrine explicitly:
  - `required_reading`
  - `supporting_reading`
  - `deeper_reading`
- [d:r:i] Make the route split visible rather than ambient:
  - `new-project` starts from init plus provided idea context, then widens only when brownfield or prior-findings routes activate
  - `new-milestone` starts from milestone-open project/state/long-arc context, then widens into seeds or research only when those routes activate
  - `ingest-docs` starts from args/init/manifest, then widens into classifications, conflicts, merge canon, and only later repo-local uplift when those routes actually surface
- [d:r:i] Keep repo-local uplift routing explicit at the boundaries where an older or vanilla project can be present:
  - `new-project` should not silently reopen initialization when the real route is progress plus uplift
  - `ingest-docs` should not pretend planning-doc merge is the same thing as runtime/governing-surface uplift

## Held Later

- [d:r:i] This slice does not yet widen into `health`, `from-gsd2`, or the broader repair/migration family.
- [d:r:i] It does not yet add automatic relevance ranking.
- [d:r:i] It does not yet widen packet tiers across spawned agent definitions or every entry skill wrapper.

## Verification Gates

- [d:r:i] Add a focused contract test that checks:
  - overlay ownership for `new-project.md`, `new-milestone.md`, and `ingest-docs.md`
  - layered packet structure on those three workflows
  - explicit `$gsd-uplift-project --write` routing on the two surfaces where older/vanilla project uplift pressure can actually surface in this slice
- [d:r:i] Re-materialize the overlay so the live `.codex` frontier carries the same initialization/onboarding contract.
- [d:r:i] Refresh propagation carriers because this slice moves a shared reference contract plus three additional workflow consumers.

## Current Consequence

- [d:r:i] If this slice lands, the harness no longer improves read-packet control only at re-entry.
- [d:r:i] The next narrower question becomes which adjacent onboarding family should inherit after this:
  - `health` / repair
  - `from-gsd2` / migration
  - seed-consumer carry
  - or a later broader packet retrofit
