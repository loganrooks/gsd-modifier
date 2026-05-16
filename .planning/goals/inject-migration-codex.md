# Goal: Inject Migration Initiative (Codex variant)

Codex-runtime sibling of [`inject-migration.md`](inject-migration.md). Drives the same autonomous initiative at [`.planning/initiatives/inject-migration/`](../initiatives/inject-migration/INITIATIVE.md) under the Codex CLI's `/goal` feature instead of Claude Code's.

The initiative governance (STATE.md, GUARDRAILS.md, REVIEWERS.md, PROTOCOL.md, INITIATIVE.md, phase plans) is runtime-neutral and shared with the Claude variant. Only the agent-spawn mechanism and runtime-specific tool references differ.

## Context

| Field | Value |
|---|---|
| Workstream | Inject migration initiative |
| Workstream home | [`.planning/initiatives/inject-migration/`](../initiatives/inject-migration/) |
| Starting state (at goal invocation) | Whatever `STATE.md` reports; agent runs Cold Start reconciliation per `PROTOCOL.md`. |
| Terminates on | `Sentinel: INITIATIVE-COMPLETE`, `Sentinel: ABORTED`, any `HARD-STOP: <reason>` in turn output, or 300-turn safety cap |
| Operator presence required at | initial invocation (below), manual interrupt, hard-stop responses, final retrospective review |
| Required runtime | Codex CLI with `/goal` and subagent support; reviewer TOMLs present locally (see Prerequisites). |

## Prerequisites (one-time, per checkout)

REVIEWERS.md names reviewer agents — the Codex loop spawns them via two mechanisms depending on the reviewer:

**Codex-native subagents** (matching a TOML in `.codex/agents/` project-local or `~/.codex/agents/` user-level):

- `.codex/agents/trajectory-verifier.toml` — phase-boundary verifier
- `.codex/agents/gsd-debugger.toml` — gate-failure investigator (shipped with GSD; check it's present)

**Cross-vendor reviewer skills** (invoke an external CLI from Codex to preserve same-vendor reading on the artifact corpus):

- `.codex/skills/adversarial-cross-vendor-audit/SKILL.md` — dispatches the Claude `adversarial-auditor-xhigh` agent via `claude -p`. Used wherever REVIEWERS.md mandates `adversarial-auditor-xhigh`. The skill exists because the inject-migration artifact corpus is Claude-authored, and a Codex GPT-class auditor reviewing Claude artifacts is cross-vendor (weaker register-pattern catch). Shelling to `claude -p --agent adversarial-auditor-xhigh --effort xhigh` preserves the same-vendor read while letting Codex drive the loop.

**Codex built-ins** cover the lower-tier reviewer roles in REVIEWERS.md:

- `Explore` → Codex `explorer` built-in (read-only investigation)
- `Plan` → Codex `explorer` built-in with the REVIEWERS.md "Slice Ambiguity Resolution" template body inline. Claude's `Plan` is a built-in read-only investigator with a planning-focused prompt; nothing about it is model-specific or capability-specific that `explorer` doesn't cover. Pass the REVIEWERS.md template body verbatim as the prompt; `explorer` reads the cited code/docs and returns a recommendation backed by file:line evidence — same shape, same output contract.

If a required reviewer mechanism is missing when first invoked, the loop hard-stops. Cross-vendor skill prerequisites (`claude` CLI installed + authenticated, `~/.claude/agents/adversarial-auditor-xhigh.md` present) are verified by the skill itself per its `<prerequisites>` section. The TOMLs in `.codex/agents/` are gitignored (the `.codex/` tree is local-only per Codex install convention); if you wipe the directory, recreate from this initiative's git history.

## Read order before invocation (optional — the agent reads these per turn anyway)

1. [`STATE.md`](../initiatives/inject-migration/STATE.md) — current state (sentinel + phase + slice + counters)
2. [`GUARDRAILS.md`](../initiatives/inject-migration/GUARDRAILS.md) — 5 hard stops + reviewer-mediated continuation
3. [`REVIEWERS.md`](../initiatives/inject-migration/REVIEWERS.md) — reviewer roster + prompt templates + verdict semantics
4. [`PROTOCOL.md`](../initiatives/inject-migration/PROTOCOL.md) — turn-end discipline + reviewer spawning
5. [`INITIATIVE.md`](../initiatives/inject-migration/INITIATIVE.md) — mission, phase catalog, completion criteria

## /goal invocation (canonical)

Paste verbatim into a fresh Codex CLI session at `/home/rookslog/workspace/projects/gsd-modifier`:

```text
/goal The inject-migration initiative has reached a terminal or operator-required state. Specifically, the most recent agent turn output contains a [GOAL-EVAL] line whose `Sentinel:` field is INITIATIVE-COMPLETE or ABORTED, OR whose `Turn-end:` field begins with `hard-stop-`. The condition is also met if the turn cap of 300 turns is exceeded (runaway safety floor).

For each turn, the agent must:

1. Set working directory to /home/rookslog/workspace/projects/gsd-modifier
2. Read in order: .planning/initiatives/inject-migration/STATE.md, GUARDRAILS.md, REVIEWERS.md, PROTOCOL.md, the active phase plan in phases/
3. Run Cold Start reconciliation per PROTOCOL.md "Cold Start"
4. If Sentinel is INITIATIVE-COMPLETE or ABORTED: output [GOAL-EVAL] line and end turn
5. Otherwise identify the next pending slice from the active phase plan
6. Execute exactly one bounded slice per its slice spec
7. Run slice's verification gates; if fail, invoke auto-recovery per GUARDRAILS.md
8. If slice spec mandates a reviewer, dispatch per its mechanism: (a) for `adversarial-auditor-xhigh` invocations, invoke the `.codex/skills/adversarial-cross-vendor-audit/` skill which shells out to `claude -p --agent adversarial-auditor-xhigh --effort xhigh` and parses the returned verdict block (preserves same-vendor read on Claude-authored artifacts); (b) for `trajectory-verifier`, `gsd-debugger`, or other Codex-native reviewers, spawn via Codex subagent — describe the task in natural language to the parent agent, name the reviewer (matches `.codex/agents/<name>.toml`), include the REVIEWERS.md prompt-template body filled in, and parse the reviewer's returned VERDICT/REASONING/RECOMMENDATION/EVIDENCE block per REVIEWERS.md verdict semantics. Where REVIEWERS.md gives the Claude-flavored example `Agent({subagent_type: '<reviewer>', description: '...', prompt: '<input>'})`, the Codex-native equivalent is natural-language delegation: "Spawn the `<reviewer>` subagent with the following input: <input>". Codex's max concurrent subagents is controlled by `agents.max_threads` in `~/.codex/config.toml`.
9. At phase boundary (last slice of phase commits), spawn trajectory-verifier in a separate turn
10. Commit with Why/Verification/Boundary body, Initiative: trailer, and Reviewer: trailer if applicable
11. Update STATE.md atomically per PROTOCOL.md "State-Update Protocol"
12. Write checkpoint to checkpoints/<UTC-timestamp>-phase<NN>-slice<MM>.md per template
13. Output the [GOAL-EVAL] line on its own; end the turn

Discipline:
- Exactly one slice per turn
- Reviewer verdicts are mandatory at the gates declared in REVIEWERS.md
- Hard-stops (5 conditions in GUARDRAILS.md) emit HARD-STOP: <reason> and end the turn
- Forbidden actions (15 in GUARDRAILS.md) are never taken regardless of reviewer recommendation
- The `adversarial-auditor-xhigh` reviewer is dispatched via the `adversarial-cross-vendor-audit` skill which shells to `claude -p --agent adversarial-auditor-xhigh --effort xhigh`. From the artifact's perspective, the reviewer is still Claude Opus reading Claude-authored prose (same-vendor read preserved). The "cross-vendor" in the skill's name refers only to the dispatcher → reviewer hop (Codex CLI → Claude CLI). Each audit costs Anthropic API tokens; track aggregate spend in STATE.md if budget pressure becomes a constraint.

Or stop after 300 turns.
```

## Status check (read-only, no advancement)

While the goal is running, the Codex CLI's `/goal` status command (analog of Claude's `/goal` with no args) returns the condition, elapsed time, turn count, token spend, and evaluator's most recent reasoning. Exact syntax may differ — check `codex --help` or `/goal --help`.

## Manual interrupt

`/goal clear` (or Codex's equivalent — aliases may include `stop`, `off`, `reset`, `none`, `cancel`). Or Ctrl+C in interactive mode.

After interrupt, the most-recent checkpoint records where the loop stopped; re-pasting the `/goal` block above will resume from that state via Cold Start reconciliation.

## Resume after hard-stop

If the goal terminated due to a `HARD-STOP:` line:

1. Read `STATE.md → Status` (should be `paused-for-operator`)
2. Read the most-recent checkpoint's `## Question for operator` section
3. Address the question — edit the slice spec / phase plan / governance carrier as needed (operator-only); or accept the diagnosis and approve a recovery action
4. Update `STATE.md → Status` from `paused-for-operator` back to `pending`
5. Re-invoke `/goal` with the same block above
6. Next turn fires Cold Start, sees `success` checkpoint status, proceeds

Full recovery flow: [`LOOP-PROMPT.md → Resume After Hard-Stop`](../initiatives/inject-migration/LOOP-PROMPT.md).

## Resume after abort

To resume from `Sentinel: ABORTED`, edit STATE.md → Sentinel back to a non-terminal value (operator-only), then re-invoke `/goal` above. See [`LOOP-PROMPT.md → Resume After Abort`](../initiatives/inject-migration/LOOP-PROMPT.md) for the full procedure.

## Cross-runtime divergence notes

This Codex variant differs from the Claude variant ([`inject-migration.md`](inject-migration.md)) in exactly these places:

- **Step 8 spawn mechanism**: Codex uses two paths — (1) Codex-native subagents via natural-language description to the parent (`trajectory-verifier`, `gsd-debugger`), and (2) cross-vendor skills via shell-out to `claude -p` (`adversarial-cross-vendor-audit` for `adversarial-auditor-xhigh`). Claude uses a single path: `Agent({subagent_type, ...})` for all reviewers.
- **Reviewer carriers**: Codex requires local `.codex/agents/*.toml` (for native subagents) + `.codex/skills/*/SKILL.md` (for cross-vendor dispatch); Claude requires `~/.claude/agents/*.md`. None ship with the modifier — all are operator-local.
- **Adversarial auditor vantage**: BOTH runtimes end up with Claude Opus reading Claude-authored artifacts (same-vendor read), because the Codex variant's skill shells to `claude -p`. The Codex path adds a network round-trip + Anthropic API spend; the Claude path uses Claude Code's in-session Agent tool. Substance of the read is equivalent.
- **Plan reviewer**: Claude's `Plan` is a system built-in read-only investigator with a planning-focused prompt — nothing model-specific. Codex's `explorer` built-in covers the same role; pass the REVIEWERS.md "Slice Ambiguity Resolution" template body verbatim as the prompt. Phase 2-3 work has not invoked `Plan`, but the mapping is in place if it fires.
- **Cost model**: Codex loops pay Anthropic API spend for each `adversarial-auditor-xhigh` invocation (estimated $0.50–$5 per single-artifact audit; $10 cap per invocation in the skill default). Claude loops use the operator's Claude Code subscription/credit balance — same underlying cost basis but different metering surface.

Everything else — STATE.md mechanics, slice protocol, hard-stop conditions, verification gates, commit hygiene, checkpoint template — is runtime-neutral and identical across the two variants. If a divergence beyond the list above emerges during use, treat it as a finding and surface it to the operator.

## See also

- [`inject-migration.md`](inject-migration.md) — Claude variant of this goal
- [`LOOP-PROMPT.md`](../initiatives/inject-migration/LOOP-PROMPT.md) — initiative's operator-facing invocation surface (status check, manual interrupt, halt, fallback manual single-turn prompt)
- [`README.md`](README.md) — goal prompts registry convention
