"""style-guide.html declares every custom property inside a rule and uses only declared ones."""
import re
import unittest
from pathlib import Path

PAGE = (Path(__file__).resolve().parent.parent / "style-guide.html").read_text()


class StyleGuide(unittest.TestCase):
    def test_no_custom_property_outside_a_rule(self):
        css = PAGE.split("<style>", 1)[1].split("</style>", 1)[0]
        depth, stray = 0, []
        for line in css.splitlines():
            if depth == 0 and re.match(r"\s*--[\w-]+\s*:", line):
                stray.append(line.strip()[:40])
            depth += line.count("{") - line.count("}")
        self.assertEqual(stray, [])

    def test_every_var_is_declared(self):
        declared = set(re.findall(r"(--[\w-]+)\s*:", PAGE))
        # 'var(--color-' + name + ')' in the page script builds a name at run time; skip that prefix.
        used = {u for u in re.findall(r"var\((--[\w-]+)", PAGE) if u != "--color-"}
        self.assertEqual(sorted(used - declared), [])


if __name__ == "__main__":
    unittest.main()
