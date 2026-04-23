import json
import pathlib
import tempfile
import unittest

from harness_modifier.closure import observation_record
from harness_modifier.closure import observation_writer


class ClosureObservationWriterTests(unittest.TestCase):
    def _payload(self) -> dict:
        return {
            "observation_id": "obs-001",
            "observed_at": "2026-04-23T15:00:00+00:00",
            "basis_commit": "4172c52",
            "exercise_id": "exercise-001",
            "target_host_class": "codex-disjoint-gsd-installed-no-reflect",
            "evidence_family": "modifier",
            "disposition": "accept",
            "deployment_context": [
                {"key": "compatibility_window_state", "value": "inside-window"},
            ],
            "expectation_vs_observation": [
                {
                    "check": "verify-materialized",
                    "check_outcome": "accept",
                    "skip_reason": "level-1",
                }
            ],
            "semantic_deviation": [
                {
                    "signal_subtype": "contract-mismatch",
                    "summary": "example discrepancy",
                }
            ],
            "positive_gain": [
                {
                    "signal_subtype": "authority-clarified",
                    "summary": "example gain",
                }
            ],
            "measurement_provenance": {
                "detected_by": {"runtime": "codex", "model": "gpt-5.4"},
                "written_by": {"runtime": "codex", "model": "gpt-5.4"},
                "about_work": {"bundle_family": "responsible-closure"},
            },
        }

    def test_policy_loads_expected_shape(self) -> None:
        policy = observation_record.load_observation_record()
        self.assertEqual(policy["bundle_family"], "responsible-closure")
        self.assertEqual(policy["default_provenance_schema"], "v2_split")
        self.assertEqual(policy["format"], "json_only")
        self.assertIn("contract-mismatch", policy["semantic_deviation_subtypes"])
        self.assertIn("authority-clarified", policy["positive_gain_subtypes"])

    def test_write_observation_record_applies_defaults(self) -> None:
        payload = self._payload()
        with tempfile.TemporaryDirectory() as tmpdir:
            target = pathlib.Path(tmpdir) / "observation.json"
            written = observation_writer.write_observation_record(target, payload)

            self.assertEqual(written["carrier_version"], 1)
            self.assertEqual(written["provenance_schema"], "v2_split")
            self.assertEqual(written["status"], "recorded")
            self.assertEqual(written["automation_level"], 1)
            self.assertEqual(written["bundle_family"], "responsible-closure")

            on_disk = json.loads(target.read_text(encoding="utf-8"))
            self.assertEqual(on_disk["observation_id"], "obs-001")
            self.assertEqual(on_disk["status"], "recorded")

    def test_validate_rejects_noncanonical_skip_reason(self) -> None:
        payload = self._payload()
        payload["expectation_vs_observation"][0]["skip_reason"] = "bogus-reason"
        with self.assertRaisesRegex(ValueError, "skip_reason"):
            observation_writer.validate_observation_record(payload)

    def test_validate_rejects_missing_measurement_provenance_key(self) -> None:
        payload = self._payload()
        del payload["measurement_provenance"]["written_by"]
        with self.assertRaisesRegex(ValueError, "written_by"):
            observation_writer.validate_observation_record(payload)

    def test_validate_rejects_unknown_positive_gain_subtype(self) -> None:
        payload = self._payload()
        payload["positive_gain"][0]["signal_subtype"] = "unknown-gain"
        with self.assertRaisesRegex(ValueError, "positive_gain"):
            observation_writer.validate_observation_record(payload)

    def test_validate_rejects_unknown_target_host_class(self) -> None:
        payload = self._payload()
        payload["target_host_class"] = "unknown-host-class"
        with self.assertRaisesRegex(ValueError, "target_host_class"):
            observation_writer.validate_observation_record(payload)

    def test_validate_rejects_unexpected_top_level_field(self) -> None:
        payload = self._payload()
        payload["unexpected_field"] = {"leak": True}
        with self.assertRaisesRegex(ValueError, "unexpected top-level fields"):
            observation_writer.validate_observation_record(payload)

    def test_validate_requires_semantic_deviation_subtype(self) -> None:
        payload = self._payload()
        del payload["semantic_deviation"][0]["signal_subtype"]
        with self.assertRaisesRegex(ValueError, "semantic_deviation"):
            observation_writer.validate_observation_record(payload)

    def test_validate_requires_positive_gain_subtype(self) -> None:
        payload = self._payload()
        payload["positive_gain"] = [{}]
        with self.assertRaisesRegex(ValueError, "positive_gain"):
            observation_writer.validate_observation_record(payload)


if __name__ == "__main__":
    unittest.main()
