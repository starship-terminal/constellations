#!/usr/bin/env python3
"""Run every package's own tests: each `systems/<slug>/tools/test_*.py`.

    python3 tools/package_tests.py            run every package that has tests
    python3 tools/package_tests.py luma-ios   run only the packages named

Each package runs in its own interpreter with its `tools/` folder as the working
directory, because its tests import sibling builders by name (`measure`,
`build_tokens`, which many packages share) and read `../tokens.json`. A test that
needs Pillow when this interpreter lacks it is reported as skipped, not failed, and
the line says so; any other error fails the run. `make test` runs this after the
top-level tools' tests.

Standard library only.
"""
from __future__ import annotations

import re
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NEEDS = {"PIL": "Pillow"}


def packages(root: Path = ROOT, only: list[str] | None = None) -> list[Path]:
    """Every `systems/<slug>/tools/` folder holding a test_*.py, by slug."""
    found = sorted(p.parent for p in (root / "systems").glob("*/tools/test_*.py"))
    found = list(dict.fromkeys(found))
    if only:
        found = [p for p in found if p.parent.name in only]
    return found


class Result(unittest.TextTestResult):
    """Counts an error raised because an optional module is missing as a skip."""

    def addError(self, test, err):
        # A module that fails to import during discovery comes back as a plain ImportError
        # holding the original traceback as text, so read the name from the message too.
        missing = getattr(err[1], "name", None) if isinstance(err[1], ImportError) else None
        if isinstance(err[1], ImportError) and not missing:
            found = re.search(r"No module named '([^']+)'", str(err[1]))
            missing = found and found.group(1)
        top = (missing or "").split(".")[0]
        if top in NEEDS:
            self.addSkip(test, f"needs {NEEDS[top]}, which {sys.executable} lacks")
        else:
            super().addError(test, err)


def run_here() -> int:
    """Discover and run the tests in the working directory (one package's tools/)."""
    sys.path.insert(0, ".")
    suite = unittest.defaultTestLoader.discover(".", pattern="test_*.py", top_level_dir=".")
    result = unittest.TextTestRunner(resultclass=Result, verbosity=0, stream=sys.stderr).run(suite)
    needs = sorted({r for _, r in result.skipped if r.startswith("needs ")})
    for reason in needs:
        print(f"skipped: {reason}", file=sys.stderr)
    return 0 if result.wasSuccessful() else 1


def main(argv: list[str]) -> int:
    if argv[:1] == ["--here"]:
        return run_here()
    dirs = packages(only=argv or None)
    if argv and len(dirs) != len(set(argv)):
        missing = set(argv) - {d.parent.name for d in dirs}
        print(f"no tests for: {', '.join(sorted(missing))}", file=sys.stderr)
        return 2
    failed = []
    for d in dirs:
        slug = d.parent.name
        proc = subprocess.run([sys.executable, str(Path(__file__).resolve()), "--here"],
                              cwd=d, capture_output=True, text=True)
        out = proc.stderr.strip().splitlines()
        summary = next((l for l in reversed(out) if l.startswith(("OK", "FAILED"))), "no result")
        ran = next((l.split()[1] for l in reversed(out) if l.startswith("Ran ")), "0")
        notes = "".join(f"; {l}" for l in out if l.startswith("skipped: "))
        print(f"systems/{slug}: {ran} tests {summary}{notes}")
        if proc.returncode:
            failed.append(slug)
            print(proc.stderr, file=sys.stderr)
    print(f"{len(dirs)} packages, {len(failed)} failed" + (f": {', '.join(failed)}" if failed else ""))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
