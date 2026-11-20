"""Checks on the committed glossgenius tokens that the builders must keep true."""
import json
import pathlib
import re
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((ROOT / "tokens.json").read_text())
C = json.loads((ROOT / "raw" / "components-computed.json").read_text())["components"]
NAMES = {100: "thin", 200: "extralight", 300: "light", 400: "regular", 500: "medium",
         600: "semibold", 700: "bold", 800: "extrabold", 900: "black"}


def leaves(tree, prefix=""):
    for k, v in tree.items():
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict) and not k.startswith("$"):
            yield from leaves(v, prefix + k + ".")


class Tokens(unittest.TestCase):
    def test_weight_names_match_their_values(self):
        for name, t in leaves(T["core"]["font"]["weight"]):
            self.assertEqual(NAMES.get(t["$value"]), name, name)

    def test_weights_equal_the_readings_they_cite(self):
        for name, t in leaves(T["core"]["font"]["weight"]):
            for comp, state in re.findall(r"([a-z0-9-]+) (default|hover)", t["$extensions"]["source"].split("(raw/")[0]):
                st = C[comp]["states"][state]
                w = (st.get("textStyle") or {}).get("fontWeight") or st["style"]["fontWeight"]
                self.assertEqual(int(float(w)), t["$value"], (name, comp))

    def test_a_colour_alias_points_at_a_colour(self):
        sets = {k: dict(leaves(v)) for k, v in T.items() if not k.startswith("$")}
        for setname, tree in sets.items():
            for name, t in tree.items():
                m = re.fullmatch(r"\{(.+)\}", str(t["$value"]))
                if not m or t["$type"] != "color":
                    continue
                target = next((tree.get(m.group(1)) or s.get(m.group(1)) for s in sets.values() if m.group(1) in s), None)
                if target:
                    self.assertEqual(target["$type"], "color", f"{setname}.{name} -> {m.group(1)}")

    def test_components_md_labels_a_colour_once(self):
        text = (ROOT / "components.md").read_text()
        self.assertEqual(re.findall(r"(`[a-z0-9.-]+`) \1", text), [])


if __name__ == "__main__":
    unittest.main()
