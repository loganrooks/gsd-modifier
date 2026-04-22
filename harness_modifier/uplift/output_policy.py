"""Load the uplift output-policy carrier for the harness modifier."""

from __future__ import annotations

import copy
import functools
import json
import pathlib
from typing import Any


OUTPUT_POLICY_REL_PATH = "harness_modifier/uplift/output_policy.json"
OUTPUT_POLICY_PATH = pathlib.Path(__file__).resolve().with_name("output_policy.json")


@functools.lru_cache(maxsize=1)
def _load_output_policy() -> dict[str, Any]:
    return json.loads(OUTPUT_POLICY_PATH.read_text(encoding="utf-8"))


def load_output_policy() -> dict[str, Any]:
    return copy.deepcopy(_load_output_policy())
