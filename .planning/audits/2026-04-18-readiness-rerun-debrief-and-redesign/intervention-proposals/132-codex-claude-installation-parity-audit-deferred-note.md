Date: 2026-04-22
Status: completed opening note and route pointer

# Codex Claude Installation Parity Audit Deferred Note

## Why This Note Exists

- [d:r:i] A bounded `.codex` / `.claude` installation-parity audit was earned earlier and deliberately held until the `update + gsd-update` consumer branch settled.
- [d:r:i] That trigger is now satisfied by commit `c530a6a`, so this note now serves as the opening note for the live audit route rather than a still-deferred reminder.

## What Prompted The Note

- [e:c+i] Upstream GSD already treats installation as runtime-specific rather than as plain reference substitution. Sources: [/home/rookslog/.npm/_npx/a2a7266cd903ec8b/node_modules/get-shit-done-cc/README.md](/home/rookslog/.npm/_npx/a2a7266cd903ec8b/node_modules/get-shit-done-cc/README.md:110), [/home/rookslog/.npm/_npx/a2a7266cd903ec8b/node_modules/get-shit-done-cc/README.md](/home/rookslog/.npm/_npx/a2a7266cd903ec8b/node_modules/get-shit-done-cc/README.md:120), [/home/rookslog/.npm/_npx/a2a7266cd903ec8b/node_modules/get-shit-done-cc/bin/install.js](/home/rookslog/.npm/_npx/a2a7266cd903ec8b/node_modules/get-shit-done-cc/bin/install.js:4104), [/home/rookslog/.npm/_npx/a2a7266cd903ec8b/node_modules/get-shit-done-cc/bin/install.js](/home/rookslog/.npm/_npx/a2a7266cd903ec8b/node_modules/get-shit-done-cc/bin/install.js:4204), [/home/rookslog/.npm/_npx/a2a7266cd903ec8b/node_modules/get-shit-done-cc/bin/install.js](/home/rookslog/.npm/_npx/a2a7266cd903ec8b/node_modules/get-shit-done-cc/bin/install.js:4394), [/home/rookslog/.npm/_npx/a2a7266cd903ec8b/node_modules/get-shit-done-cc/bin/install.js](/home/rookslog/.npm/_npx/a2a7266cd903ec8b/node_modules/get-shit-done-cc/bin/install.js:4446).
- [e:c+i] The repo-local installer is currently Codex-first and then applies the repo-local overlay/materialization chain. Source: [scripts/setup-portable-gsd.sh](/home/rookslog/workspace/projects/prix-guesser/scripts/setup-portable-gsd.sh:21).
- [e:c+i] The latest repo-local rematerialization still triggers upstream's unreplaced `.claude` path warning for `get-shit-done/workflows/update.md`, but those hits currently sit inside runtime-detection examples and loops rather than an obviously broken local continuity pointer. Sources: [tooling/portable-gsd/overlay/get-shit-done/workflows/update.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/update.md:53), [tooling/portable-gsd/overlay/get-shit-done/workflows/update.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/update.md:112), [tooling/portable-gsd/overlay/get-shit-done/workflows/update.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/update.md:352), [tooling/portable-gsd/overlay/get-shit-done/workflows/update.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/update.md:438), [tooling/portable-gsd/overlay/get-shit-done/workflows/update.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/update.md:574).
- [d:r:i] That means the local open question is no longer whether runtime-specific installation differences exist. The sharper question is whether this repo's modifier layer, update/install surfaces, and continuity references stay in tune with the upstream `.codex` / `.claude` split.

## What The Later Audit Should Cover

- [d:r:i] Limit the field to `.codex` and `.claude`.
- [d:r:i] Check runtime-specific differences across:
  - install commands and layout
  - commands versus skills
  - agent conversion and agent config
  - hooks and runtime config surfaces
  - repo-local overlay/materialization behavior
  - workflow/reference wording where provider-specific install shape matters
- [d:r:i] Use upstream runtime-specific install logic as the comparison frontier, then inspect where repo-local overlay or workflow surfaces diverge, flatten, or blur those differences.

## Why It Was Deferred

- [d:r:i] The current bounded cross-vendor boundary is still the `update + gsd-update` consumer reread and inheritance path.
- [d:r:i] Opening the parity audit before that boundary closes would widen terrain on top of an unresolved consumer slice and make it harder to tell which pressure belongs to the current `update` branch versus the later installation-parity branch.
- [d:r:i] The cleaner sequence is:
  1. inherit the current `update` reread
  2. revise or land the `update + gsd-update` continuity slice
  3. then open the bounded `.codex` / `.claude` installation-parity audit

## Current Trigger State

- [d:r:i] The `update` consumer branch is now settled, and the parity question was not absorbed away.
- [d:r:i] The bounded audit is now completed under:
  - [../entry-uplift-audit/outputs/23-codex-claude-installation-parity-audit-opus47-max-r1.md](../entry-uplift-audit/outputs/23-codex-claude-installation-parity-audit-opus47-max-r1.md)
  - [../entry-uplift-audit/dispositions/23-codex-claude-installation-parity-audit-inheritance.md](../entry-uplift-audit/dispositions/23-codex-claude-installation-parity-audit-inheritance.md)
- [d:r:i] The next bounded follow-through is now landed at:
  - [134-codex-claude-parity-classification-carrier-proposal.md](134-codex-claude-parity-classification-carrier-proposal.md)
  - [135-codex-claude-parity-classification-carrier-implementation.md](135-codex-claude-parity-classification-carrier-implementation.md)
