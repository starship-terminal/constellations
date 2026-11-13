# Cushion patterns — page layouts

Captured signed out on 2026-11-12. Heights are the painted `scrollHeight` of each route at 1440 wide; mobile is 390 wide at DPR 2. One painted theme: every page is light (#f5f5f5 page, #fcfcfc surfaces, #1f1f1f ink).

## Shell

- **Nav bar (1440x72, sticky top).** Wordmark left (112x25), right side: 40px text links (Pricing / Updates / Blog, 16px/500, 8px radius, a 5% black fill on hover and pressed), "Log in" (80x40) and "Sign up" (91x40, #00a6f4 fill, white 500 text, 8px radius — darkens to #0085c3 on hover/press).
- **Page column.** Content sits in a max-1280px column (`--page-max-width`) with 16px inline gutters (`--page-padding-inline`).
- **Footer (1240x184).** Link columns (Product / legal) at 14px plus the `hey@cushion.so` contact link.

## Home (`/`; H≈10584)

- **Hero.** A centred 768px column: 60px/600 Inter Tight h1 ("Work messaging that keeps your team organised"), a 20px/500 #858585 sub, then two 44px CTAs side by side — "Get started" (119x44, #00a6f4, 12px radius) and "Talk to a human" (154x44, #fcfcfc fill, 1px hairline, 12px radius).
- **App mock (1280x720, 12px radius, hairline border).** A rendered "Acme Inc" inbox used as a product preview: a 209px sidebar of 32px rows ("New post", "Inbox", "Search", emoji-prefixed channels, DM rows), 606x108 post cards and a 655x48 composer/post bar. Marketing component, not the authenticated app.
- **Problem statement (728x562).** "Workspace messaging is broken" — a 36px/600 animated statement that fills as you scroll.
- **Feature sections.** 36px/600 Inter Tight h2s ("Collaborate without the chaos") with the `--color-feature-*` hues marking each feature (posts #00a6f4, inbox #34c759, check-ins #ff9500, agents #af52de).

## Pricing (`/pricing`; H≈2649)

- **Plan panel (1240x354, #fafafa fill, 16px radius, 1px hairline).** A 579px heading column ("Everything you need for just $8/mo/user. 30 day free trial.") next to the plan details and a 143x56 #00a6f4 CTA (20px/600, 16px radius).
- **FAQs.** Accordion rows at 1238x72 (16px/500 question, `#fcfcfc` fill at rest, `#ebebeb` when opened), toggled locally.

## Updates (`/updates`; H≈11042)

- An 840px prose column: "Updates" h1, then ~1024x1720 release entries — date rail left, 32px release title ("Post Redesign, Slack Sync Upgrades, and more"), 35px item headings and body.

## Blog (`/blog`; H≈2674)

- "Blog" h1, a 1240x339 featured row, then a 3-across grid of 397x403 post cards (12px radius, 18px titles).

## Download / Integrations (`/download` H≈1178, `/integrations` H≈1163)

- Short single-section pages: an h1 ("Cushion Desktop", "Integrations") over the standard shell. Download buttons were never followed.

## Slack alternative (`/slack-alternative`; H≈7340)

- A long comparison page: the same 60px hero pattern ("The best Slack alternative for async teams") over ~366x148 comparison sections.

## Terms (`/terms`; H≈3368)

- A centred 736px legal column: 40px heading, 24px body lines. (/privacy shares the layout; not captured.)

## Mobile (390 wide)

- Same 72px nav (links collapse behind a menu button — the mobile menu shot is a documented transient state). The hero reflows to 48px Inter Tight (350x192) and the CTA goes full-width (350x44). Home paints H≈7244.
