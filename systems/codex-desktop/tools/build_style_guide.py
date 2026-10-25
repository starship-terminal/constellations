#!/usr/bin/env python3
"""Render style-guide.html from tokens.json.

    python3 tools/build_style_guide.py

Every token becomes a CSS custom property (its path joined with dashes; an alias becomes a var()), so
the swatches, scales and specimens cannot drift from the file. The page starts in the reader's
system theme and has a Light/Dark toggle that sets data-theme on <html>. Specimens are drawn from
tokens only, in the system font and with no Codex artwork or icons. PRODUCT (adapt): NAME, LEDE, GROUP_ORDER, specimens(),
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

NAME = "Codex desktop"  # PRODUCT (adapt)
LEDE = ("Codex 26.1013 for macOS (OpenAI's desktop app, an Electron build on Chromium 155), read live from the running app over its "
        "remote-debugging port on 2026-10-25, in the owner's two themes: Absolutely (dark) and Catppuccin (light). Every value below is "
        "a token from tokens.json; the specimens are rebuilt from those tokens in the system font, not copied from the app.")  # PRODUCT (adapt)
GROUP_ORDER = ["role", "seed", "token", "bg", "text", "border", "ring", "app", "codex", "chat", "content", "surface", "alpha", "gray",
               "grayFixed", "neutral", "chart", "misc", "kit", "shadow", "component"]


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
 <figure><figcaption>Sidebar: new chat, projects, a selected chat</figcaption>
  <div class="sp-sidebar">
   <div class="sp-row">New chat</div>
   <div class="sp-group">Projects</div>
   <div class="sp-row sel">design-capture</div>
   <div class="sp-row" style="padding-left:28px">List folder files</div>
   <div class="sp-row hover">downloads</div>
   <div class="sp-group">Recents</div>
   <div class="sp-row">grafana</div>
  </div>
 </figure>
 <figure><figcaption>Chat: prompt bubble, folded work, reply with inline code, composer</figcaption>
  <div class="sp-chat">
   <div class="sp-user">Create hello.txt here with one line</div>
   <div class="sp-turn">Worked for 4s ›</div>
   <div class="t-body">Created <span class="sp-mention">hello.txt</span> with one line: <code class="sp-code">hello from the design capture</code>.</div>
   <div class="sp-composer"><div style="color:var(--text-tertiary)">Work with Codex</div>
    <div class="sp-toolbar"><span>+</span><span style="color:var(--text-warning)">Full access</span><span style="flex:1"></span><span>GPT-6 Astra <span style="color:var(--text-tertiary)">Light</span></span><span class="sp-send">●</span></div></div>
  </div>
 </figure>
 <figure><figcaption>Buttons: primary (ink), secondary, ghost, danger; focus ring</figcaption>
  <div class="sp-buttons">
   <span class="sp-btn primary">Create project</span><span class="sp-btn secondary">Change</span><span class="sp-btn ghost">Cancel</span>
   <span class="sp-btn danger">Remove project</span><span class="sp-btn secondary focus">Focus ring</span>
  </div>
 </figure>
 <figure><figcaption>Menu</figcaption>
  <div class="sp-menu"><div class="sp-mrow">Rename <span class="sp-end">⌥⌘R</span></div><div class="sp-mrow hi">Pin</div><div class="sp-mrow">Fork ›</div><hr><div class="sp-mrow">Archive <span class="sp-end">⇧⌘A</span></div></div>
 </figure>
 <figure><figcaption>Confirmation dialog (no scrim)</figcaption>
  <div class="sp-dialog"><div style="font-weight:600;font-size:18px">Remove design-capture?</div>
   <div style="color:var(--text-secondary);margin-top:6px">This only removes the project from the app. Files on your computer and existing chats won't be deleted.</div>
   <div style="display:flex;gap:8px;justify-content:flex-end;margin-top:16px"><span class="sp-btn ghost">Cancel</span><span class="sp-btn danger">Remove project</span></div></div>
 </figure>
 <figure><figcaption>Settings card: rows, switches, select</figcaption>
  <div class="sp-card">
   <div class="sp-field"><div><div class="sp-label">Prevent sleep while running</div><div class="sp-desc">Keep your computer awake while a task runs</div></div><span class="sp-switch on"></span></div>
   <div class="sp-field"><div><div class="sp-label">Show in menu bar</div></div><span class="sp-switch"></span></div>
   <div class="sp-field"><div><div class="sp-label">Default file open destination</div></div><span class="sp-select">Zed ⌄</span></div>
  </div>
 </figure>
 <figure><figcaption>Tooltip and settings search</figcaption>
  <span class="sp-tooltip">Search <span style="color:var(--text-tertiary)">⌘K</span></span>
  <div class="sp-search">Search</div>
 </figure>
</div>"""


SPEC_CSS = """
.spec-grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(320px,1fr)); gap:20px; }
figure { margin:0; padding:16px; background:var(--role-page); border:1px solid var(--role-border-default); border-radius:var(--radius-xl); color:var(--role-text-primary); font-family:var(--fontFamily-sans); font-size:var(--fontSize-ui); }
figcaption { font-size:12px; color:var(--role-text-secondary); margin-bottom:12px; }
.sp-sidebar { background:var(--role-surface); border-radius:var(--radius-lg); padding:8px; }
.sp-row { display:flex; align-items:center; height:var(--component-project-row-height); padding:0 10px; border-radius:var(--radius-row); color:var(--component-thread-row-text); }
.sp-row.sel { background:var(--component-project-row-selected-bg); } .sp-row.hover { background:var(--component-project-row-bg-hover); }
.sp-group { padding:12px 10px 4px; color:var(--text-tertiary); }
.sp-chat { padding:4px; }
.sp-user { margin-left:auto; width:fit-content; max-width:80%; background:var(--component-user-message-bg); color:var(--component-user-message-text); border-radius:var(--component-user-message-radius); padding:10px var(--component-user-message-padding); }
.sp-turn { margin:14px 0 8px; padding-bottom:8px; border-bottom:1px solid var(--role-border-default); color:var(--text-tertiary); }
.sp-mention { color:var(--component-file-mention-text); }
.sp-code { font-family:var(--fontFamily-mono); font-size:var(--fontSize-chat-code); background:var(--component-inline-code-bg); border-radius:var(--component-inline-code-radius); padding:1px 5px; }
.sp-composer { margin-top:16px; background:var(--component-composer-bg); border:1px solid var(--component-composer-border, transparent); border-radius:var(--component-composer-radius); padding:12px 14px; box-shadow:var(--shadow-sm); }
.sp-toolbar { display:flex; align-items:center; gap:12px; margin-top:18px; color:var(--text-secondary); }
.sp-send { width:var(--component-voice-button-size); height:var(--component-voice-button-size); border-radius:99px; display:inline-grid; place-items:center; background:var(--component-voice-button-bg); color:var(--role-page); font-size:10px; }
.sp-buttons { display:flex; flex-wrap:wrap; gap:8px; align-items:center; }
.sp-btn { display:inline-flex; align-items:center; height:var(--component-button-primary-height); padding:0 14px; border-radius:var(--component-button-primary-radius); font-weight:500; }
.sp-btn.primary { background:var(--component-button-primary-bg); color:var(--component-button-primary-text); }
.sp-btn.secondary { background:var(--component-button-secondary-bg); color:var(--component-button-secondary-text); height:var(--component-button-secondary-height); }
.sp-btn.ghost { color:var(--component-button-ghost-text); }
.sp-btn.danger { background:var(--component-button-danger-bg); color:var(--component-button-danger-text); }
.sp-btn.focus { box-shadow:0 0 0 var(--focusRing-width) var(--role-border-focus); }
.sp-menu { background:var(--component-menu-bg); color:var(--component-menu-text); border-radius:var(--component-menu-radius); padding:6px; max-width:240px; box-shadow:var(--shadow-menu-box-shadow); }
.sp-menu hr { border:0; border-top:1px solid var(--role-border-default); margin:4px 6px; }
.sp-mrow { display:flex; align-items:center; height:var(--component-menu-row-height); padding:0 var(--component-menu-row-padding); border-radius:var(--component-menu-row-radius); font-size:var(--fontSize-menu); }
.sp-mrow.hi { background:var(--component-menu-row-bg-hover); } .sp-end { margin-left:auto; color:var(--text-tertiary); font-size:12px; }
.sp-dialog { background:var(--component-dialog-bg); border-radius:var(--component-dialog-radius); padding:20px; box-shadow:var(--shadow-dialog-backdrop-fade-shadow); }
.sp-card { background:var(--component-settings-card-bg); border:1px solid var(--component-settings-card-border); border-radius:var(--component-settings-card-radius); padding:4px 16px; }
.sp-field { display:flex; align-items:center; justify-content:space-between; gap:12px; padding:12px 0; border-bottom:1px solid var(--role-border-default); } .sp-field:last-child { border-bottom:0; }
.sp-label { font-weight:500; } .sp-desc { color:var(--role-text-secondary); font-size:var(--fontSize-text-xs); }
.sp-switch { flex:none; display:inline-block; width:var(--size-switch-track-width); height:var(--size-switch-track); border-radius:99px; background:var(--component-switch-off-bg); position:relative; }
.sp-switch::after { content:""; position:absolute; top:3px; left:3px; width:var(--size-switch-thumb); height:var(--size-switch-thumb); border-radius:99px; background:#fff; box-shadow:var(--shadow-switch-thumb-shadow); }
.sp-switch.on { background:var(--component-switch-on-bg); } .sp-switch.on::after { left:16px; }
.sp-select { background:var(--component-select-bg); border:1px solid var(--component-select-border); border-radius:var(--component-select-radius); padding:4px 10px; }
.sp-tooltip { display:inline-block; background:var(--component-tooltip-bg); color:var(--component-tooltip-text); border-radius:var(--component-tooltip-radius); padding:5px 12px; font-size:var(--fontSize-tooltip); box-shadow:var(--shadow-tooltip); }
.sp-search { margin-top:16px; height:var(--component-settings-search-height); display:flex; align-items:center; padding:0 14px; border-radius:var(--radius-full); background:var(--component-settings-search-bg); color:var(--text-tertiary); }
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
sections.append("<h2>Colour roles and theme</h2><p>role.* maps the checklist roles onto Codex's tokens. seed.* is the four theme inputs "
                "(surface, ink, accent; contrast is in core); almost every other colour is a formula over them, kept on each token in tokens.json. "
                "The hue palettes, the same in both themes, follow.</p>")
groups = []
for p, _ in light.items():
    if p[0] not in groups:
        groups.append(p[0])
groups.sort(key=lambda g: (GROUP_ORDER.index(g) if g in GROUP_ORDER else 99, g))
sections.append('<div class="scroll">' + "".join(colour_table(g) for g in groups) + "</div>")
palette_rows = "".join(f'<tr><th><code>{esc(".".join(p))}</code></th><td><span class="sw"><i style="background:{esc(t["$value"])}"></i></span><code>{esc(t["$value"])}</code> {ev(t)}</td></tr>'
                       for p, t in core.items() if p[0] == "color")
sections.append(f'<details><summary>color (hue palettes, core) <small>{sum(1 for p in core if p[0] == "color")}</small></summary><table class="tok">{palette_rows}</table></details>')
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
