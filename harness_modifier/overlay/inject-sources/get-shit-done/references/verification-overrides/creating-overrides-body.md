## Creating Overrides

### Interactive Override Suggestion

When the verifier marks a must-have as FAIL and the failure looks intentional (e.g., alternative implementation exists, or the code explicitly handles the case differently), the verifier should suggest creating an override:

```markdown
### F-002: OAuth2 PKCE flow

**Status:** FAILED
**Evidence:** No PKCE implementation found. Session-based auth used instead.

**This looks intentional.** The codebase uses session-based authentication which achieves the same goal differently. To accept this deviation, add an override to VERIFICATION.md frontmatter:

```yaml
overrides:
  - must_have: "OAuth2 PKCE flow implemented"
    reason: "Using session-based auth instead — PKCE unnecessary for server-rendered app"
    accepted_by: "{your name}"
    accepted_at: "{current ISO timestamp}"
```

Then re-run verification to apply.
```

### Override via gsd-tools

Overrides can also be managed through the verification workflow:

1. Run `$gsd-verify-work` — verification finds gaps
2. Review gaps — determine which are intentional deviations
3. Add override entries to VERIFICATION.md frontmatter
4. Re-run `$gsd-verify-work` — overrides are applied, remaining gaps shown
