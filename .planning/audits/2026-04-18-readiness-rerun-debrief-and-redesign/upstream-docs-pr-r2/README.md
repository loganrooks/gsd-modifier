# Upstream Docs PR R2 Snapshot

This subtree is a frozen local capture of the submitted upstream docs PR read set used by the readiness-rerun audit on 2026-04-20.

- source branch/commit: `docs/pr4-consistency-drift-guards-r2` at `4f3de809`
- capture method: `git archive` from the local upstream clone
- purpose: stable local evidence for carry/leverage auditing of the submitted docs PR

Why the files end in `.md.txt`:

- the snapshot is intentionally partial and does not include the full upstream repository
- keeping the captured docs as live `.md` files would poison local markdown-reference verification inside this audit workspace
- `.md.txt` preserves the exact document text and line structure for citation while preventing a partial copy from posing as a healthy markdown subtree
