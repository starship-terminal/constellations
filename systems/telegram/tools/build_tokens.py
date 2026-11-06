#!/usr/bin/env python3
"""Build tokens.json (W3C DTCG, Tokens Studio multi-set layout) from raw/readings.json (native kit).

Copied from the native kit (tools/kit/native, from systems/grokbot); core() and semantic() map
Telegram's readings to roles. The helpers, check() and build() are the kit's.

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

TILES = ["blue", "green", "orange", "violet", "pink", "red", "purple", "grey"]
AVATARS = ["red", "orange", "green", "blue", "purple"]


def neutral_ramp():
    """Every grey the semantic sets use, both themes, sorted light to dark. Not a published ramp:
    the steps are the values the app shows, named by order."""
    ids = ["bg.chats", "bg.pinned", "bg.grouped", "bg.groupedAlt", "surface.card", "surface.cardAlt", "surface.search",
           "surface.tabSelected", "border.divider", "border.dividerList", "text.primary", "text.secondary", "text.value",
           "text.footnote", "text.chatPreview", "text.placeholder", "switch.off", "badge.count"]
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


def pitch(rid, theme="dark"):
    """The row height in pt: the most common distance, 30 to 100 pt, between any two pixels found
    down a list. Dividers repeat at the row pitch; a text pixel of the same grey does not."""
    found = rd(rid, theme)["value"]
    gaps = [b - a for i, a in enumerate(found) for b in found[i + 1:] if 60 <= b - a <= 200]
    return max(sorted(set(gaps)), key=gaps.count) / 2


def bbox(rid, index, theme="dark"):
    return pt_of(rid, theme, index)


# PRODUCT (adapt) from here to semantic()'s end: the mapping from readings to tokens.
def core():
    c = {}
    c["color"] = {
        "iconTile": {name: from_reading(f"tile.{name}", "dark", "color",
                                        f"Settings icon tile, {name}. The tiles are gradients, lighter at the top; this is a 10 x 3 px band beside the glyph, so it is one colour along the gradient. The same tiles appear in both themes.")
                     for name in TILES},
        "avatar": {name: from_reading(f"avatar.{name}", "dark", "color",
                                      f"Initials avatar for a contact with no photo, {name}. Gradients too: a band beside the letter.")
                   for name in AVATARS},
        "neutral": neutral_ramp(),
    }
    c["radius"] = {
        "card": derived("26px", "dimension", f"Grouped cards in settings, both page styles: diagonal-inset readings {rd('radius.card')['value']} (Privacy and Security) and {rd('radius.cardAlt')['value']} (Chat Folders) in both themes. Plus or minus 2 pt."),
        "bubble": derived("16px", "dimension", f"Message bubble corner away from the tail: {rd('radius.bubble')['value']} dark, {rd('radius.bubble', 'light')['value']} light. Plus or minus 2 pt."),
        "iconTile": derived("8px", "dimension", f"Settings icon tile: {rd('radius.iconTile')['value']} on a 30 pt tile."),
        "menu": derived("30px", "dimension", f"Context and pull-down menus (iOS 26 glass): {rd('radius.menu')['value']} dark, {rd('radius.menu', 'light')['value']} light."),
        "sheet": derived("36px", "dimension", f"Top corners of a sheet (attachment sheet): {rd('radius.sheet')['value']}."),
        "capsule": derived("999px", "dimension", f"Fully round ends: the accent button ({rd('radius.button')['value']} on a 50 pt button), search fields ({rd('radius.search')['value']} on 44 pt), the tab bar ({rd('radius.tabBar')['value']} on 64 pt), folder chips, the segmented control, glass nav buttons and the ADD pill."),
    }
    card = rd("size.button")["box"]
    c["space"] = {
        "base": derived("4px", "dimension", "Measured gaps land on multiples of 4 pt within a pixel or two."),
        "xs": derived("4px", "dimension", "Gap between a row title and its subtitle."),
        "sm": derived("8px", "dimension", "Gap between folder chips and inside the selected tab pill."),
        "md": derived("12px", "dimension", "Gap between a row's icon tile or avatar and its text column."),
        "lg": derived("16px", "dimension", f"Screen margin: grouped cards and the accent button start {(card[0] - 16 - 1) / 2:g} pt from the screen edge (the box is measured from its first full pixel); row text inside a card sits 16 pt in."),
        "xl": derived("24px", "dimension", "Gap between grouped cards with no header between them (Settings root)."),
        "screenMargin": alias("space.lg", "dimension", "Left and right margin of cards, the search field, the chip bar and the accent button."),
    }
    navw = pt_of("size.navButton.w")
    c["size"] = {
        "row": tok(px(pitch("rows.grouped")), "dimension", "One-line grouped row (Privacy and Security), divider to divider.", "Sampled", rd("rows.grouped")["capture"]),
        "rowTwoLine": tok(px(pitch("rows.groupedTwoLine")), "dimension", "Grouped row with a subtitle (Notifications), divider to divider.", "Sampled", rd("rows.groupedTwoLine")["capture"]),
        "rowChat": tok(px(pitch("rows.chats")), "dimension", "Chat list row: 60 pt avatar, title, two preview lines, time and pin. The same in both themes.", "Sampled", rd("rows.chats")["capture"]),
        "rowCall": tok(px(pitch("rows.calls")), "dimension", "Calls list row.", "Sampled", rd("rows.calls")["capture"]),
        "rowContact": tok(px(pitch("rows.contacts")), "dimension", "Contacts list row (name and presence).", "Sampled", rd("rows.contacts")["capture"]),
        "navButton": tok(px(round(navw)), "dimension", f"Round glass back and action buttons: {rd('size.navButton.w')['value']} wide, {rd('size.navButton.h')['value']} tall dark, {rd('size.navButton.w', 'light')['value']} wide light, rim included.", "Sampled", rd("size.navButton.w")["capture"]),
        "search": tok(px(round(pt_of("size.search.h", "light"))), "dimension", f"Search field height: {rd('size.search.h')['value']} dark, {rd('size.search.h', 'light')['value']} light.", "Sampled", rd("size.search.h", "light")["capture"]),
        "chipBar": tok(px(pt_of("size.chipBar.h")), "dimension", "Height of the glass bar holding the folder chips.", "Sampled", rd("size.chipBar.h")["capture"]),
        "chip": tok(px(bbox("size.chipSelected", 1)), "dimension", f"Folder chip height ({rd('size.chipSelected')['value']} for 'All').", "Sampled", rd("size.chipSelected")["capture"]),
        "tabBar": {
            "height": tok(px(pt_of("size.tabBar.h")), "dimension", "Floating glass tab bar (Contacts, Calls, Chats, Settings).", "Sampled", rd("size.tabBar.h")["capture"]),
            "width": tok(px(pt_of("size.tabBar.w")), "dimension", "Tab bar width: it floats with about 20 pt each side.", "Sampled", rd("size.tabBar.w")["capture"]),
            "itemWidth": tok(px(pt_of("size.tabSelected.w")), "dimension", "The selected tab's pill, width.", "Sampled", rd("size.tabSelected.w")["capture"]),
            "itemHeight": tok(px(pt_of("size.tabSelected.h")), "dimension", "The selected tab's pill, height.", "Sampled", rd("size.tabSelected.h")["capture"]),
        },
        "segmented": {
            "width": tok(px(pt_of("size.segmented")), "dimension", "Segmented control in the Calls nav bar (All / Missed).", "Sampled", rd("size.segmented")["capture"]),
            "height": tok(px(pt_of("size.segmented.h")), "dimension", "Segmented control height.", "Sampled", rd("size.segmented.h")["capture"]),
        },
        "button": tok(px(round(bbox("size.button", 1))), "dimension", f"Full-width accent button (Add Device): {rd('size.button')['value']} dark, {rd('size.button', 'light')['value']} light.", "Sampled", rd("size.button")["capture"]),
        "pill": tok(px(round(bbox("size.pill", 1))), "dimension", f"Small accent pill in a row (ADD): {rd('size.pill')['value']}.", "Sampled", rd("size.pill")["capture"]),
        "switch": {
            "width": tok(px(bbox("size.switch", 0)), "dimension", f"Switch track ({rd('size.switch')['value']}), anti-aliased edge excluded.", "Sampled", rd("size.switch")["capture"]),
            "height": tok(px(bbox("size.switch", 1)), "dimension", "Switch track height.", "Sampled", rd("size.switch")["capture"]),
            "thumb": tok(px(bbox("size.switchThumb", 0)), "dimension", f"Switch thumb width (a pill, {rd('size.switchThumb')['value']}).", "Sampled", rd("size.switchThumb")["capture"]),
        },
        "iconTile": derived("30px", "dimension", f"Settings icon tile: {rd('size.iconTile')['value']} including a pixel of anti-aliasing at each end."),
        "avatarChat": tok(px(pt_of("size.avatarChat")), "dimension", "Chat list avatar (a circle; forum groups use a rounded square of the same size).", "Sampled", rd("size.avatarChat")["capture"]),
        "avatarList": tok(px(pt_of("size.avatarList")), "dimension", f"Calls list avatar ({rd('size.avatarList')['value']}); contacts read {rd('size.avatarContact')['value']}, anti-aliasing included.", "Sampled", rd("size.avatarList")["capture"]),
        "send": {
            "width": tok(px(bbox("size.send", 0)), "dimension", f"Send button inside the composer: a pill {rd('size.send')['value']}.", "Sampled", rd("size.send")["capture"]),
            "height": tok(px(bbox("size.send", 1)), "dimension", "Send button height.", "Sampled", rd("size.send")["capture"]),
        },
        "touchTarget": derived("44px", "dimension", "Nav buttons, rows, chips and the tab pills are 36 pt or more tall; the 44 pt target is the platform rule, met by rows and nav buttons. The ADD pill (27 pt) sits inside a 72 pt row."),
    }
    c["border"] = {"width": {
        "hairline": derived("0.5px", "dimension", "Dividers between rows: one device pixel at 2x, with one pixel of anti-aliasing beside it."),
    }}
    c["fontFamily"] = {"base": tok("system", "fontFamily", "Not determinable from pixels. The letterforms match the iOS system face (SF Pro) closely; use the platform font.", "Not captured", MEASURED)}
    c["fontWeight"] = {
        "regular": derived(400, "fontWeight", "Row titles, subtitles, previews, bubble text, menu items. Judged by stroke width, not measured."),
        "medium": derived(500, "fontWeight", "Tab labels, folder chips and segment labels. Judged by stroke width."),
        "semibold": derived(600, "fontWeight", "Navigation titles, chat titles, the accent button label, the profile name. Judged by stroke width."),
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
        "profileName": ty("type.profileName", "semibold", None, "The owner's name on the Settings root, read from the ascender of a lowercase k, which sits a little above cap height."),
        "navTitle": ty("type.navTitle", "semibold", None, "Navigation titles (Notifications, Chats, Contacts) and the accent button label.", ("type.button",)),
        "body": ty("type.rowTitle", "regular", None, "Settings and list row titles, menu items.", ("type.menuItem",)),
        "bubble": ty("type.bubble", "regular", None, "Message text in a bubble (Appearance preview)."),
        "chatTitle": ty("type.chatTitle", "semibold", None, "Chat list row titles."),
        "subheadline": ty("type.rowSubtitle", "regular", lines("lines.chatPreview"), "Row subtitles, chat previews (two lines), folder chips, segment labels.", ("type.chatPreview", "type.chip", "type.segmented")),
        "quote": ty("type.quote", "regular", lines("lines.quote"), "A link preview's description inside a bubble."),
        "footnote": ty("type.footnote", "regular", lines("lines.footnote"), "Footnotes under cards and section headers (upper case).", ("type.sectionHeader",)),
        "caption": ty("type.tab", "medium", None, "Tab bar labels and the time inside a bubble.", ("type.bubbleMeta",)),
    }
    c["$extensions"] = {"notTokenised": [
        "iOS 26 glass (nav buttons, the tab bar, the chip bar, the segmented control, menus, the composer): blur and refraction come from the system material",
        "Gradients: outgoing bubbles in dark, icon tiles and initials avatars are gradients; each token is one reading along it",
        "Chat wallpapers: a photo or pattern chosen per chat or theme; the dark captures show the owner's photo, the light ones Telegram's pattern",
        "Continuous (squircle) corners: DTCG has no value for corner smoothing",
        "Motion and easing: stills only",
        "Line heights of one-line labels: only multi-line blocks were measured",
    ]}
    return c


# ---------------------------------------------------------------- semantic sets

def dark_only(theme, rid, desc, light_from=None, why=""):
    """A role read in dark only. Light reuses the dark value (light_from None) or the light value of
    the closest role, as Derived, and says which."""
    if theme == "dark":
        return from_reading(rid, "dark", "color", desc)
    src = rd(light_from, "light") if light_from else rd(rid, "dark")
    return derived(src["value"], "color", desc + " Not captured in light: " + why, src["capture"])


def semantic(theme):
    f = lambda rid, desc, typ="color": from_reading(rid, theme, typ, desc)
    s = {"color": {
        "bg": {
            "chats": f("bg.chats", "Chat list, calls, contacts and search results."),
            "pinned": f("bg.pinned", "Band behind the pinned chats at the top of the list (and the header above them)."),
            "grouped": f("bg.grouped", "Grouped settings pages (Settings root, Notifications, Privacy, Devices)."),
            "groupedAlt": f("bg.groupedAlt", "Chat Folders: a second grouped style whose page is grey in dark, with lighter cards."),
            "sheet": dark_only(theme, "bg.sheet", "Attachment sheet over the chat.", "surface.card", "filled from surface.card, the light card white."),
        },
        "surface": {
            "card": f("surface.card", "Grouped cards on bg.grouped."),
            "cardAlt": f("surface.cardAlt", "Grouped cards on bg.groupedAlt."),
            "search": f("surface.search", "Search fields (Contacts, New Message, the chat list in light)."),
            "glass": f("surface.glassButton", "Round glass nav buttons (back, Edit, compose's neighbours), centre reading. The material tints with what is behind it."),
            "chipBar": f("surface.chipBar", "Glass bar holding the folder chips."),
            "chipSelected": f("surface.chipSelected", "The selected folder chip inside the bar."),
            "tabBar": f("surface.tabBar", "Floating glass tab bar."),
            "tabSelected": f("surface.tabSelected", "Pill behind the selected tab."),
            "segmented": f("surface.segmented", "Segmented control track (glass)."),
            "segmentedSelected": f("surface.segmentedSelected", "The selected segment."),
            "menu": f("surface.menu", "Context menu (glass over the blurred chat; it takes the chat's colours)."),
            "menuPlain": dark_only(theme, "surface.menuSort", "Pull-down menu over a plain list (Contacts > Sort): glass over black reads as a flat grey.", "surface.card", "filled from surface.card."),
            "reactions": f("surface.reactions", "Reaction bar above a long-pressed message (glass)."),
            "bubbleIn": f("surface.bubbleIn", "Incoming message bubble, from the theme preview. In dark it is translucent over the wallpaper."),
            "bubbleOut": f("surface.bubbleOut", "Outgoing message bubble, top. Dark: a violet-to-blue gradient; light: a flat pale green."),
            "bubbleOutEnd": f("surface.bubbleOutEnd", "Outgoing message bubble, bottom: the gradient's end in dark, the same green in light."),
            "quote": f("surface.quote", "Link preview card inside an outgoing bubble, with a bar on its left edge."),
            "service": f("surface.service", "Service message pills (topic created, date) over the wallpaper: translucent, so the reading depends on the wallpaper."),
            "composer": f("surface.composer", "Composer field (glass over the wallpaper)."),
        },
        "border": {
            "divider": f("border.divider", "Hairline between grouped rows, inset to the row text."),
            "list": f("border.dividerList", "Hairline between chat, call and contact rows, inset past the avatar."),
        },
        "text": {
            "primary": f("text.primary", "Row titles, chat titles, nav titles, bubble text."),
            "secondary": f("text.secondary", "Row subtitles ('173 exceptions')."),
            "value": f("text.value", "Values at the end of a row ('My Contacts', 'On')."),
            "sectionHeader": f("text.sectionHeader", "Upper-case section headers above cards."),
            "footnote": f("text.footnote", "Footnotes under cards."),
            "preview": f("text.chatPreview", "Chat list preview lines."),
            "time": f("text.chatTime", "Times and dates in list rows."),
            "placeholder": f("text.placeholder", "Search field placeholder and magnifier."),
            "link": f("text.link", "Accent text actions (Change Profile Photo, Create a Folder, Start New Call, Invite Friends)."),
            "online": f("text.online", "Presence when online, in the accent colour."),
            "username": dark_only(theme, "text.username", "Usernames in global search results.", "text.online", "filled from text.online, the same accent."),
            "danger": f("text.danger", "Destructive rows (Terminate all other sessions): red text, never a red fill."),
            "dangerMenu": f("text.dangerMenu", "Destructive menu items (Delete), over glass."),
            "missed": f("text.missed", "A missed call's name in the calls list."),
            "onAccent": f("text.onAccent", "Label on the accent button."),
            "disabled": dark_only(theme, "text.disabled", "Label of a disabled row (Night Mode while Auto-Night is on).", "text.secondary", "the light pass had Auto-Night off, so Night Mode was enabled; filled from text.secondary."),
            "disabledAction": dark_only(theme, "text.disabledAction", "Disabled bottom actions in edit mode (Read All, Archive, Delete with nothing selected).", "text.secondary", "edit mode was captured in dark only; filled from text.secondary."),
            "onBubbleOut": f("text.onBubbleOut", "Text in an outgoing bubble."),
            "bubbleMeta": f("text.bubbleMeta", "Time and ticks inside an outgoing bubble."),
            "bubbleLink": f("text.bubbleLink", "A link in an outgoing bubble (underlined white in dark, blue in light)."),
            "quoteTitle": f("text.quoteTitle", "Site name on a link preview, in the bubble's accent."),
            "service": f("text.service", "Text on service message pills."),
            "tab": f("text.tab", "Unselected tab labels and icons."),
            "tabSelected": f("text.tabSelected", "Selected tab label and icon."),
            "readMark": f("text.readMark", "Read ticks beside a chat row time (blue in dark, green in light)."),
        },
        "accent": {
            "default": f("accent.button", "The accent: filled buttons, links, the selected tab, checkmarks, the caret. Telegram blue, lighter in dark."),
            "compose": f("accent.compose", "The round compose button in the chat list header (accent glass)."),
            "send": f("accent.send", "Send button in the composer."),
            "pill": f("accent.pill", "Small accent pill in a row (ADD)."),
            "check": f("accent.check", "Checkmark on the chosen row of a choice list."),
        },
        "focus": {
            "caret": f("accent.caret", "Text caret in a focused field: the only focus indicator (no ring)."),
        },
        "switch": {
            "on": f("switch.on", "Switch on."),
            "off": f("switch.off", "Switch off track. Very pale in light."),
            "thumb": f("switch.thumb", "Switch thumb, both states."),
            "offDisabled": dark_only(theme, "switch.offDisabled", "Switch off and disabled (Night Mode while Auto-Night is on).", "switch.off", "filled from switch.off."),
            "thumbDisabled": dark_only(theme, "switch.thumbDisabled", "Thumb of a disabled switch, dimmed.", "switch.thumb", "filled from switch.thumb."),
        },
        "badge": {
            "muted": f("badge.count", "Muted count badge (a folder chip's unread count, the archive's count)."),
        },
        "icon": {
            "secondary": f("icon.secondary", "Secondary glyphs in rows (pin, mute)."),
        },
        "status": {
            "success": alias("color.switch.on", "color", "Success: the green of an on switch. No success message was seen."),
            "danger": alias("color.text.danger", "color", "Danger: red text on destructive rows and items. No danger fill was seen."),
            "info": alias("color.accent.default", "color", "Info: the accent."),
        },
    }}
    s["$extensions"] = {"notTokenised": [
        "Warning colour: no warning state was seen",
        "Pressed states: stills only",
        "Unread badges: every chat in the captures was read, so no accent (unmuted) unread badge appears",
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


class CheckError(ValueError):
    """A token file check() rejects. Raised explicitly so the check still runs under python3 -O."""


def check(doc):
    sets = [s for s in ("core", "light", "dark") if s in doc]  # a one-theme app has no light or no dark
    paths = {".".join(p) for name in sets for p, _ in walk(doc[name])}
    for name in sets:
        for p, t in walk(doc[name]):
            where = name + "." + ".".join(p)
            src = t.get("$extensions", {}).get("source", {})
            if not (src.get("evidence") and src.get("capture")):
                raise CheckError(f"{where}: no source")
            v = t["$value"]
            for a in aliases(v):
                if a not in paths:
                    raise CheckError(f"{where}: alias {{{a}}} points at nothing")
            if isinstance(v, str) and v.startswith("{"):
                continue
            elif t["$type"] == "color":
                if not re.fullmatch(r"#[0-9A-F]{6}([0-9A-F]{2})?", v):
                    raise CheckError(f"{where}: bad colour {v}")
            elif t["$type"] == "dimension":
                if not re.fullmatch(r"-?\d+(\.\d+)?px", v):
                    raise CheckError(f"{where}: bad dimension {v}")
    keys = lambda s: sorted(".".join(p) for p, _ in walk(doc[s]))
    if "light" in doc and "dark" in doc:
        if keys("light") != keys("dark"):
            raise CheckError("light and dark keys differ")


def build():
    doc = {
        "core": core(),
        "light": semantic("light"),
        "dark": semantic("dark"),
        "$themes": [  # PRODUCT (adapt): how each theme was set for the capture; drop a theme the app lacks
            {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"},
             "$description": "Settings > Appearance > Auto-Night Mode > Disabled (the day theme), set for the light pass on 2026-10-24 and put back to System afterwards. Read from screenshots/light/."},
            {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"},
             "$description": "Auto-Night Mode > System with the phone in dark mode (the Night theme). Read from screenshots/dark/."},
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
