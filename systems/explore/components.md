# Explore components

The discovery list of every page and view captured, then one entry per component with crops of the real product and the Gaps. Captured on 2026-11-14 by replaying the archived 2023-02-23 explore.family build from a local Internet Archive mirror (the product closed 2023-04-19 and the domain later lapsed), signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, created, sent or uploaded.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (57 components, 104 states). The mined stylesheet is [raw/css-declarations.json](raw/css-declarations.json).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `UntitledSans 14/20 400, #262626`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the replayed page, in [components/crops/](components/crops) (102 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-light-{state}.png` (Explore shows one fixed light theme signed out). Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home. Grey header and hero with the positioning sentence and feature tags, then the feed preview. | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png) |
| Discover. Intro line, category pills and the 3-up post grid from the archived feed API. | `/discover` | [default](screenshots/discover-light-default.png), [full](screenshots/discover-light-full.png) |
| Login. The split auth screen: welcome panel left, email/password + "Log in" submit right. | `/login` | [default](screenshots/login-light-default.png), [full](screenshots/login-light-full.png) |
| Register. Same split with the newsletter checkbox, the terms/privacy line and the dark "Sign up" submit. | `/register` | [default](screenshots/register-light-default.png), [full](screenshots/register-light-full.png) |
| Forgot password. Intro copy, the email field and the reset submit. | `/forgot-password` | [default](screenshots/forgot-password-light-default.png), [full](screenshots/forgot-password-light-full.png) |
| About. The marketing pitch: features, "no numbers", "no algorithms", portfolio and domain CTAs. | `/about` | [default](screenshots/about-light-default.png), [full](screenshots/about-light-full.png) |
| Terms of Service, effective 2022-09-27. | `/terms` | [default](screenshots/terms-light-default.png), [full](screenshots/terms-light-full.png) |
| Privacy Policy, effective 2022-09-27. | `/privacy` | [default](screenshots/privacy-light-default.png), [full](screenshots/privacy-light-full.png) |
| Code of Conduct. Its illustration was not archived and renders absent. | `/conduct` | [default](screenshots/conduct-light-default.png), [full](screenshots/conduct-light-full.png) |
| The June 2023 closure announcement shell (2023-06-08 snapshot): the product closed on 2023-04-19. | `/` | [default](screenshots/announcement-light-default.png), [full](screenshots/announcement-light-full.png) |
| A member profile as the SPA renders it signed out: the shell only, because the member API records were never archived. | `/sawdust` | [default](screenshots/profile-shell-light-default.png) |
| A post permalink as the SPA renders it: the shell only, same missing-API reason. | `/p/2193` | [default](screenshots/post-shell-light-default.png) |
| Malika Favre's profile from the archived server-rendered HTML, replayed with JavaScript disabled. | `/malikafavre` | [default](screenshots/ssr-profile-malika-light-default.png), [full](screenshots/ssr-profile-malika-light-full.png) |
| Sawdust's profile, same server-rendered evidence. | `/sawdust` | [default](screenshots/ssr-profile-sawdust-light-default.png), [full](screenshots/ssr-profile-sawdust-light-full.png) |
| Home at 390: the 56px header, "Sign up free" only, hero and feed. | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png) |
| Discover at 390: pill row and full-width post cards. | `/discover` | [default](screenshots/mobile-discover-light-default.png), [full](screenshots/mobile-discover-light-full.png) |
| Login at 390. | `/login` | [default](screenshots/mobile-login-light-default.png), [full](screenshots/mobile-login-light-full.png) |
| Register at 390. | `/register` | [default](screenshots/mobile-register-light-default.png) |

### Archive boundaries

| Surface | What was reached | Captured |
|---|---|---|
| SPA profile `/sawdust` | the app shell only: the `/user/*` API records were never archived, so the router renders an unauthenticated empty state | [profile-shell-light-default](screenshots/profile-shell-light-default.png) |
| SPA post `/p/2193` | the app shell only: `/post/single/*` was never archived | [post-shell-light-default](screenshots/post-shell-light-default.png) |
| Server-rendered profiles | the archived SSR HTML for /malikafavre, /sawdust and /burnttoast, replayed with JavaScript disabled | [ssr-profile-malika-light-default](screenshots/ssr-profile-malika-light-default.png), [ssr-profile-sawdust-light-default](screenshots/ssr-profile-sawdust-light-default.png) |
| Closure announcement | the 2023-06-08 archive snapshot of the signed-out shell after the 2023-04-19 shutdown | [announcement-light-default](screenshots/announcement-light-default.png) |
| Missing media | grey placeholders where MP4/GIF/WebP uploads were not archived; misses are recorded per capture in the `.capture.json` sidecars | [discover-light-full](screenshots/discover-light-full.png) |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 10 components were given a real keyboard focus. 4 draw a ring: `nav-signin` (1px auto #101010, offset 1px), `hero-tag-cta` (1px auto #101010, offset 1px), `forgot-link` (1px auto #101010, offset 1px), `signup-link` (1px auto #101010, offset 1px). The other 6 draw none, so a keyboard user sees no change: `nav-signup`, `login-submit`, `reg-submit`, `forgot-submit`, `about-cta`, `m-signup`. Focus could not be moved onto 2 controls — `pill`, `pill-idle` — so their focus appearance is a capture gap, not a measurement.

**Pressed.** Explore's controls do not redraw on press; the measured `pressed` states match their defaults, so the entries read "same". Hovers recolour text and borders over the shared 0.2s transition rather than repainting backgrounds.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.2s | `ease` | all, color, opacity | about-cta, auth-logo, forgot-link, forgot-submit, hero-tag-cta, login-submit, m-pill, m-post and more |

**Layout.** The fixed header is 60px (56px at 390) at z-index 300; content sits in a 1640px-max column with 20px gutters. The feed lays its cards out at `calc(33.3333% - .5px)` wide with 15px side padding and a 50px row pitch on the white page; at 390 each card is full width. A fixed alert tray sits bottom-left at z-index 2000.

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Post card](#post-card) | 476 x 488.5 | - | - | #5a5958 (div.media.media--image) | none | 0px 15px 50px 15px |
| [Auth layout](#auth-layout) | 1440 x 900 | - | - | #717171 `color.grey.700` (div.auth__left) | none | 0 |
| [Feature card](#feature-card) | 511 x 371 | - | 7px | #f4f4f4 | none | 24px 40px 38px 40px |
| [Email field](#email-field) | 388 x 20 | - | - | #ffffff `color.white` | none | 0 |
| [Log in button](#log-in-button) | 424 x 47 | - | 7px | #262626 `color.grey.950` | none | 14px 25px |
| [Sign up button](#sign-up-button) | 424 x 47 | - | 7px | #262626 `color.grey.950` | none | 14px 25px |
| [Category pill (active)](#category-pill-active) | 47 x 36 | 2px solid #262626 `color.grey.950` | 20px | transparent | none | 5px 12px 6px 12px |
| [Hero tag CTA](#hero-tag-cta) | 137 x 46 | 1px solid #b7b7b7 `color.grey.450` | 7px | transparent | none | 11px 23px |
| [SSR post tile](#ssr-post-tile) | 58.16 x 264.08 | - | 34px (div.post__author-image) | #9d9d9d `color.grey.500` (div.post__author-image) | none | 0px 15px 50px 15px |
| [Mobile post card](#mobile-post-card) | 390 x 448.5 | - | - | #5a5958 (div.media.media--image) | none | 0px 0px 40px 0px |
| [Footer](#footer) | 990 x 585 | - | - | transparent | none | 130px 0px 175px 0px |

## Components

### Auth forms

The marketing chrome (fixed 60px grey header, E wordmark, Sign in + yellow "Sign up free") and the split auth screen: a community welcome over a darker `#717171` grey panel at the left, a ~424px form column at the right. Email/password fields are 8px-radius hairline inputs; all three submits ("Log in", "Sign up", "Reset Password") are the same full-width dark `#262626` button with 7px corners. Fields were focused and filled for measurement, then cleared; nothing was submitted.

#### Site header
The fixed grey top bar: logo left, "Sign in" link and yellow "Sign up free" pill right. Read as `mkt-header` on the forgot password page.

**Values (default).** size 1440 x 60; background #9d9d9d `color.grey.500`; text UntitledSans 16/22 400, #ffffff `color.white`.

![Site header default](components/crops/mkt-header-default.png)

#### Logo
The Explore wordmark (inline svg) in the header, linking home. Read as `mkt-logo` on the forgot password page.

**Values (default).** size 27 x 31; background transparent; text UntitledSans 16/0 400, #262626 `color.grey.950`; transition color 0.2s ease; transform translate(-13.5px, -15.5px); icon 27 x 31, #ffffff `color.white`.

![Logo default](components/crops/mkt-logo-default.png)

#### Sign in link
The "Sign in" header link; measured, never followed. Read as `nav-signin` on the forgot password page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 52 x 22; background transparent; text UntitledSans 16/22 400, #ffffff `color.white`; transition color 0.2s ease |
| focus-visible | outline 1px auto #101010, offset 1px |

![Sign in link default](components/crops/nav-signin-default.png) ![Sign in link hover](components/crops/nav-signin-hover.png) ![Sign in link focus-visible](components/crops/nav-signin-focus-visible.png) ![Sign in link pressed](components/crops/nav-signin-pressed.png)

#### Sign up pill
The yellow "Sign up free" pill (btn--yellow btn--rounded btn--small); measured, never followed. Read as `nav-signup` on the forgot password page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 121 x 38; padding 9px 16px 10px 16px; radius 50px; background #ffc60a `color.accent.DEFAULT`; text UntitledSans 16/19 400, #262626 `color.grey.950`; transition all 0.2s ease |
| hover, focus-visible, pressed | background #ffcc24 `color.accent.hover` |

![Sign up pill default](components/crops/nav-signup-default.png) ![Sign up pill hover](components/crops/nav-signup-hover.png) ![Sign up pill focus-visible](components/crops/nav-signup-focus-visible.png) ![Sign up pill pressed](components/crops/nav-signup-pressed.png)

#### Auth layout
The split auth screen: community welcome on the left, the form panel on the right. Read as `auth-panel` on the login page.

**Values (default).** size 1440 x 900; background transparent; text UntitledSans 16/22 400, #c1c1c1 `color.grey.400`.

Child layers that carry the look: div 720x900 background #717171 `color.grey.700`; div 424x73 border 1px solid radius 8px; input 388x20 background #ffffff `color.white`.

![Auth layout default](components/crops/auth-panel-default.png)

#### Welcome quote
The left welcome panel: "Remember we are a community…" over the looping animation. Read as `auth-quote` on the login page.

**Values (default).** size 720 x 900; padding 60px; background #717171 `color.grey.700`; text UntitledSans 16/22 400, #c1c1c1 `color.grey.400`.

![Welcome quote default](components/crops/auth-quote-default.png)

#### Auth logo
The Explore logo above the form. Read as `auth-logo` on the login page.

**Values (default).** size 424 x 28; background transparent; text UntitledSans 16/22 400, #262626 `color.grey.950`; transition color 0.2s ease.

![Auth logo default](components/crops/auth-logo-default.png)

#### Auth heading
"Welcome back to Explore! / Log in to your account" — the form intro. Read as `auth-heading` on the login page.

**Values (default).** size 330 x 50; background transparent; text UntitledSans 21/25 400, #262626 `color.grey.950`.

![Auth heading default](components/crops/auth-heading-default.png)

#### Email field
The Email input; focused and typed into then cleared — never submitted. Read as `field-email` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 388 x 20; background #ffffff `color.white`; text UntitledSans 16/20 400, #262626 `color.grey.950`; placeholder #262626 `color.grey.950` |

![Email field default](components/crops/field-email-default.png) ![Email field focused](components/crops/field-email-focused.png) ![Email field filled](components/crops/field-email-filled.png)

#### Password field
The Password input with the visibility eye; typed into and cleared, never submitted. Read as `field-password` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 388 x 20; padding 0px 34px 0px 0px; background #ffffff `color.white`; text UntitledSans 16/20 400, #262626 `color.grey.950`; placeholder #9d9d9d `color.grey.500` |

![Password field default](components/crops/field-password-default.png) ![Password field focused](components/crops/field-password-focused.png) ![Password field filled](components/crops/field-password-filled.png)

#### Password visibility eye
The eye icon that toggles password visibility — a local UI toggle, pressed for nothing else. Read as `password-eye` on the login page.

**Values (default).** size 16 x 16; background transparent; text UntitledSans 16/22 400, #d0d0d0 `color.grey.300`; transform translate(0px, -8px); icon 16 x 16, #d0d0d0 `color.grey.300`.

![Password visibility eye default](components/crops/password-eye-default.png)

#### Log in button
The full-width "Log in" submit (btn--full); states measured, never clicked — nothing was submitted. Read as `login-submit` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 424 x 47; padding 14px 25px; radius 7px; background #262626 `color.grey.950`; text UntitledSans 16/normal 400, #ffffff `color.white`; transition all 0.2s ease |
| hover, focus-visible, pressed | background #333333 `color.grey.800` |

![Log in button default](components/crops/login-submit-default.png) ![Log in button hover](components/crops/login-submit-hover.png) ![Log in button focus-visible](components/crops/login-submit-focus-visible.png) ![Log in button pressed](components/crops/login-submit-pressed.png)

#### Forgot password link
The "Forgot your password?" link under the submit; measured, never followed. Read as `forgot-link` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 169 x 22; background transparent; text UntitledSans 16/22 400, #9d9d9d `color.grey.500`; transition color 0.2s ease |
| hover | text UntitledSans 16/22 400, #262626 `color.grey.950` |
| focus-visible | outline 1px auto #101010, offset 1px; text UntitledSans 16/22 400, #262626 `color.grey.950` |
| pressed | text UntitledSans 16/22 400, #262626 `color.grey.950` |

![Forgot password link default](components/crops/forgot-link-default.png) ![Forgot password link hover](components/crops/forgot-link-hover.png) ![Forgot password link focus-visible](components/crops/forgot-link-focus-visible.png) ![Forgot password link pressed](components/crops/forgot-link-pressed.png)

#### Sign up link
The "Sign up free" link under the submit; measured, never followed. Read as `signup-link` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 89 x 19; background transparent; text UntitledSans 16/22 400, #262626 `color.grey.950`; transition color 0.2s ease |
| focus-visible | outline 1px auto #101010, offset 1px |

![Sign up link default](components/crops/signup-link-default.png) ![Sign up link hover](components/crops/signup-link-hover.png) ![Sign up link focus-visible](components/crops/signup-link-focus-visible.png) ![Sign up link pressed](components/crops/signup-link-pressed.png)

#### Register heading
The sign-up form intro. Read as `reg-heading` on the register page.

**Values (default).** size 720 x 900; padding 60px; background transparent; text UntitledSans 14/17 400, #9d9d9d `color.grey.500`.

Child layers that carry the look: div 424x73 border 1px solid radius 8px; input 388x20 background #ffffff `color.white`; div 424x73 border 1px solid radius 8px.

![Register heading default](components/crops/reg-heading-default.png)

#### Email field (register)
The Email input; typed into and cleared, never submitted. Read as `reg-field-email` on the register page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 388 x 20; background #ffffff `color.white`; text UntitledSans 16/20 400, #262626 `color.grey.950`; placeholder #262626 `color.grey.950` |

![Email field (register) default](components/crops/reg-field-email-default.png) ![Email field (register) focused](components/crops/reg-field-email-focused.png) ![Email field (register) filled](components/crops/reg-field-email-filled.png)

#### Password field (register)
The Password input; typed into and cleared, never submitted. Read as `reg-field-password` on the register page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 388 x 20; padding 0px 34px 0px 0px; background #ffffff `color.white`; text UntitledSans 16/20 400, #262626 `color.grey.950`; placeholder #9d9d9d `color.grey.500` |

![Password field (register) default](components/crops/reg-field-password-default.png) ![Password field (register) focused](components/crops/reg-field-password-focused.png) ![Password field (register) filled](components/crops/reg-field-password-filled.png)

#### Newsletter checkbox
The "Subscribe to newsletter (no spam…)" checkbox; measured, never toggled. Read as `newsletter-check` on the register page.

**Values (default).** size 424 x 28; background transparent; text UntitledSans 16/28 400, #9d9d9d `color.grey.500`.

Child layers that carry the look: label::before 17pxx17px border 1px solid radius 6px.

![Newsletter checkbox default](components/crops/newsletter-check-default.png)

#### Terms agreement line
"By clicking Sign up, I agree to Terms of Service and Privacy Policy." Read as `terms-line` on the register page.

**Values (default).** size 424 x 92; background transparent; text UntitledSans 16/28 400, #9d9d9d `color.grey.500`.

Child layers that carry the look: label::before 17pxx17px border 1px solid radius 6px.

![Terms agreement line default](components/crops/terms-line-default.png)

#### Sign up button
The "Sign up" submit; states measured, never clicked — nothing was submitted. Read as `reg-submit` on the register page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 424 x 47; padding 14px 25px; radius 7px; background #262626 `color.grey.950`; text UntitledSans 16/normal 400, #ffffff `color.white`; transition all 0.2s ease |
| hover, focus-visible, pressed | background #333333 `color.grey.800` |

![Sign up button default](components/crops/reg-submit-default.png) ![Sign up button hover](components/crops/reg-submit-hover.png) ![Sign up button focus-visible](components/crops/reg-submit-focus-visible.png) ![Sign up button pressed](components/crops/reg-submit-pressed.png)

#### Reset intro
"Please enter your email address and you will receive a link…" Read as `forgot-intro` on the forgot password page.

**Values (default).** size 720 x 900; padding 60px; background transparent; text UntitledSans 21/25 400, #262626 `color.grey.950`.

Child layers that carry the look: div 424x73 border 1px solid radius 8px; input 388x20 background #ffffff `color.white`; button 424x47 background #262626 `color.grey.950` radius 7px.

![Reset intro default](components/crops/forgot-intro-default.png)

#### Email field (reset)
The Email input on the reset form; typed into and cleared, never submitted. Read as `forgot-field` on the forgot password page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 388 x 20; background #ffffff `color.white`; text UntitledSans 16/20 400, #262626 `color.grey.950`; placeholder #262626 `color.grey.950` |

![Email field (reset) default](components/crops/forgot-field-default.png) ![Email field (reset) focused](components/crops/forgot-field-focused.png) ![Email field (reset) filled](components/crops/forgot-field-filled.png)

#### Reset button
The "Reset Password" submit; states measured, never clicked. Read as `forgot-submit` on the forgot password page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 424 x 47; padding 14px 25px; radius 7px; background #262626 `color.grey.950`; text UntitledSans 16/normal 400, #ffffff `color.white`; transition all 0.2s ease |
| hover, focus-visible, pressed | background #333333 `color.grey.800` |

![Reset button default](components/crops/forgot-submit-default.png) ![Reset button hover](components/crops/forgot-submit-hover.png) ![Reset button focus-visible](components/crops/forgot-submit-focus-visible.png) ![Reset button pressed](components/crops/forgot-submit-pressed.png)

### Home (marketing + feed)

The signed-out home page: the LabilGrotesk-Medium positioning sentence over the grey hero with hairline feature tags, then a feed preview.

#### Hero section
The home hero: "Welcome" greeting, the positioning sentence and the feature tags, over the testimonial imagery. Read as `hero` on the home page.

**Values (default).** size 1440 x 680; border T: 1px solid #b7b7b7 `color.grey.450`; background #9d9d9d `color.grey.500`; text UntitledSans 16/22 400, #e0e0e0.

![Hero section default](components/crops/hero-default.png)

#### Hero greeting
The "Welcome" greeting at the top of the hero. Read as `hero-welcome` on the home page.

**Values (default).** size 1400 x 22; background transparent; text UntitledSans 16/22 400, #e0e0e0.

![Hero greeting default](components/crops/hero-welcome-default.png)

#### Hero headline
"Explore is an emotionally intelligent ad-free social media platform…" — the display sentence. Read as `hero-title` on the home page.

**Values (default).** size 1082 x 123; background transparent; text LabilGrotesk-Medium 40/41 400, #ffffff `color.white`.

![Hero headline default](components/crops/hero-title-default.png)

#### Hero tag
A feature tag in the hero tag list (Free / For creatives / No ads…). Read as `hero-tag` on the home page.

**Values (default).** size 82 x 46; padding 11px 23px; border 1px solid #b7b7b7 `color.grey.450`; radius 7px; background transparent; text UntitledSansMedium 16/22 400, #ffffff `color.white`.

![Hero tag default](components/crops/hero-tag-default.png)

#### Hero tag CTA
The "All features" tag link; measured, never followed. Read as `hero-tag-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 137 x 46; padding 11px 23px; border 1px solid #b7b7b7 `color.grey.450`; radius 7px; background transparent; text UntitledSansMedium 16/22 400, #ffffff `color.white`; transition color 0.2s ease |
| focus-visible | outline 1px auto #101010, offset 1px |

![Hero tag CTA default](components/crops/hero-tag-cta-default.png) ![Hero tag CTA hover](components/crops/hero-tag-cta-hover.png) ![Hero tag CTA focus-visible](components/crops/hero-tag-cta-focus-visible.png) ![Hero tag CTA pressed](components/crops/hero-tag-cta-pressed.png)

#### Feed section
The post feed below the hero (the same card grid as /discover). Read as `feed-section` on the home page.

**Values (default).** size 1440 x 679; padding 0px 20px; background transparent; text UntitledSans 16/22 400, #e0e0e0.

Child layers that carry the look: div 446.7x230 border 1px solid radius 7px; div 446.7x230 border 1px solid radius 7px; div 446.7x230 border 1px solid radius 7px.

![Feed section default](components/crops/feed-section-default.png)

### Discover feed

`/discover`: an intro line, a row of category pills (hairline idle, ink-bordered active) and the 3-up post grid, fed by the archived `/discover` API records. Some post media was not archived and renders as the grey placeholder.

#### Discover heading
"Browse inspiring work on Explore curated by our team" — the page heading above the feed. Read as `discover-title` on the Discover page.

**Values (default).** size 300 x 44; background transparent; text UntitledSans 16/22 400, #9d9d9d `color.grey.500`.

![Discover heading default](components/crops/discover-title-default.png)

#### Category pill row
The scrollable category pills row (All / 3D Design / Animation / Art…). Read as `pill-row` on the Discover page.

**Values (default).** size 1000 x 90; background transparent; text UntitledSans 16/21 400, #262626 `color.grey.950`.

Child layers that carry the look: a 47x36 border 2px solid radius 20px; a 106x36 border 1px solid radius 20px; a 106x36 border 1px solid radius 20px.

![Category pill row default](components/crops/pill-row-default.png)

#### Category pill (active)
The selected "All" category pill; measured, never followed. Read as `pill` on the Discover page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 47 x 36; padding 5px 12px 6px 12px; border 2px solid #262626 `color.grey.950`; radius 20px; background transparent; text UntitledSans 16/21 400, #262626 `color.grey.950`; transition color 0.2s ease |

![Category pill (active) default](components/crops/pill-default.png) ![Category pill (active) hover](components/crops/pill-hover.png) ![Category pill (active) pressed](components/crops/pill-pressed.png)

#### Category pill
An unselected category pill; measured, never followed. Read as `pill-idle` on the Discover page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 106 x 36; padding 6px 13px 7px 13px; border 1px solid #efefef `color.grey.100`; radius 20px; background transparent; text UntitledSans 16/21 400, #262626 `color.grey.950`; transition color 0.2s ease |

![Category pill default](components/crops/pill-idle-default.png) ![Category pill hover](components/crops/pill-idle-hover.png) ![Category pill pressed](components/crops/pill-idle-pressed.png)

#### Post card
A feed post card: gallery tile on top, author row and title below. Read as `post-card` on the Discover page.

**Values (default).** size 476 x 488.5; padding 0px 15px 50px 15px; background transparent; text UntitledSansMedium 16/22 400, #262626 `color.grey.950`; transition opacity 0.2s ease; icon 22 x 8, #ffffff `color.white`.

Child layers that carry the look: div 446x334.5 background #5a5958; div::after 446pxx334.5px background rgba(0, 0, 0, 0.02); div 37x20 background #262626 `color.grey.950` radius 30px.

![Post card default](components/crops/post-card-default.png)

#### Post gallery
The media tile of a feed card (post__gallery--rounded); images or a video poster. Read as `post-gallery` on the Discover page.

**Values (default).** size 446 x 334.5; radius 7px; background transparent; text UntitledSans 16/22 400, #262626 `color.grey.950`.

Child layers that carry the look: div 446x334.5 background #5a5958; div::after 446pxx334.5px background rgba(0, 0, 0, 0.02).

![Post gallery default](components/crops/post-gallery-default.png)

#### Post author row
The author line under a card: avatar, name, age ("4yr"). Read as `post-author` on the Discover page.

**Values (default).** size 446 x 28; background transparent; text UntitledSansMedium 16/22 400, #262626 `color.grey.950`; icon 22 x 8, #ffffff `color.white`.

Child layers that carry the look: div 37x20 background #262626 `color.grey.950` radius 30px.

![Post author row default](components/crops/post-author-default.png)

#### Author avatar
The round author avatar on a feed card (post__author-image--blank when empty). Read as `post-avatar` on the Discover page.

**Values (default).** size 28 x 28; radius 34px; background transparent; text UntitledSansMedium 16/22 400, #262626 `color.grey.950`.

![Author avatar default](components/crops/post-avatar-default.png)

#### Post title
The work title under a card. Read as `post-title` on the Discover page.

**Values (default).** size 446 x 22; padding 0px 30px 0px 41px; background transparent; text UntitledSans 16/22 400, #262626 `color.grey.950`.

![Post title default](components/crops/post-title-default.png)

#### Post actions
The action icon row on a card (appreciate/save/comment affordances). Read as `post-actions` on the Discover page.

**Values (default).** size 458 x 30; padding 0px 0px 0px 41px; background transparent; text UntitledSans 16/22 400, #262626 `color.grey.950`; icon 16 x 16, #9d9d9d `color.grey.500`.

![Post actions default](components/crops/post-actions-default.png)

#### Carousel next arrow
The next-arrow on a multi-image post carousel. Read as `carousel-next` on the Discover page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 24 x 24; padding 8px; radius 24px; background rgba(113, 113, 113, 0.3) `color.overlay.header-dim`; text system 13.33/normal 400, #ffffff `color.white`; icon 8 x 11, #ffffff `color.white` |

![Carousel next arrow default](components/crops/carousel-next-default.png) ![Carousel next arrow hover](components/crops/carousel-next-hover.png)

### About / legal

The /about marketing page (features, no-numbers, no-algorithms, portfolio/domain pitches, CTAs) and the Terms, Privacy and Conduct legal pages, plus the shared footer.

#### About headline
The about page masthead sentence. Read as `about-title` on the about page.

**Values (default).** size 1082 x 161; padding 35px 0px 0px 0px; background transparent; text LabilGrotesk-Medium 41/42 400, #262626 `color.grey.950`.

![About headline default](components/crops/about-title-default.png)

#### Feature card
A feature block ("Perfectly simple", "Community not numbers"…). Read as `feature` on the about page.

**Values (default).** size 511 x 371; padding 24px 40px 38px 40px; radius 7px; background #f4f4f4; text LabilGrotesk-Medium 41/42 400, #262626 `color.grey.950`.

![Feature card default](components/crops/feature-default.png)

#### About statement
"We are building Explore as it should be built…" — the statement copy. Read as `about-copy` on the about page.

**Values (default).** size 484 x 588; padding 140px 0px; background transparent; text UntitledSans 16/22 400, #262626 `color.grey.950`.

![About statement default](components/crops/about-copy-default.png)

#### About CTA
"Sign up — No bank card required" in the closing section; measured, never followed. Read as `about-cta` on the about page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 294 x 47; padding 14px 25px; radius 50px; background #ffc60a `color.accent.DEFAULT`; text UntitledSans 16/normal 400, #262626 `color.grey.950`; transition all 0.2s ease |
| hover, focus-visible, pressed | background #ffcc24 `color.accent.hover` |

![About CTA default](components/crops/about-cta-default.png) ![About CTA hover](components/crops/about-cta-hover.png) ![About CTA focus-visible](components/crops/about-cta-focus-visible.png) ![About CTA pressed](components/crops/about-cta-pressed.png)

#### Footer
The grey closing footer: typeface credits and site links. Read as `footer` on the about page.

**Values (default).** size 990 x 585; padding 130px 0px 175px 0px; background transparent; text UntitledSans 18/28 400, #262626 `color.grey.950`.

![Footer default](components/crops/footer-default.png)

#### Footer column
One footer column (Typefaces credits: Labil Grotesk / Untitled Sans…). Read as `footer-column` on the about page.

**Values (default).** size 155 x 280; padding 0px 20px; background transparent; text UntitledSans 18/28 400, #262626 `color.grey.950`.

![Footer column default](components/crops/footer-column-default.png)

#### Legal heading
The page heading on the code of conduct. Read as `legal-title` on the legal page.

**Values (default).** size 760 x 22; background transparent; text UntitledSans 21/22 400, #262626 `color.grey.950`.

![Legal heading default](components/crops/legal-title-default.png)

#### Legal body
Body copy on a legal page (the same type treatment as /terms and /privacy). Read as `legal-body` on the legal page.

**Values (default).** size 760 x 42; background transparent; text UntitledSans 16/21 400, #262626 `color.grey.950`.

![Legal body default](components/crops/legal-body-default.png)

### Server-rendered profile

Public profiles were server-rendered: these entries were measured on the archived SSR HTML for /malikafavre and /sawdust, replayed with JavaScript disabled so the SPA could not replace the server markup. Real names, post titles, avatars and gallery frames are archived data, shown as they appeared in February 2023.

#### SSR profile
The server-rendered profile page (Malika Favre): name, avatar placeholder and the post grid the crawler received. Read as `ssr-profile` on the ssr page.

**Values (default).** size 842 x 3092.78; background transparent; text UntitledSans 21/22 400, #262626 `color.grey.950`.

Child layers that carry the look: div 396x396 background #f8f8f8 `color.grey.50` radius 5px; div 396x396 background #eaeaea; div 142x142 background #3a3a3a `color.grey.750` radius 150px.

![SSR profile default](components/crops/ssr-profile-default.png)

#### SSR profile avatar
The profile image slot; the avatar file itself was never archived, so it reads as its placeholder. Read as `ssr-avatar` on the ssr page.

**Values (default).** size 142 x 142; radius 150px; background #3a3a3a `color.grey.750`; text UntitledSans 16/22 400, #262626 `color.grey.950`; transform translate(-71px, -71px).

![SSR profile avatar default](components/crops/ssr-avatar-default.png)

#### SSR profile name
The display name on the server-rendered profile. Read as `ssr-name` on the ssr page.

**Values (default).** size 396 x 22; background transparent; text UntitledSans 21/22 400, #262626 `color.grey.950`.

![SSR profile name default](components/crops/ssr-name-default.png)

#### SSR post tile
A post tile in the server-rendered feed; its video/poster media was never archived, so it paints the empty placeholder. Read as `ssr-post` on the ssr page.

**Values (default).** size 58.16 x 264.08; padding 0px 15px 50px 15px; background transparent; text UntitledSansMedium 16/22 400, #262626 `color.grey.950`.

Child layers that carry the look: div::after 28.1562pxx14781px background rgba(0, 0, 0, 0.02); div 17.7x28 background #9d9d9d `color.grey.500` radius 34px.

![SSR post tile default](components/crops/ssr-post-default.png)

#### SSR post gallery
The media tile of a server-rendered post. Read as `ssr-gallery` on the ssr page.

**Values (default).** size 28.16 x 14.08; background transparent; text UntitledSans 16/22 400, #262626 `color.grey.950`.

Child layers that carry the look: div::after 28.1562pxx14781px background rgba(0, 0, 0, 0.02).

![SSR post gallery default](components/crops/ssr-gallery-default.png)

### Mobile (390 wide)

A few components as a phone draws them, at 390 x 844 at 2x: a 56px header, "Sign up free" only, the pill row and the full-width post cards.

#### Mobile header
The fixed top bar at 390 wide. Read as `m-header` on the mobile page at 390 wide.

**Values (default).** size 390 x 56; background #9d9d9d `color.grey.500`; text UntitledSans 16/19 400, #262626 `color.grey.950`.

![Mobile header default](components/crops/m-header-default.png)

#### Mobile sign up pill
The header "Sign up free" pill at 390 wide. Read as `m-signup` on the mobile page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 121 x 38; padding 9px 16px 10px 16px; radius 50px; background #ffc60a `color.accent.DEFAULT`; text UntitledSans 16/19 400, #262626 `color.grey.950`; transition all 0.2s ease |
| hover, focus-visible, pressed | background #ffcc24 `color.accent.hover` |

![Mobile sign up pill default](components/crops/m-signup-default.png) ![Mobile sign up pill hover](components/crops/m-signup-hover.png) ![Mobile sign up pill focus-visible](components/crops/m-signup-focus-visible.png) ![Mobile sign up pill pressed](components/crops/m-signup-pressed.png)

#### Mobile category pill
A category pill in the horizontally scrolling row at 390 wide. Read as `m-pill` on the mobile page at 390 wide.

**Values (default).** size 47 x 36; padding 5px 12px 6px 12px; border 2px solid #262626 `color.grey.950`; radius 20px; background transparent; text UntitledSans 16/21 400, #262626 `color.grey.950`; transition color 0.2s ease.

![Mobile category pill default](components/crops/m-pill-default.png)

#### Mobile post card
A feed card at 390 wide. Read as `m-post` on the mobile page at 390 wide.

**Values (default).** size 390 x 448.5; padding 0px 0px 40px 0px; background transparent; text UntitledSansMedium 16/22 400, #262626 `color.grey.950`; transition opacity 0.2s ease; icon 22 x 8, #ffffff `color.white`.

Child layers that carry the look: div 390x292.5 background #5a5958; div::after 390pxx292.5px background rgba(0, 0, 0, 0.02); div 37x20 background #262626 `color.grey.950` radius 30px.

![Mobile post card default](components/crops/m-post-default.png)

## Icons

Explore's interface icons (the wordmark, appreciate/comment/save glyphs, the carousel arrows, the password eye) are inline SVGs drawn by the compiled Vue bundle and were not lifted into `icons/` this pass; the catalog records the gap. They are visible inside the crops and screenshots.

## Gaps

### Pages

- **Everything signed in.** The member app (network feed, notifications, saved posts, subscriptions, the post composer, settings) lived behind sign-in, and its API was never archived besides. The signed-out `/sawdust` and `/p/2193` shells in the discovery list are the honest boundary.
- **Archive misses.** Some post videos, GIFs, WebPs and profile media were never archived and render as the grey placeholder; `/img/code-of-conduct.ddc79720.png` is missing so the Conduct page shows no illustration. Per-capture misses are listed in each screenshot's `.capture.json` sidecar.
- **Anything that sends or creates.** No form was submitted, no account created, nothing posted, appreciated, saved or purchased; the PRO/subscribe plans were reached only as links.
- **Reset-password.** `/reset-password/{id}/{code}` needs a live token; the route exists in the bundle but was never reachable, so only `/forgot-password` was measured.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled and validation states** were not seen on any public control; error alerts exist in the CSS (`alert--visible`) but never fired without a submit.

### Themes

Explore shows one fixed light theme on every public surface: no `prefers-color-scheme` rule exists in the compiled stylesheet and nothing on a signed-out page toggles a theme. Member portfolios had a dark presentation theme in the app's marketing, but it lived behind sign-in and was never captured, so the token file ships a single `light` set.

### Fonts

- **UntitledSans** and **UntitledSansMedium** (Klim Type Foundry) carry the UI; they are proprietary served faces, so the style guide falls back to system sans.
- **LabilGrotesk-Medium** (Kometa Typefaces) draws the hero sentence, section titles and the wordmark; also proprietary.

### Screenshots

- Post images and profile media are members' and Explore's content and appear only inside screenshots and crops.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Member-generated content (post bodies, comments, profile bios beyond the SSR markup) was never archived or was not transcribed; only the interface around it was measured.
- No personal data was captured: the pages were read signed out, and the names and works visible in the SSR profiles are public archive records reproduced as captured.
