"""build_tokens.check() runs before tokens.json is written and refuses a broken file (finding 16-6)."""
import copy
import json
import pathlib
import unittest

import build_tokens

TOKENS = pathlib.Path(__file__).resolve().parent.parent / "tokens.json"


def first_literal_colour(doc):
    for set_name in [k for k in doc if not k.startswith("$") and isinstance(doc[k], dict)]:
        for path, token in build_tokens._token_paths(doc[set_name]):
            if token["$type"] == "color" and not str(token["$value"]).startswith("{"):
                return token


class CheckTest(unittest.TestCase):
    def test_committed_tokens_pass(self):
        build_tokens.check(json.loads(TOKENS.read_text()))

    def test_rgba_colour_is_refused(self):
        doc = json.loads(TOKENS.read_text())
        first_literal_colour(doc)["$value"] = "rgba(0, 0, 0, 0.5)"
        with self.assertRaisesRegex(SystemExit, "not #rrggbb"):
            build_tokens.check(doc)

    def test_dangling_alias_and_missing_source_are_refused(self):
        doc = json.loads(TOKENS.read_text())
        token = first_literal_colour(doc)
        bad = copy.deepcopy(doc)
        first_literal_colour(bad)["$value"] = "{color.does-not-exist}"
        with self.assertRaisesRegex(SystemExit, "resolves nowhere"):
            build_tokens.check(bad)
        del token["$extensions"]
        with self.assertRaisesRegex(SystemExit, "no source"):
            build_tokens.check(doc)


    def test_two_token_alias_loop_is_refused(self):
        doc = json.loads(TOKENS.read_text())
        for set_name in [k for k in doc if not k.startswith("$") and isinstance(doc[k], dict)]:
            colours = [(p, t) for p, t in build_tokens._token_paths(doc[set_name]) if t["$type"] == "color"]
            if len(colours) >= 2:
                (pa, a), (pb, b) = colours[:2]
                a["$value"], b["$value"] = "{%s}" % pb, "{%s}" % pa
                break
        with self.assertRaisesRegex(SystemExit, "alias loop"):
            build_tokens.check(doc)

    def test_text_after_an_alias_is_refused(self):
        doc = json.loads(TOKENS.read_text())
        for set_name in [k for k in doc if not k.startswith("$") and isinstance(doc[k], dict)]:
            colours = [(p, t) for p, t in build_tokens._token_paths(doc[set_name]) if t["$type"] == "color"]
            if len(colours) >= 2:
                colours[0][1]["$value"] = "{%s} garbage" % colours[1][0]
                break
        with self.assertRaisesRegex(SystemExit, "one whole alias"):
            build_tokens.check(doc)

    def test_set_qualified_alias_resolves_from_the_root(self):
        doc = json.loads(TOKENS.read_text())
        theme = next(k for k in doc if k not in ("core",) and not k.startswith("$") and isinstance(doc[k], dict))
        theme_colours = [(p, t) for p, t in build_tokens._token_paths(doc[theme]) if t["$type"] == "color"]
        core_colours = [p for p, t in build_tokens._token_paths(doc.get("core", {})) if t["$type"] == "color"]
        # A set-qualified name: a core colour when core has one, else another colour in the theme itself.
        qualified = "core." + core_colours[0] if core_colours else f"{theme}.{theme_colours[1][0]}"
        target = theme_colours[0][1]
        target["$value"] = "{%s}" % qualified
        build_tokens.check(doc)  # resolves at the root; must not raise
        target["$value"] = "{core.no-such-token}"
        with self.assertRaisesRegex(SystemExit, "resolves nowhere"):
            build_tokens.check(doc)

if __name__ == "__main__":
    unittest.main()
