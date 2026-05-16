### Researcher -> Planner (via RESEARCH.md)

| Field / Section | Required | Description |
|-----------------|----------|-------------|
| `## User Constraints` | Yes when CONTEXT.md exists | Locked decisions, discretion areas, and deferred ideas copied from CONTEXT.md |
| `## Research Disposition` | Yes when anything remains open, escalated, intentionally preserved, or inconclusive | Names what planning may treat as settled versus what it must still carry forward |
| `## Standard Stack` | Yes | Libraries/tools planning should prefer |
| `## Architecture Patterns` | Yes | Structural guidance and anti-patterns |
| `## Common Pitfalls` | Yes | Things verification and task design should guard against |
| `## Sources` | Yes | Confidence-bearing provenance for research claims |

### Planner -> Executor (via PLAN.md)

| Field | Required | Description |
|-------|----------|-------------|
| Frontmatter | Yes | phase, plan, type, wave, depends_on, files_modified, autonomous, requirements |
| `future_preservation` | Yes when CONTEXT future-awareness is non-empty | Preserved seams, explicit non-decisions, posture assumptions, and strengthening routes |
| `<objective>` | Yes | What the plan achieves |
| `<tasks>` | Yes | Ordered task list with type, files, action, verify, acceptance_criteria |
| `<verification>` | Yes | Overall verification steps |
| `<success_criteria>` | Yes | Measurable completion criteria |

### Executor -> Verifier (via SUMMARY.md)

| Field | Required | Description |
|-------|----------|-------------|
| Frontmatter | Yes | phase, plan, subsystem, tags, key-files, metrics |
| `completion_mode` | Yes | `clean_execution` or `debt_carrying_execution` so downstream consumers know whether execution itself carried known debt before verification |
| `completion_debt` | Yes when `completion_mode=debt_carrying_execution` | Structured reasons carried out of execution (auth gates, intentional stubs, failed self-check, other known debt) |
| Commits table | Yes | Per-task commit hashes and descriptions |
| Deviations section | Yes | Auto-fixed issues or "None" |
| Self-Check | Yes | PASSED or FAILED with details |

### Verifier -> Routing (via VERIFICATION.md)

| Field | Required | Description |
|-------|----------|-------------|
| `status` | Yes | `passed`, `gaps_found`, or `human_needed` |
| `completion_mode` | Yes | `clean_completion` or `debt_carrying_completion`; distinguishes clean closure from accepted or unresolved carried debt |
| `debt_bearing` | Yes | Boolean mirror of `completion_mode` for consumers that only need a quick debt flag |
| `overrides_applied` | Yes | Count of accepted verification overrides contributing to the final result |
| `future_preservation_review` | Yes when any source PLAN carries `future_preservation` | Structured verifier review of whether preserved seams, explicit non-decisions, posture assumptions, and strengthening routes were carried, thinned, or still need human judgment |
| `gaps` / `human_verification` | Yes when applicable | Structured downstream debt details for routing and planning |
