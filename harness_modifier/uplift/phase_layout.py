"""Load the uplift phase-layout carrier for the harness modifier."""

from __future__ import annotations

import copy
import functools
import json
import pathlib
from typing import Any


PHASE_LAYOUT_REL_PATH = "harness_modifier/uplift/phase_layout.json"
PHASE_LAYOUT_PATH = pathlib.Path(__file__).resolve().with_name("phase_layout.json")


@functools.lru_cache(maxsize=1)
def _load_phase_layout() -> dict[str, Any]:
    return json.loads(PHASE_LAYOUT_PATH.read_text(encoding="utf-8"))


def load_phase_layout() -> dict[str, Any]:
    return copy.deepcopy(_load_phase_layout())
