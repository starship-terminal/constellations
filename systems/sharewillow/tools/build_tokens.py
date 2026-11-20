#!/usr/bin/env python3
"""Build tokens.json from the live readings in raw/.

Marketing colours, type and radii come from the :root custom properties in
raw/theme.css.json. App colours come from the resolved HSL tokens in
raw/login-tokens.json. Component sizes come from raw/components.json.
Nothing here is invented: a value that was not read is listed under
$extensions.notTokenised instead of filled in.

The marketing site had no dark theme. The `dark` set is the measured hero
and footer palette (a dark band on the light page), not a second theme.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
THEME = json.loads((RAW / "theme.css.json").read_text())
LOGIN = json.loads((RAW / "login-tokens.json").read_text())
COMP = json.loads((RAW / "components.json").read_text())

M_SRC = "raw/theme.css.json :root custom property, www.sharewillow.com, 2026-11-19"
L_SRC = "raw/login-tokens.json computed hsl() on app.sharewillow.com/login, 2026-11-19"
C_SRC = "raw/components.json getComputedStyle, 2026-11-19"


def color(value, source):
    return {"$type": "color", "$value": value, "$extensions": {"source": source, "evidence": "Measured"}}


def dim(value, source):
    return {"$type": "dimension", "$value": value, "$extensions": {"source": source, "evidence": "Measured"}}


def num(value, source):
    return {"$type": "number", "$value": value, "$extensions": {"source": source, "evidence": "Measured"}}


def font(value, source):
    return {"$type": "fontFamily", "$value": value, "$extensions": {"source": source, "evidence": "Measured"}}


def other(value, source, evidence="Measured"):
    return {"$value": value, "$extensions": {"source": source, "evidence": evidence}}


def typo(family, size, weight, line, tracking, source):
    token = {
        "$type": "typography",
        "$value": {
            "fontFamily": family,
            "fontSize": size,
            "fontWeight": weight,
            "lineHeight": line,
        },
        "$extensions": {"source": source, "evidence": "Measured"},
    }
    if tracking is not None:
        token["$value"]["letterSpacing"] = tracking
    return token


P = THEME["properties"]
props = P  # alias used below

core = {
    "font": {
        "family": {
            "sans": font(props["--font-sans"], M_SRC + " --font-sans"),
            "display": font(props["--font-display"], M_SRC + " --font-display"),
            "mono": font(props["--font-mono"], M_SRC + " --font-mono"),
        },
        "weight": {
            "normal": num(400, M_SRC + " --font-weight-normal"),
            "medium": num(500, M_SRC + " --font-weight-medium"),
            "semibold": num(600, M_SRC + " --font-weight-semibold"),
            "bold": num(700, M_SRC + " --font-weight-bold"),
        },
    },
    "palette": {
        "lemon": color(props["--color-lemon"], M_SRC + " --color-lemon"),
        "lemon-deep": color(props["--color-lemon-deep"], M_SRC + " --color-lemon-deep"),
        "ivory": color(props["--color-ivory"], M_SRC + " --color-ivory"),
        "paper": color(props["--color-paper"], M_SRC + " --color-paper"),
        "espresso": color(props["--color-espresso"], M_SRC + " --color-espresso"),
        "lime": color(props["--color-lime"], M_SRC + " --color-lime"),
        "peach": color(props["--color-peach"], M_SRC + " --color-peach"),
        "sky": color(props["--color-sky"], M_SRC + " --color-sky"),
        "rose": color(props["--color-rose"], M_SRC + " --color-rose"),
    },
    "radius": {
        "sm": dim(props["--radius-sm"], M_SRC + " --radius-sm"),
        "md": dim(props["--radius-md"], M_SRC + " --radius-md"),
        "lg": dim(props["--radius-lg"], M_SRC + " --radius-lg"),
        "xl": dim(props["--radius-xl"], M_SRC + " --radius-xl"),
        "2xl": dim(props["--radius-2xl"], M_SRC + " --radius-2xl"),
        "3xl": dim(props["--radius-3xl"], M_SRC + " --radius-3xl"),
        "full": dim("9999px", C_SRC + " pill controls computed borderRadius 1.67772e+07px, recorded as 9999px"),
    },
    "spacing": {
        "unit": dim("4px", M_SRC + " --spacing .25rem at a 16px root"),
        "2": dim("8px", C_SRC + " announcement gap 8px and padding 8px"),
        "3": dim("12px", C_SRC + " menu row padding 12px"),
        "4": dim("16px", C_SRC + " body font-size 16px and header button padding-inline 16px"),
        "5": dim("20px", C_SRC + " menu feature card padding 20px"),
        "6": dim("24px", C_SRC + " body line-height 24px"),
        "7": dim("28px", C_SRC + " hero button padding-inline 28px"),
        "8": dim("32px", C_SRC + " pricing card padding 32px"),
        "12": dim("48px", C_SRC + " login card padding 48px"),
    },
    "layout": {
        "content": dim("1280px", C_SRC + " max-w-[1280px] measured 1280px at innerWidth 1440"),
        "menu": dim("860px", C_SRC + " product menu card width 860px"),
        "login-card": dim("576px", C_SRC + " login card width 576px"),
        "container-6xl": dim("1152px", M_SRC + " --container-6xl 72rem"),
    },
    "typography": {
        "display-xl": typo(
            "{font.family.display}", "80px", 500, "80px", "-2.4px",
            C_SRC + " h1.text-display-xl at innerWidth 1440. Class rule is clamp(2.75rem, 6vw, 5rem), weight 500, line-height 1, tracking -0.03em",
        ),
        "display-lg": typo(
            "{font.family.display}", "52px", 500, "54.6px", "-1.3px",
            C_SRC + " text-display-lg class is clamp(2rem, 4vw, 3.25rem), tracking -0.025em, line-height 1.05. 52px is the measured pricing figure at 1440, the same clamp ceiling.",
        ),
        "body": typo(
            "{font.family.sans}", "16px", 400, "24px", "0px",
            C_SRC + " body computed 16px/24px Matter 400",
        ),
        "lede": typo(
            "{font.family.sans}", "18px", 400, "27.9px", "0px",
            C_SRC + " hero lede computed 18px, line-height 27.9px, color ink-muted",
        ),
        "nav": typo(
            "{font.family.sans}", "14px", 400, "21px", "0px",
            C_SRC + " nav link computed 14px/21px",
        ),
        "button": typo(
            "{font.family.sans}", "13px", 500, "19.5px", "0px",
            C_SRC + " header Book a demo computed 13px/19.5px weight 500",
        ),
        "eyebrow": typo(
            "{font.family.sans}", "10px", 500, "16px", "1.6px",
            C_SRC + " menu eyebrow FOR YOUR TECHS, 10px/16px, tracking 1.6px, uppercase",
        ),
        "login-title": typo(
            "{font.family.display}", "24px", 400, "32px", "0px",
            C_SRC + " login h1 Welcome Back, p22-mackinac-pro 24px/32px weight 400",
        ),
        "login-label": typo(
            "{font.family.sans}", "14px", 400, "20px", "0px",
            C_SRC + " login label 14px/20px. Line-height taken from the 14px input, not the label.",
        ),
    },
    "motion": {
        "duration": {
            "fast": other("150ms", M_SRC + " --default-transition-duration .15s"),
            "button": other("200ms", C_SRC + " button transition duration-200"),
            "header": other("300ms", C_SRC + " header transform 0.3s"),
            "hero": other("700ms", M_SRC + " .hero-in animation 0.7s, raw/theme.css.json motion.hero-in"),
        },
        "easing": {
            "out": other(props["--ease-out"], M_SRC + " --ease-out"),
            "in-out": other(props["--ease-in-out"], M_SRC + " --ease-in-out"),
            "out-quart": other(props["--ease-out-quart"], M_SRC + " --ease-out-quart"),
        },
        "$extensions": {
            "reducedMotion": THEME["motion"]["reducedMotion"],
            "evidence": "Measured",
        },
    },
    "control": {
        "nav-height": dim("33px", C_SRC + " nav link height 33px"),
        "button-sm": dim("36px", C_SRC + " header Book a demo height 36px"),
        "button-md": dim("48px", C_SRC + " lemon and Ask buttons height 48px"),
        "button-lg": dim("56px", C_SRC + " hero Book a demo height 56px"),
        "login-input": dim("40px", C_SRC + " login input height 40px"),
        "login-button": dim("44px", C_SRC + " login submit height 44px"),
        "signup-input": dim("48px", C_SRC + " signup email height 48px at innerWidth 1169"),
        "checkbox": dim("16px", C_SRC + " login checkbox 16px"),
        "focus-ring": dim("2px", C_SRC + " login focus box-shadow 2px white offset plus 4px ink ring"),
    },
}

light = {
    "bg": {
        "page": color(props["--color-bg"], M_SRC + " --color-bg. Body computed rgb(247, 245, 241)."),
        "surface": color(props["--color-surface"], M_SRC + " --color-surface"),
        "surface-2": color(props["--color-surface-2"], M_SRC + " --color-surface-2"),
        "paper": color(props["--color-paper"], M_SRC + " --color-paper"),
    },
    "text": {
        "primary": color(props["--color-ink"], M_SRC + " --color-ink. Body computed rgb(24, 6, 0)."),
        "muted": color(props["--color-ink-muted"], M_SRC + " --color-ink-muted. Lede computed rgb(107, 91, 74)."),
        "subtle": color(props["--color-ink-subtle"], M_SRC + " --color-ink-subtle"),
        "on-accent": color(props["--color-accent-ink"], M_SRC + " --color-accent-ink"),
        "on-primary": color("#ffffff", C_SRC + " header Book a demo computed color rgb(255, 255, 255)"),
    },
    "accent": {
        "default": color(props["--color-accent"], M_SRC + " --color-accent"),
        "deep": color(props["--color-lemon-deep"], M_SRC + " --color-lemon-deep. Declared hover target for lemon, not measured on a hovered element."),
        "ink": color(props["--color-espresso"], M_SRC + " --color-espresso. Primary button face."),
    },
    "border": {
        "default": color(props["--color-border"], M_SRC + " --color-border"),
        "strong": color(props["--color-border-strong"], M_SRC + " --color-border-strong"),
    },
    "status": {
        "lime": color(props["--color-lime"], M_SRC + " --color-lime. Palette swatch, not seen as a status chip."),
        "peach": color(props["--color-peach"], M_SRC + " --color-peach. Palette swatch, not seen as a status chip."),
        "sky": color(props["--color-sky"], M_SRC + " --color-sky. Palette swatch, not seen as a status chip."),
        "rose": color(props["--color-rose"], M_SRC + " --color-rose. Palette swatch, not seen as a status chip."),
    },
    "shadow": {
        "button": other(
            "inset 0 1px 0 rgba(255, 255, 255, 0.06), 0 8px 24px -12px rgba(24, 6, 0, 0.4)",
            C_SRC + " header Book a demo computed box-shadow",
        ),
        "menu": other(
            "0 24px 48px -12px rgba(24, 6, 0, 0.22)",
            C_SRC + " product menu card computed box-shadow",
        ),
    },
    "app": {
        "page": color(LOGIN["tokens"]["--background"]["rgb"], L_SRC + " --background"),
        "surface": color(LOGIN["tokens"]["--bg-admin-layout"]["rgb"], L_SRC + " --bg-admin-layout. Login card computed rgb(254, 252, 251)."),
        "text": color(LOGIN["tokens"]["--foreground"]["rgb"], L_SRC + " --foreground"),
        "muted": color(LOGIN["tokens"]["--muted-foreground"]["rgb"], L_SRC + " --muted-foreground"),
        "body": color(LOGIN["tokens"]["--body-text"]["rgb"], L_SRC + " --body-text"),
        "primary": color(LOGIN["tokens"]["--primary"]["rgb"], L_SRC + " --primary. Login submit computed rgb(26, 26, 26)."),
        "primary-foreground": color(LOGIN["tokens"]["--primary-foreground"]["rgb"], L_SRC + " --primary-foreground"),
        "link": color(LOGIN["tokens"]["--brand-accent"]["rgb"], L_SRC + " --brand-accent. Forgot password computed rgb(87, 100, 244)."),
        "border": color(LOGIN["tokens"]["--input"]["rgb"], L_SRC + " --input. Login field border computed rgb(222, 222, 222)."),
        "card-border": color(LOGIN["tokens"]["--mushroom-500"]["rgb"], L_SRC + " --mushroom-500. Login card border computed rgb(215, 210, 208)."),
        "lemon": color(LOGIN["tokens"]["--lemon-300"]["rgb"], L_SRC + " --lemon-300. Logo tile computed rgb(254, 248, 200)."),
        "destructive": color(LOGIN["tokens"]["--destructive"]["rgb"], L_SRC + " --destructive. Declared, not seen on the login form."),
        "success": color(LOGIN["tokens"]["--success"]["rgb"], L_SRC + " --success. Declared, not seen on the login form."),
        "warning": color(LOGIN["tokens"]["--warning"]["rgb"], L_SRC + " --warning. Declared, not seen on the login form."),
        "info": color(LOGIN["tokens"]["--info"]["rgb"], L_SRC + " --info. Declared, not seen on the login form."),
        "radius": dim("8px", L_SRC + " --radius .5rem. Login input and submit computed 8px."),
        "focus": other(
            "0 0 0 2px rgb(255, 255, 255), 0 0 0 4px rgb(26, 26, 26)",
            C_SRC + " login email and password focus box-shadow",
        ),
    },
}

# The hero and footer band on the light marketing page: a group of the light set, not a theme.
# The site has no dark mode, so there is no dark set.
band = {
    "bg": {
        "page": color(props["--color-hero-bg"], M_SRC + " --color-hero-bg. Footer computed rgb(13, 10, 7)."),
        "surface": color(props["--color-hero-surface"], M_SRC + " --color-hero-surface"),
        "surface-2": color(props["--color-hero-surface-2"], M_SRC + " --color-hero-surface-2"),
    },
    "text": {
        "primary": color(props["--color-hero-ink"], M_SRC + " --color-hero-ink. Footer computed rgb(245, 242, 224)."),
        "muted": color(props["--color-hero-ink-muted"], M_SRC + " --color-hero-ink-muted"),
        "subtle": color(props["--color-hero-ink-subtle"], M_SRC + " --color-hero-ink-subtle"),
    },
    "border": {
        "default": color(props["--color-hero-border"], M_SRC + " --color-hero-border"),
        "strong": color(props["--color-hero-border-strong"], M_SRC + " --color-hero-border-strong"),
    },
    "accent": {
        "default": color(props["--color-accent"], M_SRC + " --color-accent. Same lemon, used on the dark footer band."),
        "ink": color(props["--color-accent-ink"], M_SRC + " --color-accent-ink"),
    },
    "$description": "The hero and footer band measured on the light marketing page. Not a theme: the site has no dark mode.",
}
light["band"] = band

doc = {
    "$description": "ShareWillow public marketing (www.sharewillow.com) and signed-out login (app.sharewillow.com/login), measured 2026-11-19.",
    "core": core,
    "light": light,
    "$themes": [
        {"id": "light", "name": "light", "selectedTokenSets": {"core": "enabled", "light": "enabled"}},
    ],
    "$extensions": {
        "notTokenised": [
            "Marketing focus-visible ring was declared (ring-espresso/30, #1806004d) but a real :focus-visible was not forced. Keyboard focus on Product painted the browser outline auto 1px rgb(229, 151, 0).",
            "Login checkbox unchecked fill was not read. The control was already checked.",
            "Signup steps 2 to 6 were not opened. Step 1 asks for a password and shows reCAPTCHA, so the form was not submitted.",
            "Phone sign-in, payment, payroll, and the signed-in app were not entered.",
            "No screenshot was saved. preview_snapshot returned: The browser is not producing screenshot frames.",
            "App colour ramps beyond the roles used on login (earth, emerald, fir, golden-sand, lavender, ocean, rose, rust, terracotta, and the unused steps of espresso, ivory, lemon, mushroom, slate) were declared and not resolved.",
            "Range thumb colour computed accentColor auto. The track height was 8px.",
            "Pressed and hover colours are stylesheet rules (espresso/90, ivory, lemon-deep). They were not read from a hovered element.",
        ]
    },
}



def render():
    """tokens.json's exact text; importing this module writes nothing."""
    return json.dumps(doc, indent=2) + "\n"


if __name__ == "__main__":
    (HERE / "tokens.json").write_text(render())
    print("wrote", HERE / "tokens.json")
