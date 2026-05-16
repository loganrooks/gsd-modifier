## Override Format

Overrides are declared in the VERIFICATION.md frontmatter under an `overrides:` key:

```yaml
---
phase: 03-authentication
verified: 2026-04-05T12:00:00Z
status: passed
completion_mode: debt_carrying_completion
debt_bearing: true
score: 5/5
overrides_applied: 2
overrides:
  - must_have: "OAuth2 PKCE flow implemented"
    reason: "Using session-based auth instead — PKCE unnecessary for server-rendered app"
    accepted_by: "dave"
    accepted_at: "2026-04-04T15:30:00Z"
  - must_have: "Rate limiting on login endpoint"
    reason: "Deferred to Phase 5 (infrastructure) — tracked in ROADMAP.md"
    accepted_by: "dave"
    accepted_at: "2026-04-04T15:30:00Z"
---
```

### Required Fields

| Field | Type | Description |
|-------|------|-------------|
| `must_have` | string | The must-have truth, artifact description, or key link being overridden. Does not need to be an exact match — fuzzy matching applies. |
| `reason` | string | Why this deviation is acceptable. Must be specific — not just "not needed". |
| `accepted_by` | string | Who accepted the override (username or role). Required. |
| `accepted_at` | string | ISO timestamp of when the override was accepted. Required. |
