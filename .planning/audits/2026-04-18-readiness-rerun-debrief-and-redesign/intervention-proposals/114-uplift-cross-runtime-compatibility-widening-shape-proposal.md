Date: 2026-04-22
Status: active bounded proposal

# Uplift Cross-Runtime Compatibility Widening Shape Proposal

## Purpose

- [g:r:i] Open the next bounded cross-runtime proposal after the completed concern-family split lane.
- [g:r:i] The target is not a live compatibility-matrix claim, not `.claude` translation, and not a composition judgment.
- [g:r:i] The target is to choose how the existing uplift-side compatibility anchor should widen, if at all.

## Why This Proposal Opens First

- [e:c+i] The concern-family split lane recommends `compatibility-family widening shape` as the first bounded proposal because it is already a decision surface rather than another field-discovery surface. Source:
  - [entry-uplift-audit/outputs/12-uplift-cross-runtime-concern-family-split-opus47-max-r1.md](../entry-uplift-audit/outputs/12-uplift-cross-runtime-concern-family-split-opus47-max-r1.md)
- [d:r:i] The current compatibility anchor already has one durable home:
  - [.planning/UPLIFT-REPORT.md](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-REPORT.md)
  - [.planning/UPLIFT-MANIFEST.json](/home/rookslog/workspace/projects/prix-guesser/.planning/UPLIFT-MANIFEST.json)
  - the `Project Uplift` section in [.planning/STATE.md](/home/rookslog/workspace/projects/prix-guesser/.planning/STATE.md)
- [d:r:i] The current shape choice also gates where `consumer-chain asymmetry` can later live. Opening the shape proposal first keeps that downstream family from being forced into the wrong home too early.

## Current Anchor Posture

- [e:c+i] The current compatibility anchor posture is `observed_basis_only`, with `.codex` as the observed runtime basis and broader cross-runtime compatibility still held. Source:
  - [43-project-uplift-compatibility-anchor-slice.md](43-project-uplift-compatibility-anchor-slice.md)
- [d:r:i] The current anchor therefore carries real observed `.codex` basis, but still leaves `.claude` mostly in prose and audit surfaces rather than in the durable anchor itself.

## Observed Cross-Runtime Gap

- [e:c+i] The current observed runtime versions are not the same:
  - `.codex/get-shit-done/VERSION` = `1.38.3`
  - `.claude/get-shit-done/VERSION` = `1.34.2`
  Sources:
  - [.codex/get-shit-done/VERSION](/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/VERSION)
  - [.claude/get-shit-done/VERSION](/home/rookslog/workspace/projects/prix-guesser/.claude/get-shit-done/VERSION)
- [d:r:i] That version gap is the motivating concrete for this widening route. The current question is how that gap should become more durable inside the compatibility anchor family without relabeling the whole posture too early.

## Candidate Shapes

### 1. Annotation Posture

- [d:r:i] Keep `observed_basis_only` as the anchor posture.
- [d:r:i] Annotation posture now has two visible sub-shapes:
  - held-scalar annotation:
    - add one explicit held `.claude` version / posture note beside the existing anchor without introducing a structurally parallel runtime row
  - structural-row annotation:
    - add one explicit held `.claude` runtime row inside the anchor while still preserving `compatibility_posture: observed_basis_only`
- [d:r:i] Both sub-shapes widen the anchor without changing the top-level posture label.

### 2. Dual-Basis Posture

- [d:r:i] Widen the anchor so both `.codex` and `.claude` sit inside one observed-basis surface.
- [d:r:i] The main distinction here is posture-label discipline:
  - this shape would tend to relabel the top-level anchor away from `observed_basis_only`
  - that relabeling travels farther than annotation posture even if the raw facts carried inside the anchor stay bounded

### 3. Typed Multi-Runtime Carrier

- [d:r:i] Leave the current uplift-side anchor narrow and open a separate typed carrier for multi-runtime compatibility.
- [d:r:i] This shape gives the most structural separation, but it depends more heavily on the wider route-asymmetry field that family-6 mapping still needs to disclose farther.
- [d:r:i] So the hold here is not a general reluctance to add structure. The hold is that this shape wants information the current family-10 route does not yet carry by itself.

## Recommended Shape

- [d:r:i] Recommend **annotation posture** as the next bounded move.
- [d:r:i] Within annotation posture, the proposal should keep the held-scalar versus structural-row split explicit until the implementation slice either:
  - chooses one directly
  - or inherits a named rule for choosing between them

## Why Annotation Posture First

- [d:r:i] It keeps the current `.codex` observed-basis anchor honest instead of widening it faster than the present carrier field warrants.
- [d:r:i] It makes the currently live `.claude` version and posture difference durable inside the existing anchor family rather than leaving them only in packet/reread prose.
- [d:r:i] It gives the next family, `consumer-chain asymmetry`, a reachable home inside the current anchor family without forcing a new carrier family or a posture relabel first.
- [d:r:i] It preserves `compatibility_posture: observed_basis_only`, so the top-level label keeps reflecting the current observed `.codex` basis even while `.claude` becomes more explicit inside the same family.
- [d:r:i] It keeps the typed-carrier route held until family-6 mapping carries farther rather than making that route decide too early on a thinner field.
- [d:r:i] It leaves family-6 mapping parallelizable rather than blocked. The family-10 shape choice and the wider family-6 field do not collide.

## What This Proposal Does Not Authorize

- [d:r:i] No live edit to `.planning/UPLIFT-REPORT.md`, `.planning/UPLIFT-MANIFEST.json`, or `.planning/STATE.md` yet.
- [d:r:i] No compatibility-matrix claim.
- [d:r:i] No `.claude` route translation.
- [d:r:i] No cross-runtime composition judgment.
- [d:r:i] No change to `$gsd-propagation-review`.

## Verification Gates

- [d:r:i] The chosen shape must stay family-by-family rather than widening into parity appetite.
- [d:r:i] The chosen shape must preserve the current observed-basis discipline around `.codex` even if `.claude` becomes more visible.
- [d:r:i] The chosen shape must preserve the top-level anchor label:
  - `compatibility_posture: observed_basis_only`
- [d:r:i] The chosen shape must make the next family opening for `consumer-chain asymmetry` cleaner rather than blurrier.
- [d:r:i] The proposal should remain narrow enough that a later implementation slice can update the existing compatibility anchor without also forcing matrix work or translation work.
- [d:r:i] The proposal should keep the operator-facing `progress` / `resume-project` asymmetry explicit:
  - annotation widening would become durable in uplift outputs first
  - consumer-chain carry across later surfaces still opens as its own downstream family

## Current Consequence

- [d:r:i] The cross-runtime uplift family now has a concrete next bounded proposal instead of only a wider audit result.
- [d:r:i] If this proposal is accepted, the next move after it should be one small implementation slice on the existing compatibility anchor surfaces, followed by the bounded `consumer-chain asymmetry` proposal it unblocks.
- [d:r:i] Family-6 wider route-asymmetry mapping can still open in parallel if the parent thread decides that the field should widen while the annotation route narrows.

## Implementation-Slice Choice Held Explicitly

- [d:r:i] The later implementation slice should name one helper-side choice in [tooling/codex/project_uplift.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/project_uplift.py):
  - a narrow `.claude`-specific addition beside the current `.codex`-only compatibility reader
  - or a more general runtime-dir reader that still preserves `compatibility_posture: observed_basis_only`
- [d:r:i] That choice belongs to the implementation slice, not to this proposal-only note.
