#!/usr/bin/env python3
"""Render style-guide.html from tokens.json.

    python3 tools/build_style_guide.py

Every token becomes a CSS custom property (its path joined with dashes; an alias becomes a var()), so
the swatches, scales and specimens cannot drift from the file. The page starts in the reader's
system theme and has a Light/Dark toggle that sets data-theme on <html>. Specimens are drawn from
tokens only, with the families the tokens name (Inter and IBM Plex Mono when installed, else the
system fallbacks; no font file is shipped) and no OpenCode artwork, wordmark or icons.
PRODUCT (adapt): NAME, LEDE, GROUP_ORDER, specimens(), SPEC_CSS and the section texts.
Standard library only, deterministic.
"""
import html
import json
import pathlib
import re

PKG = pathlib.Path(__file__).resolve().parent.parent
TOKENS = json.loads((PKG / "tokens.json").read_text())
OUT = PKG / "style-guide.html"

NAME = "OpenCode desktop"  # PRODUCT (adapt)
LEDE = ("OpenCode 2.1.4 for macOS (Electron 44, Anomaly), read live from the running app over its remote-debugging "
        "port on 2026-10-25, in its OpenCode theme, light and dark. Every value below is a token from tokens.json; the "
        "specimens are rebuilt from those tokens, not copied from the app.")  # PRODUCT (adapt)
GROUP_ORDER = ["role", "bg", "text", "border", "icon", "overlay", "state", "agent", "avatar", "illustration", "syntax", "markdown",
               "legacy", "shadow", "component"]


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
    open_ = " open" if group in ("role",) else ""
    return (f'<details{open_}><summary>{esc(group)} <small>{len(rows)}</small></summary><table class="tok"><thead><tr><th>Token</th>'
            f'<th>Light</th><th>Dark</th></tr></thead><tbody>{"".join(rows)}</tbody></table></details>')


def ramps():  # PRODUCT (adapt): OpenCode's ramps are core colours, the same in both schemes
    out = []
    names = []
    for p, t in core.items():
        if p[0] == "color" and p[1:2] not in [(n,) for n in names]:
            names.append(p[1])
    # neutral first, the hues in hue order, the translucent steps last; each ramp light to dark
    order = ["grey", "red", "orange", "yellow", "green", "cyan", "blue", "purple", "pink", "alpha"]
    names.sort(key=lambda n: order.index(n) if n in order else len(order))
    step = lambda p: [int(x) if x.isdigit() else x for x in p[2:]]
    for name in names:
        steps = sorted(((p, t) for p, t in core.items() if p[:2] == ("color", name) and t["$type"] == "color"), key=lambda pt: step(pt[0]))
        cells = "".join(f'<span class="ramp-step" title="{esc(".".join(p))} {esc(t["$value"])}"><i style="background:{esc(t["$value"])}"></i>'
                        f'<code>{esc(".".join(p[2:]))}</code></span>' for p, t in steps)
        out.append(f'<div class="ramp"><code class="ramp-name">color.{esc(name)}</code>{cells}</div>')
    return "".join(out)


def scale_rows(group, render):
    rows = []
    for p, t in core.items():
        if p[0] == group:
            rows.append(f"<tr><th><code>{esc('.'.join(p))}</code></th><td>{render(p, t)}</td><td><code>{esc(json.dumps(t['$value']) if not isinstance(t['$value'], str) else t['$value'])}</code> {ev(t)}</td></tr>")
    return f'<table class="tok">{"".join(rows)}</table>'


def specimens():  # PRODUCT (adapt)
    return """
<div class="spec-grid">
 <figure><figcaption>Title bar: Home, session tabs on the deep window colour, the selected tab raised</figcaption>
  <div class="sp-titlebar"><span class="sp-icon-btn sel">⊞</span><span class="sp-tab"><i>O</i>List folder files</span><span class="sp-tab active"><i>O</i>Contents of hello.txt<b>×</b></span><span class="sp-icon-btn">+</span></div>
 </figure>
 <figure><figcaption>Home: the project list (selected row on a layer fill), sessions as rows with the project name muted</figcaption>
  <div class="sp-home">
   <div class="sp-col"><div class="sp-label">Projects</div><div class="sp-row sel"><i>O</i>opencode</div><div class="sp-row"><i>C</i>cache-simulator</div><div class="sp-row"><i>D</i>Default Project</div></div>
   <div class="sp-col"><div class="sp-label">Today</div><div class="sp-srow"><i>O</i><b>Contents of hello.txt</b> <span>opencode</span></div><div class="sp-srow hover"><i>O</i><b>List folder files</b> <span>opencode</span></div></div>
  </div>
 </figure>
 <figure><figcaption>Conversation: the owner's prompt in blue on a faint blue bubble; the reply on the page; a tool summary; code</figcaption>
  <div class="sp-user">Create hello.txt here with one line</div>
  <div class="t-tool sp-tool">Used <b>1</b> Write</div>
  <div class="t-body">Created <span class="sp-link">hello.txt</span> with the line <code class="sp-code">hello from the design capture</code>.</div>
  <pre class="sp-block">:root {
  --surface-raised: #ffffff;
}</pre>
 </figure>
 <figure><figcaption>Composer: a raised card with the floating ring, the model button and the ink Send button</figcaption>
  <div class="sp-composer"><div class="t-prompt" style="color:var(--text-faint)">Ask anything, / for commands, @ for context...</div>
   <div class="sp-cbar"><span class="sp-icon-btn">+</span><span class="sp-pill">MiniMax-M3 ⌄</span><span class="sp-pill">Default ⌄</span><span class="sp-send empty">↑</span></div></div>
 </figure>
 <figure><figcaption>Buttons: neutral, secondary, danger (red text, not a red fill), the contrast Send, and the focus outline</figcaption>
  <div class="sp-buttons">
   <span class="sp-btn neutral">✎ New session</span><span class="sp-btn secondary">Cancel</span><span class="sp-btn danger">Delete session</span>
   <span class="sp-send">↑</span><span class="sp-btn secondary focus">Focus</span>
  </div>
 </figure>
 <figure><figcaption>Menu (floating shadow, 6px; 28px rows with a 4px radius, a group label and a tag)</figcaption>
  <div class="sp-menu"><div class="sp-mlabel">OpenCode</div><div class="sp-mrow hi">Beam Free <span class="sp-tag">Free</span></div><div class="sp-mrow">DeepSeek V4.1 Flash Free <span class="sp-tag">Free</span></div><hr><div class="sp-mrow">Manage models</div></div>
 </figure>
 <figure><figcaption>Confirmation over the scrim: the destructive action is a neutral button with red text</figcaption>
  <div class="sp-scrim"><div class="sp-dialog"><div class="t-title">Delete session</div>
   <div class="t-ui" style="color:var(--text-muted)">Delete session "List folder files"?</div>
   <div style="display:flex;gap:8px;margin-top:14px;justify-content:flex-end"><span class="sp-btn secondary">Cancel</span><span class="sp-btn danger">Delete session</span></div></div></div>
 </figure>
 <figure><figcaption>Settings: a group of rows on layer-01 with a hairline ring, a select and a switch</figcaption>
  <div class="sp-group-card">
   <div class="sp-field"><span><b class="t-ui">Tabs</b><br><small>Choose how session tabs are arranged</small></span><span class="sp-select">Horizontal ⌄</span></div>
   <div class="sp-field"><span><b class="t-ui">Auto-accept permissions</b><br><small>Approve permission requests without asking</small></span><span class="sp-switch"></span></div>
   <div class="sp-field"><span><b class="t-ui">Agent</b><br><small>Show system notification when the agent is complete</small></span><span class="sp-switch on"></span></div>
  </div>
 </figure>
</div>"""


SPEC_CSS = """
.spec-grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(300px,1fr)); gap:20px; }
figure { margin:0; padding:16px; background:var(--role-page); border:1px solid var(--role-border-subtle); border-radius:var(--radius-lg); color:var(--text-base); font-family:var(--fontFamily-sans); font-size:var(--fontSize-small); font-weight:var(--fontWeight-ui); min-width:0; }
figcaption { font-size:12px; color:var(--text-faint); margin-bottom:12px; }
.sp-titlebar { display:flex; align-items:center; gap:6px; background:var(--role-surface); padding:4px 8px; border-radius:var(--radius-md); overflow:hidden; }
.sp-tab { display:inline-flex; align-items:center; gap:6px; height:var(--size-control-session-tab); padding:0 8px; border-radius:var(--radius-measured-6); color:var(--text-muted); white-space:nowrap; }
.sp-tab.active { background:var(--bg-layer-01); color:var(--text-base); } .sp-tab b { font-weight:400; color:var(--text-faint); margin-left:4px; }
.sp-tab i, .sp-row i, .sp-srow i { font-style:normal; width:16px; height:16px; border-radius:4px; display:inline-grid; place-items:center; font-size:10px; background:var(--avatar-bg-gray); color:var(--avatar-fg); flex:none; }
.sp-icon-btn { width:var(--size-control-icon-button); height:var(--size-control-icon-button); border-radius:var(--component-icon-button-radius); display:inline-grid; place-items:center; color:var(--icon-base); flex:none; }
.sp-icon-btn.sel { background:var(--component-icon-button-selected-bg); color:var(--component-icon-button-selected-text); }
.sp-home { display:flex; gap:16px; } .sp-col { flex:1; min-width:0; }
.sp-label { color:var(--text-muted); font-weight:var(--fontWeight-label); margin:0 0 6px 6px; }
.sp-row { display:flex; align-items:center; gap:8px; height:var(--size-control-project-row); padding:0 6px; border-radius:var(--radius-measured-6); color:var(--component-project-row-text); }
.sp-row.sel { background:var(--bg-layer-03); color:var(--text-base); }
.sp-srow { display:flex; align-items:center; gap:6px; height:var(--size-control-session-row); padding:0 8px; border-radius:var(--radius-measured-6); white-space:nowrap; overflow:hidden; }
.sp-srow b { font-weight:var(--fontWeight-label); } .sp-srow span { color:var(--text-muted); } .sp-srow.hover { background:var(--component-session-row-bg-hover); }
.sp-user { margin:4px 0 10px auto; width:fit-content; max-width:85%; background:var(--role-accent-subtle); color:var(--text-accent); border-radius:var(--radius-measured-8); padding:8px 12px; }
.sp-tool { color:var(--text-muted); margin:6px 0; } .sp-tool b { color:var(--text-base); font-weight:var(--fontWeight-medium); }
.sp-link { color:var(--text-accent); }
.sp-code { font-family:var(--fontFamily-mono); color:var(--component-inline-code-text); background:var(--bg-layer-02); border-radius:var(--component-inline-code-radius); padding:1px 4px; font-size:13px; }
.sp-block { font-family:var(--fontFamily-mono); font-size:12px; line-height:1.6; color:var(--syntax-variable); background:var(--bg-base); border:0.5px solid var(--border-base); border-radius:var(--radius-measured-6); padding:10px 12px; margin:10px 0 0; overflow:auto; }
.sp-composer { background:var(--component-composer-bg); border-radius:var(--component-composer-radius); box-shadow:var(--shadow-raised); padding:12px 8px 8px 16px; }
.sp-cbar { display:flex; align-items:center; gap:4px; margin:16px 0 0 -8px; }
.sp-pill { height:var(--size-control-button); padding:0 10px; display:inline-flex; align-items:center; border-radius:var(--radius-measured-6); color:var(--component-model-button-text); }
.sp-send { margin-left:auto; width:28px; height:28px; border-radius:var(--component-send-button-radius); display:inline-grid; place-items:center; background:linear-gradient(var(--component-send-button-highlight), transparent), var(--component-send-button-bg); color:var(--component-send-button-text); box-shadow:var(--shadow-button-contrast); opacity:var(--component-send-button-opacity-filled); flex:none; }
.sp-send.empty { opacity:var(--component-send-button-opacity-empty); }
.sp-buttons { display:flex; flex-wrap:wrap; gap:8px; align-items:center; } .sp-buttons .sp-send { margin-left:0; }
.sp-btn { display:inline-flex; align-items:center; justify-content:center; gap:6px; height:var(--size-control-button); padding:0 var(--component-button-secondary-padding); border-radius:var(--radius-measured-6); font-weight:var(--fontWeight-label); }
.sp-btn.neutral { color:var(--component-button-neutral-text); padding:0 var(--component-button-neutral-padding); }
.sp-btn.neutral:hover, .sp-btn.secondary:hover { background:var(--component-button-secondary-bg-hover); }
.sp-btn.secondary { color:var(--component-button-secondary-text); }
.sp-btn.danger { background:var(--component-button-danger-bg); color:var(--component-button-danger-text); box-shadow:var(--shadow-button-neutral); }
.sp-btn.focus { outline:var(--focusRing-width) solid var(--role-border-focus); outline-offset:var(--focusRing-offset); }
.sp-menu { background:var(--component-menu-bg); box-shadow:var(--shadow-floating); border-radius:var(--component-menu-radius); padding:2px; max-width:260px; }
.sp-menu hr { border:0; border-top:0.5px solid var(--border-base); margin:2px 6px; }
.sp-mlabel { font-size:11px; font-weight:var(--fontWeight-label); color:var(--component-menu-group-label-text); padding:6px 10px 2px; }
.sp-mrow { display:flex; align-items:center; gap:6px; height:var(--component-menu-row-height); padding:0 var(--component-menu-row-padding); border-radius:var(--component-menu-row-radius); color:var(--component-menu-row-text); }
.sp-mrow.hi { background:var(--component-menu-row-bg-hover); }
.sp-tag { font-size:11px; font-weight:var(--fontWeight-label); height:var(--component-tag-height); padding:0 4px; display:inline-flex; align-items:center; border-radius:var(--component-tag-radius); background:var(--component-tag-bg); color:var(--component-tag-text); border:0.5px solid var(--component-tag-border); }
.sp-switch { display:inline-block; width:var(--component-switch-width); height:var(--component-switch-height); border-radius:5px; background:var(--bg-layer-04); box-shadow:var(--shadow-switch-off); position:relative; flex:none; }
.sp-switch::after { content:""; position:absolute; top:2px; left:2px; width:12px; height:12px; border-radius:4px; background:#fff; }
.sp-switch.on { background:var(--bg-accent); box-shadow:var(--shadow-switch-on); } .sp-switch.on::after { left:10px; }
.sp-scrim { background:var(--role-scrim); padding:24px; border-radius:var(--radius-lg); }
.sp-dialog { background:var(--bg-layer-01); box-shadow:var(--shadow-overlay); border-radius:var(--radius-measured-10); padding:16px; }
.sp-group-card { border-radius:var(--component-settings-list-radius); background:var(--component-settings-list-bg); box-shadow:inset 0 0 0 0.5px var(--border-muted); padding:0 14px; }
.sp-field { display:flex; align-items:center; justify-content:space-between; gap:8px; padding:12px 0; border-bottom:0.5px solid var(--border-muted); }
.sp-field:last-child { border-bottom:0; } .sp-field small { color:var(--text-muted); }
.sp-select { padding:2px 8px; border-radius:var(--component-select-radius); color:var(--text-base); white-space:nowrap; }
"""

PAGE_CSS = """
:root { color-scheme: light dark; }
html[data-theme="dark"] { color-scheme: dark; }
body { margin:0; background:var(--role-surface); color:var(--text-base); font:13px/1.45 var(--fontFamily-sans); }
main { max-width:1180px; margin:0 auto; padding:24px 16px 64px; }
header { display:flex; gap:16px; align-items:flex-start; justify-content:space-between; flex-wrap:wrap; }
h1 { font-size:22px; margin:0 0 6px; } h2 { font-size:17px; margin:36px 0 12px; } p { color:var(--text-muted); max-width:820px; }
button.toggle { font:inherit; padding:6px 12px; border-radius:6px; border:0.5px solid var(--border-strong); background:var(--bg-layer-01); color:var(--text-base); cursor:pointer; }
details { margin:8px 0; } summary { cursor:pointer; font-weight:600; padding:6px 0; } summary small { color:var(--text-faint); font-weight:400; }
.scroll { overflow-x:auto; }
table.tok { border-collapse:collapse; width:100%; font-size:12px; } table.tok th, table.tok td { text-align:left; padding:4px 8px; border-bottom:0.5px solid var(--border-muted); vertical-align:middle; }
.sw { display:inline-block; width:22px; height:16px; border-radius:4px; vertical-align:middle; margin-right:6px; background-image:linear-gradient(45deg,#ccc 25%,transparent 25%,transparent 75%,#ccc 75%),linear-gradient(45deg,#ccc 25%,#fff 25%,#fff 75%,#ccc 75%); background-size:8px 8px; background-position:0 0,4px 4px; overflow:hidden; }
.sw i { display:block; width:100%; height:100%; }
code { font-family:var(--fontFamily-mono); font-size:11px; }
.ev { font-size:10px; padding:1px 5px; border-radius:99px; background:var(--bg-layer-02); color:var(--text-muted); white-space:nowrap; }
.ev-derived { background:var(--state-info-bg); }
.bar { display:inline-block; height:10px; background:var(--role-accent-default); border-radius:2px; vertical-align:middle; }
.rad { display:inline-block; width:40px; height:24px; border:1px solid var(--border-strong); background:var(--bg-layer-02); vertical-align:middle; }
.shadow-box { display:inline-block; width:80px; height:36px; background:var(--role-raised); border-radius:8px; vertical-align:middle; }
.ramp { display:flex; align-items:flex-start; gap:2px; margin:6px 0; overflow-x:auto; }
.ramp-name { width:130px; flex:none; padding-top:6px; }
.ramp-step { display:flex; flex-direction:column; align-items:center; gap:2px; } .ramp-step i { width:44px; height:28px; border-radius:4px; display:block; }
.ramp-step code { font-size:10px; color:var(--text-faint); }
"""

sections = []
sections.append("<h2>Ramps</h2><p>The OpenCode theme's v2 ramps (grey in 13 steps, eight hues in 12) and its translucent steps. They are "
                "the same in light and dark; the semantic tokens below point at different steps per scheme.</p>" + ramps())
sections.append("<h2>Colour roles</h2><p>role.* maps the checklist roles onto OpenCode's v2 tokens. bg, text, border, icon, overlay "
                "and state are the v2 layer; legacy.* is the theme's older layer, which still colours code and markdown.</p>")
groups = []
for p, _ in light.items():
    if p[0] not in groups:
        groups.append(p[0])
groups.sort(key=lambda g: (GROUP_ORDER.index(g) if g in GROUP_ORDER else 99, g))
sections.append('<div class="scroll">' + "".join(colour_table(g) for g in groups) + "</div>")
sections.append("<h2>Type</h2>" + "".join(
    f'<div style="margin:8px 0"><div class="t-{p[-1]}">{esc(p[-1].capitalize())}: The folder is empty, no files or subdirectories</div>'
    f'<code>{esc(json.dumps(t["$value"]))}</code> {ev(t)}</div>' for p, t in core.items() if t["$type"] == "typography"))
sections.append("<h2>Type scales</h2>" + "".join(scale_rows(g, lambda p, t: "") for g in ("fontSize", "fontWeight", "lineHeight", "letterSpacing")))
sections.append("<h2>Radius</h2>" + scale_rows("radius", lambda p, t: f'<span class="rad" style="border-radius:{t["$value"]}"></span>'))
sections.append("<h2>Spacing</h2>" + scale_rows("spacing", lambda p, t: f'<span class="bar" style="width:{t["$value"]}"></span>'))
sections.append("<h2>Sizes and layout</h2>" + scale_rows("size", lambda p, t: f'<span class="bar" style="width:{t["$value"]}"></span>')
                + scale_rows("layout", lambda p, t: "") + scale_rows("container", lambda p, t: "") + scale_rows("breakpoint", lambda p, t: "")
                + scale_rows("focusRing", lambda p, t: "") + scale_rows("zIndex", lambda p, t: "") + scale_rows("borderWidth", lambda p, t: ""))
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
