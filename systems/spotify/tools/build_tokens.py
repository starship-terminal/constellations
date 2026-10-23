#!/usr/bin/env python3
"""Build tokens.json (W3C DTCG, Tokens Studio multi-set layout) from raw/readings.json (native kit).

Copied from systems/grokbot through tools/kit/native/. core() and semantic(), marked PRODUCT (adapt),
map Spotify's readings to roles; build() writes one semantic set, dark, because Spotify for iOS has no
light theme. The helpers and check() are the kit's.

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

CATEGORIES = [("music", "Music"), ("podcasts", "Podcasts"), ("liveEvents", "Live Events"), ("fitness", "Fitness"),
              ("madeForYou", "Made For You"), ("upcoming", "Upcoming releases"), ("newReleases", "New Releases"),
              ("playlisting", "The Art of Playlisting")]


def neutral_ramp():
    """Every grey the dark set uses, sorted light to dark. Not a published ramp: the steps are the
    values the app shows, named by order."""
    ids = ["bg.page", "bg.drawer", "surface.tile", "surface.card", "surface.sheet", "surface.sheetSort",
           "surface.shareTarget", "surface.chip", "border.divider", "border.drawerDivider", "border.outline",
           "text.primary", "text.secondary", "text.searchSubtitle", "text.tertiary", "slider.track", "text.onInverse"]
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
        "brand": {
            "green": from_reading("accent.green", "dark", "color", "Spotify green: selected chips, the play button, the saved tick, pins, the tab underline and the slider's filled part all read this value."),
        },
        "system": {
            "green": from_reading("switch.on", "dark", "color", "The iOS system green (dark appearance), used only by switches. It is not Spotify green: the app keeps the stock UISwitch."),
        },
        "category": {k: from_reading(f"category.{k}", "dark", "color",
                                     f"Search > Browse all tile '{label}'. Each category has its own flat colour with tilted artwork in the corner."
                                     + (" The same value as 'Podcasts'." if k == "upcoming" else ""))
                     for k, label in CATEGORIES},
        "neutral": neutral_ramp(),
    }
    c["radius"] = {
        "sm": derived("4px", "dimension", f"Home shortcut tiles ({rd('radius.tile')['value']}) and browse category tiles ({rd('radius.category')['value']}). Plus or minus 2 pt."),
        "md": derived("8px", "dimension", f"Cards and panels: the promo card ({rd('radius.card')['value']}), the mini player ({rd('radius.miniPlayer')['value']}), settings quick tiles ({rd('radius.settingsTile')['value']}), the drawer's account card ({rd('radius.drawerCard')['value']}) and notification card ({rd('radius.notice')['value']}). Plus or minus 2 pt."),
        "field": derived("6px", "dimension", f"The resting search field: {rd('radius.field')['value']}, plus or minus 2 pt; its corners look tighter than the cards'."),
        "sheet": derived("34px", "dimension", f"Top corners of the context, sort and share sheets (iOS 26 glass): {rd('radius.sheet')['value']}."),
        "capsule": derived("999px", "dimension", "Fully round ends: chips, the Pre-save, Following and Turn on pills, the focused search field, Cancel, the segmented control, switches. Circles (play button, avatars, share targets, the saved tick) use it too."),
    }
    tile = rd("size.shortcut.w")
    cat = rd("size.category")["box"]
    c["space"] = {
        "base": derived("4px", "dimension", "Measured gaps land on multiples of 4 pt within a pixel or two."),
        "xs": derived("4px", "dimension", "Between a row title and its subtitle, and around small icons in a subtitle (pin, download)."),
        "sm": derived("8px", "dimension", f"Between home shortcut tiles ({(413 - tile['to'] - 1) / 2:g} pt), between chips (8.5 pt), and the inset of the mini player and sheets from the screen edge ({(rd('size.miniPlayer')['box'][0] - 16) / 2:g} pt)."),
        "md": derived("12px", "dimension", f"Artwork to text in a list row (12.5 pt in 10-library and 09-search-results-rows); settings quick tiles start {(rd('size.settingsTile')['box'][0] - 16) / 2:g} pt from the edge."),
        "lg": derived("16px", "dimension", f"Screen margin (tiles, cards, rows and headings start {(tile['from'] - 16) / 2:g} pt from the edge) and the gap between browse tiles ({(422 - cat[2] - 1) / 2:g} pt)."),
        "xl": derived("24px", "dimension", "Below a home section title before its row of cards (about 22 pt in 02-home)."),
        "screenMargin": alias("space.lg", "dimension", "Left and right margin of tiles, cards, rows and headings."),
    }
    art_l, art_l2 = rd("size.artLibrary"), rd("size.artLibrary2")
    art_s, art_s2 = rd("size.artSearch"), rd("size.artSearch2")
    c["size"] = {
        "chip": derived("32px", "dimension", f"Filter chips: {rd('size.chip')['value']} selected (green, a crisp edge), {rd('size.chipGlass.h')['value']} tall unselected with the glass rim."),
        "pill": derived("32px", "dimension", f"Small pill buttons: Pre-save {rd('size.pill')['value']}, Turn on {rd('size.noticeButton')['value']}, Following {rd('size.following.w')['value']} x {rd('size.following.h')['value']} (outlined)."),
        "shortcutTile": tok(px(pt_of("size.shortcut.h")), "dimension", f"Home shortcut tile height; the artwork is a square of the same size at its left. Two tiles share a row ({rd('size.shortcut.w')['value']} wide each).", "Sampled", rd("size.shortcut.h")["capture"]),
        "categoryTile": tok(px(pt_of("size.category", "dark", 1)), "dimension", f"Browse category tile height; two per row ({rd('size.category')['value']}).", "Sampled", rd("size.category")["capture"]),
        "promoCard": tok(px(pt_of("size.card.h")), "dimension", f"Promo card (Upcoming release) height, full width ({rd('size.card.w')['value']}).", "Sampled", rd("size.card.h")["capture"]),
        "searchField": derived("48px", "dimension", f"Resting search field (white): {rd('size.searchField')['value']} inside its anti-aliased edge."),
        "searchFieldFocused": tok(px(pt_of("size.fieldFocused.h")), "dimension", f"Focused search field (glass capsule), rim included; Cancel beside it is {rd('size.cancel.w')['value']} x {rd('size.cancel.h')['value']}.", "Sampled", rd("size.fieldFocused.h")["capture"]),
        "rowArtwork": derived("48px", "dimension", f"Artwork in search results and recent searches: {rd('size.artSearch')['value']} and {rd('size.artSearch2')['value']} across the anti-aliased edge."),
        "libraryArtwork": derived("64px", "dimension", f"Artwork in Your Library rows: {rd('size.artLibrary')['value']} across the anti-aliased edge."),
        "row": derived(px((art_s2["from"] - art_s["from"]) / 2 // 1), "dimension", f"Search result row pitch: artwork tops {art_s['from']} and {art_s2['from']} px."),
        "libraryRow": derived(px((art_l2["from"] - art_l["from"]) / 2), "dimension", f"Your Library row pitch: artwork tops {art_l['from']} and {art_l2['from']} px."),
        "settingsRow": derived(px((rd("type.settingsRow3")["top"] - rd("type.settingsRow")["top"]) / 4), "dimension", "Settings row pitch (title and subtitle): the cap tops of the first and third row titles are two rows apart."),
        "miniPlayer": derived("56px", "dimension", f"Mini player: {rd('size.miniPlayer')['value']} above a 2 pt progress line ({rd('size.miniPlayer.h')['value']} with it)."),
        "miniArtwork": tok(px(pt_of("size.miniArt")), "dimension", "Artwork in the mini player.", "Sampled", rd("size.miniArt")["capture"]),
        "savedIcon": derived("20px", "dimension", f"The green saved tick (a filled circle): {rd('size.like')['value']} with its edge."),
        "playButton": derived("48px", "dimension", f"Round green play button on an artist page: {rd('size.play')['value']} inside its anti-aliased edge."),
        "navButton": tok(px(pt_of("size.navButton.w")), "dimension", f"Round glass back and search buttons ({rd('size.navButton.w')['value']} x {rd('size.navButton.h')['value']} with the rim).", "Sampled", rd("size.navButton.w")["capture"]),
        "settingsTile": tok(px(pt_of("size.settingsTile", "dark", 1)), "dimension", f"Settings quick tile height; three share the row ({rd('size.settingsTile')['value']}).", "Sampled", rd("size.settingsTile")["capture"]),
        "switch": {
            "width": tok(px(pt_of("size.switch")), "dimension", "Switch track (iOS 26 UISwitch).", "Sampled", rd("size.switch")["capture"]),
            "height": derived("28px", "dimension", f"Switch track height ({rd('size.switch')['value']})."),
            "thumb": tok(px(pt_of("size.switchThumb")), "dimension", f"Switch thumb width (a pill {rd('size.switchThumb')['value']}).", "Sampled", rd("size.switchThumb")["capture"]),
        },
        "slider": {
            "track": derived("2px", "dimension", f"Slider track thickness ({rd('size.sliderTrack')['value']} across the anti-aliased edge)."),
            "thumb": tok(px(pt_of("size.sliderThumb")), "dimension", "Slider thumb, a white circle.", "Sampled", rd("size.sliderThumb")["capture"]),
        },
        "tabIndicator": tok(px(pt_of("size.tabIndicator.h")), "dimension", f"Underline under the selected artist-page tab, as wide as its label ({rd('size.tabIndicator.w')['value']} for 'Music').", "Sampled", rd("size.tabIndicator.h")["capture"]),
        "segmented": tok(px(pt_of("size.segmented.h")), "dimension", f"Segmented control height ({rd('size.segmented.w')['value']} wide for two segments; the selected segment is {rd('size.segmentedSelected')['value']}).", "Sampled", rd("size.segmented.h")["capture"]),
        "shareTarget": tok(px(pt_of("size.shareTarget")), "dimension", "Round share target (Search, Create group, contacts, apps).", "Sampled", rd("size.shareTarget")["capture"]),
        "avatar": {
            "header": tok(px(pt_of("size.avatarHeader")), "dimension", "Account avatar at the left of a page header (Home, Search, Your Library).", "Sampled", rd("size.avatarHeader")["capture"]),
            "drawer": tok(px(pt_of("size.avatarDrawer")), "dimension", "Account avatar in the profile drawer, and message avatars.", "Sampled", rd("size.avatarDrawer")["capture"]),
        },
        "badge": tok(px(pt_of("size.family", "dark", 1)), "dimension", f"Plan badge ('Family', {rd('size.family')['value']}); the 'Beta' tag is {rd('size.beta')['value']}.", "Sampled", rd("size.family")["capture"]),
        "dot": derived("8px", "dimension", f"Unread dot: {rd('size.dot')['value']} inside its anti-aliased edge."),
        "grabber": {
            "width": tok(px(pt_of("size.grabber.w")), "dimension", "Sheet grabber width.", "Sampled", rd("size.grabber.w")["capture"]),
            "height": tok(px(pt_of("size.grabber.h")), "dimension", "Sheet grabber height.", "Sampled", rd("size.grabber.h")["capture"]),
        },
        "drawerWidth": derived(px((rd("size.drawerEdge")["from"] - 16) / 2), "dimension", "The profile drawer covers the screen but for a strip on the right where the page shows."),
        "touchTarget": derived("44px", "dimension", "Nav buttons, rows and the play button are 44 pt or more. Chips (32 pt), pills (31 pt) and the saved tick sit inside larger rows."),
    }
    c["border"] = {"width": {
        "hairline": derived("0.5px", "dimension", "Dividers between sections and under a sheet header: one device pixel at 2x."),
        "outline": derived("1px", "dimension", "The Following pill's outline: two device pixels."),
    }}
    c["fontFamily"] = {"base": tok("system", "fontFamily", "Not determinable from pixels. The letterforms are Spotify's own geometric sans, not the iOS system face; Spotify ships its own typeface, which is not public. Use the platform font.", "Not captured", MEASURED)}
    c["fontWeight"] = {
        "regular": derived(400, "fontWeight", "Row titles, subtitles, settings rows, sheet items. Judged by stroke width, not measured."),
        "bold": derived(700, "fontWeight", "Page and section titles, nav titles, tile titles, chip-less buttons (Pre-save, Following), the selected tab, browse tiles. Judged by stroke width."),
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
        "display": ty("type.display", "bold", None, "The artist's name over the header photo, tightly set."),
        "pageTitle": ty("type.pageTitle", "bold", None, "Tab page titles beside the account avatar (Search, Your Library)."),
        "sectionTitle": ty("type.sectionTitle", "bold", None, "Home and search section titles, 'Recent searches', 'Popular', the drawer's 'Messages'.", ("type.sectionTitle2", "type.drawerSection")),
        "navTitle": ty("type.navTitle", "bold", None, "Centred title of a pushed page (Settings, Playback)."),
        "body": ty("type.rowTitle", "regular", None, "Row titles, settings rows, drawer rows, the search placeholder, segment labels.", ("type.settingsRow", "type.settingsRow3", "type.searchPlaceholder", "type.drawerRow", "type.segmented")),
        "bodyBold": ty("type.tab", "bold", lines("lines.category"), "The selected artist-page tab, browse tile titles and the selected segment's label.", ("type.category",)),
        "sheetItem": ty("type.sheetItem", "regular", None, "Items in context and sort sheets.", ("type.sortItem",)),
        "subtitle": ty("type.subtitle", "regular", lines("lines.settingsSubtitle"), "Row subtitles, chip labels, setting descriptions, the promo card eyebrow, the mini player's lines, the notification card.", ("type.chip", "type.eyebrow", "type.miniPlayer")),
        "label": ty("type.tileTitle", "bold", lines("lines.tileTitle"), "Shortcut tile titles, pill labels (Pre-save, Following), the promo card title, the plan badge.", ("type.button", "type.buttonOutline", "type.cardTitle", "type.badgeFamily")),
        "sheetHeader": ty("type.sheetHeader", "regular", None, "A sheet's small header ('Sort by')."),
        "caption": ty("type.settingsTile", "regular", None, "Settings quick tile labels."),
        "tag": ty("type.badge", "bold", None, "The 'Beta' tag in a sheet item."),
        "tabLabel": ty("type.tabLabel", "regular", None, "Tab bar labels under the icons."),
    }
    c["$extensions"] = {"notTokenised": [
        "iOS 26 glass (chips, the focused search field, Cancel, nav buttons, sheets): blur and refraction come from the system material",
        "Artwork-tinted colour: the mini player, the share sheet and its card take their colour from the current artwork",
        "Continuous (squircle) corners: DTCG has no value for corner smoothing",
        "Motion and easing: stills only",
        "Shadows: none drawn; separation comes from fills and the glass material",
        "Line heights of titles and one-line labels: only multi-line blocks were measured",
    ]}
    return c


# ---------------------------------------------------------------- semantic set

def scrim(ref, dim, desc):
    r, v = rd(ref)["value"], rd(dim)["value"]
    a = 1 - int(v[1:3], 16) / int(r[1:3], 16)
    return derived("#000000%02X" % round(a * 255), "color",
                   f"Black at {round(a * 100)}%: {desc} reads {r} undimmed and {v} under it.", rd(dim)["capture"])


def semantic(theme):
    f = lambda rid, desc, typ="color": from_reading(rid, theme, typ, desc)
    s = {"color": {
        "bg": {
            "page": f("bg.page", "Every tab page, pushed page and list: Spotify's near-black."),
            "elevated": f("bg.drawer", "The profile drawer, and the settings quick tiles (the same value)."),
            "scrim": scrim("scrim.ref", "scrim.sort", "the sort sheet's backdrop: Your Library"),
            "scrimContext": scrim("scrim.contextRef", "scrim.context", "a context sheet's backdrop: the artist page"),
            "scrimStrong": scrim("scrim.shareRef", "scrim.share", "the share sheet's backdrop: the Your Library header"),
        },
        "surface": {
            "tile": f("surface.tile", "Home shortcut tiles and the drawer's account card."),
            "card": f("surface.card", "Promo cards on Home (Upcoming release)."),
            "panel": f("surface.settingsTile", "Settings quick tiles (Data Saver mode, Offline mode, Private session)."),
            "notice": f("surface.notice", "The notification prompt card in the drawer."),
            "glass": f("surface.glass", "Round glass buttons (back, search), centre reading. The material tints with what is behind it."),
            "chip": f("surface.chip", "Unselected filter chips (glass)."),
            "field": f("surface.field", "The resting search field: white, the one light surface in the app."),
            "fieldFocused": f("surface.fieldFocused", "The focused search field and Cancel (glass)."),
            "sheet": f("surface.sheet", "Context sheets (track, artist), glass; reads lighter where artwork shows through."),
            "sheetSort": f("surface.sheetSort", "The sort sheet (glass)."),
            "shareSheet": f("surface.shareSheet", "The share sheet's glass, which takes the shared item's artwork colour (14-share-sheet); 18-share-song-segmented reads green-black."),
            "shareTarget": f("surface.shareTarget", "Round share targets that carry an icon (Search, Create group, Copy link)."),
            "miniPlayer": f("surface.miniPlayer", "The mini player above the tab bar, tinted from the playing track's artwork (this reading is one album's). Not a fixed colour."),
        },
        "border": {
            "divider": f("border.divider", "Divider between settings sections."),
            "sheet": f("border.sheetDivider", "Divider under a sheet's header row."),
            "card": f("border.drawerDivider", "Divider inside the drawer's account card."),
            "outline": f("border.outline", "Outline of the Following pill."),
            "grabber": f("border.grabber", "Sheet grabber."),
        },
        "text": {
            "primary": f("text.primary", "Titles, row titles, tile titles, settings labels."),
            "secondary": f("text.secondary", f"Subtitles, settings descriptions, chevrons, inactive tabs, Cancel. Readings in this role range {', '.join(sorted({rd(r, theme)['value'] for r in ('text.secondary', 'text.searchSubtitle', 'text.settingsSubtitle', 'text.eyebrow', 'text.chevron', 'text.listeners', 'text.pageTabInactive', 'text.cancel', 'text.placeholderFocused')}))}."),
            "tertiary": f("text.tertiary", "A dimmer subtitle ('Tap to start' on the DJ row). Read once."),
            "placeholder": f("text.placeholder", "Placeholder and icon on the white resting search field."),
            "placeholderFocused": f("text.placeholderFocused", "Placeholder in the focused glass field."),
            "accent": f("text.accent", "Green text for an active state on a solid surface (Data Saver mode, Always on)."),
            "accentOnSheet": f("text.accentOnSheet", f"Green text and tick for the selected option in a glass sheet ({rd('text.checkOnSheet')['value']} for the tick). It reads darker than text.accent; the glass may dim it."),
            "onAccent": f("text.onAccent", "Labels and glyphs on Spotify green (the selected chip; the play glyph reads " + rd("text.onPlay")["value"] + ")."),
            "onInverse": f("text.onInverse", "Labels on white pills (Pre-save, Turn on) and the selected segment."),
            "onBadge": f("text.onFamily", f"Text on coloured badges (Family; Beta reads {rd('text.onBeta')['value']})."),
            "onMiniPlayer": f("text.miniArtist", f"The mini player's artist line, white at reduced opacity over the artwork tint (the title reads {rd('text.miniTitle')['value']})."),
            "sheetHeader": f("text.sheetHeader", "A glass sheet's small header ('Sort by')."),
            "tabActive": f("text.tabActive", "Tab bar label of the current tab."),
            "tabInactive": f("text.tabInactive", "Tab bar labels of the other tabs."),
        },
        "accent": {
            "default": alias("color.brand.green", "color", "Spotify green: the one accent. Selected chips, play, saved, pins, tab underline, slider fill, caret."),
            "dot": f("accent.dot", "Unread dot (Your Updates) and the dot on the account avatar: system blue, the only other accent."),
        },
        "focus": {
            "caret": f("accent.caret", "Text caret in the focused search field: Spotify green, the only focus indicator (no ring)."),
        },
        "button": {
            "primary": {"bg": alias("color.brand.green", "color", "The round play button."),
                        "glyph": f("text.onPlay", "The play glyph on it.")},
            "inverse": {"bg": f("button.inverse", "White pills: Pre-save, Turn on."),
                        "text": alias("color.text.onInverse", "color", "Their labels.")},
            "outline": {"border": alias("color.border.outline", "color", "Outlined pill (Following)."),
                        "text": alias("color.text.primary", "color", "Its label.")},
        },
        "chip": {
            "bg": alias("color.surface.chip", "color", "Unselected chip."),
            "text": alias("color.text.primary", "color", "Unselected chip label."),
            "selectedBg": f("accent.green", "Selected chip: Spotify green. On Home a chip tied to a promoted page can take that page's colour instead (04-home-music-chip)."),
            "selectedText": alias("color.text.onAccent", "color", "Selected chip label."),
        },
        "switch": {
            "on": f("switch.on", "Switch on: the iOS system green, not Spotify green."),
            "off": f("switch.off", "Switch off, track."),
            "thumb": f("switch.thumb", "Switch thumb, on."),
            "thumbOff": f("switch.thumbOff", "Switch thumb, off: a shaded light grey."),
        },
        "slider": {
            "fill": f("accent.slider", "Slider, filled part: Spotify green."),
            "track": f("slider.track", "Slider, empty part."),
            "thumb": f("slider.thumb", "Slider thumb."),
        },
        "tab": {
            "selected": alias("color.text.primary", "color", "Selected artist-page tab label."),
            "unselected": f("text.pageTabInactive", "Other artist-page tab labels."),
            "indicator": f("accent.tabIndicator", "Underline under the selected tab."),
        },
        "segmented": {
            "track": f("surface.segmented", "Segmented control track (glass over the share sheet; tinted by the artwork)."),
            "selectedBg": f("segmented.selected", "Selected segment: a white pill."),
            "selectedText": f("text.onSegmented", "Selected segment label."),
            "text": alias("color.text.primary", "color", "Unselected segment label."),
        },
        "badge": {
            "plan": f("badge.family", "Plan badge (Family) in the drawer."),
            "beta": f("badge.beta", "'Beta' tag in a sheet item: Spotify green."),
        },
        "status": {
            "success": f("accent.like", "Saved: the green tick in the mini player and on saved rows. No other success state was seen."),
            "info": alias("color.accent.dot", "color", "Info: the blue unread dot."),
        },
    }}
    s["$extensions"] = {"notTokenised": [
        "Danger and warning colours: no error, warning or destructive state was seen",
        "Pressed states: stills only",
        "Artwork-tinted fills: the mini player, the share sheet and its preview card change with the artwork",
        "Home chip tied to a promoted page (Music on 04-home-music-chip) takes that page's colour; one case read by eye, no token",
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
        "dark": semantic("dark"),
        "$themes": [  # PRODUCT (adapt): Spotify for iOS has dark only, so there is no light set
            {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"},
             "$description": "Spotify for iOS has one appearance, dark; it does not follow the phone's setting. Read from screenshots/dark/."},
        ],
        "$metadata": {"tokenSetOrder": ["core", "dark"]},
    }
    check(doc)
    (PKG / "tokens.json").write_text(json.dumps(doc, indent=1, ensure_ascii=False) + "\n")
    n = sum(1 for s in ("core", "dark") for _ in walk(doc[s]))
    print(f"tokens.json: {n} tokens")


if __name__ == "__main__":
    if not READ:
        raise SystemExit("no raw/readings.json: run tools/measure.py first")
    build()
