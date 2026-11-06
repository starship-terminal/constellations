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

# The Accent color menu (Settings > Theme), top to bottom. The tenth option is White in dark and Black
# in light, so it is a semantic token (color.accent.inkOption), not a core one.
PALETTE = ["blue", "cyan", "green", "lime", "yellow", "orange", "pink", "magenta", "purple"]

# PRODUCT (adapt): the readings whose greys make up the ramp.
NEUTRAL_IDS = ["bg.page", "bg.grouped", "surface.card", "surface.composer", "surface.segmentTrack",
               "surface.segmentThumb", "surface.menu", "surface.menuIcon", "surface.tabSelected", "surface.taskCard",
               "border.divider", "text.primary", "text.value", "text.seeAll", "text.sectionHeader", "text.placeholder",
               "text.chevron", "slider.step"]


def neutral_ramp():
    """Every grey the semantic sets use, both themes, sorted light to dark. Not a published ramp:
    the steps are the values the app shows, named by order."""
    seen = {}
    for rid in NEUTRAL_IDS:
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
        "accent": {name: from_reading(f"palette.{name}", "dark", "color",
                                      f"Accent colour option '{name.title()}' in Settings > Theme > Accent color. The same swatch in both themes. The owner's account uses Blue; the other options were seen only as swatches.")
                   for name in PALETTE},
        "neutral": neutral_ramp(),
    }
    c["radius"] = {
        "card": derived("26px", "dimension", f"Grouped settings cards and the custom-instructions field. Diagonal-inset reading: {rd('radius.card')['value']} dark, {rd('radius.card', 'light')['value']} light. Plus or minus 2 pt."),
        "composer": derived("22px", "dimension", f"The composer's corners: {rd('radius.composer')['value']}. The composer grows to two rows, so it is a rounded rectangle, not a capsule."),
        "bubble": derived("22px", "dimension", f"The owner's message bubble: {rd('radius.userBubble')['value']}, all four corners alike (no tail)."),
        "dialog": derived("32px", "dimension", f"Alert card: {rd('radius.dialog')['value']}."),
        "menu": derived("30px", "dimension", f"The chat's pull-down menu (iOS 26 glass): {rd('radius.menuChat')['value']}."),
        "menuLarge": derived("44px", "dimension", f"The plus menu, which rises from the composer's corner: {rd('radius.menuPlus')['value']}. The glass rim softens the edge, so this reads high; plus or minus 4 pt."),
        "tile": derived("12px", "dimension", "The 40 pt tile behind the empty-state magnifier: too small for the diagonal reading, judged against the tile's size."),
        "capsule": derived("999px", "dimension", "Fully round ends: the Chat / Work control and its thumb, tab pills, the Chat, New task and New chat pills, alert buttons, the search field, switches, the usage meter and the effort slider."),
    }
    card = rd("size.card")["box"]
    rows = rd("rows.settings")["value"]
    pitch = (rows[rows.index(463)] - 359) / 2 if 359 in rows and 463 in rows else None
    c["space"] = {
        "base": derived("4px", "dimension", "Measured gaps land on multiples of 4 pt within a pixel or two."),
        "xs": derived("4px", "dimension", "Gap between a section header and its card's top rim region, and inside pills."),
        "sm": derived("8px", "dimension", "Gap between the composer's two rows and between the slider's steps and its rim."),
        "md": derived("12px", "dimension", f"The composer's side margin: it starts {(rd('size.composer.w')['from'] - 16) / 2:g} pt from the screen edge."),
        "lg": derived("16px", "dimension", f"Screen margin: settings cards start {(card[0] - 16) / 2:g} pt from the screen edge, reply text 17 pt, the owner's bubble ends 16.5 pt from the right."),
        "xl": derived("20px", "dimension", "Text inset of section headers and helper text from the screen margin: they start 36 pt from the screen edge, 20 pt inside the cards' edge."),
        "xxl": derived("24px", "dimension", "Gap between the end of a reply and its action row, and between stacked task cards (24 pt in 21-scheduled-tabs-cards-primary-pill)."),
        "screenMargin": alias("space.lg", "dimension", "Left and right margin of cards, reply text and the owner's bubble."),
    }
    c["size"] = {
        "row": tok(px(pitch or 52), "dimension", "Single-line grouped row in Settings, divider to divider.", "Sampled", rd("rows.settings")["capture"]),
        "navButton": tok(px(pt_of("size.navButton.w")), "dimension", "Round glass buttons: sidebar, close, back, new chat (a circle). The reading includes the glass rim's soft edge.", "Sampled", rd("size.navButton.w")["capture"]),
        "segmented": {
            "width": tok(px(pt_of("size.segmented.w")), "dimension", "The Chat / Work control at the top of a new chat.", "Sampled", rd("size.segmented.w")["capture"]),
            "height": tok(px(round(pt_of("size.segmented.h"))), "dimension", f"The Chat / Work control ({rd('size.segmented.h')['value']}).", "Sampled", rd("size.segmented.h")["capture"]),
            "thumb": tok(px(pt_of("size.segmentThumb")), "dimension", f"The selected thumb: {rd('size.segmentThumb')['value']}, half the control.", "Sampled", rd("size.segmentThumb")["capture"]),
        },
        "composer": {
            "width": tok(px(pt_of("size.composer.w")), "dimension", "The composer, full width less the side margins.", "Sampled", rd("size.composer.w")["capture"]),
            "height": tok(px(pt_of("size.composer.h")), "dimension", "The composer with an empty field: the text row above, the tool row (+, model pill, microphone, send) below.", "Sampled", rd("size.composer.h")["capture"]),
        },
        "sendButton": tok(px(round(pt_of("size.sendButton"))), "dimension", f"Send and voice buttons, a circle: {rd('size.sendButton')['value']} dark, {rd('size.sendButton', 'light')['value']} light.", "Sampled", rd("size.sendButton")["capture"]),
        "pill": tok(px(round(pt_of("size.chatPill", "dark", 1))), "dimension", f"Accent pills (sidebar Chat {rd('size.chatPill')['value']}, New task {rd('size.newTask')['value']}).", "Sampled", rd("size.chatPill")["capture"]),
        "inkButton": tok(px(pt_of("size.inkButton", "dark", 1)), "dimension", f"The ink pill on an empty state (New chat): {rd('size.inkButton')['value']}.", "Sampled", rd("size.inkButton")["capture"]),
        "tab": tok(px(round(pt_of("size.tab.h"))), "dimension", f"Tab pills (Active, Paused; search's All), height. 'Active' is {rd('size.tab')['value']} wide.", "Sampled", rd("size.tab.h")["capture"]),
        "switch": {
            "width": tok(px(round(pt_of("size.switch"))), "dimension", f"Switch track ({rd('size.switch')['value']}).", "Sampled", rd("size.switch")["capture"]),
            "height": tok(px(round(pt_of("size.switch", "dark", 1))), "dimension", f"Switch track height ({rd('size.switch')['value']}).", "Sampled", rd("size.switch")["capture"]),
            "thumb": tok(px(pt_of("size.switchThumb")), "dimension", f"Switch thumb width (a pill {rd('size.switchThumb')['value']}).", "Sampled", rd("size.switchThumb")["capture"]),
        },
        "menuIcon": tok(px(pt_of("size.menuIcon")), "dimension", "Round icon well beside each plus-menu item.", "Sampled", rd("size.menuIcon")["capture"]),
        "menuWidth": tok(px(round(pt_of("size.menu.w"))), "dimension", "The plus menu's width.", "Sampled", rd("size.menu.w")["capture"]),
        "dialog": {
            "width": tok(px(pt_of("size.dialog.w")), "dimension", "Alert card width.", "Sampled", rd("size.dialog.w")["capture"]),
            "button": tok(px(round(pt_of("size.dialogButton", "dark", 1))), "dimension", f"Alert button height ({rd('size.dialogButton')['value']}, two side by side).", "Sampled", rd("size.dialogButton")["capture"]),
        },
        "searchBar": tok(px(pt_of("size.searchBar.h")), "dimension", f"Search field height ({rd('size.searchBar.w')['value']} wide beside a round close button).", "Sampled", rd("size.searchBar.h")["capture"]),
        "searchTile": tok(px(round(pt_of("size.searchTile", "dark", 1))), "dimension", f"Tile behind the empty-state magnifier: {rd('size.searchTile')['value']}.", "Sampled", rd("size.searchTile")["capture"]),
        "progress": tok(px(pt_of("size.progress.h")), "dimension", "Usage meter track height.", "Sampled", rd("size.progress.h")["capture"]),
        "slider": {
            "height": tok(px(pt_of("size.slider.h")), "dimension", "Effort slider: a glass capsule holding six steps.", "Sampled", rd("size.slider.h")["capture"]),
            "thumb": tok(px(round(pt_of("size.sliderThumb"))), "dimension", f"Effort slider thumb, a white circle ({rd('size.sliderThumb')['value']}).", "Sampled", rd("size.sliderThumb")["capture"]),
        },
        "bubbleMaxWidth": tok(px(pt_of("size.userBubble")), "dimension", f"The widest owner's bubble ({rd('size.userBubble')['value']}), right-aligned. Replies have no bubble and run the full text width.", "Sampled", rd("size.userBubble")["capture"]),
        "caret": derived("23px", "dimension", "Text caret height: 46 px (light 02, one column scan), 2 px wide."),
        "touchTarget": derived("44px", "dimension", "The round glass buttons, rows and the alert buttons are 44 pt or more. The send button (32 pt) sits inside the composer."),
    }
    c["border"] = {"width": {
        "hairline": derived("0.5px", "dimension", "Dividers between grouped rows: one device pixel at 2x (border.divider reads a one-pixel row)."),
        "dashed": derived("1px", "dimension", "The dashed rim of a recommended task card, about two device pixels."),
    }}
    c["fontFamily"] = {
        "base": tok("system", "fontFamily", "Not determinable from pixels. The letterforms match the iOS system face (SF Pro); use the platform font.", "Not captured", MEASURED),
        "math": tok("serif", "fontFamily", "Rendered maths in replies uses a serif italic close to KaTeX's; not determinable from pixels.", "Not captured", MEASURED),
    }
    c["fontWeight"] = {
        "regular": derived(400, "fontWeight", "Reply text, rows, menu items, suggestions, helper text. Judged by stroke width, not measured."),
        "medium": derived(500, "fontWeight", "Segment and tab labels, pill labels. Judged by stroke width."),
        "semibold": derived(600, "fontWeight", "Nav titles, section headers, the alert title, bold reply text. Judged by stroke width."),
        "bold": derived(700, "fontWeight", "The sidebar's ChatGPT title. Judged by stroke width."),
    }

    def ty(size_rid, weight, lh, desc, extra=()):
        sizes = [rd(r)["value"] for r in (size_rid,) + tuple(extra)]
        v = {"fontFamily": "{fontFamily.base}", "fontWeight": "{fontWeight.%s}" % weight,
             "fontSize": sizes[0].replace("pt", "px")}
        if lh:
            v["lineHeight"] = lh
        return tok(v, "typography", desc + f" Cap-height readings: {', '.join(sorted(set(sizes)))}.", "Derived", rd(size_rid)["capture"])

    lines = lambda rid: f"{round(float(rd(rid)['value'].rstrip('pt'))):g}px"
    c["typography"] = {
        "titleLarge": ty("type.sidebarTitle", "bold", None, "The sidebar's ChatGPT title."),
        "menuLarge": ty("type.plusItem", "regular", None, "Plus-menu items (Camera, Photos, Files), larger than other menus."),
        "headline": ty("type.navTitle", "semibold", None, "Nav titles, section headers, the alert title, bold lines in replies.", ("type.sectionHeader", "type.dialogTitle", "type.threadBold")),
        "body": ty("type.thread", "regular", lines("lines.thread"), "Reply text, settings rows, sidebar items and recents, menu items, the composer, suggestions, tab labels, task-card titles, pill and alert-button labels.", ("type.body", "type.sidebarItem", "type.recent", "type.menuItem", "type.composer", "type.suggestion", "type.tab", "type.cardTitle", "type.pillButton", "type.dialogButton", "type.emptyTitle", "type.usageRow")),
        "bubble": ty("type.userBubble", "regular", lines("lines.userBubble"), "Text in the owner's bubble: body size on a looser line."),
        "callout": ty("type.segment", "medium", None, "Chat / Work labels and empty-state body text.", ("type.emptyBody",)),
        "subheadline": ty("type.dialogBody", "regular", lines("lines.dialogBody"), "Alert body."),
        "footnote": ty("type.footnote", "regular", lines("lines.footnote"), "Helper text under cards, the thread date line, the usage reset time.", ("type.timestamp", "type.usageFoot")),
        "taskBody": ty("type.cardBody", "regular", lines("lines.taskBody"), "Task-card descriptions on Scheduled: footnote size on a looser line."),
    }
    c["$extensions"] = {"notTokenised": [
        "iOS 26 glass (round buttons, the Chat / Work control, the composer, menus, the alert, the search field, the slider): blur and refraction come from the system material",
        "Continuous (squircle) corners: DTCG has no value for corner smoothing",
        "Motion and easing: stills only",
        "Shadows: the light theme's glass casts a soft shadow that was not measured; dark draws none",
        "Line heights of titles and one-line labels: only multi-line blocks were measured",
        "Dash pattern of a task card's rim: 7 pt dashes on a 16 pt period (DTCG strokeStyle has no dash length)",
        "Sidebar and suggestion row pitch: 48 pt and 47 pt (lines.sidebar, lines.suggestions); rows have no dividers",
    ]}
    return c


# ---------------------------------------------------------------- semantic sets

def scrim(theme):
    ref, dim = rd("scrim.ref", theme)["value"], rd("scrim.dim", theme)["value"]
    a = 1 - int(dim[1:3], 16) / int(ref[1:3], 16)
    return derived("#000000%02X" % round(a * 255), "color",
                   f"Black at {round(a * 100)}%: the custom-instructions field reads {ref} undimmed and {dim} under the alert.",
                   rd("scrim.dim", theme)["capture"])


def one_theme(theme, rid, have, desc, other_from=None, why=""):
    """A role read in one theme only (have). The other theme reuses that value (other_from None) or the
    value of the closest role in its own theme, as Derived, and says which."""
    if theme == have:
        return from_reading(rid, have, "color", desc)
    src = rd(other_from, theme) if other_from else rd(rid, have)
    return derived(src["value"], "color", desc + f" Not captured in {theme}: " + why, src["capture"])


def semantic(theme):
    f = lambda rid, desc, typ="color": from_reading(rid, theme, typ, desc)
    caret = "accent.caret" if theme == "dark" else "accent.caretLight"
    s = {"color": {
        "bg": {
            "page": f("bg.page", "New chat, threads, the sidebar, search and Scheduled."),
            "grouped": f("bg.grouped", "Settings pages behind the grouped cards: black in dark, iOS's grouped grey in light."),
            "scrim": scrim(theme),
        },
        "surface": {
            "card": f("surface.card", "Grouped cards and the custom-instructions field."),
            "composer": f("surface.composer", "The composer (glass), centre reading." + (" In light the material is a soft white gradient." if theme == "light" else "")),
            "glass": f("surface.glassButton", "Round glass buttons (sidebar, close, back, new chat), read beside the glyph. Translucent: tints with what is behind."),
            "segmentTrack": f("surface.segmentTrack", "The Chat / Work control's track."),
            "segmentThumb": f("surface.segmentThumb", "The selected half of the Chat / Work control: darker than the track in dark, a grey in light."),
            "tabSelected": f("surface.tabSelected", "The selected tab pill (Active, Paused, search's All)."),
            "menu": f("surface.menu", "Menus over the page (plus menu, accent colour pop-up)."),
            "menuIcon": f("surface.menuIcon", "The round well behind each plus-menu icon."),
            "menuTinted": f("surface.menuOverBubble", "The chat menu over the owner's blue bubble: the glass takes the bubble's colour, so this is an example, not a fixed value."),
            "userBubble": f("surface.userBubble", "The owner's message bubble, set by the Blue accent: a deep navy in dark, a pale blue in light."),
            "dialog": f("surface.dialog", "Alert card (glass over the scrim)."),
            "dialogButton": f("surface.dialogButton", "Buttons inside an alert (Cancel, Retry): a lighter glass capsule."),
            "taskCard": f("surface.taskCard", "A recommended task card on Scheduled" + (": filled grey in dark." if theme == "dark" else ": white, close to the page, so the dashed rim carries it.")),
            "searchTile": f("surface.searchTile", "The tile behind the empty-state magnifier."),
            "searchField": one_theme(theme, "surface.searchBar", "dark", "Search field at the bottom of search (glass).", "surface.composer", "filled from surface.composer, the same glass."),
            "progressTrack": f("surface.progressTrack", "Usage meter track: the meter's blue at low opacity."),
            "sliderTrack": f("surface.sliderTrack", "Effort slider track (glass)."),
            "banner": one_theme(theme, "surface.banner", "light", "The 'Share Message' banner that slid over the top of a thread.", "surface.menu", "filled from surface.menu, the closest dark glass."),
        },
        "border": {
            "divider": f("border.divider", "Hairline between grouped rows, inset to the row label."),
            "sidebar": f("border.sidebar", "Rule between the sidebar's nav items and its recents."),
            "dashed": f("border.taskCard" if theme == "dark" else "border.taskCardLight", "The dashed rim of a recommended task card: 7 pt dashes on a 16 pt period."),
        },
        "text": {
            "primary": f("text.primary", "Row labels, titles, sidebar items, menu items, nav titles."),
            "reply": f("text.thread", "Assistant reply text, which sits on the page with no bubble."),
            "secondary": f("text.value", "Row values (Premium seat, System, Default)."),
            "muted": f("text.seeAll", f"See all, empty-state body, unselected tabs, the model pill's effort, find-in-chat count, task-card descriptions. Readings in this role: {', '.join(sorted({rd(r, theme)['value'] for r in ('text.seeAll', 'text.emptyBody', 'text.emptyLine', 'text.tabUnselected', 'text.modelEffort', 'text.findCount', 'text.taskBody')}))}."),
            "sectionHeader": f("text.sectionHeader", "Settings section headers (Customize ChatGPT, Account)."),
            "footnote": f("text.footnote", "Helper text under a card."),
            "placeholder": f("text.placeholder", "Composer and search placeholders."),
            "fieldPlaceholder": f("text.fieldPlaceholder", "Placeholder in a grouped-card field (Custom instructions): lighter than the composer's in dark."),
            "chevron": f("text.chevron", "Disclosure chevrons and the pop-up arrows on row values."),
            "suggestion": f("text.suggestion", "Suggestion rows above an empty composer."),
            "timestamp": one_theme(theme, "text.timestamp", "dark", "The thread's date line.", "text.seeAll", "the banner covered it, so text.muted is used, which reads the same in dark."),
            "onUserBubble": f("text.onUserBubble", "Text in the owner's bubble: a pale blue in dark, the accent's darker blue in light."),
            "onAccent": f("accent.sendGlyph", "Glyphs and labels on the accent (send arrow, Chat, New task)."),
            "accent": f("text.menuSelected", "A selected menu item (Think harder), tinted with the accent; its tick uses the same colour."),
            "danger": f("text.danger", "Destructive menu items (Delete): red text and a red outline icon, never a red fill."),
            "menuHeader": f("text.menuHeader", "The chat menu's header (the chat title), over tinted glass."),
            "dialogBody": f("text.dialogBody", "Alert body text."),
            "bannerTitle": one_theme(theme, "text.bannerTitle", "light", "Banner title.", "text.primary", "filled from text.primary."),
            "bannerBody": one_theme(theme, "text.bannerBody", "light", "Banner body.", "text.seeAll", "filled from text.muted."),
        },
        "accent": {
            "default": f("accent.send", "The Blue accent: send and voice buttons, the effort slider's fill, the Accent color swatch."),
            "pill": f("accent.chatPill", f"Accent pills (sidebar Chat, New task); New task reads {rd('accent.newTask', theme)['value']}."),
            "meter": f("accent.progress", "Usage meter fill: a lighter blue than the accent, the same in both themes."),
            "unread": f("accent.unread", "Unread dot after a recent chat and on the sidebar button: a system blue, not the accent."),
            "inkOption": f("palette.ink", "The tenth Accent color option: White in dark, Black in light."),
        },
        "focus": {
            "caret": f(caret, "Text caret in a focused field, the accent blue: the only focus indicator."),
        },
        "button": {
            "ink": {"bg": f("button.ink", "Ink pill on an empty state (New chat): white in dark, near-black in light."),
                    "text": f("button.inkLabel", "Ink pill label.")},
            "dialog": {"text": f("button.dialogLabel", "Alert button labels (Cancel, Retry), both alike.")},
        },
        "switch": {
            "on": f("switch.on", "Switch on: iOS system green, not the accent."),
            "thumb": f("switch.thumb", "Switch thumb."),
        },
        "slider": {
            "thumb": f("slider.thumb", "Effort slider thumb."),
            "step": f("slider.step", "Effort slider step dots beyond the thumb."),
        },
        "status": {
            "danger": alias("color.text.danger", "color", "Danger: red text on destructive items. No danger fill was seen."),
            "info": alias("color.accent.unread", "color", "Info: the unread blue."),
        },
    }}
    s["$extensions"] = {"notTokenised": [
        "Switch off: every switch in the captures was on",
        "Warning and success colours: no such state was seen (the error alert uses neutral text)",
        "Pressed states: stills only",
        "Other accents: choosing Cyan, Green and so on recolours the bubble, send button and pills; only Blue was applied",
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
             "$description": "Settings > Theme > Appearance > Light, set for the capture and put back to System afterwards. Read from screenshots/light/."},
            {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"},
             "$description": "Settings > Theme > Appearance > System with the phone in dark mode. Read from screenshots/dark/."},
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
