# Current State

- extracted repo exists
- filtered history has been carried for the modifier-owned executable/development-support surface
- fresh bootstrap/onboarding docs now exist for Codex and Claude
- `codex-core`, `claude-core`, and `dual-runtime-core` are now active at the repo-self proof layer
- bootstrap/CI now verify both runtimes together
- the synthetic host matrix now covers codex and dual-runtime read-side, aligned, and conflict cases
- **inject-migration initiative is the active workstream** (`.planning/initiatives/inject-migration/STATE.md`); Phases 0+1 closed 2026-05-16; ADR-001 (manifest schema v4 / `mode: inject`) operator-approved 2026-05-16T01:53Z; Phase 2 (contract tools) cleared to start
- widening host proof beyond the synthetic matrix is deferred to after inject-migration completes
- internal path collapse remains later; it is not required for this first safe migration cut
