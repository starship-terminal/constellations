#!/usr/bin/env python3
"""Build tokens.json (W3C DTCG, Tokens Studio multi-set layout) from raw/readings.json (native kit).

Copied from tools/kit/native (Grok Bot's). Adapt core() and semantic(), marked PRODUCT (adapt): they map this
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
    if r.get("spread") is not None:
        note += f" The average of a small box (channel spread {r['spread']}): the mirroring stream leaves a few levels of noise on small tinted fills, so no one pixel is exact."
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
    ids = ["bg.page", "bg.grouped", "surface.card", "surface.bubble", "surface.glass", "surface.selected",
           "surface.menu", "surface.primary", "border.divider", "border.cardDivider", "border.control",
           "text.primary", "text.secondary", "text.tertiary", "text.placeholder", "text.tab"]
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


# PRODUCT (adapt) from here to semantic()'s end: the mapping from readings to tokens.
def core():
    c = {}
    c["color"] = {"neutral": neutral_ramp()}
    c["radius"] = {
        "card": derived("26px", "dimension", f"Grouped cards and the Push Notifications banner: {rd('radius.card')['value']} on Settings and {rd('radius.banner')['value']} on the banner, both themes. Plus or minus 2 pt."),
        "textArea": derived("24px", "dimension", f"Multi-line fields (Bio on Edit Profile): {rd('radius.textArea')['value']} in both themes."),
        "control": derived("12px", "dimension", f"Tiles that hold a control: the event page's Register, Contact and More buttons ({rd('radius.eventAction')['value']}) and the Start and End group on Create Event ({rd('radius.formGroup')['value']} over the cover tint)."),
        "thumb": derived("8px", "dimension", f"Event cover thumbnails ({rd('radius.thumb')['value']} on a flat cover) and calendar tiles ({rd('radius.calendarTile', 'light')['value']})."),
        "icon": derived("6px", "dimension", f"Coloured icon tiles in Settings rows: {rd('radius.settingsIcon')['value']} dark, {rd('radius.settingsIcon', 'light')['value']} light."),
        "capsule": derived("999px", "dimension", "Fully round ends: the tab bar and its selected pill, glass nav buttons, the search field, filter chips, outlined category chips, the segmented control, Invited badges, price and status pills, the Subscribe and Confirm buttons, single-line fields (Name), the composer, message bubbles, the send button and switches."),
    }
    c["space"] = {
        "base": derived("4px", "dimension", "Measured gaps land on multiples of 4 pt within a pixel or two."),
        "xs": derived("4px", "dimension", "Gap between a host line and the title under it, and between stacked meta lines."),
        "sm": derived("8px", "dimension", "Gap between filter chips and between category chips."),
        "md": derived("12px", "dimension", "Gap between an event thumbnail and its text: the thumbnail ends at x 216 px and the host line starts at x 240 px in 01."),
        "lg": derived("16px", "dimension", "Inner padding of grouped cards: Settings row text starts 16 pt inside the card (x 88 px, card edge at 56 px in 23)."),
        "xl": derived("20px", "dimension", "Screen margin: titles, list rows, cards and chips start 20 pt from the screen edge (x 56 px, screen edge at 16 px, in every capture)."),
        "cardGap": derived("24px", "dimension", f"Between two grouped cards with no header: the first Settings card ends at y 524 px and the next starts at 572 px in 23 (edges in rows.settings)."),
        "screenMargin": alias("space.xl", "dimension", "Left and right margin of titles, rows, cards and chips."),
        "cardPadding": alias("space.lg", "dimension", "Inner padding of grouped cards."),
    }
    c["size"] = {
        "row": tok("49px", "dimension", "Grouped row (Settings, Notifications), divider to divider: dividers at 830 and 928 px in 25, 669 px and the card's end at 766 px in 23.", "Sampled", rd("rows.notifSettings")["capture"]),
        "tabBar": {
            "height": tok(px(pt_of("size.tabBar.h")), "dimension", "Floating glass tab bar (Home, Discover, Chat).", "Sampled", rd("size.tabBar.h")["capture"]),
            "width": tok(px(pt_of("size.tabBar.w")), "dimension", "Tab bar width, centred, inset from the screen edges.", "Sampled", rd("size.tabBar.w")["capture"]),
            "selected": tok(px(pt_of("size.tabSelected")), "dimension", "Width of the selected tab's pill inside the bar.", "Sampled", rd("size.tabSelected")["capture"]),
        },
        "navButton": tok("44px", "dimension", f"Round glass back, share, search and more buttons: {rd('size.navButton.w')['value']} wide and {rd('size.navButton.h')['value']} tall, the glass rim's soft edge included. Two actions share one {rd('size.headerButtons.w')['value']} capsule on tab roots (+ and the bell).", "Sampled", rd("size.navButton.w")["capture"]),
        "searchField": tok(px(pt_of("size.search.h")), "dimension", "Search field (glass capsule) beside the back button.", "Sampled", rd("size.search.h")["capture"]),
        "chip": tok(px(pt_of("size.chip.h")), "dimension", f"Glass filter chip height ('Near you' is {rd('size.chip.w')['value']} wide), glass rim included.", "Sampled", rd("size.chip.h")["capture"]),
        "categoryChip": derived("40px", "dimension", f"Outlined category chip height (Family, Tech): {rd('size.categoryChip.h')['value']} dark, {rd('size.categoryChip.h', 'light')['value']} light, outline included."),
        "segmented": {
            "height": derived("47px", "dimension", f"Segmented control (Upcoming, Past): {rd('size.segmented.h')['value']} including the glass rim's soft edge; 47 pt from the pixel runs in 31. {rd('size.segmented.w')['value']} wide with the rim."),
            "pill": derived("40px", "dimension", f"The selected segment's pill: {rd('size.segmentPill.h')['value']} tall with its edge, {rd('size.segmentPill.w')['value']} wide; 40 pt (y 175 to 254 px) inside the edge."),
        },
        "thumb": tok(px(pt_of("size.thumb")), "dimension", f"Square event cover thumbnail in a list row: {rd('size.thumb')['value']} dark, {rd('size.thumb', 'light')['value']} light.", "Sampled", rd("size.thumb")["capture"]),
        "badge": tok(px(pt_of("size.badge", "dark", 1)), "dimension", f"'Invited' badge straddling a thumbnail's lower edge ({rd('size.badge')['value']}).", "Sampled", rd("size.badge")["capture"]),
        "pill": tok(px(pt_of("size.pill", "dark", 1)), "dimension", f"Price and status pills (US$15 {rd('size.pill')['value']}; Sold Out {rd('size.statusPill.h')['value']} with its soft edge).", "Sampled", rd("size.pill")["capture"]),
        "button": derived("45px", "dimension", f"Full-width capsule button (Confirm): {rd('size.primary')['value']} dark, {rd('size.primary', 'light')['value']} light; the white fill's anti-aliasing reads taller on dark."),
        "buttonCompact": derived("34px", "dimension", f"Inline capsule button (Subscribe): {rd('size.subscribe.w')['value']} wide, {rd('size.subscribe.h')['value']} tall dark, {rd('size.subscribe.h', 'light')['value']} light."),
        "actionTile": tok(px(pt_of("size.eventAction", "dark", 1)), "dimension", f"Event page action tile, icon over label (Register {rd('size.eventAction')['value']}; Contact and More the same).", "Sampled", rd("size.eventAction")["capture"]),
        "field": derived("48px", "dimension", f"Single-line field (Name): {rd('size.field')['value']} dark, {rd('size.field', 'light')['value']} light."),
        "composer": tok(px(round(pt_of("size.composer.h"))), "dimension", f"Message composer field: {rd('size.composer.h')['value']}.", "Sampled", rd("size.composer.h")["capture"]),
        "send": tok(px(round(pt_of("size.send"))), "dimension", f"Round send button inside the composer: {rd('size.send')['value']}.", "Sampled", rd("size.send")["capture"]),
        "switch": {
            "width": derived("63px", "dimension", f"Switch track: {rd('size.switch')['value']} in both themes."),
            "height": derived("28px", "dimension", "Switch track height."),
            "thumb": tok(px(pt_of("size.switchThumb")), "dimension", f"Switch thumb, a pill ({rd('size.switchThumb')['value']}).", "Sampled", rd("size.switchThumb")["capture"]),
        },
        "avatar": {
            "header": tok(px(pt_of("size.avatarHeader")), "dimension", f"Account avatar at the top left of a tab root: {rd('size.avatarHeader')['value']} dark, {rd('size.avatarHeader', 'light')['value']} light.", "Sampled", rd("size.avatarHeader")["capture"]),
        },
        "calendarTile": derived("80px", "dimension", f"Square calendar tile in Your Calendars: {rd('size.calendarTile', 'light')['value']} with its anti-aliased edge."),
        "icon": {
            "meta": tok(px(pt_of("size.icon.meta")), "dimension", "Line icons before event meta lines (clock, pin) and in menus.", "Sampled", rd("size.icon.meta")["capture"]),
            "tab": tok(px(pt_of("size.icon.tab")), "dimension", "Tab bar icons (Home, Discover, Chat).", "Sampled", rd("size.icon.tab")["capture"]),
        },
        "settingsIcon": tok(px(pt_of("size.settingsIcon")), "dimension", "Coloured icon tile at the start of a Settings row.", "Sampled", rd("size.settingsIcon")["capture"]),
        "countBadge": derived("20px", "dimension", f"Red unread count on a tab: {rd('size.tabBadge')['value']}."),
        "dot": tok("8px", "dimension", f"Red unread dot in a chat row: {rd('size.dot')['value']}.", "Sampled", rd("size.dot")["capture"]),
        "touchTarget": derived("44px", "dimension", "Nav buttons, rows, the tab bar and full buttons are 44 pt or more. Filter chips (34 pt), the composer (42 pt), the send button (28 pt) and the switch are smaller."),
    }
    c["border"] = {"width": {
        "hairline": derived("0.5px", "dimension", "Dividers between event rows and between card rows: one device pixel at 2x."),
        "outline": derived("1px", "dimension", "Outlined category chips: a two-pixel anti-aliased edge (y 1216 to 1218 px in 09)."),
        "selected": derived("1.5px", "dimension", "The selected Colour Scheme card's outline: three pixels with anti-aliasing (y 437 to 439 px in 24)."),
    }}
    c["fontFamily"] = {
        "base": tok("system", "fontFamily", "Not determinable from pixels. The letterforms are close to the iOS system face; use the platform font.", "Not captured", MEASURED),
    }
    c["fontWeight"] = {
        "regular": derived(400, "fontWeight", "Meta lines, host lines, descriptions, Settings rows. Judged by stroke width, not measured."),
        "medium": derived(500, "fontWeight", "Event row titles, badge and pill labels, tab labels, action tile labels. Judged by stroke width."),
        "semibold": derived(600, "fontWeight", "Nav titles, section titles, date sections, chat row titles, button labels. Judged by stroke width."),
        "bold": derived(700, "fontWeight", "Tab root titles, category and event page titles, the About Event opening, the Event Name placeholder. Judged by stroke width."),
    }

    def ty(size_rid, weight, lh, desc, extra=()):
        sizes = [rd(r)["value"] for r in (size_rid,) + tuple(extra)]
        v = {"fontFamily": "{fontFamily.base}", "fontWeight": "{fontWeight.%s}" % weight,
             "fontSize": sizes[0].replace("pt", "px")}
        if lh:
            v["lineHeight"] = lh
        return tok(v, "typography", desc + f" Cap-height readings: {', '.join(sorted(set(sizes)))}.", "Derived", rd(size_rid)["capture"])

    lines = lambda rid: f"{round(float(rd(rid)['value'].rstrip('pt')))}px"
    c["typography"] = {
        "title1": ty("type.title1", "bold", None, "Category and calendar page titles (Family, [SF] HackerSquad)."),
        "title2": ty("type.largeTitle", "bold", None, "Tab root titles beside the avatar (Discover, Chat) and the event page title.", ("type.eventTitle",)),
        "aboutHeading": ty("type.aboutHeading", "bold", lines("lines.aboutHeading"), "The bold opening line of About Event."),
        "placeholderLarge": ty("type.placeholderLarge", "bold", None, "The Event Name field on Create Event, placeholder and typed text."),
        "title3": ty("type.title2", "semibold", None, "Section titles with a chevron (Your Events, Picked for You, Browse by Category)."),
        "headline": ty("type.headline", "medium", lines("lines.headline"), "Event row titles, up to two lines.", ("type.chatTitle",)),
        "navTitle": ty("type.navTitle", "semibold", None, "Nav titles (Notifications, Settings), date sections ('Today'), chat row titles.", ("type.dateSection", "type.chatTitle")),
        "body": ty("type.body", "regular", None, "Settings rows, grouped section headers (grey), menu items.", ("type.sectionHeader",)),
        "callout": ty("type.meta", "regular", lines("lines.body"), "Event meta lines (time, place), category descriptions, notifications (on a " + lines("lines.notification") + " line).", ("type.description",)),
        "subhead": ty("type.host", "regular", None, "Host lines above an event title ('Emergent', 'TEDxSingapore')."),
        "caption": ty("type.caption", "medium", None, "Badge labels ('Invited'), action tile labels ('Register'), thread timestamps and footnotes under cards.", ("type.button", "type.timestamp", "type.footnote")),
        "pill": ty("type.pill", "semibold", None, "Price and status pill labels (US$15, Sold Out, Near Capacity)."),
        "tab": ty("type.tab", "medium", None, "Tab bar labels."),
    }
    c["$extensions"] = {"notTokenised": [
        "Cover tint: event pages and the Create Event sheet take their background, buttons and fields from the cover image in both themes; color.coverExample holds one cover's readings, not fixed values",
        "iOS 26 glass (tab bar, nav buttons, search field, filter chips, segmented control, menus, the Date Range sheet, the composer): blur and refraction come from the system material",
        "Continuous (squircle) corners: DTCG has no value for corner smoothing",
        "Motion and easing: stills only",
        "Shadows: none drawn; separation comes from the page and card fills and the glass material",
        "Line heights of one-line labels: only multi-line blocks were measured",
    ]}
    return c


# ---------------------------------------------------------------- semantic sets

def scrim(theme):
    """The dim behind the Date Range sheet as black at an alpha: the search field's grey under the sheet
    over the same grey without it (red channel; the greys are neutral)."""
    ref, dim = int(rd("scrim.ref", theme)["value"][1:3], 16), int(rd("scrim.sheet", theme)["value"][1:3], 16)
    alpha = round(1 - dim / ref, 2)
    return derived("#000000%02X" % round(alpha * 255), "color",
                   f"Behind the Date Range sheet: black at {alpha:.2f}, from the search field reading {rd('scrim.ref', theme)['value']} undimmed (12) and {rd('scrim.sheet', theme)['value']} under the sheet (14).",
                   rd("scrim.sheet", theme)["capture"])


def semantic(theme):
    f = lambda rid, desc, typ="color": from_reading(rid, theme, typ, desc)
    v = lambda rid: rd(rid, theme)["value"]
    s = {"color": {
        "bg": {
            "page": f("bg.page", "Full-bleed pages: Home, Discover, Chat, search, a category or calendar page, Your Events, Notifications."),
            "grouped": f("bg.grouped", "Page behind grouped cards: Settings and its pushed pages (Notifications, Account, Edit Profile). Black in dark, a pale grey in light."),
            "scrim": scrim(theme),
        },
        "surface": {
            "card": f("surface.card", f"Grouped cards, the Push Notifications banner ({v('surface.banner')}) and fields on Edit Profile ({v('surface.field')})."),
            "bubble": f("surface.bubble", "Message bubbles in a chat thread."),
            "glass": f("surface.glass", f"Glass controls over an empty page: the tab bar; nav buttons read {v('surface.navButton')}, the search field {v('surface.search')}, filter chips {v('surface.chip')}, the composer {v('surface.composer')}. The material tints with what is behind it."),
            "selected": f("surface.selected", f"The selected pill inside glass: the current tab, the selected segment ({v('surface.segmentSelected')}). Darker than the glass in both themes."),
            "menu": f("surface.menu", f"Pull-down and pop-up menus (glass; pop-ups read {v('surface.popup')}). The reading picks up the page behind."),
            "sheet": f("surface.sheet", "The Date Range sheet (glass over the dimmed search page)."),
            "primary": f("surface.primary", "The theme's ink: the Confirm button, the enabled Create Event check. White in dark, near-black in light."),
        },
        "border": {
            "divider": f("border.divider", "Hairline between event rows, inset to the row text."),
            "cardDivider": f("border.cardDivider", "Hairline between rows inside a grouped card, inset to the row text."),
            "chip": f("border.chip", "Outline of category chips (Family, Tech): the only outlined control."),
            "control": f("border.control", "Outline of an unselected option card (Colour Scheme)."),
            "selected": f("border.selected", "Outline of the selected option card: the theme's ink."),
        },
        "text": {
            "primary": f("text.primary", f"Titles, event row titles, Settings rows; nav titles read {v('text.navTitle')}."),
            "secondary": f("text.secondary", f"Meta lines (time, place), host lines ({v('text.host')}), descriptions."),
            "tertiary": f("text.tertiary", f"The weekday after a date section ('/ Saturday'), grouped section headers ({v('text.sectionHeader')}), chat row dates ({v('text.time')})."),
            "placeholder": f("text.placeholder", "Field placeholders (Bio)."),
            "disabled": f("text.disabled", "Past days in the Date Range calendar, read over the glass sheet."),
            "link": f("text.link", f"Text links ('Open Settings'); 'Now' in the Date Range sheet reads {v('text.linkDate')}."),
            "onPrimary": f("text.onPrimary", "Label on the ink button (Confirm)."),
            "onAccent": f("text.onAccent", "Label on the purple Subscribe button and the blue send button's arrow."),
            "tab": f("text.tab", "Unselected tab label and icon."),
            "tabSelected": f("text.tabSelected", "Selected tab label and icon: the ink, not a brand colour."),
        },
        "accent": {
            "fg": f("accent.fg", "Luma's purple as text: 'Invited' badge labels."),
            "subtle": f("accent.subtle", "'Invited' badge fill."),
            "emphasis": f("accent.emphasis", "The Subscribe button: a lighter, warmer purple than the badge text."),
            "tile": f("accent.tile", "The category icon disc (Family) and avatar role dots in Notifications."),
        },
        "focus": {
            "caret": f("focus.caret", "Text caret in a focused field: the only focus indicator (no ring). A two-pixel column, so the share is low; it is the ink, anti-aliased."),
        },
        "success": {
            "fg": f("success.fg", "Price pill labels (US$15, $88)."),
            "subtle": f("success.subtle", "Price pill fill."),
        },
        "danger": {
            "fg": f("danger.fg", f"'Sold Out' pill label; destructive rows read {v('text.danger')} (Delete Account) and destructive menu items {v('text.dangerMenu')} (Unfollow, Report Event)."),
            "subtle": f("danger.subtle", "'Sold Out' pill fill."),
            "emphasis": f("danger.badge", f"Unread count on the Chat tab and the unread dot in a chat row ({v('danger.dot')})."),
        },
        "warning": {
            "fg": f("warning.fg", "'Near Capacity' pill label."),
            "subtle": f("warning.subtle", "'Near Capacity' pill fill."),
        },
        "info": {
            "fg": f("info.fg", "'Waitlist Open' pill label."),
            "subtle": f("info.subtle", "'Waitlist Open' pill fill."),
            "emphasis": f("info.emphasis", "The send button in the composer, once there is text."),
        },
        "switch": {
            "off": f("switch.off", "Switch off track, read over the Create Event sheet, so it carries the cover tint (orange cover in dark, purple in light). No switch was captured on a plain page."),
            "thumb": f("switch.thumb", "Switch thumb."),
        },
        "coverExample": {
            "eventPage": f("tint.eventPage", "One event page's background (the TEDxSingapore cover). The app derives it from each cover; do not use it as a fixed value."),
            "eventButton": f("tint.eventButton", "Contact and More tiles on that event page: a lighter wash of the same tint."),
            "createPage": f("tint.createPage", "The Create Event sheet with a random cover (orange in dark, purple in light). The app derives it from the cover."),
            "createField": f("tint.createField", "Fields on that sheet: a lighter wash of the same tint."),
        },
        "button": {
            "primary": {"bg": alias("color.surface.primary", "color", "Full-width capsule (Confirm)."),
                        "text": alias("color.text.onPrimary", "color", "Its label.")},
            "accent": {"bg": alias("color.accent.emphasis", "color", "Subscribe."),
                       "text": alias("color.text.onAccent", "color", "Its label.")},
            "glass": {"bg": alias("color.surface.glass", "color", "Nav buttons, filter chips, the Following button."),
                      "text": alias("color.text.primary", "color", "Their icon or label.")},
        },
        "status": {
            "success": alias("color.success.fg", "color", "Success: green pill labels (prices)."),
            "danger": alias("color.danger.fg", "color", "Danger: red labels, destructive rows and menu items."),
            "warning": alias("color.warning.fg", "color", "Warning: amber pill labels (Near Capacity)."),
            "info": alias("color.info.fg", "color", "Info: blue pill labels (Waitlist Open)."),
        },
    }}
    s["$extensions"] = {"notTokenised": [
        "Pressed states: stills only",
        "Disabled buttons: the Create Event check is a faint glass circle before a name is typed (19) and the ink once one is (20); read from the screenshots, not tokenised",
        "Map tiles, cover art, calendar avatars and app icons: content, not tokens",
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
             "$description": "Luma's Settings > Appearance > Colour Scheme > Light, set for the capture and put back to System afterwards. Read from screenshots/light/."},
            {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"},
             "$description": "Colour Scheme > System with the phone in dark mode. Read from screenshots/dark/."},
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
