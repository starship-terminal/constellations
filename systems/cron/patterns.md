# Cron patterns — page layouts

Captured signed out on 2026-11-12. Heights are the painted `scrollHeight` of each route at 1440 wide; mobile is 390 wide at DPR 2. Two painted surfaces, no theme attribute: the home is dark, the content pages are light.

## Shell

- **Header (120px dark).** The 126x40 Cron wordmark, then Blog / Changelog / Docs / Login (22px, white on #161412) and the 46px #ff4700 Sign up pill (9999px radius) glowing under `--glow` (0 0 100px 20% orange, tightening to 0 0 25px 40% on hover via `--glow-hover`).
- **Banner.** A 44px #161412 strip under the header — "Cron is now Notion Calendar →" — ringed by an inset 0.5px orange hairline and a 28px 20% orange glow, radius 4px.
- **Footer (180px, #0f0d0a).** Social glyphs and legal links at 13px on the darkest band.
- **Mobile.** The header compresses to ~96px; the hamburger toggles `body.showing-menu` into a 390x768 dark overlay with 24px nav items and a ~342x54 full-width Sign up.

## Home (`/`, dark; H≈1475)

- **Hero.** "It's about time." at 140px Helvetica Neue 700 (-3px tracking, 90% leading; 80px on mobile) over the #161412 page, with a 22px #ccc sub and the Sign up CTA.
- Content is sparse by design — the page is the hero, the banner and the footer.

## Blog (`/blog`, light; white page)

- **Heading.** "Cron Blog" at 40px/700, black on white.
- **Entries.** 676px-wide `<article>` cards (~987-1124px tall): the post's media, its title and meta, stacked down the column.

## Changelog (`/changelog`, light; H=113351, bounded at 112000)

- **Heading.** "Cron Changelog" at 40px/700.
- **Entries.** 676px `<article>` cards (1000-2200px tall) — version media, title, date and the release notes — plus a "see the demo" link. The page grows indefinitely; capture is capped at 8 chunks.

## Post (`/blog/<post>`, light)

- **Article.** "Cron is now Notion Calendar" at 32px/700, a #616161 meta line (`--ratio`), 16px `--text-default` body copy, a 676x451 media frame (16px radius, full-bleed on mobile) and a "← All blog posts" back link. Links throughout are `--chronos` #ff4700.
