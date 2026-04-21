# Repo Canon Loading Guide

Use this guide to decide which local docs to read before researching. Load only what is relevant to the question.

## Base Canon

These are the first places to look for project posture and constraints:

- `AGENTS.md` - agent-facing runtime rules and delegation policy
- `WORKFLOW.md` - git workflow, verification posture, Codex hooks posture, and branch discipline
- `AI-GUARDRAILS.md` - human signoff boundaries and solo+AI operating guardrails
- `ARTIFACT-GOVERNANCE.md` - artifact classes, staleness handling, and generated-corpus retention rules
- `.planning/PROJECT.md` - project framing and high-level intent
- `.planning/ROADMAP.md` - phase order and current implementation lanes
- `.planning/REQUIREMENTS.md` - current requirements, protected seams, explicit deferrals
- `.planning/LONG-ARC.md` - durable long-arc doctrine and future-awareness constraints
- `.planning/knowledge/index.md` - project lessons and failure signals

## Research Canon

Use these when the question touches architecture, product-shape tradeoffs, or known pitfalls:

- `.planning/research/SUMMARY.md`
- `.planning/research/ARCHITECTURE.md`
- `.planning/research/FEATURES.md`
- `.planning/research/PITFALLS.md`

## Phase-Adjacent Canon

If the question is tied to a phase, add the phase artifacts:

- `.planning/phases/XX-*/XX-CONTEXT.md` - current decisions, assumptions, constraints, open questions, future awareness
- `.planning/phases/XX-*/XX-RESEARCH.md` - prior implementation research
- `.planning/phases/XX-*/XX-VALIDATION.md` - what has already been checked
- `.planning/phases/XX-*/XX-DISCUSSION-LOG.md` - discussion history when relevant

Prefer the current phase directory over anything in `superseded/`.

## Explore And Audit Canon

Use these when the question is open-ended, comparative, or about prior reasoning quality:

- `.planning/explore/CURRENT.md`
- relevant active directories under `.planning/explore/`
- latest relevant artifacts under `.planning/audits/`

Audits are especially useful for:
- prior contradictions
- missed assumptions
- canon conflicts
- methodology failures

## Initiative-Specific Canon

If the work is inside the vision-alignment initiative, also read:

- `.planning/initiatives/vision-alignment-2026-04/RESEARCH-PRINCIPLES.md`

If the work is phase-steering or planning-adjacent, use these local GSD materials to shape the handoff:

- `.codex/get-shit-done/workflows/discuss-phase.md`
- `.codex/get-shit-done/templates/context.md`

They define the steering categories downstream planning expects: decisions, assumptions, derived constraints, open questions, epistemic guardrails, future awareness (including strengthening opportunities), and deferred ideas.

## Canon Rules

- Treat repo governance docs and `.planning/` canon together as the live source of truth.
- Treat `discovery/` as upstream context, not live operational state.
- Prefer canonical docs over exploratory notes when they conflict.
- Prefer the latest non-superseded artifact over archived or superseded ones.
- If canon conflicts, report the conflict directly instead of choosing a side silently.
- If the user explicitly asks to challenge canon, say which canon is being challenged and why.
