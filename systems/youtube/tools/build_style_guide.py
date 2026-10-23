#!/usr/bin/env python3
"""Render style-guide.html from tokens.json (native kit, from systems/grokbot).

    python3 tools/build_style_guide.py

Adapted for YouTube from the native kit (tools/kit/native, from systems/grokbot).

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
NAME = "YouTube"   # PRODUCT (adapt)
OWNER = "Google"    # PRODUCT (adapt): whose visual system it is
LEDE = ("YouTube for iOS, read from stills captured through iPhone Mirroring on 2026-10-23 (dark) and 2026-10-24 (light).")  # PRODUCT (adapt)
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
                      % (esc(css(t["$value"])), esc(".".join(p)), esc(t["$value"])) for p, t in under(("color", "red")))
    neutrals = "".join('<div class="ramp-step" style="background:%s" title="%s"><code>%s</code></div>'
                       % (esc(t["$value"]), esc(t["$description"]), esc(p[-1] + " " + t["$value"])) for p, t in under(("color", "neutral")))
    radii = "".join('<div class="radius-box" style="border-radius:%s"><code>%s</code><span>%s</span></div>'
                    % (esc(css(t["$value"])), esc(".".join(p)), esc(t["$value"])) for p, t in under(("radius",)))
    spacing = "".join('<div class="space-row"><code>%s</code><span class="bar" style="width:%s"></span><span>%s</span></div>'
                      % (esc(".".join(p)), esc(css(t["$value"])), esc(t["$value"])) for p, t in under(("space",)))
    sizes = "".join('<div class="space-row"><code>%s</code><span class="bar thin" style="width:%s"></span><span>%s</span></div>'
                    % (esc(".".join(p)), esc(css(t["$value"])), esc(t["$value"])) for p, t in under(("size",)))
    sample = {  # PRODUCT (adapt): specimen text per type style
        "display": "Try something new", "sheetTitle": "About this sheet", "navTitle": "Settings", "sectionTitle": "History",
        "body": "Play next in queue", "videoTitle": "How to make a good launch video", "label": "Watch",
        "meta": "Channel name \u00b7 12K views \u00b7 3 days ago", "tab": "Home"}
    type_rows = "".join('<tr><th scope="row"><code>%s</code><span class="desc">%s</span></th><td class="meta">%s, %s%s</td>'
                        '<td><span class="type-%s">%s</span></td></tr>'
                        % (esc(".".join(p)), esc(t["$description"]), esc(t["$value"]["fontSize"]), esc(t["$value"]["fontWeight"]),
                           (", line " + t["$value"]["lineHeight"]) if "lineHeight" in t["$value"] else "", p[-1], esc(sample.get(p[-1], "Sample")))
                        for p, t in under(("typography",)))

    # PRODUCT (adapt): specimens built from tokens only
    specimens = """
<div class="spec-grid">
 <div class="spec phone">
  <h3>Feed: chips, video card, tab bar</h3>
  <div class="screen">
   <div class="chips"><span class="chip on type-label">All</span><span class="chip type-label">Today</span><span class="chip type-label">Videos</span><span class="chip type-label">Live</span></div>
   <div class="thumb"><span class="dur type-meta">12:34</span><span class="prog"></span></div>
   <div class="vrow"><span class="av ch"></span><div><div class="type-videoTitle">How to make a good launch video</div><div class="type-meta sec">Channel name &#183; 12K views &#183; 3 days ago</div></div><span class="sec">&#8943;</span></div>
   <div class="tabbar"><span class="type-tab">Home</span><span class="type-tab">Shorts</span><span class="create">+</span><span class="type-tab">Subscriptions</span><span class="type-tab">You</span></div>
  </div>
  <p class="note">surface.secondary, surface.inverse, radius.chip, overlay.duration, brand.red, size.avatarChannel, surface.tabBar, border.tabBar, size.createButton</p>
 </div>
 <div class="spec phone">
  <h3>Ad card and buttons</h3>
  <div class="screen">
   <div class="ad"><div class="type-videoTitle">Shop for less this week</div><div class="type-meta sec">Sponsored &#183; Advertiser</div>
    <div class="pair"><span class="btn tonal type-label">Watch</span><span class="btn filled type-label">Install</span></div></div>
   <div class="pair"><span class="pill type-label">View channel</span><span class="pill outl type-label">Get Premium</span></div>
   <div class="search type-body">Search YouTube</div>
  </div>
  <p class="note">surface.ad, button.tonal, button.filled, button.pill, button.outlined, size.button, size.pill, size.searchField, radius.capsule</p>
 </div>
 <div class="spec">
  <h3>Settings rows and switches</h3>
  <div class="list">
   <div class="srow"><span class="type-body">Appearance</span><span class="type-meta sec">Use device theme</span></div>
   <div class="srow"><span class="type-body">Rotate screen<span class="type-meta sec blk">Enable landscape layout when you rotate your device</span></span><span class="sw-ctl"></span></div>
   <div class="srow"><span class="type-body">Earn badges</span><span class="sw-ctl on"></span></div>
  </div>
  <p class="secthead type-sectionTitle">Account</p>
  <div class="list"><div class="srow"><span class="type-body">General</span></div><div class="srow"><span class="type-body">Notifications</span></div></div>
  <p class="note">size.row, text.secondary, switch.onTrack / onThumb / offTrack / offThumb, typography.sectionTitle</p>
 </div>
 <div class="spec">
  <h3>Sheet, menu, comments</h3>
  <div class="sheet"><span class="grab"></span><div class="type-body"><span class="tick">&#10003;</span>Recent</div><div class="type-body ind">A&#8211;Z</div><div class="type-body ind">Z&#8211;A</div></div>
  <div class="menu"><div class="type-body">Play next in queue</div><div class="type-body">Save to Watch Later</div><div class="type-body">Share</div></div>
  <div class="comments"><span class="type-label">Comments</span><div class="cfield type-meta">Comment...</div></div>
  <p class="note">bg.sheet, radius.sheet, icon.grabber, icon.check, surface.menu, radius.menu, surface.card, surface.field, size.commentField</p>
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
.toggle{display:inline-flex;border-radius:var(--radius-capsule);padding:3px;gap:2px;background:var(--color-surface-secondary)}
.toggle button{border:0;background:transparent;color:var(--color-text-secondary);font:inherit;padding:6px 14px;border-radius:var(--radius-capsule);cursor:pointer}
.toggle button[aria-pressed="true"]{background:var(--color-surface-inverse);color:var(--color-text-inverse)}
.scroll{overflow-x:auto}
table.tokens{border-collapse:collapse;width:100%;min-width:660px}
table.tokens th,table.tokens td{text-align:left;vertical-align:top;padding:8px 10px;border-bottom:var(--border-width-hairline) solid var(--color-border-outline)}
table.tokens thead th{color:var(--color-text-secondary);font-size:12px;font-weight:400}
table.tokens th[scope=row]{font-weight:500;width:40%}
.desc{display:block;color:var(--color-text-secondary);font-size:12px;font-weight:400;margin-top:2px}
.meta{color:var(--color-text-secondary);white-space:nowrap}
.sw{display:inline-block;width:28px;height:28px;border-radius:8px;vertical-align:middle;margin-right:8px;border:1px solid var(--color-border-outline);background-image:linear-gradient(45deg,#8883 25%,transparent 25%,transparent 75%,#8883 75%),linear-gradient(45deg,#8883 25%,transparent 25%,transparent 75%,#8883 75%);background-size:8px 8px;background-position:0 0,4px 4px;overflow:hidden}
.sw i{display:block;width:100%;height:100%}
.ev{display:inline-block;font-size:11px;padding:1px 7px;border-radius:var(--radius-capsule);border:1px solid var(--color-border-outline);color:var(--color-text-secondary);white-space:nowrap}
.ev-derived{border-style:dashed}.ev-none{border-style:dotted}
.palette{display:flex;flex-wrap:wrap;gap:12px}
.chip-sw{display:flex;flex-direction:column;align-items:center;gap:4px;width:84px;font-size:12px;color:var(--color-text-secondary)}
.chip-sw .dot{width:44px;height:44px;border-radius:50%}
.ramp{display:flex;flex-wrap:wrap;border-radius:var(--radius-card);overflow:hidden;border:1px solid var(--color-border-outline)}
.ramp-step{flex:1 0 76px;height:64px;display:flex;align-items:flex-end;padding:4px}
.ramp-step code{font-size:10px;background:#0008;color:#fff;padding:0 3px;border-radius:3px}
.radii{display:flex;flex-wrap:wrap;gap:16px}
.radius-box{width:120px;height:80px;background:var(--color-surface-card);border:1px solid var(--color-border-outline);display:flex;flex-direction:column;align-items:center;justify-content:center;font-size:12px;color:var(--color-text-secondary)}
.space-row{display:grid;grid-template-columns:minmax(150px,240px) 1fr 70px;align-items:center;gap:12px;padding:3px 0}
.space-row .bar{display:block;height:12px;background:var(--color-accent-default);border-radius:2px;max-width:100%}
.space-row .bar.thin{height:8px;background:var(--color-text-secondary)}
.spec-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,330px),1fr));gap:16px}
.spec{border:1px solid var(--color-border-outline);border-radius:var(--radius-card);padding:4px 16px 16px;min-width:0}
.screen{background:var(--color-bg-page);border:1px solid var(--color-border-outline);border-radius:var(--radius-card);padding:12px 0 0;max-width:390px;overflow:hidden}
.sec{color:var(--color-text-secondary)}.blk{display:block}
.chips{display:flex;gap:var(--space-sm);padding:0 var(--space-screenMargin);overflow:hidden}
.chip{flex:none;height:var(--size-chip);padding:0 12px;border-radius:var(--radius-chip);background:var(--color-surface-secondary);color:var(--color-text-primary);display:inline-flex;align-items:center}
.chip.on{background:var(--color-surface-inverse);color:var(--color-text-inverse)}
.thumb{position:relative;margin-top:var(--space-md);aspect-ratio:16/9;background:linear-gradient(135deg,var(--color-surface-secondary),var(--color-surface-menu))}
.dur{position:absolute;right:8px;bottom:10px;padding:1px 5px;border-radius:var(--radius-capsule);background:var(--color-overlay-duration);color:#fff}
.prog{position:absolute;left:0;bottom:0;height:3px;width:35%;background:var(--color-brand-red)}
.vrow{display:flex;gap:10px;align-items:flex-start;padding:var(--space-md) var(--space-screenMargin)}.vrow>div{flex:1}
.av{display:inline-block;border-radius:50%;background:var(--color-surface-secondary)}.av.ch{flex:none;width:var(--size-avatarChannel);height:var(--size-avatarChannel)}
.tabbar{display:flex;justify-content:space-around;align-items:center;height:var(--size-tabBar);background:var(--color-surface-tabBar);border-top:var(--border-width-hairline) solid var(--color-border-tabBar);color:var(--color-text-tab);margin-top:var(--space-lg)}
.create{width:var(--size-createButton);height:var(--size-createButton);border-radius:50%;background:var(--color-surface-createButton);display:inline-flex;align-items:center;justify-content:center;font-size:22px}
.ad{background:var(--color-surface-ad);padding:var(--space-md) var(--space-screenMargin)}
.pair{display:flex;gap:var(--space-sm);margin:var(--space-md) 0}
.screen>.pair{padding:0 var(--space-screenMargin)}
.btn,.pill{flex:1;display:inline-flex;align-items:center;justify-content:center;border-radius:var(--radius-capsule)}
.btn{height:var(--size-button)}.pill{height:var(--size-pill)}
.btn.tonal{background:var(--color-button-tonal-bg);color:var(--color-button-tonal-text)}
.btn.filled{background:var(--color-button-filled-bg);color:var(--color-button-filled-text)}
.pill{background:var(--color-button-pill-bg);color:var(--color-button-pill-text)}
.pill.outl{background:var(--color-button-outlined-bg);color:var(--color-text-primary);border:var(--border-width-outline) solid var(--color-button-outlined-border)}
.search{height:var(--size-searchField);border-radius:var(--radius-capsule);background:var(--color-surface-secondary);color:var(--color-text-placeholder);display:flex;align-items:center;padding:0 16px;margin:0 var(--space-screenMargin) 16px}
.list{background:var(--color-bg-page);max-width:358px}
.srow{display:flex;justify-content:space-between;align-items:center;gap:12px;min-height:var(--size-row);padding:6px 0}
.secthead{margin:16px 0 0}
.sw-ctl{position:relative;flex:none;width:var(--size-switch-width);height:var(--size-switch-height);border-radius:var(--radius-capsule);background:var(--color-switch-offTrack)}
.sw-ctl::after{content:"";position:absolute;top:50%;left:-2px;width:var(--size-switch-thumb);height:var(--size-switch-thumb);margin-top:calc(var(--size-switch-thumb) / -2);border-radius:50%;background:var(--color-switch-offThumb)}
.sw-ctl.on{background:var(--color-switch-onTrack)}.sw-ctl.on::after{left:auto;right:-2px;background:var(--color-switch-onThumb)}
.sheet{background:var(--color-bg-sheet);border-radius:var(--radius-sheet) var(--radius-sheet) 0 0;padding:10px 16px 12px;max-width:358px;border:1px solid var(--color-border-outline)}
.sheet>div{min-height:48px;display:flex;align-items:center}
.grab{display:block;width:40px;height:4px;border-radius:2px;background:var(--color-icon-grabber);margin:0 auto 4px}
.tick{color:var(--color-icon-check);width:34px}.ind{padding-left:34px}
.menu{margin-top:14px;width:var(--size-menuWidth);max-width:100%;border-radius:var(--radius-menu);background:var(--color-surface-menu);padding:8px 0;border:1px solid var(--color-border-outline)}
.menu div{padding:12px 20px}
.comments{margin-top:14px;max-width:358px;background:var(--color-surface-card);border-radius:var(--radius-card);padding:12px 16px}
.cfield{margin-top:10px;height:var(--size-commentField);border-radius:var(--radius-capsule);background:var(--color-surface-field);color:var(--color-text-secondary);display:flex;align-items:center;padding:0 12px}
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
             "The tab bar is drawn as one reading of a translucent material, and the ad block as one reading of a tint that follows the ad.</p></div>",
             '<div class="toggle" role="group" aria-label="Theme"><button type="button" data-set-theme="light" aria-pressed="false">Light</button>'
             '<button type="button" data-set-theme="dark" aria-pressed="true">Dark</button></div></header>',
             "<h2>Colour</h2>",
             '<p class="lede">Light and dark side by side. The badge says how each value was read: Sampled (a flat fill, exact), Sampled (text) '
             "(the anti-aliased pixel furthest from the fill), Derived (worked out, or a reading of a material, tint or gradient). Hover a swatch for its capture.</p>",
             "".join(colour_html),
             # PRODUCT (adapt): the palette and ramp captions
             "<h3>Red (core)</h3><p class=\"lede\">YouTube red, the same in both themes: watch progress and the Subscriptions tab dot. It is the brand, never an error colour.</p>",
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
