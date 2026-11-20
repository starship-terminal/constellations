"""build_tokens.py's checks: the committed file passes, and each kind of broken file is refused."""
import copy
import json
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import build_tokens  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
TOKENS = json.loads((ROOT / "tokens.json").read_text())
RAW = [p.read_text() for p in sorted((ROOT / "raw").glob("*.json"))]


class Check(unittest.TestCase):
    def broken(self, value, evidence="Measured"):
        t = copy.deepcopy(TOKENS)
        t["core"]["color"]["zz-test"] = {"$type": "color", "$value": value,
                                         "$extensions": {"source": {"evidence": evidence}}}
        return build_tokens.problems(t, RAW)

    def test_committed_tokens_pass(self):
        self.assertEqual(build_tokens.problems(TOKENS, RAW), [])

    def test_colour_not_in_raw_is_refused(self):
        self.assertTrue(any("in no raw/ reading" in p for p in self.broken("#123457")))

    def test_hand_entered_colour_is_exempt(self):
        self.assertEqual(self.broken("#123457", "Reconstruction"), [])

    def test_dead_alias_is_refused(self):
        self.assertTrue(any("dead alias" in p for p in self.broken("{color.nope}")))

    def test_self_alias_is_refused(self):
        self.assertTrue(any("cycle" in p for p in self.broken("{color.zz-test}")))

    def test_unknown_label_is_refused(self):
        self.assertTrue(any("evidence label" in p for p in self.broken("#121212", "guessed")))


    def test_captured_rgb_value_is_accepted(self):
        t = copy.deepcopy(TOKENS)
        t["core"]["color"]["search-ink"]["$value"] = "rgb(51, 51, 51)"
        self.assertEqual(build_tokens.problems(t, RAW), [])

    def test_alias_through_another_set_is_not_a_loop(self):
        # light.color.ink -> {core.color.zz-ref} -> {color.ink}, which resolves in core to core.color.ink.
        t = copy.deepcopy(TOKENS)
        t["core"]["color"]["zz-ref"] = {"$type": "color", "$value": "{color.ink}",
                                        "$extensions": {"source": {"evidence": "Derived"}}}
        t.setdefault("light", {}).setdefault("color", {})["ink"] = {
            "$type": "color", "$value": "{core.color.zz-ref}", "$extensions": {"source": {"evidence": "Derived"}}}
        self.assertEqual(build_tokens.problems(t, RAW), [])

if __name__ == "__main__":
    unittest.main()
