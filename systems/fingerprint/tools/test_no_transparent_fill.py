"""No measured fill is transparent: a transparent backgroundColor reading is
no fill (the colour comes from an ancestor) and is never committed, either as
a literal or as an alias to a transparent declared name.

Run from the package root: python3 -m unittest discover -s tools
"""
import json
import pathlib
import re
import unittest

T = json.loads((pathlib.Path(__file__).resolve().parent.parent / "tokens.json").read_text())
TRANSPARENT = re.compile(r"transparent|rgba\(\s*[\d.]+[,\s]+[\d.]+[,\s]+[\d.]+\s*[,/]\s*0(\.0+)?%?\s*\)")


def tokens(tree, prefix=""):
    for k, v in tree.items():
        if k.startswith("$"):
            continue
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from tokens(v, prefix + k + ".")


SETS = [k for k in T if not k.startswith("$")]
INDEX = {s: dict(tokens(T[s])) for s in SETS}


def resolve(setname, v, depth=0):
    m = re.fullmatch(r"\{([^{}]+)\}", str(v))
    if not m or depth > 10:
        return str(v)
    for s in (setname, "core"):
        if m.group(1) in INDEX.get(s, {}):
            return resolve(s, INDEX[s][m.group(1)]["$value"], depth + 1)
    return str(v)


class NoTransparentFillTest(unittest.TestCase):
    def test_measured_fills_are_painted(self):
        for s in SETS:
            for n, t in INDEX[s].items():
                if t.get("$type") == "color" and "computed backgroundColor" in t.get("$extensions", {}).get("source", ""):
                    self.assertIsNone(TRANSPARENT.fullmatch(resolve(s, t["$value"])), f"{s}.{n}")


if __name__ == "__main__":
    unittest.main()
