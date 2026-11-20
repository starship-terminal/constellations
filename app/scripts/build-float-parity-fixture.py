#!/usr/bin/env python3
"""Write app/tests/fixtures/float-parity.json: what the Python tool layer
(server/library.py and tools/catalog.py) prints for JSON floats, so the
TypeScript port in app/src/server/sources/pyjson.ts can be tested against the
real thing. Python is the reference for every value in the fixture.

Run `python3 app/scripts/build-float-parity-fixture.py` from any directory;
`--check` compares against the committed fixture without writing it.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "app/tests/fixtures/float-parity.json"
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "server"))
import catalog  # noqa: E402

spec = importlib.util.spec_from_file_location("library", ROOT / "server/library.py")
library = importlib.util.module_from_spec(spec)
spec.loader.exec_module(library)

# Each text is parsed and printed by Python exactly as library.call prints a
# result it has to truncate: json.dumps(ensure_ascii=False, compact separators).
JSON_CASES = {
    "whole floats stay floats": "[1.0, 0.0, 2.0, -3.0, 100.0, 1.00, 12.50]",
    "negative zero": "[-0.0, 0.0]",
    "integers stay integers": "[0, 1, -1, 100, 9007199254740991]",
    "exponent spellings of whole numbers": "[1e2, 1E+2, 1.0e0, 5e0, -2E1]",
    "plain fractions": "[0.5, 0.25, 0.1, 0.0001, 123.456, 3.14159]",
    "small floats switch to an exponent": "[0.00001, 1e-5, 1.5e-7, 0.00001234, 1e-10, -2.5e-05]",
    "large floats switch to an exponent": "[1e15, 1e16, 1.5e16, 12345678901234567.0, 1e22, 123456789012345.0]",
    "floats in objects and nesting": '{"a": 1.0, "b": [0.0, {"c": 2.0, "d": 0.5}], "e": 1}',
    "strings and other scalars are untouched": '{"s": "1.0", "t": "café \\u00e9", "n": null, "b": [true, false], "u": "\\n\\t\\""}',
    "empty containers": '{"a": [], "b": {}}',
}
TOKENS = {
    "core": {
        "opacity": {"$value": 1.0, "$type": "number"},
        "lineHeight": {"$value": 1.50, "$type": "number"},
        "weight": {"$value": 600, "$type": "number"},
        "tiny": {"$value": 0.00001, "$type": "number"},
        "alias": {"$value": "{core.opacity}", "$type": "number"},
        "ease": {"$value": [0.0, 0.0, 1.0, 1.0], "$type": "cubicBezier"},
        "legacy": {"value": 2.0, "type": "number"},
        "wash": {
            "$value": {"colorSpace": "srgb", "components": [1.0, 0.5, 0.0], "alpha": 1.0},
            "$type": "color",
        },
        # 0.3 and 0.7 land on .5 after * 255; round() takes the even side.
        "half": {
            "$value": {"colorSpace": "srgb", "components": [0.3, 0.7, 0.5], "alpha": 0.3},
            "$type": "color",
        },
    }
}
# Written with the spellings a real file uses, which json.dumps would normalise.
TOKENS_TEXT = """{
  "core": {
    "opacity": {"$value": 1.0, "$type": "number"},
    "lineHeight": {"$value": 1.50, "$type": "number"},
    "weight": {"$value": 600, "$type": "number"},
    "tiny": {"$value": 0.00001, "$type": "number"},
    "alias": {"$value": "{core.opacity}", "$type": "number"},
    "ease": {"$value": [0.0, 0.0, 1.0, 1.0], "$type": "cubicBezier"},
    "legacy": {"value": 2.0, "type": "number"},
    "wash": {
      "$value": {"colorSpace": "srgb", "components": [1.0, 0.5, 0.0], "alpha": 1.0},
      "$type": "color"
    },
    "half": {
      "$value": {"colorSpace": "srgb", "components": [0.3, 0.7, 0.5], "alpha": 0.3},
      "$type": "color"
    }
  }
}
"""


def compact(value) -> str:
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"))


def build() -> dict:
    cases = [
        {"name": name, "text": text, "python": compact(json.loads(text))}
        for name, text in JSON_CASES.items()
    ]
    # Sanity: the compact form is the one library._json_size measures.
    for case in cases:
        assert library._json_size(json.loads(case["text"])) == len(case["python"].encode())
    tokens = json.loads(TOKENS_TEXT)
    assert tokens == TOKENS
    exported = catalog.export_tokens(tokens, [])
    return {
        "generatedBy": "python3 app/scripts/build-float-parity-fixture.py",
        "json": cases,
        "tokens": {"text": TOKENS_TEXT, "python": exported["base"]},
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    text = json.dumps(build(), indent=2, ensure_ascii=False) + "\n"
    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_text(encoding="utf-8") != text:
            print(f"{OUTPUT.relative_to(ROOT)} is stale; rerun without --check")
            return 1
        return 0
    OUTPUT.write_text(text, encoding="utf-8")
    print(f"wrote {OUTPUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
