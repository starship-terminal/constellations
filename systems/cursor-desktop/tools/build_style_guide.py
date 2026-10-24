#!/usr/bin/env python3
"""Render style-guide.html from tokens.json.

    python3 tools/build_style_guide.py

Every token becomes a CSS custom property (its path joined with dashes; an alias becomes a var()), so
the swatches, scales and specimens cannot drift from the file. The page starts in the reader's
system theme and has a Light/Dark toggle that sets data-theme on <html>. Specimens are drawn from
tokens only, with the system font in place of nothing (Cursor uses the system font too) and no
Cursor artwork or icons. PRODUCT (adapt): NAME, LEDE, GROUP_ORDER and specimens().
Standard library only, deterministic.
"""
import html
import json
import pathlib
import re

PKG = pathlib.Path(__file__).resolve().parent.parent
TOKENS = json.loads((PKG / "tokens.json").read_text())
OUT = PKG / "style-guide.html"

NAME = "Cursor desktop"  # PRODUCT (adapt)
LEDE = ("Cursor 3.27.6 for macOS (Electron 42), the Agents window and the IDE window, read live from the running app over "
        "its remote-debugging port on 2026-10-25, in Cursor Light and Cursor Dark. Every value below is a token from "
        "tokens.json; the specimens are rebuilt from those tokens, not copied from the app.")  # PRODUCT (adapt)
GROUP_ORDER = ["role", "seed", "bg", "text", "stroke", "icon", "button", "control", "accent", "glass", "ide", "blue", "cyan",
               "green", "magenta", "orange", "purple", "red", "yellow", "brown", "success", "danger", "warn", "diff", "editor",
               "terminal", "syntax", "scrollbar", "specular", "command", "input", "titlebar", "toolbar", "progress", "focus",
               "on", "added", "modified", "removed", "untracked", "ui", "shadow", "component"]


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
        type_css.append(f".t-{p[-1]} {{ font-family: {fam}; font-size: {v['fontSize']}; font-weight: {v['fontWeight']}; "
                        f"line-height: {v['lineHeight']}; letter-spacing: {v['letterSpacing']}; }}")


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
    c = lambda name: f"var(--component-{name})"
    return f"""
<div class="spec-grid">
 <figure><figcaption>Sidebar and rows</figcaption>
  <div class="sp-sidebar">
   <div class="sp-row sel">New Chat</div><div class="sp-row">Automations</div><div class="sp-row">Customize</div>
   <div class="sp-group t-caption">Projects</div>
   <div class="sp-row"><span class="dot" style="background:var(--bg-accent-primary)"></span>toolbox-v1 <span class="sp-end">19h</span></div>
   <div class="sp-row hover"><span class="dot"></span>harness-scratch <span class="sp-end">1m</span></div>
   <div class="sp-foot"><span class="sp-avatar">WC</span><span>Account</span><span class="sp-update">Update</span></div>
  </div>
 </figure>
 <figure><figcaption>Composer on the New Chat page</figcaption>
  <div class="sp-composer"><div class="t-prompt" style="color:var(--text-tertiary)">Plan, Build, / for skills, @ for context</div>
   <div class="sp-toolbar"><span class="sp-icon-btn">+</span><span style="flex:1"></span><span class="sp-model">Model High</span><span class="sp-send"></span></div></div>
  <div style="display:flex;gap:8px;margin-top:10px"><span class="sp-pill">Plan New Idea</span><span class="sp-pill">Multitask</span></div>
 </figure>
 <figure><figcaption>Buttons: primary (accent), inverse, outline, quiet, icon; hover and pressed share one fill</figcaption>
  <div class="sp-buttons">
   <span class="sp-btn primary">Create Project</span><span class="sp-btn primary is-hover">Hover</span>
   <span class="sp-btn inverse">New Automation</span><span class="sp-btn outline">Open</span>
   <span class="sp-btn quiet">Cancel</span><span class="sp-icon-btn">⋯</span><span class="sp-btn primary focus">Focus ring</span>
  </div>
 </figure>
 <figure><figcaption>Menu (raised surface, 8px rows)</figcaption>
  <div class="sp-menu"><div class="sp-mrow">Rename</div><div class="sp-mrow hi">Mark as Read</div><hr><div class="sp-mrow">Copy <span class="sp-end">›</span></div>
   <div class="sp-mrow"><span>Fast</span><span class="sp-end"><span class="sp-switch sm"></span></span></div></div>
 </figure>
 <figure><figcaption>Dialog over the scrim</figcaption>
  <div class="sp-scrim"><div class="sp-dialog"><div class="t-body" style="font-weight:600">Delete automation</div>
   <div class="t-body-secondary">Are you sure? This cannot be undone.</div>
   <div style="display:flex;gap:8px;justify-content:flex-end;margin-top:14px"><span class="sp-btn quiet">Cancel</span><span class="sp-btn primary">Delete</span></div></div></div>
 </figure>
 <figure><figcaption>Settings rows: tabs, switch, select, field</figcaption>
  <div class="sp-tabs"><span class="sp-tab sel">All</span><span class="sp-tab">Projects</span><span class="sp-tab">Agents</span></div>
  <div class="sp-field-group">
   <div class="sp-field"><div><div class="t-body">System Notifications</div><div class="t-body-secondary">When Agent completes</div></div><span class="sp-switch on"></span></div>
   <div class="sp-field"><div><div class="t-body">Warning Notifications</div><div class="t-body-secondary">Less urgent issues</div></div><span class="sp-switch"></span></div>
   <div class="sp-field"><div class="t-body">Window Restoration</div><span class="sp-select">Default ⌄</span></div>
  </div>
  <div class="sp-input">Search Settings</div>
 </figure>
 <figure><figcaption>Banner, badge, table</figcaption>
  <div class="sp-banner">Plugins, MCPs, Skills, and Rules have moved to Customize</div>
  <div class="sp-table"><div class="sp-tr head t-caption"><span>Name</span><span>Status</span></div>
   <div class="sp-tr"><span>Daily digest</span><span style="color:var(--text-success-primary)">✓ Active</span></div>
   <div class="sp-tr hover"><span>Untitled <span class="sp-badge">Plugin</span></span><span style="color:var(--text-secondary)">× Inactive</span></div></div>
 </figure>
 <figure><figcaption>Conversation: user bubble, plain reply, code block</figcaption>
  <div class="sp-user">List the files in this folder.</div>
  <div class="t-caption" style="color:var(--text-tertiary);margin:8px 0">Worked for 13s</div>
  <div class="t-message">This folder is empty. No files or subfolders.</div>
  <pre class="sp-code t-code">total 8
-rw-r--r--  1 user  staff  30 hello.txt</pre>
 </figure>
</div>"""


SPEC_CSS = """
.spec-grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(320px,1fr)); gap:20px; }
figure { margin:0; padding:16px; background:var(--role-page); border:1px solid var(--role-border-subtle); border-radius:var(--radius-xl); color:var(--text-primary); font-family:var(--fontFamily-sans); font-size:var(--fontSize-base); font-weight:var(--fontWeight-normal-ui); }
figcaption { font-size:12px; color:var(--text-tertiary); margin-bottom:12px; }
.sp-sidebar { background:var(--role-surface); border-radius:var(--radius-lg); padding:var(--spacing-2); }
.sp-row { display:flex; align-items:center; gap:8px; height:var(--size-control-sidebar-row); padding:0 var(--spacing-1-5); border-radius:var(--radius-lg); color:var(--text-secondary); }
.sp-row.sel { background:var(--bg-tertiary); color:var(--text-primary); }
.sp-row.hover { background:var(--bg-quaternary); color:var(--text-primary); }
.sp-group { padding:8px 6px 4px; color:var(--text-tertiary); }
.sp-end { margin-left:auto; color:var(--text-tertiary); }
.dot { width:6px; height:6px; border-radius:99px; background:var(--text-quaternary); }
.sp-foot { display:flex; align-items:center; gap:8px; padding:8px 6px 2px; }
.sp-avatar { width:28px; height:28px; border-radius:99px; display:grid; place-items:center; font-size:11px; color:var(--text-secondary); background:var(--bg-tertiary); }
.sp-update { margin-left:auto; height:24px; padding:0 8px; border-radius:99px; display:inline-flex; align-items:center; background:var(--component-button-update-bg); color:var(--component-button-update-text); font-weight:500; }
.sp-composer { background:var(--component-composer-bg); border:1px solid var(--component-composer-border); border-radius:var(--component-composer-radius); padding:8px 12px; }
.sp-toolbar { display:flex; align-items:center; gap:8px; margin-top:22px; }
.sp-model { color:var(--text-secondary); }
.sp-send { width:24px; height:24px; border-radius:99px; background:var(--text-primary); }
.sp-pill { display:inline-flex; align-items:center; height:var(--component-pill-height); padding:0 10px; border-radius:99px; border:1px solid var(--component-pill-border); color:var(--component-pill-text); }
.sp-buttons { display:flex; flex-wrap:wrap; gap:8px; align-items:center; }
.sp-btn { display:inline-flex; align-items:center; height:var(--size-control-button); padding:0 10px; border-radius:var(--radius-lg); font-weight:500; letter-spacing:-0.08px; border:1px solid transparent; }
.sp-btn.primary { background:var(--component-button-primary-bg); color:var(--component-button-primary-text); }
.sp-btn.primary.is-hover { background:var(--component-button-primary-bg-hover); }
.sp-btn.inverse { background:var(--component-button-inverse-bg); color:var(--component-button-inverse-text); border-radius:99px; padding:0 12px; }
.sp-btn.outline { border-color:var(--role-border-default); color:var(--text-primary); border-radius:99px; }
.sp-btn.quiet { color:var(--text-secondary); }
.sp-btn.focus { outline:var(--focusRing-width) solid var(--role-border-focus); outline-offset:var(--focusRing-offset-default); }
.sp-icon-btn { width:24px; height:24px; border-radius:var(--radius-base); display:inline-grid; place-items:center; color:var(--text-secondary); background:var(--bg-tertiary); }
.sp-menu { background:var(--component-menu-bg); border-radius:var(--radius-xl); padding:4px; box-shadow:var(--shadow-popup); max-width:220px; }
.sp-menu hr { border:0; border-top:1px solid var(--stroke-tertiary); margin:4px 10px; }
.sp-mrow { display:flex; align-items:center; height:28px; padding:0 10px; border-radius:var(--radius-lg); }
.sp-mrow.hi { background:var(--bg-tertiary); }
.sp-switch { display:inline-block; width:32px; height:20px; border-radius:99px; background:var(--bg-secondary); position:relative; }
.sp-switch::after { content:""; position:absolute; top:2px; left:2px; width:16px; height:16px; border-radius:99px; background:#fff; }
.sp-switch.on { background:var(--bg-success-primary); } .sp-switch.on::after { left:14px; }
.sp-switch.sm { width:26px; height:16px; } .sp-switch.sm::after { width:12px; height:12px; }
.sp-scrim { background:var(--role-scrim); padding:24px; border-radius:var(--radius-lg); }
.sp-dialog { background:var(--component-dialog-bg); border:1px solid var(--component-dialog-border); border-radius:var(--component-dialog-radius); padding:16px; box-shadow:var(--shadow-xl); }
.sp-tabs { display:flex; gap:4px; margin-bottom:10px; } .sp-tab { padding:5px 10px; border-radius:99px; color:var(--text-secondary); } .sp-tab.sel { background:var(--bg-tertiary); color:var(--text-primary); }
.sp-field-group { border-radius:var(--radius-xl); background:var(--bg-card); }
.sp-field { display:flex; align-items:center; justify-content:space-between; padding:12px; border-bottom:1px solid var(--stroke-quaternary); }
.sp-select { border:1px solid var(--role-border-default); border-radius:var(--radius-base); padding:2px 8px; color:var(--text-secondary); }
.sp-input { margin-top:10px; height:28px; display:flex; align-items:center; padding:0 8px; border-radius:var(--radius-base); background:var(--component-text-field-bg); border:1px solid var(--component-text-field-border); color:var(--text-tertiary); }
.sp-banner { border-radius:var(--radius-xl); padding:12px 14px; background:var(--component-banner-info-bg); border:1px solid var(--component-banner-info-border); margin-bottom:10px; }
.sp-table { background:var(--component-table-bg); border:1px solid var(--component-table-border); border-radius:var(--component-table-radius); padding:4px 6px; }
.sp-tr { display:flex; justify-content:space-between; padding:10px 8px; border-radius:var(--radius-base); } .sp-tr.head { color:var(--text-tertiary); } .sp-tr.hover { background:var(--bg-quaternary); }
.sp-badge { display:inline-flex; height:20px; align-items:center; padding:0 8px; border-radius:99px; background:var(--component-badge-bg); color:var(--component-badge-text); font-size:12px; }
.sp-user { background:var(--component-user-message-bg); border:1px solid var(--component-user-message-border); border-radius:var(--component-user-message-radius); padding:8px 12px; }
.sp-code { background:var(--component-code-block-bg); border:1px solid var(--component-code-block-border); border-radius:var(--component-code-block-radius); padding:10px 12px; margin:10px 0 0; overflow:auto; }
"""

PAGE_CSS = """
:root { color-scheme: light dark; }
html[data-theme="dark"] { color-scheme: dark; }
body { margin:0; background:var(--role-page); color:var(--text-primary); font:13px/1.45 -apple-system, BlinkMacSystemFont, sans-serif; }
main { max-width:1180px; margin:0 auto; padding:24px 16px 64px; }
header { display:flex; gap:16px; align-items:flex-start; justify-content:space-between; flex-wrap:wrap; }
h1 { font-size:22px; margin:0 0 6px; } h2 { font-size:17px; margin:36px 0 12px; } p { color:var(--text-secondary); max-width:820px; }
button.toggle { font:inherit; padding:6px 12px; border-radius:99px; border:1px solid var(--role-border-default); background:var(--bg-tertiary); color:var(--text-primary); cursor:pointer; }
details { margin:8px 0; } summary { cursor:pointer; font-weight:600; padding:6px 0; } summary small { color:var(--text-tertiary); font-weight:400; }
.scroll { overflow-x:auto; }
table.tok { border-collapse:collapse; width:100%; font-size:12px; } table.tok th, table.tok td { text-align:left; padding:4px 8px; border-bottom:1px solid var(--stroke-quaternary); vertical-align:middle; }
.sw { display:inline-block; width:22px; height:16px; border-radius:4px; vertical-align:middle; margin-right:6px; background-image:linear-gradient(45deg,#ccc 25%,transparent 25%,transparent 75%,#ccc 75%),linear-gradient(45deg,#ccc 25%,#fff 25%,#fff 75%,#ccc 75%); background-size:8px 8px; background-position:0 0,4px 4px; overflow:hidden; }
.sw i { display:block; width:100%; height:100%; }
code { font-family:ui-monospace, Menlo, monospace; font-size:11px; }
.ev { font-size:10px; padding:1px 5px; border-radius:99px; background:var(--bg-quaternary); color:var(--text-secondary); white-space:nowrap; }
.ev-derived { background:var(--bg-accent-quaternary); }
.bar { display:inline-block; height:10px; background:var(--bg-accent-primary); border-radius:2px; vertical-align:middle; }
.rad { display:inline-block; width:40px; height:24px; border:1px solid var(--role-border-strong); background:var(--bg-quaternary); vertical-align:middle; }
.shadow-box { display:inline-block; width:80px; height:36px; background:var(--role-raised); border-radius:8px; vertical-align:middle; }
"""

sections = []
sections.append("<h2>Colour roles and seeds</h2><p>role.* maps the checklist roles onto Cursor's tokens. A theme is a few seed colours; "
                "most other colours are a seed mixed with transparent (the formula is on each token in tokens.json).</p>")
groups = []
for p, _ in light.items():
    if p[0] not in groups:
        groups.append(p[0])
groups.sort(key=lambda g: (GROUP_ORDER.index(g) if g in GROUP_ORDER else 99, g))
sections.append('<div class="scroll">' + "".join(colour_table(g) for g in groups if g not in ("shadow",)) + "</div>")
sections.append("<h2>Type</h2>" + "".join(
    f'<div style="margin:8px 0"><div class="t-{p[-1]}">{esc(p[-1].capitalize())}: The agent listed the files in this folder</div>'
    f'<code>{esc(json.dumps(t["$value"]))}</code> {ev(t)}</div>' for p, t in core.items() if t["$type"] == "typography"))
sections.append("<h2>Radius</h2>" + scale_rows("radius", lambda p, t: f'<span class="rad" style="border-radius:{t["$value"]}"></span>'))
sections.append("<h2>Spacing</h2>" + scale_rows("spacing", lambda p, t: f'<span class="bar" style="width:{t["$value"]}"></span>'))
sections.append("<h2>Control heights, sizes and layout</h2>" + scale_rows("controlHeight", lambda p, t: f'<span class="bar" style="width:{t["$value"]}"></span>')
                + scale_rows("size", lambda p, t: "") + scale_rows("layout", lambda p, t: "") + scale_rows("focusRing", lambda p, t: "")
                + scale_rows("zIndex", lambda p, t: "") + scale_rows("borderWidth", lambda p, t: ""))
shadow_rows = "".join(f"<tr><th><code>{esc('.'.join(p))}</code></th><td><span class=\"shadow-box\" style=\"box-shadow:var({var(p)})\"></span></td><td>{ev(t)}</td></tr>"
                      for p, t in light.items() if p[0] == "shadow")
sections.append(f'<h2>Elevation</h2><table class="tok">{shadow_rows}</table>')
sections.append("<h2>Motion</h2>" + scale_rows("duration", lambda p, t: "") + scale_rows("easing", lambda p, t: ""))
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
