# Craftwork patterns — page layouts

Captured signed out on 2026-11-12. Heights are the painted `scrollHeight` of each route at 1440 wide; mobile is 390 wide at DPR 2.

## Shell

- **Promo bar + nav (36px + 60px).** A #161616 countdown bar ("Black Friday · Lifetime Pro for $224 instead of $449 · Ends in · See the deal", 13px 500) sits above the 60px nav: craftwork wordmark (20px 600), Assets / Templates / Inspiration dropdown rows (36px h-9), a 350px #fafafa search pill (radius 9999px, CMD-K hint), Pricing, the 32px theme toggle, Sign in and the 30px #1e1e1e Connect agent pill (8px radius, white 16px 500 text). On mobile it compresses to wordmark + a 44px menu button.

## Home (`/`, H=10732; dark shot captured via the toggle)

- **Hero.** 68px/70.72px 600 Euclid ("UI kits, templates and fonts made by real designers") on white; a two-line subline ("4,000+ packs ... 570+ independent designers"); the 46px buttons pair a #1e1e1e "Get full access" (10px radius) with a #efefef "Browse the catalog".
- **Product rail.** A horizontal card strip: 363px cards with a preview image, an 18px 500 title and a "from $N" price (Mini Bento, Blank 3 Pro, ElementX, SONANCE STUDIO, Notos).
- **Sections.** Long storefront page — category bands, stats, author CTAs and the footer.

## Pricing (`/pricing`, H=7737; mobile H=11923)

- **Heading.** "Browse for free. Go Pro to use it all."
- **Plan cards.** A 547px plan card column (name, a 40px 600 price figure, feature list, CTA) beside the Pro pitch; the deal page repeats the "Lifetime Pro, half price" banner.
- **FAQ.** 572px accordion rows (68px tall) that toggle locally.

## Components (`/components`, H=8713)

- **Library list + grid.** A 259px column of 34px rows ("Smooth UI | 231", "Magic UI | 76" — name + live count, 7% ink active fill, 10px radius) beside a grid of component cards; two 30px filter fields sit above. The route's only h1 ("Components, 1,224") is a 1x1 accessibility heading.

## Catalog (`/catalog`, H=3846)

- The asset index: the visible "Assets" h1 (472x47, ~40px 600), a 193px filter field and the card grid (the first feature card measured 1050x551).

## Black Friday (`/black-friday`, H=6392)

- The deal landing page: "Lifetime Pro, half price" under the same promo bar, benefit columns and the purchase CTA — measured, never used.

## Login (`/login`, H=900)

- A split auth screen: the OTP card (390 wide) on the left, the empty "Your Email" field, the "Send code" button, an "or" divider, and "Log in with Google", with a product image on the right. Photographed empty on 2026-11-21. Send code was not pressed. Google was not clicked.

## Footer

- The footer (1400x938 on home): category link columns, social icons (30px), small-print rows at 14px 500 in #999 tertiary text.

## Mobile (390 wide, DPR 2)

- The header holds wordmark + a 44px menu button. The menu opens as a 300px sheet overlaying the content. The hero drops to 38px 600.

## Theme behaviour

- **The toggle paints both themes.** `data-theme` flips on `<html>` and the same `--background-*`/`--text-icons-*` vars repaint: primary inverts #1e1e1e → #fff, primary text → #fff, surfaces go near-black; the #cafc00 brand lime stays put. Dark is a user toggle, not an OS media query — the dark harvest resolved every var under `[data-theme="dark"]`.
