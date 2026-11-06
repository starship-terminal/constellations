"""capture/shot.sh hands only a numeric window id to screencapture. The window lookup, screencapture and sips
are stubs in a temporary folder, so nothing is captured and the real raw-shots folder is not touched."""
import os
import pathlib
import shutil
import subprocess
import tempfile
import unittest

SHOT = pathlib.Path(__file__).resolve().parent / "capture" / "shot.sh"
LOOKUP = "zwin"   # the window-id helper shot.sh calls


@unittest.skipUnless(shutil.which("sh"), "needs a POSIX sh")
class ShotTest(unittest.TestCase):
    def shot(self, out, code=0):
        with tempfile.TemporaryDirectory() as d:
            d = pathlib.Path(d)
            cap, bin_ = d / "capture", d / "bin"
            cap.mkdir(); bin_.mkdir()
            shutil.copy(SHOT, cap / "shot.sh")
            log = d / "calls"
            stubs = {LOOKUP: f"#!/bin/sh\nprintf '%s' '{out}'\nexit {code}\n",
                     "screencapture": f'#!/bin/sh\necho screencapture >> "{log}"\n',
                     "sips": f'#!/bin/sh\necho sips >> "{log}"\n'}
            for name, body in stubs.items():
                where = cap if name == LOOKUP else bin_
                (where / name).write_text(body); (where / name).chmod(0o755)
            env = {**os.environ, "HOME": str(d), "PATH": f"{bin_}:/usr/bin:/bin", "RWIN": str(cap / LOOKUP)}
            r = subprocess.run(["sh", str(cap / "shot.sh"), "light", "t"], env=env, capture_output=True, text=True, timeout=30)
            return r.returncode, log.read_text().split() if log.exists() else []

    def test_bad_ids_never_reach_capture(self):
        for out, code in (("", 0), ("abc", 0), ("12 34", 0), ("4242", 1)):
            rc, calls = self.shot(out, code)
            self.assertNotEqual(rc, 0, (out, code))
            self.assertEqual(calls, [], (out, code))

    def test_a_window_id_reaches_capture(self):
        self.assertEqual(self.shot("4242"), (0, ["screencapture", "sips"]))


if __name__ == "__main__":
    unittest.main()
