Date: 2026-04-20
Status: draft bounded proposal

# Live Vs Overlay Drift Visibility Proposal

## Purpose

- [g:r:i] This proposal defines a bounded follow-through candidate for the visibility gap between tracked overlay canon and the actual live runtime: important behavior can drift into the live `.codex/` tree, but that drift is not yet surfaced in a compact, reviewable way.

## Why This Proposal Exists

- [e:c+i] The topology and intervention onboarding work both made the same point: important behavior can live beyond the tracked overlay canon, especially in live workflow/helper surfaces and runtime-authoritative agent contracts. Sources: [HARNESS-INTERVENTION-ONBOARDING.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/harness-interventions/HARNESS-INTERVENTION-ONBOARDING.md:16), [HARNESS-INTERVENTION-ONBOARDING.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/harness-interventions/HARNESS-INTERVENTION-ONBOARDING.md:73), [RUNTIME-MATERIALIZATION-AND-AUTHORITY.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/governance/RUNTIME-MATERIALIZATION-AND-AUTHORITY.md:42), [RUNTIME-MATERIALIZATION-AND-AUTHORITY.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/governance/RUNTIME-MATERIALIZATION-AND-AUTHORITY.md:63).
- [e:c+i] The surface-status note now formalizes why this matters: overlay canon is a tracked persistence layer, but not the same thing as final live runtime truth. Sources: [SURFACE-STATUS-AND-DELTA.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/indexes/SURFACE-STATUS-AND-DELTA.md:22), [SURFACE-STATUS-AND-DELTA.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/indexes/SURFACE-STATUS-AND-DELTA.md:40), [SURFACE-STATUS-AND-DELTA.md](/home/rookslog/workspace/projects/gsd-modifier/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/indexes/SURFACE-STATUS-AND-DELTA.md:62).

## Bounded Scope

- [d:r:i] Limit the first pass to a small set of load-bearing families:
  - `.codex/config.toml`
  - `.codex/agents/*.toml`
  - `.codex/get-shit-done/workflows/*`
  - `.codex/get-shit-done/references/*`
  - `.codex/get-shit-done/bin/lib/*`
- [d:r:i] Do not try to build a total repo-wide diff portal before those families are legible.

## Proposed Move

### 1. Produce A Small Drift Register

- [d:r:i] Maintain a compact artifact that lists, for each in-scope family:
  - overlay-covered or not
  - known live drift or not
  - whether the drift is intentional, unknown, or obsolete
  - whether the drift has been carried back into overlay canon

### 2. Classify Drift, Don’t Just Detect It

- [d:r:i] Distinguish at least:
  - `intentional live carry`
  - `unknown live drift`
  - `overlay lag`
  - `obsolete live residue`
- [d:r:i] The goal is not just file mismatch detection. It is intervention-relevant classification.

### 3. Pair It With Fresh-Reinstall Comparison When Needed

- [d:r:i] For in-scope families that matter to a current intervention lane, compare against a fresh reinstall/probe when necessary instead of assuming the current live tree is self-explanatory.

## Explicit Non-Goals

- [d:r:i] Do not try to diff every file in `.codex/` at once.
- [d:r:i] Do not treat any diff as automatically bad; some live carry is intentional and load-bearing.
- [d:r:i] Do not build a complicated visualization layer before the drift classes themselves are stable.

## Why This Bounded Shape Is Stronger

- [d:r:i] It makes drift actionable instead of merely alarming.
- [d:r:i] It helps future update/intervention work decide whether to carry a change back into overlay, park it, or remove it.
- [d:r:i] It supports both persistence work and authority work without pretending they are the same proposal.

## Success Signals

- [d:r:i] Future intervention lanes can quickly see whether a surface is overlay-governed, live-carried, or ambiguously drifted.
- [d:r:i] Update probes stop rediscovering the same live-vs-overlay questions from scratch.
- [d:r:i] Reviewers can tell which drifts are intentional and which still need repair.

## Ceremony Risk Check

- [d:r:i] This proposal fails if it becomes a static mismatch spreadsheet no one uses to make decisions.
- [d:r:i] It also fails if it collapses all drift into one scary bucket and therefore encourages blunt cleanup instead of discriminating carry decisions.

## Next Disposition Question

- [g:r:i] The next decision on this proposal should be whether to accept a small drift-register pilot now, revise the family/scheme, or hold it behind another narrower prerequisite.
