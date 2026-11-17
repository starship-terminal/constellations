# Kitchen Stories component measurements

Computed styles read from kitchenstories.com on 2026-11-17 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the public magazine and the pages.kitchenstories.com marketing site. The consentmanager overlay was hidden, never answered. Written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Navigation and site chrome

#### header

Site header. The sticky magazine header: wordmark, primary links (Rezepte, Artikel, App, Plus, Partner) and the search and menu buttons.

Page: home. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 84.77 |
| Padding | 0px |
| Border | T: none; R: none; B: 1px solid #e3e3e3; L: none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Plus Jakarta Sans 16px/25.6px 500 |
| Letter spacing | 0.3px |
| Colour | #000000 |
| Text node | a: Plus Jakarta Sans 15px/18.75px 600, #000000, ls 0.2px |
| Transition | transform 0.25s ease |
| Icon | 28 x 28, colour #000000 |
| ::before | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| ::after | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| Painted layers | header.site-header.hide-header-search 1440.0x84.8 bg #ffffff border B:1px solid #e3e3e3; div.middle-header-contain 1440.0x83.8 bg #ffffff; a::before 60.3594pxx1px bg #000000; a::before 46.25pxx1px bg #000000; a::before 30.3906pxx1px bg #000000; a::before 30.125pxx1px bg #000000 |
| How | at rest |

Crops: `header-default.png`.

#### nav-link

Primary nav link. The "Rezepte" link in the header; measured, never followed.

Page: home. Selector: `header a Rezepte`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 60.36 x 19 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Plus Jakarta Sans 15px/18.75px 600 | = | = | = |
| Letter spacing | 0.2px | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | color 0.11s ease-in-out | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 60.3594px x 1px, absolute, bg #000000, radius 0px | = | = | = |
| Painted layers | a::before 60.3594pxx1px bg #000000 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.75 | = | 0.75 |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### nav-plus

Plus link. The "Plus" marketing link; measured, never followed. Checkout sits behind it.

Page: home. Selector: `header a Plus`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 30.13 x 19 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Plus Jakarta Sans 15px/18.75px 600 | = | = | = |
| Letter spacing | 0.2px | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | color 0.11s ease-in-out | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 30.125px x 1px, absolute, bg #000000, radius 0px | = | = | = |
| Painted layers | a::before 30.125pxx1px bg #000000 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.75 | = | 0.75 |

Crops: `nav-plus-default.png`, `nav-plus-hover.png`, `nav-plus-focus-visible.png`, `nav-plus-pressed.png`.

#### wordmark

Wordmark. The Kitchen Stories wordmark linking home.

Page: home. Selector: `header home link`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 97 x 63.77 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Plus Jakarta Sans 16px/16px 500 | = |
| Letter spacing | 0.3px | = |
| Colour | #515151 | #111111 |
| Transition | color 0.11s ease-in-out | = |
| Cursor | pointer | = |
| How | at rest | mouse hover |

Crops: `wordmark-default.png`, `wordmark-hover.png`.

#### search-open

Open search. The "Suche öffnen" button. Measured at rest; the field itself is measured after it opens.

Page: home. Selector: `button Suche öffnen`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 28 x 36.34 | = | = | = |
| Padding | 5px 0px 0px 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 5px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Plus Jakarta Sans 12.8px/15.36px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | background 0.15s ease-in-out | = | = | = |
| Cursor | default | pointer | = | pointer |
| Icon | 28 x 28, colour #000000 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.7 | = | 0.7 |

Crops: `search-open-default.png`, `search-open-hover.png`, `search-open-focus-visible.png`, `search-open-pressed.png`.

#### search-field

Search field. The header search field (placeholder "Suche …"). Focused and typed into, then cleared. Enter is never pressed.

Page: home. Selector: `input[name=s]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 298 x 41.97 | = | = |
| Padding | 7.2px 50px 7.2px 13.2px | = | = |
| Border | 1px solid #cccccc | 1px solid #111111 | 1px solid #111111 |
| Radius | 0px | = | = |
| Background | #ffffff | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Plus Jakarta Sans 16px/25.6px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #111111 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #757575, opacity 1 | = | = |
| Painted layers | input.search-field 298.0x42.0 bg #ffffff border T:1px solid #cccccc / R:1px solid #cccccc / B:1px solid #cccccc / L:1px solid #cccccc | input.search-field 298.0x42.0 bg #ffffff border T:1px solid #111111 / R:1px solid #111111 / B:1px solid #111111 / L:1px solid #111111 | input.search-field 298.0x42.0 bg #ffffff border T:1px solid #111111 / R:1px solid #111111 / B:1px solid #111111 / L:1px solid #111111 |
| How | at rest | clicked into the field | typed "pasta", then deleted; nothing sent |

Crops: `search-field-default.png`, `search-field-focused.png`, `search-field-filled.png`.

#### search-submit

Search submit. The search submit control. Measured, never pressed.

Page: home. Selector: `button.search-submit`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 48 x 37.97 | = | = | = |
| Padding | 0px 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 5px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Plus Jakarta Sans 12.8px/15.36px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #111111 | #212121 | #212121 | #212121 |
| Transition | background 0.15s ease-in-out | = | = | = |
| Cursor | default | pointer | = | pointer |
| Icon | 28 x 28, colour #111111 | 28 x 28, colour #212121 | 28 x 28, colour #212121 | 28 x 28, colour #212121 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `search-submit-default.png`, `search-submit-hover.png`, `search-submit-focus-visible.png`, `search-submit-pressed.png`.

#### menu-toggle

Menu toggle. The desktop menu button. Measured before search opens, because opening search slides the header. The opened state is a local toggle; its links are never followed.

Page: home. Selector: `button.desktop-menu-toggle`. States: .

Not found on the page at capture time.

### Home page

#### home-h1

Home title. The home page heading.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 97 x 46.06 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Plus Jakarta Sans 19.2px/23.04px 700 |
| Letter spacing | 0.3px |
| Colour | #000000 |
| Text node | a: Plus Jakarta Sans 19.2px/23.04px 700, #000000, ls 0.3px |
| Transition | none |
| How | at rest |

Crops: `home-h1-default.png`.

#### recipe-card

Recipe card. A home recipe card: thumbnail, time, category, title and author.

Page: home. Selector: `article`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 970 x 357.75 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Plus Jakarta Sans 16px/25.6px 500 |
| Letter spacing | 0.3px |
| Colour | #212121 |
| Text node | span.time-label: Plus Jakarta Sans 12px/19.2px 500, #212121, ls 0.3px |
| Transition | none |
| Painted layers | figure.post-thumbnail 477.0x357.8 bg #ffffff r 5px; span.time-label 50.7x19.2 bg #fff5c6 r 10px |
| How | at rest |

Crops: `recipe-card-default.png`.

#### card-title

Card title. A recipe card title link. Measured, never followed.

Page: home. Selector: `article title a`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 428.64 x 106 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Spectral 38px/48px 600 | = |
| Letter spacing | -1.3px | = |
| Colour | #212121 | = |
| Transition | color 0.11s ease-in-out | = |
| Cursor | pointer | = |
| How | at rest | mouse hover |

Crops: `card-title-default.png`, `card-title-hover.png`.

#### card-meta

Card meta. Category or time meta on a recipe card.

Page: home. Selector: `article meta`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 477 x 50 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Plus Jakarta Sans 12.8px/20.48px 500 |
| Letter spacing | 0.2px |
| Colour | #515151 |
| Text node | a.url.fn: Plus Jakarta Sans 12px/19.2px 500, #fc642d, ls 0.5px |
| Transition | none |
| How | at rest |

Crops: `card-meta-default.png`.

#### author-link

Author link. An author byline link. Measured, never followed.

Page: home. Selector: `a[rel=author]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 51.67 x 19.19 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Plus Jakarta Sans 12px/19.2px 500 | = |
| Letter spacing | 0.5px | = |
| Colour | #fc642d | #d4562a |
| Transition | color 0.11s ease-in-out | = |
| Cursor | pointer | = |
| How | at rest | mouse hover |

Crops: `author-link-default.png`, `author-link-hover.png`.

### Footer

#### footer

Footer. The site footer: follow links, legal links and the published hello@kitchenstories.de contact.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 500.97 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #fff5ea |
| Box shadow | none |
| Outline | none |
| Font | Plus Jakarta Sans 16px/25.6px 500 |
| Letter spacing | 0.3px |
| Colour | #000000 |
| Text node | h2.widget-title: Plus Jakarta Sans 16px/19.2px 600, #000000, ls 0.2px |
| Transition | none |
| ::before | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| ::after | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| Painted layers | footer.site-footer 1440.0x501.0 bg #fff5ea; section.widget.widget_nav_menu 220.3x246.0 border R:1px solid #c8c8c8; section.widget.widget_nav_menu 220.3x246.0 border R:1px solid #c8c8c8; section.widget.widget_nav_menu 220.3x246.0 border R:1px solid #c8c8c8 |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link. A legal footer link. Measured, never followed.

Page: home. Selector: `footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 66.11 x 29 | = | = | = |
| Padding | 2.5px 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Plus Jakarta Sans 12px/24px 500 | = | = | = |
| Letter spacing | 0.3px | = | = | = |
| Colour | #585450 | = | = | = |
| Transition | opacity 0.11s ease-in-out | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.7 | = | 0.7 |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

### Recipe index

#### index-h1

Index title. The recipes index heading.

Page: recipes. Selector: `h1`. States: .

Not found on the page at capture time.

#### index-card

Index card. A recipe card on the /rezepte index.

Page: recipes. Selector: `article`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 308.39 x 376.19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Plus Jakarta Sans 16px/25.6px 500 |
| Letter spacing | 0.3px |
| Colour | #212121 |
| Text node | span.time-label: Plus Jakarta Sans 12px/19.2px 500, #212121, ls 0.3px |
| Transition | none |
| Painted layers | figure.post-thumbnail 308.4x250.0 bg #ffffff r 16px; span.time-label 50.7x19.2 bg #fff5c6 r 10px; span.cat-links 0.0x0.0 bg #ceec9c r 12px |
| How | at rest |

Crops: `index-card-default.png`.

#### pagination

Pagination. The archive pagination. Measured, never followed.

Page: recipes. Selector: `.nav-links`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 980 x 40.34 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Plus Jakarta Sans 16px/25.6px 500 |
| Letter spacing | 0.3px |
| Colour | #212121 |
| Text node | span.page-numbers.current: Plus Jakarta Sans 12.8px/15.36px 700, #ffffff, ls 0.3px |
| Transition | none |
| Icon | 22 x 22, colour #515151 |
| Painted layers | span.page-numbers.current 39.1x40.3 bg #145f48 r 50px |
| How | at rest |

Crops: `pagination-default.png`.

#### page-link

Page link. A pagination page link. Measured, never followed.

Page: recipes. Selector: `pagination a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 38.75 x 40.34 | = | = | = |
| Padding | 10px 15px 5px 15px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Plus Jakarta Sans 14.08px/16.896px 400 | = | = | = |
| Letter spacing | 0.3px | = | = | = |
| Colour | #212121 | = | = | = |
| Transition | color 0.11s ease-in-out | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `page-link-default.png`, `page-link-hover.png`, `page-link-focus-visible.png`, `page-link-pressed.png`.

### Recipe page

#### recipe-h1

Recipe title. The recipe headline.

Page: recipe. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 970 x 38.39 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Spectral 32px/38.4px 600 |
| Letter spacing | -1.1px |
| Colour | #212121 |
| Transition | none |
| How | at rest |

Crops: `recipe-h1-default.png`.

#### recipe-card-block

Recipe card block. The WP Recipe Maker card: image, name, rating, ingredients, utensils, nutrition and steps. The cart and rating submit inside it were not pressed.

Page: recipe. Selector: `.wprm-recipe`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 655 x 3789.75 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Plus Jakarta Sans 15px/24px 500 |
| Letter spacing | 0.3px |
| Colour | #212121 |
| Text node | h2.wprm-recipe-name.wprm-block-text-bold: Plus Jakarta Sans 27px/35.1px 700, #212121 |
| Transition | none |
| Icon | 0 x 0, colour #212121 |
| Painted layers | div.wprm-recipe.wprm-recipe-template-kitchen-stories-recipe-template---glacier 655.0x3789.8 bg #ffffff; a.wprm-recipe-share-options-popup.wprm-recipe-link 98.7x42.0 bg #ffffff border T:1px solid #145f48 / R:1px solid #145f48 / B:1px solid #145f48 / L:1px solid #145f48 r 400px; a.wprm-recipe-print.wprm-recipe-link 118.1x42.0 bg #ffffff border T:1px solid #145f48 / R:1px solid #145f48 / B:1px solid #145f48 / L:1px solid #145f48 r 400px; div.wprm-layout-container.wprm-align-center 655.0x78.0 bg #fff5ea r 15px; div.wprm-layout-column.wprm-align-center 645.0x68.0 bg #fff5ea; span.wprm-recipe-servings-decrement.wprm-recipe-servings-change 20.0x30.0 bg #fff5ea border T:1px solid #fff5ea / B:1px solid #fff5ea / L:1px solid #fff5ea r 25px 0px 0px 25px |
| How | at rest |

Crops: `recipe-card-block-default.png`.

#### recipe-name

Recipe name. The recipe name inside the card.

Page: recipe. Selector: `.wprm-recipe-name`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 655 x 35.09 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Plus Jakarta Sans 27px/35.1px 700 |
| Letter spacing | normal |
| Colour | #212121 |
| Transition | none |
| How | at rest |

Crops: `recipe-name-default.png`.

#### rating

Rating. The star rating. Measured at rest. The rating form was not submitted.

Page: recipe. Selector: `.wprm-recipe-rating`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 277.53 x 51 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Plus Jakarta Sans 15px/24px 500 |
| Letter spacing | 0.3px |
| Colour | #212121 |
| Text node | span.wprm-recipe-rating-average: Plus Jakarta Sans 12px/24px 400, #212121, ls 0.3px |
| Transition | none |
| Icon | 24.75 x 24.75, colour #212121 |
| How | at rest |

Crops: `rating-default.png`.

#### ingredient-heading

Ingredients heading. The "Zutaten" heading inside the recipe card.

Page: recipe. Selector: `h3.wprm-recipe-ingredients-header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 655 x 42.97 |
| Padding | 8px 0px |
| Border | none |
| Radius | 15px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Plus Jakarta Sans 19.95px/25.935px 700 |
| Letter spacing | normal |
| Colour | #212121 |
| Transition | none |
| Icon | 0 x 0, colour #c8c8c8, fill #000000 @ 0 |
| Painted layers | h3.wprm-recipe-header.wprm-recipe-ingredients-header 655.0x43.0 bg #ffffff r 15px; div.wprm-decoration-line 531.2x1.0 border B:1px solid #c8c8c8 |
| How | at rest |

Crops: `ingredient-heading-default.png`.

#### ingredient

Ingredient row. One ingredient row.

Page: recipe. Selector: `.wprm-recipe-ingredient`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 585 x 30 |
| Padding | 0px 0px 5px 0px |
| Border | T: none; R: none; B: 1px solid #eeeeee; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Plus Jakarta Sans 15px/24px 400 |
| Letter spacing | 0.3px |
| Colour | #212121 |
| Text node | span.wprm-recipe-ingredient-amount: Plus Jakarta Sans 15px/24px 400, #212121, ls 0.3px |
| Transition | none |
| Painted layers | li.wprm-recipe-ingredient 585.0x30.0 border B:1px solid #eeeeee; input.wprm-checkbox 16.0x20.0 bg #ffffff border T:1px solid #cccccc / R:1px solid #cccccc / B:1px solid #cccccc / L:1px solid #cccccc r 2px; input::before.wprm-checkbox 24pxx24px image url(data:…); label::before.wprm-checkbox-label 16pxx16px bg #ffffff border T:1px double #f3f3f0 / R:1px double #f3f3f0 / B:1px double #f3f3f0 / L:1px double #f3f3f0 r 4px |
| How | at rest |

Crops: `ingredient-default.png`.

#### instruction-heading

Steps heading. The "Zubereitung" heading inside the recipe card.

Page: recipe. Selector: `h3.wprm-recipe-instructions-header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 655 x 64 |
| Padding | 8px 0px |
| Border | none |
| Radius | 15px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Plus Jakarta Sans 19.95px/25.935px 700 |
| Letter spacing | normal |
| Colour | #212121 |
| Transition | none |
| Icon | 18.19 x 18.19, colour #000000, fill #000000 @ 0 |
| Painted layers | h3.wprm-recipe-header.wprm-recipe-instructions-header 655.0x64.0 bg #ffffff r 15px; div.wprm-decoration-line 404.5x1.0 border B:1px solid #c8c8c8; input.wprm-media-toggle-checkbox 20.0x20.0 bg #000000 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 2px; input::before.wprm-media-toggle-checkbox 24pxx24px image url(data:…); span.wprm-toggle-switch-slider 60.1x28.0 bg #fc642d r 999px; span::before.wprm-toggle-switch-slider 22.3906pxx22.3906px bg #ffffff r 50% |
| How | at rest |

Crops: `instruction-heading-default.png`.

#### instruction

Step. One preparation step.

Page: recipe. Selector: `.wprm-recipe-instruction`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 595 x 633.5 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Plus Jakarta Sans 15px/24px 400 |
| Letter spacing | 0.3px |
| Colour | #212121 |
| Text node | div.wprm-recipe-instruction-text: Plus Jakarta Sans 15px/24px 400, #212121, ls 0.3px |
| Transition | none |
| How | at rest |

Crops: `instruction-default.png`.

#### step-nav

Next step. The "Weiter" step control if the template renders one. Measured, never used to submit.

Page: recipe. Selector: `Weiter`. States: .

Not found on the page at capture time.

#### body

Body paragraph. A paragraph of the recipe story.

Page: recipe. Selector: `article p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 655 x 84 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Plus Jakarta Sans 15px/28px 500 |
| Letter spacing | 0.3px |
| Colour | #212121 |
| Transition | none |
| How | at rest |

Crops: `body-default.png`.

#### app-cta

App call to action. An app download call to action. Measured, never followed.

Page: recipe. Selector: `Jetzt loslegen`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 30.39 x 19 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Plus Jakarta Sans 15px/18.75px 600 | = | = | = |
| Letter spacing | 0.2px | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | color 0.11s ease-in-out | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 30.3906px x 1px, absolute, bg #000000, radius 0px | = | = | = |
| Painted layers | a::before 30.3906pxx1px bg #000000 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.75 | = | 0.75 |

Crops: `app-cta-default.png`, `app-cta-hover.png`, `app-cta-focus-visible.png`, `app-cta-pressed.png`.

### Stories

#### stories-h1

Stories title. The stories index heading.

Page: stories. Selector: `h1`. States: .

Not found on the page at capture time.

#### story-card

Story card. A story card on /stories.

Page: stories. Selector: `article`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 308.39 x 376.19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Plus Jakarta Sans 16px/25.6px 500 |
| Letter spacing | 0.3px |
| Colour | #212121 |
| Text node | a: Plus Jakarta Sans 15px/26px 600, #212121, ls 0.2px |
| Transition | none |
| Painted layers | figure.post-thumbnail 308.4x250.0 bg #ffffff r 16px; span.cat-links 0.0x0.0 bg #ceec9c r 12px |
| How | at rest |

Crops: `story-card-default.png`.

#### stories-title

Story title. A story title on the /stories index. The index has no page h1.

Page: stories. Selector: `h2.entry-title`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 308.39 x 52 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Plus Jakarta Sans 15px/26px 600 |
| Letter spacing | 0.2px |
| Colour | #212121 |
| Text node | a: Plus Jakarta Sans 15px/26px 600, #212121, ls 0.2px |
| Transition | none |
| How | at rest |

Crops: `stories-title-default.png`.

### Search

#### results-h1

Results heading. The search results heading ("SUCHERGEBNISSE") for the public query pasta.

Page: search. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 650 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Plus Jakarta Sans 20px/24px 700 |
| Letter spacing | 0.2px |
| Colour | #212121 |
| Transition | none |
| How | at rest |

Crops: `results-h1-default.png`.

#### results-field

Results field. The search field on the results page. Typed into and cleared. Never submitted from this pass.

Page: search. Selector: `input[name=s]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 648 x 41.97 | = | = |
| Padding | 7.2px 50px 7.2px 13.2px | = | = |
| Border | 1px solid #cccccc | 1px solid #111111 | 1px solid #111111 |
| Radius | 0px | = | = |
| Background | #ffffff | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Plus Jakarta Sans 16px/25.6px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #111111 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #757575, opacity 1 | = | = |
| Painted layers | input.search-field 648.0x42.0 bg #ffffff border T:1px solid #cccccc / R:1px solid #cccccc / B:1px solid #cccccc / L:1px solid #cccccc | input.search-field 648.0x42.0 bg #ffffff border T:1px solid #111111 / R:1px solid #111111 / B:1px solid #111111 / L:1px solid #111111 | input.search-field 648.0x42.0 bg #ffffff border T:1px solid #111111 / R:1px solid #111111 / B:1px solid #111111 / L:1px solid #111111 |
| How | at rest | clicked into the field | typed "suppe", then deleted; nothing sent |

Crops: `results-field-default.png`, `results-field-focused.png`, `results-field-filled.png`.

#### result-card

Result card. A search result card.

Page: search. Selector: `article`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 322 x 324.69 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Plus Jakarta Sans 16px/25.6px 500 |
| Letter spacing | 0.3px |
| Colour | #212121 |
| Text node | span.time-label: Plus Jakarta Sans 12px/19.2px 500, #212121, ls 0.3px |
| Transition | none |
| Painted layers | figure.post-thumbnail 322.0x247.7 bg #ffffff r 5px; span.time-label 50.7x19.2 bg #fff5c6 r 10px |
| How | at rest |

Crops: `result-card-default.png`.

### Plus marketing

#### plus-h1

Plus heading. The Plus marketing headline on pages.kitchenstories.com.

Page: plus. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 655.55 x 212 |
| Padding | 20px 0px 0px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Fam-aime 64px/64px 600 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `plus-h1-default.png`.

#### plus-cta

Start free link. The "Jetzt kostenlos starten" link to /de/checkout. Measured, never followed. Checkout is a gated surface.

Page: plus. Selector: `a kostenlos starten`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 218.13 x 56.95 | = | = | = |
| Padding | 16px 24px | = | = | = |
| Border | none | = | = | = |
| Radius | 50px | = | = | = |
| Background | #621863 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Tt commons 19.2px/24.96px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | color 0.2s ease-in-out | = | = | = |
| Cursor | row-resize | = | = | = |
| Painted layers | a.cta.plus 218.1x57.0 bg #621863 r 50px | = | a.cta.plus 218.1x57.0 bg #621863 r 50px outline 1px auto #005fcc offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `plus-cta-default.png`, `plus-cta-hover.png`, `plus-cta-focus-visible.png`, `plus-cta-pressed.png`.

#### plus-nav

Marketing nav link. A pages.kitchenstories.com nav link. Measured, never followed.

Page: plus. Selector: `marketing nav a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 178.67 x 29.39 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Tt commons 19.6px/29.4px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | color 0.2s ease-in-out | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.heading-433.no-underline 178.7x29.4 outline 1px auto #005fcc offset 1px | = |

Crops: `plus-nav-default.png`, `plus-nav-hover.png`, `plus-nav-focus-visible.png`, `plus-nav-pressed.png`.

### Mobile (390 wide)

#### m-header

Mobile header. The phone header.

Page: mobile. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 64.77 |
| Padding | 0px |
| Border | T: none; R: none; B: 1px solid #e3e3e3; L: none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Plus Jakarta Sans 16px/25.6px 500 |
| Letter spacing | 0.3px |
| Colour | #000000 |
| Text node | a: Plus Jakarta Sans 19.2px/23.04px 700, #000000, ls 0.3px |
| Transition | transform 0.25s ease |
| Icon | 28 x 28, colour #000000 |
| ::before | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| ::after | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| Painted layers | header.site-header.hide-header-search 390.0x64.8 bg #ffffff border B:1px solid #e3e3e3; div.middle-header-contain 390.0x63.8 bg #ffffff; a::before 100%x1px bg #000000; a::before 100%x1px bg #000000; a::before 100%x1px bg #000000; a::before 100%x1px bg #000000 |
| How | at rest |

Crops: `m-header-default.png`.

#### m-menu

Mobile menu. The painted phone hamburger. The first .mobile-menu-toggle sits off-canvas in the header track. Opened as a local toggle; links not followed.

Page: mobile. Selector: `button.mobile-menu-toggle:visible`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 34.5 x 30 | = | = | = | = |
| Padding | 0px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 5px | = | = | = | = |
| Background | transparent | = | = | = | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | = | = | = |
| Font | Plus Jakarta Sans 12.8px/15.36px 700 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #000000 | = | = | = | = |
| Transition | background 0.15s ease-in-out | = | = | = | = |
| Cursor | default | pointer | = | pointer | = |
| Icon | 30 x 30, colour #000000, fill #212121 | = | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |

Crops: `m-menu-default.png`, `m-menu-hover.png`, `m-menu-focus-visible.png`, `m-menu-pressed.png`, `m-menu-opened.png`.

#### m-footer

Mobile footer. The phone footer.

Page: mobile. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 1366.83 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #fff5ea |
| Box shadow | none |
| Outline | none |
| Font | Plus Jakarta Sans 16px/25.6px 500 |
| Letter spacing | 0.3px |
| Colour | #000000 |
| Text node | h2.widget-title: Plus Jakarta Sans 16px/19.2px 600, #000000, ls 0.2px |
| Transition | none |
| ::before | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| ::after | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| Painted layers | footer.site-footer 390.0x1366.8 bg #fff5ea; section.widget.widget_nav_menu 351.0x267.0 border B:1px solid #cccccc; section.widget.widget_nav_menu 351.0x267.0 border B:1px solid #cccccc; section.widget.widget_nav_menu 351.0x267.0 border B:1px solid #cccccc; section.widget.widget_nav_menu 351.0x168.0 border B:1px solid #cccccc |
| How | at rest |

Crops: `m-footer-default.png`.

### Menus and overlays

#### m-menu-link

Mobile menu link. A link in the opened phone menu. Measured, never followed.

Page: mobile. Selector: `#menu-main-menue a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 66.39 x 34.59 | = | = | = |
| Padding | 4.5px 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Plus Jakarta Sans 16px/25.6px 500 | = | = | = |
| Letter spacing | 0.5px | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | color 0.11s ease-in-out | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.75 | = | 0.75 |

Crops: `m-menu-link-default.png`, `m-menu-link-hover.png`, `m-menu-link-focus-visible.png`, `m-menu-link-pressed.png`.

#### m-menu-panel

Mobile menu panel. The phone nav panel opened by the hamburger. Links measured, never followed.

Page: mobile. Selector: `nav.main-navigation`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 354 x 195.47 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Plus Jakarta Sans 12.8px/15.36px 500 |
| Letter spacing | 0.3px |
| Colour | #000000 |
| Text node | a: Plus Jakarta Sans 16px/25.6px 500, #000000, ls 0.5px |
| Transition | none |
| Ancestor paint | 1 up aside.mobile-sidebar bg #ffffff |
| How | at rest |

Crops: `m-menu-panel-default.png`.

## Transitions declared in the readable stylesheets

kitchenstories.com serves its stylesheets same-origin, so this list holds the transitions the readable sheets declare on each page; the per-state Transition rows above are computed values and cover every rule the page paints.

- home: `background 125ms ease-in-out, border-color 125ms ease-in-out`, `transform 0.25s ease-out, height 0.2s ease-out 0.25s, margin-bottom 0.2s ease-out 0.25s`, `none`, `transform 0.25s ease-out, height`, `max-height 0.4s ease-in-out, opacity 0.4s ease-in-out`, `background-color 125ms ease-in-out, border-color 125ms ease-in-out, outline 125ms ease-in-out`, `background-color 125ms ease-in-out, border-color 125ms ease-in-out`, `opacity 125ms ease-in-out`, `opacity 0.125s linear`, `transform 0.125s linear, opacity 0.125s linear`, `border-color 0.1s linear`, `box-shadow 0.1s linear`

- plus: `unset`, `background-color 0.1s, color 0.1s`, `0.3s`, `color 0.2s ease-in-out`, `color 0.2s ease-in-out, background-color 0.2s ease-in-out`, `background-color 0.3s ease-out`, `opacity 0.2s`, `opacity 0.25s`, `0.2s`, `0.3s cubic-bezier(0.455, 0.03, 0.515, 0.955)`, `0.25s`

- recipe: `opacity 0.2s`, `background 125ms ease-in-out, border-color 125ms ease-in-out`, `transform 0.25s ease-out, height 0.2s ease-out 0.25s, margin-bottom 0.2s ease-out 0.25s`, `none`, `transform 0.25s ease-out, height`, `max-height 0.4s ease-in-out, opacity 0.4s ease-in-out`, `background-color 125ms ease-in-out, border-color 125ms ease-in-out, outline 125ms ease-in-out`, `background-color 125ms ease-in-out, border-color 125ms ease-in-out`, `opacity 125ms ease-in-out`, `opacity 0.125s linear`, `transform 0.125s linear, opacity 0.125s linear`, `border-color 0.1s linear`

- recipes: `opacity 0.2s`, `background 125ms ease-in-out, border-color 125ms ease-in-out`, `transform 0.25s ease-out, height 0.2s ease-out 0.25s, margin-bottom 0.2s ease-out 0.25s`, `none`, `transform 0.25s ease-out, height`, `max-height 0.4s ease-in-out, opacity 0.4s ease-in-out`, `background-color 125ms ease-in-out, border-color 125ms ease-in-out, outline 125ms ease-in-out`, `background-color 125ms ease-in-out, border-color 125ms ease-in-out`, `opacity 125ms ease-in-out`, `opacity 0.125s linear`, `transform 0.125s linear, opacity 0.125s linear`, `border-color 0.1s linear`

- search: `opacity 0.2s`, `background 125ms ease-in-out, border-color 125ms ease-in-out`, `transform 0.25s ease-out, height 0.2s ease-out 0.25s, margin-bottom 0.2s ease-out 0.25s`, `none`, `transform 0.25s ease-out, height`, `max-height 0.4s ease-in-out, opacity 0.4s ease-in-out`, `background-color 125ms ease-in-out, border-color 125ms ease-in-out, outline 125ms ease-in-out`, `background-color 125ms ease-in-out, border-color 125ms ease-in-out`, `opacity 125ms ease-in-out`, `opacity 0.125s linear`, `transform 0.125s linear, opacity 0.125s linear`, `border-color 0.1s linear`
