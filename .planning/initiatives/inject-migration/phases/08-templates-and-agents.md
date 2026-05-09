# Phase 8 — Templates and Agents

ID: `08-templates-and-agents`
Status: `pending`
Dependencies: Phase 6 complete (Phase 7 may be deferred — this phase does not depend on Phase 7's outcome)
Approval gates: per-file decision gate (each template / agent gets explicit operator decision)

## Objective

Evaluate the 7 overwrite-mode templates and 4 overwrite-mode agent .md files for migration to `mode: inject`. Migrate carriers where injection is clean; document carriers that intentionally stay overwrite.

## Rationale

Templates and agents have different characteristics from workflows:

- **Templates**: smaller files (typically <100 lines); often modifier-substantially-rewritten rather than additive (e.g., `phase-prompt.md`, `verification-report.md`). Many will likely stay overwrite.
- **Agent .md files**: 4 carriers (`gsd-code-fixer`, `gsd-code-reviewer`, `gsd-intel-updater`, `gsd-pattern-mapper`); 200–600 lines each; have a 269-line diff in at least one case (per intervention-strategies §1.7). Mostly behavioral prompts; modifier additions are typically `<additional_instructions>` style blocks.

The phase decides per-file rather than uniformly applying inject. A carrier moves to inject only if the operations express the modifier intent simply.

## Approach

Multi-slice with per-file decision gates:

- Slice 1: triage all 11 carriers (7 templates + 4 agents); produce a triage doc with per-file recommendation
- Slices 2–N: one design + apply per "migrate" recommendation; per-file decision-recording slice for "keep overwrite" recommendations
- Final slice: phase debrief

The slice count varies based on the triage. Estimate 8–14 slices total.

## Slice Catalog

### Slice 1 — Triage all 11 carriers

- **Status**: `[ ]`
- **Write set**: `.planning/initiatives/inject-migration/decisions/PHASE-08-triage.md`
- **Required content**:
  - For each of 11 carriers (7 templates + 4 agents):
    - Path, parity_tier, current mode
    - Diff line count vs upstream (cite intervention-strategies §1.7 if applicable)
    - Diff character: pure-additive | block-replace | section-replace | step-level | substantial-rewrite | trivial
    - Recommendation: `migrate-clean` (inject easily expresses), `migrate-with-block-replace` (use the block_replace operation; OK), `keep-overwrite` (modifier rewrites too much), `keep-modifier-owned` (already mode: add — exclude from this phase)
  - Suggested ordering: migrate-clean candidates first, then migrate-with-block-replace, then record keep-overwrite decisions
- **Approach**:
  1. Read each carrier's overlay version + upstream version (use `git show origin/main:<path>`)
  2. Classify each
  3. Record recommendation
- **Verification**: per-slice gates
- **Commit**: `docs(initiative): triage templates and agents for phase 08`

### Slices 2 through N — Per-carrier action

For each carrier with `migrate-clean` or `migrate-with-block-replace` recommendation: design slice + apply slice (Phase 5 pattern).

For each carrier with `keep-overwrite` recommendation: one decision-recording slice.

The agent reads the triage doc to determine the order and slice count. Each carrier slice pair commits its outcome (migration or decision-recorded). If a "migrate-clean" turns out hard during design, the design slice can transition the carrier to "keep-overwrite" without escalation; the apply slice then becomes the decision-recording slice.

### Final slice — Phase debrief

- **Write set**: `.planning/initiatives/inject-migration/decisions/PHASE-08-debrief.md`
- **Required**: per-carrier outcome (migrated / kept overwrite); reasoning summary; total inject carrier count; recommendations for Phase 9
- **Verification**: state-mutating gates
- **Commit**: `docs(initiative): phase 08 debrief and template/agent migration outcomes`

## Exit Criteria (phase boundary)

1. All 11 carriers (templates + agents) have an explicit recommendation in the triage doc and a recorded outcome (migrated or kept-overwrite)
2. Migrated carriers verify under both runtimes
3. Bootstrap gate green; `hard_failures: []`
4. STATE.md → Phase 8 `[x]`; advance to Phase 9
5. Counters: agent migrations and template migrations recorded

## Boundary

- This phase covers 7 templates + 4 agents = 11 carriers exactly. Other modifier-owned files are out of scope.
- If a template/agent has been substantially refactored upstream since the modifier's last sync, the design slice may surface a content-resync need. That's a separate concern; the inject migration goes ahead with current modifier content.
- Agents `.toml` files (codex-only) stay `mode: add` — they're modifier-net-new for codex routing.

## Risks (phase-level)

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Triage misclassifies a carrier (e.g., flags as `migrate-clean` when it actually needs substantial-rewrite) | medium | low | per-carrier design slice catches; falls back to `keep-overwrite` |
| Several agent .md files have the same kind of additive block (`<additional_instructions>`); migrating each separately is repetitive | medium | low | acceptable; consistency is more valuable than DRY here |
| Phase 8's slice count is unpredictable | high | low | the triage in Slice 1 produces the count |
| A template's content is functionally inseparable from its position in the upstream file (e.g., must be at exact line N) | low | medium | rare; if surfaces, keep-overwrite |

## Notes For Future Iterations

- Phase 8 produces an honest "what stays overwrite forever" set. That set + the 5 lib `.cjs` files + (potentially) some Phase 7 carriers comprise the documented bounded overwrite list at initiative end.
- The triage doc becomes the authoritative reference for "why does carrier X stay overwrite?" — Phase 10 closeout cites it.
