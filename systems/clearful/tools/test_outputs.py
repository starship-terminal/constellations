"""Checks on clearful's committed tokens."""
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((ROOT / "tokens.json").read_text())


def leaves(tree, prefix=""):
    for k, v in tree.items():
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict) and not k.startswith("$"):
            yield from leaves(v, prefix + k + ".")


class Tokens(unittest.TestCase):
    def test_the_semantic_set_holds_no_pixel_sample(self):
        # docs/EVIDENCE.md: a sampled colour is labelled and kept out of the semantic sets.
        for name, t in leaves(T["light"]):
            src = t["$extensions"]["source"].lower()
            self.assertNotIn("sampl", src, name)
            self.assertNotIn("raw/full/", src, name)

    def test_samples_say_sampled(self):
        for name, t in leaves(T["core"]["sampled"]):
            self.assertTrue(t["$extensions"]["source"].startswith("Sampled:"), name)


if __name__ == "__main__":
    unittest.main()
