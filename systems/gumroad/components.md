# Gumroad components

Public pages on gumroad.com, captured 2026-11-21, signed out, headless Chromium. Desktop viewport measured 1440×900 at 1×. Phone viewport measured 390×844 at 2×. The site tree is [site-tree.md](site-tree.md).

Values below are token names. Read the numbers from [tokens.json](tokens.json).

## Button

Start selling in the marketing header. Light fill is `component.button.fill` (`#000000`), hover fill is `component.button.fill-hover` (`#ff90e8`). Dark default is already the pink accent. Height `component.button.height` (79px) on the marketing header. Radius is 0. Discover's Start selling is a separate 48px control and was not the measured specimen.

Crops: [nav-cta-light-default.png](components/crops/nav-cta-light-default.png), [nav-cta-dark-default.png](components/crops/nav-cta-dark-default.png).

Pressed, disabled, and loading were not captured. The header button has no pressed style that stays visible after the pointer lifts.

## Link

Nav links (Discover, Blog, Pricing, Features, About, Gumclaw) are 18px ABC Favorit, transparent fill, black text in light. See [nav-link-light-default.png](components/crops/nav-link-light-default.png).

## Text field

Search marketplace on the home page. Height `component.field.height` (64px), radius `component.field.radius` (4px), 20px type, page-coloured fill. See [search-field-light-default.png](components/crops/search-field-light-default.png).

Discover's search is a separate 16px field: [search-products-light-default.png](components/crops/search-products-light-default.png).

Login email and password were photographed and not filled. See [login-email-light-default.png](components/crops/login-email-light-default.png).

## Tabs

Discover sort tabs: Trending, Best Sellers, Hot & New. Selected tab is a white pill in light. See [sort-tab-light-default.png](components/crops/sort-tab-light-default.png) and [discover-light-best-sellers.png](screenshots/discover-light-best-sellers.png) if present; the best-sellers shot is [mobile-discover-light-best-sellers.png](screenshots/mobile-discover-light-best-sellers.png).

## Menu and dialog

Category hover opens a dialog (Drawing & Painting and its subcategories). More opens a second dialog. See [discover-light-category-dialog.png](screenshots/discover-light-category-dialog.png) and [discover-light-more-dialog.png](screenshots/discover-light-more-dialog.png).

The phone header button opens an in-page menu. See [mobile-home-light-menu.png](screenshots/mobile-home-light-menu.png).

## Card

Product cards on Discover link to a public product page. See [product-card-light-default.png](components/crops/product-card-light-default.png) and [product-light-default.png](screenshots/product-light-default.png).

## Checkbox, radio, select

Discover filters include checkboxes, a price pair, rating radios, and a currency select. They are on the page. Individual state crops were not cut. See [discover-light-default.png](screenshots/discover-light-default.png).

## Not present on the public surface

Text area, switch, tooltip, toast, table, avatar, and badge were not found as product chrome on the captured pages. Status colours are declared (`--color-danger`, `--color-success`, `--color-warning`, `--color-info`) and tokenised. They do not paint a status component on the marketing home.

## Gaps

- Signed-in library, product editor, payouts, and settings were not opened. Follow and Start selling stop at the login or signup wall.
- Checkout (`I want this!`) was not followed.
- Newsletter field was not typed or submitted.
- No validation error was produced, because no form was submitted.
- Pressed and disabled states of the header button were not held.
- Icon extraction was not run. The wordmark and social marks stay in the screenshots.
