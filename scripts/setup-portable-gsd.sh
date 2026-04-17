#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
OVERLAY_ROOT="${REPO_ROOT}/tooling/portable-gsd/overlay"
DEFAULT_COMPACT_PROMPT_FILE="tooling/compact-prompts/project.md"
LOCAL_COMPACT_PROMPT_SELECTOR="${REPO_ROOT}/.codex.local/compact-prompt.txt"

cd "${REPO_ROOT}"

COMPACT_PROMPT_FILE="${PRIX_COMPACT_PROMPT_FILE:-}"
if [[ -z "${COMPACT_PROMPT_FILE}" && -f "${LOCAL_COMPACT_PROMPT_SELECTOR}" ]]; then
  COMPACT_PROMPT_FILE="$(head -n 1 "${LOCAL_COMPACT_PROMPT_SELECTOR}" | tr -d '\r')"
fi
if [[ -z "${COMPACT_PROMPT_FILE}" ]]; then
  COMPACT_PROMPT_FILE="${DEFAULT_COMPACT_PROMPT_FILE}"
fi

echo "Installing repo-local regular GSD for Codex..."
npx get-shit-done-cc --codex --local

echo "Applying tracked prix-guesser GSD overlay..."
echo "Using compact prompt: ${COMPACT_PROMPT_FILE}"

while IFS= read -r -d '' file; do
  rel="${file#${OVERLAY_ROOT}/}"
  target="${REPO_ROOT}/.codex/${rel}"
  mkdir -p "$(dirname "${target}")"
  python - <<'PY' "${file}" "${target}" "${REPO_ROOT}" "${COMPACT_PROMPT_FILE}"
import pathlib, sys

src = pathlib.Path(sys.argv[1])
dst = pathlib.Path(sys.argv[2])
repo_root = sys.argv[3]
compact_prompt_file = sys.argv[4]

text = src.read_text()
text = text.replace("__PROJECT_ROOT__", repo_root)
text = text.replace("__COMPACT_PROMPT_FILE__", compact_prompt_file)
dst.write_text(text)
PY
  echo "  patched .codex/${rel}"
done < <(find "${OVERLAY_ROOT}" -type f -print0 | sort -z)

echo "Applying repo-local GSD reasoning defaults..."
python - <<'PY' "${REPO_ROOT}"
import pathlib
import re
import sys

repo_root = pathlib.Path(sys.argv[1])
codex_root = repo_root / ".codex"

config_path = codex_root / "config.toml"
config_text = config_path.read_text()
config_text = re.sub(
    r'^model_reasoning_effort = "[^"]+"$',
    'model_reasoning_effort = "high"',
    config_text,
    count=1,
    flags=re.M,
)
config_path.write_text(config_text)

quality_reasoning = {
    "gsd-planner": "xhigh",
    "gsd-roadmapper": "xhigh",
    "gsd-phase-researcher": "xhigh",
    "gsd-project-researcher": "xhigh",
    "gsd-ui-researcher": "xhigh",
    "gsd-executor": "high",
    "gsd-debugger": "high",
    "gsd-doc-writer": "high",
    "gsd-research-synthesizer": "high",
    "gsd-codebase-mapper": "high",
    "gsd-verifier": "high",
    "gsd-plan-checker": "high",
    "gsd-integration-checker": "high",
    "gsd-nyquist-auditor": "high",
    "gsd-ui-checker": "high",
    "gsd-ui-auditor": "high",
    "gsd-doc-verifier": "high",
}

for agent_name, effort in quality_reasoning.items():
    agent_path = codex_root / "agents" / f"{agent_name}.toml"
    text = agent_path.read_text()
    line = f'model_reasoning_effort = "{effort}"'
    if re.search(r'^model_reasoning_effort = "[^"]+"$', text, re.M):
        text = re.sub(r'^model_reasoning_effort = "[^"]+"$', line, text, count=1, flags=re.M)
    else:
        text = re.sub(r'^(description = ".*"\n)', r"\1" + line + "\n", text, count=1, flags=re.M)
    agent_path.write_text(text)
PY

echo
echo "Portable local GSD is ready."
echo "Current discuss mode:"
node "${REPO_ROOT}/.codex/get-shit-done/bin/gsd-tools.cjs" config-get workflow.discuss_mode || true
