"""Candidate profile registry validation for model benchmark runs."""

from __future__ import annotations

import copy
from typing import Any

from tooling.codex.model_benchmark.schema import ALLOWED_REASONING, NOT_AVAILABLE, require_object, require_string


ALLOWED_ROLE_FAMILIES = {"executor", "planner", "reviewer", "researcher", "general"}
DEFAULT_ROLE_FAMILIES = ["executor", "planner", "reviewer", "researcher", "general"]

DEFAULT_PROFILE_REGISTRY: tuple[dict[str, Any], ...] = (
    {
        "profile_id": "54-medium",
        "model": "gpt-5.4",
        "reasoning_effort": "medium",
        "role_families": DEFAULT_ROLE_FAMILIES,
    },
    {
        "profile_id": "54-high",
        "model": "gpt-5.4",
        "reasoning_effort": "high",
        "role_families": DEFAULT_ROLE_FAMILIES,
    },
    {
        "profile_id": "54-xhigh",
        "model": "gpt-5.4",
        "reasoning_effort": "xhigh",
        "role_families": DEFAULT_ROLE_FAMILIES,
    },
    {
        "profile_id": "55-low",
        "model": "gpt-5.5",
        "reasoning_effort": "low",
        "role_families": DEFAULT_ROLE_FAMILIES,
    },
    {
        "profile_id": "55-medium",
        "model": "gpt-5.5",
        "reasoning_effort": "medium",
        "role_families": DEFAULT_ROLE_FAMILIES,
    },
    {
        "profile_id": "55-high",
        "model": "gpt-5.5",
        "reasoning_effort": "high",
        "role_families": DEFAULT_ROLE_FAMILIES,
    },
)


def _profile_rows(raw_registry: Any | None) -> list[dict[str, Any]]:
    if raw_registry is None:
        return [copy.deepcopy(profile) for profile in DEFAULT_PROFILE_REGISTRY]
    if isinstance(raw_registry, dict):
        rows = raw_registry.get("profiles")
        if rows is None:
            raise ValueError("profile registry object must contain profiles")
    else:
        rows = raw_registry
    if not isinstance(rows, list):
        raise ValueError("profile registry must be a list of profile objects")
    return copy.deepcopy(rows)


def validate_profile(profile: dict[str, Any]) -> dict[str, Any]:
    normalized = copy.deepcopy(require_object(profile, "profile"))
    normalized["profile_id"] = require_string(normalized.get("profile_id"), "profile.profile_id")
    normalized["model"] = require_string(normalized.get("model"), "profile.model")
    reasoning = require_string(normalized.get("reasoning_effort"), "profile.reasoning_effort")
    allowed_reasoning = ALLOWED_REASONING - {NOT_AVAILABLE}
    if reasoning not in allowed_reasoning:
        raise ValueError(f"profile.reasoning_effort must be one of {sorted(allowed_reasoning)}")
    normalized["reasoning_effort"] = reasoning

    if "role_family" in normalized and "role_families" not in normalized:
        normalized["role_families"] = [require_string(normalized.pop("role_family"), "profile.role_family")]
    role_families = normalized.get("role_families", ["general"])
    if not isinstance(role_families, list) or not role_families:
        raise ValueError("profile.role_families must be a non-empty list")
    cleaned_roles: list[str] = []
    for index, role in enumerate(role_families):
        role_value = require_string(role, f"profile.role_families[{index}]")
        if role_value not in ALLOWED_ROLE_FAMILIES:
            raise ValueError(f"profile.role_families[{index}] must be one of {sorted(ALLOWED_ROLE_FAMILIES)}")
        if role_value not in cleaned_roles:
            cleaned_roles.append(role_value)
    normalized["role_families"] = cleaned_roles
    return normalized


def validate_profile_registry(raw_registry: Any | None = None) -> dict[str, dict[str, Any]]:
    profiles: dict[str, dict[str, Any]] = {}
    for raw_profile in _profile_rows(raw_registry):
        profile = validate_profile(raw_profile)
        profile_id = profile["profile_id"]
        if profile_id in profiles:
            raise ValueError(f"duplicate profile_id: {profile_id}")
        profiles[profile_id] = profile
    return profiles


def validate_run_profile_consistency(
    run: dict[str, Any], registry: dict[str, dict[str, Any]] | list[dict[str, Any]] | None = None
) -> dict[str, Any]:
    profiles = registry if isinstance(registry, dict) else validate_profile_registry(registry)
    normalized = copy.deepcopy(require_object(run, "run_record"))
    profile_id = require_string(normalized.get("candidate_profile"), "candidate_profile")
    if profile_id not in profiles:
        raise ValueError(f"candidate_profile {profile_id} is not present in profile registry")
    profile = profiles[profile_id]
    mismatches = []
    for field in ("model", "reasoning_effort"):
        if normalized.get(field) != profile[field]:
            mismatches.append(f"{field} expected {profile[field]} got {normalized.get(field)}")
    telemetry = normalized.get("telemetry_features")
    if isinstance(telemetry, dict):
        role = telemetry.get("agent_role", NOT_AVAILABLE)
        if role not in (NOT_AVAILABLE, None) and role not in profile["role_families"]:
            mismatches.append(f"agent_role {role} not allowed for profile {profile_id}")
    if mismatches:
        raise ValueError(f"profile mismatch for {profile_id}: {'; '.join(mismatches)}")
    normalized["profile_consistency_status"] = "matched"
    return normalized
