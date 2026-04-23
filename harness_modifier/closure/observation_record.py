"""Load the responsible-closure observation-record carrier."""

from __future__ import annotations

import copy
import functools
import json
import pathlib
from typing import Any


OBSERVATION_RECORD_REL_PATH = "harness_modifier/closure/observation_record.json"
OBSERVATION_RECORD_PATH = pathlib.Path(__file__).resolve().with_name("observation_record.json")


@functools.lru_cache(maxsize=1)
def _load_observation_record() -> dict[str, Any]:
    return json.loads(OBSERVATION_RECORD_PATH.read_text(encoding="utf-8"))


def load_observation_record() -> dict[str, Any]:
    return copy.deepcopy(_load_observation_record())
