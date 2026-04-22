"""Load the seed-contract carrier for the harness modifier."""

from __future__ import annotations

import copy
import functools
import json
import pathlib
from typing import Any


SEED_CONTRACT_REL_PATH = "harness_modifier/compatibility/seed_contract.json"
SEED_CONTRACT_PATH = pathlib.Path(__file__).resolve().with_name("seed_contract.json")


@functools.lru_cache(maxsize=1)
def _load_seed_contract() -> dict[str, Any]:
    return json.loads(SEED_CONTRACT_PATH.read_text(encoding="utf-8"))


def load_seed_contract() -> dict[str, Any]:
    return copy.deepcopy(_load_seed_contract())
