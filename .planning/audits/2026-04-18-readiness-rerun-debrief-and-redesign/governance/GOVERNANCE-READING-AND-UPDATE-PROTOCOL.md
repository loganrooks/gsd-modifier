Date: 2026-04-21
Status: active governance protocol

# Governance Reading And Update Protocol

## Purpose

- [g:r:i] This note gives the governance docs in this workspace distinct jobs.
- [d:r:i] Its aims are:
  - progressive disclosure instead of forced deep rereads
  - tighter control over what a reader loads
  - clearer routing for where new information should be recorded
  - less duplication across `INDEX.md`, `CURRENT-STATE.md`, `STATUS.md`, and the authority note

## Governance Surface Roles

### `INDEX.md`

- [g:r:i] Role: entry point and controlled read order
- [d:r:i] Use it when:
  - you need the official read order
  - you need the controlled entry path into the workspace
- [d:r:i] Do not use it as the cumulative state narrative or mutable queue

### `ARTIFACT-INVENTORY.md`

- [g:r:i] Role: denser artifact discovery and family-location map
- [d:r:i] Use it when:
  - you need to find an artifact family
  - you need the active baseline files for a family
  - you need a quick map of the current subtree layout without reading the whole queue
- [d:r:i] Do not use it as the mutable queue or as the short governing synthesis

### `WORKSPACE-AUTHORITY-AND-ORGANIZATION.md`

- [g:r:i] Role: authority classes, role disputes, and reread discipline
- [d:r:i] Use it when:
  - you are unsure what governs versus what merely pressures
  - two artifacts seem to conflict in force
  - you need to know which doc should absorb a new kind of update

### Audit-program infrastructure surfaces

- [g:r:i] Role: reusable lane structure, canon-absorption routing, and subtree-aging control
- [d:r:i] Surfaces:
  - `AUDIT-LANE-PATTERN-LIBRARY.md`
  - `AUDIT-CANON-ABSORPTION-PROTOCOL.md`
  - `AUDIT-SUBTREE-AGING-AND-GRADUATION.md`
  - `AUDIT-SUBTREE-STATUS-REGISTER.md`
- [d:r:i] Use them when:
  - a new audit lane is being designed and recurring scaffold questions keep reappearing
  - a landed family needs doctrine/helper/register absorption rather than remaining trapped in one subtree
  - an audit subtree no longer owns the immediate next move and its later force needs clearer routing
  - a reader needs the quickest current answer to which subtree is still live route, companion context, or aging trace

### `../plain-language/PLAIN-LANGUAGE-STATE.md` and `../plain-language/PLAIN-LANGUAGE-GLOSSARY.md`

- [g:r:i] Role: fastest honest re-entry for a reader who has lost the thread
- [d:r:i] Use them before denser rereads when shorthand, internal lane labels, or audit-program language starts obscuring the actual work

### `CURRENT-STATE.md`

- [g:r:i] Role: short governing synthesis
- [d:r:i] It should answer only:
  - what remains stably true
  - what the active baselines are
  - what the immediate decision surfaces are
- [d:r:i] It should stay compact enough that a reader can recover the workspace posture without traversing the whole historical buildup

### `CURRENT-STATE-TRACE.md`

- [g:r:i] Role: supporting cumulative trace
- [d:r:i] Use it when the short synthesis is too compressed and the reader needs the longer buildup behind current baselines
- [d:r:i] It is allowed to be richer and more cumulative than `CURRENT-STATE.md`, but it should still be grouped by family rather than devolving into raw chronology

### `STATUS.md`

- [g:r:i] Role: mutable queue, checkpoint ledger, and current routing pressure
- [d:r:i] Use it when:
  - you need to know what is active now
  - you need the next queue
  - you need a recent checkpoint or boundary
- [d:r:i] Do not let it silently outrank `CURRENT-STATE.md` on substantive state claims

### `../root-support/LAUNCH-LEDGER.md`

- [g:r:i] Role: requested-vs-effective external launch history
- [d:r:i] Use it for launch truth, not for general workspace status

## What To Read By Task

### Fast Re-entry

Read:

1. `../plain-language/PLAIN-LANGUAGE-STATE.md`
2. `../plain-language/PLAIN-LANGUAGE-GLOSSARY.md`
3. `CURRENT-STATE.md`

### Baseline And Next Decisions

Read:

1. `CURRENT-STATE.md`
2. `STATUS.md`
3. the family-specific artifacts named in `CURRENT-STATE.md`

### Authority Or Relevance Dispute

Read:

1. `WORKSPACE-AUTHORITY-AND-ORGANIZATION.md`
2. this protocol
3. `CURRENT-STATE.md`

### Need The Longer Buildup

Read:

1. `CURRENT-STATE.md`
2. `CURRENT-STATE-TRACE.md`
3. only the family-specific artifacts that the trace points you toward

### Artifact Search Or Read-Order Recovery

Read:

1. `INDEX.md`
2. `ARTIFACT-INVENTORY.md` if you need denser discovery
3. `STATUS.md` only if you also need the current queue

## Update Rules

- [d:r:i] When new work lands, decide first which governance surface owns it.
- [d:r:i] Preferred routing:
  - current baseline or governing consequence -> `CURRENT-STATE.md`
  - cumulative buildup or multi-family narrative -> `CURRENT-STATE-TRACE.md`
  - mutable next steps, queue changes, or checkpoint boundaries -> `STATUS.md`
  - read-order/control-path shifts -> `INDEX.md`
  - denser discovery or family-location expansion -> `ARTIFACT-INVENTORY.md`
  - role disputes or new doc-boundary rules -> `WORKSPACE-AUTHORITY-AND-ORGANIZATION.md`
  - reusable audit-lane structure -> `AUDIT-LANE-PATTERN-LIBRARY.md`
  - doctrine/helper/register uplift routing -> `AUDIT-CANON-ABSORPTION-PROTOCOL.md`
  - subtree-force aging or graduation -> `AUDIT-SUBTREE-AGING-AND-GRADUATION.md`
  - current subtree-force application -> `AUDIT-SUBTREE-STATUS-REGISTER.md`
- [d:r:i] If a new update seems to belong in all of them, that is a warning sign that the change has not been decomposed cleanly enough yet.
- [d:r:i] If one governance doc starts carrying multiple jobs at once, split the file instead of continuing to accrete prose.

## Contract-Change Recording

- [d:r:i] When a change alters a contract family rather than a single isolated file, record not only what changed but where the change should propagate.
- [d:r:i] The minimum governed record for a contract-changing slice should usually include:
  - the active family baseline
  - the adjacent producer / consumer or carrier surfaces that were updated
  - the neighbors that were intentionally held for later
  - the next audit or verification surface if the propagation burden is wider than one local slice
- [d:r:i] Do not leave propagation obligations ambient in chat or commit messages alone.
- [d:r:i] If a contract change starts to require several families to stay in tune at once, prefer a dedicated family note or audit subtree over expanding `CURRENT-STATE.md` into a spread tracker.

## Relevance Filters

- [d:r:i] A reader should not need the whole workspace to work on one family.
- [d:r:i] When a family becomes active, ensure the short synthesis names:
  - the active baseline artifact(s)
  - the next adjacent choice
  - the minimal reread set for that family
- [d:r:i] When deeper detail is useful but not always needed, prefer a supporting trace or family-specific note over expanding the short synthesis.
- [d:r:i] When a harness-improvement family lives inside a host-product repo, mark loaded surfaces as `host-project context`, `shared boundary`, or `harness doctrine`.
- [d:r:i] Do not let a product-level planning doc become default harness doctrine just because it is nearby in the same repo.

## Current Local Application

- [d:r:i] `CURRENT-STATE.md` is now the short governing synthesis for this workspace.
- [d:r:i] `CURRENT-STATE-TRACE.md` is the longer cumulative trace.
- [d:r:i] `ARTIFACT-INVENTORY.md` is the denser discovery surface.
- [d:r:i] This protocol should be reread the next time the governance set starts to feel overloaded again, especially if `INDEX.md` and `STATUS.md` begin to duplicate each other or if `CURRENT-STATE.md` starts turning back into a warehouse.
