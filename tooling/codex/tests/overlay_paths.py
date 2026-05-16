import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
OVERLAY_ROOT = ROOT / "tooling/portable-gsd/overlay"
OVERLAY_MANIFEST = OVERLAY_ROOT / "OVERLAY-MANIFEST.json"


def overlay_manifest_payload() -> dict:
    return json.loads(OVERLAY_MANIFEST.read_text(encoding="utf-8"))


def overlay_entry(rel_path: str):
    entries = overlay_manifest_payload()["entries"]
    if rel_path in entries:
        return entries[rel_path]
    for entry in entries.values():
        if not isinstance(entry, dict):
            continue
        materializers = entry.get("materializers", {})
        for materializer in materializers.values():
            if materializer.get("target") == rel_path:
                return entry
    raise KeyError(rel_path)


def overlay_entry_mode(rel_path: str) -> str:
    entry = overlay_entry(rel_path)
    if isinstance(entry, str):
        return entry
    if "mode" in entry:
        return entry["mode"]
    materializers = entry.get("materializers", {})
    for materializer in materializers.values():
        if materializer.get("target") == rel_path:
            return materializer["mode"]
    if "codex" in materializers:
        return materializers["codex"]["mode"]
    return next(iter(materializers.values()))["mode"]


def _materializer_for_path(rel_path: str, runtime: str = "codex") -> dict:
    entry = overlay_entry(rel_path)
    if isinstance(entry, str) or "mode" in entry:
        raise ValueError(f"overlay entry {rel_path!r} has no materializers")
    materializers = entry.get("materializers", {})
    if runtime in materializers and materializers[runtime].get("target") == rel_path:
        return materializers[runtime]
    for materializer in materializers.values():
        if materializer.get("target") == rel_path:
            return materializer
    if runtime in materializers:
        return materializers[runtime]
    return next(iter(materializers.values()))


def overlay_source_path(rel_path: str) -> Path:
    entry = overlay_entry(rel_path)
    if isinstance(entry, str):
        source_rel_path = f"tooling/portable-gsd/overlay/{rel_path}"
    elif "source" in entry:
        source_rel_path = entry.get("source", f"tooling/portable-gsd/overlay/{rel_path}")
    else:
        materializers = entry.get("materializers", {})
        for materializer in materializers.values():
            if materializer.get("target") == rel_path:
                source_rel_path = materializer["source"]
                break
        else:
            source_rel_path = materializers["codex"]["source"]
    return ROOT / source_rel_path


def overlay_inject_source_paths(rel_path: str, runtime: str = "codex") -> list[Path]:
    materializer = _materializer_for_path(rel_path, runtime=runtime)
    if materializer.get("mode") != "inject":
        raise ValueError(f"overlay entry {rel_path!r} is not mode: inject")
    return [
        ROOT / operation["source"]
        for operation in materializer.get("operations", [])
        if isinstance(operation, dict) and operation.get("source")
    ]
