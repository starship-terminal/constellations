import json
import pathlib
import re
import unittest

import build_tokens

HERE = pathlib.Path(__file__).resolve().parent
PKG = HERE.parent


def walk(node, path=()):
    if isinstance(node, dict) and "$value" in node:
        yield path, node
        return
    for k, v in node.items():
        if isinstance(v, dict) and not k.startswith("$"):
            yield from walk(v, path + (k,))


def raw_colours():
    """Every colour a raw/ file holds, as lower-case #rrggbb."""
    seen = set()
    for f in (PKG / "raw").glob("*.json"):
        text = f.read_text()
        for h in re.findall(r"#([0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b", text):
            seen.add("#" + (h if len(h) == 6 else "".join(c * 2 for c in h)).lower())
        for body in re.findall(r"rgba?\(([^)]*)\)", text):
            parts = [p for p in re.split(r"[\s,/]+", body.strip()) if p]
            try:
                seen.add("#%02x%02x%02x" % tuple(round(float(p)) for p in parts[:3]))
            except ValueError:
                pass
    return seen


class BuildTokens(unittest.TestCase):
    def test_rebuild_matches(self):
        # Built in memory; the committed file is never rewritten by the test.
        self.assertEqual((PKG / "tokens.json").read_text(), build_tokens.render())

    def test_measured_roles(self):
        tokens = json.loads((PKG / "tokens.json").read_text())
        self.assertEqual(tokens["core"]["color"]["blue5"]["$value"], "#1b66e7")
        self.assertEqual(tokens["light"]["page"]["$value"], "{color.white}")
        self.assertEqual(tokens["dark"]["page"]["$value"], "{color.stDarkGrey6}")
        self.assertEqual(tokens["light"]["positive"]["$value"], "{color.greenLight}")
        self.assertEqual(tokens["dark"]["negative"]["$value"], "{color.redDark}")
        self.assertEqual(tokens["core"]["radius"]["full"]["$value"], "9999px")

    def test_colours_without_a_reading_are_labelled_by_hand(self):
        seen = raw_colours()
        doc = build_tokens.build()
        for theme in ("core", "light", "dark"):
            for path, token in walk(doc[theme]):
                value = token["$value"]
                if token["$type"] != "color" or value.startswith("{"):
                    continue
                if value.lower() not in seen:
                    with self.subTest(token=f"{theme}.{'.'.join(path)}"):
                        self.assertTrue(token["$extensions"]["source"].startswith("Reconstruction: entered by hand"))


if __name__ == "__main__":
    unittest.main()
