# Verification Report Template

Template for `.planning/phases/XX-name/{phase_num}-VERIFICATION.md`.

This overlay copy preserves verifier-side lifecycle carry. When any source plan carries `future_preservation`, the report should capture whether that planning carry remained visible through execution and verification.

---

## File Template

```markdown
---
phase: XX-name
verified: YYYY-MM-DDTHH:MM:SSZ
status: passed | gaps_found | human_needed
completion_mode: clean_completion | debt_carrying_completion
debt_bearing: true | false
score: N/M must-haves verified
overrides_applied: 0
future_preservation_review: # Only if any source PLAN carries future_preservation
  status: carried | carry_gaps_found | human_judgment_needed
  reviewed_items: 0
  carried_items: 0
  carry_gaps: []
  human_items: []
re_verification: # Only if previous VERIFICATION.md existed
  previous_status: gaps_found
  previous_score: 2/5
  gaps_closed: []
  gaps_remaining: []
  regressions: []
gaps: # Only if status: gaps_found
  - truth: "Observable truth that failed"
    status: failed
    reason: "Why it failed"
    artifacts:
      - path: "src/path/to/file.tsx"
        issue: "What's wrong"
    missing:
      - "Specific thing to add/fix"
deferred: # Only if deferred items exist
  - truth: "Observable truth addressed in a later phase"
    addressed_in: "Phase N"
    evidence: "Matching roadmap text"
human_verification: # Only if status: human_needed
  - test: "What to do"
    expected: "What should happen"
    why_human: "Why can't verify programmatically"
---

# Phase {X}: {Name} Verification Report

**Phase Goal:** {goal from ROADMAP.md}
**Verified:** {timestamp}
**Status:** {status}
**Re-verification:** {Yes | No}

## Goal Achievement

### Observable Truths

| # | Truth | Status | Evidence |
|---|-------|--------|----------|
| 1 | {truth} | ✓ VERIFIED | {evidence} |
| 2 | {truth} | ✗ FAILED | {evidence} |

**Score:** {N}/{M} truths verified

### Future-Preservation Carry

Only include this section when any source plan carries `future_preservation`.

| Bucket | Item | Planned Route | Status | Evidence |
|--------|------|---------------|--------|----------|
| protected_seams | {item} | preserve seam | carried | {evidence} |
| non_decisions | {item} | keep open | thinned | {evidence} |
| posture_assumptions | {item} | carry posture | uncertain | {why_human} |
| strengthening_routes | {item} | intensify now / explicit hold-and-seed | carried | {evidence} |

**Carry review summary:** {carried_count}/{reviewed_count} items carried; {gap_count} thinned; {human_count} uncertain.

### Deferred Items

Only include this section when deferred items exist.

| # | Item | Addressed In | Evidence |
|---|------|-------------|----------|
| 1 | {truth} | Phase {N} | {matching roadmap text} |

### Required Artifacts

| Artifact | Expected | Status | Details |
|----------|----------|--------|---------|
| `path` | {description} | {status} | {details} |

### Key Link Verification

| From | To | Via | Status | Details |
|------|----|-----|--------|---------|
| {from} | {to} | {via} | {status} | {details} |

### Data-Flow Trace (Level 4)

| Artifact | Data Variable | Source | Produces Real Data | Status |
|----------|---------------|--------|--------------------|--------|
| {artifact} | {state} | {source} | {detail} | {status} |

### Behavioral Spot-Checks

| Behavior | Command | Result | Status |
|----------|---------|--------|--------|
| {truth} | {command} | {result} | {status} |

### Requirements Coverage

| Requirement | Source Plan | Description | Status | Evidence |
|-------------|-------------|-------------|--------|----------|
| {REQ-ID} | {plan} | {description} | {status} | {evidence} |

### Anti-Patterns Found

| File | Line | Pattern | Severity | Impact |
|------|------|---------|----------|--------|
| {file} | {line} | {pattern} | {severity} | {impact} |

### Human Verification Required

{Detailed human verification items when needed}

### Gaps Summary

{Narrative summary of present-tense failures, carry thinning, and the strongest next fix routing}

## Verification Metadata

**Verification approach:** Goal-backward
**Must-haves source:** {ROADMAP success criteria + PLAN frontmatter | derived from goal}
**Automated checks:** {N} passed, {M} failed
**Human checks required:** {N}
**Future-preservation review:** {omitted | carried clear | carry gaps found | human judgment needed}
**Total verification time:** {duration}

---
*Verified: {timestamp}*
*Verifier: the agent (subagent)*
```

## Guidance

- Use `future_preservation_review` only when any source plan carries `future_preservation`.
- `thinned` means present-tense behavior may work while future-preservation carry weakened or disappeared.
- `uncertain` means the verifier needs human judgment on that carry item; it is not a silent pass.
- When a strengthening route was intentionally held instead of realized, point to the seed or later-routing evidence directly.
