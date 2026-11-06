#!/usr/bin/env python3
"""Build tokens.json (W3C DTCG, Tokens Studio multi-set layout) from raw/readings.json (native kit).

Copied from the native kit (systems/grokbot). Adapt core() and semantic(), marked PRODUCT (adapt): they map this
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

def lum(h):
    return sum(int(h[i:i + 2], 16) for i in (1, 3, 5))


def ramp(ids, keep, what):
    """Every value a group of readings shows, both themes, sorted light to dark and named by order.
    Not a published ramp: the steps are the values the app shows. keep(r, g, b) picks the hue."""
    seen = {}
    for rid in ids:
        for theme, r in READ[rid].items():
            v = r["value"]
            if keep(int(v[1:3], 16), int(v[3:5], 16), int(v[5:7], 16)):
                seen.setdefault(v, []).append((f"{theme} {rid}", r["evidence"], r["capture"]))
    rank = ["Sampled", "Sampled (text)", "Derived"]   # the most exact reading of the value wins
    out = {}
    for i, v in enumerate(sorted(seen, key=lum, reverse=True)):
        uses = sorted(set(seen[v]))
        best = min(uses, key=lambda u: rank.index(u[1]))
        listed = ", ".join(f"{name} ({ev})" for name, ev, _ in uses)
        out[f"{i * 50:03d}"] = tok(v, "color", f"{what} Used by: {listed}.", best[1], best[2])
    return out


NEUTRAL_IDS = ["bg.page", "bg.list", "bg.sidebar", "surface.card", "surface.userBubble", "surface.control",
               "surface.selected", "surface.badge", "surface.field", "border.divider", "border.grabber",
               "text.primary", "text.secondary", "text.tertiary", "text.footnote", "text.disabled",
               "switch.off", "button.primary"]
BLUE_IDS = ["accent.blue", "accent.check", "text.link", "switch.onDisabled", "progress.fill", "progress.track"]
CLAY_IDS = ["accent.brand", "accent.send", "accent.archive"]


# PRODUCT (adapt) from here to semantic()'s end: the mapping from readings to tokens.
def core():
    c = {}
    c["color"] = {
        "neutral": ramp(NEUTRAL_IDS, lambda r, g, b: max(r, g, b) - min(r, g, b) <= 12,
                        "A grey the two themes use; dark ones are neutral, light and mid ones lean warm."),
        "blue": ramp(BLUE_IDS, lambda r, g, b: b > r + 30,
                     "A blue the app uses for interactive state (switches, ticks, links, meters)."),
        "clay": ramp(CLAY_IDS, lambda r, g, b: r > b + 60,
                     "Claude's orange: the brand spark, the send button and an active filter. The same in both themes."),
    }
    sel = rd("size.selectedRow")["box"]
    c["radius"] = {
        "card": derived("26px", "dimension", f"Grouped cards on a page or the Settings sheet: {rd('radius.card')['value']} in both themes. Plus or minus 2 pt; the corner is continuous (squircle)."),
        "cardSheet": derived("24px", "dimension", f"Grouped cards inside a bottom sheet: {rd('radius.cardSheet')['value']} in both themes."),
        "bubble": derived("24px", "dimension", f"The owner's message bubble: {rd('radius.userBubble')['value']} in both themes. Every corner is the same; no tail."),
        "composer": derived("22px", "dimension", f"The composer: {rd('radius.composer')['value']}."),
        "sheet": derived("36px", "dimension", f"Top corners of a bottom sheet: {rd('radius.sheet')['value']} in both themes."),
        "row": derived("14px", "dimension", f"Selected sidebar row: {rd('radius.selectedRow')['value']} on a {rd('size.selectedRow')['value'].split('x')[1]} row."),
        "menu": derived("17px", "dimension", f"Pull-down and context menus (iOS 26 glass): {rd('radius.menu')['value']}. The glass edge is soft, so plus or minus 4 pt."),
        "field": derived("10px", "dimension", f"Pop-up select field: {rd('radius.select', 'light')['value']} in light, where its rim reads."),
        "capsule": derived("999px", "dimension", "Fully round ends: the Talk and New chat pills, the send button, glass nav buttons, the model pill, badges, the search field, switches and day toggles."),
    }
    card = rd("size.cardAccount")["box"]
    sheet_card = rd("size.cardSheet")["box"]
    c["space"] = {
        "base": derived("4px", "dimension", "Every measured gap is a multiple of 4 pt within a pixel or two."),
        "xs": derived("4px", "dimension", "Gap between a row title and its subtitle."),
        "sm": derived("8px", "dimension", "Gap between controls in the composer's lower row."),
        "md": derived("12px", "dimension", "Gap between the composer's input line and its controls."),
        "lg": derived("16px", "dimension", f"Screen margin: cards, the response and the composer start {(card[0] - 16) / 2:g} pt from the screen edge; cards stack 16.5 pt apart in Settings."),
        "xl": derived("20px", "dimension", f"Inset of text inside a card: section headers and card text start 20 pt inside the card's edge (Usage, Settings)."),
        "xxl": derived("24px", "dimension", f"Side margin of cards inside a bottom sheet: {(sheet_card[0] - 16) / 2:g} pt from the screen edge."),
        "screenMargin": alias("space.lg", "dimension", "Left and right margin of cards, text and the composer."),
        "cardPadding": alias("space.xl", "dimension", "Horizontal padding inside a grouped card."),
    }
    pitch = lambda rid: (rd(rid)["value"][-1] - rd(rid)["value"][0]) / (len(rd(rid)["value"]) - 1) / 2
    lines_pt = lambda rid: float(rd(rid)["value"].rstrip("pt"))
    sz = lambda rid, i=0: pt_of(rid, "dark", i)
    c["size"] = {
        "navButton": tok(px(sz("size.navButton.w")), "dimension", f"Round glass buttons (sidebar, close, back, more): {rd('size.navButton.w')['value']} wide, {rd('size.navButton.h')['value']} tall with the rim's soft edge.", "Sampled", rd("size.navButton.w")["capture"]),
        "composer": {
            "height": tok(px(sz("size.composer.h")), "dimension", "The composer, two rows: the input line over the controls (+, model pill, microphone, Talk or send).", "Sampled", rd("size.composer.h")["capture"]),
            "width": tok(px(sz("size.composer.w")), "dimension", f"The composer in a thread spans the screen less its margins; on a new chat it is wider ({rd('size.composerNew.w')['value']}).", "Sampled", rd("size.composer.w")["capture"]),
        },
        "control": tok(px(sz("size.composerButton")), "dimension", "Round + and microphone buttons and the model pill inside the composer: one 36 pt height.", "Sampled", rd("size.composerButton")["capture"]),
        "send": tok(px(sz("size.send")), "dimension", f"The orange send button, a circle ({rd('size.send')['value']}).", "Sampled", rd("size.send")["capture"]),
        "talk": {
            "width": tok(px(sz("size.talk")), "dimension", "The Talk pill, the composer's resting primary action.", "Sampled", rd("size.talk")["capture"]),
            "height": tok(px(sz("size.talk", 1)), "dimension", "The Talk pill.", "Sampled", rd("size.talk")["capture"]),
        },
        "pill": tok(px(sz("size.pillPrimary", 1)), "dimension", f"Floating primary pill (New chat, New project, New session): {rd('size.pillPrimary')['value']}.", "Sampled", rd("size.pillPrimary")["capture"]),
        "pillSecondary": tok(px(sz("size.pillSecondary", 1)), "dimension", f"Glass secondary pill (Add device): {rd('size.pillSecondary')['value']}.", "Sampled", rd("size.pillSecondary")["capture"]),
        "button": tok(px(sz("size.buttonFull", 1)), "dimension", f"Full-width button at the bottom of a sheet (Share): {rd('size.buttonFull')['value']}.", "Sampled", rd("size.buttonFull")["capture"]),
        "row": derived(px(pitch("rows.settings")), "dimension", f"Settings row with an icon: the mean pitch of the {len(rd('rows.settings')['value'])} divider rows in rows.settings, divider to divider.", rd("rows.settings")["capture"]),
        "rowTwoLine": derived(px(round(pitch("rows.sheet"))), "dimension", f"Two-line row in a sheet (model name over a description): the mean pitch of the divider rows in rows.sheet, {pitch('rows.sheet'):g} pt, rounded to a point.", rd("rows.sheet")["capture"]),
        "rowSidebar": tok(px(lines_pt("rows.sidebar")), "dimension", "Sidebar row pitch (no dividers).", "Derived", rd("rows.sidebar")["capture"]),
        "rowList": tok(px(lines_pt("rows.chats")), "dimension", "Chats and Projects list row with a subtitle (no dividers).", "Derived", rd("rows.chats")["capture"]),
        "selectedRow": tok(px(sz("size.selectedRow", 1)), "dimension", f"The selected sidebar row's fill: {rd('size.selectedRow')['value']}, {(sel[0] - 16) / 2:g} pt from the screen edge.", "Sampled", rd("size.selectedRow")["capture"]),
        "switch": {
            "width": tok(px(sz("size.switch")), "dimension", f"Switch track ({rd('size.switch')['value']}).", "Sampled", rd("size.switch")["capture"]),
            "height": tok(px(sz("size.switch", 1)), "dimension", f"Switch track ({rd('size.switch')['value']}).", "Sampled", rd("size.switch")["capture"]),
            "thumb": tok(px(sz("size.switchThumb")), "dimension", f"Switch thumb width, a pill ({rd('size.switchThumb')['value']}).", "Sampled", rd("size.switchThumb")["capture"]),
        },
        "select": derived(px(round(sz("size.select", 1))), "dimension", f"Pop-up select field: {rd('size.select')['value']} dark, {rd('size.select', 'light')['value']} light, rim included; the height rounded to a point.", rd("size.select")["capture"]),
        "dayToggle": tok(px(sz("size.dayToggle")), "dimension", f"Round day toggle (Quiet hours): {rd('size.dayToggle')['value']}.", "Sampled", rd("size.dayToggle")["capture"]),
        "searchField": tok(px(sz("size.searchField.h")), "dimension", "Search field height, rim included.", "Sampled", rd("size.searchField.h")["capture"]),
        "progress": tok(px(sz("size.progress", 1)), "dimension", f"Usage meter track thickness ({rd('size.progress')['value']}, round ends).", "Sampled", rd("size.progress")["capture"]),
        "grabber": {
            "width": tok(px(sz("size.grabber")), "dimension", "Sheet grabber.", "Sampled", rd("size.grabber")["capture"]),
            "height": tok(px(sz("size.grabber", 1)), "dimension", "Sheet grabber.", "Sampled", rd("size.grabber")["capture"]),
        },
        "emptyIcon": tok(px(sz("size.emptyIcon")), "dimension", "Circle behind an empty-state icon.", "Sampled", rd("size.emptyIcon")["capture"]),
        "badge": tok(px(sz("size.badge", 1)), "dimension", f"Badge height (Recommended {rd('size.badge')['value']}, usage {rd('size.badgeUsage')['value']}).", "Sampled", rd("size.badge")["capture"]),
        "bubbleMaxWidth": tok(px(sz("size.userBubble")), "dimension", f"The owner's bubble at three lines ({rd('size.userBubble')['value']}), right-aligned to the screen margin.", "Sampled", rd("size.userBubble")["capture"]),
        "touchTarget": derived("44px", "dimension", "Nav buttons, rows and the selected-row fill are 44 pt or more. Composer controls (36 pt), the Talk pill (35 pt), switches (27 pt) and badges (20.5 pt) are smaller and sit inside larger rows or the composer."),
    }
    c["border"] = {"width": {
        "hairline": derived("0.5px", "dimension", "Dividers between grouped rows and the pop-up select's rim: one device pixel at 2x."),
    }}
    c["fontFamily"] = {
        "sans": tok("system", "fontFamily", "The interface sans. Not determinable from pixels; its letterforms are not the iOS system face (a single-storey g, round dots), so the family is the product's own. Use the platform sans.", "Not captured", MEASURED),
        "serif": tok("serif", "fontFamily", "The serif of responses, greetings, the sidebar wordmark and promo titles. Not determinable from pixels; a book serif with bracketed serifs. Use the platform serif.", "Not captured", MEASURED),
    }
    c["fontWeight"] = {
        "regular": derived(400, "fontWeight", "Body, rows, responses, subtitles. Judged by stroke width, not measured."),
        "medium": derived(500, "fontWeight", "Pill labels (New chat, Add device) and badges. Judged by stroke width."),
        "semibold": derived(600, "fontWeight", "Nav and sheet titles, the page heading, the Share and Talk labels. Judged by stroke width."),
    }

    def ty(size_rid, family, weight, lh, desc, extra=()):
        sizes = [rd(r)["value"] for r in (size_rid,) + tuple(extra)]
        v = {"fontFamily": "{fontFamily.%s}" % family, "fontWeight": "{fontWeight.%s}" % weight,
             "fontSize": sizes[0].replace("pt", "px")}
        if lh:
            v["lineHeight"] = lh
        return tok(v, "typography", desc + f" Cap-height readings: {', '.join(sorted(set(sizes), key=lambda s: float(s[:-2])))}.", "Derived", rd(size_rid)["capture"])

    lines = lambda rid: f"{lines_pt(rid):g}px"
    c["typography"] = {
        "display": ty("type.display", "serif", "regular", None, "Promo sheet title ('Give the gift of Claude')."),
        "titleSerif": ty("type.wordmark", "serif", "regular", None, "The sidebar wordmark and the new-chat greeting.", ("type.greeting",)),
        "response": ty("type.response", "serif", "regular", lines("lines.response"), "Claude's responses in a thread: serif, on the page, with no bubble."),
        "headline": ty("type.navTitle", "sans", "semibold", None, "Nav and sheet titles.", ("type.sheetTitle",)),
        "bodyLarge": ty("type.sidebarItem", "sans", "regular", None, "Sidebar items."),
        "body": ty("type.bubble", "sans", "regular", lines("lines.bubble"), "The owner's bubble, settings rows, list titles, menu items, the composer, empty-state titles.", ("type.row", "type.listTitle", "type.menuItem", "type.composer", "type.emptyTitle")),
        "pageHeading": ty("type.pageHeading", "sans", "semibold", None, "Heading at the top of a settings page ('Time and focus')."),
        "callout": ty("type.listSubtitle", "sans", "regular", None, "List subtitles, section headers, tool-step rows, pill labels, empty-state explanations, artifact titles, Appearance tile labels.", ("type.sectionHeader", "type.toolStep", "type.pill", "type.emptyBody", "type.cardTitle", "type.tileLabel")),
        "subheadline": ty("type.subtitle", "sans", "regular", lines("lines.subtitle"), "Setting subtitles, the disclaimer under a response, artifact dates, the Talk label.", ("type.footnote", "type.cardMeta", "type.talk")),
        "footnote": ty("type.sheetSubtitle", "sans", "regular", lines("lines.helper"), "Sheet row subtitles and helper text under a sheet card."),
        "caption": ty("type.badge", "sans", "medium", None, "Badge labels (Recommended, Beta, usage)."),
    }
    c["$extensions"] = {"notTokenised": [
        "iOS 26 glass (nav buttons, the composer, menus, the search bar, the Add device pill): blur and refraction come from the system material",
        "Continuous (squircle) corners: DTCG has no value for corner smoothing",
        "Motion and easing: stills only; the streaming response and the Talk mode were not captured",
        "Shadows: none drawn in dark; light glass controls carry a faint soft shadow that was not measured",
        "Line heights of titles and one-line labels: only multi-line blocks were measured",
    ]}
    return c


# ---------------------------------------------------------------- semantic sets

def scrim(theme, rid, ref="scrim.ref"):
    r, dim = rd(ref, theme)["value"], rd(rid, theme)["value"]
    a = 1 - int(dim[1:3], 16) / int(r[1:3], 16)
    return derived("#000000%02X" % round(a * 255), "color",
                   f"Black at {round(a * 100)}%: the new chat reads {r} undimmed and {dim} under a sheet.",
                   rd(rid, theme)["capture"])


def dark_only(theme, rid, desc, light_from=None, why=""):
    """A role read in dark only. Light reuses the dark value (light_from None) or the light value of
    the closest role, as Derived, and says which."""
    if theme == "dark":
        return from_reading(rid, "dark", "color", desc)
    src = rd(light_from, "light") if light_from else rd(rid, "dark")
    return derived(src["value"], "color", desc + " Not captured in light: " + why, src["capture"])


def semantic(theme):
    f = lambda rid, desc, typ="color": from_reading(rid, theme, typ, desc)
    ranges = lambda ids: ", ".join(sorted({rd(r, theme)["value"] for r in ids if theme in READ[r]}))
    s = {"color": {
        "bg": {
            "page": f("bg.page", "New chat and chat threads; also bottom sheets and the Settings sheet, which use the same value."),
            "list": f("bg.list", "Pushed list and settings pages (Chats, Projects, Artifacts, Code, Time & focus): darker than the chat page in dark, the same as it in light."),
            "sidebar": f("bg.sidebar", "The sidebar, which slides over the page from the left."),
            "sheet": f("bg.sheet", "Bottom sheets (Select model, Effort, Add to Chat) and the Settings sheet."),
            "scrim": scrim(theme, "scrim.sheet"),
        },
        "surface": {
            "card": f("surface.card", "Grouped cards in Settings and in sheets (sheet cards read the same)."),
            "userBubble": f("surface.userBubble", "The owner's message bubble. Claude's replies have no bubble."),
            "glass": f("surface.composer", "The composer (glass), centre reading above the placeholder. The material tints with what is behind it."),
            "control": f("surface.control", "Controls inside the composer (+, model pill, microphone)."),
            "navGlass": f("surface.navGlass", "Round glass nav buttons, beside the icon."),
            "menu": f("surface.menu", "Pull-down and context menus (glass)."),
            "selected": dark_only(theme, "surface.selected", "The selected sidebar row.", "surface.control", "filled from surface.control, the closest light grey fill."),
            "badge": f("surface.badge", "Neutral badges (Beta, Recommended)."),
            "field": f("surface.field", "Pop-up select field."),
            "search": dark_only(theme, "surface.searchField", "Search field once typing.", "surface.control", "filled from surface.control."),
            "dayToggle": f("surface.dayToggle", "Day toggle circle, off. The reading includes the letter, so it is the dominant pixel."),
            "emptyIcon": dark_only(theme, "surface.emptyIcon", "Circle behind an empty-state icon: the card colour.", "surface.card", "filled from surface.card, which it matches in dark."),
        },
        "border": {
            "divider": f("border.divider", "Hairline between grouped rows, inset to the row text."),
            "field": f("border.field", "Rim of a pop-up select field."),
            "card": dark_only(theme, "border.listCard", "Rim of an artifact card, which has no fill of its own.", "border.divider", "filled from border.divider."),
            "grabber": f("border.grabber", "Sheet grabber."),
        },
        "text": {
            "primary": f("text.primary", f"Row labels, titles, the owner's bubble, menu items. Readings in this role: {ranges(('text.primary', 'text.onUserBubble', 'text.menuItem', 'text.wordmark'))}."),
            "response": f("text.response", "Claude's serif responses."),
            "greeting": f("text.greeting", "The serif greeting on a new chat: softer than primary text."),
            "secondary": f("text.secondary", f"The account line, sidebar section headers, unchosen tile labels, badge labels. Readings: {ranges(('text.secondary', 'text.sidebarSection', 'text.tileLabel', 'text.badge'))}."),
            "tertiary": f("text.tertiary", f"Subtitles, section headers, tool-step rows, action icons, row values, empty-state lines. Readings: {ranges(('text.tertiary', 'text.subtitle', 'text.sectionHeader', 'text.toolStep', 'text.actionIcon', 'text.rowValue', 'text.emptyTitle', 'text.listSubtitle'))}."),
            "placeholder": f("text.placeholder", "Composer placeholder."),
            "footnote": f("text.footnote", "The disclaimer under a response and list subtitles."),
            "chevron": f("text.chevron", "Disclosure chevrons on rows."),
            "disabled": f("text.disabled", "Title of a locked setting (Artifacts, required by code execution)."),
            "disabledSubtitle": f("text.disabledSubtitle", "Subtitle of a locked setting."),
            "link": f("text.link", "Action text in a card (Add account, Give the gift of Claude)."),
            "selected": tok(rd("text.selected" + theme.title(), theme)["value"], "color", "Label of the chosen Appearance tile.", rd("text.selected" + theme.title(), theme)["evidence"], rd("text.selected" + theme.title(), theme)["capture"]),
            "danger": f("text.destructive", "Destructive menu items (Delete): red text with a red icon, never a red fill."),
            "onPrimary": f("text.onPrimary", "Label on the inverse primary pill (Talk, New chat, Share)."),
            "onAccent": f("text.onAccent", "Arrow on the orange send button."),
        },
        "accent": {
            "default": f("accent.blue", "The interactive blue: switches on, the chosen-model tick, the chosen Appearance tile, usage meters."),
            "check": f("accent.check", "Tick on the chosen item in a sheet."),
            "brand": f("accent.brand", "Claude's spark above the greeting. The same in both themes."),
            "send": f("accent.send", "The send button once the composer has text. The same in both themes."),
            "filter": dark_only(theme, "accent.archive", "An active filter button (Archived), glass tinted orange.", None, "the dark value is used, as the brand orange is the same in both themes."),
        },
        "focus": {
            "caret": f("focus.caret", "Text caret in the composer: the only focus indicator seen (no ring)."),
        },
        "button": {
            "primary": {"bg": f("button.primary", "The inverse primary pill (Talk, New chat, New project, Share): near-white in dark, near-black in light."),
                        "text": f("text.onPrimary", "Label on the inverse primary pill.")},
            "control": {"bg": f("button.control", "Round + and microphone buttons and the model pill inside the composer.")},
            "send": {"bg": f("accent.send", "The orange send button."),
                     "glyph": f("text.onAccent", "Send arrow.")},
        },
        "switch": {
            "on": f("switch.on", "Switch on."),
            "onDisabled": f("switch.onDisabled", "Switch on, locked by another setting."),
            "off": f("switch.off", "Switch off track."),
            "thumb": f("switch.thumb", "Switch thumb."),
            "thumbDisabled": f("switch.thumbDisabled", "Switch thumb, locked (grey in dark, white in light)."),
        },
        "progress": {
            "fill": f("progress.fill", "Usage meter fill. The same in both themes."),
            "track": f("progress.track", "Usage meter track: a deep blue in dark, a pale blue in light."),
        },
        "badge": {
            "bg": f("surface.badge", "Neutral badge fill (Beta, Recommended)."),
            "text": f("text.badge", "Neutral badge label."),
            "warningBg": dark_only(theme, "surface.badgeUsage", "Amber badge that warns of higher usage ('5.5x or more usage').", None, "the dark value is used; the effort sheet was captured in dark only."),
            "warningText": dark_only(theme, "text.badgeUsage", "Label on the amber usage badge.", None, "the dark value is used; the effort sheet was captured in dark only."),
        },
        "status": {
            "danger": alias("color.text.danger", "color", "Danger: red text on destructive items. No danger fill was seen."),
            "warning": alias("color.badge.warningText", "color", "Warning: the amber usage badge. No other warning state was seen."),
            "info": alias("color.accent.default", "color", "Info: the interactive blue."),
        },
    }}
    s["$extensions"] = {"notTokenised": [
        "Success colour: no success state was seen",
        "Pressed states: stills only",
        "Streaming and loading states: no message was sent",
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
             "$description": "Settings > App > Appearance > Light, set for the capture and put back to System afterwards. Read from screenshots/light/."},
            {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"},
             "$description": "Settings > App > Appearance > System with the phone in dark mode. Read from screenshots/dark/."},
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
