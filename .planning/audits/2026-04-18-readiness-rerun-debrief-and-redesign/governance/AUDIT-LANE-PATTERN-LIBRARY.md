Date: 2026-04-21
Status: active audit-program infrastructure surface

# Audit Lane Pattern Library

## Purpose

- [g:r:i] This note records the recurring lane structure that now spans multiple audit families in this workspace.
- [d:r:i] It is not a demand that every lane instantiate every possible artifact.
- [d:r:i] Its job is to make recurring audit structure explicit so later lanes can reuse a cleaner pattern instead of rebuilding scaffold from memory or chat.

## Core Lane Objects

### Opening note

- [g:r:i] Use when a family or lane needs a bounded local starting object before packeting or review.
- [d:r:i] It should name:
  - the family
  - the local question
  - scope
  - non-goals
  - why this lane exists now instead of later
- [d:r:i] When the lane is parallelization-adjacent, add one lane-local declaration block on the face of the opening note:
  - frozen basis
  - authority surface
  - companion-safe carry
  - must-wait set
  - recheck window

### Packet

- [g:r:i] Use when the reviewer should not infer the read set from repo shape alone.
- [d:r:i] The packet should carry:
  - exact read set
  - explicit absolute paths for external or sibling-repo docs when those matter
  - anti-misread framing
  - what the lane should not silently widen into
- [d:r:i] When the lane is parallelization-adjacent, preserve the same declaration shape inside the packet too:
  - frozen basis
  - read set
  - authority surface
  - companion-safe carry
  - must-wait set
  - recheck window

### Spec

- [g:r:i] The spec owns the governing question and output shape.
- [d:r:i] It should state:
  - what the lane is being asked to map, challenge, or refine
  - what collapse or narrowing it must avoid
  - what output shape later inheritance needs

### Prompt

- [g:r:i] The prompt is the launch surface, not the source of truth for the lane contract.
- [d:r:i] It should remain consistent with the packet and spec rather than improvising new scope.

### Launch-truth note

- [g:r:i] Preserve requested versus effective launch settings whenever external review or spawned review materially steers later inheritance.
- [d:r:i] The note should preserve:
  - basis commit or other frozen boundary
  - packet/spec/prompt paths
  - requested model settings
  - effective model settings
  - estimated wall-clock time or bounded runtime range before launch
  - actual elapsed wall-clock time after completion
  - one short calibration note comparing estimate versus actual so later launches can inherit a less naive timing expectation
  - any discovered mismatch and how it was handled
- [d:r:i] Preserve one of two launch-truth shapes explicitly rather than blurring them:
  - `launch-truth-lite`:
    - packet/spec/prompt paths
    - frozen basis
    - requested settings
    - timing expectation and actual outcome
    - output path
    - reviewer-state classification when relevant (`complete` / `partial` / `absent`)
  - full requested-versus-effective capture:
    - the `launch-truth-lite` fields above
    - plus the requested/effective runtime fields preserved through `capture_launch_truth.py` or an equivalent stronger carrier
- [d:r:i] Do not let a lane silently downgrade from full capture to `launch-truth-lite`; name the lighter shape directly when that is all the runner can honestly preserve.
- [d:r:i] For cross-vendor Claude / Opus lanes launched through `run_claude_probe.py`, prefer `opus[1m]` with `xhigh` as the default high-reasoning setting.
- [d:r:i] Reserve `max` for particularly thinking-heavy rereads or adjudication lanes whose read set, comparison burden, or synthesis density materially exceeds the ordinary bounded lane.
- [d:r:i] When `max` is chosen, the launch-truth note should state why the heavier setting was earned instead of leaving it as implied custom.

### Timing estimate

- [g:r:i] For every substantial external lane or delegated bounded job, preserve an explicit timing expectation before launch instead of treating wait behavior as ambient intuition.
- [d:r:i] The estimate may be:
  - one expected duration
  - or one bounded range when the frontier is still uncertain
- [d:r:i] The estimate should reflect the real lane shape:
  - read-set size
  - model/reasoning choice
  - whether the lane is widening, bounded reread, or implementation review
  - whether the output is expected to be short, medium, or long
- [d:r:i] After completion, compare actual elapsed time to the estimate and record one brief calibration note:
  - `shorter than expected because ...`
  - `roughly matched because ...`
  - `longer than expected because ...`
- [d:r:i] The task is not perfect prediction.
- [d:r:i] The task is to build a less naive local runtime model over repeated lanes.
- [d:r:i] When the lane is review-family or helper-backed review work, cross-reference the helper-backed run-home case rather than reconstructing timing expectations from chat memory:
  - [intervention-proposals/145-gsd-review-helper-backed-run-home-first-slice-implementation.md](../intervention-proposals/145-gsd-review-helper-backed-run-home-first-slice-implementation.md)
  - [propagation-audit/53-review-route-helper-backed-run-home-first-slice-change-triggered-refresh.md](../propagation-audit/53-review-route-helper-backed-run-home-first-slice-change-triggered-refresh.md)

## Bounded Parallelization And Overlap

- [g:r:i] Treat parallelization as bounded overlap discipline, not as generic appetite for more moving parts.
- [d:r:i] Earned patterns:
  - external-lane overlap:
    - while one long-running external lane reads a frozen basis, land unrelated propagation refreshes, subtree-status updates, launch-ledger housekeeping, or other bounded governance carry that does not touch the lane basis
  - narrower delegated work with parent-thread composition ownership:
    - use sub-agents for bounded classification, packet assembly, or gap-identification work while the parent thread keeps composition-layer judgment and inheritance
  - change-triggered refresh cadence:
    - let mechanical refresh notes travel alongside landed slices instead of waiting for one giant catch-up pass
  - bounded reread on a frozen landed slice:
    - launch one narrow challenge lane against a coherent checkpoint while adjacent unrelated families continue
- [d:r:i] Forbidden overlaps:
  - editing the packet, spec, prompt, or core governed basis a live lane is currently reading
  - changing governance-role surfaces during a live lane when the lane depends on those role definitions
  - refmap or topology rewrites that could invalidate the lane's frozen basis or artifact paths
  - crossing a larger program boundary, especially the Phase 01 rerun boundary, while a lane is still returning on the prior governed baseline
- [d:r:i] Companion carry during a live external lane:
  - unrelated propagation change-triggered refreshes
  - subtree-status or README force updates for other families
  - launch-ledger and launch-truth housekeeping on earlier completed lanes
  - durable-register updates when a family's state shifts independently of the live lane
  - bounded verification or artifact-hygiene cleanup that does not touch the lane basis
- [d:r:i] Recheck rule:
  - use the timing estimate above as the first recheck window
  - if companion carry finishes before that window, check the lane rather than idling on user reply
  - if there is nothing safe and useful left to do, wait on the lane instead of manufacturing filler work
- [d:r:i] Read this section together with `Timing estimate`; one governs when to check, the other governs what can safely travel while waiting.

### Parent-thread retention

- [g:r:i] Parent-thread retention is the default when delegated or overlapping work is used inside harness-modifier development.
- [d:r:i] The parent thread keeps ownership of:
  - disposition authority
  - governance carry
  - propagation carry
  - checkpoint boundaries
  - inheritance writing

### Sub-agent earned work

- [g:r:i] Use sub-agents only for bounded work that sharpens the slice without displacing composition ownership.
- [d:r:i] Earned categories include:
  - bounded classification
  - packet assembly
  - gap identification
  - focused audit reads
  - focused implementation slices with a clean write boundary
  - bounded verification / review against intended effects and propagation obligations
- [d:r:i] If a verifier or reviewer is launched, keep its role explicit:
  - what slice it is checking
  - what it is not authorized to widen into
  - what artifact should preserve its return

### Output

- [g:r:i] Preserve reviewer output as output, not as already-adopted doctrine.
- [d:r:i] Do not rewrite the output to sound more aligned with local preference.

### Inheritance / disposition

- [g:r:i] This is the point where local force is assigned.
- [d:r:i] It should record:
  - what is carried forward
  - what is held later
  - what is not adopted
  - what concrete next move follows

### Comparative disposition

- [g:r:i] Use only when multiple lanes materially diverge or when the comparative view is itself a durable object.
- [d:r:i] Do not force a comparative layer when one lane is clearly secondary or merely corroborative.

### Frozen artifacts

- [g:r:i] Use when the lane yields a bounded structured output that later work should compare against.
- [d:r:i] Examples already used in this workspace:
  - runtime snapshots
  - canary reports
  - propagation registry layers

## Common Lane Shapes

### Widening lane

- [d:r:i] Best when the current terrain is still undernamed.
- [d:r:i] Preferred shape:
  - opening note
  - packet
  - spec
  - prompt
  - launch-truth
  - output
  - inheritance

### Bounded reread or challenge lane

- [d:r:i] Best when a concrete local artifact already exists and the task is to widen, sharpen, or qualify it.
- [d:r:i] Preferred shape:
  - packet or tightly scoped read set
  - spec
  - prompt
  - launch-truth
  - output
  - inheritance

### Change-triggered refresh

- [d:r:i] Best when a real contract-moving slice already landed and a family map or registry should reflect the new state.
- [d:r:i] Preferred shape:
  - refresh note
  - refreshed artifact
  - governance routing update
- [d:r:i] Do not overbuild packet/spec/prompt scaffolding if no external lane is actually being launched.

### Implementation reread

- [d:r:i] Best when a landed slice needs one more adversarial read before further widening.
- [d:r:i] Preferred shape:
  - frozen basis note
  - narrow reread packet/spec/prompt
  - launch-truth
  - output
  - inheritance

## Review And Quality Discipline

- [g:r:i] Prefer a coherent baseline before a substantial lane or bounded edit batch.
- [d:r:i] Preserve launch truth when the lane materially matters.
- [d:r:i] Preserve timing expectation and post-run comparison when the lane materially matters.
- [d:r:i] Preserve explicit inheritance before treating output as live doctrine.
- [d:r:i] Keep contextual reread sovereign over heuristic scanner quieting.
- [d:r:i] Use audit/program verification surfaces that fit the slice:
  - `audit_refmap.py verify` for audit-link integrity
  - helper-specific tests for tooling slices
  - runtime/install gates like `harness_canary.py` only when the slice actually changes those families

## Intervention Lifecycle

- [g:r:i] Treat intervention work as a repeated loop, not as one local patch plus ambient memory.
- [d:r:i] The minimal lifecycle declaration on proposal, implementation, or inheritance surfaces should carry:
  - `Intended Effects`
  - `Propagation Obligations`
  - `Monitor Target`
  - disposition-verb close (`accept` / `revise` / `park` / `reject`)
- [d:r:i] When a slice's effects are not self-evident from the landed diff alone, schedule one bounded verification or review task rather than leaving proof implicit.
- [d:r:i] Prefer reusable verification shape over one-off prompt reinvention:
  - intended-effects check
  - propagation-obligation check
  - mismatch / under-carry check
  - whether a periodic big-picture review gate is now due

## Anti-Patterns

- [d:r:i] orphaned outputs with no inheritance note
- [d:r:i] lane outputs treated as canon without explicit absorption
- [d:r:i] repeated recreation of the same packet/spec/prompt logic with no reusable local reference
- [d:r:i] forcing full lane scaffolding onto a local change-triggered refresh that does not need it
- [d:r:i] letting one family's packet, prompt, or launch-truth conventions survive only as chat memory

## Current Local Consequence

- [d:r:i] Later audit families in this workspace should treat this note as the default reusable lane pattern surface.
- [d:r:i] This note does not replace family-specific judgment; it reduces repeated scaffold rediscovery.
