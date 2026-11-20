"""The committed tokens.json is what build_tokens.build() makes from raw/, and check() refuses a broken file.

Nothing here writes tokens.json: the build runs in memory."""
import copy
import json
import pathlib
import re
import subprocess
import sys
import unittest

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import build_tokens  # noqa: E402

TOKENS = HERE.parent / "tokens.json"
RAW = HERE.parent / "raw"


def tok(type_, value):
    return {"$type": type_, "$value": value, "$extensions": {"source": {"evidence": "Measured", "capture": "fixture"}}}


FIXTURE = {
    "core": {
        "color": {"red": tok("color", "#e50914")},
        "fontWeight": {"bold": tok("fontWeight", 700)},
        "typography": {"display": tok("typography", {"fontWeight": "{fontWeight.bold}", "fontSize": "40px"})},
        "easing": {"button": tok("cubicBezier", [0.4, 0, 0.68, 0.06])},
    },
    "dark": {"background": {"action": tok("color", "{color.red}")}},
}


class TokensTest(unittest.TestCase):
    def test_committed_file_is_what_the_builder_makes(self):
        self.assertEqual(json.loads(TOKENS.read_text()), build_tokens.build())

    def test_committed_tokens_pass(self):
        build_tokens.check(json.loads(TOKENS.read_text()))

    def test_red_is_the_measured_action(self):
        doc = json.loads(TOKENS.read_text())
        self.assertEqual(doc["core"]["color"]["red"]["$value"], "#e50914")
        self.assertEqual(doc["dark"]["background"]["page"]["$value"], "{color.page}")

    def test_easings_are_the_declared_beziers_as_lists(self):
        hawkins = json.loads((RAW / "hawkins-vars.json").read_text())["vars"]
        easing = json.loads(TOKENS.read_text())["core"]["motion"]["easing"]
        for key, var in (("button", "--hcw--local-design--Button-Easing"), ("hover", "--hcw--local-design--Button-EasingHovered")):
            declared = re.fullmatch(r"cubic-bezier\(([^)]*)\)", hawkins[var]["computed"]).group(1)
            self.assertEqual(easing[key]["$value"], [float(x) for x in declared.split(",")])

    def test_every_measured_literal_is_in_raw(self):
        # The builder types some readings as literals; each one labelled Measured must appear in raw/.
        text = " ".join(p.read_text() for p in RAW.glob("*.json"))
        rgb = {"#%02x%02x%02x" % tuple(int(x) for x in m) for m in re.findall(r"rgb\((\d+),\s*(\d+),\s*(\d+)\)", text)}
        found = rgb | {h.lower() for h in re.findall(r"#[0-9a-fA-F]{6}\b", text)}

        def leaves(node, path=""):
            if isinstance(node, dict) and "$value" in node:
                yield path, node
            elif isinstance(node, dict):
                for k, v in node.items():
                    if not k.startswith("$"):
                        yield from leaves(v, f"{path}.{k}" if path else k)

        for path, t in leaves(json.loads(TOKENS.read_text())["core"]):
            v, src = t["$value"], t["$extensions"]["source"]
            if src["evidence"] != "Measured" or not isinstance(v, str) or v.startswith("{"):
                continue
            if t["$type"] == "color" and v.startswith("#"):
                self.assertIn(v, found, path)
            elif t["$type"] == "dimension" and v.endswith("px") and "--hcw" not in src["note"]:
                self.assertRegex(text, rf"(?<![\d.]){re.escape(v)}", path)

    def test_fixture_passes(self):
        build_tokens.check(copy.deepcopy(FIXTURE))

    def test_missing_alias_inside_a_typography_style_fails(self):
        doc = copy.deepcopy(FIXTURE)
        doc["core"]["typography"]["display"]["$value"]["fontWeight"] = "{fontWeight.doesNotExist}"
        with self.assertRaisesRegex(SystemExit, "doesNotExist"):
            build_tokens.check(doc)

    def test_missing_top_level_alias_fails(self):
        doc = copy.deepcopy(FIXTURE)
        doc["dark"]["background"]["action"]["$value"] = "{color.nothing}"
        with self.assertRaisesRegex(SystemExit, "nothing"):
            build_tokens.check(doc)

    def test_a_token_without_evidence_fails(self):
        doc = copy.deepcopy(FIXTURE)
        del doc["core"]["color"]["red"]["$extensions"]
        with self.assertRaisesRegex(SystemExit, "no source"):
            build_tokens.check(doc)

    def test_a_string_cubic_bezier_fails(self):
        doc = copy.deepcopy(FIXTURE)
        doc["core"]["easing"]["button"]["$value"] = "[0.4, 0, 0.68, 0.06]"
        with self.assertRaisesRegex(SystemExit, "four numbers"):
            build_tokens.check(doc)

    def test_a_boolean_cubic_bezier_fails(self):
        # bool is an int in Python; CSS cannot use cubic-bezier(True, False, True, False)
        doc = copy.deepcopy(FIXTURE)
        doc["core"]["easing"]["button"]["$value"] = [True, False, True, False]
        with self.assertRaisesRegex(SystemExit, "four numbers"):
            build_tokens.check(doc)

    def test_the_check_still_runs_under_python_O(self):
        code = ("import sys, build_tokens; doc = {'core': {'c': {'$type': 'color', '$value': '{nope}', "
                "'$extensions': {'source': {'evidence': 'Measured'}}}}, 'dark': {}}\n"
                "try:\n build_tokens.check(doc)\nexcept SystemExit as e:\n print(e); sys.exit(3)")
        done = subprocess.run([sys.executable, "-O", "-c", code], cwd=HERE, capture_output=True, text=True)
        self.assertEqual(done.returncode, 3, done.stderr)
        self.assertIn("dangling alias", done.stdout)


if __name__ == "__main__":
    unittest.main()
