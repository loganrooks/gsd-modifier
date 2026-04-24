# Workspace Authority And Organization

Status: active authority note  
Date: 2026-04-19

## Research Frame

- Mode: synthesis
- Question: how should this audit workspace distinguish governing setup, challenge input, inquiry corpus, and launch scaffolding before the next serious lane?
- Scope: `.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/`
- Non-goals:
  - rewrite readiness canon
  - settle corpus inheritance globally
  - authorize main-wave launch from this artifact alone
- Stop condition: a later reader can tell what governs, what can challenge, what remains exploratory, and what the next local decision sequence is

## Path Of Inquiry

- Entry point: the workspace accumulated a large mix of setup docs, challenge lanes, prompts, corpus files, and historical passes, while lane-03's narrow result was starting to sprawl into a broader `no-change` reading.
- Branches considered:
  - launch another Opus lane immediately
  - keep patching setup docs without clarifying authority
  - clarify workspace authority first, then design the next lane
- Branches pursued: clarify workspace authority first, then design the next lane
- Branches deferred or abandoned:
  - direct canon/doctrine rewrites
  - immediate `CLAIM-TYPES.md` mutation
  - main-wave launch-readiness call

## Why This Artifact Exists

- [g:c+i] This directory is `audit trail + program design`, not canon, so authority cannot be inferred just from top-level proximity or file density. Sources: .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/INDEX.md:20-28, .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/INDEX.md:69-71, .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/governance/GOVERNANCE-READING-AND-UPDATE-PROTOCOL.md:17-32, ARTIFACT-GOVERNANCE.md:33-41.
- [d:c+i] The governance set now separates controlled entry, denser artifact discovery, short governing synthesis, and longer cumulative trace, which makes it easier to judge force by role instead of by file density. Sources: .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/INDEX.md:5-12, .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/governance/GOVERNANCE-READING-AND-UPDATE-PROTOCOL.md:17-69, .planning/AGENTS.md:42-77.
- [d:c+i] Lane-03 answered a narrow question because its spec asked whether corpus distinctions changed recommendation, warrant, salience, or only rephrased, and its own output flags both coarse-category risk and doctrine-friendly case selection as failure modes. Sources: .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/review-specs/OPUS-CORPUS-VOCABULARY-STRESS-TEST-SPEC.md:17-28, .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/review-specs/OPUS-CORPUS-VOCABULARY-STRESS-TEST-SPEC.md:160-187, .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/lane-reviews/lane-03-opus47-max-corpus-vocabulary-stress-test.md:303-311, .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/lane-reviews/lane-03-opus47-max-corpus-vocabulary-stress-test.md:317-333.
- [d:r:i] Therefore lane-03 is authoritative only on the narrow question it actually tested: no immediate corpus-to-doctrine promotion was earned on those three cases. It is not a general warrant for non-change, non-operationalization, or no further inheritance work.

## Host Project Context Versus Harness Modifier Scope

- [g:r:i] This audit workspace lives inside the `prix-guesser` repo, but the harness-uplift program carried here is not identical to the `prix-guesser` product-planning surface.
- [d:r:i] Product-side planning docs such as `.planning/LONG-ARC.md`, `.planning/ROADMAP.md`, `.planning/STATE.md`, and readiness/rerun canon remain host-project context unless a slice explicitly crosses into product planning, rerun coupling, or entry / re-entry integration.
- [d:r:i] For harness-uplift work, short / medium / long horizons mean:
  - immediate harness slice
  - near-term harness family queue
  - longer-horizon harness doctrine, extraction, propagation, and distribution direction
- [d:r:i] When a read set mixes surfaces from both scopes, mark each one as:
  - `host-project context`
  - `shared boundary`
  - `harness doctrine`
- [d:r:i] Do not let a nearby host-project planning doc become default harness doctrine merely because the harness-improvement work is currently co-located in the same repository.

## Authority Classes

### 1. Governing Setup Spine

These are the files that currently govern local decisions about what this workspace is for, what questions it should ask, how evidence should be packeted, and what program shapes remain live.

- `AUDIT-CHARTER.md`
- `GOVERNANCE-READING-AND-UPDATE-PROTOCOL.md`
- `CURRENT-STATE.md`
- `../planning-notes/QUESTION-SET.md`
- `EVIDENCE-ARCHITECTURE.md`
- `../planning-notes/PLAN-PROPOSALS.md`
- `STATUS.md`
- `WORKSPACE-AUTHORITY-AND-ORGANIZATION.md`
- `AUDIT-LANE-PATTERN-LIBRARY.md`
- `AUDIT-CANON-ABSORPTION-PROTOCOL.md`
- `AUDIT-SUBTREE-AGING-AND-GRADUATION.md`

What this class can do:

- define the workspace's current remit
- set burden-of-proof expectations
- name the live comparison model and proposal space
- sequence the next local program-design moves
- route recurring audit-lane structure, canon absorption, and subtree-aging judgments

What this class cannot do on its own:

- mutate readiness canon
- mutate repo canon
- silently promote challenge outputs or inquiry corpus into doctrine

### 2. Briefing, Support Traces, And Procedural Scaffolding

These files route readers, preserve launch contracts, or carry longer supporting traces, but they do not settle substantive claims on their own.

- `INDEX.md`
- `ARTIFACT-INVENTORY.md`
- `CURRENT-STATE-TRACE.md`
- `ONBOARDING.md`
- `../planning-notes/SESSION-FRAMING-BRIEF.md`
- lane specs and launch prompts in this directory
- `../root-support/LAUNCH-LEDGER.md`

What this class can do:

- define read order
- preserve longer cumulative buildup without overloading the short governing synthesis
- preserve denser artifact discovery without overloading the controlled entry path
- preserve situated framing and operator hypotheses
- define the contract for a given external lane
- preserve launch history and audit trail

What this class cannot do on its own:

- override the governing setup spine
- turn a local framing claim into a settled fact
- convert one lane's framing into workspace doctrine without adoption in the spine

### 3. Challenge Inputs

These are review artifacts that can challenge, pressure, narrow, or reopen the setup, but must be explicitly dispositioned before they gain local force.

- `../lane-reviews/lane-01-opus47-audit-setup-cross-review.md`
- `../lane-reviews/lane-01-opus47-cross-review-disposition.md`
- `../lane-reviews/lane-02-opus47-max-resituation-review.md`
- the paired `../review-specs/OPUS-CORPUS-VOCABULARY-STRESS-TEST-SPEC.md` plus `../lane-reviews/lane-03-opus47-max-corpus-vocabulary-stress-test.md`

What this class can do:

- expose weak framing
- surface missing evidence families
- narrow what has or has not yet been earned
- propose next lanes or bounded proposals

What this class cannot do on its own:

- become sovereign doctrine
- silently demote the governing setup spine
- authorize rewrite just because a prestige model said so

Working rule:

- [d:r:i] Read a challenge output together with the contract that framed it whenever the scope of its authority is in question. Lane-03 especially should be read as a paired spec-and-output artifact, not just as a free-floating verdict.

### 4. Inquiry Corpus

These artifacts are the exploratory inheritance layer produced by the contestation / claim ontology inquiry.

- `corpus/source/CONTESTATION-AND-CLAIM-ONTOLOGY-NOTE.md`
- `corpus/translation/CONTESTATION-AND-CLAIM-ONTOLOGY-NOTE-DERRIDEAN-REWRITE-AND-AUDIT-TRANSLATION.md`
- `corpus/COMMENTARY-CORPUS-READSET.md`
- the 37 active chunk commentary files named in the manifest
- commentary prompts

What this class can do:

- supply distinctions, hypotheses, and pressure points
- identify candidate operationalization surfaces
- sharpen later audit or workflow proposals
- pressure existing doctrine without yet rewriting it

What this class cannot do on its own:

- rewrite doctrine, workflow, or audit setup
- count as settled canon
- bypass case-grounded or surface-grounded inheritance testing

Working rule:

- [d:c+i] The manifest, not filename drift, defines the current inheritable chunk corpus. Earlier passes remain historical trail unless explicitly reopened. Sources: .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/corpus/COMMENTARY-CORPUS-READSET.md:5-10, .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/corpus/COMMENTARY-CORPUS-READSET.md:12-50, .planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/corpus/COMMENTARY-CORPUS-READSET.md:52-55.

### 5. Historical And Superseded Trail

These are still part of the reasoning trail, but they are not the current inheritable layer unless a later artifact points back to them deliberately.

- earlier whole-note commentary attempts
- non-manifest chunk passes
- historical prompt variants once superseded

What this class can do:

- preserve auditability
- show how the inquiry evolved
- support bounded rereads when a later artifact points back to them

What this class cannot do on its own:

- compete with the manifest-defined active corpus
- govern future reading order

## Authority / Force Snapshot

Use this register when a file's declared class and its effective routing force are materially different, or when a later reviewer needs a compact answer to `why did this file matter here?`

- Artifact or class: `../planning-notes/SESSION-FRAMING-BRIEF.md`
  - Declared authority: briefing / procedural scaffolding
  - Effective authority: class-1-adjacent during spec writing and framing disputes
  - Sources of force: repeated citation in specs and dispositions, anti-tame framing pressure
  - Divergence risk: medium
  - Next local review consequence: if this brief materially steers a lane contract, name that explicitly and test it against the governing setup spine rather than treating the brief as silent floor

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
- a class-2 artifact is cited in three or more specs, dispositions, or setup docs as steering authority
- an accepted proposal or stress-test result materially changes which files can route lane or phase choices

## Read Discipline By Task

### If the task is current setup judgment

Read:

1. `AUDIT-CHARTER.md`
2. `WORKSPACE-AUTHORITY-AND-ORGANIZATION.md`
3. `GOVERNANCE-READING-AND-UPDATE-PROTOCOL.md`
4. `CURRENT-STATE.md`
5. `../planning-notes/QUESTION-SET.md`
6. `EVIDENCE-ARCHITECTURE.md`
7. `../planning-notes/PLAN-PROPOSALS.md`
8. `STATUS.md`

Then add only the challenge artifacts directly relevant to the disputed point.

### If the task is interpreting a challenge lane

Read:

1. the governing setup spine above
2. the paired spec and output for that lane
3. any local disposition artifact for that lane

Do not read a lane output as if it arrived without a frame.

### If the task is corpus inheritance or operationalization

Read:

1. the governing setup spine
2. `corpus/COMMENTARY-CORPUS-READSET.md`
3. the derivative translation
4. only the chunk subset actually relevant to the candidate surface
5. the source note only as bounded spot-check reserve

### If the task is launching a new external lane

Read:

1. the governing setup spine
2. the authority note
3. the specific lane spec
4. the launch prompt
5. `../root-support/LAUNCH-LEDGER.md`

Do not treat older lane specs as the current contract unless the spine or the authority note still points to them as active.

## Current Working Judgments

- [d:r:i] Carriage improvement and doctrine promotion must stay separate. A distinction can earn a local proposal or a bounded stress-test target without yet earning canon rewrite.
- [d:r:i] The current workspace question is broader than lane-03's question. The live issue is not only whether the corpus flips prior verdicts, but also whether it lets this workspace carry audit design, harness interpretation, workflow inheritance, and future-facing judgment better.
- [d:r:i] The next candidate operationalization surfaces are:
  - workspace authority and organization
  - audit output registers and question design
  - claim-type limits and adjacent doctrine surfaces
  - workflow / harness carriers such as `discuss-phase.md` and `context.md`
- [d:r:i] Direct rewrites of `CLAIM-TYPES.md`, readiness doctrine, or harness files remain deferred until a narrower carriage-and-operationalization pass earns something more concrete than reviewer-register value.

## What Can Close Now

- [d:r:i] The workspace now has an explicit authority model rather than a flat pile of same-level files.
- [d:r:i] Lane-03 can now be treated narrowly and legibly rather than as an inflated `no-change` verdict.
- [d:r:i] A new lane can now be specified against carriage quality and operationalization rather than only verdict change.

## What Must Stay Open

- [o:r:i] Which candidate operationalizations are strong enough to justify local proposal now
- [o:r:i] Which candidates are only strong enough for a bounded next stress test
- [o:r:i] Whether any claim-type limitation statement, sibling layer, or workflow prompt change is actually earned
- [o:r:i] Whether the next Opus lane should be launched immediately after local review of the new spec

## Sources

- `ARTIFACT-GOVERNANCE.md`
- `.planning/AGENTS.md`
- `INDEX.md`
- `corpus/COMMENTARY-CORPUS-READSET.md`
- `../review-specs/OPUS-CORPUS-VOCABULARY-STRESS-TEST-SPEC.md`
- `../lane-reviews/lane-03-opus47-max-corpus-vocabulary-stress-test.md`
