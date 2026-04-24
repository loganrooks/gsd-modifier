import unittest

from tooling.codex.model_benchmark import costs
from tooling.codex.model_benchmark import reports
from tooling.codex.model_benchmark import schema


class ModelBenchmarkTests(unittest.TestCase):
    def _run_record(self, **overrides):
        record = {
            "run_id": "run-001",
            "task_id": "EXEC-001",
            "candidate_profile": "55-medium",
            "model": "gpt-5.5",
            "reasoning_effort": "medium",
            "runtime_provider": "codex_cli",
            "status": "completed",
            "effective_model": "gpt-5.5",
            "effective_reasoning_effort": "medium",
            "usage": {
                "input_tokens": 1000,
                "cached_input_tokens": 200,
                "output_tokens": 300,
                "reasoning_tokens": 400,
                "initialization_tokens": 50,
                "tool_result_tokens": 75,
                "usage_metric_status": "measured",
            },
            "telemetry_features": {
                "trace_id": "trace-001",
                "runtime_provider": "codex_cli",
                "agent_role": "executor",
                "intervention_id": "profile-55-medium-exec",
                "metric_granularity": "run",
                "provenance": "fixture",
                "derived_feature_version": "v1",
            },
            "score": {"overall": 3.5},
        }
        record.update(overrides)
        return record

    def _rate_table(self, **overrides):
        table = {
            "model": "gpt-5.5",
            "currency": "USD",
            "source_url": "https://example.test/pricing",
            "retrieved_at": "2026-04-24T00:00:00Z",
            "effective_date": "2026-04-24",
            "input_per_million": "1.00",
            "cached_input_per_million": "0.10",
            "output_per_million": "10.00",
            "reasoning_per_million": "10.00",
        }
        table.update(overrides)
        return table

    def test_validate_run_record_preserves_telemetry_extension_fields(self):
        normalized = schema.validate_run_record(self._run_record())

        self.assertEqual(normalized["telemetry_features"]["trace_id"], "trace-001")
        self.assertEqual(normalized["telemetry_features"]["intervention_id"], "profile-55-medium-exec")
        self.assertFalse(normalized["qualitative_only"])

    def test_validate_run_record_marks_unproven_effective_settings_qualitative_only(self):
        normalized = schema.validate_run_record(
            self._run_record(effective_model="not_available", effective_reasoning_effort="not_available")
        )

        self.assertTrue(normalized["qualitative_only"])

    def test_validate_usage_rejects_negative_tokens(self):
        record = self._run_record(usage={"input_tokens": -1, "usage_metric_status": "measured"})

        with self.assertRaisesRegex(ValueError, "cannot be negative"):
            schema.validate_run_record(record)

    def test_cost_estimate_keeps_reasoning_tokens_separate(self):
        estimate = costs.estimate_cost(self._run_record()["usage"], self._rate_table())

        self.assertEqual(estimate["estimate_status"], "estimated")
        self.assertEqual(estimate["total_estimated_cost"], "0.008145")
        reasoning_items = [item for item in estimate["line_items"] if item["token_field"] == "reasoning_tokens"]
        self.assertEqual(reasoning_items[0]["estimated_cost"], "0.004000")
        self.assertIn("API-equivalent", estimate["caveat"])

    def test_cost_estimate_missing_reasoning_split_is_partial_not_zero(self):
        usage = self._run_record()["usage"]
        usage["reasoning_tokens"] = "not_available"

        estimate = costs.estimate_cost(usage, self._rate_table())

        self.assertEqual(estimate["estimate_status"], "partial")
        self.assertIn("reasoning_tokens", estimate["missing_token_fields"])
        self.assertEqual(estimate["total_estimated_cost"], "0.004145")

    def test_cost_estimate_requires_sourced_pricing_metadata(self):
        with self.assertRaisesRegex(ValueError, "missing required metadata"):
            costs.estimate_cost(self._run_record()["usage"], self._rate_table(source_url=""))

    def test_cost_estimate_missing_all_usage_is_not_available(self):
        estimate = costs.estimate_cost({"usage_metric_status": "not_available"}, self._rate_table())

        self.assertEqual(estimate["estimate_status"], "not_available")
        self.assertEqual(estimate["total_estimated_cost"], "not_available")

    def test_summarize_runs_groups_by_task_profile_and_reasoning(self):
        first = self._run_record(
            run_id="run-001",
            candidate_profile="55-medium",
            reasoning_effort="medium",
            cost_estimate={"total_estimated_cost": "0.008145"},
        )
        second = self._run_record(
            run_id="run-002",
            candidate_profile="54-high",
            model="gpt-5.4",
            reasoning_effort="high",
            effective_model="not_available",
            effective_reasoning_effort="not_available",
            cost_estimate={"total_estimated_cost": "0.010000"},
            score={"overall": 3.0},
        )

        summary = reports.summarize_runs([first, second])

        self.assertEqual(len(summary["groups"]), 2)
        qualitative = [group for group in summary["groups"] if group["candidate_profile"] == "54-high"][0]
        self.assertEqual(qualitative["qualitative_only_count"], 1)
        self.assertEqual(qualitative["average_score"], 3.0)

    def test_summarize_runs_does_not_treat_missing_tokens_as_zero(self):
        record = self._run_record(usage={"usage_metric_status": "not_available"})

        summary = reports.summarize_runs([record])

        self.assertEqual(summary["groups"][0]["average_known_tokens"], "not_available")


if __name__ == "__main__":
    unittest.main()
