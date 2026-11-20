#!/usr/bin/env python3
"""Render style-guide.html from tokens.json (native kit, Grok Bot's, from tools/kit/native).

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
NAME = "Luma"   # PRODUCT (adapt)
OWNER = "Luma AI, Inc."    # PRODUCT (adapt): whose visual system it is
LEDE = ("Luma for iOS 26, read from stills captured through iPhone Mirroring on 2026-10-24.")  # PRODUCT (adapt)
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
    palette = "".join('<div class="chip-sw"><span class="dot" style="background:var(%s)"></span><code>%s</code><span>%s / %s</span></div>'
                      % (esc(var(p)), esc(".".join(p)), esc(t["$value"]), esc(dark_by[p]["$value"])) for p, t in light
                      if p[:2] in (("color", "accent"), ("color", "success"), ("color", "danger"), ("color", "warning"), ("color", "info")))
    neutrals = "".join('<div class="ramp-step" style="background:%s" title="%s"><code>%s</code></div>'
                       % (esc(t["$value"]), esc(t["$description"]), esc(p[-1] + " " + t["$value"])) for p, t in under(("color", "neutral")))
    radii = "".join('<div class="radius-box" style="border-radius:%s"><code>%s</code><span>%s</span></div>'
                    % (esc(css(t["$value"])), esc(".".join(p)), esc(t["$value"])) for p, t in under(("radius",)))
    spacing = "".join('<div class="space-row"><code>%s</code><span class="bar" style="width:%s"></span><span>%s</span></div>'
                      % (esc(".".join(p)), esc(css(t["$value"])), esc(t["$value"])) for p, t in under(("space",)))
    sizes = "".join('<div class="space-row"><code>%s</code><span class="bar thin" style="width:%s"></span><span>%s</span></div>'
                    % (esc(".".join(p)), esc(css(t["$value"])), esc(t["$value"])) for p, t in under(("size",)))
    sample = {  # PRODUCT (adapt): specimen text per type style
        "title1": "Family", "title2": "Discover", "aboutHeading": "Back with our main stage event.",
        "placeholderLarge": "Event Name", "title3": "Your Events", "headline": "Mahjong After Dark: Spooky Edition",
        "navTitle": "Notifications", "body": "Account Settings", "callout": "Yesterday, 19:00 GMT-7",
        "subhead": "Host name", "caption": "Invited", "pill": "US$15", "tab": "Discover"}
    type_rows = "".join('<tr><th scope="row"><code>%s</code><span class="desc">%s</span></th><td class="meta">%s, %s%s</td>'
                        '<td><span class="type-%s">%s</span></td></tr>'
                        % (esc(".".join(p)), esc(t["$description"]), esc(t["$value"]["fontSize"]), esc(t["$value"]["fontWeight"]),
                           (", line " + t["$value"]["lineHeight"]) if "lineHeight" in t["$value"] else "", p[-1], esc(sample.get(p[-1], "Sample")))
                        for p, t in under(("typography",)))

    # PRODUCT (adapt): specimens built from tokens only
    specimens = """
<div class="spec-grid">
 <div class="spec phone">
  <h3>Home: event rows and tab bar</h3>
  <div class="screen">
   <div class="nav"><span class="av"></span><span class="type-title2 grow">Discover</span><span class="glass pair"><span>+</span><span>&#9675;</span></span></div>
   <div class="type-title3">Your Events <span class="ter">&#8250;</span></div>
   <div class="erow"><span class="thumb"><span class="badge type-caption">Invited</span></span>
    <div class="etext"><div class="type-subhead sec">Host name <span class="pill price type-pill">US$15</span></div><div class="type-headline">Fri/Sat Gamenight</div><div class="type-callout sec">Yesterday, 19:00 GMT-7</div></div></div>
   <div class="erow"><span class="thumb"></span>
    <div class="etext"><div class="type-subhead sec">Emergent <span class="pill sold type-pill">Sold Out</span></div><div class="type-headline">Emergent: VibeCon SF 2026</div><div class="type-callout sec">08:00 GMT-7</div></div></div>
   <div class="type-navTitle date">Today <span class="ter">/ Saturday</span></div>
   <div class="tabbar"><span class="tab sel type-tab">Home</span><span class="tab type-tab">Discover</span><span class="tab type-tab">Chat<i class="count">1</i></span></div>
  </div>
  <p class="note">bg.page, text.primary / secondary / tertiary, border.divider, size.thumb, accent.subtle + accent.fg, success and danger pills, surface.glass, surface.selected, danger.emphasis</p>
 </div>
 <div class="spec phone">
  <h3>Event page (one cover's tint)</h3>
  <div class="screen cover">
   <div class="nav"><span class="glass round">&#8249;</span><span class="grow"></span><span class="glass round">&#8679;</span></div>
   <div class="type-title2">TEDxSingapore Main Stage 2026: Landing Points</div>
   <div class="type-callout sec">TEDxSingapore &#8250;</div>
   <div class="type-callout sec">Today, 14:00 - 18:30</div>
   <span class="pill price type-pill">$88</span>
   <div class="tiles"><span class="tile type-caption">Contact</span><span class="tile type-caption">More</span></div>
   <div class="type-body">TEDxSingapore is back with our iconic main stage event.</div>
  </div>
  <p class="note">coverExample.eventPage and eventButton hold one cover's readings: the app tints each event page from its cover, in both themes. radius.control, size.actionTile</p>
 </div>
 <div class="spec">
  <h3>Grouped settings</h3>
  <div class="grouped">
   <div class="card">
    <div class="srow"><span class="ico"></span><span class="type-body grow">Account Settings</span><span class="ter">&#8250;</span></div>
    <div class="srow"><span class="ico"></span><span class="type-body grow">Payment</span><span class="ter">&#8250;</span></div>
   </div>
   <p class="secthead type-body">Events You Attend</p>
   <div class="card">
    <div class="srow"><span class="type-body grow">Event Invites</span><span class="type-body sec">Push &#8661;</span></div>
    <div class="srow"><span class="type-body grow">Require Approval</span><span class="sw-ctl"></span></div>
   </div>
   <div class="card gap"><div class="srow"><span class="type-body danger">Delete Account</span></div></div>
  </div>
  <p class="note">bg.grouped, surface.card, border.cardDivider, size.row, size.settingsIcon, radius.card, text.tertiary, switch.off / thumb, danger.fg</p>
 </div>
 <div class="spec">
  <h3>Search, chips, buttons, composer</h3>
  <div class="row-btns"><span class="glass round">&#8249;</span><span class="search type-body">Search events&#8230;</span></div>
  <div class="row-btns"><span class="chip glass type-callout">Near you</span><span class="chip glass type-callout">Any Date</span></div>
  <div class="row-btns"><span class="cat type-callout">Family</span><span class="cat type-callout">Tech</span><span class="cat type-callout">Books</span></div>
  <div class="seg"><span class="sel type-callout">Upcoming</span><span class="type-callout">Past</span></div>
  <div class="row-btns"><span class="sub type-callout">Subscribe</span><span class="pill warn type-pill">Near Capacity</span><span class="pill info type-pill">Waitlist Open</span></div>
  <button class="btn type-navTitle" type="button">Confirm</button>
  <div class="composer"><span class="field-c type-callout">hey<span class="send">&#8593;</span></span></div>
  <p class="note">surface.glass, border.chip, surface.selected, accent.emphasis, warning and info pills, button.primary, surface.primary, info.emphasis, link: <a class="link">Open Settings</a></p>
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
.toggle{display:inline-flex;border-radius:var(--radius-capsule);padding:3px;gap:2px;background:var(--color-surface-glass)}
.toggle button{border:0;background:transparent;color:var(--color-text-secondary);font:inherit;padding:6px 14px;border-radius:var(--radius-capsule);cursor:pointer}
.toggle button[aria-pressed="true"]{background:var(--color-button-primary-bg);color:var(--color-button-primary-text)}
.scroll{overflow-x:auto}
table.tokens{border-collapse:collapse;width:100%;min-width:660px}
table.tokens th,table.tokens td{text-align:left;vertical-align:top;padding:8px 10px;border-bottom:var(--border-width-hairline) solid var(--color-border-cardDivider)}
table.tokens thead th{color:var(--color-text-secondary);font-size:12px;font-weight:400}
table.tokens th[scope=row]{font-weight:500;width:40%}
.desc{display:block;color:var(--color-text-secondary);font-size:12px;font-weight:400;margin-top:2px}
.meta{color:var(--color-text-secondary);white-space:nowrap}
.sw{display:inline-block;width:28px;height:28px;border-radius:8px;vertical-align:middle;margin-right:8px;border:1px solid var(--color-border-control);background-image:linear-gradient(45deg,#8883 25%,transparent 25%,transparent 75%,#8883 75%),linear-gradient(45deg,#8883 25%,transparent 25%,transparent 75%,#8883 75%);background-size:8px 8px;background-position:0 0,4px 4px;overflow:hidden}
.sw i{display:block;width:100%;height:100%}
.ev{display:inline-block;font-size:11px;padding:1px 7px;border-radius:var(--radius-capsule);border:1px solid var(--color-border-control);color:var(--color-text-secondary);white-space:nowrap}
.ev-derived{border-style:dashed}.ev-none{border-style:dotted}
.palette{display:flex;flex-wrap:wrap;gap:12px}
.chip-sw{display:flex;flex-direction:column;align-items:center;gap:4px;width:110px;font-size:12px;color:var(--color-text-secondary);text-align:center}
.chip-sw .dot{width:44px;height:44px;border-radius:50%;border:1px solid var(--color-border-control)}
.ramp{display:flex;flex-wrap:wrap;border-radius:var(--radius-card);overflow:hidden;border:1px solid var(--color-border-control)}
.ramp-step{flex:1 0 76px;height:64px;display:flex;align-items:flex-end;padding:4px}
.ramp-step code{font-size:10px;background:#0008;color:#fff;padding:0 3px;border-radius:3px}
.radii{display:flex;flex-wrap:wrap;gap:16px}
.radius-box{width:120px;height:80px;background:var(--color-surface-card);border:1px solid var(--color-border-control);display:flex;flex-direction:column;align-items:center;justify-content:center;font-size:12px;color:var(--color-text-secondary)}
.space-row{display:grid;grid-template-columns:minmax(150px,240px) 1fr 70px;align-items:center;gap:12px;padding:3px 0}
.space-row .bar{display:block;height:12px;background:var(--color-accent-emphasis);border-radius:2px;max-width:100%}
.space-row .bar.thin{height:8px;background:var(--color-text-tertiary)}
.spec-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,330px),1fr));gap:16px}
.spec{border:1px solid var(--color-border-control);border-radius:var(--radius-card);padding:4px 16px 16px;min-width:0}
.screen{background:var(--color-bg-page);border:1px solid var(--color-border-control);border-radius:var(--radius-card);padding:12px var(--space-screenMargin) 16px;max-width:390px;position:relative}
.screen.cover{background:var(--color-coverExample-eventPage);color:var(--color-text-onAccent)}
.screen.cover .sec{color:var(--color-text-onAccent)}
.screen.cover .glass{background:var(--color-coverExample-eventButton);color:var(--color-text-onAccent)}
.grow{flex:1}
.glass{background:var(--color-surface-glass);color:var(--color-text-primary);display:inline-flex;align-items:center;justify-content:center;gap:8px}
.round{width:var(--size-navButton);height:var(--size-navButton);border-radius:50%;font-size:22px;flex:none}
.pair{height:var(--size-navButton);border-radius:var(--radius-capsule);padding:0 14px;gap:18px;font-size:20px}
.nav{display:flex;align-items:center;gap:10px;margin-bottom:12px}
.av{display:inline-block;width:var(--size-avatar-header);height:var(--size-avatar-header);border-radius:50%;background:var(--color-surface-bubble);flex:none}
.sec{color:var(--color-text-secondary)}.ter{color:var(--color-text-tertiary)}.danger{color:var(--color-danger-fg)}
.erow{display:flex;gap:var(--space-md);padding:var(--space-md) 0;border-bottom:var(--border-width-hairline) solid var(--color-border-divider)}
.thumb{position:relative;flex:none;width:var(--size-thumb);height:var(--size-thumb);border-radius:var(--radius-thumb);background:var(--color-surface-bubble)}
.badge{position:absolute;left:50%;bottom:-6px;transform:translateX(-50%);height:var(--size-badge);padding:0 6px;border-radius:var(--radius-capsule);background:var(--color-accent-subtle);color:var(--color-accent-fg);display:inline-flex;align-items:center;box-shadow:0 0 0 2px var(--color-bg-page)}
.etext{flex:1;min-width:0;display:flex;flex-direction:column;gap:var(--space-xs)}
.etext>div:first-child{display:flex;justify-content:space-between;align-items:center}
.pill{display:inline-flex;align-items:center;height:var(--size-pill);padding:0 6px;border-radius:var(--radius-capsule);width:max-content}
.price{background:var(--color-success-subtle);color:var(--color-success-fg)}
.sold{background:var(--color-danger-subtle);color:var(--color-danger-fg)}
.warn{background:var(--color-warning-subtle);color:var(--color-warning-fg)}
.info{background:var(--color-info-subtle);color:var(--color-info-fg)}
.date{margin:var(--space-lg) 0 64px}
.tabbar{position:absolute;left:50%;bottom:12px;transform:translateX(-50%);width:min(var(--size-tabBar-width),90%);height:var(--size-tabBar-height);border-radius:var(--radius-capsule);background:var(--color-surface-glass);display:flex;align-items:center;padding:4px}
.tab{flex:1;height:100%;display:flex;align-items:flex-end;justify-content:center;padding-bottom:10px;color:var(--color-text-tab);border-radius:var(--radius-capsule);position:relative}
.tab.sel{background:var(--color-surface-selected);color:var(--color-text-tabSelected)}
.count{position:absolute;top:6px;right:22px;width:var(--size-countBadge);height:var(--size-countBadge);border-radius:50%;background:var(--color-danger-emphasis);color:var(--color-text-onAccent);font-style:normal;font-size:12px;display:flex;align-items:center;justify-content:center}
.tiles{display:flex;gap:var(--space-sm);margin:var(--space-md) 0}
.tile{flex:1;height:var(--size-actionTile);border-radius:var(--radius-control);background:var(--color-coverExample-eventButton);display:flex;align-items:flex-end;justify-content:center;padding-bottom:8px}
.grouped{background:var(--color-bg-grouped);padding:var(--space-lg) var(--space-xl);border-radius:var(--radius-card)}
.card{background:var(--color-surface-card);border-radius:var(--radius-card);overflow:hidden;max-width:358px}
.card.gap{margin-top:var(--space-cardGap)}
.srow{display:flex;align-items:center;gap:12px;min-height:var(--size-row);padding:0 var(--space-cardPadding);border-bottom:var(--border-width-hairline) solid var(--color-border-cardDivider)}
.srow:last-child{border-bottom:0}
.ico{flex:none;width:var(--size-settingsIcon);height:var(--size-settingsIcon);border-radius:var(--radius-icon);background:var(--color-accent-emphasis)}
.secthead{color:var(--color-text-tertiary);margin:var(--space-cardGap) 0 6px var(--space-cardPadding)}
.sw-ctl{position:relative;flex:none;width:var(--size-switch-width);height:var(--size-switch-height);border-radius:var(--radius-capsule);background:var(--color-switch-off)}
.sw-ctl::after{content:"";position:absolute;top:2px;left:2px;width:var(--size-switch-thumb);height:calc(var(--size-switch-height) - 4px);border-radius:var(--radius-capsule);background:var(--color-switch-thumb)}
.row-btns{display:flex;flex-wrap:wrap;gap:var(--space-sm);align-items:center;margin-top:14px}
.search{flex:1;height:var(--size-searchField);border-radius:var(--radius-capsule);background:var(--color-surface-glass);color:var(--color-text-placeholder);display:flex;align-items:center;padding:0 16px}
.chip{height:var(--size-chip);padding:0 14px;border-radius:var(--radius-capsule)}
.cat{height:var(--size-categoryChip);padding:0 14px;border-radius:var(--radius-capsule);border:var(--border-width-outline) solid var(--color-border-chip);display:inline-flex;align-items:center}
.seg{display:inline-flex;margin-top:14px;height:var(--size-segmented-height);padding:3px;border-radius:var(--radius-capsule);background:var(--color-surface-glass)}
.seg span{display:inline-flex;align-items:center;padding:0 22px;border-radius:var(--radius-capsule)}
.seg .sel{background:var(--color-surface-selected)}
.sub{height:var(--size-buttonCompact);padding:0 16px;border-radius:var(--radius-capsule);background:var(--color-button-accent-bg);color:var(--color-button-accent-text);display:inline-flex;align-items:center}
.btn{display:block;width:100%;max-width:335px;height:var(--size-button);margin:14px 0 0;border:0;border-radius:var(--radius-capsule);background:var(--color-button-primary-bg);color:var(--color-button-primary-text);font-family:var(--font-base)}
.composer{display:flex;margin-top:14px}
.field-c{flex:1;height:var(--size-composer);border-radius:var(--radius-capsule);background:var(--color-surface-glass);display:flex;align-items:center;justify-content:space-between;padding:0 6px 0 16px;max-width:335px}
.send{width:var(--size-send);height:var(--size-send);border-radius:50%;background:var(--color-info-emphasis);color:var(--color-text-onAccent);display:inline-flex;align-items:center;justify-content:center;font-weight:600}
.link{color:var(--color-text-link)}
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
             "<h3>Accent and status colours</h3><p class=\"lede\">Purple is Luma's accent (Invited, Subscribe); green, red, amber and blue mark prices and event status. Light / dark values; the circles follow the toggle.</p>",
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
