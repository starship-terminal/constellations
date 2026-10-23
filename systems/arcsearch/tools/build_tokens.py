#!/usr/bin/env python3
"""Build tokens.json (W3C DTCG, Tokens Studio multi-set layout) from raw/readings.json (native kit).

Copied from the native kit (tools/kit/native, from systems/grokbot). core() and semantic(), marked
PRODUCT (adapt), map Arc Search's readings to roles; the helpers, check() and build() are the kit's.

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
    ids = ["bg.page", "bg.sheet", "surface.group", "surface.card", "surface.edit", "surface.iconSheet", "surface.close",
           "border.separator", "text.row", "text.value", "text.chevron", "text.section", "text.helper", "text.subtitle",
           "text.rowUrl"]
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


def pt(rid, theme="dark"):
    """A number in pt from a one-number reading ('48.5pt')."""
    return float(rd(rid, theme)["value"].rstrip("pt"))


def edges():
    """Group tops and bottoms down x = 145 in dark/05: pairs of edge pixels, top first."""
    v = rd("edges.groups")["value"]
    return v[1::2]   # the second pixel of each pair is the first one inside (or outside) a group


# PRODUCT (adapt) from here to semantic()'s end: the mapping from readings to tokens.
def core():
    c = {}
    tile = lambda rid, desc: tok(rd(rid)["value"], "color", desc + f" The same in both themes ({rd(rid, 'light')['value']} in light).",
                                 rd(rid)["evidence"], rd(rid)["capture"])
    c["color"] = {
        "neutral": neutral_ramp(),
        "tile": {
            "blue": tile("tile.blue", "Settings icon tile: Search Engine, Change App Icon, Open App Links, Pinch to Summarize, Export Data."),
            "green": tile("tile.green", "Settings icon tile: Languages, Swipe to Navigate."),
            "yellow": tile("tile.yellow", "Settings icon tile: Auto-Open Keyboard, Block Trackers."),
            "purple": tile("tile.purple", "Settings icon tile: Archive Inactive Tabs, Add to Home Screen, Collapse Bottom Bar."),
            "red": tile("tile.red", "Settings icon tile: Clear Browsing Data, Block Ads."),
        },
    }
    e = edges()
    c["radius"] = {
        "tile": derived(f"{round(pt('radius.tile')):g}px", "dimension", f"Settings icon tiles: {rd('radius.tile')['value']} on a 28 pt tile, both themes. At this size the reading is plus or minus 2 pt."),
        "pill": derived("10px", "dimension", f"Browse for Me buttons: {rd('radius.pill')['value']} on a 30 pt button (dark/02). Plus or minus 2 pt."),
        "panel": derived("14px", "dimension", f"Panels inside the page menu (the list of Display Options to Request Desktop Site, Site Settings, the notice): {rd('radius.menuGroup')['value']} from where the panel's straight edges meet."),
        "tileButton": derived("20px", "dimension", f"The square Find on Page, Summarize, Pin and Share buttons in the page menu: {rd('radius.tileButton')['value']}."),
        "group": derived("26px", "dimension", f"Grouped list cards in Settings ({rd('radius.group')['value']}) and the Archive's cards ({rd('radius.card')['value']}), in both themes."),
        "sheet": derived("48px", "dimension", f"Top corners of a sheet (Settings): {rd('radius.sheet', 'light')['value']} in light, the same as the screen's own corners. The dark sheet is too close to the dimmed page behind it to bound."),
        "capsule": derived("999px", "dimension", f"Fully round ends: the Downloads and Archive buttons ({rd('radius.button')['value']} on 40 pt), the search field ({rd('radius.search')['value']} on 48 pt), the address bar ({rd('radius.address')['value']} on 48 pt), Done, Edit, the + button, the find bar and every round icon button."),
    }
    c["space"] = {
        "screenMargin": derived(f"{(rd('size.group')['box'][0] - 16) / 2:g}px", "dimension", f"Left and right margin of grouped cards, buttons and the search field: the Settings groups start at x = {rd('size.group')['box'][0]} px, 16 px in from the screen's edge at 16."),
        "groupGap": derived(f"{(e[3] - e[2]) / 2:g}px", "dimension", f"Between two groups in Settings: one group ends at y = {e[2]} px and the next starts at {e[3]} (edges.groups)."),
        "buttonToGroup": derived(f"{(e[1] - e[0]) / 2:g}px", "dimension", f"Between the Downloads and Archive buttons and the first group: {e[0]} to {e[1]} px."),
    }
    a, b = rd("size.button")["box"][2], rd("size.buttonRight")["box"][0]
    c["space"]["buttonGap"] = derived(f"{(b - a - 3) / 2:g}px", "dimension", f"Between the Downloads and Archive buttons: the flat fills end at x = {a} px and start at {b}, with one anti-aliased pixel at each edge between them.")
    c["size"] = {
        "row": tok(px(float(rd("rows.settings")["value"].rstrip("pt"))), "dimension", "Settings row (icon tile and one-line label), tile to tile. A group of two rows is 103.5 pt tall (size.group).", "Derived", rd("rows.settings")["capture"]),
        "rowLauncher": tok(px(round(pt("rows.launcher"))), "dimension", f"Launcher and suggestion rows under the search field, label to label ({rd('rows.launcher')['value']} dark, {rd('rows.launcher', 'light')['value']} light).", "Derived", rd("rows.launcher")["capture"]),
        "rowHistory": tok(px(pt("rows.archive")), "dimension", "Archive history row (favicon, title, URL), favicon to favicon.", "Derived", rd("rows.archive")["capture"]),
        "rowMenu": tok(px(pt("rows.menu")), "dimension", "Page menu list row (Display Options to Request Desktop Site), label to label.", "Derived", rd("rows.menu")["capture"]),
        "tile": derived("28px", "dimension", f"Settings icon tile: {rd('size.tile')['value']} with its anti-aliased edge left out."),
        "button": tok(px(round(pt_of("size.button", "dark", 1))), "dimension", f"Downloads and Archive buttons: {rd('size.button')['value']}, two side by side.", "Sampled", rd("size.button")["capture"]),
        "searchField": tok(px(pt_of("size.search", "dark", 1)), "dimension", f"Search field in the launcher: {rd('size.search')['value']}.", "Sampled", rd("size.search")["capture"]),
        "addressBar": derived(px(round(pt("size.address"))), "dimension", f"Address bar at the top of the page menu: {rd('size.address')['value']} between its rims in both themes.", rd("size.address")["capture"]),
        "findField": derived("48px", "dimension", f"Find field: {rd('size.findField')['value']} dark, {rd('size.findField', 'light')['value']} light between its rims. Plus or minus 1 pt.", rd("size.findField")["capture"]),
        "iconButton": derived("48px", "dimension", f"Round glass icon buttons in the find bar: the close button reads {rd('size.findClose')['value']} dark and {rd('size.findClose', 'light')['value']} light between its rims, the find field beside it 48."),
        "pill": tok(px(round(pt_of("size.pill", "dark", 1))), "dimension", f"Browse for Me button: {rd('size.pill')['value']} dark, {rd('size.pill', 'light')['value']} light.", "Sampled", rd("size.pill")["capture"]),
        "plus": tok(px(round(pt_of("size.plus", "dark", 1))), "dimension", f"The + (new tab) button in the bottom toolbar: {rd('size.plus')['value']}.", "Sampled", rd("size.plus")["capture"]),
        "plusWidth": tok(px(pt_of("size.plus")), "dimension", "Width of the + button.", "Sampled", rd("size.plus")["capture"]),
        "tileButton": tok(px(round(pt_of("size.tileButton", "dark", 1))), "dimension", f"Square buttons in the page menu (Find on Page, Summarize, Pin, Share): {rd('size.tileButton')['value']}, four across.", "Sampled", rd("size.tileButton")["capture"]),
        "closeButton": tok(px(round(pt_of("size.close", "dark", 1))), "dimension", f"Round close button in a sheet's header (App Icon): {rd('size.close')['value']}.", "Sampled", rd("size.close")["capture"]),
        "confirmButton": derived("44px", "dimension", f"Round accent button at the Archive's top right: {rd('size.confirm')['value']} dark, {rd('size.confirm', 'light')['value']} light with the anti-aliased edge left out, so 44 pt.", rd("size.confirm")["capture"]),
        "navButtonHeight": tok(px(pt_of("size.edit", "dark", 1)), "dimension", f"Edit and Done capsules in a nav bar: Edit is {rd('size.edit')['value']}.", "Sampled", rd("size.edit")["capture"]),
        "searchBar": tok(px(pt_of("size.searchBar", "dark", 1)), "dimension", f"Archive search field at the bottom of the screen: {rd('size.searchBar')['value']} with a 48 pt round close button beside it.", "Sampled", rd("size.searchBar")["capture"]),
        "switch": {
            "width": derived("64px", "dimension", f"Switch track: {rd('size.switch')['value']} with the anti-aliased edge left out, so 64 x 28 pt, the iOS 26 switch."),
            "height": derived("28px", "dimension", f"Switch track height ({rd('size.switch')['value']} read)."),
            "thumb": tok(px(pt_of("size.switchThumb")), "dimension", f"Switch thumb, a white capsule wider than it is tall: {rd('size.switchThumb')['value']} in dark.", "Sampled", rd("size.switchThumb")["capture"]),
        },
        "touchTarget": derived("44px", "dimension", "Rows, the confirm button and every round icon button are 44 pt or more; Browse for Me (30 pt) and the + button (40 pt) sit in taller rows."),
    }
    c["border"] = {"width": {
        "hairline": derived("1px", "dimension", "Separators inside a group, inset to start at the label: two anti-aliased device pixels at 2x (border.separator)."),
    }}
    c["fontFamily"] = {"base": tok("system", "fontFamily", "Not determinable from pixels. The labels look like SF Pro, the iOS system font, but a screenshot cannot prove it; use the platform font.", "Not captured", MEASURED)}
    c["fontWeight"] = {
        "regular": derived(400, "fontWeight", "Row labels, values, history titles and URLs, helper text, menu items. Judged by stroke width, not measured."),
        "medium": derived(500, "fontWeight", "Button labels (Downloads, Archive), the notice. Judged by stroke width."),
        "semibold": derived(600, "fontWeight", "Nav and page titles, Done, section headers, Browse for Me, the space name. Judged by stroke width."),
    }

    def ty(size_rid, weight, lh, desc, extra=()):
        sizes = [rd(r)["value"] for r in (size_rid,) + tuple(extra)]
        v = {"fontFamily": "{fontFamily.base}", "fontWeight": "{fontWeight.%s}" % weight,
             "fontSize": sizes[0].replace("pt", "px")}
        if lh:
            v["lineHeight"] = lh
        return tok(v, "typography", desc + f" Cap-height readings: {', '.join(sorted(set(sizes)))}.", "Derived", rd(size_rid)["capture"])

    c["typography"] = {
        "spaceTitle": ty("type.spaceTitle", "semibold", None, "The space's name at the top of its sheet ('Main')."),
        "search": ty("type.search", "regular", None, "Text and placeholder in the launcher's search field ('Search...')."),
        "navTitle": ty("type.navTitle", "semibold", None, "Nav and page titles: Settings, Default Search Engine, Archive.", ("type.title",)),
        "body": ty("type.row", "regular", f"{pt('lines.helper'):g}px", "Settings rows, row values, helper text over a group, pop-up and context menu items. The line height is the two-line helper's.", ("type.helper", "type.destructive")),
        "button": ty("type.button", "medium", None, "Labels on capsule buttons (Downloads, Archive, Done, Edit).", ("type.navButton",)),
        "row": ty("type.launcherRow", "regular", None, "Launcher rows, suggestions, history titles, page menu rows.", ("type.rowTitle", "type.menuRow")),
        "sectionHeader": ty("type.section", "semibold", None, "Archive day headers (Today, Yesterday) and a sheet's title (App Icon).", ("type.sheetTitle",)),
        "notice": ty("type.notice", "medium", None, "The first line of the page menu's notice ('Arc scrubbed 5 ads and trackers')."),
        "caption": ty("type.subtitle", "regular", None, "Second lines: a settings row's subtitle, the notice's second line, history URLs.", ("type.noticeSub",)),
        "pill": ty("type.pill", "semibold", None, "Browse for Me button labels."),
        "tileLabel": ty("type.tileLabel", "regular", None, "Labels under the page menu's square buttons (Find on Page, Summarize, Pin, Share)."),
    }
    c["$extensions"] = {"notTokenised": [
        "Glass: launcher, toolbar, page menu, find bar, pop-up and context menus are translucent materials over the page and take its colour; the glass tokens are readings of one moment",
        "Space gradients: each space has its own colour (Main is plum to green); the gradient tokens are Main's",
        "Motion and easing: stills only",
        "Shadows and blur radii of the glass: not measurable from stills",
        "Line heights of one-line labels: only the two-line helper was measured",
    ]}
    return c


# ---------------------------------------------------------------- semantic sets

def semantic(theme):
    f = lambda rid, desc, typ="color": from_reading(rid, theme, typ, desc)
    glass = " A reading of glass over the page: it takes the colour of whatever is behind it."
    s = {"color": {
        "bg": {
            "page": f("bg.page", "Full-screen pages: the Archive and its search. The iOS grouped background."),
            "sheet": f("bg.sheet", "Settings and its sub-pages, a sheet over the browser. Lighter than bg.page in dark, darker in light."),
            "dimmed": f("bg.behindSheet", "The page behind the Settings sheet, darkened (dark) or greyed (light) while the sheet is up. A mean over one moment's page."),
        },
        "surface": {
            "group": f("surface.group", "Grouped list cards and capsule buttons on the Settings sheet: one grey for both."),
            "card": f("surface.card", "Grouped list cards on bg.page (the Archive)."),
            "sheet": f("surface.iconSheet", "A secondary sheet over Settings (App Icon)."),
            "control": f("surface.edit", "Edit capsule in the Archive's nav bar (opaque grey in dark, white glass in light)."),
            "close": f("surface.close", "Round close button in a sheet's header (glass; white with a soft edge in light)."),
        },
        "glass": {
            "navButton": f("surface.navButton", "Done capsule on the Settings sheet." + glass),
            "launcher": f("surface.launcher", "The launcher sheet under the search field." + glass),
            "searchField": f("surface.search", "The launcher's search field, a capsule a step lighter (dark) or darker (light) than the sheet." + glass),
            "pill": f("surface.pill", "Browse for Me buttons on the launcher." + glass),
            "toolbar": f("surface.toolbar", "The bottom toolbar (tabs, +, page menu)." + glass),
            "plus": f("surface.plus", "The + capsule in the toolbar." + glass),
            "menu": f("surface.menu", "The page menu sheet." + glass),
            "panel": f("surface.menuGroup", "Panels inside the page menu (the list, Site Settings)." + glass),
            "address": f("surface.address", "The address bar in the page menu." + glass),
            "tileButton": f("surface.tileButton", "Square buttons in the page menu." + glass),
            "notice": f("surface.notice", "The notice panel at the bottom of the page menu." + glass),
            "findField": f("surface.findField", "The find field in the find bar." + glass),
            "popup": f("surface.popup", "Pop-up menu (Archive Inactive Tabs)." + glass),
            "searchBar": f("surface.searchBar", "Archive search field floating over the list." + glass),
        },
        "border": {
            "separator": f("border.separator", "Hairline between rows of a group, inset to start at the label."),
        },
        "text": {
            "primary": f("text.row", "Row labels, titles, button labels, history titles, suggestions."),
            "secondary": f("text.value", f"Row values ('Google', 'After 7 days'), the typed part of a suggestion, the helper over a group, second lines. Readings in this role: {', '.join(sorted({rd(r, theme)['value'] for r in ('text.value', 'text.typedPrefix', 'text.helper', 'text.subtitle', 'text.rowUrl')}))}."),
            "tertiary": f("text.chevron", "Disclosure chevrons and the pin glyph on a pinned row."),
            "section": f("text.section", "Archive day headers (Today, Yesterday)."),
            "placeholder": f("text.placeholder", "'Search...' in the empty launcher field."),
            "url": f("text.rowUrl", "URL line under a history title."),
            "onAccent": f("text.onAccent", "The tick on the accent confirm button."),
            "onGlass": f("text.notice", "Labels on the page menu's glass panels (light: a dark grey that takes the glass's tint)."),
            "onGlassSecondary": f("text.noticeSub", "Second lines on glass (the notice's 'Problems? Tap to restore original page')."),
            "tileLabel": f("text.tileLabel", "Labels under the page menu's square buttons (white in dark, a muted grey in light)."),
            "findCount": f("text.findCount", "The match count in the find field ('1 of 2')."),
        },
        "accent": {
            "default": f("accent.default", "Arc's blue-violet: the round confirm button in the Archive. Lighter and softer in dark, a saturated blue in light."),
            "check": f("accent.check", "Tick on the chosen row of a choice list (Default Search Engine)."),
            "link": f("accent.link", "Text actions in a list ('Add Search Engine')."),
        },
        "focus": {
            "caret": f("focus.caret", "Text caret in the search field, in the accent colour: the only focus indicator seen. A reading of two pixel columns."),
        },
        "destructive": {
            "text": f("text.destructive", "Destructive menu item ('Remove Favorite') on a glass context menu."),
            "textOnControl": f("text.destructiveEdit", "Destructive action in the Archive's Edit capsule ('Clear All')."),
        },
        "switch": {
            "onTrack": f("switch.onTrack", "Switch on, track: the iOS green."),
            "thumb": f("switch.thumb", "Switch thumb: white in both themes."),
        },
        "space": {
            "top": f("gradient.top", "The Main space's gradient near the top of its sheet (plum). Each space has its own colour."),
            "bottom": f("gradient.bottom", "The Main space's gradient near the bottom (green)."),
            "title": f("text.spaceTitle", "The space's name over its gradient."),
        },
        "status": {
            "danger": alias("color.destructive.text", "color", "Danger: the destructive menu red. No success, warning or info colour appeared."),
        },
    }}
    s["$extensions"] = {"notTokenised": [
        "Switch off: every switch in Arc's settings is on, and none was changed",
        "Success, warning and info colours: no such state was seen",
        "Pressed and disabled states: stills only, and no disabled control appeared",
        "Glass tints: they follow the page behind the glass",
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
             "$description": "Arc Search follows the phone: the owner switched the phone to light mode for the capture on 2026-10-24 and back to dark afterwards. Read from screenshots/light/."},
            {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"},
             "$description": "The phone in dark mode, as the owner keeps it (2026-10-23). Read from screenshots/dark/."},
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
