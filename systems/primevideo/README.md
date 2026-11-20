# Prime Video design reference

A token set and component reference for Prime Video's public signed-out site, https://www.primevideo.com/. Captured 2026-11-21 in headless Chromium, signed out, at 1440x900 (device pixel ratio 1) and 390x844 (device pixel ratio 2). The homepage redirects to `/offers/nonprimehomepage`. The storefront that loaded prices the trial in the page's own currency. One theme: dark. No account was used.

Prime Video paints a near-black page (`#00050D`), white type in Amazon Ember, and one blue (`#1A98FF`) spent on Join Prime. Hero actions are white pills. Poster cards carry the colour. Signed-in playback, watchlist, profiles and purchases stop at Amazon Sign-In (https://www.amazon.sg/ap/signin). Password was not submitted. No email or mobile number was typed.

This package contains no Prime Video code. Screenshots show the product's pages, including poster artwork, which stays in the images for layout only ([docs/RIGHTS.md](../../docs/RIGHTS.md)). Borrow structure and proportions, not the logo, posters or the blue.

| File | What it is |
|---|---|
| [site-tree.md](site-tree.md) | Which control opens which page, menu, dialog or wall, mapped before the screenshots |
| [icon.png](icon.png) | Site icon, 128 px PNG |
| [tokens.json](tokens.json) | DTCG tokens. `core` holds type, radii, a few sizes and the Fable metrics that resolved. `dark` holds the measured colour roles. No light set. Every token has `$extensions.source` |
| [DESIGN.md](DESIGN.md) | A DESIGN.md-shaped export of the dark tokens. Not `make design-md` output: that command needs a catalog.json entry, and this capture does not edit catalog.json |
| [style-guide.html](style-guide.html) | The tokens rendered. Dark only. Amazon Ember is not loaded |
| [components.md](components.md) | Component inventory with crops and the gaps |
| [patterns.md](patterns.md) | How the shell, home, browse, title, search and help pages combine |
| [components/crops/](components/crops) | 19 element crops, cut from the full-colour captures, then quantised |
| [screenshots/](screenshots) | 37 captures, `{page}-dark-{state}.png`. Desktop 1440x900. `mobile-*` are 780x1688 (390x844 at 2x). `-full` pages are the scrolled page, capped |
| [raw/](raw) | `css-vars.json` (191 resolved custom properties, Fable metrics, no colours), `elements.json`, `capture.json`, `captures/` sidecars with measured viewport size |
| [tools/](tools) | `build_tokens.py`, `build_style_guide.py`, `capture/public.mjs`, `capture/screenshot.mjs`, `capture/quantize.py` |

## Brief

<!-- brief:start -->
<!-- brief:end -->

## Health

<!-- health:start -->
<!-- health:end -->

## How the values were read

Headless Playwright opened the public URLs. `tools/capture/public.mjs` saved screenshots with measured `innerWidth`, `innerHeight` and `devicePixelRatio` in `raw/captures/*.capture.json`. Desktop shots are 1440x900 at 1x. Phone shots are 390x844 at 2x, so the PNGs are 780px wide.

Colour and type came from `getComputedStyle` on named elements, written to [raw/elements.json](raw/elements.json) and the component block of [raw/capture.json](raw/capture.json). Custom properties were harvested from the homepage stylesheets and resolved on `:root` into [raw/css-vars.json](raw/css-vars.json). 191 names resolved. They are `--fable-*` sizes, weights and component metrics. Two `--dva-page-*` names are layout clamps. No colour custom property resolved, so colour tokens are measured computed styles, not aliases of a declared ramp.

Join Prime hover, focus and pressed were read on the live element. Pressed used a mouse-down with the click prevented, so the button did not navigate. Search was opened and left empty.

## What to distrust

- **Amazon Ember is not in the package.** The computed family is Amazon Ember, Amazon Arabic Ember, Arial, sans-serif. The style guide falls back to Arial. Weights 400, 500 and 700 were read on elements. Weight 900 is a declared Fable token and was not seen on a measured control.
- **Join Prime blue is translucent at rest.** Default fill is rgba(26, 152, 255, 0.8). Hover and pressed are opaque `#1A98FF`. A flat `#1A98FF` button is the hover state, not the rest state.
- **White on the blue fails contrast.** White on `#1A98FF` is about 2.6:1. The token keeps the product's value.
- **Muted grey `#999999` on the page** is about 7.4:1 on `#00050D` and passes. It was read on the advisory line, not on a declared muted role.
- **The language menu fill was not isolated.** The measured wrapper was transparent. The crop is the evidence.
- **NC16 badge fill was not isolated.** The crop shows the label. The colour is Not captured.
- **Synopsis line height** in `core.typography.synopsis` uses the body 20px because that node's own line-height was not read. Marked Derived in the source string.
- **Screenshots are 256-colour PNGs.** Read colours from tokens.json.
- **The genre Movies chip click left the page** for `/movie`. That shot was dropped. It is not a filtered genre state.
- **Trailer** showed Video Unavailable. That is the state that loaded, not a player skin.
- **No light theme was offered.** Do not invent one.

## Fonts

Amazon Ember and Amazon Arabic Ember are Amazon's faces. They are not committed. The token fallback is Arial, then sans-serif, which is what the computed stack names after Ember. The style guide uses that fallback.

## Coverage

| Checklist item | Status |
|---|---|
| Colour roles, dark | Captured. Page, nav, search, card, dialog, icon button, selected chip, inverse button, text primary, on-accent, on-inverse, muted, chip text, accent default/hover/pressed, card border, icon-button border, focus outline. [tokens.json](tokens.json) |
| Colour roles, light | Not present. The signed-out site paints one dark page |
| Success, warning, danger, info | Not present on the pages that loaded |
| Type roles | Captured for display, heading, synopsis, body, nav, button, large button, label. Code face not present. [tokens.json](tokens.json) `core.typography` |
| Spacing scale | Not captured as a scale. Four measured paddings are in `core.space`. The rest of the spacing is per component in [components.md](components.md) |
| Radii | Captured: 8px control and poster, 12px card, 24px dialog, 180px chip, circle icon button |
| Border widths | Captured: 1px card, 3px icon button, 2px focus outline |
| Elevation | Captured for the Join Prime glow only. Other shadows were `none` on the measured nodes |
| Motion | Not captured. No duration custom property resolved |
| Sizing | Captured: nav 66px, Join Prime 42px, hero button 62px, chip 39px, icon button 48px, search field 74px. Icon sizes 22/24/33/44px are declared Fable tokens |
| Layout | Captured at 1440 and 390. Content width is the viewport. No published breakpoint list |
| Button | Captured, including hover, focus, pressed on Join Prime. [components.md](components.md) |
| Icon button | Captured default. Other states not captured |
| Link | Observed. No separate link colour |
| Text field | Captured empty search field. Focus, filled, error not captured. Not submitted |
| Text area, select, checkbox, radio, switch | Not present |
| Tabs | Captured: genre chips, Related/Details |
| Menu | Captured: language, account, phone menu |
| Tooltip | Not present |
| Dialog | Captured: Share. Trailer unavailable overlay captured |
| Toast | Not present |
| Card | Captured: poster and detail metadata cards |
| List row | Observed on Help and the language list. No row fill measured |
| Table | Not present |
| Avatar | Not present beyond the generic account glyph |
| Badge | Observed (NC16). Fill not captured |
| App shell | Captured, both widths |
| Form with validation | Not present. Sign-in is a wall |
| Empty, loading, error | Trailer unavailable is the error that loaded. No empty library. Loading not held |
| Destructive confirmation | Not present |
| Feedback after an action | Share dialog. No toast |
| Search and filtering | Search panel captured empty. Genre chips captured. No results page |
| List or table | Poster rows and help lists. No data table |
| Onboarding | Not present signed out |
| Desktop 1440 and phone 390 | Captured. Sidecars in [raw/captures/](raw/captures) record the measured viewport |

## Do and don't

- **Do keep the page near-black and spend blue once.** Join Prime is the only blue control. Everything else is white, grey or artwork. [home-dark-default.png](screenshots/home-dark-default.png).
- **Do make hero actions white pills.** Sign in and the trial button are white on `#00050D`, 62px, 8px radius. [button-signin-default.png](components/crops/button-signin-default.png).
- **Do let posters carry the colour.** Browse pages are rows of 8px-radius stills on the page colour, not tinted cards. [genre-action-dark-default.png](screenshots/genre-action-dark-default.png).
- **Do use Amazon Ember at 400, 500 and 700.** Display is 50/56 bold. Body is 14/20 regular. [heading-hero-default.png](components/crops/heading-hero-default.png).
- **Don't treat the rest-state blue as opaque.** Join Prime at rest is 80% `#1A98FF`. Opaque blue is the hover. [button-join-default.png](components/crops/button-join-default.png), [button-join-hover.png](components/crops/button-join-hover.png).
- **Don't style the player or the signed-in home from this package.** Playback failed closed, and the account wall is Amazon Sign-In. [detail-dark-trailer-unavailable.png](screenshots/detail-dark-trailer-unavailable.png).

## Rebuild

```bash
python3 tools/build_tokens.py
python3 tools/build_style_guide.py
python3 tools/write_design_md.py
```

Run from `systems/primevideo`. Recapture with `PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node tools/capture/public.mjs`. Raw PNGs land in `~/.design-systems/primevideo/raw-shots` and are quantised into `screenshots/` by the same Pillow step the capture notes describe. Do not edit [catalog.json](../../catalog.json) from a capture branch that is not registering the package.
