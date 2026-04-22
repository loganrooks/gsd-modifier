"""Load the portable compatibility declaration for the harness modifier."""

from __future__ import annotations

import copy
import functools
import json
import pathlib
from typing import Any


DECLARATION_REL_PATH = "harness_modifier/compatibility/declaration.json"
DECLARATION_PATH = pathlib.Path(__file__).resolve().with_name("declaration.json")


@functools.lru_cache(maxsize=1)
def _load_declaration() -> dict[str, Any]:
    return json.loads(DECLARATION_PATH.read_text(encoding="utf-8"))


def load_declaration() -> dict[str, Any]:
    return copy.deepcopy(_load_declaration())
