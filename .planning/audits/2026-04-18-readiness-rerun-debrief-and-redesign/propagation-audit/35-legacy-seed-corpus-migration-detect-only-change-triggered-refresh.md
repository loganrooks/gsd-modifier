Date: 2026-04-22
Status: landed refresh

# Legacy Seed Corpus Migration Detect-Only Change-Triggered Refresh

## Trigger

- [g:r:i] The trigger here is a new seed-family specialist route:
  - helper-side inventory for legacy or drifted seed corpora
  - a dedicated workflow and wrapper
  - an explicit uplift handoff into that packet

## What The Refresh Carries

- [e:r:i] The typed propagation layer now keeps the new helper/workflow/wrapper route explicit instead of leaving migration planning ambient behind uplift posture plus held-later prose.
- [e:r:i] The refresh also keeps one important separation explicit:
  - `.planning/seeds/SEED-*.md` remain the corpus under migration inventory
  - `STATE.md` `Future Carry Forward -> Seeded` remains a different continuity carrier
- [e:r:i] The uplift route now names the specialist detect-only packet instead of stopping at posture examples and a held-later register line.

## Neighboring Non-Moves

- [d:r:i] This refresh does not widen `progress` or `resume-project`.
- [d:r:i] It does not widen `audit.cjs`.
- [d:r:i] It does not widen canary, runtime-visibility, or manifest-coherence helpers into seed-aware checks.
- [d:r:i] It does not introduce rewrite automation.

## Current Consequence

- [d:r:i] The propagation family now keeps the seed-migration detect-only route explicit as a separate carrier cluster rather than leaving legacy seed migration as only posture plus future promise.
