# Creative Market patterns — page layouts

Captured signed out on 2026-11-12. Heights are the painted `scrollHeight` of each route at 1440 wide; mobile is 390 wide at DPR 2. The storefront carries `data-theme="legacy"` — one painted theme.

## Shell

- **Header (73px).** The Creative Market wordmark (88x36), the 585x44 search field with its "All Categories" multiselect dropdown on the left and a teal search button, then Join | Log in (14px 600), a 92x32 #4e42a1 purple "Save 25%" pill (8px radius, white 14px 600 text) and a 20x23 teal cart icon. A second row carries the uppercase category nav: FONTS / TEMPLATES / GRAPHICS & ILLUSTRATIONS / BRUSHES & EFFECTS / MORE / SALE (#d53a9d) / INSPIRATION / ENTERPRISE at 13px.
- On mobile the header grows to 119px (wordmark + a 45px hamburger + the 46px search field stacked) and the hamburger opens a 295px drawer: category links with chevrons, then "Join Creative Market" and "Log in".

## Home (`/`, H=5189; mobile H=6403)

- **Hero.** An illustrated masthead — "Bring your creative ideas to life." painted as artwork — over a strip of category tiles.
- **Product rail.** "Handpicked designs" rows of 337x275 cards: a preview image, shop + product name, and a teal price pill; hovering exposes the 329x44 Add To Cart button (#003a37 fill, measured, never pressed).
- **Suggested searches.** Pill chips (69x44, #fee4c3 fill, 20px radius): Serif, Script, Nostalgic, Font Duo...
- **Newsletter.** A 368x31 email field in the footer band — never submitted.

## Category (`/fonts`, H=5702; mobile H=8223)

- **Heading.** "Fonts" at 48px Averta 600 over a two-column filter sidebar and a result grid.
- **Filters.** 44px pill triggers (32px radius) opening 480x202 filter groups; ticking an option refetches the grid — toggles were measured, never activated.
- **Result cards.** 320x213 tiles: preview image, name, price pill.

## Product (`/SilverStag/7290900-Silver-Garden-Nostalgic-Font-Duo`, H=5160)

- **Left column.** Preview images (specimen strips), an "About" block, then the Reviews / Comments / FAQs accordions — 878x88 details/summary rows that toggle locally.
- **Buy box (450px).** The $79 price figure (50x35), four 450x24 license radio rows (Desktop / Webfont / App / E-pub — measured at rest, never ticked), the 450x45 #088178 teal "Add to cart" (8px radius, white 14px 600), the 450x40 outlined "Buy now" (white fill, teal text + border), the 450x52 #dff8f6 "Enterprise or Custom License" CTA and the Product Specs block (File Size, Vector, Web Font, Created date).
- **Bundle.** "Complete your Project" rows with teal checkboxes and an "Add N items to cart" footer — never used.
- **Meet the shop.** A 1376px card (16px radius): shop avatar + name, 232x35 FOLLOW pill (24px radius), MESSAGE, and stats — joined, sales, rating.
- **Rails.** "More from this shop" / "Similar Fonts" render empty on this capture — the related-card component is recorded as a miss.

## Search (`/search?query=font`, H=5702)

- The same category template: a 48px heading, filter pills and the 320px result grid.

## Membership (`/membership`, H=5145)

- A 72px #4e42a1 purple hero heading and 274x323 plan cards (16px radius, 700-weight price figure) with their CTAs — measured, never followed.

## Sign in (`/sign-in`, H=900)

- A centered 673px card: "Welcome back to the world's marketplace for design" at 36px 600, the 43px username and password fields (436/392 wide, 14px), a Remember me checkbox (missed this run), the 438x51 teal "Log In" and three 51px outlined SSO buttons — filled/cleared, never submitted.

## Footer

- The 1440x488 footer: category link columns at 15px, a socials row of 20px icon links, the legal row.

## Mobile (390 wide, DPR 2)

- The 119px header stacks wordmark + hamburger over the 358x46 search field. The drawer overlays at 295x844 with 18px-tall nav items. Page sections reflow to one column; headings drop to 20px 600.

## Theme behaviour

- **One theme.** `html[data-theme="legacy"]` paints the storefront: white page, #303538 ink, #088178 teal actions, #4e42a1 accents. The `:root` and legacy selectors disagree on a few declarations (input radius 3px vs 12px, border width 1px vs 2px, banner #dff8f6 vs #f9d1e7) — the legacy values are what paint, and both are recorded in raw/css-vars.json.
- **No dark surface.** The sheets carry no second theme layer; tokens.json's dark set is intentionally empty.
