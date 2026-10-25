#!/usr/bin/env python3
"""Render style-guide.html from tokens.json.

    python3 tools/build_style_guide.py

Every token becomes a CSS custom property (its path joined with dashes; an alias becomes a var()), so
the swatches, scales and specimens cannot drift from the file. The page starts in the reader's
system theme and has a Light/Dark toggle that sets data-theme on <html>. Specimens are drawn from
tokens only, in the system font and with no Notion artwork or icons. PRODUCT (adapt): NAME, LEDE, GROUP_ORDER, specimens(),
SPEC_CSS and the colour words in PAGE_CSS.
Standard library only, deterministic.
"""
import html
import json
import pathlib
import re

PKG = pathlib.Path(__file__).resolve().parent.parent
TOKENS = json.loads((PKG / "tokens.json").read_text())
OUT = PKG / "style-guide.html"

NAME = "Notion desktop"  # PRODUCT (adapt)
LEDE = ("Notion 7.40.0 for macOS (Electron 44.9.1, Chrome 152), read live from the running app over its remote-debugging port on "
        "2026-10-25, in both of Notion's own themes, Light and Dark, at the owner's 90% zoom. Every value below is a token from tokens.json; "
        "the specimens are rebuilt from those tokens in the system font, not copied from the app.")  # PRODUCT (adapt)
GROUP_ORDER = ["role", "text", "icon", "bg", "border", "blue", "gray", "brown", "orange", "yellow", "green", "teal", "purple", "pink", "red",
               "palette", "misc", "shadow", "component"]


def walk(node, path=()):
    if isinstance(node, dict) and "$value" in node:
        yield path, node
        return
    if isinstance(node, dict):
        for k, v in node.items():
            if not k.startswith("$"):
                yield from walk(v, path + (k,))


def var(path):
    return "--" + "-".join(path)


def css_value(t):
    v = t["$value"]
    if isinstance(v, str) and re.fullmatch(r"\{[^{}]+\}", v):
        return "var(%s)" % var(tuple(v[1:-1].split(".")))
    if t["$type"] == "shadow":
        return ", ".join(("inset " if l["inset"] else "") + f"{l['offsetX']} {l['offsetY']} {l['blur']} {l['spread']} {l['color']}" for l in v) or "none"
    if t["$type"] == "fontFamily":
        return ", ".join(f'"{f}"' if " " in f else f for f in v)
    if t["$type"] == "cubicBezier":
        return "cubic-bezier(%s)" % ", ".join("%g" % x for x in v)
    if t["$type"] == "typography":
        return None
    return str(v)


def esc(s):
    return html.escape(str(s), quote=True)


def resolve(v, *sets):
    seen = 0
    while isinstance(v, str) and re.fullmatch(r"\{[^{}]+\}", v) and seen < 20:
        path = tuple(v[1:-1].split("."))
        v = next(s[path]["$value"] for s in sets if path in s)
        seen += 1
    return v


core, light, dark = (dict(walk(TOKENS[s])) for s in ("core", "light", "dark"))


def block(sel, toks):
    lines = []
    for p, t in toks.items():
        c = css_value(t)
        if c is not None:
            lines.append(f"  {var(p)}: {c};")
    return sel + " {\n" + "\n".join(lines) + "\n}\n"


type_css = []
for p, t in core.items():
    if t["$type"] == "typography":
        v = t["$value"]
        fam = "var(--fontFamily-mono)" if "mono" in v["fontFamily"] else "var(--fontFamily-sans)"
        # A role may alias a scale step ({fontSize.chat-code}); resolve it, since a brace is not CSS.
        r = {k: resolve(v[k], core) for k in ("fontSize", "fontWeight", "lineHeight", "letterSpacing")}
        type_css.append(f".t-{p[-1]} {{ font-family: {fam}; font-size: {r['fontSize']}; font-weight: {r['fontWeight']}; "
                        f"line-height: {r['lineHeight']}; letter-spacing: {r['letterSpacing']}; }}")


def ev(t):
    s = t["$extensions"]["source"]
    return f'<span class="ev ev-{s["evidence"].lower().replace(" ", "-")}" title="{esc(s["from"])}">{esc(s["evidence"])}</span>'


def colour_table(group):
    rows = []
    for p, t in light.items():
        if p[0] != group or t["$type"] != "color":
            continue
        cells = []
        for sets in ((light, core), (dark, core)):
            tok = sets[0][p]
            shown = resolve(tok["$value"], *sets)
            label = tok["$value"] if tok["$value"] == shown else f"{tok['$value']} = {shown}"
            cells.append(f'<td><span class="sw"><i style="background:{esc(shown)}"></i></span><code>{esc(label)}</code> {ev(tok)}</td>')
        rows.append(f"<tr><th><code>{esc('.'.join(p))}</code></th>{''.join(cells)}</tr>")
    if not rows:
        return ""
    open_ = " open" if group in ("role", "seed") else ""
    return (f'<details{open_}><summary>{esc(group)} <small>{len(rows)}</small></summary><table class="tok"><thead><tr><th>Token</th>'
            f'<th>Light</th><th>Dark</th></tr></thead><tbody>{"".join(rows)}</tbody></table></details>')


def scale_rows(group, render):
    rows = []
    for p, t in core.items():
        if p[0] == group:
            rows.append(f"<tr><th><code>{esc('.'.join(p))}</code></th><td>{render(p, t)}</td><td><code>{esc(json.dumps(t['$value']) if not isinstance(t['$value'], str) else t['$value'])}</code> {ev(t)}</td></tr>")
    return f'<table class="tok">{"".join(rows)}</table>'


def specimens():  # PRODUCT (adapt)
    return """
<div class="spec-grid">
 <figure><figcaption>Sidebar: search, tabs, a section, a selected page</figcaption>
  <div class="sp-sidebar">
   <div class="sp-search">Search or ask</div>
   <div class="sp-tabs"><span class="sp-tab sel">Home</span><span class="sp-tab">Chat</span></div>
   <div class="sp-group">Private</div>
   <div class="sp-row sel">Design capture (scratch)</div>
   <div class="sp-row">Another page</div>
   <div class="sp-row muted">+ Add new</div>
  </div>
 </figure>
 <figure><figcaption>A page: title, heading, body, list, to-do, callout, inline code</figcaption>
  <div class="sp-page">
   <div class="t-page-title">Design capture</div>
   <div class="t-heading-2" style="margin-top:12px">Sample heading</div>
   <div class="t-body">A paragraph with <b>bold</b>, a <span class="sp-link">link</span> and <code class="sp-code">code</code>.</div>
   <div class="t-body">&bull;&nbsp; First bullet</div>
   <div class="t-body sp-todo"><span class="sp-check on"></span><s>A finished to-do</s></div>
   <div class="sp-callout t-body">A callout block</div>
  </div>
 </figure>
 <figure><figcaption>Buttons: the blue New, a ghost Share, the confirmation's Delete and Cancel</figcaption>
  <div class="sp-buttons"><span class="sp-btn primary">New</span><span class="sp-btn ghost">Share</span><span class="sp-btn ghost hover">Share (hover)</span>
   <span class="sp-btn danger">Delete</span><span class="sp-btn ghost focus">Focus ring</span></div>
 </figure>
 <figure><figcaption>Menu with a highlighted row</figcaption>
  <div class="sp-menu"><div class="sp-mrow">Copy link <span class="sp-end">&#8984;L</span></div><div class="sp-mrow hi">Duplicate <span class="sp-end">&#8984;D</span></div><div class="sp-mrow">Move to</div><hr><div class="sp-mrow danger">Move to Trash</div></div>
 </figure>
 <figure><figcaption>Confirmation dialog over the scrim</figcaption>
  <div class="sp-scrim"><div class="sp-dialog"><div style="font-weight:600;text-align:center">Delete this property?</div>
   <div class="sp-btn danger block" style="margin-top:14px">Delete</div><div class="sp-btn ghost block">Cancel</div></div></div>
 </figure>
 <figure><figcaption>Database table: header, rows, select pills; tooltip</figcaption>
  <div class="sp-table"><div class="sp-tr head"><span>Name</span><span>Priority</span></div>
   <div class="sp-tr"><span>Measure the table view</span><span><i class="sp-pill">High</i></span></div>
   <div class="sp-tr hover"><span>Open the board view</span><span><i class="sp-pill">High</i></span></div></div>
  <div style="margin-top:14px"><span class="sp-tooltip">Copy link <span style="opacity:.6">&#8984;L</span></span></div>
 </figure>
</div>"""


SPEC_CSS = """
.spec-grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(320px,1fr)); gap:20px; }
figure { margin:0; padding:16px; background:var(--role-page); border:1px solid var(--role-border-default); border-radius:var(--radius-menu); color:var(--role-text-primary); font-family:var(--fontFamily-sans); font-size:14px; }
figcaption { font-size:12px; color:var(--role-text-secondary); margin-bottom:12px; }
.sp-sidebar { background:var(--component-sidebar-bg); border-radius:var(--radius-control); padding:8px; }
.sp-search { height:var(--component-sidebar-search-height); display:flex; align-items:center; padding:0 8px; border-radius:var(--component-sidebar-search-radius); color:var(--component-sidebar-search-text); background:var(--component-sidebar-search-bg-hover); }
.sp-tabs { display:flex; gap:4px; margin:8px 0; } .sp-tab { padding:6px 8px; border-radius:var(--component-nav-tab-radius); color:var(--component-nav-tab-text); font-weight:500; }
.sp-tab.sel { background:var(--component-nav-tab-selected-bg); color:var(--component-nav-tab-selected-text); }
.sp-group { padding:10px 8px 4px; font-size:12px; font-weight:500; color:var(--component-section-label-text); }
.sp-row { display:flex; align-items:center; height:var(--component-page-row-height); padding:0 var(--component-page-row-selected-padding); border-radius:var(--component-page-row-radius); color:var(--component-page-row-text); font-weight:500; }
.sp-row.sel { background:var(--component-page-row-selected-bg); color:var(--component-page-row-selected-text); } .sp-row.muted { color:var(--text-tertiary); }
.sp-page { padding:4px 8px; } .sp-page > div { margin:4px 0; }
.sp-link { text-decoration:underline; text-decoration-color:var(--misc-line-decoration-color); }
.sp-code { font-family:var(--fontFamily-mono); font-size:85%; background:var(--component-inline-code-bg); color:var(--component-inline-code-text); border-radius:var(--component-inline-code-radius); padding:1px 4px; }
.sp-todo { display:flex; align-items:center; gap:8px; color:var(--text-tertiary); }
.sp-check { width:16px; height:16px; border-radius:var(--component-checkbox-radius); border:1px solid var(--icon-secondary); display:inline-block; }
.sp-check.on { background:var(--role-accent-default); border-color:var(--role-accent-default); }
.sp-callout { background:var(--component-callout-bg); border-radius:var(--component-callout-radius); padding:var(--component-callout-padding); }
.sp-buttons { display:flex; flex-wrap:wrap; gap:8px; align-items:center; }
.sp-btn { display:inline-flex; align-items:center; justify-content:center; height:var(--component-button-new-height); padding:0 var(--component-button-new-padding); border-radius:var(--component-button-new-radius); font-weight:500; }
.sp-btn.primary { background:var(--component-button-new-bg); color:var(--component-button-new-text); }
.sp-btn.ghost { color:var(--component-button-share-text); } .sp-btn.ghost.hover { background:var(--component-button-share-bg-hover); }
.sp-btn.danger { color:var(--component-button-danger-text); box-shadow:inset 0 0 0 1px var(--role-border-default); }
.sp-btn.block { display:flex; height:var(--component-button-danger-height); margin-top:6px; }
.sp-btn.focus { box-shadow:var(--shadow-focus-shadow); }
.sp-menu { background:var(--component-menu-bg); color:var(--component-menu-text); border-radius:var(--component-menu-radius); padding:6px 4px; max-width:240px; box-shadow:var(--shadow-outline-md); }
.sp-menu hr { border:0; border-top:1px solid var(--role-border-default); margin:4px 8px; }
.sp-mrow { display:flex; align-items:center; height:var(--component-menu-row-height); padding:0 8px; border-radius:var(--component-menu-row-radius); }
.sp-mrow.hi { background:var(--component-menu-row-bg-hover); } .sp-mrow.danger { color:var(--red-text-secondary); } .sp-end { margin-left:auto; color:var(--text-tertiary); font-size:12px; }
.sp-scrim { background:var(--role-scrim); padding:22px; border-radius:var(--radius-control); }
.sp-dialog { background:var(--component-dialog-bg); border-radius:var(--component-dialog-radius); padding:var(--component-dialog-padding); box-shadow:var(--shadow-outline-lg); max-width:260px; margin:0 auto; }
.sp-table { border-top:1px solid var(--role-border-default); } .sp-tr { display:grid; grid-template-columns:2fr 1fr; border-bottom:1px solid var(--role-border-default); }
.sp-tr span { padding:7px 8px; } .sp-tr.head { color:var(--component-table-header-text); } .sp-tr.hover { background:var(--misc-table-row-hover-bg); }
.sp-pill { font-style:normal; background:var(--component-select-pill-bg); color:var(--component-select-pill-text); border-radius:var(--component-select-pill-radius); padding:1px 6px; }
.sp-tooltip { display:inline-block; background:var(--component-tooltip-bg); color:var(--component-tooltip-text); border-radius:var(--component-tooltip-radius); padding:4px 8px; font-size:12px; }
"""

PAGE_CSS = """
:root { color-scheme: light dark; }
html[data-theme="dark"] { color-scheme: dark; }
body { margin:0; background:var(--role-page); color:var(--role-text-primary); font:14px/1.45 var(--fontFamily-sans); }
main { max-width:1180px; margin:0 auto; padding:24px 16px 64px; }
header { display:flex; gap:16px; align-items:flex-start; justify-content:space-between; flex-wrap:wrap; }
h1 { font-size:22px; margin:0 0 6px; } h2 { font-size:17px; margin:36px 0 12px; } p { color:var(--role-text-secondary); max-width:820px; }
button.toggle { font:inherit; padding:6px 12px; border-radius:99px; border:1px solid var(--role-border-strong); background:var(--role-surface); color:var(--role-text-primary); cursor:pointer; }
details { margin:8px 0; } summary { cursor:pointer; font-weight:600; padding:6px 0; } summary small { color:var(--role-text-secondary); font-weight:400; }
.scroll { overflow-x:auto; }
table.tok { border-collapse:collapse; width:100%; font-size:12px; } table.tok th, table.tok td { text-align:left; padding:4px 8px; border-bottom:1px solid var(--role-border-default); vertical-align:middle; }
.sw { display:inline-block; width:22px; height:16px; border-radius:4px; vertical-align:middle; margin-right:6px; background-image:linear-gradient(45deg,#ccc 25%,transparent 25%,transparent 75%,#ccc 75%),linear-gradient(45deg,#ccc 25%,#fff 25%,#fff 75%,#ccc 75%); background-size:8px 8px; background-position:0 0,4px 4px; overflow:hidden; }
.sw i { display:block; width:100%; height:100%; }
code { font-family:ui-monospace, Menlo, monospace; font-size:11px; }
.ev { font-size:10px; padding:1px 5px; border-radius:99px; background:var(--role-surface); color:var(--role-text-secondary); white-space:nowrap; }
.ev-derived { background:var(--role-accent-subtle); }
.bar { display:inline-block; height:10px; background:var(--role-accent-default); border-radius:2px; vertical-align:middle; }
.rad { display:inline-block; width:40px; height:24px; border:1px solid var(--role-border-strong); background:var(--role-surface); vertical-align:middle; }
.shadow-box { display:inline-block; width:80px; height:36px; background:var(--role-raised); border-radius:8px; vertical-align:middle; }
"""

sections = []
sections.append("<h2>Colour roles and theme</h2><p>role.* maps the checklist roles onto Notion's tokens. text, icon, border and bg are the neutral roles; "
                "the ten hue families (blue to red) each have the same text, icon, border and background steps; misc holds Notion's named colours. "
                "Every token keeps the custom property it came from.</p>")
groups = []
for p, _ in light.items():
    if p[0] not in groups:
        groups.append(p[0])
groups.sort(key=lambda g: (GROUP_ORDER.index(g) if g in GROUP_ORDER else 99, g))
sections.append('<div class="scroll">' + "".join(colour_table(g) for g in groups) + "</div>")
palette_rows = "".join(  # (Notion has no theme-independent hue palette in core)
    f'<tr><th><code>{esc(".".join(p))}</code></th><td><span class="sw"><i style="background:{esc(t["$value"])}"></i></span><code>{esc(t["$value"])}</code> {ev(t)}</td></tr>'
                       for p, t in core.items() if p[0] == "color")
sections.append(f'<details><summary>color (hue palettes, core) <small>{sum(1 for p in core if p[0] == "color")}</small></summary><table class="tok">{palette_rows}</table></details>')
sections.append("<h2>Type</h2>" + "".join(
    f'<div style="margin:8px 0"><div class="t-{p[-1]}">{esc(p[-1].capitalize())}: A page of notes, docs and databases</div>'
    f'<code>{esc(json.dumps(t["$value"]))}</code> {ev(t)}</div>' for p, t in core.items() if t["$type"] == "typography"))
sections.append("<h2>Radius</h2>" + scale_rows("radius", lambda p, t: f'<span class="rad" style="border-radius:{t["$value"]}"></span>'))
sections.append("<h2>Spacing</h2>" + scale_rows("spacing", lambda p, t: f'<span class="bar" style="width:{t["$value"]}"></span>'))
sections.append("<h2>Type scale</h2>" + scale_rows("fontSize", lambda p, t: f'<span style="font-size:{t["$value"]}">Aa</span>') + scale_rows("lineHeight", lambda p, t: "")
                + scale_rows("fontWeight", lambda p, t: "") + scale_rows("letterSpacing", lambda p, t: ""))
sections.append("<h2>Control heights, sizes and layout</h2>" + scale_rows("controlHeight", lambda p, t: f'<span class="bar" style="width:{t["$value"]}"></span>')
                + scale_rows("size", lambda p, t: "") + scale_rows("layout", lambda p, t: "") + scale_rows("focusRing", lambda p, t: "")
                + scale_rows("zIndex", lambda p, t: "") + scale_rows("borderWidth", lambda p, t: "") + scale_rows("container", lambda p, t: ""))
shadow_rows = "".join(f"<tr><th><code>{esc('.'.join(p))}</code></th><td><span class=\"shadow-box\" style=\"box-shadow:var({var(p)})\"></span></td><td>{ev(t)}</td></tr>"
                      for p, t in list(core.items()) + list(light.items()) if p[0] == "shadow" and t["$type"] == "shadow")
sections.append(f'<h2>Elevation</h2><table class="tok">{shadow_rows}</table>')
sections.append("<h2>Motion and blur</h2>" + scale_rows("duration", lambda p, t: "") + scale_rows("easing", lambda p, t: "") + scale_rows("blur", lambda p, t: ""))
sections.append("<h2>Components</h2><p>Rebuilt from component.* and the semantic tokens. The crops in components/crops/ show the real ones.</p>" + specimens())

page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(NAME)} style guide</title>
<style>
{block(':root', core)}
{block(':root, html[data-theme="light"]', light)}
{block('html[data-theme="dark"]', dark)}
@media (prefers-color-scheme: dark) {{
{block('html:not([data-theme="light"])', dark)}
}}
{chr(10).join(type_css)}
{PAGE_CSS}
{SPEC_CSS}
</style>
</head>
<body>
<main>
<header><div><h1>{esc(NAME)}</h1><p>{esc(LEDE)}</p></div>
<button class="toggle" type="button" onclick="var h=document.documentElement;var d=h.getAttribute('data-theme')==='dark'||(!h.getAttribute('data-theme')&&matchMedia('(prefers-color-scheme: dark)').matches);h.setAttribute('data-theme',d?'light':'dark')">Light / Dark</button></header>
{''.join(sections)}
</main>
</body>
</html>
"""
OUT.write_text(page)
print("style-guide.html", len(page) // 1024, "KB")
