"""Checks build_tokens.py's output: every token names its source, every alias resolves, the
theme sets agree on names where they should, and the evidence split (painted vs declared) is
kept. Run via tools/package_tests.py."""
import json, re, unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())


def tokens_of(tree, prefix=""):
    for k, v in tree.items():
        if k.startswith("$"):
            continue
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from tokens_of(v, prefix + k + ".")


def aliases(v):
    if isinstance(v, str):
        return re.findall(r"\{([^{}]+)\}", v)
    if isinstance(v, dict):
        return [a for x in v.values() for a in aliases(x)]
    if isinstance(v, list):
        return [a for x in v for a in aliases(x)]
    return []


SETS = ["core", "light", "dark", "accent", "app"]


class Sets(unittest.TestCase):
    def test_sets_exist(self):
        for s in SETS:
            self.assertIn(s, T, s)
            self.assertTrue(list(tokens_of(T[s])), s)

    def test_theme_order(self):
        self.assertEqual(T["$metadata"]["tokenSetOrder"], SETS)

    def test_every_token_has_source(self):
        for s in SETS:
            missing = [n for n, t in tokens_of(T[s])
                       if not (t.get("$extensions") or {}).get("source") and not t.get("$description")]
            self.assertEqual(missing, [], f"{s}: tokens without a source label")

    def test_aliases_resolve(self):
        core_names = {n for n, _ in tokens_of(T["core"])}
        for s in SETS:
            names = core_names | {n for n, _ in tokens_of(T[s])}
            for n, t in tokens_of(T[s]):
                for a in aliases(t["$value"]):
                    self.assertIn(a, names, f"{s}.{n}: alias {{{a}}} points at nothing")

    def test_light_dark_parity(self):
        l, d = ({n for n, _ in tokens_of(T[s])} for s in ("light", "dark"))
        self.assertEqual(l, d, "dark must name exactly light's tokens")

    def test_accent_near_parity(self):
        l, a = ({n for n, _ in tokens_of(T[s])} for s in ("light", "accent"))
        # the accent probe carries partner+b2b sheets only; consumer-only hashed vars are absent
        self.assertLessEqual(len(l - a), 10, f"accent lacks {len(l - a)} light tokens")
        self.assertEqual(a - l, set(), "accent names tokens light does not")

    def test_core_scale_counts(self):
        names = {n for n, _ in tokens_of(T["core"])}
        for fam in ("spacing.", "sizes.", "durations.", "easings.", "aspectRatios.", "shadows."):
            self.assertTrue(any(n.startswith(fam) for n in names), f"core.{fam} empty")

    def test_painted_labels(self):
        dark = dict(tokens_of(T["dark"]))
        # the dark source text says where it paints; the accent set carries an explicit "painted" extension
        self.assertIn("painted", (dark["colors.foreground.neutral"].get("$extensions") or {}).get("source", ""))
        accent = dict(tokens_of(T["accent"]))
        self.assertIn("declared", (accent["colors.foreground.neutral"].get("$extensions") or {}).get("painted", ""))

    def test_signature_values(self):
        light = dict(tokens_of(T["light"]))
        self.assertEqual(light["colors.foreground.neutral"]["$value"], "#0d0d0d")
        self.assertEqual(light["colors.background.accent"]["$value"], "#6950f3")
        dark = dict(tokens_of(T["dark"]))
        self.assertEqual(dark["colors.foreground.neutral"]["$value"], "#f5f5f5")

    def test_component_and_motion(self):
        core = dict(tokens_of(T["core"]))
        self.assertEqual(core["component.header.height"]["$value"], "72px")
        self.assertTrue(any(n.startswith("motion.") for n in core), "core.motion empty")


if __name__ == "__main__":
    unittest.main()
