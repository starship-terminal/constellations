# Cosmos patterns — page layouts

Captured signed out on 2026-11-12. Heights are the painted `scrollHeight` of each route at 1440 wide; mobile is 390 wide at DPR 2.

## Home (`/`, H=3661; mobile H=3331)

- **Header (92px desktop, 68px mobile).** White, transparent-background measured. Left: 32px mark + Sequence/Instagram/TikTok/X text links (15px/22 500, secondary gray). Right: Log in text link + Sign up black pill (101x48, radius-full, 15px 500).
- **Hero.** 72px/72px 700 cosmosOracle display in ink; the second line is a rotating-word anchor cycling search terms (measured `hero-search` before the pill fix). Below it, the 640x82 search pill: elevation-gray 90% fill, 12% ink hairline ring, radius-full, 16px placeholder text.
- **CTA + QR card.** A black Join Cosmos for free pill (16px 700, radius-full) and a white 25%-radius QR card (209x242).
- **Footer (276px).** Link columns in 16px 500 secondary gray, social icons.

## Explore (`/explore`, H=4011; mobile H=4713)

- **Floating search pill** (456x56, radius-full) at the top of the content column.
- **Category tab bar** — 40px radius-full tabs (14px 500); inactive tabs sit in elevation gray, the active tab in ink (measured `cat-tab` is the 89x40 pill).
- **Section heads** — 20px/23 400 across the 1376px content width.
- **Selected cards** (365x201) and **element tiles** on the paper surface; the masonry column measures 1376 wide.

## Sequence (`/sequence`, H=4130)

- 88px 700 display heading over sequence cards — the heaviest display size on the surface.

## Shop (`/shop`, H=3142) · Careers (`/careers`, H=1859)

- Compact marketing pages in the same shell: white header, ink display, light sections.

## Search (`/search`, H=23694) · Brand (`/brand/...`, H=9690) · Profile (`/profile/...`, H=23029)

- Infinite feeds: the painted scrollHeight is a boundary, not the whole page. `-full` shots truncate at the 8-chunk cap and the boundary is recorded in each sidecar.

## Login (`/login`)

- A centred 344px card: username-or-email + password fields (~310px rows, 15px 400), a password visibility toggle, Forgot password in 14px 500 secondary gray, and the 56px radius-full Next pill. Disabled: elevation fill + tertiary text, `cursor: default`. Enabled (both fields typed, never submitted): ink fill + white text, `cursor: pointer`. Sign-up link below in ink.

## Sign-up start (`/start`)

- The first step of the account flow, screenshotted only — never advanced.

## Mobile (390 wide, DPR 2)

- Header collapses to 68px with a 44px radius-full menu button. The menu opens as a white overlay: full-width nav rows (~358x69) plus a 358x56 black sign-up pill. The hero drops to 32px 700.

## Theme behaviour

`data-theme="light"` on every route, and a CDP-forced `prefers-color-scheme: dark` emulation does not repaint: the `--dark-*` set is declared but un-painted. `.force-dark` / `.force-light` utility classes exist in the sheets for section-level overrides.
