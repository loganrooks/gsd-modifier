"""Load the uplift carrier-catalog carrier for the harness modifier."""

from __future__ import annotations

import copy
import functools
import json
import pathlib
from typing import Any


CARRIER_CATALOG_REL_PATH = "harness_modifier/uplift/carrier_catalog.json"
CARRIER_CATALOG_PATH = pathlib.Path(__file__).resolve().with_name("carrier_catalog.json")


@functools.lru_cache(maxsize=1)
def _load_carrier_catalog() -> dict[str, Any]:
    return json.loads(CARRIER_CATALOG_PATH.read_text(encoding="utf-8"))


def load_carrier_catalog() -> dict[str, Any]:
    return copy.deepcopy(_load_carrier_catalog())
