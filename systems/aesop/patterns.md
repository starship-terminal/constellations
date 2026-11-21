# Aesop patterns

How the components combine on each surface, with the screenshots that show them. Captured on aesop.com (US storefront) on 2026-11-21, signed out, at 1440 x 900 and 390 x 844. The control map is [site-tree.md](site-tree.md).

## Shell

Two tiers on every page: a 30px utility row (Stores / Customer service left; Email sign up, Account, My cart right) over a ~51px main row (wordmark centred, nav links, Search trigger). Transparent over the hero, translucent cream (rgba(255,254,242,.686)) once scrolled. At 390 it collapses to Stores + wordmark + My cart + burger. [home-light-default](screenshots/home-light-default.png), [mobile-home-light-default](screenshots/mobile-home-light-default.png)

## Overlays

- **Search disclosure** — a full-width band under the nav ("I'm looking for…", a 960px field at 24px, Close at right). [home-light-search](screenshots/home-light-search.png)
- **Email sign up modal** — a cream panel, "Subscribe to stay in-the-know", with an email field and a submit button. The empty phone field is painted out. Not submitted. [home-light-signup](screenshots/home-light-signup.png)
- **Account sign-in dialog** — opened from the Account control. Email, password, Stay signed in, Facebook, Google, Create My Account. Login wall. Nothing typed, nothing clicked through. [home-light-account](screenshots/home-light-account.png)
- **My cart drawer** — a 405px right sliding panel: "My cart" head, empty-state body, secure-payment note. [home-light-cart](screenshots/home-light-cart.png)
- **Filter rail** — a 400px left rail "Filter by / Cancel": accordion groups (Price, Skin type, Skin concern, Form, Ingredients, Aroma), RESET ALL + ink APPLY at the foot. [shopall-light-sort](screenshots/shopall-light-sort.png)
- **No-result dialog** — the locator's "No result found" card (415px) with an ink OK dismiss.

## Catalogue page

Title + count ("Shop all · 165 products"), All filters toggle, Sort select, then a 4-across grid of tall tiles: photo, amber badge line, bold name, descriptor, size select, price, ink "Loading/Add to cart" bar. [shopall-light-default](screenshots/shopall-light-default.png)

## Product page

Breadcrumbs over two columns: 700px gallery left; badge, title, price, descriptor, bordered variant box, ink add-to-cart bar, promo note right, a Description tab below. The information accordion rows render only at phone widths (h-hide-for-large) — the open state is on the mobile capture. Suggested-partners rail below. [pdp-light-default](screenshots/pdp-light-default.png), [mobile-pdp-light-accordion](screenshots/mobile-pdp-light-accordion.png)

## Footer

Dark ink ground (#252525): secure-checkout and samples lines, then link columns (Orders and support, About, Sustainability) in cream, the Online Preferences OneTrust trigger, payment marks. [cart-light-full](screenshots/cart-light-full.png)

## Error surfaces

`/account` and `/account/login` both serve the styled "unexpected error" page in full chrome with a "You may also like" rail. `Login-Show` serves the Demandware sign-in form. That form is a login wall: nothing was typed or submitted. [notfound-light-default](screenshots/notfound-light-default.png), [login404-light-default](screenshots/login404-light-default.png), [login-light-default](screenshots/login-light-default.png)

## 2026-11-21 surfaces

Gifts, Library, Experience, Our story, Contact us, Gift Finder, The Aesop Gift Gathering and the site map use the same shell. [gifts-light-default](screenshots/gifts-light-default.png), [library-light-default](screenshots/library-light-default.png), [contact-light-default](screenshots/contact-light-default.png), [sitemap-light-default](screenshots/sitemap-light-default.png). Store-locator map tiles are painted out. [stores-light-default](screenshots/stores-light-default.png)
