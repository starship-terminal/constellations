#!/usr/bin/env python3
"""Run every package's own tests: each test file anywhere under `systems/<slug>/`.

    python3 tools/package_tests.py            run every package that has tests
    python3 tools/package_tests.py luma-ios   run only the packages named
    python3 tools/package_tests.py -j 4       run four packages at a time (default: CPU count)

A test file is a `test_*.py`, `test_*.mjs` or `*.test.mjs` under the package, at any
depth (`tools/`, `tools/native/`, `tools/capture/`, ...), outside the captured-evidence
folders (`raw/`, `screenshots/`, ...) and dependency folders. Each Python file runs in
its own interpreter with its own folder as the working directory, because tests import
sibling builders by name (`measure`, `build_tokens`, which many packages share) and read
files relative to themselves. Each `.mjs` file runs under `node --test` the same way, and
is reported as skipped when Node.js is not installed.

Every package runs against a private copy of its folder in a scratch directory, so a test
that rewrites `tokens.json` or a board cannot dirty the checkout. The scratch directory
links the rest of the repository, so a test that reads `tools/` or another package still
works. The run also fails when the checkout's `git status` changed while it ran.

A test that needs Pillow when this interpreter lacks it is reported as skipped, not
failed, and the line says so; any other error fails the run. A file listed in
tools/package_tests_expected_failures.json with a reason is known to fail: its failure is
reported and not counted; once it passes the run says so, and an entry that names no
test file fails the run, so the list stays current. `make test` runs this after the top-level tools' tests.

Standard library only.
"""
from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SELF = Path(__file__).resolve()
EXPECTED = "tools/package_tests_expected_failures.json"
NEEDS = {"PIL": "Pillow"}
TEST_NAME = re.compile(r"test_.*\.py|test_.*\.mjs|.*\.test\.mjs")
# Captured evidence and dependency folders: nothing in them is a package test.
SKIP_TOP = {"raw", "screenshots", "components", "boards", "icons", "fonts"}
SKIP_ANY = {"node_modules", "__pycache__", ".venv", ".git"}
TIMEOUT = 900


def test_files(package: Path) -> list[str]:
    """Every test file in one package folder, as POSIX paths relative to it, sorted."""
    found = []
    for folder, dirs, files in os.walk(package):
        rel = Path(folder).relative_to(package)
        dirs[:] = sorted(d for d in dirs if d not in SKIP_ANY and not (rel == Path(".") and d in SKIP_TOP))
        found += [(rel / f).as_posix() for f in files if TEST_NAME.fullmatch(f)]
    return sorted(found)


def packages(root: Path = ROOT, only: list[str] | None = None) -> dict[str, list[str]]:
    """{slug: test files} for every package that has a test file, by slug."""
    out = {}
    for package in sorted(p for p in (root / "systems").iterdir() if p.is_dir()):
        if only and package.name not in only:
            continue
        files = test_files(package)
        if files:
            out[package.name] = files
    return out


def installed(module: str) -> bool:
    """Whether this interpreter can import `module`, so a bad import of an installed
    package (a name Pillow does not have, say) stays an error."""
    return importlib.util.find_spec(module) is not None


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
        if top in NEEDS and not installed(top):
            self.addSkip(test, f"needs {NEEDS[top]}, which {sys.executable} lacks")
        else:
            super().addError(test, err)


def run_here(pattern: str = "test_*.py") -> int:
    """Discover and run the tests matching `pattern` in the working directory."""
    sys.path.insert(0, ".")
    suite = unittest.defaultTestLoader.discover(".", pattern=pattern, top_level_dir=".")
    result = unittest.TextTestRunner(resultclass=Result, verbosity=0, stream=sys.stderr).run(suite)
    needs = sorted({r for _, r in result.skipped if r.startswith("needs ")})
    for reason in needs:
        print(f"skipped: {reason}", file=sys.stderr)
    return 0 if result.wasSuccessful() else 1


def sandbox(root: Path, slug: str) -> tempfile.TemporaryDirectory:
    """A scratch tree holding a copy of systems/<slug>/ and links to everything else."""
    tmp = tempfile.TemporaryDirectory(prefix=f"package-tests-{slug}-")
    scratch = Path(tmp.name)
    for entry in root.iterdir():
        if entry.name not in ("systems", ".git"):
            (scratch / entry.name).symlink_to(entry)
    (scratch / "systems").mkdir()
    for entry in (root / "systems").iterdir():
        if entry.name == slug:
            shutil.copytree(entry, scratch / "systems" / slug, symlinks=True)
        else:
            (scratch / "systems" / entry.name).symlink_to(entry)
    return tmp


def run_file(package: Path, rel: str) -> tuple[bool, str, str]:
    """(passed, one-line summary, output) for one test file in a package copy."""
    path = package / rel
    if path.suffix == ".py":
        cmd = [sys.executable, str(SELF), "--here", path.name]
    else:
        node = shutil.which("node")
        if not node:
            return True, "skipped: needs Node.js", ""
        # TAP explicitly: newer Node versions default to the spec reporter even when piped.
        cmd = [node, "--test", "--test-reporter=tap", path.name]
    try:
        proc = subprocess.run(cmd, cwd=path.parent, capture_output=True, text=True, timeout=TIMEOUT,
                              stdin=subprocess.DEVNULL)
    except subprocess.TimeoutExpired as e:
        return False, f"timed out after {TIMEOUT}s", f"{e.stdout or ''}{e.stderr or ''}"
    output = (proc.stdout or "") + (proc.stderr or "")
    lines = output.strip().splitlines()
    if path.suffix == ".py":
        summary = next((l for l in reversed(lines) if l.startswith(("OK", "FAILED"))), "no result")
        ran = next((l.split()[1] for l in reversed(lines) if l.startswith("Ran ")), "0")
        notes = "".join(f"; {l}" for l in lines if l.startswith("skipped: "))
        line = f"{ran} tests {summary}{notes}"
    else:
        count = lambda key: next((l.split()[-1] for l in reversed(lines) if l.startswith(f"# {key} ")), "0")
        line = f"{count('tests')} tests, {count('fail')} failed (node --test)"
    return proc.returncode == 0, line, output


def run_package(root: Path, slug: str, files: list[str]) -> list[tuple[str, bool, str, str]]:
    with sandbox(root, slug) as scratch:
        package = Path(scratch) / "systems" / slug
        return [(rel, *run_file(package, rel)) for rel in files]


def git_state(root: Path) -> dict[str, str | None] | None:
    """{`git status` entry: digest of that file's contents} for the checkout, or None
    outside a git checkout. The digest catches a test that changes a file that was
    already modified or untracked, whose status entry stays the same."""
    try:
        out = subprocess.run(["git", "-C", str(root), "status", "--porcelain=v1", "-z", "--untracked-files=all"],
                             capture_output=True, check=True).stdout
    except (OSError, subprocess.CalledProcessError):
        return None
    state = {}
    entries = iter(out.split(b"\0"))
    for raw in entries:
        if not raw:
            continue
        entry = raw.decode("utf-8", "surrogateescape")
        if entry[:1] in "RC":
            next(entries, None)  # a rename or copy carries its source path as the next field
        path = root / entry[3:]
        try:
            state[entry] = hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else None
        except OSError:
            state[entry] = None
    return state


def changed_entries(before: dict, after: dict) -> list[str]:
    """Status entries that appeared, disappeared, or whose file contents changed."""
    return sorted(e for e in set(before) | set(after) if before.get(e, "absent") != after.get(e, "absent"))


def load_expected(root: Path) -> dict[str, str]:
    path = root / EXPECTED
    if not path.is_file():
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    bad = [k for k, v in data.items() if not isinstance(v, str) or not v.strip()]
    if bad:
        raise SystemExit(f"{EXPECTED}: every entry needs a reason: {', '.join(bad)}")
    return data


def main(argv: list[str], root: Path = ROOT) -> int:
    if argv[:1] == ["--here"]:
        return run_here(*argv[1:2])
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("slugs", nargs="*", help="run only these packages")
    parser.add_argument("-j", "--jobs", type=int, default=os.cpu_count() or 1, help="packages run at a time")
    args = parser.parse_args(argv)
    found = packages(root, args.slugs or None)
    if args.slugs and len(found) != len(set(args.slugs)):
        print(f"no tests for: {', '.join(sorted(set(args.slugs) - set(found)))}", file=sys.stderr)
        return 2
    expected = load_expected(root)
    before = git_state(root)
    failed, known, fixed = [], [], []
    with concurrent.futures.ThreadPoolExecutor(max(1, args.jobs)) as pool:
        runs = {slug: pool.submit(run_package, root, slug, files) for slug, files in found.items()}
        for slug, run in runs.items():
            for rel, passed, line, output in run.result():
                key = f"systems/{slug}/{rel}"
                if key in expected:
                    if passed:
                        # A warning, not a failure: some listed tests fail only on one
                        # platform, so a pass elsewhere is expected.
                        fixed.append(key)
                        line += f"; passes here but is listed in {EXPECTED}; remove it once it passes everywhere"
                    else:
                        known.append(key)
                        line += f"; expected failure: {expected[key]}"
                elif not passed:
                    failed.append(key)
                print(f"{key}: {line}")
                if not passed and key not in expected:
                    print(output, file=sys.stderr)
    stale = [] if args.slugs else sorted(k for k in expected
                                         if k.removeprefix("systems/").split("/", 1)[0] not in found
                                         or k.split("/", 2)[2] not in found[k.split("/", 2)[1]])
    for key in stale:
        print(f"{EXPECTED} lists {key}, which is not a package test file", file=sys.stderr)
    after = git_state(root)
    dirtied = changed_entries(before, after or {}) if before is not None else []
    for entry in dirtied:
        print(f"a package test changed the checkout: {entry}", file=sys.stderr)
    files = sum(len(v) for v in found.values())
    print(f"{len(found)} packages, {files} test files, {len(failed)} failed"
          + (f": {', '.join(failed)}" if failed else "")
          + (f"; {len(known)} expected failures" if known else ""))
    return 1 if failed or stale or dirtied else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
