"""Runtime adapter registry for portable GSD materialization."""

from .registry import get_adapter, supported_adapters, supported_runtimes

__all__ = ["get_adapter", "supported_adapters", "supported_runtimes"]
