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
NAME = "ChatGPT for iOS"   # PRODUCT (adapt)
OWNER = "OpenAI"    # PRODUCT (adapt): whose visual system it is
LEDE = ("ChatGPT for iOS 26, signed in to a workspace seat, read from stills captured through iPhone Mirroring on 2026-10-23 (dark) and 2026-10-24 (light).")  # PRODUCT (adapt)
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
                      % (esc(css(t["$value"])), esc(".".join(p)), esc(t["$value"])) for p, t in under(("color", "accent")))
    neutrals = "".join('<div class="ramp-step" style="background:%s" title="%s"><code>%s</code></div>'
                       % (esc(t["$value"]), esc(t["$description"]), esc(p[-1] + " " + t["$value"])) for p, t in under(("color", "neutral")))
    radii = "".join('<div class="radius-box" style="border-radius:%s"><code>%s</code><span>%s</span></div>'
                    % (esc(css(t["$value"])), esc(".".join(p)), esc(t["$value"])) for p, t in under(("radius",)))
    spacing = "".join('<div class="space-row"><code>%s</code><span class="bar" style="width:%s"></span><span>%s</span></div>'
                      % (esc(".".join(p)), esc(css(t["$value"])), esc(t["$value"])) for p, t in under(("space",)))
    sizes = "".join('<div class="space-row"><code>%s</code><span class="bar thin" style="width:%s"></span><span>%s</span></div>'
                    % (esc(".".join(p)), esc(css(t["$value"])), esc(t["$value"])) for p, t in under(("size",)))
    sample = {  # PRODUCT (adapt): specimen text per type style
        "titleLarge": "ChatGPT", "menuLarge": "Think harder", "headline": "Correct answer: option 1",
        "body": "A vertex cover of size k exists iff an independent set of size n - k exists.",
        "bubble": "Why does the proposed transformation fail?", "callout": "Work",
        "subheadline": "Could not load your photo. Please try again.", "footnote": "Choose where you start when you open ChatGPT."}
    type_rows = "".join('<tr><th scope="row"><code>%s</code><span class="desc">%s</span></th><td class="meta">%s, %s%s</td>'
                        '<td><span class="type-%s">%s</span></td></tr>'
                        % (esc(".".join(p)), esc(t["$description"]), esc(t["$value"]["fontSize"]), esc(t["$value"]["fontWeight"]),
                           (", line " + t["$value"]["lineHeight"]) if "lineHeight" in t["$value"] else "", p[-1], esc(sample.get(p[-1], "Sample")))
                        for p, t in under(("typography",)))

    # PRODUCT (adapt): specimens built from tokens only
    specimens = """
<div class="spec-grid">
 <div class="spec phone">
  <h3>New chat and composer</h3>
  <div class="screen">
   <div class="nav"><span class="glass round">&#9776;</span><span class="seg type-callout"><span class="on">Chat</span><span>Work</span></span><span class="glass round">&#9711;</span></div>
   <div class="sugg type-body">Compare the two demo plans</div>
   <div class="sugg type-body">Multi-project development recap</div>
   <div class="composer"><div class="type-body ph">Ask ChatGPT</div><div class="tools"><span class="type-headline">+</span><span class="model type-body">6.1 <span class="mut">Medium</span></span><span class="send">&#8593;</span></div></div>
  </div>
  <p class="note">surface.segmentTrack / segmentThumb, size.segmented, text.suggestion, surface.composer, radius.composer, accent.default, size.sendButton</p>
 </div>
 <div class="spec phone">
  <h3>Thread</h3>
  <div class="screen">
   <p class="sys type-footnote">Today 15:42</p>
   <div class="own type-bubble">Why does the proposed transformation generally fail?</div>
   <p class="reply type-headline">Correct answer: option 1.</p>
   <p class="reply type-body">It changes the target condition, so the sum it tests is no longer the one we wanted.</p>
   <p class="acts type-body">&#10697; &#8613; &#8943;</p>
  </div>
  <p class="note">surface.userBubble, text.onUserBubble, radius.bubble, size.bubbleMaxWidth, text.reply, text.timestamp</p>
 </div>
 <div class="spec">
  <h3>Grouped settings</h3>
  <div class="grouped">
   <p class="secthead type-headline">Account</p>
   <div class="card">
    <div class="srow"><span class="type-body">Subscription</span><span class="type-body sec">Premium seat</span></div>
    <div class="srow"><span class="type-body">Accent color</span><span class="type-body sec"><i class="dot acc"></i> Blue <span class="chev">&#8597;</span></span></div>
    <div class="srow"><span class="type-body">Haptic feedback</span><span class="sw-ctl on"></span></div>
   </div>
   <p class="foot type-footnote">Choose where you start when you open ChatGPT.</p>
   <div class="card"><div class="srow"><span class="type-body">Weekly usage limit</span><span class="type-body sec">67% remaining</span></div>
    <div class="meter"><i></i></div></div>
  </div>
  <p class="note">bg.grouped, surface.card, radius.card, border.divider, size.row, text.sectionHeader, text.secondary, switch.on, accent.meter, surface.progressTrack</p>
 </div>
 <div class="spec">
  <h3>Pills, menu, alert</h3>
  <div class="row-btns"><span class="pill type-body">New task</span><span class="ink type-body">New chat</span><span class="tab on type-body">Active</span><span class="tab type-body mut">Paused</span></div>
  <div class="menu"><div class="type-menuLarge"><i class="well"></i>Camera</div><div class="type-menuLarge selected"><i class="well"></i>Think harder &#10003;</div></div>
  <div class="menu small"><div class="type-body">Share</div><div class="type-body">Archive</div><div class="type-body danger">Delete</div></div>
  <div class="alert"><div class="type-headline">Error</div><div class="type-subheadline dbody">Could not load your photo. Please try again.</div>
   <div class="abtns"><span class="type-body">Cancel</span><span class="type-body">Retry</span></div></div>
  <div class="task"><div class="type-body">Multi-project development recap</div><div class="type-footnote mut">Give me a concise Friday recap of progress.</div></div>
  <p class="note">accent.pill, button.ink, surface.tabSelected, surface.menu, radius.menuLarge / menu, text.accent, text.danger, surface.dialog, surface.dialogButton, border.dashed</p>
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
p.lede{color:var(--color-text-muted);margin:4px 0 0;max-width:70ch}p.note{color:var(--color-text-muted);font-size:12px;margin:10px 0 0}
code{font-family:var(--font-mono);font-size:12px}
.toggle{display:inline-flex;border-radius:var(--radius-capsule);padding:3px;gap:2px;background:var(--color-surface-segmentTrack)}
.toggle button{border:0;background:transparent;color:var(--color-text-muted);font:inherit;padding:6px 14px;border-radius:var(--radius-capsule);cursor:pointer}
.toggle button[aria-pressed="true"]{background:var(--color-button-ink-bg);color:var(--color-button-ink-text)}
.scroll{overflow-x:auto}
table.tokens{border-collapse:collapse;width:100%;min-width:660px}
table.tokens th,table.tokens td{text-align:left;vertical-align:top;padding:8px 10px;border-bottom:var(--border-width-hairline) solid var(--color-border-divider)}
table.tokens thead th{color:var(--color-text-muted);font-size:12px;font-weight:400}
table.tokens th[scope=row]{font-weight:500;width:40%}
.desc{display:block;color:var(--color-text-muted);font-size:12px;font-weight:400;margin-top:2px}
.meta{color:var(--color-text-muted);white-space:nowrap}
.sw{display:inline-block;width:28px;height:28px;border-radius:8px;vertical-align:middle;margin-right:8px;border:1px solid var(--color-border-divider);background-image:linear-gradient(45deg,#8883 25%,transparent 25%,transparent 75%,#8883 75%),linear-gradient(45deg,#8883 25%,transparent 25%,transparent 75%,#8883 75%);background-size:8px 8px;background-position:0 0,4px 4px;overflow:hidden}
.sw i{display:block;width:100%;height:100%}
.ev{display:inline-block;font-size:11px;padding:1px 7px;border-radius:var(--radius-capsule);border:1px solid var(--color-border-divider);color:var(--color-text-muted);white-space:nowrap}
.ev-derived{border-style:dashed}.ev-none{border-style:dotted}
.palette{display:flex;flex-wrap:wrap;gap:12px}
.chip-sw{display:flex;flex-direction:column;align-items:center;gap:4px;width:84px;font-size:12px;color:var(--color-text-muted)}
.chip-sw .dot{width:44px;height:44px;border-radius:50%}
.ramp{display:flex;flex-wrap:wrap;border-radius:var(--radius-tile);overflow:hidden;border:1px solid var(--color-border-divider)}
.ramp-step{flex:1 0 76px;height:64px;display:flex;align-items:flex-end;padding:4px}
.ramp-step code{font-size:10px;background:#0008;color:#fff;padding:0 3px;border-radius:3px}
.radii{display:flex;flex-wrap:wrap;gap:16px}
.radius-box{width:120px;height:80px;background:var(--color-surface-card);border:1px solid var(--color-border-divider);display:flex;flex-direction:column;align-items:center;justify-content:center;font-size:12px;color:var(--color-text-muted)}
.space-row{display:grid;grid-template-columns:minmax(150px,240px) 1fr 70px;align-items:center;gap:12px;padding:3px 0}
.space-row .bar{display:block;height:12px;background:var(--color-accent-default);border-radius:2px;max-width:100%}
.space-row .bar.thin{height:8px;background:var(--color-text-muted)}
.spec-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,330px),1fr));gap:16px}
.spec{border:1px solid var(--color-border-divider);border-radius:var(--radius-card);padding:4px 16px 16px;min-width:0}
.screen{background:var(--color-bg-page);border:1px solid var(--color-border-divider);border-radius:var(--radius-menuLarge);padding:12px var(--space-screenMargin) 16px;max-width:390px}
.glass{background:var(--color-surface-glass);color:var(--color-text-primary);display:inline-flex;align-items:center;justify-content:center}
.round{width:var(--size-navButton);height:var(--size-navButton);border-radius:50%;font-size:18px}
.nav{display:flex;justify-content:space-between;align-items:center;margin-bottom:96px}
.seg{display:inline-flex;width:var(--size-segmented-width);height:var(--size-segmented-height);border-radius:var(--radius-capsule);background:var(--color-surface-segmentTrack);padding:0}
.seg span{flex:1;display:flex;align-items:center;justify-content:center;border-radius:var(--radius-capsule)}
.seg .on{background:var(--color-surface-segmentThumb)}
.sugg{color:var(--color-text-suggestion);padding:12px 4px}
.composer{margin-top:12px;border-radius:var(--radius-composer);background:var(--color-surface-composer);padding:14px 16px 10px}
.ph{color:var(--color-text-placeholder);border-left:2px solid var(--color-focus-caret);padding-left:2px}
.tools{display:flex;align-items:center;gap:14px;margin-top:14px}.tools .model{margin-left:auto}
.send{width:var(--size-sendButton);height:var(--size-sendButton);border-radius:50%;background:var(--color-accent-default);color:var(--color-text-onAccent);display:inline-flex;align-items:center;justify-content:center;font-weight:600}
.mut{color:var(--color-text-muted)}.sec{color:var(--color-text-secondary)}.danger{color:var(--color-text-danger)}.selected{color:var(--color-text-accent)}
.sys{color:var(--color-text-timestamp);text-align:center;margin:8px 0 16px}
.own{max-width:var(--size-bubbleMaxWidth);margin-left:auto;border-radius:var(--radius-bubble);background:var(--color-surface-userBubble);color:var(--color-text-onUserBubble);padding:12px 16px}
.reply{color:var(--color-text-reply);margin:16px 0 0}
.acts{color:var(--color-text-reply);margin:var(--space-xxl) 0 0;letter-spacing:12px}
.grouped{background:var(--color-bg-grouped);border-radius:var(--radius-card);padding:8px var(--space-lg) 16px}
.secthead{color:var(--color-text-sectionHeader);margin:12px 0 8px var(--space-xl)}
.foot{color:var(--color-text-footnote);margin:8px var(--space-xl) 16px}
.card{background:var(--color-surface-card);border-radius:var(--radius-card);overflow:hidden}
.srow{display:flex;justify-content:space-between;align-items:center;gap:12px;min-height:var(--size-row);padding:0 16px;border-bottom:var(--border-width-hairline) solid var(--color-border-divider)}
.srow:last-child{border-bottom:0}
.chev{color:var(--color-text-chevron)}
.dot{display:inline-block;width:12px;height:12px;border-radius:50%;vertical-align:middle}.dot.acc{background:var(--color-accent-default)}
.meter{height:var(--size-progress);border-radius:var(--radius-capsule);background:var(--color-surface-progressTrack);margin:0 16px 16px;overflow:hidden}
.meter i{display:block;width:67%;height:100%;background:var(--color-accent-meter);border-radius:var(--radius-capsule)}
.sw-ctl{position:relative;flex:none;width:var(--size-switch-width);height:var(--size-switch-height);border-radius:var(--radius-capsule);background:var(--color-switch-on)}
.sw-ctl::after{content:"";position:absolute;top:2px;right:2px;width:var(--size-switch-thumb);height:calc(var(--size-switch-height) - 4px);border-radius:var(--radius-capsule);background:var(--color-switch-thumb)}
.row-btns{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin-top:14px}
.pill{height:var(--size-pill);padding:0 22px;border-radius:var(--radius-capsule);background:var(--color-accent-pill);color:var(--color-text-onAccent);display:inline-flex;align-items:center}
.ink{height:var(--size-inkButton);padding:0 16px;border-radius:var(--radius-capsule);background:var(--color-button-ink-bg);color:var(--color-button-ink-text);display:inline-flex;align-items:center}
.tab{height:var(--size-tab);padding:0 16px;border-radius:var(--radius-capsule);display:inline-flex;align-items:center}.tab.on{background:var(--color-surface-tabSelected)}
.menu{margin-top:14px;width:var(--size-menuWidth);max-width:100%;border-radius:var(--radius-menuLarge);background:var(--color-surface-menu);padding:10px 8px}
.menu div{padding:10px 12px;display:flex;align-items:center;gap:14px}
.menu.small{border-radius:var(--radius-menu);width:220px}
.well{display:inline-block;width:var(--size-menuIcon);height:var(--size-menuIcon);border-radius:50%;background:var(--color-surface-menuIcon)}
.alert{margin-top:14px;max-width:var(--size-dialog-width);border-radius:var(--radius-dialog);background:var(--color-surface-dialog);padding:22px 16px 16px}
.alert>div:first-child{padding:0 14px}.dbody{color:var(--color-text-dialogBody);padding:6px 14px 0}
.abtns{display:flex;gap:8px;margin-top:20px}.abtns span{flex:1;height:var(--size-dialog-button);border-radius:var(--radius-capsule);background:var(--color-surface-dialogButton);color:var(--color-button-dialog-text);display:flex;align-items:center;justify-content:center}
.task{margin-top:14px;border-radius:var(--radius-card);background:var(--color-surface-taskCard);border:var(--border-width-dashed) dashed var(--color-border-dashed);padding:14px 16px}
footer{margin-top:48px;color:var(--color-text-muted);font-size:12px}
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
             "<h3>Accent palette (core)</h3><p class=\"lede\">The Accent color menu's nine colours. The tenth option, White in dark and Black in light, is color.accent.inkOption. Only Blue was applied.</p>",
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
