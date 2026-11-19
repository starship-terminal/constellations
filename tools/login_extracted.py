"""Check a signed-in capture before login-extracted may be done.

webapps-manifest.json carries one login-extracted value per app:

  not-started     no signed-in pass yet
  partial         a pass started and stopped short; notes must say why
  done            the review below passed
  not-applicable  the product has no signed-in web surface

done is not a claim that every gated feature was reached. It is a claim
that the agent walked the signed-in navigation it could open, wrote a
review of that walk, and left an honest gap for anything an empty
account cannot show. A review of the first page only fails.

    python3 tools/login_extracted.py --check

A review names the screens the signed-in product offered and the file
that shows each one. A screen with no file fails. A file that is not in
the package fails. A package screenshot the review never names fails,
so a later page cannot be captured and then left out of the review.
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "webapps-manifest.json"
STATES = ("not-started", "partial", "done", "not-applicable")
REQUIRED_REVIEW = ("offered", "screens", "gaps", "not_submitted")
# The three places a signed-in walk stops early. Each must be answered.
WALK = ("nav", "settings", "create")


def load_manifest(path=MANIFEST):
    return json.loads(path.read_text())


def check_app(app):
    """One app's login-extracted problems. Empty means the row is well formed."""
    name = app.get("name") or app.get("domain") or "?"
    state = app.get("login-extracted")
    problems = []
    if state not in STATES:
        problems.append(f"{name}: login-extracted must be one of {', '.join(STATES)}")
        return problems
    review = app.get("login-review")
    if state == "done":
        problems.extend(_review_problems(name, app, review, require_walk=True))
    elif state == "partial":
        if not (app.get("notes") or "").strip():
            problems.append(f"{name}: a partial login pass needs the stop reason in notes")
        if review is not None:
            problems.extend(_review_problems(name, app, review, require_walk=False))
    elif review is not None:
        problems.append(f"{name}: login-review is only set once a pass has started")
    return problems


def _review_problems(name, app, review, require_walk):
    if not isinstance(review, dict):
        return [f"{name}: login-review must name every signed-in screen and the file that shows it"]
    missing = [key for key in REQUIRED_REVIEW if key not in review]
    if missing:
        return [f"{name}: login-review is missing {', '.join(missing)}"]
    problems = []
    if require_walk:
        problems.extend(_walk_problems(name, review.get("offered")))
    screens = review.get("screens")
    if not isinstance(screens, list) or not screens:
        return problems + [f"{name}: login-review.screens must list every signed-in screen that was open"]
    package = app.get("package") or ""
    folder = ROOT / package if package else None
    seen = set()
    for screen in screens:
        if not isinstance(screen, dict):
            problems.append(f"{name}: a login-review screen must have a name and a file")
            continue
        label = screen.get("name") or "?"
        path = screen.get("file") or ""
        if not path:
            problems.append(f"{name}: {label} has no screenshot")
            continue
        if path in seen:
            problems.append(f"{name}: {label} repeats {path}")
        seen.add(path)
        if folder is None or not (folder / path).is_file():
            problems.append(f"{name}: {label} points at {path}, which is not in the package")
    if require_walk and len(seen) < 2:
        problems.append(
            f"{name}: login-review names one screenshot; a signed-in walk covers more than the first page")
    gaps = review.get("gaps")
    if not isinstance(gaps, list):
        problems.append(f"{name}: login-review.gaps must list what the account could not reach")
    submitted = review.get("not_submitted")
    if not isinstance(submitted, list) or not submitted:
        problems.append(
            f"{name}: login-review.not_submitted must name what was not sent, bought, or created")
    if folder is not None and require_walk:
        problems.extend(_unreviewed_shots(name, folder, seen))
    return problems


def _walk_problems(name, offered):
    """offered answers the three stops: nav, settings, create."""
    if not isinstance(offered, dict):
        return [f"{name}: login-review.offered must answer nav, settings, and create"]
    problems = []
    for stop in WALK:
        item = offered.get(stop)
        if not isinstance(item, dict):
            problems.append(f"{name}: login-review.offered.{stop} must say what that area showed")
            continue
        items = item.get("items")
        if not isinstance(items, list) or not items or not all(isinstance(x, str) and x.strip() for x in items):
            problems.append(f"{name}: login-review.offered.{stop}.items must name what that area showed")
        reached = item.get("reached")
        if not isinstance(reached, list):
            problems.append(f"{name}: login-review.offered.{stop}.reached must name the screens opened there")
            continue
        if set(reached) != set(items):
            problems.append(
                f"{name}: login-review.offered.{stop} leaves "
                f"{', '.join(sorted(set(items) - set(reached))) or 'extra screens'} unopened")
    return problems


def _unreviewed_shots(name, folder, seen):
    """A committed signed-in screenshot the review never names is an unfinished walk.

    Public captures share screenshots/ and are not part of this pass. The
    signed-in kit writes signed-in-<label>.png.
    """
    shots = folder / "screenshots"
    if not shots.is_dir():
        return []
    problems = []
    for path in sorted(shots.glob("signed-in-*.png")):
        rel = path.relative_to(folder).as_posix()
        if rel not in seen:
            problems.append(f"{name}: {rel} is in the package and missing from login-review")
    return problems


def check(doc):
    problems = []
    for app in doc.get("apps") or []:
        problems.extend(check_app(app))
    return problems


def main(argv):
    if argv[1:2] == ["--check"]:
        problems = check(load_manifest())
        if problems:
            print("\n".join(problems), file=sys.stderr)
            return 1
        print(f"login-extracted ok ({len(load_manifest()['apps'])} apps)")
        return 0
    if argv[1:2] == ["--help"]:
        print("usage: login_extracted.py --check")
        return 0
    print("usage: login_extracted.py --check", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
