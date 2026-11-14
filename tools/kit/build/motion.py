"""Turn raw/motion.json (tools/capture/motion-probe.mjs) into the `core.motion` token group.

Product-free: build_tokens.py imports this and adds the result to its `core` set, so every package
that runs the probe gets the same shape. See docs/decisions/0001-motion-tokens.md.

    motion
      duration      one `<n>ms` token per duration read (a motion custom property, when the product
                    names one, names it instead), $type duration
      easing        one token per easing read, as cubicBezier control points; a keyword is expanded
                    (Derived); steps() and linear() cannot be cubicBezier and go to notTokenised
      transition    one token per (property, duration, easing, delay) seen on a real element, $type
                    transition (DTCG composite), with the elements it covers and what reduced motion did
      animation     one token per animation name: its dominant timing, the properties its @keyframes
                    set, and what reduced motion did; $type animation (not a DTCG type: DTCG has none)
      $extensions   reducedMotion (the probe's verdict and the product's own rules), propertyUsage
                    (which properties transition, by element count), keyframes declared but unused

Every token carries `$extensions.source = {evidence, capture}` with the labels of docs/EVIDENCE.md:
Measured for a value read from a computed style, a rule or a custom property, Derived for a keyword
expanded to control points. Deterministic: same input, same bytes.
"""
import re

CAPTURE = "raw/motion.json"
NEGLIGIBLE_MS = 1
MAX_TRANSITIONS = 60

KEYWORDS = {"linear": [0, 0, 1, 1], "ease": [0.25, 0.1, 0.25, 1], "ease-in": [0.42, 0, 1, 1],
            "ease-out": [0, 0, 0.58, 1], "ease-in-out": [0.42, 0, 0.58, 1]}
_NUM = r"[-+]?(?:\d+\.?\d*|\.\d+)(?:e[-+]?\d+)?"


def parse_time(s):
    """'0.2s' -> 200.0, '150ms' -> 150.0; None for anything else (var(), calc(), a bad value)."""
    m = re.fullmatch(r"(%s)(ms|s)" % _NUM, str(s or "").strip().lower())
    if not m:
        return None
    return round(float(m.group(1)) * (1000 if m.group(2) == "s" else 1), 3)


def ms_str(n):
    """200.0 -> '200ms', 0.5 -> '0.5ms'."""
    return "%gms" % round(float(n), 3)


def ms_key(n):
    """A token name for a duration: no '.', which separates the parts of an alias."""
    return ms_str(n).replace(".", "_")


def _num(x):
    return "%g" % round(float(x), 4)


def norm_easing(s):
    """The same spelling motion.mjs's normEasing gives, so a custom property's value (read raw in the
    page) and a computed one compare equal."""
    t = re.sub(r"\s+", " ", str(s or "").strip().lower())
    if not t:
        return ""
    if t in KEYWORDS:
        return t
    if t == "step-start":
        return "steps(1, start)"
    if t == "step-end":
        return "steps(1, end)"
    m = re.fullmatch(r"cubic-bezier\(\s*([^)]*)\)", t)
    if m:
        p = [x.strip() for x in m.group(1).split(",")]
        if len(p) == 4 and all(re.fullmatch(_NUM, x) for x in p):
            return "cubic-bezier(%s)" % ", ".join(_num(x) for x in p)
        return re.sub(r"\s*,\s*", ", ", t)
    m = re.fullmatch(r"steps\(\s*(\d+)\s*(?:,\s*([a-z-]+)\s*)?\)", t)
    if m:
        jump = {"jump-end": "end", "jump-start": "start"}.get(m.group(2), m.group(2) or "end")
        return "steps(%s, %s)" % (m.group(1), jump)
    return re.sub(r"\s*,\s*", ", ", t)


def easing_bezier(s):
    """Control points of a keyword or cubic-bezier() easing, else None (steps, linear())."""
    t = norm_easing(s)
    if t in KEYWORDS:
        return list(KEYWORDS[t])
    m = re.fullmatch(r"cubic-bezier\(([^)]*)\)", t)
    if not m:
        return None
    try:
        p = [float(x) for x in m.group(1).split(",")]
    except ValueError:
        return None
    return [int(x) if x == int(x) else x for x in p] if len(p) == 4 else None


def easing_key(s):
    """A token name for an easing: the keyword, or bezier-<points> with '.' written '_'."""
    t = norm_easing(s)
    if t in KEYWORDS:
        return t
    b = easing_bezier(t)
    if b:
        return "bezier-" + "-".join(_num(x).replace(".", "_").replace("-", "m") for x in b)
    return None


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", str(s).lower()).strip("-") or "x"


def classify_value(v):
    t = str(v or "").strip()
    if parse_time(t) is not None:
        return "duration"
    e = norm_easing(t)
    if e in KEYWORDS or re.match(r"(cubic-bezier|steps|linear)\(", e):
        return "easing"
    return "other"


def _src(evidence, detail=None):
    s = {"evidence": evidence, "capture": CAPTURE + ("#" + detail if detail else "")}
    return s


def _tok(value, ty, evidence, detail=None, description=None, **ext):
    t = {"$value": value, "$type": ty}
    if description:
        t["$description"] = description
    t["$extensions"] = {"source": _src(evidence, detail), **ext}
    return t


def _plural(n, word):
    return "%d %s%s" % (n, word, "" if n == 1 else "s")


def tally(raw):
    """Counts over every page's groups: what moved, how long, how, and what reduce did to it."""
    t = {"duration": {}, "easing": {}, "transition": {}, "animation": {}, "props": {}, "outcomes": {}, "declared_duration": {},
         "declared_easing": {}, "keyframes": {}, "used_names": set(), "rules": [], "scroll": 0}
    bump = lambda d, k, n=1: d.__setitem__(k, d.get(k, 0) + n)
    for page in raw.get("pages", {}).values():
        for g in page.get("groups", []):
            c = g["count"]
            outcome = {(i["kind"], i["key"]): i["outcome"] for i in g.get("items", [])}
            for tr in g["base"]["transitions"]:
                if "durationRaw" in tr:
                    continue
                key = (tr["property"], tr["durationMs"], tr["delayMs"], tr["easing"])
                bump(t["transition"], key, c)
                bump(t["duration"], tr["durationMs"], c)
                bump(t["easing"], tr["easing"], c)
                bump(t["props"], tr["property"], c)
                o = t["outcomes"].setdefault(("transition", key), {})
                bump(o, outcome.get(("transition", tr["property"]), "kept"), c)
            for an in g["base"]["animations"]:
                if "durationRaw" in an:
                    continue
                key = (an["name"], an["durationMs"], an["delayMs"], an["easing"], an["iterationCount"], an["direction"], an["fillMode"])
                bump(t["animation"], key, c)
                bump(t["duration"], an["durationMs"], c)
                bump(t["easing"], an["easing"], c)
                t["used_names"].add(an["name"])
                o = t["outcomes"].setdefault(("animation", an["name"]), {})
                bump(o, outcome.get(("animation", an["name"]), "kept"), c)
            if g["base"].get("scrollBehavior"):
                t["scroll"] += c
        for k in page.get("keyframes", []):
            t["keyframes"].setdefault(k["name"], k)
        for d in page.get("declared", []):
            if any("prefers-reduced-motion" in c for c in d.get("context", [])):
                continue          # the product's own reduce values are not its motion
            for tr in d.get("transitions", []):
                if "durationRaw" not in tr:
                    bump(t["declared_duration"], tr["durationMs"])
                    bump(t["declared_easing"], tr["easing"])
            for an in d.get("animations", []):
                if "durationRaw" not in an:
                    bump(t["declared_duration"], an["durationMs"])
                    bump(t["declared_easing"], an["easing"])
        for r in page.get("reducedMotionRules", []):
            if r not in t["rules"]:
                t["rules"].append(r)
    return t


def build(raw):
    """(motion group, notTokenised entries) for build_tokens.py to put at core["motion"]."""
    t = tally(raw)
    not_tokenised = []

    # ---- named values: motion custom properties the product declares
    var_tokens = {"duration": {}, "easing": {}}
    seen_vars = {}
    for page in raw.get("pages", {}).values():
        for v in page.get("customProperties", []):
            seen_vars.setdefault(v["name"], v)
    for name, v in sorted(seen_vars.items()):
        value = v.get("resolved") or v.get("declared") or ""
        kind = classify_value(value)
        key = slug(name.lstrip("-"))
        if kind == "duration":
            ms = parse_time(value)
            if key not in var_tokens["duration"]:
                var_tokens["duration"][key] = (ms, name, v)
        elif kind == "easing":
            e = norm_easing(value)
            if key not in var_tokens["easing"]:
                var_tokens["easing"][key] = (e, name, v)

    # ---- duration
    rows, dkey = [], {}
    for key, (ms, name, v) in var_tokens["duration"].items():
        rows.append((ms, key, _tok(ms_str(ms), "duration", "Measured", "customProperties/" + name,
                                   "Custom property %s, declared on %s." % (name, v.get("selector", ":root")), uses=t["duration"].get(ms, 0))))
        dkey.setdefault(ms, key)
    for ms in sorted(set(t["duration"]) | set(t["declared_duration"])):
        if ms in dkey:
            continue
        uses = t["duration"].get(ms, 0)
        seen = ("Read at rest on %s." % _plural(uses, "element")) if uses else "Declared in a state rule, not seen running at rest."
        rows.append((ms, ms_key(ms), _tok(ms_str(ms), "duration", "Measured", "pages" if uses else "declared", seen, uses=uses)))
        dkey[ms] = ms_key(ms)
    duration = {key: tok for _, key, tok in sorted(rows, key=lambda r: (r[0], r[1]))}

    # ---- easing
    easing, ekey = {}, {}
    for key, (e, name, v) in var_tokens["easing"].items():
        b = easing_bezier(e)
        if b:
            easing[key] = _tok(b, "cubicBezier", "Measured", "customProperties/" + name, "Custom property %s, declared on %s." % (name, v.get("selector", ":root")))
            ekey.setdefault(e, key)
        else:
            not_tokenised.append({"name": name, "value": e, "why": "an easing DTCG's cubicBezier cannot carry (steps() or a linear() curve)"})
    for e in sorted(set(t["easing"]) | set(t["declared_easing"])):
        if e in ekey or not e:
            continue
        b = easing_bezier(e)
        uses = t["easing"].get(e, 0)
        if b is None:
            not_tokenised.append({"name": "motion easing " + e, "value": e, "why": "an easing DTCG's cubicBezier cannot carry (steps() or a linear() curve)", "uses": uses})
            continue
        derived = e in KEYWORDS
        easing[easing_key(e)] = _tok(b, "cubicBezier", "Derived" if derived else "Measured", "pages" if uses else "declared",
                                     ("The keyword `%s`, expanded to its control points." % e) if derived else None, uses=uses)
        ekey[e] = easing_key(e)
    easing = dict(sorted(easing.items()))

    # ---- transition
    tkeys = sorted(t["transition"], key=lambda k: (-t["transition"][k], k))
    transition, used_keys = {}, set()
    for k in tkeys[:MAX_TRANSITIONS]:
        prop, ms, delay, e = k
        name = "-".join(x for x in (slug(prop), ms_key(ms), ekey.get(e) or slug(e)) + (("delay" + ms_key(delay),) if delay else ()) if x)
        while name in used_keys:
            name += "-x"
        used_keys.add(name)
        value = {"duration": "{motion.duration.%s}" % dkey[ms], "delay": ms_str(delay),
                 "timingFunction": ("{motion.easing.%s}" % ekey[e]) if e in ekey else e}
        transition[name] = _tok(value, "transition", "Measured", "pages", "Read at rest on %s." % _plural(t["transition"][k], "element"),
                                property=prop, elements=t["transition"][k], reducedMotion=dict(sorted(t["outcomes"].get(("transition", k), {}).items())))
    if len(tkeys) > MAX_TRANSITIONS:
        not_tokenised.append({"name": "motion.transition", "value": "%d more" % (len(tkeys) - MAX_TRANSITIONS),
                              "why": "the %d most-used transitions are tokens; the rest are in raw/motion.json" % MAX_TRANSITIONS})

    # ---- animation: the dominant timing per name
    by_name = {}
    for k, c in t["animation"].items():
        by_name.setdefault(k[0], []).append((c, k))
    animation = {}
    for name, rows in sorted(by_name.items()):
        c, k = sorted(rows, key=lambda r: (-r[0], r[1]))[0]
        _, ms, delay, e, iters, direction, fill = k
        kf = t["keyframes"].get(name)
        ext = {"elements": sum(r[0] for r in rows)}
        if kf:
            ext["keyframes"] = {"properties": kf["properties"], "steps": [s["offset"] for s in kf["steps"]]}
        ext["reducedMotion"] = dict(sorted(t["outcomes"].get(("animation", name), {}).items()))
        value = {"name": name, "duration": "{motion.duration.%s}" % dkey[ms], "delay": ms_str(delay),
                 "timingFunction": ("{motion.easing.%s}" % ekey[e]) if e in ekey else e,
                 "iterationCount": iters, "direction": direction, "fillMode": fill}
        animation[slug(name)] = _tok(value, "animation", "Measured", "pages", "Animation `%s`." % name, **ext)
    unused = sorted(n for n in t["keyframes"] if n not in t["used_names"])

    group = {"$description": ("Motion as measured: the durations and easing curves the product's elements run, which properties transition, "
                              "its animations and @keyframes, and what prefers-reduced-motion: reduce changes. Read by tools/capture/motion-probe.mjs.")}
    for k, v in (("duration", duration), ("easing", easing), ("transition", transition), ("animation", animation)):
        if v:
            group[k] = v
    pages = raw.get("pages", {})
    group["$extensions"] = {
        "reducedMotion": {
            "probe": raw.get("_meta", {}).get("probe", "page.emulateMedia({ reducedMotion })"),
            "verified": bool(pages) and all(p["matchMedia"]["reduce"] and not p["matchMedia"]["normal"] for p in pages.values()),
            "pages": len(pages),
            **{k: raw["summary"][k] for k in ("behaviour", "moving", "removed", "reduced", "kept", "partial", "added", "loops")},
            "authoredRules": t["rules"][:20],
        },
        "propertyUsage": dict(sorted(t["props"].items(), key=lambda kv: (-kv[1], kv[0]))),
        "smoothScrollElements": t["scroll"],
        "unusedKeyframes": unused,
    }
    return group, not_tokenised
