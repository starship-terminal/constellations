# Patterns

Public pages only. Measured 2026-11-19 on `https://nomadgoods.com/sg/`. No screenshots: the preview browser did not produce frames.

## App shell

Sticky header. First row is an announcement, 50px, white Gotham Bold 14px, on a gradient that fades to `rgba(0,0,0,.6)`. Copy on this day was "Sitewide Black Friday Savings" plus a countdown. Second row is the wordmark (136 by 25px at 1440, 67 by 25px at 390) and, at desktop, text links at 70px tall: Best Sellers, Cases, Watch, Charging, Tracking & Wallets, More Gear, Sale. Account, search, and cart sit at the end.

At 390 the text links are gone. An "Open menu" button opens a `#f3f3f3` card, radius 25px, over a `rgba(0,0,0,.6)` scrim.

Footer ground matches the page (`#f3f3f3`), padding 70px block, with a 50px top border in the same colour and a background SVG. Columns: Support, About, Sales, Explore. A newsletter field (`field-sm`, placeholder Email) sits beside a light Submit pill. Neither was submitted.

## Hero

Home hero is a full-bleed deal. White display type, `type-title-lg`, 77px at 1440, tracking `-0.04em`, line height 0.95. A light Shop Now pill sits under it. The measured headline was "35% Off Tracking Card Pro".

## Collection

`/sg/collections/phone-cases`. Visually hidden h1 still computes the display size. Tiles are about 353px wide. Names use `type-heading-md` (24px Gotham Bold). Captions use Gotham Book 12px. Sale pills use the clay colour.

## Product

Buy region is a white `.surface-card`, radius 25px, padding `30px 40px 15px`. Page title is `type-page-title` at 36px. Price is `type-price` at 32px. Colour choices are 30px circles, radius 1000px. The measured product was sold out. The action was `button-dark button-md` reading "Sold Out | Join the Waitlist". That button was focused and not clicked.

Overview, FAQ, and Reviews sit below. Reviews heading computed at 50px.

## Content page

`/sg/pages/about`. Hero title uses `type-title-lg` in white. Section titles repeat that class in black at 1440 (77px). Body paragraphs are Aleo 23px, line height 34.5px.

## 404

`/sg/products/modern-leather-case-black-camino-leather` returned "Page not found". Heading: "Whoops! Looks like you're lost." Body: "This page doesn’t exist, but let’s get you back on track." Actions named on the page: Go Back, Wander On. Styles of those two controls were not measured after the redirect to a real product.

## Not entered

No search query. No filter applied. No cart. No checkout. No account. No newsletter submit. No waitlist join.
