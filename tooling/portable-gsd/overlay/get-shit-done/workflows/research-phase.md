<purpose>
Research how to implement a phase. Spawns gsd-phase-researcher with phase steering context.

Standalone research command. For most workflows, use `/gsd-plan-phase` which integrates research automatically.
</purpose>

<available_agent_types>
Valid GSD subagent types (use exact names — do not fall back to 'general-purpose'):
- gsd-phase-researcher — Researches technical approaches for a phase
</available_agent_types>

<process>

## Step 0: Resolve Model Profile

@__PROJECT_ROOT__/.codex/get-shit-done/references/model-profile-resolution.md

Resolve model for:
- `gsd-phase-researcher`

## Step 1: Normalize and Validate Phase

@__PROJECT_ROOT__/.codex/get-shit-done/references/phase-argument-parsing.md

```bash
PHASE_INFO=$(node "__PROJECT_ROOT__/.codex/get-shit-done/bin/gsd-tools.cjs" roadmap get-phase "${PHASE}")
```

If `found` is false: Error and exit.

## Step 2: Check Existing Research

```bash
ls .planning/phases/${PHASE}-*/RESEARCH.md 2>/dev/null || true
```

If exists: Offer update/view/skip options.

## Step 3: Gather Phase Context

```bash
INIT=$(node "__PROJECT_ROOT__/.codex/get-shit-done/bin/gsd-tools.cjs" init phase-op "${PHASE}")
if [[ "$INIT" == @file:* ]]; then INIT=$(cat "${INIT#@file:}"); fi
# Extract: phase_dir, padded_phase, phase_number, state_path, requirements_path, context_path
AGENT_SKILLS_RESEARCHER=$(node "__PROJECT_ROOT__/.codex/get-shit-done/bin/gsd-tools.cjs" agent-skills gsd-researcher 2>/dev/null)
```

If `context_path` exists, resolve the `<canonical_refs>` entries in `CONTEXT.md` into a deduplicated internal `context_canonical_refs` list and include those files in the researcher's `<files_to_read>` block below when they exist in the repo.

## Step 4: Spawn Researcher

```
Task(
  prompt="<objective>
Research implementation approach for Phase {phase}: {name}
Treat CONTEXT.md as a steering brief, not just a list of locked choices.
</objective>

<files_to_read>
- {context_path} (Phase steering brief from /gsd-discuss-phase — decisions, assumptions, open questions, future awareness)
- {requirements_path} (Project requirements)
- {state_path} (Project decisions and history)
- {context_canonical_refs} (Resolved files from CONTEXT.md `<canonical_refs>` — MUST be read when present)
</files_to_read>

${AGENT_SKILLS_RESEARCHER}

<additional_context>
Phase description: {description}

Research guidance:
- Respect locked decisions in `<decisions>`
- Treat `<working_model>` and `<open_questions>` as things to investigate, validate, or narrow
- Treat `<derived_constraints>` and `<future_awareness>` as implementation guardrails
- Treat `Protected Seams` as things research should preserve unless evidence forces a different conclusion
- Treat `Explicit Non-Decisions` as intentionally open rather than accidentally missing
- Treat `Current Posture` as a real trust/visibility/service constraint
- Use `Future Shape Notes` to inform seams and interfaces without pulling future scope into the current phase
- Treat `<epistemic_guardrails>` as standards for how much confidence/evidence the research should establish
</additional_context>

<output>
Write to: .planning/phases/${PHASE}-{slug}/${PHASE}-RESEARCH.md
</output>",
  subagent_type="gsd-phase-researcher",
  model="{researcher_model}"
)
```

## Step 5: Handle Return

- `## RESEARCH COMPLETE` — Display summary and disposition accounting, offer: Plan/Dig deeper/Review/Done
- `## CHECKPOINT REACHED` — Present to user, spawn continuation
- `## RESEARCH BLOCKED` — Show attempts, offer: Add context/Try different mode/Manual

When research completes with preserved non-decisions or inconclusive items, do not treat that as a failure by default. Carry those items forward into planning as named consequences rather than forcing fake closure.

</process>
