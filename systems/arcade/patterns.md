# Arcade patterns

How the measured components compose into arcade.software's public pages. The
values behind every name are in [tokens.json](tokens.json) and
[components.md](components.md); the screenshots are in [screenshots/](screenshots).

## App shell: fixed white bar over a white page

`.navbar.w-nav` is a 72px fixed white bar (`layout.header-height`) holding the
Arcade mark, four 70%-ink `muted` links, a ghost Log in and the black `ink`
Sign up pill (`radius.control` 12px). It sits over a pure `page` white field
with `border` hairlines, never a coloured band. At 390px the bar keeps the mark
and the black pill and collapses the links behind a `m-menu-button`; the open
menu is a white sheet with 52px link rows and a paired Log in / Sign up row
([mobile-home-light-menu](screenshots/mobile-home-light-menu.png)).

## Hero: display line over a composer

Every marketing page opens on an Inter Display `typography.display` line
(56px/67px, weight 400) and a 16px `muted` subline. The home hero then shows
the product: a 680 x 148 `radius.card` composer (`prompt-box`) with a placeholder
line, a black `control.iconButton` send and a plus link, over a row of
`suggestion-chip` pills (12px/500 `chip-text`, 1px hairline, `radius.control`).
The chips swap the prompt's text locally — nothing is sent
([home-light-default](screenshots/home-light-default.png),
[home-light-suggestion](screenshots/home-light-suggestion.png)).

## Scatter wall and quote spotlight

The "Made to be seen" section is a sticky `scatter-stage` of video cards
(`scatter-card-trigger`) that drift and scale on hover (rect grows ~5%);
each card is a thumbnail plus a "Play <title>" link. Below, the `spotlight-*`
quote carousel pairs a `spotlight-quote` with white 40px `spotlight-prev/next`
arrow pills (`border` hairline, `radius.control` 14px)
([home-light-quote-next](screenshots/home-light-quote-next.png)).

## Pricing: grey card trio + credit calculator + FAQ

Three `radius.panel` 24px plan cards on a white page: `surface` #f4f4f4 fill,
plan title (28px) + subtitle, an Inter Display `typography.price` numeral
(36px), a credit line and a full-width 42px CTA — black `ink` for Pro
(`plan-cta-pro`), neutral white-outlined for Free and Enterprise
(`plan-cta-neutral`). Under them, a "How much does a video cost?" calculator
with pill `model-radio` options (white, 1px #e5e5e5, 12px), then hairline
`faq-question` accordion rows (56px, `radius.card` 16px when open)
([pricing-light-full](screenshots/pricing-light-full.png),
[pricing-light-faq](screenshots/pricing-light-faq.png)).

## Demo pages: the brand blue

Only on /product/interactive-demo does `accent` blue appear: the
`url-to-demo-input` pill field (72px, 18px type) with a `radius.pill` 72px
`url-button` arrow in `--primary-600`, plus `.signup-btn`/`tts-btn` nav pairs.
Elsewhere blue survives only as the `#005fcc` focus ring and the `ask-ai`
FAQ icon pills. Keep blue out of the core surfaces: the marketing chrome is
strictly black-on-white ([interactive-demo-light-full](screenshots/interactive-demo-light-full.png)).

## Forms: grey fields, black submit

The contact-sales card (`form-card`, white, `radius.panel`) stacks `.ds-input`
fields: `surface` fill, `radius.field` 12px, 40px tall (`control.fieldHeight`),
14px/400 text in 60%-grey placeholders. The select matches. `form-submit` is a
full-width black 40px `radius.control` button
([contact-sales-light-full](screenshots/contact-sales-light-full.png)).

## Content pages: the long scroll

Blog, changelog and video-examples are light list layouts: Inter Display
section heads over rows of cards and hairline dividers, all in the same
black/white/muted palette. The changelog is a single 91,833px scroll of every
release ([changelog-light-full](screenshots/changelog-light-full.png),
[blog-light-full](screenshots/blog-light-full.png)).

## Footer: brand band, not black

`.new-footer-brand` is a wide white `radius.card` panel (670px tall at 1440)
with the giant Arcade wordmark, `new-footer-grid` columns of
`footer-muted` #717171 links (14px, 17.5px rows) and 32px `new-social-link`
icon pills — the only oversized type on the site
([home-light-full](screenshots/home-light-full.png)).
