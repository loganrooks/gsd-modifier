import contextlib
import io as stdio
import json
import tempfile
import unittest
from pathlib import Path

from tooling.codex.model_benchmark import cli
from tooling.codex.model_benchmark import costs
from tooling.codex.model_benchmark import io as bench_io
from tooling.codex.model_benchmark import profiles
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

    def _run_cli(self, argv):
        stdout = stdio.StringIO()
        stderr = stdio.StringIO()
        with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
            return cli.main(argv)

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

    def test_validate_usage_rejects_boolean_tokens(self):
        record = self._run_record(usage={"input_tokens": True, "usage_metric_status": "measured"})

        with self.assertRaisesRegex(ValueError, "must be an integer"):
            schema.validate_run_record(record)

    def test_validate_run_record_defaults_schema_and_profile_status(self):
        normalized = schema.validate_run_record(self._run_record())

        self.assertEqual(normalized["schema_version"], "model-benchmark-run/v1")
        self.assertEqual(normalized["profile_consistency_status"], "not_checked")
        self.assertEqual(normalized["usage"]["reasoning_tokens"], 400)

    def test_validate_run_record_normalizes_missing_usage_categories(self):
        normalized = schema.validate_run_record(self._run_record(usage={"usage_metric_status": "not_available"}))

        self.assertEqual(normalized["usage"]["reasoning_tokens"], "not_available")
        self.assertEqual(normalized["usage"]["input_tokens"], "not_available")

    def test_read_jsonl_objects_loads_valid_utf8_objects(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "runs.jsonl"
            rows = [{"name": "alpha"}, {"name": "cafe"}]
            bench_io.write_jsonl_objects(path, rows)

            self.assertEqual(bench_io.read_jsonl_objects(path), rows)

    def test_read_jsonl_objects_reports_invalid_line_number(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "runs.jsonl"
            path.write_text('{"ok": true}\n{"bad"\n', encoding="utf-8")

            with self.assertRaisesRegex(ValueError, r"runs\.jsonl line 2"):
                bench_io.read_jsonl_objects(path)

    def test_read_jsonl_objects_rejects_non_object_rows(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "runs.jsonl"
            path.write_text("[1, 2]\n", encoding="utf-8")

            with self.assertRaisesRegex(ValueError, "row must be an object"):
                bench_io.read_jsonl_objects(path)

    def test_write_jsonl_objects_refuses_overwrite_by_default(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "runs.jsonl"
            bench_io.write_jsonl_objects(path, [{"one": 1}])

            with self.assertRaises(FileExistsError):
                bench_io.write_jsonl_objects(path, [{"two": 2}])
            bench_io.write_jsonl_objects(path, [{"two": 2}], overwrite=True)
            self.assertEqual(bench_io.read_jsonl_objects(path), [{"two": 2}])

    def test_read_json_object_rejects_arrays(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "rates.json"
            path.write_text("[]", encoding="utf-8")

            with self.assertRaisesRegex(ValueError, "single JSON object"):
                bench_io.read_json_object(path)

    def test_default_profile_registry_contains_planned_matrix(self):
        registry = profiles.validate_profile_registry()

        self.assertEqual(set(registry), {"54-medium", "54-high", "54-xhigh", "55-low", "55-medium", "55-high"})
        self.assertEqual(registry["55-low"]["model"], "gpt-5.5")
        self.assertEqual(registry["55-low"]["reasoning_effort"], "low")
        self.assertEqual(registry["55-medium"]["model"], "gpt-5.5")
        self.assertEqual(registry["55-medium"]["reasoning_effort"], "medium")

    def test_profile_registry_rejects_duplicate_ids(self):
        with self.assertRaisesRegex(ValueError, "duplicate profile_id"):
            profiles.validate_profile_registry(
                [
                    {"profile_id": "55-medium", "model": "gpt-5.5", "reasoning_effort": "medium"},
                    {"profile_id": "55-medium", "model": "gpt-5.5", "reasoning_effort": "high"},
                ]
            )

    def test_profile_registry_rejects_invalid_reasoning(self):
        with self.assertRaisesRegex(ValueError, "reasoning_effort"):
            profiles.validate_profile_registry(
                [{"profile_id": "bad", "model": "gpt-5.5", "reasoning_effort": "turbo"}]
            )

    def test_profile_registry_normalizes_legacy_role_family(self):
        registry = profiles.validate_profile_registry(
            [
                {
                    "profile_id": "55-medium",
                    "model": "gpt-5.5",
                    "reasoning_effort": "medium",
                    "role_family": "executor",
                }
            ]
        )

        self.assertEqual(registry["55-medium"]["role_families"], ["executor"])

    def test_run_profile_mismatch_fails_validation(self):
        registry = profiles.validate_profile_registry()

        with self.assertRaisesRegex(ValueError, "profile mismatch"):
            schema.validate_run_record(
                self._run_record(candidate_profile="55-medium", reasoning_effort="high"),
                registry,
            )

    def test_run_profile_match_sets_consistency_status(self):
        normalized = schema.validate_run_record(self._run_record(), profiles.validate_profile_registry())

        self.assertEqual(normalized["profile_consistency_status"], "matched")

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

    def test_attach_cost_estimate_adds_estimate_to_new_run_object(self):
        run = schema.validate_run_record(
            self._run_record(cost_estimate={"estimate_status": "stale"}),
            profiles.validate_profile_registry(),
        )

        estimated = costs.attach_cost_estimate(run, self._rate_table())

        self.assertEqual(estimated["cost_estimate"]["estimate_status"], "estimated")
        self.assertEqual(run["cost_estimate"]["estimate_status"], "stale")
        self.assertEqual(estimated["profile_consistency_status"], "matched")

    def test_cost_estimate_decimal_math_accepts_string_rates(self):
        estimate = costs.estimate_cost(
            {"input_tokens": 3, "usage_metric_status": "measured"},
            self._rate_table(input_per_million="0.333333"),
        )

        self.assertEqual(estimate["total_estimated_cost"], "0.000001")

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
        self.assertNotIn("winner", summary)
        self.assertNotIn("recommendation", summary)

    def test_summarize_runs_does_not_treat_missing_tokens_as_zero(self):
        record = self._run_record(usage={"usage_metric_status": "not_available"})

        summary = reports.summarize_runs([record])

        self.assertEqual(summary["groups"][0]["average_known_tokens"], "not_available")
        self.assertEqual(summary["groups"][0]["reasoning_token_total"], "not_available")

    def test_summarize_runs_includes_reasoning_and_partial_cost_counts(self):
        record = costs.attach_cost_estimate(
            self._run_record(
                usage={
                    "input_tokens": 100,
                    "reasoning_tokens": "not_available",
                    "usage_metric_status": "measured",
                }
            ),
            self._rate_table(),
        )

        summary = reports.summarize_runs([record])

        self.assertEqual(summary["groups"][0]["partial_cost_count"], 1)
        self.assertEqual(summary["groups"][0]["average_reasoning_tokens"], "not_available")

    def test_cli_validate_runs_exits_zero_for_valid_records(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            runs = Path(tmpdir) / "runs.jsonl"
            bench_io.write_jsonl_objects(runs, [self._run_record()])

            self.assertEqual(self._run_cli(["validate-runs", "--runs", str(runs)]), 0)

    def test_cli_validate_runs_exits_nonzero_for_invalid_records(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            runs = Path(tmpdir) / "runs.jsonl"
            bench_io.write_jsonl_objects(runs, [self._run_record(reasoning_effort="bad")])

            self.assertNotEqual(self._run_cli(["validate-runs", "--runs", str(runs)]), 0)

    def test_cli_estimate_costs_writes_jsonl_and_refuses_overwrite(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            runs = Path(tmpdir) / "runs.jsonl"
            rates = Path(tmpdir) / "rates.json"
            output = Path(tmpdir) / "estimated.jsonl"
            bench_io.write_jsonl_objects(runs, [self._run_record()])
            rates.write_text(json.dumps(self._rate_table()), encoding="utf-8")

            self.assertEqual(
                self._run_cli(
                    ["estimate-costs", "--runs", str(runs), "--rates", str(rates), "--output", str(output)]
                ),
                0,
            )
            self.assertEqual(
                self._run_cli(
                    ["estimate-costs", "--runs", str(runs), "--rates", str(rates), "--output", str(output)]
                ),
                1,
            )
            self.assertEqual(bench_io.read_jsonl_objects(output)[0]["cost_estimate"]["estimate_status"], "estimated")

    def test_cli_summarize_runs_writes_grouped_json(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            runs = Path(tmpdir) / "runs.jsonl"
            output = Path(tmpdir) / "summary.json"
            bench_io.write_jsonl_objects(
                runs,
                [
                    self._run_record(),
                    self._run_record(
                        run_id="run-002",
                        candidate_profile="54-high",
                        model="gpt-5.4",
                        reasoning_effort="high",
                    ),
                ],
            )

            self.assertEqual(self._run_cli(["summarize-runs", "--runs", str(runs), "--output", str(output)]), 0)
            summary = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual(len(summary["groups"]), 2)

    def test_cli_profile_mismatch_fails(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            runs = Path(tmpdir) / "runs.jsonl"
            bench_io.write_jsonl_objects(
                runs,
                [self._run_record(candidate_profile="55-medium", reasoning_effort="high")],
            )

            self.assertEqual(self._run_cli(["validate-runs", "--runs", str(runs)]), 1)


if __name__ == "__main__":
    unittest.main()
