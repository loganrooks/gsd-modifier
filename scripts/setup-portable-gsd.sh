#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
OVERLAY_ROOT="${REPO_ROOT}/tooling/portable-gsd/overlay"

cd "${REPO_ROOT}"

echo "Installing repo-local regular GSD for Codex..."
npx get-shit-done-cc --codex --local

echo "Applying tracked prix-guesser GSD overlay..."

while IFS= read -r -d '' file; do
  rel="${file#${OVERLAY_ROOT}/}"
  target="${REPO_ROOT}/.codex/${rel}"
  mkdir -p "$(dirname "${target}")"
  python - <<'PY' "${file}" "${target}" "${REPO_ROOT}"
import pathlib, sys

src = pathlib.Path(sys.argv[1])
dst = pathlib.Path(sys.argv[2])
repo_root = sys.argv[3]

text = src.read_text()
text = text.replace("__PROJECT_ROOT__", repo_root)
dst.write_text(text)
PY
  echo "  patched .codex/${rel}"
done < <(find "${OVERLAY_ROOT}" -type f -print0 | sort -z)

echo
echo "Portable local GSD is ready."
echo "Current discuss mode:"
node "${REPO_ROOT}/.codex/get-shit-done/bin/gsd-tools.cjs" config-get workflow.discuss_mode || true
