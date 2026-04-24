# Codex Launch Truth Capture

- `label`: seed-doctrine-vintage-sidecar
- `captured_at`: 2026-04-21T20:04:24-04:00
- `db_path`: /home/rookslog/.codex/state_5.sqlite
- `selection`: latest 1 worker thread(s)

## Requested Settings
- `model`: gpt-5.4
- `reasoning_effort`: xhigh
- `requested_agent`: explorer

## Effective Thread Rows

| thread_id | created_at | model | reasoning_effort | approval_mode | sandbox_policy | agent_role | agent_path |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 019dae40-516b-7ff2-a973-4831bdae1376 | 2026-04-21T00:15:44-04:00 | gpt-5.4 | xhigh | never | danger-full-access | worker | - |

## Assessment
- `model`: matched requested `gpt-5.4` across 1/1 captured rows.
- `reasoning_effort`: matched requested `xhigh` across 1/1 captured rows.
- `approval_mode`: not captured as a requested setting.
- `sandbox_policy`: not captured as a requested setting.
- `requested_agent`: preserved as operator-declared intent only. The current sqlite thread rows do not prove the named agent.
- Selection caveat: `--latest` is weaker evidence than a pre-recorded `--since` boundary because unrelated recent worker launches can fall into the same capture.
- This artifact records operator-declared requested settings beside effective thread rows. It does not replace reviewer judgment, and missing runtime fields must stay unresolved rather than being inferred.
