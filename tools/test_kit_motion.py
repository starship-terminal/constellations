"""Tests for the kit's motion readings: tools/kit/capture/motion.mjs and motion-probe.mjs (through
test_motion.mjs, under node) and tools/kit/build/motion.py, which turns raw/motion.json into the `core.motion`
token group (docs/decisions/0001-motion-tokens.md). Run with `make test`."""
import ast
import json
import re
import shutil
import subprocess
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
KIT = HERE / "kit"
sys.path.insert(0, str(KIT / "build"))
sys.path.insert(0, str(HERE))
import motion  # noqa: E402
import catalog  # noqa: E402

NODE = shutil.which("node")

EASINGS = ["ease", " EASE-OUT ", "cubic-bezier(0.40, 0, .2, 1.0)", "cubic-bezier(0.4,0,0.2,1)", "cubic-bezier(0.1234567, 0, 0, 1)",
           "steps(4)", "steps(4, jump-start)", "step-end", "step-start", "linear(0,  0.25 20%,1)", "", "nonsense  value"]
TIMES = ["0.2s", "150ms", ".5S", "0s", "0.01ms", "1e-2s", "var(--d)", "calc(1s + 2s)", "200", "", "fast"]


@unittest.skipIf(NODE is None, "node is not on PATH")
class MotionMjs(unittest.TestCase):
    def test_the_node_tests_pass(self):
        res = subprocess.run([NODE, "--test", "tools/kit/capture/test_motion.mjs"], cwd=HERE.parent, capture_output=True, text=True)
        self.assertEqual(res.returncode, 0, res.stdout + res.stderr)

    def test_python_and_node_normalise_alike(self):
        # The builder reads a custom property's raw value in Python, the probe reads computed ones in node:
        # one spelling on both sides, or a named easing would not match the one an element runs.
        mod = (KIT / "capture" / "motion.mjs").as_uri()
        res = subprocess.run([NODE, "--input-type=module", "-e",
                              f"import {{ normEasing, parseTime }} from {json.dumps(mod)};"
                              f"console.log(JSON.stringify([{json.dumps(EASINGS)}.map(normEasing), {json.dumps(TIMES)}.map(parseTime)]))"],
                             capture_output=True, text=True, timeout=30)
        self.assertEqual(res.returncode, 0, res.stderr)
        js_easing, js_time = json.loads(res.stdout)
        self.assertEqual([motion.norm_easing(e) for e in EASINGS], js_easing)
        self.assertEqual([motion.parse_time(t) for t in TIMES], js_time)

    def test_every_no_url_in_motion_mjs_is_the_kits(self):
        tested = re.search(r"noUrl = .*?: v\);", (KIT / "capture/vars.mjs").read_text()).group(0)
        copies = re.findall(r"noUrl = .*?: v\);", (KIT / "capture/motion.mjs").read_text())
        self.assertGreaterEqual(len(copies), 3)  # the module's own, and one in each page function
        for c in copies:
            self.assertEqual(c, tested)


class Normalise(unittest.TestCase):
    def test_times(self):
        self.assertEqual(motion.parse_time("0.2s"), 200)
        self.assertEqual(motion.parse_time("var(--d)"), None)
        self.assertEqual(motion.ms_str(200.0), "200ms")
        self.assertEqual(motion.ms_str(0.5), "0.5ms")
        self.assertEqual(motion.ms_key(0.5), "0_5ms")
        # a long duration keeps fixed decimals: %g wrote 6e+08ms as the value and the key
        self.assertEqual(motion.ms_str(6e8), "600000000ms")
        self.assertEqual(motion.ms_key(1234567.5), "1234567_5ms")
        self.assertEqual(motion.ms_str(0.0123), "0.012ms")
        self.assertEqual(motion.ms_str(0), "0ms")

    def test_easings(self):
        self.assertEqual(motion.norm_easing("cubic-bezier(0.40, 0, .2, 1.0)"), "cubic-bezier(0.4, 0, 0.2, 1)")
        self.assertEqual(motion.easing_bezier("ease-out"), [0, 0, 0.58, 1])
        self.assertEqual(motion.easing_bezier("cubic-bezier(0.4, 0, 0.2, 1)"), [0.4, 0, 0.2, 1])
        self.assertIsNone(motion.easing_bezier("steps(4, end)"))
        self.assertIsNone(motion.easing_bezier("linear(0, 1)"))
        self.assertEqual(motion.easing_key("ease-in-out"), "ease-in-out")
        self.assertEqual(motion.easing_key("cubic-bezier(0.4, 0, 0.2, 1)"), "bezier-0_4-0-0_2-1")
        self.assertEqual(motion.easing_key("cubic-bezier(0.3, -0.5, 0.6, 1.4)"), "bezier-0_3-m0_5-0_6-1_4")
        self.assertIsNone(motion.easing_key("steps(4, end)"))

    def test_classify(self):
        self.assertEqual([motion.classify_value(v) for v in ("120ms", "ease", "cubic-bezier(0.2, 0, 0, 1)", "8px", "0.2s")],
                         ["duration", "easing", "easing", "other", "duration"])


def tr(prop, ms, easing="ease", delay=0):
    return {"property": prop, "durationMs": ms, "delayMs": delay, "easing": easing}


def an(name, ms, easing="linear", iters="1"):
    return {"name": name, "durationMs": ms, "delayMs": 0, "easing": easing, "iterationCount": iters, "direction": "normal", "fillMode": "none"}


def group(count, transitions=(), animations=(), outcome="removed", items=()):
    return {"count": count, "outcome": outcome, "nodes": ["div.x"], "items": list(items),
            "base": {"transitions": list(transitions), "animations": list(animations)}, "reduced": {"transitions": [], "animations": []}}


RAW = {
    "_meta": {"probe": "page.emulateMedia({ reducedMotion })"},
    "summary": {"behaviour": "partial", "moving": 6, "removed": 4, "reduced": 0, "kept": 2, "partial": 0, "added": 0, "loops": ["spin"]},
    "pages": {"home": {
        "matchMedia": {"normal": False, "reduce": True},
        "groups": [
            group(4, [tr("background-color", 120, "cubic-bezier(0.2, 0, 0, 1)"), tr("transform", 200, "ease-in-out")],
                  items=[{"kind": "transition", "key": "background-color", "outcome": "removed"}, {"kind": "transition", "key": "transform", "outcome": "removed"}]),
            group(2, [tr("opacity", 200, "steps(4, end)")], [an("spin", 1000, "linear", "infinite")], "kept",
                  [{"kind": "transition", "key": "opacity", "outcome": "kept"}, {"kind": "animation", "key": "spin", "outcome": "kept", "loops": True}]),
        ],
        "keyframes": [{"name": "spin", "steps": [{"offset": "from", "properties": ["transform"]}, {"offset": "to", "properties": ["transform"]}], "properties": ["transform"]},
                      {"name": "orphan", "steps": [{"offset": "from", "properties": ["opacity"]}], "properties": ["opacity"]}],
        "declared": [{"selector": ".btn:hover", "context": [], "transitions": [{"property": "(base #0)", "durationMs": 400}], "animations": []},
                     {"selector": ".btn", "context": ["@media (prefers-reduced-motion: reduce)"], "transitions": [{"property": "(base #0)", "durationMs": 0.01}], "animations": []},
                     {"selector": ".menu:hover", "context": ["@media (prefers-reduced-motion: no-preference)"], "transitions": [{"property": "transform", "durationMs": 700, "easing": "ease-out"}], "animations": []}],
        "reducedMotionRules": [{"media": "@media (prefers-reduced-motion: reduce)", "selector": ".btn", "declarations": {"transition": "none"}}],
        "customProperties": [{"name": "--dur-fast", "declared": "120ms", "resolved": "0.12s", "selector": ":root"},
                             {"name": "--ease-out", "declared": "cubic-bezier(0.2,0,0,1)", "resolved": "cubic-bezier(0.2, 0, 0, 1)", "selector": ":root"},
                             {"name": "--ease-spring", "declared": "linear(0, 1)", "resolved": "linear(0, 1)", "selector": ":root"}],
    }},
}


class Build(unittest.TestCase):
    def setUp(self):
        self.group, self.not_tokenised = motion.build(RAW)

    def test_durations_are_named_by_a_custom_property_when_the_product_has_one(self):
        d = self.group["duration"]
        self.assertEqual(list(d), ["dur-fast", "200ms", "400ms", "700ms", "1000ms"])  # by value; the reduce rule's 0.01ms is not motion, a no-preference rule's 700ms is
        self.assertEqual(d["dur-fast"]["$value"], "120ms")
        self.assertEqual(d["dur-fast"]["$type"], "duration")
        self.assertEqual(d["400ms"]["$extensions"]["source"], {"evidence": "Measured", "capture": "raw/motion.json#declared"})
        self.assertEqual(d["dur-fast"]["$extensions"]["uses"], 4)

    def test_easings_label_derived_and_measured_and_set_aside_what_dtcg_cannot_carry(self):
        e = self.group["easing"]
        self.assertEqual(e["ease-out"]["$value"], [0.2, 0, 0, 1])
        self.assertEqual(e["ease-out"]["$extensions"]["source"]["evidence"], "Measured")
        self.assertEqual(e["ease-in-out"]["$value"], [0.42, 0, 0.58, 1])
        self.assertEqual(e["ease-in-out"]["$extensions"]["source"]["evidence"], "Derived")
        self.assertEqual(sorted(n["value"] for n in self.not_tokenised), ["linear(0, 1)", "steps(4, end)"])

    def test_transitions_alias_durations_and_easings_and_carry_what_reduce_did(self):
        t = self.group["transition"]
        self.assertEqual(t["background-color-120ms-ease-out"]["$value"],
                         {"duration": "{motion.duration.dur-fast}", "delay": "0ms", "timingFunction": "{motion.easing.ease-out}"})
        self.assertEqual(t["background-color-120ms-ease-out"]["$extensions"]["reducedMotion"], {"removed": 4})
        # an easing with no token stays a literal
        self.assertEqual(t["opacity-200ms-steps-4-end"]["$value"]["timingFunction"], "steps(4, end)")
        self.assertEqual(t["opacity-200ms-steps-4-end"]["$extensions"]["reducedMotion"], {"kept": 2})
        self.assertEqual(t["opacity-200ms-steps-4-end"]["$type"], "transition")

    def test_animations_carry_keyframes_and_the_unused_ones_are_listed(self):
        a = self.group["animation"]["spin"]
        self.assertEqual(a["$type"], "animation")
        self.assertEqual(a["$value"]["iterationCount"], "infinite")
        self.assertEqual(a["$extensions"]["keyframes"], {"properties": ["transform"], "steps": ["from", "to"]})
        self.assertEqual(a["$extensions"]["reducedMotion"], {"kept": 2})
        self.assertEqual(self.group["$extensions"]["unusedKeyframes"], ["orphan"])

    def test_a_normal_motion_rule_is_kept_and_a_reduce_rule_is_not(self):
        self.assertTrue(motion._is_reduce("@media (prefers-reduced-motion: reduce)"))
        self.assertFalse(motion._is_reduce("@media (prefers-reduced-motion: no-preference)"))
        self.assertFalse(motion._is_reduce("@media not (prefers-reduced-motion: reduce)"))
        self.assertIn("700ms", self.group["duration"])
        self.assertNotIn("0_01ms", self.group["duration"])

    def test_an_unresolved_var_or_keyword_easing_says_so(self):
        raw = json.loads(json.dumps(RAW))
        page = raw["pages"]["home"]
        page["groups"].append(group(1, [tr("color", 150, "var(--ease-x)"), tr("width", 150, "unset")], outcome="kept"))
        _, not_tokenised = motion.build(raw)
        why = {n["value"]: n["why"] for n in not_tokenised}
        self.assertIn("steps() or a linear() curve", why["steps(4, end)"])
        self.assertIn("unresolved var()", why["var(--ease-x)"])
        self.assertIn("CSS-wide keyword", why["unset"])

    def test_a_keyword_in_a_custom_property_is_derived(self):
        raw = json.loads(json.dumps(RAW))
        raw["pages"]["home"]["customProperties"].append({"name": "--ease-default", "declared": "ease", "resolved": "ease", "selector": ":root"})
        g, _ = motion.build(raw)
        self.assertEqual(g["easing"]["ease-default"]["$extensions"]["source"]["evidence"], "Derived")
        self.assertEqual(g["easing"]["ease-out"]["$extensions"]["source"]["evidence"], "Measured")  # a real cubic-bezier

    def test_names_that_would_collide_get_their_own_tokens_and_aliases_follow(self):
        raw = json.loads(json.dumps(RAW))
        pg = raw["pages"]["home"]
        # the custom --ease-out curve and the keyword ease-out, on two different transitions
        pg["groups"] = [group(1, [tr("opacity", 150, "cubic-bezier(0.2, 0, 0, 1)")]), group(1, [tr("color", 150, "ease-out")]),
                        group(1, [], [an("spin-x", 500)]), group(1, [], [an("spin_x", 700)])]
        g, _ = motion.build(raw)
        e = g["easing"]
        self.assertEqual(e["ease-out"]["$value"], [0.2, 0, 0, 1])
        self.assertEqual(e["ease-out-2"]["$value"], [0, 0, 0.58, 1])
        self.assertEqual(e["ease-out-2"]["$extensions"]["source"]["evidence"], "Derived")
        t = g["transition"]
        self.assertEqual(t["opacity-150ms-ease-out"]["$value"]["timingFunction"], "{motion.easing.ease-out}")
        self.assertEqual(t["color-150ms-ease-out-2"]["$value"]["timingFunction"], "{motion.easing.ease-out-2}")
        self.assertEqual(sorted(g["animation"]), ["spin-x", "spin-x-2"])
        self.assertEqual({v["$value"]["name"] for v in g["animation"].values()}, {"spin-x", "spin_x"})
        self.assertEqual(motion.uniq({"a", "a-2"}, "a"), "a-3")

    def test_a_cut_list_or_capped_page_is_recorded(self):
        raw = json.loads(json.dumps(RAW))
        raw["pages"]["home"]["sheetsTruncated"] = {"declared": True, "reducedRules": False, "customProperties": False}
        raw["pages"]["home"]["capped"] = {"cap": 3, "droppedNormal": 2, "droppedReduced": 0}
        g, _ = motion.build(raw)
        self.assertEqual(g["$extensions"]["incomplete"],
                         {"truncatedLists": ["declared"], "cappedPages": ["home"], "unreadableSheets": {}})
        self.assertNotIn("incomplete", self.group["$extensions"])

    def test_unreadable_cross_origin_sheets_are_recorded(self):
        raw = json.loads(json.dumps(RAW))
        raw["pages"]["home"]["unreadableSheets"] = 2
        g, _ = motion.build(raw)
        self.assertEqual(g["$extensions"]["incomplete"],
                         {"truncatedLists": [], "cappedPages": [], "unreadableSheets": {"home": 2}})

    def test_the_probe_verdict_and_which_properties_transition(self):
        x = self.group["$extensions"]
        self.assertEqual(x["reducedMotion"]["behaviour"], "partial")
        self.assertTrue(x["reducedMotion"]["verified"])
        self.assertEqual(x["reducedMotion"]["loops"], ["spin"])
        self.assertEqual(x["reducedMotion"]["authoredRules"][0]["declarations"], {"transition": "none"})
        self.assertEqual(x["propertyUsage"], {"background-color": 4, "transform": 4, "opacity": 2})

    def test_every_alias_points_at_a_token_and_every_token_has_a_label(self):
        core = {"motion": self.group}
        found = set()

        def walk(node, path):
            for k, v in node.items():
                if k.startswith("$"):
                    continue
                if "$value" in v:
                    found.add(".".join(path + [k]))
                    src = v["$extensions"]["source"]
                    self.assertIn(src["evidence"], ("Measured", "Derived"), k)
                    self.assertTrue(src["capture"].startswith("raw/motion.json"), k)
                else:
                    walk(v, path + [k])
        walk(core["motion"], ["motion"])
        for path in list(found):
            node = self.group
            for k in path.split(".")[1:]:
                node = node[k]
            for a in re.findall(r"\{([^{}]+)\}", json.dumps(node["$value"])):
                self.assertIn(a, found, f"{path}: {{{a}}} points at nothing")

    def test_same_input_same_bytes(self):
        again, _ = motion.build(json.loads(json.dumps(RAW)))
        self.assertEqual(json.dumps(again), json.dumps(self.group))

    def test_the_catalog_exports_durations_and_easings_and_skips_the_composites(self):
        out = catalog.export_tokens({"core": {"motion": self.group}}, ["light", "dark"])
        self.assertEqual(out["unresolved"], [])
        self.assertEqual(out["base"]["--motion-duration-dur-fast"], "120ms")
        self.assertEqual(out["base"]["--motion-easing-ease-out"], "cubic-bezier(0.2, 0, 0, 1)")
        self.assertIn("core.motion.animation.spin", out["skipped"])

    def test_no_motion_read_makes_an_empty_group(self):
        g, nt = motion.build({"_meta": {}, "summary": {"behaviour": "no-motion", "moving": 0, "removed": 0, "reduced": 0, "kept": 0, "partial": 0, "added": 0, "loops": []},
                              "pages": {"p": {"matchMedia": {"normal": False, "reduce": True}, "groups": []}}})
        self.assertEqual(set(g) - {"$description", "$extensions"}, set())
        self.assertEqual(g["$extensions"]["reducedMotion"]["behaviour"], "no-motion")


class Wiring(unittest.TestCase):
    def test_build_tokens_adds_the_group_only_when_the_probe_ran(self):
        src = (KIT / "build/build_tokens.py").read_text()
        self.assertIn('if (RAW / "motion.json").exists():', src)
        self.assertIn('core["motion"], motion_not_core = motion.build(', src)

    def test_the_style_guide_motion_previews_name_variables_through_cssname(self):
        # easing keys hold "_" (bezier-0_4-0-0_2-1); the builder writes "-", so a hand-built name points at nothing
        tpl = (KIT / "build/style-guide.template.html").read_text()
        self.assertNotIn("var(--motion-", tpl)
        self.assertIn("cssname('motion.easing.", tpl)
        self.assertIn("cssname('motion.' + n)", tpl)

    def test_the_style_guide_builder_leaves_composites_out_of_css(self):
        tree = ast.parse((KIT / "build/build_style_guide.py").read_text())
        fns = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name in ("cssname", "alias", "css_val")]
        ns = {"re": re}
        exec(compile(ast.Module(fns, []), "build_style_guide.py", "exec"), ns)
        t = {"$value": {"duration": "{motion.duration.x}"}, "$type": "transition", "$extensions": {}}
        self.assertIsNone(ns["css_val"]("motion.transition.x", t))
        self.assertIsNone(ns["css_val"]("motion.animation.x", {**t, "$type": "animation"}))
        self.assertEqual(ns["css_val"]("motion.duration.x", {"$value": "120ms", "$type": "duration"}), "120ms")
        self.assertEqual(ns["css_val"]("motion.easing.x", {"$value": [0.2, 0, 0, 1], "$type": "cubicBezier"}), "cubic-bezier(0.2, 0, 0, 1)")


if __name__ == "__main__":
    unittest.main()
