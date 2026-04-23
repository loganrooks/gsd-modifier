"""Load the responsible-closure host-exercise packet contract."""

from __future__ import annotations

import copy
import functools
import json
import pathlib
from typing import Any


HOST_EXERCISE_PACKET_REL_PATH = "harness_modifier/closure/host_exercise_packet.json"
HOST_EXERCISE_PACKET_PATH = pathlib.Path(__file__).resolve().with_name("host_exercise_packet.json")


@functools.lru_cache(maxsize=1)
def _load_host_exercise_packet() -> dict[str, Any]:
    return json.loads(HOST_EXERCISE_PACKET_PATH.read_text(encoding="utf-8"))


def load_host_exercise_packet() -> dict[str, Any]:
    return copy.deepcopy(_load_host_exercise_packet())
