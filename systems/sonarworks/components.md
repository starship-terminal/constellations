# Sonarworks components

Public marketing site at www.sonarworks.com, captured 2026-11-21, signed out, light only. Desktop 1440×900 at 1x. Phone 390×844 at 2x. Computed styles are in [raw/components-computed.json](raw/components-computed.json). Crops are in [components/crops/](components/crops).

Nothing was submitted. CookieScript and GetSiteControl were removed from the DOM, never clicked. Login was opened and not filled. Facebook, Google and Apple were not clicked.

## Discovery

The control map is [site-tree.md](site-tree.md). Screenshots are `{page}-light-{state}.png`.

| Surface | URL | Screenshot |
|---|---|---|
| Home, company menu, product bar | `/` | [home-light-default](screenshots/home-light-default.png), [home-light-company-menu](screenshots/home-light-company-menu.png), [home-light-product-menu](screenshots/home-light-product-menu.png) |
| SoundID Reference | `/soundid-reference` | [reference-light-default](screenshots/reference-light-default.png) |
| VM PRO | `/soundid-vm-pro` | [vm-pro-light-default](screenshots/vm-pro-light-default.png) |
| VoiceAI | `/soundid-produce/voiceai` | [voiceai-light-default](screenshots/voiceai-light-default.png) |
| SoundID app | `/soundid` | [soundid-light-default](screenshots/soundid-light-default.png) |
| Pricing (redirects) | `/soundid-reference/pricing` lands on `/black-friday` | [pricing-light-default](screenshots/pricing-light-default.png) |
| Download center | `/download-center` | [download-center-light-default](screenshots/download-center-light-default.png) |
| Blog, reviews, company, contacts, legal | footer and top bar | matching `{page}-light-default.png` |
| Login wall | `/account/login` | [login-light-wall](screenshots/login-light-wall.png) |
| Store, empty cart | store.sonarworks.com | [store-light-default](screenshots/store-light-default.png), [cart-light-default](screenshots/cart-light-default.png) |
| Phone home and menu | `/` at 390 | [mobile-home-light-default](screenshots/mobile-home-light-default.png), [mobile-home-light-menu](screenshots/mobile-home-light-menu.png) |

## Components

### Top link

Reviews in the black utility bar. Transparent fill, Inter 16/24 400, color `#96999c` (`core.color.base.60`). Padding 8px 16px. Height 40. Radius 0. Crop: [top-link-default](components/crops/top-link-default.png).

### Primary tab

Product tab in `#primary-navigation`. Transparent fill, Inter 16/24 400, color `#96999c`. Height 104 at 1440. Hover and keyboard focus both paint background `#1e1f20` (`core.color.base.10`). Crops: [primary-tab-default](components/crops/primary-tab-default.png), [primary-tab-hover](components/crops/primary-tab-hover.png).

### Wordmark

"Sonarworks" link. Inter 16/24 600, color `#ffffff` (`light.text.on-inverse`).

### Hero title

Home `h1`. Inter 44/52 400, color `#000000`, letter-spacing -1.5px. Token `core.typography.display`.

### Section title

First home `h2` sits on a photo and computes color `#ffffff`, Inter 24/32 400, letter-spacing -0.5px. That white is the on-image treatment, not the page text role.

### Learn more

Pill CTA. Background `#ffffff`, color `#000000`, radius 9999px (`core.radius.full`), height 32. The home page also paints a black pill on the light card. Both are visible in [home-light-default](screenshots/home-light-default.png).

### Company menu

Hover on Company. Panel class `bg-base-10` (`#1e1f20`). Items are white Inter 16. Screenshot: [home-light-company-menu](screenshots/home-light-company-menu.png). The item crop missed because the panel's first link reported height 0 while the panel itself was visible.

### Footer link

About Us. Inter 16/24 400, color `#ffffff` on the black footer. Height 88 including the footer cell.

### FAQ

`<details>` on `/soundid-reference`. Summary Inter 16/24 400, color `#000000`, height 96. Open state was set in the DOM. Crop of the closed summary failed (clip outside the viewport after scroll). The open reading is in raw/components-computed.json under `faq-open`.

### Contact field

On `/company/contacts`. Background `#000000`, color `#f3f3f3`, radius 4px (`core.radius.md`), height 34. Label "Email *" is `#d8d9da` (`core.color.base.85`). Not typed. Not submitted. Crop: [field-default](components/crops/field-default.png).

### Send

The first button on the contact page is Cancel: transparent fill, white text, radius 9999px, height 66. Send the message was not clicked.

### Login field

Email field on the wall. Background `#ffffff`, color `#000000`, height 48, radius 0. Empty placeholder only. Crop: [login-field-default](components/crops/login-field-default.png).

## Shared values

| Role | Value | Token |
|---|---|---|
| Page | `#ffffff` | `light.surface.page` |
| Header | `#000000` | `light.surface.inverse` |
| Muted nav text | `#96999c` | `light.text.muted` |
| Menu panel | `#1e1f20` | `light.surface.menu` |
| Body type | Inter 16/24 400 | `core.typography.body` |
| Display | Inter 44/52 400, -1.5px | `core.typography.display` |
| Pill radius | 9999px | `core.radius.full` |
| Field radius | 4px | `core.radius.md` |

## Gaps

| Item | Status |
|---|---|
| Text area, select, checkbox, radio, switch | Not captured as distinct controls. Pricing checkboxes exist on `/black-friday` and were not measured. |
| Tabs | Not present as a tab widget. Product nav is hover bars. |
| Tooltip, toast, dialog (product) | Cookie dialog was hidden, not captured as a component. No product dialog was opened. |
| Table, avatar, badge | No avatar or table on the public shell. "Badge" crop is the same pill as Learn more. |
| Disabled, loading, error | Not present on the pages measured. Login submit looks muted in the screenshot. Its computed disabled style was not read (the button selector missed it). |
| Pressed | Not captured. CDP pressed was not run. |
| Focus ring colour | `--tw-ring-color` is declared. A painted focus ring on `:focus-visible` was not confirmed. Primary-tab focus matched hover (`#1e1f20`). |
| Dark theme | Not present. |
| Signed-in app, checkout, support center | Not captured. Login wall stops the account branch. Support is a Cloudflare challenge. |
| Icon set | Not extracted. Glyphs stay in screenshots. |
| Hover on Learn more, footer link, field | Not captured. |
