import json
import pathlib
import tempfile
import unittest
from unittest import mock

from tooling.codex.model_opinion_mining import build_inventory
from tooling.codex.model_opinion_mining import common
from tooling.codex.model_opinion_mining import extract_text
from tooling.codex.model_opinion_mining import fetch_pages
from tooling.codex.model_opinion_mining import verify_sources


class FakeResponse:
    def __init__(self, *, status_code: int, text: str, headers: dict[str, str] | None = None) -> None:
        self.status_code = status_code
        self.text = text
        self.headers = headers or {}
        self.encoding = "utf-8"
        self.url = "https://example.test/final"

    def json(self):
        return json.loads(self.text)


class ModelOpinionMiningTests(unittest.TestCase):
    def _write_seed_file(self, root: pathlib.Path, rows: list[dict]) -> pathlib.Path:
        path = root / "seeds.jsonl"
        path.write_text("".join(json.dumps(row) + "\n" for row in rows), encoding="utf-8")
        return path

    def _seed_row(self, **overrides) -> dict:
        row = {
            "source_id": "reddit-codex-001",
            "platform": "reddit",
            "url": "https://example.test/thread",
            "query": 'site:reddit.com/r/codex "GPT-5.5" "usage"',
            "claim_tags": ["usage", "capability"],
            "collection_caveat": "Search-indexed sample; not representative.",
        }
        row.update(overrides)
        return row

    def test_read_seed_rows_rejects_missing_required_fields(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = pathlib.Path(tmpdir)
            seed_path = self._write_seed_file(root, [{"source_id": "missing"}])

            with self.assertRaisesRegex(ValueError, "missing required fields"):
                common.read_seed_rows(seed_path)

    def test_fetch_pages_writes_raw_html_and_safe_metadata(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = pathlib.Path(tmpdir)
            seed_path = self._write_seed_file(root, [self._seed_row()])
            raw_dir = root / "raw"
            metadata_path = root / "metadata.json"

            with mock.patch.object(
                fetch_pages.requests,
                "get",
                return_value=FakeResponse(
                    status_code=200,
                    text="<html><body><p>GPT-5.5 feels better.</p></body></html>",
                    headers={"Content-Type": "text/html", "Set-Cookie": "secret=value"},
                ),
            ):
                rows = fetch_pages.fetch_pages(seed_path, raw_dir, metadata_path, timeout=1.0)

            self.assertEqual(rows[0]["fetch_status"], "fetched")
            self.assertEqual(rows[0]["http_status"], 200)
            self.assertEqual(rows[0]["safe_headers"], {"content-type": "text/html"})
            self.assertNotIn("set-cookie", rows[0]["safe_headers"])
            self.assertTrue((raw_dir / "reddit-codex-001.html").exists())
            self.assertTrue(metadata_path.exists())

    def test_fetch_pages_uses_reddit_json_endpoint(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = pathlib.Path(tmpdir)
            seed_path = self._write_seed_file(root, [self._seed_row(url="https://www.reddit.com/r/codex/comments/abc/example/")])
            metadata_path = root / "metadata.json"

            with mock.patch.object(
                fetch_pages.requests,
                "get",
                return_value=FakeResponse(
                    status_code=200,
                    text='[{"data":{"children":[]}}]',
                    headers={"Content-Type": "application/json"},
                ),
            ) as get_mock:
                rows = fetch_pages.fetch_pages(seed_path, root / "raw", metadata_path, timeout=1.0)

            get_mock.assert_called_once()
            self.assertEqual(get_mock.call_args.args[0], "https://www.reddit.com/r/codex/comments/abc/example/.json")
            self.assertEqual(rows[0]["fetch_url"], "https://www.reddit.com/r/codex/comments/abc/example/.json")
            self.assertTrue((root / "raw" / "reddit-codex-001.json").exists())

    def test_fetch_pages_records_failed_status_without_raw_file(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = pathlib.Path(tmpdir)
            seed_path = self._write_seed_file(root, [self._seed_row()])
            metadata_path = root / "metadata.json"

            with mock.patch.object(
                fetch_pages.requests,
                "get",
                return_value=FakeResponse(status_code=404, text="missing"),
            ):
                rows = fetch_pages.fetch_pages(seed_path, root / "raw", metadata_path, timeout=1.0)

            self.assertEqual(rows[0]["fetch_status"], "failed")
            self.assertEqual(rows[0]["http_status"], 404)
            self.assertEqual(rows[0]["raw_path"], "not_available")
            self.assertEqual(rows[0]["error"], "http_status_404")

    def test_extract_text_drops_scripts_and_augments_metadata(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = pathlib.Path(tmpdir)
            raw_dir = root / "raw"
            raw_dir.mkdir()
            raw_path = raw_dir / "reddit-codex-001.html"
            raw_path.write_text(
                "<html><head><script>secret()</script></head><body><article><p>Useful claim.</p></article></body></html>",
                encoding="utf-8",
            )
            metadata_path = root / "metadata.json"
            common.write_json(
                metadata_path,
                [
                    {
                        "source_id": "reddit-codex-001",
                        "fetch_status": "fetched",
                        "raw_path": str(raw_path),
                    }
                ],
            )

            rows = extract_text.extract_text(raw_dir, root / "text", metadata_path)

            self.assertEqual(rows[0]["extract_status"], "extracted")
            text = pathlib.Path(rows[0]["text_path"]).read_text(encoding="utf-8")
            self.assertIn("Useful claim.", text)
            self.assertNotIn("secret()", text)

    def test_extract_text_handles_reddit_json(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = pathlib.Path(tmpdir)
            raw_dir = root / "raw"
            raw_dir.mkdir()
            raw_path = raw_dir / "reddit-codex-001.json"
            raw_path.write_text(
                json.dumps(
                    [
                        {"data": {"children": [{"data": {"title": "GPT-5.5 usage thread", "selftext": "More quota details."}}]}},
                        {"data": {"children": [{"data": {"body": "It burns through limits faster."}}]}},
                    ]
                ),
                encoding="utf-8",
            )
            metadata_path = root / "metadata.json"
            common.write_json(
                metadata_path,
                [
                    {
                        "source_id": "reddit-codex-001",
                        "platform": "reddit",
                        "fetch_status": "fetched",
                        "raw_path": str(raw_path),
                        "safe_headers": {"content-type": "application/json"},
                    }
                ],
            )

            rows = extract_text.extract_text(raw_dir, root / "text", metadata_path)

            self.assertEqual(rows[0]["extract_status"], "extracted")
            text = pathlib.Path(rows[0]["text_path"]).read_text(encoding="utf-8")
            self.assertIn("GPT-5.5 usage thread", text)
            self.assertIn("It burns through limits faster.", text)

    def test_build_inventory_uses_extracted_text_and_seed_metadata(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            root = pathlib.Path(tmpdir)
            seed_path = self._write_seed_file(
                root,
                [
                    self._seed_row(
                        posted_at="2026-04-23",
                        engagement={"score": "10", "comments": "4"},
                    )
                ],
            )
            text_dir = root / "text"
            text_dir.mkdir()
            (text_dir / "reddit-codex-001.txt").write_text(
                "GPT-5.5 completed the UI task faster. Additional details follow.",
                encoding="utf-8",
            )
            metadata_path = root / "metadata.json"
            common.write_json(
                metadata_path,
                [
                    {
                        "source_id": "reddit-codex-001",
                        "fetched_at": "2026-04-23T20:00:00+00:00",
                        "fetch_status": "fetched",
                        "extract_status": "extracted",
                        "text_path": str(text_dir / "reddit-codex-001.txt"),
                    }
                ],
            )
            output_path = root / "inventory.jsonl"

            rows = build_inventory.build_inventory(seed_path, text_dir, metadata_path, output_path)

            self.assertEqual(rows[0]["source_id"], "reddit-codex-001")
            self.assertEqual(rows[0]["posted_at"], "2026-04-23")
            self.assertEqual(rows[0]["engagement"]["score"], "10")
            self.assertEqual(rows[0]["fetch_status"], "fetched")
            self.assertEqual(rows[0]["extract_status"], "extracted")
            self.assertEqual(rows[0]["text_char_count"], 0)
            self.assertIn("GPT-5.5 completed the UI task faster", rows[0]["summary"])
            self.assertTrue(output_path.exists())

    def test_verify_sources_uses_low_noise_probe_endpoints(self) -> None:
        reddit = self._seed_row(url="https://www.reddit.com/r/codex/comments/abc/example/")
        hacker_news = self._seed_row(
            source_id="hn-001",
            platform="Hacker News",
            url="https://news.ycombinator.com/item?id=12345",
        )
        github = self._seed_row(
            source_id="gh-001",
            platform="github-issue",
            url="https://github.com/openai/codex/issues/14181",
        )

        self.assertEqual(
            verify_sources.probe_url(reddit),
            "https://www.reddit.com/r/codex/comments/abc/example/.json",
        )
        self.assertEqual(
            verify_sources.probe_url(hacker_news),
            "https://hacker-news.firebaseio.com/v0/item/12345.json",
        )
        self.assertEqual(
            verify_sources.probe_url(github),
            "https://api.github.com/repos/openai/codex/issues/14181",
        )

    def test_verify_sources_accepts_reddit_json_thread(self) -> None:
        seed = self._seed_row(url="https://www.reddit.com/r/codex/comments/abc/example/")
        with mock.patch.object(
            verify_sources.requests,
            "get",
            return_value=FakeResponse(
                status_code=200,
                text=json.dumps([{"data": {"children": [{"data": {"title": "GPT-5.5 usage thread"}}]}}]),
                headers={"Content-Type": "application/json"},
            ),
        ):
            row = verify_sources.verify_one(seed, timeout=1.0)

        self.assertEqual(row["verification_status"], "accept")
        self.assertEqual(row["source_kind"], "discussion_thread")
        self.assertEqual(row["title"], "GPT-5.5 usage thread")

    def test_verify_sources_rejects_inferred_social_permalink(self) -> None:
        seed = self._seed_row(
            source_id="x-001",
            platform="X/Twitter",
            url="https://x.com/openai/status/1914940000000000000",
            collection_caveat="X URL inferred from search-indexed excerpt.",
        )
        with mock.patch.object(
            verify_sources.requests,
            "get",
            return_value=FakeResponse(
                status_code=200,
                text="<html><body></body></html>",
                headers={"Content-Type": "text/html"},
            ),
        ):
            row = verify_sources.verify_one(seed, timeout=1.0)

        self.assertEqual(row["verification_status"], "reject")
        self.assertEqual(row["rejection_reason"], "inferred_social_permalink")

    def test_verify_sources_holds_fetch_blocked_official_source(self) -> None:
        seed = self._seed_row(
            source_id="official-001",
            platform="official",
            url="https://openai.com/index/introducing-gpt-5-5/",
        )
        with mock.patch.object(
            verify_sources.requests,
            "get",
            return_value=FakeResponse(
                status_code=403,
                text="<html><title>Forbidden</title></html>",
                headers={"Content-Type": "text/html"},
            ),
        ):
            row = verify_sources.verify_one(seed, timeout=1.0)

        self.assertEqual(row["verification_status"], "hold")
        self.assertEqual(row["rejection_reason"], "official_fetch_blocked_403")

    def test_verify_sources_does_not_classify_openai_community_as_official(self) -> None:
        seed = self._seed_row(
            source_id="community-001",
            platform="OpenAI Community",
            url="https://community.openai.com/t/usage-limits-of-codex-within-cursor/1356784",
        )
        with mock.patch.object(
            verify_sources.requests,
            "get",
            return_value=FakeResponse(
                status_code=200,
                text="<html><title>Usage Limits of Codex within Cursor - Codex - OpenAI Developer Community</title></html>",
                headers={"Content-Type": "text/html"},
            ),
        ):
            row = verify_sources.verify_one(seed, timeout=1.0)

        self.assertEqual(row["source_kind"], "discussion_thread")
        self.assertEqual(row["verification_status"], "accept")


if __name__ == "__main__":
    unittest.main()
