# Goal: Inject Migration Comparative Uplift Review

Drives a proposal-only initiative that compares the substantive content of this repo's `inject-migration` uplift against the F1 Modeling Lab local GSD uplift proposal at `/home/rookslog/workspace/projects/f1-modeling/.planning/initiatives/gsd-local-migration-plus-uplift-2026-05/`.

The review is about **content**, not form. It should identify what is actually being proposed for uplift in each initiative, what modifications are implied, which F1 proposal ideas should be borrowed into `gsd-modifier`, and whether each borrowing should be adopted as-is, adapted, deferred, or rejected.

## Context

| Field | Value |
|---|---|
| Workstream | Inject migration comparative uplift review |
| Primary repo | `/home/rookslog/workspace/projects/gsd-modifier` |
| Local source initiative | `.planning/initiatives/inject-migration/` |
| Comparator initiative | `/home/rookslog/workspace/projects/f1-modeling/.planning/initiatives/gsd-local-migration-plus-uplift-2026-05/` |
| Output directory | `.planning/initiatives/inject-migration-comparative-uplift-review/` |
| Required output | `.planning/initiatives/inject-migration-comparative-uplift-review/UPLIFT-BORROWING-PROPOSAL.md` |
| Out of scope | implementation, manifest edits, contract code edits, overlay edits, governance edits outside the output directory |

## /goal invocation

Paste verbatim into a fresh Codex CLI or Claude Code session at `/home/rookslog/workspace/projects/gsd-modifier`:

```text
/goal The inject-migration comparative uplift review has reached a terminal state. Specifically, the most recent agent turn output contains a [GOAL-EVAL] line whose `Sentinel:` field is PROPOSAL-COMPLETE or ABORTED, OR whose `Turn-end:` field begins with `hard-stop-`. The condition is also met if the turn cap of 20 turns is exceeded.

For each turn, the agent must:

1. Set working directory to `/home/rookslog/workspace/projects/gsd-modifier`.
2. Treat this as a proposal-only review. Do not modify runtime, overlay, contract, bootstrap, manifest, AGENTS.md, CLAUDE.md, WORKFLOW.md, docs/handoff/current.md, `.planning/STATUS.md`, or `.planning/CURRENT-STATE.md`.
3. Write only inside `.planning/initiatives/inject-migration-comparative-uplift-review/` unless the operator explicitly authorizes more.
4. Read the local governing surfaces:
   - `AGENTS.md`
   - `docs/handoff/current.md`
   - `.planning/CURRENT-STATE.md`
   - `.planning/STATUS.md`
5. Read the local inject-migration content surfaces:
   - `.planning/initiatives/inject-migration/INITIATIVE.md`
   - `.planning/initiatives/inject-migration/STATE.md`
   - `.planning/initiatives/inject-migration/decisions/ADR-001-manifest-schema-v4.md`
   - `.planning/initiatives/inject-migration/phases/03-pilot.md`
   - `.planning/initiatives/inject-migration/phases/04-first-wave-references.md`
   - `.planning/initiatives/inject-migration/phases/05-second-wave-additive-workflows.md`
   - `.planning/initiatives/inject-migration/phases/06-third-wave-step-level.md`
   - `.planning/initiatives/inject-migration/phases/07-fourth-wave-large-workflows.md`
   - `.planning/initiatives/inject-migration/phases/08-templates-and-agents.md`
   - `.planning/readiness/intervention-strategies-2026-05-08.md`
   - `.planning/readiness/release-readiness-orientation-2026-05-08.md`
6. Read the F1 comparator surfaces:
   - `/home/rookslog/workspace/projects/f1-modeling/.planning/initiatives/gsd-local-migration-plus-uplift-2026-05/UPLIFT-PROPOSAL.md`
   - `/home/rookslog/workspace/projects/f1-modeling/.planning/initiatives/gsd-local-migration-plus-uplift-2026-05/UPLIFT-REVIEW-2026-05-16.md`
   - `/home/rookslog/workspace/projects/f1-modeling/.planning/initiatives/gsd-local-migration-plus-uplift-2026-05/codex-prompt-uplift-proposal.md`
   - `/home/rookslog/workspace/projects/f1-modeling/.planning/initiatives/gsd-local-migration-plus-uplift-2026-05/codex-prompt.md`
   - `/home/rookslog/workspace/projects/f1-modeling/.planning/initiatives/gsd-local-migration-plus-uplift-2026-05/CLAUDE-DESIGN-GUIDE.md`
7. Review content, not form. Do not score whether the F1 proposal has a nicer section structure. Extract what it proposes to change: artifact inputs, workflow/agent/template modifications, verification semantics, design-intake lane, tests, optional config/file-presence gates, upstream-compatible vs project-local split, and review revisions.
8. Extract what `inject-migration` proposes to uplift: schema v4, `mode: inject`, operation kinds, marker/idempotency contract, apply/verify semantics, `parity_intent`, carrier wave plan, bounded overwrite doctrine, runtime verification, and operator/audit obligations.
9. Produce a borrowing/disposition analysis. For each F1 idea that could matter to `gsd-modifier`, classify it as exactly one:
   - `borrow_as_is`
   - `borrow_with_modification`
   - `defer_until_after_inject_pilot`
   - `reference_only`
   - `reject`
10. For every `borrow_with_modification`, state precisely what changes in translation from F1 to `gsd-modifier`. Avoid importing F1 product doctrine or Formula 1-specific language. Extract generic GSD/uplift mechanics only.
11. For every `reject`, state whether the rejection is because it is F1-specific, conflicts with `gsd-modifier` scope, reintroduces GSDR-style machinery, duplicates existing inject-migration work, or belongs to a separate future initiative.
12. Draft `.planning/initiatives/inject-migration-comparative-uplift-review/UPLIFT-BORROWING-PROPOSAL.md`.
13. The proposal must be usable by a future agent without chat context and must contain:
    - Executive summary: the recommended borrowing stance.
    - Scope and non-goals: content review only; no implementation.
    - Source grounding: what was read and any stale/uncertain surfaces.
    - F1 uplift content map: UPLIFT-01..UPLIFT-11 summarized by substantive proposed modification.
    - Inject-migration content map: local uplift items summarized by substantive proposed modification.
    - Comparative findings: where the initiatives overlap, diverge, or expose gaps in each other.
    - Borrowing disposition table: F1 idea, local relevance, disposition, translation needed, target local surface, verification need.
    - Proposed local uplift proposal for `gsd-modifier`: numbered `IM-UPLIFT-XX` records describing what should be added to the inject-migration proposal layer or future overlay/uplift roadmap.
    - Explicit "do not borrow" section.
    - Open questions for the operator before adopting any borrowed item.
    - Suggested next action: approve proposal, revise proposal, or reject/park.
14. The `IM-UPLIFT-XX` records must be concrete. Each record must include:
    - What is being uplifted.
    - Why it matters for `gsd-modifier`.
    - Whether it modifies current `inject-migration` scope, Phase 3+ planning, future closeout docs, or a separate future initiative.
    - Which existing local artifacts would be touched if later approved.
    - Verification that would be required if later implemented.
    - Boundary: what is intentionally not included.
15. Required analysis questions:
    - Should `gsd-modifier` borrow F1's optional `project_doctrine` lane as an overlay capability, or treat it as a comparator-only local patch? Explain.
    - Should `inject-migration` add a first-class proposal artifact like F1's UPLIFT-PROPOSAL, or is ADR-001 plus phase plans enough? Explain in content terms, not form terms.
    - Does F1's `project_doctrine` chain reveal missing consumers in `inject-migration` (for example verifier, installer, docs, canary, or test consumers)?
    - Does `inject-migration` have an equally explicit upstream-compatible vs modifier-specific split? If not, what should be added?
    - Which F1 review revisions map to local inject concerns? For example, "separate related but distinct doctrines" maps to mechanism vs maintenance goal vs bounded-overwrite doctrine vs runtime-parity obligation.
    - Which ideas must wait until Phase 3 pilot evidence exists?
16. Cite sources with file paths and line ranges where possible. If a claim is inferred, label it `[inferred]`.
17. Before finishing, cold-read the proposal as a fresh future maintainer. Fix any section that assumes chat context.
18. Run `git diff --check` before completing. Do not run state-mutating bootstrap or materialization gates.
19. Output a final [GOAL-EVAL] line on its own; end the turn.

Hard stops:

- If the F1 comparator directory is missing, emit `HARD-STOP: missing-f1-comparator`.
- If local inject-migration source files are missing or contradictory enough that no grounded comparison is possible, emit `HARD-STOP: missing-local-source`.
- If producing the proposal would require editing outside `.planning/initiatives/inject-migration-comparative-uplift-review/`, emit `HARD-STOP: write-scope-expansion-required`.
- If the worktree contains unrelated dirty files that would be overwritten, emit `HARD-STOP: worktree-drift`.

Discipline:

- Proposal only.
- Content over form.
- No implementation.
- No F1-specific doctrine imported as local truth.
- Do not collapse mechanism, maintenance goal, bounded-overwrite doctrine, runtime parity, and upstreamability into one category.
- Prefer exact borrowing dispositions over vague "learn from this" language.
- If the review spans multiple turns, write or update `.planning/initiatives/inject-migration-comparative-uplift-review/CHECKPOINT.md` before ending each non-terminal turn.

Or stop after 20 turns.
```

## Expected Output

The goal should produce:

- `.planning/initiatives/inject-migration-comparative-uplift-review/UPLIFT-BORROWING-PROPOSAL.md`
- Optional `.planning/initiatives/inject-migration-comparative-uplift-review/CHECKPOINT.md` if the run spans multiple turns

It should not produce code, manifest, overlay, contract, bootstrap, or governance changes.

## Review Standard

The output is acceptable only if a future maintainer can answer:

1. What exactly did F1 propose to uplift?
2. What exactly does `inject-migration` propose to uplift?
3. Which F1 ideas should `gsd-modifier` borrow?
4. Which should be modified, rejected, or deferred?
5. What concrete local proposal should be approved or revised next?
