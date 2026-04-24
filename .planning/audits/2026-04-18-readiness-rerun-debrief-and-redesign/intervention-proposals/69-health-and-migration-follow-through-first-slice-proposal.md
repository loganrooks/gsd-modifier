Date: 2026-04-21
Status: accepted bounded proposal

# Health And Migration Follow-Through First Slice Proposal

## Purpose

- [g:r:i] This proposal opens the next bounded onboarding inheritance step after the landed initialization/doc-ingest slice in `67` and `68`.
- [g:r:i] The target is not every remaining entry wrapper. The target is the older-project repair and migration pair that still ends too early:
  - `health`
  - `from-gsd2`

## Why This Slice Is Real

- [e:r:i] `health` already owns structural planning validation and low-risk repair, but it still treats broader repo-local posture refresh as outside its owned route.
- [e:r:i] `from-gsd2` already owns format migration from `.gsd/` to `.planning/`, but it still stops at structural conversion rather than validating the migrated tree and separating later repo-local uplift explicitly.
- [e:r:i] These surfaces matter disproportionately because they are exactly where an older, damaged, or migrated project can look usable while still missing stronger repo-local runtime, governing-doc, or doctrine posture.

## Bounded First Slice

- [d:r:i] Bring the current `health` workflow plus the `gsd-health` and `gsd-from-gsd2` skill wrappers into tracked overlay ownership.
- [d:r:i] Teach `health` to inherit the shared mandatory-read doctrine explicitly:
  - `required_reading`
  - `supporting_reading`
  - `deeper_reading`
- [d:r:i] Keep route ownership explicit rather than blended:
  - `health` owns structural planning integrity and limited low-risk repair
  - missing planning state still routes to `new-project` or `ingest-docs`
  - repo-local runtime, governing-doc, or doctrine posture refresh routes separately to `$gsd-uplift-project --write`
- [d:r:i] Keep `from-gsd2` from ending at format conversion alone:
  - after migration, run structural health validation
  - report the health result with the migration output
  - route later repo-local uplift explicitly rather than pretending migration installed that posture

## Held Later

- [d:r:i] This slice does not yet widen into `update`.
- [d:r:i] It does not yet add automatic uplift launching from `health` or `from-gsd2`.
- [d:r:i] It does not yet widen across every remaining entry or repair wrapper.

## Verification Gates

- [d:r:i] Add a focused contract test that checks:
  - overlay ownership for `health.md`, `skills/gsd-health/SKILL.md`, and `skills/gsd-from-gsd2/SKILL.md`
  - layered packet doctrine plus explicit separate uplift route in `health.md`
  - explicit structural-health and later-uplift follow-through in the two skill wrappers
- [d:r:i] Re-materialize the overlay so the live `.codex` frontier carries the same repair/migration follow-through.
- [d:r:i] Refresh propagation carriers because this slice moves one shared reference consumer, two wrapper carriers, and the repair/migration route split.

## Current Consequence

- [d:r:i] If this slice lands, the onboarding family no longer improves only creation, milestone opening, doc ingest, and re-entry.
- [d:r:i] The next narrower question becomes which adjacent family should inherit after this:
  - `update`
  - seed-consumer carry
  - or a later wider entry-wrapper retrofit
