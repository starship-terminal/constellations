#!/usr/bin/env python3
"""Render style-guide.html from tokens.json (native kit, from systems/grokbot; light only for Grab).

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
DISPLAY_STACK = 'ui-rounded, "SF Pro Rounded", -apple-system, system-ui, "Helvetica Neue", Arial, sans-serif'
NAME = "Grab"   # PRODUCT (adapt)
OWNER = "Grab Holdings"    # PRODUCT (adapt): whose visual system it is
LEDE = ("Grab for iOS, read from stills captured through iPhone Mirroring on 2026-10-23. Grab has one theme: it stays light with the phone in dark mode.")  # PRODUCT (adapt)
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
    core, light = (list(walk(data[s])) for s in ("core", "light"))
    core_by, light_by = dict(core), dict(light)

    core_css, type_css = [], []
    for p, t in core:
        if t["$type"] == "typography":
            v = t["$value"]
            fam = "var(--font-display)" if "display" in v["fontFamily"] else "var(--font-base)"
            type_css.append(".type-%s{font-family:%s;font-weight:%s;font-size:%s;line-height:%s}"
                            % (p[-1], fam, css(v["fontWeight"]), v["fontSize"], v.get("lineHeight", "1.25")))
        elif t["$type"] == "fontFamily":
            core_css.append("%s:%s" % (var(p), DISPLAY_STACK if p[-1] == "display" else FONT_STACK))
        else:
            core_css.append("%s:%s" % (var(p), css(t["$value"])))
    core_css += ["--font-base:%s" % FONT_STACK, "--font-display:%s" % DISPLAY_STACK, "--font-mono:%s" % MONO_STACK]
    light_css = ["%s:%s" % (var(p), css(t["$value"])) for p, t in light]

    # ---- semantic colours (one theme)
    groups = {}
    for p, t in light:
        groups.setdefault(p[1], []).append((p, t))
    colour_html = []
    for g, items in groups.items():
        rows = "".join('<tr><th scope="row"><code>%s</code><span class="desc">%s</span></th>%s</tr>'
                       % (esc(".".join(p)), esc(t["$description"]), swatch_cell(t, light_by, core_by)) for p, t in items)
        colour_html.append('<h3>%s</h3><div class="scroll"><table class="tokens"><thead><tr><th>Token</th><th>Light</th>'
                           '</tr></thead><tbody>%s</tbody></table></div>' % (esc(g), rows))

    under = lambda pre: [(p, t) for p, t in core if p[:len(pre)] == pre]
    palette = "".join('<div class="chip-sw"><span class="dot" style="background:%s"></span><code>%s</code><span>%s</span></div>'
                      % (esc(css(t["$value"])), esc(".".join(p)), esc(t["$value"]))
                      for p, t in under(("color", "brand")) + under(("color", "service")))
    neutrals = "".join('<div class="ramp-step" style="background:%s" title="%s"><code>%s</code></div>'
                       % (esc(t["$value"]), esc(t["$description"]), esc(p[-1] + " " + t["$value"])) for p, t in under(("color", "neutral")))
    radii = "".join('<div class="radius-box" style="border-radius:%s"><code>%s</code><span>%s</span></div>'
                    % (esc(css(t["$value"])), esc(".".join(p)), esc(t["$value"])) for p, t in under(("radius",)))
    spacing = "".join('<div class="space-row"><code>%s</code><span class="bar" style="width:%s"></span><span>%s</span></div>'
                      % (esc(".".join(p)), esc(css(t["$value"])), esc(t["$value"])) for p, t in under(("space",)))
    sizes = "".join('<div class="space-row"><code>%s</code><span class="bar thin" style="width:%s"></span><span>%s</span></div>'
                    % (esc(".".join(p)), esc(css(t["$value"])), esc(t["$value"])) for p, t in under(("size",)))
    sample = {  # PRODUCT (adapt): specimen text per type style
        "largeTitle": "Activity", "sheetTitle": "Timely updates for a stress-free experience", "display": "Night munchies",
        "title": "For more value", "button": "Book Standard", "body": "Subscriptions", "chip": "Transport",
        "subhead": "May contain dairy, egg, or alliums", "label": "Finance", "caption": "Messages"}
    type_rows = "".join('<tr><th scope="row"><code>%s</code><span class="desc">%s</span></th><td class="meta">%s, %s%s</td>'
                        '<td><span class="type-%s">%s</span></td></tr>'
                        % (esc(".".join(p)), esc(t["$description"]), esc(t["$value"]["fontSize"]), esc(t["$value"]["fontWeight"]),
                           (", line " + t["$value"]["lineHeight"]) if "lineHeight" in t["$value"] else "", p[-1], esc(sample.get(p[-1], "Sample")))
                        for p, t in under(("typography",)))

    # PRODUCT (adapt): specimens built from tokens only
    specimens = """
<div class="spec-grid">
 <div class="spec phone">
  <h3>Home header, shortcut cards, tab bar</h3>
  <div class="screen flush">
   <div class="hdr"><span class="hsearch type-body">&#9906; Search places</span></div>
   <div class="pad">
    <div class="cards"><div class="mini"><span class="type-label sec">Finance</span><b class="type-body">S$0.00</b></div><div class="mini"><span class="type-label sec">Ride to</span><b class="type-body">&#160;</b></div></div>
    <div class="row-btns"><span class="chip on type-chip">All</span><span class="chip type-chip">Transport</span><span class="chip type-chip">Food</span></div>
   </div>
   <div class="tabbar"><span class="ti act type-caption">&#8962;<br>Home</span><span class="ti type-caption">&#9678;<br>Moments</span><span class="scan">&#9635;</span><span class="ti type-caption">&#9636;<br>Activity</span><span class="ti type-caption">&#9993;<br>Messages</span></div>
  </div>
  <p class="note">bg.header, surface.card, border.card, size.card.height, chip.selected / default, size.chip, nav.active / inactive / scan, size.scanButton</p>
 </div>
 <div class="spec phone">
  <h3>Bottom sheet with two buttons</h3>
  <div class="screen scrimmed">
   <div class="sheet">
    <div class="art"></div>
    <p class="type-sheetTitle">Timely updates for a stress-free experience</p>
    <p class="type-body sec">Keep your delivery on track with real-time updates.</p>
    <button class="btn type-button" type="button">Yes</button>
    <button class="btn second type-button" type="button">Later</button>
   </div>
  </div>
  <p class="note">bg.scrim, surface.sheet, radius.sheet, button.primary / secondary, size.button, radius.capsule, typography.sheetTitle</p>
 </div>
 <div class="spec">
  <h3>List with status labels, tabs, link</h3>
  <div class="tabs"><span class="tab type-chip">Following</span><span class="tab act type-chip">For you</span><span class="tab type-chip">Top posts</span></div>
  <div class="lhead"><span class="type-title">Recent</span><span class="type-body link">View History</span></div>
  <div class="trip"><span class="type-label danger">Cancelled</span><span class="type-body">to i12 Katong</span><span class="type-label sec">8 Oct 2026, 14:30</span></div>
  <div class="trip"><span class="type-label ok">Bill paid</span><span class="type-body">Huong Pho</span><span class="type-label sec">27 Sep 2026, 17:31</span><span class="price type-body">S$18.72</span></div>
  <p class="note">tab.active / inactive / indicator, text.danger, text.success, text.secondary, text.link, border.divider</p>
 </div>
 <div class="spec">
  <h3>Fields, checkboxes, disabled and compact buttons</h3>
  <div class="field type-body">Home</div>
  <div class="field focus type-body"><i class="caret"></i><span class="ph">Find airports by flight no.</span></div>
  <div class="gfield type-body"><span class="ph2">&#9906; Search food</span></div>
  <div class="crow"><span class="type-body">Halal</span><span class="box"></span></div>
  <div class="crow"><span class="type-body">Non-pork</span><span class="box"></span></div>
  <button class="btn dis type-button" type="button" disabled>Save</button>
  <div class="row-btns"><span class="buy type-chip">Buy</span><span class="badge type-label">New</span><span class="tip type-label">Save posts that you like</span></div>
  <div class="flash type-body"><b>25% off flash deals</b><span><i>14</i>:<i>24</i></span></div>
  <p class="note">border.field, focus.ring / glow / caret, surface.field, border.control, size.checkbox, button.disabled, button.compact, badge.new, surface.tooltip, badge.discount, color.service.timer</p>
 </div>
</div>
"""

    page_css = """
*{box-sizing:border-box}
html,body{background:var(--color-bg-page)}
body{margin:0;color:var(--color-text-primary);font-family:var(--font-base);font-size:15px;line-height:1.45}
.wrap{max-width:1080px;margin:0 auto;padding:24px 16px 64px}
h1{font-family:var(--font-display);font-size:26px;margin:0}h2{font-family:var(--font-display);font-size:20px;margin:40px 0 8px}h3{font-size:15px;margin:20px 0 8px}
p.lede{color:var(--color-text-secondary);margin:4px 0 0;max-width:70ch}p.note{color:var(--color-text-secondary);font-size:12px;margin:10px 0 0}
code{font-family:var(--font-mono);font-size:12px}
.scroll{overflow-x:auto}
table.tokens{border-collapse:collapse;width:100%;min-width:520px}
table.tokens th,table.tokens td{text-align:left;vertical-align:top;padding:8px 10px;border-bottom:var(--border-width-hairline) solid var(--color-border-divider)}
table.tokens thead th{color:var(--color-text-secondary);font-size:12px;font-weight:400}
table.tokens th[scope=row]{font-weight:500;width:55%}
.desc{display:block;color:var(--color-text-secondary);font-size:12px;font-weight:400;margin-top:2px}
.meta{color:var(--color-text-secondary);white-space:nowrap}
.sw{display:inline-block;width:28px;height:28px;border-radius:8px;vertical-align:middle;margin-right:8px;border:1px solid var(--color-border-divider);background-image:linear-gradient(45deg,#8883 25%,transparent 25%,transparent 75%,#8883 75%),linear-gradient(45deg,#8883 25%,transparent 25%,transparent 75%,#8883 75%);background-size:8px 8px;background-position:0 0,4px 4px;overflow:hidden}
.sw i{display:block;width:100%;height:100%}
.ev{display:inline-block;font-size:11px;padding:1px 7px;border-radius:var(--radius-capsule);border:1px solid var(--color-border-divider);color:var(--color-text-secondary);white-space:nowrap}
.ev-derived{border-style:dashed}.ev-none{border-style:dotted}
.palette{display:flex;flex-wrap:wrap;gap:12px}
.chip-sw{display:flex;flex-direction:column;align-items:center;gap:4px;width:110px;font-size:12px;color:var(--color-text-secondary);text-align:center}
.chip-sw .dot{width:44px;height:44px;border-radius:50%;border:1px solid var(--color-border-divider)}
.ramp{display:flex;flex-wrap:wrap;border-radius:var(--radius-card);overflow:hidden;border:1px solid var(--color-border-divider)}
.ramp-step{flex:1 0 76px;height:64px;display:flex;align-items:flex-end;padding:4px}
.ramp-step code{font-size:10px;background:#0008;color:#fff;padding:0 3px;border-radius:3px}
.radii{display:flex;flex-wrap:wrap;gap:16px}
.radius-box{width:120px;height:80px;background:var(--color-surface-card);border:1px solid var(--color-border-card);display:flex;flex-direction:column;align-items:center;justify-content:center;font-size:12px;color:var(--color-text-secondary)}
.space-row{display:grid;grid-template-columns:minmax(150px,240px) 1fr 70px;align-items:center;gap:12px;padding:3px 0}
.space-row .bar{display:block;height:12px;background:var(--color-accent-default);border-radius:2px;max-width:100%}
.space-row .bar.thin{height:8px;background:var(--color-text-secondary)}
.spec-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,330px),1fr));gap:16px}
.spec{border:1px solid var(--color-border-divider);border-radius:var(--radius-card);padding:4px 16px 16px;min-width:0}
.screen{background:var(--color-bg-page);border:1px solid var(--color-border-divider);border-radius:var(--radius-sheet);padding:12px var(--space-screenMargin) 16px;max-width:390px;overflow:hidden;position:relative}
.screen.flush{padding:0}.pad{padding:12px var(--space-screenMargin)}
.hdr{background:linear-gradient(var(--color-bg-header),var(--color-bg-headerEnd));padding:28px var(--space-screenMargin) 16px}
.hsearch{display:flex;align-items:center;height:var(--size-field);border-radius:var(--radius-field);background:var(--color-surface-card);color:var(--color-text-placeholder);padding:0 12px}
.cards{display:grid;grid-template-columns:1fr 1fr;gap:var(--space-md)}
.mini{height:var(--size-card-height);border:var(--border-width-default) solid var(--color-border-card);border-radius:var(--radius-card);padding:6px 14px;display:flex;flex-direction:column;justify-content:center;background:var(--color-surface-card)}
.sec{color:var(--color-text-secondary)}.danger{color:var(--color-text-danger)}.ok{color:var(--color-text-success)}.link{color:var(--color-text-link)}
.row-btns{display:flex;flex-wrap:wrap;gap:var(--space-sm);align-items:center;margin-top:14px}
.chip{height:var(--size-chip);padding:0 16px;border-radius:var(--radius-capsule);background:var(--color-chip-default-bg);color:var(--color-chip-default-text);display:inline-flex;align-items:center}
.chip.on{background:var(--color-chip-selected-bg);color:var(--color-chip-selected-text)}
.tabbar{display:flex;justify-content:space-around;align-items:center;border-top:var(--border-width-hairline) solid var(--color-border-divider);padding:8px 4px 14px;margin-top:20px}
.ti{color:var(--color-nav-inactive);text-align:center;font-size:18px}.ti.act{color:var(--color-nav-active)}
.scan{width:var(--size-scanButton);height:var(--size-scanButton);border-radius:50%;background:var(--color-nav-scan);color:var(--color-text-onPrimary);display:inline-flex;align-items:center;justify-content:center;font-size:24px;margin-top:-20px}
.scrimmed{background:var(--color-bg-page);padding:120px 0 0}
.scrimmed::before{content:"";position:absolute;inset:0;background:var(--color-bg-scrim)}
.sheet{position:relative;background:var(--color-surface-sheet);border-radius:var(--radius-sheet) var(--radius-sheet) 0 0;padding:20px var(--space-screenMargin) 20px}
.sheet p{margin:10px 0}
.art{height:110px;border-radius:var(--radius-card);background:var(--color-brand-mint)}
.btn{display:block;width:100%;height:var(--size-button);margin:12px 0 0;border:0;border-radius:var(--radius-capsule);background:var(--color-button-primary-bg);color:var(--color-button-primary-text);font-family:var(--font-base)}
.btn.second{background:var(--color-button-secondary-bg);color:var(--color-button-secondary-text)}
.btn.dis{background:var(--color-button-disabled-bg);color:var(--color-button-disabled-text)}
.tabs{display:flex;justify-content:space-around;border-bottom:var(--border-width-hairline) solid var(--color-border-divider);background:var(--color-bg-tint)}
.tab{padding:10px 8px;color:var(--color-tab-inactive)}.tab.act{color:var(--color-tab-active);box-shadow:inset 0 -3px 0 var(--color-tab-indicator)}
.lhead{display:flex;justify-content:space-between;align-items:baseline;margin:16px 0 4px}
.trip{display:grid;grid-template-columns:1fr auto;gap:2px 12px;padding:12px 0;border-bottom:var(--border-width-hairline) solid var(--color-border-divider)}
.trip>span{grid-column:1}.trip .price{grid-column:2;grid-row:1}
.field{height:var(--size-field);border:var(--border-width-default) solid var(--color-border-field);border-radius:var(--radius-field);display:flex;align-items:center;padding:0 14px;margin-bottom:10px}
.field.focus{border-color:var(--color-focus-ring);box-shadow:0 0 0 3px var(--color-focus-glow)}
.caret{display:inline-block;width:1.5px;height:20px;background:var(--color-focus-caret);margin-right:2px}
.ph{color:var(--color-text-placeholder)}.ph2{color:var(--color-text-placeholder)}
.gfield{height:var(--size-field);border-radius:var(--radius-field);background:var(--color-surface-field);display:flex;align-items:center;padding:0 14px}
.crow{display:flex;justify-content:space-between;align-items:center;min-height:var(--size-row)}
.box{width:var(--size-checkbox);height:var(--size-checkbox);border:var(--border-width-control) solid var(--color-border-control);border-radius:5px}
.buy{height:var(--size-buttonCompact);padding:0 16px;border-radius:var(--radius-capsule);background:var(--color-button-compact-bg);color:var(--color-button-compact-text);display:inline-flex;align-items:center}
.badge{padding:1px 8px;border-radius:var(--radius-capsule);background:var(--color-badge-new);color:var(--color-text-onPrimary)}
.tip{padding:8px 12px;border-radius:var(--radius-tooltip);background:var(--color-surface-tooltip);color:var(--color-text-onTooltip)}
.flash{display:flex;justify-content:space-between;align-items:center;margin-top:14px;padding:10px 16px;border-radius:var(--radius-card);background:var(--color-badge-discount);color:var(--color-text-onPrimary)}
.flash i{font-style:normal;background:var(--color-service-timer);border-radius:6px;padding:0 6px;margin:0 2px}
footer{margin-top:48px;color:var(--color-text-secondary);font-size:12px}
""".strip()

    parts = ["<!doctype html>", '<html lang="en" data-theme="light">', "<head>", '<meta charset="utf-8">',
             '<meta name="viewport" content="width=device-width, initial-scale=1">', "<title>%s style guide</title>" % esc(NAME), "<style>",
             ":root{%s}" % ";".join(core_css),
             ':root,:root[data-theme="light"]{color-scheme:light;%s}' % ";".join(light_css),
             "\n".join(type_css), page_css, "</style>", "</head>", "<body>", '<div class="wrap">',
             '<header class="top"><div><h1>%s style guide</h1>' % esc(NAME),
             '<p class="lede">%s Every value below comes from tokens.json; points are 1:1 with CSS pixels. ' % esc(LEDE)
             + "The fonts are not known, so the page uses the platform sans for text and a rounded system face for titles. "
             "There is no theme toggle: dark is not applicable.</p></div></header>",
             "<h2>Colour</h2>",
             '<p class="lede">The badge says how each value was read: Sampled (a flat fill, exact), Sampled (text) '
             "(the anti-aliased pixel furthest from the fill), Derived (worked out, or a gradient or thin-line reading). Hover a swatch for its capture.</p>",
             "".join(colour_html),
             # PRODUCT (adapt): the palette and ramp captions
             "<h3>Brand and service colours (core)</h3><p class=\"lede\">Grab green and its darker greens, the mint that backs secondary controls, and the colours each service header uses.</p>",
             '<div class="palette">%s</div>' % palette,
             "<h3>Neutral ramp (core)</h3><p class=\"lede\">Every grey the app uses, light to dark. Named by order, not a published ramp.</p>",
             '<div class="ramp">%s</div>' % neutrals,
             "<h2>Radii</h2>", '<div class="radii">%s</div>' % radii,
             "<h2>Spacing</h2>", spacing, "<h2>Sizes</h2>", sizes,
             "<h2>Type scale</h2>",
             '<div class="scroll"><table class="tokens"><thead><tr><th>Token</th><th>Spec</th><th>Specimen</th></tr></thead><tbody>%s</tbody></table></div>' % type_rows,
             "<h2>Components</h2>", '<p class="lede">Built from the tokens only, with no Grab artwork.</p>', specimens,
             "<footer>Generated by tools/build_style_guide.py from tokens.json. %s's screenshots and visual system belong to %s; this package holds no %s code or artwork.</footer>" % (esc(NAME), esc(OWNER), esc(NAME)),
             "</div>", "</body>", "</html>", ""]
    OUT.write_text("\n".join(parts), encoding="utf-8")
    return OUT


if __name__ == "__main__":
    print("wrote", build().relative_to(PKG))
