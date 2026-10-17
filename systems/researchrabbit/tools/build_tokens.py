#!/usr/bin/env python3
"""Build tokens.json (W3C DTCG, Tokens Studio multi-set layout) from the raw readings.

Sources, read from app.researchrabbit.ai on 2026-10-04 and in the 2026-10-17 refresh:
  raw/css-vars.json        the app's :root custom properties ("root"), every styled-component's
                           CSS rules ("components"), the rules on bare elements ("globals") and the
                           @media conditions ("media"), read from the DOM and CSSOM
  raw/components-computed.json  computed styles per component and state, read headless from the
                           redacted snapshots (measure.mjs)
  raw/graph-tokens.json    the graph engine's constants, transcribed from raw/graph-code-notes.md
  raw/graph-code-notes.md  the reverse-engineered Canvas 2D engine (Litmaps' map engine)

Every token carries $extensions.source, one of:
  "css var --name"                          a :root custom property, value read from css-vars.json
  "css rule Component: <declaration>"       a literal in a styled-component rule; the builder checks
                                            the declaration really is in that component's rules
  "sampled <screenshot> at (x, y)"          a pixel read from a 2880 x 1800 screenshot, used only where
                                            no rule names the colour
  "graph engine: <identifier> (...)"        a constant from the engine; the builder checks the
                                            identifier is quoted in raw/graph-code-notes.md
  "css rule <element selector>: <decl>"     a rule on a bare element (body, h2, button:focus)
  "css @media <condition>"                  a media query the stylesheets declare
  "computed <component> <state>: <prop>"    a computed style from raw/components-computed.json; the
                                            builder checks the value against the file

ResearchRabbit paints one light theme: no page offers a dark switch. So there is a light set and no
dark set; the engine's dark and print edge and label colours ride along as $extensions on the tokens.

Strict: a value that is not the DTCG type it claims, an alias that points at nothing, an alias whose
target is a different type, a css var that is not declared, or a rule or identifier that is not in
the raw files stops the build. Deterministic: same inputs, byte-identical output. Edit the inputs or
the SPEC below, never tokens.json.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
CSS = json.loads((RAW / "css-vars.json").read_text())
ROOT = CSS["root"]
RULES = CSS["components"]
GRAPH = json.loads((RAW / "graph-tokens.json").read_text())
GLOBALS = CSS.get("globals", [])
MEDIA = CSS.get("media", {})
COMPUTED = json.loads((RAW / "components-computed.json").read_text())["components"]
NOTES = (RAW / "graph-code-notes.md").read_text()
APP_NOTES = (RAW / "app-code-notes.md").read_text()

SHOT = "screenshots/search-split-light-default.png"

# ---------------------------------------------------------------------------------------------------
# Value checks


def norm_color(v):
    """#rgb, #rrggbb, #rrggbbaa, rgb(), rgba(), black, white -> #rrggbb or #rrggbbaa (lower case)."""
    v = v.strip().lower()
    v = {"black": "#000", "white": "#fff"}.get(v, v)
    m = re.fullmatch(r"#([0-9a-f]{3}|[0-9a-f]{4}|[0-9a-f]{6}|[0-9a-f]{8})", v)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        return "#" + (h[:6] if h[6:] == "ff" else h)
    m = re.fullmatch(r"rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*(?:,\s*([\d.]+)\s*)?\)", v)
    if m:
        r, g, b, a = m.groups()
        a = 1.0 if a is None else float(a)
        out = "#%02x%02x%02x" % (int(r), int(g), int(b))
        return out if a == 1 else out + "%02x" % round(a * 255)
    raise ValueError("not a colour: " + v)


DIM = re.compile(r"-?\d+(\.\d+)?(px|rem)")
ALIAS = re.compile(r"\{([^{}]+)\}")


def is_alias(v):
    return isinstance(v, str) and ALIAS.fullmatch(v) is not None


def check(path, ty, val):
    """Refuse a value that is not the DTCG type it claims. A whole-value alias is checked later."""
    if is_alias(val):
        return
    bad = lambda what: ValueError(f"{path}: {ty} must be {what}, got {val!r}")
    if ty == "color":
        if not re.fullmatch(r"#[0-9a-f]{6}([0-9a-f]{2})?", str(val)):
            raise bad("#rrggbb or #rrggbbaa")
    elif ty == "dimension":
        if not DIM.fullmatch(str(val)):
            raise bad("one px or rem length")
    elif ty == "number":
        if isinstance(val, bool) or not isinstance(val, (int, float)):
            raise bad("a number")
    elif ty == "fontWeight":
        if not (isinstance(val, int) and 1 <= val <= 1000):
            raise bad("an integer weight")
    elif ty == "fontFamily":
        if not (isinstance(val, list) and val and all(isinstance(x, str) for x in val)):
            raise bad("a list of family names")
    elif ty == "duration":
        if not re.fullmatch(r"\d+ms", str(val)):
            raise bad("whole milliseconds like 200ms")
    elif ty == "cubicBezier":
        if not (isinstance(val, list) and len(val) == 4 and all(isinstance(x, (int, float)) for x in val)
                and 0 <= val[0] <= 1 and 0 <= val[2] <= 1):
            raise bad("[x1, y1, x2, y2] with x in 0..1")
    elif ty == "shadow":
        if not isinstance(val, list) or not val:
            raise bad("a list of layers")
        for layer in val:
            for k in ("offsetX", "offsetY", "blur", "spread"):
                if not DIM.fullmatch(layer[k]):
                    raise ValueError(f"{path}: shadow {k} {layer[k]!r}")
            check(path + ".color", "color", layer["color"])
    elif ty == "typography":
        for k, t in (("fontFamily", "fontFamily"), ("fontSize", "dimension"), ("fontWeight", "fontWeight"),
                     ("lineHeight", "number"), ("letterSpacing", "dimension")):
            if k not in val:
                raise ValueError(f"{path}: typography is missing {k}")
            check(f"{path}.{k}", t, val[k])
    else:
        raise ValueError(f"{path}: unknown type {ty}")


def parse_shadow(s):
    """'0px 2px 3px #a9b3c64d,0px 1px 3px #a9b3c680' or 'rgba(...) 0px 10px 38px -10px, ...' -> layers."""
    layers = []
    for part in re.split(r",(?![^()]*\))", s):
        part = part.strip()
        m = re.search(r"(rgba?\([^)]*\)|#[0-9a-fA-F]{3,8})", part)
        color = norm_color(m.group(1))
        lens = re.findall(r"-?\d+(?:\.\d+)?px|(?<![\w.#])0(?![\w.])", part.replace(m.group(1), ""))
        lens = [x if x.endswith("px") else "0px" for x in lens] + ["0px"] * 4
        layer = {"color": color, "offsetX": lens[0], "offsetY": lens[1], "blur": lens[2], "spread": lens[3]}
        if re.search(r"\binset\b", part):
            layer["inset"] = True
        layers.append(layer)
    return layers


# ---------------------------------------------------------------------------------------------------
# The token tree. A leaf is a dict with "type" and one of:
#   "var"    a :root custom property; var(--x) values become aliases to x's token
#   "rule"   (component, declaration): the literal value, checked against css-vars.json
#   "sample" (x, y) on SHOT: a pixel colour, for the few colours no rule names
# plus "value" where the leaf states the value itself (an alias, or a parsed literal).


def V(name, desc=None):
    return {"var": name, "description": desc}


def R(ty, value, comp, decl, desc=None):
    return {"type": ty, "value": value, "rule": (comp, decl), "description": desc}


def G(ty, value, sel, decl, desc=None):
    return {"type": ty, "value": value, "global": (sel, decl), "description": desc}


def M(ty, value, comp, state, prop, desc=None):
    return {"type": ty, "value": value, "computed": (comp, state, prop), "description": desc}


def A(ty, value, ident, section, desc=None):
    """A value from the app's production bundle, quoted in raw/app-code-notes.md."""
    return {"type": ty, "value": value, "app": (ident, section), "description": desc}


def Q(value, cond, desc=None):
    return {"type": "dimension", "value": value, "media": cond, "description": desc}


def S(value, xy, desc=None, shot=SHOT):
    return {"type": "color", "value": value, "sample": (shot, xy), "description": desc}


TY = lambda fam, size, weight, lh: {"fontFamily": fam, "fontSize": size, "fontWeight": weight,
                                    "lineHeight": lh, "letterSpacing": "0px"}
LH = ("Line height measured, not set by the component's rule: every text line read computes to 1.5 times its "
      "size (14/21, 16/24, 24/36, 32/48 in raw/components-computed.json), the html default.")

SPEC_CORE = {
    "palette": {
        "base": {"primary": V("--primary"), "secondary": V("--secondary"), "tertiary": V("--tertiary"),
                 "white": R("color", "#ffffff", "Scaffold__Header", "background-color: white"),
                 "black": R("color", "#000000", "SearchBar__Container", "background-color: black")},
        "turq": {"base": V("--turq"), "50": V("--turq-50"), "25": V("--turq-25")},
        "green": {"base": V("--green"), "50": V("--green-50"), "25": V("--green-25")},
        "lavender": {"base": V("--lavender"), "50": V("--lavender-50"), "25": V("--lavender-25"), "12": V("--lavender-12")},
        "peach": {"base": V("--peach"), "50": V("--peach-50"), "25": V("--peach-25")},
        "selection": {"base": V("--selection"), "dark": V("--selection-dark"), "light": V("--selection-light")},
        "grey": {"primary": V("--grey-primary"), "secondary": V("--grey-secondary"), "tertiary": V("--grey-tertiary"),
                 "3": V("--grey-3"), "2": V("--grey-2"), "1": V("--grey-1"),
                 "bg2": V("--grey-bg2"), "bg1": V("--grey-bg1"), "bg0": V("--grey-bg-0")},
        "ui": {"bg": V("--ui-bg"), "bg-hover": V("--ui-bg-hover"), "bg-nested": V("--ui-bg-nested")},
        "ugc": {"amber": V("--ugc-amber", "The first folder colour; ResearchRabbit's orange"),
                "ruby": V("--ugc-ruby"), "amethyst": V("--ugc-amethyst"), "violet": V("--ugc-violet"),
                "sky": V("--ugc-sky"), "cyan": V("--ugc-cyan"), "teal": V("--ugc-teal"), "leaf": V("--ugc-leaf"),
                "unsorted": V("--unsorted", "A saved article in no collection")},
        "activity": {"success": V("--activity-success"), "success-dark": V("--activity-success-dark"),
                     "success-bg": V("--activity-success-bg"), "important": V("--activity-important"),
                     "important-dark": V("--activity-important-dark"), "important-bg": V("--activity-important-bg"),
                     "error": V("--activity-error"), "error-dark": V("--activity-error-dark"),
                     "error-bg": V("--activity-error-bg")},
        "alpha": {
            "black-05": R("color", "rgba(0, 0, 0, 0.05)", "GraphControls__StyledButton", "background-color: rgba(0, 0, 0, 0.05)", "Quiet hover on toolbar, ghost and side buttons"),
            "black-07": R("color", "rgba(0, 0, 0, 0.07)", "Select__Trigger", "background-color: rgba(0, 0, 0, 0.07)"),
            "black-10": R("color", "rgba(0, 0, 0, 0.1)", "ExploreSession__NavButtonsContainer", "background-color: rgba(0, 0, 0, 0.1)", "The back and forward trail behind the header"),
            "white-10": R("color", "rgba(255, 255, 255, 0.1)", "Toast__InlineButton", "&:hover { background-color: rgba(255, 255, 255, 0.1); }", "Quiet hover on dark surfaces: the toast's close button and the drawer's filter buttons"),
            "white-30": R("color", "rgba(255, 255, 255, 0.3)", "LibraryFolder__ArticlesContainer", "background-color: rgba(255, 255, 255, 0.3)"),
            "white-40": R("color", "rgba(255, 255, 255, 0.4)", "DashboardFolders__StyledSection", "background-color: rgba(255, 255, 255, 0.4)"),
            "white-50": R("color", "rgba(255, 255, 255, 0.5)", "ExploreStep__StyledScaffoldMain", "background-color: rgba(255, 255, 255, 0.5)"),
            "white-90": R("color", "rgba(255, 255, 255, 0.9)", "StickerButton__Button", "background-color: rgba(255, 255, 255, 0.9)"),
            "amber-20": R("color", "rgba(240, 125, 89, 0.2)", "ArticleFolders__FolderContainer", "background-color: rgba(240, 125, 89, 0.2)", "Folder chip tint"),
            "violet-20": R("color", "rgba(221, 204, 255, 0.2)", "ExploreBuilder__Container", "background-color: rgba(221, 204, 255, 0.2)"),
            "scrim": R("color", "rgba(48, 85, 94, 0.3)", "Modal__Overlay", "background-color: rgba(48, 85, 94, 0.3)", "The teal-grey overlay behind every dialog"),
        },
        "literal": {
            "charcoal": R("color", "rgb(51, 51, 51)", "HintContainer__Content", "background-color: rgb(51, 51, 51)", "Tooltip fill and the black button's hover"),
            "link-hover": R("color", "rgb(116, 111, 163)", "ArticleTitle__Title", "color: rgb(116, 111, 163)"),
            "toast": R("color", "rgb(255, 238, 138)", "Commander__Container", "background-color: rgb(255, 238, 138)"),
            "drawer-button": S("#86878c", (2690, 1745), "The drawer's Search button while there is nothing new to search; the rule was not captured"),
            "drawer-row": R("color", "rgb(53, 53, 53)", "ExploreFilters__ItemContainer", "background-color: rgb(53, 53, 53)", "A settings row on the black drawer"),
            "drawer-row-on": R("color", "rgb(77, 76, 91)", "ExploreFilters__ItemContainer", "background-color: rgb(77, 76, 91)", "A drawer row whose filter is set"),
        },
    },
    "fontFamily": {
        "ui": {"type": "fontFamily", "value": ["Plus Jakarta Sans", "system-ui", "sans-serif"], "font": "Plus+Jakarta+Sans",
               "description": "Every UI line and every canvas label"},
        "mono": R("fontFamily", ["monospace"], "CopyContainer__Preview", "font-family: monospace; font-size: 12px", "The citation box in Cite Article; the browser's monospace face"),
        "light": {"type": "fontFamily", "value": ["IBM Plex Sans", "system-ui", "sans-serif"], "font": "IBM+Plex+Sans",
                  "description": "Loaded by the app at weight 300; which lines paint it was not read"},
    },
    "fontWeight": {
        "light": R("fontWeight", 300, "ArticleAbstract__AbstractParagraph", "font-weight: 300"),
        "regular": R("fontWeight", 400, "DashboardNew__Desc", "font-weight: 400"),
        "medium": R("fontWeight", 500, "DashboardFolders__Label", "font-weight: 500"),
        "semibold": R("fontWeight", 600, "DashboardSearch__Title", "font-weight: 600"),
        "bold": R("fontWeight", 700, "Navigation__LinkContainer", "font-weight: 700"),
    },
    "fontSize": {
        "12": R("dimension", "12px", "GraphAxes__AxisLabel", "font-size: 12px"),
        "14": R("dimension", "14px", "SearchSummary__Label", "font-size: 14px"),
        "16": R("dimension", "16px", "ArticleDetailsDisplay__Nickname", "font-size: 16px"),
        "18": R("dimension", "18px", "GraphControls__StyledButton", "font-size: 18px"),
        "20": R("dimension", "20px", "DashboardSearch__Subtitle", "font-size: 20px"),
        "24": R("dimension", "24px", "Modal__Title", "font-size: 24px", "Dialog titles; also the h3 default"),
        "28": G("dimension", "28px", "h2", "font-size: 28px", "The h2 default"),
        "32": R("dimension", "32px", "DashboardSearch__Title", "font-size: 32px"),
    },
    "typography": {
        "display": R("typography", TY("{fontFamily.ui}", "{fontSize.32}", "{fontWeight.semibold}", 1.5), "DashboardSearch__Title", "font-size: 32px; font-weight: 600", LH),
        "title": R("typography", TY("{fontFamily.ui}", "{fontSize.20}", "{fontWeight.semibold}", 1.5), "LibraryStyles__LibraryHeaderName", "font-size: 20px; font-weight: 600", LH),
        "subtitle": R("typography", TY("{fontFamily.ui}", "{fontSize.20}", "{fontWeight.medium}", 1.5), "DashboardSearch__Subtitle", "font-size: 20px; font-weight: 500", LH),
        "nickname": R("typography", TY("{fontFamily.ui}", "{fontSize.16}", "{fontWeight.medium}", 1.5), "ArticleDetailsDisplay__Nickname", "font-size: 16px; font-weight: 500", LH),
        "folder": R("typography", TY("{fontFamily.ui}", "{fontSize.16}", "{fontWeight.medium}", 1.5), "DashboardFolders__Label", "font-size: 16px; font-weight: 500", LH),
        "label": R("typography", TY("{fontFamily.ui}", "{fontSize.14}", "{fontWeight.semibold}", 1.5), "SearchSummary__Label", "font-size: 14px; font-weight: 600", LH),
        "nav": R("typography", TY("{fontFamily.ui}", "{fontSize.14}", "{fontWeight.bold}", 1.5), "Navigation__LinkContainer", "font-weight: 700", "The rule sets the weight only; 14px fits the measured text width in the screenshots. " + LH),
        "drawer-title": R("typography", TY("{fontFamily.ui}", "{fontSize.16}", "{fontWeight.semibold}", 1.5), "FilterableSearchActions__Title", "font-weight: 600", "The rule sets the weight only; 16px fits the measured text width in the screenshots. " + LH),
        "summary": R("typography", TY("{fontFamily.ui}", "{fontSize.14}", "{fontWeight.light}", 1.5), "ExploreActionsMain__Summary", "font-weight: 300", "Light running copy, with ExploreActionsMain__SummaryEmph at 600 for the counts. 14px fits the measured text width. " + LH),
        "body": R("typography", TY("{fontFamily.ui}", "{fontSize.14}", "{fontWeight.regular}", 1.5), "SearchSummary__With", "font-size: 14px; font-weight: 400", "The app's running text size: nav links, list titles, journals and option titles all measure 14px in the screenshots. " + LH),
        "small": R("typography", TY("{fontFamily.ui}", "{fontSize.12}", "{fontWeight.regular}", 1.5), "GraphAxes__AxisLabel", "font-size: 12px", LH),
        "small-strong": R("typography", TY("{fontFamily.ui}", "{fontSize.12}", "{fontWeight.semibold}", 1.5), "ArticleDetailsDisplay__LibraryButton", "font-weight: 600; font-size: 12px", LH),
        "abstract": R("typography", TY("{fontFamily.ui}", "{fontSize.12}", "{fontWeight.light}", 1.5), "ArticleAbstract__AbstractParagraph", "font-weight: 300; font-size: 12px", LH),
        "heading-2": G("typography", TY("{fontFamily.ui}", "{fontSize.28}", "{fontWeight.regular}", 1.5), "h2", "font-size: 28px", "The page's h2 default; the 'Screen too small' heading. " + LH),
        "heading-3": R("typography", TY("{fontFamily.ui}", "{fontSize.24}", "{fontWeight.regular}", 1.5), "Modal__Title", "font-size: 24px", "Dialog titles. " + LH),
        "heading-4": G("typography", TY("{fontFamily.ui}", "{fontSize.16}", "{fontWeight.medium}", 1.5), "h4", "font-size: 16px; font-weight: 500", "The h4 default. " + LH),
        "heading-5": G("typography", TY("{fontFamily.ui}", "{fontSize.14}", "{fontWeight.semibold}", 1.5), "h5", "font-size: 14px; font-weight: 600", "The h5 default. " + LH),
        "form-label": G("typography", TY("{fontFamily.ui}", "{fontSize.14}", "{fontWeight.medium}", 1.5), "label", "font-size: 14px; font-weight: 500", "Field labels in dialogs. " + LH),
        "code": R("typography", TY("{fontFamily.mono}", "{fontSize.12}", "{fontWeight.regular}", 1.5), "CopyContainer__Preview", "font-family: monospace; font-size: 12px", "Formatted citations to copy (Cite Article). Line height measured 12/18 on the citation box (raw/components-computed.json)."),
        "caption": R("typography", TY("{fontFamily.ui}", "{fontSize.12}", "{fontWeight.regular}", 1), "DashboardSearch__Tip", "font-size: 12px", "The one-line hint under the home search field. Line height measured 12/12 on that tip (home-hero, a span, in raw/components-computed.json), unlike the 1.5 of running text."),
    },
    "spacing": {},  # filled from --neg2..--16 below
    "radius": {
        "xs": R("dimension", "3px", "LayoutSettings__NavItemContainer", "border-radius: 3px", "Settings tabs"),
        "sm": R("dimension", "{spacing.1}", "GraphControls__StyledButton", "border-radius: var(--1)", "Toolbar buttons, select triggers"),
        "md": R("dimension", "6px", "LayoutSettingsGeneric__OptionContainer", "border-radius: 6px", "Settings option cards, dropdowns"),
        "lg": R("dimension", "{spacing.2}", "LibraryStyles__HeaderContainer", "border-radius: var(--2)", "List cards, sections"),
        "xl": R("dimension", "{spacing.3}", "ExploreBuilder__Container", "border-radius: var(--3)", "Main panels"),
        "2xl": R("dimension", "{spacing.4}", "Popup__Content", "border-radius: var(--4)", "Popups, the inspector, dashboard cards"),
        "chip": R("dimension", "24px", "ExploreGraphLegend__ItemContainer", "border-radius: 24px", "Legend chips"),
        "search": R("dimension", "36px", "SearchBar__Container", "border-radius: 36px", "The home search bar"),
        "pill": R("dimension", "48px", "SearchSummary__Container", "border-radius: 48px", "Every pill button"),
        "drawer": R("dimension", "{spacing.8}", "FilterableSearchActions__Container", "border-radius: var(--8) var(--8) var(--4) var(--4)", "Top corners of the black Search settings drawer"),
    },
    "borderWidth": {
        "default": R("dimension", "1px", "Modal__HeadContainer", "border-bottom: 1px solid var(--grey-2)", "Every drawn border and rule is 1px; the app has no other border width"),
        "ring": R("dimension", "2px", "Select__Trigger", "&:focus { box-shadow: black 0px 0px 0px 2px", "The black ring a focused select draws"),
        "thumb-ring": R("dimension", "4px", "Slider__Thumb", "box-shadow: 0 0 0 4px var(--lavender)", "The lavender ring round a slider thumb (5px when focused)"),
    },
    "size": {
        "header": V("--h-header", "Panel header height"),
        "nav": R("dimension", "48px", "Scaffold__Nav", "height: 48px"),
        "nav-button": R("dimension", "32px", "ExploreSession__NavButton", "height: 32px"),
        "wordmark-width": R("dimension", "208px", "Navigation__StyledWordmark", "width: 208px"),
        "axis-corner": R("dimension", "22px", "GraphAxes__CornerSpace", "width: 22px; height: 22px"),
        "axis-gutter": {"type": "dimension", "value": "30px", "graph": ("vertical 30 px wide", "5"), "description": "Width of the vertical axis strip and height of the horizontal one"},
        "list-min": {"type": "dimension", "value": "400px", "graph": ("list (min 400, max 450 px)", "4"), "description": "Split view: the list column"},
        "list-max": {"type": "dimension", "value": "450px", "graph": ("list (min 400, max 450 px)", "4")},
        "actions-min": R("dimension", "290px", "Scaffold__Actions", "min-width: 290px", "The right-hand Next search column"),
        "actions-max": R("dimension", "390px", "Scaffold__Actions", "max-width: 390px"),
        "root-max": R("dimension", "1400px", "Dashboard__StyledRoot", "max-width: 1400px", "Home page width"),
        "control-sm": M("dimension", "24px", "button-link", "default", "height", "Small text buttons (Link Zotero)"),
        "control-md": R("dimension", "32px", "ExploreSession__NavButton", "height: 32px", "Top-bar pills, the account button, session buttons"),
        "control-lg": M("dimension", "40px", "settings-tab", "current", "height", "Tab rows and the typed-phrase input"),
        "control-xl": M("dimension", "56px", "button-primary", "default", "height", "Dialog action buttons (Done, Cancel, Permanently Delete My Account)"),
        "field": M("dimension", "37px", "text-field", "filled", "height", "A dialog text field"),
        "icon": G("dimension", "16px", "button svg", "font-size: 16px", "The default icon in a button"),
        "icon-sm": R("dimension", "14px", "ListItemSideButton__StyledButton", "& svg { font-size: 14px", "List side buttons, the lock in a notice"),
        "icon-md": R("dimension", "18px", "ListItemSideButton__StyledButton", "& svg { font-size: 18px", "Larger side-button icons, graph toolbar"),
        "icon-lg": M("dimension", "20px", "drawer-head", "search-settings", "iconWidth", "The drawer chevron; the largest UI icon measured (the dialog close cross is 16px)"),
        "focus-ring-width": M("dimension", "1px", "button-primary", "focus-visible", "outlineWidth", "The browser's auto outline, 1px, recoloured by button:focus and input:focus"),
        "focus-ring-offset": M("dimension", "0px", "button-primary", "focus-visible", "outlineOffset"),
        "dialog-width": R("dimension", "650px", "Account__StyledModal", "width: 650px; height: 600px", "Account Settings; form and confirm dialogs fit their content between 500 and 800px"),
        "dialog-min": R("dimension", "500px", "Confirm__StyledModal", "min-width: 500px"),
        "dialog-max": R("dimension", "800px", "Confirm__StyledModal", "max-width: 800px"),
        "menu-min": R("dimension", "220px", "Dropdown__Content", "min-width: 220px"),
        "menu-max": R("dimension", "500px", "Dropdown__Content", "max-width: 500px"),
        "settings-tabs": R("dimension", "180px", "TabbedContent__Sidebar", "width: 180px", "The tab column in Account Settings"),
    },
    "breakpoint": {
        "too-small": Q("640px", "(max-width: 640px)", "At this width or less every page is covered by the Screen too small notice; there is no phone layout"),
        "sm": A("dimension", "640px", 'sm:640', "1", "The app's script breakpoints (useBreakpoint); sm changes the upgrade dialog's price line"),
        "md": A("dimension", "768px", 'md:768', "1", "The home hero illustration shows above this width"),
        "xmd": A("dimension", "896px", 'xmd:896', "1", "Below this width the home cards stack in one column"),
        "lg": A("dimension", "1024px", 'lg:1024', "1", "Below this width a split search view falls back to the list"),
        "xl": A("dimension", "1280px", 'xl:1280', "1", "Declared; no use found"),
        "2xl": A("dimension", "1536px", '"2xl":1536', "1", "Declared; no use found"),
    },
    "grid": {
        "home-columns": A("number", 3, 'isSmallerThan("xmd")', "1", "Home cards per row at 896px and wider: three equal flex children, measured (home-columns row-1440); there is no CSS grid"),
        "home-columns-narrow": A("number", 1, 'isSmallerThan("xmd")', "1", "Below 896px the same cards stack in one column (home-columns stacked-800)"),
    },
    "zIndex": {
        "raised": R("number", 1, "ArticleAuthors__AuthorButton", "z-index: 1", "Author chips and the note composer over their neighbours"),
        "toast": R("number", 2, "ToastManager__Container", "z-index: 2", "The toast stack (mounted empty in every capture)"),
        "commander": R("number", 3, "Commander__Container", "z-index: 3", "The command bar"),
    },
    "duration": {
        "fast": R("duration", "150ms", "Commander__Container", "transition: transform 150ms, opacity 150ms"),
        "base": R("duration", "200ms", "ArticleAuthors__SlideHint", "transition: transform 200ms, opacity 200ms"),
        "slow": R("duration", "300ms", "DashboardFolders__StyledArrowRight", "transition: transform 300ms, opacity 300ms"),
        "popup": R("duration", "400ms", "Popup__Content", "animation-duration: 400ms"),
        "chevron": R("duration", "500ms", "FilterableSearchActions__Chevron", "transition: transform 500ms", "The drawer chevron and the nav logo width"),
        "dialog": R("duration", "400ms", "Modal__Content", "animation: 400ms cubic-bezier(0.16, 1, 0.3, 1)", "Dialog and scrim entrance"),
        "spinner": R("duration", "1100ms", "LoadWheel__StyledIcon", "animation: 1.1s linear 0s infinite", "One turn of the loading wheel"),
        "enter": R("duration", "200ms", "AnimatedContainer__Container", "&.ac-enter-active, &.ac-appear-active { transition: opacity 200ms, transform 200ms", "Panels, menus and toasts sliding in (200, 300 or 350ms by size)"),
        "exit": R("duration", "150ms", "AnimatedContainer__Container", "&.ac-exit-active { transition: opacity 150ms, transform 150ms", "The quickest exit (150 to 300ms)"),
        "toast": A("duration", "4000ms", "duration:P=4e3", "2", "How long a toast stays"),
        "toast-after-hover": A("duration", "2000ms", "durationAfterHover:me=2e3", "2", "How long a toast stays after the pointer leaves it"),
    },
    "easing": {
        "standard": R("cubicBezier", [0.25, 0.1, 0.25, 1], "AnimatedContainer__Container", "&.ac-enter-active, &.ac-appear-active { transition: opacity 200ms, transform 200ms", "Derived: the rule names no timing function, so CSS's default ease applies (computed 'ease' on the drawer and note composer)"),
        "out": R("cubicBezier", [0, 0, 0.58, 1], "ScrollContainer__Scrollbar", "transition: background-color 160ms ease-out", "ease-out, the scrollbar thumb's colour change"),
        "linear": R("cubicBezier", [0, 0, 1, 1], "LoadWheel__StyledIcon", "animation: 1.1s linear 0s infinite", "The spinner's constant turn"),
        "popup": R("cubicBezier", [0.16, 1, 0.3, 1], "Popup__Content", "animation-timing-function: cubic-bezier(0.16, 1, 0.3, 1)", "Popups, dropdowns and hints slide in on this"),
    },
}

SPEC_LIGHT = {
    "background": {
        "page": G("color", "{palette.grey.bg2}", "body", "background-color: rgb(238, 240, 241)", "The body colour under the corner glows; the glows cover every pixel, so it is never seen bare"),
        "surface": R("color", "{palette.base.white}", "ArticleTable__Container", "background-color: white", "Cards, the table, list rows"),
        "raised": R("color", "{palette.base.white}", "Modal__Content", "background-color: white", "Dialogs"),
        "overlay": R("color", "{palette.base.white}", "Dropdown__Content", "background-color: white", "Menus, select lists, popovers"),
        "scrim": R("color", "{palette.alpha.scrim}", "Modal__Overlay", "background-color: rgba(48, 85, 94, 0.3)", "Behind every dialog; a second dialog stacks a second scrim"),
        "panel": R("color", "{palette.base.white}", "Scaffold__Header", "background-color: white", "Panel headers, list cards, the settings panel"),
        "panel-glass": R("color", "{palette.alpha.white-50}", "ExploreStep__StyledScaffoldMain", "background-color: rgba(255, 255, 255, 0.5)", "The body of the results panel, graph included"),
        "section": R("color", "{palette.alpha.white-40}", "DashboardFolders__StyledSection", "background-color: rgba(255, 255, 255, 0.4)"),
        "panel-tint": R("color", "{palette.alpha.violet-20}", "ExploreBuilder__Container", "background-color: rgba(221, 204, 255, 0.2)", "The faint violet behind the Next Search panel"),
        "hint": R("color", "{palette.turq.25}", "GradientBackground__Container", "background-color: rgb(215, 246, 248)", "The turquoise tip strip, and the colour of the top glow"),
    },
    "gradient": {
        "glow-top": R("color", "{palette.turq.25}", "GradientBackground__TopRight", "width: 75%; padding-bottom: 40%", "Colour sampled at the top centre of the page; the glow is a 75 percent wide ellipse"),
        "glow-left": S("{palette.lavender.25}", (5, 1795), "Lower left glow"),
        "glow-bottom-right": S("{palette.peach.25}", (2870, 1795), "Lower right glow"),
    },
    "text": {
        "default": M("color", "{palette.base.black}", "home-section", "recent", "color", "Most text: body sets no colour, so it inherits the browser's black (computed on the home cards, dialogs and list cards)"),
        "primary": R("color", "{palette.grey.primary}", "ExploreGraphLegend__Container", "color: var(--grey-primary)"),
        "secondary": R("color", "{palette.grey.secondary}", "GraphAxes__AxisLabel", "color: var(--grey-secondary)"),
        "tertiary": R("color", "{palette.grey.tertiary}", "GraphAxes__AxisIcon", "color: var(--grey-tertiary)"),
        "inverse": R("color", "{palette.base.white}", "SearchSummary__InfoContainer", "color: white"),
        "link-hover": R("color", "{palette.literal.link-hover}", "ArticleTitle__Title", "color: rgb(116, 111, 163)"),
        "link": M("color", "{palette.base.black}", "empty-state-link", "default", "color", "Links keep the text colour and are told apart by weight 600 (a { font-weight: 600 }) and an underline"),
        "disabled": R("color", "{palette.grey.3}", "Select__SelectItem", "&[data-disabled] { color: var(--grey-3)", "Disabled options; disabled buttons instead drop to 30 or 50 percent opacity"),
        "on-accent": R("color", "{palette.base.black}", "ExploreFiltersStyles__ExploreFiltersButton", "background-color: var(--lavender-25); color: black", "Text on the lavender accent"),
    },
    "border": {
        "default": R("color", "{palette.grey.2}", "Modal__HeadContainer", "border-bottom: 1px solid var(--grey-2)", "Dialog head rule, field outlines"),
        "strong": R("color", "{palette.base.black}", "Popup__Content", "border: 1px solid black", "The bordered popup, the current filter pill's inset ring"),
        "line": V("--line", "Settings option cards"),
        "field": R("color", "{palette.grey.2}", "Input__form", "inset var(--grey-2)"),
        "rule": R("color", "{palette.grey.1}", "InspectorStyles__Header", "border-bottom: 1px solid var(--grey-1)"),
        "drawer": R("color", "rgb(104, 109, 121)", "FilterableSearchActions__TrayHeadButton", "border-bottom: 1px solid rgb(104, 109, 121)"),
        "focus": R("color", "{palette.selection.base}", "InspectorStyles__Content", "box-shadow: inset 0 0 0 1px var(--selection)"),
        "focus-browser": M("color", "#005fcc", "nav-logo", "focus-visible", "outlineColor", "The browser's own focus ring (outline auto), on links and elements no rule restyles; computed on the wordmark, tabs, links and the note composer"),
    },
    "action": {
        "primary": R("color", "{palette.base.black}", "ExploreBuilder__AutosaveFolderButton", "background-color: black"),
        "primary-text": R("color", "{palette.base.white}", "ExploreBuilder__AutosaveFolderButton", "color: white"),
        "primary-hover": R("color", "{palette.literal.charcoal}", "ViewSelection__Button", "&:hover { background-color: rgb(51, 51, 51)"),
        "primary-pressed": M("color", "{palette.literal.charcoal}", "button-primary", "pressed", "backgroundColor", "Pressed keeps the hover fill: no captured rule styles :active"),
        "focus-ring": G("color", "{palette.turq.50}", "button:focus, input:focus", "outline-color: var(--turq-50)", "The 1px outline every focused button and input draws; links keep the browser's blue"),
        "danger": M("color", "{palette.peach.base}", "button-danger", "disabled", "backgroundColor", "The destructive button, seen only disabled"),
        "accent": R("color", "{palette.lavender.50}", "SearchBar__SearchButton", "background-color: var(--lavender-50)", "The lavender Search button and search pill"),
        "accent-soft": R("color", "{palette.lavender.25}", "ExploreActionsMain__StyledExploreFurtherButton", "background-color: var(--lavender-25)"),
        "quiet": R("color", "{palette.alpha.black-05}", "ViewSelection__Button", "background-color: rgba(0, 0, 0, 0.05)"),
        "control": R("color", "{palette.ui.bg}", "ArticleDetailsDisplay__NavContainer", "background-color: var(--ui-bg)", "Grey pill controls in the article panel (the previous and next pill, close and action buttons)"),
        "control-hover": R("color", "{palette.ui.bg-hover}", "ArticleEvaluation__Container", "&:hover { background-color: var(--ui-bg-hover); }", "Hover on those grey controls"),
        "select-hover": R("color", "{palette.alpha.black-07}", "Select__Trigger", "&:hover { background-color: rgba(0, 0, 0, 0.07); }", "Hover on selects and the layout select"),
        "glass-hover": R("color", "{palette.alpha.white-90}", "DashboardSearch__StyledFolderSelect", "&:hover { background-color: rgba(255, 255, 255, 0.9); }", "Hover on white-glass buttons (Browse Library, the sticker and nickname buttons)"),
        "quiet-hover-inverse": R("color", "{palette.alpha.white-10}", "Toast__InlineButton", "&:hover { background-color: rgba(255, 255, 255, 0.1); }", "Quiet hover on the toast and the black drawer"),
        "quiet-hover": R("color", "{palette.alpha.black-10}", "ViewSelection__Button", "&:hover { background-color: rgba(0, 0, 0, 0.1)"),
        "upgrade": M("color", "{palette.green.base}", "nav-upgrade", "default", "backgroundColor", "The Upgrade pill and the Upgrade badges"),
        "highlighted": R("color", "{palette.selection.base}", "Dropdown__Item", "&[data-highlighted] { background-color: var(--selection)"),
    },
    "elevation": {
        "s": V("--shadow-s"), "m": V("--shadow-m"), "l": V("--shadow-l", "Toasts"),
        "s-dark": V("--shadow-s-dark", "Declared beside the light ones; no captured surface paints it"),
        "m-dark": V("--shadow-m-dark"), "l-dark": V("--shadow-l-dark"),
        "menu": {"type": "shadow", "rule": ("Dropdown__Content", "box-shadow: rgba(22, 23, 24, 0.35) 0px 10px 38px -10px, rgba(22, 23, 24, 0.2) 0px 10px 20px -15px"),
                 "value": "rgba(22, 23, 24, 0.35) 0px 10px 38px -10px, rgba(22, 23, 24, 0.2) 0px 10px 20px -15px",
                 "description": "Menus and select lists"},
        "ring-strong": M("shadow", "rgb(0, 0, 0) 0px 0px 0px 1px inset", "list-card", "selected", "boxShadow", "A 1px black ring drawn inside: selected cards, the current library list and filter pill"),
        "ring-field": M("shadow", "rgb(201, 205, 211) 0px 0px 0px 1px inset", "text-field", "filled", "boxShadow", "A 1px grey-2 ring inside a light field and a disabled button"),
        "ring-field-dark": M("shadow", "rgb(221, 224, 228) 0px 0px 0px 1px inset", "drawer-input", "keyword", "boxShadow", "The ring inside the black drawer's inputs"),
        "ring-highlight": M("shadow", "rgb(167, 212, 255) 0px 0px 0px 1px inset", "list-card", "tinted", "boxShadow", "The selection-blue ring on a highlighted card and the article panel"),
        "toast": {"type": "shadow", "rule": ("Toast__ToastFill", "box-shadow: rgba(0, 0, 0, 0.3) 3px 3px 12px"),
                  "value": "rgba(0, 0, 0, 0.3) 3px 3px 12px", "description": "Toasts"},
        "dialog": {"type": "shadow", "rule": ("Modal__Content", "box-shadow: rgba(0, 0, 0, 0.5) 3px 3px 12px"),
                   "value": "rgba(0, 0, 0, 0.5) 3px 3px 12px", "description": "Dialogs, over the scrim"},
        "popup": {"type": "shadow", "rule": ("Popup__Content", "box-shadow: rgba(14, 18, 22, 0.35) 0px 10px 38px -10px, rgba(14, 18, 22, 0.2) 0px 10px 20px -15px"),
                  "value": "rgba(14, 18, 22, 0.35) 0px 10px 38px -10px, rgba(14, 18, 22, 0.2) 0px 10px 20px -15px",
                  "description": "Popups, hints and dropdowns (dropdowns use 22, 23, 24)"},
    },
    "status": {
        "success": {"fill": V("--activity-success-bg"), "text": V("--activity-success-dark"),
                    "border": V("--activity-success", "No captured surface draws a status border; this is the status's strong step")},
        "warning": {"fill": R("color", "{palette.activity.important-bg}", "Confirm__SafeguardContainer", "background-color: var(--activity-important-bg)", "The typed-phrase box in a destructive confirmation"),
                    "text": V("--activity-important-dark"),
                    "border": R("color", "{palette.activity.important}", "GraphBrokenAxes__BrokenAxesDropdown", "background-color: var(--activity-important)", "Also the Positions moved pill and the account alert dot")},
        "danger": {"fill": V("--activity-error-bg"), "text": V("--activity-error-dark"),
                   "border": V("--activity-error", "No captured surface draws a status border; this is the status's strong step")},
        "info": {"fill": R("color", "{palette.green.25}", "PaywallIndicator__VerboseContainer", "background-color: var(--green-25)", "The notice banner (previewing a paid setting)"),
                 "text": R("color", "{palette.grey.primary}", "PaywallIndicator__VerboseContainer", "color: var(--grey-primary)"),
                 "border": R("color", "{palette.green.base}", "PaywallIndicator__Container", "background-color: var(--green)", "The notice draws no border; this is its badge's fill, the hue's strong step")},
    },
    "component": {
        "nav-link-active": R("color", "{palette.base.white}", "Navigation__LinkContainer", "background-color: white"),
        "nav-top-button": R("color", "{palette.alpha.white-50}", "Navigation__TopButton", "background-color: rgba(255, 255, 255, 0.5)"),
        "search-bar": R("color", "{palette.base.black}", "SearchBar__Container", "background-color: black"),
        "search-summary": R("color", "{palette.lavender.50}", "SearchSummary__Container", "background-color: var(--lavender-50)"),
        "search-summary-info": R("color", "{palette.base.black}", "SearchSummary__InfoContainer", "background-color: black"),
        "search-summary-label": S("{palette.base.white}", (160, 260), "The white half of the pill; no rule names it"),
        "filter-button": R("color", "{palette.grey.bg2}", "ExploreHeader__SimpleFilterPopupButton", "background-color: var(--grey-bg2)"),
        "legend-chip-hover": R("color", "{palette.base.white}", "ExploreGraphLegend__ItemContainer", "&:hover { background-color: white"),
        "axis-line": R("color", "{palette.grey.tertiary}", "GraphAxes__AxisLine", "background-color: var(--grey-tertiary)"),
        "axis-line-length": R("dimension", "{spacing.8}", "GraphAxes__AxisLine", "width: var(--8)"),
        "axis-hover": R("color", "{palette.base.white}", "GraphAxes__AxisContainer", "&:hover { background-color: white"),
        "toolbar-hover": R("color", "{palette.alpha.black-05}", "GraphControls__StyledButton", "&:hover { background-color: rgba(0, 0, 0, 0.05)"),
        "card-rule": S("{palette.grey.1}", (200, 598), "Line between a card's title block and its abstract; sampled #dfe1e4"),
        "drawer": R("color", "{palette.base.black}", "FilterableSearchActions__Container", "background-color: black"),
        "drawer-button": S("{palette.literal.drawer-button}", (2690, 1745), "The drawer's Search button while there is nothing new to search"),
        "option-selected": R("color", "{palette.selection.light}", "LayoutSettingsGeneric__OptionContainer", "background-color: var(--selection-light)"),
        "option-selected-hover": R("color", "{palette.selection.base}", "LayoutSettingsGeneric__OptionContainer", "&:hover { background-color: var(--selection)"),
        "option-padding": R("dimension", "12px", "LayoutSettingsGeneric__OptionContainer", "padding: 12px"),
        "settings-tab-active": R("color", "{palette.base.black}", "LayoutSettings__NavItemContainer", "background-color: black"),
        "positions-moved": R("color", "{palette.activity.important}", "GraphBrokenAxes__BrokenAxesDropdown", "background-color: var(--activity-important)"),
        "folder-tint": R("color", "{palette.alpha.amber-20}", "ArticleFolders__FolderContainer", "background-color: rgba(240, 125, 89, 0.2)"),
        "tooltip": R("color", "{palette.literal.charcoal}", "HintContainer__Content", "background-color: rgb(51, 51, 51)"),
        "list-card-tinted": M("color", "#f0f6ff", "list-card", "tinted", "backgroundColor", "A result card while its node is hovered in the graph (set by script; no rule names it)"),
        "note-placeholder": M("color", "#aaaaaa", "note-composer", "default", "textColor", "The note composer's italic placeholder line"),
        "toast": R("color", "{palette.literal.charcoal}", "Toast__ToastFill", "background-color: rgb(51, 51, 51)", "The toast bar, with white text"),
        "citation-box": R("color", "{palette.selection.light}", "CopyContainer__Container", "background-color: var(--selection-light)", "The citation box at rest and on hover"),
        "incomplete-warning": R("color", "{palette.peach.25}", "IncompleteInlineWarning__Container", "background-color: var(--peach-25)", "Incomplete data chip and banner"),
        "drawer-row": R("color", "{palette.literal.drawer-row}", "ExploreFilters__ItemContainer", "background-color: rgb(53, 53, 53)"),
        "drawer-row-on": R("color", "{palette.literal.drawer-row-on}", "ExploreFilters__ItemContainer", "background-color: rgb(77, 76, 91)"),
        "tab-current": R("color", "{palette.grey.bg2}", "TabbedContent__Option", "background-color: var(--grey-bg2)", "The current vertical tab in Account Settings"),
        "tab-hover": R("color", "{palette.grey.bg1}", "TabbedContent__Option", "&:hover { background-color: var(--grey-bg1)"),
        "table-row-hover": M("color", "{palette.grey.bg2}", "table-row", "hover", "backgroundColor"),
    },
}

# ---------------------------------------------------------------------------------------------------
# Building

VAR_PATH = {}  # css var name -> token path, so var(--x) inside a value becomes an alias


def find_rule(comp, decl):
    rules = RULES.get(comp)
    if rules is None:
        raise KeyError(f"no component {comp} in raw/css-vars.json")
    flat = " ".join(rules)
    for piece in [p.strip() for p in decl.split(";")]:
        if piece and piece not in flat:
            raise KeyError(f"{comp}: {piece!r} is not in its rules")


def var_value(name):
    if name not in ROOT:
        raise KeyError(f"{name} is not a :root variable in raw/css-vars.json")
    return ROOT[name]


def leaf(path, spec):
    ty = spec.get("type")
    ext = {}
    if "var" in spec:
        raw = var_value(spec["var"]).strip()
        src = f"css var {spec['var']}"
        m = re.fullmatch(r"var\((--[\w-]+)\)", raw)
        if m:
            if m.group(1) not in VAR_PATH:
                raise KeyError(f"{path}: {spec['var']} refers to {m.group(1)}, which has no token")
            val = "{" + VAR_PATH[m.group(1)] + "}"
            ty = ty or "color"
        elif re.search(r"\dpx\s+-?\d", raw):
            ty, val = "shadow", parse_shadow(raw)
        elif DIM.fullmatch(re.sub(r"^(-?)\.", r"\g<1>0.", raw)):
            ty, val = "dimension", re.sub(r"^(-?)\.", r"\g<1>0.", raw)
        else:
            ty, val = "color", norm_color(raw)
        VAR_PATH.setdefault(spec["var"], path)
    elif "rule" in spec:
        comp, decl = spec["rule"]
        find_rule(comp, decl)
        val = spec["value"]
        src = f"css rule {comp}: {decl}"
    elif "global" in spec:
        sel, decl = spec["global"]
        rules = [g for g in GLOBALS if g.startswith(sel + " {")]
        flat = " ".join(rules)
        for piece in [x.strip() for x in decl.split(";")]:
            if not rules or (piece and piece not in flat):
                raise KeyError(f"{path}: {sel} {{ {piece} }} is not in raw/css-vars.json globals")
        val, src = spec["value"], f"css rule {sel}: {decl}"
    elif "app" in spec:
        ident, sec = spec["app"]
        if ident not in APP_NOTES:
            raise KeyError(f"{path}: {ident!r} is not in raw/app-code-notes.md")
        val, src = spec["value"], f"app code: {ident} (raw/app-code-notes.md section {sec})"
    elif "media" in spec:
        if spec["media"] not in MEDIA:
            raise KeyError(f"{path}: @media {spec['media']} is not in raw/css-vars.json")
        val, src = spec["value"], f"css @media {spec['media']}"
    elif "computed" in spec:
        comp, state, prop = spec["computed"]
        got = COMPUTED[comp]["states"][state]
        raw = (f"{got['rect']['h']:g}px" if prop == "height" else f"{got['icon']['w']:g}px" if prop == "iconWidth"
               else got["textStyle"]["color"] if prop == "textColor" else got["style"][prop])
        val = spec["value"]
        want = val
        if is_alias(val):
            want = ALL_PRE.get(val[1:-1])
        if ty == "color":
            same = norm_color(raw) == norm_color(want)
        else:
            same = raw == want
        if not same:
            raise ValueError(f"{path}: {comp} {state} {prop} is {raw}, not {want}")
        src = f"computed {comp} {state}: {prop} {raw} (raw/components-computed.json)"
    elif "sample" in spec:
        shot, (x, y) = spec["sample"]
        val, src = spec["value"], f"sampled {shot} at ({x}, {y})"
    elif "graph" in spec:
        ident, sec = spec["graph"]
        if ident not in NOTES:
            raise KeyError(f"{path}: {ident!r} is not in raw/graph-code-notes.md")
        val, src = spec["value"], f"graph engine: {plain(ident)} (raw/graph-code-notes.md section {sec})"
    elif "font" in spec:
        if spec["font"] not in CSS["fonts"]:
            raise KeyError(f"{path}: font {spec['font']} was not loaded by the app")
        val, src = spec["value"], f"raw/css-vars.json fonts: {spec['font']}"
    else:
        raise ValueError(f"{path}: leaf has no source")
    if ty == "color" and isinstance(val, str) and not is_alias(val):
        val = norm_color(val)
    if ty == "shadow" and isinstance(val, str):
        val = parse_shadow(val)
    check(path, ty, val)
    t = {"$value": val, "$type": ty, "$extensions": {"source": src}}
    if spec.get("description"):
        t["$description"] = spec["description"]
    return t


def build(node, path=""):
    out = {}
    for k, v in node.items():
        p = f"{path}.{k}" if path else k
        if isinstance(v, dict) and ("type" in v or "var" in v):
            out[k] = leaf(p, v)
        else:
            out[k] = build(v, p)
    return out


def plain(ident):
    """The identifier as quoted in the notes, without the notes' Markdown emphasis and code marks."""
    return ident.replace("**", "").replace("`", "")


def graph_leaf(path, spec):
    ident, sec = spec["id"], spec["section"]
    if ident not in NOTES:
        raise KeyError(f"{path}: {ident!r} is not in raw/graph-code-notes.md")
    ty, val = spec["type"], spec["value"]
    check(path, ty, val)
    t = {"$value": val, "$type": ty,
         "$extensions": {"source": f"graph engine: {plain(ident)} (raw/graph-code-notes.md section {sec})"}}
    for k, v in sorted(spec.get("extensions", {}).items()):
        t["$extensions"][k] = norm_color(v) if ty == "color" else v
    desc = spec.get("description", "")
    if spec.get("inferred"):
        desc = ("Inferred. " + desc).strip()
    if desc:
        t["$description"] = desc
    return t


def build_graph(node, path):
    return {k: graph_leaf(f"{path}.{k}", v) if "type" in v else build_graph(v, f"{path}.{k}")
            for k, v in node.items() if not k.startswith("_")}


# spacing first, straight from --neg2..--16, so radius and size can alias it
spacing = {}
for name in ROOT:
    m = re.fullmatch(r"--(neg)?(\d+)", name)
    if m:
        spacing[("neg" if m.group(1) else "") + m.group(2)] = V(name)
SPEC_CORE["spacing"] = spacing

core = {}
for group in ("palette", "spacing", "fontFamily", "fontWeight", "fontSize", "typography", "radius", "borderWidth", "size", "breakpoint", "grid", "zIndex", "duration", "easing"):
    core[group] = build(SPEC_CORE[group], group)
core = {k: core[k] for k in SPEC_CORE}  # keep the SPEC's order in the file
core["graph"] = build_graph(GRAPH, "graph")
ALL_PRE = {}
def _flat(tree, prefix=""):
    for k, v in tree.items():
        if isinstance(v, dict) and "$value" in v:
            ALL_PRE[prefix + k] = v["$value"]
        elif isinstance(v, dict):
            _flat(v, prefix + k + ".")
_flat(core)
for _ in range(3):  # resolve aliases among primitives
    for k, v in ALL_PRE.items():
        if is_alias(v) and v[1:-1] in ALL_PRE:
            ALL_PRE[k] = ALL_PRE[v[1:-1]]
light = build(SPEC_LIGHT)

# ---------------------------------------------------------------------------------------------------
# Aliases: every one must point at a token, and a whole-value alias at a token of the same type


def tokens_of(tree, prefix=""):
    for k, v in tree.items():
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from tokens_of(v, prefix + k + ".")


ALL = dict(tokens_of(core)) | dict(tokens_of(light))
if len(ALL) != len(list(tokens_of(core))) + len(list(tokens_of(light))):
    raise ValueError("a token name is used in both sets")


def aliases(v):
    if isinstance(v, str):
        return ALIAS.findall(v)
    if isinstance(v, dict):
        return [a for x in v.values() for a in aliases(x)]
    if isinstance(v, list):
        return [a for x in v for a in aliases(x)]
    return []


for n, t in ALL.items():
    for a in aliases(t["$value"]):
        if a not in ALL:
            raise KeyError(f"{n}: alias {{{a}}} points at nothing")
    if is_alias(t["$value"]):
        target = ALL[t["$value"][1:-1]]
        if target["$type"] != t["$type"]:
            raise TypeError(f"{n}: is {t['$type']} but its alias {t['$value']} is {target['$type']}")

# CSS custom property names must not collide either (build_style_guide.py turns dots into dashes)
css_names = {}
for n in ALL:
    c = re.sub(r"[^a-zA-Z0-9-]", "-", n.replace(".", "-"))
    if c in css_names:
        raise ValueError(f"{n} and {css_names[c]} both become --{c}")
    css_names[c] = n

tokens = {
    "core": core,
    "light": light,
    "$themes": [
        {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"},
         "$description": "The only theme ResearchRabbit paints. The graph engine carries dark and print colours for edges and labels; they are kept as $extensions on those tokens, not as a set."},
    ],
    "$metadata": {"tokenSetOrder": ["core", "light"]},
}
(HERE / "tokens.json").write_text(json.dumps(tokens, indent=2, ensure_ascii=False) + "\n")


def count(d):
    return sum(count(v) for v in d.values()) if isinstance(d, dict) and "$value" not in d else 1


print({"core": count(core), "core.graph": count(core["graph"]), "light": count(light)})
