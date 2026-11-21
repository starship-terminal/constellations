# Component measurements

Computed styles read from avnier.com on 2026-11-21 by `tools/capture/public/measure.mjs`, signed out, in headless Chrome at 1440 x 900 (the Mobile group at 390 x 844) in the site's one light theme, across `avnier.com/`, `avnier.com/account/login`, `avnier.com/cart`, `avnier.com/collections/tous-les-produits`, `avnier.com/products/doudoune-symphony`, with the Axeptio consent layer and the shipping-country popup hidden (never answered), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### skip-link

Skip link. "IGNORER ET PASSER AU CONTENU" — off-screen until focused.

Page: home. Selector: `a:has-text("IGNORER")`. States: default, focus-visible.

| Property | default | focus-visible |
|---|---|---|
| Size (w x h) | 120 x 45 | 347.05 x 45 |
| Padding | 9px 30px 11px 30px | = |
| Border | 1px solid #000000 @ 0 | = |
| Radius | 0px | = |
| Background | #000000 | = |
| Box shadow | #000000 0px 0px 0px 1px | #000000 0px 0px 0px 1px, #ffffff 0px 0px 0px 3px, #000000 @ 0.3 0px 0px 5px 4px |
| Outline | none | = |
| Font | Space Mono 15px/18px 400 | = |
| Letter spacing | 1px | = |
| Colour | #ffffff | = |
| Transition | box-shadow 0.1s ease | = |
| Cursor | pointer | = |
| Painted layers | a.skip-to-content-link.button 120.0x45.0 bg #000000 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 shadow #000000 0px 0px 0px 1px | a.skip-to-content-link.button 347.0x45.0 bg #000000 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 shadow #000000 0px 0px 0px 1px, #ffffff 0px 0px 0px 3px, #000000 @ 0.3 0px 0px 5px 4px |
| Ancestor paint | 1 up body.gradient.template-index bg #ffffff | = |
| How | at rest | Shift+Tab, Tab |

Crops: `skip-link-default.png`, `skip-link-focus-visible.png`.

#### header

Header. The white bar: wordmark, SHOP/MARQUE/SECONDE MAIN/ARCHIVE SALE nav, search, CONNEXION and PANIER.

Page: home. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 60 |
| Padding | 10px 50px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Space Mono 13px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | li.mega-menu__item: Space Mono 13px/normal 400, #ffffff |
| Transition | background-color 0.4s ease |
| Icon | 0 x 0, colour #000000 |
| Painted layers | div.mega-menu__dropdown 0.0x0.0 bg #757575 border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff; a::after.dropdown-item__list-item-link 0pxx100% bg #f4ff7a; a::after.dropdown-item__list-item-link 0pxx100% bg #f4ff7a; a::after.dropdown-item__list-item-link 0pxx100% bg #f4ff7a; a::after.dropdown-item__list-item-link 0pxx100% bg #f4ff7a; a::after.dropdown-item__list-item-link 0pxx100% bg #f4ff7a |
| How | at rest |

Crops: `header-default.png`.

#### logo

Logo. The wordmark link (a hidden drawer copy is filtered out).

Page: home. Selector: `a.header__heading-link`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 155 x 38.5 |
| Padding | 7.5px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | avnier-font 14px/0px 500 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `logo-default.png`.

#### nav-item

Nav link. A top-level nav link (SECONDE MAIN). Measured, never followed.

Page: home. Selector: `.mega-menu__item-link:has-text("SECONDE MAIN")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 95.48 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Space Mono 13px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-item-default.png`, `nav-item-hover.png`, `nav-item-focus-visible.png`, `nav-item-pressed.png`.

#### nav-mega

SHOP menu item, hover. The SHOP item while its mega-menu dropdown is open.

Page: home. Selector: `mega-menu__item "SHOP"`. States: hover.

| Property | hover |
|---|---|
| Size (w x h) | 85.83 x 64 |
| Padding | 22px 27px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Space Mono 13px/normal 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| Cursor | pointer |
| How | mouse hover |

Crops: `nav-mega-hover.png`.

#### nav-dropdown

Mega-menu dropdown. The open SHOP dropdown panel.

Page: undefined. Selector: `.mega-menu__dropdown`. States: .

Not found on the page at capture time.

#### search-toggle

Search icon. The magnifier that opens the search modal. Measured, never submitted.

Page: home. Selector: `header search icon`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 40 x 40 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Space Mono 14px/0px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #ffffff | = | = | 21.4 x 21.4, colour #ffffff |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `search-toggle-default.png`, `search-toggle-hover.png`, `search-toggle-focus-visible.png`, `search-toggle-pressed.png`.

#### account-link

Login link. CONNEXION in the header. Measured, never followed.

Page: home. Selector: `header a:has-text("CONNEXION")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 40 x 40 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Space Mono 14px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #ffffff | = | = | 21.4 x 21.4, colour #ffffff |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `account-link-default.png`, `account-link-hover.png`, `account-link-focus-visible.png`, `account-link-pressed.png`.

#### cart-link

Cart link. PANIER in the header. Measured, never followed.

Page: home. Selector: `header a:has-text("PANIER")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 40 x 40 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Space Mono 14px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 40 x 40, colour #ffffff | = | = | 42.8 x 42.8, colour #ffffff |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `cart-link-default.png`, `cart-link-hover.png`, `cart-link-focus-visible.png`, `cart-link-pressed.png`.

### Home

#### hero

Hero. The collection announcement block under the header.

Page: home. Selector: `[class*="banner"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 799 x 799 |
| Padding | 799px 0px 0px 0px |
| Border | none |
| Radius | 0px |
| Background | #000000 @ 0.1 |
| Box shadow | none |
| Outline | none |
| Font | Space Mono 13px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Cursor | pointer |
| Painted layers | div.slideshow__media.banner__media 799.0x799.0 bg #000000 @ 0.1 |
| How | at rest |

Crops: `hero-default.png`.

#### hero-cta

Hero CTA. The first call-to-action on the home page. Measured, never followed.

Page: home. Selector: `:has-text("DÉCOUVRIR")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 481 x 30 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Space Mono 14px/normal 400 | = | = | = |
| Letter spacing | 1px | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span: Space Mono 13px/normal 400, #ffffff, ls 1px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 30 x 30, colour #ffffff, fill #000000 | = | = | = |
| Painted layers | span::after 0pxx1px bg #f4ff7a | = | = | span::after 232.859pxx1px bg #f4ff7a |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`, `hero-cta-focus-visible.png`, `hero-cta-pressed.png`.

### Shop grid

#### plp-title

Collection count. The "100 PRODUITS" count / collection heading.

Page: shop. Selector: `.product-count, .facets__heading`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 59.98 x 17.5 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Space Mono 14px/17.5px 400 |
| Letter spacing | normal |
| Colour | #7a7a7a |
| Transition | none |
| How | at rest |

Crops: `plp-title-default.png`.

#### facet

Facet filter. A PRIX/COULEUR/TAILLE filter disclosure; opened by its own summary.

Page: shop. Selector: `details.facets__disclosure`. States: default, opened.

| Property | default | opened |
|---|---|---|
| Size (w x h) | 74.92 x 36 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Space Mono 13px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | span: Space Mono 14px/21px 400, #000000, ls 1px | = |
| Transition | none | = |
| Painted layers | div.facets__display 350.0x237.0 bg #ffffff border T:1px solid #000000 @ 0.2 / R:1px solid #000000 @ 0.2 / B:1px solid #000000 @ 0.2 / L:1px solid #000000 @ 0.2; div.facets__header 348.0x52.0 bg #ffffff border B:1px solid #000000 @ 0.2; span 20.0x20.0 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 50%; span 20.0x20.0 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 50%; span 20.0x20.0 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 50%; span 20.0x20.0 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 50% | = |
| How | at rest | own toggle |

Crops: `facet-default.png`, `facet-opened.png`.

#### facet-checkbox

Facet checkbox. A checkbox row inside the open COULEUR facet.

Page: shop. Selector: `details[open].facets__disclosure input[type=checkbox]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 16 x 16 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Space Mono 13.3333px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Cursor | pointer |
| Placeholder | #000000, opacity 1 |
| How | at rest |

Crops: `facet-checkbox-default.png`.

#### sort-select

Sort select. The "Recommandés" sort dropdown.

Page: shop. Selector: `select[name="sort_by"]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 166 x 21 | = |
| Padding | 0px 20px 0px 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Space Mono 14px/21px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 @ 0.75 | = |
| Transition | box-shadow 0.1s ease | = |
| Cursor | pointer | = |
| How | at rest | clicked into the field |

Crops: `sort-select-default.png`, `sort-select-focused.png`.

#### product-card

Product card. A grid card: image, name, price.

Page: shop. Selector: `card ancestor of a[href*="/products/"]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 450 x 562.5 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Space Mono 13px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | label: Space Mono 13px/normal 400, #000000 | = |
| Transition | none | = |
| Painted layers | a 72.0x36.0 bg #ffffff border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000; a 72.0x36.0 bg #ffffff border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000; a 72.0x36.0 bg #ffffff border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000; a 72.0x36.0 bg #ffffff border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000; a 72.0x36.0 bg #ffffff border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000; a 72.0x36.0 bg #ffffff border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 | = |
| How | at rest | mouse hover |

Crops: `product-card-default.png`, `product-card-hover.png`.

#### card-name

Card link. The product name/link inside a card.

Page: shop. Selector: `a[href*="/products/"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 450 x 562.5 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Space Mono 13px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `card-name-default.png`, `card-name-hover.png`, `card-name-focus-visible.png`, `card-name-pressed.png`.

#### card-price

Card price.

Page: shop. Selector: `.price`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 68.42 x 18 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Space Mono 12px/18px 400 |
| Letter spacing | 1px |
| Colour | #000000 |
| Text node | span.price-item.price-item--regular: Space Mono 12px/18px 400, #000000, ls 1px |
| Transition | none |
| How | at rest |

Crops: `card-price-default.png`.

### undefined

#### pdp_url

PDP URL.

Page: pdp. Selector: ``. States: default.

| Property | default |
|---|---|
| Note | /products/doudoune-symphony |

Crops: none.

#### cart-page

/cart is a 404.

Page: cart. Selector: ``. States: default.

| Property | default |
|---|---|
| Note | 404 Page introuvable – AVNIER — /cart answers 404 "Page non trouvée" for everyone; the cart opens as the side-cart drawer (PANIER intercepts the link). |

Crops: none.

### Product page

#### pdp-title

Product title.

Page: pdp. Selector: `.product__title, product h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 440 x 18 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | avnier-font 15px/18px 500 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `pdp-title-default.png`.

#### pdp-price

Product price.

Page: pdp. Selector: `.price`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 440 x 27.5 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Space Mono 18px/27px 400 |
| Letter spacing | 1.3px |
| Colour | #000000 |
| Text node | span.price-item.price-item--regular: avnier-font 15px/22.5px 400, #000000, ls 1.3px |
| Transition | none |
| How | at rest |

Crops: `pdp-price-default.png`.

#### variant-radio

Variant option. A TAILLE size chip — the visible label of a visually hidden radio input.

Page: pdp. Selector: `input[type=radio] + label`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 73.2 x 40 | = |
| Padding | 0px | = |
| Border | T: 1px solid #000000; R: none; B: 1px solid #000000; L: 1px solid #000000 | = |
| Radius | 0px | = |
| Background | #000000 | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Space Mono 14px/14px 400 | = |
| Letter spacing | 1px | = |
| Colour | #ffffff | = |
| Text node | span: Space Mono 14px/14px 400, #ffffff, ls 1px | = |
| Transition | all 0.2s ease | = |
| Cursor | pointer | = |
| Icon | 13 x 9.75, colour #ffffff | = |
| Painted layers | label 73.2x40.0 bg #000000 border T:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 | = |
| How | at rest | mouse hover |

Crops: `variant-radio-default.png`, `variant-radio-hover.png`.

#### qty-input

Quantity field.

Page: undefined. Selector: `input[name="quantity"]`. States: .

Not found on the page at capture time.

#### add-to-cart

Add to cart. The AJOUTER AU PANIER buy button; measured in every state except a real press.

Page: pdp. Selector: `.product-form__submit`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 440 x 48 | = | = | = |
| Padding | 9px 30px 11px 30px | = | = | = |
| Border | 1px solid #000000 | = | = | = |
| Radius | 0px | = | = | = |
| Background | #000000 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Space Mono 15px/18px 400 | = | = | = |
| Letter spacing | 1px | = | = | = |
| Colour | #f6f6f6 | = | = | = |
| Text node | span: Space Mono 15px/18px 400, #f6f6f6, ls 1px | = | = | span: Space Mono 15px/18px 400, #000000, ls 1px |
| Transition | box-shadow 0.1s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 0 x 0, colour #f6f6f6, fill #000000 | = | = | = |
| ::after | 0px x 46px, absolute, bg #f4ff7a, radius 0px | = | = | 438px x 46px, absolute, bg #f4ff7a, radius 0px |
| Painted layers | button.product-form__submit.button 440.0x48.0 bg #000000 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000; button::after.product-form__submit.button 0pxx46px bg #f4ff7a | = | = | button.product-form__submit.button 440.0x48.0 bg #000000 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000; button::after.product-form__submit.button 438pxx46px bg #f4ff7a |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `add-to-cart-default.png`, `add-to-cart-hover.png`, `add-to-cart-focus-visible.png`, `add-to-cart-pressed.png`.

#### accordion

PDP accordion. A disclosure row (Description / Livraison…) — none on the captured product.

Page: pdp. Selector: `main details summary`. States: .

Not found on the page at capture time.

### Cart

#### cart-title

/cart 404 title. The 404 page /cart serves — the cart is the drawer, measured next.

Page: cart. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 188 |
| Padding | 0px |
| Gap | 1% |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | avnier-font 188px/188px 500 |
| Letter spacing | 3% |
| Colour | #0a0a0a @ 0 |
| Transition | none |
| How | at rest |

Crops: `cart-title-default.png`.

#### cart-empty

Empty cart. LE PANIER EST VIDE in the drawer.

Page: cart. Selector: `.side-cart__cart-empty`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 458 x 20 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Space Mono 13px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p: Space Mono 13px/normal 400, #000000 |
| Transition | none |
| How | at rest |

Crops: `cart-empty-default.png`.

#### cart-cta

Cart CTA. Measured, never followed.

Page: cart. Selector: `a:has-text("Continuer")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 265.61 x 45 | = | = | = |
| Padding | 9px 30px 11px 30px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 0px | = | = | = |
| Background | #000000 | = | = | = |
| Box shadow | #000000 0px 0px 0px 1px | = | #000000 0px 0px 0px 1px, #ffffff 0px 0px 0px 3px, #000000 @ 0.3 0px 0px 5px 4px | none |
| Outline | none | = | = | = |
| Font | Space Mono 15px/18px 400 | = | = | = |
| Letter spacing | 1px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | box-shadow 0.1s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.button 265.6x45.0 bg #000000 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 shadow #000000 0px 0px 0px 1px | = | a.button 265.6x45.0 bg #000000 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 shadow #000000 0px 0px 0px 1px, #ffffff 0px 0px 0px 3px, #000000 @ 0.3 0px 0px 5px 4px | a.button 265.6x45.0 bg #000000 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `cart-cta-default.png`, `cart-cta-hover.png`, `cart-cta-focus-visible.png`, `cart-cta-pressed.png`.

#### cart-drawer

Cart drawer. The side-cart opened by PANIER — "MON PANIER - 0 ARTICLE" empty.

Page: cart. Selector: `.side-cart__wrapper`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 900 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #000000 @ 0.55 |
| Box shadow | none |
| Outline | none |
| Font | Space Mono 13px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h4.text.text--medium: avnier-font 14px/20.02px 500, #000000 |
| Transition | background-color 0.24s ease delay 0.16s |
| Icon | 16 x 16, colour #000000 |
| Painted layers | side-cart.side-cart.side-cart--open 1440.0x900.0 bg #000000 @ 0.55; form.sidecart--empty 460.0x900.0 bg #ffffff; div.side-cart__wrapper 460.0x900.0 border T:1px solid #0a0a0a / R:1px solid #0a0a0a / B:1px solid #0a0a0a / L:1px solid #0a0a0a; div.side-cart__header 458.0x58.2 bg #ffffff border B:1px solid #000000 |
| How | at rest |

Crops: `cart-drawer-default.png`.

### Login gate

#### login-title

Login title.

Page: login. Selector: `main h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 448 x 223 |
| Padding | 0px |
| Gap | 1% |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | avnier-font 220px/220px 500 |
| Letter spacing | 3% |
| Colour | #0a0a0a @ 0 |
| Transition | none |
| How | at rest |

Crops: `login-title-default.png`.

#### email-input

Email field. The login email field. Nothing was typed. Nothing was submitted.

Page: login. Selector: `input[type=email]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 448 x 45 | = |
| Padding | 15px | 16px |
| Border | 1px solid #000000 @ 0 | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | #000000 @ 0.55 0px 0px 0px 1px | #000000 @ 0.75 0px 0px 0px 2px |
| Outline | none | = |
| Font | Space Mono 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Transition | box-shadow 0.1s ease | = |
| Cursor | text | = |
| Placeholder | #757575, opacity 0 | = |
| Painted layers | input 448.0x45.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 shadow #000000 @ 0.55 0px 0px 0px 1px | input 448.0x45.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 shadow #000000 @ 0.75 0px 0px 0px 2px |
| How | at rest | clicked into the field |

Crops: `email-input-default.png`, `email-input-focused.png`.

#### password-input

Password field. Focused only; nothing typed.

Page: login. Selector: `input[type="password"]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 448 x 45 | = |
| Padding | 15px | 16px |
| Border | 1px solid #000000 @ 0 | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | #000000 @ 0.55 0px 0px 0px 1px | #000000 @ 0.75 0px 0px 0px 2px |
| Outline | none | = |
| Font | Space Mono 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Transition | box-shadow 0.1s ease | = |
| Cursor | text | = |
| Placeholder | #757575, opacity 0 | = |
| Painted layers | input 448.0x45.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 shadow #000000 @ 0.55 0px 0px 0px 1px | input 448.0x45.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 shadow #000000 @ 0.75 0px 0px 0px 2px |
| How | at rest | clicked into the field |

Crops: `password-input-default.png`, `password-input-focused.png`.

#### login-button

Login button. The submit; measured except a real press — the form was never submitted.

Page: login. Selector: `button[type="submit"]`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 153.63 x 48 | = | = |
| Padding | 9px 30px 11px 30px | = | = |
| Border | 1px solid #000000 @ 0 | = | = |
| Radius | 0px | = | = |
| Background | #000000 | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Space Mono 15px/18px 400 | = | = |
| Letter spacing | 1px | = | = |
| Colour | #ffffff | = | = |
| Text node | span: Space Mono 15px/18px 400, #ffffff, ls 1px | = | = |
| Transition | box-shadow 0.1s ease | = | = |
| Cursor | pointer | = | = |
| ::after | 0px x 46px, absolute, bg #f4ff7a, radius 0px | = | = |
| Painted layers | button.button.submit-form 153.6x48.0 bg #000000 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0; button::after.button.submit-form 0pxx46px bg #f4ff7a | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab |

Crops: `login-button-default.png`, `login-button-hover.png`, `login-button-focus-visible.png`.

### Mobile (390 wide)

#### m-header

Mobile header.

Page: home. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 50.94 |
| Padding | 10px 15px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Space Mono 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span: Space Mono 10px/normal 400, #ffffff |
| Transition | background-color 0.4s ease |
| Icon | 0 x 0, colour #000000 |
| Painted layers | div.mega-menu__dropdown 0.0x0.0 bg #757575 border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff; a::after.dropdown-item__list-item-link 0pxx100% bg #f4ff7a; a::after.dropdown-item__list-item-link 0pxx100% bg #f4ff7a; a::after.dropdown-item__list-item-link 0pxx100% bg #f4ff7a; a::after.dropdown-item__list-item-link 0pxx100% bg #f4ff7a; a::after.dropdown-item__list-item-link 0pxx100% bg #f4ff7a |
| How | at rest |

Crops: `m-header-default.png`.

#### m-menu-button

Mobile menu button.

Page: home. Selector: `header details summary`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 35 x 30 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Space Mono 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span: Space Mono 10px/normal 400, #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #ffffff | 21.4 x 21.4, colour #ffffff | = | 21.4 x 21.4, colour #ffffff |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-menu-button-default.png`, `m-menu-button-hover.png`, `m-menu-button-focus-visible.png`, `m-menu-button-pressed.png`.

#### m-menu-open

Mobile menu, open. The menu summary after its own toggle; the crop is the open drawer.

Page: home. Selector: `header details summary`. States: opened.

| Property | opened |
|---|---|
| Size (w x h) | 35 x 30 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Space Mono 12px/normal 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span: Space Mono 10px/normal 400, #ffffff |
| Transition | none |
| Cursor | pointer |
| Icon | 16 x 16, colour #ffffff |
| How | own toggle |

Crops: `m-menu-open-opened.png`.

#### m-nav-link

Mobile nav link. A row inside the opened drawer.

Page: home. Selector: `.toggle-item__header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 388 x 59.11 |
| Padding | 10px 10px 10px 20px |
| Border | T: 1px solid #ffffff; R: none; B: 1px solid #ffffff; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Space Mono 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h3.h3: avnier-font 20px/22.8px 500, #ffffff |
| Transition | all 0.35s ease |
| Cursor | pointer |
| Icon | 35 x 37.11, colour #000000 |
| Painted layers | div.toggle-item__header 388.0x59.1 border T:1px solid #ffffff / B:1px solid #ffffff |
| How | at rest |

Crops: `m-nav-link-default.png`.

#### m-feature-tile

Mobile content tile. A content tile under the hero.

Page: home. Selector: `.card a`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 390 |
| Padding | 390px 0px 0px 0px |
| Border | none |
| Radius | 0px |
| Background | #000000 @ 0.1 |
| Box shadow | none |
| Outline | none |
| Font | Space Mono 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Cursor | pointer |
| Painted layers | div.slideshow__media.banner__media 390.0x390.0 bg #000000 @ 0.1 |
| How | at rest |

Crops: `m-feature-tile-default.png`.

### Footer

#### footer

Footer.

Page: home. Selector: `.footer-bottom`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1340 x 70 |
| Padding | 20px 50px |
| Border | T: 1px solid #ffffff @ 0.22; R: none; B: none; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Space Mono 13px/normal 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | label.text--small.opacity-75: Space Mono 12px/15px 400, #ffffff |
| Transition | none |
| Painted layers | div.footer-bottom 1340.0x70.0 border T:1px solid #ffffff @ 0.22 |
| Ancestor paint | 1 up section.section bg #000000 |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link.

Page: home. Selector: `.footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 190.86 x 36.8 | = | = | = |
| Padding | 10px 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Space Mono 12px/16.8px 400 | = | = | = |
| Letter spacing | 1px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.25s ease | = | = | = |
| Opacity | 0.75 | = | = | - |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### newsletter-input

Newsletter field. Focused only; never subscribed.

Page: home. Selector: `footer input[type="email"]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 320 x 45 | = |
| Padding | 15px | 16px |
| Border | 1px solid #ffffff | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | #000000 @ 0.55 0px 0px 0px 1px | #000000 @ 0.75 0px 0px 0px 2px |
| Outline | none | = |
| Font | Space Mono 12px/15px 400 | = |
| Letter spacing | normal | = |
| Colour | #ffffff | = |
| Transition | all 0.25s ease | = |
| Opacity | 0.75 | - |
| Cursor | text | = |
| Placeholder | #ffffff, opacity 0.75 | = |
| Painted layers | input.field__input.text--small 320.0x45.0 border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff shadow #000000 @ 0.55 0px 0px 0px 1px | input.field__input.text--small 320.0x45.0 border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff shadow #000000 @ 0.75 0px 0px 0px 2px |
| How | at rest | clicked into the field |

Crops: `newsletter-input-default.png`, `newsletter-input-focused.png`.

## Transitions declared in the readable stylesheets

This list is what the CSSOM could read on each page. The Shopify theme's own sheets and its inline `<style>` blocks are served from avnier.com and readable; `measure.mjs` skips any sheet the CSSOM refuses as cross-origin, which can include the 4 served from other hosts (`fonts.axept.io`, `fonts.googleapis.com`, `static.loloyal.com`, `unpkg.com`; see [css-vars.json](css-vars.json)). The per-state Transition rows above are computed values: they include a rule from an unreadable sheet only where it applies to a measured element in a measured state.

- home: `opacity 0.3s`, `transform 0.2s, top 0.2s`, `transform 0.2s, left 0.2s`, `transform 0.2s, right 0.2s`, `background 0.2s ease-in-out`, `none`, `text-decoration-thickness 0.1s`, `transform var(--duration-short) ease`, `opacity 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94)`, `box-shadow var(--duration-short) ease`, `top var(--duration-short) ease,font-size var(--duration-short) ease`, `transform 0.15s ease-out`
