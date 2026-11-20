"""Patreon token checks. Run from the package tools/ directory."""
import importlib.util
import json
import pathlib
import unittest

HERE = pathlib.Path(__file__).resolve().parent
TOKENS = json.loads((HERE.parent / "tokens.json").read_text())
RAW = json.loads((HERE.parent / "raw" / "computed.json").read_text())
_spec = importlib.util.spec_from_file_location("patreon_check", HERE / "build" / "build_tokens.py")
CHECK = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(CHECK)


class TokenTest(unittest.TestCase):
    def test_every_token_is_a_reading_or_says_it_was_typed(self):
        # tools/build/build_tokens.py checks every token against raw/computed.json; it writes nothing.
        self.assertEqual(CHECK.check(), [])

    def edited(self, path, value):
        """check()'s problems with one token's $value replaced, restored afterwards."""
        node = CHECK.TOKENS
        for part in path[:-1]:
            node = node[part]
        saved = node[path[-1]]["$value"]
        try:
            node[path[-1]]["$value"] = value
            return CHECK.check()
        finally:
            node[path[-1]]["$value"] = saved

    def test_check_catches_values_no_pin_covers(self):
        # core.color.nprogress, the easing, the measured nav size and the login font have no exact
        # pin, so only the all-token loop can catch these.
        cases = [
            (("core", "color", "nprogress"), "#123456", "core.color.nprogress"),
            (("core", "motion", "easing"), [0.111, 0.222, 0.333, 0.444], "core.motion.easing"),
            (("core", "font", "family", "login"), "Unrecorded Family, Arial", "core.font.family.login"),
        ]
        for path, value, name in cases:
            self.assertTrue(any(p.startswith(name + ":") for p in self.edited(path, value)), name)
        nav = dict(CHECK.TOKENS["core"]["typography"]["nav"]["$value"], fontSize="987px")
        self.assertTrue(any(p.startswith("core.typography.nav:") for p in self.edited(("core", "typography", "nav"), nav)))

    def test_check_catches_an_alias_loop(self):
        problems = self.edited(("light", "color", "page"), "{color.page}")
        self.assertTrue(any(p.startswith("light.color.page:") and "loop" in p for p in problems), problems)

    def test_primary_matches_reading(self):
        self.assertEqual(TOKENS["core"]["color"]["primary"]["$value"], RAW["resolved"]["--color-primary"])

    def test_button_height_matches_desktop(self):
        self.assertEqual(
            TOKENS["core"]["size"]["button"]["$value"],
            RAW["computed"]["desktop1440"]["getStarted"]["height"],
        )

    def test_login_page_is_measured(self):
        self.assertEqual(TOKENS["light"]["color"]["login"]["page"]["$value"], "#020202")
        self.assertEqual(RAW["computed"]["login"]["htmlBackground"], "rgb(2, 2, 2)")

    def test_every_token_has_a_source(self):
        missing = []

        def walk(node, path):
            if isinstance(node, dict) and "$value" in node:
                if "source" not in node.get("$extensions", {}):
                    missing.append(path)
            elif isinstance(node, dict):
                for key, child in node.items():
                    if not key.startswith("$"):
                        walk(child, f"{path}.{key}" if path else key)

        walk(TOKENS, "")
        self.assertEqual(missing, [])


if __name__ == "__main__":
    unittest.main()
