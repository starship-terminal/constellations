#!/usr/bin/env python3
"""measure-pass2.mjs folds a rerun into readings-pass2.json state by state (capture/merge-readings.mjs).

A saved component with default and hover, then a rerun whose hover read fails: hover must survive with
its own date, and default takes the new reading and the new date. Runs the module with Node; skipped
when Node is not installed."""
import json
import pathlib
import shutil
import subprocess
import unittest

MODULE = pathlib.Path(__file__).resolve().parent / "capture" / "merge-readings.mjs"

SCRIPT = """
const { mergeReadings } = await import(process.argv[1]);
const earlier = { components: { 'hero-cta': {
  default: { style: { color: 'old' }, readAt: '2026-11-16' },
  hover: { style: { color: 'old-hover' }, readAt: '2026-11-16' },
  crop: 'hero-cta-default.png' },
  footer: { default: { style: { color: 'f' }, readAt: '2026-11-16' } } }, motion: { a: 1 }, notes: ['old'] };
// the rerun read default, then its hover read failed: the component has no hover (or an undefined one)
const out = { components: { 'hero-cta': { default: { style: { color: 'new' } }, hover: undefined, crop: 'hero-cta-default.png' } },
  motion: {}, notes: ['pass stopped early: hover failed'] };
console.log(JSON.stringify(mergeReadings(earlier, out, '2026-11-20')));
"""


@unittest.skipUnless(shutil.which("node"), "node is not installed")
class MergeReadings(unittest.TestCase):
    def setUp(self):
        proc = subprocess.run(["node", "--input-type=module", "-e", SCRIPT, MODULE.as_uri()],
                              capture_output=True, text=True, check=True)
        self.m = json.loads(proc.stdout)

    def test_failed_hover_keeps_the_saved_hover_and_its_date(self):
        hero = self.m["components"]["hero-cta"]
        self.assertEqual(hero["hover"], {"style": {"color": "old-hover"}, "readAt": "2026-11-16"})

    def test_a_new_reading_replaces_its_state_with_this_run_date(self):
        self.assertEqual(self.m["components"]["hero-cta"]["default"], {"style": {"color": "new"}, "readAt": "2026-11-20"})

    def test_a_component_this_run_never_reached_is_kept(self):
        self.assertEqual(self.m["components"]["footer"]["default"]["readAt"], "2026-11-16")
        self.assertEqual(self.m["motion"], {"a": 1})


if __name__ == "__main__":
    unittest.main()
