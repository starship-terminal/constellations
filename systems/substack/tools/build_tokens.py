#!/usr/bin/env python3
"""Build tokens.json (W3C DTCG, Tokens Studio multi-set layout) from raw/readings.json (native kit).

Adapted from the native kit (tools/kit/native, from systems/grokbot): core() and semantic(), marked
PRODUCT (adapt), map Substack's readings to roles. The helpers, check() and build() are the kit's.

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
    ids = ["bg.page", "bg.grouped", "surface.card", "surface.sheet", "surface.raised", "surface.secondary",
           "surface.tile", "surface.glass", "border.divider", "border.dividerGrouped", "border.dividerSheet",
           "text.primary", "text.secondary", "text.tertiary", "text.placeholder", "text.optionValue",
           "control.progressTrack", "control.progressFill"]
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
    c["color"] = {
        "orange": from_reading("brand.primary", "dark", "color", f"Substack orange: the 'Turn on' button, 'Subscribe back', the unread dots, the light compose button and the badge on Chat. The same value in both themes (light reads {rd('brand.primary', 'light')['value']})."),
        "blue": from_reading("control.switchOn", "dark", "color", f"The system blue Substack keeps for controls: switches, the selected option rim, checklist ticks. The same value in both themes (light reads {rd('control.switchOn', 'light')['value']})."),
        "red": from_reading("text.danger", "dark", "color", "Destructive red: Report, Mute, Block, Disable all, and a liked heart."),
        "publicationBlue": from_reading("publication.button", "dark", "color", "The System Design Newsletter's own colour on its Subscribe buttons. Each publication brings its own; this is the only one read."),
        "neutral": neutral_ramp(),
    }
    rows = rd("rows.settings")["value"]
    runs = []                                   # dividers are two or three anti-aliased pixels; take each run's centre
    for y in rows:
        if runs and y - runs[-1][-1] <= 1:
            runs[-1].append(y)
        else:
            runs.append([y])
    centres = [sum(r) / len(r) for r in runs if len(r) >= 2 and 700 < r[0] < 860]
    if len(centres) < 2:
        raise ValueError(f"rows.settings: {len(centres)} dividers between y 700 and 860, need 2 for the row pitch")
    pitch = (centres[1] - centres[0]) / 2
    c["radius"] = {
        "card": derived("12px", "dimension", f"Grouped cards in Settings, the banner and the 'Find people' card. Diagonal-inset readings: Settings card {rd('radius.card')['value']}, empty-state card {rd('radius.cardEmpty')['value']}, 'Find people' card {rd('radius.raisedCard')['value']}. Plus or minus 2 pt."),
        "button": derived("12px", "dimension", f"Full-size buttons: 'Share' {rd('radius.buttonLarge')['value']}, 'Turn on' {rd('radius.buttonBanner')['value']}. Plus or minus 2 pt."),
        "publicationButton": derived("10px", "dimension", f"The publication's Subscribe button inside a post: {rd('radius.buttonPublication')['value']}."),
        "small": derived("7px", "dimension", f"Small buttons and checkboxes: 'Subscribe back' {rd('radius.buttonSmall')['value']}, checkbox {rd('radius.checkbox')['value']}."),
        "option": derived("8px", "dimension", f"Option buttons in Display Settings, read along the diagonal of the selected button's outer rim: {rd('radius.option')['value']}."),
        "sheet": derived("36px", "dimension", f"Top corners of a sheet: {rd('radius.sheet')['value']}."),
        "capsule": derived("999px", "dimension", "Fully round ends: the tab bar and its selected pill, the top tabs' selected pill, chips, the switch, the search fields, the nav bar's Subscribe pill, glass nav buttons and the compose button (a circle)."),
    }
    card = rd("size.card")["box"]
    c["space"] = {
        "base": derived("4px", "dimension", "Measured gaps land on multiples of 4 pt within a pixel or two."),
        "xs": derived("4px", "dimension", "Between an icon and its count under a note."),
        "sm": derived("8px", "dimension", "Between the title and the meta line of an inbox row, and between stacked buttons."),
        "md": derived("12px", "dimension", "Inside chips and option buttons, and between a row icon tile and its label."),
        "lg": derived("16px", "dimension", f"Screen margin: grouped cards start {(card[0] - 16) / 2:g} pt from the screen edge, and grouped cards sit 16 pt apart (rows.settings: 947 to 979 px)."),
        "xl": derived("24px", "dimension", "Between feed items and above a section title."),
        "screenMargin": alias("space.lg", "dimension", "Left and right margin of cards, rows, notes and post text (notes start at 16 to 17 pt, post text at 20 pt)."),
    }
    sw = rd("size.switch")["value"]
    c["size"] = {
        "row": tok(px(pitch), "dimension", "Grouped settings row, divider to divider.", "Sampled", rd("rows.settings")["capture"]),
        "tabBar": {
            "height": tok(px(pt_of("size.tabBar.h")), "dimension", "Floating glass tab bar, rim included.", "Sampled", rd("size.tabBar.h")["capture"]),
            "width": tok(px(round(pt_of("size.tabBar.w"))), "dimension", f"Floating tab bar width ({rd('size.tabBar.w')['value']}): 22 pt in from each screen edge.", "Sampled", rd("size.tabBar.w")["capture"]),
            "item": tok(px(round(pt_of("size.tabBarItem", "dark", 1))), "dimension", f"Height of the selected item's pill inside the bar ({rd('size.tabBarItem')['value']} dark, {rd('size.tabBarItem', 'light')['value']} light; glass edges make the width vary).", "Sampled", rd("size.tabBarItem")["capture"]),
        },
        "navButton": tok(px(round(pt_of("size.navButton"))), "dimension", f"Round glass back, close and more buttons ({rd('size.navButton')['value']} dark, rim included).", "Sampled", rd("size.navButton")["capture"]),
        "fab": tok(px(round(pt_of("size.fab"))), "dimension", f"Orange compose button, a circle ({rd('size.fab')['value']}).", "Sampled", rd("size.fab")["capture"]),
        "button": tok(px(round(pt_of("size.buttonLarge", "dark", 1))), "dimension", f"Paired full-width buttons on the profile (Share, Edit): {rd('size.buttonLarge')['value']}.", "Sampled", rd("size.buttonLarge")["capture"]),
        "buttonBanner": tok(px(round(pt_of("size.buttonBanner", "dark", 1))), "dimension", f"Buttons inside the banner (Later, Turn on): {rd('size.buttonBanner')['value']}.", "Sampled", rd("size.buttonBanner")["capture"]),
        "buttonPublication": tok(px(round(pt_of("size.buttonPublication", "dark", 1))), "dimension", f"The publication's Subscribe button inside a post: {rd('size.buttonPublication')['value']}.", "Sampled", rd("size.buttonPublication")["capture"]),
        "buttonSmall": tok(px(round(pt_of("size.buttonSmall", "dark", 1))), "dimension", f"Small inline buttons on activity rows (Subscribe back, Message): {rd('size.buttonSmall')['value']}.", "Sampled", rd("size.buttonSmall")["capture"]),
        "navPill": tok(px(round(pt_of("size.navSubscribe", "dark", 1))), "dimension", f"The Subscribe pill in the reader's nav bar: {rd('size.navSubscribe')['value']}.", "Sampled", rd("size.navSubscribe")["capture"]),
        "searchField": tok(px(round(pt_of("size.searchField", "dark", 1))), "dimension", f"Search fields (Chat, Search): {rd('size.searchField')['value']}.", "Sampled", rd("size.searchField")["capture"]),
        "chip": tok(px(round(pt_of("size.chip", "dark", 1))), "dimension", f"Search topic chips: {rd('size.chip')['value']} for 'Suggested'.", "Sampled", rd("size.chip")["capture"]),
        "tab": tok(px(pt_of("size.tabSelected.h")), "dimension", f"Selected pill behind a top tab ('For you' is {rd('size.tabSelected.w')['value']} wide).", "Sampled", rd("size.tabSelected.h")["capture"]),
        "option": tok(px(round(pt_of("size.option", "dark", 1))), "dimension", f"Option buttons in Display Settings, fill inside the rim: {rd('size.option')['value']}.", "Sampled", rd("size.option")["capture"]),
        "switch": {
            "width": tok(px(round(pt_of("size.switch"))), "dimension", f"Switch track ({sw}).", "Sampled", rd("size.switch")["capture"]),
            "height": tok(px(round(pt_of("size.switch", "dark", 1))), "dimension", f"Switch track height ({sw}).", "Sampled", rd("size.switch")["capture"]),
        },
        "checkbox": tok(px(round(pt_of("size.checkbox"))), "dimension", f"Checkbox in the notification grid: {rd('size.checkbox')['value']}.", "Sampled", rd("size.checkbox")["capture"]),
        "avatarStory": tok(px(pt_of("size.avatarStory")), "dimension", "Publication avatar in the top row of Home (a rounded square of the publication's artwork).", "Sampled", rd("size.avatarStory")["capture"]),
        "thumbnail": tok(px(round(pt_of("size.thumbnail.w"))), "dimension", f"Post thumbnail at the end of an inbox row: {rd('size.thumbnail.w')['value']} by {rd('size.thumbnail.h')['value']}.", "Sampled", rd("size.thumbnail.w")["capture"]),
        "raisedRow": tok(px(round(pt_of("size.raisedRow", "dark", 1))), "dimension", f"Full-width raised row ('View saved notes'): {rd('size.raisedRow')['value']}.", "Sampled", rd("size.raisedRow")["capture"]),
        "progress": tok(px(round(pt_of("size.progress"))), "dimension", f"Reading-progress bar width ({rd('size.progress')['value']} at tolerance 20; the solid core is about 2.5 pt tall).", "Sampled", rd("size.progress")["capture"]),
        "touchTarget": derived("44px", "dimension", "Rows, nav buttons, the tab bar items and the search field are 44 pt or more. Small buttons (31 pt), chips (35 pt), top tabs (26 pt) and checkboxes (23 pt) are smaller and sit inside taller rows."),
    }
    c["border"] = {"width": {
        "hairline": derived("0.5px", "dimension", "Dividers between rows and the rim of raised rows: one device pixel at 2x, anti-aliased over two or three capture pixels."),
        "option": derived("1px", "dimension", "Rim of an unselected option button: two capture pixels."),
        "optionSelected": derived("2px", "dimension", "Rim of the selected option button: four capture pixels."),
    }}
    c["fontFamily"] = {
        "base": tok("system", "fontFamily", "Not determinable from pixels. A neo-grotesque sans for the whole interface, heavier in titles; use the platform font.", "Not captured", MEASURED),
        "reader": derived("New York", "fontFamily", "The serif for post bodies. The app names it: Display Settings > Article font lists New York (selected), Messina and Tiempos. The style guide falls back to the platform serif.", rd("type.readerBody")["capture"]),
    }
    c["fontWeight"] = {
        "regular": derived(400, "fontWeight", "Note and post text, subtitles, meta lines. Judged by stroke width, not measured."),
        "medium": derived(500, "fontWeight", "Top tabs, chips and tab bar labels. Judged by stroke width."),
        "semibold": derived(600, "fontWeight", "Row titles, settings rows, nav and sheet titles, button labels, names on notes. Judged by stroke width."),
        "bold": derived(700, "fontWeight", "Tab screen titles, section titles and the Settings title. Judged by stroke width."),
        "heavy": derived(800, "fontWeight", "Post titles in the reader. Judged by stroke width."),
    }

    def ty(size_rid, weight, lh, desc, extra=(), family="base"):
        sizes = [rd(r)["value"] for r in (size_rid,) + tuple(extra)]
        v = {"fontFamily": "{fontFamily.%s}" % family, "fontWeight": "{fontWeight.%s}" % weight,
             "fontSize": sizes[0].replace("pt", "px")}
        if lh:
            v["lineHeight"] = lh
        return tok(v, "typography", desc + f" Cap-height readings: {', '.join(sorted(set(sizes)))}.", "Derived", rd(size_rid)["capture"])

    lines = lambda rid: f"{round(float(rd(rid)['value'].rstrip('pt')))}px"
    c["typography"] = {
        "largeTitle": ty("type.largeTitle", "bold", None, "The Settings sheet title."),
        "screenTitle": ty("type.screenTitle", "bold", None, "Tab screen titles (Read, Podcasts, Chat, Activity)."),
        "postTitle": ty("type.postTitle", "heavy", None, "A post's title in the reader."),
        "sectionTitle": ty("type.sectionTitle", "bold", None, "Section titles (Your inbox, Next up, Your shows).", ("type.sectionTitleB",)),
        "reader": ty("type.readerBody", "regular", lines("lines.readerBody"), "Post body text, in the reader serif.", family="reader"),
        "postSubtitle": ty("type.postSubtitle", "regular", lines("lines.postSubtitle"), "A post's subtitle under its title."),
        "headline": ty("type.rowTitle", "semibold", None, "Inbox and search row titles, settings rows, nav and sheet titles, button labels, menu items, the banner title, the Listen pill.", ("type.settingsRow", "type.navTitle", "type.sheetTitle", "type.button", "type.searchTitle", "type.bannerTitle", "type.menuItem", "type.listen")),
        "body": ty("type.noteBody", "regular", lines("lines.noteBody"), "Note text in the feed and the profile bio."),
        "link": ty("type.link", "semibold", None, "Link buttons in a grouped card (Restore in-app purchases) and empty-state titles.", ("type.emptyTitle",)),
        "subheadline": ty("type.tabActive", "medium", None, "Top tabs and topic chips.", ("type.tabInactive", "type.chip")),
        "footnote": ty("type.meta", "regular", lines("lines.footnote"), "Publication names, read times, dates, bylines, search result subtitles, the banner subtitle, helper text under cards.", ("type.searchSubtitle", "type.byline", "type.bannerSubtitle", "type.podcastMeta", "type.helper")),
        "kicker": ty("type.kicker", "semibold", None, "Upper-case publication name above a post title and the byline names (text case is not a DTCG property)."),
        "caption": ty("type.tabBar", "medium", lines("lines.rowSubtitle"), "Tab bar labels, upper-case grouped section headers and settings row subtitles.", ("type.sectionHeader", "type.rowSubtitle")),
    }
    c["$extensions"] = {"notTokenised": [
        "iOS 26 glass (the tab bar, nav buttons, the selected top tab, the nav bar's Subscribe pill): blur and refraction come from the system material",
        "Continuous (squircle) corners: DTCG has no value for corner smoothing",
        "Motion and easing: stills only",
        "Shadows: only the light banner shows a soft one, too faint to read as a value",
        "Text case: section headers, the kicker and the byline are upper case",
        "Per-publication colour: each publication's Subscribe buttons take its own colour; color.publicationBlue is one example",
    ]}
    return c


# ---------------------------------------------------------------- semantic sets

def scrim(theme):
    ref, dim = rd("scrim.ref", theme)["value"], rd("scrim.sheet", theme)["value"]
    a = 1 - int(dim[1:3], 16) / int(ref[1:3], 16)
    return derived("#000000%02X" % round(a * 255), "color",
                   f"Black at {round(a * 100)}%: the post reader reads {ref} undimmed and {dim} under the Options sheet.",
                   rd("scrim.sheet", theme)["capture"])


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
            "page": f("bg.page", "Tab screens (Home, Read, Search, Podcasts, Chat, Activity) and the post reader."),
            "grouped": f("bg.grouped", "The Settings sheet and its pushed pages, behind grouped cards." + (" Lighter than the cards in dark, the reverse of iOS's grouped style." if theme == "dark" else "")),
            "scrim": scrim(theme),
        },
        "surface": {
            "card": f("surface.card", "Grouped cards on the Settings sheet and its pages: the page colour, set on bg.grouped."),
            "sheet": f("surface.sheet", "Options and Display Settings sheets, and the notifications pre-prompt."),
            "raised": f("surface.raised", "Full-width raised rows on a page ('View saved notes', 'Find people you know')."),
            "banner": f("surface.banner", "The 'Notifications are off' banner card in Chat."),
            "secondary": f("surface.secondary", "Secondary buttons on a card ('Later')."),
            "tile": f("surface.tile", "Small tiles and pills on a page: Creator stats, the Listen pill, the '1 recommendation' chip, unselected chips."),
            "iconTile": f("surface.iconTile", "Rounded tile behind each settings row icon."),
            "glass": f("surface.glass", "Glass controls over a flat page (search fields); the tab bar and nav buttons use the same material."),
            "tabBar": f("surface.tabBar", "Floating tab bar, centre reading."),
            "tabBarSelected": f("surface.tabBarSelected", "Pill behind the selected tab bar item: darker than the bar in dark, a grey in light."),
            "tabSelected": f("surface.tabSelected", "Glass pill behind the selected top tab ('For you', 'Saved', 'All')."),
            "chipSelected": f("surface.chipSelected", "Fill of the selected topic chip: the theme's ink (white in dark, near-black in light)."),
            "optionSelected": f("surface.optionSelected", "Fill of the selected option button: a faint blue tint."),
            "highlight": f("surface.highlight", "Highlight behind the matched word in search results."),
            "tintOrange": dark_only(theme, "surface.promptButton", "Orange-tinted fill behind orange content: the 'Enable notifications' button on the pre-prompt.", "surface.activityIcon", "filled from the orange-tinted circle behind a subscribe activity's + icon, the same role."),
            "tintOrangeIcon": f("surface.activityIcon", "Circle behind the orange + on a subscribe activity row."),
            "tintPurpleIcon": f("surface.activityIconNote", "Circle behind the purple sparkle on a first-note activity row."),
        },
        "border": {
            "divider": f("border.divider", "Hairline between feed and inbox rows."),
            "grouped": f("border.dividerGrouped", "Hairline between rows in a grouped card, inset to the row text."),
            "sheet": f("border.dividerSheet", "Hairline under a sheet header and between groups of sheet items."),
            "raised": f("border.raised", "Rim of a raised row or card on a page."),
            "option": f("border.option", "Rim of an unselected option button (Messina, Tiempos)."),
            "outline": f("border.outlineButton", "Rim of an outlined button ('Message'): barely visible."),
        },
        "text": {
            "primary": f("text.primary", "Titles, row titles, note text, settings labels." + (" Not black: a dark grey." if theme == "light" else "")),
            "reader": f("text.reader", "Serif post body."),
            "secondary": f("text.secondary", f"Post subtitles, the kicker, byline dates, the profile handle, note action icons. Readings in this role range {', '.join(sorted({rd(r, theme)['value'] for r in ('text.secondary', 'text.kicker', 'text.byline', 'text.handle', 'text.noteAction')}))}."),
            "tertiary": f("text.tertiary", f"Publication names and meta lines on rows, dates, section headers, unselected tabs, row subtitles, the account email. Readings range {', '.join(sorted({rd(r, theme)['value'] for r in ('text.tertiary', 'text.meta', 'text.date', 'text.sectionHeader', 'text.tabInactive', 'text.rowSubtitle', 'text.email', 'text.seeAll', 'text.optionInactive')}))}."),
            "quaternary": f("text.optionValue", "The current value beside a Display Settings header ('NEW YORK')."),
            "placeholder": f("text.placeholder", f"Search field placeholders (the Search screen reads {rd('text.placeholderSearch', theme)['value']})."),
            "footnote": f("text.footnote", "Helper text under a grouped card."),
            "onBrand": f("text.onBrand", "Labels on orange buttons."),
            "onPublication": f("text.onPublication", "Labels on the publication-coloured Subscribe button."),
            "link": f("text.link", f"Link buttons ('Restore in-app purchases'); inline links read {rd('text.linkInline', theme)['value']}."),
            "highlight": f("text.highlight", "Matched word in search results, on surface.highlight."),
            "selected": f("text.selected", "Label of the selected option button."),
            "danger": f("text.danger", f"Destructive items (Report, Mute, Block) and buttons ('Disable all' reads {rd('text.dangerButton', theme)['value']}): red text, never a red fill."),
            "brand": f("text.brand", "Orange 'Subscribe' link on a note header."),
            "tabActive": f("text.tabActive", "Selected top tab label."),
            "chipSelected": f("text.chipSelected", "Label on the selected topic chip, the inverse of the theme."),
            "tabBar": f("text.tabBarInactive", "Tab bar labels and icons."),
            "tabBarSelected": f("text.tabBarActive", "The selected tab bar item's label, on its pill."),
        },
        "accent": {
            "brand": f("brand.primary", "Primary actions: 'Turn on', 'Subscribe back'. Substack orange."),
            "brandFab": f("brand.fab", "The floating compose button."),
            "brandShare": f("brand.share", "'Share' on the owner's profile: a lighter orange than the primary."),
            "dot": f("brand.dot", "Unread dots on publication avatars, inbox rows and chats; the badge on the Chat tab."),
            "control": f("control.switchOn", "Switches, checklist ticks and the selected option: the system blue, never orange."),
            "publication": f("publication.button", "A publication's own colour, on its Subscribe buttons in a post. Varies by publication."),
            "publicationGlass": f("publication.navPill", "The same colour as a glass pill in the reader's nav bar."),
        },
        "focus": {
            "caret": f("focus.caret", "Text caret in a focused search field: the primary text colour, not a tint. The only focus indicator captured."),
        },
        "control": {
            "switchOn": alias("color.accent.control", "color", "Switch track, on."),
            "switchThumb": f("control.switchThumb", "Switch thumb."),
            "optionRim": f("control.optionBorder", "Rim of the selected option button."),
            "check": f("text.check", "Tick on the chosen row of a checklist (Theme, Default tab)."),
            "checkbox": f("control.checkbox", "Checked checkbox: the theme's ink (white in dark, near-black in light)."),
            "checkboxTick": f("control.checkboxTick", "Tick inside a checked checkbox."),
            "progressTrack": f("control.progressTrack", "Reading-progress track on a saved post."),
            "progressFill": f("control.progressFill", "Reading-progress fill: a grey, not an accent."),
        },
        "status": {
            "danger": alias("color.text.danger", "color", "Danger: red text on destructive items, and a liked heart. No danger fill was seen."),
            "info": alias("color.text.link", "color", "Info: link blue."),
        },
    }}
    s["$extensions"] = {"notTokenised": [
        "Success and warning colours: the warning banner draws its triangle in the primary text colour; no success state was seen",
        "Pressed states: stills only",
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
        "$themes": [
            {"id": "light", "name": "Day", "selectedTokenSets": {"core": "source", "light": "enabled"},
             "$description": "Settings > Appearance > Theme > Day, set for the capture and put back to System afterwards. Read from screenshots/light/."},
            {"id": "dark", "name": "Night", "selectedTokenSets": {"core": "source", "dark": "enabled"},
             "$description": "Settings > Appearance > Theme > System with the phone in dark mode (the app's Night look). Read from screenshots/dark/."},
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
