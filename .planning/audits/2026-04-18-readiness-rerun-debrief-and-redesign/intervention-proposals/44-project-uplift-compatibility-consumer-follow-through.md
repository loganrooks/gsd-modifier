Date: 2026-04-21
Status: landed consumer-chain follow-through

# Project-Uplift Compatibility Consumer Follow-Through

## Trigger

- [e:c+i] The xhigh reviewer lane preserved in [threshold-audit/outputs/04-scanner-side-effects-internal-audit-review-gpt54-xhigh-r1.md](../threshold-audit/outputs/04-scanner-side-effects-internal-audit-review-gpt54-xhigh-r1.md) surfaced a real carry failure: the compatibility anchor added in `43` lived in durable outputs, but the active routed consumers still returned `Continue with current routing.` after observed runtime-basis movement.
- [d:r:i] That meant the compatibility anchor was present as stored memory but not yet steering the live read-only consumer path that operators actually see through `progress` and `resume-project`.

## What Landed

- [e:r:i] [project_uplift.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/project_uplift.py) now compares the stored `compatibility_basis` block with the current observed runtime basis during `progress-note`.
- [e:r:i] When the observed basis moves, the helper now:
  - sets `recommend_write: true`
  - marks `compatibility_basis_changed: true`
  - routes the recommendation toward `$gsd-uplift-project --write`
  - records explicit movement reasons instead of returning a flat continue signal
- [e:r:i] The helper now anchors the observed runtime version only to the canonical repo-local path `.codex/get-shit-done/VERSION` rather than silently falling back to `.codex/VERSION`.
- [e:r:i] The overlay workflow and skill now inherit that sharper routed consequence:
  - [uplift-project.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/get-shit-done/workflows/uplift-project.md)
  - [gsd-uplift-project/SKILL.md](/home/rookslog/workspace/projects/prix-guesser/harness_modifier/overlay/skills/gsd-uplift-project/SKILL.md)
- [e:r:i] The helper test suite now covers:
  - runtime-basis movement producing a `--write` recommendation
  - noncanonical `.codex/VERSION` presence not masquerading as observed regular-runtime truth

## Current Consequence

- [d:r:i] The compatibility anchor now reaches the live routed-consumer chain instead of remaining only in `UPLIFT-REPORT.md`, `UPLIFT-MANIFEST.json`, and `STATE.md`.
- [d:r:i] The current compatibility family still remains bounded:
  - no wider supported-version window claim
  - no standalone compatibility carrier
  - no broader cross-runtime reconciliation family folded in here
- [d:r:i] What changed is narrower and more important for the current slice: when the observed runtime basis moves, the active operator-facing route now says so and points back to a durable uplift refresh.
