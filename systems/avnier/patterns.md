# Avnier patterns

How the measured components combine on each public surface of avnier.com (signed out, 1440 x 900 and 390 x 844, fr-FR). Values are in [tokens.json](tokens.json); the per-state measurements in [raw/measurements.md](raw/measurements.md).

## Chrome: the header

The header is a 60px white bar (`header`, 50.9px on mobile) with a `background-color` transition — it paints its own state, not a shadow. Left: the `avnier` wordmark (`logo`, 155x38.5). Middle: the mega-menu row — SHOP, MARQUE, then the plain `.mega-menu__item-link` anchors SECONDE MAIN and ARCHIVE SALE (`nav-item`, 95.5x20, 13px Space Mono uppercase). Right: 40x40 icon targets — search (`search-toggle`), CONNEXION (`account-link`), PANIER (`cart-link`) — icon-only, white-on-transparent over the bar.

The SHOP item is a `.mega-menu__item` whose dropdown opens on hover; the visible dropdown was not captured on this pass (see [components.md](components.md) `nav-dropdown`, recorded missing). The keyboard route in is the skip link: `skip-link` is off-screen until focused, then a 347x45 black rectangle — the same black action style as the buy button.

At 390px the bar collapses to wordmark + `m-menu-button` (35x30) + cart. The button opens the side drawer (`m-menu-open`); rows inside it are `m-nav-link` (`.toggle-item__header`, ~59px tall full-width rows; the social icons at the drawer's foot are `.list-social__link`). The open drawer is [mobile-home-light-menu](screenshots/mobile-home-light-menu.png).

## Product surfaces

The shop grid (`/collections/tous-les-produits`) opens with the count (`plp-title`, "100 PRODUITS" in the #7a7a7a muted grey), the facet row — PRIX, COULEUR, TAILLE, TYPE DE PRODUIT disclosures (`facet`, 75x36 summary) whose options are 16px `facet-checkbox` inputs — and the Recommandés sort (`sort-select`, 166x21, dimmed rgba(0,0,0,.75) label).

Cards (`product-card`, 450x562.5 at 1440 — three across inside the 160rem page width) are borderless image+text rows: `card-name` (13px uppercase Space Mono) over `card-price` (12px, 1px tracking). No box, no shadow, no border — the product photo is the card.

## PDP

A product page (whichever the grid lists first — `pdp_url`) stacks a 440px column: `pdp-title` (avnier-font, 15px, 500, uppercase), `pdp-price` (18px Space Mono, 1.3px), the TAILLE chip row — `variant-radio` is the visible black-chip label of a visually hidden `input[type=radio]` (73.2x40, white on black when checked) — and `add-to-cart` (440x48 black, #f6f6f6 label, 15px uppercase, 1px tracking). This product had no quantity input or disclosure accordions; both are recorded absent, not missing.

## Cart and login

`/cart` is a 404 — avnier's cart is the **side-cart drawer** `cart-drawer` (`.side-cart__wrapper`), opened by the header's PANIER link (JS intercepts the `/cart` href). Signed out it holds `cart-empty` ("LE PANIER EST VIDE") under its `side-cart__title` ("MON PANIER - 0 ARTICLE"). The 404 page itself is recorded as `cart-page`/`cart-title`. Login is a 448px column: `login-title` (220px display), `email-input` and `password-input` (448x45, transparent fill, 16px uppercase — their 1px border is painted as a `rgba(0,0,0,.55)` box-shadow ring, not a border), and `login-button` (153.6x48 black). The form was never submitted.

## Buttons and controls

One visual language: a black 0px-radius rectangle carrying a near-white (#fff/#f6f6f6) 15px uppercase Space Mono label at 1px tracking — `add-to-cart`, `login-button`, `cart-cta`, `skip-link` all share it (48px tall; the skip link is narrower). Hover keeps the shape — Avnier answers hover with fill swaps, not scale or shadow. Fields are 45px transparent boxes with the shadow ring. Checkboxes are native 16px squares. Focus is a `focus-visible` outline on the element itself.

## Mobile

The same surfaces recompose at 390x844: header to `m-header`, nav to the drawer (`m-menu-open`, `m-nav-link` rows), cards to full-width `m-feature-tile` (390x390) rows. The shop grid stacks cards one across.

## Consent and popups

Two overlays arrive unsigned-in: the Axeptio consent SDK and the shipping-country popup (the country `<select>`, 237 options). Both are captured first — [home-light-consent](screenshots/home-light-consent.png) — then hidden, never answered: no Accept/Reject is ever clicked anywhere in the capture.
