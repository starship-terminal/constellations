#!/usr/bin/env python3
"""Build tokens.json from the public Brilliant readings.

Source: raw/css-vars.json, computed on documentElement at
https://brilliant.org/ on 2026-11-21, signed out, data-theme light.
Component colours come from raw/components-computed.json.

The previous signed-in token file is kept as tokens.signed-in-2026-10.json.
This builder writes the public set only. Same inputs, same bytes.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
VARS = json.loads((HERE / "raw" / "css-vars.json").read_text())["computed"]


def token(value, ty, source, description=None):
    out = {"$value": value, "$type": ty, "$extensions": {"source": source}}
    if description:
        out["$description"] = description
    return out


def color(name):
    value = VARS[name].strip()
    if value == "#fff":
        return "#FFFFFF"
    if value == "#000":
        return "#000000"
    if value.startswith("#") and len(value) == 7:
        return value.upper()
    raise ValueError("not a 6-digit colour: %s=%r" % (name, value))


def main():
    src = "css-var, computed on :root at brilliant.org, signed out, data-theme light, 2026-11-21"
    face = "computed style of the painted span, signed-out homepage, 2026-11-21"
    data = {
        "core": {
            "fontFamily": {
                "brilliant": token(
                    VARS["--panda-fonts-brilliant"],
                    "fontFamily",
                    src,
                ),
                "robert": token(VARS["--panda-fonts-robert"], "fontFamily", src),
                "code": token(VARS["--panda-fonts-code"], "fontFamily", src),
            },
            "radius": {
                "field": token("8px", "dimension", "computed #id_login border-radius on /login/"),
                "pill": token("60px", "dimension", face + ", learner face"),
                "sign-in": token("54px", "dimension", "computed Sign in button border-radius"),
            },
        },
        "light": {
            "page": token(color("--panda-colors-bg-primary"), "color", src, "Body background."),
            "oat": token(color("--panda-colors-bg-oat"), "color", src, "Homepage hero surface."),
            "text": token(color("--panda-colors-text-primary"), "color", src, "Homepage h1."),
            "accent": token(color("--panda-colors-text-link"), "color", src, "Link colour."),
            "learner": token(color("--panda-colors-bg-green-primary"), "color", src, "I'm a learner face."),
            "learner-lip": token(color("--panda-colors-bg-success-hover"), "color", src, "3D lip under the learner face."),
            "border-oat": token(color("--panda-colors-border-oat"), "color", src, "Sign in outline."),
            "login-page": token(color("--panda-colors-gray-950"), "color", src, "/login/ page background rgb(20, 20, 20)."),
            "login-button": token(color("--panda-colors-gray-200"), "color", src, "Login Sign in face rgb(229, 229, 229)."),
        },
        "$themes": [{"name": "light", "selectedColor": "#29CC57"}],
    }
    out = json.dumps(data, indent=2) + "\n"
    (HERE / "tokens.json").write_text(out)
    print("wrote", HERE / "tokens.json")


if __name__ == "__main__":
    main()
