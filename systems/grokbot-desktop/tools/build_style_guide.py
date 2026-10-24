#!/usr/bin/env python3
"""Render style-guide.html from tokens.json.

    python3 tools/build_style_guide.py

Every token becomes a CSS custom property (its path joined with dashes; an alias becomes a var()), so
the swatches, scales and specimens cannot drift from the file. The page starts in the reader's
system theme and has a Light/Dark toggle that sets data-theme on <html>. Specimens are drawn from
tokens only, with the system font (Grok Bot uses it too) and no Grok Bot artwork, Bot characters
or icons. PRODUCT (adapt): NAME, LEDE, GROUP_ORDER and specimens().
Standard library only, deterministic.
"""
import html
import json
import pathlib
import re

PKG = pathlib.Path(__file__).resolve().parent.parent
TOKENS = json.loads((PKG / "tokens.json").read_text())
OUT = PKG / "style-guide.html"

NAME = "Grok Bot desktop"  # PRODUCT (adapt)
LEDE = ("Grok Bot 0.75.5 for macOS (Electron 42, SpaceXAI), read live from the running app over its remote-debugging "
        "port on 2026-10-25, in its Light and Dark themes. Every value below is a token from tokens.json; the specimens are "
        "rebuilt from those tokens, not copied from the app.")  # PRODUCT (adapt)
GROUP_ORDER = ["role", "bg", "text", "border", "icon", "fill", "transcript", "prompt", "activity", "specular", "dataviz", "kit",
               "shadow", "component"]


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
 <figure><figcaption>Sidebar: pinned Bots, groups, a selected Bot row, the footer</figcaption>
  <div class="sp-sidebar">
   <div class="sp-grid"><span class="sp-tile sel"><i style="background:var(--bg-magenta-bright)"></i>Chief</span><span class="sp-tile"><i style="background:var(--bg-orange-bright)"></i>Lead</span><span class="sp-tile"><i style="background:var(--bg-purple-bright)"></i>Ops</span></div>
   <div class="sp-group"><span>Developers</span><span class="sp-end">7</span></div>
   <div class="sp-group hover"><span>Studio</span><span class="sp-end">›</span></div>
   <div class="sp-botrow"><i style="background:var(--bg-magenta-bright)"></i><span><b>Design Capture</b><br><small>A design token is a named value…</small></span></div>
   <div class="sp-foot"><span class="sp-avatar">WC</span><span class="sp-acct">Account</span><span class="sp-icon-btn round">⊞</span></div>
  </div>
 </figure>
 <figure><figcaption>Conversation: the owner's bubble in the Bot's colour, the Bot's reply on a raised bubble, an activity line</figcaption>
  <div class="t-caption" style="text-align:center;color:var(--text-tertiary)">Today 6:41 AM</div>
  <div class="sp-user">List the files in this folder.</div>
  <div class="sp-agent">There's one file in there, <code class="sp-code">hello.txt</code>.</div>
  <div class="sp-activity"><i></i><span>Listing the directory files</span></div>
 </figure>
 <figure><figcaption>Composer: a pill on the raised fill, icon buttons, the voice button in the Bot's colour</figcaption>
  <div class="sp-composer"><span class="sp-icon-btn round">+</span><span class="t-prompt" style="flex:1;color:var(--text-tertiary)">Message Design Capture</span><span class="sp-icon-btn round">♪</span><span class="sp-voice"></span></div>
 </figure>
 <figure><figcaption>Buttons: ink primary, secondary, danger, disabled, and the focus ring a Tab press turns on</figcaption>
  <div class="sp-buttons">
   <span class="sp-btn primary">Create</span><span class="sp-btn secondary">Cancel</span><span class="sp-btn danger">Delete</span>
   <span class="sp-btn primary disabled">Create</span><span class="sp-btn secondary focus">Focus ring</span>
  </div>
 </figure>
 <figure><figcaption>Menu (raised, 12px; 30px rows with a 6px radius)</figcaption>
  <div class="sp-menu"><div class="sp-mrow">Weekly usage <span class="sp-end">0% used ›</span></div><div class="sp-mrow hi">Settings</div><hr><div class="sp-mrow">Add account</div><div class="sp-mrow danger">Delete</div></div>
 </figure>
 <figure><figcaption>Confirmation over the scrim</figcaption>
  <div class="sp-scrim"><div class="sp-dialog"><div class="t-heading">Delete “Design Capture”</div>
   <div class="t-body" style="color:var(--text-secondary)">This permanently deletes the Bot and its chat history.</div>
   <div style="display:flex;gap:8px;margin-top:14px"><span class="sp-btn secondary" style="flex:1">Cancel</span><span class="sp-btn danger" style="flex:1">Delete</span></div></div></div>
 </figure>
 <figure><figcaption>Settings: a grouped card of rows with a select and a switch</figcaption>
  <div class="sp-group-card">
   <div class="sp-field"><span class="t-label">Theme</span><span class="sp-select">Follow System ⌄</span></div>
   <div class="sp-field"><span class="t-label">Check Spelling While Typing</span><span class="sp-switch on"></span></div>
   <div class="sp-field"><span class="t-label">Automatic Updates</span><span class="sp-switch"></span></div>
  </div>
 </figure>
</div>"""


SPEC_CSS = """
.spec-grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(300px,1fr)); gap:20px; }
figure { margin:0; padding:16px; background:var(--role-page); border:1px solid var(--role-border-subtle); border-radius:var(--radius-xl); color:var(--text-primary); font-family:var(--fontFamily-sans); font-size:var(--fontSize-base); font-weight:var(--fontWeight-regular); min-width:0; }
figcaption { font-size:12px; color:var(--text-tertiary); margin-bottom:12px; }
.sp-sidebar { background:var(--role-surface); border-radius:var(--radius-lg); padding:var(--spacing-2); }
.sp-grid { display:flex; gap:4px; margin-bottom:8px; }
.sp-tile { flex:1; display:flex; flex-direction:column; align-items:center; gap:4px; padding:8px 0; border-radius:var(--botItem-radius); font-size:var(--fontSize-sm); }
.sp-tile i { width:32px; height:32px; border-radius:40%; }
.sp-tile.sel { background:var(--bg-secondary-hover); }
.sp-group { display:flex; align-items:center; height:30px; padding:0 8px; border-radius:var(--radius-base); color:var(--text-secondary); }
.sp-group.hover { background:var(--bg-secondary); color:var(--text-primary); }
.sp-botrow { display:flex; gap:8px; align-items:center; padding:8px; border-radius:var(--botItem-radius); background:var(--bg-secondary-hover); }
.sp-botrow i { width:28px; height:28px; border-radius:40%; flex:none; } .sp-botrow small { color:var(--text-secondary); }
.sp-end { margin-left:auto; color:var(--text-tertiary); }
.sp-foot { display:flex; align-items:center; gap:8px; padding:8px 0 0; }
.sp-acct { flex:1; height:32px; display:flex; align-items:center; padding:0 10px; border-radius:99px; background:var(--bg-secondary); }
.sp-avatar { width:28px; height:28px; border-radius:99px; display:grid; place-items:center; font-size:11px; color:var(--text-secondary); background:var(--bg-secondary); }
.sp-icon-btn { width:28px; height:28px; border-radius:var(--radius-base); display:inline-grid; place-items:center; color:var(--icon-secondary); background:var(--bg-secondary); flex:none; }
.sp-icon-btn.round { border-radius:99px; }
.sp-user { margin:10px 0 8px auto; width:fit-content; max-width:80%; background:var(--fill-magenta-bubble-user); color:var(--transcript-bubble-user-text); border-radius:var(--transcript-bubble-radius); padding:7px 12px; }
.sp-agent { width:fit-content; max-width:85%; background:var(--transcript-bubble-agent-fill); border-radius:var(--transcript-bubble-radius); padding:7px 12px; line-height:var(--transcript-line-height); }
.sp-code { font-family:var(--fontFamily-mono); background:var(--bg-secondary); border-radius:4px; padding:1px 4px; }
.sp-activity { display:flex; align-items:center; gap:8px; margin-top:10px; color:var(--text-tertiary); }
.sp-activity i { width:16px; height:16px; border-radius:40%; background:var(--bg-magenta-bright); }
.sp-composer { display:flex; align-items:center; gap:8px; background:var(--component-composer-bg); border:1px solid var(--component-composer-border); border-radius:var(--component-composer-radius); padding:6px; }
.sp-voice { width:28px; height:28px; border-radius:99px; background:var(--bg-magenta-bright); flex:none; }
.sp-buttons { display:flex; flex-wrap:wrap; gap:8px; align-items:center; }
.sp-btn { display:inline-flex; align-items:center; justify-content:center; height:var(--size-control-button); padding:0 14px; border-radius:99px; font-weight:var(--fontWeight-medium); border:1px solid transparent; }
.sp-btn.primary { background:var(--bg-primary); color:var(--text-on-primary); }
.sp-btn.primary.disabled { background:var(--bg-primary-disabled); color:var(--text-quaternary); }
.sp-btn.secondary { background:var(--component-button-secondary-bg); color:var(--component-button-secondary-text); border-color:var(--role-border-default); }
.sp-btn.danger { background:var(--component-button-danger-bg); color:var(--component-button-danger-text); }
.sp-btn.focus { outline:var(--focusRing-width) solid var(--role-border-focus); outline-offset:var(--focusRing-offset); }
.sp-menu { background:var(--component-menu-bg); border:1px solid var(--role-border-subtle); border-radius:var(--menu-radius); padding:4px; max-width:240px; }
.sp-menu hr { border:0; border-top:1px solid var(--role-border-subtle); margin:4px 8px; }
.sp-mrow { display:flex; align-items:center; height:var(--menu-row-height); padding:0 8px; border-radius:var(--menu-row-radius); }
.sp-mrow.hi { background:var(--bg-secondary-hover); } .sp-mrow.danger { color:var(--text-danger-primary); }
.sp-switch { display:inline-block; width:32px; height:20px; border-radius:99px; background:var(--bg-secondary-active); position:relative; }
.sp-switch::after { content:""; position:absolute; top:2px; left:2px; width:16px; height:16px; border-radius:99px; background:#fff; }
.sp-switch.on { background:var(--component-switch-on-bg); } .sp-switch.on::after { left:14px; }
.sp-scrim { background:var(--role-scrim); padding:24px; border-radius:var(--radius-lg); }
.sp-dialog { background:var(--component-confirm-dialog-bg); border-radius:var(--component-confirm-dialog-radius); padding:16px; }
.sp-group-card { border-radius:var(--radius-xl); background:var(--bg-elevated); padding:4px 0; }
.sp-field { display:flex; align-items:center; justify-content:space-between; gap:8px; padding:10px 14px; }
.sp-select { border:1px solid var(--role-border-default); border-radius:var(--radius-base); padding:3px 8px; color:var(--text-primary); white-space:nowrap; }
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
table.tok { border-collapse:collapse; width:100%; font-size:12px; } table.tok th, table.tok td { text-align:left; padding:4px 8px; border-bottom:1px solid var(--role-border-subtle); vertical-align:middle; }
.sw { display:inline-block; width:22px; height:16px; border-radius:4px; vertical-align:middle; margin-right:6px; background-image:linear-gradient(45deg,#ccc 25%,transparent 25%,transparent 75%,#ccc 75%),linear-gradient(45deg,#ccc 25%,#fff 25%,#fff 75%,#ccc 75%); background-size:8px 8px; background-position:0 0,4px 4px; overflow:hidden; }
.sw i { display:block; width:100%; height:100%; }
code { font-family:ui-monospace, Menlo, monospace; font-size:11px; }
.ev { font-size:10px; padding:1px 5px; border-radius:99px; background:var(--bg-secondary); color:var(--text-secondary); white-space:nowrap; }
.ev-derived { background:var(--bg-accent-secondary); }
.bar { display:inline-block; height:10px; background:var(--role-accent-default); border-radius:2px; vertical-align:middle; }
.rad { display:inline-block; width:40px; height:24px; border:1px solid var(--role-border-strong); background:var(--bg-secondary); vertical-align:middle; }
.shadow-box { display:inline-block; width:80px; height:36px; background:var(--role-raised); border-radius:8px; vertical-align:middle; }
"""

sections = []
sections.append("<h2>Colour roles and seeds</h2><p>role.* maps the checklist roles onto Grok Bot's sand tokens. Sand is a flat list of literal colours per theme; "
                "kit.* is the anysphere-ui layer underneath, mostly pointing back at sand.</p>")
groups = []
for p, _ in light.items():
    if p[0] not in groups:
        groups.append(p[0])
groups.sort(key=lambda g: (GROUP_ORDER.index(g) if g in GROUP_ORDER else 99, g))
sections.append('<div class="scroll">' + "".join(colour_table(g) for g in groups) + "</div>")
sections.append("<h2>Type</h2>" + "".join(
    f'<div style="margin:8px 0"><div class="t-{p[-1]}">{esc(p[-1].capitalize())}: The Bot listed the files in this folder</div>'
    f'<code>{esc(json.dumps(t["$value"]))}</code> {ev(t)}</div>' for p, t in core.items() if t["$type"] == "typography"))
sections.append("<h2>Radius</h2>" + scale_rows("radius", lambda p, t: f'<span class="rad" style="border-radius:{t["$value"]}"></span>'))
sections.append("<h2>Spacing</h2>" + scale_rows("spacing", lambda p, t: f'<span class="bar" style="width:{t["$value"]}"></span>'))
sections.append("<h2>Control heights, sizes and layout</h2>" + scale_rows("controlHeight", lambda p, t: f'<span class="bar" style="width:{t["$value"]}"></span>')
                + scale_rows("size", lambda p, t: "") + scale_rows("layout", lambda p, t: "") + scale_rows("focusRing", lambda p, t: "")
                + scale_rows("zIndex", lambda p, t: "") + scale_rows("borderWidth", lambda p, t: "")
                + "".join(scale_rows(g, lambda p, t: "") for g in ("menu", "searchMenu", "palette", "newChatMenu", "botItem", "transcript", "tooltip", "blur", "press", "zoom")))
shadow_rows = "".join(f"<tr><th><code>{esc('.'.join(p))}</code></th><td><span class=\"shadow-box\" style=\"box-shadow:var({var(p)})\"></span></td><td>{ev(t)}</td></tr>"
                      for p, t in light.items() if p[0] == "shadow" and t["$type"] == "shadow")
sections.append(f'<h2>Elevation</h2><table class="tok">{shadow_rows}</table>')
sections.append("<h2>Motion</h2>" + scale_rows("duration", lambda p, t: ""))
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
