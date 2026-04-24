Date: 2026-04-22
Status: active bounded proposal

# Milestone-Boundary Uplift Shared-Reference First Slice Proposal

## Purpose

- [g:r:i] Open the next bounded `119` route after the landed transition/state continuity slice in `121`.
- [g:r:i] The target is not another direct per-workflow patch by itself.
- [g:r:i] The target is to carry held-runtime awareness through milestone open and milestone close by attaching both routes to one shared read-only reference instead of widening either route into write-side posture.

## Why This Proposal Opens Now

- [e:r:i] `119` already classifies the milestone-boundary pair as:
  - `attach through a shared reference`
  - surfacing direction: `read-only`
- [e:r:i] `121` now gives the family a top-level `Project Uplift` digest in `STATE.md`, helper-side fill-in-place behavior, and explicit preserve-versus-refresh handling at phase close.
- [e:r:i] `60` already gives milestone open and milestone close a stronger future-carry bridge through `LONG-ARC.md` and `Future Carry Forward`.
- [d:r:i] That means the next missing lift is narrower:
  - do not rediscover uplift posture at milestone boundaries from ambient memory
  - do not widen milestone boundaries into write-side compatibility dispatch
  - instead, attach the pair to one shared reference that tells them what to read, what to surface, and what to keep held

## Current Boundary

- [d:r:i] The relevant milestone-boundary carriers already exist:
  - [tooling/portable-gsd/overlay/get-shit-done/workflows/new-milestone.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/new-milestone.md)
  - [tooling/portable-gsd/overlay/get-shit-done/workflows/complete-milestone.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/workflows/complete-milestone.md)
- [d:r:i] The relevant uplift continuity carriers now already exist too:
  - [tooling/portable-gsd/overlay/get-shit-done/templates/state.md](/home/rookslog/workspace/projects/prix-guesser/tooling/portable-gsd/overlay/get-shit-done/templates/state.md)
  - [tooling/codex/project_uplift.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/project_uplift.py)
  - [.planning/UPLIFT-REPORT.md](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-REPORT.md)
  - [.planning/UPLIFT-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-MANIFEST.json)
- [d:r:i] What is still missing is the explicit boundary-reader that tells milestone open and milestone close:
  - the `Project Uplift` digest is the first compact read
  - `UPLIFT-REPORT.md` is the next narrative read when the boundary needs more context
  - `UPLIFT-MANIFEST.json` is the typed detail surface when the route hits real basis or annotation ambiguity
  - none of that widens the milestone boundary into matrix claims, parity claims, or inline write-side dispatch

## Proposed First Slice

- [d:r:i] Add one dedicated shared reference under the repo-local GSD references layer for milestone-boundary uplift continuity:
  - `tooling/portable-gsd/overlay/get-shit-done/references/milestone-boundary-uplift-continuity.md`
- [d:r:i] Materialize that reference into live `.codex` through an explicit `add` entry in:
  - `tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json`
- [d:r:i] Teach both `new-milestone.md` and `complete-milestone.md` to read that shared reference as part of their boundary packet rather than inventing separate uplift prose in each workflow.
- [d:r:i] Keep the shared reference read-only in character:
  - milestone open should surface uplift posture only when the reference's boundary triggers say it belongs in frame
  - milestone close should keep uplift posture visible only when the same kind of bounded trigger says it belongs in closure carry
  - neither route becomes the place that runs `$gsd-uplift-project --write` by default

## Shared-Reference Placement

- [d:r:i] This slice uses a dedicated new reference instead of widening `mandatory-initial-read.md`.
- [d:r:i] Reason:
  - `mandatory-initial-read.md` owns read-packet grammar
  - this new reference owns milestone-boundary uplift content
- [d:r:i] The new reference should use that existing grammar without re-teaching it.
- [d:r:i] That keeps:
  - packet discipline in the existing shared read-control reference
  - milestone-boundary uplift continuity in its own topic-specific carrier

## Shared-Reference Shape

- [d:r:i] The shared reference should define:
  - `Primary Compact Read`
    - always consult `STATE.md` top-level `Project Uplift` when the boundary surfaces uplift continuity at all
  - `Supporting Narrative Read`
    - widen into `.planning/UPLIFT-REPORT.md` when the compact digest does not carry enough operator-facing context
  - `Deeper Typed Read`
    - widen into `.planning/UPLIFT-MANIFEST.json` only when basis or annotation ambiguity remains after the first two reads
  - `Interpretation Frame`
    - `compatibility_posture: observed_basis_only` remains the top-level posture
    - held runtime annotation is visible but still distinct from dual-basis relabel
    - milestone boundaries may surface posture
    - milestone boundaries do not convert posture into parity, translation, matrix, or version-window claims
  - `When To Surface`
    - milestone-open triggers
    - milestone-close triggers
- [d:r:i] The reference should stay narrower than a second uplift manifest.
- [d:r:i] Minimum content floor:
  - `Primary Compact Read`
  - `Supporting Narrative Read`
  - `Deeper Typed Read`
  - `Interpretation Frame`
  - `When To Surface`
- [d:r:i] The reference should keep read-only voice explicit:
  - it tells the boundary what to read and how to interpret it
  - it does not tell the boundary to run helper commands
- [d:r:i] Milestone-open trigger list should include:
  - observed runtime basis moved since the last milestone
  - `pending_doctrine_sensitive_proposals` count is greater than zero
  - a `held_later_families` partial landing is relevant to the next milestone's target scope
  - `phase_boundary_signal.mid_phase_signal` changes what should enter the milestone-opening packet
- [d:r:i] Milestone-close trigger list should include:
  - the milestone moved observed runtime basis
  - seed corpus posture changed during the milestone
  - `held_later_families` gained or closed partial-landing entries during the milestone
  - doctrine-sensitive carrier posture changed during the milestone's phases
- [d:r:i] Relationship notes should stay explicit:
  - this reference adds uplift continuity beside `60`'s long-arc / future-carry reread
  - this reference reads the `Project Uplift` block produced and preserved by `121`'s transition-side continuity route; it does not absorb that route into milestone boundaries

## Workflow Follow-Through Intended By This Proposal

- [d:r:i] `new-milestone.md`
  - already carries `required`, `supporting`, and `deeper` reading blocks
  - add the new uplift reference to the `required_reading` block beside the existing `mandatory-initial-read.md` pointer
  - consult the new reference's milestone-open triggers before shaping the milestone-opening packet
  - keep the boundary read-only rather than turning milestone open into an uplift-write checkpoint
- [d:r:i] `complete-milestone.md`
  - currently carries only a `required_reading` block and does not yet point at `mandatory-initial-read.md`
  - add the new uplift reference to that existing `required_reading` block
  - consult the new reference's milestone-close triggers beside the existing future-carry and long-arc review
  - keep the boundary read-only rather than turning milestone close into a compatibility-dispatch route
- [d:r:i] This slice does not silently answer the broader read-packet question for `complete-milestone.md`:
  - whether it should later adopt `mandatory-initial-read.md` plus `supporting` / `deeper` grammar remains a separate later-family question

## Why This Route Before `health.md`

- [d:r:i] This route intensifies two lifecycle boundaries at once instead of one repair-facing carrier.
- [d:r:i] This route composes directly with already-landed milestone-boundary lifecycle carry from `60` and transition/state continuity from `121`.
- [d:r:i] `health.md` remains a real next route, but it is narrower:
  - structural-health and later posture separation already travel there
  - the milestone-boundary pair broadens carry across entry and closure together

## What This Proposal Does Not Authorize

- [d:r:i] No write-recommending milestone-boundary dispatcher.
- [d:r:i] No compatibility matrix or version-window claims.
- [d:r:i] No `.claude` parity or route-translation claim.
- [d:r:i] No structural-row promotion inside milestone workflow output.
- [d:r:i] No widening of `health.md` through this slice.
- [d:r:i] No cross-repo extraction or npm/`npx` work through this family.
- [d:r:i] No silent adoption of `mandatory-initial-read.md` into `complete-milestone.md` through this slice.
- [d:r:i] No third-runtime held-annotation widening through this reference.
- [d:r:i] No widening of milestone outputs such as `MILESTONES.md`, archived roadmap/requirements, or retrospective surfaces through this slice.

## Verification Gates

- [d:r:i] The shared reference must stay narrower than a second uplift manifest.
- [d:r:i] Both milestone workflows must point to the same reference rather than drifting into two separate local doctrines.
- [d:r:i] The landed slice must survive repo-local rematerialization through tracked overlay carry.
- [d:r:i] The landed slice should leave one explicit propagation refresh and one governance-trace note rather than only mutating workflow prose.
- [d:r:i] The propagation refresh should land as a compatibility-family sibling to `44`, not as backfill into lifecycle-carry `22`.
- [d:r:i] The governance trace should land in two places:
  - one entry-uplift disposition / inheritance note
  - one intervention-proposals implementation note

## Held Later

- [d:r:i] `health.md` deepen-in-place route remains explicit as the next adjacent single-carrier alternative after this proposal.
- [d:r:i] Wider family-6 route asymmetry remains parallelizable rather than absorbed here.
- [d:r:i] Compatibility-anchor structural-row, typed standalone carrier, translation posture, and extraction/distribution all remain later-family questions.
- [d:r:i] Whether `complete-milestone.md` later adopts `mandatory-initial-read.md` plus full `supporting` / `deeper` packet grammar remains a separate later-family question.
- [d:r:i] Third-runtime annotation widening remains later-family work.
- [d:r:i] Structural-row promotion into milestone or retrospective outputs remains later-family work.

## Current Consequence

- [d:r:i] The next `119` choice is now no longer ambient.
- [d:r:i] The active next object is:
  - milestone-boundary uplift shared-reference first
- [d:r:i] The held adjacent route remains:
  - `health.md` deepen-in-place follow-through
