#!/usr/bin/env python3
"""Render style-guide.html from tokens.json (native kit, from systems/grokbot).

    python3 tools/build_style_guide.py

Every token becomes a CSS custom property (its path joined with dashes; an alias becomes a var()
reference), so the swatches, scales and specimens cannot drift from the file. NAME, LEDE, OWNER,
`sample` and `specimens` are Telegram's; specimens are drawn from tokens only, never the product's
artwork.
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
NAME = "Telegram"
OWNER = "Telegram FZ-LLC"
LEDE = ("Telegram for iOS 26, read from stills captured through iPhone Mirroring on 2026-10-23 (dark) and 2026-10-24 (light).")
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
    chip = lambda group: "".join('<div class="chip-sw"><span class="dot" style="background:%s"></span><code>%s</code><span>%s</span></div>'
                                 % (esc(css(t["$value"])), esc(".".join(p)), esc(t["$value"])) for p, t in under(("color", group)))
    palette, tiles = chip("avatar"), chip("iconTile")
    neutrals = "".join('<div class="ramp-step" style="background:%s" title="%s"><code>%s</code></div>'
                       % (esc(t["$value"]), esc(t["$description"]), esc(p[-1] + " " + t["$value"])) for p, t in under(("color", "neutral")))
    radii = "".join('<div class="radius-box" style="border-radius:%s"><code>%s</code><span>%s</span></div>'
                    % (esc(css(t["$value"])), esc(".".join(p)), esc(t["$value"])) for p, t in under(("radius",)))
    spacing = "".join('<div class="space-row"><code>%s</code><span class="bar" style="width:%s"></span><span>%s</span></div>'
                      % (esc(".".join(p)), esc(css(t["$value"])), esc(t["$value"])) for p, t in under(("space",)))
    sizes = "".join('<div class="space-row"><code>%s</code><span class="bar thin" style="width:%s"></span><span>%s</span></div>'
                    % (esc(".".join(p)), esc(css(t["$value"])), esc(t["$value"])) for p, t in under(("size",)))
    sample = {"profileName": "kai chen", "navTitle": "Notifications", "body": "Privacy and Security", "bubble": "Do you know what time it is?",
              "chatTitle": "books & brunches", "subheadline": "next meetup moved to saturday, bring the maps!!",
              "quote": "Build documentation websites, blogs, marketing pages, and more.", "footnote": "Tap 'Edit' to change the order or delete folders.",
              "caption": "Chats 23:08"}
    type_rows = "".join('<tr><th scope="row"><code>%s</code><span class="desc">%s</span></th><td class="meta">%s, %s%s</td>'
                        '<td><span class="type-%s">%s</span></td></tr>'
                        % (esc(".".join(p)), esc(t["$description"]), esc(t["$value"]["fontSize"]), esc(t["$value"]["fontWeight"]),
                           (", line " + t["$value"]["lineHeight"]) if "lineHeight" in t["$value"] else "", p[-1], esc(sample.get(p[-1], "Sample")))
                        for p, t in under(("typography",)))

    specimens = """
<div class="spec-grid">
 <div class="spec phone">
  <h3>Chat list</h3>
  <div class="screen">
   <div class="nav"><span class="glass cap type-body">Edit</span><span class="type-navTitle">Chats</span><span class="round accent">&#9998;</span></div>
   <div class="chips"><span class="chip on type-subheadline">All</span><span class="chip type-subheadline">os</span><span class="chip type-subheadline">hobby</span><span class="chip type-subheadline">groups <b class="count">19</b></span></div>
   <div class="crow pinned"><span class="av" style="background:var(--color-avatar-purple)"></span><div><div class="type-chatTitle">books &amp; brunches</div><div class="type-subheadline prev">next meetup moved to saturday, bring the maps!!</div></div><span class="type-footnote time">11:27</span></div>
   <div class="crow pinned"><span class="av" style="background:var(--color-avatar-blue)"></span><div><div class="type-chatTitle">kai's stash</div><div class="type-subheadline prev">You: insanely funny PR</div></div><span class="type-footnote time"><i class="tick">&#10003;</i> 08/10</span></div>
   <div class="crow"><span class="av" style="background:var(--color-avatar-green)"></span><div><div class="type-chatTitle">Mira</div><div class="type-subheadline prev">see you!!</div></div><span class="type-footnote time">14:53</span></div>
   <div class="tabbar"><span class="type-caption">Contacts</span><span class="type-caption">Calls</span><span class="type-caption sel">Chats</span><span class="type-caption">Settings</span></div>
  </div>
  <p class="note">bg.chats, bg.pinned, surface.chipBar / chipSelected, badge.muted, size.rowChat, size.avatarChat, text.preview, text.readMark, surface.tabBar / tabSelected</p>
 </div>
 <div class="spec phone">
  <h3>Thread</h3>
  <div class="screen thread">
   <p class="svc type-footnote">"Tech" was created</p>
   <div class="bin type-bubble">Do you know what time it is?</div>
   <div class="bout type-bubble"><a class="blink">https://docusaurus.io/</a><div class="quote"><b class="qt type-subheadline">docusaurus.io</b><span class="type-quote">Build documentation websites, blogs, marketing pages, and more.</span></div><span class="meta type-caption">23:08 &#10003;</span></div>
   <div class="composer"><span class="round glass">&#128206;</span><span class="field-c type-body">hey<i class="caret"></i></span><span class="send">&#10148;</span></div>
  </div>
  <p class="note">surface.bubbleIn, surface.bubbleOut to bubbleOutEnd, surface.quote, text.quoteTitle, surface.service, surface.glass (surface.composer is a reading over one wallpaper), accent.send, focus.caret, radius.bubble</p>
 </div>
 <div class="spec">
  <h3>Grouped settings</h3>
  <p class="secthead type-footnote">MESSAGE NOTIFICATIONS</p>
  <div class="card">
   <div class="srow two"><span class="tile" style="background:var(--color-iconTile-blue)"></span><span class="grow type-body">Private Chats<span class="type-subheadline sec blk">173 exceptions</span></span><span class="type-body val">On &#8250;</span></div>
   <div class="srow"><span class="tile" style="background:var(--color-iconTile-green)"></span><span class="grow type-body">Group Chats</span><span class="type-body val">Off &#8250;</span></div>
   <div class="srow"><span class="grow type-body">In-App Sounds</span><span class="sw-ctl on"></span></div>
   <div class="srow"><span class="grow type-body">In-App Vibrate</span><span class="sw-ctl"></span></div>
   <div class="srow"><span class="grow type-body dis">Night Mode</span><span class="sw-ctl dis"></span></div>
  </div>
  <p class="foot type-footnote">Logs out all devices except for this one.</p>
  <div class="card"><div class="srow"><span class="grow type-body link">Change Profile Photo</span></div><div class="srow"><span class="grow type-body danger">Terminate all other sessions</span></div></div>
  <p class="note">bg.grouped, surface.card, radius.card, border.divider, size.row / rowTwoLine, color.iconTile, text.value, switch.on / off / offDisabled, text.link, text.danger</p>
 </div>
 <div class="spec">
  <h3>Buttons, search, segments, menu</h3>
  <div class="search type-body">&#9906; Search</div>
  <button class="btn type-navTitle" type="button">Add Device</button>
  <div class="row-btns"><span class="seg"><span class="on type-subheadline">All</span><span class="type-subheadline">Missed</span></span><span class="pill type-footnote">ADD</span><span class="round glass">&#8249;</span></div>
  <div class="menu"><div class="type-body">Reply</div><div class="type-body">Copy Link</div><div class="type-body danger">Delete</div></div>
  <p class="note">surface.search, size.search, accent.default, size.button, surface.segmented / segmentedSelected, accent.pill, surface.glass, surface.menuPlain, radius.menu, text.dangerMenu</p>
 </div>
</div>
"""

    page_css = """
*{box-sizing:border-box}
html,body{background:var(--color-bg-chats)}
body{margin:0;color:var(--color-text-primary);font-family:var(--font-base);font-size:15px;line-height:1.45}
.wrap{max-width:1080px;margin:0 auto;padding:24px 16px 64px}
header.top{display:flex;flex-wrap:wrap;gap:12px 24px;align-items:center;justify-content:space-between}
h1{font-size:26px;margin:0}h2{font-size:20px;margin:40px 0 8px}h3{font-size:15px;margin:20px 0 8px}
p.lede{color:var(--color-text-secondary);margin:4px 0 0;max-width:70ch}p.note{color:var(--color-text-secondary);font-size:12px;margin:10px 0 0}
code{font-family:var(--font-mono);font-size:12px}
.toggle{display:inline-flex;border-radius:var(--radius-capsule);padding:3px;gap:2px;background:var(--color-surface-search)}
.toggle button{border:0;background:transparent;color:var(--color-text-secondary);font:inherit;padding:6px 14px;border-radius:var(--radius-capsule);cursor:pointer}
.toggle button[aria-pressed="true"]{background:var(--color-accent-default);color:var(--color-text-onAccent)}
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
.radius-box{width:120px;height:80px;background:var(--color-surface-card);border:1px solid var(--color-border-divider);display:flex;flex-direction:column;align-items:center;justify-content:center;font-size:12px;color:var(--color-text-secondary)}
.space-row{display:grid;grid-template-columns:minmax(150px,240px) 1fr 70px;align-items:center;gap:12px;padding:3px 0}
.space-row .bar{display:block;height:12px;background:var(--color-accent-default);border-radius:2px;max-width:100%}
.space-row .bar.thin{height:8px;background:var(--color-text-secondary)}
.spec-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,330px),1fr));gap:16px}
.spec{border:1px solid var(--color-border-divider);border-radius:var(--radius-card);padding:4px 16px 16px;min-width:0}
.screen{background:var(--color-bg-chats);border:1px solid var(--color-border-divider);border-radius:var(--radius-sheet);padding:12px 0 12px;max-width:390px;overflow:hidden}
.screen.thread{background:linear-gradient(160deg,var(--color-bg-pinned),var(--color-bg-grouped));padding:12px var(--space-screenMargin)}
.glass{background:var(--color-surface-glass);color:var(--color-text-primary);display:inline-flex;align-items:center;justify-content:center}
.round{width:var(--size-navButton);height:var(--size-navButton);border-radius:50%;font-size:20px;flex:none;display:inline-flex;align-items:center;justify-content:center}
.round.accent{background:var(--color-accent-compose);color:var(--color-text-onAccent)}
.cap{height:var(--size-navButton);padding:0 16px;border-radius:var(--radius-capsule)}
.nav{display:flex;justify-content:space-between;align-items:center;padding:0 var(--space-screenMargin) 0;margin-bottom:10px}
.chips{display:flex;gap:4px;align-items:center;height:var(--size-chipBar);margin:0 var(--space-screenMargin) 8px;padding:0 3px;border-radius:var(--radius-capsule);background:var(--color-surface-chipBar);overflow:hidden}
.chip{height:var(--size-chip);padding:0 14px;border-radius:var(--radius-capsule);display:inline-flex;align-items:center;gap:6px;font-weight:500;white-space:nowrap}
.chip.on{background:var(--color-surface-chipSelected)}
.count{font-size:11px;padding:1px 6px;border-radius:var(--radius-capsule);background:var(--color-badge-muted);color:var(--color-text-onAccent)}
.crow{display:flex;gap:var(--space-md);align-items:center;min-height:var(--size-rowChat);padding:0 var(--space-screenMargin);border-bottom:var(--border-width-hairline) solid var(--color-border-list)}
.crow.pinned{background:var(--color-bg-pinned)}.crow>div{flex:1;min-width:0}
.av{display:inline-block;width:var(--size-avatarChat);height:var(--size-avatarChat);border-radius:50%;flex:none}
.prev{color:var(--color-text-preview);display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.time{color:var(--color-text-time);align-self:flex-start;margin-top:12px;white-space:nowrap}.tick{color:var(--color-text-readMark);font-style:normal}
.tabbar{display:flex;justify-content:space-around;align-items:center;height:var(--size-tabBar-height);margin:16px var(--space-lg) 0;border-radius:var(--radius-capsule);background:var(--color-surface-tabBar);color:var(--color-text-tab);padding:0 4px}
.tabbar .sel{color:var(--color-text-tabSelected);background:var(--color-surface-tabSelected);border-radius:var(--radius-capsule);padding:18px 16px}
.svc{width:max-content;margin:0 auto 10px;padding:3px 10px;border-radius:var(--radius-capsule);background:var(--color-surface-service);color:var(--color-text-service)}
.bin,.bout{max-width:290px;border-radius:var(--radius-bubble);padding:8px 12px;margin:8px 0}
.bin{background:var(--color-surface-bubbleIn);color:var(--color-text-primary)}
.bout{margin-left:auto;background:linear-gradient(var(--color-surface-bubbleOut),var(--color-surface-bubbleOutEnd));color:var(--color-text-onBubbleOut)}
.blink{color:var(--color-text-bubbleLink);text-decoration:underline}
.quote{background:var(--color-surface-quote);border-left:3px solid var(--color-text-quoteTitle);border-radius:6px;padding:6px 8px;margin:6px 0;display:flex;flex-direction:column}
.qt{color:var(--color-text-quoteTitle)}.bout .meta{display:block;text-align:right;color:var(--color-text-bubbleMeta)}
.composer{display:flex;gap:8px;align-items:center;margin-top:14px}
.field-c{flex:1;height:var(--size-navButton);border-radius:var(--radius-capsule);background:var(--color-surface-glass);color:var(--color-text-primary);display:flex;align-items:center;padding:0 16px}
.caret{display:inline-block;width:2px;height:20px;background:var(--color-focus-caret);margin-left:1px}
.send{width:var(--size-send-width);height:var(--size-send-height);border-radius:var(--radius-capsule);background:var(--color-accent-send);color:var(--color-text-onAccent);display:inline-flex;align-items:center;justify-content:center;flex:none}
.secthead{color:var(--color-text-sectionHeader);margin:12px 0 6px 16px}.foot{color:var(--color-text-footnote);margin:6px 16px 14px}
.card{background:var(--color-surface-card);border-radius:var(--radius-card);max-width:358px;overflow:hidden}
.spec>.card{box-shadow:0 0 0 12px var(--color-bg-grouped)}
.srow{display:flex;align-items:center;gap:var(--space-md);min-height:var(--size-row);padding:6px 16px;border-bottom:var(--border-width-hairline) solid var(--color-border-divider)}
.srow:last-child{border-bottom:0}.srow.two{min-height:var(--size-rowTwoLine)}.grow{flex:1}
.tile{width:var(--size-iconTile);height:var(--size-iconTile);border-radius:var(--radius-iconTile);flex:none}
.sec{color:var(--color-text-secondary)}.val{color:var(--color-text-value)}.blk{display:block}
.danger{color:var(--color-text-danger)}.link{color:var(--color-text-link)}.dis{color:var(--color-text-disabled)}
.sw-ctl{position:relative;flex:none;width:var(--size-switch-width);height:var(--size-switch-height);border-radius:var(--radius-capsule);background:var(--color-switch-off)}
.sw-ctl::after{content:"";position:absolute;top:2px;left:2px;width:var(--size-switch-thumb);height:calc(var(--size-switch-height) - 4px);border-radius:var(--radius-capsule);background:var(--color-switch-thumb);box-shadow:0 1px 2px #0003}
.sw-ctl.on{background:var(--color-switch-on)}.sw-ctl.on::after{left:auto;right:2px}
.sw-ctl.dis{background:var(--color-switch-offDisabled)}.sw-ctl.dis::after{background:var(--color-switch-thumbDisabled)}
.search{height:var(--size-search);border-radius:var(--radius-capsule);background:var(--color-surface-search);color:var(--color-text-placeholder);display:flex;align-items:center;justify-content:center;max-width:358px;margin-top:12px}
.btn{display:block;width:100%;max-width:358px;height:var(--size-button);margin:12px 0 0;border:0;border-radius:var(--radius-capsule);background:var(--color-accent-default);color:var(--color-text-onAccent);font-family:var(--font-base)}
.row-btns{display:flex;flex-wrap:wrap;gap:10px;align-items:center;margin-top:14px}
.seg{display:inline-flex;height:var(--size-segmented-height);width:var(--size-segmented-width);padding:3px;border-radius:var(--radius-capsule);background:var(--color-surface-segmented)}
.seg span{flex:1;display:inline-flex;align-items:center;justify-content:center;border-radius:var(--radius-capsule);font-weight:500}.seg .on{background:var(--color-surface-segmentedSelected)}
.pill{height:var(--size-pill);padding:0 14px;border-radius:var(--radius-capsule);background:var(--color-accent-pill);color:var(--color-text-onAccent);display:inline-flex;align-items:center;font-weight:600}
.menu{margin-top:14px;width:250px;max-width:100%;border-radius:var(--radius-menu);background:var(--color-surface-menuPlain);padding:8px 0}
.menu div{padding:10px 24px}
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
             "Glass is drawn as its centre colour: the real material blurs what is behind it. The thread's wallpaper is a stand-in gradient.</p></div>",
             '<div class="toggle" role="group" aria-label="Theme"><button type="button" data-set-theme="light" aria-pressed="false">Light</button>'
             '<button type="button" data-set-theme="dark" aria-pressed="true">Dark</button></div></header>',
             "<h2>Colour</h2>",
             '<p class="lede">Light and dark side by side. The badge says how each value was read: Sampled (a flat fill, exact), Sampled (text) '
             "(the anti-aliased pixel furthest from the fill), Derived (worked out, or a glass or gradient reading). Hover a swatch for its capture.</p>",
             "".join(colour_html),
             # PRODUCT (adapt): the palette and ramp captions
             "<h3>Icon tiles (core)</h3><p class=\"lede\">The gradient tiles that lead settings rows. Each swatch is one band of its gradient.</p>",
             '<div class="palette">%s</div>' % tiles,
             "<h3>Initials avatars (core)</h3><p class=\"lede\">The gradients behind a contact's initials when it has no photo.</p>",
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
