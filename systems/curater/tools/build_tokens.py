#!/usr/bin/env python3
"""Build tokens.json from raw/css-vars.json and raw/components-computed.json.

Read from https://curater.org/ on 2026-11-21, signed out, light only.
Every token carries $extensions.source. Unread values are not invented.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = json.loads((HERE / "raw" / "css-vars.json").read_text())
COMP = json.loads((HERE / "raw" / "components-computed.json").read_text())
C = RAW["computed"]


def src(text):
    return {"$extensions": {"source": text}}


def color(value, source):
    return {"$type": "color", "$value": value, **src(source)}


def dim(value, source):
    return {"$type": "dimension", "$value": value, **src(source)}


def font(value, source):
    return {"$type": "fontFamily", "$value": value, **src(source)}


def number(value, source):
    return {"$type": "number", "$value": value, **src(source)}


def shadow(value, source):
    return {"$type": "shadow", "$value": value, **src(source)}


def other(value, source):
    return {"$type": "other", "$value": value, **src(source)}


def alias(path):
    return "{" + path + "}"


# Brand palette declared as --Curater-* on :root. Relative oklch() values
# that the browser did not resolve to a painted colour stay as declared.
brand = {}
for name, value in C.items():
    if not name.startswith("--Curater-"):
        continue
    key = name.removeprefix("--Curater-")
    brand[key] = color(value, f"css-var {name} on :root, computed")

core = {
    "color": brand,
    "fontFamily": {
        "sans": font(
            "ABCDiatype, -apple-system, system-ui, Segoe UI, Roboto, Oxygen, Ubuntu, Cantarell, Fira Sans, Droid Sans, Helvetica Neue, sans-serif",
            "computed font-family on the Sign in button, home, 1440x900",
        ),
        "sansDeclared": font(C["--font-sans"], "css-var --font-sans on :root; the painted UI uses ABCDiatype instead"),
        "mono": font(C["--font-mono"], "css-var --font-mono on :root; no public code sample was measured"),
    },
    "fontWeight": {
        "regular": number(400, "computed font-weight on body text, home"),
        "medium": number(500, "css-var --font-weight-medium; also the Sign in button"),
        "semibold": number(600, "css-var --font-weight-semibold; not observed on a public control"),
        "bold": number(700, "css-var --font-weight-bold"),
    },
    "fontSize": {
        "xs": dim(C["--text-xs"], "css-var --text-xs"),
        "sm": dim(C["--text-sm"], "css-var --text-sm"),
        "base": dim(C["--text-base"], "css-var --text-base"),
        "lg": dim(C["--text-lg"], "css-var --text-lg"),
        "xl": dim(C["--text-xl"], "css-var --text-xl"),
        "2xl": dim(C["--text-2xl"], "css-var --text-2xl"),
        "3xl": dim(C["--text-3xl"], "css-var --text-3xl"),
        "4xl": dim(C["--text-4xl"], "css-var --text-4xl"),
        "5xl": dim(C["--text-5xl"], "css-var --text-5xl"),
    },
    "lineHeight": {
        "xs": number(C["--text-xs--line-height"], "css-var --text-xs--line-height"),
        "sm": number(C["--text-sm--line-height"], "css-var --text-sm--line-height"),
        "base": number(C["--text-base--line-height"], "css-var --text-base--line-height"),
        "lg": number(C["--text-lg--line-height"], "css-var --text-lg--line-height"),
        "xl": number(C["--text-xl--line-height"], "css-var --text-xl--line-height"),
        "2xl": number(C["--text-2xl--line-height"], "css-var --text-2xl--line-height"),
        "3xl": number(C["--text-3xl--line-height"], "css-var --text-3xl--line-height"),
        "4xl": number(C["--text-4xl--line-height"], "css-var --text-4xl--line-height"),
        "5xl": number(C["--text-5xl--line-height"], "css-var --text-5xl--line-height"),
    },
    "spacing": {
        "1": dim(C["--space-1"], "css-var --space-1"),
        "2": dim(C["--space-2"], "css-var --space-2"),
        "3": dim(C["--space-3"], "css-var --space-3"),
        "4": dim(C["--space-4"], "css-var --space-4"),
        "5": dim(C["--space-5"], "css-var --space-5"),
        "6": dim(C["--space-6"], "css-var --space-6"),
        "8": dim(C["--space-8"], "css-var --space-8"),
        "10": dim(C["--space-10"], "css-var --space-10"),
        "12": dim(C["--space-12"], "css-var --space-12"),
        "unit": dim(C["--spacing"], "css-var --spacing, the 4px base"),
    },
    "radius": {
        "sm": dim(C["--radius-sm"], "css-var --radius-sm"),
        "md": dim(C["--radius-md"], "css-var --radius-md"),
        "default": dim(C["--radius"], "css-var --radius"),
        "lg": dim(C["--radius-lg"], "css-var --radius-lg"),
        "xl": dim(C["--radius-xl"], "css-var --radius-xl"),
        "2xl": dim(C["--radius-2xl"], "css-var --radius-2xl"),
        "full": dim(C["--radius-full"], "css-var --radius-full"),
        "menu": dim("12px", "computed border-radius on [role=menu], settings menu, home"),
    },
    "shadow": {
        "sm": shadow(C["--shadow-sm"], "css-var --shadow-sm"),
        "md": shadow(C["--shadow-md"], "css-var --shadow-md"),
        "lg": shadow(C["--shadow-lg"], "css-var --shadow-lg"),
        "xl": shadow(C["--shadow-xl"], "css-var --shadow-xl"),
    },
    "motion": {
        "durationFast": other(C["--transition-fast"], "css-var --transition-fast"),
        "durationNormal": other(C["--transition-normal"], "css-var --transition-normal"),
        "durationSlow": other(C["--transition-slow"], "css-var --transition-slow"),
        "durationSlower": other(C["--transition-slower"], "css-var --transition-slower"),
        "easeOutExpo": other(C["--ease-out-expo"], "css-var --ease-out-expo"),
        "defaultDuration": other(".15s", "css-var --default-transition-duration on :root"),
        "defaultEasing": other("cubic-bezier(.4,0,.2,1)", "css-var --default-transition-timing-function on :root"),
    },
    "layout": {
        "sidebarWidth": dim(C["--sidebar-width"], "css-var --sidebar-width"),
        "headerHeight": dim(C["--header-height"], "css-var --header-height"),
        "mobileBarHeight": dim(C["--mobile-bar-height"], "css-var --mobile-bar-height"),
        "contentWidth": dim(C["--centered-content-width"], "css-var --centered-content-width"),
        "contentWidthMobile": other(C["--centered-content-width-mobile"], "css-var --centered-content-width-mobile"),
        "containerSm": dim(C["--container-sm"], "css-var --container-sm"),
        "containerMd": dim(C["--container-md"], "css-var --container-md"),
        "container2xl": dim(C["--container-2xl"], "css-var --container-2xl"),
        "container4xl": dim(C["--container-4xl"], "css-var --container-4xl"),
        "container6xl": dim(C["--container-6xl"], "css-var --container-6xl"),
    },
    "z": {
        "base": number(int(C["--z-base"]), "css-var --z-base"),
        "dropdown": number(int(C["--z-dropdown"]), "css-var --z-dropdown"),
        "sticky": number(int(C["--z-sticky"]), "css-var --z-sticky"),
        "fixed": number(int(C["--z-fixed"]), "css-var --z-fixed"),
        "sidebar": number(int(C["--z-sidebar"]), "css-var --z-sidebar"),
        "overlay": number(int(C["--z-overlay"]), "css-var --z-overlay"),
        "modal": number(int(C["--z-modal"]), "css-var --z-modal"),
        "popover": number(int(C["--z-popover"]), "css-var --z-popover"),
        "tooltip": number(int(C["--z-tooltip"]), "css-var --z-tooltip"),
    },
}

light = {
    "page": color(C["--background"], "css-var --background, computed on :root; body paints the same oklch(1 0 0)"),
    "surface": color(C["--card"], "css-var --card"),
    "raised": color(C["--popover"], "css-var --popover; settings menu paints oklch(1 0 0)"),
    "overlay": color("rgba(0, 0, 0, 0.5)", "computed background-color of the sign-in dialog scrim, home"),
    "scrim": color("rgba(0, 0, 0, 0.5)", "same scrim as overlay; one painted value"),
    "text": {
        "primary": color(C["--foreground"], "css-var --foreground"),
        "secondary": color(C["--muted-foreground"], "css-var --muted-foreground"),
        "disabled": other("Not captured", "no disabled text colour was isolated from a painted disabled control"),
        "onAccent": color(C["--primary-foreground"], "css-var --primary-foreground"),
        "link": other("Not captured", "public links paint as foreground; no separate link colour was measured"),
    },
    "border": {
        "default": color(C["--border"], "css-var --border"),
        "strong": color(C["--input"], "css-var --input"),
        "focus": color(C["--ring"], "css-var --ring; a visible focus ring width was not isolated"),
    },
    "accent": {
        "default": color(C["--primary"], "css-var --primary; the filled Search button on phone paints near-black"),
        "hover": other("Not captured", "hover on the pill button did not change its computed background"),
        "pressed": other("Not captured", "a held pressed state was not measured"),
    },
    "status": {
        "success": color(C["--Curater-green"], "css-var --Curater-green"),
        "warning": color(C["--Curater-yellow"], "css-var --Curater-yellow"),
        "danger": color(C["--destructive"], "css-var --destructive"),
        "info": other("Not captured", "no info role was painted on a public page"),
    },
    "sidebar": {
        "background": color(C["--sidebar"], "css-var --sidebar"),
        "foreground": color(C["--sidebar-foreground"], "css-var --sidebar-foreground"),
        "accent": color(C["--sidebar-accent"], "css-var --sidebar-accent"),
        "border": color(C["--sidebar-border"], "css-var --sidebar-border"),
        "width": dim(C["--sidebar-width"], "css-var --sidebar-width"),
    },
    "component": {
        "button": {
            "background": color("oklch(1 0 0)", "computed background-color, Sign in or create account, home"),
            "text": color("oklch(0.141 0.005 285.823)", "computed color, Sign in or create account, home"),
            "border": color("oklch(0.95 0.004 286.32)", "computed border-top-color, Sign in or create account"),
            "borderWidth": dim("1px", "computed border-top-width, Sign in or create account"),
            "radius": dim("9999px", "computed border-radius, Sign in or create account"),
            "height": dim("58px", "computed height, Sign in or create account, 1440x900"),
            "fontSize": dim("16px", "computed font-size, Sign in or create account"),
            "fontWeight": number(500, "computed font-weight, Sign in or create account"),
            "paddingX": dim("24px", "computed padding-left on Continue with Google, /auth/login"),
            "paddingY": dim("16px", "computed padding-top on Continue with Google, /auth/login"),
        },
        "searchButton": {
            "background": color(C["--primary"], "phone Search submit paints a near-black fill; token is --primary"),
            "text": color(C["--primary-foreground"], "css-var --primary-foreground"),
            "radius": dim(C["--radius-full"], "the phone Search button is a full pill; see mobile-home-light-search.png"),
        },
        "menu": {
            "background": color("oklch(1 0 0)", "computed background-color, [role=menu], settings"),
            "radius": dim("12px", "computed border-radius, [role=menu]"),
            "border": color("oklch(0.95 0.004 286.32)", "computed border-top-color, [role=menu]"),
            "padding": dim("4px", "computed padding, [role=menu]"),
        },
        "field": {
            "fontSize": dim("14px", "computed font-size, feed search input"),
            "placeholder": other("Search curations...", "placeholder attribute, feed search input; phone overlay says Type anything"),
        },
        "tab": {
            "height": dim("40px", "computed height, Featured tab, /feed"),
            "fontSize": dim("16px", "computed font-size, Featured tab"),
            "fontWeight": number(500, "computed font-weight, Featured tab"),
        },
    },
}

tokens = {
    "$schema": "https://design-tokens.org/schema.json",
    "core": core,
    "light": light,
    "$themes": [
        {"id": "light", "name": "light", "selectedTokenSets": {"core": "source", "light": "enabled"}}
    ],
    "$extensions": {
        "capture": {
            "product": "Curater",
            "url": "https://curater.org/",
            "date": "2026-11-21",
            "theme": "light only; prefers-color-scheme: dark emulation left body at oklch(1 0 0)",
            "account": "signed-out",
        }
    },
}

out = HERE / "tokens.json"
out.write_text(json.dumps(tokens, indent=2) + "\n")
print("wrote", out, "tokens")
