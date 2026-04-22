from __future__ import annotations

import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace

from harness_modifier.capture import run_review_reviewer


def write(path: Path, text: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)
    return path


class ReviewReviewerTests(unittest.TestCase):
    def test_prepare_run_home_creates_paths(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            phase_dir = Path(tmpdir) / ".planning" / "phases" / "007-test"

            args = SimpleNamespace(
                phase_dir=str(phase_dir),
                padded_phase="007-test",
                run_id="20260422T000000Z-abcd123",
                git_sha=None,
            )

            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                run_review_reviewer.prepare_run_home(args)

            payload = json.loads(output.getvalue())
            self.assertTrue(Path(payload["run_home"]).exists())
            self.assertTrue(Path(payload["launch_truth_dir"]).exists())
            self.assertTrue(payload["prompt_path"].endswith("prompt.md"))
            self.assertTrue(payload["timing_path"].endswith("timing.md"))

    def test_classify_claude_complete_from_stream(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            stream = write(
                Path(tmpdir) / "claude.stream.jsonl",
                "\n".join(
                    [
                        json.dumps(
                            {
                                "type": "assistant",
                                "message": {"content": [{"type": "text", "text": "review body"}]},
                            }
                        ),
                        json.dumps({"type": "result", "result": "review body"}),
                    ]
                )
                + "\n",
            )
            state, recovered = run_review_reviewer.classify_claude(stream, 0)
            self.assertEqual(state, "complete")
            self.assertEqual(recovered, "review body")

    def test_classify_claude_partial_from_stream_without_result(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            stream = write(
                Path(tmpdir) / "claude.stream.jsonl",
                json.dumps(
                    {
                        "type": "assistant",
                        "message": {"content": [{"type": "text", "text": "partial body"}]},
                    }
                )
                + "\n",
            )
            state, recovered = run_review_reviewer.classify_claude(stream, 1)
            self.assertEqual(state, "partial")
            self.assertEqual(recovered, "partial body")

    def test_record_reviewer_plain_absent(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            run_home = Path(tmpdir) / "reviews" / "run-1"
            stderr_file = write(Path(tmpdir) / "stderr.log", "boom")

            args = SimpleNamespace(
                run_home=str(run_home),
                reviewer="gemini",
                shape="plain",
                stdout_file=None,
                stderr_file=str(stderr_file),
                stream_file=None,
                launch_truth_markdown=None,
                probe_summary_file=None,
                estimated_duration="4-6 minutes",
                invocation="gemini -p ...",
                requested_model=None,
                requested_reasoning=None,
                requested_approval=None,
                requested_sandbox=None,
                exit_code=1,
                elapsed_seconds=12.5,
            )

            with contextlib.redirect_stdout(io.StringIO()):
                run_review_reviewer.record_reviewer(args)
            status_note = run_home / "gemini.status.md"
            launch_truth = run_home / "launch-truth" / "gemini.md"
            timing = run_home / "timing.md"

            self.assertTrue(status_note.exists())
            self.assertIn("`state`: absent", status_note.read_text())
            self.assertTrue(launch_truth.exists())
            self.assertTrue(timing.exists())

    def test_record_reviewer_codex_copies_launch_truth_and_review(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            run_home = Path(tmpdir) / "reviews" / "run-2"
            stdout_file = write(Path(tmpdir) / "codex.stdout.md", "codex review")
            launch_truth_src = write(Path(tmpdir) / "codex-launch.md", "# Codex Launch Truth\n")

            args = SimpleNamespace(
                run_home=str(run_home),
                reviewer="codex",
                shape="codex",
                stdout_file=str(stdout_file),
                stderr_file=None,
                stream_file=None,
                launch_truth_markdown=str(launch_truth_src),
                probe_summary_file=None,
                estimated_duration="5-8 minutes",
                invocation="codex exec ...",
                requested_model="gpt-5.4",
                requested_reasoning="high",
                requested_approval="never",
                requested_sandbox="danger-full-access",
                exit_code=0,
                elapsed_seconds=8.25,
            )

            with contextlib.redirect_stdout(io.StringIO()):
                run_review_reviewer.record_reviewer(args)
            self.assertEqual((run_home / "codex.review.md").read_text(), "codex review\n")
            self.assertTrue((run_home / "launch-truth" / "codex.captured.md").exists())
            self.assertTrue((run_home / "launch-truth" / "codex.md").exists())
