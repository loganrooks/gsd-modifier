"""Runtime adapter registry."""

from __future__ import annotations

from harness_modifier.contract.runtime_adapters.claude import ClaudeRuntimeAdapter
from harness_modifier.contract.runtime_adapters.codex import CodexRuntimeAdapter


_ADAPTERS = {
    "codex": CodexRuntimeAdapter(),
    "claude": ClaudeRuntimeAdapter(),
}


def supported_runtimes() -> list[str]:
    return list(_ADAPTERS)


def supported_adapters() -> list[object]:
    return [adapter for _, adapter in _ADAPTERS.items()]


def get_adapter(runtime: str):
    if runtime not in _ADAPTERS:
        raise KeyError(f"unknown runtime adapter: {runtime}")
    return _ADAPTERS[runtime]
