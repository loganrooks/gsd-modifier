#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/../.." && pwd)"

cd "${REPO_ROOT}"

./scripts/setup-portable-gsd.sh

python3 -m unittest discover -s tooling/codex/tests

python3 harness_modifier/contract/portable_gsd_contract.py validate-manifest . --strict
python3 harness_modifier/contract/portable_gsd_contract.py verify-materialized . --strict
python3 tooling/codex/audit_refmap.py verify .

git diff --check
