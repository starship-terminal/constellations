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
    ids = ["bg.sidebar", "bg.page", "surface.card", "surface.cardInSheet", "surface.tableHeader", "surface.bubble",
           "surface.code", "surface.tab", "surface.tabSelected", "surface.glass", "surface.menu", "border.divider",
           "border.settings", "border.control", "text.primary", "text.prose", "text.secondary", "text.tertiary",
           "text.placeholder", "switch.off", "switch.offSettings"]
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


def margin(rid):
    """Distance in pt from the screen's left edge (x 16 in the capture) to the first ink."""
    return (rd(rid)["from"] - 16) / 2


def pitch(rid):
    return float(rd(rid)["value"].rstrip("pt"))


# PRODUCT (adapt) from here to semantic()'s end: the mapping from readings to tokens.
def core():
    c = {}
    c["color"] = {"neutral": neutral_ramp()}
    both = lambda rid: f"{rd(rid)['value']} dark, {rd(rid, 'light')['value']} light"
    c["radius"] = {
        "control": derived("4px", "dimension", f"Outlined buttons and selects in Settings (Connect, Off): {rd('radius.control')['value']} and {both('radius.select')}. Plus or minus 2 pt."),
        "frame": derived("7px", "dimension", f"Inline database frame ({both('radius.frame')}) and its blue + split button ({both('radius.dbAdd')}). Plus or minus 2 pt."),
        "card": derived("10px", "dimension", f"Grouped cards in a large sheet (Actions, Theme): {both('radius.card')}; the segmented font card {both('radius.cardSeg')}; the outlined result card in an AI answer {both('radius.resultCard')}. Plus or minus 2 pt."),
        "composer": derived("20px", "dimension", f"The expanded AI composer: {both('radius.composer')}."),
        "bubble": derived("22px", "dimension", f"The owner's message bubble in an AI chat: {both('radius.bubble')}. All four corners are the same."),
        "list": derived("26px", "dimension", f"The inset grouped list inside a small sheet (Sort): {rd('radius.cardInSheet')['value']}, the system's own list style, larger than Notion's cards."),
        "menu": derived("32px", "dimension", f"Pop-up menus (iOS 26 glass, model picker): {rd('radius.menu')['value']}."),
        "sheet": derived("36px", "dimension", f"Top corners of a sheet: {both('radius.sheet')}."),
        "capsule": derived("999px", "dimension", f"Fully round ends: the top tabs, the bottom-bar pill and buttons, the + Chat button, the view chip ({both('radius.viewChip')} on a 33 pt chip), switches and the send button."),
    }
    c["space"] = {
        "base": derived("4px", "dimension", "Most measured gaps are multiples of 4 pt within a point."),
        "xs": derived("4px", "dimension", "Gap between a row icon and the edge of its tile."),
        "sm": derived("8px", "dimension", "Gap between the top tabs (408 - 392 px = 8 pt in 01-home-sidebar-tree) and between the bottom-bar buttons."),
        "md": derived("12px", "dimension", "Gap between an icon and its label in rows and tabs."),
        "lg": derived("16px", "dimension", f"Side margin of grouped cards in sheets (the Actions cards start at x 48, (48 - 16) / 2 = 16 pt)."),
        "xl": derived("20px", "dimension", f"Text margin of the sidebar and lists: section headers and rows start {margin('space.sidebarText'):g} pt from the edge; settings text {margin('space.settingsText'):g} pt."),
        "page": derived("27px", "dimension", f"Text margin of a page: body text starts {margin('space.pageText'):g} pt from the edge, wider than the sidebar's."),
        "screenMargin": alias("space.xl", "dimension", "Left and right margin of text in the sidebar, Chats, Inbox and Settings."),
    }
    sw = rd("size.switchThumb")["value"].rstrip("pt").split("x")
    c["size"] = {
        "row": derived(px(round(pitch("lines.sidebarRows"))), "dimension", f"Single-line row in the sidebar and the Chats list: the line pitch of their titles, {rd('lines.sidebarRows')['value']} and {rd('lines.chatRows')['value']}."),
        "rowSheet": derived(px(round(pitch("lines.sheetRows"))), "dimension", f"Single-line row in a grouped card in a sheet (Actions, Filters): {rd('lines.sheetRows')['value']} divider to divider."),
        "rowSearch": derived(px(round(pitch("lines.searchRows"))), "dimension", f"Two-line search result (title and location): {rd('lines.searchRows')['value']} pitch."),
        "rowDatabase": derived(px(round(pitch("lines.dbRows"))), "dimension", f"Row in a database list view (coloured groups): {rd('lines.dbRows')['value']} pitch, with a 2 pt gap between rows."),
        "tab": tok(px(pt_of("size.tab.h")), "dimension", f"Height of the top tabs. Unselected tabs are circles about {pt_of('size.tab.w'):g} pt wide; the selected one grows into a pill with its label ({pt_of('size.tabSelected.w'):g} pt for Home).", "Sampled", rd("size.tab.h")["capture"]),
        "avatarButton": tok(px(round(pt_of("size.avatarButton.w"))), "dimension", f"The round account button left of the tabs ({both('size.avatarButton.w')}).", "Sampled", rd("size.avatarButton.w")["capture"]),
        "barButton": tok(px(round(pt_of("size.barButton.w"))), "dimension", f"Round glass buttons in the bottom bar (search, compose): {both('size.barButton.w')}.", "Sampled", rd("size.barButton.w")["capture"]),
        "barPill": tok(px(round(pt_of("size.barPill.h"))), "dimension", f"Height of the bottom bar's 'Ask AI' glass pill ({both('size.barPill.h')}); it fills the width between the two buttons ({pt_of('size.barPill.w'):g} pt).", "Sampled", rd("size.barPill.h")["capture"]),
        "navButton": tok(px(round(pt_of("size.navButton.w"))), "dimension", "Round glass buttons on the AI chat (history, new chat) and sheet close buttons.", "Sampled", rd("size.navButton.w")["capture"]),
        "composer": tok(px(round(pt_of("size.composer.h"))), "dimension", f"The AI composer while focused: a two-row glass card ({both('size.composer.h')}), text above, tools below.", "Sampled", rd("size.composer.h")["capture"]),
        "composerCompact": tok(px(round(pt_of("size.composerCompact.h"))), "dimension", "The AI composer when not focused: one capsule row with + and the mic.", "Sampled", rd("size.composerCompact.h")["capture"]),
        "sendButton": tok(px(pt_of("size.send")), "dimension", f"The blue round send button in the composer ({rd('size.send')['value']}).", "Sampled", rd("size.send")["capture"]),
        "button": tok(px(pt_of("size.chatButton", "dark", 1)), "dimension", f"Floating primary button (+ Chat): {rd('size.chatButton')['value']}.", "Sampled", rd("size.chatButton")["capture"]),
        "control": tok(px(pt_of("size.control.h")), "dimension", f"Outlined buttons and selects in Settings (Connect {rd('size.control.h')['value']}, Off {rd('size.select.h')['value']}).", "Sampled", rd("size.control.h")["capture"]),
        "controlLarge": tok(px(pt_of("size.selectWide.h")), "dimension", "The wide select on its own line in Settings (Theme).", "Sampled", rd("size.selectWide.h")["capture"]),
        "chip": tok(px(pt_of("size.viewChip.h")), "dimension", f"Database view chip ('Areas'): {pt_of('size.viewChip.w'):g} x {rd('size.viewChip.h')['value']}.", "Sampled", rd("size.viewChip.h")["capture"]),
        "splitButton": tok(px(pt_of("size.dbAdd", "dark", 1)), "dimension", f"The blue + split button on a database ({rd('size.dbAdd')['value']}).", "Sampled", rd("size.dbAdd")["capture"]),
        "switch": {
            "width": tok(px(pt_of("size.switch.w")), "dimension", "Switch track, anti-aliased edge included.", "Sampled", rd("size.switch.w")["capture"]),
            "height": tok(px(round(pt_of("size.switch.h"))), "dimension", f"Switch track height ({both('size.switch.h')}).", "Sampled", rd("size.switch.h")["capture"]),
            "thumb": tok(px(float(sw[0])), "dimension", f"Switch thumb: a pill {rd('size.switchThumb')['value']} (iOS 26).", "Sampled", rd("size.switchThumb")["capture"]),
        },
        "radio": tok(px(pt_of("size.radio")), "dimension", "Radio outer diameter (Sort): a ring when off, a blue ring with a dark centre when on.", "Sampled", rd("size.radio")["capture"]),
        "touchTarget": derived("44px", "dimension", "Tabs, rows and bar buttons are 44 pt or more. The Settings controls (28 pt) and the split button (31.5 pt) are smaller and sit in taller rows."),
    }
    c["border"] = {"width": {
        "hairline": derived("1px", "dimension", "Dividers and rims: two device pixels at 2x, so 1 pt (border.divider reads a two-pixel row in 19-page-actions-sheet)."),
    }}
    c["fontFamily"] = {"base": tok("system", "fontFamily", "Not determinable from pixels. The letterforms are a neo-grotesque close to the iOS system face; the Actions sheet offers Default, Serif and Mono for a page. Use the platform font.", "Not captured", MEASURED)}
    c["fontWeight"] = {
        "regular": derived(400, "fontWeight", "Rows, body text, subtitles, menu items. Judged by stroke width, not measured."),
        "medium": derived(500, "fontWeight", "Tab labels and the + Chat label. Judged by stroke width."),
        "semibold": derived(600, "fontWeight", "Nav and sheet titles, the settings section title. Judged by stroke width."),
        "bold": derived(700, "fontWeight", "Page titles and headings. Judged by stroke width."),
    }

    def ty(size_rid, weight, lh, desc, extra=()):
        sizes = [rd(r, t)["value"] for r in (size_rid,) + tuple(extra) for t in READ[r]]
        v = {"fontFamily": "{fontFamily.base}", "fontWeight": "{fontWeight.%s}" % weight,
             "fontSize": rd(size_rid)["value"].replace("pt", "px")}
        if lh:
            v["lineHeight"] = lh
        return tok(v, "typography", desc + f" Cap-height readings: {', '.join(sorted(set(sizes), key=lambda x: float(x[:-2])))}.", "Derived", rd(size_rid)["capture"])

    lines = lambda rid: f"{round(float(rd(rid)['value'].rstrip('pt'))):g}px"
    c["typography"] = {
        "pageTitle": ty("type.pageTitle", "bold", None, "Page title under the icon (Databases (Engine))."),
        "heading1": ty("type.h1", "bold", None, "Heading 1 in a page."),
        "heading2": ty("type.h2", "bold", None, "Heading 2 in a page."),
        "title": ty("type.settingsTitle", "semibold", None, "Section title in Settings (Notifications, Preferences)."),
        "bodyLarge": ty("type.rowTitle", "regular", lines("lines.prose"), "Sidebar, Chats and sheet rows, the owner's bubble, AI answers, menu items, nav and sheet titles (titles semibold).", ("type.chatRow", "type.sheetRow", "type.actionItem", "type.bubble", "type.prose", "type.menuItem", "type.navTitle", "type.sheetTitle")),
        "button": ty("type.button", "medium", None, "The + Chat button label."),
        "body": ty("type.body", "regular", lines("lines.pageBody"), "Page body text, on a 24 pt line."),
        "callout": ty("type.tab", "medium", None, "Tab labels, the composer placeholder, model picker items, small sheet titles.", ("type.composer", "type.modelItem", "type.sheetTitleSmall")),
        "subheadline": ty("type.sectionHeader", "regular", None, "Sidebar section headers, settings row titles, empty-state lines, Settings controls, dates, Done.", ("type.settingsRow", "type.empty", "type.control", "type.date", "type.done")),
        "footnote": ty("type.subtitle", "regular", lines("lines.subtitle"), "Settings subtitles and segment labels, on an 18 pt line.", ("type.segLabel",)),
        "caption": ty("type.searchSub", "regular", None, "Search result locations, menu headers and descriptions, table headers.", ("type.menuHeader", "type.menuDesc", "type.tableHeader")),
    }
    c["$extensions"] = {"notTokenised": [
        "iOS 26 glass (tabs, bottom bar, composer, menus, nav buttons): blur and refraction come from the system material",
        "Continuous (squircle) corners: DTCG has no value for corner smoothing",
        "Motion and easing: stills only",
        "Shadows: none drawn under cards; glass controls carry the system's own soft shadow",
        "Inline code corner radius: too small to read off the captures",
        "Line heights of titles and one-line labels: only multi-line blocks were measured",
    ]}
    return c


# ---------------------------------------------------------------- semantic sets

def scrim(theme):
    ref, dim = rd("scrim.ref", theme)["value"], rd("scrim.sheet", theme)["value"]
    a = 1 - int(dim[1:3], 16) / int(ref[1:3], 16)
    return derived("#000000%02X" % round(a * 255), "color",
                   f"Black at {round(a * 100)}%: the search canvas reads {ref} undimmed and {dim} under the Filters sheet. A pushed card (the AI chat) dims the sidebar above it to {rd('bg.behindPushed', theme)['value']}.",
                   rd("scrim.sheet", theme)["capture"])


def dark_only(theme, rid, desc, light_from=None, why=""):
    """A role read in dark only. Light reuses the dark value (light_from None) or the light value of
    the closest role, as Derived, and says which."""
    if theme == "dark":
        return from_reading(rid, "dark", "color", desc)
    src = rd(light_from, "light") if light_from else rd(rid, "dark")
    return derived(src["value"], "color", desc + " Not captured in light: " + why, src["capture"])


def line(rid, theme, desc):
    """A hairline's colour: its most extreme anti-aliased pixel, so Derived rather than a flat fill."""
    r = rd(rid, theme)
    return derived(r["value"], "color", desc + " The hairline's lightest pixel in dark, darkest in light.", r["capture"])


def semantic(theme):
    f = lambda rid, desc, typ="color": from_reading(rid, theme, typ, desc)
    s = {"color": {
        "bg": {
            "sidebar": f("bg.sidebar", "Home (the sidebar tree), the Chats, Meetings and Inbox tabs, Settings and the bar behind search."),
            "page": f("bg.page", "Pages, the AI chat and search results: the canvas content sits on."),
            "sheet": f("bg.sheet", "Small sheets (search Filters, Sort): the page colour."),
            "sheetGrouped": f("bg.sheetLarge", "Large sheets with grouped cards (page Actions, Theme, Views): the sidebar colour."),
            "scrim": scrim(theme),
        },
        "surface": {
            "card": f("surface.card", "Grouped cards in a large sheet (Actions, Theme, Views)." + (" Lighter than the sheet in dark." if theme == "dark" else " White on the off-white sheet in light.")),
            "list": dark_only(theme, "surface.cardInSheet", "The system's inset grouped list inside a small sheet (Sort).", "bg.sidebar", "filled from bg.sidebar, the grey the light theme uses for raised rows (table header, large sheet)."),
            "tableHeader": f("surface.tableHeader", "Table header row in a page."),
            "bubble": f("surface.bubble", "The owner's message bubble in an AI chat: a quiet grey, never the accent."),
            "code": f("surface.code", "Inline code behind red monospace text."),
            "tab": f("surface.tab", "Unselected top tabs (Chats, Meetings, Inbox as circles)."),
            "tabSelected": f("surface.tabSelected", "The selected top tab, a pill holding its icon and label."),
            "glass": f("surface.glass", "Glass controls (the search bar, nav buttons), centre reading. The material tints with whatever is behind it."),
            "composer": f("surface.composer", "The expanded AI composer (glass)."),
            "menu": f("surface.menu", "Pop-up menus (glass, model picker). Over content the reading shifts with what is behind."),
            "chip": f("surface.viewChip", "Database view chip ('Areas')."),
            "iconTile": f("surface.icon", "Square tile behind a teamspace icon."),
            "grabber": f("surface.grabber", "Sheet grabber."),
        },
        "group": {
            "blue": f("group.blue", "Database group background, blue. Rows in the group sit on it with primary text."),
            "green": f("group.green", "Database group background, green."),
            "pink": f("group.pink", "Database group background, pink."),
            "orange": f("group.orange", "Database group background, orange."),
        },
        "border": {
            "divider": line("border.divider", theme, "Hairline between rows of a grouped card, full width of the card."),
            "separator": line("border.settings", theme, "Hairline between settings rows, inset to the text margin."),
            "control": line("border.control", theme, "Rim of outlined buttons and selects in Settings (Connect, Off)."),
            "card": line("border.card", theme, "Rim of an outlined card (the result card in an AI answer)."),
            "table": line("border.table", theme, "Table rim and cell lines in a page."),
            "frame": line("border.frame", theme, "Rim of an inline database."),
        },
        "text": {
            "primary": f("text.primary", f"Titles, sidebar and sheet rows, page text, settings rows (page body reads {rd('text.pageBody', theme)['value']}, settings rows {rd('text.settingsRow', theme)['value']})."),
            "prose": f("text.prose", f"AI answers, the owner's bubble, Inbox bodies and small sheet titles: softer than primary in dark (bubble {rd('text.bubble', theme)['value']}, inbox {rd('text.inbox', theme)['value']}, sheet title {rd('text.sheetTitle', theme)['value']})."),
            "secondary": f("text.secondary", f"Section headers, subtitles, empty states, the bar's 'Ask AI'. Readings in this role: {', '.join(sorted({rd(r, theme)['value'] for r in ('text.secondary', 'text.subtitle', 'text.emptyBody', 'text.askPlaceholder') if theme in READ[r]}))}."),
            "tertiary": f("text.tertiary", f"Dates, row values, footnotes (Sort value reads {rd('text.sortValue', theme)['value']})."),
            "placeholder": f("text.placeholder", f"Composer placeholder (the property search placeholder reads {rd('text.propertySearch', theme)['value']})."),
            "menu": f("text.menu", "Items in a system pop-up menu: near-white or near-black, not Notion's warm ink."),
            "menuSecondary": f("text.menuDesc", "Descriptions under menu items (model picker)."),
            "code": f("text.code", "Inline code: red monospace."),
            "danger": f("text.danger", "Destructive rows (Move to Bin): red text and a red icon, never a red fill."),
            "accent": f("text.accent", f"Active controls in text: an applied sort or filter, Done, the selected font ('Ag' reads {rd('text.accentSel', theme)['value']})."),
            "onAccent": f("text.onAccent", "Label and glyph on a blue button."),
            "icon": f("text.icon", "Row icons in sheets: the primary ink."),
            "iconMuted": f("text.iconMuted", "Unselected tab icons and the bar's glyphs."),
        },
        "accent": {
            "default": f("accent.fill", "Notion blue: the database + button, the selected radio, the send button."),
            "button": f("accent.button", "The floating + Chat button (glass over blue), centre reading."),
        },
        "focus": {
            "caret": f("accent.caret", "Text caret in a focused field: the only focus indicator (no ring).") if theme == "dark" else f("accent.caretLight", "Text caret in a focused field: the only focus indicator (no ring)."),
        },
        "button": {
            "primary": {"bg": alias("color.accent.button", "color", "Primary button (+ Chat): blue capsule."),
                        "text": alias("color.text.onAccent", "color", "Primary button label.")},
            "secondary": {"border": alias("color.border.control", "color", "Outlined button (Connect, Manage settings): no fill, a hairline rim."),
                          "text": alias("color.text.primary", "color", "Outlined button label.")},
        },
        "switch": {
            "off": f("switch.off", "Switch off track in native sheets (search Filters, Actions)."),
            "offSettings": f("switch.offSettings", "Switch off track in Settings: a warmer grey than the native sheets'."),
            "thumb": f("switch.thumb", "Switch thumb."),
        },
        "radio": {
            "on": alias("color.accent.default", "color", "Selected radio: a blue ring around a dark centre."),
            "off": dark_only(theme, "radio.off", "Unselected radio ring.", "text.secondary", "filled from text.secondary, the closest light role."),
        },
        "status": {
            "danger": alias("color.text.danger", "color", "Danger: red text on destructive rows. No danger fill was seen."),
            "info": alias("color.accent.default", "color", "Info: the blue accent."),
            "unread": f("accent.dot", "The dot on the account button for unread activity (salmon in dark, red in light)."),
        },
    }}
    s["$extensions"] = {"notTokenised": [
        "Success and warning colours: no such state was seen",
        "Pressed states: stills only",
        "The other database and select colours (grey, brown, yellow, purple, red): only blue, green, pink and orange groups were on screen",
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
             "$description": "Settings > Preferences > Theme > Light, set for the capture on 2026-10-24 and put back to Use system setting. Read from screenshots/light/."},
            {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"},
             "$description": "Theme > Use system setting with the phone in dark mode, 2026-10-23. Read from screenshots/dark/."},
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
