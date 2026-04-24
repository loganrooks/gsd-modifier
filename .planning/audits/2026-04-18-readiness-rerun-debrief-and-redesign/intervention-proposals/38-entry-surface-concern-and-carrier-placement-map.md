Date: 2026-04-21
Status: active placement map

# Entry Surface Concern And Carrier Placement Map

## Purpose

- [g:r:i] This artifact records where the concerns in the entry/uplift family should surface most strongly.
- [g:r:i] The task here is not to repeat the terrain map in `37`. The task is to decide strongest placement: which concerns belong in entry questions, which belong in governing docs, which belong in runtime/install checks, which belong in project-state carriers, which belong in seeds, and which belong in uplift outputs.
- [g:r:i] The point is stronger form, not mere mention. A concern can appear in several places and still be weakly carried if none of those places actually owns its strongest expression.

## Placement Rule

- [d:r:i] Each concern in this family should have:
  - one primary carrier surface
  - any number of supporting carriers
  - explicit non-owners where mention would be weaker than routing
- [d:r:i] This prevents two recurring failures:
  - everything gets mentioned everywhere and nothing owns it
  - a concern is present in one weak location and then treated as already carried

## Concern Families

### 1. Runtime / Install / Materialization Posture

- [d:r:i] Primary carriers:
  - `update`
  - installer/materialization carrier: `scripts/setup-portable-gsd.sh`
  - runtime/install tooling: `runtime_visibility.py`, `manifest_install_coherence.py`
  - uplift outputs: `UPLIFT-REPORT.md`, `STATE.md` uplift section, `UPLIFT-MANIFEST.json`
- [d:r:i] Supporting carriers:
  - `../governance/RUNTIME-MATERIALIZATION-AND-AUTHORITY.md`
  - generated instruction/runtime notes when a project is freshly initialized
- [d:r:i] Non-owners:
  - `health`
  - `new-milestone`
  - general planning prompts
- [d:r:i] Why this placement is stronger:
  - runtime posture is a materialization and install-truth problem first
  - it should later surface in state and routing, but not be primarily owned by generic planning surfaces

### 2. Governing-Doc And Instruction Posture

- [d:r:i] Primary carriers:
  - root `AGENTS.md`
  - `.planning/AGENTS.md`
  - root/planning `CLAUDE.md`
  - generated instruction file and later uplift outputs
- [d:r:i] Supporting carriers:
  - project doctrine manifest
  - `UPLIFT-REPORT.md`
- [d:r:i] Non-owners:
  - `health`
  - `progress`
  - `resume-project`
- [d:r:i] Why this placement is stronger:
  - these concerns are about operating posture and governing doctrine
  - situational routing surfaces should consume the result, not define the doctrine

### 3. Required-Reading Posture

- [d:r:i] Primary carriers:
  - governing docs that instruct authors to include `<required_reading>`
  - prompt/spec/packet templates that actually carry those blocks
  - uplift workflow/install pass that brings the practice into older projects
- [d:r:i] Supporting carriers:
  - `mandatory-initial-read` as the enforcement reference
  - launch-truth or packet review notes when a lane fails to install it
- [d:r:i] Non-owners:
  - `progress`
  - `health`
  - runtime/install tools
- [d:r:i] Why this placement is stronger:
  - enforcement is not the same thing as project-wide install
  - the practice has to live in authoring surfaces, not only in a reminder reference

### 4. Claim-Type And Anti-Threshold Posture

- [d:r:i] Primary carriers:
  - root/planning `AGENTS.md`
  - root/planning `CLAUDE.md`
  - `.planning/CLAIM-TYPES.md`
- [d:r:i] Supporting carriers:
  - `scan_threshold_language.py`
  - `gsd-rigorous-research` method and related review/spec surfaces
- [d:r:i] Non-owners:
  - `update`
  - `health`
  - `resume-project`
- [d:r:i] Why this placement is stronger:
  - this concern governs how planning, audit, and research think
  - it should sit in doctrine and in doctrine-enforcing tooling, not as a stray note in downstream execution surfaces

### 5. Long-Horizon And Strengthening Carry

- [d:r:i] Primary carriers:
  - `.planning/LONG-ARC.md`
  - discuss/context/plan/phase-prompt surfaces
  - `future_preservation` and strengthening-route carriers
- [d:r:i] Supporting carriers:
  - `plant-seed`
  - `new-milestone`
  - uplift outputs that note whether a project has inherited this posture
- [d:r:i] Non-owners:
  - runtime/install tools
  - `health`
- [d:r:i] Why this placement is stronger:
  - horizon carry begins in doctrine and planning, then gets preserved into seeds and milestone renewal
  - runtime surfaces can report whether the chain is present, but they do not own its content

### 6. Doctrine Vintage / Pre-Rerun Boundary / Active Boundary Posture

- [d:r:i] Primary carriers:
  - per-phase `CONTEXT.md` boundary stamp
  - `STATE.md`
  - `STATE.md` uplift section or equivalent in-file uplift history
  - `progress` / `resume-project` routing branches
- [d:r:i] Supporting carriers:
  - root/planning `AGENTS.md`
  - explicit rerun-boundary notes in audit or phase artifacts
- [d:r:i] Non-owners:
  - `update`
  - `health`
  - `new-project`
- [d:r:i] Why this placement is stronger:
  - this concern matters when deciding what to do next with an already-existing project
  - it belongs in the phase boundary plus state/routing surfaces that can actually change behavior, not only in static doctrine prose

### 7. Discovery Boundary And Brownfield Carry

- [d:r:i] Primary carriers:
  - `new-project`
  - `ingest-docs`
  - root `AGENTS.md` rule distinguishing `discovery/` from live planning state
- [d:r:i] Supporting carriers:
  - `PROJECT.md`
  - uplift outputs where a project still carries large upstream-discovery residue
- [d:r:i] Non-owners:
  - `update`
  - `resume-project`
- [d:r:i] Why this placement is stronger:
  - the discovery/live-planning distinction matters most at creation and bootstrap boundaries
  - later surfaces should consume the result, not re-litigate the boundary each time

### 8. Cross-Runtime Posture

- [d:r:i] Primary carriers:
  - `.codex/config.toml`
  - `.codex/agents/*.toml`
  - uplift outputs that record runtime posture and wrapper alignment
- [d:r:i] Supporting carriers:
  - root/planning `CLAUDE.md` wrappers plus root/planning `AGENTS.md`
  - generated instruction file
  - `update`
- [d:r:i] Non-owners:
  - `health`
  - `new-milestone`
- [d:r:i] Why this placement is stronger:
  - runtime plurality has runtime-side registry truth and wrapper-side operator truth, and those can drift independently
  - the runtime-side registry therefore needs first seat, while wrappers and reports expose the posture to operators

### 9. Repo-Local Tooling Install

- [d:r:i] Primary carriers:
  - explicit tooling inventory carrier such as `tooling/codex/INVENTORY.md`
  - uplift workflow/install pass
  - project doctrine manifest
- [d:r:i] Supporting carriers:
  - root/planning `AGENTS.md`
  - `UPLIFT-REPORT.md`
  - audit subtree README conventions
- [d:r:i] Non-owners:
  - `progress`
  - `resume-project`
- [d:r:i] Why this placement is stronger:
  - the tools are governing infrastructure
  - their presence should be inventoried, installed, and recorded explicitly, not discovered accidentally only when an audit lane tries to use them

### 10. Audit-Subtree And Companion-Carrier Aging

- [d:r:i] Primary carriers:
  - audit-subtree `README.md`, `INDEX.md`, `STATUS.md`
  - doctrine-vintage stamp on doctrine-carrying audit subtrees
  - uplift outputs only when an uplift pass explicitly touches an active audit family
- [d:r:i] Supporting carriers:
  - seeds for later cleanup or re-entry
  - governance docs that name audit artifact classes
- [d:r:i] Non-owners:
  - `new-project`
  - `update`
  - `health`
- [d:r:i] Why this placement is stronger:
  - audit aging is a companion-carrier problem, not a runtime or milestone problem
  - it should be visible where audit work is actually governed

### 11. Uplift Output And Deferred-Routing Carry

- [d:r:i] Primary carriers:
  - `UPLIFT-REPORT.md`
  - `STATE.md` uplift section
  - `UPLIFT-MANIFEST.json`
- [d:r:i] Supporting carriers:
  - uplift-origin seeds
  - `STATE.md`
- [d:r:i] Non-owners:
  - `new-project`
  - `new-milestone`
  - `health`
- [d:r:i] Why this placement is stronger:
  - the uplift family needs its own durable before/after memory
  - otherwise the composition-layer work disappears into scattered specialist outputs

## Surface-Family Placement Summary

### Entry Workflow Question Flow

- [d:r:i] Best place for:
  - discovery boundary
  - brownfield distinctions
  - first-run posture installation
  - milestone-entry distinctions
- [d:r:i] Not the strongest place for:
  - runtime materialization truth
  - audit aging
  - deep doctrine-vintage history

### Governing Docs

- [d:r:i] Best place for:
  - anti-threshold posture
  - claim-type posture
  - cross-runtime posture
  - required-reading installation doctrine
  - tool-use doctrine
- [d:r:i] Not the strongest place for:
  - current runtime/install state
  - active project-specific before/after uplift disposition

### Project Docs And State Carriers

- [d:r:i] `PROJECT.md`
  - strongest for project identity, scope, discovery inheritance
- [d:r:i] `STATE.md`
  - strongest for active boundary, doctrine-vintage routing, current next-step consequences
- [d:r:i] per-phase `CONTEXT.md`
  - strongest for live phase-boundary posture, especially when doctrine has moved during an active phase
- [d:r:i] `ROADMAP.md`
  - strongest for milestone/phase carry, not for governing posture install
- [d:r:i] `LONG-ARC.md`
  - strongest for long-horizon carry, optionality, and future-shape protection

### Runtime / Install / Update Checks

- [d:r:i] Best place for:
  - materialization truth
  - overlay/live drift
  - manifest/install coherence
  - installer rerun posture
- [d:r:i] Not the strongest place for:
  - claim-type posture
  - audit-aging concerns

### Seeds And Later Routing

- [d:r:i] Best place for:
  - deferred long-horizon work
  - uplift-origin remainder that should not widen the first slice
  - milestone-triggered revisit items
- [d:r:i] Not the strongest place for:
  - current governing-doc refresh
  - current runtime truth

## Current Consequence

- [d:r:i] `37` now carries the widened terrain, including the four-way uplift split and mid-phase case.
- [d:r:i] `38` now carries stronger placement, especially for phase-boundary posture, runtime-side registry truth, tooling inventory, and doctrine-carrying audit subtrees.
- [d:r:i] The revised workflow pass should therefore use this map as the active carrier-allocation basis rather than improvising ownership from memory or from a generic onboarding brief.
