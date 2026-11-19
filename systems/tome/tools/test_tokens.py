"""The 404-page tokens resolve, and the colours match the reading in raw/computed.json."""
import json
import pathlib
import unittest

HERE = pathlib.Path(__file__).resolve().parent.parent


def flatten(node, path=()):
    if isinstance(node, dict) and "$value" in node:
        yield ".".join(path), node["$value"]
        return
    if isinstance(node, dict):
        for key, child in node.items():
            if not key.startswith("$"):
                yield from flatten(child, path + (key,))


class Tokens(unittest.TestCase):
    def test_measured_colours_match_the_reading(self):
        tokens = json.loads((HERE / "tokens.json").read_text())
        raw = json.loads((HERE / "raw" / "computed.json").read_text())
        flat = dict(flatten(tokens))
        for theme in ("dark", "light"):
            declared = raw["customProperties"][theme]
            self.assertEqual(flat[f"{theme}.background.page"], declared["--background"])
            self.assertEqual(flat[f"{theme}.text.primary"], declared["--foreground"])
            self.assertEqual(flat[f"{theme}.text.secondary"], declared["--secondary"])
            self.assertEqual(flat[f"{theme}.border.focus"], declared["--focus"])
            self.assertEqual(flat[f"{theme}.border.divider"], declared["--divider"])

    def test_radius_and_focus_were_on_the_page(self):
        tokens = json.loads((HERE / "tokens.json").read_text())
        flat = dict(flatten(tokens))
        self.assertEqual(flat["core.radius.control"], "6px")
        self.assertEqual(flat["core.size.outline"], "2px")
        self.assertEqual(flat["dark.border.focus"], "#0070f3")


if __name__ == "__main__":
    unittest.main()
