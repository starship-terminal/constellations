# Matter components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from getmatter.com on 2026-11-18, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. The marketing site paints one near-black theme (MR-Camphor display, a blurple pill). A published article on words.getmatter.com loads signed out. The publication home is a subscribe gate. The web reader at web.getmatter.com is a sign-in card. Nothing was signed into, bought or submitted.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (37 components, 75 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (75 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-state.png`. The marketing site paints `dark`. The sign-in card is `light`. Docs has a `dark` default and a `light` theme-toggle shot. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages bounded to 8 chunks; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `https://www.getmatter.com/` | [default](screenshots/home-dark-default.png), [full](screenshots/home-dark-full.png) |
| Web extension | `https://www.getmatter.com/web-extension` | [default](screenshots/web-extension-dark-default.png), [full](screenshots/web-extension-dark-full.png) |
| Newsletters | `https://www.getmatter.com/newsletters` | [default](screenshots/newsletters-dark-default.png), [full](screenshots/newsletters-dark-full.png) |
| Privacy | `https://www.getmatter.com/privacy` | [default](screenshots/privacy-dark-default.png), [full](screenshots/privacy-dark-full.png) |
| Terms | `https://www.getmatter.com/terms` | [default](screenshots/terms-dark-default.png), [full](screenshots/terms-dark-full.png) |
| Words That Matter | `https://words.getmatter.com/` | [default](screenshots/words-dark-default.png) |
| Article | `https://words.getmatter.com/p/anu-coolhunt-before-sunrise-why-i` | [default](screenshots/article-dark-default.png), [full](screenshots/article-dark-full.png) |
| Docs | `https://docs.getmatter.com/` | [default](screenshots/docs-light-default.png), [full](screenshots/docs-light-full.png), [theme](screenshots/docs-light-theme.png) |
| Sign in | `https://web.getmatter.com/` | [default](screenshots/signin-light-default.png) |
| Home, phone | `https://www.getmatter.com/` | [default](screenshots/mobile-home-dark-default.png), [full](screenshots/mobile-home-dark-full.png) |
| Article, phone | `https://words.getmatter.com/p/anu-coolhunt-before-sunrise-why-i` | [default](screenshots/mobile-article-dark-default.png), [full](screenshots/mobile-article-dark-full.png) |
| Docs, phone | `https://docs.getmatter.com/` | [default](screenshots/mobile-docs-light-default.png) |
| Sign in, phone | `https://web.getmatter.com/` | [default](screenshots/mobile-signin-light-default.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Docs theme toggle | docs.getmatter.com | the theme button's own menu, then Light | [docs-light-theme](screenshots/docs-light-theme.png) |
| Subscribe gate | words.getmatter.com | the publication home is the gate; Subscribe was never pressed | [words-dark-default](screenshots/words-dark-default.png) |
| Sign-in card | web.getmatter.com | loaded signed out; OAuth never pressed; email focused, never filled, never submitted | [signin-light-default](screenshots/signin-light-default.png) |
| Consent overlays | marketing pages | hidden, never answered | hidden before every shot and reading |
| The reader app | web.getmatter.com behind sign-in | library, reader and settings need an account | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 11 components were given a real keyboard focus. 11 draw an outline ring: `nav-link` (1px auto #005fcc, offset 1px), `nav-signin` (1px auto #005fcc, offset 1px), `nav-cta` (1px auto #005fcc, offset 1px), `hero-cta` (1px auto #005fcc, offset 1px), `secondary-link` (1px auto #005fcc, offset 1px), `install-button` (1px auto #005fcc, offset 1px), `docs-tab` (1px auto #6366f1, offset 1px), `docs-search` (1px auto #6366f1, offset 0px), `apple-button` (2px solid #009efa, offset 2px), `footer-link` (1px auto #005fcc, offset 1px), `footer-cta` (1px auto #005fcc, offset 1px).

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.15s | `ease-out` | background-color, border-color, box-shadow, color, opacity, transform | apple-button, email-continue, email-field |
| 0.25s | `cubic-bezier(0.19, 1, 0.22, 1)` | background-color, border, border-radius, box-shadow, color, filter, opacity, outline, scale, stroke, transform | words-nav, words-subscribe |
| 0.3s | `ease` | filter | footer-cta, footer-link, hero-cta, install-button, m-cta, nav-cta, nav-link, nav-signin and more |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Get Matter pill](#get-matter-pill) | 95 x 32 | - | 100px | #6d7eec `color.blurple` | none | 0 |
| [Hero CTA](#hero-cta) | 134 x 48 | - | 100px | #6d7eec `color.blurple` | none | 0 |
| [Apple button](#apple-button) | 340 x 44 | - | 10px | #ffffff `color.white` | rgba(0, 0, 0, 0.2) 0px 0px 0px 1px inset, rgba(0, 0, 0, 0.04) 0px 1px 2px 0px | 0px 44px |
| [Google button](#google-button) | 340 x 48.4 | - | 4px | transparent | none | 0 |
| [Email field](#email-field) | 340 x 44 | 1px solid rgba(0, 0, 0, 0.2) | 10px | #ffffff `color.white` | none | 0px 50px 0px 14px |
| [Subscribe button](#subscribe-button) | 108.52 x 40 | 1px solid #020617 | 0px 8px 8px 0px | #020617 | none | 0px 20px |
| [Docs search](#docs-search) | 256 x 32 | 1px solid #f1f1f5 | 8px | #f5f5fa | none | 0px 8px |

## Components

### Shell and navigation

The marketing chrome on #0d0d0d: wordmark, gray nav links, a Sign In text link, and the blurple Get Matter pill.

#### Header
The 62px near-black top bar: wordmark, Overview, Developer, Words That Matter, X, Sign In and the blurple Get Matter pill. Read as `header` on the home page.

**Values (default).** size 1440 x 62; padding 15px; background #0d0d0d `color.black`; text MR-Camphor 17/normal 600, #ffffff `color.white`.

![Header default](components/crops/header-default.png)

#### Wordmark
The Matter lockup in the header. Read as `logo` on the home page.

**Values (default).** size 118.8 x 32; padding 0px 25px 0px 0px; border R: 1px solid rgba(255, 255, 255, 0.1); background transparent; text MR-Camphor 17/normal 600, #ffffff `color.white`; layers span.Nav_logoLockup__8R5pW 118.8x32.0 R:1px solid rgba(255, 255, 255, 0.1).

Child layers that carry the look: span 118.8x32 border 1px solid rgba(255, 255, 255, 0.1).

![Wordmark default](components/crops/logo-default.png)

#### Nav link
A header text link. Overview is the current item. Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 58.22 x 17; background transparent; text MR-Camphor 14/normal 400, #ffffff `color.white`; transition filter 0.3s ease |
| focus-visible | outline 1px auto #005fcc, offset 1px; layers a.Nav_active__NSFUZ 58.2x17.0 1px auto rgb(0, 95, 204) offset 1px |

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Sign-in link
The header Sign In link to web.getmatter.com. Measured, never followed. Read as `nav-signin` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 42.2 x 17; background transparent; text MR-Camphor 14/normal 400, #969698 `color.gray`; transition filter 0.3s ease |
| focus-visible | outline 1px auto #005fcc, offset 1px; layers a 42.2x17.0 1px auto rgb(0, 95, 204) offset 1px |

![Sign-in link default](components/crops/nav-signin-default.png) ![Sign-in link hover](components/crops/nav-signin-hover.png) ![Sign-in link focus-visible](components/crops/nav-signin-focus-visible.png) ![Sign-in link pressed](components/crops/nav-signin-pressed.png)

#### Get Matter pill
The small blurple App Store pill in the header. Measured, never followed. Read as `nav-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 95 x 32; radius 100px; background #6d7eec `color.blurple`; image linear-gradient(210.25deg, rgba(62, 70, 124, 0.2) 18.42%, rgba(255, 255, 255, 0) 75.82%), none; text MR-Camphor 14/36 500, #ffffff `color.white`; transition filter 0.3s ease |
| focus-visible | outline 1px auto #005fcc, offset 1px |

![Get Matter pill default](components/crops/nav-cta-default.png) ![Get Matter pill hover](components/crops/nav-cta-hover.png) ![Get Matter pill focus-visible](components/crops/nav-cta-focus-visible.png) ![Get Matter pill pressed](components/crops/nav-cta-pressed.png)

### Home hero

The Camphor headline, the gray lede, and the large Get Matter pill under it.

#### Hero headline
The Camphor display headline on the near-black hero. Read as `hero-h1` on the home page.

**Values (default).** size 850 x 80; background transparent; text MR-Camphor 80/80 700, #ffffff `color.white`.

![Hero headline default](components/crops/hero-h1-default.png)

#### Hero lede
The sentence under the headline. Read as `hero-lede` on the home page.

**Values (default).** size 850 x 84; background transparent; text MR-Camphor 20/28 400, #969698 `color.gray`.

![Hero lede default](components/crops/hero-lede-default.png)

#### Hero CTA
The large blurple Get Matter pill. Measured, never followed (it opens the App Store). Read as `hero-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 134 x 48; radius 100px; background #6d7eec `color.blurple`; image linear-gradient(210.25deg, rgba(62, 70, 124, 0.2) 18.42%, rgba(255, 255, 255, 0) 75.82%), none; text MR-Camphor 18/36 500, #ffffff `color.white`; transition filter 0.3s ease |
| focus-visible | outline 1px auto #005fcc, offset 1px |

![Hero CTA default](components/crops/hero-cta-default.png) ![Hero CTA hover](components/crops/hero-cta-hover.png) ![Hero CTA focus-visible](components/crops/hero-cta-focus-visible.png) ![Hero CTA pressed](components/crops/hero-cta-pressed.png)

#### Secondary link
The "Get the browser extension" text link under the hero CTA. Measured, never followed in this reading. Read as `secondary-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 216.73 x 19; background transparent; text MR-Camphor 16/normal 700, #6d7eec `color.blurple`; transition filter 0.3s ease; icon 16 x 14, #6d7eec `color.blurple` |
| focus-visible | outline 1px auto #005fcc, offset 1px; layers a.SecondaryLink_a__cZLT2 216.7x19.0 1px auto rgb(0, 95, 204) offset 1px |

![Secondary link default](components/crops/secondary-link-default.png) ![Secondary link hover](components/crops/secondary-link-hover.png) ![Secondary link focus-visible](components/crops/secondary-link-focus-visible.png) ![Secondary link pressed](components/crops/secondary-link-pressed.png)

### Home sections

Mid-page section headings and the footer quote.

#### Section heading
A Camphor section heading. Read as `section-h2` on the home page.

**Values (default).** size 650 x 140; background transparent; text MR-Camphor 60/70 700, #ffffff `color.white`.

![Section heading default](components/crops/section-h2-default.png)

#### Footer quote
The Ursula K. Le Guin line above the footer CTA. Read as `quote` on the home page.

**Values (default).** size 555.31 x 70; background transparent; text MR-Camphor 60/70 700, #ffffff `color.white`.

![Footer quote default](components/crops/quote-default.png)

### Words That Matter

The public Substack subscribe gate at words.getmatter.com. Subscribe was never pressed.

#### Publication title
The Words That Matter title on the public Substack subscribe gate. Subscribe was never pressed. Read as `words-h1` on the Words That Matter page.

**Values (default).** size 219 x 24; background transparent; text Lora 24/24 700, #363737.

![Publication title default](components/crops/words-h1-default.png)

#### Subscribe button
The publication Subscribe button on the gate. Measured at rest, never pressed (a press opens a sign-up). Read as `words-subscribe` on the Words That Matter page.

**Values (default).** size 108.52 x 40; padding 0px 20px; border 1px solid #020617; radius 0px 8px 8px 0px; background #020617; text system-ui 14/normal 500, #ffffff `color.white`; transition color 0.25s cubic-bezier(0.19, 1, 0.22, 1), background-color 0.25s cubic-bezier(0.19, 1, 0.22, 1), box-shadow 0.25s cubic-bezier(0.19, 1, 0.22, 1), border 0.25s cubic-bezier(0.19, 1, 0.22, 1), border-radius 0.25s cubic-bezier(0.19, 1, 0.22, 1), opacity 0.25s cubic-bezier(0.19, 1, 0.22, 1), filter 0.25s cubic-bezier(0.19, 1, 0.22, 1), stroke 0.25s cubic-bezier(0.19, 1, 0.22, 1), transform 0.25s cubic-bezier(0.19, 1, 0.22, 1), scale 0.25s cubic-bezier(0.19, 1, 0.22, 1), outline 0.25s cubic-bezier(0.19, 1, 0.22, 1); opacity 0.75.

![Subscribe button default](components/crops/words-subscribe-default.png)

#### Subscribe dismiss
The No thanks control on the subscribe gate. Measured at rest, never pressed. Read as `words-nav` on the Words That Matter page.

**Values (default).** size 132.17 x 40; padding 0px 16px; radius 8px; background rgba(255, 255, 255, 0); text system-ui 15/20 600, #757575; transition color 0.25s cubic-bezier(0.19, 1, 0.22, 1), background-color 0.25s cubic-bezier(0.19, 1, 0.22, 1), box-shadow 0.25s cubic-bezier(0.19, 1, 0.22, 1), border 0.25s cubic-bezier(0.19, 1, 0.22, 1), border-radius 0.25s cubic-bezier(0.19, 1, 0.22, 1), opacity 0.25s cubic-bezier(0.19, 1, 0.22, 1), filter 0.25s cubic-bezier(0.19, 1, 0.22, 1), stroke 0.25s cubic-bezier(0.19, 1, 0.22, 1), transform 0.25s cubic-bezier(0.19, 1, 0.22, 1), scale 0.25s cubic-bezier(0.19, 1, 0.22, 1), outline 0.25s cubic-bezier(0.19, 1, 0.22, 1); icon 20 x 20, #757575.

![Subscribe dismiss default](components/crops/words-nav-default.png)

### Docs

The public docs home at docs.getmatter.com. Search was never submitted. Get API Key was never followed.

#### Docs heading
The Matter Documentation heading on docs.getmatter.com. Read as `docs-h1` on the docs page.

**Values (default).** size 366.48 x 40; background transparent; text Inter 36/40 500, #19191e.

![Docs heading default](components/crops/docs-h1-default.png)

#### Docs tab
A top tab (API). Measured, never followed in this reading. Read as `docs-tab` on the docs page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 22.73 x 48; background transparent; text Inter 14/20 500, #535357 |
| hover | text Inter 14/20 500, #28282c; layers div.absolute.bottom-0 22.7x1.5 rgb(225, 225, 229) |
| focus-visible | outline 1px auto #6366f1, offset 1px; layers a.link.nav-tabs-item 22.7x48.0 1px auto rgb(99, 102, 241) offset 1px |
| pressed | text Inter 14/20 500, #28282c; layers div.absolute.bottom-0 22.7x1.5 rgb(225, 225, 229) |

![Docs tab default](components/crops/docs-tab-default.png) ![Docs tab hover](components/crops/docs-tab-hover.png) ![Docs tab focus-visible](components/crops/docs-tab-focus-visible.png) ![Docs tab pressed](components/crops/docs-tab-pressed.png)

#### Docs search
The Search button. Measured, never opened into a query. Read as `docs-search` on the docs page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 256 x 32; padding 0px 8px; border 1px solid #f1f1f5; radius 8px; background #f5f5fa; text Inter 14/20 400, #737377; icon 16 x 16, #737377 |
| hover | background #f1f1f5 |
| focus-visible | outline 1px auto #6366f1, offset 0px |
| pressed | background #f1f1f5 |

![Docs search default](components/crops/docs-search-default.png) ![Docs search hover](components/crops/docs-search-hover.png) ![Docs search focus-visible](components/crops/docs-search-focus-visible.png) ![Docs search pressed](components/crops/docs-search-pressed.png)

#### Docs API link
The API card or tab link. Measured, never followed in this reading. Read as `docs-card` on the docs page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 22.73 x 48; background transparent; text Inter 14/20 500, #535357 |
| hover | text Inter 14/20 500, #28282c; layers div.absolute.bottom-0 22.7x1.5 rgb(225, 225, 229) |

![Docs API link default](components/crops/docs-card-default.png) ![Docs API link hover](components/crops/docs-card-hover.png)

### Footer

The marketing footer: the quote, the Get Matter pill, and the legal row.

#### Footer
The marketing footer: quote, Get Matter, Terms, Privacy, X, Say hello. Read as `footer` on the home page.

**Values (default).** size 1440 x 900; background #0d0d0d `color.black`; text MR-Camphor 60/70 700, #ffffff `color.white`.

![Footer default](components/crops/footer-default.png)

#### Footer link
A footer text link. Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 50.88 x 19; background transparent; text MR-Camphor 16/normal 400, #969698 `color.gray`; transition filter 0.3s ease |
| focus-visible | outline 1px auto #005fcc, offset 1px; layers a 50.9x19.0 1px auto rgb(0, 95, 204) offset 1px |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Footer CTA
The footer Get Matter pill. Measured, never followed. Read as `footer-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 134 x 48; radius 100px; background #6d7eec `color.blurple`; image linear-gradient(210.25deg, rgba(62, 70, 124, 0.2) 18.42%, rgba(255, 255, 255, 0) 75.82%), none; text MR-Camphor 18/36 500, #ffffff `color.white`; transition filter 0.3s ease |
| focus-visible | outline 1px auto #005fcc, offset 1px |

![Footer CTA default](components/crops/footer-cta-default.png) ![Footer CTA hover](components/crops/footer-cta-hover.png) ![Footer CTA focus-visible](components/crops/footer-cta-focus-visible.png) ![Footer CTA pressed](components/crops/footer-cta-pressed.png)

### Mobile (390 wide)

The marketing home at phone width.

#### Mobile header
The header at 390px. Read as `m-header` on the home page at 390 wide.

**Values (default).** size 390 x 66; padding 15px 25px; background #0d0d0d `color.black`; text MR-Camphor 14/36 500, #ffffff `color.white`; icon 91.83 x 32, #ffffff `color.white`.

![Mobile header default](components/crops/m-header-default.png)

#### Mobile headline
The hero headline at 390px. Read as `m-hero` on the home page at 390 wide.

**Values (default).** size 340 x 50; background transparent; text MR-Camphor 40/50 700, #ffffff `color.white`.

![Mobile headline default](components/crops/m-hero-default.png)

#### Mobile CTA
The large Get Matter pill at 390px. Measured, never followed. Read as `m-cta` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 134 x 48; radius 100px; background #6d7eec `color.blurple`; image linear-gradient(210.25deg, rgba(62, 70, 124, 0.2) 18.42%, rgba(255, 255, 255, 0) 75.82%), none; text MR-Camphor 18/36 500, #ffffff `color.white`; transition filter 0.3s ease |

![Mobile CTA default](components/crops/m-cta-default.png) ![Mobile CTA hover](components/crops/m-cta-hover.png)

### Browser extension



#### Extension heading
The web-extension page heading. Read as `ext-h2` on the web extension page.

**Values (default).** size 650 x 140; background transparent; text MR-Camphor 60/70 700, #ffffff `color.white`.

![Extension heading default](components/crops/ext-h2-default.png)

#### Install button
An Install-on-Chrome/Safari/Firefox button. Measured, never followed. Read as `install-button` on the web extension page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 600 x 104; padding 20px; radius 30px; background #1e1f22 `color.dark-2`; text MR-Camphor 18/normal 700, #ffffff `color.white`; transition filter 0.3s ease; icon 10 x 16, #ffffff `color.white` |
| focus-visible | outline 1px auto #005fcc, offset 1px |

![Install button default](components/crops/install-button-default.png) ![Install button hover](components/crops/install-button-hover.png) ![Install button focus-visible](components/crops/install-button-focus-visible.png) ![Install button pressed](components/crops/install-button-pressed.png)

### Legal pages



#### Legal heading
A privacy-policy section heading. Read as `legal-h1` on the privacy page.

**Values (default).** size 1035 x 38; background transparent; text MR-Camphor 32/normal 700, #000000.

![Legal heading default](components/crops/legal-h1-default.png)

#### Legal body
A body paragraph on the privacy page. Read as `legal-body` on the privacy page.

**Values (default).** size 1035 x 48; background transparent; text MR-Camphor 17/24 400, #969698 `color.gray`.

![Legal body default](components/crops/legal-body-default.png)

### Public article



#### Article title
The published article headline, loaded signed out. Read as `article-h1` on the article page.

**Values (default).** size 728 x 72; background transparent; text Lora 32/36 600, #5d4c37.

![Article title default](components/crops/article-h1-default.png)

#### Byline link
The author byline link. Measured, never followed. Read as `article-byline` on the article page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 108.5 x 13; background transparent; text SF Compact 11/20 500, #5d4c37 |
| hover | text SF Compact 11/20 500, #5d4c37, underline |

![Byline link default](components/crops/article-byline-default.png) ![Byline link hover](components/crops/article-byline-hover.png)

#### Article paragraph
A body paragraph on the public article. Read as `article-body` on the article page.

**Values (default).** size 728 x 32; background transparent; text Lora 20/32 400, #5d4c37.

![Article paragraph default](components/crops/article-body-default.png)

### Sign-in card



#### Sign-in heading
The Welcome to Matter heading on the web reader sign-in card. Nothing was submitted. Read as `signin-h1` on the sign in page.

**Values (default).** size 199.56 x 30; background transparent; text -apple-system 24/30 600, rgba(0, 0, 0, 0.95) `color.content-400`.

![Sign-in heading default](components/crops/signin-h1-default.png)

#### Google button
Continue with Google (a Google identity widget). Measured, never pressed. Read as `google-button` on the sign in page.

**Values (default).** size 340 x 48.4; radius 4px; background transparent; text -apple-system 16/normal 400, rgba(0, 0, 0, 0.95) `color.content-400`; transform matrix(1, 0, 0, 1.1, 0, 0).

![Google button default](components/crops/google-button-default.png)

#### Apple button
Continue with Apple. Measured, never pressed. Read as `apple-button` on the sign in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 340 x 44; padding 0px 44px; radius 10px; background #ffffff `color.white`; shadow rgba(0, 0, 0, 0.2) 0px 0px 0px 1px inset, rgba(0, 0, 0, 0.04) 0px 1px 2px 0px; text -apple-system 14/normal 500, rgba(0, 0, 0, 0.95) `color.content-400`; transition background-color 0.15s ease-out, opacity 0.15s ease-out, transform 0.15s ease-out; icon 16 x 16, rgba(0, 0, 0, 0.95) `color.content-400` |
| hover | background rgba(245, 245, 245, 0.997961) |
| focus-visible | outline 2px solid #009efa, offset 2px |
| pressed | size 334.9 x 43.34; background rgba(245, 245, 245, 0.997961); transform scale(0.985); icon 15.76 x 15.76, rgba(0, 0, 0, 0.95) `color.content-400` |

![Apple button default](components/crops/apple-button-default.png) ![Apple button hover](components/crops/apple-button-hover.png) ![Apple button focus-visible](components/crops/apple-button-focus-visible.png) ![Apple button pressed](components/crops/apple-button-pressed.png)

#### Email field
The email field on the sign-in card. Focused only, never filled, never submitted. Read as `email-field` on the sign in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 340 x 44; padding 0px 50px 0px 14px; border 1px solid rgba(0, 0, 0, 0.2); radius 10px; background #ffffff `color.white`; text -apple-system 14/normal 400, rgba(0, 0, 0, 0.95) `color.content-400`; transition border-color 0.15s ease-out, box-shadow 0.15s ease-out, opacity 0.15s ease-out; placeholder rgba(0, 0, 0, 0.53) `color.content-200` |
| focused | border 1px solid rgba(0, 0, 0, 0.53) `color.content-200`; shadow rgba(0, 0, 0, 0.04) 0px 0px 0px 3px |

![Email field default](components/crops/email-field-default.png) ![Email field focused](components/crops/email-field-focused.png)

#### Email continue arrow
The arrow button beside the email field. Measured at rest, never pressed (a press would submit). Read as `email-continue` on the sign in page.

**Values (default).** size 32 x 32; radius 8px; background rgba(0, 0, 0, 0.04); text -apple-system 13.33/normal 400, rgba(0, 0, 0, 0.53) `color.content-200`; transition background-color 0.15s ease-out, color 0.15s ease-out, opacity 0.15s ease-out, transform 0.15s ease-out; icon 16 x 16, rgba(0, 0, 0, 0.53) `color.content-200`.

![Email continue arrow default](components/crops/email-continue-default.png)

#### Legal link
The Terms of Service link under the sign-in card. Read as `legal-link` on the sign in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 98.44 x 15; radius 3px; background transparent; text -apple-system 12.5/18 400, rgba(0, 0, 0, 0.75) `color.content-300` |
| hover | text -apple-system 12.5/18 400, rgba(0, 0, 0, 0.95) `color.content-400`, underline offset 2px |

![Legal link default](components/crops/legal-link-default.png) ![Legal link hover](components/crops/legal-link-hover.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the Matter wordmark, the Google and Apple glyphs, the phone mockups and the press logos) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

Matter's reader — library, highlights, settings, API keys — lives behind the sign-in card at web.getmatter.com and was never reached. Continue with Google and Continue with Apple were never pressed. The email field was focused and never filled. The arrow beside it was never pressed, so no form was submitted.

### Pages

- **The reader app.** Library, reader, settings and API keys need a sign-in and were never reached. web.getmatter.com was captured as the sign-in boundary.
- **Checkout.** Get Matter links to the App Store. That checkout was never followed.
- **Subscribe.** The publication home is a subscribe gate. Subscribe was never pressed, so the form was not submitted.
- **External links.** The Chrome Web Store install, X, and mailto links were measured, never followed.

### States

- **Pressed** on marketing controls was forced with DevTools, so a state a script adds on mousedown is uncaptured.
- **Disabled, error and loading states** were not seen on the public surface.
- **The Google button** was measured at rest only. Hover on that widget expands to the page, so hover was not recorded.

### Themes

The marketing site paints one near-black theme. A `.dark` class on the probe resolves the same `--mr-*` values. The light token set is the declared light colours used by the sign-in card and content roles, not a painted marketing inversion. Docs has its own light theme, captured by clicking the theme control.

### Fonts

- **MR-Camphor** is the measured face on the marketing headlines, body, navigation, and buttons, loaded from getmatter.com. The system stack is the sign-in card.

### Screenshots

- Phone mockups, press logos and the wordmark in the screenshots are the product's published content.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.
- The publication home has no `-full` shot. The gate is the page, and a full-page capture of it is a blank sheet.

### Content left out

- Marketing copy and the published article body are the product's content; only frames and components were measured.
