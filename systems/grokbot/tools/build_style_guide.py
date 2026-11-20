#!/usr/bin/env python3
"""Render style-guide.html from tokens.json (Grok Bot iOS design reference).

    python3 tools/build_style_guide.py

Every token becomes a CSS custom property (its path joined with dashes; an alias becomes a var()
reference), so the swatches, scales and specimens cannot drift from the file. The avatars are plain
circles in the palette colours: Grok Bot's blob characters are its artwork and are not redrawn.
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
EV_CLASS = {"Sampled": "ev-sampled", "Sampled (text)": "ev-text", "Derived": "ev-derived", "Reconstruction": "ev-derived", "Not captured": "ev-none"}


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
                      % (esc(css(t["$value"])), esc(".".join(p)), esc(t["$value"])) for p, t in under(("color", "avatar")))
    neutrals = "".join('<div class="ramp-step" style="background:%s" title="%s"><code>%s</code></div>'
                       % (esc(t["$value"]), esc(t["$description"]), esc(p[-1] + " " + t["$value"])) for p, t in under(("color", "neutral")))
    radii = "".join('<div class="radius-box" style="border-radius:%s"><code>%s</code><span>%s</span></div>'
                    % (esc(css(t["$value"])), esc(".".join(p)), esc(t["$value"])) for p, t in under(("radius",)))
    spacing = "".join('<div class="space-row"><code>%s</code><span class="bar" style="width:%s"></span><span>%s</span></div>'
                      % (esc(".".join(p)), esc(css(t["$value"])), esc(t["$value"])) for p, t in under(("space",)))
    sizes = "".join('<div class="space-row"><code>%s</code><span class="bar thin" style="width:%s"></span><span>%s</span></div>'
                    % (esc(".".join(p)), esc(css(t["$value"])), esc(t["$value"])) for p, t in under(("size",)))
    sample = {"titleLarge": "[Tutor] Hardware", "fieldLarge": "Name your Bot", "body": "Picture this code before we go on.",
              "rowTitle": "Executives", "button": "Create", "callout": "Ask [Tutor] Hardware", "preview": "New standing role from Kai",
              "subheadline": "Tools and skills for Grok Bot", "footnote": "Get notified when this Bot finishes", "caption": "[Studio] Lead"}
    type_rows = "".join('<tr><th scope="row"><code>%s</code><span class="desc">%s</span></th><td class="meta">%s, %s%s</td>'
                        '<td><span class="type-%s">%s</span></td></tr>'
                        % (esc(".".join(p)), esc(t["$description"]), esc(t["$value"]["fontSize"]), esc(t["$value"]["fontWeight"]),
                           (", line " + t["$value"]["lineHeight"]) if "lineHeight" in t["$value"] else "", p[-1], esc(sample.get(p[-1], "Sample")))
                        for p, t in under(("typography",)))

    specimens = """
<div class="spec-grid">
 <div class="spec phone">
  <h3>Thread</h3>
  <div class="screen">
   <div class="nav"><span class="glass round">&#8249;</span><span class="glass title type-rowTitle"><span class="av sm" style="background:var(--color-avatar-amber)"></span>[Tutor] Hardware</span><span class="glass round">&#8943;</span></div>
   <div class="own type-body">why does superscalar sound so impressive?</div>
   <div class="bub type-body">Because "single instruction stream" describes the program, not the hardware.</div>
   <div class="bub joined type-body">Picture this code:<pre class="code">a = b + c
d = e * f</pre>See <a class="link">Computer Architecture</a>.</div>
   <p class="sys type-subheadline">Today 7:03 AM</p>
   <div class="composer"><span class="glass round big">+</span><span class="field-c type-callout">Ask [Tutor] Hardware<span class="send">&#8593;</span></span></div>
  </div>
  <p class="note">surface.bubble, surface.ownBubble, surface.code, radius.bubble / bubbleJoined / code, size.composer, surface.glass, button.send</p>
 </div>
 <div class="spec phone">
  <h3>Home grid and list row</h3>
  <div class="screen">
   <div class="grid"><div><span class="av" style="background:var(--color-avatar-pink)"></span><span class="type-subheadline lab">Chief of St&#8230; <i class="dot"></i></span></div>
    <div><span class="av" style="background:var(--color-avatar-orange)"></span><span class="type-subheadline lab">[Tutor] Lead</span></div>
    <div><span class="av" style="background:var(--color-avatar-teal)"></span><span class="type-subheadline lab">[Pulse] Lead</span></div></div>
   <div class="lrow"><span class="av md" style="background:var(--color-avatar-purple)"></span><div><div class="type-rowTitle">Hackerspace</div><div class="type-preview sec">New standing role from Kai</div></div><span class="type-footnote ter">Wednesday</span></div>
   <div class="pill type-callout">&#8964; 3 unread</div>
   <div class="search type-callout">&#9906; Search</div>
  </div>
  <p class="note">size.avatarGrid, text.secondary, text.tertiary, accent.default, accent.pill, size.searchBar</p>
 </div>
 <div class="spec">
  <h3>Grouped settings card</h3>
  <div class="card">
   <div class="srow"><span class="type-body">Auto-review<span class="type-subheadline sec blk">Require approval for risky actions.</span></span><span class="sw-ctl on"></span></div>
   <div class="srow"><span class="type-body">Notifications</span><span class="sw-ctl"></span></div>
   <div class="srow"><span class="type-body">Routines</span><span class="type-body sec">3 on &#8250;</span></div>
   <div class="srow"><span class="type-body">Notifications (bot)</span><span class="sw-ctl bot"></span></div>
  </div>
  <p class="secthead type-subheadline">Bot</p>
  <div class="card"><div class="srow"><span class="type-body danger">Sign Out</span></div></div>
  <p class="note">surface.card, border.card, border.divider, size.row, switch.on / onBot / off, text.danger</p>
 </div>
 <div class="spec">
  <h3>Buttons, field, chips</h3>
  <div class="fieldx type-fieldLarge">Name your Bot</div>
  <button class="btn type-button" type="button">Create</button>
  <button class="btn dis type-button" type="button" disabled>Create</button>
  <div class="row-btns"><span class="chip type-subheadline">default <b class="ok">&#10003;</b></span><span class="sbtn type-subheadline">Add</span><span class="sbtn off type-subheadline">Added</span><span class="edit type-callout">Edit</span></div>
  <div class="menu"><div class="type-callout">New Bot</div><div class="type-callout">New Group Chat</div><div class="type-callout danger">Delete</div></div>
  <p class="note">surface.field, button.primary / primaryDisabled / secondary, surface.secondary, surface.tertiary, surface.menu, radius.menu</p>
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
.radius-box{width:120px;height:80px;background:var(--color-surface-card);border:1px solid var(--color-border-card);display:flex;flex-direction:column;align-items:center;justify-content:center;font-size:12px;color:var(--color-text-secondary)}
.space-row{display:grid;grid-template-columns:minmax(150px,240px) 1fr 70px;align-items:center;gap:12px;padding:3px 0}
.space-row .bar{display:block;height:12px;background:var(--color-accent-default);border-radius:2px;max-width:100%}
.space-row .bar.thin{height:8px;background:var(--color-text-tertiary)}
.spec-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,330px),1fr));gap:16px}
.spec{border:1px solid var(--color-border-divider);border-radius:var(--radius-card);padding:4px 16px 16px;min-width:0}
.screen{background:var(--color-bg-page);border:1px solid var(--color-border-divider);border-radius:var(--radius-sheet);padding:12px var(--space-screenMargin) 16px;max-width:390px}
.glass{background:var(--color-surface-glass);color:var(--color-text-primary);display:inline-flex;align-items:center;justify-content:center;gap:8px}
.round{width:var(--size-navButton);height:var(--size-navButton);border-radius:50%;font-size:22px}
.round.big{width:var(--size-composerButton);height:var(--size-composerButton)}
.nav{display:flex;justify-content:space-between;align-items:center;margin-bottom:12px}
.nav .title{height:var(--size-navButton);padding:0 16px 0 10px;border-radius:var(--radius-capsule)}
.av{display:inline-block;width:var(--size-avatarGrid);height:var(--size-avatarGrid);border-radius:50%}.av.sm{width:24px;height:24px}.av.md{width:48px;height:48px;flex:none}
.bub,.own{max-width:var(--size-bubbleMaxWidth);border-radius:var(--radius-bubble);padding:var(--space-md) 14px;margin:var(--space-sm) 0}
.bub{background:var(--color-surface-bubbleDirect);color:var(--color-text-primary)}
.bub.joined{border-top-left-radius:var(--radius-bubbleJoined);border-top-right-radius:var(--radius-bubbleJoined);margin-top:4px}
.own{background:var(--color-surface-ownBubble);color:var(--color-text-onOwnBubble);margin-left:auto}
.code{background:var(--color-surface-code);color:var(--color-text-code);font-family:var(--font-mono);font-size:14px;border-radius:var(--radius-code);padding:10px 12px;margin:8px 0;white-space:pre}
.link{color:var(--color-text-link)}
.sys{color:var(--color-text-tertiary);text-align:center;margin:12px 0}
.composer{display:flex;gap:10px;align-items:center}
.field-c{flex:1;height:var(--size-composer);border-radius:var(--radius-capsule);background:var(--color-surface-glass);color:var(--color-text-placeholder);display:flex;align-items:center;justify-content:space-between;padding:0 6px 0 16px}
.send{width:var(--size-sendButton-width);height:var(--size-sendButton-height);border-radius:var(--radius-capsule);background:var(--color-button-send-bg);color:var(--color-button-send-glyph);display:inline-flex;align-items:center;justify-content:center;font-weight:600}
.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:var(--space-lg) 8px;text-align:center}
.grid .lab{display:block;color:var(--color-text-secondary);margin-top:var(--space-xs)}
.dot{display:inline-block;width:8px;height:8px;border-radius:50%;background:var(--color-accent-default);vertical-align:middle}
.lrow{display:flex;gap:14px;align-items:center;margin-top:var(--space-xl)}.lrow>div{flex:1}
.sec{color:var(--color-text-secondary)}.ter{color:var(--color-text-tertiary)}.danger{color:var(--color-text-danger)}.blk{display:block}
.pill{width:max-content;margin:12px auto;padding:6px 14px;border-radius:var(--radius-capsule);background:var(--color-accent-pill);color:var(--color-text-onAccent)}
.search{height:var(--size-searchBar);border-radius:var(--radius-capsule);background:var(--color-surface-glass);color:var(--color-text-secondary);display:flex;align-items:center;padding:0 16px}
.card{background:var(--color-surface-card);border:var(--border-width-rim) solid var(--color-border-card);border-radius:var(--radius-card);max-width:358px;overflow:hidden}
.srow{display:flex;justify-content:space-between;align-items:center;gap:12px;min-height:var(--size-row);padding:8px 16px;border-bottom:var(--border-width-hairline) solid var(--color-border-divider)}
.srow:last-child{border-bottom:0}
.secthead{color:var(--color-text-tertiary);margin:16px 0 6px 16px}
.sw-ctl{position:relative;flex:none;width:var(--size-switch-width);height:var(--size-switch-height);border-radius:var(--radius-capsule);background:var(--color-switch-off)}
.sw-ctl::after{content:"";position:absolute;top:2px;left:2px;width:var(--size-switch-thumb);height:calc(var(--size-switch-height) - 4px);border-radius:var(--radius-capsule);background:var(--color-switch-thumb)}
.sw-ctl.on{background:var(--color-switch-on)}.sw-ctl.bot{background:var(--color-switch-onBot)}
.sw-ctl.on::after,.sw-ctl.bot::after{left:auto;right:2px}
.fieldx{height:var(--size-field);border-radius:var(--radius-field);background:var(--color-surface-field);border:var(--border-width-rim) solid var(--color-border-card);color:var(--color-text-placeholder);display:flex;align-items:center;justify-content:center;max-width:358px}
.btn{display:block;width:100%;max-width:316px;height:var(--size-button);margin:12px 0 0;border:0;border-radius:var(--radius-capsule);background:var(--color-button-primary-bg);color:var(--color-button-primary-text);font-family:var(--font-base)}
.btn.dis{background:var(--color-button-primaryDisabled-bg);color:var(--color-button-primaryDisabled-text)}
.row-btns{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin-top:14px}
.chip{height:var(--size-chip);padding:0 12px;border-radius:var(--radius-capsule);background:var(--color-surface-secondary);display:inline-flex;align-items:center;gap:6px}.ok{color:var(--color-text-success)}
.sbtn{height:var(--size-secondaryButton);padding:0 16px;border-radius:var(--radius-capsule);background:var(--color-button-secondary-bg);color:var(--color-button-secondary-text);display:inline-flex;align-items:center}
.sbtn.off{color:var(--color-text-disabled)}
.edit{height:var(--size-pill);padding:0 14px;border-radius:var(--radius-capsule);background:var(--color-surface-tertiary);display:inline-flex;align-items:center}
.menu{margin-top:14px;width:var(--size-menuWidth);max-width:100%;border-radius:var(--radius-menu);background:var(--color-surface-menu);padding:8px 0}
.menu div{padding:10px 24px}
footer{margin-top:48px;color:var(--color-text-secondary);font-size:12px}
""".strip()

    script = """(function(){var r=document.documentElement,b=document.querySelectorAll('[data-set-theme]');
function a(t){r.setAttribute('data-theme',t);for(var i=0;i<b.length;i++){b[i].setAttribute('aria-pressed',String(b[i].getAttribute('data-set-theme')===t));}}
for(var i=0;i<b.length;i++){b[i].addEventListener('click',function(e){a(e.currentTarget.getAttribute('data-set-theme'));});}a('dark');})();"""

    parts = ["<!doctype html>", '<html lang="en" data-theme="dark">', "<head>", '<meta charset="utf-8">',
             '<meta name="viewport" content="width=device-width, initial-scale=1">', "<title>Grok Bot style guide</title>", "<style>",
             ":root{%s}" % ";".join(core_css),
             ':root,:root[data-theme="light"]{color-scheme:light;%s}' % ";".join(light_css),
             ':root[data-theme="dark"]{color-scheme:dark;%s}' % ";".join(dark_css),
             "\n".join(type_css), page_css, "</style>", "</head>", "<body>", '<div class="wrap">',
             '<header class="top"><div><h1>Grok Bot style guide</h1>',
             '<p class="lede">Grok Bot 1.16.0 for iOS 26, read from stills captured through iPhone Mirroring on 2026-10-23. Every value '
             "below comes from tokens.json; points are 1:1 with CSS pixels. The font is not known, so the page uses the platform sans. "
             "Glass is drawn as its centre colour: the real material blurs what is behind it.</p></div>",
             '<div class="toggle" role="group" aria-label="Theme"><button type="button" data-set-theme="light" aria-pressed="false">Light</button>'
             '<button type="button" data-set-theme="dark" aria-pressed="true">Dark</button></div></header>',
             "<h2>Colour</h2>",
             '<p class="lede">Light and dark side by side. The badge says how each value was read: Sampled (a pixel read off a capture; '
             "a glass or gradient box gives its share in the description), Sampled (text) (the anti-aliased pixel furthest from the fill), "
             "Derived (worked out from readings), Reconstruction (judged by eye). Hover a swatch for its capture.</p>",
             "".join(colour_html),
             "<h3>Avatar palette (core)</h3><p class=\"lede\">The Create New Bot palette. Bots take one colour each; their switches and the owner's bubbles use it darkened to about 77%.</p>",
             '<div class="palette">%s</div>' % palette,
             "<h3>Neutral ramp (core)</h3><p class=\"lede\">Every grey the two themes use, light to dark. Named by order, not a published ramp.</p>",
             '<div class="ramp">%s</div>' % neutrals,
             "<h2>Radii</h2>", '<div class="radii">%s</div>' % radii,
             "<h2>Spacing</h2>", spacing, "<h2>Sizes</h2>", sizes,
             "<h2>Type scale</h2>",
             '<div class="scroll"><table class="tokens"><thead><tr><th>Token</th><th>Spec</th><th>Specimen</th></tr></thead><tbody>%s</tbody></table></div>' % type_rows,
             "<h2>Components</h2>", '<p class="lede">Built from the tokens only. Switch the theme to see light.</p>', specimens,
             "<footer>Generated by tools/build_style_guide.py from tokens.json. Grok Bot's screenshots and visual system belong to X Corp; this package holds no Grok Bot code or artwork.</footer>",
             "</div>", "<script>", script, "</script>", "</body>", "</html>", ""]
    OUT.write_text("\n".join(parts), encoding="utf-8")
    return OUT


if __name__ == "__main__":
    print("wrote", build().relative_to(PKG))
