# Component measurements

Computed styles read from linkedin.com on 2026-11-18 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the guest home, jobs search, the LinkedIn company page, a public profile, the user agreement and the sign-in wall at rest — and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed and no sign-in, apply or follow was submitted; `focused` is a field focused without typing; `filled` is sample text typed into the jobs keyword field and deleted, with Enter never pressed.

## Components

### Shell and navigation

#### header-nav

Guest nav. The guest header: logo, Top Content, People, Learning, Jobs, Games, Sign in, Join now.

Page: home. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1128 x 80 |
| Padding | 12px 0px 16px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 @ 0.9 |
| Text node | span.top-nav-link__label-text.font-sans: -apple-system 12px/15px 400, #000000 @ 0.6 |
| Transition | none |
| Icon | 0 x 0, colour #0a66c2, fill #000000 |
| Painted layers | ul::after.top-nav-menu.flex 1pxx37px bg #000000 @ 0.3; a.nav__button-secondary.btn-secondary-emphasis 99.2x48.0 r 24px shadow #0a66c2 0px 0px 0px 1px; a.nav__button-tertiary.btn-primary 115.2x48.0 bg #0a66c2 r 24px shadow #000000 @ 0 0px 0px 0px 1px |
| Ancestor paint | 1 up div.sticky.top-0 bg #ffffff |
| How | at rest |

Crops: `header-nav-default.png`.

#### nav-logo

Logo. The LinkedIn wordmark in the guest nav. Measured, never followed.

Page: home. Selector: `a`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 102 x 52 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 16px/24px 600 |
| Letter spacing | normal |
| Colour | #0a66c2 |
| Transition | none |
| Cursor | pointer |
| Icon | 0 x 0, colour #0a66c2, fill #000000 |
| How | at rest |

Crops: `nav-logo-default.png`.

#### nav-link

Nav link. "Jobs" in the guest nav. A destination link, measured, never followed.

Page: home. Selector: `a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 64 x 52 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | -apple-system 16px/24px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 @ 0.6 | #000000 @ 0.9 | #0a66c2 | #000000 @ 0.9 |
| Text node | span.top-nav-link__label-text.font-sans: -apple-system 12px/15px 400, #000000 @ 0.6 | span.top-nav-link__label-text.font-sans: -apple-system 12px/15px 400, #000000 @ 0.9 | span.top-nav-link__label-text.font-sans: -apple-system 12px/15px 400, #0a66c2 | span.top-nav-link__label-text.font-sans: -apple-system 12px/15px 400, #000000 @ 0.9 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 18, colour #000000 @ 0.6 | 20 x 18, colour #000000 @ 0.9 | 20 x 18, colour #0a66c2 | 20 x 18, colour #000000 @ 0.9 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.top-nav-link.flex 64.0x52.0 outline 1px auto #005fcc offset 1px | = |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### nav-signin

Sign in. "Sign in" secondary-emphasis pill. A sign-in destination, measured, never followed.

Page: home. Selector: `a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 99.17 x 48 | = | = | = |
| Padding | 12px 24px | = | = | = |
| Border | none | = | = | = |
| Radius | 24px | = | = | = |
| Background | transparent | #70b5f9 @ 0.1 | = | #70b5f9 @ 0.2 |
| Box shadow | #0a66c2 0px 0px 0px 1px | = | = | #004182 0px 0px 0px 1px |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | -apple-system 16px/24px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0a66c2 | #004182 | = | #004182 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.nav__button-secondary.btn-secondary-emphasis 99.2x48.0 r 24px shadow #0a66c2 0px 0px 0px 1px | a.nav__button-secondary.btn-secondary-emphasis 99.2x48.0 bg #70b5f9 @ 0.1 r 24px shadow #0a66c2 0px 0px 0px 1px | a.nav__button-secondary.btn-secondary-emphasis 99.2x48.0 r 24px shadow #0a66c2 0px 0px 0px 1px outline 1px auto #005fcc offset 1px | a.nav__button-secondary.btn-secondary-emphasis 99.2x48.0 bg #70b5f9 @ 0.2 r 24px shadow #004182 0px 0px 0px 1px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-signin-default.png`, `nav-signin-hover.png`, `nav-signin-focus-visible.png`, `nav-signin-pressed.png`.

#### nav-join

Join now. "Join now" primary pill. A sign-in destination, measured, never followed.

Page: home. Selector: `a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 115.23 x 48 | = | = | = |
| Padding | 12px 24px | = | = | = |
| Border | none | = | = | = |
| Radius | 24px | = | = | = |
| Background | #0a66c2 | #004182 | = | #004182 |
| Box shadow | #000000 @ 0 0px 0px 0px 1px | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | -apple-system 16px/24px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | #ffffff @ 0.6 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.nav__button-tertiary.btn-primary 115.2x48.0 bg #0a66c2 r 24px shadow #000000 @ 0 0px 0px 0px 1px | a.nav__button-tertiary.btn-primary 115.2x48.0 bg #004182 r 24px shadow #000000 @ 0 0px 0px 0px 1px | a.nav__button-tertiary.btn-primary 115.2x48.0 bg #0a66c2 r 24px shadow #000000 @ 0 0px 0px 0px 1px outline 1px auto #005fcc offset 1px | a.nav__button-tertiary.btn-primary 115.2x48.0 bg #004182 r 24px shadow #000000 @ 0 0px 0px 0px 1px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-join-default.png`, `nav-join-hover.png`, `nav-join-focus-visible.png`, `nav-join-pressed.png`.

#### footer

Footer. The guest footer: legal links and the LinkedIn Corporation line.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 50 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 @ 0.9 |
| Text node | span.li-footer__copy-text.flex: -apple-system 12px/18px 400, #666666 |
| Transition | none |
| Icon | 56 x 14, colour #000000 |
| Painted layers | ul.collapsible-dropdown__list.hidden 0.0x0.0 bg #ffffff r 8px shadow #000000 @ 0.3 0px 4px 12px 0px; button.font-sans.text-xs 0.0x0.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0; button.font-sans.text-xs 0.0x0.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0; button.font-sans.text-xs 0.0x0.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0; button.font-sans.text-xs 0.0x0.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0; button.font-sans.text-xs 0.0x0.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link. A footer legal link. Measured, never followed.

Page: home. Selector: `footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 35.66 x 18 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | -apple-system 12px/18px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #666666 | #004182 | #0a66c2 | #004182 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.li-footer__item-link.flex 35.7x18.0 outline 1px auto #005fcc offset 1px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

### Guest home

#### hero-h1

Hero heading. "Welcome to your professional community" at text-display-lg (48px).

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 572.39 x 120 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 48px/60px 400 |
| Letter spacing | normal |
| Colour | #000000 @ 0.9 |
| Transition | none |
| How | at rest |

Crops: `hero-h1-default.png`.

#### hero-email

Sign in with email. "Sign in with email" outline pill under the hero. A sign-in destination, measured, never followed.

Page: home. Selector: `a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 400 x 40 | = | = | = |
| Padding | 8px 24px | = | = | = |
| Border | none | = | = | = |
| Radius | 24px | = | = | = |
| Background | transparent | #000000 @ 0.04 | = | #000000 @ 0.08 |
| Box shadow | #000000 @ 0.75 0px 0px 0px 1px | = | = | #000000 @ 0.9 0px 0px 0px 1px |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | -apple-system 16px/24px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 @ 0.75 | #000000 @ 0.9 | = | #000000 @ 0.9 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.sign-in-form__sign-in-cta.my-2 400.0x40.0 r 24px shadow #000000 @ 0.75 0px 0px 0px 1px | a.sign-in-form__sign-in-cta.my-2 400.0x40.0 bg #000000 @ 0.04 r 24px shadow #000000 @ 0.75 0px 0px 0px 1px | a.sign-in-form__sign-in-cta.my-2 400.0x40.0 r 24px shadow #000000 @ 0.75 0px 0px 0px 1px outline 1px auto #005fcc offset 1px | a.sign-in-form__sign-in-cta.my-2 400.0x40.0 bg #000000 @ 0.08 r 24px shadow #000000 @ 0.9 0px 0px 0px 1px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-email-default.png`, `hero-email-hover.png`, `hero-email-focus-visible.png`, `hero-email-pressed.png`.

#### topic-chip

Topic chip. A topic pill ("Career") in Explore top LinkedIn content. Measured, never followed.

Page: home. Selector: `a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 99.14 x 48 | = | = | = |
| Padding | 12px 24px | = | = | = |
| Border | none | = | = | = |
| Radius | 24px | = | = | = |
| Background | transparent | #000000 @ 0.04 | = | #000000 @ 0.08 |
| Box shadow | #000000 @ 0.75 0px 0px 0px 1px | = | = | #000000 @ 0.9 0px 0px 0px 1px |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | -apple-system 16px/24px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 @ 0.75 | #000000 @ 0.9 | = | #000000 @ 0.9 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.btn-md.babybear:btn-sm 99.1x48.0 r 24px shadow #000000 @ 0.75 0px 0px 0px 1px | a.btn-md.babybear:btn-sm 99.1x48.0 bg #000000 @ 0.04 r 24px shadow #000000 @ 0.75 0px 0px 0px 1px | a.btn-md.babybear:btn-sm 99.1x48.0 r 24px shadow #000000 @ 0.75 0px 0px 0px 1px outline 1px auto #005fcc offset 1px | a.btn-md.babybear:btn-sm 99.1x48.0 bg #000000 @ 0.08 r 24px shadow #000000 @ 0.9 0px 0px 0px 1px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `topic-chip-default.png`, `topic-chip-hover.png`, `topic-chip-focus-visible.png`, `topic-chip-pressed.png`.

#### job-chip

Job category chip. A suggested job-search chip. Measured, never followed.

Page: home. Selector: `a`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 138.41 x 48 | = | = |
| Padding | 12px 24px | = | = |
| Border | none | = | = |
| Radius | 24px | = | = |
| Background | transparent | #000000 @ 0.04 | = |
| Box shadow | #000000 @ 0.75 0px 0px 0px 1px | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px |
| Font | -apple-system 16px/24px 600 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 @ 0.75 | #000000 @ 0.9 | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| Painted layers | a.btn-md.babybear:btn-sm 138.4x48.0 r 24px shadow #000000 @ 0.75 0px 0px 0px 1px | a.btn-md.babybear:btn-sm 138.4x48.0 bg #000000 @ 0.04 r 24px shadow #000000 @ 0.75 0px 0px 0px 1px | a.btn-md.babybear:btn-sm 138.4x48.0 r 24px shadow #000000 @ 0.75 0px 0px 0px 1px outline 1px auto #005fcc offset 1px |
| How | at rest | mouse hover | Shift+Tab, Tab |

Crops: `job-chip-default.png`, `job-chip-hover.png`, `job-chip-focus-visible.png`.

#### section-heading

Section heading. "Explore top LinkedIn content", the first section heading on the guest home.

Page: home. Selector: `h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 429 x 40 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 32px/40px 400 |
| Letter spacing | normal |
| Colour | #000000 @ 0.9 |
| Transition | none |
| How | at rest |

Crops: `section-heading-default.png`.

### Jobs search

#### jobs-h1

Results heading. The jobs-search results heading, as the page painted it for this capture IP.

Page: jobs. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 472 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 @ 0.6 |
| Text node | span.results-context-header__job-count: -apple-system 16px/24px 400, #000000 @ 0.6 |
| Transition | none |
| How | at rest |

Crops: `jobs-h1-default.png`.

#### filter-chip

Filter chip. "Date posted" filter chip. Opened as a local dropdown, never submitted.

Page: jobs. Selector: `button`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 140.02 x 32 | = | = | = | = |
| Padding | 3.5px 16px | = | 4px 16px | = | = |
| Border | 1px solid #000000 @ 0.3 | 1px solid #000000 @ 0.45 | = | 1px solid #000000 @ 0.45 | 1px solid #000000 @ 0.45 |
| Radius | 16px | = | = | = | = |
| Background | transparent | #000000 @ 0.04 | = | #000000 @ 0.08 | #000000 @ 0.04 |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = | = |
| Font | -apple-system 14px/normal 600 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #000000 @ 0.75 | #000000 @ 0.9 | = | #000000 @ 0.9 | #000000 @ 0.9 |
| Transition | none | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Icon | 24 x 24, colour #000000 @ 0.75 | 24 x 24, colour #000000 @ 0.9 | = | 24 x 24, colour #000000 @ 0.9 | 24 x 24, colour #000000 @ 0.9 |
| Painted layers | button.filter-button.pill 140.0x32.0 border T:1px solid #000000 @ 0.3 / R:1px solid #000000 @ 0.3 / B:1px solid #000000 @ 0.3 / L:1px solid #000000 @ 0.3 r 16px | button.filter-button.pill 140.0x32.0 bg #000000 @ 0.04 border T:1px solid #000000 @ 0.45 / R:1px solid #000000 @ 0.45 / B:1px solid #000000 @ 0.45 / L:1px solid #000000 @ 0.45 r 16px | button.filter-button.pill 140.0x32.0 border T:1px solid #000000 @ 0.3 / R:1px solid #000000 @ 0.3 / B:1px solid #000000 @ 0.3 / L:1px solid #000000 @ 0.3 r 16px outline 1px auto #005fcc offset 0px | button.filter-button.pill 140.0x32.0 bg #000000 @ 0.08 border T:1px solid #000000 @ 0.45 / R:1px solid #000000 @ 0.45 / B:1px solid #000000 @ 0.45 / L:1px solid #000000 @ 0.45 r 16px | button.filter-button.pill 140.0x32.0 bg #000000 @ 0.04 border T:1px solid #000000 @ 0.45 / R:1px solid #000000 @ 0.45 / B:1px solid #000000 @ 0.45 / L:1px solid #000000 @ 0.45 r 16px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |

Crops: `filter-chip-default.png`, `filter-chip-hover.png`, `filter-chip-focus-visible.png`, `filter-chip-pressed.png`, `filter-chip-opened.png`.

#### job-row

Job card. A job result card on the public search. Measured, never followed. Apply was not clicked.

Page: jobs. Selector: `li`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 504 x 132.98 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | -apple-system 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 @ 0.9 | = | = |
| Text node | h3.base-search-card__title: -apple-system 18px/23.9999px 600, #000000 @ 0.9 | = | = |
| Transition | none | = | = |
| Painted layers | div.base-card.relative 504.0x133.0 bg #e6f7ff border B:1px solid #e6e9ec; img.artdeco-entity-image.artdeco-entity-image--square-4 56.0x56.0 border T:4px solid #000000 @ 0 / R:4px solid #000000 @ 0 / B:4px solid #000000 @ 0 / L:4px solid #000000 @ 0 r 6px | = | div.base-card.relative 504.0x133.0 bg #e6f7ff border B:1px solid #e6e9ec; a.base-card__full-link.absolute 504.0x132.0 outline 1px auto #005fcc offset 4px; img.artdeco-entity-image.artdeco-entity-image--square-4 56.0x56.0 border T:4px solid #000000 @ 0 / R:4px solid #000000 @ 0 / B:4px solid #000000 @ 0 / L:4px solid #000000 @ 0 r 6px |
| How | at rest | mouse hover | Shift+Tab, Tab |

Crops: `job-row-default.png`, `job-row-hover.png`, `job-row-focus-visible.png`.

#### apply-cta

Apply. "Apply" on the job detail pane. A sign-in destination, measured, never followed.

Page: jobs. Selector: `button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 117.86 x 48 | = | = | = |
| Padding | 12px 24px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 24px | = | = | = |
| Background | #0a66c2 | #004182 | = | #004182 |
| Box shadow | #000000 @ 0 0px 0px 0px 1px | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | -apple-system 16px/normal 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | #ffffff @ 0.6 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #ffffff, fill #000000 | = | = | 16 x 16, colour #ffffff @ 0.6, fill #000000 |
| Painted layers | button.sign-up-modal__outlet.top-card-layout__cta 117.9x48.0 bg #0a66c2 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 24px shadow #000000 @ 0 0px 0px 0px 1px | button.sign-up-modal__outlet.top-card-layout__cta 117.9x48.0 bg #004182 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 24px shadow #000000 @ 0 0px 0px 0px 1px | button.sign-up-modal__outlet.top-card-layout__cta 117.9x48.0 bg #0a66c2 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 24px shadow #000000 @ 0 0px 0px 0px 1px outline 1px auto #005fcc offset 0px | button.sign-up-modal__outlet.top-card-layout__cta 117.9x48.0 bg #004182 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 24px shadow #000000 @ 0 0px 0px 0px 1px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `apply-cta-default.png`, `apply-cta-hover.png`, `apply-cta-focus-visible.png`, `apply-cta-pressed.png`.

### Company page

#### company-h1

Company name. The public company page title.

Page: company. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 422 x 36 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 24px/36px 600 |
| Letter spacing | normal |
| Colour | #000000 @ 0.9 |
| Transition | none |
| How | at rest |

Crops: `company-h1-default.png`.

#### company-follow

Follow. "Follow" on the company top card. A sign-in destination, measured, never followed.

Page: company. Selector: `button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 96.88 x 48 | = | = | = |
| Padding | 12px 24px | = | = | = |
| Border | none | = | = | = |
| Radius | 24px | = | = | = |
| Background | transparent | #000000 @ 0.04 | = | #000000 @ 0.08 |
| Box shadow | #000000 @ 0.75 0px 0px 0px 1px | = | = | #000000 @ 0.9 0px 0px 0px 1px |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | -apple-system 16px/24px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 @ 0.75 | #000000 @ 0.9 | = | #000000 @ 0.9 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.top-card-layout__cta.mt-2 96.9x48.0 r 24px shadow #000000 @ 0.75 0px 0px 0px 1px | a.top-card-layout__cta.mt-2 96.9x48.0 bg #000000 @ 0.04 r 24px shadow #000000 @ 0.75 0px 0px 0px 1px | a.top-card-layout__cta.mt-2 96.9x48.0 r 24px shadow #000000 @ 0.75 0px 0px 0px 1px outline 1px auto #005fcc offset 1px | a.top-card-layout__cta.mt-2 96.9x48.0 bg #000000 @ 0.08 r 24px shadow #000000 @ 0.9 0px 0px 0px 1px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `company-follow-default.png`, `company-follow-hover.png`, `company-follow-focus-visible.png`, `company-follow-pressed.png`.

#### company-jobs

See jobs. "See jobs" primary pill. Measured, never followed.

Page: company. Selector: `a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 112.45 x 48 | = | = | = |
| Padding | 12px 24px | = | = | = |
| Border | none | = | = | = |
| Radius | 24px | = | = | = |
| Background | #0a66c2 | #004182 | = | #004182 |
| Box shadow | #000000 @ 0 0px 0px 0px 1px | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | -apple-system 16px/24px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | #ffffff @ 0.6 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.top-card-layout__cta.mt-2 112.5x48.0 bg #0a66c2 r 24px shadow #000000 @ 0 0px 0px 0px 1px | a.top-card-layout__cta.mt-2 112.5x48.0 bg #004182 r 24px shadow #000000 @ 0 0px 0px 0px 1px | a.top-card-layout__cta.mt-2 112.5x48.0 bg #0a66c2 r 24px shadow #000000 @ 0 0px 0px 0px 1px outline 1px auto #005fcc offset 1px | a.top-card-layout__cta.mt-2 112.5x48.0 bg #004182 r 24px shadow #000000 @ 0 0px 0px 0px 1px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `company-jobs-default.png`, `company-jobs-hover.png`, `company-jobs-focus-visible.png`, `company-jobs-pressed.png`.

### Public profile

#### profile-h1

Profile name. The public profile name. A published profile, captured signed out.

Page: profile. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 149.16 x 36 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 24px/36px 600 |
| Letter spacing | normal |
| Colour | #000000 @ 0.9 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `profile-h1-default.png`.

#### profile-headline

Headline. The public profile headline under the name.

Page: profile. Selector: `.top-card-layout__headline`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 422 x 72 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 @ 0.9 |
| Transition | none |
| How | at rest |

Crops: `profile-headline-default.png`.

#### profile-join

Join to view profile. "Join to view profile". A sign-in destination, measured, never followed.

Page: profile. Selector: `a.btn-primary`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 190.61 x 48 | = | = | = |
| Padding | 12px 24px | = | = | = |
| Border | none | = | = | = |
| Radius | 24px | = | = | = |
| Background | #0a66c2 | #004182 | = | #004182 |
| Box shadow | #000000 @ 0 0px 0px 0px 1px | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | -apple-system 16px/24px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | #ffffff @ 0.6 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.top-card-layout__cta.mt-2 190.6x48.0 bg #0a66c2 r 24px shadow #000000 @ 0 0px 0px 0px 1px | a.top-card-layout__cta.mt-2 190.6x48.0 bg #004182 r 24px shadow #000000 @ 0 0px 0px 0px 1px | a.top-card-layout__cta.mt-2 190.6x48.0 bg #0a66c2 r 24px shadow #000000 @ 0 0px 0px 0px 1px outline 1px auto #005fcc offset 1px | a.top-card-layout__cta.mt-2 190.6x48.0 bg #004182 r 24px shadow #000000 @ 0 0px 0px 0px 1px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `profile-join-default.png`, `profile-join-hover.png`, `profile-join-focus-visible.png`, `profile-join-pressed.png`.

#### profile-message

Message. "Message". A sign-in destination into messaging, measured, never followed.

Page: profile. Selector: `a, button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 145.88 x 48 | = | = | = |
| Padding | 12px 24px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 24px | = | = | = |
| Background | transparent | #70b5f9 @ 0.1 | = | #70b5f9 @ 0.2 |
| Box shadow | #0a66c2 0px 0px 0px 1px | = | = | #004182 0px 0px 0px 1px |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | -apple-system 16px/normal 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0a66c2 | #004182 | = | #004182 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #0a66c2 | 16 x 16, colour #004182 | = | 16 x 16, colour #004182 |
| Painted layers | button.contextual-sign-in-modal__outlet-btn.cursor-pointer 145.9x48.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 24px shadow #0a66c2 0px 0px 0px 1px | button.contextual-sign-in-modal__outlet-btn.cursor-pointer 145.9x48.0 bg #70b5f9 @ 0.1 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 24px shadow #0a66c2 0px 0px 0px 1px | button.contextual-sign-in-modal__outlet-btn.cursor-pointer 145.9x48.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 24px shadow #0a66c2 0px 0px 0px 1px outline 1px auto #005fcc offset 0px | button.contextual-sign-in-modal__outlet-btn.cursor-pointer 145.9x48.0 bg #70b5f9 @ 0.2 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 24px shadow #004182 0px 0px 0px 1px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `profile-message-default.png`, `profile-message-hover.png`, `profile-message-focus-visible.png`, `profile-message-pressed.png`.

#### avatar

Avatar. The public profile photo as the page paints it.

Page: profile. Selector: `img`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 128 x 128 |
| Padding | 0px |
| Border | 4px solid #ffffff |
| Radius | 50% |
| Background | transparent |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.3 0px 4px 12px 0px |
| Outline | none |
| Font | -apple-system 13.3333px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | opacity 0.336s cubic-bezier(0.34, 0, 0.21, 1) |
| Cursor | pointer |
| Painted layers | img.inline-block.relative 128.0x128.0 border T:4px solid #ffffff / R:4px solid #ffffff / B:4px solid #ffffff / L:4px solid #ffffff r 50% shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.3 0px 4px 12px 0px |
| How | at rest |

Crops: `avatar-default.png`.

### Legal

#### legal-h1

Legal heading. The User Agreement banner heading (t-64).

Page: legal. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 648 x 72 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 64px/72px 400 |
| Letter spacing | normal |
| Colour | #000000 @ 0.9 |
| Transition | none |
| How | at rest |

Crops: `legal-h1-default.png`.

#### legal-link

Legal nav link. A legal-section link. Measured, never followed.

Page: legal. Selector: `a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 102.88 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | -apple-system 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 @ 0.6 | #000000 | #0a66c2 | #000000 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Ancestor paint | - | 3 up li shadow #0073b1 0px -3px 0px 0px inset | = | = |
| Painted layers | - | = | a.t-sans.t-black--light 102.9x24.0 outline 1px auto #005fcc offset 1px | = |

Crops: `legal-link-default.png`, `legal-link-hover.png`, `legal-link-focus-visible.png`, `legal-link-pressed.png`.

### Sign-in wall

#### signin-heading

Sign-in heading. The sign-in wall heading, captured at rest. Nothing was typed or submitted.

Page: signin. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 400 x 33.75 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | system-ui 30px/33.75px 600 |
| Letter spacing | normal |
| Colour | #000000 @ 0.9 |
| Transition | none |
| How | at rest |

Crops: `signin-heading-default.png`.

#### signin-email

Email field. The sign-in email field at rest and focused. No text was typed. The form was not submitted.

Page: signin. Selector: `input`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 400 x 48 | = |
| Padding | 1px 12px | = |
| Border | 1px solid #000000 @ 0.75 | 1px solid #000000 @ 0.9 |
| Radius | 4px | = |
| Background | #ffffff @ 0 | = |
| Box shadow | none | #000000 @ 0.9 0px 0px 0px 1px inset |
| Outline | none | 3px auto #005fcc offset -1px |
| Font | system-ui 16px/20px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 @ 0.9 | = |
| Transition | box-shadow, border-color 0.084s ease | = |
| Cursor | text | = |
| Placeholder | #000000 @ 0.9, opacity 1 | = |
| Painted layers | input.aaal32.aaal3w 400.0x48.0 bg #ffffff @ 0 border T:1px solid #000000 @ 0.75 / R:1px solid #000000 @ 0.75 / B:1px solid #000000 @ 0.75 / L:1px solid #000000 @ 0.75 r 4px | input.aaal32.aaal3w 400.0x48.0 bg #ffffff @ 0 border T:1px solid #000000 @ 0.9 / R:1px solid #000000 @ 0.9 / B:1px solid #000000 @ 0.9 / L:1px solid #000000 @ 0.9 r 4px shadow #000000 @ 0.9 0px 0px 0px 1px inset outline 3px auto #005fcc offset -1px |
| How | at rest | clicked into the field |

Crops: `signin-email-default.png`, `signin-email-focused.png`.

#### signin-submit

Sign in submit. The sign-in submit control. Hover and focus only. It was not pressed, so no sign-in was attempted.

Page: signin. Selector: `button`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 400 x 48 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px |
| Font | system-ui 14px/17.5px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 @ 0.9 | = | = |
| Text node | span.aaalje.aaalqv: system-ui 16px/20px 600, #ffffff | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| Painted layers | span.aaalzr.aaalyb 400.0x48.0 bg #0a66c2 r 24px | span.aaalzr.aaalyb 400.0x48.0 bg #004182 r 24px | button.aaalxl.aaalxk 400.0x48.0 outline 1px auto #005fcc offset 0px; span.aaalzr.aaalyb 400.0x48.0 bg #0a66c2 r 24px |
| How | at rest | mouse hover | Shift+Tab, Tab |

Crops: `signin-submit-default.png`, `signin-submit-hover.png`, `signin-submit-focus-visible.png`.

### Mobile (390 wide)

#### m-nav

Mobile nav. The guest nav at 390px.

Page: home. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 76 |
| Padding | 12px 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 @ 0.9 |
| Text node | a.nav__button-secondary.btn-secondary-emphasis: -apple-system 16px/24px 600, #0a66c2 |
| Transition | none |
| Icon | 26 x 26, colour #0a66c2, fill #000000 |
| Painted layers | a.nav__button-secondary.btn-secondary-emphasis 99.2x48.0 r 24px shadow #0a66c2 0px 0px 0px 1px; a.nav__button-tertiary.btn-primary 115.2x48.0 bg #0a66c2 r 24px shadow #000000 @ 0 0px 0px 0px 1px |
| Ancestor paint | 1 up div.sticky.top-0 bg #ffffff |
| How | at rest |

Crops: `m-nav-default.png`.

#### m-join

Mobile Join now. The Join now pill at 390px. A sign-in destination, measured, never followed.

Page: home. Selector: `a`. States: default, pressed.

| Property | default | pressed |
|---|---|---|
| Size (w x h) | 83.83 x 48 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | system-ui 14px/17.5px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 @ 0.9 | = |
| Text node | span.aaalje.aaalqt: system-ui 14px/17.5px 600, #0a66c2 | = |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | span.aaalzr.aaalyb 83.8x32.0 bg #ffffff @ 0 r 24px shadow #0a66c2 0px 0px 0px 1px inset | = |
| How | at rest | CDP forcePseudoState :active:hover |

Crops: `m-join-default.png`, `m-join-pressed.png`.

#### m-h1

Mobile hero heading. The guest-home heading at 390px.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 358 x 67.5 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | system-ui 30px/33.75px 400 |
| Letter spacing | normal |
| Colour | #000000 @ 0.9 |
| Transition | none |
| How | at rest |

Crops: `m-h1-default.png`.

## Transitions declared in the readable stylesheets

linkedin.com guest surfaces paint one light theme. Sign in, Join now, Apply, Follow and Message were measured, never followed. The login form was not submitted. Consent overlays were hidden, never clicked. Every value above is the computed value the page paints.

- company: none

- home: none

- jobs: none

- legal: none

- profile: none

- signin: `0.3s`, `0.5s`, `all`
