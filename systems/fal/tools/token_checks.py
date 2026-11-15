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


def alias_errors(core, light, dark):
    """Each set resolves against core and itself only (the $themes pair core with one of light or
    dark), so a light alias that only dark holds points at nothing in the light theme."""
    core_names = {n for n, _ in tokens_of(core)}
    sets = {"core": (core, core_names), "light": (light, core_names | {n for n, _ in tokens_of(light)}),
            "dark": (dark, core_names | {n for n, _ in tokens_of(dark)})}
    return [f"{s}.{n}: alias {{{a}}} points at nothing in core or {s}"
            for s, (tree, names) in sets.items() for n, tok in tokens_of(tree)
            for a in aliases(tok["$value"]) if a not in names]


def parity_gap(light, dark):
    """The roles only light names and the ones only dark names."""
    lt, dk = {n for n, _ in tokens_of(light)}, {n for n, _ in tokens_of(dark)}
    return sorted(lt - dk), sorted(dk - lt)


if __name__ == "__main__":
    # Structural checks on the finished tokens.json: every {alias} must resolve
    # inside its own set plus core (the $themes pairing), and the light/dark
    # role gap is reported. Exits 1 while any alias points at nothing.
    import json, pathlib, sys

    T = json.loads((pathlib.Path(__file__).resolve().parent.parent / "tokens.json").read_text())
    core, light, dark = (T.get(s, {}) for s in ("core", "light", "dark"))
    errors = alias_errors(core, light, dark)
    for e in errors:
        print("alias error:", e)
    only_light, only_dark = parity_gap(light, dark)
    print(f"{sum(1 for _ in tokens_of(core))} core / "
          f"{sum(1 for _ in tokens_of(light))} light / "
          f"{sum(1 for _ in tokens_of(dark))} dark tokens; "
          f"{len(errors)} alias errors")
    if only_light:
        print("roles only light names:", ", ".join(only_light))
    if only_dark:
        print("roles only dark names:", ", ".join(only_dark))
    sys.exit(1 if errors else 0)
