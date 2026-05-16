"""Tests for extract_inject_markers (Phase 2 Slice 3).

Per slice spec: no markers, one marker, multiple markers, nested (fail),
unbalanced (fail). Plus: duplicate key (fail), mismatched end (fail),
whitespace tolerance, body extraction correctness, and a regression test
that find_marker (Slice 2) preserves its apply-time tolerance after the
Slice 3 refactor.
"""

import unittest

from harness_modifier.contract import inject_operations
from harness_modifier.contract.inject_operations import (
    MarkerExtractionError,
    MarkerRegion,
    extract_inject_markers,
    find_marker,
)


def _wrap(body: str, key: str) -> str:
    return (
        f"<!-- GSD_MODIFIER:start key:{key} -->\n"
        f"{body}\n"
        f"<!-- GSD_MODIFIER:end key:{key} -->"
    )


class ExtractInjectMarkersHappyPathTests(unittest.TestCase):
    def test_no_markers_returns_empty_dict(self) -> None:
        content = "<header/>\n<body>plain content</body>\n<footer/>\n"
        self.assertEqual(extract_inject_markers(content), {})

    def test_empty_content_returns_empty_dict(self) -> None:
        self.assertEqual(extract_inject_markers(""), {})

    def test_one_marker_returns_single_entry(self) -> None:
        body = "INJECTED LINE 1\nINJECTED LINE 2"
        key = "GSD_MODIFIER:test-carrier:single-op"
        content = "<prefix/>\n" + _wrap(body, key) + "\n<suffix/>\n"
        result = extract_inject_markers(content)
        self.assertEqual(list(result.keys()), [key])
        region = result[key]
        self.assertEqual(region.key, key)
        self.assertEqual(region.body, body)
        # start_line/end_line are 0-indexed line positions of the marker LINES themselves
        self.assertEqual(region.start_line, 1)  # line after <prefix/>
        self.assertEqual(region.end_line, 4)  # 1 + 1 body line + 1 second body line + 1 end marker = lines 1,2,3,4

    def test_multiple_markers_returned_in_first_occurrence_order(self) -> None:
        body_a = "BODY A"
        body_b = "BODY B"
        body_c = "BODY C"
        key_a = "GSD_MODIFIER:multi:a"
        key_b = "GSD_MODIFIER:multi:b"
        key_c = "GSD_MODIFIER:multi:c"
        content = (
            _wrap(body_a, key_a)
            + "\nseparator1\n"
            + _wrap(body_b, key_b)
            + "\nseparator2\n"
            + _wrap(body_c, key_c)
            + "\n"
        )
        result = extract_inject_markers(content)
        self.assertEqual(list(result.keys()), [key_a, key_b, key_c])
        self.assertEqual(result[key_a].body, body_a)
        self.assertEqual(result[key_b].body, body_b)
        self.assertEqual(result[key_c].body, body_c)

    def test_marker_with_empty_body(self) -> None:
        key = "GSD_MODIFIER:empty:body"
        content = (
            f"<!-- GSD_MODIFIER:start key:{key} -->\n"
            f"<!-- GSD_MODIFIER:end key:{key} -->\n"
        )
        result = extract_inject_markers(content)
        self.assertIn(key, result)
        self.assertEqual(result[key].body, "")

    def test_marker_with_multi_line_body_preserves_internal_newlines(self) -> None:
        body = "line one\n\nline three after blank\nline four"
        key = "GSD_MODIFIER:multiline:body"
        content = _wrap(body, key) + "\n"
        result = extract_inject_markers(content)
        self.assertEqual(result[key].body, body)

    def test_indented_marker_lines_are_recognized(self) -> None:
        # The marker lines may have leading/trailing whitespace; extract_inject_markers
        # uses .strip() on each line before matching.
        key = "GSD_MODIFIER:indented:op"
        content = (
            "  <!-- GSD_MODIFIER:start key:" + key + " -->\n"
            "BODY\n"
            "\t<!-- GSD_MODIFIER:end key:" + key + " -->\n"
        )
        result = extract_inject_markers(content)
        self.assertIn(key, result)
        self.assertEqual(result[key].body, "BODY")


class ExtractInjectMarkersFailurePathTests(unittest.TestCase):
    def test_nested_markers_raise_with_reason_nested(self) -> None:
        outer = "GSD_MODIFIER:outer:op"
        inner = "GSD_MODIFIER:inner:op"
        content = (
            f"<!-- GSD_MODIFIER:start key:{outer} -->\n"
            f"<!-- GSD_MODIFIER:start key:{inner} -->\n"
            f"<!-- GSD_MODIFIER:end key:{inner} -->\n"
            f"<!-- GSD_MODIFIER:end key:{outer} -->\n"
        )
        with self.assertRaises(MarkerExtractionError) as ctx:
            extract_inject_markers(content)
        self.assertEqual(ctx.exception.reason, "nested")
        self.assertEqual(ctx.exception.key, inner)

    def test_unbalanced_start_marker_raises(self) -> None:
        key = "GSD_MODIFIER:unbalanced:start"
        content = (
            f"<!-- GSD_MODIFIER:start key:{key} -->\n"
            f"BODY\n"
            # no end marker
        )
        with self.assertRaises(MarkerExtractionError) as ctx:
            extract_inject_markers(content)
        self.assertEqual(ctx.exception.reason, "unbalanced_start")
        self.assertEqual(ctx.exception.key, key)

    def test_unbalanced_end_marker_raises(self) -> None:
        key = "GSD_MODIFIER:unbalanced:end"
        content = (
            "header\n"
            f"<!-- GSD_MODIFIER:end key:{key} -->\n"
        )
        with self.assertRaises(MarkerExtractionError) as ctx:
            extract_inject_markers(content)
        self.assertEqual(ctx.exception.reason, "unbalanced_end")
        self.assertEqual(ctx.exception.key, key)

    def test_mismatched_end_key_raises(self) -> None:
        key_a = "GSD_MODIFIER:mismatch:a"
        key_b = "GSD_MODIFIER:mismatch:b"
        content = (
            f"<!-- GSD_MODIFIER:start key:{key_a} -->\n"
            f"BODY\n"
            f"<!-- GSD_MODIFIER:end key:{key_b} -->\n"
        )
        with self.assertRaises(MarkerExtractionError) as ctx:
            extract_inject_markers(content)
        self.assertEqual(ctx.exception.reason, "mismatched_end")
        self.assertEqual(ctx.exception.key, key_b)

    def test_duplicate_key_raises(self) -> None:
        key = "GSD_MODIFIER:dup:op"
        content = _wrap("body 1", key) + "\nseparator\n" + _wrap("body 2", key) + "\n"
        with self.assertRaises(MarkerExtractionError) as ctx:
            extract_inject_markers(content)
        self.assertEqual(ctx.exception.reason, "duplicate_key")
        self.assertEqual(ctx.exception.key, key)


class MarkerExtractionErrorContractTests(unittest.TestCase):
    def test_error_carries_structured_fields(self) -> None:
        key = "GSD_MODIFIER:contract:op"
        content = f"<!-- GSD_MODIFIER:end key:{key} -->\n"
        try:
            extract_inject_markers(content)
        except MarkerExtractionError as exc:
            self.assertEqual(exc.reason, "unbalanced_end")
            self.assertEqual(exc.key, key)
            self.assertEqual(exc.line, 1)
            self.assertIn("unbalanced end marker", str(exc))
        else:
            self.fail("expected MarkerExtractionError")


class FindMarkerToleranceAfterRefactorTests(unittest.TestCase):
    """find_marker is now implemented in terms of extract_inject_markers but must
    preserve Slice 2's apply-time tolerance: malformed content returns None, not
    a hard failure. This is the safety property that lets apply re-correct a
    corrupt on-disk state."""

    def test_find_marker_returns_none_for_absent_key(self) -> None:
        content = "<header/>\n" + _wrap("body", "GSD_MODIFIER:present:op") + "\n"
        self.assertIsNone(find_marker(content, "GSD_MODIFIER:absent:op"))

    def test_find_marker_returns_region_for_present_key(self) -> None:
        key = "GSD_MODIFIER:present:op"
        body = "BODY"
        content = "<header/>\n" + _wrap(body, key) + "\n<footer/>\n"
        region = find_marker(content, key)
        self.assertIsNotNone(region)
        assert region is not None
        self.assertEqual(region.body, body)
        self.assertEqual(region.key, key)

    def test_find_marker_tolerates_nested_markers(self) -> None:
        # The on-disk content is corrupt (nested), but apply must still be able
        # to produce a corrected output. So find_marker returns None for the
        # absent key rather than propagating MarkerExtractionError.
        content = (
            "<!-- GSD_MODIFIER:start key:GSD_MODIFIER:a:op -->\n"
            "<!-- GSD_MODIFIER:start key:GSD_MODIFIER:b:op -->\n"
            "<!-- GSD_MODIFIER:end key:GSD_MODIFIER:b:op -->\n"
            "<!-- GSD_MODIFIER:end key:GSD_MODIFIER:a:op -->\n"
        )
        # find_marker must return None — apply-time tolerance per docstring
        self.assertIsNone(find_marker(content, "GSD_MODIFIER:a:op"))
        # extract_inject_markers, by contrast, surfaces the corruption
        with self.assertRaises(MarkerExtractionError):
            extract_inject_markers(content)

    def test_find_marker_tolerates_unbalanced_start(self) -> None:
        content = "<!-- GSD_MODIFIER:start key:GSD_MODIFIER:dangling:op -->\nBODY\n"
        self.assertIsNone(find_marker(content, "GSD_MODIFIER:dangling:op"))
        with self.assertRaises(MarkerExtractionError):
            extract_inject_markers(content)


class ExtractInjectMarkersBoundaryTests(unittest.TestCase):
    def test_marker_inside_a_code_fence_is_still_detected_when_on_its_own_line(self) -> None:
        # Markers are line-oriented; if they appear on their own line they are
        # detected regardless of surrounding content. Worth surfacing because
        # users may wrap modifier content in fenced code blocks.
        key = "GSD_MODIFIER:fence:op"
        content = (
            "```\n"
            f"<!-- GSD_MODIFIER:start key:{key} -->\n"
            "BODY\n"
            f"<!-- GSD_MODIFIER:end key:{key} -->\n"
            "```\n"
        )
        result = extract_inject_markers(content)
        self.assertIn(key, result)
        self.assertEqual(result[key].body, "BODY")

    def test_non_marker_html_comments_are_ignored(self) -> None:
        content = (
            "<!-- a regular html comment -->\n"
            "<!-- GSD_MODIFIER:something_else -->\n"
            "body\n"
        )
        # No GSD_MODIFIER:start or :end on its own line; result is empty
        self.assertEqual(extract_inject_markers(content), {})

    def test_marker_with_inline_text_not_recognized(self) -> None:
        # If the marker is not on its own line (e.g., embedded in prose), it is
        # NOT a marker per the line-oriented contract. This protects against
        # accidental triggering by documentation that quotes the marker syntax.
        key = "GSD_MODIFIER:inline:op"
        content = f"prose text <!-- GSD_MODIFIER:start key:{key} --> more text\n"
        self.assertEqual(extract_inject_markers(content), {})


if __name__ == "__main__":
    unittest.main()
