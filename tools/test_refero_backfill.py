"""Tests for tools/refero/backfill_components.py's component resolution and
retry selection. Pure functions over in-memory data; nothing is fetched.
Run with `make test`."""
import json
import sys
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
sys.path.insert(0, str(TOOLS / "refero"))
import backfill_components as backfill  # noqa: E402


def result(*htmls):
    return {"designSystem": {"components": [{"name": f"c{i}", "html": h}
                                            for i, h in enumerate(htmls)]}}


class ResolveComponentsTest(unittest.TestCase):
    def test_a_ref_resolves_to_its_text_row(self):
        blob = "1e:T9,<b>é</b>x".encode("utf-8")  # 9 UTF-8 bytes: é is two
        r = result("$1e")
        self.assertEqual(backfill.resolve_components(r, blob), (1, 0))
        self.assertEqual(r["designSystem"]["components"][0]["html"], "<b>é</b>")

    def test_an_unresolved_ref_becomes_none_not_a_stored_ref(self):
        r = result("$2f", "$undefined", "<i>kept</i>", None)
        r["designSystem"]["components"].append("not a component")
        self.assertEqual(backfill.resolve_components(r, b"1e:T2,ab"), (1, 1))
        self.assertEqual([c["html"] for c in r["designSystem"]["components"][:4]],
                         [None, None, "<i>kept</i>", None])


class HasTruthyHtmlTest(unittest.TestCase):
    def test_only_resolved_html_counts(self):
        self.assertTrue(backfill.has_truthy_html(json.dumps(result(None, "<p>x</p>"))))
        self.assertFalse(backfill.has_truthy_html(json.dumps(result("$1e", None, ""))))
        self.assertFalse(backfill.has_truthy_html(json.dumps({"designSystem": {}})))
        self.assertFalse(backfill.has_truthy_html("not json"))
        self.assertFalse(backfill.has_truthy_html(None))


if __name__ == "__main__":
    unittest.main()
