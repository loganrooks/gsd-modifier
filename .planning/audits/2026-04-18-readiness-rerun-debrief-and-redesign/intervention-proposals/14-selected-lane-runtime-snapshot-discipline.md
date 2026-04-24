Date: 2026-04-20
Status: accepted bounded discipline

# Selected-Lane Runtime Snapshot Discipline

## Purpose

- [g:r:i] This note lands the third move in the accepted second-tranche order: durable runtime snapshots for selected lanes, not as repo-wide fossilization but as stronger carry at the places where final-runtime truth materially affects later inheritance.

## Why This Is Now The Right Move

- [e:c+i] The targeted reread just rejected broad stale-agent cleanup as the immediate next step. Most of the live-only cohort is active carry, and the narrower pressure is now better routing and later coherence, not immediate retirement. Sources: [13-live-only-agent-targeted-reread-disposition.md](/home/rookslog/workspace/projects/prix-guesser/.planning/audits/2026-04-18-readiness-rerun-debrief-and-redesign/intervention-proposals/13-live-only-agent-targeted-reread-disposition.md:1).
- [d:r:i] That makes snapshot discipline stronger now than it would have been earlier: we can freeze runtime truth for selected lanes without first dragging a false cleanup story into the snapshot layer.

## Accepted Shape

- [d:r:i] Use the new [capture_runtime_visibility_snapshot.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/capture_runtime_visibility_snapshot.py:1) wrapper for selected lane boundaries.
- [d:r:i] Do not capture snapshots for every ordinary edit.
- [d:r:i] Treat snapshots as durable lane artifacts only when later audit, disposition, or installer/materialization reasoning would otherwise depend on chat memory or ephemeral terminal output.

## Selected Trigger Conditions

- [d:r:i] Capture a runtime snapshot when any of the following is true:
  - a lane changes overlay/runtime authority surfaces
  - a lane changes installer/materialization behavior
  - a lane resolves a disputed live-vs-overlay or manifest/install question
  - a lane is about to hand runtime-truth evidence to a later cross-vendor or inheritance review

## Preferred Capture Pattern

- [d:r:i] Prefer capture on a clean checkpoint boundary.
- [d:r:i] Preferred command shape:

```bash
python3 tooling/codex/capture_runtime_visibility_snapshot.py \
  . \
  --label <lane-or-boundary-label> \
  --output <audit-subtree>/artifacts/<snapshot-name>.json \
  --notes "<why this boundary matters>"
```

- [d:r:i] If the worktree is dirty, treat that as an explicit warning in the snapshot metadata, not as hidden ambient context.

## What This Carries Better

- [d:r:i] Better inheritance discipline:
  - later reviewers can see the actual classified runtime state tied to a basis commit
- [d:r:i] Better update resilience:
  - manifest/install questions can compare frozen runtime truth to boundary metadata without overloading one file
- [d:r:i] Better maintainability:
  - no need to re-derive past runtime conditions from prose notes and memory

## What This Rejects

- [d:r:i] Reject repo-wide automatic snapshotting after every write.
- [d:r:i] Reject lane-local prose summaries as the only runtime-truth carry when a classified snapshot is easy to preserve.

## Immediate Next Move

- [g:r:i] Capture the first selected-lane snapshot after the current checkpoint lands, then use that cleaner baseline in the manifest/install coherence follow-through.
