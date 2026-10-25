#!/usr/bin/env python3
"""Render style-guide.html from tokens.json.

    python3 tools/build_style_guide.py

Every token becomes a CSS custom property (its path joined with dashes; an alias becomes a var()), so
the swatches, scales and specimens cannot drift from the file. The page starts in the reader's
system theme and has a Light/Dark toggle that sets data-theme on <html>. Specimens are drawn from
tokens only, in Geist and with no Orca artwork or icons. PRODUCT (adapt): NAME, LEDE, GROUP_ORDER and specimens().
Standard library only, deterministic.
"""
import html
import json
import pathlib
import re

PKG = pathlib.Path(__file__).resolve().parent.parent
TOKENS = json.loads((PKG / "tokens.json").read_text())
OUT = PKG / "style-guide.html"

NAME = "Orca desktop"  # PRODUCT (adapt)
LEDE = ("Orca 1.4.237 for macOS (Electron), the stablyai coding-agent harness, read live from the running app over its "
        "remote-debugging port on 2026-10-25, in its light and dark themes. Every value below is a token from tokens.json; the "
        "specimens are rebuilt from those tokens in Geist, Orca's interface font, not copied from the app.")  # PRODUCT (adapt)
GROUP_ORDER = ["role", "base", "worktreeSidebar", "sidebar", "chat", "status", "agent", "callout", "workspaceStatus", "git", "diff",
               "gitGraph", "terminalPaneTitle", "paneTitle", "terminal", "chart", "markdown", "tabGroup", "security", "shadow", "component"]


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
 <figure><figcaption>Sidebar: navigation, project, workspace card</figcaption>
  <div class="sp-sidebar">
   <div class="sp-search">Search</div>
   <div class="sp-row">Tasks</div><div class="sp-row hover">Automations</div><div class="sp-row">Orca Mobile <span class="sp-new">New</span></div>
   <div class="sp-group">Projects</div>
   <div class="sp-row" style="font-weight:600">orca</div>
   <div class="sp-ws"><div><span class="dot" style="background:var(--status-success)"></span> main <span class="sp-badge">primary</span></div><div class="sp-muted">main</div></div>
  </div>
 </figure>
 <figure><figcaption>Chat: user bubble, collapsed turn, reply, code block, composer</figcaption>
  <div class="sp-chat">
   <div class="sp-user">List the files in this folder.</div>
   <div class="sp-turn">Worked for 11s ›</div>
   <div class="t-message"><b>Done</b><br>The folder contains only the hidden .git directory.</div>
   <pre class="sp-code t-code">total 8
-rw-r--r--  1 user  staff  30 hello.txt</pre>
   <div class="sp-composer"><div style="color:var(--chat-foreground-faint)">Ask anything, @ to mention files, / for commands</div>
    <div class="sp-toolbar"><span>+</span><span style="color:var(--status-warning)">Full access</span><span style="flex:1"></span><span>Opus High</span><span class="sp-send">↑</span></div></div>
  </div>
 </figure>
 <figure><figcaption>Buttons: default (ink), outline, secondary, ghost, destructive; focus ring</figcaption>
  <div class="sp-buttons">
   <span class="sp-btn default">Update</span><span class="sp-btn default is-hover">Hover</span>
   <span class="sp-btn outline">Browse</span><span class="sp-btn secondary">Secondary</span><span class="sp-btn ghost">Ghost</span>
   <span class="sp-btn destructive">Remove</span><span class="sp-btn outline focus">Focus ring</span>
  </div>
 </figure>
 <figure><figcaption>Menu with a destructive item</figcaption>
  <div class="sp-menu"><div class="sp-mrow">Project Settings</div><div class="sp-mrow hi">Change Project Icon</div><div class="sp-mrow">New Terminal <span class="sp-end">⌘T</span></div><hr><div class="sp-mrow danger">Remove Project</div></div>
 </figure>
 <figure><figcaption>Confirmation dialog over the overlay</figcaption>
  <div class="sp-scrim"><div class="sp-dialog"><div style="font-weight:600;font-size:16px">Remove Project</div>
   <div style="color:var(--base-muted-foreground);margin-top:6px">This only removes <b style="color:var(--base-foreground)">orca</b> from Orca. It is still on your disk.</div>
   <div style="display:flex;gap:8px;justify-content:flex-end;margin-top:16px"><span class="sp-btn outline">Cancel</span><span class="sp-btn destructive">Remove</span></div></div></div>
 </figure>
 <figure><figcaption>Settings card: rows, switches, select, segmented radio, input</figcaption>
  <div class="sp-card">
   <div style="font-weight:600;margin-bottom:12px">Navigation</div>
   <div class="sp-field"><div><div class="sp-label">Confirm before closing pinned tabs</div><div class="sp-desc">Show a confirmation dialog before a pinned tab is closed.</div></div><span class="sp-switch on"></span></div>
   <div class="sp-field"><div class="sp-label">Chat UI</div><span class="sp-switch"></span></div>
   <div class="sp-field"><div class="sp-label">Tab Order</div><span class="sp-select">Most recent ⌄</span></div>
   <div class="sp-field"><div class="sp-label">Theme</div><span class="sp-radio"><span class="on">System</span><span>Dark</span><span>Light</span></span></div>
   <div class="sp-input">/Users/you/orca/workspaces</div>
  </div>
 </figure>
 <figure><figcaption>Update card (Orca's toast) and tooltip</figcaption>
  <div class="sp-toast"><div style="font-weight:600">Update Available</div><div style="margin:8px 0">Orca v1.4.239 is ready.</div>
   <div class="sp-desc" style="margin-bottom:10px">Sessions won't be interrupted.</div><span class="sp-btn default" style="width:100%;justify-content:center;box-sizing:border-box">Update</span></div>
  <span class="sp-tooltip">Add project</span>
 </figure>
</div>"""


SPEC_CSS = """
.spec-grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(320px,1fr)); gap:20px; }
figure { margin:0; padding:16px; background:var(--role-page); border:1px solid var(--base-border); border-radius:var(--radius-xl); color:var(--base-foreground); font-family:var(--fontFamily-sans); font-size:var(--fontSize-sm); }
figcaption { font-size:12px; color:var(--base-muted-foreground); margin-bottom:12px; }
.sp-sidebar { background:var(--worktreeSidebar-default); border-radius:var(--radius-lg); padding:var(--spacing-2); color:var(--worktreeSidebar-foreground); }
.sp-search { height:28px; display:flex; align-items:center; padding:0 10px; border-radius:var(--radius-md); background:var(--worktreeSidebar-accent); margin-bottom:6px; }
.sp-row { display:flex; align-items:center; gap:8px; height:30px; padding:0 8px; border-radius:var(--radius-md); }
.sp-row.hover { background:var(--worktreeSidebar-accent); }
.sp-group { padding:10px 8px 4px; color:var(--base-muted-foreground); font-size:var(--fontSize-sm); }
.sp-ws { padding:8px 10px; border-radius:var(--radius-lg); background:var(--worktreeSidebar-accent); border:1px solid var(--worktreeSidebar-border); }
.sp-muted { color:var(--base-muted-foreground); font-size:var(--fontSize-xs); padding-left:14px; }
.sp-end { margin-left:auto; color:var(--base-muted-foreground); font-size:var(--fontSize-xs); }
.dot { display:inline-block; width:7px; height:7px; border-radius:99px; }
.sp-badge { display:inline-flex; height:18px; align-items:center; padding:0 6px; border-radius:var(--radius-sm); border:1px solid var(--base-border); font-size:var(--fontSize-xs); color:var(--base-foreground); }
.sp-new { margin-left:auto; padding:1px 7px; border-radius:99px; background:var(--base-primary); color:var(--base-primary-foreground); font-size:11px; }
.sp-chat { background:var(--chat-canvas); padding:12px; border-radius:var(--radius-lg); color:var(--chat-foreground); }
.sp-user { margin-left:auto; width:fit-content; max-width:80%; background:var(--component-user-message-bg); border:1px solid var(--component-user-message-border); border-radius:var(--component-user-message-radius); padding:8px 12px; color:var(--component-user-message-text); }
.sp-turn { margin:12px 0 8px; padding-bottom:6px; border-bottom:1px solid var(--base-border); color:var(--chat-foreground-faint); }
.sp-code { background:var(--component-code-block-bg); border:1px solid var(--component-code-block-border); color:var(--chat-code-foreground); border-radius:var(--component-code-block-radius); padding:10px 12px; margin:10px 0; overflow:auto; }
.sp-composer { background:var(--component-composer-bg); border:1px solid var(--component-composer-border); border-radius:var(--component-composer-radius); padding:10px 12px; box-shadow:var(--shadow-composer); }
.sp-toolbar { display:flex; align-items:center; gap:10px; margin-top:18px; color:var(--chat-foreground); }
.sp-send { width:28px; height:28px; border-radius:99px; display:inline-grid; place-items:center; background:var(--base-primary); color:var(--base-primary-foreground); opacity:.5; }
.sp-buttons { display:flex; flex-wrap:wrap; gap:8px; align-items:center; }
.sp-btn { display:inline-flex; align-items:center; height:var(--controlHeight-sm); padding:0 12px; border-radius:var(--radius-md); font-weight:500; border:1px solid transparent; }
.sp-btn.default { background:var(--base-primary); color:var(--base-primary-foreground); }
.sp-btn.default.is-hover { background:var(--role-accent-hover); }
.sp-btn.outline { background:var(--base-background); border-color:var(--base-input); color:var(--base-foreground); box-shadow:0 1px 2px rgba(0,0,0,.05); }
.sp-btn.secondary { background:var(--base-secondary); color:var(--base-secondary-foreground); }
.sp-btn.ghost { color:var(--base-foreground); } .sp-btn.ghost:hover { background:var(--base-accent); }
.sp-btn.destructive { background:var(--component-button-destructive-bg); color:var(--component-button-destructive-text); }
.sp-btn.focus { border-color:var(--base-ring); box-shadow:0 0 0 var(--focusRing-width) color-mix(in srgb, var(--base-ring) 50%, transparent); }
.sp-menu { background:var(--component-menu-bg); color:var(--component-menu-text); border:1px solid var(--component-menu-border); border-radius:var(--component-menu-radius); padding:4px; max-width:240px; box-shadow:var(--shadow-menu); backdrop-filter:blur(var(--blur-xl)); }
.sp-menu hr { border:0; border-top:1px solid var(--component-menu-border); margin:4px -4px; }
.sp-mrow { display:flex; align-items:center; height:var(--component-menu-item-height); padding:0 var(--component-menu-item-padding); border-radius:var(--component-menu-item-radius); }
.sp-mrow.hi { background:var(--component-menu-item-bg-hover); } .sp-mrow.danger { color:var(--base-destructive); }
.sp-scrim { background:var(--component-scrim-bg); padding:24px; border-radius:var(--radius-lg); }
.sp-dialog { background:var(--component-dialog-bg); border:1px solid var(--component-dialog-border); border-radius:var(--component-dialog-radius); padding:20px; box-shadow:var(--shadow-dialog); }
.sp-card { background:var(--base-card); color:var(--base-card-foreground); border:1px solid var(--base-border); border-radius:var(--radius-xl); padding:16px; }
.sp-field { display:flex; align-items:center; justify-content:space-between; gap:12px; padding:8px 0; }
.sp-label { font-weight:500; } .sp-desc { color:var(--base-muted-foreground); font-size:var(--fontSize-xs); }
.sp-switch { flex:none; display:inline-block; width:var(--size-control-switch-width); height:var(--size-control-switch-height); border-radius:99px; background:var(--component-switch-off-bg); position:relative; }
.sp-switch::after { content:""; position:absolute; top:2px; left:2px; width:16px; height:16px; border-radius:99px; background:var(--base-background); }
.sp-switch.on { background:var(--component-switch-on-bg); } .sp-switch.on::after { left:18px; }
.sp-select { border:1px solid var(--base-input); border-radius:var(--radius-md); padding:6px 10px; }
.sp-radio { display:inline-flex; border:1px solid var(--base-border); border-radius:var(--radius-md); padding:2px; } .sp-radio span { padding:3px 10px; border-radius:var(--radius-sm); color:var(--base-muted-foreground); } .sp-radio span.on { background:var(--base-accent); color:var(--base-foreground); font-weight:500; }
.sp-input { margin-top:8px; height:var(--controlHeight-default); display:flex; align-items:center; padding:0 12px; border-radius:var(--radius-md); border:1px solid var(--base-input); }
.sp-toast { background:var(--component-toast-bg); border:1px solid var(--component-toast-border); border-radius:var(--component-toast-radius); padding:14px; box-shadow:var(--shadow-toast); }
.sp-tooltip { display:inline-block; margin-top:14px; background:var(--component-tooltip-bg); color:var(--component-tooltip-text); border-radius:var(--component-tooltip-radius); padding:5px 10px; font-size:var(--fontSize-xs); }
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
sections.append("<h2>Colour roles and theme</h2><p>role.* maps the checklist roles onto Orca's tokens. base.* is shadcn/ui's neutral theme; "
                "the chat colours are the foreground mixed into the canvas (the formula is on each token in tokens.json). Tailwind's palette, "
                "the same in both themes, follows.</p>")
groups = []
for p, _ in light.items():
    if p[0] not in groups:
        groups.append(p[0])
groups.sort(key=lambda g: (GROUP_ORDER.index(g) if g in GROUP_ORDER else 99, g))
sections.append('<div class="scroll">' + "".join(colour_table(g) for g in groups) + "</div>")
palette_rows = "".join(f'<tr><th><code>{esc(".".join(p))}</code></th><td><span class="sw"><i style="background:{esc(t["$value"])}"></i></span><code>{esc(t["$value"])}</code> {ev(t)}</td></tr>'
                       for p, t in core.items() if p[0] == "color")
sections.append(f'<details><summary>color (Tailwind palette, core) <small>{sum(1 for p in core if p[0] == "color")}</small></summary><table class="tok">{palette_rows}</table></details>')
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
