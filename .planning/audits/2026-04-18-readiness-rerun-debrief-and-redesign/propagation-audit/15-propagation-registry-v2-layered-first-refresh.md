Date: 2026-04-21
Status: active typed v2 refresh

# Propagation Registry V2 Layered First Refresh

## Purpose

- [g:r:i] This note lands the first typed refresh of the propagation registry after the lane-03 cross-vendor reread.
- [g:r:i] The target is not a bigger flat registry. The target is a clearer split between roster ownership, declared contracts, semantic mapping, observed evidence, and operator-control carry.
- [d:r:i] Opus leads the structural widening here. The local GPT review remains corroborating pressure where it sharpens the same split.

## What Lands In V2

- [e:c+i] The first typed `v2` artifact family is now:
  - [artifacts/02-propagation-registry-v2-inventory-roster.json](artifacts/02-propagation-registry-v2-inventory-roster.json)
  - [artifacts/03-propagation-registry-v2-declared-contracts.json](artifacts/03-propagation-registry-v2-declared-contracts.json)
  - [artifacts/04-propagation-registry-v2-semantic-map.json](artifacts/04-propagation-registry-v2-semantic-map.json)
  - [artifacts/05-propagation-registry-v2-evidence-index.json](artifacts/05-propagation-registry-v2-evidence-index.json)
  - [artifacts/06-propagation-registry-v2-coverage-and-refresh.json](artifacts/06-propagation-registry-v2-coverage-and-refresh.json)

## Why This Split Is Better

- [d:r:i] The old `v1` slice compressed roster truth, semantic mapping, and evidence pointers into one file.
- [d:r:i] The `v2` split makes it easier to see:
  - what is roster-owned
  - what is declared contract
  - what is AI-authored semantic carry
  - what is observed or validated evidence
  - what is still held, refused, or routed to a later refresh
- [d:r:i] This gives the family a more explicit base for later operator tooling without pretending the tooling should come first.

## Current Scope

- [d:r:i] This is still a bounded first typed refresh.
- [d:r:i] It does not attempt whole-upstream roster coverage.
- [d:r:i] It does not open cross-runtime topology, upstream-template drift machinery, or a diff helper yet.
- [d:r:i] It does make the current slice easier to refresh by change-triggered family rather than only by rebuilding a single flat JSON.

## Current Consequence

- [d:r:i] The propagation family now has:
  - prose widening and edge notes in `08-12`
  - predecessor compact slice in `13` and `artifacts/01-*`
  - layered registry policy in `14`
  - typed first refresh in this note and `artifacts/02-06`
- [d:r:i] The next move is no longer `should we build a diff helper now?`
- [d:r:i] The first real `change-triggered slice refresh` is now recorded in [16-compatibility-anchor-change-triggered-refresh.md](16-compatibility-anchor-change-triggered-refresh.md), and later registry movement should keep following actual contract change rather than abstract appetite for a bigger map.
