# Fable patterns

How the measured components combine on each captured surface. Every value cited is in [tokens.json](tokens.json); the components are in [components.md](components.md) and the full-page evidence in [screenshots/](screenshots).

## Two skins over one token layer

Fable ships one Tailwind-style token layer (`--color-*` scales, `--color-background/text/border/line-*` semantics, `--radius-*`, `--shadow-above/below-*`) and paints it through two very different styling systems:

- The **emotion skin** — marketing pages (home, /signin, /signup, /support, /discover): Emotion styled-components (`css-*` classes) on cream `#fcf9f5` pearl-50 sections and deep forest bands (`color.forest.200` #064c37, `color.forest.300` #053829). Display copy runs `"Heldane Display"`; controls are literal-radius pills — 60px on buttons and fields, 44px on the text-input shell — with 2px same-as-fill borders. Ink is the softer `#161015` (`color.quote.theme.6`), cream `#f7f4ee` (`color.pearl.extra.light`) on dark, and focus draws a lighter blue `#116ecd` outline (offset 4px).
- The **catalog skin** — product pages (/clubs, /books, /club/fantasy, /book/*, /club/*): CSS modules (`*-module-scss-module__*`) on a white field (`color.background.primary`). Mastheads run the `heldane` face bold/regular; controls are `radius.full` 9999px pills with `graphite-600` fills or `graphite-300` hairlines; focus draws the declared `--color-focus` ring `#0064c3` (offset 2–4px).

## Chrome

A fixed 60px header (`component.headerHeight`) on every page carries the ~82px wordmark (`component.logoWidth`), the Clubs/Books/Library/Blog links and the sign-in/cart glyphs. On the marketing pages it floats transparent over the forest hero with cream ink (`text.onDark`) and a 0.04-alpha drop shadow; on the catalog pages it sits on white in `graphite-600` ink. Both fade their icon buttons to opacity .7 on hover.

## Home (marketing skin)

The hero is a forest band: a 500px-measure 72px/62px Heldane Display medium masthead (`font.size.masthead`) — "The modern app for every reader" — beside a 151x225 cover tile, over paired "Get the app" pills: white fill with `quote-theme-6` ink, or the named graphite `#292229` fill with white ink (`component.marketingPillH` 52px, `component.marketingPillRadius` 60px). Sections below alternate pearl/cream fields with 80px display headlines (`font.size.display`); the popular-clubs rail carries 248x380 cards that zoom to scale(1.01) over 0.4s ease-in-out (`motion.cardZoom`); a Fortune quote block sits in cream on another forest band. The closing band repeats the pill CTAs at 44px (`component.ctaHeight`).

## Clubs index (catalog skin)

A 58px heldane page title (`font.size.pageTitle`) over a 440x52 white search trigger (`component.searchTriggerW/H`, `radius.full`) that opens a 480x497 modal (`component.searchModalW/H`, radius 24, `shadow.above.2`-class elevation) holding a 430x41 input (radius 12). Below, 46px-tall genre chips (`component.genrePillH`) in white with `graphite-300` hairlines scroll horizontally behind a round `graphite-600` scroll arrow; shelf headings run `font.size.sectionTitle` 36px; club cards are 256x372 with 24px-rounded stacked covers (3px pearl-100 frame over a pearl-200 placeholder). A 132px `forest-300` app banner closes the page, its store badges beside a forest-200 headline.

## Book and club detail

/book/* runs the same catalog chrome: a 46px title (`font.size.detailTitle`), 12px byline link, ratings row, then the paired actions — a 361x52 `graphite-600` primary pill and a hairline secondary pill (`component.catalogButtonW/H`) — a 136x28 `olive-500` "Spoilers" badge (`component.spoilerPillH`), a "Read more" collapse and the author row with its hairline profile pill. The spoiler guard and read-more are local toggles; both were opened for capture and never submitted anything. /club/* mirrors the template: 46px name, member line, a 224x52 join pill and 52px share circle (both measured, never pressed), 36px section heads and the FAQ accordion rows.

## Sign-in and support (emotion skin)

/signin is a narrow emotion panel: 26px title (`font.size.panelTitle`), two ~396px text inputs in 44px-radius white shells with `#bcbcbc` hairlines (`component.signinPanelW`, `component.signinFieldH`) — the password field carrying a 12px-radius "show" button — a 396x44 dark `#292229` submit pill and matching white SSO pills (`component.signinButtonH`). Fields were focused and filled with sample values then cleared; nothing was submitted. /support mounts a `forest-200` masthead band (radius 12) behind a 58px headline in quote-theme-5 pink `#e4adbb`, with help/contact cards in 8px-radius icon tiles.

## Discover (dark)

/discover is the only public page painted dark: a full-viewport wall of drifting book covers under a layered radial-gradient scrim (`component.skin.discover.wallScrim`, lead stop `rgba(12,92,66,0.85)`), a ~81px wordmark (`component.discoverWordmarkW`), a 64px/69px Heldane cream headline (`font.size.discoverTitle`), a 420x60 white search field with a heavy shadow (`component.discoverFieldW/H`, `component.skin.discover.fieldShadow` rgba(12,12,12,.45) 0 10px 34px) and two ~50px `forest-400` pills with muted `#c5c1c5` ink. The wall was measured after the "Gathering ten thousand covers" state cleared, with its animation loop frozen; the Random and What-is-this pills brighten their muted ink to cream `#f7f4ee` on hover but show no focus change.

## Mobile (390px)

The phone keeps both skins: the same 60px header (`component.mHeaderH`), a full-viewport nav sheet off the menu button, the hero masthead stepping down to 46px (the same step as desktop detail titles — recorded on `font.size.masthead`'s responsive note), club cards widening to ~317px (`component.mClubCardW`) and the footer padding dropping to 80px (`component.mFooterPadY`). /discover keeps its dark wall, headline and pills at phone width.

## Motion and focus

Controls transition over 0.15s ease in the catalog skin (the Button module's background/color/opacity/border list — `motion.catalogControl`) and 0.2s ease on emotion controls (`motion.emotionControl`); the marketing club card scales over 0.4s ease-in-out. The declared `animate.flicker` (1s linear infinite) drives the twinkling star paths on the marketing hero. Focus is always an outline ring, never a border swap: `2px solid #0064c3` (`color.focus`, royal-400) with 2–4px offsets in the catalog skin, `2px solid #116ecd` offset 4px on the emotion pages, and the browser's 1px auto ring on unstyled controls — 33 of 37 focused components draw a ring; the four that don't (the two support cards, the two discover pills) are recorded as no measured change, and the two carousel icon buttons whose focus could not be held are recorded `via: focus failed`, not as absent.
