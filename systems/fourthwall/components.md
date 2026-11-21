# Fourthwall components

Measured on fourthwall.com on 2026-11-21, signed out, desktop 1440, deviceScaleFactor 2 for crops. Nothing was typed, submitted, or signed into. Link press was not forced, because mouse-down navigates away. The full readings are in [raw/components-computed.json](raw/components-computed.json).

Crops are in [components/crops/](components/crops) (26 files). Page shots are in [screenshots/](screenshots). The control map is in [site-tree.md](site-tree.md).

## Discovery list

| Surface | URL | Screenshots |
|---|---|---|
| Home, header, hero, product rail | `/` | [home](screenshots/home-default.png), [phone](screenshots/mobile-home-default.png) |
| Features menu open | `/` hover on Features | [features](screenshots/home-menu-features.png), [phone accordion](screenshots/mobile-home-menu-features.png) |
| Learn menu open | `/` hover on Learn | [learn](screenshots/home-menu-learn.png), [phone accordion](screenshots/mobile-home-menu-learn.png) |
| Phone burger | `/` at 390 | [menu](screenshots/mobile-home-menu.png) |
| Search page, empty | `/search` | [search](screenshots/home-search.png), [search-default](screenshots/search-default.png) |
| Pricing | `/pricing` | [pricing](screenshots/pricing-default.png) |
| Auth login wall | Keycloak via the Log in href | [desktop](screenshots/auth-login-desktop.png), [phone](screenshots/auth-login-mobile.png) |
| Auth registration wall | `/get-started` | [desktop](screenshots/get-started-default.png), [phone](screenshots/mobile-get-started-default.png) |

Generated templates (`/make-your-own/*`, `/blog/*`, `/design-and-sell/*`, `/compare/*`) were sampled, not enumerated. See [site-tree.md](site-tree.md).

## Shared values

**Type.** Suisse Intl. Nav and the hero button: 16.9995px, weight 450, line-height 28.0492px. Footer links: 16.9995px, weight 400, colour `rgba(255, 255, 255, 0.5)` on ink `#0a0a0a`. Hero heading: 57.6px, weight 420, paper on the dark hero.

**Radius.** Hero button 12px (`core.radius.lg`). Search field on `/search` measured 0. The small text-field reading (64px) is a different control and is not the search spec.

**Hover.** Computed colour did not change on button, nav link, login link, footer link, menu link, text field or search field. A hover the script missed is Not captured.

**Focus.** Links: outline 1px, `rgb(0, 95, 204)`, offset 1px. That colour is not a declared token. Status: Not captured. Search field and the small text field painted no outline.

**Pressed.** Not captured. `button-pressed.png` is an earlier crop with the same paint as default. The finished JSON has no pressed state.

## Components

### Button

Hero and header Start now. Selector `.btn-primary`. 117x43. Fill `rgb(255, 255, 255)`, text `rgb(10, 10, 10)`, radius 12px, padding 12px 20px, shadow none. Computed text included a hidden duplicate ("Start now Start now"). The crop shows the visible label.

This is not the declared action fill. `--_surface---bg--action` is ink `#0a0a0a` with paper text. The auth wall Log in button shows that pair. See [auth-login-desktop.png](screenshots/auth-login-desktop.png).

| State | Crop | What changed |
|---|---|---|
| default | [button-default](components/crops/button-default.png) | white pill, ink text |
| hover | [button-hover](components/crops/button-hover.png) | computed paint unchanged |
| focus-visible | [button-focus-visible](components/crops/button-focus-visible.png) | 1px outline `rgb(0, 95, 204)`, offset 1px |
| pressed | [button-pressed](components/crops/button-pressed.png) | Not captured. Crop matches default. |

### Nav link

Features, in the desktop bar. 90x36. Paper text, transparent fill, weight 450, radius 0. Hover unchanged. Focus paints the same 1px blue outline.

Crops: [default](components/crops/nav-link-default.png), [hover](components/crops/nav-link-hover.png), [focus](components/crops/nav-link-focus-visible.png).

### Login link

Log in. 49x36. Same type as the nav link. Opens the Keycloak wall. Not clicked during measurement.

Crops: [default](components/crops/login-link-default.png), [hover](components/crops/login-link-hover.png), [focus](components/crops/login-link-focus-visible.png).

### Menu link

Product catalog inside the open Features menu. 126x28. Paper, weight 400. Hover unchanged. Focus paints the 1px outline.

Crops: [default](components/crops/menu-link-default.png), [hover](components/crops/menu-link-hover.png), [focus](components/crops/menu-link-focus-visible.png). The open menu itself is [menu-default](components/crops/menu-default.png) and the page shot [home-menu-features](screenshots/home-menu-features.png).

### Footer link

Product catalog in the footer. 126x28. Colour `rgba(255, 255, 255, 0.5)`, weight 400, on footer fill `#0a0a0a`.

Crops: [default](components/crops/footer-link-default.png), [hover](components/crops/footer-link-hover.png), [focus](components/crops/footer-link-focus-visible.png).

### Nav and footer

Nav bar: 1440x71, transparent (the hero behind it is ink). Crop: [nav-default](components/crops/nav-default.png).

Footer: 1440x362, fill `#0a0a0a`, text at 50% paper. No separate footer crop beyond the link crops. The home shot shows the bar; scroll the full page shots for the footer columns listed in [site-tree.md](site-tree.md).

### Heading and body

Hero heading: 1028x181, 57.6px, weight 420, paper. Crop: [heading-default](components/crops/heading-default.png).

A body sample measured 300x49, 17px, weight 400, `rgba(255, 255, 255, 0.5)`. No crop. On paper pages the declared body colour is ink `#0a0a0a`.

### Search field

`/search`, empty, not submitted. 940x38. Fill white, text `rgb(51, 51, 51)`, 14px, weight 400, radius 0, placeholder "Search…". Hover and focus-visible did not paint an outline.

Crops: [default](components/crops/search-field-default.png), [hover](components/crops/search-field-hover.png), [focus](components/crops/search-field-focus-visible.png). Page: [home-search](screenshots/home-search.png).

The Search button on that page is a blue control in the screenshot. Its fill was not read into a token. Status: Not captured. Do not sample it from the quantized PNG.

### Text field

A 52x23 control, radius 64px, measured on the home page. It is not the search field and not the auth email field. Do not use it as the form-field spec. Auth fields were photographed and not measured, because the branch stopped at the empty wall.

Crops: [default](components/crops/text-field-default.png), [hover](components/crops/text-field-hover.png), [focus](components/crops/text-field-focus-visible.png).

### Accordion

The desktop measurement matched a hidden burger (`Open menu`, 0x0). Phone accordions were photographed, not measured: [features](screenshots/mobile-home-menu-features.png), [learn](screenshots/mobile-home-menu-learn.png).

### Auth wall

Registration wall fields were listed, not filled: Sign up with Google, Sign up with Apple, Sign up with email, Login, Terms, Privacy Policy. Crop: [auth-wall-default](components/crops/auth-wall-default.png). The login wall is the page shots, not a filled form. See [login-review.json](login-review.json).

## Gaps

- Signed-in app was not captured.
- Unread token values are Not captured.
- Pressed, disabled, error and loading states were not captured.
- Checkbox, radio, select, switch, toast, tooltip, table, avatar and dialog were not measured on the marketing pages.
- Onboarding, checkout, newsletter, plan and survey fields were not filled.
