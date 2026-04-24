Date: 2026-04-23
Status: revised after lane-05 audit

# Harness Modifier First Observe-Only Host Exercise Packet Proposal

## Role

- [d:r:i] This proposal defines the first bounded host-exercise packet for responsible closure.
- [d:r:i] It is a packet/probe design, not a claim that the run has happened and not a claim that broader deployment is now earned.

## Why This Packet Is Needed

- [d:r:i] Responsible closure now needs more than local install green checks inside `prix-guesser`.
- [d:r:i] But jumping straight to a second-host run without a packet would blur:
  - what is being exercised
  - what is being observed
  - what is allowed to be written
  - what would count as divergence versus positive gain

## Packet Target

- [g:r:i] First target should be one disjoint `.codex`-only host with:
  - regular GSD already installed
  - no pre-existing GSD Reflect artifacts
  - clean worktree
  - known basis commit
  - no coupling to the current `prix-guesser` repo
- [d:r:i] Mixed `.codex` + held-annotation `.claude` remains the stronger second exercise when the first packet returns cleanly enough to refine the carrier.
- [d:r:i] Hosts with pre-existing GSD Reflect artifacts remain a later explicit target, not the first packet.

## Packet Sections

### 1. Host Declaration

- [d:r:i] identify the host repo
- [d:r:i] identify runtime class
- [d:r:i] assign `host_shape`
- [d:r:i] identify whether regular GSD is present
- [d:r:i] capture `host_has_reflect_artifacts: bool`
- [d:r:i] capture a short rationale for that determination
- [d:r:i] identify whether the host is pristine, lightly aged, or drifted relative to current modifier assumptions

### 2. Preflight Reads

- [d:r:i] compatibility declaration read
- [d:r:i] overlay/install contract read
- [d:r:i] runtime visibility read
- [d:r:i] manifest/install coherence read if the host already materializes runtime surfaces
- [d:r:i] capture:
  - `declaration_posture`
  - `observed_basis_runtime`
  - `held_annotation_runtime`
  - `compatibility_window_state`
  - `basis_commit`
  - `dirty_worktree`
- [d:r:i] `held_annotation_runtime` is declaration-side capture only and does not count as `.claude` exercise proof.
- [d:r:i] no write-side install claim during this stage

### 3. Observe-Only Exercise Steps

- [d:r:i] capture deployment-context facts
- [d:r:i] run the bounded read-side checks that the current declaration says should hold
- [d:r:i] classify:
  - expected carry
  - warning
  - shift-mode
  - refusal
- [d:r:i] record per-step `skip_reason` where a planned check is intentionally not run rather than silently omitting it
- [d:r:i] bind `skip_reason` to the same bounded `automation_skip_reasons` vocabulary carried by the observation carrier
- [d:r:i] write only the harness-modifier observation artifact, not host planning docs

### 4. Capture Outputs

 - [d:r:i] typed observation carrier
 - [d:r:i] optional terse `narrative_summary` inside the typed observation only if a reader needs quick interpretation
 - [d:r:i] run metadata:
  - basis commit
  - host reference
  - runtime class
  - invoked checks
  - resulting disposition
  - `runtime_visibility_snapshot_path`
  - `verify_materialized_summary`
 - [d:r:i] `verify_materialized_summary` should be a pointer to a separately written file under the harness-modifier audit tree, not inline content inside the observation record.

### 5. Abort Or Hold Conditions

- [d:r:i] host runtime lies outside the explicit compatibility window
- [d:r:i] host worktree is dirty or not on a known basis commit
- [d:r:i] host requires write-side install mutation to even observe the posture
- [d:r:i] packet would have to alter single-writer governance surfaces in the host
- [d:r:i] host is too blended with Reflect-specific machinery for the first bounded packet
- [d:r:i] use an enumerated Reflect-artifact abort list rather than a prose-only blend test:
  - `.planning/knowledge-base/`
  - `commands/gsd/signal.md`
  - `commands/gsd/reflect.md`
  - `session_meta_postlude` hook carry

## Propagation Rule

- [d:r:i] This packet will have propagation consequences even before the run:
  - responsible-closure governance surfaces
  - possibly the compatibility declaration family
  - possibly the parity classification family
- [d:r:i] That means the later implementation/run slice must travel with an explicit propagation refresh, not only with the observation artifact.

## Parallelization Rule

- [d:r:i] Later exercise runs may overlap safely with unrelated governance carry only when:
  - the run basis is frozen
  - no installer/materialization rewrites happen concurrently
  - no single-writer governance surface is being edited by the companion lane
- [d:r:i] Verification or review-side sidecars are promising here, but they should be scheduled explicitly rather than improvised opportunistically.

## Explicitly Later

- [d:r:i] actual mixed-host packet
- [d:r:i] packet for hosts carrying Reflect artifacts
- [d:r:i] any write-side deployment path
- [d:r:i] durability/recurrence logic on packet outcomes
- [d:r:i] automation-level escalation beyond operator-triggered packet runs
- [d:r:i] automated fleet-style exercise scheduling
- [d:r:i] multi-host comparison dashboard

## Exact Next Move

1. [d:r:i] Treat responsible-closure lane `05` as the completed audit over this packet plus `172` and `173`.
2. [d:r:i] Keep this packet as the owner of exercise vocabulary and first-host scope.
3. [d:r:i] Implement the packet contract after the observation-carrier writer lands.
4. [d:r:i] Keep the actual observe-only run later, after both the carrier and packet implementation slices are landed and reread.
