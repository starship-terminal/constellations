#!/usr/bin/env python3
"""Generate the scorecard pages and the docs site's zensical.toml.

    python3 tools/scorecard.py            write docs/scorecard/ and zensical.toml
    python3 tools/scorecard.py --check    fail if the audit data is malformed

The rubric is scorecard/criteria.json and each audit is one dated snapshot,
scorecard/audits/<YYYY-MM-DD>.json. The newest snapshot drives every page; older ones
feed the changelog. docs/scorecard/ and zensical.toml are generated and gitignored, so
edit the data, never the pages. The rest of docs/ (the library docs, the home page and
the gallery) is written by hand. Standard library only.
"""
from __future__ import annotations

import argparse
import html
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "scorecard"
DOCS = ROOT / "docs"
OUT = DOCS / "scorecard"
GRADES = {
    "meets": ("●", "Meets"),
    "partly": ("◐", "Partly"),
    "missing": ("○", "Missing"),
    "na": ("–", "Not applicable"),
}
FRONT = "---\nsearch:\n  exclude: true\n{extra}---\n\n"
SITE_URL = "https://c-wenlong.github.io/design-systems/"
LIBRARY_DOCS = [
    ("What a design system contains", "DESIGN-SYSTEM.md"),
    ("Capturing a product", "CAPTURE.md"),
    ("Package layout", "PACKAGE.md"),
    ("Evidence labels", "EVIDENCE.md"),
    ("Rights and privacy", "RIGHTS.md"),
    ("Open items", "TODO.md"),
]


def esc(text: str) -> str:
    return html.escape(str(text), quote=True)


def load() -> tuple[dict, list[dict]]:
    criteria = json.loads((DATA / "criteria.json").read_text())
    audits = [json.loads(p.read_text()) for p in sorted((DATA / "audits").glob("*.json"))]
    if not audits:
        sys.exit("no audit snapshots in scorecard/audits/")
    return criteria, audits


def check(criteria: dict, audits: list[dict]) -> list[str]:
    ids = [c["id"] for c in criteria["criteria"]]
    problems = []
    for audit in audits:
        slugs = [s["slug"] for s in audit["systems"]]
        for slug in sorted({x for x in slugs if slugs.count(x) > 1}):
            problems.append(f"{audit['date']}: slug {slug!r} appears {slugs.count(slug)} times; each page needs its own")
        for s in audit["systems"]:
            missing = [i for i in ids if i not in s["grades"]]
            if missing:
                problems.append(f"{audit['date']} {s['slug']}: missing {', '.join(missing)}")
            unknown = [i for i in s["grades"] if i not in ids]
            if unknown:
                problems.append(f"{audit['date']} {s['slug']}: grades for criteria not in the rubric: {', '.join(unknown)}")
            for cid, g in s["grades"].items():
                if g["grade"] not in GRADES:
                    problems.append(f"{audit['date']} {s['slug']} {cid}: unknown grade {g['grade']!r}")
    return problems


def short(system: dict) -> str:
    return system.get("short") or system["name"]


def counts(system: dict) -> dict:
    out = {k: 0 for k in GRADES}
    for g in system["grades"].values():
        out[g["grade"]] += 1
    return out


def ranked(systems: list[dict]) -> list[dict]:
    return sorted(systems, key=lambda s: (-counts(s)["meets"], -counts(s)["partly"], s["name"]))


def badge(grade: str) -> str:
    glyph, word = GRADES[grade]
    return f'<span class="sc-badge g-{grade}"><span aria-hidden="true">{glyph}</span> {word}</span>'


def heatmap(criteria: dict, systems: list[dict], audit: dict) -> str:
    """An accessible table: caption, row and column headers, a glyph plus hidden text in
    every cell, and each cell linking to that grade's evidence."""
    crit = criteria["criteria"]
    layers: list[tuple[str, int]] = []
    for c in crit:
        if layers and layers[-1][0] == c["layer"]:
            layers[-1] = (c["layer"], layers[-1][1] + 1)
        else:
            layers.append((c["layer"], 1))
    out = ['<div class="sc-scroll" role="region" aria-labelledby="sc-caption" tabindex="0">',
           '<table class="sc-heat">',
           f'<caption id="sc-caption">{len(systems)} design systems graded against {len(crit)} criteria, '
           f'audit of {esc(audit["date"])}. Each cell links to its evidence.</caption>',
           '<thead><tr class="sc-layers"><td></td>']
    # Narrow groups (patterns, voice, assets) get no label: it would widen their
    # columns. The legend under the table names every layer letter.
    out += [f'<th scope="colgroup" colspan="{n}">{esc(name)}</th>' if n >= 3
            else f'<td colspan="{n}" class="sc-layer-gap"></td>' for name, n in layers]
    out += ['<td colspan="3"></td></tr><tr><th scope="col" class="sc-corner">System</th>']
    out += [f'<th scope="col"><a href="criteria/#{c["id"].lower()}" title="{esc(c["title"])}">{c["id"]}</a></th>'
            for c in crit]
    out += ['<th scope="col" class="sc-total">Meets</th><th scope="col" class="sc-total">Partly</th>'
            '<th scope="col" class="sc-total">Missing</th></tr></thead><tbody>']
    for s in systems:
        n = counts(s)
        out.append(f'<tr><th scope="row"><a href="systems/{s["slug"]}/">{esc(short(s))}</a></th>')
        for c in crit:
            g = s["grades"][c["id"]]["grade"]
            glyph, word = GRADES[g]
            out.append(f'<td class="g-{g}"><a href="systems/{s["slug"]}/#{c["id"].lower()}">'
                       f'<span aria-hidden="true">{glyph}</span>'
                       f'<span class="sc-sr">{c["id"]} {esc(c["title"])}: {word}</span></a></td>')
        out.append(f'<td class="sc-total">{n["meets"]}</td><td class="sc-total">{n["partly"]}</td>'
                   f'<td class="sc-total">{n["missing"]}</td></tr>')
    out += ['</tbody></table></div>']
    return "\n".join(out)


def legend() -> str:
    return ('<p class="sc-legend">' + " ".join(badge(g) for g in GRADES) +
            ' <span class="sc-key">F foundations · C components · P patterns · '
            'V principles and voice · A assets · K package</span></p>')


def index_page(criteria: dict, audit: dict) -> str:
    systems = ranked(audit["systems"])
    total = len(systems) * len(criteria["criteria"])
    meets = sum(counts(s)["meets"] for s in systems)
    best = systems[0]
    by_crit = {c["id"]: sum(s["grades"][c["id"]]["grade"] == "meets" for s in systems) for c in criteria["criteria"]}
    floor = min(by_crit.values())
    weakest = [c for c in criteria["criteria"] if by_crit[c["id"]] == floor]
    md = FRONT.format(extra="hide:\n  - navigation\n  - toc\n")
    md += "# Scorecard\n\n"
    md += (f"Every captured design system in the library, graded against the checklist a complete "
           f"design system has to meet ([What a design system contains](../DESIGN-SYSTEM.md)). "
           f"Last audit: **{audit['date']}**.\n\n")
    md += '<div class="grid cards" markdown>\n\n'
    md += f"-   **{len(systems)} systems**\n\n    ---\n\n    Captured from real products, from Linear to Duolingo.\n\n"
    md += (f"-   **{meets} of {total} cells meet**\n\n    ---\n\n    {round(100 * meets / total)}% of grades fully "
           f"meet their criterion.\n\n")
    md += (f"-   **Leader: {short(best)}**\n\n    ---\n\n    {counts(best)['meets']} of {len(criteria['criteria'])} "
           f"criteria met. [See its page](systems/{best['slug']}.md).\n\n")
    label = "Met by no system" if floor == 0 else f"Met by only {floor}"
    md += (f"-   **{label}**\n\n    ---\n\n    " +
           ", ".join(f"[{c['id']} {c['title']}](criteria.md#{c['id'].lower()})" for c in weakest) + ".\n\n")
    md += "</div>\n\n## Scorecard\n\n"
    md += heatmap(criteria, systems, audit) + "\n\n" + legend() + "\n\n"
    md += ('!!! info "Reading the grades"\n\n'
           "    These are captures of other companies' products, so the top layers (principles, voice, "
           "per-component behaviour) are usually missing: a capture records how a product looks, not "
           "why. [How each criterion is judged](criteria.md).\n")
    return md


def system_page(criteria: dict, audit: dict, system: dict, rank: int) -> str:
    n = counts(system)
    md = FRONT.format(extra="")
    md += f"# {system['name']}\n\n"
    md += f"{esc(system['goodFor'])}.\n\n"
    md += (f"**Rank {rank} of {len(audit['systems'])}** · {badge('meets')} {n['meets']} · "
           f"{badge('partly')} {n['partly']} · {badge('missing')} {n['missing']}"
           + (f" · {badge('na')} {n['na']}" if n["na"] else "") + "\n\n")
    md += (f"{esc(system['category'])} · captured {system['captured']} · themes: {', '.join(system['themes'])} · "
           f"<{system['url']}>\n\n")
    md += ('<div class="sc-bar" role="img" aria-label="'
           f'{n["meets"]} meets, {n["partly"]} partly, {n["missing"]} missing, {n["na"]} not applicable">'
           + "".join(f'<span class="g-{g}" style="flex:{n[g]}"></span>' for g in GRADES if n[g]) +
           "</div>\n\n")
    # One visible section per layer, not tabs: the heatmap links straight to a row's
    # anchor, and an anchor inside a hidden tab cannot be scrolled to.
    for layer in criteria["layers"].values():
        rows = [c for c in criteria["criteria"] if c["layer"] == layer]
        md += f"## {layer}\n\n"
        md += "| | Criterion | Grade | Evidence |\n|---|---|---|---|\n"
        for c in rows:
            g = system["grades"][c["id"]]
            evidence = esc(g["evidence"]).replace("|", "\\|")
            md += (f'| <span id="{c["id"].lower()}"></span>[{c["id"]}](../criteria.md#{c["id"].lower()}) '
                   f'| {esc(c["title"])} | {badge(g["grade"])} | {evidence} |\n')
        md += "\n"
    return md


def criteria_page(criteria: dict, audit: dict) -> str:
    md = FRONT.format(extra="")
    md += "# Criteria and method\n\n"
    md += ("The checklist comes from the library's own definition of a complete design system: five "
           "layers (foundations, components, patterns, principles and voice, assets), each with a "
           "done-when rule, plus three checks on the package itself.\n\n")
    md += "## Grades\n\n| Grade | Means |\n|---|---|\n"
    md += f"| {badge('meets')} | The done-when rule is fully met |\n"
    md += f"| {badge('partly')} | Some of it is there; the evidence says what is missing |\n"
    md += f"| {badge('missing')} | Absent |\n"
    md += f"| {badge('na')} | The product has no such thing, for example a dark theme on a light-only product |\n\n"
    md += f"## How the audit was run\n\n{esc(audit['method'])}\n\n"
    for layer in criteria["layers"].values():
        md += f"## {layer}\n\n| | Criterion | Done when |\n|---|---|---|\n"
        for c in criteria["criteria"]:
            if c["layer"] == layer:
                md += f'| <span id="{c["id"].lower()}"></span>**{c["id"]}** | {esc(c["title"])} | {esc(c["doneWhen"])} |\n'
        md += "\n"
    return md


def changelog_page(criteria: dict, audits: list[dict]) -> str:
    md = FRONT.format(extra="") + "# Changelog\n\nNewest first. Each entry compares one audit with the one before it.\n\n"
    titles = {c["id"]: c["title"] for c in criteria["criteria"]}
    for i in range(len(audits) - 1, -1, -1):
        audit = audits[i]
        md += f"## {audit['date']}\n\n"
        if i == 0:
            md += f"First audit: {len(audit['systems'])} systems against {len(criteria['criteria'])} criteria.\n\n"
            continue
        before = {s["slug"]: s for s in audits[i - 1]["systems"]}
        lines = []
        for s in ranked(audit["systems"]):
            old = before.get(s["slug"])
            if not old:
                lines.append(f"- **{s['name']}** added: {counts(s)['meets']} criteria met.")
                continue
            changed = [f"{cid} {titles.get(cid, cid)} {GRADES[old['grades'][cid]['grade']][1].lower()} → "
                       f"{GRADES[g['grade']][1].lower()}"
                       for cid, g in s["grades"].items()
                       if cid in old["grades"] and old["grades"][cid]["grade"] != g["grade"]]
            if changed:
                lines.append(f"- **{s['name']}**: " + "; ".join(changed) + ".")
        for slug in before.keys() - {s["slug"] for s in audit["systems"]}:
            lines.append(f"- **{before[slug]['name']}** removed.")
        md += ("\n".join(lines) if lines else "No grade changed.") + "\n\n"
    return md


def config(audit: dict) -> str:
    systems = ranked(audit["systems"])
    nav_systems = ", ".join(f'{{ "{short(s)}" = "scorecard/systems/{s["slug"]}.md" }}' for s in systems)
    nav_docs = ", ".join(f'{{ "{title}" = "{path}" }}' for title, path in LIBRARY_DOCS)
    return f'''# Generated by tools/scorecard.py. Edit the template there, not this file.
[project]
site_name = "Design systems"
site_url = "{SITE_URL}"
site_description = "The design-systems library: captured styles, the scorecard, and how the library works"
copyright = "Private study notes. Products and trademarks belong to their owners."
extra_css = ["stylesheets/scorecard.css"]
nav = [
  {{ "Home" = "index.md" }},
  {{ "Gallery" = "gallery/index.html" }},
  {{ "Scorecard" = [
    {{ "Overview" = "scorecard/index.md" }},
    {{ "Systems" = [{nav_systems}] }},
    {{ "Criteria and method" = "scorecard/criteria.md" }},
    {{ "Changelog" = "scorecard/changelog.md" }},
  ] }},
  {{ "Docs" = [{nav_docs}] }},
]

# Search is off: its index would hold every page's text in plain JSON next to the
# encrypted pages on GitHub Pages.
[project.plugins.search]
enabled = false

[project.theme]
language = "en"
# No navigation.instant: StatiCrypt encrypts every published page, and instant
# loading would fetch the encrypted HTML behind the decrypt step.
features = [
  "navigation.tabs",
  "content.tabs.link",
  "content.tooltips",
  "navigation.footer",
  "navigation.sections",
  "navigation.top",
  "navigation.tracking",
  "toc.follow",
]

[[project.theme.palette]]
media = "(prefers-color-scheme)"
toggle.icon = "lucide/sun-moon"
toggle.name = "Switch to light mode"

[[project.theme.palette]]
media = "(prefers-color-scheme: light)"
scheme = "default"
primary = "white"
accent = "indigo"
toggle.icon = "lucide/sun"
toggle.name = "Switch to dark mode"

[[project.theme.palette]]
media = "(prefers-color-scheme: dark)"
scheme = "slate"
primary = "black"
accent = "indigo"
toggle.icon = "lucide/moon"
toggle.name = "Switch to system preference"

[project.markdown_extensions]
abbr = {{}}
admonition = {{}}
attr_list = {{}}
def_list = {{}}
footnotes = {{}}
md_in_html = {{}}
tables = {{}}
toc.permalink = true
pymdownx.betterem = {{}}
pymdownx.details = {{}}
pymdownx.emoji.emoji_generator = "zensical.extensions.emoji.to_svg"
pymdownx.emoji.emoji_index = "zensical.extensions.emoji.twemoji"
pymdownx.superfences = {{}}
pymdownx.tabbed.alternate_style = true
pymdownx.tabbed.combine_header_slug = true
'''


def build() -> None:
    criteria, audits = load()
    problems = check(criteria, audits)
    if problems:
        sys.exit("data problems:\n  " + "\n  ".join(problems))
    audit = audits[-1]
    systems_dir = OUT / "systems"
    systems_dir.mkdir(parents=True, exist_ok=True)
    for old in systems_dir.glob("*.md"):
        old.unlink()
    (OUT / "index.md").write_text(index_page(criteria, audit))
    (OUT / "criteria.md").write_text(criteria_page(criteria, audit))
    (OUT / "changelog.md").write_text(changelog_page(criteria, audits))
    for rank, s in enumerate(ranked(audit["systems"]), 1):
        (systems_dir / f"{s['slug']}.md").write_text(system_page(criteria, audit, s, rank))
    (ROOT / "zensical.toml").write_text(config(audit))
    print(f"wrote {len(audit['systems'])} system pages from the {audit['date']} audit")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--check", action="store_true", help="validate data only")
    args = parser.parse_args()
    if args.check:
        problems = check(*load())
        print("data ok" if not problems else "\n".join(problems))
        sys.exit(1 if problems else 0)
    build()


if __name__ == "__main__":
    main()
