#!/usr/bin/env python3
"""Render style-guide.html from tokens.json (native kit, from systems/grokbot).

    python3 tools/build_style_guide.py

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
NAME = "Notion"     # PRODUCT (adapt)
OWNER = "Notion Labs"  # PRODUCT (adapt): whose visual system it is
LEDE = ("Notion for iOS 26, read from stills captured through iPhone Mirroring on 2026-10-23 (dark) and 2026-10-24 (light).")  # PRODUCT (adapt)
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
    groups_sw = "".join('<div class="chip-sw"><span class="dot sq" style="background:var(%s)"></span><code>%s</code></div>'
                        % (var(p), esc(".".join(p))) for p, t in light if p[:2] == ("color", "group"))
    neutrals = "".join('<div class="ramp-step" style="background:%s" title="%s"><code>%s</code></div>'
                       % (esc(t["$value"]), esc(t["$description"]), esc(p[-1] + " " + t["$value"])) for p, t in under(("color", "neutral")))
    radii = "".join('<div class="radius-box" style="border-radius:%s"><code>%s</code><span>%s</span></div>'
                    % (esc(css(t["$value"])), esc(".".join(p)), esc(t["$value"])) for p, t in under(("radius",)))
    spacing = "".join('<div class="space-row"><code>%s</code><span class="bar" style="width:%s"></span><span>%s</span></div>'
                      % (esc(".".join(p)), esc(css(t["$value"])), esc(t["$value"])) for p, t in under(("space",)))
    sizes = "".join('<div class="space-row"><code>%s</code><span class="bar thin" style="width:%s"></span><span>%s</span></div>'
                    % (esc(".".join(p)), esc(css(t["$value"])), esc(t["$value"])) for p, t in under(("size",)))
    sample = {  # PRODUCT (adapt): specimen text per type style
              "pageTitle": "Databases (Engine)", "heading1": "Local ML model inventory", "heading2": "Method, and what it covers",
              "title": "Notifications", "bodyLarge": "Formula field progress issue", "button": "Chat", "body": "Every model installed on this Mac, whether standalone or managed by a service.",
              "callout": "Ask AI", "subheadline": "Recents", "footnote": "Get push notifications for mentions", "caption": "in Databases (Engine)"}
    type_rows = "".join('<tr><th scope="row"><code>%s</code><span class="desc">%s</span></th><td class="meta">%s, %s%s</td>'
                        '<td><span class="type-%s">%s</span></td></tr>'
                        % (esc(".".join(p)), esc(t["$description"]), esc(t["$value"]["fontSize"]), esc(t["$value"]["fontWeight"]),
                           (", line " + t["$value"]["lineHeight"]) if "lineHeight" in t["$value"] else "", p[-1], esc(sample.get(p[-1], "Sample")))
                        for p, t in under(("typography",)))

    # PRODUCT (adapt): specimens built from tokens only
    specimens = """
<div class="spec-grid">
 <div class="spec phone">
  <h3>Sidebar and bars</h3>
  <div class="screen side">
   <div class="tabs"><span class="tab round">&#9679;</span><span class="tab sel type-callout">&#8962; Home</span><span class="tab">&#9675;</span><span class="tab">&#9633;</span></div>
   <p class="hdr type-subheadline">Favourites &#8964;</p>
   <div class="srow0 type-bodyLarge">Setup call Logs</div>
   <div class="srow0 type-bodyLarge">Operating System</div>
   <p class="hdr type-subheadline">Private &#8964;</p>
   <div class="srow0 type-bodyLarge">local-models-inventory</div>
   <div class="bar"><span class="glass circ">&#9906;</span><span class="glass barpill type-callout">Ask AI</span><span class="glass circ">&#9998;</span></div>
  </div>
  <p class="note">bg.sidebar, surface.tab / tabSelected, size.tab, size.row, text.secondary, surface.glass, size.barButton / barPill</p>
 </div>
 <div class="spec phone">
  <h3>Page and AI chat</h3>
  <div class="screen pg">
   <div class="type-pageTitle">Databases</div>
   <div class="type-heading2">Method</div>
   <p class="type-body">Five agents each took a region, so <code class="ic">~/.cache</code> was covered once.</p>
   <table class="tbl"><tr><th class="type-caption">Region</th><th class="type-caption">Scope</th></tr><tr><td class="type-footnote">Ollama</td><td><code class="ic">~/.ollama</code></td></tr></table>
   <div class="bub type-bodyLarge">Now create the final formula.</div>
   <p class="prose type-bodyLarge">All set. It now shows the distance in the Places database.</p>
   <div class="composer"><span class="type-callout ph">Ask AI</span><span class="crow"><span>+</span><span class="send">&#8593;</span></span></div>
  </div>
  <p class="note">bg.page, typography.pageTitle / heading2 / body, surface.code, text.code, border.table, surface.bubble, text.prose, surface.composer, accent.default</p>
 </div>
 <div class="spec">
  <h3>Sheet with grouped cards</h3>
  <div class="sheetx">
   <div class="grab"></div><p class="stitle type-bodyLarge">Actions</p>
   <div class="card seg"><span class="acc">Ag<small class="type-footnote">Default</small></span><span>Ag<small class="type-footnote">Serif</small></span><span>Ag<small class="type-footnote">Mono</small></span></div>
   <div class="card">
    <div class="srow type-bodyLarge">Add to Favourites</div><div class="srow type-bodyLarge">Duplicate</div><div class="srow type-bodyLarge danger">Move to Bin</div>
   </div>
   <div class="card"><div class="srow type-bodyLarge">Available offline<span class="sw-ctl"></span></div></div>
  </div>
  <p class="note">bg.sheetGrouped, surface.card, radius.card, border.divider, size.rowSheet, text.accent, text.danger, switch.off</p>
 </div>
 <div class="spec">
  <h3>Database, controls, menu</h3>
  <div class="dbf">
   <div class="tool"><span class="chipx type-callout">Areas &#8964;</span><span class="split">+ &#8964;</span></div>
   <div class="grp" style="background:var(--color-group-blue)">Mind (Self)</div>
   <div class="grp" style="background:var(--color-group-green)">Building (Action)</div>
   <div class="grp" style="background:var(--color-group-pink)">Relationships</div>
   <div class="grp" style="background:var(--color-group-orange)">Travel</div>
  </div>
  <div class="row-btns"><span class="ctl type-subheadline">Connect</span><span class="ctl type-subheadline">Off &#8964;</span><button class="btn type-button" type="button">+ Chat</button></div>
  <div class="menu"><p class="type-caption mh">Filter</p><div class="type-bodyLarge">&#10003; Unread and read</div><div class="type-bodyLarge">Unread only</div></div>
  <p class="note">border.frame, radius.frame, surface.chip, accent.default, group.*, size.rowDatabase, border.control, radius.control, button.primary, surface.menu, radius.menu</p>
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
.toggle{display:inline-flex;border-radius:var(--radius-capsule);padding:3px;gap:2px;background:var(--color-surface-tab)}
.toggle button{border:0;background:transparent;color:var(--color-text-secondary);font:inherit;padding:6px 14px;border-radius:var(--radius-capsule);cursor:pointer}
.toggle button[aria-pressed="true"]{background:var(--color-surface-tabSelected);color:var(--color-text-primary)}
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
.chip-sw{display:flex;flex-direction:column;align-items:center;gap:4px;width:130px;font-size:12px;color:var(--color-text-secondary)}
.chip-sw .dot{width:44px;height:44px;border-radius:50%}.chip-sw .dot.sq{width:110px;border-radius:var(--radius-control)}
.ramp{display:flex;flex-wrap:wrap;border-radius:var(--radius-card);overflow:hidden;border:1px solid var(--color-border-separator)}
.ramp-step{flex:1 0 76px;height:64px;display:flex;align-items:flex-end;padding:4px}
.ramp-step code{font-size:10px;background:#0008;color:#fff;padding:0 3px;border-radius:3px}
.radii{display:flex;flex-wrap:wrap;gap:16px}
.radius-box{width:120px;height:80px;background:var(--color-surface-card);border:1px solid var(--color-border-card);display:flex;flex-direction:column;align-items:center;justify-content:center;font-size:12px;color:var(--color-text-secondary)}
.space-row{display:grid;grid-template-columns:minmax(150px,240px) 1fr 70px;align-items:center;gap:12px;padding:3px 0}
.space-row .bar{display:block;height:12px;background:var(--color-accent-default);border-radius:2px;max-width:100%}
.space-row .bar.thin{height:8px;background:var(--color-text-tertiary)}
.spec-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,330px),1fr));gap:16px}
.spec{border:1px solid var(--color-border-separator);border-radius:var(--radius-card);padding:4px 16px 16px;min-width:0}
.screen{border:1px solid var(--color-border-separator);border-radius:var(--radius-sheet);padding:12px var(--space-lg) 16px;max-width:390px}
.screen.side{background:var(--color-bg-sidebar)}.screen.pg{background:var(--color-bg-page);padding:16px var(--space-page)}
.tabs{display:flex;gap:var(--space-sm);margin-bottom:8px}
.tab{height:var(--size-tab);min-width:var(--size-tab);border-radius:var(--radius-capsule);background:var(--color-surface-tab);color:var(--color-text-iconMuted);display:inline-flex;align-items:center;justify-content:center;padding:0 12px}
.tab.sel{background:var(--color-surface-tabSelected);color:var(--color-text-primary);padding:0 22px}
.tab.round{background:var(--color-surface-glass);width:var(--size-avatarButton);padding:0}
.hdr{color:var(--color-text-secondary);margin:18px 0 4px var(--space-xs)}
.srow0{min-height:var(--size-row);display:flex;align-items:center;padding-left:var(--space-xs)}
.bar{display:flex;gap:var(--space-sm);align-items:center;margin-top:24px}
.glass{background:var(--color-surface-glass);color:var(--color-text-iconMuted);display:inline-flex;align-items:center;justify-content:center}
.circ{width:var(--size-barButton);height:var(--size-barButton);border-radius:50%;flex:none;font-size:20px}
.barpill{flex:1;height:var(--size-barPill);border-radius:var(--radius-capsule);justify-content:flex-start;padding:0 16px;color:var(--color-text-secondary)}
.ic{background:var(--color-surface-code);color:var(--color-text-code);padding:1px 4px;border-radius:3px}
.tbl{border-collapse:collapse;margin:10px 0;width:100%}
.tbl th,.tbl td{border:var(--border-width-hairline) solid var(--color-border-table);padding:6px 8px;text-align:left;font-weight:400}
.tbl th{background:var(--color-surface-tableHeader)}
.bub{max-width:80%;margin:14px 0 0 auto;background:var(--color-surface-bubble);color:var(--color-text-prose);border-radius:var(--radius-bubble);padding:var(--space-md) var(--space-lg)}
.prose{color:var(--color-text-prose)}
.composer{background:var(--color-surface-composer);border-radius:var(--radius-composer);height:var(--size-composer);padding:12px 16px;display:flex;flex-direction:column;justify-content:space-between}
.composer .ph{color:var(--color-text-placeholder)}
.crow{display:flex;justify-content:space-between;align-items:center;color:var(--color-text-icon)}
.send{width:var(--size-sendButton);height:var(--size-sendButton);border-radius:50%;background:var(--color-accent-default);color:var(--color-text-onAccent);display:inline-flex;align-items:center;justify-content:center;font-weight:600}
.sheetx{background:var(--color-bg-sheetGrouped);border-radius:var(--radius-sheet) var(--radius-sheet) 0 0;padding:8px var(--space-lg) 16px;max-width:390px}
.grab{width:38px;height:5px;border-radius:3px;background:var(--color-surface-grabber);margin:0 auto}
.stitle{text-align:center;font-weight:600;margin:8px 0 16px}
.card{background:var(--color-surface-card);border-radius:var(--radius-card);overflow:hidden;margin-bottom:var(--space-lg)}
.seg{display:flex;justify-content:space-around;padding:14px 0;font-size:24px;text-align:center}
.seg small{display:block;color:var(--color-text-secondary)}.seg .acc{color:var(--color-text-accent)}
.srow{display:flex;justify-content:space-between;align-items:center;min-height:var(--size-rowSheet);padding:0 var(--space-lg);border-bottom:var(--border-width-hairline) solid var(--color-border-divider)}
.srow:last-child{border-bottom:0}
.danger{color:var(--color-text-danger)}
.sw-ctl{position:relative;flex:none;width:var(--size-switch-width);height:var(--size-switch-height);border-radius:var(--radius-capsule);background:var(--color-switch-off)}
.sw-ctl::after{content:"";position:absolute;top:2px;left:2px;width:var(--size-switch-thumb);height:calc(var(--size-switch-height) - 4px);border-radius:var(--radius-capsule);background:var(--color-switch-thumb)}
.dbf{border:var(--border-width-hairline) solid var(--color-border-frame);border-radius:var(--radius-frame);padding:10px 16px;background:var(--color-bg-page)}
.tool{display:flex;justify-content:space-between;align-items:center;margin-bottom:8px}
.chipx{height:var(--size-chip);border-radius:var(--radius-capsule);background:var(--color-surface-chip);display:inline-flex;align-items:center;padding:0 14px}
.split{height:var(--size-splitButton);border-radius:var(--radius-frame);background:var(--color-accent-default);color:var(--color-text-onAccent);display:inline-flex;align-items:center;padding:0 12px}
.grp{height:calc(var(--size-rowDatabase) - 2px);margin-bottom:2px;display:flex;align-items:center;padding:0 12px}
.row-btns{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin-top:14px}
.ctl{height:var(--size-control);padding:0 10px;border:var(--border-width-hairline) solid var(--color-button-secondary-border);border-radius:var(--radius-control);color:var(--color-button-secondary-text);display:inline-flex;align-items:center}
.btn{height:var(--size-button);padding:0 22px;border:0;border-radius:var(--radius-capsule);background:var(--color-button-primary-bg);color:var(--color-button-primary-text);font-family:var(--font-base)}
.menu{margin-top:14px;width:250px;max-width:100%;border-radius:var(--radius-menu);background:var(--color-surface-menu);color:var(--color-text-menu);padding:8px 0}
.menu div{padding:8px 24px}.menu .mh{color:var(--color-text-menuSecondary);margin:4px 24px}
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
             "Glass is drawn as its centre colour: the real material blurs what is behind it.</p></div>",
             '<div class="toggle" role="group" aria-label="Theme"><button type="button" data-set-theme="light" aria-pressed="false">Light</button>'
             '<button type="button" data-set-theme="dark" aria-pressed="true">Dark</button></div></header>',
             "<h2>Colour</h2>",
             '<p class="lede">Light and dark side by side. The badge says how each value was read: Sampled (a flat fill, exact), Sampled (text) '
             "(the anti-aliased pixel furthest from the fill), Derived (worked out, or a glass or gradient reading). Hover a swatch for its capture.</p>",
             "".join(colour_html),
             # PRODUCT (adapt): the palette and ramp captions
             "<h3>Database group colours</h3><p class=\"lede\">The four group backgrounds on screen, in the current theme. Rows sit on them with primary text.</p>",
             '<div class="palette">%s</div>' % groups_sw,
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
