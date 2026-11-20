#!/usr/bin/env python3
"""Teal tokens only contain values the 2026-11-19 readings recorded."""
import json
import re
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
TOKENS = json.loads((HERE / "tokens.json").read_text())
READINGS = json.loads((HERE / "raw" / "readings.json").read_text())


class TokensTest(unittest.TestCase):
    def test_marketing_yellow_matches_declaration(self):
        self.assertEqual(TOKENS["light"]["color"]["yellow"]["$value"], "#f5b501")
        self.assertEqual(READINGS["declaredMarketing"]["--color-teal-yellow"], "#f5b501")

    def test_marketing_face_is_roobert(self):
        self.assertIn("Roobert", TOKENS["core"]["font"]["marketing"]["$value"])

    def test_cta_height_is_measured(self):
        self.assertEqual(TOKENS["core"]["size"]["cta"]["$value"], "53px")
        self.assertEqual(READINGS["marketing"]["cta"]["height"], 53)

    def test_app_field_radius_is_measured(self):
        self.assertEqual(TOKENS["core"]["radius"]["xs"]["$value"], "3px")
        self.assertEqual(READINGS["app"]["field"]["borderRadius"], "3px")

    def test_every_token_has_a_source(self):
        missing = []

        def walk(node, path):
            if isinstance(node, dict) and "$value" in node:
                source = node.get("$extensions", {}).get("source", "")
                if not source.startswith(("Measured", "Derived", "Reconstruction: entered by hand")):
                    missing.append(path)
            elif isinstance(node, dict):
                for key, value in node.items():
                    if key.startswith("$"):
                        continue
                    walk(value, f"{path}.{key}" if path else key)

        walk(TOKENS["core"], "core")
        walk(TOKENS["light"], "light")
        walk(TOKENS["app"], "app")
        self.assertEqual(missing, [])

    def test_committed_file_matches_builder(self):
        sys.path.insert(0, str(HERE / "tools"))
        import build_tokens
        self.assertEqual((HERE / "tokens.json").read_text(), build_tokens.render())

    def test_measured_colours_are_in_the_readings(self):
        raw = (HERE / "raw" / "readings.json").read_text().lower()
        rgb = {"#%02x%02x%02x" % tuple(int(float(c)) for c in m.split(",")[:3])
               for m in re.findall(r"rgba?\(([\d.]+, [\d.]+, [\d.]+)", raw)}
        for theme in ("light", "app"):
            for name, token in TOKENS[theme]["color"].items():
                value = token["$value"].lower()
                if token["$extensions"]["source"].startswith("Measured") and value.startswith("#"):
                    with self.subTest(token=f"{theme}.color.{name}"):
                        self.assertTrue(value in raw or value in rgb, value)

    def test_measured_values_are_whole_values_in_the_readings(self):
        """Every scalar of a Measured or Derived token is a whole raw value, or one part of a raw shorthand."""
        def colour(s):
            m = re.fullmatch(r"rgba?\(\s*([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\s*\)", s)
            if not m:
                return s
            h = "#%02x%02x%02x" % tuple(int(float(c)) for c in m.groups()[:3])
            return h + ("%02x" % int(float(m.group(4)) * 255 + 0.5) if m.group(4) and float(m.group(4)) < 1 else "")

        seen = set()

        def collect(node):
            if isinstance(node, dict):
                for v in node.values():
                    collect(v)
            elif isinstance(node, list):
                for v in node:
                    collect(v)
            else:
                text = str(node).strip().lower()
                seen.add(colour(text))
                if isinstance(node, (int, float)) and not isinstance(node, bool):
                    seen.add(f"{node}px")
                seen.update(colour(part) for part in re.split(r"\s+(?![^()]*\))", text))

        collect(READINGS)

        def leaves(node, path):
            if isinstance(node, dict) and "$value" in node:
                yield path, node
            elif isinstance(node, dict):
                for k, v in node.items():
                    if not k.startswith("$"):
                        yield from leaves(v, f"{path}.{k}" if path else k)

        def scalars(v):
            if isinstance(v, dict):
                for x in v.values():
                    yield from scalars(x)
            elif isinstance(v, list):
                for x in v:
                    yield from scalars(x)
            else:
                yield str(v).strip().lower()

        for path, token in leaves(TOKENS, ""):
            if token["$extensions"]["source"].startswith("Reconstruction"):
                continue
            for s in scalars(token["$value"]):
                if s.startswith("{"):
                    continue
                with self.subTest(token=path):
                    self.assertIn(colour(s), seen, s)

    def test_no_dark_set(self):
        self.assertNotIn("dark", TOKENS)


if __name__ == "__main__":
    unittest.main()
