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
SERIF_STACK = 'ui-serif, "New York", Georgia, "Times New Roman", serif'
MONO_STACK = 'ui-monospace, "SF Mono", Menlo, monospace'
NAME = "Claude for iOS"   # PRODUCT (adapt)
OWNER = "Anthropic"    # PRODUCT (adapt): whose visual system it is
LEDE = ("Claude for iOS on iOS 26, read from stills captured through iPhone Mirroring on 2026-10-23 (dark) and 2026-10-24 (light).")  # PRODUCT (adapt)
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
            type_css.append(".type-%s{font-family:%s;font-weight:%s;font-size:%s;line-height:%s}"
                            % (p[-1], css(v["fontFamily"]), css(v["fontWeight"]), v["fontSize"], v.get("lineHeight", "1.25")))
        elif t["$type"] == "fontFamily":
            core_css.append("%s:%s" % (var(p), SERIF_STACK if p[-1] == "serif" else FONT_STACK))
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
                      % (esc(css(t["$value"])), esc(".".join(p)), esc(t["$value"])) for p, t in under(("color", "clay")) + under(("color", "blue")))
    neutrals = "".join('<div class="ramp-step" style="background:%s" title="%s"><code>%s</code></div>'
                       % (esc(t["$value"]), esc(t["$description"]), esc(p[-1] + " " + t["$value"])) for p, t in under(("color", "neutral")))
    radii = "".join('<div class="radius-box" style="border-radius:%s"><code>%s</code><span>%s</span></div>'
                    % (esc(css(t["$value"])), esc(".".join(p)), esc(t["$value"])) for p, t in under(("radius",)))
    spacing = "".join('<div class="space-row"><code>%s</code><span class="bar" style="width:%s"></span><span>%s</span></div>'
                      % (esc(".".join(p)), esc(css(t["$value"])), esc(t["$value"])) for p, t in under(("space",)))
    sizes = "".join('<div class="space-row"><code>%s</code><span class="bar thin" style="width:%s"></span><span>%s</span></div>'
                    % (esc(".".join(p)), esc(css(t["$value"])), esc(t["$value"])) for p, t in under(("size",)))
    sample = {  # PRODUCT (adapt): specimen text per type style
        "display": "Give the gift of Claude", "titleSerif": "Claude", "response": "Done. Both now use the gallery gradients.",
        "headline": "Select model", "bodyLarge": "Projects", "body": "Notifications", "pageHeading": "Time and focus",
        "callout": "Checking whether the cover image URL", "subheadline": "Allow Claude to search the web",
        "footnote": "For complex work and everyday tasks", "caption": "Recommended"}
    type_rows = "".join('<tr><th scope="row"><code>%s</code><span class="desc">%s</span></th><td class="meta">%s, %s%s</td>'
                        '<td><span class="type-%s">%s</span></td></tr>'
                        % (esc(".".join(p)), esc(t["$description"]), esc(t["$value"]["fontSize"]), esc(t["$value"]["fontWeight"]),
                           (", line " + t["$value"]["lineHeight"]) if "lineHeight" in t["$value"] else "", p[-1], esc(sample.get(p[-1], "Sample")))
                        for p, t in under(("typography",)))

    # PRODUCT (adapt): specimens built from tokens only
    specimens = """
<div class="spec-grid">
 <div class="spec phone">
  <h3>Thread</h3>
  <div class="screen">
   <div class="nav"><span class="glass round">&#8801;</span><span class="glass cap">&#8853; &nbsp; &#8943;</span></div>
   <div class="ub type-body">Update the cover image of Home Server based on the context.</div>
   <div class="step type-callout">&#9719; Checking whether the cover image URL&#8230; <span>&#8250;</span></div>
   <p class="resp type-response">Done. Both now use the gallery gradients: the dark blue one for Home Server, the warm one for Self Learn.</p>
   <div class="acts">&#10697; &#8682; &#9655; &#8679; &#8681; &#8635;</div>
   <p class="foot type-subheadline">Claude is AI and can make mistakes.</p>
   <div class="composer"><div class="ph type-body">Reply to Claude or hold to talk</div>
    <div class="ctl"><span class="ctrl round-c">+</span><span class="ctrl pillc type-callout">Opus 5.5 <i>High</i></span><span class="sp"></span><span class="ctrl round-c">&#9675;</span><span class="talk type-subheadline">Talk</span></div></div>
  </div>
  <p class="note">surface.userBubble, typography.response, text.tertiary, surface.glass, surface.control, button.primary</p>
 </div>
 <div class="spec phone">
  <h3>New chat, typed</h3>
  <div class="screen center">
   <div class="spark">&#10059;</div>
   <p class="greet type-titleSerif">It&#8217;s a late-night jam session.</p>
   <div class="composer"><div class="typed type-body">hello<span class="caret"></span></div>
    <div class="ctl"><span class="ctrl round-c">+</span><span class="ctrl pillc type-callout">Opus 5.5 <i>High</i></span><span class="sp"></span><span class="ctrl round-c">&#9675;</span><span class="send">&#8593;</span></div></div>
  </div>
  <p class="note">accent.brand, text.greeting, typography.titleSerif, focus.caret, button.send</p>
 </div>
 <div class="spec">
  <h3>Settings sheet</h3>
  <div class="card"><div class="srow"><span class="type-body">Personal<span class="type-callout sec blk">owner@example.com &#183; Max</span></span></div>
   <div class="srow"><span class="type-body link">+ &nbsp;Add account</span></div></div>
  <p class="secthead type-callout">Account</p>
  <div class="card">
   <div class="srow"><span class="type-body">Billing</span><span class="type-body ter">Max plan <b class="chev">&#8250;</b></span></div>
   <div class="srow"><span class="type-body">Usage</span><b class="chev">&#8250;</b></div>
   <div class="srow"><span class="type-body">Haptic feedback</span><span class="sw-ctl on"></span></div>
   <div class="srow"><span class="type-body">Usage credits<span class="type-subheadline ter blk">Turn on usage credits to keep using Claude.</span></span><span class="sw-ctl"></span></div>
   <div class="srow"><span class="type-body dis">Artifacts<span class="type-subheadline dis2 blk">Required by code execution</span></span><span class="sw-ctl lock"></span></div>
  </div>
  <p class="note">surface.card, border.divider, size.row, text.link, text.chevron, switch.on / off / onDisabled</p>
 </div>
 <div class="spec">
  <h3>Bottom sheet</h3>
  <div class="sheet"><div class="grab"></div>
   <div class="shead"><span class="glass round">&#215;</span><span class="type-headline">Effort</span><span class="round ghost"></span></div>
   <div class="card sc">
    <div class="srow tall"><span class="type-body">Medium <span class="badge type-caption">Recommended</span></span></div>
    <div class="srow tall"><span class="type-body">High</span><b class="tick">&#10003;</b></div>
    <div class="srow tall"><span class="type-body">Max <span class="badge warn type-caption">5.5&#215; or more usage</span></span></div>
   </div>
   <p class="help type-footnote">Higher effort means more thorough responses, but takes longer and uses your limits faster.</p>
  </div>
  <p class="note">bg.sheet, radius.sheet, border.grabber, radius.cardSheet, badge.bg / text / warningBg / warningText, accent.check</p>
 </div>
 <div class="spec">
  <h3>Sidebar</h3>
  <div class="side">
   <p class="type-titleSerif wm">Claude</p>
   <div class="sbi type-bodyLarge">Chats</div><div class="sbi type-bodyLarge">Projects</div>
   <div class="sbi sel type-bodyLarge">Code</div><div class="sbi type-bodyLarge">Artifacts</div>
   <p class="sbs type-callout">Pinned</p><div class="sbi type-bodyLarge">calendar-helper</div>
   <span class="pill type-callout">+ &nbsp;New chat</span>
  </div>
  <p class="note">bg.sidebar, typography.titleSerif, size.rowSidebar, surface.selected, radius.row, button.primary, size.pill</p>
 </div>
 <div class="spec">
  <h3>Menu, meter, select, empty state</h3>
  <div class="menu"><div class="type-body">Share</div><div class="type-body">Rename</div><hr class="mdiv"><div class="type-body danger">Delete</div></div>
  <div class="card meter"><div class="mrow"><span class="type-body">All models</span><span class="type-body ter">17% used</span></div>
   <div class="track"><i style="width:17%"></i></div><span class="type-callout ter">Resets Fri 04:00</span></div>
  <div class="row-btns"><span class="sel-f type-body">&#8211; <b>&#8964;</b></span><span class="day type-callout">S</span><span class="day type-callout">M</span><span class="pill2 type-callout">+ &nbsp;Add device</span></div>
  <div class="empty"><span class="eicon">&#9707;</span><p class="type-body ter">No archived projects</p></div>
  <p class="note">surface.menu, radius.menu, text.danger, progress.fill / track, surface.field, border.field, surface.dayToggle, surface.emptyIcon</p>
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
.toggle{display:inline-flex;border-radius:var(--radius-capsule);padding:3px;gap:2px;background:var(--color-surface-control)}
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
.spec-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,430px),1fr));gap:16px}
.spec{border:1px solid var(--color-border-divider);border-radius:var(--radius-cardSheet);padding:4px 16px 16px;min-width:0}
.screen{background:var(--color-bg-page);border:1px solid var(--color-border-divider);border-radius:var(--radius-sheet);padding:12px var(--space-screenMargin) 16px;max-width:390px}
.screen.center{text-align:center;display:flex;flex-direction:column;justify-content:flex-end;min-height:420px}
.glass{background:var(--color-surface-navGlass);color:var(--color-text-primary);display:inline-flex;align-items:center;justify-content:center}
.round{width:var(--size-navButton);height:var(--size-navButton);border-radius:50%;font-size:20px;flex:none}.round.ghost{visibility:hidden}
.cap{height:var(--size-navButton);padding:0 18px;border-radius:var(--radius-capsule);gap:24px}
.nav{display:flex;justify-content:space-between;align-items:center;margin-bottom:12px}
.ub{max-width:var(--size-bubbleMaxWidth);margin:0 0 0 auto;background:var(--color-surface-userBubble);color:var(--color-text-primary);border-radius:var(--radius-bubble);padding:var(--space-md) var(--space-lg)}
.step{color:var(--color-text-tertiary);display:flex;justify-content:space-between;margin:var(--space-lg) 0 var(--space-sm)}
.resp{color:var(--color-text-response);margin:0}
.acts{color:var(--color-text-tertiary);letter-spacing:12px;margin:var(--space-md) 0 var(--space-sm);font-size:16px}
.foot{color:var(--color-text-footnote);margin:0 0 var(--space-lg)}
.composer{background:var(--color-surface-glass);border-radius:var(--radius-composer);min-height:var(--size-composer-height);padding:12px 8px 8px;text-align:left}
.ph{color:var(--color-text-placeholder);padding:0 8px 10px}.typed{color:var(--color-text-primary);padding:0 8px 10px}
.caret{display:inline-block;width:2px;height:1.1em;vertical-align:-3px;background:var(--color-focus-caret);margin-left:1px}
.ctl{display:flex;align-items:center;gap:var(--space-sm)}.ctl>*{flex:none}.ctl .sp{flex:1 1 0}
.screen{overflow-x:auto}.composer{min-width:340px}.ctl .sp{flex:1}
.ctrl{background:var(--color-button-control-bg);color:var(--color-text-primary);height:var(--size-control);display:inline-flex;align-items:center;justify-content:center}
.round-c{width:var(--size-control);border-radius:50%}
.pillc{padding:0 14px;border-radius:var(--radius-capsule);gap:6px}.pillc i{font-style:normal;color:var(--color-text-tertiary)}
.talk{width:var(--size-talk-width);height:var(--size-talk-height);border-radius:var(--radius-capsule);background:var(--color-button-primary-bg);color:var(--color-button-primary-text);display:inline-flex;align-items:center;justify-content:center;font-weight:600}
.send{width:var(--size-send);height:var(--size-send);border-radius:50%;background:var(--color-button-send-bg);color:var(--color-button-send-glyph);display:inline-flex;align-items:center;justify-content:center;font-weight:700}
.spark{color:var(--color-accent-brand);font-size:44px;line-height:1}
.greet{color:var(--color-text-greeting);margin:8px 0 120px}
.card{background:var(--color-surface-card);border-radius:var(--radius-card);max-width:358px;overflow:hidden}
.srow{display:flex;justify-content:space-between;align-items:center;gap:12px;min-height:var(--size-row);padding:8px var(--space-cardPadding);border-bottom:var(--border-width-hairline) solid var(--color-border-divider)}
.srow:last-child{border-bottom:0}.srow.tall{min-height:50px}
.secthead{color:var(--color-text-tertiary);margin:var(--space-lg) 0 6px var(--space-cardPadding)}
.sec{color:var(--color-text-secondary)}.ter{color:var(--color-text-tertiary)}.danger{color:var(--color-text-danger)}.blk{display:block}
.link{color:var(--color-text-link)}.chev{color:var(--color-text-chevron);font-weight:400;margin-left:6px}
.dis{color:var(--color-text-disabled)}.dis2{color:var(--color-text-disabledSubtitle)}
.sw-ctl{position:relative;flex:none;width:var(--size-switch-width);height:var(--size-switch-height);border-radius:var(--radius-capsule);background:var(--color-switch-off)}
.sw-ctl::after{content:"";position:absolute;top:2px;left:2px;width:var(--size-switch-thumb);height:calc(var(--size-switch-height) - 4px);border-radius:var(--radius-capsule);background:var(--color-switch-thumb)}
.sw-ctl.on{background:var(--color-switch-on)}.sw-ctl.lock{background:var(--color-switch-onDisabled)}.sw-ctl.lock::after{background:var(--color-switch-thumbDisabled)}
.sw-ctl.on::after,.sw-ctl.lock::after{left:auto;right:2px}
.sheet{background:var(--color-bg-sheet);border-radius:var(--radius-sheet) var(--radius-sheet) 0 0;padding:8px 14px 16px;max-width:358px}
.grab{width:var(--size-grabber-width);height:var(--size-grabber-height);border-radius:var(--radius-capsule);background:var(--color-border-grabber);margin:0 auto 8px}
.shead{display:flex;justify-content:space-between;align-items:center;margin-bottom:16px}
.sc{border-radius:var(--radius-cardSheet)}
.tick{color:var(--color-accent-check);font-size:20px}
.badge{display:inline-flex;align-items:center;height:var(--size-badge);padding:0 8px;border-radius:var(--radius-capsule);background:var(--color-badge-bg);color:var(--color-badge-text);margin-left:6px;vertical-align:2px}
.badge.warn{background:var(--color-badge-warningBg);color:var(--color-badge-warningText)}
.help{color:var(--color-text-tertiary);margin:10px var(--space-cardPadding) 0}
.side{background:var(--color-bg-sidebar);border-radius:var(--radius-cardSheet);padding:12px 8px;max-width:330px;position:relative;padding-bottom:64px}
.wm{margin:4px 8px 12px;color:var(--color-text-primary)}
.sbi{height:var(--size-rowSidebar);display:flex;align-items:center;padding:0 12px;border-radius:var(--radius-row)}
.sbi.sel{background:var(--color-surface-selected);height:var(--size-selectedRow)}
.sbs{color:var(--color-text-secondary);margin:14px 12px 0}
.pill{position:absolute;right:16px;bottom:12px;height:var(--size-pill);padding:0 20px;border-radius:var(--radius-capsule);background:var(--color-button-primary-bg);color:var(--color-button-primary-text);display:inline-flex;align-items:center;font-weight:500}
.menu{width:250px;max-width:100%;border-radius:var(--radius-menu);background:var(--color-surface-menu);padding:6px 0;margin-top:12px}
.menu div{padding:12px 24px}
.mdiv{border:0;border-top:var(--border-width-hairline) solid var(--color-border-divider);margin:4px 24px}
.meter{padding:14px var(--space-cardPadding);margin-top:14px}.mrow{display:flex;justify-content:space-between}
.track{height:var(--size-progress);border-radius:var(--radius-capsule);background:var(--color-progress-track);margin:10px 0 8px;overflow:hidden}
.track i{display:block;height:100%;background:var(--color-progress-fill);border-radius:var(--radius-capsule)}
.row-btns{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin-top:14px}
.sel-f{height:var(--size-select);width:120px;border-radius:var(--radius-field);background:var(--color-surface-field);border:var(--border-width-hairline) solid var(--color-border-field);display:inline-flex;align-items:center;justify-content:space-between;padding:0 12px;color:var(--color-text-primary)}
.sel-f b{color:var(--color-text-tertiary);font-weight:400}
.day{width:var(--size-dayToggle);height:var(--size-dayToggle);border-radius:50%;background:var(--color-surface-dayToggle);color:var(--color-text-tertiary);display:inline-flex;align-items:center;justify-content:center}
.pill2{height:var(--size-pillSecondary);padding:0 16px;border-radius:var(--radius-capsule);background:var(--color-surface-glass);color:var(--color-text-primary);display:inline-flex;align-items:center}
.empty{text-align:center;margin-top:18px}.empty p{margin:8px 0 0}
.eicon{display:inline-flex;width:var(--size-emptyIcon);height:var(--size-emptyIcon);border-radius:50%;background:var(--color-surface-emptyIcon);color:var(--color-text-tertiary);align-items:center;justify-content:center;font-size:20px}
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
             + "The fonts are not known, so the page uses the platform sans and serif. "
             "Glass is drawn as its centre colour: the real material blurs what is behind it.</p></div>",
             '<div class="toggle" role="group" aria-label="Theme"><button type="button" data-set-theme="light" aria-pressed="false">Light</button>'
             '<button type="button" data-set-theme="dark" aria-pressed="true">Dark</button></div></header>',
             "<h2>Colour</h2>",
             '<p class="lede">Light and dark side by side. The badge says how each value was read: Sampled (a flat fill, exact), Sampled (text) '
             "(the anti-aliased pixel furthest from the fill), Derived (worked out, or a glass or gradient reading). Hover a swatch for its capture.</p>",
             "".join(colour_html),
             # PRODUCT (adapt): the palette and ramp captions
             "<h3>Clay and blue (core)</h3><p class=\"lede\">Claude's orange (the spark, the send button, an active filter) and every blue the app uses for interactive state, light to dark. Named by order, not a published ramp.</p>",
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
