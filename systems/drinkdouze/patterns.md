# Douze patterns

How the measured components combine into Douze's public storefront. Every screen is the same grammar: boxed sections at a 45px radius floating on the sable field `#f6f2e9`, 25px of sable air between them, dusk `#301816` ink inside. The screenshots named are in [screenshots/](screenshots); component values in [components.md](components.md).

## Page chrome

Every page opens with two boxed layers ([home-light-default](screenshots/home-light-default.png)):

1. **Announcement bar** — a 1390 x 36.5 sable box (its own 45px radius), Robin Semibold 12px dusk text: "Livraison gratuite en France métropolitaine à partir de 50€ d'achat". Not sticky.
2. **Header** — a 1390 x 57 transparent bar inside its own boxed strip, `z-index` on top of the hero. Left: the nav (`Shop` marked `has-dropdown`, `Notre histoire`, `Nos engagements`, `Recettes` at Robin Semibold 12px, with a 1px dusk `::after` underline that animates on hover). Centre: the DOUZE wordmark (70 x 23 SVG). Right: `Nous trouver`, `S'abonner`, then the account and bag icons with a 15px cart-count bubble. The envelope newsletter toggle exists in the DOM but is `display:none` at desktop.

At 390 the header compresses to a 360 x 65 bar: hamburger left, wordmark centre, bag right. The hamburger opens a from-left `mobile-navigation` drawer — full-height, nav items as `heading h4` rows at 45px each, `Compte` pinned to the bottom ([mobile-home-light-menu](screenshots/mobile-home-light-menu.png)).

## The boxed hero

The home and shop pages lead with an `image-hero` — a 1390 x 550 photo box inside the boxed section ([home-light-default](screenshots/home-light-default.png), [shop-light-default](screenshots/shop-light-default.png)). Text sits on an `image-overlay__text-container` over the media and paints in the inverse roles: the hero headline is Boogy ~72px/1.1 in sable `#f6f2e9` — "Orange Sanguine & Piment : floral, envoûtant et épicé." — with the flavour words in Boogy Italic. The CTA is a small square dusk button (`SHOP`, 67.69 x 44) pinned to the hero's lower edge. The heading node itself is a `hidden-phone`/`hidden-tablet-and-up` pair — different crop per breakpoint, and on the shop page the heading is a wordmark image, not live text.

## The moving banner

Between boxed sections a `.moving-banner` scrolls at 50px high ([home-light-default](screenshots/home-light-default.png) bottom): uppercase Robin Semibold claims — "Sans sucre ajouté · Faible en calories · Ingrédients 100% naturels · Produit en France" — in dusk on sable, divided by 9px dots. It repeats several times down the page as punctuation between sections.

## The shop grid

`/collections/all` ([shop-light-full](screenshots/shop-light-full.png)) is the image-hero band, then a grid of `product-item` cards (398.66 x 498.31 at desktop, ~316 x 395 at 390) inside a white boxed section. Each card is:

- a packshot `aspect-ratio` image area that swaps to a second image on hover,
- `.product-item__title-wrapper` — the flavour name as a **wordmark image** (no live text),
- a pack line — `p.h5`, "6 canettes 25cl, 1 bouteille 75cl",
- `.product-item__quick-form` — `visibility:hidden` until the card is hovered, then a 210 x 44 flavour-accented `Ajouter au panier — 36€` button whose fill re-binds to the card's `--button-background-color` (`#f26554` orange-piment). Its press posts `/cart/add` — measured, never pressed.

A small sort control (71 x 44) sits over the grid; the catalogue is one page, so no pagination paints. Search results reuse the same card grid at a smaller ~229 x 286 size ([search-light-full](screenshots/search-light-full.png)).

## The buy box

The product page splits the boxed section in two ([product-light-default](screenshots/product-light-default.png)): a 695 x 810 media gallery left (packshots plus thumbs) and the buy column right:

1. Boogy product title ~60px ("Orange Sanguine & Piment", 403 x 80) with the sub-line "Canette 25cl",
2. the Klaviyo star rating row (★★★★★ dusk stars, "13 avis"),
3. a Robin paragraph of tasting notes,
4. `Quantité` pack-size `block-swatch` radios — 106–114 x 36 pill chips (999px radius), 1px dusk border; the checked one fills with the flavour accent `#f26554` under dusk text ([product-light-variant](screenshots/product-light-variant.png)),
5. purchase-option radios (`Achat unique` / `Abonnement −10%` with struck prices) that render once a pack size is settled — a vendor widget never toggled,
6. the 380 x 44 dusk submit "Ajouter au panier — 21€" and the "Acheter en 1-clic" button below it — both measured, never pressed,
7. a `.product-info__reassurance` column — "Livraison à J+2 et gratuite à partir de 50€", "−10% en s'inscrivant à la newsletter" — dusk text with a flavour-coloured divider,
8. further down, the Klaviyo reviews widget (`kl_reviews` tabs and the only native `<select>` on the surface, its sort control at 152 x 36) painted in the theme's chrome.

The bundle page (`/products/trio-douze`) is the same buy box around the trio product ([trio-light-default](screenshots/trio-light-default.png)).

## Content pages

The editorial pages keep the same frame: boxed sections over sable, a Boogy h1 at ~52–104px ([story-light-full](screenshots/story-light-full.png)), Robin paragraphs ("Le mode de vie méditerranéen…"), and image-with-text blocks alternating media and prose inside their own boxes. The FAQ page is a stub: a title and `details`-style disclosure rows (632 x 57) with animated-plus markers ([faq-light-full](screenshots/faq-light-full.png)). Store locator, Abonnement, Parrainage and the recipes blog/article are the same section grammar ([locator-light-full](screenshots/locator-light-full.png), [recipes-light-full](screenshots/recipes-light-full.png)).

## Account and cart — the boundary surfaces

- **Login** ([login-light-default](screenshots/login-light-default.png)): a centred 480 x 482 sable card at 45px radius with 44/48px padding — "Se connecter" in Boogy, two 384 x 52 fields with floating labels (E-mail, Mot de passe), the "Mot de passe oublié ?" text button that swaps the card to the recover form in place, a 384 x 44 dusk `Se connecter` submit, then `S'inscrire` and `Gérer mon abonnement` links. Measured, filled once and emptied, never submitted.
- **Cart** ([cart-light-default](screenshots/cart-light-default.png), [cart-light-full](screenshots/cart-light-full.png)): the empty state — "Votre panier est vide" with an `Explorer nos produits` button — the only cart surface reachable without adding an item.
- **Mini-cart drawer** ([home-light-cart-drawer](screenshots/home-light-cart-drawer.png)): the bag icon opens the same empty state as a right-side drawer over a dimmed page — the only drawer captured, since the newsletter drawer's toggle is hidden at both widths.

## Footer

The footer is a boxed section over a photo field ([home-light-full](screenshots/home-light-full.png) bottom): nav link columns (Shop, Notre histoire, Engagements, Compte, FAQ, Parrainage, the legal pages) in inverse sable-on-media, the "La News Douze" Klaviyo embed — a 450 x 34 email field and a 32 x 34 submit, measured never filled — and the `Français` locale button (110 x 26). No social links paint.

## Motion

- Buttons, swatches, links and drawers run `0.2s ease`/`ease-in-out` transitions on background, colour, box-shadow and transform; the nav underline is a scaled `::after`.
- The moving banner animates continuously (its `transform` is the reduced-motion probe's target).
- The mobile drawer opens on a 0.6s `cubic-bezier(0.75, 0, 0.175, 1)` transform+visibility transition.
- The quick-add reveal is `visibility`/`opacity`, not a drawer — hover the card and the form is simply there.

## What never painted

The Shop dropdown panel, the newsletter drawer (toggle hidden), the Klaviyo popup, pagination, social icons, sold-out/disabled/error states, and everything past a purchase or a login — checkout, filled cart, account, subscription management. The `/en` locale duplicates the surface.
