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
    ids = ["bg.page", "bg.sheetAccount", "surface.card", "surface.cardSuggestion", "surface.cardUsage", "surface.cardAccount",
           "surface.bubble", "surface.bubbleLight", "surface.glass", "surface.tile", "border.divider", "text.primary",
           "text.menuItem", "text.rowSubtitle", "text.sectionHeader", "text.menuSubtitle", "text.placeholder",
           "text.searchPlaceholder", "button.primary"]
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
    """Width in pt of a find reading: its first to its last position."""
    v = rd(rid, theme)["value"]
    return (v[-1] - v[0] + 1) / 2


# PRODUCT (adapt) from here to semantic()'s end: the mapping from readings to tokens.
def core():
    c = {}
    c["color"] = {"neutral": neutral_ramp()}
    c["radius"] = {
        "card": derived("26px", "dimension", f"Grouped settings cards: diagonal-inset reading {rd('radius.card')['value']} in both themes. Plus or minus 2 pt."),
        "cardSuggestion": derived("24px", "dimension", f"Suggestion and notebook cards: {rd('radius.cardSuggestion')['value']} in both themes."),
        "bubble": derived("40px", "dimension", f"The owner's message bubble: {rd('radius.bubble')['value']} dark, {rd('radius.bubbleLight', 'light')['value']} light, on a {rd('size.bubble')['value'].split('x')[1]} two-line bubble. Read on two lines only; a one-line bubble may be a capsule."),
        "menu": derived("29px", "dimension", f"Pull-down and pop-up menus (iOS 26 glass): {rd('radius.menu')['value']}."),
        "sheet": derived("38px", "dimension", f"Top corners of a sheet: {rd('radius.sheet')['value']} on the account sheet."),
        "capsule": derived("999px", "dimension", f"Fully round ends: the composer ({rd('radius.composer')['value']} on a 70 pt capsule), the account sheet's row cards ({rd('radius.cardAccount')['value']} on 54 pt), buttons, the Chat / Task pill, switches, the PRO badge, glass nav buttons and the search field."),
    }
    card = rd("size.card")["box"]
    sug = rd("size.cardSuggestion")["box"]
    bub = rd("size.bubble")["box"]
    c["space"] = {
        "xs": derived("4px", "dimension", "Gap between a row title and its subtitle, and inside badges."),
        "sm": derived("8px", "dimension", "Gap between the composer's controls."),
        "md": derived("12px", "dimension", "Gap between stacked cards: suggestion cards and the account sheet's row cards sit 12.5 pt apart."),
        "lg": derived("16px", "dimension", f"Screen margin: grouped and suggestion cards start {(card[0] - 16) / 2:g} pt from the screen edge, the reply text 24 pt."),
        "xl": derived("20px", "dimension", f"Inner padding of a suggestion card: its title starts {(88 - sug[0]) / 2:g} pt from the card edge."),
        "xxl": derived("28px", "dimension", f"Inner horizontal padding of the owner's bubble: text starts {(168 - bub[0]) / 2:g} pt from its edge."),
        "screenMargin": alias("space.lg", "dimension", "Left and right margin of cards, menus and the composer when typing."),
    }
    voice = rd("size.card")["box"]
    voice_div = rd("border.divider")["args"][1]
    rows = rd("rows.settings")["value"]
    pitch = (rows[4] - rows[0]) / 2 if len(rows) >= 5 else 54
    c["size"] = {
        "row": tok(px(pitch), "dimension", "Single-line settings row, divider to divider (rows.settings: dividers every 108 px).", "Sampled", rd("rows.settings")["capture"]),
        "rowSubtitle": derived(px((voice_div - voice[1]) / 2), "dimension", f"Settings row with a one-line subtitle (Gemini's voice): the Voice card's top edge (y {voice[1]}) to its divider (y {voice_div}).", rd("size.card")["capture"]),
        "rowSubtitleTwoLine": derived(px((voice[3] + 1 - voice_div) / 2), "dimension", f"Settings row with a two-line subtitle (Interrupt Live responses): the Voice card's divider (y {voice_div}) to its bottom edge (y {voice[3]}).", rd("size.card")["capture"]),
        "sidebarRow": derived(px(round(float(rd("lines.sidebar")["value"].rstrip("pt")))), "dimension", f"Sidebar row pitch: {rd('lines.sidebar')['value']} between label tops."),
        "searchRow": derived(px(round(float(rd("lines.search")["value"].rstrip("pt")))), "dimension", f"Search result row pitch: {rd('lines.search')['value']}."),
        "menuRow": derived(px(round(float(rd("lines.menu")["value"].rstrip("pt")))), "dimension", f"Single-line menu item pitch: {rd('lines.menu')['value']}. The model picker's two-line items are 60 pt."),
        "navButton": tok(px(pt_of("size.navButton.w")), "dimension", f"Round glass menu, close and back buttons (a circle; {rd('size.navButton.h')['value']} tall with the rim's soft edge). The account avatar beside them is the same size.", "Sampled", rd("size.navButton.w")["capture"]),
        "composer": {
            "height": tok(px(span("size.composer.h")), "dimension", "Composer capsule height, empty or typed.", "Sampled", rd("size.composer.h")["capture"]),
            "width": tok(px(span("size.composer.w")), "dimension", "Composer width while empty: it floats inset from the margins.", "Sampled", rd("size.composer.w")["capture"]),
            "widthTyped": tok(px(span("size.composerTyped.w")), "dimension", "Composer width once text is typed: it widens to the screen margins.", "Sampled", rd("size.composerTyped.w")["capture"]),
        },
        "sendButton": tok(px(pt_of("size.sendButton.w")), "dimension", f"Send and voice buttons inside the composer: circles ({rd('size.sendButton.h')['value']} tall, voice {rd('size.voiceButton.w')['value']} wide).", "Sampled", rd("size.sendButton.w")["capture"]),
        "segment": {
            "width": tok(px(span("size.segment.w", "light")), "dimension", "Selected pill of the Chat / Task toggle (white interior, rim excluded).", "Sampled", rd("size.segment.w", "light")["capture"]),
            "height": tok(px(span("size.segment.h", "light")), "dimension", "Selected pill of the Chat / Task toggle.", "Sampled", rd("size.segment.h", "light")["capture"]),
        },
        "button": tok(px(round(pt_of("size.primaryButton", "dark", 1))), "dimension", f"Full-width primary button (Get started, Try it): {rd('size.primaryButton')['value']}.", "Sampled", rd("size.primaryButton")["capture"]),
        "buttonTonal": tok(px(round(pt_of("size.tonalButton", "dark", 1))), "dimension", f"Filled capsule button with an icon (Add): {rd('size.tonalButton')['value']}.", "Sampled", rd("size.tonalButton")["capture"]),
        "buttonSignIn": tok(px(pt_of("size.signInButton", "dark", 1)), "dimension", f"Google sign-in button at onboarding: {rd('size.signInButton')['value']}, a rounded rectangle, not a capsule.", "Sampled", rd("size.signInButton")["capture"]),
        "switch": {
            "width": tok(px(pt_of("size.switch")), "dimension", "Material switch (Memory): track width, anti-aliased edge excluded.", "Sampled", rd("size.switch")["capture"]),
            "height": tok(px(pt_of("size.switch", "dark", 1)), "dimension", "Material switch: track height.", "Sampled", rd("size.switch")["capture"]),
        },
        "switchSystem": {
            "width": tok(px(pt_of("size.switchSystem")), "dimension", "iOS switch (Voice): track width, anti-aliased edge excluded.", "Sampled", rd("size.switchSystem")["capture"]),
            "height": tok(px(pt_of("size.switchSystem", "dark", 1)), "dimension", "iOS switch: track height.", "Sampled", rd("size.switchSystem")["capture"]),
        },
        "rowCard": tok(px(pt_of("size.cardAccount", "dark", 1)), "dimension", f"Capsule row card on the account sheet: {rd('size.cardAccount')['value']}.", "Sampled", rd("size.cardAccount")["capture"]),
        "suggestionCard": tok(px(round(pt_of("size.cardSuggestion", "dark", 1))), "dimension", f"Suggestion card with a title and a two-line description: {rd('size.cardSuggestion')['value']} dark, {rd('size.cardSuggestion', 'light')['value']} light.", "Sampled", rd("size.cardSuggestion")["capture"]),
        "mediaCard": tok(px(pt_of("size.videoCard.w")), "dimension", "Video result card in a thread: its width, 24 pt from the left edge.", "Sampled", rd("size.videoCard.w")["capture"]),
        "menuWidth": tok(px(pt_of("size.menu.w")), "dimension", f"Pull-down menu width ({rd('size.menu.w')['value']}); the model picker is {rd('size.menu.h')['value']} tall with four models and a Thinking level row.", "Sampled", rd("size.menu.w")["capture"]),
        "grabber": {
            "width": tok(px(pt_of("size.grabber.w")), "dimension", "Sheet grabber width.", "Sampled", rd("size.grabber.w")["capture"]),
            "height": tok(px(pt_of("size.grabber.h")), "dimension", "Sheet grabber height.", "Sampled", rd("size.grabber.h")["capture"]),
        },
        "touchTarget": derived("44px", "dimension", "Nav buttons, sidebar rows and the composer are 44 pt or more. The send and voice circles (40 pt), the Add button (39 pt) and the Chat / Task pill (29 pt) are smaller and sit in larger hit areas or rows."),
    }
    c["border"] = {"width": {
        "hairline": derived("0.5px", "dimension", "Dividers between grouped rows: one device pixel at 2x (border.divider reads a one-pixel row)."),
    }}
    c["fontFamily"] = {"base": derived(["Google Sans", "-apple-system", "system-ui", "sans-serif"], "fontFamily", "Identified by eye from the letterforms (the round geometric G, a, y and the tittle shapes), not read from the app. Google's own typeface; it is not committed here, so the stack falls back to the platform sans.")}
    c["fontWeight"] = {
        "regular": derived(400, "fontWeight", "Greetings, titles, body, rows, menus. Judged by stroke width, not measured."),
        "medium": derived(500, "fontWeight", "Card titles, usage titles, the empty-state title, the PRO and Pro badges, nav titles. Judged by stroke width."),
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
        "display": ty("type.greeting", "regular", lines("lines.greeting"), "The greeting on home and onboarding ('Let's jump in'), centred; the Task greeting wraps on this line height.", ("type.onboarding", "type.taskGreeting")),
        "titleLarge": ty("type.largeTitle", "regular", None, "Page titles: Settings, the Students and Memory headers. The 'S' has an overshoot, so the reading may be a point high.", ("type.pageTitle",)),
        "title": ty("type.navTitle", "medium", None, "Nav titles in a sheet ('Voice', 'Usage limits', 'Scheduled')."),
        "body": ty("type.body", "regular", lines("lines.body"), "Gemini's replies, the owner's bubble, composer text, settings and sidebar rows, search results, card titles, button labels.", ("type.bubble", "type.composer", "type.rowTitle", "type.sidebarItem", "type.searchRow", "type.cardTitle", "type.button", "type.sidebarHeader")),
        "bodyStrong": ty("type.emptyTitle", "medium", None, "Empty-state titles ('No results') and card titles in bold ('Learning tailored to you')."),
        "callout": ty("type.menuItem", "regular", None, "Menu items."),
        "subheadline": ty("type.subtitle", "regular", lines("lines.subtitle"), "Row subtitles, section headers, card descriptions, empty-state lines; medium for usage titles and the PRO badge.", ("type.sectionHeader", "type.cardBody", "type.emptyBody", "type.usageTitle", "type.badge")),
        "footnote": ty("type.disclaimer", "regular", None, "The disclaimer under a thread ('Gemini is AI and can make mistakes')."),
        "caption": ty("type.segment", "regular", None, "Labels in the Chat / Task toggle."),
        "caption2": ty("type.menuSubtitle", "regular", None, "Model descriptions in the model picker ('Fastest answers')."),
    }
    c["$extensions"] = {"notTokenised": [
        "The home glow: a radial gradient rising from the bottom edge, blue in Chat and purple in Task (bg.glow and bg.glowTask hold its edge colour only)",
        "iOS 26 glass (nav buttons, the composer, menus, the + sheet, the search field): blur and refraction come from the system material",
        "The Gemini spark and the multicolour avatar ring at sign-in: artwork, not kept",
        "Continuous (squircle) corners: DTCG has no value for corner smoothing",
        "Motion and easing: stills only",
        "Shadows: light theme shows soft shadows under the composer, the segment pill and menus; they were not measured",
    ]}
    return c


# ---------------------------------------------------------------- semantic sets

def scrim(theme):
    ref, dim = (rd("scrim.refDark", "dark"), rd("scrim.dimDark", "dark")) if theme == "dark" else (rd("scrim.refLight", "light"), rd("scrim.dimLight", "light"))
    a = 1 - int(dim["value"][1:3], 16) / int(ref["value"][1:3], 16)
    what = "the menu button's glass" if theme == "dark" else "the home page"
    return derived("#000000%02X" % round(a * 255), "color",
                   f"Black at {round(a * 100)}%: {what} reads {ref['value']} undimmed and {dim['value']} under the + sheet." + (" The dark page itself is black, so only a lighter control shows the scrim." if theme == "dark" else ""),
                   dim["capture"])


def dark_only(theme, rid, desc, light_from=None, why=""):
    """A role read in dark only. Light reuses the dark value (light_from None) or the light value of
    the closest role, as Derived, and says which."""
    if theme == "dark":
        return from_reading(rid, "dark", "color", desc)
    src = rd(light_from, "light") if light_from else rd(rid, "dark")
    return derived(src["value"], "color", desc + " Not captured in light: " + why, src["capture"])


def light_only(theme, rid, desc, why):
    """A role read in light only; dark reuses the light value, as Derived, and says so."""
    if theme == "light":
        return from_reading(rid, "light", "color", desc)
    src = rd(rid, "light")
    return derived(src["value"], "color", desc + " Not read in dark: " + why, src["capture"])


def semantic(theme):
    f = lambda rid, desc, typ="color": from_reading(rid, theme, typ, desc)
    pick = lambda d, l: d if theme == "dark" else l
    onboarding = "onboarding was captured in dark only (the app was set to light afterwards, from Settings)"
    s = {"color": {
        "bg": {
            "page": f("bg.page", "Home, chat threads, search, the sidebar and pushed pages. Pure black in dark."),
            "sheet": f("bg.sheet", "Settings and Usage sheets: the page colour."),
            "sheetAccount": f("bg.sheetAccount", "The account sheet: a tinted grey, unlike the other sheets."),
            "glow": f("bg.glow", "Bottom edge of the glow behind the home composer (Chat mode)."),
            "glowTask": f("bg.glowTask", "Bottom edge of the glow in Task mode: purple instead of blue."),
            "scrim": scrim(theme),
        },
        "surface": {
            "card": f("surface.card", "Grouped settings cards (Account, Preferences, Voice)."),
            "raised": f("surface.cardSuggestion", "Suggestion cards (Scheduled) and the study-notebook card (Students); the usage progress track."),
            "container": f(pick("surface.bubble", "surface.bubbleLight"), "The owner's message bubble, the Usage cards and the PRO badge: a step off the page."),
            "rowCard": f("surface.cardAccount", "Capsule row cards on the account sheet (Manage your Google Account, Settings)."),
            "selected": dark_only(theme, "surface.navSelected", "Current row in the sidebar (New chat): a full-width capsule.", "surface.bubbleLight", "the light sidebar was scrolled past it, so the light container colour is used."),
            "composer": f("surface.composer", "Composer capsule (glass), centre reading."),
            "glass": f("surface.glass", "Round glass buttons (menu, close, back, new chat) and the search field, centre reading. The material tints with what is behind it."),
            "segment": f("surface.segment", "Selected pill of the Chat / Task toggle: black in dark, white in light."),
            "menu": f("surface.menu", "Pull-down menus (model picker, chat menu), glass. The reading picks up what is behind the menu."),
            "menuPopup": f(pick("surface.menuPopupDark", "surface.menuPopup"), "Pop-up select menu over a card (Theme)."),
            "sheetPlus": f("surface.sheetPlus", "The + sheet: glass over the page, tinted by the glow."),
            "tile": f("surface.tile", "Large tiles at the top of the + sheet (Photos, Camera, Avatar)."),
            "track": f("surface.track", "Usage progress track (0% used): the raised colour inside a container card."),
            "signIn": dark_only(theme, "surface.signIn", "Google sign-in sheet at onboarding.", "surface.card", onboarding + "; the light card colour is used."),
        },
        "border": {
            "divider": f("border.divider", "Hairline between grouped rows, inset to the row text. Cards have no rim."),
        },
        "text": {
            "primary": f("text.primary", f"Greetings, replies, the owner's bubble, row titles (reply text reads {rd(pick('text.body', 'text.bodyLight'), theme)['value']})."),
            "onGlass": f("text.menuItem", f"Labels on glass: menu items and the Chat / Task labels (Task reads {rd('text.segmentOff', theme)['value']}). A touch brighter than text.primary in dark."),
            "secondary": f("text.rowSubtitle", f"Row subtitles and card descriptions. Readings in this role range {', '.join(sorted({rd(r, theme)['value'] for r in ('text.rowSubtitle', 'text.cardBody', 'text.modelName')}))}."),
            "tertiary": f("text.sectionHeader", f"Section headers, timestamps, helper lines, the disclaimer. Readings range {', '.join(sorted({rd(r, theme)['value'] for r in ('text.sectionHeader', 'text.timestamp', 'text.helper') + (('text.disclaimer',) if theme == 'dark' else ())}))}."),
            "onMenuSecondary": f("text.menuSubtitle", "Model descriptions inside the model picker (on glass)."),
            "placeholder": f("text.placeholder", "Composer placeholder ('Ask Gemini', 'Describe task')."),
            "placeholderSearch": f("text.searchPlaceholder", "Search field placeholder, on glass."),
            "link": f("text.link", "Inline links ('Learn more'): the same bright blue in both themes."),
            "action": f("text.action", "Text buttons in a sheet header ('Done'): the Material primary blue."),
            "badge": f("text.badge", "Label of the PRO badge."),
            "danger": f("text.danger", "Destructive menu items (Delete): red text and a red icon, never a red fill."),
        },
        "accent": {
            "primary": f("button.tonal", "Google's Material primary: filled buttons (Add), the Material switch, the Done text. Light blue in dark, deep blue in light."),
            "onPrimary": f("button.tonalLabel", "Label and icon on accent.primary."),
            "bright": f("text.link", "The bright system-style blue: links, the iOS switch, the dot after the model name, the avatar ring. One value in both themes."),
            "dot": dark_only(theme, "accent.dot", "Dot after the model name in the title (new-model hint).", None, "no dot showed in the light captures, so the dark value is used (it matches accent.bright)."),
            "ring": f("accent.ring", "Ring around the account avatar (sidebar and account sheet)."),
        },
        "focus": {
            "caret": light_only(theme, "accent.caret", "Text caret in a focused field (composer, search): the only focus indicator.", "the dark caret was not read, so the light value is used."),
        },
        "button": {
            "primary": {"bg": dark_only(theme, "button.primary", "Full-width primary button (Get started, Try it): a near-black capsule over the glow.", "surface.cardSuggestion", onboarding + "; the light raised colour is used."),
                        "text": dark_only(theme, "button.primaryLabel", "Primary button label.", "text.menuItem", onboarding + "; the light label-on-glass colour is used.")},
            "tonal": {"bg": f("button.tonal", "Filled capsule button with a leading icon (Add)."),
                      "text": f("button.tonalLabel", "Its label and icon.")},
            "signIn": {"bg": dark_only(theme, "button.signIn", "Google sign-in button (Continue as Kai): light blue, a rounded rectangle.", "button.tonal", onboarding + "; the light accent.primary is used."),
                       "text": dark_only(theme, "button.signInLabel", "Google sign-in button label.", "button.tonalLabel", onboarding + "; the light accent.onPrimary is used.")},
            "send": {"bg": f("button.send", "Send button once text is typed: a blue circle."),
                     "glyph": f("button.sendGlyph", "Send arrow.")},
            "voice": {"bg": f("button.voice", "Voice (Live) button while the composer is empty: a blue-tinted circle."),
                      "bgTask": f("button.voiceTask", "Voice button in Task mode: purple-tinted."),
                      "glyph": f("button.voiceGlyph", "Voice bars glyph.")},
        },
        "switch": {
            "on": f("switch.on", "Material switch on (Memory): accent.primary track."),
            "thumb": f("switch.thumb", "Material switch thumb, on: holds a tick."),
            "tick": f("switch.tick", "Tick on the Material switch's thumb."),
            "onSystem": f("switch.onSystem", "iOS switch on (Voice): the bright blue, both themes."),
            "thumbSystem": f("switch.thumbSystem", "iOS switch thumb."),
        },
        "status": {
            "danger": alias("color.text.danger", "color", "Danger: red text on destructive items. No danger fill was seen."),
            "info": alias("color.accent.bright", "color", "Info: the bright blue (links, the new-model dot)."),
        },
    }}
    s["$extensions"] = {"notTokenised": [
        "Success and warning colours: no such state was seen",
        "Pressed and disabled states: stills only, and no disabled control appeared",
        "Two switch styles: Gemini's own pages use a Material switch (accent.primary), iOS-styled pages the system switch (accent.bright)",
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
             "$description": "The app's Settings > Theme > Light, set for the light pass on 2026-10-24 and put back to System default afterwards. Read from screenshots/light/."},
            {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"},
             "$description": "Settings > Theme > System default with the phone in dark mode. Read from screenshots/dark/."},
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
