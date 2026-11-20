#!/usr/bin/env python3
"""Build tokens.json (W3C DTCG, Tokens Studio multi-set layout) from raw/readings.json (native kit).

Copied from systems/grokbot. Adapt core() and semantic(), marked PRODUCT (adapt): they map this
product's readings to roles. Keep the helpers, check() and build().

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
import os
import pathlib
import re

PKG = pathlib.Path(__file__).resolve().parent.parent
_READINGS = PKG / "raw" / "readings.json"
READ = json.loads(_READINGS.read_text()) if _READINGS.exists() else {}  # empty in the kit copy, for its tests
MEASURED = f"raw/{PKG.name}-measured.md"


SCALE = 2   # capture pixels per pt: the iPhone Mirroring stills are 2x, as measure.py reads them


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


def evidence_of(r):
    """A reading's label. A fill reading (it has a share) is a sampled pixel however mixed the box: an
    older readings.json labelled a mixed box Derived."""
    return "Sampled" if r.get("share") is not None else r["evidence"]


def from_reading(rid, theme, typ, desc):
    r = rd(rid, theme)
    note = desc
    evidence = evidence_of(r)
    if r.get("share") is not None:
        if r["share"] < 0.9:
            note += f" The box's dominant colour covers {round(r['share'] * 100)}% of it (a gradient, glass or a thin mark), so it is a reading, not an exact fill."
    return tok(r["value"], typ, note, evidence, r["capture"])


def px(v):
    return f"{v:g}px"


def pt_of(rid, theme="dark", index=0):
    """A number in pt from an extent ('45pt') or bbox ('343x54pt') reading."""
    v = rd(rid, theme)["value"].rstrip("pt")
    return float(v.split("x")[index])


def derived(value, typ, desc, capture=MEASURED):
    return tok(value, typ, desc, "Derived", capture)


def estimated(value, typ, desc, capture=MEASURED):
    """A value judged by eye (a font weight from stroke width): a suggestion, not a reading."""
    return tok(value, typ, desc, "Reconstruction", capture)


def row_pitch(rows):
    """The commonest distance between consecutive row edges of a `find` reading, in pt. Each edge spans
    a pixel or three of anti-aliasing, so a run of adjacent values is one edge."""
    edges, last = [], None
    for y in sorted(rows):
        if last is None or y - last > 3:
            edges.append(y)
        last = y
    gaps = [b - a for a, b in zip(edges, edges[1:])]
    if not gaps:
        raise SystemExit(f"rows.profile: {len(edges)} row edge(s), so no row pitch can be read; widen the reading")
    return max(sorted(set(gaps)), key=gaps.count) / SCALE


def alias(path, typ, desc):
    return tok("{" + path + "}", typ, desc, "Derived", MEASURED)


# ---------------------------------------------------------------- core

PALETTE = [("brown", 2), ("red", 3), ("orange", 4), ("amber", 5), ("green", 6), ("teal", 7),
           ("blue", 8), ("purple", 9), ("pink", 10), ("gray", 11)]


def neutral_ramp():
    """Every grey the semantic sets use, both themes, sorted light to dark. Not a published ramp:
    the steps are the values the app shows, named by order."""
    ids = ["bg.page", "bg.sheet", "surface.card", "surface.bubble", "surface.bubbleDirectLight", "surface.chip",
           "surface.pill", "border.dividerColour", "text.primary", "text.preview", "text.timestamp",
           "text.placeholder", "text.disabled", "switch.off", "switch.onNeutral"]
    seen = {}
    for rid in ids:
        for theme, r in READ[rid].items():
            v = r["value"]
            rr, gg, bb = int(v[1:3], 16), int(v[3:5], 16), int(v[5:7], 16)
            if max(rr, gg, bb) - min(rr, gg, bb) <= 12:     # neutral enough
                seen.setdefault(v, []).append((f"{theme} {rid}", evidence_of(r), r["capture"]))
    lum = lambda h: sum(int(h[i:i + 2], 16) for i in (1, 3, 5))
    rank = ["Sampled", "Sampled (text)", "Derived"]   # the most exact reading of the value wins
    out = {}
    for i, v in enumerate(sorted(seen, key=lum, reverse=True)):
        uses = sorted(set(seen[v]))
        best = min(uses, key=lambda u: rank.index(u[1]))
        listed = ", ".join(f"{name} ({ev})" for name, ev, _ in uses)
        out[f"{i * 50:03d}"] = tok(v, "color", f"Used by: {listed}.", best[1], best[2])
    return out


# PRODUCT (adapt) from here to semantic()'s end: the mapping from readings to tokens.
def core():
    c = {}
    c["color"] = {
        "avatar": {name: from_reading(f"palette.{n}", "dark", "color",
                                      f"Bot avatar colour '{name}', swatch {n} of the Create New Bot palette. The same value in both themes. A bot's avatar, its switches (darkened) and its group-avatar stack use it.")
                   for name, n in PALETTE},
        "neutral": neutral_ramp(),
    }
    c["radius"] = {
        "card": derived("14px", "dimension", f"Grouped cards in settings and on the bot profile, and single-line fields. Diagonal-inset readings: settings card {rd('radius.card')['value']} dark, {rd('radius.card', 'light')['value']} light; profile card {rd('radius.cardProfile')['value']} dark, {rd('radius.cardProfile', 'light')['value']} light; name field {rd('radius.field')['value']}. Plus or minus 2 pt."),
        "field": alias("radius.card", "dimension", "Single-line and multi-line fields share the card radius (text area reads " + rd("radius.textArea")["value"] + ")."),
        "bubble": derived("20px", "dimension", f"Message bubble, first or only bubble from a sender: {rd('radius.bubble')['value']} in both themes, and the owner's bubble {rd('radius.ownBubble')['value']}. Plus or minus 2 pt."),
        "bubbleJoined": derived("8px", "dimension", f"The top corners of a bubble that follows another from the same sender: {rd('radius.bubbleJoined')['value']}. Plus or minus 2 pt."),
        "code": derived("10px", "dimension", f"Code block inside a bubble: {rd('radius.code')['value']}."),
        "menu": derived("30px", "dimension", f"Pull-down and context menus (iOS 26 glass): {rd('radius.menu')['value']}."),
        "sheet": derived("36px", "dimension", f"Top corners of a sheet: {rd('radius.sheet')['value']} dark, {rd('radius.sheet', 'light')['value']} light."),
        "capsule": derived("999px", "dimension", f"Fully round ends: buttons ({rd('radius.button')['value']} on a 42 pt button), chips ({rd('radius.chip')['value']} on 25 pt), the 'Added' button ({rd('radius.secondaryButton')['value']} on 34 pt), the composer ({rd('radius.composer')['value']} on 48 pt), the Edit pill, glass nav buttons and the search bar."),
    }
    pitch = row_pitch(rd("rows.profile")["value"])
    card = rd("size.cardSettings")["box"]
    prof = rd("size.cardProfile")["box"]
    c["space"] = {
        "base": derived("4px", "dimension", "Every measured gap is a multiple of 4 pt within a pixel or two."),
        "xs": derived("4px", "dimension", "Gap between a home-grid avatar and its label, and inside chips."),
        "sm": derived("8px", "dimension", "Gap between stacked bubbles from one sender (about 9 pt edge to edge in dark/07-chat-bubbles)."),
        "md": derived("12px", "dimension", "Padding above the first line of a bubble and between composer controls."),
        "lg": derived("16px", "dimension", f"Screen margin: settings cards start {(card[0] - 16) / 2:g} pt from the screen edge (rim included), bubbles 16.5 pt."),
        "xl": derived("24px", "dimension", f"Bot profile cards' side margin ({(prof[0] - 16) / 2:g} pt) and the gap between grouped cards on that page (24 pt, rows.profile)."),
        "screenMargin": alias("space.lg", "dimension", "Left and right margin of cards, bubbles and the home grid."),
    }
    c["size"] = {
        "row": tok(px(pitch), "dimension", "Single-line grouped row (bot profile rows, settings rows), divider to divider.", "Sampled", rd("rows.profile")["capture"]),
        "rowTwoLine": derived("70px", "dimension", "Grouped row with a subtitle (Connect apps, Auto-review): about 70 pt in dark/19-account-menu."),
        "navButton": tok(px(pt_of("size.navButton.w")), "dimension", "Round glass back, close and more buttons (a circle). The reading includes the glass rim's soft edge; the touch target is at least this.", "Sampled", rd("size.navButton.w")["capture"]),
        "searchBar": tok(px(round(pt_of("size.searchBar.h"))), "dimension", "Height of the home search bar (glass capsule).", "Sampled", rd("size.searchBar.h")["capture"]),
        "composer": tok(px(pt_of("size.composer.h")), "dimension", "Height of the composer field (glass capsule).", "Sampled", rd("size.composer.h")["capture"]),
        "composerButton": tok(px(pt_of("size.composerPlus.w")), "dimension", "The round + button beside the composer.", "Sampled", rd("size.composerPlus.w")["capture"]),
        "sendButton": {
            "width": tok(px(pt_of("size.sendButton.w")), "dimension", "Send and voice buttons inside the composer: a pill, not a circle.", "Sampled", rd("size.sendButton.w")["capture"]),
            "height": tok(px(pt_of("size.sendButton.h")), "dimension", "Send and voice buttons inside the composer.", "Sampled", rd("size.sendButton.h")["capture"]),
        },
        "button": tok(px(round(pt_of("size.button", "dark", 1))), "dimension", f"Full-width primary button (Create, Send Feedback): {rd('size.button')['value']} in dark.", "Sampled", rd("size.button")["capture"]),
        "field": derived("52px", "dimension", f"Single-line field height: {rd('size.field')['value']} dark (rim included), {rd('size.field', 'light')['value']} light."),
        "pill": tok(px(round(pt_of("size.pill", "dark", 1))), "dimension", f"Small secondary pill (Edit): {rd('size.pill')['value']}.", "Sampled", rd("size.pill")["capture"]),
        "chip": tok(px(pt_of("size.chip", "dark", 1)), "dimension", f"Account chip with a tick: {rd('size.chip')['value']}.", "Sampled", rd("size.chip")["capture"]),
        "secondaryButton": tok(px(pt_of("size.secondaryButton", "dark", 1)), "dimension", f"Inline Add or Added button in a list row: {rd('size.secondaryButton')['value']}.", "Sampled", rd("size.secondaryButton")["capture"]),
        "switch": {
            "width": tok(px(pt_of("size.switch")), "dimension", "Switch track, anti-aliased edge excluded.", "Sampled", rd("size.switch")["capture"]),
            "height": tok(px(round(pt_of("size.switch", "dark", 1))), "dimension", f"Switch track height ({rd('size.switch')['value']}).", "Sampled", rd("size.switch")["capture"]),
            "thumb": tok(px(pt_of("size.switchThumb")), "dimension", f"Switch thumb width (a pill {rd('size.switchThumb')['value']}).", "Sampled", rd("size.switchThumb")["capture"]),
        },
        "swatch": tok(px(pt_of("size.swatch")), "dimension", "Colour swatch in the avatar picker.", "Sampled", rd("size.swatch")["capture"]),
        "avatarGrid": derived("88px", "dimension", f"Home-grid bot avatar. The shapes differ, so their boxes do: {rd('size.avatarGrid')['value']} (heart), {rd('size.avatarGridB')['value']} (star)."),
        "menuWidth": tok(px(round(pt_of("size.menu.w"))), "dimension", f"Pull-down menu width ({rd('size.menu.w')['value']}); two items make it {rd('size.menu.h')['value']} tall.", "Sampled", rd("size.menu.w")["capture"]),
        "bubbleMaxWidth": tok(px(pt_of("size.bubbleDirect", "dark")), "dimension", f"The widest one-to-one bubble ({rd('size.bubbleDirect')['value']}), 16 pt from the left edge. Group bubbles sit after a 24 pt avatar column and reach {rd('size.bubbleGroup')['value'].split('x')[0]} pt.", "Sampled", rd("size.bubbleDirect")["capture"]),
        "touchTarget": derived("44px", "dimension", "The nav buttons, rows and composer controls are 44 pt or more. Chips (25 pt), the Edit pill and the send pill (32 pt) are smaller and sit inside larger rows or fields."),
    }
    c["border"] = {"width": {
        "hairline": derived("0.5px", "dimension", "Dividers between grouped rows: one device pixel at 2x (border.dividerColour reads a one-pixel row)."),
        "rim": derived("0.5px", "dimension", "The rim around grouped cards and fields (border.card), one device pixel."),
    }}
    c["fontFamily"] = {"base": tok("system", "fontFamily", "Not determinable from pixels. The letterforms are a neo-grotesque close to the iOS system face; use the platform font.", "Not captured", MEASURED)}
    c["fontWeight"] = {
        "regular": estimated(400, "fontWeight", "Body text, settings rows, previews. Judged by stroke width, not measured."),
        "medium": estimated(500, "fontWeight", "Home row titles and nav titles. Judged by stroke width."),
        "semibold": estimated(600, "fontWeight", "The bot name on its profile and the primary button label. Judged by stroke width."),
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
        "titleLarge": ty("type.profileTitle", "semibold", None, "The bot's name on its profile."),
        "fieldLarge": ty("type.fieldText", "regular", None, "Text typed into the Create New Bot name field, centred.", ("type.fieldText",)),
        "body": ty("type.bubble", "regular", lines("lines.bubble"), "Bubble text, settings rows, sheet titles, empty-state lines.", ("type.settingsRow", "type.sheetTitle", "type.emptyState")),
        "rowTitle": ty("type.rowTitle", "medium", None, "Home list row titles and nav bar titles.", ("type.navTitle",)),
        "button": ty("type.button", "semibold", None, "Full-width button label (Create)."),
        "callout": ty("type.composer", "regular", None, "Composer placeholder, menu items, the unread pill.", ("type.menuItem",)),
        "preview": ty("type.preview", "regular", None, "Home row preview line and folder names."),
        "subheadline": ty("type.subtitle", "regular", lines("lines.subtitle"), "Row subtitles, home-grid labels, section headers, thread system lines, the 'Added' label.", ("type.gridLabel", "type.sectionHeader", "type.systemLine")),
        "footnote": ty("type.footnote", "regular", lines("lines.footnote"), "Helper text under cards, row timestamps.", ("type.timestamp",)),
        "caption": ty("type.senderLabel", "regular", None, "Sender label above a group bubble."),
    }
    c["$extensions"] = {"notTokenised": [
        "iOS 26 glass (nav buttons, menus, the composer, the search bar): blur and refraction come from the system material",
        "Continuous (squircle) corners: DTCG has no value for corner smoothing",
        "Motion and easing: stills only",
        "Shadows: none drawn; separation comes from fills, rims and the glass material",
        "Line heights of titles and one-line labels: only multi-line blocks were measured",
    ]}
    return c


# ---------------------------------------------------------------- semantic sets

def scrim(theme):
    ref, dim = rd("scrim.ref", theme)["value"], rd("scrim.context", theme)["value"]
    a = 1 - int(dim[1:3], 16) / int(ref[1:3], 16)
    return derived("#000000%02X" % round(a * 255), "color",
                   f"Black at {round(a * 100)}%: the home screen reads {ref} undimmed and {dim} under a context menu (a sheet dims it to {rd('scrim.sheet', theme)['value']}).",
                   rd("scrim.context", theme)["capture"])


def dark_only(theme, rid, desc, light_from=None, why=""):
    """A role read in dark only. Light reuses the dark value (light_from None) or the light value of
    the closest role, as Derived, and says which."""
    if theme == "dark":
        return from_reading(rid, "dark", "color", desc)
    src = rd(light_from, "light") if light_from else rd(rid, "dark")
    return derived(src["value"], "color", desc + " Not captured in light: " + why, src["capture"])


def semantic(theme):
    f = lambda rid, desc, typ="color": from_reading(rid, theme, typ, desc)
    other = "light" if theme == "dark" else "dark"
    bubble_direct = "surface.bubbleDirect" if theme == "dark" else "surface.bubbleDirectLight"
    s = {"color": {
        "bg": {
            "page": f("bg.page", "Home, chat threads and search results."),
            "sheet": f("bg.sheet", "Sheets (Settings, Create New Bot) and pushed detail pages (Routines, bot profile, Usage)."),
            "scrim": scrim(theme),
        },
        "surface": {
            "card": f("surface.card", "Grouped cards, single-line fields and the text area."),
            "field": f("surface.field", "Single-line field fill; the same value as the card."),
            "bubble": f("surface.bubble", "Bot message bubble in a group chat."),
            "bubbleDirect": f(bubble_direct, "Bot message bubble in a one-to-one chat." + (" A warm grey in dark, not the group bubble's neutral." if theme == "dark" else "")),
            "ownBubble": dark_only(theme, "surface.ownBubble", "The owner's own message bubble: the bot's avatar colour darkened to about 77% (amber #FF9700 gives #C37300), the same rule as switch.onBot.", None, "the bubble follows the bot colour, and switch.onBot, made by the same rule, reads the same in both themes, so the dark value is used."),
            "code": dark_only(theme, "surface.code", "Code block inside a bot bubble, with a copy button at its top right.", "surface.chip", "filled from surface.secondary, the closest light role."),
            "secondary": f("surface.chip", "Chips and inline secondary buttons (Added, Add)."),
            "tertiary": f("surface.pill", "The Edit pill on a bot profile."),
            "glass": f("surface.composer", "Glass controls (composer field, nav buttons, search bar), centre reading. The material tints with whatever is behind it."),
            "menu": f("surface.menu", "Pull-down and context menus (glass). The reading picks up the avatars behind the menu."),
        },
        "border": {
            "divider": f("border.dividerColour", "Hairline between grouped rows, inset to the row text."),
            "card": f("border.card", "Rim around grouped cards and fields: lighter than the card in dark, darker in light."),
        },
        "text": {
            "primary": f("text.primary", "Titles, row titles, bubble text, settings labels."),
            "secondary": f("text.preview", f"Previews, grid labels, row values and subtitles, sender labels. Readings in this role range {', '.join(sorted({rd(r, theme)['value'] for r in ('text.preview', 'text.gridLabel', 'text.rowValue', 'text.rowSubtitle', 'text.senderLabel', 'text.systemLine')}))}."),
            "tertiary": f("text.timestamp", f"Timestamps, section headers, folder counts, helper text, field labels. Readings range {', '.join(sorted({rd(r, theme)['value'] for r in ('text.timestamp', 'text.sectionHeader', 'text.folderCount', 'text.footnote', 'text.fieldLabel', 'text.systemTime')}))}."),
            "placeholder": f("text.placeholder", f"Field and composer placeholders (composer reads {rd('text.composerPlaceholder', theme)['value']})."),
            "disabled": f("text.disabled", "Label of a disabled inline button (Added)."),
            "onOwnBubble": dark_only(theme, "text.onOwnBubble", "Text on the owner's coloured bubble.", None, "the dark value is used, as for surface.ownBubble."),
            "code": dark_only(theme, "text.code", "Monospace text in a code block.", "text.preview", "filled from text.secondary, the closest light role."),
            "link": f("text.link", "Inline links in bubbles (with a cube icon for internal objects)."),
            "onAccent": f("text.onPill", "Label on the blue unread pill."),
            "danger": f("text.destructive", "Destructive menu items (Delete, Hide) and Sign Out: red text, never a red fill."),
            "success": f("text.success", "Tick on a connected-account chip."),
        },
        "accent": {
            "default": f("accent.dot", "Unread dots and the update dot. The app's only system accent; a bot's own colour takes over its switches."),
            "pill": f("accent.pill", "The floating 'N unread' pill (glass over blue)."),
        },
        "focus": {
            "caret": f("accent.caret", "Text caret in a focused field: the only focus indicator (no ring)."),
        },
        "button": {
            "primary": {"bg": f("button.primary", "Full-width primary button, enabled: white in dark, near-black in light."),
                        "text": f("button.primaryLabel", "Primary button label.")},
            "primaryDisabled": {"bg": f("button.disabled", "Primary button, disabled (glass)."),
                                "text": f("button.disabledLabel", "Disabled primary button label.")},
            "secondary": {"bg": f("button.secondary", "Inline secondary button (Add): the secondary surface."),
                          "text": f("button.secondaryLabel", "Inline secondary button label, enabled.")},
            "send": {"bg": f("button.send", "Send and voice pills inside the composer: the inverse of the theme."),
                     "glyph": f("button.sendGlyph", "Arrow and waveform glyphs on them.")},
        },
        "switch": {
            "on": f("switch.onNeutral", "Switch on, app-wide settings (Auto-review, time zone)."),
            "onBot": f("switch.onBot", "Switch on, on a bot's own pages: the bot's avatar colour darkened to about 77% (purple #9158FE gives #6F44C3). Settings > Appearance > Bot color turns this on."),
            "off": f("switch.off", "Switch off track."),
            "thumb": f("switch.thumb", "Switch thumb, both states."),
        },
        "avatar": {
            "ink": f("palette.1", "First swatch of the avatar palette: the theme's ink (white in dark, black in light)."),
            "eye": f("avatar.eye", "A bot's eyes are cut-outs that show the page colour."),
        },
        "badge": {
            "star": f("badge.star", "Star badge on a pinned bot: the amber avatar colour."),
        },
        "status": {
            "success": alias("color.text.success", "color", "Success: the connected-account tick. No success fill or border was seen."),
            "danger": alias("color.text.danger", "color", "Danger: red text on destructive items. No danger fill was seen."),
            "info": alias("color.accent.default", "color", "Info: the blue accent (unread, update available)."),
        },
    }}
    s["$extensions"] = {"notTokenised": [
        "Warning colour: no warning state was seen",
        "Pressed states: stills only",
        "Per-bot accent: every bot's switches take its own avatar colour; only the purple bot's was read",
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


class CheckError(AssertionError):
    """A tokens file check() rejects. Raised explicitly, not by `assert`, so the
    check still runs under `python3 -O`; an AssertionError for older callers."""


def require(ok, message):
    if not ok:
        raise CheckError(message)


def check(doc):
    sets = [s for s in ("core", "light", "dark") if s in doc]  # a one-theme app has no light or no dark
    paths = {".".join(p) for name in sets for p, _ in walk(doc[name])}
    for name in sets:
        for p, t in walk(doc[name]):
            where = name + "." + ".".join(p)
            src = t.get("$extensions", {}).get("source", {})
            require(src.get("evidence") and src.get("capture"), f"{where}: no source")
            v = t["$value"]
            for a in aliases(v):
                require(a in paths, f"{where}: alias {{{a}}} points at nothing")
            if isinstance(v, str) and v.startswith("{"):
                continue
            elif t["$type"] == "color":
                require(re.fullmatch(r"#[0-9A-F]{6}([0-9A-F]{2})?", v), f"{where}: bad colour {v}")
            elif t["$type"] == "dimension":
                require(re.fullmatch(r"-?\d+(\.\d+)?px", v), f"{where}: bad dimension {v}")
    keys = lambda s: sorted(".".join(p) for p, _ in walk(doc[s]))
    if "light" in doc and "dark" in doc:
        require(keys("light") == keys("dark"), "light and dark keys differ")


def build():
    doc = {
        "core": core(),
        "light": semantic("light"),
        "dark": semantic("dark"),
        "$themes": [  # PRODUCT (adapt): how each theme was set for the capture; drop a theme the app lacks
            {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"},
             "$description": "Settings > Appearance > Light, set for the capture and put back afterwards. Read from screenshots/light/."},
            {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"},
             "$description": "Settings > Appearance > Follow System with the phone in dark mode. Read from screenshots/dark/."},
        ],
        "$metadata": {"tokenSetOrder": ["core", "light", "dark"]},
    }
    check(doc)
    (PKG / "tokens.json").write_text(json.dumps(doc, indent=1, ensure_ascii=False) + "\n")
    n = sum(1 for s in ("core", "light", "dark") for _ in walk(doc[s]))
    print(f"tokens.json: {n} tokens")


# PRODUCT (adapt): name the product here once every part marked PRODUCT (adapt) is rewritten
# for it. While this is None the script stops when run: the kit's copy is Grok Bot's example and
# would write Grok Bot's values. KIT_EXAMPLE=1 runs the example as it is.
ADAPTED_FOR = None

if __name__ == "__main__":
    if ADAPTED_FOR is None and not os.environ.get("KIT_EXAMPLE"):
        raise SystemExit("build_tokens.py is the kit's Grok Bot example, not adapted: rewrite the parts marked PRODUCT (adapt), then set ADAPTED_FOR")
    if not READ:
        raise SystemExit("no raw/readings.json: run tools/measure.py first")
    build()
