"""Tests for build_tokens.check. Run: python3 -m unittest discover -s tools (from this package)."""
import copy
import json
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import build_tokens  # noqa: E402

DOC = json.loads((pathlib.Path(__file__).resolve().parent.parent / "tokens.json").read_text())


class CheckTest(unittest.TestCase):
    def test_committed_tokens_pass(self):
        build_tokens.check(copy.deepcopy(DOC))

    def test_missing_alias_inside_a_typography_style_fails(self):
        doc = copy.deepcopy(DOC)
        doc["core"]["typography"]["body"]["$value"]["fontWeight"] = "{fontWeight.doesNotExist}"
        with self.assertRaisesRegex(AssertionError, "doesNotExist"):
            build_tokens.check(doc)

    def test_missing_top_level_alias_fails(self):
        doc = copy.deepcopy(DOC)
        doc["light"]["color"]["status"]["info"]["$value"] = "{color.accent.nothing}"
        with self.assertRaisesRegex(AssertionError, "nothing"):
            build_tokens.check(doc)

    def test_neutral_list_keeps_the_readings_evidence(self):
        labels = {t["$extensions"]["source"]["evidence"] for t in DOC["core"]["color"]["neutral"].values()}
        self.assertLessEqual(labels, {"Sampled", "Sampled (text)", "Derived"})
        self.assertGreater(len(labels), 1)


if __name__ == "__main__":
    unittest.main()
