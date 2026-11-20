# Measurements

Read on 2026-11-19 from the T3 preview tab, signed out, on seed.com.

Viewport readings:

| Page | innerWidth | innerHeight | devicePixelRatio |
|---|---|---|---|
| https://seed.com/ | 1169 | 731 | 2 |
| https://seed.com/ at phone resize | 390 | 844 | 2 |
| https://seed.com/products | 1169 | 731 | 2 |
| https://seed.com/daily-synbiotic | 1169 | 731 | 2 |
| https://seed.com/approach | 1169 | 731 | 2 |
| https://seed.com/lp/ds01-quiz-baseline | 1169, then 390 | 731, then 844 | 2 |

The preview viewport setting was fill (1169x731), then freeform 390x844. The freeform request reported a setting width of 390 and the page then reported innerWidth 390.

## Custom properties

216 custom properties resolved on :root. The colour, type, radius and spacing scales in tokens.json are those values. Product accent tokens `--products-am-02-*`, `--products-dm-02-*`, `--products-pm-02-*`, `--products-dvs-01-*` each have dark, highlight, light and primary steps. Only the primary step is tokenised. The rest are in this note:

| Token | Value |
|---|---|
| --products-am-02-dark | #9f995b |
| --products-am-02-highlight | #fff593 |
| --products-am-02-light | #faf7d3 |
| --products-dm-02-dark | #757c5d |
| --products-dm-02-highlight | #dcf194 |
| --products-dm-02-light | #ecf2d7 |
| --products-pm-02-dark | #698e79 |
| --products-pm-02-highlight | #c9f3db |
| --products-pm-02-light | #ebf5ef |
| --products-dvs-01-dark | #6a4540 |
| --products-dvs-01-highlight | #e7938e |
| --products-dvs-01-light | #e0cdca |

Opacity ramps `--color-dark-opacity-*` and `--color-light-opacity-*` run 00, 08, 10, 12, 16, 20, 30, 40, 50, 60, 70, 80, 90, 100. State layers: dark hovered 0.08, focused and pressed 0.12, disabled 0.4. Light hovered 0.08 white, focused and pressed 0.12 white, disabled 0.6 white.

## Elements

| Element | Page | Size | Weight | Line height | Tracking | Color | Background | Radius | Padding | Box |
|---|---|---|---|---|---|---|---|---|---|---|
| body | / | 16px | 400 | 22.4px | normal | rgb(28, 58, 19) | transparent | | | |
| html | / | | | | | rgb(28, 58, 19) | rgb(28, 58, 19) | | | |
| header | / 1169 | 16px | 400 | 24px | | rgb(28, 58, 19) | transparent | 0 | 0 8px 0 16px | 56 x 1169 |
| header | / 390 | | | | | | | | 0 8px | 48px tall. Menu icon, not the tab row |
| hero h2 | / 1169 | 48px | 350 | 52.8px | -1.2px | rgb(252, 252, 247) | transparent | 0 | 0 | 158 x 432 |
| hero h2 | / 390 | 32px | 350 | 35.2px | -0.8px | | | | | |
| h2 benefits | / | 24px | 350 | 28.8px | -0.36px | rgb(28, 58, 19) | | | | |
| h2 whole-body | / | 40px | 350 | 44px | -0.8px | rgb(28, 58, 19) | | | | 44 x 557 |
| h2 more than human | / | 48px | 350 | 52.8px | -0.72px | rgb(28, 58, 19) | | | | |
| ViaCap h3 | / | 12px | 500 | 13.2px | normal | rgb(252, 252, 247) | | | | uppercase |
| Take the Quiz a | / | 16px | 350 | normal | -0.04px | rgb(28, 58, 19) | rgb(252, 252, 247) | 1000px | 16px 24px | 52 x 146 |
| Shop DS-01 a | / | 16px | 350 | 22.4px | -0.16px | rgb(28, 58, 19) | rgb(252, 252, 247) | 1000px | 16px 24px | 48 x 143 |
| Skip link | / | 14px | 400 | 14px | | rgb(252, 252, 247) | rgb(28, 58, 19) | 8px | 12px 20px | 38 x 172 |
| products h1 | /products | 48px | 350 | 52.8px | -0.96px | rgb(252, 252, 247) | | | | |
| Cart button | /products | 14px | 350 | | -0.035px | rgb(28, 58, 19) | rgb(252, 252, 247) | 1000px | 10px 16px | 43 x 66, border 3px transparent |
| Learn More filled | /products | 16px | 350 | | -0.04px | rgb(252, 252, 247) | rgb(28, 58, 19) | 1000px | 16px 24px | 52 x 150 |
| featured price | /products | 20px | 400 | 26px | -0.2px | rgb(252, 252, 247) | | | 24px 0 0 | |
| grid price | /products | 20px | 350 | 26px | -0.2px | rgb(28, 58, 19) | | | | |
| struck price | /products | 20px | 350 | 26px | -0.2px | rgba(28, 58, 19, 0.5) | | | | |
| product h1 | /daily-synbiotic | 24px | 350 | 26.4px | -0.64px | rgb(28, 58, 19) | | | | |
| price | /daily-synbiotic | 24px | 350 | 28.8px | -0.36px | rgb(28, 58, 19) | | | | |
| blurb | /daily-synbiotic | 16px | 400 | | | rgb(28, 58, 19) | | | | |
| Start Now | /daily-synbiotic | 16px | 350 | 22.4px | -0.16px | rgb(252, 252, 247) | rgb(28, 58, 19) | 1000px | 16px 24px | 48 x 304 |
| Bestseller | /daily-synbiotic | 12px | 500 | | -0.06px | rgb(28, 58, 19) | rgb(211, 250, 153) | 1000px | 4px 8px | 25 x 71 |
| DS-01 badge | /daily-synbiotic | 14px | 350 | 19.6px | -0.14px | rgb(28, 58, 19) | transparent | 50px | 8px | 27 x 65, border 1.5px |
| reviews link | /daily-synbiotic | 14px | 350 | 14px | | rgb(28, 58, 19) | | | | |
| Shop tab | /daily-synbiotic | 14px | 400 | 14px | | rgb(28, 58, 19) | transparent | 0 | 7px 10.5px | 28 x 55 |
| shop menu | /daily-synbiotic | | | | | | rgba(87, 94, 85, 0.35) | 32px | 16px | 587 x 375, blur(19px) |
| menu row | shop menu | 16px | 400 | | | rgb(252, 252, 247) | | | | 75px tall |
| Shop All | shop menu | 14px | 500 | | | rgb(252, 252, 247) | | 1000px | | |
| sign-in panel | /products | | | | | | rgba(87, 94, 85, 0.35) | 32px | 16px | 215 x 375, blur(19px) |
| sign-in h3 | panel | 20px | 500 | 26px | -0.2px | rgb(252, 252, 247) | | | | |
| sign-in copy | panel | 14px | 350 | 19.6px | -0.14px | rgb(252, 252, 247) | | | | |
| email input | panel | 14px | 350 | 35px | | rgb(255, 255, 255) | transparent | 8px | 14px 20px | 48 x 327, border 1px rgba(252, 252, 247, 0.2) |
| Continue | panel | 14px | 350 | | -0.035px | rgb(28, 58, 19) | rgb(252, 252, 247) | 1000px | 10px 16px | 37 x 91 |
| focused link | /daily-synbiotic | | | | | | | | | outline 3px solid rgb(28, 58, 19), offset 2.5px |
| promo bar | /approach | 14px | 350 | | | rgb(28, 58, 19) | rgb(211, 250, 153) | | | 40px tall |
| science h2 | /approach | 64px | 300 | 96px | -2% | rgb(28, 58, 19) | | | | |
| science h1 | /approach | 16px | 500 | 17.6px | -2% | rgb(28, 58, 19) | | | | |
| quiz option | quiz | 18px | | | | rgb(28, 58, 19) | rgb(252, 252, 247) | 16px | 16px 24px | 72 x 552, border 1px rgb(210, 216, 208) |
| quiz option phone | quiz 390 | 18px | | | | | | 16px | 16px 24px | 72 x 342 |
| quiz heading | quiz 390 | 32px | 350 | 35.2px | | | | | | |
| footer caption | / | 14px | 350 | 19.6px | | rgb(252, 252, 247) | | | | |

Cookie Settings is a OneTrust control: 13.008px / 600, white fill, 1px black border, radius 2px. It is not a Seed token.

## Motion

Declared, not timed on screen:

- .link color 0.15s ease-in
- .button 0.25s
- main transform 0.25s cubic-bezier(0.75, 0, 0.25, 1)
- body opacity 0.25s 0.25s
- .shadow-hover 0.5s cubic-bezier(0.165, 0.84, 0.44, 1)
- prefers-reduced-motion sets transition-duration 0s and transition-property none, and html:focus-within scroll-behavior auto

Keyframes seen: swiper-preloader-spin, slide-up, opacity, onetrust-fade-in, otFloatingBtnIntro, otFloatingBtnImageIntro.

## Fonts

@font-face on seed.com:

- Seed Sans 300, 350, 400, 500, normal and italic, woff2 at /fonts/SeedSans-*.woff2
- Seed Sans Mono 400, /fonts/SeedSansMono-Regular-subset.woff2

Hero heading stack: "Seed Sans", system-ui, "Helvetic Neue", Helvetica, Arial, sans-serif. Body stack: "Seed Sans", Helvetica, sans-serif.

## Playwright pass, 2026-11-21

Headless Chromium, signed out. Desktop 1440x900 at 1x. Phone 390x844 at 2x. Custom properties: [css-vars.json](css-vars.json). Element styles: [components-computed.json](components-computed.json). Screenshots are under `screenshots/`. These readings confirm the token colours. They do not replace the 2026-11-19 table above.

| Element | Size | Notes |
|---|---|---|
| Hero quiz pill | 145.9 x 51 | Snow fill, seed-green text, 16px / 350, radius 1000px. Token height is 52px |
| Start Now | 432 x 48 | Seed-green fill, snow text, 16px / 350, radius 1000px |
| Sign-in email | 327 x 48 | Transparent fill, white text, 14px / 350, radius 8px, border 1px rgba(252, 252, 247, 0.2). Empty |
| Login email | 550 x 35 | White fill, seed-green text, 16px / 400, radius 0. Empty |
| Cart dialog | 500 x 884 | Snow fill, seed-green text, radius 16px, title 24px. Menu token radius is 32px |
| Quiz option | 552 x 72 | role=radio, snow fill, seed-green text, 18px / 350, radius 16px, border 1px #d2d8d0. Not selected |
| Review search | 350 x 40 | White fill, radius 0, border 1px #eaeaea, Neue Haas Unica Pro. Third-party widget |

Product-card and quiz-option selectors missed their crops. Header-link focus was not remeasured. Homepage locale screenshot was discarded because a promo overlay covered the listbox.
