#!/usr/bin/env python3
"""Build tokens.json from the Meiro public capture.

Marketing pages (meiro.cc, Framer ab3275d) declare a 15-step palette as
unnamed --token-* custom properties on body. The signed-out app
(app.meiro.cc) paints the same ink, lime and surface steps with its own
radii, SF Pro and TT Hoves. This builder writes those measured values.
It does not invent a light theme: both surfaces ship dark.

    python3 tools/build_tokens.py

Deterministic: same inputs, same bytes. Run from anywhere.
"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
RAW = ROOT / "raw"
sys.path.insert(0, str(HERE))
import motion  # noqa: E402

SRC = "Measured on meiro.cc and app.meiro.cc, 2026-11-19, signed out, 1440x900 and 390x844"


def color(value, source, evidence="Measured"):
    return {"$value": value, "$type": "color", "$extensions": {"source": source, "evidence": evidence}}


def dim(value, source, evidence="Measured"):
    return {"$value": value, "$type": "dimension", "$extensions": {"source": source, "evidence": evidence}}


def font(value, source, evidence="Measured"):
    return {"$value": value, "$type": "fontFamily", "$extensions": {"source": source, "evidence": evidence}}


def num(value, source, typ="number", evidence="Measured"):
    return {"$value": value, "$type": typ, "$extensions": {"source": source, "evidence": evidence}}


def typography(family, size, line, weight, source, evidence="Measured"):
    return {
        "$value": {
            "fontFamily": family,
            "fontSize": size,
            "fontWeight": int(weight),  # DTCG fontWeight is a number, not the string getComputedStyle returns
            "lineHeight": line,
        },
        "$type": "typography",
        "$extensions": {"source": source, "evidence": evidence},
    }


HAND = "Entered by hand at capture time; no file in raw/ holds this reading. "


# Framer body tokens, declared in the marketing stylesheet (raw/framer-tokens.css).
# Names are roles, assigned by which computed style used the value.
PALETTE = {
    "ink": ("#0e0f0f", "--token-af7f1007-a891-404b-a923-96f397ca18a3"),
    "ink-raised": ("#171818", "--token-5e6ff635-baf9-4d5f-b7d3-3ea121a7b343"),
    "ink-card": ("#202222", "--token-6ca14b64-8de1-4483-b242-dc1b60e851d4"),
    "ink-hover": ("#2e3030", "--token-76f83a23-c2c8-42e5-b84a-3e4723900f33"),
    "line": ("#3b3e3e", "--token-c53cbadf-9768-4d52-8708-bc48d4ef0139"),
    "muted-strong": ("#6e7171", "--token-36f08672-fd87-4103-9f44-06f1274049c3"),
    "muted": ("#787878", "--token-15e1f524-8540-4922-9db3-a1054b564935"),
    "muted-soft": ("#808484", "--token-aedab33d-8442-4753-9f74-03d578a5e7d6"),
    "text-secondary": ("#ced1d1", "--token-701b5db7-fa87-43a2-bdc2-258a39792047"),
    "text-on-dark": ("#f3f4f9", "--token-c7d25ff6-d839-4357-a663-9119ff394b7c"),
    "white": ("#ffffff", "--token-cba57776-6077-412b-ad81-0f6ad78a69c7"),
    "lime-soft": ("#e4ff8f", "--token-910a4c25-d6d3-4a02-b0ee-de8c71fab9f5"),
    "lime": ("#d5fe52", "--token-e482d2e1-beb7-471b-8735-ba80bb36a684"),
    "lime-deep": ("#c0ef2a", "--token-297d6991-d526-4209-bc7c-68148dc51b26"),
    "danger": ("#ff7c7c", "--token-58f0f0dc-405d-4172-910c-f2559c870309"),
}

core_color = {}
for name, (value, var) in PALETTE.items():
    core_color[name] = color(value, f"Declared on body as {var} in the Framer stylesheet; {SRC}")

# Widget purple is painted, not a Framer token.
core_color["widget"] = color(
    "#a280ff",
    "Computed background of the Gleap launcher, rgb(162, 128, 255), on meiro.cc at 1440",
)

core = {
    "color": core_color,
    "font": {
        "family": {
            "display": font(
                '"TT Hoves DemiBold", "TT Hoves DemiBold Placeholder", sans-serif',
                "Computed font-family of h1 on meiro.cc",
            ),
            "medium": font(
                '"TT Hoves Medium", "TT Hoves Medium Placeholder", sans-serif',
                "Computed font-family of nav labels and primary button labels on meiro.cc",
            ),
            "regular": font(
                '"TT Hoves Regular", "TT Hoves Regular Placeholder", sans-serif',
                "Computed font-family of the hero body paragraph on meiro.cc",
            ),
            "app-display": font(
                "TTHoves, sans-serif",
                "Computed font-family of h2 on app.meiro.cc/login",
            ),
            "app-ui": font(
                "SFPro, system-ui, sans-serif",
                "Computed font-family of buttons and inputs on app.meiro.cc/login",
            ),
        }
    },
    "typography": {
        "display": typography("{font.family.display}", "50px", "70px", "400", "h1 on meiro.cc at 1440"),
        "display-mobile": typography("{font.family.display}", "34px", "44.2px", "400",
                                     HAND + "h1 on meiro.cc at 390: raw/ holds the 34px size but no 390-wide line height; 44.2px is 34px x 1.3",
                                     evidence="Reconstruction"),
        "title": typography("{font.family.display}", "32px", "44.8px", "400", "h3 section titles on meiro.cc"),
        "eyebrow": typography("{font.family.medium}", "18px", "23.4px", "400", "lime eyebrow on meiro.cc/pricing"),
        "body": typography("{font.family.regular}", "20px", "30px", "400", "hero paragraph on meiro.cc"),
        "body-secondary": typography("{font.family.regular}", "16px", "24px", "400", "plan description on meiro.cc/pricing"),
        "nav": typography("{font.family.medium}", "16px", "20px", "400", "header nav labels on meiro.cc"),
        "caption": typography("{font.family.regular}", "15px", "21px", "400", "trial note under the hero CTA"),
        "price": typography("{font.family.display}", "34px", "47.6px", "400", "price figure on meiro.cc/pricing"),
        "app-title": typography("{font.family.app-display}", "24px", "34px", "600", "h2 on app.meiro.cc/login"),
        "app-button": typography("{font.family.app-ui}", "15px", "20px", "600", "Continue with email on app.meiro.cc/login"),
        "app-legal": typography("{font.family.app-ui}", "13px", "16px", "400", "Terms of Use link on app.meiro.cc/login"),
    },
    "radius": {
        "header": dim("24px", "header border-bottom radius on meiro.cc"),
        "nav": dim("18px", "nav pill and primary marketing button on meiro.cc"),
        "card": dim("20px", "review cards, data-framer-name Review 1, on meiro.cc"),
        "plan": dim("18px", "Start for free button on meiro.cc/pricing"),
        "billing": dim("90px", "selected Annual billing pill on meiro.cc/pricing"),
        "app-card": dim("30px", "sign-in card on app.meiro.cc/login"),
        "app-button": dim("17px", "Continue with email on app.meiro.cc/login"),
        "app-field": dim("15px", "email input on app.meiro.cc/login"),
        "widget": dim("48px", "Gleap launcher circle"),
    },
    "spacing": {
        "1": dim("4px", HAND + "A 4px step chosen for the rhythm of the measured paddings (the 5px nav inset rounds to it)",
                 evidence="Reconstruction"),
        "2": dim("8px", "gap between trial notes"),
        "3": dim("12px", "input horizontal padding on the app field"),
        "4": dim("16px", "primary button vertical padding on meiro.cc"),
        "5": dim("20px", "section rhythm"),
        "6": dim("24px", "primary button horizontal padding on meiro.cc"),
        "8": dim("32px", "hero block gap"),
        "10": dim("40px", "sign-in card horizontal padding"),
    },
    "size": {
        "header": dim("84px", "header height on meiro.cc at 1440"),
        "header-mobile": dim("72px", "header height on meiro.cc at 390"),
        "button": dim("52px", "Get started button height on meiro.cc"),
        "button-hero": dim("56px", "hero Get started button height on meiro.cc"),
        "app-control": dim("50px", "email button and input height on app.meiro.cc/login"),
        "app-card": dim("520px", "sign-in card width on app.meiro.cc/login at 1440"),
        "content": dim("1080px", HAND + "A content width chosen for the plan row. The three 332px plan cards in raw/states.json start at x 144, 554 and 964, a 1152px span, so 1080px is not derived from them",
                       evidence="Reconstruction"),
    },
    "border": {
        "field": dim("1px", "email input border width on app.meiro.cc/forgot-password"),
    },
}

# Semantic set. One theme: dark. Marketing and the signed-out app share it.
dark = {
    "page": color("{color.ink}", "body background rgb(14, 15, 15) on meiro.cc; html background #0e0f0f on app.meiro.cc"),
    "surface": color("{color.ink-raised}", "nav pill and review cards rgb(23, 24, 24); sign-in card on app.meiro.cc"),
    "surface-raised": color("{color.ink-card}", "email field and Google button rgb(32, 34, 34) on app.meiro.cc/login"),
    "surface-hover": color("#2c2e2e", "Google button hover background rgb(44, 46, 46) on app.meiro.cc/login"),
    "text": color("{color.white}", "h1 color rgb(255, 255, 255) on meiro.cc"),
    "muted": color("{color.text-secondary}", "hero paragraph rgb(206, 209, 209) on meiro.cc"),
    "muted-soft": color("{color.muted-soft}", "legal links rgb(128, 132, 132) on app.meiro.cc/login"),
    "on-accent": color("{color.ink}", "primary button label rgb(14, 15, 15)"),
    "accent": color("{color.lime}", "Get started and Start for free fill rgb(213, 254, 82); pricing eyebrow"),
    "accent-deep": color("{color.lime-deep}", "Continue with email fill rgb(192, 239, 42) on app.meiro.cc/login"),
    "accent-text": color("{color.lime}", "Save $84 and legal-page links on meiro.cc"),
    "border": color("{color.line}", "email field border rgb(59, 62, 62) on app.meiro.cc/forgot-password"),
    "danger": color("{color.danger}", "declared --token danger #ff7c7c; not painted on a captured control"),
    "focus": color("#005fcc", "Chromium's default focus ring, not a Meiro colour: the forced focus-visible outline on the marketing Get started link reads rgb(0, 95, 204), the browser's -webkit-focus-ring-color. Meiro styles no ring of its own",
                   evidence="Observed"),
    "widget": color("{color.widget}", "Gleap launcher"),
    "component": {
        "button-primary": {
            "background": color("{color.lime}", "Get started computed background"),
            "text": color("{color.ink}", "Get started label color"),
            "radius": dim("{radius.nav}", "Get started border-radius 18px"),
            "height": dim("{size.button}", "Get started height 52px"),
            "padding": dim("16px", "Get started padding-block"),
        },
        "button-email": {
            "background": color("{color.lime-deep}", "Continue with email computed background"),
            "text": color("{color.ink}", "Continue with email label color"),
            "radius": dim("{radius.app-button}", "17px"),
            "height": dim("{size.app-control}", "50px"),
        },
        "button-google": {
            "background": color("{color.ink-card}", "Continue with Google computed background"),
            "text": color("{color.white}", "Continue with Google label color"),
            "radius": dim("{radius.app-button}", "17px"),
            "height": dim("{size.app-control}", "50px"),
        },
        "text-field": {
            "background": color("{color.ink-card}", "email input computed background"),
            "text": color("{color.white}", "email input color"),
            "radius": dim("{radius.app-field}", "15px"),
            "height": dim("{size.app-control}", "50px"),
        },
        "card": {
            "background": color("{color.ink-raised}", "sign-in card computed background"),
            "radius": dim("{radius.app-card}", "30px"),
        },
    },
}

doc = {
    "core": core,
    "dark": dark,
    "$themes": [
        {
            "id": "dark",
            "name": "Dark",
            "selectedTokenSets": {"core": "source", "dark": "enabled"},
            "$extensions": {
                "source": "Both meiro.cc and app.meiro.cc paint one dark theme. No light theme was declared or switched."
            },
        }
    ],
}

if (RAW / "motion.json").exists():
    motion_raw = json.loads((RAW / "motion.json").read_text())
    motion_group, not_tokenised = motion.build(motion_raw)
    core["motion"] = motion_group
    if not_tokenised:
        core.setdefault("$extensions", {})["notTokenised"] = not_tokenised

def leaves(node, path=""):
    for k, v in node.items():
        if k.startswith("$") or not isinstance(v, dict):
            continue
        here = f"{path}.{k}" if path else k
        if "$value" in v:
            yield here, v
        else:
            yield from leaves(v, here)


CHANNEL = r"\s*\d{1,3}\s*"
COLOR = (r"#[0-9a-f]{6}([0-9a-f]{2})?"
         rf"|rgb\({CHANNEL},{CHANNEL},{CHANNEL}\)|rgba\({CHANNEL},{CHANNEL},{CHANNEL},\s*(0|1|0?\.\d+)\s*\)")


def check(doc):
    """The kit's guards: every alias resolves (dark first, then core), every leaf has a source
    and an evidence label, and dimensions and colours have DTCG shapes. Raises before writing."""
    core_names = {p for p, _ in leaves(doc["core"])}
    for setname in ("core", "dark"):
        local = {p for p, _ in leaves(doc[setname])}
        for path, tok in leaves(doc[setname]):
            ext = tok.get("$extensions", {})
            src = ext.get("source")
            evidence = ext.get("evidence") or (src.get("evidence") if isinstance(src, dict) else None)
            if not src or not evidence:
                raise SystemExit(f"{setname}.{path}: no source or evidence")
            values = tok["$value"].values() if isinstance(tok["$value"], dict) else [tok["$value"]]
            for v in values:
                for ref in re.findall(r"\{([^{}]+)\}", str(v)):
                    if ref not in local and ref not in core_names:
                        raise SystemExit(f"{setname}.{path}: alias {{{ref}}} resolves to nothing")
            v = tok["$value"]
            if isinstance(v, str) and v.startswith("{"):
                continue
            if tok["$type"] == "dimension" and not (isinstance(v, str) and re.fullmatch(r"-?\d*\.?\d+(px|rem)", v)):
                raise SystemExit(f"{setname}.{path}: dimension {v!r}")
            if tok["$type"] == "color" and not (isinstance(v, str) and re.fullmatch(COLOR, v)):
                raise SystemExit(f"{setname}.{path}: colour {v!r}")


check(doc)

if __name__ == "__main__":
    out = ROOT / "tokens.json"
    text = json.dumps(doc, indent=2, ensure_ascii=False) + "\n"
    out.write_text(text)
    print(f"wrote {out} ({out.stat().st_size} bytes)")
