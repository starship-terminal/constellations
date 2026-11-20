"""Every package's component-tokens.json, the tree its build_tokens.py turns into tokens.json, checked
the same way across all of systems/: each {alias} resolves to a token, no alias chain loops, and each
package file a `source` names exists. Package tests check their own tokens.json; nothing else read the
builder input across packages. Run with `make test`; needs only python3."""
import json
import re
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SYSTEMS = ROOT / "systems"

# Packages that fail on main for a real defect: slug -> the exact problems it has. The listed package
# is still checked, its problems must equal the list (a new defect fails, and so does a fix, so the
# entry is removed with it). A new package is never listed: fix it instead.
EXPECTED_FAILURES = {
    # light and dark component.code-block-surface alias tokens that do not exist (the light one lives
    # at surface.elevated-secondary), so tokens.json carries no code-block-surface at all.
    "chatgpt": [
        "dark.component.code-block-surface: {surface.composer-surface-primary} names no token",
        "light.component.code-block-surface: {bg.elevated-secondary} names no token",
    ],
}

ALIAS = re.compile(r"\{([^{}]+)\}")
# A file named in a source string: a path under one of the package's own folders, or a bare
# .json/.md name that sits at the package root, in raw/ or in tools/. Other names (the product's own
# stylesheets, app.4ef09b07.css) are the product's files, not the package's, and are not checked.
FILE_REF = re.compile(r"(?<![\w/.-])((?:[\w.-]+/)*[\w.-]+\.(?:json|jsonl|md|png|html|css|txt|svg|js|mjs|py))")
PACKAGE_DIRS = ("raw/", "screenshots/", "components/", "boards/", "tools/")
MAX_DEPTH = 32


def component_token_files():
    """Every component-tokens.json under systems/, at a package's top level or in its raw/."""
    return sorted(set(SYSTEMS.glob("*/component-tokens.json")) | set(SYSTEMS.glob("*/raw/component-tokens.json")))


def leaves(tree):
    """{dotted path: leaf} for every token in a tree. A leaf carries "$value", "var", or "value" (a
    plain value, or a composite one beside its "type"); "$" keys are metadata, never tokens."""
    out = {}

    def walk(node, path):
        if not isinstance(node, dict):
            return
        if "$value" in node or "var" in node or ("value" in node and (not isinstance(node["value"], dict) or "type" in node)):
            out[".".join(path)] = node
            return
        for key, child in node.items():
            if not key.startswith("$"):
                walk(child, path + [key])

    walk(tree, [])
    return out


def strings(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, list):
        for v in value:
            yield from strings(v)
    elif isinstance(value, dict):
        for v in value.values():
            yield from strings(v)


def refs(leaf):
    """The alias targets in a leaf's value, in order."""
    return [m.group(1) for s in strings(leaf.get("$value", leaf.get("value"))) for m in ALIAS.finditer(s)]


def sources(tree):
    """Every `source` string in a tree, at a leaf or inside its $extensions."""
    out = []

    def walk(node):
        if isinstance(node, dict):
            for k, v in node.items():
                if k == "source" and isinstance(v, str):
                    out.append(v)
                elif k == "$extensions" and isinstance(v, dict) and isinstance(v.get("source"), str):
                    out.append(v["source"])
                else:
                    walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)

    walk(tree)
    return out


def component_token_problems(pkg):
    """One line per defect in the package's component-tokens.json; [] when it is sound."""
    pkg = Path(pkg)
    src = pkg / "component-tokens.json" if (pkg / "component-tokens.json").is_file() else pkg / "raw/component-tokens.json"
    try:
        tree = json.loads(src.read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        return [f"{src.name} cannot be read: {e}"]
    comp = leaves(tree)
    built, themes = {}, []
    if (pkg / "tokens.json").is_file():
        try:
            built_tree = json.loads((pkg / "tokens.json").read_text(encoding="utf-8"))
        except ValueError as e:
            return [f"tokens.json is not valid JSON: {e}"]
        built = leaves(built_tree)
        themes = [t.get("selectedTokenSets") or {} for t in built_tree.get("$themes") or [] if isinstance(t, dict)]
    # An alias may name a token the builder makes from another reading, so tokens.json counts too;
    # the input's own leaf wins where both hold a path.
    known = {**built, **comp}
    sets = sorted({p.split(".")[0] for p in known})
    # A theme set (light, dark, or any set a tokens.json theme enables) is active only with the sets
    # its own themes select; every other set is shared and active in every theme.
    theme_sets = {s for t in themes for s, state in t.items() if state == "enabled"} | {"light", "dark"}
    shared = [s for s in sets if s not in theme_sets]
    with_set = {s: sorted({o for t in themes if t.get(s) in ("enabled", "source") for o in t} - {s}) for s in theme_sets}

    def target(ref, set_name):
        """The path an alias resolves to, or None: its own set, then core, then the root, then the
        sets active beside it. A theme set's token sees only the sets its themes select and the shared
        sets, so light.a -> {b} never resolves to a dark-only b; a shared set's token (a component set
        every theme reads) may name each theme's role."""
        if set_name in theme_sets:
            others = with_set.get(set_name, []) + shared
        else:
            others = sets
        for cand in [f"{set_name}.{ref}", f"core.{ref}", ref] + [f"{s}.{ref}" for s in others]:
            if cand in known:
                return cand
        return None

    problems = []
    for path, leaf in comp.items():
        for ref in refs(leaf):
            if target(ref, path.split(".")[0]) is None:
                problems.append(f"{path}: {{{ref}}} names no token")

    def edges(path):
        return [t for t in (target(r, path.split(".")[0]) for r in refs(known[path])) if t]

    # Depth-first over every chain an input token starts, built tokens included, with the nodes on
    # the current chain tracked: reaching one of them again is a loop, wherever in the chain it is.
    done = set()
    for start in comp:
        if start in done:
            continue
        stack, on_chain = [(start, iter(edges(start)))], [start]
        while stack:
            path, it = stack[-1]
            nxt = next(it, None)
            if nxt is None:
                stack.pop()
                on_chain.pop()
                done.add(path)
            elif nxt in on_chain:
                loop = on_chain[on_chain.index(nxt):] + [nxt]
                problems.append("alias loop: " + " -> ".join(loop))
            elif nxt not in done:
                if len(on_chain) > MAX_DEPTH:
                    problems.append(f"{start}: alias chain deeper than {MAX_DEPTH}")
                    continue
                stack.append((nxt, iter(edges(nxt))))
                on_chain.append(nxt)

    for s in sources(tree):
        for m in FILE_REF.finditer(s):
            ref = m.group(1)
            if ref.startswith(PACKAGE_DIRS):
                ok = (pkg / ref).exists()
            elif "/" not in ref and ref.endswith((".json", ".md")):
                ok = any((pkg / d / ref).exists() for d in ("", "raw", "tools"))
            else:
                continue
            if not ok:
                problems.append(f"source names {ref}, which is not in the package")
    return sorted(set(problems))


class EveryPackage(unittest.TestCase):
    def test_component_tokens_resolve_and_cite_files_that_exist(self):
        files = component_token_files()
        self.assertTrue(files, "no component-tokens.json found under systems/")
        for f in files:
            pkg = f.parent.parent if f.parent.name == "raw" else f.parent
            with self.subTest(package=pkg.name):
                self.assertEqual(component_token_problems(pkg), EXPECTED_FAILURES.get(pkg.name, []),
                                 "a listed package that changed: update or remove its EXPECTED_FAILURES entry")

    def test_expected_failures_name_packages_that_exist(self):
        for slug in EXPECTED_FAILURES:
            self.assertTrue(any(f.parent.parent.name == slug or f.parent.name == slug
                                for f in component_token_files()), slug)


class Checker(unittest.TestCase):
    """The checks on an invented package, so a check that stops finding anything fails here."""

    def problems(self, tree, tokens=None, files=()):
        with tempfile.TemporaryDirectory() as d:
            pkg = Path(d) / "demo"
            (pkg / "raw").mkdir(parents=True)
            (pkg / "raw/component-tokens.json").write_text(json.dumps(tree))
            if tokens is not None:
                (pkg / "tokens.json").write_text(json.dumps(tokens))
            for rel in files:
                (pkg / rel).parent.mkdir(parents=True, exist_ok=True)
                (pkg / rel).write_text("{}")
            return component_token_problems(pkg)

    def test_a_sound_tree_passes(self):
        tree = {"_about": "notes",
                "core": {"palette": {"ink": {"var": "--ink", "type": "color", "source": "raw/css-vars.json"}}},
                "light": {"text": {"DEFAULT": {"value": "{palette.ink}", "type": "color"},
                                   "muted": {"value": "#777777", "type": "color",
                                             "source": "raw/components-computed.json#body, app.4ef09b07.css"}},
                          "type": {"body": {"value": {"fontFamily": "{font.sans}"}, "type": "typography"}}},
                "component": {"button": {"ink": {"value": "{text.DEFAULT}", "type": "color",
                                                 "source": "measurements.md#button"}}}}
        tokens = {"core": {"font": {"sans": {"$value": "Inter", "$type": "fontFamily"}}}}
        self.assertEqual(self.problems(tree, tokens, files=("raw/css-vars.json", "raw/components-computed.json",
                                                            "raw/measurements.md")), [])

    def test_an_alias_to_no_token_is_named(self):
        tree = {"light": {"text": {"value": "{palette.gone}", "type": "color"}}}
        self.assertEqual(self.problems(tree), ["light.text: {palette.gone} names no token"])

    def test_a_theme_token_never_resolves_in_another_theme(self):
        tree = {"light": {"a": {"value": "{b}", "type": "color"}},
                "dark": {"b": {"value": "#000000", "type": "color"}}}
        self.assertEqual(self.problems(tree), ["light.a: {b} names no token"])
        tokens = {"$themes": [{"name": "light", "selectedTokenSets": {"core": "source", "light": "enabled"}},
                              {"name": "dark", "selectedTokenSets": {"core": "source", "dark": "enabled"}}],
                  "dark": {"b": {"$value": "#000000", "$type": "color"}}}
        self.assertEqual(self.problems({"light": tree["light"]}, tokens), ["light.a: {b} names no token"])

    def test_a_theme_token_resolves_in_a_set_its_theme_enables_or_a_shared_set(self):
        tokens = {"$themes": [{"name": "docs", "selectedTokenSets": {"core": "source", "light": "enabled",
                                                                     "docs": "enabled"}}],
                  "docs": {"b": {"$value": "#000000", "$type": "color"}}}
        self.assertEqual(self.problems({"light": {"a": {"value": "{b}", "type": "color"}}}, tokens), [])
        tree = {"light": {"a": {"value": "{b}", "type": "color"}},
                "_surface": {"b": {"value": "#000000", "type": "color"}},
                "component": {"c": {"value": "{a}", "type": "color"}}}
        self.assertEqual(self.problems(tree), [])

    def test_an_alias_inside_a_composite_value_is_checked(self):
        tree = {"core": {"type": {"body": {"value": {"fontFamily": "{font.gone}"}, "type": "typography"}}}}
        self.assertEqual(self.problems(tree), ["core.type.body: {font.gone} names no token"])

    def test_an_alias_loop_is_named(self):
        tree = {"light": {"a": {"value": "{b}", "type": "color"}, "b": {"value": "{c}", "type": "color"},
                          "c": {"value": "{a}", "type": "color"}}}
        self.assertEqual(self.problems(tree), ["alias loop: light.a -> light.b -> light.c -> light.a"])

    def test_a_loop_among_built_tokens_is_named(self):
        tree = {"light": {"a": {"value": "{b}", "type": "color"}}}
        tokens = {"light": {"b": {"$value": "{c}", "$type": "color"}, "c": {"$value": "{b}", "$type": "color"}}}
        self.assertEqual(self.problems(tree, tokens), ["alias loop: light.b -> light.c -> light.b"])

    def test_a_missing_package_file_is_named_and_product_files_are_not(self):
        tree = {"core": {"x": {"value": "1px", "type": "dimension",
                               "source": "raw/gone.json#a; layout.json; main.css; screenshots/home.png"}}}
        self.assertEqual(self.problems(tree, files=("screenshots/home.png",)), [
            "source names layout.json, which is not in the package",
            "source names raw/gone.json, which is not in the package",
        ])

    def test_a_dtcg_extensions_source_is_read(self):
        tree = {"core": {"x": {"$value": "1px", "$type": "dimension", "$extensions": {"source": "raw/gone.json"}}}}
        self.assertEqual(self.problems(tree), ["source names raw/gone.json, which is not in the package"])


if __name__ == "__main__":
    unittest.main()
