#!/usr/bin/env python3
"""Transitional shim to harness_modifier.contract.portable_gsd_contract."""

from __future__ import annotations

import pathlib
import sys

repo_root = pathlib.Path(__file__).resolve().parents[2]
if str(repo_root) not in sys.path:
    sys.path.insert(0, str(repo_root))

from harness_modifier.contract.portable_gsd_contract import *  # noqa: F401,F403
from harness_modifier.contract.portable_gsd_contract import main


if __name__ == "__main__":
    raise SystemExit(main())
