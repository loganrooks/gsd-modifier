#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/../.." && pwd)"

cd "${REPO_ROOT}"

python3 -m py_compile $(find harness_modifier tooling/codex -name '*.py' -type f | tr '\n' ' ')

bash -n scripts/setup-portable-gsd.sh
bash -n scripts/ci/check-deterministic.sh
bash -n scripts/ci/check-bootstrap.sh

python3 -m unittest \
  tooling.codex.tests.test_audit_refmap \
  tooling.codex.tests.test_closure_observation_writer \
  tooling.codex.tests.test_closure_host_exercise_packet_writer \
  tooling.codex.tests.test_harness_canary

python3 harness_modifier/contract/portable_gsd_contract.py validate-manifest . --strict

(cd docs/origin-audit/archive && sha256sum -c SHA256SUMS)

git diff --check
