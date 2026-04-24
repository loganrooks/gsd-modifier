# Lane 04 Surface D Proposal: High-Force Local Carrier Legibility

Status: draft bounded local proposal  
Date: 2026-04-19  
Target surfaces:
- [.codex/get-shit-done/templates/context.md](../../../../.codex/get-shit-done/templates/context.md)
- [.codex/get-shit-done/workflows/discuss-phase.md](../../../../.codex/get-shit-done/workflows/discuss-phase.md)

## Proposal Judgment

- [d:c+i] A bounded Surface D proposal is earned now, but only for high-force planning carriers and only as a narrow pilotable supplement. Sources: .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/lane-reviews/lane-04-comparative-disposition.md:32, .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/lane-reviews/lane-04-comparative-disposition.md:43-44, .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/lane-reviews/lane-04-gpt54-xhigh-carriage-and-operationalization-review.md:174-185, .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/lane-reviews/lane-04-opus47-max-carriage-and-operationalization-review.md:327-339.
- [d:r:i] This proposal treats Opus's `disposition:` logic as one candidate implementation, but not as an already-authorized template-wide rule.

## Problem This Proposal Targets

- [d:c+i] The current `context.md` template preserves `Open Questions`, `Future Awareness`, and `Deferred Ideas`, but it does not currently force wake logic or state-change discipline for the subset of items that can materially steer later planning. Sources: .codex/get-shit-done/templates/context.md:66-73, .codex/get-shit-done/templates/context.md:126-152.
- [d:c+i] The `discuss-phase.md` contract already says downstream planners and researchers should treat open questions and future-preservation seams as real steering inputs, but the template surface is still light enough that high-force items can remain generic or be carried by operator memory. Sources: .codex/get-shit-done/workflows/discuss-phase.md:15-31, .codex/get-shit-done/workflows/discuss-phase.md:50-57.
- [d:r:i] The gap is not lack of future-oriented language. The gap is lack of concrete wake conditions, affected decision surfaces, and explicit state-change discipline for the small subset of items that are too load-bearing to remain generic.

## Pilot Boundary

- [d:r:i] The pilot applies only to high-stakes steering items.
- [d:r:i] It should not be used for every open question or every deferred idea.
- [d:r:i] An item qualifies only if at least one of the following is true:
  - silence would likely harden a future seam into a de facto decision
  - the item is likely to resurface across phases
  - the item can materially change research sequencing, planning sequence, or adoption posture
- [d:r:i] No repo-wide workflow rewrite is authorized by this proposal.

## Proposed Supplement Shape

- [d:r:i] Keep the existing `Open Questions` section.
- [d:r:i] For qualifying high-force items only, allow an optional compact mini-format inside `Open Questions` or `Deferred Ideas`.
- [d:r:i] Update the `discuss-phase.md` write step only enough to tell the writer to surface the high-force supplement when such items exist.

### Candidate Fragment

```markdown
### High-Force Inquiry Entry
- Question:
- Current disposition: act now | open inquiry | defer with updated trigger | retire
- Current trigger:
- Updated trigger:
- Affected decision surface:
- Next wake point:
```

### Candidate Use Rule

```markdown
Use the high-force inquiry entry only when an unresolved item is likely to:
- reshape the current phase's research or planning sequence
- resurface across phases
- or silently settle a future seam if left generic
```

## Why This Is Narrower Than The Stronger Opus Move

- [d:c+i] Opus's strongest Surface D move was a required `disposition:` field per `<open_questions>` entry. GPT-5.4 argued for a narrower high-force supplement. The comparative disposition accepted the narrower GPT starting point. Sources: .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/lane-reviews/lane-04-opus47-max-carriage-and-operationalization-review.md:327-339, .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/lane-reviews/lane-04-gpt54-xhigh-carriage-and-operationalization-review.md:176-185, .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/lane-reviews/lane-04-comparative-disposition.md:43-44.
- [d:r:i] This proposal therefore does not assume every open question needs a disposition field. It assumes only that some high-force items do.

## Expected Treatment Change

- [d:r:i] A planner or researcher should be able to tell which unresolved items must change current treatment, which are intentionally deferred, and what event should wake them.
- [d:r:i] At least one high-force item in a pilot phase should be routed by the carrier itself rather than by operator recall.
- [d:r:i] Future-awareness constraints should become more answerable: they should have a concrete relation to an affected decision surface rather than remaining generic caution prose.

## Anti-Ceremony Criteria

- [d:r:i] Success:
  - one or more high-force items change downstream research or planning output because the supplement made the wake logic explicit
  - at least one item resurfaces through the documented trigger rather than through memory alone
  - the supplement remains selective rather than spreading to all open questions
- [d:r:i] Failure:
  - entries are filled formulaically with no plan or research consequence
  - every open question receives the supplement, producing reminder noise
  - the same downstream treatment would have happened without the extra fields
  - the supplement becomes a disguised seriousness ladder rather than a routing aid

## Non-Goals

- [d:r:i] Not a wholesale rewrite of `context.md`
- [d:r:i] Not a repo-wide rewrite of wrapper workflows
- [d:r:i] Not a standing dependency-map or interrupt-infrastructure program
- [d:r:i] Not a mandate that every unresolved question be dispositioned

## Suggested Adoption Path

1. Review this proposal against the lane-04 comparative disposition and the current template/workflow surfaces.
2. If accepted, patch only the narrowest pilotable portion of `context.md` and the matching `discuss-phase.md` write guidance.
3. Pilot it on one phase with a maximum of two or three qualifying high-force items.
4. If the pilot does not change treatment, roll the supplement back rather than normalizing it.
