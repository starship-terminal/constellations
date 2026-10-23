#!/usr/bin/env python3
"""Render style-guide.html from tokens.json (native kit, from systems/grokbot).

    python3 tools/build_style_guide.py

Every token becomes a CSS custom property (its path joined with dashes; an alias becomes a var()
reference), so the swatches, scales and specimens cannot drift from the file. NAME, LEDE, OWNER,
`sample` and `specimens` are Spotify's (PRODUCT (adapt)); the specimens are drawn from tokens only,
never the product's artwork. Spotify for iOS has one theme, dark, so the page has no theme toggle.
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
NAME = "Spotify"   # PRODUCT (adapt)
OWNER = "Spotify AB"  # PRODUCT (adapt): whose visual system it is
LEDE = ("Spotify for iOS 26, dark (its only theme), read from stills captured through iPhone Mirroring on 2026-10-23.")  # PRODUCT (adapt)
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
    """Follow an alias through the given token sets (the theme first, then core) to a value."""
    while isinstance(v, str) and v.startswith("{") and v.endswith("}"):
        path = tuple(v[1:-1].split("."))
        v = next(s[path]["$value"] for s in sets if path in s)
    return v


def swatch_cell(tok, *sets):
    ev = tok["$extensions"]["source"]["evidence"]
    v = tok["$value"]
    shown = resolve(v, *sets)
    label = v if v == shown else f"{v} = {shown}"
    return ('<td><span class="sw" title="%s"><i style="background:%s"></i></span><code>%s</code> '
            '<span class="ev %s">%s</span></td>' % (esc(tok["$extensions"]["source"]["capture"]), esc(shown),
                                                    esc(label), EV_CLASS[ev], esc(ev)))


def build():
    data = json.loads(TOKENS.read_text())
    core, dark = (list(walk(data[s])) for s in ("core", "dark"))
    core_by, dark_by = dict(core), dict(dark)

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
    dark_css = ["%s:%s" % (var(p), css(t["$value"])) for p, t in dark]

    # ---- semantic colours, one theme
    groups = {}
    for p, t in dark:
        groups.setdefault(p[1], []).append((p, t))
    colour_html = []
    for g, items in groups.items():
        rows = "".join('<tr><th scope="row"><code>%s</code><span class="desc">%s</span></th>%s</tr>'
                       % (esc(".".join(p)), esc(t["$description"]), swatch_cell(t, dark_by, core_by))
                       for p, t in items)
        colour_html.append('<h3>%s</h3><div class="scroll"><table class="tokens"><thead><tr><th>Token</th><th>Dark</th>'
                           '</tr></thead><tbody>%s</tbody></table></div>' % (esc(g), rows))

    under = lambda pre: [(p, t) for p, t in core if p[:len(pre)] == pre]
    dots = lambda pre: "".join('<div class="chip-sw"><span class="dot" style="background:%s"></span><code>%s</code><span>%s</span></div>'
                               % (esc(css(t["$value"])), esc(".".join(p)), esc(t["$value"])) for p, t in under(pre))
    neutrals = "".join('<div class="ramp-step" style="background:%s" title="%s"><code>%s</code></div>'
                       % (esc(t["$value"]), esc(t["$description"]), esc(p[-1] + " " + t["$value"])) for p, t in under(("color", "neutral")))
    radii = "".join('<div class="radius-box" style="border-radius:%s"><code>%s</code><span>%s</span></div>'
                    % (esc(css(t["$value"])), esc(".".join(p)), esc(t["$value"])) for p, t in under(("radius",)))
    spacing = "".join('<div class="space-row"><code>%s</code><span class="bar" style="width:%s"></span><span>%s</span></div>'
                      % (esc(".".join(p)), esc(css(t["$value"])), esc(t["$value"])) for p, t in under(("space",)))
    sizes = "".join('<div class="space-row"><code>%s</code><span class="bar thin" style="width:%s"></span><span>%s</span></div>'
                    % (esc(".".join(p)), esc(css(t["$value"])), esc(t["$value"])) for p, t in under(("size",)))
    sample = {  # PRODUCT (adapt): specimen text per type style
        "display": "Artist Name", "pageTitle": "Your Library", "sectionTitle": "Recently played", "navTitle": "Playback",
        "body": "What do you want to listen to?", "bodyBold": "Music", "sheetItem": "Add to queue", "subtitle": "Playlist • 12 songs",
        "label": "Liked Songs", "sheetHeader": "Sort by", "caption": "Offline mode", "tabLabel": "Home"}
    type_rows = "".join('<tr><th scope="row"><code>%s</code><span class="desc">%s</span></th><td class="meta">%s, %s%s</td>'
                        '<td><span class="type-%s">%s</span></td></tr>'
                        % (esc(".".join(p)), esc(t["$description"]), esc(t["$value"]["fontSize"]), esc(t["$value"]["fontWeight"]),
                           (", line " + t["$value"]["lineHeight"]) if "lineHeight" in t["$value"] else "", p[-1], esc(sample.get(p[-1], "Sample")))
                        for p, t in under(("typography",)))

    # PRODUCT (adapt): specimens built from tokens only; grey squares stand in for artwork
    specimens = """
<div class="spec-grid">
 <div class="spec phone">
  <h3>Home</h3>
  <div class="screen">
   <div class="chips"><span class="av"></span><span class="chip sel type-subtitle">All</span><span class="chip type-subtitle">Music</span><span class="chip type-subtitle">Podcasts</span></div>
   <div class="tiles">
    <div class="tile"><i class="art"></i><span class="type-label">Liked Songs</span></div>
    <div class="tile"><i class="art"></i><span class="type-label">Daily Mix 1</span></div>
    <div class="tile"><i class="art"></i><span class="type-label">Release Radar</span></div>
    <div class="tile"><i class="art"></i><span class="type-label">On Repeat</span></div>
   </div>
   <p class="type-sectionTitle sect">Recently played</p>
   <div class="promo"><i class="art big"></i><div><span class="type-subtitle sec blk">EP</span><span class="type-label blk">New release</span><span class="type-subtitle sec blk">Artist</span><span class="pillw type-label">Pre-save</span></div></div>
   <div class="mini"><i class="art sm"></i><div><span class="type-subtitle blk">Track title</span><span class="type-subtitle on-mini blk">Artist</span></div><span class="saved"></span></div>
   <div class="tabs"><span class="type-tabLabel on">Home</span><span class="type-tabLabel">Search</span><span class="type-tabLabel">Your Library</span><span class="type-tabLabel">Create</span></div>
  </div>
  <p class="note">chip.selectedBg, surface.tile, size.shortcutTile, radius.sm, surface.card, button.inverse, surface.miniPlayer (artwork-tinted), text.tabActive / tabInactive</p>
 </div>
 <div class="spec phone">
  <h3>Search and Your Library</h3>
  <div class="screen">
   <div class="field type-body"><b class="mag">&#9906;</b>What do you want to listen to?</div>
   <div class="ffield"><span class="glassf type-body"><i class="caret"></i>What do you want to listen to?</span><span class="cancel type-subtitle">Cancel</span></div>
   <p class="type-pageTitle hdr"><span class="av"></span>Your Library</p>
   <div class="row lib"><i class="art lg"></i><div><span class="type-body blk">Liked Songs</span><span class="type-subtitle sec blk"><b class="pin">&#9679;</b> Playlist • 120 songs</span></div></div>
   <div class="row"><i class="art"></i><div><span class="type-body blk">Song title</span><span class="type-subtitle sec blk">Song • Artist</span></div><span class="add">&#8853;</span></div>
   <div class="row"><i class="art round"></i><div><span class="type-body blk">Artist</span><span class="type-subtitle sec blk">Artist</span></div><span class="saved"></span></div>
  </div>
  <p class="note">surface.field, text.placeholder, surface.fieldFocused, focus.caret, size.libraryArtwork, size.rowArtwork, status.success</p>
 </div>
 <div class="spec">
  <h3>Settings</h3>
  <div class="qtiles"><div class="qt"><span class="type-caption acc">Data Saver<br>Always on</span></div><div class="qt"><span class="type-caption">Offline mode<br><span class="sec">Off</span></span></div><div class="qt"><span class="type-caption">Private session<br><span class="sec">Off</span></span></div></div>
  <div class="srow"><div><span class="type-body blk">Gapless playback</span><span class="type-subtitle sec blk">Removes any gaps or pauses between tracks.</span></div><span class="sw-ctl on"></span></div>
  <div class="srow"><div><span class="type-body blk">Mono audio</span><span class="type-subtitle sec blk">Left and right play the same audio.</span></div><span class="sw-ctl"></span></div>
  <div class="slider"><span class="type-subtitle sec">0 sec</span><span class="track"><i class="fill"></i><i class="thumb"></i></span><span class="type-subtitle sec">12 sec</span></div>
  <hr class="div">
  <p class="note">surface.panel, radius.md, text.accent, switch.on (system green) / off / thumb / thumbOff, slider.fill / track / thumb, border.divider</p>
 </div>
 <div class="spec">
  <h3>Artist page and sheet</h3>
  <p class="type-display disp">Artist</p>
  <div class="acts"><span class="pillo type-label">Following</span><span class="sec">&#8943;</span><span class="play">&#9654;</span></div>
  <div class="ptabs"><span class="type-bodyBold on">Music</span><span class="type-bodyBold">Video</span><span class="type-bodyBold">Events</span></div>
  <div class="seg"><span class="segs type-body">Song</span><span class="type-body">Lyrics</span></div>
  <div class="sheet"><i class="grab"></i><p class="type-sheetHeader sh">Sort by</p><p class="type-sheetItem selo">Recents <span>&#10003;</span></p><p class="type-sheetItem">Recently added</p><p class="type-sheetItem">Alphabetical <span class="beta type-caption">Beta</span></p></div>
  <p class="note">typography.display, button.outline, button.primary, tab.indicator, segmented.*, surface.sheetSort, radius.sheet, text.accentOnSheet, badge.beta</p>
 </div>
</div>
"""

    page_css = """
*{box-sizing:border-box}
html,body{background:var(--color-bg-page)}
body{margin:0;color:var(--color-text-primary);font-family:var(--font-base);font-size:15px;line-height:1.45}
.wrap{max-width:1080px;margin:0 auto;padding:24px 16px 64px}
h1{font-size:26px;margin:0}h2{font-size:20px;margin:40px 0 8px}h3{font-size:15px;margin:20px 0 8px}
p.lede{color:var(--color-text-secondary);margin:4px 0 0;max-width:70ch}p.note{color:var(--color-text-secondary);font-size:12px;margin:10px 0 0}
code{font-family:var(--font-mono);font-size:12px}
.scroll{overflow-x:auto}
table.tokens{border-collapse:collapse;width:100%;min-width:560px}
table.tokens th,table.tokens td{text-align:left;vertical-align:top;padding:8px 10px;border-bottom:var(--border-width-hairline) solid var(--color-border-divider)}
table.tokens thead th{color:var(--color-text-secondary);font-size:12px;font-weight:400}
table.tokens th[scope=row]{font-weight:500;width:55%}
.desc{display:block;color:var(--color-text-secondary);font-size:12px;font-weight:400;margin-top:2px}
.meta{color:var(--color-text-secondary);white-space:nowrap}
.sw{display:inline-block;width:28px;height:28px;border-radius:8px;vertical-align:middle;margin-right:8px;border:1px solid var(--color-border-card);background-image:linear-gradient(45deg,#8883 25%,transparent 25%,transparent 75%,#8883 75%),linear-gradient(45deg,#8883 25%,transparent 25%,transparent 75%,#8883 75%);background-size:8px 8px;background-position:0 0,4px 4px;overflow:hidden}
.sw i{display:block;width:100%;height:100%}
.ev{display:inline-block;font-size:11px;padding:1px 7px;border-radius:var(--radius-capsule);border:1px solid var(--color-border-card);color:var(--color-text-secondary);white-space:nowrap}
.ev-derived{border-style:dashed}.ev-none{border-style:dotted}
.palette{display:flex;flex-wrap:wrap;gap:12px}
.chip-sw{display:flex;flex-direction:column;align-items:center;gap:4px;width:96px;font-size:12px;color:var(--color-text-secondary);text-align:center}
.chip-sw .dot{width:44px;height:44px;border-radius:var(--radius-sm)}
.ramp{display:flex;flex-wrap:wrap;border-radius:var(--radius-md);overflow:hidden;border:1px solid var(--color-border-card)}
.ramp-step{flex:1 0 76px;height:64px;display:flex;align-items:flex-end;padding:4px}
.ramp-step code{font-size:10px;background:#0008;color:#fff;padding:0 3px;border-radius:3px}
.radii{display:flex;flex-wrap:wrap;gap:16px}
.radius-box{width:120px;height:80px;background:var(--color-surface-tile);display:flex;flex-direction:column;align-items:center;justify-content:center;font-size:12px;color:var(--color-text-secondary)}
.space-row{display:grid;grid-template-columns:minmax(150px,240px) 1fr 70px;align-items:center;gap:12px;padding:3px 0}
.space-row .bar{display:block;height:12px;background:var(--color-accent-default);border-radius:2px;max-width:100%}
.space-row .bar.thin{height:8px;background:var(--color-text-tertiary)}
.spec-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,330px),1fr));gap:16px}
.spec{border:1px solid var(--color-border-card);border-radius:var(--radius-md);padding:4px 16px 16px;min-width:0}
.screen{background:var(--color-bg-page);border:1px solid var(--color-border-card);border-radius:var(--radius-sheet);padding:12px var(--space-screenMargin) 12px;max-width:390px}
.sec{color:var(--color-text-secondary)}.blk{display:block}.acc{color:var(--color-text-accent)}
.av{display:inline-block;width:var(--size-avatar-header);height:var(--size-avatar-header);border-radius:50%;background:var(--color-surface-card);flex:none;vertical-align:middle}
.chips{display:flex;gap:var(--space-sm);align-items:center;margin-bottom:var(--space-md);flex-wrap:wrap}
.chip{height:var(--size-chip);padding:0 14px;border-radius:var(--radius-capsule);background:var(--color-chip-bg);color:var(--color-chip-text);display:inline-flex;align-items:center}
.chip.sel{background:var(--color-chip-selectedBg);color:var(--color-chip-selectedText)}
.tiles{display:grid;grid-template-columns:1fr 1fr;gap:var(--space-sm)}
.tile{height:var(--size-shortcutTile);background:var(--color-surface-tile);border-radius:var(--radius-sm);display:flex;align-items:center;gap:var(--space-sm);overflow:hidden}
.art{display:inline-block;flex:none;width:var(--size-rowArtwork);height:var(--size-rowArtwork);background:var(--color-surface-shareTarget);border-radius:var(--radius-sm)}
.tile .art{width:var(--size-shortcutTile);height:var(--size-shortcutTile);border-radius:0}
.art.sm{width:var(--size-miniArtwork);height:var(--size-miniArtwork)}.art.lg{width:var(--size-libraryArtwork);height:var(--size-libraryArtwork)}
.art.big{width:120px;height:120px;border-radius:0}.art.round{border-radius:50%}
.sect{margin:var(--space-xl) 0 var(--space-md)}
.promo{display:flex;gap:var(--space-lg);background:var(--color-surface-card);border-radius:var(--radius-md);overflow:hidden;padding-right:var(--space-lg)}
.promo>div{padding:var(--space-md) 0;flex:1}
.pillw{display:inline-flex;align-items:center;height:var(--size-pill);padding:0 16px;margin-top:var(--space-md);border-radius:var(--radius-capsule);background:var(--color-button-inverse-bg);color:var(--color-button-inverse-text)}
.mini{display:flex;align-items:center;gap:var(--space-sm);height:var(--size-miniPlayer);margin:var(--space-lg) calc(var(--space-sm) - var(--space-screenMargin)) 0;padding:0 var(--space-sm);border-radius:var(--radius-md);background:var(--color-surface-miniPlayer)}
.mini>div{flex:1}.on-mini{color:var(--color-text-onMiniPlayer)}
.saved{flex:none;width:var(--size-savedIcon);height:var(--size-savedIcon);border-radius:50%;background:var(--color-status-success)}
.tabs{display:flex;justify-content:space-around;padding-top:var(--space-md);color:var(--color-text-tabInactive)}.tabs .on{color:var(--color-text-tabActive)}
.field{display:flex;align-items:center;gap:var(--space-md);height:var(--size-searchField);padding:0 var(--space-md);border-radius:var(--radius-field);background:var(--color-surface-field);color:var(--color-text-placeholder)}
.mag{font-weight:400}
.ffield{display:flex;gap:var(--space-sm);margin-top:var(--space-md)}
.glassf{flex:1;display:flex;align-items:center;height:var(--size-searchFieldFocused);padding:0 var(--space-md);border-radius:var(--radius-capsule);background:var(--color-surface-fieldFocused);color:var(--color-text-placeholderFocused);white-space:nowrap;overflow:hidden}
.caret{display:inline-block;width:2px;height:20px;margin-right:2px;background:var(--color-focus-caret)}
.cancel{display:inline-flex;align-items:center;padding:0 12px;border-radius:var(--radius-capsule);background:var(--color-surface-fieldFocused)}
.hdr{display:flex;align-items:center;gap:var(--space-md);margin:var(--space-lg) 0 var(--space-sm)}
.row{display:flex;align-items:center;gap:var(--space-md);min-height:var(--size-row)}.row>div{flex:1}.row.lib{min-height:var(--size-libraryRow)}
.pin{color:var(--color-accent-default);font-size:10px}.add{color:var(--color-text-secondary);font-size:22px}
.qtiles{display:grid;grid-template-columns:repeat(3,1fr);gap:var(--space-sm)}
.qt{height:var(--size-settingsTile);border-radius:var(--radius-md);background:var(--color-surface-panel);display:flex;align-items:flex-end;justify-content:center;text-align:center;padding-bottom:8px}
.srow{display:flex;justify-content:space-between;align-items:center;gap:12px;padding:12px 0}
.sw-ctl{position:relative;flex:none;width:var(--size-switch-width);height:var(--size-switch-height);border-radius:var(--radius-capsule);background:var(--color-switch-off)}
.sw-ctl::after{content:"";position:absolute;top:2px;left:2px;width:var(--size-switch-thumb);height:calc(var(--size-switch-height) - 4px);border-radius:var(--radius-capsule);background:var(--color-switch-thumbOff)}
.sw-ctl.on{background:var(--color-switch-on)}.sw-ctl.on::after{left:auto;right:2px;background:var(--color-switch-thumb)}
.slider{display:flex;align-items:center;gap:var(--space-md)}
.track{position:relative;flex:1;height:var(--size-slider-track);background:var(--color-slider-track)}
.track .fill{position:absolute;left:0;top:0;bottom:0;width:18%;background:var(--color-slider-fill)}
.track .thumb{position:absolute;left:18%;top:50%;width:var(--size-slider-thumb);height:var(--size-slider-thumb);margin:calc(var(--size-slider-thumb) / -2);border-radius:50%;background:var(--color-slider-thumb)}
.div{border:0;border-top:var(--border-width-hairline) solid var(--color-border-divider);margin:var(--space-lg) 0 0}
.disp{margin:8px 0;line-height:1;letter-spacing:-0.03em}
.acts{display:flex;align-items:center;gap:var(--space-lg)}
.pillo{display:inline-flex;align-items:center;height:var(--size-pill);padding:0 16px;border-radius:var(--radius-capsule);border:var(--border-width-outline) solid var(--color-button-outline-border);color:var(--color-button-outline-text)}
.play{margin-left:auto;display:inline-flex;align-items:center;justify-content:center;width:var(--size-playButton);height:var(--size-playButton);border-radius:50%;background:var(--color-button-primary-bg);color:var(--color-button-primary-glyph)}
.ptabs{display:flex;gap:var(--space-xl);margin:var(--space-lg) 0;color:var(--color-tab-unselected)}
.ptabs .on{color:var(--color-tab-selected);border-bottom:var(--size-tabIndicator) solid var(--color-tab-indicator);padding-bottom:4px}
.seg{display:inline-flex;align-items:center;height:var(--size-segmented);border-radius:var(--radius-capsule);background:var(--color-segmented-track);color:var(--color-segmented-text);padding-right:16px;gap:16px}
.segs{display:inline-flex;align-items:center;height:100%;padding:0 18px;border-radius:var(--radius-capsule);background:var(--color-segmented-selectedBg);color:var(--color-segmented-selectedText);font-weight:700}
.sheet{margin-top:var(--space-lg);background:var(--color-surface-sheetSort);border-radius:var(--radius-sheet) var(--radius-sheet) var(--radius-md) var(--radius-md);padding:8px 24px 16px}
.sheet p{margin:10px 0}.sh{color:var(--color-text-sheetHeader)}
.grab{display:block;margin:0 auto;width:var(--size-grabber-width);height:var(--size-grabber-height);border-radius:var(--radius-capsule);background:var(--color-border-grabber)}
.selo{color:var(--color-text-accentOnSheet);display:flex;justify-content:space-between}
.beta{margin-left:8px;padding:1px 6px;border-radius:4px;background:var(--color-badge-beta);color:var(--color-text-onBadge);font-weight:700}
footer{margin-top:48px;color:var(--color-text-secondary);font-size:12px}
""".strip()

    parts = ["<!doctype html>", '<html lang="en" data-theme="dark">', "<head>", '<meta charset="utf-8">',
             '<meta name="viewport" content="width=device-width, initial-scale=1">', "<title>%s style guide</title>" % esc(NAME), "<style>",
             ":root{%s}" % ";".join(core_css),
             ':root{color-scheme:dark;%s}' % ";".join(dark_css),
             "\n".join(type_css), page_css, "</style>", "</head>", "<body>", '<div class="wrap">',
             '<header class="top"><h1>%s style guide</h1>' % esc(NAME),
             '<p class="lede">%s Every value below comes from tokens.json; points are 1:1 with CSS pixels. ' % esc(LEDE)
             + "The font is not known, so the page uses the platform sans. "
             "Glass is drawn as its centre colour: the real material blurs what is behind it. There is no light theme to switch to.</p></header>",
             "<h2>Colour</h2>",
             '<p class="lede">The badge says how each value was read: Sampled (a flat fill, exact), Sampled (text) '
             "(the anti-aliased pixel furthest from the fill), Derived (worked out, or a glass or gradient reading). Hover a swatch for its capture.</p>",
             "".join(colour_html),
             # PRODUCT (adapt): the palette and ramp captions
             "<h3>Greens and categories (core)</h3><p class=\"lede\">Spotify green, the iOS system green its switches keep, and the flat colours of Search's browse tiles.</p>",
             '<div class="palette">%s%s</div>' % (dots(("color", "brand")) + dots(("color", "system")), dots(("color", "category"))),
             "<h3>Neutral ramp (core)</h3><p class=\"lede\">Every grey the dark theme uses, light to dark. Named by order, not a published ramp.</p>",
             '<div class="ramp">%s</div>' % neutrals,
             "<h2>Radii</h2>", '<div class="radii">%s</div>' % radii,
             "<h2>Spacing</h2>", spacing, "<h2>Sizes</h2>", sizes,
             "<h2>Type scale</h2>",
             '<div class="scroll"><table class="tokens"><thead><tr><th>Token</th><th>Spec</th><th>Specimen</th></tr></thead><tbody>%s</tbody></table></div>' % type_rows,
             "<h2>Components</h2>", '<p class="lede">Built from the tokens only; grey squares stand in for artwork.</p>', specimens,
             "<footer>Generated by tools/build_style_guide.py from tokens.json. %s's screenshots and visual system belong to %s; this package holds no %s code or artwork.</footer>" % (esc(NAME), esc(OWNER), esc(NAME)),
             "</div>", "</body>", "</html>", ""]
    OUT.write_text("\n".join(parts), encoding="utf-8")
    return OUT


if __name__ == "__main__":
    print("wrote", build().relative_to(PKG))
