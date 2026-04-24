# Audit Refmap Policy

This directory carries the explicit missing-link policy used by `tooling/codex/audit_refmap.py`.

The verifier stays strict for active documentation. A missing local link fails unless it has an exact entry in `audit-refmap-policy.json` matching the source path, source line, raw target, and resolved target.

The current policy exists because `gsd-modifier` preserves imported audit and readiness archives from the old `prix-guesser` workspace. Those archives intentionally keep some old-host references as provenance. They are not active repo-local authority surfaces, and they should not be silently rewritten to unrelated current files.

Outside-repo absolute paths are classified by the scanner as `external-absolute`, even when they happen to exist on the current workstation. That keeps verification portable: old host paths remain visible in snapshots, but they do not become machine-dependent local edges.

Current enforced missing-link baseline:

- `intentionally_unimported_origin_artifact`: old-host governance artifacts that were not imported as active `gsd-modifier` authority surfaces.
- `deferred_archive_gap`: relative-depth archive references to sibling or generated artifacts outside the imported provenance set.

Future missing links should not be added mechanically. First decide whether the target should be repaired to a real local path. Add a policy entry only when the missing target is an intentionally preserved archive/provenance reference.
