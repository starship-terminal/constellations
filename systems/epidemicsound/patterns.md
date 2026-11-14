# Epidemic Sound patterns

How the measured components combine on each captured surface. Every value cited is in [tokens.json](tokens.json); the components are in [components.md](components.md) and the full-page evidence in [screenshots/](screenshots).

## Marketing chrome (ecru)

The marketing site paints the alternative-light theme: a `#f1f0eb` ecru field (`light.background.page`) with black ink (`light.text.ink`). The sticky header is a 1440 x 100 shell holding an inset pill bar — ES glyph, mega-menu triggers (Music / Sound effects / Tools / License / Resources / For business), Pricing, a ghost `rgba(61,77,116,.12)` Log in pill and the black Create-free-account pill (`light.action.primary`, `radius.button` 10000px). "Music" opens a 1359 x 331 mega menu of 356 x 56 genre items, a local disclosure.

The home hero is the voice of the brand: "You bring the idea. We bring the sound." in Sebenta 80px/80 at weight 500 with -2.4px tracking (`core.font.family.display`), then black 56px pill CTAs (`hero-cta`). Section headings drop to Sebenta 32px/40 (`section-h2`). See [home-light-default](screenshots/home-light-default.png) and [home-light-full](screenshots/home-light-full.png).

## Pricing (ecru)

/pricing keeps the same chrome: a 68px page heading, a 40 x 24 Monthly/Yearly `input[role=switch]` (`billing-switch`, black track, `rgba(61,77,116,.12)` when toggled), plan columns headed Creator/Pro/Pro Plus (`plan-name`, Inter 20px/24 — the es-subheading-l step), black 56px Get-30-days-free pills (`plan-cta`), then the "Compare plans" matrix heading (`compare-h2`, Sebenta 40px/48) and an FAQ block. Every trial action was measured, never followed.

## The dark catalog shell

The catalog pages (/music/genres/*, /music/themes/*, /artists/*, /sound-effects/categories/*) paint the dark theme: a `#121418` canvas (`dark.background.canvas`) under the same sticky pill header, now with the white primary pill inverted (`dark.action.primary` — white fill, black text).

The genre page opens MUSIC / GENRES / POP breadcrumbs (uppercase 12px, `rgba(255,255,255,.72)`) over the 1328 x 204 genre banner — a `#ff82c2` pink card (`dark.action.accent`, `radius.surface` 16px) carrying the GENRE kicker and the 40px/48 Sebenta "Pop music" heading in black. Below it, the track list runs 1328 x 56 rows (`track-row`, `radius.element` 8px, grid 288 / 576 / 64 / 144 / 184 with 16px gaps): a 56px album-cover Play button, title, artist, duration, BPM and scrolling genre/mood tag links. Row hover lays an `rgba(207,214,229,.08)` wash and swaps the cover button out — the hover-state box of `track-play` is a real 0x0. Like / Find similar / Add to playlist / Download / Copy link are 44px ghost icon buttons (8% hover wash, 16% pressed), all measured, never activated.

Under the list: a "Want more music?" banner (`wantmore`, 1328 x 244) with a white pill CTA, an FAQ accordion (`faq-row`, Inter 16/600 headings, a local disclosure), and the footer (`footer`, 1440 x 681) with 56px round social icon buttons. The theme and artist catalog pages repeat the same shell with their own banner hues; the SFX category page swaps genre/mood tags for subcategory links in periwinkle `#9e9eff` (`sfx-category-card`). See [genre-dark-default](screenshots/genre-dark-default.png), [artist-dark-default](screenshots/artist-dark-default.png) and [sfxcat-dark-default](screenshots/sfxcat-dark-default.png).

## Auth forms (login.epidemicsound.com)

The Keycloak account surfaces paint dark too: a 416px form column (`kc-card` ~883 tall) beside a pink-collage artwork panel. White 56px pill social buttons (Google, Apple), then `div.form-group` field wells — 8px radius, `rgba(207,214,229,.16)` ghost fill lifting to `.24` on focus — holding transparent 54px inputs, a 44px show-password eye, the white `Log in` submit pill (`kc-submit`, #0f0f0f text), Create-account / SSO / forgotten-password links and the terms row. Measured as forms, never filled with real credentials or submitted. See [login-dark-default](screenshots/login-dark-default.png) and [signup-dark-default](screenshots/signup-dark-default.png).

## Mobile (390px)

The phone keeps both surfaces: a 390 x 100 header with the ES glyph, a centered 44px Create-free-account pill and a "Show navigation menu" hamburger opening the nav drawer (`mobile-genre-dark-drawer`). The genre page re-runs the pink banner and 358 x 56 track rows. See [mobile-home-light-default](screenshots/mobile-home-light-default.png) and [mobile-genre-dark-default](screenshots/mobile-genre-dark-default.png).

## Radii, focus and motion

The shipped pages all carry the `radii-override` body class: buttons are full pills (`radius.button` 10000px), surfaces 16px, elements 8px, details 4px, tiny 2px; the base `--es-radius-small/medium/large` resolve to 0 under it. Keyboard focus draws a real outline, not a border: 2px solid black on the ecru surface (`light.border.focus`), 2px solid `#20afff` azur on the dark surface (`dark.border.focus`). The declared transition default is `--default-transition-duration` 0.15s with `--animation-duration` 0.6s; hovers settle through ghost washes rather than colour flips.
