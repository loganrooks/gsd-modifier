# Codex Launch Truth Capture

- `label`: checkpoint-5 track launches (fallback evidence)
- `captured_at`: 2026-04-15T19:25:58-04:00
- `db_path`: /home/rookslog/.codex/state_5.sqlite
- `selection`: latest 3 worker thread(s)

## Requested Settings
- `model`: gpt-5.4
- `reasoning_effort`: high
- `approval_mode`: never
- `sandbox_policy`: danger-full-access

## Effective Thread Rows

| thread_id | created_at | model | reasoning_effort | approval_mode | sandbox_policy | agent_role | agent_path |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 019d936c-e844-75a0-9601-dc56d99987ec | 2026-04-15T19:14:41-04:00 | gpt-5.4 | high | never | danger-full-access | worker | - |
| 019d936c-e8b9-7640-ab7c-9874cdf3f38d | 2026-04-15T19:14:41-04:00 | gpt-5.4 | high | never | danger-full-access | worker | - |
| 019d936c-e902-7791-a78d-cd85b64a1382 | 2026-04-15T19:14:41-04:00 | gpt-5.4 | high | never | danger-full-access | worker | - |

## Assessment
- `model`: matched requested `gpt-5.4` across 3/3 captured rows.
- `reasoning_effort`: matched requested `high` across 3/3 captured rows.
- `approval_mode`: matched requested `never` across 3/3 captured rows.
- `sandbox_policy`: matched requested `danger-full-access` across 3/3 captured rows.
- Selection caveat: `--latest` is weaker evidence than a pre-recorded `--since` boundary because unrelated recent worker launches can fall into the same capture.
- This artifact records operator-declared requested settings beside effective thread rows. It does not replace reviewer judgment, and missing runtime fields must stay unresolved rather than being inferred.
