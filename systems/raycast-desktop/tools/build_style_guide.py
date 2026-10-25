#!/usr/bin/env python3
"""Render style-guide.html from tokens.json.

    python3 tools/build_style_guide.py

Adapted from the native kit (systems/grokbot). Every token becomes a CSS custom property (its path
joined with dashes; an alias becomes a var() reference), light on :root and dark under
[data-theme="dark"], so the swatches, scales and specimens cannot drift from the file. Specimens are
drawn from tokens only; none of Raycast's icons or artwork is used. Standard library only, deterministic.
"""
import html
import json
import pathlib

PKG = pathlib.Path(__file__).resolve().parent.parent
TOKENS = PKG / "tokens.json"
OUT = PKG / "style-guide.html"
EV_CLASS = {"Measured": "ev-measured", "Sampled": "ev-sampled", "Sampled (text)": "ev-text", "Derived": "ev-derived", "Not captured": "ev-none"}


def walk(node, path=()):
    if isinstance(node, dict) and "$value" in node:
        yield path, node
        return
    if isinstance(node, dict):
        for k, v in node.items():
            if not k.startswith("$"):
                yield from walk(v, path + (k,))


def var(path):
    return "--" + "-".join(path).replace("_", "-")


def css(v):
    if isinstance(v, str) and v.startswith("{") and v.endswith("}"):
        return "var(%s)" % var(tuple(v[1:-1].split(".")))
    if isinstance(v, list) and v and isinstance(v[0], str):          # a font stack
        return ", ".join(f'"{f}"' if " " in f else f for f in v)
    if isinstance(v, list) and v and isinstance(v[0], (int, float)):  # a cubic bezier
        return "cubic-bezier(%s)" % ", ".join(f"{n:g}" for n in v)
    if isinstance(v, list) and v and isinstance(v[0], dict):         # a shadow
        return ", ".join(f"{'inset ' if l.get('inset') else ''}{l['offsetX']} {l['offsetY']} {l['blur']} {l['spread']} {l['color']}" for l in v)
    return str(v)


def esc(t):
    return html.escape(str(t), quote=True)


def resolve(v, *sets):
    while isinstance(v, str) and v.startswith("{") and v.endswith("}"):
        path = tuple(v[1:-1].split("."))
        v = next(s[path]["$value"] for s in sets if path in s)
    return v


def ev(t):
    e = t["$extensions"]["source"]["evidence"]
    return '<span class="ev %s">%s</span>' % (EV_CLASS[e], esc(e))


def build():
    data = json.loads(TOKENS.read_text())
    core = dict(walk(data["core"]))
    light = dict(walk(data["light"]))
    dark = dict(walk(data["dark"]))

    root = []
    for p, t in core.items():
        if t["$type"] == "typography":
            continue
        root.append(f"{var(p)}:{css(t['$value'])};")
    lvars = "".join(f"{var(p)}:{css(t['$value'])};" for p, t in light.items())
    dvars = "".join(f"{var(p)}:{css(t['$value'])};" for p, t in dark.items())
    type_css = []
    for p, t in core.items():
        if t["$type"] == "typography":
            v = t["$value"]
            type_css.append(".t-%s{font-family:%s;font-weight:%s;font-size:%s;letter-spacing:%s;line-height:1.4}" % (
                p[-1], css(v["fontFamily"]), css(v["fontWeight"]), css(v["fontSize"]), css(v.get("letterSpacing", "0px"))))

    def swatch_rows(prefixes):
        rows = []
        for p in light:
            if p[0] not in prefixes or light[p]["$type"] != "color":
                continue
            cells = []
            for theme_set in (light, dark):
                t = theme_set[p]
                shown = resolve(t["$value"], theme_set, core)
                label = t["$value"] if t["$value"] == shown else f"{t['$value']} = {shown}"
                # A translucent swatch is drawn over its own theme's painted window, not over the page
                # the guide happens to show, so each column previews what that theme paints.
                ground = resolve(theme_set[("page",)]["$value"], theme_set, core)
                cells.append('<td><i class="sw" style="background:linear-gradient(%s,%s),%s"></i><code>%s</code> %s</td>' % (
                    esc(shown), esc(shown), esc(ground), esc(label), ev(t)))
            rows.append("<tr><th><code>%s</code></th>%s<td class=d>%s</td></tr>" % (esc(".".join(p)), "".join(cells), esc(light[p]["$description"])))
        return "\n".join(rows)

    def dim_rows(prefixes):
        rows = []
        for p in light:
            if p[0] not in prefixes or light[p]["$type"] == "color":
                continue
            t = light[p]
            shown = resolve(t["$value"], light, core)
            rows.append("<tr><th><code>%s</code></th><td><code>%s</code> %s</td><td class=d>%s</td></tr>" % (
                esc(".".join(p)), esc(t["$value"] if t["$value"] == shown else f"{t['$value']} = {shown}"), ev(t), esc(t["$description"])))
        return "\n".join(rows)

    def core_rows(group):
        rows = []
        for p, t in core.items():
            if p[0] != group:
                continue
            v = t["$value"]
            shown = json.dumps(v) if isinstance(v, (dict, list)) else v
            demo = ""
            if group == "radius":
                demo = '<i class="rad" style="border-radius:%s"></i>' % css(v)
            elif group == "spacing":
                demo = '<i class="spc" style="width:%s"></i>' % css(v)
            elif group == "typography":
                demo = '<span class="t-%s">Search for apps and commands, 0123</span>' % p[-1]
            elif group == "shadow":
                demo = '<i class="rad" style="box-shadow:%s;background:var(--dialog)"></i>' % css(v)
            rows.append("<tr><th><code>%s</code></th><td><code>%s</code> %s</td><td>%s</td><td class=d>%s</td></tr>" % (
                esc(".".join(p)), esc(shown), ev(t), demo, esc(t["$description"])))
        return "\n".join(rows)

    roles = sorted({p[0] for p in light} - {"theme", "alpha", "component"}, key=lambda k: list(dict.fromkeys(q[0] for q in light)).index(k))
    kbd = lambda k: f'<span class="kbd">{k}</span>'
    specimens = f"""
<div class="win">
 <div class="search"><span class="ph">Search for apps and commands...</span></div>
 <div class="list">
  <div class="row sel"><i class="ico" style="background:var(--theme-red)"></i><span>See what's new</span><span class="mut">v2.9.0</span><span class="acc">Changelog</span></div>
  <div class="hdr">Suggestions</div>
  <div class="row"><i class="ico" style="background:var(--theme-blue)"></i><span>Telegram</span><span class="acc">Application</span></div>
  <div class="row hov"><i class="ico" style="background:var(--theme-green)"></i><span>Orca</span><span class="acc">Application</span></div>
  <div class="row"><i class="ico" style="background:var(--theme-purple)"></i><span>Search Emoji &amp; Symbols</span><span class="mut">Raycast</span><span class="badge">Pro</span><span class="acc">Command</span></div>
  <div class="row dis"><i class="ico" style="background:var(--theme-orange)"></i><span>Disabled row</span><span class="acc">Command</span></div>
 </div>
 <div class="footer"><span class="pill round">&#8801;</span><span class="pill">Open Application {kbd("&#8629;")} <span class="sep"></span> Actions {kbd("&#8984;")}{kbd("K")}</span></div>
</div>
<div class="row2">
 <div class="panel"><div class="mut small">Digital Color Meter</div><div class="mi sel">Open Application<span class="r">{kbd("&#8629;")}</span></div><div class="mi">Show in Finder<span class="r">{kbd("&#8984;")}{kbd("&#8629;")}</span></div><div class="mi">Show Info in Finder<span class="r">{kbd("&#8984;")}{kbd("I")}</span></div><div class="msearch mut">Search for actions...</div></div>
 <div class="spage"><div class="card">
  <div class="srow"><span>Open at Login</span><i class="switch on"></i></div>
  <div class="srow"><span>Show In Menu Bar</span><i class="switch"></i></div>
  <div class="srow"><span>Dark Theme</span><span class="dd">Raycast Dark &#8964;</span></div>
  <div class="srow"><span>Theme Studio<br><span class="mut small">Edit or create themes for Raycast</span></span><span class="btn">Upgrade to Pro</span></div>
  <div class="srow"><span>Name</span><span class="field err">Required</span></div>
  <div class="srow"><span>Show "What's New" after an update</span><i class="cb on">&#10003;</i></div>
 </div></div>
</div>"""
    page = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Raycast style guide</title>
<style>
:root{{{''.join(root)}{lvars}}}
[data-theme="dark"]{{{dvars}}}
{''.join(type_css)}
body{{margin:0;font-family:var(--fontFamily-ui);font-size:13px;background:var(--page);color:var(--text-primary);padding:16px 24px}}
h1{{font-size:24px}} h2{{margin-top:40px;font-size:18px;border-bottom:1px solid var(--border-separator);padding-bottom:6px}}
table{{border-collapse:collapse;width:100%;font-size:12px}} td,th{{text-align:left;vertical-align:top;padding:4px 6px;border-bottom:1px solid var(--border-tertiary)}}
.wrap{{overflow-x:auto}} .d{{color:var(--text-secondary);max-width:520px}} .mut{{color:var(--text-secondary)}} .ph{{color:var(--text-placeholder)}} .small{{font-size:var(--fontSize-11)}}
.sw{{display:inline-block;width:18px;height:18px;border-radius:4px;vertical-align:middle;margin-right:6px;box-shadow:0 0 0 1px var(--border-secondary)}}
.ev{{font-size:10px;padding:1px 4px;border-radius:4px;box-shadow:0 0 0 1px var(--border-secondary)}} .ev-measured{{color:var(--theme-green)}} .ev-derived{{color:var(--theme-orange)}} .ev-sampled{{color:var(--theme-blue)}}
.rad{{display:inline-block;width:40px;height:28px;box-shadow:0 0 0 1px var(--border-secondary);background:var(--surface)}} .spc{{display:inline-block;height:10px;background:var(--accent-default)}}
.toggle{{position:sticky;top:0;float:right;font:inherit;background:var(--surfaceFill-control);color:inherit;border:0;border-radius:var(--radius-full);padding:4px 12px}}
.win{{max-width:var(--size-mainWindow-width);border-radius:var(--radius-window);background:var(--page);box-shadow:var(--shadow-panel),0 0 0 1px var(--border-separator);overflow:hidden;position:relative}}
.search{{height:var(--size-mainWindow-header);display:flex;align-items:center;padding:0 var(--spacing-24);font-size:var(--fontSize-18)}}
.list{{padding:0 var(--size-listInset) 52px}} .hdr{{font-size:var(--fontSize-11);color:var(--component-list-sectionHeader-text);padding:12px var(--spacing-8) 6px}}
.row{{height:var(--component-list-row-height);border-radius:var(--component-list-row-radius);display:flex;align-items:center;gap:var(--spacing-12);padding:0 var(--spacing-8)}}
.row.sel{{background:var(--component-list-row-selectedBg)}} .row.hov{{background:var(--component-list-row-hoverBg)}} .row.dis{{opacity:.3}} .acc{{margin-left:auto;color:var(--text-secondary)}}
.ico{{width:var(--size-icon-22);height:var(--size-icon-22);border-radius:var(--radius-6);display:inline-block}}
.badge{{background:var(--alpha-blue-10);color:var(--theme-blue);font-size:var(--fontSize-11);border-radius:var(--radius-full);padding:1px 8px}}
.footer{{position:absolute;left:0;right:0;bottom:0;height:var(--size-mainWindow-footer);display:flex;justify-content:space-between;align-items:center;padding:0 var(--spacing-8) var(--spacing-8)}}
.pill{{height:var(--size-actionBarPill);border-radius:var(--radius-full);display:inline-flex;align-items:center;gap:6px;padding:0 var(--spacing-12);background:var(--surfaceFill-actionBar);box-shadow:0 0 0 1px var(--border-separator)}} .pill.round{{width:var(--size-actionBarPill);padding:0;justify-content:center}}
.sep{{width:1px;height:16px;background:var(--border-separator);margin:0 6px}}
.kbd{{display:inline-flex;min-width:var(--component-kbd-height);height:var(--component-kbd-height);align-items:center;justify-content:center;padding:0 var(--spacing-4);box-sizing:border-box;border-radius:var(--radius-6);box-shadow:inset 0 0 0 1px var(--component-kbd-border);color:var(--component-kbd-text);font-size:var(--fontSize-11);margin-left:2px}}
.row2{{display:flex;flex-wrap:wrap;gap:24px;margin-top:24px;align-items:flex-start}}
.panel{{width:340px;max-width:100%;border-radius:var(--radius-12);background:var(--dialog);box-shadow:var(--shadow-panel),0 0 0 1px var(--border-separator);padding:var(--spacing-8)}}
.panel .small{{padding:4px 8px}} .mi{{height:32px;display:flex;align-items:center;padding:0 var(--spacing-8);border-radius:var(--radius-8)}} .mi.sel{{background:var(--component-list-row-selectedBg)}} .r{{margin-left:auto}}
.msearch{{border-top:1px solid var(--border-separator);margin-top:6px;padding:10px 8px 2px}}
.spage{{flex:1;min-width:300px;max-width:584px;background:var(--settingsPage);border-radius:var(--radius-12);padding:var(--spacing-12)}}
.card{{background:var(--surface);border-radius:var(--radius-10);padding:0 var(--spacing-12)}}
.srow{{min-height:var(--component-settings-rowHeight);display:flex;align-items:center;justify-content:space-between;gap:12px;border-bottom:1px solid var(--component-settings-separator)}} .srow:last-child{{border:0}}
.switch{{box-sizing:border-box;display:inline-block;width:var(--component-switch-width);height:var(--component-switch-height);border-radius:var(--radius-full);background:var(--component-switch-offBg);position:relative}}
.switch:after{{content:"";position:absolute;top:1.5px;left:1.5px;width:var(--component-switch-thumbWidth);height:13px;border-radius:var(--radius-full);background:var(--component-switch-thumb)}} .switch.on{{background:var(--component-switch-onBg)}} .switch.on:after{{left:auto;right:1.5px}}
.dd{{height:var(--component-dropdown-height);display:inline-flex;align-items:center;padding:0 var(--spacing-8) 0 var(--spacing-12);border-radius:var(--radius-8);background:var(--component-dropdown-bg);box-shadow:0 0 0 1px var(--component-dropdown-border)}}
.btn{{height:var(--component-button-height);display:inline-flex;align-items:center;padding:0 var(--component-button-padding);border-radius:var(--radius-full);background:var(--component-button-bg)}}
.field{{height:var(--component-input-height);width:180px;display:inline-flex;align-items:center;padding:0 var(--component-input-padding);border-radius:var(--radius-8);background:var(--component-input-bg);box-shadow:0 0 0 1px var(--component-input-border);color:var(--text-placeholder)}} .field.err{{box-shadow:0 0 0 1px var(--component-input-errorBorder)}}
.cb{{width:var(--component-checkbox-size);height:var(--component-checkbox-size);border-radius:var(--radius-4);box-shadow:0 0 0 1px var(--component-checkbox-border);color:var(--component-checkbox-check);font-size:11px;font-style:normal;display:inline-flex;align-items:center;justify-content:center}}
</style></head><body>
<button class="toggle" onclick="var r=document.documentElement;r.dataset.theme=r.dataset.theme==='dark'?'light':'dark'">Light / Dark</button>
<h1>Raycast 2.9: Raycast Light and Raycast Dark</h1>
<p class="d">Swatches in each theme's column are drawn over that theme's painted launcher window (page), so translucent roles preview as the app paints them. Every colour and size is Raycast's own declaration, read from the stylesheets and theme definitions shipped in the app (Measured), with the alpha steps worked out from them (Derived) and checked against the window's pixels (raw/pixel-check.json). The window fills (page, settingsPage, sidebar) are pixels (Sampled): the windows are translucent over the macOS window material, so no declaration gives them. Specimens are drawn from tokens only; none of Raycast's icons or artwork is used (the coloured squares stand in for app icons).</p>
<h2>Specimens</h2>
{specimens}
<h2>Roles (light, dark)</h2><div class="wrap"><table>{swatch_rows(roles)}</table></div>
<h2>Component colours (light, dark)</h2><div class="wrap"><table>{swatch_rows(["component"])}</table></div>
<h2>Component sizes</h2><div class="wrap"><table>{dim_rows(["component"])}</table></div>
<h2>Typography</h2><div class="wrap"><table>{core_rows("typography")}{core_rows("fontFamily")}{core_rows("fontSize")}{core_rows("fontWeight")}</table></div>
<h2>Radii</h2><div class="wrap"><table>{core_rows("radius")}</table></div>
<h2>Spacing</h2><div class="wrap"><table>{core_rows("spacing")}</table></div>
<h2>Sizes, borders, blur</h2><div class="wrap"><table>{core_rows("size")}{core_rows("borderWidth")}{core_rows("blur")}</table></div>
<h2>Elevation and motion</h2><div class="wrap"><table>{core_rows("shadow")}{core_rows("duration")}{core_rows("easing")}</table></div>
<h2>Theme base colours (light, dark)</h2><div class="wrap"><table>{swatch_rows(["theme"])}</table></div>
<h2>Alpha steps (light, dark)</h2><div class="wrap"><table>{swatch_rows(["alpha"])}</table></div>
</body></html>
"""
    OUT.write_text(page)
    print("style-guide.html:", len(light), "tokens per theme")


if __name__ == "__main__":
    build()
