"""Load the runtime-observation carrier for the harness modifier."""

from __future__ import annotations

import copy
import functools
import json
import pathlib
from typing import Any


OBSERVATION_REL_PATH = "harness_modifier/compatibility/observation.json"
OBSERVATION_PATH = pathlib.Path(__file__).resolve().with_name("observation.json")


@functools.lru_cache(maxsize=1)
def _load_observation() -> dict[str, Any]:
    return json.loads(OBSERVATION_PATH.read_text(encoding="utf-8"))


def load_observation() -> dict[str, Any]:
    return copy.deepcopy(_load_observation())
