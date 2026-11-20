# Components

Values in the table are computed styles from the T3 preview tab on 2026-11-19. Crops are from headless Playwright on 2026-11-21 at 2x. Read values from the table and from [tokens.json](tokens.json), not from the PNGs.

| Component | Where | Values |
|---|---|---|
| Header | `/` at 1169 | 56px tall, padding 0 8px 0 16px, transparent. Tabs Shop, Science, Learn at 14px / 400, padding 7px 10.5px |
| Header, phone | `/` at 390 | 48px tall. Logo and a 24px two-bar menu icon. Tab row not shown |
| Skip link | `/` | 14px / 400, snow text, seed-green fill, radius 8px, padding 12px 20px, 38px tall |
| Button, filled | `/products` Learn More, `/daily-synbiotic` Start Now | Seed green fill, snow text, 16px / 350, radius 1000px, padding 16px 24px. Height 52px or 48px |
| Button, inverse | `/` Take the Quiz | Snow fill, seed-green text, 16px / 350, radius 1000px, padding 16px 24px, 52px tall |
| Button, compact | Sign-in Continue, Cart | 14px / 350, radius 1000px, padding 10px 16px. Continue 37px. Cart 43px with a 3px transparent border |
| Text link | Footer captions | 14px / 350, line-height 19.6px, snow on the dark footer |
| Text field | Sign-in email | 48px, radius 8px, padding 14px 20px, 14px / 350, white text, 1px border rgba(252, 252, 247, 0.2), transparent fill |
| Promo bar | `/approach` | 40px, bright green #d3fa99, seed-green text, 14px / 350 |
| Badge | Bestseller on `/daily-synbiotic` | Bright green fill, seed-green text, 12px / 500, radius 1000px, padding 4px 8px |
| Product code pill | DS-01 on `/daily-synbiotic` | Transparent, 1.5px seed-green border, radius 50px, 14px / 350, padding 8px |
| Menu | Shop dropdown | 375px wide, radius 32px, padding 16px, glass rgba(87, 94, 85, 0.35), blur 19px. Rows 75px, 16px / 400, snow text |
| Sign-in panel | Sign in button | Same glass, 375 by 215, radius 32px. Title 20px / 500. Body 14px / 350 |
| Quiz option | `/lp/ds01-quiz-baseline` | 72px tall, radius 16px, 1px border #d2d8d0, snow fill, 18px, padding 16px 24px. Width 552px at 1169, 342px at 390 |
| Accordion row | Ingredients on the product page | 16px / 400 button, no fill. Expanded copy was in the DOM. No open-panel chrome was measured separately |
| Focus | Header link | 3px solid #1c3a13 outline, offset 2.5px. Sign-in email computed outline none |
| Cart dialog | `/products` Cart | Snow panel, "Your Cart", empty copy, total $0.00, disabled Checkout. See [products-light-cart.png](screenshots/products-light-cart.png). The element crop was dropped: a promo overlay covered it |
| Country listbox | `/login` footer | CAD / Canada and USD / United States. Opened, not changed. See [login-light-locale.png](screenshots/login-light-locale.png) |
| Review search and sort | `/daily-synbiotic` | Yotpo widget. Computed font Neue Haas Unica Pro, not Seed Sans. Crops: [review-search-default.png](components/crops/review-search-default.png), [review-sort-default.png](components/crops/review-sort-default.png) |

Crops for the rows above live in [components/crops/](components/crops/), named `{component}-{state}.png`. Hover and pressed were captured for nav, hero, menu, add-to-cart, start-now, and the phone menu. Several pairs look identical. Focus-visible crops were taken. The 2026-11-21 pass did not remeasure the header-link outline.

## Gaps

| Component | Status |
|---|---|
| Text area, checkbox, switch | Not present on the public pages that were opened |
| Select | Country listbox opened. Not changed. No other select was measured |
| Radio | Quiz options computed as `role=radio` on 2026-11-21 (552x72, snow fill, 18px, weight 350, radius 16px, 1px border #d2d8d0). The 2026-11-19 note called them buttons. No option was selected, so selected is not captured |
| Tabs | Header tabs are buttons with aria-expanded. Shop, Science, and Learn open on hover. No selected-tab fill was measured apart from the open menu |
| Tooltip, toast | Not opened |
| Dialog | Cart dialog captured. Image zoom dialog not captured. Sign-in panel is a dropdown, not a dialog |
| Table, avatar, list row | Not present as product components on the marketing pages. Product menu rows are in the shop menu screenshot |
| Disabled, loading, error | Not on the public pages that were opened. Checkout in the empty cart is a muted pill. Error and warning colours exist as custom properties |
| Search | Review search field is visible. Nothing was typed |
| Product card crop | Selector missed. The card is in [products-light-default.png](screenshots/products-light-default.png) |
| Quiz option crop | Selector missed. The options are in [quiz-light-default.png](screenshots/quiz-light-default.png) |
