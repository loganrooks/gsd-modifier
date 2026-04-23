"""Load the uplift state-section carrier for the harness modifier."""

from __future__ import annotations

import copy
import functools
import json
import pathlib
from typing import Any


STATE_SECTION_REL_PATH = "harness_modifier/uplift/state_section.json"
STATE_SECTION_PATH = pathlib.Path(__file__).resolve().with_name("state_section.json")


@functools.lru_cache(maxsize=1)
def _load_state_section() -> dict[str, Any]:
    return json.loads(STATE_SECTION_PATH.read_text(encoding="utf-8"))


def load_state_section() -> dict[str, Any]:
    return copy.deepcopy(_load_state_section())
