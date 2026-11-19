# Components

Public signed-out storefront, Sweden English (`/se/en`), measured 2026-11-19 at 1440×900. Values are computed styles. Crops were not saved: the preview browser stopped producing screenshot frames, then PerimeterX denied the page.

## Button

The storefront button is a pill. `.btn` in `styles.min.css` sets `border-radius: 1.5rem`, `border-width: 1px`, `padding: .625rem .875rem`, `text-transform: uppercase`.

| State | Where | Values |
|---|---|---|
| On photo, default | Home hero, "Shop women's jackets" | transparent background, `rgb(255, 255, 255)` text and 1px border, radius 24px, padding 10px 14px, height 34px, Helvetica Now Text 12px, line-height 12px, letter-spacing -0.36px, weight 400 |
| Outline, default | Filter sheet, "Clear filters" | transparent background, `rgb(0, 0, 0)` text, 1px solid `rgb(0, 0, 0)` border, radius 24px, padding 16px 20px, height 46px, 12px, letter-spacing -0.36px |
| Fill, default | Filter sheet, "Show results 66" | background `rgb(0, 0, 0)`, text `rgb(255, 255, 255)`, 1px solid white border, radius 24px, padding 16px 20px, height 46px |
| Hover | `.btn:hover` and `.btn-primary:hover` in the stylesheet | `font-style: italic`. Primary hover fill `rgba(0, 0, 0, 0.15)`. Secondary hover fill `hsla(0, 0%, 100%, 0.3)`. Not measured under a real pointer |
| Disabled | `.btn[disabled]` | `opacity: 0.3`, `pointer-events: none`. Not seen on a live control |
| Focus | not measured | the stylesheet sets `outline: 2px solid transparent` on text inputs, not a visible button ring |
| Sand | `.btn-sand` | background and border `rgb(235, 233, 225)`. Not painted on the pages read live |

## Icon button

`button.sidebar__close-button.btn.btn-circle` is 32×32. `.btn-circle` sets `aspect-ratio: 1/1`, `min-height: 32px`, `padding: 0`, `border-color: currentColor`. The carousel arrows on the home product rail are 32px tall with radius 24px.

## Link

Nav links (Women, Men, Junior, Hike, Ski, Outlet, Guides) are Helvetica Now Text 12px, weight 400, letter-spacing -0.36px, uppercase, `rgb(0, 0, 0)`, height 13px. Footer links use the same `.t-sm` treatment. Mega-menu group links ("New Arrivals") are Helvetica Now Display 16px, letter-spacing -0.16px, uppercase. Product name links are Helvetica Now Display 14px, letter-spacing -0.36px, no text transform.

Hover on `.btn` is italic. Nav anchors carry a `hover:italic` class. A live hover measurement was not taken.

## Text field

Header search (`.header__search-input`) is transparent, 14px Helvetica Now Display, letter-spacing -0.16px, padding 0 12px, height 45px, radius 0, placeholder "Search...". Its own border width is 0. The bar under it is the 1px `rgba(0, 0, 0, 0.15)` edge of `.header__bottom-bar`.

`.input` in the stylesheet is 16px, letter-spacing -0.16px. Focus (`.input-email:focus`, `.input-text:focus`) sets border-color `rgba(0, 0, 0, 0.9)` and `outline: 2px solid transparent`. Error (`.field._error input`) is `rgb(182, 32, 32)`. Success (`.field._success input`) is `rgb(86, 134, 94)`. Those three states were read from the stylesheet, not from a filled field.

## Text area, select, checkbox, radio, switch

Not measured. A product page, which holds size selection, never loaded. The filter sheet uses rows and 12px colour dots, not a native select.

## Tabs

Not present on the home page or the jackets collection. The collection has a "View as: Model / Product" pair. The labels are Helvetica Now Text 12px, letter-spacing -0.36px. The selected state is `peer-checked:underline`. Which option was checked was not recorded.

## Menu

The category mega-menu is in the DOM at height 0 until a nav item is opened. Group links inside it are 16px uppercase. It was not opened, so its panel colour, padding and motion were not measured.

The filter sheet is the menu that was opened. `aside.sidebar-main` is `position: fixed`, 450px wide, 900px tall, background `rgb(255, 255, 255)`, right border 1px `rgba(0, 0, 0, 0.15)`, no shadow. Header padding is 16px 12px, height 65px. Group labels ("Color", "Fit") are 14px Helvetica Now Display, uppercase, letter-spacing normal. Options ("Jackets") are 14px, letter-spacing -0.36px, sentence case. Counts are `rgba(0, 0, 0, 0.55)`.

## Tooltip, dialog, toast

OneTrust cookie banner was on screen and dismissed with "Use only necessary cookies". Its colours were not measured before the click. Closed modals stay in the DOM (`modal-popup`, authentication, country switcher, minicart) with `translate-y-full` or `display: none`. Their open styles were not measured. No toast was triggered.

## Card

`.product-item` is 360px wide, radius 0, shadow none, transparent background. The image is 359×479, radius 0. Name is 14px Helvetica Now Display, letter-spacing -0.36px, `rgb(0, 0, 0)`. Price is the same size and tracking. A second price node in the same tile is `rgba(0, 0, 0, 0.55)`. Four cards sit at x 0, 360, 720 and 1080, so the grid gap is 0.

## List row

Filter options are list rows: a 12px round swatch (`.item__color-label`, radius 9999px, 1px transparent border) plus a 14px label and a muted count. Swatch fills read from inline styles include `#000000`, `#255793`, `#7b4e2d`, `#686a4e`, `#828588`.

## Table

Not present on the captured pages.

## Avatar

Not present. The account control is a text link ("Log in", "Register") in the footer, 12px uppercase.

## Badge

Not a separate component. The filter count and the "66" on Show results are 12px or 14px text in `rgba(0, 0, 0, 0.55)` or white, not a filled chip.

## Gaps

- No crops. The preview browser returned "The browser is not producing screenshot frames" before any PNG was saved.
- Product page, size grid, add-to-bag, minicart and checkout were not entered. A direct product URL returned PerimeterX "Access to this page has been denied".
- Hover, focus-visible, pressed, disabled and loading were not measured on a live control. Hover italic and the error/success border colours are stylesheet rules.
- Dark theme was not found. `color-scheme` on the document was `normal`. No theme toggle was in the header.
- Phone width (390) was not captured. The viewport was 1440×900 when PerimeterX blocked further navigation.
- Newsletter and account forms were not submitted. They ask for an account, which this capture does not create.
