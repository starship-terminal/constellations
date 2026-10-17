#!/usr/bin/env python3
"""Re-grade the scorecard criteria a script can check, and write a new audit snapshot.

    python3 tools/grade.py            print the scripted grades for every package
    python3 tools/grade.py --write    write scorecard/audits/<today>[-N].json, then every README's Health
    python3 tools/grade.py --check    fail if the newest snapshot or a README's Health is stale
    python3 tools/grade.py --criteria SLUG    print the wording a reviewer grades SLUG against

A snapshot copies the newest audit, replaces the grades below with fresh results, and
applies each criterion's `capture` rule from scorecard/criteria.json (criteria a capture
cannot meet are graded not applicable). Every other grade is a reviewer's judgement and is
carried over unchanged, so it stays exactly as reliable as the review that set it.

A reviewer grades a package against the wording for its catalog `platform` (web, mobile
or desktop; `--criteria SLUG` prints it). Each package in a snapshot records `platform` and
`reviewedPlatform`, the platform whose wording its reviewed grades were set against. When
the two wordings differ for a reviewed criterion, `--check` warns until a `--review` of the
package sets them again; so does a capture newer than the review.

| Criterion | Scripted check |
|---|---|
| F15 Contrast | The `text` and `muted` swatches on the `page` and `surface` swatches of every theme in catalog.json's preview, at 4.5:1. A translucent surface is blended over the page |
| F16 Provenance | The share of tokens carrying `$extensions.source`, `$description` or `description` |
| K2 Do and don't | A "Do and don't" section in the package README with rules that link to its images |
| K3 DESIGN.md | `catalog.py`'s DESIGN.md check finds nothing to fix |

Standard library only.
"""
from __future__ import annotations

import argparse
import copy
import datetime as dt
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import catalog  # noqa: E402
import health  # noqa: E402
import scorecard  # noqa: E402

ROOT = catalog.ROOT
SCRIPTED = ("F15", "F16", "K2", "K3")
METHOD = ("Grades marked \"Script:\" were recomputed by tools/grade.py from the packages as they are "
          "now (contrast, token provenance, the README's Do and don't list, and DESIGN.md freshness). "
          "Criteria a capture cannot meet are graded not applicable (see each criterion). Every other "
          "grade comes from the review that last set it (each package's reviewed date, else the {base} "
          "review): ")


# ---------------------------------------------------------------- the four checks


def theme_palettes(system: dict, tokens: dict) -> tuple[dict, list[str]]:
    """The role paths to check for every declared theme. A theme with no preview palette
    borrows the first palette's paths with the theme set swapped (`light.text` becomes
    `light-mobile.text`) when every one exists; otherwise it is reported as unchecked."""
    palettes = dict(system["preview"].get("swatches", {}))
    flat = catalog.flatten(tokens)
    unchecked = []
    model_theme, model = next(iter(palettes.items()), (None, {}))
    for theme in system.get("themes", []):
        if theme in palettes:
            continue
        swapped = {role: theme + path[len(model_theme):] if path.startswith(model_theme + ".") else None
                   for role, path in model.items()}
        if model and all(p and p in flat for p in swapped.values()):
            palettes[theme] = swapped
        else:
            unchecked.append(theme)
    return palettes, unchecked


def contrast_rows(system: dict) -> tuple[list[dict], dict, list[str]]:
    """(rows, palettes, unchecked themes): the `text` and `muted` swatches on the `page`
    and `surface` swatches of every theme palette, in theme, then role, then background
    order. A translucent surface is blended over the page. tools/brief.py lists the same rows."""
    tokens = json.loads((ROOT / system["tokens"]).read_text())
    palettes, unchecked = theme_palettes(system, tokens)
    rows = []
    for theme, roles in palettes.items():
        page, surface = roles.get("page"), roles.get("surface")
        for role in ("text", "muted"):
            for bg_role, bg in (("page", page), ("surface", surface)):
                if not roles.get(role) or not bg:
                    continue
                r = catalog.contrast(tokens, theme, [f"{roles[role]}:{bg}"], over=page)[0]
                rows.append({**r, "theme": theme, "role": role, "bgRole": bg_role})
    return rows, palettes, unchecked


def grade_contrast(system: dict) -> tuple[str, str]:
    rows, palettes, unchecked = contrast_rows(system)
    if not rows:
        return "missing", "Script: no text and background swatches to check"
    checked = [r for r in rows if r["ratio"] is not None]
    worst = min(checked, key=lambda r: r["ratio"]) if checked else None
    where = (f"{worst['ratio']:.2f}:1 {worst['theme']} {worst['role']} ({worst['fg']}) on {worst['bgRole']} "
             f"({worst['bg']})") if worst else "no pair could be measured"
    text_bad = [r for r in rows if r["role"] == "text" and r["status"] != "pass"]
    muted_bad = [r for r in rows if r["role"] == "muted" and r["status"] != "pass"]
    pairs = lambda n: f"{n} pair{'s' if n != 1 else ''}"
    gap = f"; {', '.join(unchecked)} not checked (no palette)" if unchecked else ""
    if text_bad:
        return "missing", f"Script: primary text fails {pairs(len(text_bad))}; worst {where}{gap}"
    if muted_bad:
        return "partly", f"Script: primary text passes; secondary fails {pairs(len(muted_bad))}, worst {where}{gap}"
    if unchecked:
        return "partly", f"Script: all {len(rows)} checked pairs pass; lowest {where}{gap}"
    return "meets", f"Script: all {len(rows)} pairs pass 4.5:1 across {len(palettes)} themes; lowest {where}"


def _token_nodes(node, out: list) -> None:
    if not isinstance(node, dict):
        return
    if "$value" in node or ("value" in node and not isinstance(node["value"], dict)):
        out.append(node)
        return
    for key, child in node.items():
        if not key.startswith("$"):
            _token_nodes(child, out)


def grade_provenance(system: dict) -> tuple[str, str]:
    nodes: list = []
    _token_nodes(json.loads((ROOT / system["tokens"]).read_text()), nodes)
    if not nodes:
        return "missing", "Script: no tokens found"
    labelled = sum(1 for n in nodes if (n.get("$extensions") or {}).get("source")
                   or n.get("$description") or n.get("description"))
    share = labelled / len(nodes)
    grade = "meets" if labelled == len(nodes) else "partly" if share >= 0.8 else "missing"
    return grade, f"Script: {labelled} of {len(nodes)} tokens name their source"


DO_HEADING = re.compile(r"^(#{1,6})\s*do(?:'s)? and don'?t", re.I | re.M)
IMAGE_LINK = re.compile(r"\]\(([^)\s]+\.(?:png|jpe?g|gif|webp|svg))[)#?\s]", re.I)


ITEM = re.compile(r"^(\s*)(?:[-*+]|\d+\.)\s+(.*)$")


def list_items(section: str) -> list[str]:
    """Top-level list items with their wrapped continuation lines joined, so a link that
    falls on a rule's second line still counts. Text before the first item is an
    introduction and skipped. After a blank line only an indented line continues the
    item; a heading or an unindented paragraph ends the list."""
    items: list[str] = []
    base = None
    blank = False
    for line in section.splitlines():
        m = ITEM.match(line)
        if m and (base is None or len(m.group(1)) <= base):
            base = len(m.group(1)) if base is None else base
            items.append(m.group(2))
            blank = False
        elif not items:
            continue  # an introduction before the first rule
        elif not line.strip():
            blank = True
        elif items and (line.startswith((" ", "\t")) or not blank) and not line.lstrip().startswith("#"):
            items[-1] += " " + line.strip()
            blank = False
        else:
            break
    return [i for i in items if i.strip()]


def do_and_dont(readme: str) -> tuple[str, list[str]] | None:
    """(the heading's text, its rules) for the README's "Do and don't" section, or None
    when there is no such heading. The section runs to the next heading of its level or
    higher. tools/brief.py reads the same rules."""
    m = DO_HEADING.search(readme)
    if not m:
        return None
    level = len(m.group(1))
    line_end = readme.find("\n", m.start())
    heading = readme[m.start():line_end if line_end != -1 else len(readme)].lstrip("#").strip()
    rest = readme[m.end():].split("\n", 1)[1] if "\n" in readme[m.end():] else ""
    end = re.search(rf"^#{{1,{level}}}\s", rest, re.M)
    section = rest[:end.start()] if end else rest
    return heading, list_items(section)


def grade_do_and_dont(system: dict) -> tuple[str, str]:
    found = do_and_dont((ROOT / system["entry"]).read_text())
    if found is None:
        return "missing", "Script: no \"Do and don't\" section in the README"
    rules = found[1]
    linked = [r for r in rules if IMAGE_LINK.search(r + " ")]
    if len(rules) >= 3 and len(linked) == len(rules):
        return "meets", f"Script: {len(rules)} rules, each linking a screenshot or crop"
    if rules:
        return "partly", f"Script: {len(rules)} rules, {len(linked)} linking an image (needs 3+, all linked)"
    return "missing", "Script: the section has no rules"


def grade_design_md(system: dict) -> tuple[str, str]:
    problems = catalog.design_md_problems(system)
    if problems:
        return "missing", "Script: " + problems[0]
    return "meets", "Script: DESIGN.md matches a fresh generation"


CHECKS = {"F15": grade_contrast, "F16": grade_provenance, "K2": grade_do_and_dont, "K3": grade_design_md}


def scripted(system: dict) -> dict[str, dict]:
    return {cid: dict(zip(("grade", "evidence"), check(system))) for cid, check in CHECKS.items()}


# ---------------------------------------------------------------- the snapshot


META = ("name", "goodFor", "url", "captured", "themes", "platform")


def reviewable(criteria: dict) -> list[dict]:
    """The criteria a reviewer grades: not scripted here, and not a capture rule."""
    return [c for c in criteria["criteria"] if c["id"] not in SCRIPTED and not c.get("capture")]


def wording_changed(criteria: dict, system: dict, platform: str) -> list[str]:
    """Reviewed criteria whose wording for `platform` differs from the wording the
    package's reviewed grades were set against."""
    was = system.get("reviewedPlatform", scorecard.BASE_PLATFORM)
    return [c["id"] for c in reviewable(criteria)
            if scorecard.done_when(c, platform) != scorecard.done_when(c, was)]


def review_sheet(criteria: dict, system: dict) -> list[str]:
    """What a reviewer of one package grades: every reviewed criterion in the package's
    platform wording, marked where that differs from the web wording."""
    platform = system.get("platform", scorecard.BASE_PLATFORM)
    auto = [c["id"] for c in criteria["criteria"] if c["id"] in SCRIPTED or c.get("capture")]
    lines = [f"{system['slug']} is a {platform} package. Grade each criterion below against this wording, "
             f"as {{\"<id>\": {{\"grade\": \"meets|partly|missing|na\", \"evidence\": \"...\"}}}}; "
             f"{', '.join(auto)} are set automatically."]
    for c in reviewable(criteria):
        text = scorecard.done_when(c, platform)
        own = f" ({platform} wording)" if text != c["doneWhen"] else ""
        lines.append(f"{c['id']:<4} {c['title']}{own}: {text}")
    return lines


def snapshot(criteria: dict, base: dict, catalog_systems: list[dict], date: str,
             categories: dict | None = None, reviews: dict[str, dict] | None = None,
             review_method: str | None = None) -> dict:
    """The newest audit with each package's details refreshed from the catalog, any fresh
    reviews merged in, scripted grades replaced and capture rules applied. A package in
    the catalog but not in the base audit is left out until a review adds it.

    `reviews` maps a slug to {criterion: {grade, evidence}} from a new review of that
    package; it may only set reviewed criteria, and the package records the review date.
    `review_method` replaces the account of how the reviewed grades were set; later
    snapshots carry it forward, so it should cover every review still in the scorecard."""
    out = copy.deepcopy(base)
    out.pop("_seq", None)
    out["date"] = date
    out["rubric"] = str(criteria.get("version", base.get("rubric", "1")))
    # A snapshot made from an earlier scripted one still credits the original review.
    out["base"] = base.get("base", base["date"])
    if review_method and not reviews:
        raise SystemExit("--method describes a review; pass it with --review")
    out["reviewMethod"] = review_method or base.get("reviewMethod", base["method"])
    out["method"] = METHOD.format(base=out["base"]) + out["reviewMethod"]
    by_slug = {s["slug"]: s for s in catalog_systems}
    capture_rules = {c["id"]: c["capture"] for c in criteria["criteria"] if c.get("capture")}
    reviewed_ids = {c["id"] for c in reviewable(criteria)}
    for slug, grades in (reviews or {}).items():
        if slug not in by_slug:
            raise SystemExit(f"review for {slug}: not in catalog.json")
        wrong = sorted(set(grades) - reviewed_ids)
        if wrong:
            raise SystemExit(f"review for {slug} sets {', '.join(wrong)}, which are scripted or capture rules")
        # A review dates the whole package, so it must grade every reviewed criterion.
        missing = sorted(reviewed_ids - set(grades), key=lambda c: (c[0], int(c[1:]) if c[1:].isdigit() else 0))
        if missing:
            raise SystemExit(f"review for {slug} is incomplete; it also needs {', '.join(missing)}")
        # A package's first review adds it; the loop below fills in its details.
        if slug not in {s["slug"] for s in out["systems"]}:
            out["systems"].append({"slug": slug, "grades": {}})
    for system in out["systems"]:
        source = by_slug.get(system["slug"])
        if not source:
            continue
        for key in META:
            if key in source:
                system[key] = source[key]
        if categories and source.get("category") in categories:
            system["category"] = categories[source["category"]]
        elif "category" not in system and "category" in source:
            system["category"] = source["category"]
        if system["slug"] in (reviews or {}):
            system["grades"].update(reviews[system["slug"]])
            system["reviewed"] = date
            system["reviewedPlatform"] = system.get("platform", scorecard.BASE_PLATFORM)
        else:
            # Grades reviewed before rubric 3 were set against its one wording, the web one.
            system.setdefault("reviewedPlatform", scorecard.BASE_PLATFORM)
        system["grades"].update(scripted(source))
        for cid, reason in capture_rules.items():
            system["grades"][cid] = {"grade": "na", "evidence": f"Not applicable to a capture: {reason}"}
    return out


def stale(criteria: dict, audit: dict, catalog_systems: list[dict], categories: dict) -> tuple[list, list]:
    """Problems (scripted grades or package details that no longer match the packages)
    and warnings (a package captured after its reviewed grades were last set, or graded
    against another platform's wording than the one its platform now uses)."""
    problems, warnings = [], []
    by_slug = {s["slug"]: s for s in catalog_systems}
    version = str(criteria.get("version", ""))
    if version and audit.get("rubric") != version:
        problems.append(f"scorecard rubric {audit.get('rubric')!r} differs from scorecard/criteria.json "
                        f"version {version!r}")
    for system in audit["systems"]:
        source = by_slug.get(system["slug"])
        if not source:
            problems.append(f"{system['slug']}: in the scorecard but not in catalog.json")
            continue
        for cid, fresh in scripted(source).items():
            saved = system["grades"].get(cid, {})
            if saved != fresh:
                problems.append(f"{system['slug']} {cid}: scorecard has {saved.get('grade')} "
                                f"({saved.get('evidence', '')!r}), the package now gives {fresh['grade']} "
                                f"({fresh['evidence']!r})")
        for key in META:
            if system.get(key) != source.get(key):
                problems.append(f"{system['slug']}: scorecard {key} {system.get(key)!r} differs from catalog.json")
        label = categories.get(source.get("category"))
        if label and system.get("category") != label:
            problems.append(f"{system['slug']}: scorecard category {system.get('category')!r} differs from {label!r}")
        reviewed = system.get("reviewed", audit.get("base", audit["date"]))
        if source.get("captured", "") > reviewed:
            warnings.append(f"{system['slug']}: captured {source['captured']}, reviewed grades date from {reviewed}; "
                            "re-review it and pass --review")
        platform = source.get("platform", scorecard.BASE_PLATFORM)
        changed = wording_changed(criteria, system, platform)
        if changed:
            was = system.get("reviewedPlatform", scorecard.BASE_PLATFORM)
            warnings.append(f"{system['slug']}: reviewed grades for {', '.join(changed)} were set against the {was} "
                            f"wording; re-review it against the {platform} wording "
                            f"(`python3 tools/grade.py --criteria {system['slug']}`) and pass --review")
    for slug in sorted(set(by_slug) - {s["slug"] for s in audit["systems"]}):
        warnings.append(f"{slug}: in catalog.json but never reviewed for the scorecard")
    return problems, warnings


def next_path(date: str) -> Path:
    folder = scorecard.DATA / "audits"
    path, n = folder / f"{date}.json", 1
    while path.exists():
        n += 1
        path = folder / f"{date}-{n}.json"
    return path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--write", action="store_true", help="write a new audit snapshot")
    parser.add_argument("--check", action="store_true", help="fail if the newest snapshot is stale")
    parser.add_argument("--review", action="append", default=[], metavar="SLUG=FILE",
                        help="with --write, merge a fresh review of one package (JSON {criterion: {grade, evidence}})")
    parser.add_argument("--method", metavar="TEXT",
                        help="with --review, how the reviewed grades were set (replaces the carried-over account)")
    parser.add_argument("--criteria", metavar="SLUG",
                        help="print the wording a reviewer grades SLUG against, for its platform")
    parser.add_argument("--date", default=dt.date.today().isoformat(), help=argparse.SUPPRESS)
    args = parser.parse_args()
    cat = catalog.load_catalog()
    systems, categories = cat["systems"], cat.get("categories", {})
    if args.criteria:
        system = next((s for s in systems if s["slug"] == args.criteria), None)
        if not system:
            sys.exit(f"{args.criteria}: not in catalog.json")
        print("\n".join(review_sheet(scorecard.load()[0], system)))
        return
    if args.check:
        criteria, audits = scorecard.load()
        problems, warnings = stale(criteria, audits[-1], systems, categories)
        problems += health.problems(criteria, audits[-1], systems)
        for w in warnings:
            print(f"warning: {w}")
        if problems:
            sys.exit("scorecard is stale; run `make grade`:\n  " + "\n  ".join(problems))
        print("scorecard and health current")
        return
    if not args.write:
        for s in systems:
            for cid, g in scripted(s).items():
                print(f"{s['slug']:<16} {cid:<4} {g['grade']:<8} {g['evidence']}")
        return
    criteria, audits = scorecard.load()
    reviews = {}
    for spec in args.review:
        slug, _, path = spec.partition("=")
        reviews[slug] = json.loads(Path(path).read_text())
    out = snapshot(criteria, audits[-1], systems, args.date, categories, reviews, args.method)
    problems = scorecard.check(criteria, audits + [out])
    if problems:
        sys.exit("snapshot problems:\n  " + "\n  ".join(problems))
    path = next_path(args.date)
    path.write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
    missing = sorted({s["slug"] for s in systems} - {s["slug"] for s in out["systems"]})
    print(f"wrote {path.relative_to(ROOT)}" + (f"; not in any review yet: {', '.join(missing)}" if missing else ""))
    for readme in health.write(criteria, out, systems):
        print(f"wrote {readme.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
