Date: 2026-04-21
Status: accepted bounded proposal

# Update Follow-Through First Slice Proposal

## Purpose

- [g:r:i] This proposal opens the next adjacent onboarding inheritance slice after the landed repair/migration follow-through in `69` and `70`.
- [g:r:i] The target is the runtime/package update family:
  - `update`
  - `gsd-update`

## Why This Slice Is Real

- [e:r:i] `update` already owns runtime/package version detection, changelog display, clean-install warning, installer execution, cache clearing, and local patch recovery reminders.
- [e:r:i] Its thinner edge is not runtime truth. Its thinner edge is what happens after runtime/package movement is understood: the workflow can stop too early and let structural planning repair or broader repo-local posture refresh blur together under the same operator question.
- [e:r:i] This matters because an existing project can be current on package version and still need either:
  - structural planning repair
  - later repo-local posture uplift
- [e:r:i] Leaving those routes ambient makes update feel wider than it should be and makes later onboarding/uplift control harder to maintain.

## Bounded First Slice

- [d:r:i] Bring the current `update` workflow and `gsd-update` skill wrapper into tracked overlay ownership.
- [d:r:i] Teach `update` to inherit the shared layered packet doctrine explicitly:
  - `required_reading`
  - `supporting_reading`
  - `deeper_reading`
- [d:r:i] Keep route ownership explicit rather than blended:
  - `update` owns runtime/package movement, installer rerun, custom-file backup, and patch recovery reminders
  - structural planning repair routes to `$gsd-health`
  - broader repo-local posture refresh routes separately to `$gsd-uplift-project --write`
- [d:r:i] Keep the current-runtime branch from ending as if nothing else could still matter:
  - runtime/package currentness should be allowed to coexist with a later structural-repair or posture-refresh route

## Held Later

- [d:r:i] This slice does not yet widen into broader repeated-reinstall probes or standalone compatibility-carrier work.
- [d:r:i] It does not yet widen into seed-consumer carry.
- [d:r:i] It does not auto-launch uplift or health from `update`; it keeps the routes explicit and separate.

## Verification Gates

- [d:r:i] Add a focused contract test that checks:
  - overlay ownership for `update.md` and `skills/gsd-update/SKILL.md`
  - layered packet doctrine plus explicit health/uplift route separation in `update.md`
  - explicit runtime/package ownership plus separate repair/uplift follow-through in `gsd-update`
- [d:r:i] Re-materialize the overlay so the live `.codex` frontier carries the same update follow-through.
- [d:r:i] Refresh propagation carriers because this slice moves one shared reference consumer, one workflow carrier, one wrapper carrier, and explicit new route edges into `health` and `uplift`.

## Current Consequence

- [d:r:i] If this slice lands, the onboarding family no longer stops at creation, milestone opening, doc ingest, re-entry, repair, and migration.
- [d:r:i] The next narrower question becomes which adjacent family should inherit after update:
  - seed consumers
  - a later wider entry-wrapper retrofit
  - or a broader repeated-reinstall / compatibility carrier

