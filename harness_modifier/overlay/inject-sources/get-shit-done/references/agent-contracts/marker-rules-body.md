1. **ALL-CAPS markers** (e.g., `## PLANNING COMPLETE`) are the standard convention
2. **Title-case markers** (e.g., `## Verification Complete`) exist in gsd-verifier and gsd-integration-checker -- these are intentional as-is, not bugs
3. **Non-standard markers** (e.g., `## PARTIAL`, `## ESCALATE`) in audit agents indicate partial results requiring orchestrator judgment
4. **Agents without markers** either write artifacts directly to disk or return structured data (JSON/sections) that the caller parses
5. Markers must appear as H2 headings (`## `) at the start of a line in the agent's final output
6. `## RESEARCH COMPLETE` is compatible with unresolved uncertainty only when the agent also provides explicit disposition accounting for what was resolved, what planning must carry forward, what remains intentionally open, and what is still inconclusive
7. `## RESEARCH BLOCKED` is reserved for cases where no reviewable research artifact can yet guide planning
8. `## PLAN COMPLETE` means execution finished and a SUMMARY exists; it does **not** mean the phase reached clean completion. Routing must read `completion_mode` / debt metadata from SUMMARY and VERIFICATION artifacts rather than inferring clean closure from the marker alone.
