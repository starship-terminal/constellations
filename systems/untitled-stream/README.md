# untitled.stream design reference

A token set and component reference for untitled (untitled.stream), a music collaboration product. The public site was refreshed on 2026-11-22, signed out, in headless Chromium. Desktop shots are 1440 by 900 at 1x. Phone shots are 390 by 844 CSS pixels at 2x. `catalog.json` was left alone. `login-extracted` stays `not-started`.

The marketing site follows the browser colour scheme. Light paints a white page and a black Enter App pill. Dark paints `#191919` and a white pill. Both are the public site. The signed-in app was not opened.

Nothing was typed. No identity provider was clicked. No form was submitted. No captcha was solved. No email, password, code, phone, address, or recovery phrase was entered. Add to Cart and Checkout were not clicked. Subscribe was not followed.

| File | What it is |
|---|---|
| [icon.png](icon.png) | Product icon, 128 px, resized from the public apple-touch icon |
| [site-tree.md](site-tree.md) | Which public controls open which pages, drawers, and walls |
| [login-review.json](login-review.json) | Empty-wall probe. `login_extracted` is `not-started` |
| [tokens.json](tokens.json) | Hand-written DTCG tokens from the live CSS and computed styles |
| [DESIGN.md](DESIGN.md) | Hand-written short export. Not produced by `make design-md` |
| [style-guide.html](style-guide.html) | Token swatches for both public themes |
| [components.md](components.md) | Public controls and the states that were on the page |
| [patterns.md](patterns.md) | How those controls combine on the public pages |
| [screenshots/](screenshots) | 256-colour page shots. Read colours from [tokens.json](tokens.json) |
| [raw/css-vars.json](raw/css-vars.json) | Declared custom properties and a dark computed sample |
| [tools/](tools) | Capture kit. Do not run `make brief`, `make grade`, or `make design-md` for this refresh: those rewrite the catalog |

## Brief

Hand-written for this refresh. `make brief` was not run, because it rewrites `catalog.json`.

Read this before designing in this style. Take every value from [tokens.json](tokens.json). The screenshots are 256-colour PNGs.

### Principles

1. Bracket the chrome: `[shop]`, `[membership]`, `[starter]`.
2. Keep one filled pill for the primary action. Black on light, white on dark.
3. Pin a frosted pill bar over the disc hero.
4. Set display type in Untitled Sans at 26px with tracking -0.78px.
5. Let the discs carry the colour. The page itself stays black, white, and gray.
6. Follow the browser colour scheme. Both public themes are live.

### Using tokens

| Role | light | dark |
|---|---|---|
| page | #ffffff | #191919 |
| surface | #f2f2f2 | #202020 |
| text | #191919 | #ffffff |
| muted | #7e7e7e | #7e7e7e |
| action | #242424 to #101010 | #ffffff |
| on action | #ffffff | #191919 |

Fonts: Untitled Sans, then IBM Plex Mono. Plex Mono is loaded and was not used on the measured marketing controls.

### Using components

[components.md](components.md) lists the public controls. [patterns.md](patterns.md) says how they combine. [site-tree.md](site-tree.md) maps the routes.

### Accessibility

Muted gray `#7e7e7e` on white and on `#191919` is the footer colour. This pass did not recompute contrast pairs, and it did not hold keyboard focus for a crop. The earlier public pass found no painted focus ring.

## Health

Hand-written. `make grade` was not run, because it rewrites `catalog.json`.

This refresh covers the public homepage, pricing, trust, shop, one product page, an empty cart, terms, phone homepage, phone pricing, and the empty welcome, sign-up, and sign-in walls. Text fields, menus, toasts, tables, and avatars were not on those pages. Email, phone, QR, and recovery steps were not opened.

## Where this pass stopped

`/login` redirects to `/welcome`. That gate asks for Create account or I have an account, with no fields. Create account opens `/sign-up` (Apple, Google, Email, device only). I have an account opens `/sign-in` (QR Code, Apple, Google, Email, Phone, Recovery Phrase). Those buttons were not clicked. The signed-in app was not opened.
