"""Robinhood tokens (hand-written; no builder): every token has a source, every alias resolves in
its own set, then core, then from the root."""
import json
import pathlib
import unittest

TOKENS = pathlib.Path(__file__).resolve().parent.parent / "tokens.json"


class TokensTest(unittest.TestCase):
    def test_file_loads_and_themes_match_shape(self):
        doc = json.loads(TOKENS.read_text())
        self.assertIn("core", doc)
        self.assertIn("light", doc)
        self.assertIn("dark", doc)
        self.assertEqual(doc["light"]["color"]["accent"]["$value"], "#CCFF00")
        self.assertEqual(doc["dark"]["color"]["accent"]["$value"], "#00C805")
        self.assertEqual(doc["dark"]["color"]["page"]["$value"], "#000000")
        for theme in ("light", "dark"):
            for role in ("page", "surface", "text", "muted", "accent", "border"):
                token = doc[theme]["color"][role]
                self.assertTrue(token["$extensions"]["source"])
                self.assertEqual(token["$extensions"]["evidence"], "Measured")

class Contract(unittest.TestCase):
    def setUp(self):
        self.doc = json.loads(TOKENS.read_text())

    @staticmethod
    def leaves(node, prefix=""):
        for k, v in node.items():
            if k.startswith("$"):
                continue
            if isinstance(v, dict) and "$value" in v:
                yield prefix + k, v
            elif isinstance(v, dict):
                yield from Contract.leaves(v, prefix + k + ".")

    def test_every_token_has_a_source(self):
        missing = [f"{s}.{n}" for s in ("core", "light", "dark") for n, t in self.leaves(self.doc[s])
                   if not (t.get("$extensions") or {}).get("source")]
        self.assertEqual(missing, [])

    def test_every_alias_resolves(self):
        import re
        flat = {f"{s}.{n}": t for s in ("core", "light", "dark") for n, t in self.leaves(self.doc[s])}
        bad = []
        for path, tok in flat.items():
            own = path.split(".")[0]
            for ref in re.findall(r"\{([^{}]+)\}", json.dumps(tok["$value"])):
                if not any(c in flat for c in (f"{own}.{ref}", f"core.{ref}", ref)):
                    bad.append(f"{path} -> {ref}")
        self.assertEqual(bad, [])


if __name__ == "__main__":
    unittest.main()
