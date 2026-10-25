#!/usr/bin/env python3
"""Read Raycast's declared design values out of the installed app bundle, without running it.

    python3 tools/capture/read_bundle.py [/Applications/Raycast.app]

Raycast 2.9 for macOS is an AppKit shell (`Contents/MacOS/Raycast`, linking AppKit, SwiftUI and
WebKit) whose windows are web views: `Contents/Resources/macos-app_RaycastDesktopApp.bundle/
Contents/Resources/frontend/` holds one HTML page per window (main, settings, AI chat, notes, ...)
and the Vite build they load: about 1,400 files, of which 160 are stylesheets. Nothing is
inspected live; this script only reads those files. It writes three readings to raw/:

  bundled-themes.json   The built-in themes Raycast ships, as the object literals in the
                        frontend chunk that defines them (`contrast-improvement-*.js`): id, name,
                        appearance and 12 colours each. Raycast Dark and Raycast Light are the two
                        the owner uses. Also the template that turns a theme into custom
                        properties on `.theme-root` (which theme key feeds which property).
  css-tokens.json       Every custom-property declaration in the token stylesheet (`css-*.css`,
                        the one that declares `--color-text-primary`), with its selector and any
                        enclosing @media, in source order; and every rule, in any stylesheet,
                        under `prefers-reduced-motion` (reducedMotion).
  text-styles.json      The named text styles the Text component offers (`text`, `small-text`, `heading1` ...:
                        font, size, weight), from the table in `text-*.js`, plus the letter spacing the
                        `text` CSS module sets for each size and weight.
  components-css.json   Every rule of the CSS modules named in MODULES (list item, menu, popover,
                        switch, checkbox, buttons, action bar, search input, badge, settings rows,
                        toast, dialog, grid ...), selector and declarations, from every stylesheet.

Each file records the bundle path, the app version and the source file names, so a later version
can be diffed. Standard library only. Deterministic for a given bundle.
"""
import json
import pathlib
import plistlib
import re
import sys

APP = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "/Applications/Raycast.app")
FRONT = APP / "Contents/Resources/macos-app_RaycastDesktopApp.bundle/Contents/Resources/frontend"
RAW = pathlib.Path(__file__).resolve().parents[2] / "raw"
VERSION = plistlib.loads((APP / "Contents/Info.plist").read_bytes())["CFBundleShortVersionString"]
REL = "Raycast.app/Contents/Resources/macos-app_RaycastDesktopApp.bundle/Contents/Resources/frontend/"

MODULES = [
    "standard-list-item", "list", "flat-list", "grid", "emoji-picker", "menu", "popover", "switch", "checkbox",
    "base-button", "button-primitive", "action-button", "action-bar-ui", "search-input", "base-badge",
    "settings-ui", "settings-sidebar-shell", "settings-sidebar-search", "settings-window-view", "sidebar-shell",
    "input-field-primitive", "dropdown-button", "shortcut", "toast", "action-bar-toast", "alert-primitive",
    "dialog-primitive", "typography", "button-radio-group-primitive", "token-primitive", "spinner",
    "navigation-bar-ui", "command-panel", "compact-command-item", "base-extension-command-item",
    "details", "data-list", "hud-primitive", "pro-gating-component", "activity-indicator", "scroll-area",
    "general-settings-view", "about-settings-view", "raycast-account-settings-view", "extension-commands", "text",
]


def parse_css(text):
    """Yield (media, selector, body) for every style rule, descending into @media/@supports/@layer."""
    out = []

    def block(s, i, media):
        while i < len(s):
            if s[i] == "}":
                return i + 1
            j = s.find("{", i)
            k = s.find("}", i)
            if j == -1 or (k != -1 and k < j):
                return k + 1 if k != -1 else len(s)
            head = s[i:j].strip()
            if head.startswith("@media") or head.startswith("@supports") or head.startswith("@layer") or head.startswith("@container"):
                i = block(s, j + 1, media + [head])
                continue
            depth, m = 1, j + 1
            while m < len(s) and depth:
                depth += {"{": 1, "}": -1}.get(s[m], 0)
                m += 1
            body = s[j + 1:m - 1]
            if not head.startswith("@") and "{" not in body:
                out.append((" ".join(media), head, body))
            elif not head.startswith("@") and "{" in body:          # CSS nesting: keep the outer declarations
                flat = re.sub(r"[^;{}]*\{[^{}]*\}", "", body)
                out.append((" ".join(media), head, flat))
            i = m
        return i

    block(text, 0, [])
    return out


def decls(body):
    """Split a declaration block on ';' outside parentheses."""
    parts, depth, cur = [], 0, ""
    for ch in body:
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
        if ch == ";" and depth == 0:
            parts.append(cur)
            cur = ""
        else:
            cur += ch
    parts.append(cur)
    res = []
    for p in parts:
        if ":" in p and p.strip():
            n, v = p.split(":", 1)
            res.append([n.strip(), v.strip()])
    return res


def token_sheet():
    hits = [p for p in sorted(FRONT.glob("css-*.css")) if "--color-text-primary:" in p.read_text()]
    if len(hits) != 1:
        raise SystemExit(f"expected one token stylesheet, found {[h.name for h in hits]}")
    return hits[0]


def themes():
    src = [p for p in sorted(FRONT.glob("contrast-improvement-*.js")) if "bundled-raycast-dark" in p.read_text()]
    if len(src) != 1:
        raise SystemExit("expected one chunk defining the bundled themes")
    js = src[0].read_text()
    consts = dict(re.findall(r"\b([A-Za-z_$][\w$]*)=`(#[0-9A-Fa-f]{6,8})`", js))
    found = []
    for m in re.finditer(r"\{id:`(bundled-[^`]+)`,(.*?)\}", js):
        obj = {"id": m.group(1)}
        for k, q, v in re.findall(r"(\w+):(`?)([^,`]*)`?", m.group(2)):
            obj[k] = (v if q else consts.get(v, {"!0": True, "!1": False}.get(v, v)))
        found.append(obj)
    tpl = re.search(r"--bg: \$\{e\.background\};.*?--magenta: \$\{e\.magenta\};", js, re.S)
    template = re.findall(r"(--[\w-]+): \$\{e\.(\w+)\}", tpl.group(0)) if tpl else []
    return src[0].name, found, template


def text_styles():
    src = [p for p in sorted(FRONT.glob("text-*.js")) if '"small-text":{font:' in p.read_text()]
    if len(src) != 1:
        raise SystemExit("expected one chunk defining the text styles")
    table = re.search(r"\{(heading1:\{.*?)\}\};function", src[0].read_text(), re.S).group(1)
    styles = {}
    for name, font, size, weight in re.findall(r'"?([\w-]+)"?:\{font:`(\w+)`,size:(\d+),weight:(\d+)\}', table):
        styles[name] = {"font": font, "size": int(size), "weight": int(weight)}
    spacing = []
    for css in sorted(FRONT.glob("text-*.css")):
        for media, sel, body in parse_css(css.read_text()):
            m = re.search(r"\.text__size-(\d+)_\w+\.text__weight-(\d+)_\w+", sel)
            if m and "font-inter" in sel:
                for n, v in decls(body):
                    if n == "letter-spacing":
                        spacing.append({"size": int(m.group(1)), "weight": int(m.group(2)), "letterSpacing": v})
    return src[0].name, styles, spacing


def main():
    RAW.mkdir(exist_ok=True)
    meta = {"app": "Raycast", "version": VERSION, "bundle": REL}
    name, found, template = themes()
    (RAW / "bundled-themes.json").write_text(json.dumps({
        **meta, "file": name,
        "note": "Object literals of the built-in themes, read from the shipped frontend chunk. The template maps a theme's keys to "
                "custom properties on .theme-root; accent is overridden by the macOS accent colour when Raycast sees one "
                "(--accent: var(--color-system-accent, var(--theme-accent))).",
        "template": [{"property": p, "key": k} for p, k in template],
        "themes": found}, indent=1) + "\n")
    tname, styles, spacing = text_styles()
    (RAW / "text-styles.json").write_text(json.dumps({**meta, "file": tname, "styles": styles, "letterSpacing": spacing}, indent=1) + "\n")
    sheet = token_sheet()
    toks = []
    for media, sel, body in parse_css(sheet.read_text()):
        for n, v in decls(body):
            if n.startswith("--"):
                toks.append({"media": media, "selector": sel, "name": n, "value": v})
    reduced = []
    for css in sorted(FRONT.glob("*.css")):
        for media, sel, body in parse_css(css.read_text()):
            if "prefers-reduced-motion" in media:
                reduced.append({"selector": re.sub(r"_[0-9a-f]{5}\b", "", sel), "decls": decls(body)})
    reduced = [json.loads(r) for r in sorted({json.dumps(r) for r in reduced})]
    (RAW / "css-tokens.json").write_text(json.dumps({**meta, "file": sheet.name, "declarations": toks,
                                                    "reducedMotion": reduced}, indent=1) + "\n")
    comp, seen = {}, set()
    for css in sorted(FRONT.glob("*.css")):
        for media, sel, body in parse_css(css.read_text()):
            for mod in MODULES:
                if re.search(r"(^|[^\w-])\." + re.escape(mod) + r"__", sel):
                    rule = {"media": media, "selector": re.sub(r"_[0-9a-f]{5}\b", "", sel), "decls": decls(body)}
                    key = json.dumps(rule)
                    if key not in seen:     # the same module is often bundled into several windows' sheets
                        seen.add(key)
                        comp.setdefault(mod, []).append({"file": re.sub(r"-[\w-]{8}\.css$", ".css", css.name), **rule})
                    break
    head = json.dumps({**meta, "note": "One rule per line. Selectors have their 5-character CSS-module hash removed; "
                                       "file is the stylesheet with its build hash removed; a rule bundled into several "
                                       "sheets is listed once."})[:-1]
    lines = [head + ', "modules": {']
    for i, k in enumerate(sorted(comp)):
        body = ",\n".join("  " + json.dumps(r) for r in comp[k])
        lines.append(f' "{k}": [\n{body}\n ]' + ("," if i < len(comp) - 1 else ""))
    lines.append("}}")
    text = "\n".join(lines) + "\n"
    json.loads(text)
    (RAW / "components-css.json").write_text(text)
    print(f"{len(found)} themes, {len(styles)} text styles, {len(toks)} token declarations, {sum(len(v) for v in comp.values())} component rules "
          f"in {len(comp)} modules (Raycast {VERSION})")


if __name__ == "__main__":
    main()
