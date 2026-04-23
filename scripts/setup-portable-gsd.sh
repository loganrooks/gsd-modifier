#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
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
set +e
GSD_ALLOW_OFF_PATH=1 npx get-shit-done-cc --codex --local
INSTALL_EXIT=$?
set -e

if [[ "${INSTALL_EXIT}" -ne 0 && "${INSTALL_EXIT}" -ne 2 ]]; then
  echo "Upstream local GSD install failed with unrecoverable exit code ${INSTALL_EXIT}."
  exit "${INSTALL_EXIT}"
fi

echo "Verifying repo-local gsd-sdk runtime..."
python3 "${REPO_ROOT}/harness_modifier/contract/ensure_gsd_sdk_runtime.py" --pretty

if [[ "${INSTALL_EXIT}" -eq 2 ]]; then
  echo "Recovered from upstream gsd-sdk self-check failure via repo-local runtime verification."
fi

echo "Capturing fresh-install pristine copies for overwrite-mode carriers..."
python3 "${REPO_ROOT}/harness_modifier/contract/portable_gsd_contract.py" \
  capture-pristine-overwrites "${REPO_ROOT}" --strict

echo "Validating tracked gsd-modifier GSD overlay contract..."
python3 "${REPO_ROOT}/harness_modifier/contract/portable_gsd_contract.py" \
  validate-manifest "${REPO_ROOT}" --strict

echo "Applying tracked gsd-modifier GSD overlay..."
echo "Using compact prompt: ${COMPACT_PROMPT_FILE}"
python3 "${REPO_ROOT}/harness_modifier/contract/portable_gsd_contract.py" \
  apply-overlay "${REPO_ROOT}" \
  --compact-prompt-file "${COMPACT_PROMPT_FILE}"

echo "Applying repo-local GSD reasoning defaults..."
python3 "${REPO_ROOT}/harness_modifier/contract/portable_gsd_contract.py" \
  apply-reasoning-defaults "${REPO_ROOT}"

echo "Verifying post-materialization overlay coherence..."
python3 "${REPO_ROOT}/harness_modifier/contract/portable_gsd_contract.py" \
  verify-materialized "${REPO_ROOT}" \
  --compact-prompt-file "${COMPACT_PROMPT_FILE}" \
  --strict

echo
echo "Portable local GSD is ready."
echo "Current discuss mode:"
node "${REPO_ROOT}/.codex/get-shit-done/bin/gsd-tools.cjs" config-get workflow.discuss_mode || true
