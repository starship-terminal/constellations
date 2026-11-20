# Components

Measured on newbalance.co.uk, signed out, 2026-11-19, in the T3 preview browser. Viewport was the pane that loaded: innerWidth 1169, innerHeight 731, devicePixelRatio 2. Pages used the class `page design-refresh`.

No `components/` folder. The preview browser returned "The browser is not producing screenshot frames", and a headless Chromium load of the homepage returned HTTP 403. Values below are computed styles and stylesheet rules, not pixels sampled from an image.

## Button

Primary, painted on Add to Bag and Log in: background `#151415`, text `#ffffff`, border `1px solid #151415`, radius `2px`, padding `16px 12px`, type 14px / 20px / weight 300, height 54px. Width on the product and login columns was 328px.

Secondary, painted on Shop now: background `#ffffff`, text `#151415`, border `1px solid #e5e7e8`, same radius, padding, type and height.

Text link (Sign up now in the promo bar): weight 500, underline, padding `0 0 3px`.

Hover, from the stylesheet `.design-refresh .nb-button.button-primary:hover`: background `#343538`. Not confirmed by a live hover, because the snapshot tool could not drive the pointer.

Disabled, from `.design-refresh .nb-button.button-primary:disabled`: background `#e5e7e8`, text `#7c7c7c`. No disabled button was on the pages opened.

Keyboard focus, from `body.keyboard-focus .page.design-refresh .nb-button:focus`: outline `2px solid #015ecc`.

The older rule `.nb-button.button-primary { background: #cf0a2c }` is in global.css and is overridden on every captured page by `.design-refresh`.

## Link

Nav links (New, Men, Women, Kids, Running, Sports): 16px, weight 300, line-height 20px, colour `#000000`, padding `30.4px 11.2px`, no underline, radius 0. Help in the banner is 14px, weight 700, white.

## Text field

Login email and password, and the customer-care email field: background `#ffffff`, border `1px solid #abb0b4`, radius `4px`, padding `28px 10px 12px` on login (12px horizontal on the care field), height 58px, text 16px weight 500. Floating label: `#5c6268`, 14px, weight 300.

Header search (`#header-search-input`): 16px, weight 300, padding `1px 2px`, no visible border in the resting computed style, height 24px. It sits in the header row rather than as a boxed field until search is opened. The open state was not captured.

## Checkbox

Remember me on the login page: 16px box, radius 4px, from the label `::before`. Label text `#151415`, 14px, weight 500, padding-left 24px. Checked state was not toggled.

## Select, text area, radio, switch, tabs, tooltip, toast, table, avatar

Not present on the captured signed-out pages. Recorded as a gap.

## Menu

Desktop nav is a row of dropdown links. The open mega-menu was not captured. Help opens a small menu (Order Status, Return Order, Help) whose resting labels were read. The open panel's box was not measured.

## Dialog

OneTrust cookie banner was present on first load (Accept All Cookies, Reject All, Cookies Settings). It was dismissed with Accept All Cookies so later pages could be read. Its computed box was not recorded before dismiss. No other dialog was opened.

## Card

Product tiles on `/men/`: name 14px weight 700, line-height 16.8px, colour `#000000`. Price `.sales` 14px weight 300, line-height 24px. Tile container had no border, radius or shadow in the resting computed style. A tile that was off-screen reported height 0.

## Badge

Stylesheet declares `.badge` at 75% size, weight 700, radius `0.1875rem`, and `.badge-primary` at `#cf0a2c`. No product badge was in view on the tiles measured. "Best Seller" and "Selling Fast" were in the home page text and were not isolated as elements.

## List row

Filter group titles on `/men/` (Mens Shoe Sizes, Mens Clothing Sizes): 14px, weight 500, no border. Hide Filters: border `1px solid #bec0c3`, radius 4px, padding 12px, weight 700, height 42px.

## Size cell

Product page size buttons: background `#ffffff`, text `#151415`, border `1px solid #bec0c3`, radius `2px`, padding `3.2px 8px`, about 58 by 43px, 14px weight 300. Selected size was not clicked, so the selected size style is a gap.

Colour swatch, selected: 62 by 62px, border `2px solid #151415`, radius 4px.

## Icon button

Search, account and bag in the header are 32px hit targets. The marks are an SVG sprite (`#header-hamburger-icon`, `#header-my-account-icon`, and the bag link). Sprite symbols were not extracted. The wordmark was.

## Gaps

- No screenshots or crops. Preview frames failed. Headless returned 403.
- Hover, pressed, focus-visible and disabled were not driven live. Hover, disabled and keyboard-focus colours come from stylesheet rules.
- No dark theme on the captured pages. `.dark-mode` is a section class, not a site theme.
- Open search, open mega-menu, selected size, error validation, empty bag, loading and toast were not captured.
- Add to Bag and Log in were not clicked. No checkout, payment, phone or account creation.
- Mobile 390 width was not captured. The live viewport was 1169, not a requested 1440.
- Motion and reduced-motion were not probed. Button transition duration computed to `0.2s` on `.nb-button`.
