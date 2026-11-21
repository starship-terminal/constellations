# Dopper design reference

A token set and component reference for Dopper's public web, read on 2026-11-21, signed out, in headless Chromium at 1440 x 900 and 390 x 844. Two hosts share one chrome bar: www.dopper.com (marketing, Next.js) and shop.dopper.com (Magento store). The walk started at https://dopper.com/. Nothing was bought, checked out, signed into, or submitted.

Dopper paints one light theme. The page is warm paper `#fcfaf2`, type is ink `#000f2e` on the shop and black on the marketing body, and the brand blue `#0067e5` fills the home hero, the logo, the current shop link, and Add to cart. Display type is a custom face named Dopper. UI type is Gilroy. Buttons are pills: a black pill and a cream outline on the hero, a blue 20px-radius Add to cart, a green Filters pill.

The public nav has no account sign-in. https://dopper.com/account/login is a not-found page with no form. The shop login form exists only at the Magento URL `https://shop.dopper.com/customer/account/login/`, which the header and footer do not link. That URL is a login wall. The branch stopped there. No checkout wall was reached, because the basket was left empty and checkout was not started.

| File | What it is |
|---|---|
| [icon.png](icon.png) | Site icon, 128 px PNG, resized from www.dopper.com/favicon.ico |
| [tokens.json](tokens.json) | W3C DTCG tokens: `core` (measured colour, type, radius, size) and `light` (role aliases). No dark set. Every token carries `$extensions.source` |
| [DESIGN.md](DESIGN.md) | Stub. `make design-md` needs a catalog.json entry, and this capture was told not to edit catalog.json. Regenerate it after the catalog row lands |
| [style-guide.html](style-guide.html) | One page that renders the measured colours and the hero and add-to-cart buttons |
| [components.md](components.md) | Button, link, menu, language menu, field, filter, card, and the gaps |
| [patterns.md](patterns.md) | How the chrome, hero, shop, collection, product, empty cart, login wall and phone menu fit together |
| [site-tree.md](site-tree.md) | The public tree: which control opens which page or in-page panel, and where the walk stopped |
| [screenshots/](screenshots) | 102 `{page}-light-{state}.png` captures at 1440 and `mobile-*` at 390, quantised to 256 colours |
| [raw/](raw) | [component-tokens.json](raw/component-tokens.json) (the spec the builder reads), [css-vars.json](raw/css-vars.json) (the empty custom-property harvest), and full-colour PNGs in `full/` before quantise |
| [tools/](tools) | `build_tokens.py`, `build_style_guide.py`, `build_components_md.py`, and the capture kit under `capture/` |

## Brief

The generated Brief needs a catalog.json entry. This capture was told not to edit catalog.json, so the section is a stub. After the catalog row is added, run `make brief`.

Read [tokens.json](tokens.json) before designing in this style. Page is `#fcfaf2` (`color.paper`). Text is `#000f2e` (`color.ink`). Accent is `#0067e5` (`color.blue`). Display face is Dopper. UI face is Gilroy.

## Health

The generated Health section needs a catalog.json entry and a scorecard snapshot. This capture was told not to edit catalog.json, so Health is a stub. After the catalog row lands, run `make grade`.

## How the values were read

Everything was read from the running page, signed out, in headless Chromium, on 2026-11-21.

- **Custom properties.** shop.dopper.com's Magento stylesheet (`styles-l.min.css`, theme Dopper/dopper_b2c) declares no `--*` properties. The marketing nav's shadow stylesheet declares only `--line-height` on decorative rules. `raw/css-vars.json` records that empty harvest. `<meta name="theme-color">` is `#fcfaf2`.
- **Computed styles.** Body, h1, shop nav link, add to cart, price, and the shadow nav button were read with `getComputedStyle` at 1440. Add to cart focus-visible was read after a real focus. Hover of add to cart did not change the fill.
- **Sampled, because CSS does not name them.** The Filters pill fill is `#0abeaa` (pixel 10, 190, 170). The filter sheet ground is `#cce2ff` (pixel 204, 226, 255). Both were sampled from the full-colour PNG before quantise. They are marked as such in the token source.
- **What was touched.** Cookiebot was hidden, never accepted. The Bottle menu, the EN language menu, the phone menu, and the shop Filters button were opened. Nothing was added to the basket. No form was filled.

## What to distrust

- **Screenshots are 256-colour PNGs.** Read colours from tokens.json.
- **`color.green` and `light.background.raised` are sampled**, not computed. The pill and the sheet have no custom property.
- **Marketing burst buttons.** The measured wrapper is transparent. The visible black and outline pills are children. Their radius was not read as a computed style. The token `radius.pill` is observed, not measured.
- **Shop submenus** exist in the DOM and stayed `display: none` on hover. The tree lists them. The screenshot does not show them open.
- **No dark theme** was found. Do not invent one.

## Fonts

**Dopper** is the display face on marketing headlines (document.fonts, weight 400). **Gilroy** is the UI face on the shop and on the nav (weights 400, 600, 700). **Dopper-Icons** is named in the shop stylesheet. None of these is a file in this package. The style guide falls back to Georgia and system-ui.

## Coverage

- **Desktop (1440):** home, story, impact, sustainability, blog, a blog post, contact, team, stores, accessibility, product lines (insulated, original, steel, travel mug), tap, tap map, personalise, custom, second life, pledge, schools, events, campaign, legal, privacy, returns, newsletter, retailer, impact calculator, Nepal, not-found, shop home, bottles, mugs, accessories, spare parts, gift card, last chance, one PDP, empty cart, login wall. Open Bottle menu, language menu, and bottle filters.
- **Phone (390):** the same page set, plus the opened marketing menu.
- **Not captured:** signed-in account, checkout, a filled cart, newsletter submit, pressed and loading button states, dark theme (not present).

## Do and don't

1. **Do keep the page on paper, not white.** The ground is `#fcfaf2` `color.paper` on both hosts. See [shop-light-default](screenshots/shop-light-default.png).
2. **Do use one blue.** Hero, logo, current shop link and Add to cart are `#0067e5` `color.blue`. A second blue is wrong. See [home-light-default](screenshots/home-light-default.png).
3. **Do set display type in the Dopper face, cream on blue.** Headlines are cream `#f6ecc8` at 72px on the home hero. UI stays Gilroy. See [story-light-default](screenshots/story-light-default.png).
4. **Do pill the actions.** Add to cart is a 20px radius. The hero primary is a black pill. Filters is a green pill. A sharp rectangle button is wrong. See [pdp-light-default](screenshots/pdp-light-default.png).
5. **Don't add an account link to the public bar.** The bar is Bottle, Travel Mug, Tap, Mission, Get Involved, the wordmark, Impact report, Find a Store, For Businesses, EN, and the cart. Sign-in is a Magento URL the nav does not show. See [home-light-default](screenshots/home-light-default.png).
6. **Don't draw a cart drawer.** The cart icon opens the basket page. See [cart-light-default](screenshots/cart-light-default.png).

## Rebuild

```sh
# from systems/dopper
python3 tools/build_tokens.py
python3 tools/build_style_guide.py
python3 tools/build_components_md.py
python3 tools/capture/quantize.py screenshots
```

`make design-md` and `make brief` need a catalog.json row. This package does not add one.
