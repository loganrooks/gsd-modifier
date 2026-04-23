import json
import pathlib
import tempfile
import unittest
from unittest import mock

from harness_modifier.closure import host_exercise_matrix


class ClosureHostExerciseMatrixTests(unittest.TestCase):
    def _write(self, root: pathlib.Path, rel_path: str, text: str) -> None:
        path = root / rel_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def _modifier_fixture(self, root: pathlib.Path) -> None:
        self._write(
            root,
            "tooling/portable-gsd/overlay/config.toml",
            'model = "gpt-5.4"\n'
            'model_reasoning_effort = "xhigh"\n'
            'experimental_compact_prompt_file = "__COMPACT_PROMPT_FILE__"\n',
        )
        self._write(
            root,
            "tooling/portable-gsd/overlay/agents/gsd-planner.toml",
            'description = "planner"\n',
        )
        self._write(
            root,
            "tooling/portable-gsd/overlay/get-shit-done/workflows/plan-phase.md",
            "Plan phase for __PROJECT_ROOT__\n",
        )
        self._write(
            root,
            "harness_modifier/overlay/commands/gsd/uplift-project.md",
            "Claude command wrapper\n",
        )
        self._write(
            root,
            "tooling/portable-gsd/overlay/OVERLAY-MANIFEST.json",
            json.dumps(
                {
                    "schema_version": 3,
                    "entries": {
                        "agents/gsd-planner.toml": {
                            "capability_id": "agents/gsd-planner.toml",
                            "parity_tier": "runtime_specific",
                            "materializers": {
                                "codex": {
                                    "mode": "add",
                                    "target": "agents/gsd-planner.toml",
                                    "source": "tooling/portable-gsd/overlay/agents/gsd-planner.toml",
                                }
                            },
                        },
                        "config.toml": {
                            "capability_id": "config.toml",
                            "parity_tier": "runtime_specific",
                            "materializers": {
                                "codex": {
                                    "mode": "add",
                                    "target": "config.toml",
                                    "source": "tooling/portable-gsd/overlay/config.toml",
                                }
                            },
                        },
                        "get-shit-done/workflows/plan-phase.md": {
                            "capability_id": "get-shit-done/workflows/plan-phase.md",
                            "parity_tier": "core_required",
                            "materializers": {
                                "codex": {
                                    "mode": "overwrite",
                                    "target": "get-shit-done/workflows/plan-phase.md",
                                    "source": "tooling/portable-gsd/overlay/get-shit-done/workflows/plan-phase.md",
                                },
                                "claude": {
                                    "mode": "overwrite",
                                    "target": "get-shit-done/workflows/plan-phase.md",
                                    "source": "tooling/portable-gsd/overlay/get-shit-done/workflows/plan-phase.md",
                                },
                            },
                        },
                        "entrypoint.gsd-uplift-project": {
                            "capability_id": "entrypoint.gsd-uplift-project",
                            "parity_tier": "core_adapted",
                            "materializers": {
                                "codex": {
                                    "mode": "overwrite",
                                    "target": "get-shit-done/workflows/uplift-project.md",
                                    "source": "tooling/portable-gsd/overlay/get-shit-done/workflows/plan-phase.md",
                                },
                                "claude": {
                                    "mode": "overwrite",
                                    "target": "commands/gsd/uplift-project.md",
                                    "source": "harness_modifier/overlay/commands/gsd/uplift-project.md",
                                },
                            },
                        },
                    },
                }
            )
            + "\n",
        )
        self._write(root, ".codex/get-shit-done/VERSION", "1.38.3\n")
        self._write(root, ".codex/gsd-file-manifest.json", json.dumps({"version": "1.38.3"}) + "\n")
        self._write(root, ".claude/get-shit-done/VERSION", "1.38.3\n")
        self._write(root, ".claude/gsd-file-manifest.json", json.dumps({"version": "1.38.3"}) + "\n")

    def _scenario(self, payload: dict, scenario_id: str) -> dict:
        return next(scenario for scenario in payload["scenarios"] if scenario["scenario_id"] == scenario_id)

    def test_run_host_exercise_matrix_covers_codex_profile(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = pathlib.Path(tmpdir)
            modifier_root = root / "modifier"
            output_dir = root / "matrix-out"
            self._modifier_fixture(modifier_root)

            payload = host_exercise_matrix.run_host_exercise_matrix(
                modifier_root,
                output_dir,
                profile="codex",
            )

            self.assertEqual(payload["status"], "ok")
            self.assertEqual(payload["scenario_count"], 3)
            self.assertEqual(payload["profile"], "codex")

            pristine = self._scenario(payload, "pristine-read-side")
            aligned = self._scenario(payload, "materialized-aligned")
            drift = self._scenario(payload, "version-drift")

            self.assertEqual(pristine["actual_disposition"], "shift-mode")
            self.assertTrue(pristine["verify_materialized_skipped"])
            self.assertEqual(pristine["compatibility_window_state"], "inside-window")

            self.assertEqual(aligned["actual_disposition"], "accept")
            self.assertFalse(aligned["verify_materialized_skipped"])
            self.assertEqual(aligned["verify_materialized_hard_failure_count"], 0)
            self.assertEqual(aligned["compatibility_window_state"], "inside-window")

            self.assertEqual(drift["actual_disposition"], "refuse")
            self.assertTrue(drift["verify_materialized_skipped"])
            self.assertEqual(drift["compatibility_window_state"], "outside-window")

    def test_run_host_exercise_matrix_covers_dual_runtime_profile(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = pathlib.Path(tmpdir)
            modifier_root = root / "modifier"
            output_dir = root / "matrix-out"
            self._modifier_fixture(modifier_root)

            payload = host_exercise_matrix.run_host_exercise_matrix(
                modifier_root,
                output_dir,
                profile="dual-runtime",
            )

            self.assertEqual(payload["status"], "ok")
            self.assertEqual(payload["scenario_count"], 3)
            self.assertEqual(payload["profile"], "dual-runtime")

            read_side = self._scenario(payload, "dual-runtime-read-side")
            aligned = self._scenario(payload, "dual-runtime-aligned")
            conflict = self._scenario(payload, "dual-runtime-core-conflict")

            self.assertEqual(read_side["actual_disposition"], "shift-mode")
            self.assertTrue(read_side["verify_materialized_skipped"])
            self.assertEqual(read_side["parity_state"], "dual-runtime-read-side")

            self.assertEqual(aligned["actual_disposition"], "accept")
            self.assertFalse(aligned["verify_materialized_skipped"])
            self.assertEqual(aligned["verify_materialized_hard_failure_count"], 0)
            self.assertEqual(aligned["parity_state"], "dual-runtime-aligned")

            self.assertEqual(conflict["actual_disposition"], "refuse")
            self.assertFalse(conflict["verify_materialized_skipped"])
            self.assertEqual(conflict["compatibility_window_state"], "outside-window")
            self.assertEqual(conflict["parity_state"], "dual-runtime-conflict")

            for scenario in payload["scenarios"]:
                for path in scenario["artifact_paths"].values():
                    self.assertTrue(pathlib.Path(path).exists(), path)

    def test_main_strict_returns_nonzero_when_expectation_is_wrong(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = pathlib.Path(tmpdir)
            modifier_root = root / "modifier"
            output_dir = root / "matrix-out"
            self._modifier_fixture(modifier_root)

            bad_scenario = host_exercise_matrix.MatrixScenario(
                scenario_id="wrong-expectation",
                profile="codex",
                fixture_kind="pristine-read-side",
                host_reference="fixture-wrong-expectation",
                host_age_posture="pristine",
                expected_disposition="accept",
                expected_compatibility_window_state="inside-window",
                expected_parity_state="single-runtime",
                expected_verify_materialized_skipped=True,
                expect_zero_verify_hard_failures=False,
                narrative_summary="Intentional mismatch for strict-mode coverage.",
            )

            with mock.patch.object(host_exercise_matrix, "CODEX_SCENARIOS", (bad_scenario,)):
                with mock.patch.object(host_exercise_matrix, "SCENARIOS", (bad_scenario,)):
                    exit_code = host_exercise_matrix.main(
                        [str(modifier_root), "--profile", "codex", "--output-dir", str(output_dir), "--strict"]
                    )

            self.assertEqual(exit_code, 1)
            payload = json.loads((output_dir / "matrix-summary.json").read_text(encoding="utf-8"))
            self.assertEqual(payload["status"], "issue")
            self.assertIn("wrong-expectation", payload["issues"][0])


if __name__ == "__main__":
    unittest.main()
