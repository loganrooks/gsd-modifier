"""Load the uplift vocabulary carrier for the harness modifier."""

from __future__ import annotations

import copy
import functools
import json
import pathlib
from typing import Any


VOCABULARY_REL_PATH = "harness_modifier/uplift/vocabulary.json"
VOCABULARY_PATH = pathlib.Path(__file__).resolve().with_name("vocabulary.json")


@functools.lru_cache(maxsize=1)
def _load_vocabulary() -> dict[str, Any]:
    return json.loads(VOCABULARY_PATH.read_text(encoding="utf-8"))


def load_vocabulary() -> dict[str, Any]:
    return copy.deepcopy(_load_vocabulary())
