#!/usr/bin/env python3
"""Build tokens.json (W3C DTCG, Tokens Studio multi-set layout) from raw/readings.json (native kit).

Copied from the native kit (tools/kit/native, from systems/grokbot). core() and semantic(), marked
PRODUCT (adapt), map YouTube's readings to roles; the helpers, check() and build() are the kit's.

    python3 tools/build_tokens.py

raw/readings.json is written by tools/measure.py from the full-colour iPhone Mirroring captures.
Every token here names the reading it came from, so `$extensions.source` = {evidence, capture} is
the reading's own label and file. A value worked out from readings (a scale step, a scrim alpha, a
rounded size) is Derived and says how in `$description`. Dimensions are px with 1 px = 1 pt.

The builder refuses a token without a source, an alias that points at nothing, a colour that is not
#RRGGBB(AA), a dimension that is not one px length, and a light and dark set whose keys differ.
Standard library only. Deterministic: the same readings give the same bytes.
"""
import json
import pathlib
import re

PKG = pathlib.Path(__file__).resolve().parent.parent
_READINGS = PKG / "raw" / "readings.json"
READ = json.loads(_READINGS.read_text()) if _READINGS.exists() else {}  # empty in the kit copy, for its tests
MEASURED = f"raw/{PKG.name}-measured.md"


class Missing(Exception):
    pass


def rd(rid, theme="dark"):
    try:
        return READ[rid][theme]
    except KeyError:
        raise Missing(f"no reading {rid} for {theme}")


def tok(value, typ, desc, evidence, capture):
    return {"$value": value, "$type": typ, "$description": desc,
            "$extensions": {"source": {"evidence": evidence, "capture": capture}}}


def from_reading(rid, theme, typ, desc):
    r = rd(rid, theme)
    note = desc
    if r.get("share") is not None and r["evidence"] == "Derived":
        note += f" The box's dominant colour covers {round(r['share'] * 100)}% of it (a gradient, glass or a thin mark), so it is a reading, not an exact fill."
    return tok(r["value"], typ, note, r["evidence"], r["capture"])


def px(v):
    return f"{v:g}px"


def pt_of(rid, theme="dark", index=0):
    """A number in pt from an extent ('45pt') or bbox ('343x54pt') reading."""
    v = rd(rid, theme)["value"].rstrip("pt")
    return float(v.split("x")[index])


def derived(value, typ, desc, capture=MEASURED):
    return tok(value, typ, desc, "Derived", capture)


def alias(path, typ, desc):
    return tok("{" + path + "}", typ, desc, "Derived", MEASURED)


# ---------------------------------------------------------------- core

def neutral_ramp():
    """Every grey the semantic sets use, both themes, sorted light to dark. Not a published ramp:
    the steps are the values the app shows, named by order."""
    ids = ["bg.page", "bg.sheet", "surface.chip", "surface.menu", "surface.commentField", "surface.adSheet",
           "button.tonal", "border.outline", "border.tabBar", "text.title", "text.meta", "text.helper",
           "text.placeholder", "switch.offTrack", "sheet.grabber"]
    seen = {}
    for rid in ids:
        for theme, r in READ[rid].items():
            v = r["value"]
            rr, gg, bb = int(v[1:3], 16), int(v[3:5], 16), int(v[5:7], 16)
            if max(rr, gg, bb) - min(rr, gg, bb) <= 12:     # neutral enough
                seen.setdefault(v, []).append((f"{theme} {rid}", r["evidence"], r["capture"]))
    lum = lambda h: sum(int(h[i:i + 2], 16) for i in (1, 3, 5))
    rank = ["Sampled", "Sampled (text)", "Derived"]   # the most exact reading of the value wins
    out = {}
    for i, v in enumerate(sorted(seen, key=lum, reverse=True)):
        uses = sorted(set(seen[v]))
        best = min(uses, key=lambda u: rank.index(u[1]))
        listed = ", ".join(f"{name} ({ev})" for name, ev, _ in uses)
        out[f"{i * 50:03d}"] = tok(v, "color", f"Used by: {listed}.", best[1], best[2])
    return out


def span(rid, theme="dark"):
    """Length in pt of the run a `find` reading found (its first to last position)."""
    v = rd(rid, theme)["value"]
    return (v[-1] - v[0] + 1) / 2


# PRODUCT (adapt) from here to semantic()'s end: the mapping from readings to tokens.
def core():
    c = {}
    c["color"] = {
        "neutral": neutral_ramp(),
        "red": tok(rd("brand.red", "light")["value"], "color",
                   f"YouTube red: the watch-progress bar under a thumbnail ({rd('brand.red')['value']} in dark, {rd('brand.red', 'light')['value']} in light, two pixel rows) and the dot on the Subscriptions tab ({rd('brand.badge')['value']}). The same in both themes. It marks the brand and progress, never an error or a button.",
                   "Derived", rd("brand.red", "light")["capture"]),
    }
    acc = rd("size.accordion")["value"]
    c["radius"] = {
        "chip": derived("8px", "dimension", f"Filter chips: {rd('radius.chip')['value']} in both themes, on a 32 pt chip. Plus or minus 2 pt."),
        "thumbnail": derived("8px", "dimension", f"Thumbnails in shelves and History ({rd('radius.thumbnail')['value']}) and Shorts cards ({rd('radius.shortsCard')['value']}). Feed thumbnails run edge to edge with no radius."),
        "card": derived("12px", "dimension", f"The comments teaser card ({rd('radius.comments')['value']}) and the top corners of a bottom sheet ({rd('radius.sheet')['value']} in both themes)."),
        "sheet": alias("radius.card", "dimension", "Top corners of a bottom sheet (sort, My Ad Centre): the card radius."),
        "menu": derived("16px", "dimension", f"The video overflow menu: {rd('radius.menu')['value']}. Plus or minus 2 pt."),
        "capsule": derived("999px", "dimension", f"Fully round ends: the search field ({rd('radius.search')['value']} on 32 pt), ad buttons ({rd('radius.buttonFilled')['value']} on 40 pt), View channel and Get Premium, the Subscribe pill, the comment field and the duration badge."),
    }
    card = rd("size.comments")["box"]
    c["space"] = {
        "base": derived("4px", "dimension", "Measured gaps land on multiples of 4 pt within a pixel or two."),
        "xs": derived("4px", "dimension", "Between a title and its meta line, and between a subscription avatar and its name."),
        "sm": derived("8px", "dimension", "Between chips in the filter row (about 8.5 pt, dark/13) and between a channel avatar and its title column."),
        "md": derived("12px", "dimension", f"Screen margin of the feed: chips, channel avatars and the comments card start {(card[0] - 16) / 2:g} pt from the screen edge."),
        "lg": derived("16px", "dimension", "Padding inside the comments card and between grouped blocks on the You tab."),
        "xl": derived("24px", "dimension", "Between shelves (Shorts, Most relevant, History, Library)."),
        "screenMargin": alias("space.md", "dimension", "Left and right margin of the feed, chips and cards. Settings lists sit further in, at about 18 pt (their icons start at x = 52 px)."),
        "accordionGap": derived(f"{(acc[4] - acc[3] - 1) / 2:g}px", "dimension", f"Gap between the outlined accordions in My Ad Centre: the first ends at {acc[3]} px and the second starts at {acc[4]} px down x = 60."),
    }
    c["size"] = {
        "chip": tok(px(round(pt_of("size.chip", "dark", 1))), "dimension", f"Filter chip height: {rd('size.chip')['value']} dark, {rd('size.chip', 'light')['value']} light.", "Sampled", rd("size.chip")["capture"]),
        "searchField": tok(px(pt_of("size.search", "dark", 1)), "dimension", f"Search field height ({rd('size.search')['value']}).", "Sampled", rd("size.search")["capture"]),
        "button": tok(px(round(pt_of("size.buttonFilled", "dark", 1))), "dimension", f"Ad call-to-action and Watch buttons: {rd('size.buttonFilled')['value']}, two side by side.", "Sampled", rd("size.buttonFilled")["capture"]),
        "pill": tok(px(round(pt_of("size.pill", "dark", 1))), "dimension", f"View channel and Get Premium: {rd('size.pill')['value']}.", "Sampled", rd("size.pill")["capture"]),
        "subscribe": tok(px(pt_of("size.subscribe", "dark", 1)), "dimension", f"Subscribe pill on a Short: {rd('size.subscribe')['value']}.", "Sampled", rd("size.subscribe")["capture"]),
        "buttonLarge": tok(px(pt_of("size.upsellButton", "dark", 1)), "dimension", f"Full-width button on the Premium interstitial ('1 month free'): {rd('size.upsellButton')['value']}.", "Sampled", rd("size.upsellButton")["capture"]),
        "row": tok(px(float(rd("rows.settings")["value"].rstrip("pt"))), "dimension", "Settings row (icon and one-line label), label to label.", "Derived", rd("rows.settings")["capture"]),
        "rowSearch": tok(px(float(rd("rows.search")["value"].rstrip("pt"))), "dimension", "Search history and suggestion row, icon to icon.", "Derived", rd("rows.search")["capture"]),
        "accordion": derived(f"{(acc[3] - acc[0] + 1) / 2:g}px", "dimension", f"Outlined accordion row in My Ad Centre, outline included (edges {acc[0]} to {acc[3]} px down x = 60)."),
        "tabBar": derived("48px", "dimension", "Tab bar: its top hairline sits 82 pt above the screen's bottom edge (rows.tabBar, y = 1600 of 1764 px); 48 pt of that holds the icons and labels, the rest is the home-indicator inset."),
        "createButton": tok(px(pt_of("size.createButton")), "dimension", "Round Create (+) button in the middle of the tab bar.", "Sampled", rd("size.createButton")["capture"]),
        "avatarChannel": tok(px(pt_of("size.avatarChannel")), "dimension", "Channel avatar beside a video title.", "Sampled", rd("size.avatarChannel")["capture"]),
        "avatarSubscription": tok(px(pt_of("size.avatarSub")), "dimension", "Avatar in the Subscriptions row.", "Sampled", rd("size.avatarSub")["capture"]),
        "avatarProfile": tok(px(pt_of("size.avatarProfile")), "dimension", "The owner's avatar on the You tab.", "Sampled", rd("size.avatarProfile")["capture"]),
        "switch": {
            "width": tok(px(pt_of("size.switch")), "dimension", f"Switch track: {rd('size.switch')['value']} dark, {rd('size.switch', 'light')['value']} light, anti-aliased edge excluded.", "Sampled", rd("size.switch")["capture"]),
            "height": tok(px(pt_of("size.switchTrack.h")), "dimension", f"Switch track height, read beside the thumb ({rd('size.switchTrack.h')['value']} dark, {rd('size.switchTrack.h', 'light')['value']} light). The thumb is taller and overhangs it.", "Sampled", rd("size.switchTrack.h")["capture"]),
            "thumb": tok(px(pt_of("size.switchThumb")), "dimension", f"Round switch thumb ({rd('size.switchThumb')['value']} in dark), wider than the track is tall. The light thumb sits on a shadow and could not be bounded.", "Sampled", rd("size.switchThumb")["capture"]),
        },
        "menuWidth": tok(px(round(span("size.menu.w"))), "dimension", f"Video overflow menu width: {span('size.menu.w'):g} pt dark, {span('size.menu.w', 'light'):g} pt light; nine items make it {span('size.menu.h'):g} pt tall in dark.", "Sampled", rd("size.menu.w")["capture"]),
        "commentsCard": tok(px(pt_of("size.comments", "dark", 1)), "dimension", f"Comments teaser on the watch page: {rd('size.comments')['value']}.", "Sampled", rd("size.comments")["capture"]),
        "commentField": tok(px(pt_of("size.commentField", "dark", 1)), "dimension", f"'Comment...' field inside the teaser: {rd('size.commentField')['value']}.", "Sampled", rd("size.commentField")["capture"]),
        "touchTarget": derived("44px", "dimension", "Rows, tab items and the header icons are 44 pt or more. Chips, the search field and View channel are 32 pt and sit in wider rows."),
    }
    c["border"] = {"width": {
        "hairline": derived("1px", "dimension", "The tab bar's top line, two device pixels (border.tabBar)."),
        "outline": derived("1px", "dimension", "Outlined buttons (Get Premium) and accordions: a two-pixel line at 2x (border.outline, border.accordion)."),
    }}
    c["fontFamily"] = {"base": tok("system", "fontFamily", "Not determinable from pixels. Body text looks like Roboto and headings like a heavier display face (the nav titles, 'Shorts', the Premium headline); neither can be proved from a screenshot, so use the platform font.", "Not captured", MEASURED)}
    c["fontWeight"] = {
        "regular": derived(400, "fontWeight", "Settings rows, menu items, search rows, meta lines, helper text. Judged by stroke width, not measured."),
        "medium": derived(500, "fontWeight", "Video titles, chip labels, button labels. Judged by stroke width."),
        "bold": derived(700, "fontWeight", "Nav titles, shelf and section titles, the Premium headline. Judged by stroke width."),
    }

    def ty(size_rid, weight, lh, desc, extra=()):
        sizes = [rd(r)["value"] for r in (size_rid,) + tuple(extra)]
        v = {"fontFamily": "{fontFamily.base}", "fontWeight": "{fontWeight.%s}" % weight,
             "fontSize": sizes[0].replace("pt", "px")}
        if lh:
            v["lineHeight"] = lh
        return tok(v, "typography", desc + f" Cap-height readings: {', '.join(sorted(set(sizes)))}.", "Derived", rd(size_rid)["capture"])

    lines = lambda rid: f"{float(rd(rid)['value'].rstrip('pt')):g}px"
    c["typography"] = {
        "display": ty("type.display", "bold", None, "The Premium interstitial headline, centred over two lines."),
        "sheetTitle": ty("type.sheetTitle", "bold", None, "Title of the My Ad Centre sheet."),
        "navTitle": ty("type.navTitle", "bold", None, "Nav bar title on pushed pages (Settings, General, Appearance)."),
        "sectionTitle": ty("type.sectionTitle", "bold", None, "Shelf and section titles: History, Library, Most relevant, the Settings 'Account' header.", ("type.sectionHeader",)),
        "body": ty("type.settingsRow", "regular", None, "Settings rows and overflow-menu items.", ("type.menuItem",)),
        "videoTitle": ty("type.videoTitle", "medium", lines("lines.videoTitle"), "Video titles under feed cards and on the watch page, up to two lines.", ("type.searchRow",)),
        "label": ty("type.button", "medium", None, "Button and chip labels (Watch, Install, Today).", ("type.chip",)),
        "meta": ty("type.meta", "regular", lines("lines.helper"), "Meta lines (channel, views, age), helper text, suggestion second lines, channel names under avatars, the Subscribe label.", ("type.helper", "type.suggestionSub", "type.channelName", "type.subscribe", "type.duration")),
        "tab": ty("type.tab", "regular", None, "Tab bar labels (Home, Shorts, Subscriptions, You)."),
    }
    c["$extensions"] = {"notTokenised": [
        "Ambient tint: the block under a video or an ad takes a dark tint from its artwork in dark (surface.adCard reads #020F1B under one ad and a dark red under another); only the readings are kept",
        "Tab bar material: the bar is translucent over the feed, so its fill is a reading of one moment",
        "Motion and easing: stills only",
        "Shadows: the light overflow menu and switch thumb cast soft shadows; none was measured",
        "Line heights of one-line labels: only multi-line blocks were measured",
    ]}
    return c


# ---------------------------------------------------------------- semantic sets

def scrim(theme):
    ref, dim = rd("scrim.ref", theme)["value"], rd("scrim.dim", theme)["value"]
    a = 1 - int(dim[1:3], 16) / int(ref[1:3], 16)
    return derived("#000000%02X" % round(a * 255), "color",
                   f"Black at {round(a * 100)}%: the You tab reads {ref} undimmed and {dim} under the sort sheet.",
                   rd("scrim.dim", theme)["capture"])


def duration():
    ref, dim = rd("overlay.durationRef")["value"], rd("overlay.duration")["value"]
    a = 1 - int(dim[1:3], 16) / int(ref[1:3], 16)
    return derived("#000000%02X" % round(a * 255), "color",
                   f"Black at {round(a * 100)}% under a thumbnail's duration, read where the badge sits on a white frame ({ref} beside it, {dim} under it). The same in both themes: it sits on artwork.",
                   rd("overlay.duration")["capture"])


def dark_only(theme, rid, desc, light_from=None, why=""):
    """A role read in dark only. Light reuses the dark value (light_from None) or the light value of
    the closest role, as Derived, and says which."""
    if theme == "dark":
        return from_reading(rid, "dark", "color", desc)
    src = rd(light_from, "light") if light_from else rd(rid, "dark")
    return derived(src["value"], "color", desc + " Not captured in light: " + why, src["capture"])


def semantic(theme):
    f = lambda rid, desc, typ="color": from_reading(rid, theme, typ, desc)
    on_media = "it sits on video or artwork, so the dark value is used."
    s = {"color": {
        "bg": {
            "page": f("bg.page", "Every page: home, Shorts shelf, You, search, settings."),
            "sheet": f("bg.sheet", "Bottom sheets (library sort)."),
            "scrim": scrim(theme),
        },
        "surface": {
            "secondary": f("surface.chip", "Unselected filter chips, the search field, the library chips: the app's one raised neutral."),
            "inverse": f("surface.chipSelected", "The selected chip, filled buttons and the View channel pill: the theme's ink, white in dark and near-black in light."),
            "menu": f("surface.menu", "The video overflow menu (white with a soft shadow in light)."),
            "tabBar": f("surface.tabBar", "Tab bar, a translucent material over the feed; a reading of one moment."),
            "createButton": f("surface.createButton", "The round Create (+) button in the tab bar."),
            "card": dark_only(theme, "surface.comments", "The comments teaser card on the watch page (a reading over the page's ambient tint).", "surface.chip", "filled from surface.secondary, the closest light role."),
            "field": dark_only(theme, "surface.commentField", "The 'Comment...' field inside the comments card.", "surface.chip", "filled from surface.secondary."),
            "ad": f("surface.adCard", "Block behind an ad's text and buttons. In dark it takes a tint from the ad's artwork (this one is navy), so treat it as a reading, not a fixed colour."),
            "adSheet": dark_only(theme, "surface.adSheet", "Body of the My Ad Centre sheet.", None, "the sheet's body stays dark in the light theme too (light/03), so the dark value is the light value."),
        },
        "border": {
            "outline": f("border.outline", "Outlined buttons (Get Premium)."),
            "tabBar": f("border.tabBar", "Hairline along the top of the tab bar."),
            "accordion": dark_only(theme, "border.accordion", "Outline of the accordions and the Send feedback button in My Ad Centre.", None, "the sheet body is dark in both themes."),
        },
        "text": {
            "primary": f("text.title", "Video titles, settings rows, menu items, search rows, chip labels."),
            "secondary": f("text.meta", f"Meta lines (channel, views, age), helper text, row values, suggestion second lines, the owner's handle. Readings in this role: {', '.join(sorted({rd(r, theme)['value'] for r in ('text.meta', 'text.helper', 'text.rowValue', 'text.suggestionSub', 'text.handle')}))}."),
            "placeholder": f("text.placeholder", "'Search YouTube' in the empty search field."),
            "inverse": f("text.chipSelected", "Labels on the inverse surface: the selected chip, filled buttons, View channel."),
            "tab": f("text.tab", "Tab bar labels and icons."),
            "link": f("text.link", "Text links ('All' at the end of the subscriptions row)."),
            "linkOnSheet": dark_only(theme, "text.linkSheet", "Link inside the My Ad Centre sheet (Safety Centre), lighter than text.link.", None, "the sheet body is dark in both themes."),
        },
        "accent": {
            "default": f("accent.unreadDot", "The app's blue: the new-content dot on a subscription avatar, text links, the switch thumb when on."),
        },
        "brand": {
            "red": alias("color.red", "color", "YouTube red: watch progress and the Subscriptions tab dot. The same in both themes."),
        },
        "focus": {
            "caret": f("focus.caret", "Text caret in the focused search field: the only focus indicator seen. A reading of two pixel columns; the light caret may have been mid-blink."),
        },
        "button": {
            "filled": {"bg": f("button.filled", "Primary call to action (Install, Shop now, Learn more): the theme's ink."),
                       "text": f("button.filledLabel", "Filled button label.")},
            "tonal": {"bg": f("button.tonal", "The secondary button beside it (Watch). In dark it takes the ad's tint (navy here); in light it reads a neutral grey."),
                      "text": f("button.tonalLabel", "Tonal button label.")},
            "pill": {"bg": f("button.pill", "View channel: the inverse surface as a pill."),
                     "text": f("button.pillLabel", "View channel label.")},
            "outlined": {"bg": f("surface.outlined", "Get Premium: the page colour with an outline."),
                         "border": alias("color.border.outline", "color", "The outline of Get Premium.")},
            "subscribe": {"bg": dark_only(theme, "surface.subscribe", "Subscribe pill on a Short, white over the video.", None, on_media)},
            "large": {"bg": dark_only(theme, "surface.upsellButton", "The '1 month free' button on the Premium interstitial, dark over a light gradient.", None, "the interstitial was seen once, in dark; it draws its own light background."),
                      "text": dark_only(theme, "button.largeLabel", "The '1 month free' label: white on the dark button.", None, "the interstitial was seen once, in dark; it draws its own light background.")},
        },
        "switch": {
            "onTrack": f("switch.onTrack", "Switch on, track: a pale blue."),
            "onThumb": f("switch.onThumb", "Switch on, thumb: the accent blue."),
            "offTrack": f("switch.offTrack", "Switch off, track."),
            "offThumb": f("switch.offThumb", "Switch off, thumb."),
        },
        "overlay": {
            "duration": duration(),
        },
        "icon": {
            "check": f("icon.check", "Tick on the chosen row of a choice list (Appearance, library sort)."),
            "grabber": f("sheet.grabber", "Grabber at the top of a bottom sheet."),
        },
        "status": {
            "info": alias("color.accent.default", "color", "Info: the accent blue (new content). No success, warning or danger colour appeared."),
        },
    }}
    s["$extensions"] = {"notTokenised": [
        "Success, warning and danger colours: no such state was seen; YouTube red marks the brand and progress, not errors",
        "Pressed and disabled states: stills only, and no disabled control appeared",
        "Ambient tints under videos and ads: they follow the artwork",
    ]}
    return s


# ---------------------------------------------------------------- build and checks

def walk(node, path=()):
    if isinstance(node, dict) and "$value" in node:
        yield path, node
        return
    if isinstance(node, dict):
        for k, v in node.items():
            if not k.startswith("$"):
                yield from walk(v, path + (k,))


def aliases(v):
    """Every {alias} in a value, including those inside a composite (a typography style)."""
    if isinstance(v, str):
        return re.findall(r"\{([^{}]+)\}", v)
    if isinstance(v, dict):
        return [a for x in v.values() for a in aliases(x)]
    return []


def check(doc):
    sets = [s for s in ("core", "light", "dark") if s in doc]  # a one-theme app has no light or no dark
    paths = {".".join(p) for name in sets for p, _ in walk(doc[name])}
    for name in sets:
        for p, t in walk(doc[name]):
            where = name + "." + ".".join(p)
            src = t.get("$extensions", {}).get("source", {})
            assert src.get("evidence") and src.get("capture"), f"{where}: no source"
            v = t["$value"]
            for a in aliases(v):
                assert a in paths, f"{where}: alias {{{a}}} points at nothing"
            if isinstance(v, str) and v.startswith("{"):
                continue
            elif t["$type"] == "color":
                assert re.fullmatch(r"#[0-9A-F]{6}([0-9A-F]{2})?", v), f"{where}: bad colour {v}"
            elif t["$type"] == "dimension":
                assert re.fullmatch(r"-?\d+(\.\d+)?px", v), f"{where}: bad dimension {v}"
    keys = lambda s: sorted(".".join(p) for p, _ in walk(doc[s]))
    if "light" in doc and "dark" in doc:
        assert keys("light") == keys("dark"), "light and dark keys differ"


def build():
    doc = {
        "core": core(),
        "light": semantic("light"),
        "dark": semantic("dark"),
        "$themes": [  # PRODUCT (adapt): how each theme was set for the capture; drop a theme the app lacks
            {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"},
             "$description": "Settings > General > Appearance > Light theme, set for the capture on 2026-10-24 and put back to Use device theme. Read from screenshots/light/."},
            {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"},
             "$description": "Appearance > Use device theme with the phone in dark mode. Read from screenshots/dark/."},
        ],
        "$metadata": {"tokenSetOrder": ["core", "light", "dark"]},
    }
    check(doc)
    (PKG / "tokens.json").write_text(json.dumps(doc, indent=1, ensure_ascii=False) + "\n")
    n = sum(1 for s in ("core", "light", "dark") for _ in walk(doc[s]))
    print(f"tokens.json: {n} tokens")


if __name__ == "__main__":
    if not READ:
        raise SystemExit("no raw/readings.json: run tools/measure.py first")
    build()
