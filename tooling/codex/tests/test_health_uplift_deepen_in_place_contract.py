import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]


class HealthUpliftDeepenInPlaceContractTests(unittest.TestCase):
    def test_health_workflow_names_post_validation_uplift_follow_through_step(self) -> None:
        workflow = (
            ROOT
            / "tooling/portable-gsd/overlay/get-shit-done/workflows/health.md"
        ).read_text(encoding="utf-8")

        self.assertIn('<step name="review_project_uplift_health_follow_through">', workflow)
        self.assertIn("## Primary Compact Read", workflow)
        self.assertIn("## Supporting Narrative Read", workflow)
        self.assertIn("## Deeper Typed Read", workflow)
        self.assertIn("## Interpretation Frame", workflow)
        self.assertIn("## When To Surface", workflow)
        self.assertIn(".planning/STATE.md", workflow)
        self.assertIn(".planning/UPLIFT-REPORT.md", workflow)
        self.assertIn(".planning/UPLIFT-MANIFEST.json", workflow)
        self.assertIn("Compatibility posture: core_runtime_parity", workflow)
        self.assertIn("Do not run `$gsd-uplift-project --write` from inside it.", workflow)
        self.assertIn(
            "Only surface this step after all structural health validation is complete, including `verify_repairs` when `--repair` was used.",
            workflow,
        )
        self.assertLess(
            workflow.index("<step name=\"verify_repairs\">"),
            workflow.index('<step name="review_project_uplift_health_follow_through">'),
        )
        self.assertLess(
            workflow.index('<step name="review_project_uplift_health_follow_through">'),
            workflow.index("<step name=\"format_output\">"),
        )

    def test_health_workflow_keeps_trigger_and_authority_split_explicit(self) -> None:
        workflow = (
            ROOT
            / "tooling/portable-gsd/overlay/get-shit-done/workflows/health.md"
        ).read_text(encoding="utf-8")

        self.assertIn("`Compatibility posture` is not exactly `core_runtime_parity`", workflow)
        self.assertIn("`Mixed-runtime policy` is not exactly `dual-runtime-core (active)`", workflow)
        self.assertIn("`Secondary runtime observation` is present and not `none`", workflow)
        self.assertIn(
            "`Current recommendation` is not exactly `Continue with ordinary routing.`",
            workflow,
        )
        self.assertIn("structural planning state is present", workflow)
        self.assertIn("route is no longer broken or missing-planning", workflow)
        self.assertIn("gsd-sdk query validate.health", workflow)
        self.assertIn("$gsd-uplift-project --write", workflow)
        self.assertIn(
            "The footer remains the write-side route pointer when later posture refresh is still live.",
            workflow,
        )
        self.assertIn(
            "Both may surface in one pass without duplicating ownership or turning health into a second uplift workflow.",
            workflow,
        )
        self.assertIn("Do not compute compatibility drift here.", workflow)
        self.assertIn("Do not widen the health footer into a second uplift workflow.", workflow)

    def test_health_workflow_keeps_silent_case_literal(self) -> None:
        workflow = (
            ROOT
            / "tooling/portable-gsd/overlay/get-shit-done/workflows/health.md"
        ).read_text(encoding="utf-8")

        self.assertIn("Keep it silent when:", workflow)
        self.assertIn(
            "planning structure is missing and the correct route is `$gsd-new-project` or `$gsd-ingest-docs`",
            workflow,
        )
        self.assertIn("structural health itself is still the unresolved question", workflow)
        self.assertIn("Mixed-runtime policy: dual-runtime-core (active)", workflow)
        self.assertIn("Secondary runtime observation: none", workflow)
        self.assertIn("Current recommendation: Continue with ordinary routing.", workflow)

    def test_skill_wrapper_keeps_read_only_continuity_and_later_refresh_split(self) -> None:
        skill = (
            ROOT / "tooling/portable-gsd/overlay/skills/gsd-health/SKILL.md"
        ).read_text(encoding="utf-8")

        self.assertIn("structural planning health remains the primary objective", skill)
        self.assertIn("read-only uplift continuity reread may follow", skill)
        self.assertIn("$gsd-uplift-project --write` remains a later separate follow-through", skill)


if __name__ == "__main__":
    unittest.main()
