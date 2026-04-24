Date: 2026-04-21
Status: active audit-program infrastructure surface

# Audit Canon Absorption Protocol

## Purpose

- [g:r:i] This note governs how a landed audit family moves from audit-local history into more durable canon or helper surfaces.
- [d:r:i] Its job is to keep doctrine from getting trapped in one subtree while also preventing root/planning governance from turning into a warehouse.

## Canon Layers

### Repo governance canon

- [d:r:i] Examples:
  - `AGENTS.md`
  - `.planning/AGENTS.md`
  - repo governance docs such as `WORKFLOW.md` or `ARTIFACT-GOVERNANCE.md`
- [d:r:i] Use when the rule or practice should shape later work across the repo without requiring reread of one audit subtree.

### Audit-workspace governance canon

- [d:r:i] Examples:
  - `INDEX.md`
  - `CURRENT-STATE.md`
  - `STATUS.md`
  - `GOVERNANCE-READING-AND-UPDATE-PROTOCOL.md`
  - `WORKSPACE-AUTHORITY-AND-ORGANIZATION.md`
- [d:r:i] Use when the rule mainly governs this audit workspace's reading, routing, inheritance, or artifact control.

### Helper / tooling canon

- [d:r:i] Examples:
  - `tooling/codex/*.py`
  - `tooling/codex/README.md`
  - tests
- [d:r:i] Use when the family now has a machine-checkable or helper-backed expression.

### Durable cross-family register

- [d:r:i] Example:
  - `.planning/HARNESS-IMPROVEMENT-REGISTER.md`
- [d:r:i] Use when the family should remain visible outside one subtree, but does not need to bloat root governance or helper docs.

### Audit-local history

- [d:r:i] Keep in subtree:
  - reviewer disagreement
  - abandoned packaging
  - lane-specific rationale
  - historical comparison trail

## When Absorption Is Warranted

- [d:r:i] Absorb when a family now carries a reusable operating rule for later work.
- [d:r:i] Absorb when a helper, workflow, or consumer surface now depends on the family.
- [d:r:i] Absorb when later operators would otherwise need to rediscover the family by rereading one old subtree.
- [d:r:i] Absorb when omission would create repeated misread or repeated local reinvention.

## When Audit-Local Retention Is Better

- [d:r:i] Keep local when the artifact is mainly the trail of how a result was reached.
- [d:r:i] Keep local when the family is still exploratory and not yet routing later work.
- [d:r:i] Keep local when the detail is useful only as historical challenge context rather than live operating doctrine.
- [d:r:i] Keep local when the canon surface would become denser without materially helping later operators.

## Minimum Absorption Record

- [g:r:i] A family should not be treated as absorbed merely because a commit happened.
- [d:r:i] The minimum record should state:
  - source family or lane
  - target canon surfaces
  - what exactly is being carried
  - what remains audit-local
  - what adjacent routes remain held later

## Current Local Precedents

- [d:c+i] Propagation doctrine already moved partly into root and planning `AGENTS.md`, while keeping richer lane history inside `propagation-audit/`. Sources: [AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/AGENTS.md:49), [.planning/AGENTS.md](/home/rookslog/workspace/projects/prix-guesser/.planning/AGENTS.md:101), [propagation-audit/README.md](../propagation-audit/README.md).
- [d:c+i] The harness-quality canary family already moved into helper/tooling canon plus audit-workspace routing, while keeping the widening/review history inside `harness-improvement-audit/`. Sources: [tooling/codex/harness_canary.py](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/harness_canary.py), [tooling/codex/README.md](/home/rookslog/workspace/projects/prix-guesser/tooling/codex/README.md), [intervention-proposals/49-harness-quality-canary-first-slice-implementation.md](../intervention-proposals/49-harness-quality-canary-first-slice-implementation.md).
- [d:c+i] The standing self-improvement family already moved partly into a durable cross-family register while preserving proposal and widening history locally. Sources: [.planning/HARNESS-IMPROVEMENT-REGISTER.md](/home/rookslog/workspace/projects/prix-guesser/.planning/HARNESS-IMPROVEMENT-REGISTER.md), [intervention-proposals/50-harness-self-improvement-register-first-slice-implementation.md](../intervention-proposals/50-harness-self-improvement-register-first-slice-implementation.md).

## Anti-Patterns

- [d:r:i] leaving a reusable rule trapped only in one inheritance note
- [d:r:i] copying whole lane rationale into canon instead of absorbing the bounded rule
- [d:r:i] treating a subtree README mention as equivalent to canon absorption
- [d:r:i] absorbing into too many layers at once without a reasoned split

## Current Local Consequence

- [d:r:i] Later audit families in this workspace should explicitly decide what moves into repo canon, audit-workspace canon, helper canon, durable register carry, and what remains local trail.
- [d:r:i] This protocol is the default routing surface for that decision.
