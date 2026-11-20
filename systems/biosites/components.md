# Bio Sites components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from biosites.com on 2026-11-11, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, claimed, sent or uploaded.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (29 components, 73 states).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Inter 14/21 500, #111827`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (70 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-light-{state}.png`: the site paints one light theme. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages (1x on desktop, 2x on mobile); mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png) |
| Claim (signed out) | `/editor` | [default](screenshots/claim-light-default.png), [full](screenshots/claim-light-full.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png) |
| Claim, phone | `/editor` | [default](screenshots/mobile-claim-light-default.png), [full](screenshots/mobile-claim-light-full.png) |

### Overlays and transient states

The public surface mounts none: the nav has no menu (the mobile bar just drops items, no hamburger exists), the FAQ is a static `<dl>` with always-visible answers, and the TrustArc consent container stays empty in this geo — nothing to open or dismiss was found.

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 12 components were given a real keyboard focus (a further 2 could not be driven: `footer-cta`, `claim-submit`). 2 show a visible focus state: `claim-login` (1px auto #005fcc `color.blue.focus`, offset 0px), `claim-legal` (1px auto #005fcc `color.blue.focus`, offset 1px). The other 10 show no change a keyboard user can see: `nav-link`, `nav-login`, `nav-signup`, `cta`, `section-nav-link`, `card-cta`, `footer-link`, `footer-legal`, `footer-social`, `m-signup`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover): the pills invert just like their hover (the nav pills and the CTA swap their fills). Nothing a real press would submit or follow was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.2s | `ease-out` | all | card-cta |
| 0.3s | `ease` | all | m-navbar, navbar |
| 0.3s | `linear` | background-color, border, color | cta, m-cta, m-signup, nav-link, nav-login, nav-signup |
| 0.5s | `ease-in-out` | opacity | section-nav-link |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Persona card](#persona-card) | 325 x 480 | - | 20px | #4f566f `color.slate.500` | none | 20px 60px 0px 60px |
| [CTA button](#cta-button) | 325 x 80 | 1px solid #010101 `color.ink.1` | 46px | #000000 `color.ink.0` | none | 10px 32px |
| [Card CTA](#card-cta) | 305 x 45.59 | - | 46px | rgba(0, 0, 0, 0.25) `color.alpha.ink25` | none | 14px |

## Components

### Shell and navigation

The fixed #navbar bar: the mark, the BLOG / LOG IN / SIGN UP FOR FREE pills.

#### Navbar
The fixed top bar (a #navbar div, not a header): the BIO.SITES mark left, BLOG / LOG IN / SIGN UP FOR FREE pills right. Read as `navbar` on the home page.

**Values (default).** size 1440 x 97; padding 40px 40px 0px 40px; radius 39px; background transparent; text Clarkson 12/13.2 500, #000000 `color.ink.0`; transition all 0.3s ease; icon 49 x 40, #000000 `color.ink.0`.

Child layers that carry the look: a 81.3x40 background #ffffff `color.white` radius 40px; a 88.8x40 background #ffffff `color.white` radius 40px; a 155.2x40 background #ffffff `color.white` radius 40px.

![Navbar default](components/crops/navbar-default.png)

#### Logo
The BIO.SITES wordmark and Squarespace tagline (svg inside the first nav anchor). Read as `logo` on the home page.

**Values (default).** size 203 x 57; background transparent; text sans-serif 16/normal 400, #000000 `color.ink.0`; icon 49 x 40, #000000 `color.ink.0`.

![Logo default](components/crops/logo-default.png)

#### Nav link
The BLOG pill, the only outbound item in the bar (text-transform renders "Blog" caps). Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 81.34 x 40; padding 0px 24px; radius 40px; background #ffffff `color.white`; text Clarkson 12/13.2 500, #000000 `color.ink.0`; transition background-color 0.3s linear, color 0.3s linear, border 0.3s linear |
| hover, pressed | background #000000 `color.ink.0`; text Clarkson 12/13.2 500, #ffffff `color.white` |

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Log in pill
The inverted pill linking to /editor?loginUser=true. Measured, never followed. Read as `nav-login` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 88.83 x 40; padding 0px 24px; radius 40px; background #ffffff `color.white`; text Clarkson 12/13.2 500, #000000 `color.ink.0`; transition background-color 0.3s linear, color 0.3s linear, border 0.3s linear |
| hover, pressed | background #000000 `color.ink.0`; text Clarkson 12/13.2 500, #ffffff `color.white` |

![Log in pill default](components/crops/nav-login-default.png) ![Log in pill hover](components/crops/nav-login-hover.png) ![Log in pill focus-visible](components/crops/nav-login-focus-visible.png) ![Log in pill pressed](components/crops/nav-login-pressed.png)

#### Sign up pill
The black "SIGN UP FOR FREE" pill linking to /editor. Measured, never followed. Read as `nav-signup` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 155.17 x 40; padding 0px 24px; radius 40px; background #ffffff `color.white`; text Clarkson 12/13.2 500, #000000 `color.ink.0`; transition background-color 0.3s linear, color 0.3s linear, border 0.3s linear |
| hover, pressed | background #000000 `color.ink.0`; text Clarkson 12/13.2 500, #ffffff `color.white` |

![Sign up pill default](components/crops/nav-signup-default.png) ![Sign up pill hover](components/crops/nav-signup-hover.png) ![Sign up pill focus-visible](components/crops/nav-signup-focus-visible.png) ![Sign up pill pressed](components/crops/nav-signup-pressed.png)

#### Page ground
The body fill: black under the hero collage; the content sections paint their own surfaces. Read as `page-ground` on the home page.

**Values (default).** size 1440 x 7535.8; background #000000 `color.ink.0`; text Clarkson 12/13.2 500, #000000 `color.ink.0`; icon 49 x 40, #000000 `color.ink.0`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

### Home

The hero under the dark collage band, the giant section links, the persona-card marquee and the static FAQ.

#### Hero title
"Your brand, your storefront, one link." under the dark collage band. Read as `hero-title` on the home page.

**Values (default).** size 355 x 70; background transparent; text Clarkson 35/35 500, #000000 `color.ink.0`.

![Hero title default](components/crops/hero-title-default.png)

#### Hero subcopy
Read as `hero-sub` on the home page.

**Values (default).** size 437 x 87; background transparent; text Clarkson 21/29 400, #6a6a6a `color.grey.106`.

![Hero subcopy default](components/crops/hero-sub-default.png)

#### CTA button
The black "Create a free Bio Site" pill repeated down the page; a real <button>. Measured, never pressed for real. Read as `cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 325 x 80; padding 10px 32px; border 1px solid #010101 `color.ink.1`; radius 46px; background #000000 `color.ink.0`; text Clarkson 21/23 400, #ffffff `color.white`; transition background-color 0.3s linear, color 0.3s linear, border 0.3s linear |
| hover, pressed | border 1px solid #e6e6e6 `color.grey.230`; background #ffffff `color.white`; text Clarkson 21/23 400, #010101 `color.ink.1` |

![CTA button default](components/crops/cta-default.png) ![CTA button hover](components/crops/cta-hover.png) ![CTA button focus-visible](components/crops/cta-focus-visible.png) ![CTA button pressed](components/crops/cta-pressed.png)

#### Section link
One of the STAND OUT / SELL / CONNECT / ANALYZE anchor links under the hero. Read as `section-nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 380.17 x 70; background transparent; text Clarkson 70/70 500, #ffffff `color.white`; transition opacity 0.5s ease-in-out |

Child layers that carry the look: a::before 10pxx10px background #ffffff `color.white` radius 50%.

![Section link default](components/crops/section-nav-link-default.png) ![Section link hover](components/crops/section-nav-link-hover.png) ![Section link focus-visible](components/crops/section-nav-link-focus-visible.png) ![Section link pressed](components/crops/section-nav-link-pressed.png)

#### Section title
Read as `section-title` on the home page.

**Values (default).** size 331.19 x 25.2; background transparent; text Clarkson 18/25.2 400, #010101 `color.ink.1`.

![Section title default](components/crops/section-title-default.png)

#### Eyebrow label
The "TRUSTED BY MILLIONS OF" small-caps label over the carousel. Read as `eyebrow` on the home page.

**Values (default).** size 417.59 x 23; background transparent; text Clarkson 18.72/normal 500, #000000 `color.ink.0`.

![Eyebrow label default](components/crops/eyebrow-default.png)

#### Persona card
A template card in the sliding carousel ("Health & Wellness", "Musician", …) with a "Get started ↗" link. Read as `persona-card` on the home page.

**Values (default).** size 325 x 480; padding 20px 60px 0px 60px; radius 20px; background #4f566f `color.slate.500`; text sans-serif 14/17 400, #ffffff `color.white`.

![Persona card default](components/crops/persona-card-default.png)

#### Card CTA
The "Get started ↗" link inside a persona card, straight to /editor (each state reads whichever card the marquee had in view; hover/pressed force :hover on the link and its card, because a pointer can never hold the moving card still). Measured, never followed. Read as `card-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 305 x 45.59; padding 14px; radius 46px; background rgba(0, 0, 0, 0.25) `color.alpha.ink25`; text Clarkson 16/17.6 400, #ffffff `color.white`; transition all 0.2s ease-out; opacity 0 |
| hover, pressed | transition all 0.2s ease-in; opacity 1 |

![Card CTA default](components/crops/card-cta-default.png) ![Card CTA hover](components/crops/card-cta-hover.png) ![Card CTA focus-visible](components/crops/card-cta-focus-visible.png) ![Card CTA pressed](components/crops/card-cta-pressed.png)

#### FAQ item
A question row of the static FAQ <dl>; answers are always painted, nothing to expand. Read as `faq-item` on the home page.

**Values (default).** size 316.86 x 29.41; background transparent; text Clarkson 21/29.4 400, #000000 `color.ink.0`.

![FAQ item default](components/crops/faq-item-default.png)

### Claim (signed-out editor)

The /editor redirect's claim screen: the username field pill, its circular submit and the Log In pill.

#### Claim title
"Claim your free username" on the signed-out /editor screen. Read as `claim-title` on the the signed-out claim screen (/editor) page.

**Values (default).** size 387.27 x 42; background transparent; text Clarkson 32/42 400, #1b1b1b `color.ink.27`.

![Claim title default](components/crops/claim-title-default.png)

#### Username field shell
The 50px-radius bordered pill holding the bio.site/ prefix, the input and the circular submit. Read as `claim-field-wrap` on the the signed-out claim screen (/editor) page.

**Values (default).** size 652 x 102; border 1px solid rgba(0, 0, 0, 0.2) `color.alpha.ink20`; radius 50px; background transparent; text Clarkson 36/22 400, #1b1b1b `color.ink.27`; icon 28 x 28, #e6e6e6 `color.grey.230`.

![Username field shell default](components/crops/claim-field-wrap-default.png)

#### Username field
The "bio.site/username" text input; a throwaway string was typed and deleted, nothing submitted. Read as `claim-field` on the the signed-out claim screen (/editor) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 357.94 x 44; padding 0px 10px 0px 0px; background transparent; text Clarkson 36/22 400, #000000 `color.ink.0`; placeholder #9c9c9c `color.grey.156` |

![Username field default](components/crops/claim-field-default.png) ![Username field focused](components/crops/claim-field-focused.png) ![Username field filled](components/crops/claim-field-filled.png)

#### Claim submit
The circular arrow button inside the field pill. Measured, never pressed for real — nothing was claimed. Read as `claim-submit` on the the signed-out claim screen (/editor) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 53 x 53; radius 100%; background #2a2a2a `color.ink.42`; text Clarkson 10/normal 400, #1b1b1b `color.ink.27`; opacity 0.2; icon 28 x 28, #e6e6e6 `color.grey.230` |

![Claim submit default](components/crops/claim-submit-default.png) ![Claim submit hover](components/crops/claim-submit-hover.png) ![Claim submit pressed](components/crops/claim-submit-pressed.png)

#### Log in button
The "Log In" pill top right of the claim screen. Measured, never pressed. Read as `claim-login` on the the signed-out claim screen (/editor) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 112.73 x 40; padding 0px 36px; radius 20px; background #ffffff `color.white`; shadow rgba(0, 0, 0, 0.24) 0px 20px 60px 0px; text Clarkson 14/normal 400, #1b1b1b `color.ink.27` |
| focus-visible | outline 1px auto #005fcc `color.blue.focus`, offset 0px |

![Log in button default](components/crops/claim-login-default.png) ![Log in button hover](components/crops/claim-login-hover.png) ![Log in button focus-visible](components/crops/claim-login-focus-visible.png) ![Log in button pressed](components/crops/claim-login-pressed.png)

#### Legal link
The Privacy Policy link in the claim footer (squarespace.com). Measured, never followed. Read as `claim-legal` on the the signed-out claim screen (/editor) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 63.92 x 12; background transparent; text Clarkson 10/12 400, #9c9c9c `color.grey.156` |
| focus-visible | outline 1px auto #005fcc `color.blue.focus`, offset 1px |

![Legal link default](components/crops/claim-legal-default.png) ![Legal link hover](components/crops/claim-legal-hover.png) ![Legal link focus-visible](components/crops/claim-legal-focus-visible.png) ![Legal link pressed](components/crops/claim-legal-pressed.png)

### Footer

The build-your-link marquee and the link columns.

#### Footer
The bottom band: a white outer band holding the "BUILD YOUR FREE LINK IN BIO PAGE" CTA, with near-black (rgb(1,1,1)) inner panels painting the BIO.SITE/YOURNAME marquee and the ABOUT/SUPPORT/CONTACT/LEGAL/SOCIAL link hub. Read as `footer` on the home page.

**Values (default).** size 1440 x 673.42; background #ffffff `color.white`; text Clarkson 18/19.8 500, #ffffff `color.white`; icon 49 x 40, #000000 `color.ink.0`.

![Footer default](components/crops/footer-default.png)

#### Footer marquee
The giant "BIO.SITE/YOURNAME ↗" call; its ancestor links to /editor. Measured, never followed. Read as `footer-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 776.55 x 98; background transparent; text Clarkson 70/98 500, #ffffff `color.white` |

![Footer marquee default](components/crops/footer-cta-default.png) ![Footer marquee hover](components/crops/footer-cta-hover.png) ![Footer marquee pressed](components/crops/footer-cta-pressed.png)

#### Footer link
An ABOUT column link (Squarespace). Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 106.81 x 23; background transparent; text Clarkson 18/29.4 400, #6a6a6a `color.grey.106` |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Legal link
Read as `footer-legal` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible) | size 123.16 x 22.41; background transparent; text Clarkson 16/22.4 400, #6a6a6a `color.grey.106` |
| pressed | text Clarkson 16/22.4 400, #ffffff `color.white` |

![Legal link default](components/crops/footer-legal-default.png) ![Legal link hover](components/crops/footer-legal-hover.png) ![Legal link focus-visible](components/crops/footer-legal-focus-visible.png) ![Legal link pressed](components/crops/footer-legal-pressed.png)

#### Social link
A SOCIAL column link (Instagram; TikTok is the same control). Read as `footer-social` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible) | size 76.09 x 22.41; background transparent; text Clarkson 16/22.4 400, #6a6a6a `color.grey.106` |
| pressed | text Clarkson 16/22.4 400, #ffffff `color.white` |

![Social link default](components/crops/footer-social-default.png) ![Social link hover](components/crops/footer-social-hover.png) ![Social link focus-visible](components/crops/footer-social-focus-visible.png) ![Social link pressed](components/crops/footer-social-pressed.png)

### Mobile (390 wide)

The same surface at phone width — no menu exists, the bar just shrinks.

#### Mobile navbar
The fixed bar at 390 wide: the circle-dot mark, BLOG and LOG IN text links, the black SIGN UP pill. No menu trigger exists. Read as `m-navbar` on the home page at 390 wide.

**Values (default).** size 390 x 64; padding 12px 16px; background #ffffff `color.white`; shadow rgba(0, 0, 0, 0.12) 0px 20px 60px 0px; text Clarkson 12/13.2 500, #000000 `color.ink.0`; transition all 0.3s ease; icon 43 x 36, #000000 `color.ink.0`.

![Mobile navbar default](components/crops/m-navbar-default.png)

#### Mobile sign up pill
The black SIGN UP pill, the mobile bar's only button. Measured, never followed. Read as `m-signup` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 78.61 x 40; padding 0px 15px; radius 40px; background #000000 `color.ink.0`; wrapper div.index_navbar__7al9c.index_scrolled__JL789: shadow rgba(0, 0, 0, 0.12) 0px 20px 60px 0px; text Clarkson 12/13.2 500, #ffffff `color.white`; transition background-color 0.3s linear, color 0.3s linear, border 0.3s linear |
| hover, pressed | background #ffffff `color.white`; text Clarkson 12/13.2 500, #000000 `color.ink.0` |

![Mobile sign up pill default](components/crops/m-signup-default.png) ![Mobile sign up pill hover](components/crops/m-signup-hover.png) ![Mobile sign up pill focus-visible](components/crops/m-signup-focus-visible.png) ![Mobile sign up pill pressed](components/crops/m-signup-pressed.png)

#### Mobile CTA
The "Create a free Bio Site" button at 390 wide. Read as `m-cta` on the home page at 390 wide.

**Values (default).** size 325 x 64; padding 10px 32px; border 1px solid #010101 `color.ink.1`; radius 46px; background #000000 `color.ink.0`; text Clarkson 16/23 400, #ffffff `color.white`; transition background-color 0.3s linear, color 0.3s linear, border 0.3s linear.

![Mobile CTA default](components/crops/m-cta-default.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the arrow in the claim submit, the social glyphs) are Bio Sites' artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### Pages

- **The app behind sign-in.** The editor and a Bio Sites account sit behind /editor and were never signed into; only the signed-out claim screen it redirects to was measured, never used.
- **Anything that sends, claims or signs in.** The username field was never submitted, no claim was started, no link was followed, and no account was created.
- **The blog** (blog.biosites.com) and the help desk (help.unfold.com) are separate properties, not part of this capture.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing. The card-cta's hover is CDP-forced too — the JS marquee never holds the card still for a pointer.
- **Disabled, error and loading states** were not seen on the public surface.

### Themes

The public routes paint one light theme — white sections over a black body (the hero collage and marquee bands are dark inside it). No dark variant is declared anywhere: the stylesheets carry no design-token custom properties at all, so every colour in tokens.json is a measurement, not a variable resolution.

### Fonts

- **The site fonts** are webfonts declared in the bundle (Clarkson 400/500 for nearly everything, Canela light + italic for display accents; `fonts` in [raw/css-vars.json](raw/css-vars.json)); the font files themselves are not committed.
- Illustration and wordmark artwork in the screenshots are Bio Sites' property.

### Screenshots

- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- The persona photography, the template previews and the BIO.SITES wordmark are Squarespace's content; only the frames and components were measured.
