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


def alias_errors(core, light):
    """Each set resolves against core and itself only (the $themes pair core with the light set),
    so a light alias that nothing holds points at nothing."""
    core_names = {n for n, _ in tokens_of(core)}
    sets = {"core": (core, core_names),
            "light": (light, core_names | {n for n, _ in tokens_of(light)})}
    return [f"{s}.{n}: alias {{{a}}} points at nothing in core or {s}"
            for s, (tree, names) in sets.items() for n, tok in tokens_of(tree)
            for a in aliases(tok["$value"]) if a not in names]
