| `workflow.inline_plan_threshold` | `2` | Plans with this many tasks or fewer execute inline (Pattern C) instead of spawning a subagent. Avoids ~14K token spawn overhead for small plans. Set to `0` to always spawn subagents. |
| `manager.flags.discuss` | `""` | Flags passed to `/gsd-discuss-phase` when dispatched from manager (e.g. `"--auto --analyze"`) |
