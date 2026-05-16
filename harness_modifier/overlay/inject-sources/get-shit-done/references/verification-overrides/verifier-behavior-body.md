## Verifier Behavior with Overrides

### Check Order

The override check happens **before marking a must-have as FAIL**. The flow is:

1. Evaluate must-have against codebase (Steps 3-5 of verification process)
2. If evaluation result is FAIL or UNCERTAIN:
   a. Check `overrides:` array in VERIFICATION.md frontmatter for a fuzzy match
   b. If override found: mark as `PASSED (override)` instead of FAIL
   c. If no override found: mark as FAIL as normal
3. If evaluation result is PASS: mark as VERIFIED (overrides are irrelevant)

### Output Format

Overridden items appear with distinct status in all verification tables:

```markdown
| # | Truth | Status | Evidence |
|---|-------|--------|----------|
| 1 | User can authenticate | VERIFIED | OAuth session flow working |
| 2 | OAuth2 PKCE flow | PASSED (override) | Override: Using session-based auth — accepted by dave on 2026-04-04 |
| 3 | Chat renders messages | FAILED | Component returns placeholder |
```

The `PASSED (override)` status must be visually distinct from both `VERIFIED` and `FAILED`. In the evidence column, include the override reason and who accepted it.

### Impact on Overall Status

- `PASSED (override)` items count toward the passing score, not the failing score
- A phase with all items either VERIFIED or PASSED (override) can have status `passed`
- Overrides do NOT suppress `human_needed` items — those still require human testing
- Overrides do NOT imply clean completion. If any override is applied, VERIFICATION.md must set `completion_mode: debt_carrying_completion` and `debt_bearing: true` even when `status: passed`.

### Frontmatter Score

The score and override count in frontmatter reflect applied overrides:

```yaml
score: 5/5  # includes 2 overrides
overrides_applied: 2
```
