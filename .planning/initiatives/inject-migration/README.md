# Inject Migration Initiative

## What This Is

A self-driving, multi-session, autonomous initiative to migrate `gsd-modifier`'s overlay model from overwrite-heavy to surgical injection. Designed to be picked up cold by an agent in any session, advanced by one bounded slice, and resumed indefinitely until complete.

This directory contains everything an agent needs to start, advance, and complete the migration without external context. Read order is enforced by [PROTOCOL.md](PROTOCOL.md).

## Quick Start (for the operator)

To start or resume the migration loop:

1. Make sure the worktree is clean (`git status --short` shows only items the protocol expects).
2. Read [LOOP-PROMPT.md](LOOP-PROMPT.md) to find the exact invocation prompt.
3. Either:
   - **One iteration**: paste the prompt into a fresh Claude Code session and let it run one slice
   - **Loop**: use the `loop` skill (`/loop <interval> <prompt>`) for periodic auto-advance
   - **Continuous**: paste the prompt in a session and let the agent self-pace via `ScheduleWakeup` if available

The agent reads [STATE.md](STATE.md) to learn where we are and [PROTOCOL.md](PROTOCOL.md) to learn what to do.

## File Index

| File | Role |
|---|---|
| [README.md](README.md) | this file |
| [INITIATIVE.md](INITIATIVE.md) | master plan (goal, model, phases, completion criteria) |
| [STATE.md](STATE.md) | live progress tracker (agent updates each iteration) |
| [PROTOCOL.md](PROTOCOL.md) | how the agent runs each iteration |
| [GUARDRAILS.md](GUARDRAILS.md) | safety rules, hard/soft stops, rollback procedures |
| [LOOP-PROMPT.md](LOOP-PROMPT.md) | the prompt the operator invokes |
| `phases/00-*.md` … `phases/10-*.md` | per-phase plans |
| `checkpoints/` | per-iteration snapshots (populated at runtime) |

## Bottom-Line Goal

Migrate the modifier overlay from overwrite-based (~49 carriers) to a three-mode model:

- **`mode: inject`** for carriers where modifier change is additive or anchor-targetable (~50–60% of current overwrites)
- **`mode: overwrite`** kept only where injection cannot apply (lib `*.cjs`, heavy restructures) — ~10–15%
- **`mode: add`** for modifier-owned net-new content (already correct posture)

Done when: the bootstrap gate reports zero `hard_failures`, all migrated carriers verify under both runtimes, and the `mode: inject` mechanism is documented in `AGENTS.md`/`CLAUDE.md` as a stable extension point.

## Authority And Cross-References

- [AGENTS.md](../../../AGENTS.md) — runtime-neutral governance (governs all initiative work)
- [CLAUDE.md](../../../CLAUDE.md) — Claude-side carrier
- [docs/handoff/current.md](../../../docs/handoff/current.md) — live operational state
- [.planning/readiness/release-readiness-orientation-2026-05-08.md](../../readiness/release-readiness-orientation-2026-05-08.md) — orientation evidence base
- [.planning/readiness/intervention-strategies-2026-05-08.md](../../readiness/intervention-strategies-2026-05-08.md) — agent-produced strategy analysis underlying this initiative

## Initiative Status

See [STATE.md](STATE.md) for live status. As of creation date (2026-05-08), the initiative is at Phase 0 Slice 0 (not started).

## What Makes This Self-Driving

The agent loop is designed so that any Claude Code session — fresh or resumed — can:

1. Read `STATE.md` to learn current position
2. Read `PROTOCOL.md` to learn the iteration recipe
3. Read `GUARDRAILS.md` to learn the safety envelope
4. Read the active phase's plan in `phases/`
5. Execute one bounded slice
6. Verify, commit, update state
7. Stop cleanly (the operator or the loop driver re-invokes for the next iteration)

When `STATE.md` says `status: complete`, the loop terminates.
