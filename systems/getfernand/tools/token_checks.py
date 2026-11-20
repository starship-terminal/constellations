"""Checks build_tokens.py runs on the finished sets, kept apart so tests can run them on small trees."""
import re


def tokens_of(tree, prefix=""):
    """Every (dotted name, token) in a set."""
    for k, v in tree.items():
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from tokens_of(v, prefix + k + ".")


def aliases(v):
    """The {path} references anywhere in a $value."""
    if isinstance(v, str):
        return re.findall(r"\{([^{}]+)\}", v)
    if isinstance(v, dict):
        return [a for x in v.values() for a in aliases(x)]
    if isinstance(v, list):
        return [a for x in v for a in aliases(x)]
    return []


def alias_errors(core, **sets):
    """Each surface set resolves against core and itself only (the $themes
    pair core with one surface set), so a light alias that only dark holds
    points at nothing in the light theme."""
    core_names = {n for n, _ in tokens_of(core)}
    checks = {"core": (core, core_names)}
    checks.update({s: (t, core_names | {n for n, _ in tokens_of(t)}) for s, t in sets.items()})
    return [f"{s}.{n}: alias {{{a}}} points at nothing in core or {s}"
            for s, (tree, names) in checks.items() for n, tok in tokens_of(tree)
            for a in aliases(tok["$value"]) if a not in names]


def parity_gap(a, b):
    """The roles only the first set names and the ones only the second names."""
    an, bn = {n for n, _ in tokens_of(a)}, {n for n, _ in tokens_of(b)}
    return sorted(an - bn), sorted(bn - an)
