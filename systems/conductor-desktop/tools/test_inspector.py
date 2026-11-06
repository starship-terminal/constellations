"""The inspector capture's own helpers. rjs.sh returns the page's result, puts the owner's clipboard text back and leaves no
temporary file. pbcopy, pbpaste and osascript are replaced by stubs over a file, so the real clipboard and
Safari are never touched. shots.py runs a shot's `after` even when the shot fails."""
import os
import pathlib
import shutil
import sys
import subprocess
import tempfile
import unittest

INSPECTOR = pathlib.Path(__file__).resolve().parent / "capture" / "inspector"
RJS = INSPECTOR / "rjs.sh"
STUBS = {
    "pbcopy": '#!/bin/sh\ncat > "$CLIP"\n',
    "pbpaste": '#!/bin/sh\ncat "$CLIP"\n',
    # The console: run the pasted code by answering with a result, as the page's copy() would.
    "osascript": '#!/bin/sh\ncase "$1" in -e) exit 0;; esac\nprintf \'{"ok":true}\' > "$CLIP"\necho ok\n',
}


@unittest.skipUnless(shutil.which("sh"), "needs sh")
class RjsTest(unittest.TestCase):
    def test_result_returned_clipboard_restored_no_temp_left(self):
        with tempfile.TemporaryDirectory() as root:
            root = pathlib.Path(root)
            bin_, tmp = root / "bin", root / "tmp"
            bin_.mkdir(); tmp.mkdir()
            for name, body in STUBS.items():
                (bin_ / name).write_text(body); (bin_ / name).chmod(0o755)
            clip = root / "clip"
            clip.write_text("the owner's clipboard")
            env = {**os.environ, "PATH": f"{bin_}:/usr/bin:/bin", "CLIP": str(clip), "TMPDIR": str(tmp)}
            r = subprocess.run(["sh", str(RJS), "-e", "return {ok: true};"], env=env, capture_output=True, text=True, timeout=30)
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertEqual(r.stdout.strip(), '{"ok":true}')
            self.assertEqual(clip.read_text(), "the owner's clipboard")
            self.assertEqual(list(tmp.iterdir()), [])


class AfterRunsTest(unittest.TestCase):
    def test_after_runs_when_the_shot_fails(self):
        sys.path.insert(0, str(INSPECTOR))
        try:
            import shots
        finally:
            sys.path.remove(str(INSPECTOR))
        calls = []

        def run_js(body, out=None):
            calls.append(body)
            if "after ok" not in body:
                raise RuntimeError("reveal failed")
            return "after ok"

        saved = shots.run_js
        shots.run_js = run_js
        try:
            with self.assertRaises(RuntimeError):
                shots.take("dark", {"name": "menu", "after": "await P.closeAll();"})
        finally:
            shots.run_js = saved
        self.assertTrue(any("await P.closeAll();" in c and "after ok" in c for c in calls))


if __name__ == "__main__":
    unittest.main()
