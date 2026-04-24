import tempfile
import unittest
from pathlib import Path

from tooling.codex.model_benchmark import manifest


class ModelBenchmarkManifestTests(unittest.TestCase):
    def _write_manifest(self, text: str) -> Path:
        tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(tmpdir.cleanup)
        path = Path(tmpdir.name) / "telemetry-plugin.yaml"
        path.write_text(text, encoding="utf-8")
        return path

    def _minimal_manifest(self) -> str:
        return """
schema_version: telemetry-plugin-manifest/v1
registry_id: fixture.telemetry
registry_version: "2026.04.24"
source_kinds:
  - id: runtime.codex_cli.sqlite_index
namespaces:
  - id: runtime.codex_cli
predicates:
  - id: session.has_runtime_item
metrics:
  - id: tokens.input
    status: measured
    evidence_class: synthetic_fixture
    reliability_mode: direct_field
    content_contract: metadata_only
    cost_evidence_mode: not_applicable
    comparability: comparable_with_caveat
rubrics:
  - id: quality.instruction_following
    dimensions:
      - id: follows_task_boundary
emits:
  - source_kind: runtime.codex_cli.sqlite_index
    namespace: runtime.codex_cli
    predicate: session.has_runtime_item
    metric_id: tokens.input
    rubric_id: quality.instruction_following
    status: measured
    reliability_mode: direct_field
    content_contract: metadata_only
"""

    def test_valid_minimal_manifest_passes(self):
        loaded = manifest.load_manifest(self._write_manifest(self._minimal_manifest()))

        self.assertEqual(loaded["schema_version"], "telemetry-plugin-manifest/v1")
        self.assertEqual(loaded["registry_id"], "fixture.telemetry")
        self.assertEqual(loaded["registry_hash"], manifest.registry_hash(loaded))

    def test_malformed_schema_version_fails(self):
        path = self._write_manifest(self._minimal_manifest().replace("telemetry-plugin-manifest/v1", "v0"))

        with self.assertRaisesRegex(ValueError, "schema_version"):
            manifest.load_manifest(path)

    def test_duplicate_metric_rubric_and_source_ids_fail(self):
        cases = (
            (
                "metrics",
                """metrics:
  - id: tokens.input
    status: measured
    evidence_class: synthetic_fixture
    reliability_mode: direct_field
    content_contract: metadata_only
    cost_evidence_mode: not_applicable
    comparability: comparable_with_caveat""",
                """metrics:
  - id: tokens.input
    status: measured
    evidence_class: synthetic_fixture
    reliability_mode: direct_field
    content_contract: metadata_only
    cost_evidence_mode: not_applicable
    comparability: comparable_with_caveat
  - id: tokens.input
    status: measured
    evidence_class: synthetic_fixture
    reliability_mode: direct_field
    content_contract: metadata_only
    cost_evidence_mode: not_applicable
    comparability: comparable_with_caveat""",
            ),
            (
                "rubrics",
                """rubrics:
  - id: quality.instruction_following
    dimensions:
      - id: follows_task_boundary""",
                """rubrics:
  - id: quality.instruction_following
    dimensions:
      - id: follows_task_boundary
  - id: quality.instruction_following
    dimensions:
      - id: other_dimension""",
            ),
            (
                "source_kinds",
                """source_kinds:
  - id: runtime.codex_cli.sqlite_index""",
                """source_kinds:
  - id: runtime.codex_cli.sqlite_index
  - id: runtime.codex_cli.sqlite_index""",
            ),
        )
        for section, original, duplicate in cases:
            with self.subTest(section=section):
                path = self._write_manifest(self._minimal_manifest().replace(original, duplicate))

                with self.assertRaisesRegex(ValueError, f"duplicate {section} id"):
                    manifest.load_manifest(path)

    def test_undeclared_enum_values_fail(self):
        path = self._write_manifest(
            self._minimal_manifest().replace("content_contract: metadata_only", "content_contract: all_text")
        )

        with self.assertRaisesRegex(ValueError, "content_contract"):
            manifest.load_manifest(path)

    def test_undeclared_emitted_references_fail(self):
        path = self._write_manifest(
            self._minimal_manifest().replace("metric_id: tokens.input", "metric_id: tokens.output")
        )

        with self.assertRaisesRegex(ValueError, "undeclared metric_id"):
            manifest.load_manifest(path)

    def test_raw_content_modes_require_explicit_consent(self):
        path = self._write_manifest(
            self._minimal_manifest().replace("content_contract: metadata_only", "content_contract: raw_content_allowed")
        )

        with self.assertRaisesRegex(ValueError, "raw content"):
            manifest.load_manifest(path)

        allowed = self._minimal_manifest().replace(
            "content_contract: metadata_only",
            "content_contract: raw_content_allowed\n    raw_content_consent: true\n    retention_policy: fixture-only",
            1,
        ).replace(
            "content_contract: metadata_only",
            "content_contract: raw_content_allowed\n    raw_content_consent: true\n    retention_policy: fixture-only",
            1,
        )
        loaded = manifest.load_manifest(self._write_manifest(allowed))
        self.assertEqual(loaded["metrics"][0]["content_contract"], "raw_content_allowed")

    def test_canonical_json_hash_is_stable_across_yaml_key_ordering(self):
        first = manifest.load_manifest(self._write_manifest(self._minimal_manifest()))
        reordered = self._minimal_manifest().replace(
            """schema_version: telemetry-plugin-manifest/v1
registry_id: fixture.telemetry
registry_version: "2026.04.24"
""",
            """registry_version: "2026.04.24"
registry_id: fixture.telemetry
schema_version: telemetry-plugin-manifest/v1
""",
        )
        second = manifest.load_manifest(self._write_manifest(reordered))

        self.assertEqual(manifest.canonical_json(first), manifest.canonical_json(second))
        self.assertEqual(first["registry_hash"], second["registry_hash"])


if __name__ == "__main__":
    unittest.main()
