#!/usr/bin/env python3
"""Stable overlay-owned shim to tooling.codex.seed_migration_inventory."""

from __future__ import annotations

import pathlib
import sys

repo_root = pathlib.Path(__file__).resolve().parents[3]
if str(repo_root) not in sys.path:
    sys.path.insert(0, str(repo_root))

from tooling.codex.seed_migration_inventory import *  # noqa: F401,F403
from tooling.codex.seed_migration_inventory import main


if __name__ == "__main__":
    raise SystemExit(main())
