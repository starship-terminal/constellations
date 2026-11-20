"""build_tokens.py's checks against raw/: the committed file passes, each kind of broken file is refused."""
import copy
import json
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import build_tokens  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent.parent
TOKENS = json.loads((HERE / "tokens.json").read_text())
RAW = build_tokens.load_raw()
SRC = {"source": "Measured. test fixture"}


class Check(unittest.TestCase):
    def test_committed_tokens_pass(self):
        self.assertEqual(build_tokens.problems(TOKENS, RAW), [])

    def broken(self, **leaf):
        t = copy.deepcopy(TOKENS)
        t["dark"]["zz-test"] = dict({"$type": "color", "$extensions": SRC}, **leaf)
        return build_tokens.problems(t, RAW)

    def test_colour_not_in_raw_is_refused(self):
        self.assertTrue(any("no file under raw" in p for p in self.broken(**{"$value": "#123457"})))

    def test_raw_colour_is_accepted_in_any_notation(self):
        self.assertEqual(self.broken(**{"$value": "#FF5E3E"}), [])
        self.assertEqual(self.broken(**{"$value": "rgb(255, 94, 62)"}), [])

    def test_dead_alias_is_refused(self):
        self.assertTrue(any("dead alias" in p for p in self.broken(**{"$value": "{nope}"})))

    def test_self_alias_is_refused(self):
        self.assertTrue(any("cycle" in p for p in self.broken(**{"$value": "{zz-test}"})))

    def test_unlabelled_source_is_refused(self):
        t = copy.deepcopy(TOKENS)
        t["dark"]["zz-test"] = {"$value": "#ff5e3e", "$type": "color", "$extensions": {"source": "guessed"}}
        self.assertTrue(any("evidence label" in p for p in build_tokens.problems(t, RAW)))

    def test_missing_source_is_refused(self):
        t = copy.deepcopy(TOKENS)
        t["dark"]["zz-test"] = {"$value": "#ff5e3e", "$type": "color"}
        self.assertTrue(any("missing $extensions.source" in p for p in build_tokens.problems(t, RAW)))

    def test_by_hand_colour_is_passed_only_with_its_label(self):
        t = copy.deepcopy(TOKENS)
        t["dark"]["zz-test"] = {"$value": "#123457", "$type": "color",
                                "$extensions": {"source": build_tokens.BY_HAND + ". test"}}
        self.assertEqual(build_tokens.problems(t, RAW), [])

    def test_rgba_alpha_rounds_half_up(self):
        self.assertIn("#1b1b204d", build_tokens.colours_in("rgba(27, 27, 32, 0.3)"))


    def test_chain_through_core_resolves_from_core(self):
        # light.font.shared -> {core.font.shared} -> {font.base} must read core.font.base (Inter),
        # not the light theme's own font.base override.
        tree = {"core": {"font": {"base": {"$value": "Inter"}, "shared": {"$value": "{font.base}"}}},
                "light": {"font": {"base": {"$value": "{font.shared}"}, "shared": {"$value": "{core.font.shared}"}}}}
        self.assertIsNone(build_tokens.resolve(tree, "light", "core.font.shared", set()))
        tree["core"]["font"]["base"]["$value"] = "{font.shared}"   # now core loops on itself
        self.assertIn("cycle", build_tokens.resolve(tree, "light", "core.font.shared", set()))

if __name__ == "__main__":
    unittest.main()
