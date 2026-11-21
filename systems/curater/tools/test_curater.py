"""Package invariants for the Curater capture."""
import json
import pathlib
import re
import unittest

HERE = pathlib.Path(__file__).resolve().parent.parent


class CuraterPackage(unittest.TestCase):
    def test_tokens_have_sources(self):
        tokens = json.loads((HERE / "tokens.json").read_text())
        missing = []

        def walk(node, path):
            if not isinstance(node, dict):
                return
            if "$value" in node:
                source = (node.get("$extensions") or {}).get("source")
                if not source:
                    missing.append(path)
            else:
                for key, child in node.items():
                    if key.startswith("$"):
                        continue
                    walk(child, f"{path}.{key}" if path else key)

        walk(tokens, "")
        self.assertEqual(missing, [])

    def test_required_files(self):
        for name in ("README.md", "DESIGN.md", "tokens.json", "style-guide.html",
                     "components.md", "patterns.md", "site-tree.md", "login-review.json", "icon.png"):
            self.assertTrue((HERE / name).exists(), name)

    def test_no_email_literals(self):
        text = "\n".join(
            p.read_text(errors="replace")
            for p in HERE.rglob("*")
            if p.is_file() and p.suffix in {".md", ".json", ".py", ".html", ".tsv"}
        )
        self.assertIsNone(re.search(r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}", text))


if __name__ == "__main__":
    unittest.main()
