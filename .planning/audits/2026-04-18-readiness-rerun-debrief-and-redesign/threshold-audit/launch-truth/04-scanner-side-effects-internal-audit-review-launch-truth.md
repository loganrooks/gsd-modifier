# Codex Launch Truth Capture

- `label`: scanner-side-effects-internal-audit-review
- `captured_at`: 2026-04-21T16:16:45-04:00
- `db_path`: /home/rookslog/.codex/state_5.sqlite
- `selection`: worker threads created at or after 2026-04-21T15:56:57-04:00

## Requested Settings
- `model`: gpt-5.4
- `reasoning_effort`: xhigh
- `sandbox_policy`: danger-full-access
- `requested_agent`: explorer

## Effective Thread Rows

| thread_id | created_at | model | reasoning_effort | approval_mode | sandbox_policy | agent_role | agent_path |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 019db19e-0a78-7e31-8a99-60bebc41cd5e | 2026-04-21T15:56:57-04:00 | gpt-5.4 | xhigh | never | danger-full-access | explorer | - |

## Assessment
- `model`: matched requested `gpt-5.4` across 1/1 captured rows.
- `reasoning_effort`: matched requested `xhigh` across 1/1 captured rows.
- `approval_mode`: not captured as a requested setting.
- `sandbox_policy`: matched requested `danger-full-access` across 1/1 captured rows.
- `requested_agent`: preserved as operator-declared intent only. The current sqlite thread rows do not prove the named agent.
- This artifact records operator-declared requested settings beside effective thread rows. It does not replace reviewer judgment, and missing runtime fields must stay unresolved rather than being inferred.
