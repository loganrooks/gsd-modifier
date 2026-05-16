## Override Lifecycle

### During Re-verification

When a phase is re-verified (e.g., after gap closure):
- Existing overrides carry forward automatically
- If the underlying code now satisfies the must-have, the override becomes unnecessary — mark as VERIFIED instead
- Overrides are never removed automatically; they persist as documentation

### At Milestone Completion

During `$gsd-audit-milestone`, overrides are surfaced in the audit report:

```
### Verification Overrides ({count} across {phase_count} phases)

| Phase | Must-Have | Reason | Accepted By |
|-------|----------|--------|-------------|
| 03 | OAuth2 PKCE | Session-based auth used instead | dave |
```

This gives the team visibility into all accepted deviations before closing the milestone.

### Cleanup

Stale overrides (where the must-have was later implemented or removed from ROADMAP.md) can be cleaned up during milestone completion. They are informational — leaving them causes no harm.
