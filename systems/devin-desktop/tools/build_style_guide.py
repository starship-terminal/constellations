#!/usr/bin/env python3
"""Render style-guide.html from tokens.json.

    python3 tools/build_style_guide.py

Every token becomes a CSS custom property (its path joined with dashes; an alias becomes a var()), so
the swatches, scales and specimens cannot drift from the file. The page starts in the reader's
system theme and has a Light/Dark toggle that sets data-theme on <html>. Specimens are drawn from
tokens only, in the token's own families with system fallbacks (Inter and Devin Mono are not bundled),
and no Devin artwork or icons. PRODUCT (adapt): NAME, LEDE, GROUP_ORDER and specimens().
Standard library only, deterministic.
"""
import html
import json
import pathlib
import re

PKG = pathlib.Path(__file__).resolve().parent.parent
TOKENS = json.loads((PKG / "tokens.json").read_text())
OUT = PKG / "style-guide.html"

NAME = "Devin desktop"  # PRODUCT (adapt)
LEDE = ("Devin 3.11.216 for macOS (Electron 42, built on Windsurf), the Agents view and the IDE view, read live from the running app "
        "over its remote-debugging port on 2026-10-25, in Devin Light and Devin Dark. Every value below is a token from tokens.json; the "
        "specimens are rebuilt from those tokens, not copied from the app.")  # PRODUCT (adapt)
GROUP_ORDER = ["role", "bg", "text", "border", "tint", "hue", "shadow-color", "diff", "word-diff", "chart", "ide", "shadow", "component"]


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
    return """
<div class="spec-grid">
 <figure><figcaption>Sidebar: navigation, a two-line session row, the current row</figcaption>
  <div class="sp-sidebar">
   <div class="sp-row sel">New session</div><div class="sp-row">Automations</div><div class="sp-row">Wiki</div>
   <div class="sp-group t-caption">Sessions</div>
   <div class="sp-row two"><div><div>Change scene limit</div><div class="sp-meta">12 days ago · <span style="color:var(--text-purple)">1</span></div></div><span class="sp-dot"></span></div>
   <div class="sp-row two hover"><div><div>List files in the folder</div><div class="sp-meta">now</div></div></div>
  </div>
 </figure>
 <figure><figcaption>Composer on the New session page, with the Cloud / Local segments</figcaption>
  <div style="display:flex;justify-content:flex-end;margin-bottom:8px"><span class="sp-seg"><span class="on">Cloud</span><span>Local</span></span></div>
  <div class="sp-composer"><div class="t-prompt" style="color:var(--text-tertiary)">Tip: Search sessions and commands</div>
   <div class="sp-toolbar"><span class="sp-icon-btn">+</span><span class="sp-icon-btn">/</span><span style="color:var(--text-secondary)">Agent</span><span style="flex:1"></span><span style="color:var(--text-secondary)">Normal</span><span class="sp-send">↑</span></div></div>
  <div class="sp-warn">Local agents are off because this workspace is in Restricted Mode. <b>Trust workspace</b></div>
 </figure>
 <figure><figcaption>Buttons: ink, outline, danger outline, quiet, the workbench's accent primary, focus ring</figcaption>
  <div class="sp-buttons">
   <span class="sp-btn inverse">Create automation</span><span class="sp-btn outline">Customize</span><span class="sp-btn danger">Unlink user</span>
   <span class="sp-btn quiet">Reset all</span><span class="sp-btn primary">Trust Workspace &amp; Continue</span><span class="sp-btn outline focus">Focus ring</span>
  </div>
 </figure>
 <figure><figcaption>Menu (the elevated fill at 94%, a hairline outline, the large shadow)</figcaption>
  <div class="sp-menu"><div class="sp-mtitle">Capability</div><div class="sp-mrow">Fusion</div><div class="sp-mrow hi">Normal <span class="sp-end">✓</span></div><hr>
   <div class="sp-mrow">Compact view <span class="sp-end"><span class="sp-switch sm"></span></span></div></div>
 </figure>
 <figure><figcaption>Settings: a card of rows with a switch, a checkbox and a select</figcaption>
  <div class="sp-card">
   <div class="sp-field"><div><div class="t-body">Play sound with notifications</div><div class="t-body" style="color:var(--text-secondary)">When a session needs you</div></div><span class="sp-switch on"></span></div>
   <div class="sp-field"><div class="t-body">My sessions</div><span><span class="sp-check">✓</span> Mobile</span></div>
   <div class="sp-field"><div class="t-body">Theme</div><span class="sp-select">Dark ⌄</span></div>
  </div>
  <div class="sp-input">Search settings...</div>
 </figure>
 <figure><figcaption>Badges, chips and a tooltip (always dark)</figcaption>
  <div style="display:flex;gap:8px;align-items:center;flex-wrap:wrap">
   <span class="sp-badge">Merged</span><span class="sp-seg"><span class="on">All</span><span>Monitoring</span><span>Security</span></span>
   <span class="sp-tip">Search <kbd>⌘</kbd><kbd>K</kbd></span></div>
 </figure>
 <figure><figcaption>Conversation: the prompt bubble, the folded work, the plain reply, the status line</figcaption>
  <div class="sp-user">Create hello.txt here with one line</div>
  <div class="t-caption" style="color:var(--text-secondary);margin:10px 0">› Worked for a bit <span style="color:var(--text-green)">+1</span></div>
  <div class="t-message">Created <code class="sp-code-inline">hello.txt</code> with the line.</div>
  <div class="t-caption" style="color:var(--text-secondary);margin-top:10px"><span class="sp-dot" style="background:var(--hue-orange)"></span> Devin is awaiting instructions</div>
 </figure>
 <figure><figcaption>Diff rows</figcaption>
  <div class="sp-diff"><div class="del">71  const TARGET = 20 * 60 * 60;</div><div class="add">71  const TARGET = 10 * 60 * 60;</div><div>72  const CAP = 10 * 60 * 60;</div></div>
 </figure>
</div>"""


SPEC_CSS = """
.spec-grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(320px,1fr)); gap:20px; }
figure { margin:0; padding:16px; background:var(--role-page); border:1px solid var(--role-border-subtle); border-radius:var(--radius-12); color:var(--text-primary); font-family:var(--fontFamily-sans); font-size:var(--fontSize-13); }
figcaption { font-size:12px; color:var(--text-tertiary); margin-bottom:12px; }
.sp-sidebar { background:var(--bg-page); border:1px solid var(--border-secondary); border-radius:var(--radius-10); padding:var(--spacing-2); }
.sp-row { display:flex; align-items:center; gap:8px; min-height:var(--size-control-sidebar-row); padding:0 var(--spacing-2); border-radius:var(--radius-6); color:var(--text-primary); }
.sp-row.two { min-height:var(--size-control-session-row); justify-content:space-between; }
.sp-row.sel, .sp-row.hover { background:var(--tint-secondary); }
.sp-meta { color:var(--text-secondary); font-size:var(--fontSize-12); }
.sp-group { padding:10px 8px 4px; color:var(--text-secondary); font-weight:500; }
.sp-end { margin-left:auto; color:var(--text-secondary); }
.sp-dot { display:inline-block; width:8px; height:8px; border-radius:99px; background:var(--text-accent-primary); }
.sp-seg { display:inline-flex; gap:1px; padding:1px; border-radius:var(--radius-20); background:var(--component-segmented-bg); }
.sp-seg span { padding:4px 12px; border-radius:99px; color:var(--text-secondary); border:1px solid transparent; }
.sp-seg span.on { background:var(--component-segment-selected-bg); color:var(--text-primary); border-color:var(--border-secondary); box-shadow:var(--shadow-L1); }
.sp-composer { background:var(--component-composer-bg); border:1px solid var(--component-composer-border); border-radius:var(--component-composer-radius); padding:10px 12px; }
.sp-toolbar { display:flex; align-items:center; gap:8px; margin-top:22px; }
.sp-send { width:28px; height:28px; border-radius:99px; display:inline-grid; place-items:center; background:var(--bg-accent-neutral); color:var(--text-primary-inverse); }
.sp-warn { margin-top:10px; padding:10px 14px; border-radius:var(--component-banner-warning-radius); background:var(--component-banner-warning-bg); color:var(--component-banner-warning-text); }
.sp-warn b { float:right; font-weight:500; }
.sp-buttons { display:flex; flex-wrap:wrap; gap:8px; align-items:center; }
.sp-btn { display:inline-flex; align-items:center; height:var(--controlHeight-base); padding:0 10px; border-radius:var(--radius-6); font-weight:500; border:1px solid transparent; }
.sp-btn.inverse { background:var(--component-button-inverse-bg); color:var(--component-button-inverse-text); }
.sp-btn.outline { border-color:var(--component-button-outline-border); color:var(--text-primary); height:var(--controlHeight-sm); }
.sp-btn.danger { border-color:var(--component-button-danger-border); color:var(--component-button-danger-text); height:var(--controlHeight-sm); }
.sp-btn.quiet { color:var(--text-secondary); }
.sp-btn.primary { background:var(--bg-accent-primary); color:var(--text-always-white); height:var(--controlHeight-lg); padding:0 12px; }
.sp-btn.focus { outline:var(--focusRing-width) solid var(--role-border-focus); outline-offset:var(--focusRing-offset); }
.sp-icon-btn { width:28px; height:28px; border-radius:var(--radius-6); display:inline-grid; place-items:center; color:var(--text-secondary); }
.sp-menu { background:var(--component-menu-bg); outline:1px solid var(--component-menu-outline); border-radius:var(--component-menu-radius); padding:4px; max-width:240px; box-shadow:var(--shadow-L3); }
.sp-menu hr { border:0; border-top:1px solid var(--border-secondary); margin:4px 8px; }
.sp-mtitle { padding:4px 8px; color:var(--text-secondary); font-size:var(--fontSize-12); font-weight:500; }
.sp-mrow { display:flex; align-items:center; height:var(--size-control-menu-row); padding:0 8px; border-radius:var(--radius-6); }
.sp-mrow.hi { background:var(--tint-secondary); }
.sp-switch { display:inline-block; width:var(--size-control-switch-width); height:var(--size-control-switch-height); border-radius:99px; background:var(--component-switch-off-bg); position:relative; vertical-align:middle; }
.sp-switch::after { content:""; position:absolute; top:2px; left:2px; width:16px; height:16px; border-radius:99px; background:#fff; }
.sp-switch.on { background:var(--component-switch-on-bg); } .sp-switch.on::after { left:18px; }
.sp-switch.sm { width:var(--size-control-switch-sm-width); height:var(--size-control-switch-sm-height); } .sp-switch.sm::after { width:12px; height:12px; }
.sp-check { display:inline-grid; place-items:center; width:16px; height:16px; border-radius:var(--radius-4); background:var(--component-checkbox-bg); color:#fff; font-size:11px; }
.sp-card { background:var(--tint-tertiary); border-radius:var(--radius-10); padding:0; overflow:hidden; }
.sp-card > .sp-field:first-child { border-top-left-radius:var(--radius-10); border-top-right-radius:var(--radius-10); }
.sp-field { display:flex; align-items:center; justify-content:space-between; gap:12px; padding:12px; background:var(--component-settings-card-bg); border:1px solid var(--component-settings-card-border); margin-bottom:-1px; }
.sp-select { border:1px solid var(--component-select-border); border-radius:var(--radius-6); padding:3px 8px; color:var(--text-primary); }
.sp-input { margin-top:10px; height:var(--controlHeight-base); display:flex; align-items:center; padding:0 8px; border-radius:var(--radius-6); background:var(--component-text-field-bg); border:1px solid var(--component-text-field-border); color:var(--text-secondary); }
.sp-badge { display:inline-flex; height:22px; align-items:center; padding:0 10px; border-radius:99px; background:var(--component-badge-merged-bg); color:var(--component-badge-merged-text); font-weight:500; }
.sp-tip { display:inline-flex; align-items:center; gap:6px; padding:3px 6px 3px 8px; border-radius:var(--radius-6); background:#252525; color:rgba(255,255,255,0.9); font-size:12px; box-shadow:var(--shadow-L1); }
.sp-tip kbd { font:inherit; padding:0 4px; border-radius:4px; background:rgba(255,255,255,0.08); }
.sp-user { margin-left:auto; width:fit-content; max-width:80%; background:var(--tint-tertiary); border-radius:var(--radius-16); padding:8px 14px; font-size:var(--fontSize-14); }
.sp-code-inline { font-family:var(--fontFamily-mono); font-size:12px; padding:0 3px; border-radius:var(--radius-4); background:var(--component-inline-code-bg); }
.sp-diff { font-family:var(--fontFamily-mono); font-size:12px; line-height:20px; background:var(--bg-elevated); border:1px solid var(--border-secondary); border-radius:var(--radius-10); overflow:hidden; }
.sp-diff div { padding:0 10px; } .sp-diff .add { background:var(--tint-green); } .sp-diff .del { background:var(--tint-red); }
"""

PAGE_CSS = """
:root { color-scheme: light dark; }
html[data-theme="dark"] { color-scheme: dark; }
body { margin:0; background:var(--role-page); color:var(--text-primary); font:13px/1.45 -apple-system, BlinkMacSystemFont, sans-serif; }
main { max-width:1180px; margin:0 auto; padding:24px 16px 64px; }
header { display:flex; gap:16px; align-items:flex-start; justify-content:space-between; flex-wrap:wrap; }
h1 { font-size:22px; margin:0 0 6px; } h2 { font-size:17px; margin:36px 0 12px; } p { color:var(--text-secondary); max-width:820px; }
button.toggle { font:inherit; padding:6px 12px; border-radius:99px; border:1px solid var(--role-border-default); background:var(--tint-secondary); color:var(--text-primary); cursor:pointer; }
details { margin:8px 0; } summary { cursor:pointer; font-weight:600; padding:6px 0; } summary small { color:var(--text-tertiary); font-weight:400; }
.scroll { overflow-x:auto; }
table.tok { border-collapse:collapse; width:100%; font-size:12px; } table.tok th, table.tok td { text-align:left; padding:4px 8px; border-bottom:1px solid var(--border-secondary); vertical-align:middle; }
.sw { display:inline-block; width:22px; height:16px; border-radius:4px; vertical-align:middle; margin-right:6px; background-image:linear-gradient(45deg,#ccc 25%,transparent 25%,transparent 75%,#ccc 75%),linear-gradient(45deg,#ccc 25%,#fff 25%,#fff 75%,#ccc 75%); background-size:8px 8px; background-position:0 0,4px 4px; overflow:hidden; }
.sw i { display:block; width:100%; height:100%; }
code { font-family:ui-monospace, Menlo, monospace; font-size:11px; }
.ev { font-size:10px; padding:1px 5px; border-radius:99px; background:var(--tint-tertiary); color:var(--text-secondary); white-space:nowrap; }
.ev-derived { background:var(--bg-accent-secondary); }
.bar { display:inline-block; height:10px; background:var(--bg-accent-primary); border-radius:2px; vertical-align:middle; }
.rad { display:inline-block; width:40px; height:24px; border:1px solid var(--role-border-strong); background:var(--tint-tertiary); vertical-align:middle; }
.shadow-box { display:inline-block; width:80px; height:36px; background:var(--role-raised); border-radius:8px; vertical-align:middle; }
"""

sections = []
sections.append("<h2>Colour roles and tokens</h2><p>role.* maps the checklist roles onto Devin's tokens. A theme is a list of colour "
                "channels: every neutral is white (dark) or near-black (light) at a fixed alpha, plus six flat hues; the IDE view's colours are the same values.</p>")
groups = []
for p, _ in light.items():
    if p[0] not in groups:
        groups.append(p[0])
groups.sort(key=lambda g: (GROUP_ORDER.index(g) if g in GROUP_ORDER else 99, g))
sections.append('<div class="scroll">' + "".join(colour_table(g) for g in groups) + "</div>")
sections.append("<h2>Type</h2>" + scale_rows("fontSize", lambda p, t: f'<span style="font-size:{t["$value"]}">Aa</span>') + "".join(
    f'<div style="margin:8px 0"><div class="t-{p[-1]}">{esc(p[-1].capitalize())}: Devin listed the files in this folder</div>'
    f'<code>{esc(json.dumps(t["$value"]))}</code> {ev(t)}</div>' for p, t in core.items() if t["$type"] == "typography"))
sections.append("<h2>Radius</h2>" + scale_rows("radius", lambda p, t: f'<span class="rad" style="border-radius:{t["$value"]}"></span>'))
sections.append("<h2>Spacing</h2>" + scale_rows("spacing", lambda p, t: f'<span class="bar" style="width:{t["$value"]}"></span>'))
sections.append("<h2>Control heights, sizes and layout</h2>" + scale_rows("controlHeight", lambda p, t: f'<span class="bar" style="width:{t["$value"]}"></span>')
                + scale_rows("size", lambda p, t: "") + scale_rows("layout", lambda p, t: "") + scale_rows("focusRing", lambda p, t: "")
                + scale_rows("borderWidth", lambda p, t: "") + scale_rows("blur", lambda p, t: ""))
shadow_rows = "".join(f"<tr><th><code>{esc('.'.join(p))}</code></th><td><span class=\"shadow-box\" style=\"box-shadow:var({var(p)})\"></span></td><td>{ev(t)}</td></tr>"
                      for p, t in light.items() if p[0] == "shadow" and t["$type"] == "shadow")
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
