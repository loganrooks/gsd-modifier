Preserve continuity for an active engineering session in this repo.

Produce a compact replacement history that is concise but operationally faithful.

Prioritize, in order:

1. the active control surface and its exact entrypoint path
2. the exact files that must be reopened first
3. the current task and immediate next action
4. current blockers, open findings, unresolved questions, and open opportunities
5. current branch/worktree/session boundaries if they matter
6. the latest meaningful commit or checkpoint boundary if it is load-bearing
7. recent lessons learned, failed approaches, and mistakes not to repeat if they still constrain the next move
8. user corrections or policy changes that changed how the work must proceed
9. distinctions that must not flatten in summary:
   - decided vs open
   - active vs parked
   - canon vs exploratory or audit
   - repo-local evidence vs upstream/external evidence
   - current task vs deferred follow-up
   - committed vs uncommitted
   - this worktree's scope vs parallel workers' scopes

Prefer exact repo file paths over vague prose.

When the active control surface is planning, doctrine, or phase work, preserve explicitly:

- `.planning/PROJECT.md`
- `.planning/ROADMAP.md`
- `.planning/REQUIREMENTS.md`
- `.planning/LONG-ARC.md`
- `.planning/STATE.md`
- the active phase, audit, or research entrypoint relevant to the current task

If the active control surface is a package or lane under `.planning/`, preserve:

- the package or lane entrypoint path
- the minimum reread order
- the current status or state file
- the current checkpoint, gate, or lane disposition if one exists
- any files that must be updated after the next meaningful action

If the session includes external CLI runs, subagents, or background processes, preserve only:

- whether they are still alive
- exact output, log, or artifact paths if they still matter
- the next decision needed about them

If the session exposed a real failure mode or operator correction, preserve it tersely as:

- `lesson learned`
- `avoid repeating`
- `replacement approach`

Do not waste space on:

- pleasantries
- generic transcript retelling
- stale rejected branches
- raw log chatter unless it is still diagnostic

If the session is currently centered on the Phase 01 readiness package, preserve that package explicitly rather than flattening it into the general project summary.

If there is uncertainty, preserve it as uncertainty. Do not make open questions sound settled.
