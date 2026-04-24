"""Canonical vocabularies for the model benchmark telemetry substrate."""

from __future__ import annotations


OBSERVATION_STATUSES = frozenset(
    {
        "measured",
        "estimated",
        "derived",
        "inferred",
        "not_available",
        "not_applicable",
        "not_exposed",
        "not_enabled",
        "not_collected",
        "redacted",
        "deferred_live_call",
        "malformed_source",
        "conflicting_sources",
        "unknown",
    }
)

EVIDENCE_CLASSES = frozenset(
    {
        "verified_doc",
        "local_observed",
        "repo_precedent",
        "inferred",
        "unverified",
        "deferred",
        "rejected",
        "synthetic_fixture",
        "manual_evidence",
    }
)

RELIABILITY_MODES = frozenset(
    {
        "direct_field",
        "documented_field",
        "local_structural_field",
        "provider_emitted",
        "runtime_emitted",
        "harness_emitted",
        "aggregate",
        "approximate",
        "estimated_from_pricing",
        "aggregate_allocated",
        "derived_from_config",
        "derived_from_trace",
        "self_reported",
        "manual_label",
        "substitute_signal",
        "synthetic_fixture",
        "unknown",
    }
)

CONTENT_CONTRACTS = frozenset(
    {
        "no_content_access",
        "metadata_only",
        "structural_only",
        "content_hash_or_length_only",
        "derived_features_only",
        "redacted_content_reference",
        "raw_api_body_gated",
        "raw_content_allowed",
    }
)

RAW_CONTENT_CONTRACTS = frozenset({"raw_api_body_gated", "raw_content_allowed"})

COST_EVIDENCE_MODES = frozenset(
    {
        "not_exposed",
        "not_applicable",
        "provider_reported_per_request",
        "provider_reported_aggregate",
        "aggregate_allocated",
        "api_equivalent_estimate",
        "cli_approximate",
        "pricing_table_estimate",
        "manual_cost_entry",
        "unknown",
    }
)

COMPARABILITY_VALUES = frozenset(
    {
        "comparable",
        "comparable_with_caveat",
        "provider_semantics_differ",
        "surface_semantics_differ",
        "partial",
        "not_comparable",
        "insufficient_evidence",
        "unknown",
    }
)

RUNTIME_ITEM_CORRELATION_STATUSES = frozenset(
    {
        "uncorrelated",
        "correlates_with",
        "same_as_model_call",
        "not_applicable",
        "unknown",
    }
)
