# Migration Origin

## Role

This file records where the extracted `gsd-modifier` repo came from and what was intentionally carried.

## Origin

- source repo: `/home/rookslog/workspace/projects/prix-guesser`
- extraction route was locked in origin commit `de5c3a7`
- migration-set dossier was frozen in origin commit `c1f3635`

The filtered history in this repo stops at the last origin commit that materially touched the migrated path set. That is expected; later origin commits that only changed non-migrated planning/docs surfaces do not appear in the filtered product history here.

## What Was Moved With History

- `harness_modifier/`
- `tooling/codex/`
- `tooling/portable-gsd/overlay/`
- `scripts/setup-portable-gsd.sh`

## What Was Recreated Fresh

- root bootstrap docs
- root governance/onboarding docs
- minimal local planning/governance bootstrap

## Audit Carry

The origin harness-development audit was not migrated as live filtered-history planning identity.

Instead, this repo carries:
- a fresh bootstrap/governance layer for ongoing modifier development
- a compact origin-audit dossier in [docs/origin-audit](origin-audit)
- a historical archive snapshot under [docs/origin-audit/archive](origin-audit/archive)

That keeps the development trail visible and portable without forcing this repo to inherit the entire host-project planning identity as its sovereign live planning engine.
