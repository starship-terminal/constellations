#!/usr/bin/env python3
"""Render style-guide.html from tokens.json.

    python3 tools/build_style_guide.py

Every token becomes a CSS custom property (its path joined with dashes; an alias becomes a var()), so
the swatches, scales and specimens cannot drift from the file. The page starts in the reader's
system theme and has a Light/Dark toggle that sets data-theme on <html>. Specimens are drawn from
tokens only, in Inter and with no Capy artwork or icons. PRODUCT (adapt): NAME, LEDE, GROUP_ORDER, specimens(), SPEC_CSS and the colour section's note.
Standard library only, deterministic.
"""
import html
import json
import pathlib
import re

PKG = pathlib.Path(__file__).resolve().parent.parent
TOKENS = json.loads((PKG / "tokens.json").read_text())
OUT = PKG / "style-guide.html"

NAME = "Capy desktop"  # PRODUCT (adapt)
LEDE = ("Capy 0.4.7 for macOS (Electron), Scrapybara's cloud coding-agent app, read live from the running app over its "
        "remote-debugging port on 2026-10-25, in its light and dark themes with the default colour theme. Every value below is a token "
        "from tokens.json; the specimens are rebuilt from those tokens in Inter, Capy's interface font, not copied from the app.")  # PRODUCT (adapt)
GROUP_ORDER = ["role", "base", "diff", "chart", "shadow", "component"]


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
 <figure><figcaption>Window: tab strip, sidebar, content panel</figcaption>
  <div class="sp-window">
   <div class="sp-tabs"><span class="sp-lights"><i></i><i></i><i></i></span><span class="sp-tab on">New thread</span><span class="sp-tab">Threads</span><span style="flex:1"></span><span class="sp-update">Update</span></div>
   <div class="sp-shell">
    <div class="sp-sidebar">
     <div class="sp-row on">New thread <span class="sp-kbd">&#8679;&#8984;O</span></div><div class="sp-row">Threads</div><div class="sp-row hover">Pull requests</div><div class="sp-row">Automations</div>
     <div class="sp-group">Threads</div>
     <div class="sp-thread"><div>Explore repository codebase <span class="sp-age">15w</span></div><div class="sp-key">QUIVE-1</div></div>
    </div>
    <div class="sp-panel"><div class="t-heading">Capy</div><div class="sp-desc">How Capy works in your repositories</div></div>
   </div>
  </div>
 </figure>
 <figure><figcaption>Composer: pickers, editor, toolbar, Start</figcaption>
  <div class="sp-pickers"><span>My project &#8964;</span><span>Cloud &#8964;</span><span style="flex:1"></span><span>2 repos &#8964;</span></div>
  <div class="sp-composer"><div class="t-prompt">List the files in this folder.</div>
   <div class="sp-toolbar"><span>+</span><span>&#8645;</span><span style="color:var(--base-warning-fg)">claude-opus-5-5 &#8964;</span><span style="flex:1"></span><span>&#127908;</span><span class="sp-send">&#8593;</span></div></div>
 </figure>
 <figure><figcaption>Buttons: the seven looks, the painted intents, focus</figcaption>
  <div class="sp-buttons">
   <span class="sp-btn ghost">Ghost</span><span class="sp-btn soft">Soft</span><span class="sp-btn outline">Outline</span><span class="sp-btn solid">Solid</span>
   <span class="sp-btn selected">Selected</span><span class="sp-btn accent">Accent</span><span class="sp-btn inverse">Inverse</span>
   <span class="sp-btn danger">Delete</span><span class="sp-btn ghost" style="color:var(--base-destructive)">Discard</span><span class="sp-btn outline focus">Focus</span>
  </div>
 </figure>
 <figure><figcaption>Menu with section label, shortcut and a destructive row</figcaption>
  <div class="sp-menu"><div class="sp-mlabel">Run on</div><div class="sp-mrow">Cloud <span class="sp-end">&#10003;</span></div><div class="sp-mrow hi">Open in new tab</div><div class="sp-mrow">Archive <span class="sp-end">A</span></div><hr><div class="sp-mrow danger">Delete <span class="sp-end">D</span></div></div>
 </figure>
 <figure><figcaption>Confirmation dialog over the scrim</figcaption>
  <div class="sp-scrim"><div class="sp-dialog"><div style="font-weight:500;font-size:var(--fontSize-base)">Delete thread</div>
   <div class="sp-desc" style="margin-top:6px">This permanently removes the thread and its workspace.</div>
   <div style="display:flex;gap:8px;justify-content:flex-end;margin-top:16px"><span class="sp-btn ghost">Cancel</span><span class="sp-btn danger">Delete thread</span></div></div></div>
 </figure>
 <figure><figcaption>Settings card: rows, switch, select, input, segmented scope</figcaption>
  <div class="sp-seg"><span class="on">You</span><span>Org</span></div>
  <div class="sp-card">
   <div class="sp-field"><div><div class="sp-label">Commit author</div><div class="sp-desc">Who authors Capy's commits</div></div><span class="sp-select">You, Capy co-author &#8964;</span></div>
   <div class="sp-field"><div><div class="sp-label">Signed commits</div><div class="sp-desc">Sign commits with your managed GPG key</div></div><span class="sp-switch"></span></div>
   <div class="sp-field"><div><div class="sp-label">System notifications</div></div><span class="sp-switch on"></span></div>
   <div class="sp-field"><div class="sp-label">Branch prefix</div><span class="sp-input">capy</span></div>
  </div>
 </figure>
 <figure><figcaption>Thread: the prompt bubble (its fill not measured; base.secondary here), the reply on the page, the folded work</figcaption>
  <div class="sp-chat">
   <div class="sp-user"><div class="sp-who"><span class="sp-ava">U</span> user_dev <span class="sp-desc">10:02 PM</span></div>The transcript still drops events after a reconnect.</div>
   <div class="sp-worked">Worked for 14s &#8250;</div>
   <div class="t-message">Looking into it. The CI log lines up with the reconnect gap.</div>
   <pre class="sp-code t-code">pnpm --filter @capy/core test</pre>
  </div>
 </figure>
 <figure><figcaption>Toast, badges, tooltip</figcaption>
  <div class="sp-toast"><div style="font-weight:500"><span style="color:var(--base-destructive)">&#9679;</span> Failed to start thread</div><div class="sp-desc">Copilot is not connected, connect it to use Claude Opus 5.5</div></div>
  <div style="display:flex;gap:6px;flex-wrap:wrap;margin-top:12px"><span class="sp-badge">Queued</span><span class="sp-badge ok">Passing</span><span class="sp-badge bad">Failed</span><span class="sp-count">12</span></div>
  <span class="sp-tooltip">Search <span style="opacity:.6">&#8984;K</span></span>
 </figure>
</div>"""


SPEC_CSS = """
.spec-grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(320px,1fr)); gap:20px; }
figure { margin:0; padding:16px; background:var(--base-panel); border:0.5px solid var(--base-border-1); border-radius:var(--radius-panel); color:var(--base-fg); font-family:var(--fontFamily-sans); font-size:var(--fontSize-sm); }
figcaption { font-size:var(--fontSize-xs); color:var(--base-muted-foreground-2); margin-bottom:12px; }
.sp-window { background:var(--base-chrome); border-radius:var(--radius-panel); overflow:hidden; }
.sp-tabs { display:flex; align-items:center; gap:6px; height:var(--layout-tab-strip-height); padding:0 8px; }
.sp-lights i { display:inline-block; width:10px; height:10px; border-radius:99px; margin-right:5px; background:var(--base-muted); }
.sp-tab { display:inline-flex; align-items:center; height:var(--size-control-tab); padding:0 10px; border-radius:var(--radius-card); border:0.5px solid transparent; color:var(--base-tab-inactive-foreground); font-weight:500; }
.sp-tab.on { background:var(--base-popover); color:var(--base-fg); border-color:var(--base-card-hairline); box-shadow:var(--shadow-card); }
.sp-update { color:var(--base-primary); font-weight:500; }
.sp-shell { display:flex; gap:0; padding:0 6px 6px 0; }
.sp-sidebar { width:42%; padding:4px 8px; }
.sp-panel { flex:1; background:var(--base-panel); border:0.5px solid var(--base-border-1); border-radius:var(--radius-panel); padding:16px; }
.sp-row { display:flex; align-items:center; height:var(--controlHeight-menu-row); padding:0 8px; border-radius:var(--radius-button); color:var(--base-muted-foreground-1); font-weight:500; }
.sp-row.on, .sp-row.hover { background:var(--base-secondary); color:var(--base-fg); }
.sp-kbd { margin-left:auto; font-size:var(--fontSize-2xs); color:var(--base-muted-foreground-2); }
.sp-group { padding:12px 8px 4px; color:var(--base-muted-foreground-2); font-size:var(--fontSize-xs); }
.sp-thread { padding:4px 8px; border-radius:var(--radius-button); color:var(--base-fg); }
.sp-age, .sp-key { color:var(--base-muted-foreground-2); font-size:var(--fontSize-xs); }
.sp-pickers { display:flex; gap:12px; color:var(--base-muted-foreground-1); margin:0 6px 8px; }
.sp-composer { background:var(--base-popover); border-radius:var(--radius-card); padding:var(--spacing-3); box-shadow:var(--shadow-composer); }
.sp-toolbar { display:flex; align-items:center; gap:12px; margin-top:22px; color:var(--base-icon-muted); }
.sp-send { width:var(--size-control-send); height:var(--size-control-send); border-radius:var(--radius-button); display:inline-grid; place-items:center; background:var(--base-primary); color:var(--base-primary-text); }
.sp-buttons { display:flex; flex-wrap:wrap; gap:8px; align-items:center; }
.sp-btn { display:inline-flex; align-items:center; height:var(--controlHeight-sm); padding:0 10px; border-radius:var(--radius-button); font-weight:500; border:0.5px solid transparent; color:var(--base-fg); }
.sp-btn.soft { background:var(--base-secondary); } .sp-btn.outline { border-color:var(--base-border-2); }
.sp-btn.solid { background:var(--base-button); border-color:var(--base-border-2); box-shadow:var(--shadow-plate); }
.sp-btn.selected { background:var(--base-secondary-hover); } .sp-btn.accent { background:var(--base-primary); color:var(--base-primary-text); }
.sp-btn.inverse { background:var(--base-inverse); color:var(--base-inverse-text); } .sp-btn.danger { background:var(--base-destructive); color:var(--base-destructive-text); }
.sp-btn.ghost:hover, .sp-btn.outline:hover { background:var(--base-secondary); }
.sp-btn.focus { outline:var(--focusRing-width) solid var(--base-ring); outline-offset:var(--focusRing-offset); }
.sp-menu { background:var(--base-popover); border-radius:var(--radius-overlay); padding:4px; max-width:240px; box-shadow:var(--shadow-overlay); }
.sp-menu hr { border:0; border-top:0.5px solid var(--base-border-1); margin:4px -4px; }
.sp-mlabel { padding:4px 8px; font-size:var(--fontSize-xs); color:var(--base-muted-foreground-2); font-weight:500; }
.sp-mrow { display:flex; align-items:center; height:var(--controlHeight-menu-row); padding:0 8px; border-radius:var(--radius-button); }
.sp-mrow.hi { background:var(--base-popover-hover); } .sp-mrow.danger { color:var(--base-destructive); }
.sp-end { margin-left:auto; color:var(--base-muted-foreground-2); font-size:var(--fontSize-xs); }
.sp-scrim { background:var(--base-overlay); padding:24px; border-radius:var(--radius-card); }
.sp-dialog { background:var(--base-popover); border-radius:var(--radius-overlay); padding:20px; box-shadow:var(--shadow-overlay); }
.sp-seg { display:inline-flex; gap:4px; margin-bottom:10px; } .sp-seg span { padding:4px 10px; border-radius:var(--radius-button); color:var(--base-muted-foreground-1); } .sp-seg span.on { background:var(--base-secondary); color:var(--base-fg); }
.sp-card { background:var(--base-card); border:0.5px solid var(--base-card-hairline); box-shadow:var(--shadow-card); border-radius:var(--radius-card); }
.sp-field { display:flex; align-items:center; justify-content:space-between; gap:12px; padding:var(--spacing-4); border-bottom:0.5px solid var(--base-border-1); }
.sp-field:last-child { border-bottom:0; }
.sp-label { font-weight:500; } .sp-desc { color:var(--base-muted-foreground-2); font-size:var(--fontSize-sm); }
.sp-switch { flex:none; position:relative; display:inline-block; width:var(--size-control-switch-width); height:var(--size-control-switch-height); border-radius:99px; background:var(--base-muted); }
.sp-switch::after { content:""; position:absolute; top:2px; left:2px; width:12px; height:12px; border-radius:99px; background:var(--base-primary-text); box-shadow:var(--shadow-plate); }
.sp-switch.on { background:var(--base-primary); } .sp-switch.on::after { left:14px; }
.sp-select, .sp-input { display:inline-flex; align-items:center; height:var(--controlHeight-sm); padding:0 10px; border-radius:var(--radius-button); border:0.5px solid var(--base-border-2); background:var(--base-input); white-space:nowrap; }
.sp-input { min-width:110px; }
.sp-chat { padding:4px; }
.sp-user { width:fit-content; max-width:85%; background:var(--base-secondary); border-radius:var(--radius-card); padding:8px 12px; }
.sp-who { display:flex; align-items:center; gap:6px; font-size:var(--fontSize-xs); font-weight:500; margin-bottom:4px; }
.sp-ava { display:inline-grid; place-items:center; width:16px; height:16px; border-radius:var(--radius-xs); background:var(--base-muted); font-size:10px; }
.sp-worked { margin:12px 0 8px; color:var(--base-muted-foreground-2); }
.sp-code { background:var(--base-section); border:0.5px solid var(--base-border-1); border-radius:var(--radius-card); padding:10px 12px; margin:10px 0 0; overflow:auto; }
.sp-toast { background:var(--base-popover); border-radius:var(--radius-card); padding:14px 16px; box-shadow:var(--shadow-overlay); }
.sp-badge { display:inline-flex; align-items:center; height:var(--badgeHeight-sm); padding:0 8px; border-radius:99px; background:var(--base-secondary); font-size:var(--fontSize-xs); }
.sp-badge.ok { color:var(--base-success); } .sp-badge.bad { color:var(--base-destructive); background:var(--base-destructive-soft); }
.sp-count { display:inline-grid; place-items:center; min-width:16px; height:var(--badgeHeight-count); padding:0 4px; border-radius:99px; background:var(--base-primary); color:var(--base-primary-text); font-size:var(--fontSize-2xs); }
.sp-tooltip { display:inline-block; margin-top:14px; background:var(--component-tooltip-bg); color:var(--component-tooltip-text); border:0.5px solid var(--base-border-2); border-radius:var(--component-tooltip-radius); padding:4px 8px; font-size:var(--fontSize-xs); box-shadow:var(--shadow-overlay); }
"""

PAGE_CSS = """
:root { color-scheme: light dark; }
html[data-theme="dark"] { color-scheme: dark; }
body { margin:0; background:var(--role-page); color:var(--base-fg); font:14px/1.45 var(--fontFamily-sans); }
main { max-width:1180px; margin:0 auto; padding:24px 16px 64px; }
header { display:flex; gap:16px; align-items:flex-start; justify-content:space-between; flex-wrap:wrap; }
h1 { font-size:22px; margin:0 0 6px; } h2 { font-size:17px; margin:36px 0 12px; } p { color:var(--base-muted-foreground-1); max-width:820px; }
button.toggle { font:inherit; padding:6px 12px; border-radius:99px; border:1px solid var(--base-border-2); background:var(--base-secondary); color:var(--base-fg); cursor:pointer; }
details { margin:8px 0; } summary { cursor:pointer; font-weight:600; padding:6px 0; } summary small { color:var(--base-muted-foreground-2); font-weight:400; }
.scroll { overflow-x:auto; }
table.tok { border-collapse:collapse; width:100%; font-size:12px; } table.tok th, table.tok td { text-align:left; padding:4px 8px; border-bottom:1px solid var(--base-border-1); vertical-align:middle; }
.sw { display:inline-block; width:22px; height:16px; border-radius:4px; vertical-align:middle; margin-right:6px; background-image:linear-gradient(45deg,#ccc 25%,transparent 25%,transparent 75%,#ccc 75%),linear-gradient(45deg,#ccc 25%,#fff 25%,#fff 75%,#ccc 75%); background-size:8px 8px; background-position:0 0,4px 4px; overflow:hidden; }
.sw i { display:block; width:100%; height:100%; }
code { font-family:ui-monospace, Menlo, monospace; font-size:11px; }
.ev { font-size:10px; padding:1px 5px; border-radius:99px; background:var(--base-secondary); color:var(--base-muted-foreground-1); white-space:nowrap; }
.ev-derived { background:var(--base-primary-soft); }
.bar { display:inline-block; height:10px; background:var(--base-primary); border-radius:2px; vertical-align:middle; }
.rad { display:inline-block; width:40px; height:24px; border:1px solid var(--role-border-strong); background:var(--base-muted); vertical-align:middle; }
.shadow-box { display:inline-block; width:80px; height:36px; background:var(--role-raised); border-radius:8px; vertical-align:middle; }
"""

sections = []
sections.append("<h2>Colour roles and theme</h2><p>role.* maps the checklist roles onto Capy's tokens. base.* is Capy's theme: oklch seeds, "
                "and the text tiers, soft fills, link and ring mixed from them (the formula is on each token in tokens.json). Tailwind's black and "
                "white, the only palette steps Capy loads, follow.</p>")
groups = []
for p, _ in light.items():
    if p[0] not in groups:
        groups.append(p[0])
groups.sort(key=lambda g: (GROUP_ORDER.index(g) if g in GROUP_ORDER else 99, g))
sections.append('<div class="scroll">' + "".join(colour_table(g) for g in groups) + "</div>")
palette_rows = "".join(f'<tr><th><code>{esc(".".join(p))}</code></th><td><span class="sw"><i style="background:{esc(t["$value"])}"></i></span><code>{esc(t["$value"])}</code> {ev(t)}</td></tr>'
                       for p, t in core.items() if p[0] == "color")
sections.append(f'<details><summary>color (Tailwind black and white, core) <small>{sum(1 for p in core if p[0] == "color")}</small></summary><table class="tok">{palette_rows}</table></details>')
sections.append("<h2>Type</h2>" + "".join(
    f'<div style="margin:8px 0"><div class="t-{p[-1]}">{esc(p[-1].capitalize())}: The agent listed the files in this folder</div>'
    f'<code>{esc(json.dumps(t["$value"]))}</code> {ev(t)}</div>' for p, t in core.items() if t["$type"] == "typography"))
sections.append("<h2>Radius</h2>" + scale_rows("radius", lambda p, t: f'<span class="rad" style="border-radius:{t["$value"]}"></span>'))
sections.append("<h2>Spacing</h2>" + scale_rows("spacing", lambda p, t: f'<span class="bar" style="width:{t["$value"]}"></span>'))
sections.append("<h2>Type scale</h2>" + scale_rows("fontSize", lambda p, t: f'<span style="font-size:{t["$value"]}">Aa</span>') + scale_rows("lineHeight", lambda p, t: "")
                + scale_rows("fontWeight", lambda p, t: "") + scale_rows("letterSpacing", lambda p, t: ""))
sections.append("<h2>Control heights, sizes and layout</h2>" + scale_rows("controlHeight", lambda p, t: f'<span class="bar" style="width:{t["$value"]}"></span>') + scale_rows("badgeHeight", lambda p, t: "") + scale_rows("iconSize", lambda p, t: f'<span class="bar" style="width:{t["$value"]}"></span>')
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
