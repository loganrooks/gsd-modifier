import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
OVERLAY_ROOT = ROOT / "tooling/portable-gsd/overlay"
OVERLAY_MANIFEST = OVERLAY_ROOT / "OVERLAY-MANIFEST.json"


def overlay_manifest_payload() -> dict:
    return json.loads(OVERLAY_MANIFEST.read_text(encoding="utf-8"))


def overlay_entry(rel_path: str):
    return overlay_manifest_payload()["entries"][rel_path]


def overlay_entry_mode(rel_path: str) -> str:
    entry = overlay_entry(rel_path)
    if isinstance(entry, str):
        return entry
    return entry["mode"]


def overlay_source_path(rel_path: str) -> Path:
    entry = overlay_entry(rel_path)
    if isinstance(entry, str):
        source_rel_path = f"tooling/portable-gsd/overlay/{rel_path}"
    else:
        source_rel_path = entry.get("source", f"tooling/portable-gsd/overlay/{rel_path}")
    return ROOT / source_rel_path
