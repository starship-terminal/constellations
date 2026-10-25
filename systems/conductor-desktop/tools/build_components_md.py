#!/usr/bin/env python3
"""Write components.md from raw/components.<theme>.json, tokens.json and components/crops/.

    python3 tools/build_components_md.py

One entry per checklist component (docs/DESIGN-SYSTEM.md, desktop wording), listing the parts that
show it, the states captured in each theme with their crops, and the measured values written as the
token that holds them (the value after it). A value no token holds is written raw and counted.
PRODUCT (adapt): INVENTORY, NOTES and GAPS. Standard library only, deterministic.
"""
import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from colour import color, is_color  # noqa: E402
from prefer import skip  # noqa: E402

PKG = pathlib.Path(__file__).resolve().parent.parent
TOK = json.loads((PKG / "tokens.json").read_text())
CAP = {t: json.loads((PKG / "raw" / f"components.{t}.json").read_text()) for t in ("dark", "light")}
CROPS = {p.name for p in (PKG / "components" / "crops").glob("*.png")}
STATE_ORDER = ["default", "hover", "focus-visible", "focus", "pressed", "typed", "empty", "error"]

# PRODUCT (adapt): checklist component -> (parts that show it, note)
INVENTORY = [
    ("Button", ["button-primary", "button-primary-sm", "toast-button-primary", "button-outline", "button-outline-dialog", "button-secondary", "button-destructive", "button-destructive-trigger", "button-primary-disabled", "review-button"],
     "Four looks, all 6px (`radius.md`) and 32px tall, or 28px in toolbars. Primary is the ink fill (`base.foreground`: warm near-black in light, near-white in dark) with `base.background` text: Create repo and add project, Restart on the update toast, Create on Home. Outline is `base.background` with a `base.input-border` edge (Cancel, Open System Settings, Browse). Secondary is the `base.secondary` grey with no edge (Add run script). Destructive is the red fill (`base.destructive` at 90%) and appears only as the confirm button of a removal; the trigger that opens it (Remove repository) is red text. Hover takes a fill to 90% or adds the `base.popover-accent` wash; pressed keeps the fill and darkens it with an inset shadow (`active:inset-shadow-[0_0_0_999px_rgb(0_0_0/0.1)]`) and a 1px drop. Buttons draw no focus ring (`focus-visible:ring-none`). Disabled is the same control at 50% opacity (the primary button while the repository name is taken)."),
    ("Icon button", ["composer-add", "header-icon-button", "settings-icon-button", "message-action", "tab-add", "open-in-chevron", "send-button"],
     "Ghost 24px squares with a 4px radius: the icon is `base.muted-foreground` and turns `base.foreground` on a `base.popover-accent` wash under the pointer. The composer's send button is the one filled icon button: ink at 50% while the composer is empty, solid once text is typed, and a stop square while an agent runs."),
    ("Link", ["file-link", "message-meta", "toml-button"],
     "Links in agent replies are file names in `link.foreground`, the warm tan (`#a4847f` light, `#cca694` dark), underlined on hover. External links in Settings (Learn more) are foreground text with an arrow; there is no blue link colour."),
    ("Text field", ["text-field", "text-field-dialog", "settings-search", "palette-input", "home-search", "menu-search"],
     "28 to 38px (the Settings search 28, dialog fields 32, the terminal font field 38), `base.background` fill, `base.input-border` edge, 6px radius, 14px text. Focus turns the edge `base.special`, the tan (`focus:!border-special`), with no ring. Settings search carries a Command F hint; the palette and model-picker searches are borderless rows inside their popups."),
    ("Text area", ["composer", "composer-editor", "composer-placeholder", "composer-text", "composer-compact", "text-area"],
     "The composer is a 12px-radius box on `base.muted` with a `base.border` edge, a TipTap editor, a muted placeholder (Ask to make changes, @mention files, run /commands), a ⌘L to focus pill, and a toolbar row (model and effort, add, send). It collapses to one line when a file or diff is open. Scripts in repository settings are code-editor text areas."),
    ("Select", ["select", "select-dialog", "filter-select", "listbox", "option", "option-selected", "option-highlighted", "model-button"],
     "Base UI's select: an outlined 32px trigger with an up-down chevron; its listbox is a raised popover (`base.popover`) with a check on the selected option and a `base.popover-accent` highlight. Home's filters (Hiding archived, Last active) are ghost selects; the composer's model picker is a ghost trigger that opens a menu."),
    ("Checkbox", ["checkbox", "checkbox-box"], "One in the product's captured screens: Viewed, on a diff, a 16px box with a label. The capture only hovered it; marking a file viewed was not done. Most yes or no settings are switches."),
    ("Radio", [], "Radio buttons are on Settings > Git (Branch name prefix: GitHub username, Custom, None), visible in [settings-git](screenshots/dark/settings-git.png); they were not measured as a part. The diff's Unified / Split toggle is a segmented control (see Tabs)."),
    ("Switch", ["switch-on", "switch-off", "menu-switch"],
     "40 x 20px, ink (`base.switch-background`) when on with a `base.switch-foreground` thumb, `base.input` when off. Focus is a 2px `base.ring` ring with a 2px offset (`focus-visible:ring-2 ring-offset-2`). The model menu's Fast toggle is the same switch."),
    ("Tabs", ["chat-tab-selected", "chat-tab", "file-tab", "diff-tab", "panel-tab", "panel-tab-selected", "bottom-tab", "bottom-tab-selected", "palette-tab", "palette-tab-selected", "segmented", "segmented-off"],
     "Three kinds. Chat tabs across the top of the workspace (40px, 176px wide) mark the selected one with a warm underline; the right panel's All files, Changes and Checks are 28px pills with a 6px radius, the selected one filled (#ecebeb in light, #2c2a28 in dark, a value no token holds); the bottom panel's Setup, Run and Terminal are text tabs with the same underline. The palette's scope filters (All, Workspaces, Projects, Actions, Settings) are small pills. The diff's Unified and Split icons sit in a segmented control with a filled chip on the selected one."),
    ("Menu", ["menu", "menu-item", "menu-item-highlighted", "submenu", "menu-footer", "menu-group-label", "status-dot", "callout"],
     "Base UI menus: `base.popover` with a 1px `base.popover-ring` ring for an edge, 8px radius, Tailwind's shadow-md, 4px padding; 32px items with a 6px radius, a `base.popover-accent` highlight, shortcuts right-aligned in `base.muted-foreground`, submenus with a chevron. The model menu adds a search row, drag handles, the effort submenu, a Fast switch and a footer of hints; a New: Sonnet 5.5 callout floats beside it. The workspace status submenu uses coloured status dots (`status.*`)."),
    ("Context menu", ["menu", "menu-item"], "Right-clicking a workspace opens the same menu: Mark as unread, Pin, Set status, Move to section, Rename, Copy link, Archive, each with a single-key or chord shortcut. Archive is ordinary text, not red."),
    ("Tooltip", ["tooltip", "tooltip-kbd"], "A small translucent label (`base.popover` at 50% with backdrop-blur-md and a `base.popover-ring` ring, 4px radius, 12px text) with the shortcut in keycaps beside the label, after a hover delay."),
    ("Dialog", ["dialog", "dialog-title", "dialog-body", "label", "helper", "inline-code", "backdrop", "kbd", "listbox", "palette-group", "palette-item", "palette-item-highlighted", "palette-empty", "popover", "popover-label"],
     "Base UI's alert dialog: `base.background` with a `base.border` edge, 12px radius, 24px padding, shadow-lg, 512px wide, over black at 50% with backdrop-blur-xs. Title 18px medium, body 14px muted, inline code chips on `base.muted`. The removal confirmation is the small variant (Cancel outline, Remove destructive); the GitHub repository offer is a form with a select, a text field, helper text and a primary button. The command palette (⌘K) is a 672px dialog with a search row, scope pills, grouped results with icons and shortcuts, a highlighted row, and an empty state (No results found). Keyboard shortcuts is a sheet-sized dialog listing every shortcut in keycaps."),
    ("Toast", ["toast", "toast-title", "toast-close", "toast-button", "toast-button-primary"], "Conductor's update notice is a Sonner toast pinned bottom right: inverted from the app in dark (`#000000` fill, `#333333` edge) and white in light, 8px radius, a title, one line, See changes and Restart. It keeps Sonner's own colours, not the app's tokens. No other toast appeared."),
    ("Card", ["system-card", "empty-card", "diff-chip", "file-chip"],
     "Flat. The new-workspace card (You're in a new copy of conductor called dalat) is `base.muted` with an 8px radius and no edge; the run panel's empty state and Settings > Environment's No variables set are dashed or solid `base.border` boxes with centred muted text; Home's empty-state actions (Open project, Open GitHub project, Quick start), seen only before a project was added ([home-empty](screenshots/dark/home-empty.png)), are bordered cards; they were not measured. File and diff chips are small outlined pills."),
    ("List row", ["sidebar-nav-item", "repo-row", "repo-icon", "workspace-row-selected", "workspace-name", "settings-nav-item", "settings-nav-selected", "settings-row", "settings-row-title", "settings-row-description", "tree-row", "tree-row-selected", "tree-label", "list-row", "list-meta", "changes-row"],
     "Sidebar rows are 32px with a 6px radius: `base.sidebar-foreground` text at 70% (light) or 90% (dark), a `sidebar.accent` wash on hover and when selected. Repository headers are semibold with a 16px letter tile; the workspace row adds a branch icon and the diff count in green. Settings rows put a 14px medium title over a 14px muted description with the control on the right, separated by hairline rules. File tree rows are 28px Geist Mono at 12px. Home's workspace list is 44px rows with the repository and relative time on the right."),
    ("Table", [], "Not present as a table. The agent's account details on Settings > Agents are a bordered two-column list, visible in [settings-agents-bottom](screenshots/dark/settings-agents-bottom.png), not measured."),
    ("Avatar", ["account-button"], "The account's photo, round, on Settings > Account ([settings-account](screenshots/dark/settings-account.png)) and small in the sidebar's account button, beside the account's emoji and name. The photo was not measured: the part meant for it matched another image, so its reading is left out."),
    ("Badge", ["plan-badge", "count-badge", "sidebar-diff-count", "count-mono", "diff-added", "diff-removed", "kbd", "focus-hint"],
     "The plan badge (FREE) is a 2px-radius dashed outline in muted text. Counts are bare Geist Mono numbers (Changes 1, the repository's workspace count); diff counts are `git.green` and `git.red`. Keycaps are small muted boxes; the composer's ⌘L to focus hint is a `base.muted` pill."),
    ("Toolbar", ["breadcrumb", "open-in-button", "open-in-chevron", "status-warning", "resize-handle", "display-button", "back-button"],
     "The workspace header holds the repository and branch breadcrumb, the workspace's ... (target branch) popover, an Open in split button (Finder and nine editors and terminals), and the right-panel toggle; the right panel's header shows PR status (Couldn't load PR info with a warning icon, since the scratch repository has no GitHub remote). Panels are separated by draggable 8px handles."),
    ("Conversation", ["user-message", "user-message-text", "assistant-text", "assistant-heading", "list-item", "tool-summary", "tool-call", "tool-call-read", "tool-arg", "message-meta"],
     "Not on the checklist; Conductor's chat. The prompt is a right-aligned block on `base.highlight` (a warm rose tint) with `base.highlight-foreground` text and a 4px radius; replies are plain 14px text on the page, with 20px semibold headings and bullets. A turn's tool calls fold into one line (2 tool calls, 1 message) that expands into rows of an icon, a verb (List files, Write 1 lines, Read 2 lines) and a Geist Mono argument chip. Under each reply: duration and time, copy, more, and a diff chip (hello.txt +1 -0)."),
    ("Diff and file view", ["diff-code", "diff-line-added", "diff-gutter-added", "markdown-h1", "markdown-p", "code-sample"],
     "Not on the checklist. Diffs render in Geist Mono 13px inside a shadow root (@pierre/diffs): added lines on a green wash (`git.new-line-bg` mixed over the page), a green gutter number and a green bar. Markdown files render as a preview with a 30px semibold h1; the Appearance pane's code sample shows the syntax colours (`code.*`)."),
    ("Terminal", ["terminal", "terminal-rows"], "The Terminal tab is xterm drawn with Conductor's terminal palette (`terminal.*`) on `base.background`, in the owner's shell; the capture opened it and typed nothing."),
]
GAPS = [
    "Approval prompt: none appeared. The default agent (GPT-5.6 Sol, Codex) ran both test prompts without asking, and Settings > Account > Claude Code tool approvals is off; the capture changed neither.",
    "Hover, focus-visible and pressed states were forced by copying the stylesheet's own :hover, :focus-visible and :active rules onto a capture attribute, because Safari's Web Inspector console cannot force pseudo-classes and the pointer was not moved (another app was being driven by pointer). Rules marked !important inside a cascade layer (`focus:!border-special` on inputs) beat the copy, so input focus is recorded from the class list, not painted; and a copied rule whose class name itself contains `:focus-visible` (`[button,a]:focus-visible:ring-3`) did not apply. See README What to distrust.",
    "Loading at app start (Conductor's lottie loader) and onboarding: not captured. The account was already signed in and onboarded, and the app was not restarted during the capture.",
    "Radio buttons (Settings > Git) and the agent account table (Settings > Agents) are in the screenshots but were not measured as parts.",
    "Light covers the same screens as dark except the empty Home before a project was added (dark only) and the Workspace not found error (light only).",
    "A destructive confirmation was opened and cancelled (Remove repository). Archive has no confirmation and was not used.",
    "Sheets: none found. Cloud workspaces, Linear and GitHub connections were not opened (they need an account connection).",
]


def flat(tree, prefix=()):
    for k, v in tree.items():
        if k.startswith("$"):
            continue
        if isinstance(v, dict) and "$value" in v:
            yield prefix + (k,), v
        elif isinstance(v, dict):
            yield from flat(v, prefix + (k,))


CORE = dict(flat(TOK["core"]))
SETS = {t: dict(flat(TOK[t])) for t in ("light", "dark")}
CORE_NAMES = re.compile(r"^base\.(background|foreground|card|popover|primary|primary-foreground|secondary|muted|muted-foreground|accent|accent-foreground|border|input|ring|destructive)$")
PREFER = ["base", "role", "sidebar", "link", "git", "status", "highlight", "tip", "warning", "todo", "terminal", "code", "checks", "color"]


def resolve(t, v):
    while isinstance(v, str) and re.fullmatch(r"\{[^{}]+\}", v):
        p = tuple(v[1:-1].split("."))
        v = (SETS[t].get(p) or CORE[p])["$value"]
    return v


def colour_index(t):
    idx = {}
    for p, tok in SETS[t].items():
        if tok["$type"] == "color" and p[0] in PREFER:
            idx.setdefault(resolve(t, tok["$value"]), []).append(p)
    for v in idx.values():
        v.sort(key=lambda p: (not CORE_NAMES.match(".".join(p)), PREFER.index(p[0]), len(".".join(p)), p))
    return {k: [".".join(x) for x in v] for k, v in idx.items()}


# The token group a value is looked up in first, by the property it was read from.
NONROLE = ["sidebar.", "link.", "highlight.", "warning.", "tip.", "git.", "status.", "todo.", "checks.", "code.", "terminal."]
BY_PROP = {"background-color": ["base."] + NONROLE + ["role."], "color": ["base.", "role.text"] + NONROLE + ["role."],
           "border-top-color": ["base.", "role.border"] + NONROLE + ["role."]}


def pick(paths, prop):
    for pre in BY_PROP.get(prop, []):
        for x in paths:
            if x.startswith(pre):
                return x
    return paths[0]


CIDX = {t: colour_index(t) for t in SETS}
DIDX = {}
for group in ("radius", "controlHeight", "spacing", "fontSize", "lineHeight", "letterSpacing"):
    for p, tok in CORE.items():
        if p[0] == group and isinstance(tok["$value"], str):
            DIDX.setdefault((group, tok["$value"]), ".".join(p))
stats = {"written": 0, "token": 0}


def as_token(t, prop, raw):
    stats["written"] += 1
    if prop in ("background-color", "color", "border-top-color") and is_color(raw):
        v = color(raw)
        if v == "rgba(0, 0, 0, 0)":
            stats["written"] -= 1
            return None
        if v in CIDX[t]:
            stats["token"] += 1
            return f"`{pick(CIDX[t][v], prop)}` {v}"
        return f"{v}"
    m = re.fullmatch(r"([\d.]+)px", raw)
    if m:
        v = "%gpx" % round(float(m.group(1)))
        group = {"border-top-left-radius": "radius", "height": "controlHeight", "padding-right": "spacing", "padding-left": "spacing",
                 "padding-top": "spacing", "font-size": "fontSize", "line-height": "lineHeight", "letter-spacing": "letterSpacing"}.get(prop)
        if v == "9999px" and prop == "border-top-left-radius":
            stats["token"] += 1
            return "`radius.full`"
        if (group, v) in DIDX:
            stats["token"] += 1
            return f"`{DIDX[(group, v)]}` {v}"
        if prop == "font-weight":
            stats["written"] -= 1
            return None
        return v
    stats["written"] -= 1
    return None


PROPS = [("background-color", "fill"), ("color", "text"), ("border-top-color", "edge"), ("border-top-left-radius", "radius"),
         ("height", "height"), ("padding-left", "padding"), ("font-size", "size"), ("line-height", "line")]


def first(t, part, state):
    for shot, d in CAP[t].items():
        if d["state"] == state and part in d["parts"] and not skip(shot, part, state):
            return shot, d["parts"][part]["style"]
    return None, None


def states_of(t, part):
    return sorted({d["state"] for d in CAP[t].values() if part in d["parts"]}, key=lambda s: STATE_ORDER.index(s) if s in STATE_ORDER else 99)


def crop_links(part, state):
    out = []
    for suffix, label in (("", "dark"), ("-light", "light")):
        name = f"{part}-{state}{suffix}.png"
        if name in CROPS:
            out.append(f"[{label}](components/crops/{name})")
    return " ".join(out)


lines = ["# Conductor desktop: components", "",
         "Generated by `tools/build_components_md.py` from `raw/components.<theme>.json` (computed styles read live from Conductor 0.91.2 through Safari's Web Inspector on 2026-10-25), "
         "`tokens.json` and `components/crops/`. Each entry lists the parts that show the component, the states captured in each theme with "
         "links to their crops, and the measured values written as the token that holds them, the painted value after it. Values are CSS px "
         "at App zoom 100%. States: hover, focus-visible and pressed are the stylesheet's own :hover, :focus-visible and :active rules copied onto the part (no pointer moved); "
         "focus is real focus given by script; typed is text set in the field and cleared after; error is the GitHub repository offer with a name that already exists.", ""]
lines.append("| Component | Parts | Captured |")
lines.append("|---|---|---|")
for name, parts, note in INVENTORY:
    present = [p for p in parts if states_of("dark", p) or states_of("light", p)]
    lines.append(f"| [{name}](#{name.lower().replace(' ', '-')}) | {len(present)} | {'yes' if present else 'not captured'} |")
lines.append("")
seen = set()
for name, parts, note in INVENTORY:
    lines += [f"## {name}", "", note, ""]
    rows = []
    for part in dict.fromkeys(parts):
        for state in sorted(set(states_of("dark", part)) | set(states_of("light", part)), key=lambda s: STATE_ORDER.index(s) if s in STATE_ORDER else 99):
            vals = []
            for t in ("dark", "light"):
                shot, s = first(t, part, state)
                if not s:
                    continue
                cells = [f"{label} {v}" for prop, label in PROPS if not (prop == "border-top-color" and s.get("border-top-width") == "0px") and (v := as_token(t, prop, s.get(prop, "")))] if (part, state, t) not in seen else []
                seen.add((part, state, t))
                vals.append(f"{t}: " + "; ".join(cells) if cells else f"{t}: see crop")
            rows.append(f"| `{part}` | {state} | {crop_links(part, state) or 'no crop'} | {'<br>'.join(vals)} |")
    if rows:
        lines += ["| Part | State | Crops | Values |", "|---|---|---|---|"] + rows + [""]
lines += ["## Gaps", ""] + [f"- {g}" for g in GAPS] + [""]
lines.insert(4, f"{stats['token']} of {stats['written']} values written below are tokens ({round(100 * stats['token'] / max(1, stats['written']))}%); the rest no token holds and are written raw.")
lines.insert(5, "")
(PKG / "components.md").write_text("\n".join(lines))
print("components.md", len(INVENTORY), "components", stats)
