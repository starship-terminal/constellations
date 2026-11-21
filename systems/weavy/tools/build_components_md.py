#!/usr/bin/env python3
"""Rewrite components.md from the measured readings. Does not invent unread states."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
C = json.loads((HERE / "raw" / "component-tokens.json").read_text())
home = C["home"]
pricing = C["pricing"]["pricing"]

lines = []


def W(text=""):
    lines.append(text)


W("# Components")
W()
W("Public marketing surface of Figma Weave (`www.weavy.ai`, which redirects to `weave.figma.com`), measured 2026-11-21. The signed-in editor was not opened. Crops are in [components/crops](components/crops). Values come from [raw/component-tokens.json](raw/component-tokens.json).")
W()
W("## Button")
W()
cta = home["ctaDefault"]
W(f"The nav call to action (`a.huge_nav-button.is-real`, \"Start Now\") is {cta['rect']['w']} by {cta['rect']['h']} px, fill `{cta['bg']}`, text `{cta['color']}`, type {cta['fontSize']}. Hover fill `{home['ctaHover']['bg']}`, hover text `{home['ctaHover']['color']}` ([button-nav-hover.png](components/crops/button-nav-hover.png)). CSS transition is 200 ms, cubic-bezier(0.25, 0.46, 0.45, 0.94).")
W()
btn = pricing["btn"]
hover = C["pricing"]["btnHover"]
pressed = C["pricing"]["btnPressed"]
W(f"The plan button (`.button.w-button`, \"Start free\") is {btn['rect']['w']} by {btn['rect']['h']} px, fill `{btn['bg']}`, text `{btn['color']}`, radius {btn['radius']}, padding {btn['padding']}. Hover fill `{hover['bg']}`, hover text `{hover['color']}` ([button-plan-hover.png](components/crops/button-plan-hover.png)). Held pointer fill `{pressed['bg']}` ([button-plan-pressed.png](components/crops/button-plan-pressed.png)). Focus outline width computed {C['pricing']['btnFocus']['outlineWidth']} ([button-plan-focus.png](components/crops/button-plan-focus.png)).")
W()
W("Disabled, loading and error were not on the public pages.")
W()
W("## Link")
W()
link = home["linkDefault"]
W(f"Nav links (`.nav_text-link`) are {link['fontSize']}, {link['textTransform']}, letter-spacing {link['letterSpacing']}, `{link['color']}` on the dark nav bar. Hover sets text to `{home['linkHover']['color']}` ([link-hover.png](components/crops/link-hover.png)).")
W()
W("## Text field")
W()
search = C["help"]["search"]
W(f"The only public field is the knowledge-center search (`input[name=q]`, placeholder \"{search['placeholder']}\"). Focused, it computed fill `{search['bg']}`, text `{search['color']}`, {search['fontSize']}, radius {search['radius']}, outline `{search['outline']}` ([text-field-focus.png](components/crops/text-field-focus.png)). It was not typed into and not submitted.")
W()
W("## Tabs")
W()
W("Audience tabs on pricing (`.audience-tabs_link`) are 140 by 38 px, radius 4 px. Selected fill `#212126`, text white ([tabs-default.png](components/crops/tabs-default.png)). Teams is the unselected tab on the same control.")
W()
W("## Switch")
W()
W("Billing switch (`.billing-toggle_switch`, role=switch) is 32 by 16 px, radius 144 px, fill `#f1fa8c` when annual is on ([switch-default.png](components/crops/switch-default.png)). Clicking it swaps the plan prices to monthly ([switch-selected.png](components/crops/switch-selected.png)).")
W()
W("## Menu")
W()
W("Changelog filters are Webflow dropdowns. Open audience menu: All users, Paid users, Free users, Enterprise, Enterprise & Teams ([menu-open.png](components/crops/menu-open.png)). Open type menu: All update types, New model, Product improvement, Feature release, Pricing update, Model deprecation ([menu-type-open.png](components/crops/menu-type-open.png)). Hover of a menu row is declared as `#fcffdc` and was not separately measured.")
W()
W("## Card")
W()
plan = pricing["plan"]
W(f"Plan card (`.pricing_plan-v4`) is {plan['rect']['w']} by {plan['rect']['h']} px, fill `{plan['bg']}`, border `{plan['border']}`, radius {plan['radius']}, padding {plan['padding']} ([card-default.png](components/crops/card-default.png)).")
W()
W("## Badge")
W()
badge = pricing["badge"]
W(f"\"Save 30%\" (`.billing-toggle_badge`) uses {badge['fontFamily']} at {badge['fontSize']} on `{badge['bg']}`, radius {badge['radius']}.")
W()
W("## Table")
W()
W("The models pricing page (`content.weave.figma.com/models-pricing`) shows a public table. Cell styles were not measured. The pricing comparison grid on `/pricing` is a layout, not a `<table>`.")
W()
W("## Not present on the public surface")
W()
W("Icon button, text area, select, checkbox, radio, tooltip, dialog, toast, list row, avatar. The knowledge-center cards show staff avatars; they were not cropped as a component.")
W()
W("## Gaps")
W()
W("- Focus rings computed to 0 px on the buttons that were focused. A visible focus style was not captured.")
W("- Pressed was read by holding the pointer down. It is one frame, not a CSS `:active` rule.")
W("- The signed-in editor, including its light mode, was not reached. See [site-tree.md](site-tree.md).")
W()

(HERE / "components.md").write_text("\n".join(lines))
print("wrote components.md")
