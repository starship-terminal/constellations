#!/usr/bin/env python3
"""Pull the rules the 2026-10 refresh cites out of Duolingo's stylesheets.

Usage: python3 tools/capture/css_evidence.py <dir of downloaded .css chunks> > raw/2026-10/css-evidence.json
The chunks are the public CloudFront files the signed-in /learn page loaded on 2026-10-17
(listed in raw/2026-10/rootvars-live.json). They are Duolingo's property and stay outside
the repo; this file keeps only the selectors and declarations it quotes.
"""
import collections, json, pathlib, re, sys

src = pathlib.Path(sys.argv[1])
rules = []  # (file, condition, selector, body)
for f in sorted(src.glob("*.css")):
    s = f.read_text(errors="ignore")
    # one level of @media / @supports nesting is enough for these files
    for m in re.finditer(r"@(media|supports)([^{]+)\{((?:[^{}]*\{[^}]*\})*)\s*\}", s):
        for r in re.finditer(r"([^{}]+)\{([^}]*)\}", m.group(3)):
            rules.append((f.name, "@" + m.group(1) + m.group(2).strip(), r.group(1).strip(), r.group(2)))
    flat = re.sub(r"@(media|supports)[^{]+\{((?:[^{}]*\{[^}]*\})*)\s*\}", "", s)
    for r in re.finditer(r"([^{}@]+)\{([^}]*)\}", flat):
        rules.append((f.name, "", r.group(1).strip(), r.group(2)))

def pick(pred, limit=60):
    out = [{"file": f, "cond": c, "selector": sel[:200], "css": body[:300]} for f, c, sel, body in rules if pred(f, c, sel, body)]
    return {"count": len(out), "rules": out[:limit]}

border_use = collections.Counter()
for f, c, sel, body in rules:
    for m in re.finditer(r"border(?:-(?:top|right|bottom|left))?(?:-color)?:[^;]*?rgb\(var\(--color-([a-z0-9-]+)\)", body):
        border_use[m.group(1)] += 1

out = {
    "_meta": {"source": "tools/capture/css_evidence.py over %d stylesheet chunks loaded by the signed-in app on 2026-10-17" % len(list(src.glob('*.css'))), "rules_parsed": len(rules)},
    "reduced_motion_attribute": pick(lambda f, c, sel, b: "html[reduced-motion]" in sel),
    "prefers_reduced_motion_media": pick(lambda f, c, sel, b: "prefers-reduced-motion" in c),
    "focus_visible": pick(lambda f, c, sel, b: ":focus-visible" in sel),
    "focus_and_focus_within": pick(lambda f, c, sel, b: re.search(r":focus(?!-visible)", sel) is not None),
    "outline_declarations": pick(lambda f, c, sel, b: re.search(r"(^|;)outline(-[a-z]+)?:", b) is not None),
    "active_on_buttons": pick(lambda f, c, sel, b: ":active" in sel and re.search(r"\._1VYyp|\._2V6ug|\._7jW2t", sel) is not None, 20),
    "hover_filters": pick(lambda f, c, sel, b: "filter-hover" in b and "brightness" in b, 20),
    "border_colour_use": dict(border_use.most_common()),
    # every border drawn in a neutral darker than swan (hare, wolf, eel): the candidates for a strong
    # border. A border with no colour of its own takes currentColor, so a rule that sets a border
    # style or width and color: hare counts too.
    "dark_neutral_borders": pick(lambda f, c, sel, b: re.search(r"border(?:-(?:top|right|bottom|left))?(?:-color)?:[^;]*?rgb\(var\(--color-(?:hare|wolf|eel)\)", b) is not None
                                 or (not re.search(r"(?:^|;)border(?:-(?:top|right|bottom|left))?(?:-color)?:[^;]*(?:rgb|transparent|currentcolor|\b0\b|none)", b, re.I)
                                     and re.search(r"(?:^|;)border(?:-style|-width)?:", b) is not None
                                     and re.search(r"(?:^|;)color:rgb\(var\(--color-(?:hare|wolf|eel)\)\)", b) is not None), 20),
}
json.dump(out, sys.stdout, indent=1)
