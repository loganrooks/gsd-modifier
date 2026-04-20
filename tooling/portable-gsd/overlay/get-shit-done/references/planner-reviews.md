# Reviews Mode — Planner Reference

Triggered when orchestrator sets Mode to `reviews`. Replanning from scratch with REVIEWS.md feedback as additional context.

**Mindset:** Fresh planner with review insights — not a surgeon making patches, but an architect who has read peer critiques.

### Step 1: Load REVIEWS.md
Read the reviews file from `<files_to_read>`. Parse:
- Per-reviewer feedback (strengths, concerns, suggestions)
- Review Consumer Contract:
  - Must Address In Replan
  - Explicit Rebuttal Required If Not Accepted
  - Safe To Defer
- Review Synthesis:
  - Agreed Concerns
  - Lone High-Signal Concerns
  - Merely Adequate Areas
  - Later Audit Risks
  - Divergent Views
- Treat synthesis as guidance, not as permission to ignore a strong individual criticism.
- If the consumer-contract section is missing or incomplete, derive the same buckets from the individual reviews and synthesis instead of downgrading the review pass.

### Step 2: Categorize Feedback
Group review feedback into:
- **Must address**:
  - Every item in `Must Address In Replan`
  - HIGH severity agreed concerns
  - Any lone high-signal criticism that is well-justified and would create likely later-audit failure if ignored
  - Later audit risks or merely-adequate areas that would leave the plan weak, misleadingly closure-ready, or brittle against the repo quality bar if left untouched
- **Should address**:
  - MEDIUM severity agreed concerns
  - Merely adequate areas that leave the plan technically passable but weak for the repo's quality bar, when they are not already in Must address
- **Consider**:
  - Items listed in `Safe To Defer`
  - Individual reviewer suggestions that are useful but not load-bearing
  - LOW severity items
- **Explicit rebuttal required**:
  - Every item in `Explicit Rebuttal Required If Not Accepted`
- Consensus raises confidence, but lack of consensus does not automatically downgrade a criticism.

### Step 3: Plan Fresh with Review Context
Create new plans following the standard planning process, but with review feedback as additional constraints:
- Each must-address concern MUST have a task that addresses it or an explicit written rebuttal for why the criticism is not accepted
- MEDIUM concerns and merely-adequate areas should be addressed where feasible without over-engineering
- Note in task actions: "Addresses review concern: {concern}" for traceability
- If you reject a lone high-signal criticism, explain why the criticism is not persuasive; do not dismiss it solely because only one reviewer raised it
- Do not leave the existing plans materially unchanged unless you can point to the exact existing plan/task that already satisfies each must-address concern
- If a concern is already covered, say exactly which plan/task covers it instead of silently assuming coverage

### Step 4: Return
Use standard PLANNING COMPLETE return format, adding a reviews section:

```markdown
### Review Feedback Addressed

| Concern | Source | Severity | How Addressed |
|---------|--------|----------|---------------|
| {concern} | {reviewer or synthesis section} | HIGH | Plan {N}, Task {M}: {how} |

### Review Feedback Deferred
| Concern | Source | Reason |
|---------|--------|--------|
| {concern} | {reviewer or synthesis section} | {why — safe to defer or intentionally sequenced out} |

### Review Feedback Rejected
| Concern | Source | Reason |
|---------|--------|--------|
| {concern} | {reviewer or synthesis section} | {why the criticism was not accepted on the merits} |
```
