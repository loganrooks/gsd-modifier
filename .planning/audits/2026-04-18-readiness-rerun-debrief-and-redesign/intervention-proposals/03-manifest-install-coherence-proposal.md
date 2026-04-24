Date: 2026-04-20
Status: draft bounded proposal

# Manifest Install Coherence Proposal

## Purpose

- [g:r:i] This proposal defines a bounded follow-through candidate for the current manifest/install trust gap: the harness already exposes version and hash inventory surfaces, but they are not yet trustworthy enough to stand in for effective materialization truth after repo-local carry is applied.

## Why This Proposal Exists

- [e:c+i] The update lane established the concrete problem: the active repo-local runtime was semantically aligned with a fresh reinstall plus overlay, yet `gsd-file-manifest.json` still carried stale hashes relative to the actual materialized state. Sources: [HARNESS-INTERVENTION-UPDATE-LANE.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/harness-interventions/HARNESS-INTERVENTION-UPDATE-LANE.md:28), [HARNESS-INTERVENTION-UPDATE-LANE.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/harness-interventions/HARNESS-INTERVENTION-UPDATE-LANE.md:29), [HARNESS-INTERVENTION-UPDATE-LANE.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/harness-interventions/HARNESS-INTERVENTION-UPDATE-LANE.md:31), [HARNESS-INTERVENTION-UPDATE-LANE.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/harness-interventions/HARNESS-INTERVENTION-UPDATE-LANE.md:32).
- [e:c+i] The runtime/materialization companion then narrowed the lesson: the manifest and backup metadata are useful, but neither is sovereign proof of current effective runtime truth. Sources: [RUNTIME-MATERIALIZATION-AND-AUTHORITY.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/governance/RUNTIME-MATERIALIZATION-AND-AUTHORITY.md:65), [RUNTIME-MATERIALIZATION-AND-AUTHORITY.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/governance/RUNTIME-MATERIALIZATION-AND-AUTHORITY.md:68), [RUNTIME-MATERIALIZATION-AND-AUTHORITY.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/governance/RUNTIME-MATERIALIZATION-AND-AUTHORITY.md:69), [GOAL-TO-SURFACE-INTERVENTION-INDEX.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/indexes/GOAL-TO-SURFACE-INTERVENTION-INDEX.md:24), [GOAL-TO-SURFACE-INTERVENTION-INDEX.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/indexes/GOAL-TO-SURFACE-INTERVENTION-INDEX.md:45).

## Bounded Scope

- [d:r:i] Limit the first pass to the existing repo-local install path:
  - `scripts/setup-portable-gsd.sh`
  - `.codex/gsd-file-manifest.json`
  - `.codex/gsd-local-patches/backup-meta.json`
- [d:r:i] Do not widen this first pass into a whole-package updater or a broad upstream repackaging effort.

## Proposed Move

### 1. Decide What The Manifest Is Supposed To Mean

- [d:r:i] Pick one of two explicit semantics and enforce it consistently:
  - `base+overlay snapshot`
  - `final materialized runtime snapshot`
- [d:r:i] The current problem is not only stale data. It is that the manifest’s semantic status is under-specified relative to the actual three-stage materialization chain.

### 2. Make The Install Path Honor That Meaning

- [d:r:i] After the installer finishes upstream install, overlay copy, and post-copy mutation, regenerate or refresh the manifest so it matches the chosen semantic target.
- [d:r:i] If backup metadata remains subset-only by design, keep it explicit rather than letting later readers confuse it with the full intervention inventory.

### 3. Add One Coherence Check

- [d:r:i] Add a bounded check that can answer:
  - did install/materialization finish?
  - does the manifest match the meaning we claim for it?
  - if not, where did divergence occur?
- [d:r:i] This can be a local verification command or script, not a sprawling automation framework.

## Explicit Non-Goals

- [d:r:i] Do not pretend the manifest can replace semantic inspection of live runtime behavior.
- [d:r:i] Do not expand this proposal into a full update/upgrade manager.
- [d:r:i] Do not rewrite the whole portable-GSD install flow before the semantic target is chosen.

## Why This Bounded Shape Is Stronger

- [d:r:i] It turns a vague “manifest seems stale” complaint into a concrete truth-contract question.
- [d:r:i] It improves trust in install/materialization traces without conflating hash inventory with behavior.
- [d:r:i] It supports later drift-visibility work rather than trying to absorb all drift questions by itself.

## Success Signals

- [d:r:i] A later reinstall can explain what the manifest does and does not prove.
- [d:r:i] Hash drift stops appearing unexpectedly after normal repo-local materialization.
- [d:r:i] Reviewers can tell whether a mismatch is an install bug, a local carry, or an intentional semantic boundary.

## Ceremony Risk Check

- [d:r:i] This proposal fails if it only produces a prettier manifest while leaving its meaning ambiguous.
- [d:r:i] It also fails if it grows into a heavyweight package-management layer without first solving the narrower trust-contract problem.

## Next Disposition Question

- [g:r:i] The next decision on this proposal should be whether to accept a narrow manifest-semantic cleanup pass now, revise the target meaning/check, or hold it behind some other precondition.
