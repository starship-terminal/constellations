#!/usr/bin/env python3
"""Render style-guide.html from tokens.json.

    python3 tools/build_style_guide.py

Every token becomes a CSS custom property (its path joined with dashes; an alias becomes a var()), so
the swatches, scales and specimens cannot drift from the file. The page starts in the reader's
system theme and has a Light/Dark toggle that sets data-theme on <html>. Specimens are drawn from
tokens only, in Geist and with no Conductor artwork or icons. PRODUCT (adapt): NAME, LEDE, GROUP_ORDER and specimens().
Standard library only, deterministic.
"""
import html
import json
import pathlib
import re

PKG = pathlib.Path(__file__).resolve().parent.parent
TOKENS = json.loads((PKG / "tokens.json").read_text())
OUT = PKG / "style-guide.html"

NAME = "Conductor desktop"  # PRODUCT (adapt)
LEDE = ("Conductor 0.91.2 for macOS (Tauri: a WKWebView in an AppKit window), the app that runs coding agents in parallel workspaces, "
        "read live from the running app through Safari's Web Inspector on 2026-10-25, in its light and dark themes. Every value below is a "
        "token from tokens.json; the specimens are rebuilt from those tokens in Geist, Conductor's interface font, not copied from the app.")  # PRODUCT (adapt)
GROUP_ORDER = ["role", "base", "sidebar", "link", "highlight", "warning", "tip", "status", "todo", "checks", "git", "code", "terminal", "shadow", "component"]


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
        if p[0] != group or t["$type"] not in ("color", "dimension"):
            continue
        cells = []
        if t["$type"] == "dimension":     # component heights, radii, padding: shown as values, no swatch
            for sets in ((light, core), (dark, core)):
                tok = sets[0][p]
                shown = resolve(tok["$value"], *sets)
                label = tok["$value"] if tok["$value"] == shown else f"{tok['$value']} = {shown}"
                cells.append(f'<td><code>{esc(label)}</code> {ev(tok)}</td>')
            rows.append(f"<tr><th><code>{esc('.'.join(p))}</code></th>{''.join(cells)}</tr>")
            continue
        for sets in ((light, core), (dark, core)):
            tok = sets[0][p]
            shown = resolve(tok["$value"], *sets)
            label = tok["$value"] if tok["$value"] == shown else f"{tok['$value']} = {shown}"
            cells.append(f'<td><span class="sw"><i style="background:{esc(shown)}"></i></span><code>{esc(label)}</code> {ev(tok)}</td>')
        rows.append(f"<tr><th><code>{esc('.'.join(p))}</code></th>{''.join(cells)}</tr>")
    if not rows:
        return ""
    open_ = " open" if group in ("role", "base") else ""
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
 <figure><figcaption>Sidebar: navigation, repository, workspace row</figcaption>
  <div class="sp-sidebar">
   <div class="sp-row">Home <span class="sp-end">⌘⇧H</span></div><div class="sp-row hover">Create <span class="sp-end">⌘N</span></div><div class="sp-row">Search <span class="sp-end">⌘K</span></div>
   <div class="sp-group">My workspaces</div>
   <div class="sp-row sp-repo"><span class="sp-tile">C</span> scratch</div>
   <div class="sp-row selected">Folder files list <span class="sp-end" style="color:var(--git-green)">+1</span></div>
   <div class="sp-plan">FREE</div>
  </div>
 </figure>
 <figure><figcaption>Conversation: prompt, folded tool calls, reply, diff chip, composer</figcaption>
  <div class="sp-chat">
   <div class="sp-user">Create hello.txt here with one line</div>
   <div class="sp-turn">› 2 tool calls, 1 message</div>
   <div class="t-heading">Done</div>
   <div class="t-body">Created <span class="sp-link">hello.txt</span> with one line: <code class="sp-code">Hello, world!</code></div>
   <div class="sp-meta">8s · 9:41 AM <span class="sp-chip">hello.txt <span style="color:var(--git-green)">+1</span> <span style="color:var(--git-red)">-0</span></span></div>
   <div class="sp-composer"><div style="color:var(--base-muted-foreground)">Ask to make changes, @mention files, run /commands</div>
    <div class="sp-toolbar"><span>GPT-5.6 Sol <span style="color:var(--base-muted-foreground)">High</span></span><span style="flex:1"></span><span>+</span><span class="sp-send">↑</span></div></div>
  </div>
 </figure>
 <figure><figcaption>Buttons: primary (ink), outline, secondary, destructive</figcaption>
  <div class="sp-buttons">
   <span class="sp-btn primary">Create repo</span><span class="sp-btn primary is-hover">Hover</span>
   <span class="sp-btn outline">Cancel</span><span class="sp-btn secondary">Add run script</span>
   <span class="sp-btn destructive">Remove</span><span class="sp-btn primary" style="opacity:.5">Disabled</span>
  </div>
 </figure>
 <figure><figcaption>Menu</figcaption>
  <div class="sp-menu"><div class="sp-mrow">Mark as unread <span class="sp-end">R</span></div><div class="sp-mrow hi">Pin <span class="sp-end">P</span></div><div class="sp-mrow">Set status <span class="sp-end">›</span></div><div class="sp-mrow">Archive <span class="sp-end">⌘⇧A</span></div></div>
  <span class="sp-tooltip">Settings <span class="sp-kbd">⌘,</span></span>
 </figure>
 <figure><figcaption>Confirmation dialog over the scrim</figcaption>
  <div class="sp-scrim"><div class="sp-dialog"><div class="t-dialog-title">Remove scratch?</div>
   <div style="color:var(--base-muted-foreground);margin-top:6px">All your workspaces will be permanently deleted.</div>
   <div style="display:flex;gap:8px;justify-content:flex-end;margin-top:16px"><span class="sp-btn outline">Cancel</span><span class="sp-btn destructive">Remove</span></div></div></div>
 </figure>
 <figure><figcaption>Settings rows: switch, select, text field with focus and error</figcaption>
  <div class="sp-settings">
   <div class="sp-field"><div><div class="t-ui">Agent notifications</div><div class="t-body-secondary">Get notified when an agent finishes working.</div></div><span class="sp-switch on"></span></div>
   <div class="sp-field"><div><div class="t-ui">Low-contrast dark mode</div></div><span class="sp-switch"></span></div>
   <div class="sp-field"><div class="t-ui">Send messages with</div><span class="sp-select">Enter ⇅</span></div>
   <div class="sp-input focus">designs</div><div style="color:var(--base-destructive);font-size:var(--fontSize-xs);margin-top:6px">This repository already exists.</div>
  </div>
 </figure>
 <figure><figcaption>Panel tabs, file tree and a diff line</figcaption>
  <div class="sp-panel"><span class="sp-ptab on">All files</span><span class="sp-ptab">Changes <span class="t-code">1</span></span><span class="sp-ptab">Checks</span></div>
  <div class="sp-tree t-file">.context</div><div class="sp-tree t-file">hello.txt</div>
  <div class="sp-diff t-diff"><span class="sp-gutter">1</span>Hello, world!</div>
 </figure>
</div>"""


SPEC_CSS = """
.spec-grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(300px,1fr)); gap:20px; }
figure { margin:0; padding:16px; background:var(--role-page); border:1px solid var(--base-border); border-radius:var(--radius-xl); color:var(--base-foreground); font-family:var(--fontFamily-sans); font-size:var(--fontSize-sm); min-width:0; }
figcaption { font-size:12px; color:var(--base-muted-foreground); margin-bottom:12px; }
.sp-sidebar { background:var(--sidebar-background); border-radius:var(--radius-lg); padding:6px; color:var(--sidebar-foreground); }
.sp-row { display:flex; align-items:center; gap:8px; height:var(--size-control-nav-row); padding:0 8px; border-radius:var(--radius-md); color:var(--sidebar-muted-foreground); }
.sp-row.hover, .sp-row.selected { background:var(--sidebar-accent); color:var(--sidebar-accent-foreground); }
.sp-repo { font-weight:600; }
.sp-tile { display:inline-grid; place-items:center; width:16px; height:16px; border-radius:var(--radius-sm); background:var(--base-muted); font-size:10px; }
.sp-group { padding:10px 8px 4px; color:var(--sidebar-muted-foreground); opacity:.7; font-size:var(--fontSize-xs); font-weight:600; }
.sp-end { margin-left:auto; color:var(--base-muted-foreground); font-size:var(--fontSize-xs); }
.sp-plan { display:inline-block; margin:10px 8px 2px; padding:1px 8px; border:1px dashed var(--base-muted-foreground); border-radius:var(--radius-xs); color:var(--base-muted-foreground); font-size:var(--fontSize-xs); }
.sp-chat { padding:4px; }
.sp-user { margin-left:auto; width:fit-content; max-width:85%; background:var(--component-user-message-bg); color:var(--component-user-message-text); border-radius:var(--component-user-message-radius); padding:10px 14px; }
.sp-turn { margin:12px 0 6px; color:var(--base-muted-foreground); }
.sp-link { color:var(--link-foreground); }
.sp-code { font-family:var(--fontFamily-mono); font-size:var(--fontSize-xs); border:1px solid var(--base-input-border); border-radius:var(--radius-md); padding:1px 5px; }
.sp-meta { display:flex; gap:8px; align-items:center; color:var(--base-muted-foreground); font-size:var(--fontSize-xs); margin:10px 0 12px; }
.sp-chip { border:1px solid var(--component-diff-chip-border); border-radius:var(--component-diff-chip-radius); padding:1px 6px; font-family:var(--fontFamily-mono); color:var(--base-foreground); }
.sp-composer { background:var(--component-composer-bg); border:1px solid var(--component-composer-border); border-radius:var(--component-composer-radius); padding:12px 14px; }
.sp-toolbar { display:flex; align-items:center; gap:10px; margin-top:22px; font-size:var(--fontSize-xs); }
.sp-send { width:24px; height:24px; border-radius:var(--radius-sm); display:inline-grid; place-items:center; background:var(--base-foreground); color:var(--base-background); opacity:.5; }
.sp-buttons { display:flex; flex-wrap:wrap; gap:8px; align-items:center; }
.sp-btn { display:inline-flex; align-items:center; height:var(--controlHeight-default); padding:0 12px; border-radius:var(--radius-md); border:1px solid transparent; }
.sp-btn.primary { background:var(--component-button-primary-bg); color:var(--component-button-primary-text); }
.sp-btn.primary.is-hover { background:var(--component-button-primary-bg-hover); }
.sp-btn.outline { background:var(--component-button-outline-bg); border-color:var(--component-button-outline-border); color:var(--component-button-outline-text); }
.sp-btn.secondary { background:var(--component-button-secondary-bg); color:var(--component-button-secondary-text); }
.sp-btn.destructive { background:var(--component-button-destructive-bg); color:var(--component-button-destructive-text); }
.sp-menu { background:var(--base-popover); color:var(--base-popover-foreground); box-shadow:0 0 0 1px var(--base-popover-ring), 0 4px 6px -1px rgba(0,0,0,.1), 0 2px 4px -2px rgba(0,0,0,.1); border-radius:var(--radius-lg); padding:4px; max-width:240px; }
.sp-mrow { display:flex; align-items:center; height:var(--component-menu-item-height); padding:0 var(--component-menu-item-padding); border-radius:var(--component-menu-item-radius); }
.sp-mrow.hi { background:var(--component-menu-item-highlighted-bg); }
.sp-tooltip { display:inline-flex; gap:6px; align-items:center; margin-top:14px; background:var(--component-tooltip-bg); color:var(--component-tooltip-text); box-shadow:0 0 0 1px var(--base-popover-ring); backdrop-filter:blur(var(--blur-md)); border-radius:var(--component-tooltip-radius); padding:4px 4px 4px 8px; font-size:var(--fontSize-xs); }
.sp-kbd { border:1px solid var(--base-border); border-radius:var(--radius-xs); padding:0 4px; color:var(--base-muted-foreground); }
.sp-scrim { background:var(--role-scrim); padding:24px; border-radius:var(--radius-lg); }
.sp-dialog { background:var(--component-dialog-bg); border:1px solid var(--component-dialog-border); border-radius:var(--component-dialog-radius); padding:var(--component-dialog-padding); box-shadow:var(--shadow-dialog); }
.sp-settings { display:flex; flex-direction:column; }
.sp-field { display:flex; align-items:center; justify-content:space-between; gap:12px; padding:10px 0; border-bottom:1px solid var(--base-separator); }
.sp-switch { flex:none; display:inline-block; width:var(--size-control-switch-width); height:var(--size-control-switch-height); border-radius:99px; background:var(--component-switch-off-bg); position:relative; }
.sp-switch::after { content:""; position:absolute; top:2px; left:2px; width:16px; height:16px; border-radius:99px; background:var(--base-background); }
.sp-switch.on { background:var(--component-switch-on-bg); } .sp-switch.on::after { left:22px; background:var(--base-switch-foreground); }
.sp-select { border:1px solid var(--component-select-border); background:var(--component-select-bg); border-radius:var(--radius-md); padding:5px 10px; }
.sp-input { margin-top:12px; height:var(--component-text-field-height); display:flex; align-items:center; padding:0 12px; border-radius:var(--radius-md); border:1px solid var(--component-text-field-border); background:var(--component-text-field-bg); }
.sp-input.focus { border-color:var(--base-special); }
.sp-panel { display:flex; gap:4px; margin-bottom:8px; } .sp-ptab { padding:4px 8px; border-radius:var(--radius-md); color:var(--base-muted-foreground); font-size:var(--fontSize-xs); } .sp-ptab.on { background:var(--component-panel-tab-selected-bg); color:var(--base-foreground); }
.sp-tree { height:var(--size-control-tree-row); display:flex; align-items:center; padding:0 8px; }
.sp-diff { margin-top:8px; background:var(--component-diff-line-added-bg); border-left:3px solid var(--git-new-line); padding:2px 8px; }
.sp-gutter { color:var(--component-diff-gutter-added-text); margin-right:12px; }
"""

PAGE_CSS = """
:root { color-scheme: light dark; }
html[data-theme="dark"] { color-scheme: dark; }
body { margin:0; background:var(--role-page); color:var(--base-foreground); font:14px/1.45 var(--fontFamily-sans); }
main { max-width:1180px; margin:0 auto; padding:24px 16px 64px; }
header { display:flex; gap:16px; align-items:flex-start; justify-content:space-between; flex-wrap:wrap; }
h1 { font-size:22px; margin:0 0 6px; } h2 { font-size:17px; margin:36px 0 12px; } p { color:var(--base-muted-foreground); max-width:820px; }
button.toggle { font:inherit; padding:6px 12px; border-radius:99px; border:1px solid var(--base-input); background:var(--base-secondary); color:var(--base-foreground); cursor:pointer; }
details { margin:8px 0; } summary { cursor:pointer; font-weight:600; padding:6px 0; } summary small { color:var(--base-muted-foreground); font-weight:400; }
.scroll { overflow-x:auto; }
table.tok { border-collapse:collapse; width:100%; font-size:12px; } table.tok th, table.tok td { text-align:left; padding:4px 8px; border-bottom:1px solid var(--base-border); vertical-align:middle; }
.sw { display:inline-block; width:22px; height:16px; border-radius:4px; vertical-align:middle; margin-right:6px; background-image:linear-gradient(45deg,#ccc 25%,transparent 25%,transparent 75%,#ccc 75%),linear-gradient(45deg,#ccc 25%,#fff 25%,#fff 75%,#ccc 75%); background-size:8px 8px; background-position:0 0,4px 4px; overflow:hidden; }
.sw i { display:block; width:100%; height:100%; }
code { font-family:ui-monospace, Menlo, monospace; font-size:11px; }
.ev { font-size:10px; padding:1px 5px; border-radius:99px; background:var(--base-muted); color:var(--base-muted-foreground); white-space:nowrap; }
.ev-derived { background:var(--base-accent); }
.bar { display:inline-block; height:10px; background:var(--base-primary); border-radius:2px; vertical-align:middle; }
.rad { display:inline-block; width:40px; height:24px; border:1px solid var(--role-border-strong); background:var(--base-muted); vertical-align:middle; }
.shadow-box { display:inline-block; width:80px; height:36px; background:var(--role-raised); border-radius:8px; vertical-align:middle; }
"""

sections = []
sections.append("<h2>Colour roles and theme</h2><p>role.* maps the checklist roles onto Conductor's tokens. base.* is its shadcn-shaped theme "
                "(declared as hex on :root, .light and .dark); the warm grey ramp and Tailwind's palette, the same in both themes, follow.</p>")
groups = []
for p, _ in light.items():
    if p[0] not in groups:
        groups.append(p[0])
groups.sort(key=lambda g: (GROUP_ORDER.index(g) if g in GROUP_ORDER else 99, g))
sections.append('<div class="scroll">' + "".join(colour_table(g) for g in groups) + "</div>")
palette_rows = "".join(f'<tr><th><code>{esc(".".join(p))}</code></th><td><span class="sw"><i style="background:{esc(t["$value"])}"></i></span><code>{esc(t["$value"])}</code> {ev(t)}</td></tr>'
                       for p, t in core.items() if p[0] == "color")
sections.append(f'<details><summary>color (the warm grey ramp and Tailwind palette, core) <small>{sum(1 for p in core if p[0] == "color")}</small></summary><table class="tok">{palette_rows}</table></details>')
sections.append("<h2>Type</h2>" + "".join(
    f'<div style="margin:8px 0"><div class="t-{p[-1]}">{esc(p[-1].capitalize())}: The agent listed the files in this folder</div>'
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
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@300..700&family=Geist+Mono:wght@400..600&display=swap" rel="stylesheet">
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
