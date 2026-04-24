# Lane 04 Surface A Proposal: Authority / Force Snapshot

Status: draft bounded local proposal  
Date: 2026-04-19  
Target surface: [WORKSPACE-AUTHORITY-AND-ORGANIZATION.md](../governance/WORKSPACE-AUTHORITY-AND-ORGANIZATION.md)

## Proposal Judgment

- [d:c+i] A bounded Surface A augmentation is earned now: add one compact authority / force snapshot to the workspace authority note, plus a short revisability clause with concrete reread triggers. Sources: .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/lane-reviews/lane-04-comparative-disposition.md:20, .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/lane-reviews/lane-04-comparative-disposition.md:38-39, .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/lane-reviews/lane-04-gpt54-xhigh-carriage-and-operationalization-review.md:160-172, .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/lane-reviews/lane-04-opus47-max-carriage-and-operationalization-review.md:307-323.
- [d:r:i] This proposal follows the compressed GPT-5.4 boundary, but imports the Opus reread-trigger pressure so the note does not become a silently inherited stable floor.

## Problem This Proposal Targets

- [d:c+i] The current authority note sharply distinguishes governing setup, briefing/procedural scaffolding, challenge inputs, inquiry corpus, and historical trail, but it still leaves some declared-versus-effective force relationships implicit. Sources: .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/governance/WORKSPACE-AUTHORITY-AND-ORGANIZATION.md:41-62, .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/governance/WORKSPACE-AUTHORITY-AND-ORGANIZATION.md:64-111, .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/governance/WORKSPACE-AUTHORITY-AND-ORGANIZATION.md:207-216.
- [d:r:i] In practice, later reviewers can still recover force from prose density, citation frequency, or operator memory rather than from one auditable register.
- [d:c+i] The highest-pressure example is `../planning-notes/SESSION-FRAMING-BRIEF.md`: the authority note correctly classifies it as briefing/procedural scaffolding, but lane/spec work has treated it as class-1-adjacent in framing disputes. Sources: .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/governance/WORKSPACE-AUTHORITY-AND-ORGANIZATION.md:66-85, .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/lane-reviews/lane-04-opus47-max-carriage-and-operationalization-review.md:309-315, .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/lane-reviews/lane-04-comparative-disposition.md:38-39.
- [d:r:i] The note also currently states the authority model, but does not yet name a concrete reread trigger. That makes revisability depend too much on vigilance and too little on explicit workspace procedure.

## Proposed Addition

- [d:r:i] Add a short section to `../governance/WORKSPACE-AUTHORITY-AND-ORGANIZATION.md` after `Authority Classes` and before `Read Discipline By Task`.
- [d:r:i] Add a short footer near the end of the note stating that the class map is a current routing hypothesis rather than a permanent floor.

### Proposed Fragment

```markdown
## Authority / Force Snapshot

Use this register when a file's declared class and its effective routing force are materially different, or when a later reviewer needs a compact answer to "why did this file matter here?"

- Artifact or class: `../planning-notes/SESSION-FRAMING-BRIEF.md`
  - Declared authority: briefing / procedural scaffolding
  - Effective authority: class-1-adjacent during spec writing and framing disputes
  - Sources of force: repeated citation in lane specs and dispositions; anti-tame framing pressure
  - Divergence risk: medium
  - Next local review consequence: if this artifact materially steers a lane contract, name that explicitly and test it against the governing setup spine rather than treating the brief as silent floor

- Artifact or class: `STATUS.md`
  - Declared authority: governing setup spine
  - Effective authority: governing for near-term sequencing, lower for substantive doctrine
  - Sources of force: next-step routing, mutable state, launch blocking
  - Divergence risk: low-to-medium
  - Next local review consequence: do not let mutable status language silently outrank `CURRENT-STATE.md`, `../planning-notes/QUESTION-SET.md`, or `../planning-notes/PLAN-PROPOSALS.md` on substantive questions

## Revisability Trigger

This authority map is a current routing hypothesis, not a stable floor.

Reread this note when:
- a new artifact class is added to this workspace
- a Class-2 artifact is cited in three or more specs, dispositions, or setup docs as steering authority
- an accepted proposal or stress-test result materially changes which files can route lane or phase choices
```

## Why This Is Bounded Rather Than A Rewrite

- [d:c+i] This proposal does not rewrite the five-class model. It annotates the existing model so later readers do not have to recover force indirectly. Sources: .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/lane-reviews/lane-04-opus47-max-carriage-and-operationalization-review.md:307-315, .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/lane-reviews/lane-04-gpt54-xhigh-carriage-and-operationalization-review.md:160-172.
- [d:r:i] It also avoids the stronger move of a scheduled reread cadence. The trigger is event-shaped, not calendar-shaped, so the note can be revisited when routing conditions actually change rather than on ceremonial schedule.

## Expected Treatment Change

- [d:r:i] Later setup reviewers should be able to identify when a briefing artifact is exerting class-1-adjacent force without re-deriving that from the full workspace history.
- [d:r:i] Future lane/spec writing should have a compact place to check whether a citation is leaning on declared authority, effective force, or both.
- [d:r:i] The workspace authority note should become harder to inherit as an unquestioned stable floor because the reread trigger makes map revision a named obligation.

## Anti-Ceremony Criteria

- [d:r:i] Success:
  - a later spec, disposition, or setup argument cites the snapshot directly instead of informally reconstructing artifact force
  - the reread trigger names at least one plausible future event cleanly enough that a reviewer could tell when it fired
  - a declared/effective divergence becomes more contestable rather than more mystical
- [d:r:i] Failure:
  - the snapshot merely repeats class labels already stated elsewhere
  - the reread trigger is so broad it fires constantly or so vague it never fires
  - later readers still need prose-density or memory to tell why a file mattered

## Non-Goals

- [d:r:i] Not a rewrite of the five-class authority model
- [d:r:i] Not a standing function/force field added to every artifact in the workspace
- [d:r:i] Not a scheduled maintenance program or authority-audit cadence

## Suggested Adoption Path

1. Review this proposal against the current authority note and current lane-04 comparative disposition.
2. If accepted, patch `../governance/WORKSPACE-AUTHORITY-AND-ORGANIZATION.md` only.
3. Do not widen beyond that note unless a later case shows the note-level register is insufficient.
