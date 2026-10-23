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
NAME = "Cursor for iOS"   # PRODUCT (adapt)
OWNER = "Anysphere"    # PRODUCT (adapt): whose visual system it is
LEDE = ("Cursor 1.14.0 for iOS 26, read from stills captured through iPhone Mirroring on 2026-10-23 (dark) and 2026-10-24 (light).")  # PRODUCT (adapt)
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
            fam = "var(--font-mono)" if v["fontFamily"] == "{fontFamily.mono}" else "var(--font-base)"
            type_css.append(".type-%s{font-family:%s;font-weight:%s;font-size:%s;line-height:%s}"
                            % (p[-1], fam, css(v["fontWeight"]), v["fontSize"], v.get("lineHeight", "1.25")))
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
    palette = "".join('<div class="chip-sw"><span class="dot" style="background:%s"></span><code>%s</code><span>%s</span></div>'
                      % (esc(css(t["$value"])), esc(".".join(p)), esc(t["$value"])) for p, t in under(("color", "orange")))
    neutrals = "".join('<div class="ramp-step" style="background:%s" title="%s"><code>%s</code></div>'
                       % (esc(t["$value"]), esc(t["$description"]), esc(p[-1] + " " + t["$value"])) for p, t in under(("color", "neutral")))
    radii = "".join('<div class="radius-box" style="border-radius:%s"><code>%s</code><span>%s</span></div>'
                    % (esc(css(t["$value"])), esc(".".join(p)), esc(t["$value"])) for p, t in under(("radius",)))
    spacing = "".join('<div class="space-row"><code>%s</code><span class="bar" style="width:%s"></span><span>%s</span></div>'
                      % (esc(".".join(p)), esc(css(t["$value"])), esc(t["$value"])) for p, t in under(("space",)))
    sizes = "".join('<div class="space-row"><code>%s</code><span class="bar thin" style="width:%s"></span><span>%s</span></div>'
                    % (esc(".".join(p)), esc(css(t["$value"])), esc(t["$value"])) for p, t in under(("size",)))
    sample = {  # PRODUCT (adapt): specimen text per type style
        "largeTitle": "Inbox", "statValue": "947M", "detailTitle": "Validator crash, revert or fix forward", "profileName": "Account name",
        "title": "Customize", "body": "Items 1 and 2 are small config changes.", "subheadline": "Merged · +64 -14 · toolbox-v2",
        "code": "GL11_083538", "caption": "24 SEP  1 OCT  8 OCT"}
    type_rows = "".join('<tr><th scope="row"><code>%s</code><span class="desc">%s</span></th><td class="meta">%s, %s%s</td>'
                        '<td><span class="type-%s">%s</span></td></tr>'
                        % (esc(".".join(p)), esc(t["$description"]), esc(t["$value"]["fontSize"]), esc(t["$value"]["fontWeight"]),
                           (", line " + t["$value"]["lineHeight"]) if "lineHeight" in t["$value"] else "", p[-1], esc(sample.get(p[-1], "Sample")))
                        for p, t in under(("typography",)))

    # PRODUCT (adapt): specimens built from tokens only
    specimens = """
<div class="spec-grid">
 <div class="spec phone">
  <h3>Inbox</h3>
  <div class="screen">
   <div class="nav"><span class="glass round av-nav">W</span><span class="navr"><span class="glass round">&#9906;</span><span class="glass round">+</span></span></div>
   <p class="type-largeTitle ttl">Inbox</p>
   <div class="tiles">
    <div class="tile"><i class="ic" style="color:var(--color-icon-allAgents)">&#9650;</i><span class="type-subheadline">All Agents</span></div>
    <div class="tile"><i class="ic" style="color:var(--color-icon-attention)">&#9679;</i><span class="type-subheadline">Needs Attention <b class="ter">3</b></span></div>
    <div class="tile"><i class="ic" style="color:var(--color-icon-working)">&#8226;&#8226;</i><span class="type-subheadline">Working <b class="ter">0</b></span></div>
    <div class="tile"><i class="ic" style="color:var(--color-icon-review)">&#10003;</i><span class="type-subheadline">In Review <b class="ter">1</b></span></div>
   </div>
   <p class="type-subheadline sec hdr">Projects</p>
   <div class="row"><i class="ic" style="color:var(--color-icon-projectTeal)">&#9670;</i><span class="type-body">toolbox-v1</span><span class="ter chev">&#8250;</span></div>
   <div class="row"><i class="ic ter">+</i><span class="type-body mut">New Project</span></div>
   <div class="composer"><span class="cbtn">+</span><span class="type-body ph">Plan, ask, build...</span><span class="cbtn">&#9679;</span></div>
  </div>
  <p class="note">surface.card, border.tile, radius.tile, size.tile, icon.*, size.row, border.divider, text.muted, surface.glass, size.composer</p>
 </div>
 <div class="spec phone">
  <h3>Agent list and thread</h3>
  <div class="screen">
   <p class="type-subheadline sec hdr">Needs Attention &#8964;</p>
   <div class="arow"><i class="dot on"></i><div><div class="type-body">toolbox-v2 #72: sidebar keyboard access</div><div class="type-subheadline sec"><b style="color:var(--color-status-draft)">&#9675;</b> Draft &middot; <span class="add">+234</span> <span class="del">-65</span> &middot; <span class="ter">toolbox-v2</span></div></div></div>
   <div class="arow"><i class="dot"></i><div><div class="type-body">GDM VideoChunk: 120s-cap rejections</div><div class="type-subheadline sec"><b style="color:var(--color-status-merged)">&#9675;</b> Merged &middot; +64 -14 &middot; <span class="ter">egocentric-data</span></div></div></div>
   <p class="type-body reply"><b>One part</b> silently crashes the validator: <code class="ic-code">GL11_083538</code>.</p>
   <div class="ccard"><div class="type-body">Changes <span class="sec">5</span></div>
    <div class="crow type-body"><span>device_ids.py</span><span><span class="add">+5</span> <span class="del">-12</span></span></div>
    <div class="crow type-body"><span>uploads.py</span><span><span class="add">+1</span> <span class="del">-1</span></span></div></div>
   <div class="panel"><span class="type-body">hey<i class="caret"></i></span><span class="pbar"><span class="cbtn">+</span><span class="type-body">Claude Opus 5.5 &#8964;</span><span class="send">&#8593;</span></span></div>
  </div>
  <p class="note">status.unread / read / merged / draft, diff.add / delete, surface.code + text.code, surface.card, radius.card, surface.composerPanel, button.send, focus.caret</p>
 </div>
 <div class="spec">
  <h3>Sheet with switches and a pop-up</h3>
  <div class="sheet">
   <div class="grab"></div>
   <div class="shead"><span class="glass round">&#215;</span><span class="type-title emph">Customize</span><span class="round ghost"></span></div>
   <p class="type-subheadline sec hdr">Grouping</p>
   <div class="row"><span class="type-body">Group by</span><span class="type-body sec">Category &#8693;</span></div>
   <div class="popup"><div class="type-body">&#10003; Category</div><div class="type-body">Workspace</div><div class="type-body">Date</div></div>
   <p class="type-subheadline sec hdr">Show</p>
   <div class="row"><span class="type-body">Repo</span><span class="type-body sec">All <span class="ter">&#8250;</span></span></div>
   <div class="row"><span class="type-body">Status</span><span class="type-body sec">Error +4 <span class="ter">&#8250;</span></span></div>
   <p class="type-subheadline sec hdr">Agent Properties</p>
   <div class="row"><span class="type-body">Changes</span><span class="sw-ctl on"></span></div>
   <div class="row"><span class="type-body">Last Updated</span><span class="sw-ctl"></span></div>
  </div>
  <p class="note">bg.sheet, radius.sheet, surface.grabber, text.emphasis, surface.popup, radius.menu, switch.on / off / thumb</p>
 </div>
 <div class="spec">
  <h3>Search, chips, menu, chart</h3>
  <div class="search type-body"><span class="emph">&#9906;</span> Agents, workspaces...</div>
  <div class="chips"><span class="chip sel type-subheadline">All</span><span class="chip type-subheadline">egocentric-data</span><span class="chip type-subheadline">Toolbox</span></div>
  <div class="menu"><div class="type-body">View Details</div><div class="type-body">Rename</div><div class="type-body sep">Copy <span class="chev">&#8250;</span></div><div class="type-body sep">Archive</div></div>
  <div class="chart"><i style="height:20%"></i><i style="height:80%"></i><i style="height:12%"></i><i style="height:6%"></i><i style="height:30%"></i><i style="height:55%"></i><i style="height:10%"></i></div>
  <div class="heat"><i></i><i style="background:var(--color-orange-100)"></i><i style="background:var(--color-orange-200)"></i><i style="background:var(--color-orange-300)"></i><i style="background:var(--color-orange-400)"></i></div>
  <p class="type-caption sec">24 SEP &nbsp; 1 OCT &nbsp; 8 OCT</p>
  <p class="note">surface.glassField, size.searchField, surface.secondary, size.chip, surface.menu, border.menu, chart.bar, size.chartBar, core color.orange (heatmap, read in light)</p>
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
.toggle button[aria-pressed="true"]{background:var(--color-button-send-bg);color:var(--color-button-send-glyph)}
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
.radius-box{width:120px;height:80px;background:var(--color-surface-card);border:1px solid var(--color-border-tile);display:flex;flex-direction:column;align-items:center;justify-content:center;font-size:12px;color:var(--color-text-secondary)}
.space-row{display:grid;grid-template-columns:minmax(150px,240px) 1fr 70px;align-items:center;gap:12px;padding:3px 0}
.space-row .bar{display:block;height:12px;background:var(--color-accent-default);border-radius:2px;max-width:100%}
.space-row .bar.thin{height:8px;background:var(--color-text-tertiary)}
.spec-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,330px),1fr));gap:16px}
.spec{border:1px solid var(--color-border-divider);border-radius:var(--radius-card);padding:4px 16px 16px;min-width:0}
.screen{background:var(--color-bg-page);border:1px solid var(--color-border-divider);border-radius:var(--radius-sheet);padding:12px var(--space-screenMargin) 16px;max-width:390px}
.glass{background:var(--color-surface-glass);color:var(--color-text-emphasis);display:inline-flex;align-items:center;justify-content:center;gap:8px}
.round{width:var(--size-navButton);height:var(--size-navButton);border-radius:50%;font-size:20px;flex:none}
.round.ghost{visibility:hidden}
.av-nav{background:var(--color-surface-avatar);color:var(--color-text-secondary);font-size:15px}
.nav,.shead{display:flex;justify-content:space-between;align-items:center;margin-bottom:12px}.navr{display:flex;gap:12px}
.ttl{margin:8px 0 16px}
.emph{color:var(--color-text-emphasis)}.sec{color:var(--color-text-secondary)}.ter{color:var(--color-text-tertiary);font-weight:400}.mut{color:var(--color-text-muted)}
.add{color:var(--color-diff-add)}.del{color:var(--color-diff-delete)}
.tiles{display:grid;grid-template-columns:1fr 1fr;gap:var(--space-md)}
.tile{height:var(--size-tile-height);border-radius:var(--radius-tile);background:var(--color-surface-card);border:var(--border-width-hairline) solid var(--color-border-tile);padding:12px;display:flex;flex-direction:column;justify-content:flex-end;gap:6px}
.ic{font-style:normal;width:20px;display:inline-block;text-align:center}
.hdr{margin:20px 0 4px}
.row{display:flex;align-items:center;gap:12px;min-height:var(--size-row);border-bottom:var(--border-width-hairline) solid var(--color-border-divider)}
.row>span:first-of-type{flex:1}.chev{margin-left:auto}
.composer{display:flex;align-items:center;gap:10px;height:var(--size-composer);margin-top:16px;padding:0 10px;border-radius:var(--radius-capsule);background:var(--color-surface-glass)}
.composer .ph{flex:1;color:var(--color-text-placeholder)}
.cbtn{width:var(--size-composerButton);height:var(--size-composerButton);border-radius:50%;background:var(--color-surface-glassButton);color:var(--color-text-secondary);display:inline-flex;align-items:center;justify-content:center;flex:none}
.arow{display:flex;gap:14px;align-items:flex-start;min-height:var(--size-rowTwoLine);padding-top:8px;border-bottom:var(--border-width-hairline) solid var(--color-border-divider)}
.dot{flex:none;width:8px;height:8px;margin-top:8px;border-radius:50%;background:var(--color-status-read)}.dot.on{background:var(--color-status-unread)}
.reply{margin:16px 0}
.ic-code{font-family:var(--font-mono);font-size:14px;background:var(--color-surface-code);color:var(--color-text-code);padding:1px 5px;border-radius:6px}
.ccard{background:var(--color-surface-card);border-radius:var(--radius-card);padding:10px 14px}
.crow{display:flex;justify-content:space-between;padding:8px 0}
.panel{margin-top:16px;height:var(--size-composerPanel);border-radius:var(--radius-composerPanel);background:var(--color-surface-composerPanel);padding:14px;display:flex;flex-direction:column;justify-content:space-between}
.pbar{display:flex;align-items:center;gap:10px}.pbar .type-body{flex:1}
.caret{display:inline-block;width:2px;height:1.1em;vertical-align:text-bottom;background:var(--color-focus-caret);margin-left:1px}
.send{width:var(--size-sendButton);height:var(--size-sendButton);border-radius:50%;background:var(--color-button-send-bg);color:var(--color-button-send-glyph);display:inline-flex;align-items:center;justify-content:center;font-weight:600}
.sheet{position:relative;background:var(--color-bg-sheet);border-radius:var(--radius-sheet) var(--radius-sheet) 0 0;padding:8px var(--space-screenMargin) 16px;max-width:390px;border:1px solid var(--color-border-divider)}
.grab{width:var(--size-grabber-width);height:var(--size-grabber-height);border-radius:var(--radius-capsule);background:var(--color-surface-grabber);margin:0 auto 8px}
.popup{position:absolute;right:16px;top:158px;width:220px;border-radius:var(--radius-menu);background:var(--color-surface-popup);padding:6px 0;box-shadow:0 8px 30px #0003}
.popup div{padding:9px 20px}
.sw-ctl{position:relative;flex:none;width:var(--size-switch-width);height:var(--size-switch-height);border-radius:var(--radius-capsule);background:var(--color-switch-off)}
.sw-ctl::after{content:"";position:absolute;top:2px;left:2px;width:var(--size-switch-thumb);height:calc(var(--size-switch-height) - 4px);border-radius:var(--radius-capsule);background:var(--color-switch-thumb)}
.sw-ctl.on{background:var(--color-switch-on)}.sw-ctl.on::after{left:auto;right:2px}
.search{height:var(--size-searchField);border-radius:var(--radius-capsule);background:var(--color-surface-glassField);color:var(--color-text-placeholder);display:flex;align-items:center;gap:10px;padding:0 16px;max-width:358px}
.chips{display:flex;gap:4px;margin:12px 0;overflow:hidden}
.chip{height:var(--size-chip);padding:0 14px;border-radius:var(--radius-capsule);display:inline-flex;align-items:center;color:var(--color-text-muted);white-space:nowrap}
.chip.sel{background:var(--color-surface-secondary);color:var(--color-text-primary)}
.menu{width:var(--size-menuWidth);max-width:100%;border-radius:var(--radius-menu);background:var(--color-surface-menu);color:var(--color-text-emphasis);padding:6px 0}
.menu div{padding:9px 22px;display:flex}.menu .sep{border-top:var(--border-width-hairline) solid var(--color-border-menu)}
.chart{display:flex;align-items:flex-end;gap:10px;height:90px;margin-top:16px;border-bottom:1px solid var(--color-border-chartGrid)}
.chart i{display:block;width:var(--size-chartBar);background:var(--color-chart-bar);border-radius:3px 3px 0 0}
.heat{display:flex;gap:8px;margin-top:12px}.heat i{width:var(--size-heatDot);height:var(--size-heatDot);border-radius:50%;background:var(--color-surface-secondary)}
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
             "<h3>Orange ramp (core)</h3><p class=\"lede\">The profile's activity heatmap, read in light: four tints up to the chart orange. The empty step is surface.secondary.</p>",
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
