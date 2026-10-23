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
NAME = "GitHub Mobile"   # PRODUCT (adapt)
OWNER = "GitHub"    # PRODUCT (adapt): whose visual system it is
LEDE = ("GitHub Mobile for iOS 26, read from stills captured through iPhone Mirroring on 2026-10-24.")  # PRODUCT (adapt)
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
            family = "var(--font-mono)" if v["fontFamily"] == "{fontFamily.mono}" else "var(--font-base)"
            type_css.append(".type-%s{font-family:%s;font-weight:%s;font-size:%s;line-height:%s}"
                            % (p[-1], family, css(v["fontWeight"]), v["fontSize"], v.get("lineHeight", "1.25")))
        elif t["$type"] == "fontFamily":
            core_css.append("%s:%s" % (var(p), MONO_STACK if p[-1] == "mono" else FONT_STACK))
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
                      % (esc(var(p)), esc(".".join(p)), esc(t["$value"]), esc(dark_by[p]["$value"])) for p, t in light if p[:2] == ("color", "tile"))
    neutrals = "".join('<div class="ramp-step" style="background:%s" title="%s"><code>%s</code></div>'
                       % (esc(t["$value"]), esc(t["$description"]), esc(p[-1] + " " + t["$value"])) for p, t in under(("color", "neutral")))
    radii = "".join('<div class="radius-box" style="border-radius:%s"><code>%s</code><span>%s</span></div>'
                    % (esc(css(t["$value"])), esc(".".join(p)), esc(t["$value"])) for p, t in under(("radius",)))
    spacing = "".join('<div class="space-row"><code>%s</code><span class="bar" style="width:%s"></span><span>%s</span></div>'
                      % (esc(".".join(p)), esc(css(t["$value"])), esc(t["$value"])) for p, t in under(("space",)))
    sizes = "".join('<div class="space-row"><code>%s</code><span class="bar thin" style="width:%s"></span><span>%s</span></div>'
                    % (esc(".".join(p)), esc(css(t["$value"])), esc(t["$value"])) for p, t in under(("size",)))
    sample = {  # PRODUCT (adapt): specimen text per type style
        "largeTitle": "Inbox", "title": "Sidebar dropdown is displaying incorrectly", "headline": "Pull Requests",
        "body": "When opening the Primitives section, the list items display in a row.", "rowTitle": "Top Repositories",
        "callout": "c-wenlong / design-systems #82", "sectionHeader": "Display", "caption": "Focused", "footnote": "Member",
        "tab": "Explore", "code": "npm install @primer/react"}
    type_rows = "".join('<tr><th scope="row"><code>%s</code><span class="desc">%s</span></th><td class="meta">%s, %s%s</td>'
                        '<td><span class="type-%s">%s</span></td></tr>'
                        % (esc(".".join(p)), esc(t["$description"]), esc(t["$value"]["fontSize"]), esc(t["$value"]["fontWeight"]),
                           (", line " + t["$value"]["lineHeight"]) if "lineHeight" in t["$value"] else "", p[-1], esc(sample.get(p[-1], "Sample")))
                        for p, t in under(("typography",)))

    # PRODUCT (adapt): specimens built from tokens only
    specimens = """
<div class="spec-grid">
 <div class="spec phone">
  <h3>Home: section, grouped card, tab bar</h3>
  <div class="screen">
   <div class="sect type-title">My Work</div>
   <div class="card">
    <div class="trow"><span class="tile" style="background:var(--color-tile-green)">&#9711;</span><span class="type-rowTitle">Issues</span><span class="chev">&#8250;</span></div>
    <div class="trow"><span class="tile" style="background:var(--color-tile-gray)">&#9633;</span><span class="type-rowTitle">Top Repositories</span><span class="chev">&#8250;</span></div>
    <div class="trow"><span class="tile" style="background:var(--color-tile-yellow)">&#9733;</span><span class="type-rowTitle">Starred</span><span class="chev">&#8250;</span></div>
   </div>
   <div class="fab type-headline">New Session</div>
   <div class="tabbar type-tab"><span class="tab on">Home</span><span class="tab">Inbox</span><span class="tab">Explore</span><span class="tab">Copilot</span></div>
  </div>
  <p class="note">bg.page, surface.card, radius.card, size.row, tile.*, surface.fab, surface.glass, surface.tabSelected, text.tabSelected</p>
 </div>
 <div class="spec phone">
  <h3>Inbox: chips and a list row</h3>
  <div class="screen list">
   <div class="type-largeTitle">Inbox</div>
   <div class="chips"><span class="chip type-caption">Inbox &#8964;</span><span class="chip type-caption">Focused</span><span class="chip type-caption">Unread</span></div>
   <div class="lrow"><span class="dot"></span><div class="lmain"><div class="type-callout sec">c-wenlong / YCBench #5</div><div class="type-callout">Improve form accessibility and disabled button states</div></div><div class="lside"><span class="type-callout sec">3mo</span><span class="count type-caption">2</span></div></div>
   <div class="lrow"><span class="dot"></span><div class="lmain"><div class="type-callout sec">c-wenlong / quiver #7</div><div class="type-callout">Fix weak MD5 hash usage</div></div><div class="lside"><span class="type-callout sec">3mo</span><span class="count type-caption">1</span></div></div>
  </div>
  <p class="note">bg.list, surface.glass (chips), accent.fg (unread dot), accent.subtle (count), border.divider, typography.callout</p>
 </div>
 <div class="spec">
  <h3>Issue and PR header</h3>
  <div class="type-callout sec">primer / design #769</div>
  <div class="type-title">Sidebar dropdown is displaying incorrectly</div>
  <div class="badges"><span class="badge open type-caption">&#9737; Open</span><span class="badge muted type-caption">Locked</span></div>
  <div class="badges"><span class="badge draft type-caption">Draft</span><span class="badge merged type-caption">Merged</span><span class="branch type-code">main</span><span class="sec">&#8592;</span><span class="branch type-code">chore/update</span></div>
  <div class="card stat"><span class="type-body">1 file changed</span><span class="type-body"><span class="add">+30</span> <span class="del">-26</span></span></div>
  <div class="banner type-headline">Archived by owner &#183; Read-only</div>
  <p class="note">success.emphasis, neutral.emphasis, done.emphasis, surface.muted, accent.subtle (branch), success.fg, danger.fg, attention.*</p>
 </div>
 <div class="spec">
  <h3>Buttons</h3>
  <button class="btn type-headline" type="button">Add Favorites</button>
  <div class="pair"><button class="btn type-headline" type="button">&#9734; Star</button><button class="ibtn" type="button">&#5833;</button><button class="ibtn" type="button">&#9900;</button></div>
  <div class="pair"><span class="tbtn type-headline">Dismiss</span><button class="dbtn type-headline" type="button">Email me a download link</button></div>
  <div class="pair"><button class="abtn type-headline" type="button">Configure</button><span class="new type-caption">New</span><span class="glassbtn">&#8249;</span></div>
  <p class="note">button.neutral, size.button, radius.button, size.iconButton, done.fg, button.done, button.accent, size.navButton</p>
 </div>
 <div class="spec">
  <h3>Settings: values and switches</h3>
  <div class="card">
   <div class="srow"><span class="type-body">Appearance</span><span class="type-body sec">Automatic &#8250;</span></div>
   <div class="srow"><span class="type-body"><span class="new type-caption">New</span> Notifications</span><span class="type-body sec">Setup Needed &#8250;</span></div>
  </div>
  <p class="secthead type-sectionHeader">Display</p>
  <div class="card">
   <div class="srow"><span class="type-body">Show Line Numbers</span><span class="sw-ctl on"></span></div>
   <div class="srow"><span class="type-body">Line Wrapping</span><span class="sw-ctl"></span></div>
  </div>
  <p class="note">surface.card, size.rowSettings, text.secondary, accent.subtle, text.sectionHeader, switch.on / off / thumb</p>
 </div>
 <div class="spec">
  <h3>Diff</h3>
  <div class="diff type-code">
   <div class="dl hunk"><span class="g">&#8943;</span><span>@@ source: https://github.com/primer/react</span></div>
   <div class="dl"><span class="g">11</span><span><span class="kw">def</span> <span class="en">fibonacci</span>(n)</span></div>
   <div class="dl del"><span class="g">12</span><span>- npm install react@<span class="cn">18</span></span></div>
   <div class="dl add"><span class="g">12</span><span>+ npm install react@<span class="cn">19</span></span></div>
  </div>
  <p class="note">surface.code, surface.gutter, diff.*, syntax.keyword / entity / constant, typography.code</p>
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
.toggle{display:inline-flex;border-radius:var(--radius-capsule);padding:3px;gap:2px;background:var(--color-surface-button)}
.toggle button{border:0;background:transparent;color:var(--color-text-secondary);font:inherit;padding:6px 14px;border-radius:var(--radius-capsule);cursor:pointer}
.toggle button[aria-pressed="true"]{background:var(--color-accent-emphasis);color:var(--color-text-onEmphasis)}
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
.ramp{display:flex;flex-wrap:wrap;border-radius:var(--radius-button);overflow:hidden;border:1px solid var(--color-border-divider)}
.ramp-step{flex:1 0 76px;height:64px;display:flex;align-items:flex-end;padding:4px}
.ramp-step code{font-size:10px;background:#0008;color:#fff;padding:0 3px;border-radius:3px}
.radii{display:flex;flex-wrap:wrap;gap:16px}
.radius-box{width:120px;height:80px;background:var(--color-surface-card);border:1px solid var(--color-border-divider);display:flex;flex-direction:column;align-items:center;justify-content:center;font-size:12px;color:var(--color-text-secondary)}
.space-row{display:grid;grid-template-columns:minmax(150px,240px) 1fr 70px;align-items:center;gap:12px;padding:3px 0}
.space-row .bar{display:block;height:12px;background:var(--color-accent-fg);border-radius:2px;max-width:100%}
.space-row .bar.thin{height:8px;background:var(--color-text-secondary)}
.spec-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,330px),1fr));gap:16px}
.spec{background:var(--color-bg-list);border:1px solid var(--color-border-divider);border-radius:var(--radius-button);padding:4px 16px 16px;min-width:0}
.screen{position:relative;background:var(--color-bg-page);border:1px solid var(--color-border-divider);border-radius:var(--radius-card);padding:12px var(--space-screenMargin) 16px;max-width:390px}
.screen.list{background:var(--color-bg-list)}
.sec{color:var(--color-text-secondary)}
.sect{margin:4px 0 var(--space-titleGap)}
.card{background:var(--color-surface-card);border-radius:var(--radius-card);max-width:358px;overflow:hidden}
.trow{display:flex;align-items:center;gap:var(--space-md);min-height:var(--size-row);padding:0 var(--space-cardPadding);border-bottom:var(--border-width-hairline) solid var(--color-border-divider)}
.trow:last-child{border-bottom:0}.trow .type-rowTitle{flex:1}
.tile{width:var(--size-tile);height:var(--size-tile);border-radius:var(--radius-tile);color:#fff;display:inline-flex;align-items:center;justify-content:center;font-size:16px;flex:none}
.chev{color:var(--color-text-secondary)}
.fab{width:max-content;margin:16px 0 12px auto;height:var(--size-fab);padding:0 20px;border-radius:var(--radius-capsule);background:var(--color-surface-fab);color:var(--color-text-onEmphasis);display:flex;align-items:center}
.tabbar{display:flex;justify-content:space-around;align-items:center;height:var(--size-tabBar-height);border-radius:var(--radius-capsule);background:var(--color-surface-glass);padding:0 6px}
.tab{color:var(--color-text-tab);padding:14px 16px;border-radius:var(--radius-capsule)}.tab.on{background:var(--color-surface-tabSelected);color:var(--color-text-tabSelected)}
.chips{display:flex;gap:var(--space-sm);margin:12px 0;flex-wrap:wrap}
.chip{height:var(--size-chip);padding:0 12px;border-radius:var(--radius-capsule);background:var(--color-surface-glass);color:var(--color-text-secondary);display:inline-flex;align-items:center;border:var(--border-width-hairline) solid var(--color-border-divider)}
.lrow{display:flex;gap:12px;padding:12px 0;border-top:var(--border-width-hairline) solid var(--color-border-divider)}
.lmain{flex:1}.lside{display:flex;flex-direction:column;align-items:flex-end;gap:6px}
.dot{flex:none;width:12px;height:12px;border-radius:50%;background:var(--color-accent-fg);margin-top:30px}
.count{min-width:22px;padding:2px 6px;border-radius:6px;background:var(--color-accent-subtle);color:var(--color-text-link);text-align:center}
.badges{display:flex;flex-wrap:wrap;gap:var(--space-xs) 8px;align-items:center;margin:10px 0}
.badge{height:var(--size-badge);padding:0 12px;border-radius:var(--radius-capsule);display:inline-flex;align-items:center;color:var(--color-text-onEmphasis)}
.badge.open{background:var(--color-success-emphasis)}.badge.draft{background:var(--color-neutral-emphasis)}.badge.merged{background:var(--color-done-emphasis)}
.badge.muted{background:var(--color-surface-muted);color:var(--color-text-secondary)}
.branch{height:var(--size-branch);padding:0 6px;border-radius:var(--radius-branch);background:var(--color-accent-subtle);color:var(--color-text-link);display:inline-flex;align-items:center}
.stat{border:1px solid var(--color-border-divider);display:flex;justify-content:space-between;padding:14px var(--space-cardPadding);margin-top:12px}
.add{color:var(--color-success-fg)}.del{color:var(--color-danger-fg)}
.banner{margin-top:12px;padding:12px;text-align:center;background:var(--color-attention-subtle);color:var(--color-attention-fg)}
.btn{display:block;width:100%;max-width:326px;height:var(--size-button);margin:12px 0 0;border:0;border-radius:var(--radius-button);background:var(--color-button-neutral-bg);color:var(--color-button-neutral-text);font-family:var(--font-base)}
.pair{display:flex;gap:10px;align-items:center;margin-top:12px;flex-wrap:wrap}.pair .btn{margin:0;flex:1}
.ibtn{width:var(--size-iconButton);height:var(--size-iconButton);border:0;border-radius:var(--radius-button);background:var(--color-button-neutral-bg);color:var(--color-text-primary)}
.tbtn{color:var(--color-done-fg);padding:0 12px}
.dbtn{height:var(--size-buttonCompact);padding:0 18px;border:0;border-radius:var(--radius-button);background:var(--color-button-done-bg);color:var(--color-button-done-text);font-family:var(--font-base)}
.abtn{height:var(--size-buttonCompact);padding:0 18px;border:0;border-radius:var(--radius-button);background:var(--color-button-accent-bg);color:var(--color-button-accent-text);font-family:var(--font-base)}
.new{height:var(--size-newBadge);padding:0 6px;border-radius:var(--radius-capsule);background:var(--color-accent-subtle);color:var(--color-text-link);display:inline-flex;align-items:center;vertical-align:middle}
.glassbtn{width:var(--size-navButton);height:var(--size-navButton);border-radius:50%;background:var(--color-surface-glass);display:inline-flex;align-items:center;justify-content:center;font-size:26px}
.srow{display:flex;justify-content:space-between;align-items:center;gap:12px;min-height:var(--size-rowSettings);padding:0 var(--space-cardPadding);border-bottom:var(--border-width-hairline) solid var(--color-border-divider)}
.srow:last-child{border-bottom:0}
.secthead{color:var(--color-text-sectionHeader);margin:16px 0 6px var(--space-cardPadding)}
.sw-ctl{position:relative;flex:none;width:var(--size-switch-width);height:var(--size-switch-height);border-radius:var(--radius-capsule);background:var(--color-switch-off)}
.sw-ctl::after{content:"";position:absolute;top:2px;left:2px;width:var(--size-switch-thumb);height:calc(var(--size-switch-height) - 4px);border-radius:var(--radius-capsule);background:var(--color-switch-thumb)}
.sw-ctl.on{background:var(--color-switch-on)}.sw-ctl.on::after{left:auto;right:2px}
.diff{border-radius:var(--radius-button);overflow:hidden;background:var(--color-surface-code);border:1px solid var(--color-border-divider)}
.dl{display:flex;white-space:pre}.dl .g{flex:none;width:44px;text-align:right;padding-right:10px;background:var(--color-surface-gutter);color:var(--color-text-secondary)}.dl>span:last-child{padding-left:10px}
.dl.hunk,.dl.hunk .g{background:var(--color-diff-hunk);color:var(--color-text-link)}
.dl.del{background:var(--color-diff-deletion)}.dl.del .g{background:var(--color-diff-deletionGutter)}
.dl.add{background:var(--color-diff-addition)}.dl.add .g{background:var(--color-diff-additionGutter)}
.kw{color:var(--color-syntax-keyword)}.en{color:var(--color-syntax-entity)}.cn{color:var(--color-syntax-constant)}
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
             "Glass is drawn as its centre colour: the real material blurs what is behind it. Monospace text uses the platform monospace.</p></div>",
             '<div class="toggle" role="group" aria-label="Theme"><button type="button" data-set-theme="light" aria-pressed="false">Light</button>'
             '<button type="button" data-set-theme="dark" aria-pressed="true">Dark</button></div></header>',
             "<h2>Colour</h2>",
             '<p class="lede">Light and dark side by side. The badge says how each value was read: Sampled (a flat fill, exact), Sampled (text) '
             "(the anti-aliased pixel furthest from the fill), Derived (worked out, or a glass or gradient reading). Hover a swatch for its capture.</p>",
             "".join(colour_html),
             # PRODUCT (adapt): the palette and ramp captions
             "<h3>Icon tiles</h3><p class=\"lede\">The coloured tiles behind row icons (light / dark). Each kind of object keeps one colour wherever it appears.</p>",
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
