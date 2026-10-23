#!/usr/bin/env python3
"""Render style-guide.html from tokens.json (native kit, from systems/grokbot).

    python3 tools/build_style_guide.py

Every token becomes a CSS custom property (its path joined with dashes; an alias becomes a var()
reference), so the swatches, scales and specimens cannot drift from the file. Adapt NAME, LEDE,
OWNER, `sample` and `specimens` (PRODUCT (adapt)); draw specimens from tokens only, never the
product's artwork.
Adapted from the native kit (from systems/grokbot, itself from systems/hevy). Standard library only, deterministic.
"""
import html
import json
import pathlib

PKG = pathlib.Path(__file__).resolve().parent.parent
TOKENS = PKG / "tokens.json"
OUT = PKG / "style-guide.html"

FONT_STACK = '-apple-system, system-ui, "SF Pro Text", "Helvetica Neue", Arial, sans-serif'
MONO_STACK = 'ui-monospace, "SF Mono", Menlo, monospace'
SERIF_STACK = '"New York", ui-serif, Georgia, serif'  # PRODUCT (adapt): fontFamily.reader
NAME = "Substack"   # PRODUCT (adapt)
OWNER = "Substack Inc."    # PRODUCT (adapt): whose visual system it is
LEDE = ("Substack for iOS 26, read from stills captured through iPhone Mirroring on 2026-10-23 (Night) and 2026-10-24 (Day).")  # PRODUCT (adapt)
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
            fam = "var(--font-serif)" if v["fontFamily"] == "{fontFamily.reader}" else "var(--font-base)"
            type_css.append(".type-%s{font-family:%s;font-weight:%s;font-size:%s;line-height:%s}"
                            % (p[-1], fam, css(v["fontWeight"]), v["fontSize"], v.get("lineHeight", "1.25")))
        elif t["$type"] == "fontFamily":
            core_css.append("%s:%s" % (var(p), SERIF_STACK if p[-1] == "reader" else FONT_STACK))
        else:
            core_css.append("%s:%s" % (var(p), css(t["$value"])))
    core_css += ["--font-base:%s" % FONT_STACK, "--font-mono:%s" % MONO_STACK, "--font-serif:%s" % SERIF_STACK]
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
                      % (esc(css(t["$value"])), esc(".".join(p)), esc(t["$value"])) for p, t in under(("color",)) if len(p) == 2)
    neutrals = "".join('<div class="ramp-step" style="background:%s" title="%s"><code>%s</code></div>'
                       % (esc(t["$value"]), esc(t["$description"]), esc(p[-1] + " " + t["$value"])) for p, t in under(("color", "neutral")))
    radii = "".join('<div class="radius-box" style="border-radius:%s"><code>%s</code><span>%s</span></div>'
                    % (esc(css(t["$value"])), esc(".".join(p)), esc(t["$value"])) for p, t in under(("radius",)))
    spacing = "".join('<div class="space-row"><code>%s</code><span class="bar" style="width:%s"></span><span>%s</span></div>'
                      % (esc(".".join(p)), esc(css(t["$value"])), esc(t["$value"])) for p, t in under(("space",)))
    sizes = "".join('<div class="space-row"><code>%s</code><span class="bar thin" style="width:%s"></span><span>%s</span></div>'
                    % (esc(".".join(p)), esc(css(t["$value"])), esc(t["$value"])) for p, t in under(("size",)))
    sample = {  # PRODUCT (adapt): specimen text per type style
        "largeTitle": "Settings", "screenTitle": "Read", "postTitle": "How Kafka Works", "sectionTitle": "Your inbox",
        "reader": "Get my system design playbook on signup.", "postSubtitle": "Learn everything about the architecture",
        "headline": "Building World Models", "body": "Fast, lift, sprint, stretch, and meditate.", "link": "Restore in-app purchases",
        "subheadline": "For you", "footnote": "10m read", "kicker": "THE SYSTEM DESIGN NEWSLETTER", "caption": "PLAYBACK"}
    type_rows = "".join('<tr><th scope="row"><code>%s</code><span class="desc">%s</span></th><td class="meta">%s, %s%s</td>'
                        '<td><span class="type-%s">%s</span></td></tr>'
                        % (esc(".".join(p)), esc(t["$description"]), esc(t["$value"]["fontSize"]), esc(t["$value"]["fontWeight"]),
                           (", line " + t["$value"]["lineHeight"]) if "lineHeight" in t["$value"] else "", p[-1], esc(sample.get(p[-1], "Sample")))
                        for p, t in under(("typography",)))

    # PRODUCT (adapt): specimens built from tokens only
    specimens = """
<div class="spec-grid">
 <div class="spec phone">
  <h3>Read tab</h3>
  <div class="screen">
   <div class="hdr"><span class="type-screenTitle">Read</span><span class="glass cap">&#9906; &#9679;</span></div>
   <div class="tabs"><span class="tab on type-subheadline">For you</span><span class="tab type-subheadline">Latest</span><span class="tab type-subheadline">Paid</span><span class="tab type-subheadline">Saved</span></div>
   <div class="sect"><span class="type-sectionTitle">Your inbox</span><span class="type-headline ter">See all</span></div>
   <div class="irow"><div class="ib"><div class="type-footnote ter"><i class="dot"></i> Devansh's Newsletter</div><div class="type-headline">Building World Models</div><div class="type-footnote ter">10m read &#183; &#9825; 18</div></div><span class="thumb"></span></div>
   <div class="irow"><div class="ib"><div class="type-footnote ter">The System Design Newsletter</div><div class="type-headline">How Kafka Works</div><div class="type-footnote ter"><span class="prog"><b></b></span> 14m left</div></div><span class="thumb"></span></div>
   <div class="tabbar type-caption"><span>Home</span><span class="on">Read</span><span>Podcasts</span><span>Chat<i class="dot"></i></span><span>Activity</span></div>
  </div>
  <p class="note">bg.page, surface.tabSelected, text.tertiary, border.divider, accent.dot, control.progressTrack / progressFill, surface.tabBar / tabBarSelected, size.tabBar</p>
 </div>
 <div class="spec phone">
  <h3>Post reader</h3>
  <div class="screen">
   <div class="nav"><span class="glass round">&#8249;</span><span class="navpill type-headline">Subscribe</span><span class="glass round">&#8943;</span></div>
   <p class="type-kicker sec">THE SYSTEM DESIGN NEWSLETTER</p>
   <h4 class="type-postTitle">How Kafka Works</h4>
   <p class="type-postSubtitle sec">Learn everything about the architecture, brokers and topic partitions</p>
   <hr class="div">
   <p class="type-reader rd">Get my system design playbook for free on newsletter signup:</p>
   <button class="pub type-headline" type="button">Subscribe</button>
   <div class="abar glass type-headline"><span>&#9825; 645</span><span>&#9633; 9</span><span>&#8635; 90</span><span>&#8679;</span></div>
  </div>
  <p class="note">typography.kicker / postTitle / postSubtitle / reader, accent.publication / publicationGlass, radius.publicationButton, surface.glass (floating action bar)</p>
 </div>
 <div class="spec">
  <h3>Grouped settings</h3>
  <div class="grp">
   <p class="secthead type-caption">PLAYBACK</p>
   <div class="card">
    <div class="srow"><span class="itile">&#9654;</span><span class="type-headline grow">Auto-play videos</span><span class="sw-ctl on"></span></div>
    <div class="srow"><span class="itile">&#9680;</span><span class="type-headline grow">System</span><span class="chk">&#10003;</span></div>
    <div class="srow"><span class="itile">&#9790;</span><span class="type-headline grow">Night</span></div>
   </div>
   <div class="card"><div class="srow"><span class="type-headline grow">New likes</span><span class="cbx">&#10003;</span><span class="cbx">&#10003;</span></div></div>
   <div class="card"><div class="srow c"><span class="type-headline danger">Disable all</span></div></div>
   <p class="type-footnote foot">Payments go directly to your bank account. <a class="lnk">Learn more</a></p>
  </div>
  <p class="note">bg.grouped, surface.card, surface.iconTile, border.grouped, size.row, accent.control, control.check / checkbox, text.danger, text.footnote, text.link</p>
 </div>
 <div class="spec">
  <h3>Buttons, banner, options, sheet</h3>
  <div class="row-btns"><button class="btn brand type-headline" type="button">Share</button><button class="btn sec2 type-headline" type="button">Edit</button></div>
  <div class="banner"><div class="type-headline">&#9888; Notifications are off</div><div class="type-footnote ter">Turn on so you don't miss a message</div>
   <div class="row-btns"><button class="bb sec2 type-headline" type="button">Later</button><button class="bb brand type-headline" type="button">Turn on</button></div></div>
  <div class="row-btns"><span class="small brand type-headline">Subscribe back</span><span class="chip on type-subheadline">Suggested</span><span class="chip type-subheadline">Technology</span><span class="fab">+</span></div>
  <div class="row-btns"><span class="opt on type-reader">New York</span><span class="opt type-reader">Messina</span></div>
  <div class="sheet"><div class="type-headline">Options</div><hr class="div sh"><div class="type-headline mi">Search in post</div><div class="type-headline mi">Archive</div><hr class="div sh"><div class="type-headline mi danger">Report</div></div>
  <p class="note">accent.brand, accent.brandShare, surface.secondary, surface.banner, radius.button / small / option / sheet, surface.optionSelected, control.optionRim, border.option, surface.chipSelected, accent.brandFab, size.fab, surface.sheet, border.sheet</p>
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
.toggle button[aria-pressed="true"]{background:var(--color-text-primary);color:var(--color-bg-page)}
.scroll{overflow-x:auto}
table.tokens{border-collapse:collapse;width:100%;min-width:660px}
table.tokens th,table.tokens td{text-align:left;vertical-align:top;padding:8px 10px;border-bottom:var(--border-width-hairline) solid var(--color-border-divider)}
table.tokens thead th{color:var(--color-text-secondary);font-size:12px;font-weight:400}
table.tokens th[scope=row]{font-weight:500;width:40%}
.desc{display:block;color:var(--color-text-secondary);font-size:12px;font-weight:400;margin-top:2px}
.meta{color:var(--color-text-secondary);white-space:nowrap}
.sw{display:inline-block;width:28px;height:28px;border-radius:8px;vertical-align:middle;margin-right:8px;border:1px solid var(--color-border-divider);background-image:linear-gradient(45deg,#8883 25%,transparent 25%,transparent 75%,#8883 75%),linear-gradient(45deg,#8883 25%,transparent 25%,transparent 75%,#8883 75%);background-size:8px 8px;background-position:0 0,4px 4px;overflow:hidden}
.sw i{display:block;width:100%;height:100%}
.ev{display:inline-block;font-size:11px;padding:1px 7px;border-radius:var(--radius-capsule);border:1px solid var(--color-border-divider);color:var(--color-text-secondary);white-space:nowrap}
.ev-derived{border-style:dashed}.ev-none{border-style:dotted}
.palette{display:flex;flex-wrap:wrap;gap:12px}
.chip-sw{display:flex;flex-direction:column;align-items:center;gap:4px;width:84px;font-size:12px;color:var(--color-text-secondary)}
.chip-sw .dot{width:44px;height:44px;border-radius:50%}
.ramp{display:flex;flex-wrap:wrap;border-radius:var(--radius-card);overflow:hidden;border:1px solid var(--color-border-divider)}
.ramp-step{flex:1 0 76px;height:64px;display:flex;align-items:flex-end;padding:4px}
.ramp-step code{font-size:10px;background:#0008;color:#fff;padding:0 3px;border-radius:3px}
.radii{display:flex;flex-wrap:wrap;gap:16px}
.radius-box{width:120px;height:80px;background:var(--color-surface-card);border:1px solid var(--color-border-raised);display:flex;flex-direction:column;align-items:center;justify-content:center;font-size:12px;color:var(--color-text-secondary)}
.space-row{display:grid;grid-template-columns:minmax(150px,240px) 1fr 70px;align-items:center;gap:12px;padding:3px 0}
.space-row .bar{display:block;height:12px;background:var(--color-accent-brand);border-radius:2px;max-width:100%}
.space-row .bar.thin{height:8px;background:var(--color-text-tertiary)}
.spec-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,330px),1fr));gap:16px}
.spec{border:1px solid var(--color-border-divider);border-radius:var(--radius-card);padding:4px 16px 16px;min-width:0}
.screen{position:relative;background:var(--color-bg-page);border:1px solid var(--color-border-divider);border-radius:var(--radius-sheet);padding:12px var(--space-screenMargin) 16px;max-width:390px;overflow:hidden}
.glass{background:var(--color-surface-glass);color:var(--color-text-primary);display:inline-flex;align-items:center;justify-content:center;gap:8px}
.round{width:var(--size-navButton);height:var(--size-navButton);border-radius:50%;font-size:22px}
.cap{height:var(--size-navButton);padding:0 16px;border-radius:var(--radius-capsule)}
.hdr,.nav,.sect{display:flex;justify-content:space-between;align-items:center;margin-bottom:12px}
.tabs{display:flex;gap:4px;margin-bottom:16px}.tab{height:var(--size-tab);padding:0 12px;border-radius:var(--radius-capsule);display:inline-flex;align-items:center;color:var(--color-text-tertiary)}
.tab.on{background:var(--color-surface-tabSelected);color:var(--color-text-tabActive)}
.irow{display:flex;gap:12px;align-items:center;padding:12px 0;border-bottom:var(--border-width-hairline) solid var(--color-border-divider)}.ib{flex:1;display:grid;gap:6px}
.thumb{width:var(--size-thumbnail);height:var(--size-thumbnail);border-radius:var(--radius-option);background:var(--color-surface-tile);flex:none}
.dot{display:inline-block;width:8px;height:8px;border-radius:50%;background:var(--color-accent-dot);vertical-align:middle}
.prog{display:inline-block;width:var(--size-progress);height:3px;border-radius:2px;background:var(--color-control-progressTrack);vertical-align:middle;overflow:hidden}.prog b{display:block;width:40%;height:100%;background:var(--color-control-progressFill)}
.tabbar{display:flex;justify-content:space-between;align-items:center;margin-top:24px;height:var(--size-tabBar-height);border-radius:var(--radius-capsule);background:var(--color-surface-tabBar);padding:0 6px;color:var(--color-text-tabBar)}
.tabbar span{flex:1;text-align:center;height:var(--size-tabBar-item);display:flex;align-items:center;justify-content:center;border-radius:var(--radius-capsule);gap:2px}
.tabbar span.on{background:var(--color-surface-tabBarSelected);color:var(--color-text-tabBarSelected)}
.navpill{height:var(--size-navPill);padding:0 18px;border-radius:var(--radius-capsule);background:var(--color-accent-publicationGlass);color:var(--color-text-onPublication);display:inline-flex;align-items:center;margin-left:auto;margin-right:8px}
.type-postTitle{margin:6px 0}p.type-kicker,p.type-postSubtitle{margin:12px 0 0}
.sec{color:var(--color-text-secondary)}.ter{color:var(--color-text-tertiary)}.danger{color:var(--color-text-danger)}.rd{color:var(--color-text-reader)}
.div{border:0;border-top:var(--border-width-hairline) solid var(--color-border-divider);margin:16px 0}.div.sh{border-top-color:var(--color-border-sheet);margin:10px 0}
.pub{display:block;margin:12px auto;height:var(--size-buttonPublication);padding:0 22px;border:0;border-radius:var(--radius-publicationButton);background:var(--color-accent-publication);color:var(--color-text-onPublication)}
.abar{display:flex;justify-content:space-around;margin-top:16px;height:var(--size-navButton);border-radius:var(--radius-capsule);padding:0 12px}
.fab{width:var(--size-fab);height:var(--size-fab);border-radius:50%;background:var(--color-accent-brandFab);color:var(--color-text-onBrand);display:flex;align-items:center;justify-content:center;font-size:30px}
.grp{background:var(--color-bg-grouped);border-radius:var(--radius-sheet);padding:16px;max-width:390px}
.card{background:var(--color-surface-card);border-radius:var(--radius-card);overflow:hidden;margin-bottom:var(--space-lg)}
.srow{display:flex;align-items:center;gap:var(--space-md);min-height:var(--size-row);padding:0 16px;border-bottom:var(--border-width-hairline) solid var(--color-border-grouped)}.srow:last-child{border-bottom:0}.srow.c{justify-content:center}.grow{flex:1}
.itile{width:32px;height:32px;border-radius:8px;background:var(--color-surface-iconTile);display:inline-flex;align-items:center;justify-content:center;font-size:13px}
.secthead{color:var(--color-text-tertiary);margin:0 0 6px}
.chk{color:var(--color-control-check);font-size:20px}
.cbx{width:var(--size-checkbox);height:var(--size-checkbox);border-radius:var(--radius-small);background:var(--color-control-checkbox);color:var(--color-control-checkboxTick);display:inline-flex;align-items:center;justify-content:center;font-weight:700}
.foot{color:var(--color-text-footnote);margin:0 8px}.lnk{color:var(--color-text-link)}
.sw-ctl{position:relative;flex:none;width:var(--size-switch-width);height:var(--size-switch-height);border-radius:var(--radius-capsule);background:var(--color-border-option)}
.sw-ctl::after{content:"";position:absolute;top:2px;left:2px;width:36px;height:calc(var(--size-switch-height) - 4px);border-radius:var(--radius-capsule);background:var(--color-control-switchThumb)}
.sw-ctl.on{background:var(--color-control-switchOn)}.sw-ctl.on::after{left:auto;right:2px}
.row-btns{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin-top:12px}
.btn{flex:1;height:var(--size-button);border:0;border-radius:var(--radius-button);font-family:var(--font-base)}
.brand{background:var(--color-accent-brand);color:var(--color-text-onBrand)}.btn.brand{background:var(--color-accent-brandShare)}
.sec2{background:var(--color-surface-secondary);color:var(--color-text-primary)}
.banner{margin-top:14px;background:var(--color-surface-banner);border:var(--border-width-hairline) solid var(--color-border-raised);border-radius:var(--radius-card);padding:14px 16px;display:grid;gap:4px}
.bb{flex:1;height:var(--size-buttonBanner);border:0;border-radius:var(--radius-button);font-family:var(--font-base)}
.small{height:var(--size-buttonSmall);padding:0 12px;border-radius:var(--radius-small);display:inline-flex;align-items:center}
.chip{height:var(--size-chip);padding:0 14px;border-radius:var(--radius-capsule);border:var(--border-width-hairline) solid var(--color-border-raised);background:var(--color-surface-tile);display:inline-flex;align-items:center}
.chip.on{background:var(--color-surface-chipSelected);color:var(--color-text-chipSelected);border-color:var(--color-surface-chipSelected)}
.opt{height:var(--size-option);padding:0 20px;border-radius:var(--radius-option);border:var(--border-width-option) solid var(--color-border-option);color:var(--color-text-tertiary);display:inline-flex;align-items:center}
.opt.on{border:var(--border-width-optionSelected) solid var(--color-control-optionRim);background:var(--color-surface-optionSelected);color:var(--color-text-selected)}
.sheet{margin-top:14px;background:var(--color-surface-sheet);border-radius:var(--radius-sheet) var(--radius-sheet) 0 0;padding:20px;max-width:358px}
.mi{padding:10px 0}
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
             + "The sans is not known, so the page uses the platform sans; post bodies use New York, which the app names. "
             "Glass is drawn as its centre colour: the real material blurs what is behind it.</p></div>",
             '<div class="toggle" role="group" aria-label="Theme"><button type="button" data-set-theme="light" aria-pressed="false">Light</button>'
             '<button type="button" data-set-theme="dark" aria-pressed="true">Dark</button></div></header>',
             "<h2>Colour</h2>",
             '<p class="lede">Light and dark side by side. The badge says how each value was read: Sampled (a flat fill, exact), Sampled (text) '
             "(the anti-aliased pixel furthest from the fill), Derived (worked out, or a glass or gradient reading). Hover a swatch for its capture.</p>",
             "".join(colour_html),
             # PRODUCT (adapt): the palette and ramp captions
             "<h3>Brand and control colours (core)</h3><p class=\"lede\">Orange for Substack's own actions, blue for system controls, red for destructive items, and one publication's colour as an example: every publication brings its own.</p>",
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
