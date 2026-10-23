#!/usr/bin/env python3
"""Render style-guide.html from tokens.json (native kit, from systems/grokbot).

    python3 tools/build_style_guide.py

Adapted for Arc Search from the native kit (tools/kit/native, from systems/grokbot).

Every token becomes a CSS custom property (its path joined with dashes; an alias becomes a var()
reference), so the swatches, scales and specimens cannot drift from the file. Adapt NAME, LEDE,
OWNER, `sample` and `specimens` (PRODUCT (adapt)); draw specimens from tokens only, never the
product's artwork.
Adapted from systems/hevy/tools/build_style_guide.py. Standard library only, deterministic.
"""
import html
import json
import pathlib

PKG = pathlib.Path(__file__).resolve().parent.parent
TOKENS = PKG / "tokens.json"
OUT = PKG / "style-guide.html"

FONT_STACK = '-apple-system, system-ui, "SF Pro Text", "Helvetica Neue", Arial, sans-serif'
MONO_STACK = 'ui-monospace, "SF Mono", Menlo, monospace'
NAME = "Arc Search"   # PRODUCT (adapt)
OWNER = "The Browser Company"    # PRODUCT (adapt): whose visual system it is
LEDE = ("Arc Search for iOS, read from stills captured through iPhone Mirroring on 2026-10-23 (dark) and 2026-10-24 (light).")  # PRODUCT (adapt)
EV_CLASS = {"Sampled": "ev-sampled", "Sampled (text)": "ev-text", "Derived": "ev-derived", "Not captured": "ev-none"}


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


def css(v):
    if isinstance(v, str) and v.startswith("{") and v.endswith("}"):
        return "var(%s)" % var(tuple(v[1:-1].split(".")))
    return str(v)


def esc(t):
    return html.escape(str(t), quote=True)


def resolve(v, *sets):
    """Follow an alias through the given token sets (its own theme first, then core) to a value."""
    while isinstance(v, str) and v.startswith("{") and v.endswith("}"):
        path = tuple(v[1:-1].split("."))
        v = next(s[path]["$value"] for s in sets if path in s)
    return v


def swatch_cell(tok, *sets):
    ev = tok["$extensions"]["source"]["evidence"]
    v = tok["$value"]
    shown = resolve(v, *sets)       # a swatch shows its own theme's value, whatever theme the page is in
    label = v if v == shown else f"{v} = {shown}"
    return ('<td><span class="sw" title="%s"><i style="background:%s"></i></span><code>%s</code> '
            '<span class="ev %s">%s</span></td>' % (esc(tok["$extensions"]["source"]["capture"]), esc(shown),
                                                    esc(label), EV_CLASS[ev], esc(ev)))


def build():
    data = json.loads(TOKENS.read_text())
    core, light, dark = (list(walk(data[s])) for s in ("core", "light", "dark"))
    dark_by = dict(dark)
    core_by, light_by = dict(core), dict(light)

    core_css, type_css = [], []
    for p, t in core:
        if t["$type"] == "typography":
            v = t["$value"]
            type_css.append(".type-%s{font-family:var(--font-base);font-weight:%s;font-size:%s;line-height:%s}"
                            % (p[-1], css(v["fontWeight"]), v["fontSize"], v.get("lineHeight", "1.25")))
        elif t["$type"] == "fontFamily":
            core_css.append("%s:%s" % (var(p), FONT_STACK))
        else:
            core_css.append("%s:%s" % (var(p), css(t["$value"])))
    core_css += ["--font-base:%s" % FONT_STACK, "--font-mono:%s" % MONO_STACK]
    light_css = ["%s:%s" % (var(p), css(t["$value"])) for p, t in light]
    dark_css = ["%s:%s" % (var(p), css(t["$value"])) for p, t in dark]

    # ---- semantic colours, light and dark side by side
    groups = {}
    for p, t in light:
        groups.setdefault(p[1], []).append((p, t))
    colour_html = []
    for g, items in groups.items():
        rows = "".join('<tr><th scope="row"><code>%s</code><span class="desc">%s</span></th>%s%s</tr>'
                       % (esc(".".join(p)), esc(t["$description"]), swatch_cell(t, light_by, core_by), swatch_cell(dark_by[p], dark_by, core_by))
                       for p, t in items)
        colour_html.append('<h3>%s</h3><div class="scroll"><table class="tokens"><thead><tr><th>Token</th><th>Light</th>'
                           '<th>Dark</th></tr></thead><tbody>%s</tbody></table></div>' % (esc(g), rows))

    under = lambda pre: [(p, t) for p, t in core if p[:len(pre)] == pre]
    palette = "".join('<div class="chip-sw"><span class="dot" style="background:%s"></span><code>%s</code><span>%s</span></div>'
                      % (esc(css(t["$value"])), esc(".".join(p)), esc(t["$value"])) for p, t in under(("color", "tile")))
    neutrals = "".join('<div class="ramp-step" style="background:%s" title="%s"><code>%s</code></div>'
                       % (esc(t["$value"]), esc(t["$description"]), esc(p[-1] + " " + t["$value"])) for p, t in under(("color", "neutral")))
    radii = "".join('<div class="radius-box" style="border-radius:%s"><code>%s</code><span>%s</span></div>'
                    % (esc(css(t["$value"])), esc(".".join(p)), esc(t["$value"])) for p, t in under(("radius",)))
    spacing = "".join('<div class="space-row"><code>%s</code><span class="bar" style="width:%s"></span><span>%s</span></div>'
                      % (esc(".".join(p)), esc(css(t["$value"])), esc(t["$value"])) for p, t in under(("space",)))
    sizes = "".join('<div class="space-row"><code>%s</code><span class="bar thin" style="width:%s"></span><span>%s</span></div>'
                    % (esc(".".join(p)), esc(css(t["$value"])), esc(t["$value"])) for p, t in under(("size",)))
    sample = {  # PRODUCT (adapt): specimen text per type style
        "spaceTitle": "Main", "search": "Search...", "navTitle": "Settings", "body": "Search Engine",
        "button": "Downloads", "row": "Launcher", "sectionHeader": "Today", "notice": "Arc scrubbed 5 ads and trackers",
        "caption": "Share your open tab URLs", "pill": "Browse for Me", "tileLabel": "Find on Page"}
    type_rows = "".join('<tr><th scope="row"><code>%s</code><span class="desc">%s</span></th><td class="meta">%s, %s%s</td>'
                        '<td><span class="type-%s">%s</span></td></tr>'
                        % (esc(".".join(p)), esc(t["$description"]), esc(t["$value"]["fontSize"]), esc(t["$value"]["fontWeight"]),
                           (", line " + t["$value"]["lineHeight"]) if "lineHeight" in t["$value"] else "", p[-1], esc(sample.get(p[-1], "Sample")))
                        for p, t in under(("typography",)))

    # PRODUCT (adapt): specimens built from tokens only
    specimens = """
<div class="spec-grid">
 <div class="spec">
  <h3>Settings sheet: nav bar, buttons, groups, switch</h3>
  <div class="sheet">
   <div class="nav"><span></span><span class="type-navTitle">Settings</span><span class="navbtn type-button">Done</span></div>
   <div class="pair"><span class="btn type-button">Downloads</span><span class="btn type-button">Archive</span></div>
   <div class="group">
    <div class="row"><span class="tile" style="background:var(--color-tile-blue)"></span><span class="type-body lbl">Search Engine</span><span class="type-body sec">Google &#8250;</span></div>
    <div class="row"><span class="tile" style="background:var(--color-tile-green)"></span><span class="type-body lbl">Languages</span><span class="type-body ter">&#8250;</span></div>
   </div>
   <div class="group">
    <div class="row"><span class="tile" style="background:var(--color-tile-yellow)"></span><span class="type-body lbl">Auto-Open Keyboard</span><span class="sw-ctl"></span></div>
    <div class="row"><span class="tile" style="background:var(--color-tile-purple)"></span><span class="type-body lbl">Archive Inactive Tabs</span><span class="type-body sec">After 7 days</span></div>
    <div class="row"><span class="tile" style="background:var(--color-tile-red)"></span><span class="type-body lbl">Clear Browsing Data...</span></div>
   </div>
  </div>
  <p class="note">bg.sheet, surface.group, glass.navButton, size.button, radius.group, space.groupGap, size.row, size.tile, color.tile.*, border.separator, switch.onTrack</p>
 </div>
 <div class="spec">
  <h3>Archive: page, cards, confirm, search</h3>
  <div class="page">
   <div class="nav"><span class="ctl type-button">Edit</span><span class="type-navTitle">Archive</span><span class="confirm">&#10003;</span></div>
   <p class="type-sectionHeader secthead">Today</p>
   <div class="card">
    <div class="hrow"><span class="fav"></span><div><div class="type-row">How to make a good launch video</div><div class="type-caption url">example.com/watch?v=launch</div></div></div>
    <div class="hrow"><span class="fav"></span><div><div class="type-row">Release notes - Search</div><div class="type-caption url">example.com/search?q=release+notes</div></div></div>
   </div>
   <div class="sbar type-body">&#9906; Search</div>
  </div>
  <p class="note">bg.page, surface.card, surface.control, accent.default, text.onAccent, text.section, text.url, size.rowHistory, glass.searchBar, size.searchBar</p>
 </div>
 <div class="spec">
  <h3>Launcher: search field, rows, Browse for Me</h3>
  <div class="launcher">
   <div class="search type-search"><span class="caret"></span>Search...</div>
   <div class="lrow type-row"><span>design</span><span class="pill type-pill">Browse for Me</span></div>
   <div class="lrow type-row"><span><span class="sec">desig</span>nation meaning</span><span class="pill type-pill">Browse for Me</span></div>
   <div class="lrow type-row"><span>Launcher</span><span class="ter">&#9906;</span></div>
  </div>
  <div class="toolbar"><span class="plus">+</span></div>
  <p class="note">glass.launcher, glass.searchField, size.searchField, focus.caret, size.rowLauncher, glass.pill, size.pill, radius.pill, glass.toolbar, glass.plus, size.plus</p>
 </div>
 <div class="spec">
  <h3>Page menu, find bar, destructive item</h3>
  <div class="menu">
   <div class="addr type-row">m.example.com</div>
   <div class="tiles"><span><i class="tb"></i><span class="type-tileLabel tl">Find on Page</span></span><span><i class="tb"></i><span class="type-tileLabel tl">Summarize</span></span><span><i class="tb"></i><span class="type-tileLabel tl">Pin</span></span><span><i class="tb"></i><span class="type-tileLabel tl">Share</span></span></div>
   <div class="panel"><div class="type-row mrow">Translate</div><div class="type-row mrow">Reader Mode</div><div class="type-row mrow">Request Desktop Site</div></div>
   <div class="panel notice"><div class="type-notice">Arc scrubbed 5 ads and trackers</div><div class="type-caption ng2">Problems? Tap to restore original page</div></div>
  </div>
  <div class="findbar"><span class="ib">&#215;</span><span class="ff type-row">food<span class="type-row fc">1 of 2</span></span></div>
  <p class="destr type-body">Remove Favorite</p>
  <p class="note">glass.menu, glass.address, size.addressBar, glass.tileButton, size.tileButton, radius.tileButton, glass.panel, radius.panel, size.rowMenu, glass.notice, text.onGlass, glass.findField, size.findField, size.iconButton, text.findCount, destructive.text</p>
 </div>
 <div class="spec">
  <h3>Space sheet</h3>
  <div class="space"><span class="type-spaceTitle">Main</span><span class="sclose">&#215;</span></div>
  <p class="note">space.top, space.bottom, space.title, radius.sheet. Each space has its own colour; these are Main's.</p>
 </div>
</div>
"""

    page_css = """
*{box-sizing:border-box}
html,body{background:var(--color-bg-page)}
body{margin:0;color:var(--color-text-primary);font-family:var(--font-base);font-size:15px;line-height:1.45}
.wrap{max-width:1080px;margin:0 auto;padding:24px 16px 64px}
header.top{display:flex;flex-wrap:wrap;gap:12px 24px;align-items:center;justify-content:space-between}
h1{font-size:26px;margin:0}h2{font-size:20px;margin:40px 0 8px}h3{font-size:15px;margin:20px 0 8px}
p.lede{color:var(--color-text-secondary);margin:4px 0 0;max-width:70ch}p.note{color:var(--color-text-secondary);font-size:12px;margin:10px 0 0}
code{font-family:var(--font-mono);font-size:12px}
.toggle{display:inline-flex;border-radius:var(--radius-capsule);padding:3px;gap:2px;background:var(--color-surface-card)}
.toggle button{border:0;background:transparent;color:var(--color-text-secondary);font:inherit;padding:6px 14px;border-radius:var(--radius-capsule);cursor:pointer}
.toggle button[aria-pressed="true"]{background:var(--color-accent-default);color:var(--color-text-onAccent)}
.scroll{overflow-x:auto}
table.tokens{border-collapse:collapse;width:100%;min-width:660px}
table.tokens th,table.tokens td{text-align:left;vertical-align:top;padding:8px 10px;border-bottom:var(--border-width-hairline) solid var(--color-border-separator)}
table.tokens thead th{color:var(--color-text-secondary);font-size:12px;font-weight:400}
table.tokens th[scope=row]{font-weight:500;width:40%}
.desc{display:block;color:var(--color-text-secondary);font-size:12px;font-weight:400;margin-top:2px}
.meta{color:var(--color-text-secondary);white-space:nowrap}
.sw{display:inline-block;width:28px;height:28px;border-radius:8px;vertical-align:middle;margin-right:8px;border:1px solid var(--color-border-separator);background-image:linear-gradient(45deg,#8883 25%,transparent 25%,transparent 75%,#8883 75%),linear-gradient(45deg,#8883 25%,transparent 25%,transparent 75%,#8883 75%);background-size:8px 8px;background-position:0 0,4px 4px;overflow:hidden}
.sw i{display:block;width:100%;height:100%}
.ev{display:inline-block;font-size:11px;padding:1px 7px;border-radius:var(--radius-capsule);border:1px solid var(--color-border-separator);color:var(--color-text-secondary);white-space:nowrap}
.ev-derived{border-style:dashed}.ev-none{border-style:dotted}
.palette{display:flex;flex-wrap:wrap;gap:12px}
.chip-sw{display:flex;flex-direction:column;align-items:center;gap:4px;width:84px;font-size:12px;color:var(--color-text-secondary)}
.chip-sw .dot{width:44px;height:44px;border-radius:10px}
.ramp{display:flex;flex-wrap:wrap;border-radius:var(--radius-panel);overflow:hidden;border:1px solid var(--color-border-separator)}
.ramp-step{flex:1 0 76px;height:64px;display:flex;align-items:flex-end;padding:4px}
.ramp-step code{font-size:10px;background:#0008;color:#fff;padding:0 3px;border-radius:3px}
.radii{display:flex;flex-wrap:wrap;gap:16px}
.radius-box{width:120px;height:80px;background:var(--color-surface-card);border:1px solid var(--color-border-separator);display:flex;flex-direction:column;align-items:center;justify-content:center;font-size:12px;color:var(--color-text-secondary)}
.space-row{display:grid;grid-template-columns:minmax(150px,240px) 1fr 70px;align-items:center;gap:12px;padding:3px 0}
.space-row .bar{display:block;height:12px;background:var(--color-accent-default);border-radius:2px;max-width:100%}
.space-row .bar.thin{height:8px;background:var(--color-text-secondary)}
.spec-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,340px),1fr));gap:16px}
.spec{border:1px solid var(--color-border-separator);border-radius:var(--radius-panel);padding:4px 16px 16px;min-width:0}
.sec{color:var(--color-text-secondary)}.ter{color:var(--color-text-tertiary)}
.sheet{background:var(--color-bg-sheet);border-radius:var(--radius-sheet) var(--radius-sheet) 0 0;padding:12px var(--space-screenMargin) 16px;max-width:390px}
.page{background:var(--color-bg-page);border-radius:var(--radius-sheet);padding:12px var(--space-screenMargin) 16px;max-width:390px;border:1px solid var(--color-border-separator)}
.nav{display:grid;grid-template-columns:1fr auto 1fr;align-items:center;min-height:var(--size-navButtonHeight)}
.nav>:first-child{justify-self:start}.nav>:last-child{justify-self:end}
.navbtn,.ctl{display:inline-flex;align-items:center;height:var(--size-navButtonHeight);padding:0 16px;border-radius:var(--radius-capsule);background:var(--color-glass-navButton)}
.ctl{background:var(--color-surface-control)}
.confirm{display:inline-flex;align-items:center;justify-content:center;width:var(--size-confirmButton);height:var(--size-confirmButton);border-radius:50%;background:var(--color-accent-default);color:var(--color-text-onAccent);font-size:20px}
.pair{display:flex;gap:var(--space-buttonGap);margin:16px 0 var(--space-buttonToGroup)}
.btn{flex:1;display:inline-flex;align-items:center;justify-content:center;height:var(--size-button);border-radius:var(--radius-capsule);background:var(--color-surface-group)}
.group{background:var(--color-surface-group);border-radius:var(--radius-group);padding:0 16px;margin-bottom:var(--space-groupGap)}
.group:last-child{margin-bottom:0}
.row{display:flex;align-items:center;gap:12px;min-height:var(--size-row)}
.row+.row .lbl{box-shadow:0 calc(-1 * var(--border-width-hairline)) 0 var(--color-border-separator)}
.row .lbl{flex:1;align-self:stretch;display:flex;align-items:center}
.tile{flex:none;width:var(--size-tile);height:var(--size-tile);border-radius:var(--radius-tile)}
.sw-ctl{position:relative;flex:none;width:var(--size-switch-width);height:var(--size-switch-height);border-radius:var(--radius-capsule);background:var(--color-switch-onTrack)}
.sw-ctl::after{content:"";position:absolute;top:2px;right:2px;width:var(--size-switch-thumb);height:calc(var(--size-switch-height) - 4px);border-radius:var(--radius-capsule);background:var(--color-switch-thumb)}
.secthead{margin:16px 0 6px;color:var(--color-text-section)}
.card{background:var(--color-surface-card);border-radius:var(--radius-group);padding:0 16px}
.hrow{display:flex;gap:12px;align-items:center;min-height:var(--size-rowHistory)}
.fav{flex:none;width:16px;height:16px;border-radius:var(--radius-tile);background:var(--color-tile-red)}
.url{color:var(--color-text-url)}
.sbar{margin-top:16px;height:var(--size-searchBar);border-radius:var(--radius-capsule);background:var(--color-glass-searchBar);display:flex;align-items:center;padding:0 16px;color:var(--color-text-secondary)}
.launcher{background:var(--color-glass-launcher);border-radius:var(--radius-sheet) var(--radius-sheet) 0 0;padding:16px var(--space-screenMargin) 8px;max-width:390px}
.search{position:relative;height:var(--size-searchField);border-radius:var(--radius-capsule);background:var(--color-glass-searchField);display:flex;align-items:center;padding:0 18px;color:var(--color-text-placeholder)}
.caret{display:inline-block;width:2px;height:24px;background:var(--color-focus-caret);margin-right:2px}
.lrow{display:flex;align-items:center;justify-content:space-between;min-height:var(--size-rowLauncher)}
.pill{display:inline-flex;align-items:center;height:var(--size-pill);padding:0 10px;border-radius:var(--radius-pill);background:var(--color-glass-pill)}
.toolbar{display:flex;justify-content:center;padding:10px 0;background:var(--color-glass-toolbar);max-width:390px}
.plus{display:inline-flex;align-items:center;justify-content:center;width:var(--size-plusWidth);height:var(--size-plus);border-radius:var(--radius-capsule);background:var(--color-glass-plus);font-size:24px}
.menu{background:var(--color-glass-menu);border-radius:var(--radius-sheet);padding:16px var(--space-screenMargin);max-width:390px}
.addr{height:var(--size-addressBar);border-radius:var(--radius-capsule);background:var(--color-glass-address);display:flex;align-items:center;justify-content:center}
.tiles{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin:16px 0}
.tiles>span{display:flex;flex-direction:column;align-items:center;gap:4px;min-width:0}
.tb{display:block;width:100%;aspect-ratio:1;max-width:var(--size-tileButton);border-radius:var(--radius-tileButton);background:var(--color-glass-tileButton)}
.tl{color:var(--color-text-tileLabel);white-space:nowrap}
.panel{background:var(--color-glass-panel);border-radius:var(--radius-panel);padding:0 16px;margin-bottom:12px}
.mrow{display:flex;align-items:center;min-height:var(--size-rowMenu);color:var(--color-text-onGlass)}
.notice{background:var(--color-glass-notice);padding:12px 16px;color:var(--color-text-onGlass)}
.ng2{color:var(--color-text-onGlassSecondary)}
.findbar{display:flex;gap:8px;align-items:center;margin-top:12px;max-width:390px}
.ib{flex:none;display:inline-flex;align-items:center;justify-content:center;width:var(--size-iconButton);height:var(--size-iconButton);border-radius:50%;background:var(--color-glass-findField);font-size:24px}
.ff{flex:1;display:flex;justify-content:space-between;align-items:center;height:var(--size-findField);border-radius:var(--radius-capsule);background:var(--color-glass-findField);padding:0 16px}
.fc{color:var(--color-text-findCount)}
.destr{color:var(--color-destructive-text);margin:12px 0 0}
.space{display:flex;justify-content:space-between;align-items:flex-start;height:260px;max-width:390px;border-radius:var(--radius-sheet);padding:20px;background:linear-gradient(var(--color-space-top),var(--color-space-bottom));color:var(--color-space-title)}
.sclose{display:inline-flex;align-items:center;justify-content:center;width:28px;height:28px;border-radius:50%;background:#FFFFFF33}
footer{margin-top:48px;color:var(--color-text-secondary);font-size:12px}
""".strip()

    script = """(function(){var r=document.documentElement,b=document.querySelectorAll('[data-set-theme]');
function a(t){r.setAttribute('data-theme',t);for(var i=0;i<b.length;i++){b[i].setAttribute('aria-pressed',String(b[i].getAttribute('data-set-theme')===t));}}
for(var i=0;i<b.length;i++){b[i].addEventListener('click',function(e){a(e.currentTarget.getAttribute('data-set-theme'));});}a('dark');})();"""

    parts = ["<!doctype html>", '<html lang="en" data-theme="dark">', "<head>", '<meta charset="utf-8">',
             '<meta name="viewport" content="width=device-width, initial-scale=1">', "<title>%s style guide</title>" % esc(NAME), "<style>",
             ":root{%s}" % ";".join(core_css),
             ':root,:root[data-theme="light"]{color-scheme:light;%s}' % ";".join(light_css),
             ':root[data-theme="dark"]{color-scheme:dark;%s}' % ";".join(dark_css),
             "\n".join(type_css), page_css, "</style>", "</head>", "<body>", '<div class="wrap">',
             '<header class="top"><div><h1>%s style guide</h1>' % esc(NAME),
             '<p class="lede">%s Every value below comes from tokens.json; points are 1:1 with CSS pixels. ' % esc(LEDE)
             + "The font is not known, so the page uses the platform sans. "
             "Every glass surface is drawn as one reading of a translucent material that takes the colour of the page behind it.</p></div>",
             '<div class="toggle" role="group" aria-label="Theme"><button type="button" data-set-theme="light" aria-pressed="false">Light</button>'
             '<button type="button" data-set-theme="dark" aria-pressed="true">Dark</button></div></header>',
             "<h2>Colour</h2>",
             '<p class="lede">Light and dark side by side. The badge says how each value was read: Sampled (a flat fill, exact), Sampled (text) '
             "(the anti-aliased pixel furthest from the fill), Derived (worked out, or a reading of a material, tint or gradient). Hover a swatch for its capture.</p>",
             "".join(colour_html),
             # PRODUCT (adapt): the palette and ramp captions
             "<h3>Icon tiles (core)</h3><p class=\"lede\">The filled squares behind the Settings icons, the same in both themes: the only saturated colours on the Settings sheet.</p>",
             '<div class="palette">%s</div>' % palette,
             "<h3>Neutral ramp (core)</h3><p class=\"lede\">Every grey the two themes use, light to dark. Named by order, not a published ramp.</p>",
             '<div class="ramp">%s</div>' % neutrals,
             "<h2>Radii</h2>", '<div class="radii">%s</div>' % radii,
             "<h2>Spacing</h2>", spacing, "<h2>Sizes</h2>", sizes,
             "<h2>Type scale</h2>",
             '<div class="scroll"><table class="tokens"><thead><tr><th>Token</th><th>Spec</th><th>Specimen</th></tr></thead><tbody>%s</tbody></table></div>' % type_rows,
             "<h2>Components</h2>", '<p class="lede">Built from the tokens only. Switch the theme to see light.</p>', specimens,
             "<footer>Generated by tools/build_style_guide.py from tokens.json. %s's screenshots and visual system belong to %s; this package holds no %s code or artwork.</footer>" % (esc(NAME), esc(OWNER), esc(NAME)),
             "</div>", "<script>", script, "</script>", "</body>", "</html>", ""]
    OUT.write_text("\n".join(parts), encoding="utf-8")
    return OUT


if __name__ == "__main__":
    print("wrote", build().relative_to(PKG))
