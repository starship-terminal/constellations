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

NAME = "Notion Calendar desktop"  # PRODUCT (adapt)
LEDE = ("Notion Calendar 1.142.0 for macOS (formerly Cron; an Electron 44 shell around the calendar.notion.so web app), read live from the "
        "running app over its remote-debugging port on 2026-10-25, in Light mode and the owner's Dark mode. Every value below is a token from "
        "tokens.json; the specimens are rebuilt from those tokens in the system font, not copied from the app.")  # PRODUCT (adapt)
GROUP_ORDER = ["role", "surface", "text", "icon", "fill", "tint", "state", "stroke", "material", "glass", "object", "appText", "layout",
               "calendar", "app", "public", "palette", "shadow", "component"]


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
        # The specimens use the stack that rendered (sans-default), not the owner's uninstalled Garamond in front of it.
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
 <figure><figcaption>Sidebar: mini calendar, scheduling, calendar list</figcaption>
  <div class="sp-sidebar">
   <div class="sp-mini"><span class="wd">Mo</span><span class="wd">Tu</span><span class="wd">We</span><span class="wd">Th</span><span class="wd">Fr</span><span class="wd">Sa</span><span class="wd">Su</span>
    <span>19</span><span>20</span><span>21</span><span>22</span><span>23</span><span>24</span><span class="today">25</span></div>
   <div class="sp-row sel">Scheduling</div>
   <div class="sp-field-in">Meet with…</div>
   <div class="sp-acct">work account</div>
   <div class="sp-row"><span class="sp-dot" style="background:var(--palette-blue-600)"></span>Work</div>
   <div class="sp-row hover"><span class="sp-dot" style="background:var(--palette-purple-600)"></span>Personal</div>
  </div>
 </figure>
 <figure><figcaption>Week grid: header, day headers, event chips, now line</figcaption>
  <div class="sp-head"><span class="sp-title">October 2026</span><span class="sp-week">Week 43</span><span style="flex:1"></span><span class="sp-btn secondary">Week ⌄</span><span class="sp-btn secondary">Today</span></div>
  <div class="sp-days"><span>Mon 19</span><span>Tue 20</span><span class="today">Sun <b>25</b></span></div>
  <div class="sp-grid">
   <div class="sp-chip" style="--c:var(--palette-blue-600);top:6px;height:54px">Tech Sync<small>10:00 – 11:00</small></div>
   <div class="sp-chip" style="--c:var(--palette-green-600);top:70px;height:40px;left:36%">Lecture<small>14:00 – 16:00</small></div>
   <div class="sp-now"><span>11:07</span></div>
  </div>
 </figure>
 <figure><figcaption>Buttons: primary, secondary, danger, icon; focus ring</figcaption>
  <div class="sp-buttons">
   <span class="sp-btn primary">Create recurring link</span><span class="sp-btn secondary">Today</span>
   <span class="sp-btn danger">Delete account</span><span class="sp-btn icon">‹</span><span class="sp-btn secondary focus">Focus ring</span>
  </div>
 </figure>
 <figure><figcaption>Menu (dark in both themes) and tooltip</figcaption>
  <div class="sp-menu"><div class="sp-mrow">Day <span class="sp-end">1 or D</span></div><div class="sp-mrow hi">✓ Week <span class="sp-end">0 or W</span></div><div class="sp-mrow">Month <span class="sp-end">M</span></div><hr><div class="sp-mrow danger">Delete <span class="sp-end">delete</span></div></div>
  <span class="sp-tooltip">Go to today <span class="sp-kbd">T</span></span>
 </figure>
 <figure><figcaption>Event popover (floating context panel)</figcaption>
  <div class="sp-panel"><div class="sp-phead">Event</div><div class="sp-ptitle">Tech Sync</div>
   <div class="sp-prow">10:00 → 11:00 <span style="color:var(--role-text-secondary)">1h</span></div>
   <div class="sp-prow" style="color:var(--role-text-secondary)">Every week on Tue</div>
   <div class="sp-seg"><span class="on">Yes</span><span>No</span><span>Maybe</span></div></div>
 </figure>
 <figure><figcaption>Command menu</figcaption>
  <div class="sp-cmd"><div class="sp-cinput">Type a command…</div><div class="sp-chead">Calendar</div>
   <div class="sp-crow sel">Create event… <span class="sp-kbd">C</span></div><div class="sp-crow">Go to today <span class="sp-kbd">T</span></div></div>
 </figure>
 <figure><figcaption>Settings: switches, select, text field</figcaption>
  <div class="sp-dialog">
   <div class="sp-h">Calendar view</div>
   <div class="sp-field"><span class="sp-switch on"></span>Weekends</div>
   <div class="sp-field"><span class="sp-switch"></span>Week numbers</div>
   <div class="sp-select">Monday ⌄</div>
   <div class="sp-input">username</div>
  </div>
 </figure>
</div>"""


SPEC_CSS = """
.spec-grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(320px,1fr)); gap:20px; }
figure { margin:0; padding:16px; background:var(--role-page); border:1px solid var(--role-border-default); border-radius:var(--radius-xl); color:var(--role-text-primary); font-family:var(--fontFamily-sans); font-size:13px; }
figcaption { font-size:12px; color:var(--role-text-secondary); margin-bottom:12px; }
.sp-sidebar { background:var(--component-sidebar-bg); border-radius:var(--radius-l); padding:8px; box-shadow:var(--shadow-2xs); }
.sp-mini { display:grid; grid-template-columns:repeat(7,1fr); gap:2px; text-align:center; font-size:12px; margin-bottom:10px; }
.sp-mini .wd { font-size:10px; font-weight:500; color:var(--component-mini-weekday-text); }
.sp-mini .today { background:var(--component-now-badge-bg); color:#fff; border-radius:var(--radius-m); }
.sp-row { display:flex; align-items:center; gap:8px; height:var(--component-calendar-row-height); padding:0 8px; border-radius:var(--component-calendar-row-radius); color:var(--component-calendar-row-text); }
.sp-row.sel { background:var(--component-scheduling-row-selected-bg); } .sp-row.hover { background:var(--state-hover); }
.sp-dot { width:12px; height:12px; border-radius:3px; }
.sp-acct { padding:12px 8px 4px; color:var(--component-account-header-text); }
.sp-field-in { height:30px; display:flex; align-items:center; padding:0 10px; border-radius:var(--radius-control); background:var(--fill-grayTertiary); color:var(--role-text-secondary); margin:6px 0; }
.sp-head { display:flex; align-items:center; gap:6px; }
.sp-title { font-size:22px; font-weight:700; letter-spacing:-0.01em; } .sp-week { color:var(--component-week-label-text); font-size:12px; }
.sp-days { display:grid; grid-template-columns:repeat(3,1fr); margin:10px 0 4px; color:var(--component-day-header-text); }
.sp-days .today { color:var(--component-day-header-today-text); font-weight:500; } .sp-days .today b { background:var(--component-now-badge-bg); color:#fff; border-radius:var(--radius-m); padding:0 3px; font-weight:500; }
.sp-grid { position:relative; height:130px; background:var(--role-page); border-top:1px solid var(--layout-line-grid-h); }
.sp-chip { position:absolute; left:2%; width:30%; padding:2px 4px 2px 8px; border-radius:var(--component-event-chip-radius); font-size:var(--fontSize-chip-title); line-height:var(--lineHeight-chip-title); font-weight:500;
  color:color-mix(in srgb, var(--c) 70%, var(--role-text-primary)); background:color-mix(in srgb, var(--c) 22%, var(--role-page)); box-shadow:inset 3px 0 0 var(--c); }
.sp-chip small { display:block; font-size:var(--fontSize-chip-time); line-height:var(--lineHeight-chip-time); font-weight:400; opacity:.8; }
.sp-now { position:absolute; left:0; right:0; top:62px; border-top:1px solid var(--component-now-badge-bg); }
.sp-now span { position:absolute; left:-4px; top:-9px; background:var(--component-now-badge-bg); color:#fff; font-size:10px; font-weight:600; border-radius:var(--component-now-badge-radius); padding:1px 4px; }
.sp-buttons { display:flex; flex-wrap:wrap; gap:8px; align-items:center; }
.sp-btn { display:inline-flex; align-items:center; height:var(--size-button); padding:0 var(--spacing-button-x); border-radius:var(--radius-control); font-size:var(--fontSize-button); font-weight:var(--fontWeight-button); }
.sp-btn.primary { background:var(--component-button-primary-bg); color:var(--component-button-primary-text); box-shadow:var(--shadow-input-highlight-border); }
.sp-btn.secondary { color:var(--component-button-secondary-text); box-shadow:var(--shadow-input-border); }
.sp-btn.danger { color:var(--component-button-danger-text); box-shadow:var(--shadow-input-border); }
.sp-btn.icon { width:var(--size-icon-button); justify-content:center; padding:0; color:var(--component-icon-button-text); }
.sp-btn.focus { box-shadow:var(--shadow-highlight-focus); }
.sp-menu { background:var(--component-menu-bg); color:var(--component-menu-text); border-radius:var(--component-menu-radius); padding:4px; max-width:220px; box-shadow:var(--shadow-elevation-middle); }
.sp-menu hr { border:0; border-top:1px solid var(--stroke-contr-secondary); margin:4px 6px; }
.sp-mrow { display:flex; align-items:center; height:var(--component-menu-row-height); padding:0 var(--component-menu-row-padding); border-radius:var(--component-menu-row-radius); color:var(--text-contr-primary); }
.sp-mrow.hi { background:var(--state-contr-hover); } .sp-mrow.danger { color:var(--component-menu-row-danger-text); } .sp-end { margin-left:auto; color:var(--text-contr-secondary); font-size:12px; }
.sp-tooltip { display:inline-flex; gap:6px; align-items:center; margin-top:12px; background:var(--component-tooltip-bg); color:var(--component-tooltip-text); border-radius:var(--component-tooltip-radius); padding:5px 8px; font-size:12px; font-weight:500; box-shadow:var(--shadow-elevation-low); }
.sp-kbd { display:inline-grid; place-items:center; min-width:16px; height:16px; border-radius:var(--radius-kbd); background:var(--app-kbs-bg); color:var(--app-kbs); font:500 11px var(--fontFamily-compact); }
.sp-tooltip .sp-kbd { background:var(--app-contr-kbs-bg); color:var(--app-contr-kbs); }
.sp-panel { background:var(--component-panel-bg); border:1px solid var(--component-panel-border); border-radius:var(--component-panel-radius); box-shadow:var(--shadow-elevation-high); padding:8px 0 12px; max-width:284px; }
.sp-phead { padding:4px 16px 8px; font-weight:500; } .sp-ptitle { margin:0 8px 8px; padding:6px 8px; border-radius:var(--radius-control); font-size:15px; }
.sp-prow { padding:6px 16px; }
.sp-seg { display:flex; margin:8px 16px 0; background:var(--fill-grayTertiary); border-radius:var(--radius-control); padding:2px; }
.sp-seg span { flex:1; text-align:center; padding:3px 0; border-radius:5px; } .sp-seg .on { background:var(--role-raised); box-shadow:var(--shadow-xs); }
.sp-cmd { background:var(--component-command-menu-bg); border-radius:var(--component-command-menu-radius); box-shadow:var(--shadow-elevation-high); padding:6px; }
.sp-cinput { padding:10px; font-size:17px; color:var(--role-text-disabled); border-bottom:1px solid var(--role-border-default); margin-bottom:6px; }
.sp-chead { padding:6px 10px; font-size:12px; font-weight:500; color:var(--component-command-heading-text); }
.sp-crow { display:flex; align-items:center; height:var(--component-command-row-selected-height); padding:0 10px; border-radius:var(--radius-control); font-size:14px; font-weight:500; }
.sp-crow.sel { background:var(--component-command-row-selected-bg); } .sp-crow .sp-kbd { margin-left:auto; }
.sp-dialog { background:var(--component-dialog-bg); border:1px solid var(--component-dialog-border); border-radius:var(--component-dialog-radius); padding:16px; box-shadow:var(--shadow-elevation-high); }
.sp-h { font-size:17px; font-weight:600; margin-bottom:8px; }
.sp-field { display:flex; align-items:center; gap:8px; height:30px; }
.sp-switch { flex:none; display:inline-block; width:var(--component-switch-on-width); height:var(--component-switch-on-height); border-radius:var(--component-switch-on-radius); background:var(--fill-grayPrimary); position:relative; }
.sp-switch::after { content:""; position:absolute; top:1px; left:1px; width:12px; height:12px; border-radius:99px; background:#fff; }
.sp-switch.on { background:var(--component-switch-on-bg); } .sp-switch.on::after { left:11px; }
.sp-select, .sp-input { margin-top:8px; width:190px; height:var(--component-select-height); display:flex; align-items:center; padding:0 var(--component-select-padding); border-radius:var(--component-select-radius); box-shadow:var(--shadow-input-border); color:var(--component-select-text); }
.sp-input { color:var(--role-text-primary); }
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
sections.append("<h2>Colour roles and theme</h2><p>role.* maps the checklist roles onto Notion's design-system tokens (--nds-*): text, "
                "icon, surface, fill, tint, state and stroke, each with a -contr- twin that keeps the dark value in both themes for the always-dark "
                "menus and tooltips, and twelve hue ramps (palette.*). The fixed grey scale, the same in both themes, follows.</p>")
groups = []
for p, _ in light.items():
    if p[0] not in groups:
        groups.append(p[0])
groups.sort(key=lambda g: (GROUP_ORDER.index(g) if g in GROUP_ORDER else 99, g))
sections.append('<div class="scroll">' + "".join(colour_table(g) for g in groups) + "</div>")
palette_rows = "".join(f'<tr><th><code>{esc(".".join(p))}</code></th><td><span class="sw"><i style="background:{esc(t["$value"])}"></i></span><code>{esc(t["$value"])}</code> {ev(t)}</td></tr>'
                       for p, t in core.items() if p[0] == "color")
sections.append(f'<details><summary>color (fixed greys, white and black, core) <small>{sum(1 for p in core if p[0] == "color")}</small></summary><table class="tok">{palette_rows}</table></details>')
sections.append("<h2>Type</h2>" + "".join(
    f'<div style="margin:8px 0"><div class="t-{p[-1]}">{esc(p[-1].capitalize())}: Tech Sync, Tuesday 10:00 to 11:00</div>'
    f'<code>{esc(json.dumps(t["$value"]))}</code> {ev(t)}</div>' for p, t in core.items() if t["$type"] == "typography"))
sections.append("<h2>Radius</h2>" + scale_rows("radius", lambda p, t: f'<span class="rad" style="border-radius:{t["$value"]}"></span>'))
sections.append("<h2>Spacing</h2>" + scale_rows("spacing", lambda p, t: f'<span class="bar" style="width:{t["$value"]}"></span>'))
sections.append("<h2>Type scale</h2>" + scale_rows("fontSize", lambda p, t: f'<span style="font-size:{t["$value"]}">Aa</span>') + scale_rows("lineHeight", lambda p, t: "")
                + scale_rows("fontWeight", lambda p, t: "") + scale_rows("letterSpacing", lambda p, t: ""))
sections.append("<h2>Control heights, sizes and layout</h2>" + scale_rows("size", lambda p, t: "") + scale_rows("layout", lambda p, t: "") + scale_rows("focusRing", lambda p, t: "")
                + scale_rows("zIndex", lambda p, t: "") + scale_rows("borderWidth", lambda p, t: "") + scale_rows("opacity", lambda p, t: "") + scale_rows("scale", lambda p, t: ""))
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
