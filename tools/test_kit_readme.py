"""tools/kit/README.md's single-file upgrade note against the kit's real imports. A package updated one
script at a time copies the shared helpers that script imports; a helper the note leaves out stops the
script with ERR_MODULE_NOT_FOUND before capture starts (screenshot.mjs gained a safe-url.mjs import while
the note still said to copy screenshot.mjs alone)."""
import re
import unittest
from pathlib import Path

KIT = Path(__file__).resolve().parent / "kit"
CAPTURE = KIT / "capture"
README = (KIT / "README.md").read_text()
IMPORT = re.compile(r"""^import\b[^'"]*from\s+['"](\.{1,2}/[^'"]+)['"]""", re.M)


def imports(path):
    """The kit files a script imports by a relative path, resolved."""
    return [(path.parent / rel).resolve() for rel in IMPORT.findall(path.read_text())]


def closure(path):
    seen, todo = set(), [path.resolve()]
    while todo:
        for dep in imports(todo.pop()):
            if dep not in seen and dep.is_file():
                seen.add(dep)
                todo.append(dep)
    return seen


def upgrade_note():
    start = README.index("When updating an older package's individual script")
    return README[start:README.index("\n\n", start)]


class SingleFileUpgradeNote(unittest.TestCase):
    def test_every_helper_screenshot_mjs_needs_is_named(self):
        note = upgrade_note()
        for dep in sorted(closure(CAPTURE / "screenshot.mjs")):
            with self.subTest(helper=dep.name):
                self.assertIn(f"`{dep.name}`", note)

    def test_every_route_script_that_uses_screenshot_mjs_imports_it(self):
        # the note's claim that render.mjs, public.mjs and shot.mjs import the shared helper
        for rel in ("signed-in/render.mjs", "public/public.mjs", "electron/shot.mjs"):
            with self.subTest(script=rel):
                self.assertIn((CAPTURE / "screenshot.mjs").resolve(), imports(CAPTURE / rel))

    def test_every_helper_the_note_names_exists(self):
        names = set(re.findall(r"`([\w-]+\.mjs)`", upgrade_note()))
        self.assertTrue(names)
        for name in sorted(names):
            with self.subTest(name=name):
                self.assertTrue(list(CAPTURE.rglob(name)), name)


if __name__ == "__main__":
    unittest.main()
