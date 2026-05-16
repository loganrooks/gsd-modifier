```bash
INIT=$(node "__PROJECT_ROOT__/.codex/get-shit-done/bin/gsd-tools.cjs" init execute-phase "1")
if [[ "$INIT" == @file:* ]]; then INIT=$(cat "${INIT#@file:}"); fi
# JSON output includes: branching_strategy, phase_branch_template, milestone_branch_template
```
