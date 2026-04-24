Date: 2026-04-20
Status: accepted follow-through frame

# Cleaner Manifest / Install Coherence Follow-Through

## Purpose

- [g:r:i] This note lands the fourth move in the accepted second-tranche order: revisit manifest/install coherence on the corrected baseline rather than through cleanup panic or manifest semantic collapse.

## Starting Ground

- [e:c+i] The semantic contract already rejected rewriting `gsd-file-manifest.json` into a final-runtime snapshot. Sources: [08-manifest-semantic-contract-disposition.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/08-manifest-semantic-contract-disposition.md:1).
- [e:c+i] The runtime-visibility tranche then created a separate classified final-runtime surface instead of collapsing everything back into the manifest. Sources: [10-final-runtime-visibility-first-pass-disposition.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/10-final-runtime-visibility-first-pass-disposition.md:1), [01-runtime-visibility-report.json](../tranche-audit/artifacts/01-runtime-visibility-report.json:1).
- [e:c+i] The targeted reread also rejected the false story that broad stale-agent cleanup must precede any coherence work. Sources: [13-live-only-agent-targeted-reread-disposition.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/13-live-only-agent-targeted-reread-disposition.md:1).

## Accepted Coherence Shape

- [d:r:i] Manifest/install coherence should now be treated as a three-surface comparison problem:
  - updater/custom-file boundary truth from `gsd-file-manifest.json`
  - tracked subset-carry truth from `backup-meta.json`
  - selected-lane final-runtime truth from classified runtime snapshots

## What This Means

### 1. Do not rewrite manifest semantics

- [d:r:i] `gsd-file-manifest.json` still answers:
  - what the updater knows it shipped
  - what custom-file boundary logic protects

### 2. Do not ask backup metadata to be more than it is

- [d:r:i] `backup-meta.json` still answers:
  - which bounded tracked carry subset the repo preserves across reinstall/update

### 3. Ask selected-lane snapshots to carry final runtime truth

- [d:r:i] Runtime snapshots now answer:
  - what the live repo-local harness actually carried after install, overlay materialization, and repo-local mutation at a meaningful lane boundary

## Stronger Coherence Questions

- [d:r:i] The next coherence pass should ask:
  - which runtime differences are expected from materialization or repo-local carry
  - which live-only surfaces are intentionally left outside overlay canon
  - which subset should gain tracked overlay carry later
  - which update/install surfaces are currently under-explained by manifest + backup + snapshot together

## Why This Is Stronger

- [d:r:i] Better maintainability:
  - no single file is forced to lie about what it knows
- [d:r:i] Better update resilience:
  - updater semantics stay stable while runtime truth still becomes auditable
- [d:r:i] Better operator speed:
  - later intervention lanes can compare three explicit truth surfaces instead of reconstructing them from memory

## What This Rejects

- [d:r:i] Reject `manifest as runtime truth`.
- [d:r:i] Reject `backup meta as full coherence story`.
- [d:r:i] Reject coherence work that ignores selected-lane runtime snapshots once those snapshots are available.

## Immediate Next Move

- [g:r:i] Capture the first selected-lane runtime snapshot after the current checkpoint, then use that artifact as the first baseline input for the next manifest/install coherence pass.
