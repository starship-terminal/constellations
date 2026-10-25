#!/usr/bin/env python3
"""Render style-guide.html from tokens.json.

    python3 tools/build_style_guide.py

Every token becomes a CSS custom property (its path joined with dashes; an alias becomes a var()), so
the swatches, scales and specimens cannot drift from the file. The page starts in the reader's
system theme and has a Light/Dark toggle that sets data-theme on <html>. Specimens are drawn from
tokens only, in the system font Superset itself uses, with no Superset artwork, logos or icons.
PRODUCT (adapt): NAME, LEDE, GROUP_ORDER, specimens(), SPEC_CSS and the colour section's intro.
Standard library only, deterministic.
"""
import html
import json
import pathlib
import re

PKG = pathlib.Path(__file__).resolve().parent.parent
TOKENS = json.loads((PKG / "tokens.json").read_text())
OUT = PKG / "style-guide.html"

NAME = "Superset desktop"  # PRODUCT (adapt)
LEDE = ("Superset 1.39.0 for macOS (Electron), the app that runs coding agents in parallel workspaces, read live from the "
        "running app over its remote-debugging port on 2026-10-25, in its built-in Light and Dark themes. Every value below "
        "is a token from tokens.json; the specimens are rebuilt from those tokens, not copied from the app.")  # PRODUCT (adapt)
GROUP_ORDER = ["role", "ui", "focus", "link", "palette", "terminal", "syntax", "shadow", "component"]


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
    open_ = " open" if group in ("role", "ui") else ""
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
 <figure><figcaption>Sidebar: navigation, sections, a project and its workspace</figcaption>
  <div class="sp-sidebar">
   <div class="sp-row new"><span class="sp-plus">+</span>New Workspace<span class="sp-kbd">&#8984;N</span></div>
   <div class="sp-row">Search</div><div class="sp-row sel">Workspaces</div><div class="sp-row">Automations</div>
   <div class="sp-group t-overline">Projects</div>
   <div class="sp-row strong"><span class="sp-proj">S</span>scratch-project</div>
   <div class="sp-row ws sel">List files in this folder <span class="sp-end"><span class="add">+1</span> <span class="del">-0</span></span></div>
   <div class="sp-card"><span class="sp-badge-sq">Setup</span><div class="t-ui" style="font-weight:500">Lifecycle scripts</div>
    <div class="t-label" style="font-weight:400;color:var(--role-text-secondary)">Automate workspace setup</div><span class="sp-btn outline block">Configure</span></div>
  </div>
 </figure>
 <figure><figcaption>Composer on the New Workspace page: chips, ghost icons, the round send button</figcaption>
  <div class="t-display" style="text-align:center;margin:6px 0 14px;color:var(--role-text-primary)">What should we build next?</div>
  <div class="sp-composer"><div class="t-body" style="color:var(--role-text-secondary)">Find a small bug and fix it&#8230;</div>
   <div class="sp-toolbar"><span class="sp-ghost">+</span><span class="sp-chip">Claude &#8964;</span><span class="sp-chip">Default model &#8964;</span><span style="flex:1"></span><span class="sp-send">&#8593;</span></div></div>
  <div class="sp-footer t-caption"><span>This device &#8597;</span><span>scratch-project &#8597;</span><span>Worktree &#8597;</span></div>
 </figure>
 <figure><figcaption>Buttons: ink primary, outline, ghost, destructive; hover is the fill at 90%; the 3px focus ring</figcaption>
  <div class="sp-buttons">
   <span class="sp-btn primary">Create project</span><span class="sp-btn primary is-hover">Hover</span>
   <span class="sp-btn outline">Download starter</span><span class="sp-btn ghost">Cancel</span>
   <span class="sp-btn destructive">Delete</span><span class="sp-btn primary is-disabled">Disabled</span><span class="sp-btn outline focus">Focus ring</span>
  </div>
 </figure>
 <figure><figcaption>Menu over the page (popover fill, hairline, shadow-md)</figcaption>
  <div class="sp-menu"><div class="sp-mrow">Rename</div><div class="sp-mrow hi">Open in Finder</div><div class="sp-mrow">Copy Path</div><hr>
   <div class="sp-mrow">Move to group <span class="sp-end">&#8250;</span></div><div class="sp-mrow danger">Delete <span class="sp-end t-label">&#8984;&#8679;&#9003;</span></div></div>
 </figure>
 <figure><figcaption>Destructive confirmation over the scrim</figcaption>
  <div class="sp-scrim"><div class="sp-dialog"><div class="t-title" style="font-size:16px">Delete workspace?</div>
   <div class="t-body" style="color:var(--role-text-secondary)">This closes the workspace and its terminals.</div>
   <div style="display:flex;gap:8px;justify-content:flex-end;margin-top:14px"><span class="sp-btn ghost sm">Cancel</span><span class="sp-btn destructive sm">Delete</span></div></div></div>
 </figure>
 <figure><figcaption>Settings: navigation, a row group, switch, select, field</figcaption>
  <div class="sp-settings"><div class="sp-snav"><div class="sp-row">Account</div><div class="sp-row sel">General</div><div class="sp-row">Terminal</div></div>
   <div class="sp-group-box">
    <div class="sp-field"><div><div class="t-body">Confirm before quitting</div><div class="t-label" style="font-weight:400;color:var(--role-text-secondary)">Show a dialog when quitting</div></div><span class="sp-switch on"></span></div>
    <div class="sp-field"><div class="t-body">Changes open target</div><span class="sp-select">Pane in current tab &#8964;</span></div>
    <div class="sp-field"><input class="sp-input" value="1.5" aria-label="Line height"></div>
   </div></div>
 </figure>
 <figure><figcaption>Workspace: tab strip with the running dot, preset bar, pane header, terminal</figcaption>
  <div class="sp-ws"><div class="sp-tabs"><span class="sp-wtab">Claude</span><span class="sp-wtab sel">Claude <i class="run"></i></span><span class="sp-ghost">+</span></div>
   <div class="sp-presets t-label"><span>Claude</span><span>Codex</span><span>OpenCode</span><span>Grok</span></div>
   <div class="sp-pane-head t-label">Claude <i class="run"></i></div>
   <pre class="sp-term">&#10095; List the files in this folder.
<span style="color:var(--terminal-green)">&#9679;</span> Listing files in current directory
  &#9151; ls -la
<span style="color:var(--terminal-bright-black)">&#10033; Baked for 9s</span></pre></div>
 </figure>
 <figure><figcaption>Segmented control, badges, toast</figcaption>
  <div class="sp-seg"><span class="sp-segi">List</span><span class="sp-segi sel">Board</span></div>
  <div style="display:flex;gap:8px;margin:12px 0"><span class="sp-badge">MCP</span><span class="sp-pro">PRO</span></div>
  <div class="sp-toast">Create failed: Directory already exists</div>
 </figure>
</div>"""


SPEC_CSS = """
.spec-grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(320px,1fr)); gap:20px; }
figure { margin:0; padding:16px; background:var(--role-page); border:1px solid var(--role-border-default); border-radius:var(--radius-lg); color:var(--role-text-primary); font-family:var(--fontFamily-sans); font-size:var(--fontSize-sm); }
figcaption { font-size:12px; color:var(--role-text-secondary); margin-bottom:12px; }
.sp-sidebar { background:var(--role-surface); border-radius:var(--radius-lg); padding:var(--spacing-2); }
.sp-row { display:flex; align-items:center; gap:8px; height:var(--controlHeight-md); padding:0 var(--spacing-2); border-radius:var(--radius-base); color:var(--role-text-secondary); font-size:var(--fontSize-ui); font-weight:500; }
.sp-row.sel { background:var(--ui-fill-selected); color:var(--role-text-primary); }
.sp-row.new { background:var(--ui-fill-hover); }
.sp-row.strong, .sp-row.ws { color:var(--role-text-primary); }
.sp-row.ws { padding-left:24px; font-size:var(--fontSize-sm); font-weight:400; }
.sp-plus { width:16px; text-align:center; }
.sp-kbd { margin-left:auto; font-size:10px; padding:1px 4px; border-radius:var(--radius-sm); border:1px solid var(--role-border-default); background:var(--ui-fill-selected); }
.sp-group { padding:12px 8px 4px; color:var(--role-text-secondary); }
.sp-proj { width:16px; height:16px; border-radius:var(--radius-sm); display:grid; place-items:center; font-size:10px; background:var(--ui-muted); color:var(--role-text-secondary); border:1px solid var(--role-border-default); }
.sp-end { margin-left:auto; } .add { color:var(--palette-emerald-500); } .del { color:var(--palette-red-500); }
.sp-card { margin-top:12px; background:var(--component-card-bg); border:1px solid var(--component-card-border); border-radius:var(--component-card-radius); padding:var(--component-card-padding); display:grid; gap:4px; }
.sp-badge-sq { justify-self:start; font-size:10px; letter-spacing:0.5px; text-transform:uppercase; padding:0 6px; background:var(--ui-accent); border:1px solid var(--role-border-default); }
.sp-composer { background:var(--component-composer-bg); box-shadow:0 0 0 1px var(--role-border-default); border-radius:var(--component-composer-radius); padding:14px 16px 10px; }
.sp-toolbar { display:flex; align-items:center; gap:6px; margin-top:18px; }
.sp-ghost { width:26px; height:26px; border-radius:var(--radius-base); display:inline-grid; place-items:center; color:var(--role-text-secondary); }
.sp-chip { display:inline-flex; align-items:center; height:var(--component-chip-height); padding:0 8px; border-radius:var(--component-chip-radius); background:var(--component-chip-bg); border:var(--borderWidth-chip) solid var(--component-chip-border); color:var(--component-chip-text); font-size:var(--fontSize-xs-ui); }
.sp-send { width:22px; height:22px; border-radius:99px; display:inline-grid; place-items:center; background:var(--ui-fill-selected); font-size:12px; }
.sp-footer { display:flex; gap:14px; margin-top:8px; color:var(--role-text-secondary); }
.sp-buttons { display:flex; flex-wrap:wrap; gap:8px; align-items:center; }
.sp-btn { display:inline-flex; align-items:center; height:var(--controlHeight-base); padding:0 var(--spacing-3); border-radius:var(--radius-base); font-weight:500; border:1px solid transparent; }
.sp-btn.sm { height:var(--controlHeight-md); font-size:var(--fontSize-xs); }
.sp-btn.block { justify-content:center; height:var(--controlHeight-md); font-size:var(--fontSize-xs); }
.sp-btn.primary { background:var(--component-button-primary-bg); color:var(--component-button-primary-text); }
.sp-btn.primary.is-hover { background:var(--role-accent-hover); }
.sp-btn.is-disabled { opacity:0.5; }
.sp-btn.outline { background:var(--component-button-secondary-bg); border-color:var(--component-button-secondary-border); color:var(--component-button-secondary-text); box-shadow:var(--shadow-xs); }
.sp-btn.ghost { color:var(--component-button-ghost-text); }
.sp-btn.destructive { background:var(--component-button-destructive-bg); color:var(--component-button-destructive-text); }
.sp-btn.focus { border-color:var(--role-border-focus); box-shadow:0 0 0 var(--focusRing-width) var(--focus-ring); }
.sp-menu { background:var(--component-menu-bg); border:1px solid var(--component-menu-border); border-radius:var(--component-menu-radius); padding:var(--component-menu-padding); max-width:240px; box-shadow:var(--shadow-md); }
.sp-menu hr { border:0; border-top:1px solid var(--role-border-default); margin:4px -4px; }
.sp-mrow { display:flex; align-items:center; height:var(--size-control-menu-row); padding:0 var(--spacing-2); border-radius:var(--component-menu-row-radius); }
.sp-mrow.hi { background:var(--ui-accent); } .sp-mrow.danger { color:var(--role-status-danger-fill); }
.sp-switch { display:inline-block; width:var(--size-control-switch-width); height:var(--size-control-switch-height); border-radius:99px; background:var(--component-switch-off-bg); position:relative; }
.sp-switch::after { content:""; position:absolute; top:1px; left:1px; width:16px; height:16px; border-radius:99px; background:var(--role-page); }
.sp-switch.on { background:var(--component-switch-on-bg); } .sp-switch.on::after { left:15px; }
.sp-scrim { background:var(--role-scrim); padding:24px; border-radius:var(--radius-lg); }
.sp-dialog { background:var(--component-dialog-bg); border:1px solid var(--component-dialog-border); border-radius:var(--component-dialog-radius); padding:var(--spacing-6); box-shadow:var(--shadow-lg); }
.sp-settings { display:grid; grid-template-columns:110px 1fr; gap:10px; }
.sp-snav .sp-row { font-weight:400; }
.sp-group-box { border:1px solid var(--role-border-default); border-radius:var(--radius-lg); }
.sp-field { display:flex; align-items:center; justify-content:space-between; gap:8px; padding:10px 12px; border-bottom:1px solid var(--role-border-default); }
.sp-field:last-child { border-bottom:0; }
.sp-select { border:1px solid var(--component-select-border); border-radius:var(--component-select-radius); padding:4px 8px; font-size:12px; box-shadow:var(--shadow-xs); }
.sp-input { width:100%; box-sizing:border-box; height:var(--component-text-field-height); padding:0 var(--spacing-3); border-radius:var(--component-text-field-radius); border:1px solid var(--component-text-field-border); background:transparent; color:var(--role-text-primary); font:inherit; box-shadow:var(--shadow-xs); }
.sp-input:focus { outline:none; border-color:var(--role-border-focus); box-shadow:0 0 0 var(--focusRing-width) var(--focus-ring); }
.sp-ws { border:1px solid var(--role-border-default); border-radius:var(--radius-base); overflow:hidden; }
.sp-tabs { display:flex; align-items:end; gap:2px; padding:4px 4px 0; background:var(--ui-muted); }
.sp-wtab { display:flex; align-items:center; gap:6px; padding:6px 10px; border-radius:var(--radius-base) var(--radius-base) 0 0; color:var(--role-text-secondary); font-size:12px; border:1px solid transparent; border-bottom:0; }
.sp-wtab.sel { background:var(--role-page); color:var(--role-text-primary); border-color:var(--role-border-default); }
i.run { display:inline-block; width:6px; height:6px; border-radius:99px; background:var(--role-status-running); }
.sp-presets { display:flex; gap:12px; padding:6px 10px; color:var(--role-text-secondary); font-weight:400; }
.sp-pane-head { display:flex; align-items:center; gap:6px; padding:4px 10px; background:var(--component-pane-header-bg); font-weight:400; }
.sp-term { margin:0; padding:10px 12px; background:var(--terminal-background); color:var(--terminal-foreground); font-family:var(--fontFamily-terminal); font-size:12px; line-height:1.45; }
.sp-seg { display:inline-flex; padding:2px; border-radius:var(--component-segmented-radius); background:var(--component-segmented-bg); }
.sp-segi { padding:4px 10px; border-radius:var(--component-segment-selected-radius); color:var(--role-text-secondary); font-size:12px; }
.sp-segi.sel { background:var(--component-segment-selected-bg); color:var(--component-segment-selected-text); box-shadow:var(--shadow-sm); }
.sp-badge { display:inline-flex; align-items:center; height:16px; padding:0 4px; border-radius:var(--component-badge-radius); border:1px solid var(--component-badge-border); color:var(--component-badge-text); font-size:9px; font-weight:500; }
.sp-pro { display:inline-flex; align-items:center; height:var(--component-badge-solid-height); padding:0 8px; border-radius:99px; background:var(--component-badge-solid-bg); color:var(--component-badge-solid-text); font-size:12px; font-weight:500; }
.sp-toast { padding:14px 16px; border-radius:var(--component-toast-radius); background:var(--component-toast-bg); border:1px solid var(--component-toast-border); color:var(--component-toast-text); box-shadow:var(--shadow-toast); font-size:13px; }
"""

PAGE_CSS = """
:root { color-scheme: light dark; }
html[data-theme="dark"] { color-scheme: dark; }
body { margin:0; background:var(--role-page); color:var(--role-text-primary); font:13px/1.45 -apple-system, BlinkMacSystemFont, sans-serif; }
main { max-width:1180px; margin:0 auto; padding:24px 16px 64px; }
header { display:flex; gap:16px; align-items:flex-start; justify-content:space-between; flex-wrap:wrap; }
h1 { font-size:22px; margin:0 0 6px; } h2 { font-size:17px; margin:36px 0 12px; } p { color:var(--role-text-secondary); max-width:820px; }
button.toggle { font:inherit; padding:6px 12px; border-radius:99px; border:1px solid var(--role-border-default); background:var(--ui-accent); color:var(--role-text-primary); cursor:pointer; }
details { margin:8px 0; } summary { cursor:pointer; font-weight:600; padding:6px 0; } summary small { color:var(--role-text-secondary); font-weight:400; }
.scroll { overflow-x:auto; }
table.tok { border-collapse:collapse; width:100%; font-size:12px; } table.tok th, table.tok td { text-align:left; padding:4px 8px; border-bottom:1px solid var(--role-border-default); vertical-align:middle; }
.sw { display:inline-block; width:22px; height:16px; border-radius:4px; vertical-align:middle; margin-right:6px; background-image:linear-gradient(45deg,#ccc 25%,transparent 25%,transparent 75%,#ccc 75%),linear-gradient(45deg,#ccc 25%,#fff 25%,#fff 75%,#ccc 75%); background-size:8px 8px; background-position:0 0,4px 4px; overflow:hidden; }
.sw i { display:block; width:100%; height:100%; }
code { font-family:ui-monospace, Menlo, monospace; font-size:11px; }
.ev { font-size:10px; padding:1px 5px; border-radius:99px; background:var(--ui-fill-hover); color:var(--role-text-secondary); white-space:nowrap; }
.ev-derived { background:var(--ui-fill-selected); }
.bar { display:inline-block; height:10px; background:var(--role-brand); border-radius:2px; vertical-align:middle; }
.rad { display:inline-block; width:40px; height:24px; border:1px solid var(--role-border-strong); background:var(--ui-fill-hover); vertical-align:middle; }
.shadow-box { display:inline-block; width:80px; height:36px; background:var(--role-raised); border-radius:8px; vertical-align:middle; }
"""

sections = []
sections.append("<h2>Colour roles and the theme's colours</h2><p>role.* maps the checklist roles onto Superset's tokens. ui.* are the 41 "
                "colours the theme engine writes on the root (shadcn's names) and the two fills mixed from the foreground; link, syntax "
                "and the Tailwind palette steps come from the stylesheet; terminal.* is the palette xterm.js paints with.</p>")
groups = []
for p, _ in light.items():
    if p[0] not in groups:
        groups.append(p[0])
groups.sort(key=lambda g: (GROUP_ORDER.index(g) if g in GROUP_ORDER else 99, g))
sections.append('<div class="scroll">' + "".join(colour_table(g) for g in groups) + "</div>")
sections.append("<h2>Type</h2>" + "".join(
    f'<div style="margin:8px 0"><div class="t-{p[-1]}">{esc(p[-1].capitalize())}: The agent listed the files in this folder</div>'
    f'<code>{esc(json.dumps(t["$value"]))}</code> {ev(t)}</div>' for p, t in core.items() if t["$type"] == "typography"))
sections.append("<h2>Radius</h2>" + scale_rows("radius", lambda p, t: f'<span class="rad" style="border-radius:{t["$value"]}"></span>'))
sections.append("<h2>Spacing</h2>" + scale_rows("spacing", lambda p, t: f'<span class="bar" style="width:{t["$value"]}"></span>'))
sections.append("<h2>Control heights, sizes and layout</h2>" + scale_rows("controlHeight", lambda p, t: f'<span class="bar" style="width:{t["$value"]}"></span>')
                + scale_rows("size", lambda p, t: "") + scale_rows("layout", lambda p, t: "") + scale_rows("focusRing", lambda p, t: "")
                + scale_rows("zIndex", lambda p, t: "") + scale_rows("borderWidth", lambda p, t: ""))
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
