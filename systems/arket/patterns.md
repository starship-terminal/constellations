# ARKET patterns

How the measured components compose into arket.com's public pages. Values
are in [components.md](components.md) and [tokens.json](tokens.json); the
screenshots named below are in [screenshots/](screenshots).

## The shell stack

Three thin bands above the fold, in order ([women-light-default](screenshots/women-light-default.png)):

1. **Locale notice** — a beige `#faf8f3` strip, "Location and language:
   Argentina/English" with Change and Close (`locale-notice`).
2. **Promo strip** — a white hairline-edged strip carrying the current
   campaign line (`promo-strip`).
3. **Sticky header** — white, `z-header`: ARKET wordmark left, a 40px
   `#f9f9f9` radius-4 search field, then icon buttons My account, Wishlist,
   Cart; a second row holds the category buttons Women…Gift shop plus the
   ARKET CAFÉ / Customer service / AR|EN utilities (`header`, `nav-item`,
   `search-field`, `cart-button`, `locale-button`).

## The drawer pattern

Every overlay panel is the same shape: a 538px (desktop) right-side sheet
with rounded top-left corner on a warm beige dimmer
(`--color-overlay-beige`, rgba(164,155,112,0.2)). The nav drawer, the cart
drawer, the PLP filter, the location picker and the search surface all use
it ([cart-drawer](components/crops/cart-drawer-default.png),
[filter-panel](components/crops/filter-panel-default.png),
[location-dialog](components/crops/location-dialog-default.png)).

## The listing grid

Category page anatomy ([clothing-light-full](screenshots/clothing-light-full.png)):
h1 + breadcrumb, a collapsible intro paragraph ("Read more"), then the
control row — Filter / Sort by / View, all 32px outlined 2px pills that
invert to black on hover ([clothing-light-filter](screenshots/clothing-light-filter.png)).
Cards are an image cell plus a centred text block: name (uppercase),
price, "+N" small-caps colour count. Hovering a card reveals the image
carousel arrows and quick Add-to-bag / wishlist controls; "New" is a text
badge, not a coloured flag.

## The two first-visit dialogs

Before the page is usable, two overlays mount ([home-light-consent](screenshots/home-light-consent.png),
[home-light-location](screenshots/home-light-location.png)): the
cookie-consent card bottom-left (`cookie-consent-popup`, two 56px black
actions) and the location `<dialog>` on the right with a country search
field, one black "Continue to <country>" and one outlined "Stay in
<country>" 32px control. Both were hidden, never answered.

## The account gate

/en-ww/account/ is a bare gate: a 60px white field with a 1px `#767676`
border and a 48px white outlined continue button ([account-light-default](screenshots/account-light-default.png)).
No social buttons, no alternative — one field, one action.

## Footer

A wide white link-column footer with bold mono headings (About ARKET,
Customer service, More information, Account and location) over 28px link
rows and social icons ([women-light-full](screenshots/women-light-full.png),
`footer`, `footer-heading`, `footer-link`, `footer-social`).

## Mobile

At 390 the header collapses to wordmark + icons with a `menu` hamburger
that opens the same 538px pattern as a full-height drawer; nav items are
52px hairline rows ([mobile-home-light-menu](screenshots/mobile-home-light-menu.png)).
