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

FONT_STACK = '"Google Sans", "Google Sans Text", -apple-system, system-ui, "Helvetica Neue", Arial, sans-serif'
MONO_STACK = 'ui-monospace, "SF Mono", Menlo, monospace'
NAME = "Gemini"   # PRODUCT (adapt)
OWNER = "Google"    # PRODUCT (adapt): whose visual system it is
LEDE = ("Gemini for iOS 26, read from stills captured through iPhone Mirroring on 2026-10-23 (dark) and 2026-10-24 (light).")  # PRODUCT (adapt)
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
    neutrals = "".join('<div class="ramp-step" style="background:%s" title="%s"><code>%s</code></div>'
                       % (esc(t["$value"]), esc(t["$description"]), esc(p[-1] + " " + t["$value"])) for p, t in under(("color", "neutral")))
    radii = "".join('<div class="radius-box" style="border-radius:%s"><code>%s</code><span>%s</span></div>'
                    % (esc(css(t["$value"])), esc(".".join(p)), esc(t["$value"])) for p, t in under(("radius",)))
    spacing = "".join('<div class="space-row"><code>%s</code><span class="bar" style="width:%s"></span><span>%s</span></div>'
                      % (esc(".".join(p)), esc(css(t["$value"])), esc(t["$value"])) for p, t in under(("space",)))
    sizes = "".join('<div class="space-row"><code>%s</code><span class="bar thin" style="width:%s"></span><span>%s</span></div>'
                    % (esc(".".join(p)), esc(css(t["$value"])), esc(t["$value"])) for p, t in under(("size",)))
    sample = {  # PRODUCT (adapt): specimen text per type style
        "display": "Let's jump in", "titleLarge": "Settings", "title": "Usage limits", "body": "I can create more videos as soon as your limit resets.",
        "bodyStrong": "No results", "callout": "Add to notebook", "subheadline": "Choose how Gemini will sound", "footnote": "Gemini is AI and can make mistakes.",
        "caption": "Chat", "caption2": "Fastest answers"}
    type_rows = "".join('<tr><th scope="row"><code>%s</code><span class="desc">%s</span></th><td class="meta">%s, %s%s</td>'
                        '<td><span class="type-%s">%s</span></td></tr>'
                        % (esc(".".join(p)), esc(t["$description"]), esc(t["$value"]["fontSize"]), esc(t["$value"]["fontWeight"]),
                           (", line " + t["$value"]["lineHeight"]) if "lineHeight" in t["$value"] else "", p[-1], esc(sample.get(p[-1], "Sample")))
                        for p, t in under(("typography",)))

    # PRODUCT (adapt): specimens built from tokens only
    specimens = """
<div class="spec-grid">
 <div class="spec phone">
  <h3>Home</h3>
  <div class="screen home">
   <div class="nav"><span class="glass round">&#8801;</span><span class="title type-body">Gemini <span class="sec">Flash-Lite</span> &#8964;<i class="dot"></i></span><span class="glass round">&#9998;</span></div>
   <p class="greet type-display">Let&#8217;s jump in</p>
   <div class="toggle-seg"><span class="seg on type-caption">Chat</span><span class="seg type-caption">Task</span></div>
   <div class="composer"><span class="plus">+</span><span class="type-body ph">Ask Gemini</span><span class="voice">&#8214;</span></div>
  </div>
  <p class="note">bg.page, bg.glow, surface.glass, surface.segment, surface.composer, size.composer, button.voice, accent.dot</p>
 </div>
 <div class="spec phone">
  <h3>Thread</h3>
  <div class="screen">
   <div class="own type-body">Okay just one motion, extend, relax</div>
   <p class="reply type-body">I can create more videos as soon as your limit resets. Check your usage in Settings.</p>
   <p class="acts sec">&#8679; &#128077; &#128078; &#8943;</p>
   <p class="type-footnote ter">Gemini is AI and can make mistakes.</p>
   <div class="composer typed"><span class="plus">+</span><span class="type-body">hello</span><span class="send">&#8593;</span></div>
  </div>
  <p class="note">surface.container, radius.bubble, text.primary, text.tertiary, size.composer.widthTyped, button.send</p>
 </div>
 <div class="spec">
  <h3>Grouped settings card</h3>
  <p class="secthead type-subheadline">Preferences</p>
  <div class="card">
   <div class="srow"><span class="type-body">Notifications</span><span class="ter">&#8250;</span></div>
   <div class="srow"><span class="type-body">Theme</span><span class="type-body sec">System default &#8645;</span></div>
   <div class="srow"><span class="type-body">Interrupt Live responses<span class="type-subheadline sec blk">Talk to interrupt Gemini in Live chats</span></span><span class="sw-sys"></span></div>
  </div>
  <div class="mem"><span class="type-title">Your instructions</span><span class="sw-mat"><b>&#10003;</b></span></div>
  <p class="note">surface.card, border.divider, radius.card, size.row, switch.onSystem / thumbSystem (iOS), switch.on / thumb / tick (Material)</p>
 </div>
 <div class="spec">
  <h3>Buttons, menu, cards</h3>
  <div class="glowbox"><button class="btn type-body" type="button">Get started</button></div>
  <div class="row-btns"><span class="tonal type-body">+ Add</span><span class="type-body act">Done</span><span class="badge type-subheadline">PRO</span><a class="link type-body">Learn more</a></div>
  <div class="menu"><div class="type-callout">Share</div><div class="type-callout">Rename</div><div class="type-callout danger">Delete</div></div>
  <div class="sug"><div class="type-body">Create a news digest</div><div class="type-subheadline sec">Get a daily deep dive on any topic I&#8217;m curious about.</div></div>
  <div class="rowcard type-body">Manage your Google Account</div>
  <p class="note">button.primary, button.tonal, text.action, surface.container, text.link, surface.menu, text.danger, surface.raised, radius.cardSuggestion, surface.rowCard</p>
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
.toggle{display:inline-flex;border-radius:var(--radius-capsule);padding:3px;gap:2px;background:var(--color-surface-container)}
.toggle button{border:0;background:transparent;color:var(--color-text-secondary);font:inherit;padding:6px 14px;border-radius:var(--radius-capsule);cursor:pointer}
.toggle button[aria-pressed="true"]{background:var(--color-button-primary-bg);color:var(--color-button-primary-text)}
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
.space-row .bar{display:block;height:12px;background:var(--color-accent-primary);border-radius:2px;max-width:100%}
.space-row .bar.thin{height:8px;background:var(--color-text-tertiary)}
.spec-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,330px),1fr));gap:16px}
.spec{border:1px solid var(--color-border-divider);border-radius:var(--radius-card);padding:4px 16px 16px;min-width:0}
.screen{background:var(--color-bg-page);border:1px solid var(--color-border-divider);border-radius:var(--radius-sheet);padding:12px var(--space-screenMargin) 16px;max-width:390px;overflow:hidden}
.screen.home{background:linear-gradient(to bottom,var(--color-bg-page) 55%,var(--color-bg-glow))}
.glass{background:var(--color-surface-glass);color:var(--color-text-onGlass);display:inline-flex;align-items:center;justify-content:center}
.round{width:var(--size-navButton);height:var(--size-navButton);border-radius:50%;font-size:20px;flex:none}
.nav{display:flex;justify-content:space-between;align-items:center;gap:8px}
.nav .title{flex:1;padding-left:8px}
.dot{display:inline-block;width:6px;height:6px;border-radius:50%;background:var(--color-accent-dot);margin-left:6px;vertical-align:middle}
.greet{text-align:center;margin:120px 0 110px;color:var(--color-text-primary)}
.toggle-seg{display:flex;justify-content:center;gap:12px;margin-bottom:10px}
.seg{width:var(--size-segment-width);height:var(--size-segment-height);border-radius:var(--radius-capsule);display:inline-flex;align-items:center;justify-content:center;color:var(--color-text-onGlass)}
.seg.on{background:var(--color-surface-segment);border:var(--border-width-hairline) solid var(--color-border-divider)}
.composer{height:var(--size-composer-height);width:min(100%,var(--size-composer-width));margin:0 auto;border-radius:var(--radius-capsule);background:var(--color-surface-composer);display:flex;align-items:center;gap:var(--space-sm);padding:0 15px 0 22px}
.composer.typed{width:min(100%,var(--size-composer-widthTyped))}
.composer .ph{flex:1;color:var(--color-text-placeholder)}.composer.typed .type-body{flex:1}
.plus{font-size:26px;color:var(--color-text-primary);width:24px}
.voice,.send{width:var(--size-sendButton);height:var(--size-sendButton);border-radius:50%;display:inline-flex;align-items:center;justify-content:center;flex:none}
.voice{background:var(--color-button-voice-bg);color:var(--color-button-voice-glyph)}
.send{background:var(--color-button-send-bg);color:var(--color-button-send-glyph);font-weight:600}
.own{max-width:85%;margin:8px 0 8px auto;border-radius:var(--radius-bubble);padding:20px var(--space-xxl);background:var(--color-surface-container);color:var(--color-text-primary)}
.reply{margin:20px 8px 6px}.acts{margin:0 8px 18px;letter-spacing:12px}
.sec{color:var(--color-text-secondary)}.ter{color:var(--color-text-tertiary)}.danger{color:var(--color-text-danger)}.blk{display:block}
.card{background:var(--color-surface-card);border-radius:var(--radius-card);max-width:358px;overflow:hidden;padding:0 0 0 20px}
.srow{display:flex;justify-content:space-between;align-items:center;gap:12px;min-height:var(--size-row);padding:8px 20px 8px 0;border-bottom:var(--border-width-hairline) solid var(--color-border-divider)}
.srow:last-child{border-bottom:0}
.secthead{color:var(--color-text-tertiary);margin:8px 0 8px 20px}
.sw-sys{position:relative;flex:none;width:var(--size-switchSystem-width);height:var(--size-switchSystem-height);border-radius:var(--radius-capsule);background:var(--color-switch-onSystem)}
.sw-sys::after{content:"";position:absolute;top:2px;right:2px;width:38px;height:calc(var(--size-switchSystem-height) - 4px);border-radius:var(--radius-capsule);background:var(--color-switch-thumbSystem)}
.mem{display:flex;justify-content:space-between;align-items:center;max-width:358px;margin-top:16px}
.sw-mat{position:relative;flex:none;width:var(--size-switch-width);height:var(--size-switch-height);border-radius:var(--radius-capsule);background:var(--color-switch-on)}
.sw-mat b{position:absolute;top:3px;right:3px;width:calc(var(--size-switch-height) - 6px);height:calc(var(--size-switch-height) - 6px);border-radius:50%;background:var(--color-switch-thumb);color:var(--color-switch-tick);font-size:14px;display:flex;align-items:center;justify-content:center}
.glowbox{border-radius:var(--radius-card);padding:16px;background:linear-gradient(to bottom,var(--color-bg-page),var(--color-bg-glow))}
.btn{display:block;width:100%;height:var(--size-button);border:0;border-radius:var(--radius-capsule);background:var(--color-button-primary-bg);color:var(--color-button-primary-text);font-family:var(--font-base)}
.row-btns{display:flex;flex-wrap:wrap;gap:14px;align-items:center;margin-top:14px}
.tonal{height:var(--size-buttonTonal);padding:0 22px;border-radius:var(--radius-capsule);background:var(--color-button-tonal-bg);color:var(--color-button-tonal-text);display:inline-flex;align-items:center}
.act{color:var(--color-text-action)}
.badge{padding:3px 8px;border-radius:8px;background:var(--color-surface-container);color:var(--color-text-badge)}
.link{color:var(--color-text-link)}
.menu{margin-top:14px;width:var(--size-menuWidth);max-width:100%;border-radius:var(--radius-menu);background:var(--color-surface-menu);color:var(--color-text-onGlass);padding:6px 0}
.menu div{min-height:var(--size-menuRow);display:flex;align-items:center;padding:0 24px}
.sug{margin-top:14px;max-width:358px;background:var(--color-surface-raised);border-radius:var(--radius-cardSuggestion);padding:var(--space-xl)}
.rowcard{margin-top:var(--space-md);max-width:358px;height:var(--size-rowCard);border-radius:var(--radius-capsule);background:var(--color-surface-rowCard);display:flex;align-items:center;padding:0 22px}
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
             + "The font looks like Google Sans, which is not bundled, so the page falls back to the platform sans. "
             "Glass is drawn as its centre colour: the real material blurs what is behind it.</p></div>",
             '<div class="toggle" role="group" aria-label="Theme"><button type="button" data-set-theme="light" aria-pressed="false">Light</button>'
             '<button type="button" data-set-theme="dark" aria-pressed="true">Dark</button></div></header>',
             "<h2>Colour</h2>",
             '<p class="lede">Light and dark side by side. The badge says how each value was read: Sampled (a flat fill, exact), Sampled (text) '
             "(the anti-aliased pixel furthest from the fill), Derived (worked out, or a glass or gradient reading). Hover a swatch for its capture.</p>",
             "".join(colour_html),
             # PRODUCT (adapt): the ramp caption
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
