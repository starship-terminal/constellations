"""tokens.json must rebuild from the raw readings, with inset shadow layers kept wherever
Chromium writes `inset`, and font sizes typed as DTCG dimensions.

Run from the package root: python3 -m unittest discover -s tools
"""
import json
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import build_tokens  # noqa: E402

TOKENS = pathlib.Path(__file__).resolve().parent.parent / "tokens.json"


def leaves(node):
    if isinstance(node, dict):
        if "$value" in node:
            yield node
            return
        for k, v in node.items():
            if not k.startswith("$"):
                yield from leaves(v)


class BuildTokensTest(unittest.TestCase):
    def test_committed_tokens_match_builder(self):
        self.assertEqual(json.loads(TOKENS.read_text()), build_tokens.tokens)

    def test_inset_kept_first_or_last(self):
        first = build_tokens.parse_shadow("inset 0 .5px 0 0 #fff0")
        last = build_tokens.parse_shadow("rgba(255, 255, 255, 0) 0px 0.5px 0px 0px inset")
        self.assertTrue(first[0]["inset"] and last[0]["inset"])
        self.assertEqual(last[0]["offsetY"], "0.5px")

    def test_unreadable_layer_raises(self):
        for bad in ("0px 1px", "0px 1px 2px wobble rgba(0, 0, 0, 0.1)"):
            with self.assertRaises(ValueError, msg=bad):
                build_tokens.parse_shadow(bad)

    def test_committed_rim_layers_are_inset(self):
        for theme in ("light", "dark"):
            for step in ("2", "5"):
                layers = build_tokens.tokens[theme]["shadow"][step]["$value"]
                self.assertEqual([bool(l.get("inset")) for l in layers[:2]], [True, True], f"{theme}.shadow.{step}")

    def test_viewport_warning_only_for_the_old_probe(self):
        import ast, re
        src = (pathlib.Path(__file__).resolve().parent / "build_component_tokens.py").read_text()
        node = next(n for n in ast.parse(src).body if isinstance(n, ast.FunctionDef) and n.name == "viewport_note")
        entry = {"raw": "100vw", "note": "viewport-relative, resolved at 1440 x 900"}
        for probe, warned in ((None, True), ("1440x900", False)):
            V = {"resolved": {"light": {"--w": entry}}}
            if probe:
                V["probeViewport"] = probe
            ns = {"V": V, "re": re}
            exec(compile(ast.Module([node], []), "viewport_note", "exec"), ns)
            self.assertEqual("recapture needed" in ns["viewport_note"]("--w"), warned, probe)

    def test_no_fontsize_type(self):
        self.assertNotIn("fontSize", {t["$type"] for t in leaves(build_tokens.tokens)})


if __name__ == "__main__":
    unittest.main()
