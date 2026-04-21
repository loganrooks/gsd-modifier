<purpose>
Verify phase goal achievement through goal-backward analysis. Check that the codebase delivers what the phase promised, not just that tasks completed.

This overlay copy also preserves verifier-side lifecycle carry: when plans record `future_preservation`, verification must review whether preserved seams, explicit non-decisions, posture assumptions, and strengthening routes were actually carried through execution.
</purpose>

<required_reading>
@/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/templates/verification-report.md
@/home/rookslog/workspace/projects/prix-guesser/.codex/get-shit-done/references/verification-patterns.md
</required_reading>

<process>

<step name="load_context">
Load the phase goal, plans, summaries, and requirements. If a `CONTEXT.md` exists in the phase directory, read it as supporting evidence, but treat plan `future_preservation` as the normalized verifier-side carry contract.
</step>

<step name="establish_must_haves">
Verify roadmap success criteria and plan-level must-haves. Plans may add detail; they do not narrow the roadmap contract.
</step>

<step name="load_future_preservation">
If any source plan carries `future_preservation`, extract and review these buckets:
- `protected_seams`
- `non_decisions`
- `posture_assumptions`
- `strengthening_routes`

If no source plan carries it, omit the carry review for this phase.
</step>

<step name="verify_present_tense_goal">
Run the usual verifier chain:
- observable truths
- artifacts
- key links
- requirements coverage
- behavioral checks
- anti-pattern scan
- test-quality audit
</step>

<step name="verify_future_preservation">
When `future_preservation` exists, verify whether execution preserved planning carry instead of only achieving current behavior.

Use these carry review statuses:
- `carried`
- `thinned`
- `uncertain`

Review prompts:
- `protected_seams`: was the intended boundary preserved or silently collapsed?
- `non_decisions`: was the choice kept open or silently fixed?
- `posture_assumptions`: does the implemented result still match the planned posture?
- `strengthening_routes`: was the route realized, or explicitly held-and-seeded?

Treat `thinned` items as real verification concerns. Treat `uncertain` items as human-judgment surfaces.
</step>

<step name="determine_status">
Status ordering stays strict:
1. `gaps_found` when present-tense verification fails or any future-preservation item is `thinned`
2. `human_needed` when human verification is required or any future-preservation item is `uncertain`
3. `passed` only when both present-tense and future-preservation review are clear
</step>

<step name="create_report">
Create `VERIFICATION.md` using the current verification-report template.
When future-preservation review ran, include:
- structured frontmatter summary under `future_preservation_review`
- body table showing carried / thinned / uncertain items
</step>

</process>

<success_criteria>
- [ ] Goal-backward present-tense verification completed
- [ ] `future_preservation` loaded when present
- [ ] Future-preservation carry reviewed when loaded
- [ ] `VERIFICATION.md` captures both present-tense result and future-preservation carry result
</success_criteria>
