# Components

Public marketing surface of Figma Weave (`www.weavy.ai`, which redirects to `weave.figma.com`), measured 2026-11-21. The signed-in editor was not opened. Crops are in [components/crops](components/crops). Values come from [raw/component-tokens.json](raw/component-tokens.json).

## Button

The nav call to action (`a.huge_nav-button.is-real`, "Start Now") is 206.3125 by 89.90625 px, fill `rgb(247, 255, 158)`, text `rgb(0, 0, 0)`, type 40px. Hover fill `rgb(37, 37, 37)`, hover text `rgb(244, 244, 244)` ([button-nav-hover.png](components/crops/button-nav-hover.png)). CSS transition is 200 ms, cubic-bezier(0.25, 0.46, 0.45, 0.94).

The plan button (`.button.w-button`, "Start free") is 272.7 by 41.6 px, fill `rgb(37, 37, 37)`, text `rgb(255, 255, 255)`, radius 4px, padding 10.8px 21.6px 10.8px 21.6px. Hover fill `rgb(234, 242, 151)`, hover text `rgb(47, 47, 51)` ([button-plan-hover.png](components/crops/button-plan-hover.png)). Held pointer fill `rgb(247, 255, 158)` ([button-plan-pressed.png](components/crops/button-plan-pressed.png)). Focus outline width computed 0px ([button-plan-focus.png](components/crops/button-plan-focus.png)).

Disabled, loading and error were not on the public pages.

## Link

Nav links (`.nav_text-link`) are 12px, uppercase, letter-spacing 0.15px, `rgb(255, 255, 255)` on the dark nav bar. Hover sets text to `rgb(37, 37, 37)` ([link-hover.png](components/crops/link-hover.png)).

## Text field

The only public field is the knowledge-center search (`input[name=q]`, placeholder "Search for articles..."). Focused, it computed fill `rgb(255, 255, 255)`, text `rgb(26, 26, 26)`, 18px, radius 8px, outline `rgba(0, 0, 0, 0) solid 2px` ([text-field-focus.png](components/crops/text-field-focus.png)). It was not typed into and not submitted.

## Tabs

Audience tabs on pricing (`.audience-tabs_link`) are 140 by 38 px, radius 4 px. Selected fill `#212126`, text white ([tabs-default.png](components/crops/tabs-default.png)). Teams is the unselected tab on the same control.

## Switch

Billing switch (`.billing-toggle_switch`, role=switch) is 32 by 16 px, radius 144 px, fill `#f1fa8c` when annual is on ([switch-default.png](components/crops/switch-default.png)). Clicking it swaps the plan prices to monthly ([switch-selected.png](components/crops/switch-selected.png)).

## Menu

Changelog filters are Webflow dropdowns. Open audience menu: All users, Paid users, Free users, Enterprise, Enterprise & Teams ([menu-open.png](components/crops/menu-open.png)). Open type menu: All update types, New model, Product improvement, Feature release, Pricing update, Model deprecation ([menu-type-open.png](components/crops/menu-type-open.png)). Hover of a menu row is declared as `#fcffdc` and was not separately measured.

## Card

Plan card (`.pricing_plan-v4`) is 316.8 by 487.2 px, fill `rgb(245, 245, 246)`, border `1px solid rgb(230, 230, 230)`, radius 13px, padding 21.0731px 21.0731px 21.0731px 21.0731px ([card-default.png](components/crops/card-default.png)).

## Badge

"Save 30%" (`.billing-toggle_badge`) uses Dmsans, Arial, sans-serif at 13.0003px on `rgb(247, 255, 158)`, radius 2.00016px.

## Table

The models pricing page (`content.weave.figma.com/models-pricing`) shows a public table. Cell styles were not measured. The pricing comparison grid on `/pricing` is a layout, not a `<table>`.

## Not present on the public surface

Icon button, text area, select, checkbox, radio, tooltip, dialog, toast, list row, avatar. The knowledge-center cards show staff avatars; they were not cropped as a component.

## Gaps

- Focus rings computed to 0 px on the buttons that were focused. A visible focus style was not captured.
- Pressed was read by holding the pointer down. It is one frame, not a CSS `:active` rule.
- The signed-in editor, including its light mode, was not reached. See [site-tree.md](site-tree.md).
