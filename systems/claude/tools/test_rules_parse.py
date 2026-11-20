"""The stylesheet walker keeps nested selectors and outer declarations apart.

rules.py exits at import unless SNAPS is set, and it only reads that variable
when main() runs. A dummy value is enough to load parse() and decls().
"""
import importlib.util
import os
import pathlib
import unittest
from unittest import mock

HERE = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    "rules_under_test", HERE / "capture" / "rules.py")
rules = importlib.util.module_from_spec(spec)
# SNAPS is set only while rules.py loads, then restored: no process-global state leaks to other tests.
with mock.patch.dict(os.environ, {"SNAPS": os.environ.get("SNAPS", os.devnull)}):
    spec.loader.exec_module(rules)


def rows(css):
    return [(conds, sel, rules.decls(body)) for conds, sel, body in rules.parse(css)]


class ParseNestedRules(unittest.TestCase):
    def test_sibling_selectors_stay_whole(self):
        self.assertEqual(
            rows(".parent { .a { color:red; } .b { color:blue; } }"),
            [
                ([".parent"], ".a", [("color", "red")]),
                ([".parent"], ".b", [("color", "blue")]),
            ],
        )

    def test_nested_child_is_not_an_outer_property(self):
        self.assertEqual(
            rows(".outer { border-width:1px; .middle { border-width:2px; "
                 ".inner { border-width:3px; } } margin:0; }"),
            [
                ([".outer", ".middle"], ".inner", [("border-width", "3px")]),
                ([".outer"], ".middle", [("border-width", "2px")]),
                ([], ".outer", [("border-width", "1px"), ("margin", "0")]),
            ],
        )

    def test_quoted_semicolon_stays_in_the_selector(self):
        self.assertEqual(
            rows('.card { &[data-label="a;b"] { color: red } }'),
            [([".card"], '&[data-label="a;b"]', [("color", "red")])],
        )

    def test_declarations_beside_a_nested_rule_stay_on_the_parent(self):
        found = rows(".card { color: red; .title { font-size: 12px } margin: 4px }")
        self.assertIn(([], ".card", [("color", "red"), ("margin", "4px")]), found)
        self.assertIn(([".card"], ".title", [("font-size", "12px")]), found)


if __name__ == "__main__":
    unittest.main()
