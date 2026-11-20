# Fable component measurements

Computed styles read from fable.co on 2026-11-14 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the site's painted surfaces — the emotion-styled marketing pages (the cream forest-green hero home, the sign-in card, the green support band) and the CSS-module catalog skin (/clubs, /book/*, /club/*) — with the Osano consent layer hidden (never answered), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Site chrome

#### mkt-header

Marketing header. The fixed transparent top bar over the green hero: Fable wordmark, Clubs/Books/Library/Blog links, the "Sign up or log in" and cart icons.

Page: home. Selector: `header[data-header]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 60 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | #000000 @ 0.04 0px 2px 3px -2px |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.fds-ui--header-nav-text.css-1ppp6vq: Inter 14px/14px 600, #f7f4ee, ls -0.25px |
| Transition | none |
| Icon | 82 x 33, colour #000000 |
| Painted layers | header.css-1vg9pjt 1440.0x60.0 shadow #000000 @ 0.04 0px 2px 3px -2px; div.css-1g7irsi 200.0x50.0 bg #ffffff border T:1px #ededed / R:1px #ededed / B:1px #ededed / L:1px #ededed r 12px shadow #000000 @ 0.08 0px 4px 12px 0px; span.css-1pyn1fk 17.0x17.0 bg #ffffff border T:1px #ededed / L:1px #ededed r 2px 0px 0px |
| How | at rest |

Crops: `mkt-header-default.png`.

#### mkt-logo

Fable logo (marketing). The Fable mark-and-wordmark svg in the marketing header — a dark-green rounded square of rainbow book spines with cream letterforms.

Page: home. Selector: `header a[aria-label=Home]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 82 x 33 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | border, background, color 0.2s, 0.2s, 0.2s ease, ease, ease delay 0s, 0s, 0s |
| Cursor | pointer |
| Icon | 82 x 33, colour #000000 |
| Ancestor paint | 3 up header.css-1vg9pjt shadow #000000 @ 0.04 0px 2px 3px -2px |
| How | at rest |

Crops: `mkt-logo-default.png`.

#### mkt-nav-link

Nav link (marketing). A marketing header nav link; measured, never followed.

Page: home. Selector: `header a Clubs`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 39.75 x 14 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | 4px | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #116ecd offset 4px | = |
| Font | Inter 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.fds-ui--header-nav-text.css-1ppp6vq: Inter 14px/14px 600, #f7f4ee, ls -0.25px | span.fds-ui--header-nav-text.css-1ppp6vq: Inter 14px/14px 600, #ededed, ls -0.25px | = | = |
| Transition | border, background, color 0.2s, 0.2s, 0.2s ease, ease, ease delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.css-101r1r7 39.8x14.0 r 4px outline 2px solid #116ecd offset 4px | = |

Crops: `mkt-nav-link-default.png`, `mkt-nav-link-hover.png`, `mkt-nav-link-focus-visible.png`, `mkt-nav-link-pressed.png`.

#### mkt-signin

Sign-in icon (marketing). The 24px "Sign up or log in" icon button; its states were measured but it was never clicked — the sign-in flow is a gap, not a state.

Page: home. Selector: `button[aria-label="Sign up or log in"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 24 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | 4px | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #116ecd offset 4px | = |
| Font | Inter 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | opacity 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #000000 | = | = | = |
| Ancestor paint | 3 up header.css-1vg9pjt shadow #000000 @ 0.04 0px 2px 3px -2px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.7 | = | 0.7 |
| Painted layers | - | = | button.css-1r8kfqf 24.0x24.0 r 4px outline 2px solid #116ecd offset 4px | = |

Crops: `mkt-signin-default.png`, `mkt-signin-hover.png`, `mkt-signin-focus-visible.png`, `mkt-signin-pressed.png`.

#### mkt-cart

Cart icon. The 32px "Shopping cart" icon button; measured, never clicked.

Page: home. Selector: `button[aria-label="Shopping cart"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | 4px | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #116ecd offset 4px | = |
| Font | Inter 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | border, background, color 0.2s, 0.2s, 0.2s ease, ease, ease delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #000000 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.css-1q2s6jc 32.0x32.0 r 4px outline 2px solid #116ecd offset 4px | = |

Crops: `mkt-cart-default.png`, `mkt-cart-hover.png`, `mkt-cart-focus-visible.png`, `mkt-cart-pressed.png`.

#### cat-header

Catalog header. The fixed 60px catalog top bar: the heldane "Fable" wordmark, nav links (Clubs / Books / Library / Blog) and the sign-in icon.

Page: club. Selector: `header.Header-module`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 60 |
| Padding | 0px 32px |
| Gap | 24px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/normal 400 |
| Letter spacing | normal |
| Colour | #1b1a1b |
| Text node | span.Text-module-scss-module__yXps7a__base.Text-module-scss-module__yXps7a__v-button-l: Inter 14px/16px 600, #1b1a1b, ls -0.25px |
| Transition | background-color, box-shadow 0.2s, 0.2s ease, ease delay 0s, 0s |
| Icon | 32 x 32, colour #1b1a1b, fill #000000 |
| How | at rest |

Crops: `cat-header-default.png`.

#### cat-logo

Fable wordmark (catalog). The catalog header wordmark link — heldane bold type, "Fable home".

Page: club. Selector: `a.HeaderLogo-module`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 81.33 x 32 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | heldane 24px/24px 700 |
| Letter spacing | -0.48px |
| Colour | #1b1a1b |
| Transition | none |
| Cursor | pointer |
| Icon | 32 x 32, colour #1b1a1b, fill #000000 |
| How | at rest |

Crops: `cat-logo-default.png`.

#### cat-nav-link

Catalog nav link. A catalog header nav link (Clubs) — a 60px-tall cell; measured, never followed.

Page: club. Selector: `a.HeaderNav-module__link Clubs`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 39.75 x 60 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | 2px | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #0064c3 offset 4px | = |
| Font | Inter 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1b1a1b | = | = | = |
| Text node | span.Text-module-scss-module__yXps7a__base.Text-module-scss-module__yXps7a__v-button-l: Inter 14px/16px 600, #1b1a1b, ls -0.25px | = | = | = |
| Transition | opacity 0.15s ease | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.8 | = | 0.8 |
| Painted layers | - | = | a.HeaderNav-module-scss-module__GmZ0Qq__link 39.8x60.0 r 2px outline 2px solid #0064c3 offset 4px | = |

Crops: `cat-nav-link-default.png`, `cat-nav-link-hover.png`, `cat-nav-link-focus-visible.png`, `cat-nav-link-pressed.png`.

#### cat-signin

Sign-in icon (catalog). The 36x36 "Sign up or log in" avatar icon linking to /signin; measured, never followed.

Page: club. Selector: `a.HeaderUserMenu-module__signInIcon`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 36 x 36 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | 9999px | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #0064c3 offset 2px | = |
| Font | Inter 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1b1a1b | = | = | = |
| Transition | opacity 0.15s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #1b1a1b | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.7 | = | 0.7 |
| Painted layers | - | = | a.HeaderUserMenu-module-scss-module__kVbIfG__signInIcon 36.0x36.0 r 9999px outline 2px solid #0064c3 offset 2px | = |

Crops: `cat-signin-default.png`, `cat-signin-hover.png`, `cat-signin-focus-visible.png`, `cat-signin-pressed.png`.

### Home

#### hero-h1

Hero headline. "The modern app for every reader" — the Heldane Display 72px cream masthead on the forest-green cover-wall hero.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 500 x 124 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Heldane Display 72px/62px 500 |
| Letter spacing | normal |
| Colour | #f7f4ee |
| Transition | none |
| Cursor | default |
| How | at rest |

Crops: `hero-h1-default.png`.

#### hero-cover

Hero book cover. One book-cover tile in the hero cover wall, linking into the dark /discover app; measured, never followed.

Page: home. Selector: `a[href*="/discover"]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 151 x 225 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Transition | border, background, color 0.2s, 0.2s, 0.2s ease, ease, ease delay 0s, 0s, 0s | = |
| Cursor | pointer | = |
| How | at rest | mouse hover |

Crops: `hero-cover-default.png`, `hero-cover-hover.png`.

#### getapp-hero

Get the app (hero). The white "Get the app" pill on the green hero (radius 60, white-on-green); measured, never clicked.

Page: home. Selector: `hero Get the app`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 160 x 52 | = | = | = |
| Padding | 0px | = | = | = |
| Border | 2px solid #ffffff | 2px solid #f9f9f9 | = | 2px solid #f9f9f9 |
| Radius | 60px | = | = | = |
| Background | #ffffff | #f9f9f9 | = | #f9f9f9 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #116ecd offset 4px | = |
| Font | Inter 14px/21px 600 | = | = | = |
| Letter spacing | -0.25px | = | = | = |
| Colour | #161015 | #332e32 | = | #332e32 |
| Transition | border, background, color 0.2s, 0.2s, 0.2s ease, ease, ease delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.css-165o2av 160.0x52.0 bg #ffffff border T:2px #ffffff / R:2px #ffffff / B:2px #ffffff / L:2px #ffffff r 60px | button.css-165o2av 160.0x52.0 bg #f9f9f9 border T:2px #f9f9f9 / R:2px #f9f9f9 / B:2px #f9f9f9 / L:2px #f9f9f9 r 60px | button.css-165o2av 160.0x52.0 bg #ffffff border T:2px #ffffff / R:2px #ffffff / B:2px #ffffff / L:2px #ffffff r 60px outline 2px solid #116ecd offset 4px | button.css-165o2av 160.0x52.0 bg #f9f9f9 border T:2px #f9f9f9 / R:2px #f9f9f9 / B:2px #f9f9f9 / L:2px #f9f9f9 r 60px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `getapp-hero-default.png`, `getapp-hero-hover.png`, `getapp-hero-focus-visible.png`, `getapp-hero-pressed.png`.

#### getapp-dark

Get the app (on light). The dark-ink "Get the app" pill used on the light feature sections; measured, never clicked.

Page: home. Selector: `feature Get the app`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 160 x 52 | = | = | = |
| Padding | 0px | = | = | = |
| Border | 2px solid #292229 | 2px solid #433944 | = | 2px solid #433944 |
| Radius | 60px | = | = | = |
| Background | #292229 | #433944 | = | #433944 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #116ecd offset 4px | = |
| Font | Inter 14px/21px 600 | = | = | = |
| Letter spacing | -0.25px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | border, background, color 0.2s, 0.2s, 0.2s ease, ease, ease delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.css-wgur18 160.0x52.0 bg #292229 border T:2px #292229 / R:2px #292229 / B:2px #292229 / L:2px #292229 r 60px | button.css-wgur18 160.0x52.0 bg #433944 border T:2px #433944 / R:2px #433944 / B:2px #433944 / L:2px #433944 r 60px | button.css-wgur18 160.0x52.0 bg #292229 border T:2px #292229 / R:2px #292229 / B:2px #292229 / L:2px #292229 r 60px outline 2px solid #116ecd offset 4px | button.css-wgur18 160.0x52.0 bg #433944 border T:2px #433944 / R:2px #433944 / B:2px #433944 / L:2px #433944 r 60px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `getapp-dark-default.png`, `getapp-dark-hover.png`, `getapp-dark-focus-visible.png`, `getapp-dark-pressed.png`.

#### section-h2

Section headline. A Heldane Display 80px marketing section heading ("Track your books in one place").

Page: home. Selector: `h2 section`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 580 x 150 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Heldane Display 80px/75px 500 |
| Letter spacing | normal |
| Colour | #292229 |
| Transition | none |
| Cursor | default |
| How | at rest |

Crops: `section-h2-default.png`.

#### feature-h

Feature card heading. A 24px Inter semibold feature-card heading inside a marketing section.

Page: home. Selector: `feature card h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 200 x 80 |
| Padding | 8px 0px 16px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 24px/28px 600 |
| Letter spacing | -1px |
| Colour | #161015 |
| Transition | none |
| Cursor | default |
| Ancestor paint | 1 up div.css-uvg1b bg #f7f4ee |
| How | at rest |

Crops: `feature-h-default.png`.

#### fortune-quote

Press quote. The Fortune pull-quote — "A more thoughtful—and less toxic—social media app".

Page: home. Selector: `press quote block`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 560 x 293 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h2.css-8aby0: Heldane Display 48px/42px 500, #f7f4ee |
| Transition | none |
| Painted layers | button.css-3u91k5 160.0x44.0 bg #ffffff border T:2px #ffffff / R:2px #ffffff / B:2px #ffffff / L:2px #ffffff r 60px |
| How | at rest |

Crops: `fortune-quote-default.png`.

#### club-card

Club card. A "Popular clubs" card — hero image, club cover thumb, moderator line, member count.

Page: home. Selector: `[data-testid=club-card]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 248 x 380 | 250.48 x 383.8 |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | b: Inter 12px/16px 700, #3f383d, ls -0.2px | = |
| Transition | transform 0.4s ease-in-out | = |
| Cursor | pointer | = |
| Icon | 14 x 14, colour #000000, fill #433944 | 14.14 x 14.14, colour #000000, fill #433944 |
| Painted layers | div.css-1xixpw4 79.0x117.0 border T:2px #ffffff / R:2px #ffffff / B:2px #ffffff / L:2px #ffffff r 8px | div.css-1xixpw4 79.8x118.2 border T:2px #ffffff / R:2px #ffffff / B:2px #ffffff / L:2px #ffffff r 8px |
| How | at rest | mouse hover |
| Transform | - | matrix(1.01, 0, 0, 1.01, 0, 0) |

Crops: `club-card-default.png`, `club-card-hover.png`.

#### getapp-cta

Get the app (closing CTA). The "Get the app" pill in the closing call-to-action band; measured, never clicked.

Page: home. Selector: `closing Get the app`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 160 x 44 | = | = | = |
| Padding | 0px | = | = | = |
| Border | 2px solid #ffffff | 2px solid #f9f9f9 | = | 2px solid #f9f9f9 |
| Radius | 60px | = | = | = |
| Background | #ffffff | #f9f9f9 | = | #f9f9f9 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #116ecd offset 4px | = |
| Font | Inter 14px/21px 600 | = | = | = |
| Letter spacing | -0.25px | = | = | = |
| Colour | #161015 | #332e32 | = | #332e32 |
| Transition | border, background, color 0.2s, 0.2s, 0.2s ease, ease, ease delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.css-3u91k5 160.0x44.0 bg #ffffff border T:2px #ffffff / R:2px #ffffff / B:2px #ffffff / L:2px #ffffff r 60px | button.css-3u91k5 160.0x44.0 bg #f9f9f9 border T:2px #f9f9f9 / R:2px #f9f9f9 / B:2px #f9f9f9 / L:2px #f9f9f9 r 60px | button.css-3u91k5 160.0x44.0 bg #ffffff border T:2px #ffffff / R:2px #ffffff / B:2px #ffffff / L:2px #ffffff r 60px outline 2px solid #116ecd offset 4px | button.css-3u91k5 160.0x44.0 bg #f9f9f9 border T:2px #f9f9f9 / R:2px #f9f9f9 / B:2px #f9f9f9 / L:2px #f9f9f9 r 60px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `getapp-cta-default.png`, `getapp-cta-hover.png`, `getapp-cta-focus-visible.png`, `getapp-cta-pressed.png`.

### Footer

#### footer

Footer. The near-black footer: sitemap columns, social icons, legal links, "Your Privacy Choices".

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 507 |
| Padding | 100px 52px |
| Border | none |
| Radius | 0px |
| Background | #070607 |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | h2.css-175qsu5: Inter 18px/24px 600, #847f7c, ls -0.2px |
| Transition | none |
| Icon | 130 x 52.31, colour #ffffff |
| Painted layers | footer.css-147llds 1440.0x507.0 bg #070607; div.css-75av4b 1090.0x87.0 border T:1px #ffffff @ 0.1 / B:1px #ffffff @ 0.1 |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link. A footer sitemap link; measured, never followed.

Page: home. Selector: `footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 76.25 x 14 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | 4px | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #116ecd offset 4px | = |
| Font | Inter 15px/24px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.css-t7eqka: Inter 14px/14px 600, #ffffff, ls -0.25px | = | = | = |
| Transition | border, background, color 0.2s, 0.2s, 0.2s ease, ease, ease delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.css-1ge1xrf 76.3x14.0 r 4px outline 2px solid #116ecd offset 4px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### privacy-btn

Your Privacy Choices. The footer's Osano "Your Privacy Choices" control; measured at rest — clicking it would open the consent manager, so it was never pressed.

Page: home. Selector: `footer button Your Privacy Choices`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 168 x 21 | = |
| Padding | 0px | = |
| Gap | 6px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 14px/21px 400 | = |
| Letter spacing | -0.25px | = |
| Colour | #ffffff @ 0.5 | #ffffff |
| Transition | color 0.2s ease | = |
| Cursor | pointer | = |
| Icon | 26 x 12, colour #ffffff @ 0.5, fill #161015 | 26 x 12, colour #ffffff, fill #161015 |
| How | at rest | mouse hover |

Crops: `privacy-btn-default.png`, `privacy-btn-hover.png`.

### Clubs index

#### clubs-h1

Clubs headline. The /clubs masthead heading.

Page: clubs. Selector: `clubs h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 254 x 120 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | heldane 58px/60px 700 |
| Letter spacing | -1px |
| Colour | #1b1a1b |
| Transition | none |
| How | at rest |

Crops: `clubs-h1-default.png`.

#### search-trigger

Club search trigger. The 440x52 search field-styled button opening the "Find a club" modal — an aria-haspopup="dialog" local toggle; the opened state was measured after clicking it.

Page: clubs. Selector: `button[aria-haspopup=dialog] Search thousands`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 440 x 52 | = | = | = | = |
| Padding | 0px 8px 0px 24px | = | = | = | = |
| Gap | 8px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 9999px | = | = | = | = |
| Background | #ffffff | = | = | = | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 2px solid #0064c3 offset 2px | = | = |
| Font | Arial 13.3333px/normal 400 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #000000 | = | = | = | = |
| Text node | span.Text-module-scss-module__yXps7a__base.Text-module-scss-module__yXps7a__v-body-m: Inter 14px/20px 400, #4b4649, ls -0.2px | = | = | = | = |
| Transition | none | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Icon | 20 x 20, colour #000000, fill #ffffff | = | = | = | = |
| Painted layers | button.ClubsIndexSearchButton-module-scss-module__ykBIFa__trigger 440.0x52.0 bg #ffffff r 9999px; span.ClubsIndexSearchButton-module-scss-module__ykBIFa__submit 40.0x40.0 bg #1b1a1b r 9999px | = | button.ClubsIndexSearchButton-module-scss-module__ykBIFa__trigger 440.0x52.0 bg #ffffff r 9999px outline 2px solid #0064c3 offset 2px; span.ClubsIndexSearchButton-module-scss-module__ykBIFa__submit 40.0x40.0 bg #1b1a1b r 9999px | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |

Crops: `search-trigger-default.png`, `search-trigger-hover.png`, `search-trigger-focus-visible.png`, `search-trigger-pressed.png`, `search-trigger-opened.png`.

#### genre-pill

Genre pill. A 46px genre pill link (Fantasy) in the scrollable genre strip; measured, never followed.

Page: clubs. Selector: `a.ClubsIndexGenrePills-module__pill`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 102 x 46 | = | = | = |
| Padding | 10px 20px | = | = | = |
| Border | 1px solid #b1acaf | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #ffffff | #f8f8f8 | = | #f8f8f8 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Inter 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1b1a1b | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.ClubsIndexGenrePills-module-scss-module__asi_NW__pill 102.0x46.0 bg #ffffff border T:1px #b1acaf / R:1px #b1acaf / B:1px #b1acaf / L:1px #b1acaf r 9999px | a.ClubsIndexGenrePills-module-scss-module__asi_NW__pill 102.0x46.0 bg #f8f8f8 border T:1px #b1acaf / R:1px #b1acaf / B:1px #b1acaf / L:1px #b1acaf r 9999px | a.ClubsIndexGenrePills-module-scss-module__asi_NW__pill 102.0x46.0 bg #ffffff border T:1px #b1acaf / R:1px #b1acaf / B:1px #b1acaf / L:1px #b1acaf r 9999px outline 1px auto #101010 offset 1px | a.ClubsIndexGenrePills-module-scss-module__asi_NW__pill 102.0x46.0 bg #f8f8f8 border T:1px #b1acaf / R:1px #b1acaf / B:1px #b1acaf / L:1px #b1acaf r 9999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `genre-pill-default.png`, `genre-pill-hover.png`, `genre-pill-focus-visible.png`, `genre-pill-pressed.png`.

#### genre-scroll

Genre scroll arrow. The dark 40px arrow that scrolls the genre strip forward; measured, never clicked.

Page: clubs. Selector: `button[aria-label="Scroll genres forward"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 40 x 40 | = | = | = |
| Padding | 1px 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #1b1a1b | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | Arial 13.3333px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #000000, fill #ffffff | = | = | = |
| Painted layers | button.ClubsIndexGenrePills-module-scss-module__asi_NW__chevron 40.0x40.0 bg #1b1a1b r 9999px | = | button.ClubsIndexGenrePills-module-scss-module__asi_NW__chevron 40.0x40.0 bg #1b1a1b r 9999px outline 1px auto #101010 offset 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `genre-scroll-default.png`, `genre-scroll-hover.png`, `genre-scroll-focus-visible.png`, `genre-scroll-pressed.png`.

#### search-icon-btn

Search icon button. The cream 44px circular search affordance at the head of the genre strip; measured, never clicked.

Page: clubs. Selector: `button[aria-label="Search clubs"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 44 x 44 | = | = | = |
| Padding | 1px 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #f7f4eb | #ebe7d9 | = | #ebe7d9 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | Arial 13.3333px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1b1a1b | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #1b1a1b | = | = | = |
| Painted layers | button.ClubsIndexGenrePills-module-scss-module__asi_NW__search 44.0x44.0 bg #f7f4eb r 9999px | button.ClubsIndexGenrePills-module-scss-module__asi_NW__search 44.0x44.0 bg #ebe7d9 r 9999px | button.ClubsIndexGenrePills-module-scss-module__asi_NW__search 44.0x44.0 bg #f7f4eb r 9999px outline 1px auto #101010 offset 0px | button.ClubsIndexGenrePills-module-scss-module__asi_NW__search 44.0x44.0 bg #ebe7d9 r 9999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `search-icon-btn-default.png`, `search-icon-btn-hover.png`, `search-icon-btn-focus-visible.png`, `search-icon-btn-pressed.png`.

#### icon-btn

Carousel arrow. A 40px round bordered IconButton (Previous <shelf>) stepping a club/book carousel; measured, never clicked.

Page: clubs. Selector: `button.IconButton-module Previous`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 40 x 40 | = | - | = |
| Padding | 1px 6px | = | - | = |
| Border | 1px solid #070607 @ 0.1 | = | - | = |
| Radius | 9999px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Arial 13.3333px/normal 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #1b1a1b | = | - | = |
| Transition | background-color, color, opacity, border-color 0.15s, 0.15s, 0.15s, 0.15s ease, ease, ease, ease delay 0s, 0s, 0s, 0s | = | - | = |
| Opacity | 0.5 | = | - | = |
| Cursor | default | = | - | = |
| Icon | 24 x 24, colour #1b1a1b | = | - | = |
| Painted layers | button.IconButton-module-scss-module__PqhHDa__base.IconButton-module-scss-module__PqhHDa__sizeMd 40.0x40.0 border T:1px #070607 @ 0.1 / R:1px #070607 @ 0.1 / B:1px #070607 @ 0.1 / L:1px #070607 @ 0.1 r 9999px | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `icon-btn-default.png`, `icon-btn-hover.png`, `icon-btn-pressed.png`.

#### club-card-cat

Club card (catalog). A club card in a clubs-index shelf — image, moderator line, club name, member count; measured, never followed.

Page: clubs. Selector: `a.ClubCard-module__card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 256 x 372 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 24px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 16px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #1b1a1b | = |
| Text node | span.ClubCard-module-scss-module__j9KgBG__moderatorName: Inter 10px/16px 600, #1b1a1b, ls -0.2px | = |
| Transition | none | = |
| Cursor | pointer | = |
| Icon | 16 x 16, colour #1b1a1b | = |
| Painted layers | div.StackedBookCover-module-scss-module__ZNm-FG__root.StackedBookCover-module-scss-module__ZNm-FG__constrainWidth 256.0x238.0 bg #ebe7d9 border T:3px #f7f4eb / R:3px #f7f4eb / B:3px #f7f4eb / L:3px #f7f4eb r 24px; div.StackedBookCover-module-scss-module__ZNm-FG__backCard.StackedBookCover-module-scss-module__ZNm-FG__backCard1 111.3x150.7 bg #ffffff image linear-gradient(#eeebdf, #eeebdf), none r 8px shadow #000000 @ 0.28 0px 8px 18px 0px; div.StackedBookCover-module-scss-module__ZNm-FG__backCard.StackedBookCover-module-scss-module__ZNm-FG__backCard2 127.6x159.4 bg #ffffff image linear-gradient(#eeebdf, #eeebdf), none r 8px shadow #000000 @ 0.28 0px 8px 18px 0px; div.StackedBookCover-module-scss-module__ZNm-FG__backCard.StackedBookCover-module-scss-module__ZNm-FG__backCard3 115.6x153.2 bg #ffffff image linear-gradient(#eeebdf, #eeebdf), none r 8px shadow #000000 @ 0.28 0px 8px 18px 0px; div.StackedBookCover-module-scss-module__ZNm-FG__frontCard 123.0x184.4 bg #ffffff image linear-gradient(#eeebdf, #eeebdf), none r 8px shadow #000000 @ 0.4 0px 14px 28px 0px; div.ClubCard-module-scss-module__j9KgBG__moderatorImage 54.0x54.0 bg #ebe7d9 border T:3px #f7f4eb / R:3px #f7f4eb / B:3px #f7f4eb / L:3px #f7f4eb r 50% | = |
| How | at rest | mouse hover |

Crops: `club-card-cat-default.png`, `club-card-cat-hover.png`.

#### clubs-section-h

Shelf heading. A clubs-index shelf heading (heldane) above a horizontal card rail.

Page: clubs. Selector: `main h2 shelf`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 253.5 x 36 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | heldane 36px/36px 400 |
| Letter spacing | -0.5px |
| Colour | #1b1a1b |
| Transition | none |
| How | at rest |

Crops: `clubs-section-h-default.png`.

### Club search modal

#### search-modal

Find a club modal. The centered Modal-module sheet opened by the search trigger: drag handle, "Find a club" title, close button, search input and an empty results prompt.

Page: clubs. Selector: `[role=dialog].Modal-module__surface`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 480 x 497 |
| Padding | 0px |
| Border | 1px solid #070607 @ 0.1 |
| Radius | 24px |
| Background | #ffffff |
| Box shadow | #000000 @ 0.12 0px -6px 16px 0px |
| Outline | none |
| Font | Inter 16px/normal 400 |
| Letter spacing | normal |
| Colour | #1b1a1b |
| Text node | h2.Modal-module-scss-module__sP68xq__title: Inter 18px/23.4px 600, #1b1a1b |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, -240, -248.5) |
| Icon | 18 x 18, colour #1b1a1b |
| Painted layers | div.Modal-module-scss-module__sP68xq__surface.Modal-module-scss-module__sP68xq__sizeMd 480.0x497.0 bg #ffffff border T:1px #070607 @ 0.1 / R:1px #070607 @ 0.1 / B:1px #070607 @ 0.1 / L:1px #070607 @ 0.1 r 24px shadow #000000 @ 0.12 0px -6px 16px 0px; input.SearchModal-module-scss-module__kbR3AW__searchInput 430.0x41.0 border T:1px #070607 @ 0.1 / R:1px #070607 @ 0.1 / B:1px #070607 @ 0.1 / L:1px #070607 @ 0.1 r 12px |
| Ancestor paint | 1 up body.layout-module-scss-module__sQC2_W__body bg #ffffff |
| How | at rest |

Crops: `search-modal-default.png`.

#### search-input

Search input. The search field inside the Find a club modal; focused, never submitted.

Page: clubs. Selector: `[role=dialog].Modal-module input[type=search]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 430 x 41 | = |
| Padding | 10px 12px 10px 36px | = |
| Border | 1px solid #070607 @ 0.1 | 1px solid #1b1a1b |
| Radius | 12px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 15px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #1b1a1b | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #4b4649, opacity 1 | = |
| Painted layers | input.SearchModal-module-scss-module__kbR3AW__searchInput 430.0x41.0 border T:1px #070607 @ 0.1 / R:1px #070607 @ 0.1 / B:1px #070607 @ 0.1 / L:1px #070607 @ 0.1 r 12px | input.SearchModal-module-scss-module__kbR3AW__searchInput 430.0x41.0 border T:1px #1b1a1b / R:1px #1b1a1b / B:1px #1b1a1b / L:1px #1b1a1b r 12px |
| How | at rest | clicked into the field |

Crops: `search-input-default.png`, `search-input-focused.png`.

#### search-close

Modal close button. The icon-only close button in the modal header.

Page: clubs. Selector: `[role=dialog].Modal-module button[aria-label^=Close]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | = |
| Padding | 1px 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | transparent | #f7f4eb | #f7f4eb | #f7f4eb |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #0064c3 offset 2px | 2px solid #0064c3 offset 2px |
| Font | Arial 13.3333px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1b1a1b | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 18 x 18, colour #1b1a1b | = | = | = |
| Ancestor paint | 3 up div.Modal-module-scss-module__sP68xq__surface.Modal-module-scss-module__sP68xq__sizeMd bg #ffffff shadow #000000 @ 0.12 0px -6px 16px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | button.Modal-module-scss-module__sP68xq__closeButton 32.0x32.0 bg #f7f4eb r 9999px | button.Modal-module-scss-module__sP68xq__closeButton 32.0x32.0 bg #f7f4eb r 9999px outline 2px solid #0064c3 offset 2px | button.Modal-module-scss-module__sP68xq__closeButton 32.0x32.0 bg #f7f4eb r 9999px outline 2px solid #0064c3 offset 2px |

Crops: `search-close-default.png`, `search-close-hover.png`, `search-close-focus-visible.png`, `search-close-pressed.png`.

### App-install prompt

#### app-banner

App download banner. The app-install strip under the header with App Store and Play badges; the badge links are measured, never followed.

Page: book. Selector: `div.AppDownloadBanner-module`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 132 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #053829 |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/normal 400 |
| Letter spacing | normal |
| Colour | #064c37 |
| Text node | p.Text-module-scss-module__yXps7a__base.Text-module-scss-module__yXps7a__v-header-xs: heldane 32px/28px 400, #ffffff |
| Transition | none |
| Icon | 498 x 497, colour #064c37 |
| Painted layers | div.AppDownloadBanner-module-scss-module__ZLSn0q__main 1440.0x132.0 bg #053829; a.Button-module-scss-module__Y7nSpW__base.Button-module-scss-module__Y7nSpW__sizeXs 0.0x0.0 bg #ffffff border T:1px #ffffff / R:1px #ffffff / B:1px #ffffff / L:1px #ffffff r 9999px; div.AppDownloadBanner-module-scss-module__ZLSn0q__qrCodeContainer 84.0x84.0 bg #ffffff r 10px; svg.AppDownloadBanner-module-scss-module__ZLSn0q__appIcon 0.0x0.0 r 14.4px shadow #000000 @ 0.17 0px 7.286px 32.786px 0px |
| Ancestor paint | 1 up main.layout-module-scss-module__Z4Fsfq__main bg #ffffff |
| How | at rest |

Crops: `app-banner-default.png`.

#### store-badge

Store badge. The App Store badge inside the download banner; measured, never followed.

Page: book. Selector: `a[href*=apps.apple.com]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 68 x 23 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 16px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #0000ee | = |
| Transition | none | = |
| Cursor | pointer | = |
| How | at rest | mouse hover |

Crops: `store-badge-default.png`, `store-badge-hover.png`.

### Book detail

#### book-h1

Book title. The book detail masthead title.

Page: book. Selector: `book h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 706 x 48 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | heldane 46px/48px 700 |
| Letter spacing | -0.5px |
| Colour | #1b1a1b |
| Transition | none |
| How | at rest |

Crops: `book-h1-default.png`.

#### author-link

Author link. The author byline link in the book hero; measured, never followed.

Page: book. Selector: `a.BookDetailHero-module__authorLink`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 67.25 x 15 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Inter 12px/12px 600 | = | = | = |
| Letter spacing | -0.25px | = | = | = |
| Colour | #1b1a1b | = | = | = |
| Text node | span.Text-module-scss-module__yXps7a__base.Text-module-scss-module__yXps7a__v-button-m: Inter 12px/12px 600, #1b1a1b, ls -0.25px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.BookDetailHero-module-scss-module__mIHGba__authorLink 67.3x15.0 outline 1px auto #101010 offset 1px | = |

Crops: `author-link-default.png`, `author-link-hover.png`, `author-link-focus-visible.png`, `author-link-pressed.png`.

#### ratings-line

Ratings line. The "66,098 Ratings" anchor linking to the reviews block; measured, never followed.

Page: book. Selector: `a.BookDetailReviewLine-module__ratings`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 87.5 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Inter 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1b1a1b | = | = | = |
| Text node | span.Text-module-scss-module__yXps7a__base.Text-module-scss-module__yXps7a__v-button-m: Inter 12px/12px 600, #1b1a1b, ls -0.25px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.BookDetailReviewLine-module-scss-module__ne1zFW__ratings 87.5x20.0 outline 1px auto #101010 offset 1px | = |

Crops: `ratings-line-default.png`, `ratings-line-hover.png`, `ratings-line-focus-visible.png`, `ratings-line-pressed.png`.

#### btn-primary

Primary button. The dark 52px "Want to read" pill (Button-module primary, radius 9999); its states were measured but it was never clicked — saving to a shelf is signed-in functionality.

Page: book. Selector: `button.Button-module Want to read`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 361 x 52 | = | = | = |
| Padding | 10px 20px | = | = | = |
| Gap | 6px | = | = | = |
| Border | 1px solid #1b1a1b | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #1b1a1b | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #0064c3 offset 2px | = |
| Font | Inter 14px/normal 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color, color, opacity, border-color 0.15s, 0.15s, 0.15s, 0.15s ease, ease, ease, ease delay 0s, 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #ffffff | = | = | = |
| Painted layers | button.Button-module-scss-module__Y7nSpW__base.Button-module-scss-module__Y7nSpW__sizeLg 361.0x52.0 bg #1b1a1b border T:1px #1b1a1b / R:1px #1b1a1b / B:1px #1b1a1b / L:1px #1b1a1b r 9999px | = | button.Button-module-scss-module__Y7nSpW__base.Button-module-scss-module__Y7nSpW__sizeLg 361.0x52.0 bg #1b1a1b border T:1px #1b1a1b / R:1px #1b1a1b / B:1px #1b1a1b / L:1px #1b1a1b r 9999px outline 2px solid #0064c3 offset 2px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.85 | = | 0.85 |

Crops: `btn-primary-default.png`, `btn-primary-hover.png`, `btn-primary-focus-visible.png`, `btn-primary-pressed.png`.

#### btn-secondary

Secondary button. The outlined "Read or listen free today" pill below the primary; measured, never clicked.

Page: book. Selector: `button.Button-module Read or listen`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 361 x 52 | = | = | = |
| Padding | 10px 20px | = | = | = |
| Gap | 6px | = | = | = |
| Border | 1px solid #1b1a1b | = | = | = |
| Radius | 9999px | = | = | = |
| Background | transparent | #f7f4eb | = | #f7f4eb |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #0064c3 offset 2px | = |
| Font | Inter 14px/normal 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1b1a1b | = | = | = |
| Transition | background-color, color, opacity, border-color 0.15s, 0.15s, 0.15s, 0.15s ease, ease, ease, ease delay 0s, 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.Button-module-scss-module__Y7nSpW__base.Button-module-scss-module__Y7nSpW__sizeLg 361.0x52.0 border T:1px #1b1a1b / R:1px #1b1a1b / B:1px #1b1a1b / L:1px #1b1a1b r 9999px | button.Button-module-scss-module__Y7nSpW__base.Button-module-scss-module__Y7nSpW__sizeLg 361.0x52.0 bg #f7f4eb border T:1px #1b1a1b / R:1px #1b1a1b / B:1px #1b1a1b / L:1px #1b1a1b r 9999px | button.Button-module-scss-module__Y7nSpW__base.Button-module-scss-module__Y7nSpW__sizeLg 361.0x52.0 border T:1px #1b1a1b / R:1px #1b1a1b / B:1px #1b1a1b / L:1px #1b1a1b r 9999px outline 2px solid #0064c3 offset 2px | button.Button-module-scss-module__Y7nSpW__base.Button-module-scss-module__Y7nSpW__sizeLg 361.0x52.0 bg #f7f4eb border T:1px #1b1a1b / R:1px #1b1a1b / B:1px #1b1a1b / L:1px #1b1a1b r 9999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `btn-secondary-default.png`, `btn-secondary-hover.png`, `btn-secondary-focus-visible.png`, `btn-secondary-pressed.png`.

#### spoiler-pill

Spoiler disclosure. The olive "May contain spoilers!" pill toggling the pre-published review text — a local disclosure; pressing it reveals the text, so it was measured at rest.

Page: book. Selector: `button May contain spoilers`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 136 x 28 | = | = | = |
| Padding | 4px 12px | = | = | = |
| Gap | 6px | = | = | = |
| Border | 1px solid #526c03 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #526c03 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #0064c3 offset 2px | = |
| Font | Inter 10px/normal 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color, color, opacity, border-color 0.15s, 0.15s, 0.15s, 0.15s ease, ease, ease, ease delay 0s, 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.Button-module-scss-module__Y7nSpW__base.Button-module-scss-module__Y7nSpW__sizeXs 136.0x28.0 bg #526c03 border T:1px #526c03 / R:1px #526c03 / B:1px #526c03 / L:1px #526c03 r 9999px | = | button.Button-module-scss-module__Y7nSpW__base.Button-module-scss-module__Y7nSpW__sizeXs 136.0x28.0 bg #526c03 border T:1px #526c03 / R:1px #526c03 / B:1px #526c03 / L:1px #526c03 r 9999px outline 2px solid #0064c3 offset 2px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | = | = | 0.85 |

Crops: `spoiler-pill-default.png`, `spoiler-pill-hover.png`, `spoiler-pill-focus-visible.png`, `spoiler-pill-pressed.png`.

#### read-more

Read more toggle. The inline "Read more" disclosure expanding the book description — a local toggle; the opened state was measured after clicking it.

Page: book. Selector: `button.ExpandableText-module Read more`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 73.75 x 16 | = | = | = | 66.75 x 16 |
| Padding | 0px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 0px | = | = | = | = |
| Background | transparent | = | = | = | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = | = |
| Font | Arial 13.3333px/normal 400 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #000000 | = | = | = | = |
| Text node | span.Text-module-scss-module__yXps7a__base.Text-module-scss-module__yXps7a__v-button-l: Inter 14px/16px 600, #4b4649, ls -0.25px | = | = | = | = |
| Transition | none | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |
| Painted layers | - | = | button.ExpandableText-module-scss-module__10317G__toggle 73.8x16.0 outline 1px auto #101010 offset 0px | = | = |

Crops: `read-more-default.png`, `read-more-hover.png`, `read-more-focus-visible.png`, `read-more-pressed.png`, `read-more-opened.png`.

#### author-profile-btn

Author profile button. The outlined "View author profile" pill link; measured, never followed.

Page: book. Selector: `a.Button-module View author profile`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 171 x 40 | = | = | = |
| Padding | 8px 16px | = | = | = |
| Gap | 6px | = | = | = |
| Border | 1px solid #1b1a1b | = | = | = |
| Radius | 9999px | = | = | = |
| Background | transparent | #f7f4eb | = | #f7f4eb |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #0064c3 offset 2px | = |
| Font | Inter 14px/normal 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1b1a1b | = | = | = |
| Transition | background-color, color, opacity, border-color 0.15s, 0.15s, 0.15s, 0.15s ease, ease, ease, ease delay 0s, 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.Button-module-scss-module__Y7nSpW__base.Button-module-scss-module__Y7nSpW__sizeMd 171.0x40.0 border T:1px #1b1a1b / R:1px #1b1a1b / B:1px #1b1a1b / L:1px #1b1a1b r 9999px | a.Button-module-scss-module__Y7nSpW__base.Button-module-scss-module__Y7nSpW__sizeMd 171.0x40.0 bg #f7f4eb border T:1px #1b1a1b / R:1px #1b1a1b / B:1px #1b1a1b / L:1px #1b1a1b r 9999px | a.Button-module-scss-module__Y7nSpW__base.Button-module-scss-module__Y7nSpW__sizeMd 171.0x40.0 border T:1px #1b1a1b / R:1px #1b1a1b / B:1px #1b1a1b / L:1px #1b1a1b r 9999px outline 2px solid #0064c3 offset 2px | a.Button-module-scss-module__Y7nSpW__base.Button-module-scss-module__Y7nSpW__sizeMd 171.0x40.0 bg #f7f4eb border T:1px #1b1a1b / R:1px #1b1a1b / B:1px #1b1a1b / L:1px #1b1a1b r 9999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `author-profile-btn-default.png`, `author-profile-btn-hover.png`, `author-profile-btn-focus-visible.png`, `author-profile-btn-pressed.png`.

#### book-card

Book card. A book carousel item — cover image, title, author — linking to another book page; measured, never followed.

Page: book. Selector: `a.BookCarouselItem-module__item`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 167 x 290.5 | = |
| Padding | 0px | = |
| Gap | 8px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 16px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #1b1a1b | = |
| Text node | span.Text-module-scss-module__yXps7a__base.Text-module-scss-module__yXps7a__v-label-l: Inter 12px/16px 500, #1b1a1b, ls -0.2px | = |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | div.BookCover-module-scss-module__Q6C61G__cover.BookCarouselItem-module-scss-module__q4Pr7G__cover 167.0x250.5 bg #ebe7d9 r 8px | = |
| How | at rest | mouse hover |

Crops: `book-card-default.png`, `book-card-hover.png`.

#### club-card-book

Club card (book page). A club card in the "clubs reading this" rail; measured, never followed.

Page: book. Selector: `a.ClubCard-module__card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 256 x 372 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 24px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 16px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #1b1a1b | = |
| Text node | span.ClubCard-module-scss-module__j9KgBG__moderatorName: Inter 10px/16px 600, #1b1a1b, ls -0.2px | = |
| Transition | none | = |
| Cursor | pointer | = |
| Icon | 16 x 16, colour #1b1a1b | = |
| Painted layers | div.StackedBookCover-module-scss-module__ZNm-FG__root.StackedBookCover-module-scss-module__ZNm-FG__constrainWidth 256.0x238.0 bg #ebe7d9 border T:3px #f7f4eb / R:3px #f7f4eb / B:3px #f7f4eb / L:3px #f7f4eb r 24px; div.StackedBookCover-module-scss-module__ZNm-FG__backCard.StackedBookCover-module-scss-module__ZNm-FG__backCard1 111.3x150.7 bg #ffffff image linear-gradient(#eeebdf, #eeebdf), none r 8px shadow #000000 @ 0.28 0px 8px 18px 0px; div.StackedBookCover-module-scss-module__ZNm-FG__backCard.StackedBookCover-module-scss-module__ZNm-FG__backCard2 127.6x159.4 bg #ffffff image linear-gradient(#eeebdf, #eeebdf), none r 8px shadow #000000 @ 0.28 0px 8px 18px 0px; div.StackedBookCover-module-scss-module__ZNm-FG__backCard.StackedBookCover-module-scss-module__ZNm-FG__backCard3 115.6x153.2 bg #ffffff image linear-gradient(#eeebdf, #eeebdf), none r 8px shadow #000000 @ 0.28 0px 8px 18px 0px; div.StackedBookCover-module-scss-module__ZNm-FG__frontCard 123.0x184.4 bg #ffffff image linear-gradient(#eeebdf, #eeebdf), none r 8px shadow #000000 @ 0.4 0px 14px 28px 0px; div.ClubCard-module-scss-module__j9KgBG__moderatorImage 54.0x54.0 bg #ebe7d9 border T:3px #f7f4eb / R:3px #f7f4eb / B:3px #f7f4eb / L:3px #f7f4eb r 50% | = |
| How | at rest | mouse hover |

Crops: `club-card-book-default.png`, `club-card-book-hover.png`.

#### icon-btn-book

Carousel arrow (book). A 40px round bordered IconButton stepping the "Other books by" carousel; measured, never clicked.

Page: book. Selector: `button.IconButton-module`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 40 x 40 | = | - | = |
| Padding | 1px 6px | = | - | = |
| Border | 1px solid #070607 @ 0.1 | = | - | = |
| Radius | 9999px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Arial 13.3333px/normal 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #1b1a1b | = | - | = |
| Transition | background-color, color, opacity, border-color 0.15s, 0.15s, 0.15s, 0.15s ease, ease, ease, ease delay 0s, 0s, 0s, 0s | = | - | = |
| Opacity | 0.5 | = | - | = |
| Cursor | default | = | - | = |
| Icon | 24 x 24, colour #1b1a1b | = | - | = |
| Painted layers | button.IconButton-module-scss-module__PqhHDa__base.IconButton-module-scss-module__PqhHDa__sizeMd 40.0x40.0 border T:1px #070607 @ 0.1 / R:1px #070607 @ 0.1 / B:1px #070607 @ 0.1 / L:1px #070607 @ 0.1 r 9999px | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `icon-btn-book-default.png`, `icon-btn-book-hover.png`, `icon-btn-book-pressed.png`.

### Club detail

#### club-h1

Club name. The club masthead — heldane 46px bold "The Cozy Chaos Book Club".

Page: club. Selector: `club h1 Text-module v-header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 706 x 48 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | heldane 46px/48px 700 |
| Letter spacing | -0.5px |
| Colour | #1b1a1b |
| Transition | none |
| How | at rest |

Crops: `club-h1-default.png`.

#### club-sub

Moderator line. The 14px Inter semibold moderator byline under the club name.

Page: club. Selector: `club h3 Text-module v-subheader`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 186.2 x 16 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/16px 600 |
| Letter spacing | -0.2px |
| Colour | #1b1a1b |
| Transition | none |
| How | at rest |

Crops: `club-sub-default.png`.

#### join-cta

Join CTA. The dark "Download the app to join" pill — joining is app-only; measured, never followed.

Page: club. Selector: `a.Button-module Download the app to join`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 224 x 52 | = | = | = |
| Padding | 10px 20px | = | = | = |
| Gap | 6px | = | = | = |
| Border | 1px solid #1b1a1b | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #1b1a1b | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #0064c3 offset 2px | = |
| Font | Inter 14px/normal 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color, color, opacity, border-color 0.15s, 0.15s, 0.15s, 0.15s ease, ease, ease, ease delay 0s, 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.Button-module-scss-module__Y7nSpW__base.Button-module-scss-module__Y7nSpW__sizeLg 224.0x52.0 bg #1b1a1b border T:1px #1b1a1b / R:1px #1b1a1b / B:1px #1b1a1b / L:1px #1b1a1b r 9999px | = | a.Button-module-scss-module__Y7nSpW__base.Button-module-scss-module__Y7nSpW__sizeLg 224.0x52.0 bg #1b1a1b border T:1px #1b1a1b / R:1px #1b1a1b / B:1px #1b1a1b / L:1px #1b1a1b r 9999px outline 2px solid #0064c3 offset 2px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.85 | = | 0.85 |

Crops: `join-cta-default.png`, `join-cta-hover.png`, `join-cta-focus-visible.png`, `join-cta-pressed.png`.

#### share-btn

Share button. The round share icon button ("Share The Cozy Chaos Book Club"); measured, never clicked.

Page: club. Selector: `button.ShareButton-module`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 52 x 52 | = | = | = |
| Padding | 1px 6px | = | = | = |
| Border | 1px solid #070607 @ 0.1 | 1px solid #1b1a1b | = | 1px solid #1b1a1b |
| Radius | 9999px | = | = | = |
| Background | transparent | #f7f4eb | = | #f7f4eb |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #0064c3 offset 2px | = |
| Font | Arial 13.3333px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1b1a1b | = | = | = |
| Transition | background-color, border-color 0.15s, 0.15s ease, ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #1b1a1b | = | = | = |
| Painted layers | button.ShareButton-module-scss-module__n0SJ_W__button.ShareButton-module-scss-module__n0SJ_W__lg 52.0x52.0 border T:1px #070607 @ 0.1 / R:1px #070607 @ 0.1 / B:1px #070607 @ 0.1 / L:1px #070607 @ 0.1 r 9999px | button.ShareButton-module-scss-module__n0SJ_W__button.ShareButton-module-scss-module__n0SJ_W__lg 52.0x52.0 bg #f7f4eb border T:1px #1b1a1b / R:1px #1b1a1b / B:1px #1b1a1b / L:1px #1b1a1b r 9999px | button.ShareButton-module-scss-module__n0SJ_W__button.ShareButton-module-scss-module__n0SJ_W__lg 52.0x52.0 border T:1px #070607 @ 0.1 / R:1px #070607 @ 0.1 / B:1px #070607 @ 0.1 / L:1px #070607 @ 0.1 r 9999px outline 2px solid #0064c3 offset 2px | button.ShareButton-module-scss-module__n0SJ_W__button.ShareButton-module-scss-module__n0SJ_W__lg 52.0x52.0 bg #f7f4eb border T:1px #1b1a1b / R:1px #1b1a1b / B:1px #1b1a1b / L:1px #1b1a1b r 9999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `share-btn-default.png`, `share-btn-hover.png`, `share-btn-focus-visible.png`, `share-btn-pressed.png`.

#### club-h2

Club section heading. A heldane 36px club-page section heading ("About this club").

Page: club. Selector: `club h2 Text-module`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 678 x 36 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | heldane 36px/36px 400 |
| Letter spacing | -0.5px |
| Colour | #1b1a1b |
| Transition | none |
| How | at rest |

Crops: `club-h2-default.png`.

#### faq-q

FAQ question. A FAQ accordion question ("Are Fable book clubs free to join?") — a local toggle; the opened state was measured after clicking it.

Page: club. Selector: `button.FaqAccordion-module__faqQuestion`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 678 x 72 | = | = | = | = |
| Padding | 24px 0px | = | = | = | = |
| Gap | 8px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 0px | = | = | = | = |
| Background | transparent | = | = | = | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = | = |
| Font | Arial 13.3333px/normal 400 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #1b1a1b | = | = | = | = |
| Text node | span.Text-module-scss-module__yXps7a__base.Text-module-scss-module__yXps7a__v-subhead-xs: Inter 16px/20px 600, #1b1a1b, ls -0.2px | = | = | = | = |
| Transition | none | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Icon | 24 x 24, colour #1b1a1b | = | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |
| Painted layers | - | = | button.FaqAccordion-module-scss-module__ffolAG__faqQuestion 678.0x72.0 outline 1px auto #101010 offset 0px | = | = |

Crops: `faq-q-default.png`, `faq-q-hover.png`, `faq-q-focus-visible.png`, `faq-q-pressed.png`, `faq-q-opened.png`.

#### book-card-club

Club pick card. A "Club picks" book card (CURRENTLY READING badge, cover, title); measured, never followed.

Page: club. Selector: `a.BookCarouselItem-module__item`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 190 x 325 |
| Padding | 0px |
| Gap | 8px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/normal 400 |
| Letter spacing | normal |
| Colour | #1b1a1b |
| Text node | span.Text-module-scss-module__yXps7a__base.Text-module-scss-module__yXps7a__v-label-l: Inter 12px/16px 500, #1b1a1b, ls -0.2px |
| Transition | none |
| Cursor | pointer |
| Painted layers | div.BookCover-module-scss-module__Q6C61G__cover.BookCarouselItem-module-scss-module__q4Pr7G__cover 190.0x285.0 bg #ebe7d9 r 8px |
| How | at rest |

Crops: `book-card-club-default.png`.

### Sign-in

#### signin-h1

Sign-in headline. "Please log in" — the Heldane Display 26px heading over the sign-in card.

Page: signin. Selector: `signin h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 125 x 28 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Heldane Display 26px/28px 400 |
| Letter spacing | normal |
| Colour | #161015 |
| Transition | none |
| Cursor | default |
| How | at rest |

Crops: `signin-h1-default.png`.

#### signin-panel

Sign-in form. The sign-in form: email and password fields, show-password, the email submit and SSO buttons. Shot and measured at rest — never submitted.

Page: signin. Selector: `signin form`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 396 x 172 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.css-jbhaws: Inter 14px/14px 400, #847f7c, ls -0.2px |
| Transition | none |
| Painted layers | div.text-input.css-1ltccw 396.0x52.0 bg #ffffff border T:1px #bcbcbc / R:1px #bcbcbc / B:1px #bcbcbc / L:1px #bcbcbc r 44px; div.text-input.css-yvrp3z 396.0x52.0 bg #ffffff border T:1px #bcbcbc / R:1px #bcbcbc / B:1px #bcbcbc / L:1px #bcbcbc r 44px; button.css-f2o8q 48.0x40.0 bg #ffffff r 12px; button.css-15z6lc5 396.0x44.0 bg #292229 border T:2px #292229 / R:2px #292229 / B:2px #292229 / L:2px #292229 r 60px |
| How | at rest |

Crops: `signin-panel-default.png`.

#### field-email

Email field. The Email Address text input; focused and typed into then cleared — never submitted.

Page: signin. Selector: `input[type=email]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 394 x 50 | = | = |
| Padding | 0px 14px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | 2px solid #116ecd offset 2px | 2px solid #116ecd offset 2px |
| Font | Inter 14px/14px 400 | = | = |
| Letter spacing | -0.25px | = | = |
| Colour | #161015 | = | = |
| Transition | border, background, color 0.2s, 0.2s, 0.2s ease, ease, ease delay 0s, 0s, 0s | = | = |
| Cursor | text | = | = |
| Placeholder | #847f7c, opacity 1 | = | = |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |
| Painted layers | - | input.css-1r5n8r2 394.0x50.0 outline 2px solid #116ecd offset 2px | input.css-1r5n8r2 394.0x50.0 outline 2px solid #116ecd offset 2px |

Crops: `field-email-default.png`, `field-email-focused.png`, `field-email-filled.png`.

#### field-password

Password field. The Password input with the inline Show button; focused and typed into then cleared — never submitted.

Page: signin. Selector: `input[type=password]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 394 x 50 | = | = |
| Padding | 0px 14px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | 2px solid #116ecd offset 2px | 2px solid #116ecd offset 2px |
| Font | Inter 14px/14px 400 | = | = |
| Letter spacing | -0.25px | = | = |
| Colour | #161015 | = | = |
| Transition | border, background, color 0.2s, 0.2s, 0.2s ease, ease, ease delay 0s, 0s, 0s | = | = |
| Cursor | text | = | = |
| Placeholder | #847f7c, opacity 1 | = | = |
| How | at rest | clicked into the field | typed "example-password-123", then deleted; nothing sent |
| Painted layers | - | input.css-1r5n8r2 394.0x50.0 outline 2px solid #116ecd offset 2px | input.css-1r5n8r2 394.0x50.0 outline 2px solid #116ecd offset 2px |

Crops: `field-password-default.png`, `field-password-focused.png`, `field-password-filled.png`.

#### show-btn

Show password. The inline "Show" reveal button in the password field; measured, never clicked.

Page: signin. Selector: `button Show password`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 48 x 40 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #116ecd offset 4px | = |
| Font | Inter 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.css-jbhaws: Inter 14px/14px 400, #847f7c, ls -0.2px | = | = | = |
| Transition | border, background, color 0.2s, 0.2s, 0.2s ease, ease, ease delay 0s, 0s, 0s | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, -20) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.css-f2o8q 48.0x40.0 bg #ffffff r 12px | = | button.css-f2o8q 48.0x40.0 bg #ffffff r 12px outline 2px solid #116ecd offset 4px | = |
| Ancestor paint | 1 up div.text-input.css-yvrp3z bg #ffffff | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `show-btn-default.png`, `show-btn-hover.png`, `show-btn-focus-visible.png`, `show-btn-pressed.png`.

#### submit-btn

Login with email. The dark "Login with email" submit; its states were measured but the button was never clicked — nothing was submitted.

Page: signin. Selector: `button[type=submit] Login with email`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 396 x 44 | = | = | = |
| Padding | 0px | = | = | = |
| Border | 2px solid #292229 | 2px solid #433944 | = | 2px solid #433944 |
| Radius | 60px | = | = | = |
| Background | #292229 | #433944 | = | #433944 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #116ecd offset 4px | = |
| Font | Inter 14px/21px 600 | = | = | = |
| Letter spacing | -0.25px | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.button-label: Inter 14px/21px 600, #ffffff, ls -0.25px | = | = | = |
| Transition | border, background, color 0.2s, 0.2s, 0.2s ease, ease, ease delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.css-15z6lc5 396.0x44.0 bg #292229 border T:2px #292229 / R:2px #292229 / B:2px #292229 / L:2px #292229 r 60px | button.css-15z6lc5 396.0x44.0 bg #433944 border T:2px #433944 / R:2px #433944 / B:2px #433944 / L:2px #433944 r 60px | button.css-15z6lc5 396.0x44.0 bg #292229 border T:2px #292229 / R:2px #292229 / B:2px #292229 / L:2px #292229 r 60px outline 2px solid #116ecd offset 4px | button.css-15z6lc5 396.0x44.0 bg #433944 border T:2px #433944 / R:2px #433944 / B:2px #433944 / L:2px #433944 r 60px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `submit-btn-default.png`, `submit-btn-hover.png`, `submit-btn-focus-visible.png`, `submit-btn-pressed.png`.

#### sso-google

Continue with Google. The white Google SSO button; measured, never clicked.

Page: signin. Selector: `button[data-testid=auth-provider-google-button]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 396 x 44 | = | = | = |
| Padding | 0px | = | = | = |
| Border | 2px solid #161015 | 2px solid #2e272d | = | 2px solid #2e272d |
| Radius | 60px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #116ecd offset 4px | = |
| Font | Inter 14px/21px 600 | = | = | = |
| Letter spacing | -0.25px | = | = | = |
| Colour | #161015 | #332e32 | = | #332e32 |
| Text node | span.desktop-text: Inter 14px/21px 600, #161015, ls -0.25px | span.desktop-text: Inter 14px/21px 600, #332e32, ls -0.25px | = | span.desktop-text: Inter 14px/21px 600, #332e32, ls -0.25px |
| Transition | border, background, color 0.2s, 0.2s, 0.2s ease, ease, ease delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #161015, fill #292229 | 20 x 20, colour #332e32, fill #292229 | = | 20 x 20, colour #332e32, fill #292229 |
| Painted layers | button.css-y9k6zc 396.0x44.0 bg #ffffff border T:2px #161015 / R:2px #161015 / B:2px #161015 / L:2px #161015 r 60px | button.css-y9k6zc 396.0x44.0 bg #ffffff border T:2px #2e272d / R:2px #2e272d / B:2px #2e272d / L:2px #2e272d r 60px | button.css-y9k6zc 396.0x44.0 bg #ffffff border T:2px #161015 / R:2px #161015 / B:2px #161015 / L:2px #161015 r 60px outline 2px solid #116ecd offset 4px | button.css-y9k6zc 396.0x44.0 bg #ffffff border T:2px #2e272d / R:2px #2e272d / B:2px #2e272d / L:2px #2e272d r 60px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `sso-google-default.png`, `sso-google-hover.png`, `sso-google-focus-visible.png`, `sso-google-pressed.png`.

#### sso-apple

Continue with Apple. The white Apple SSO button; measured, never clicked.

Page: signin. Selector: `button[data-testid=auth-provider-apple-button]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 396 x 44 | = | = | = |
| Padding | 0px | = | = | = |
| Border | 2px solid #161015 | 2px solid #2e272d | = | 2px solid #2e272d |
| Radius | 60px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #116ecd offset 4px | = |
| Font | Inter 14px/21px 600 | = | = | = |
| Letter spacing | -0.25px | = | = | = |
| Colour | #161015 | #332e32 | = | #332e32 |
| Text node | span.desktop-text: Inter 14px/21px 600, #161015, ls -0.25px | span.desktop-text: Inter 14px/21px 600, #332e32, ls -0.25px | = | span.desktop-text: Inter 14px/21px 600, #332e32, ls -0.25px |
| Transition | border, background, color 0.2s, 0.2s, 0.2s ease, ease, ease delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 24, colour #161015, fill #292229 | 20 x 24, colour #332e32, fill #292229 | = | 20 x 24, colour #332e32, fill #292229 |
| Painted layers | button.css-ns4719 396.0x44.0 bg #ffffff border T:2px #161015 / R:2px #161015 / B:2px #161015 / L:2px #161015 r 60px | button.css-ns4719 396.0x44.0 bg #ffffff border T:2px #2e272d / R:2px #2e272d / B:2px #2e272d / L:2px #2e272d r 60px | button.css-ns4719 396.0x44.0 bg #ffffff border T:2px #161015 / R:2px #161015 / B:2px #161015 / L:2px #161015 r 60px outline 2px solid #116ecd offset 4px | button.css-ns4719 396.0x44.0 bg #ffffff border T:2px #2e272d / R:2px #2e272d / B:2px #2e272d / L:2px #2e272d r 60px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `sso-apple-default.png`, `sso-apple-hover.png`, `sso-apple-focus-visible.png`, `sso-apple-pressed.png`.

#### reset-link

Reset link. The "Reset it" password-reset link styled as a bold inline button; measured, never clicked.

Page: signin. Selector: `button Reset it`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 54 x 23 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | 4px | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #116ecd offset 4px | = |
| Font | Inter 14px/23px 600 | = | = | = |
| Letter spacing | -0.25px | = | = | = |
| Colour | #161015 | #332e32 | = | #332e32 |
| Text node | b: Inter 14px/23px 900, #161015, ls -0.25px | b: Inter 14px/23px 900, #332e32, ls -0.25px | = | b: Inter 14px/23px 900, #332e32, ls -0.25px |
| Transition | border, background, color 0.2s, 0.2s, 0.2s ease, ease, ease delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.css-p31fum 54.0x23.0 r 4px outline 2px solid #116ecd offset 4px | = |

Crops: `reset-link-default.png`, `reset-link-hover.png`, `reset-link-focus-visible.png`, `reset-link-pressed.png`.

#### signup-link

Sign up link. The "Sign up" link button under the SSO buttons; measured, never clicked.

Page: signin. Selector: `button Sign up`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 52.25 x 23 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | 4px | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #116ecd offset 4px | = |
| Font | Inter 14px/23px 600 | = | = | = |
| Letter spacing | -0.25px | = | = | = |
| Colour | #161015 | #332e32 | = | #332e32 |
| Transition | border, background, color 0.2s, 0.2s, 0.2s ease, ease, ease delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.css-p31fum 52.3x23.0 r 4px outline 2px solid #116ecd offset 4px | = |

Crops: `signup-link-default.png`, `signup-link-hover.png`, `signup-link-focus-visible.png`, `signup-link-pressed.png`.

### Support

#### support-h1

Support headline. The /support masthead heading on the forest-green band.

Page: support. Selector: `support h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 358.13 x 60 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Heldane Display 58px/60px 400 |
| Letter spacing | -1px |
| Colour | #e4adbb |
| Transition | none |
| Cursor | default |
| Ancestor paint | 1 up div.wrap.masthead bg #064c37 |
| How | at rest |

Crops: `support-h1-default.png`.

#### support-masthead

Support masthead band. The forest-green support masthead band (rgb(6, 76, 55)) carrying the heading and intro.

Page: support. Selector: `support h1 closest section`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 358.13 x 60 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Heldane Display 58px/60px 400 |
| Letter spacing | -1px |
| Colour | #e4adbb |
| Transition | none |
| Cursor | default |
| Ancestor paint | 1 up div.wrap.masthead bg #064c37 |
| How | at rest |

Crops: `support-masthead-default.png`.

#### help-card

Help card. The "FAQs" help-card linking to help.fable.co; measured, never followed.

Page: support. Selector: `support FAQs card`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 610 x 120 | = | = | = |
| Padding | 18px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | h3.css-ra294y: Inter 18px/24px 600, #161015, ls -0.2px | = | = | = |
| Transition | border, background, color 0.2s, 0.2s, 0.2s ease, ease, ease delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | div.support-icon 71.4x84.0 bg #f9f9f9 r 8px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Ancestor paint | - | 1 up div.support-card shadow #000000 @ 0.05 0px 30px 40px 0px | = | = |

Crops: `help-card-default.png`, `help-card-hover.png`, `help-card-focus-visible.png`, `help-card-pressed.png`.

#### email-card

Email card. The "Email" help-card (mailto:support@fable.co); measured, never followed.

Page: support. Selector: `support Email card`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 610 x 120 | = | = | = |
| Padding | 18px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | h3.css-ra294y: Inter 18px/24px 600, #161015, ls -0.2px | = | = | = |
| Transition | border, background, color 0.2s, 0.2s, 0.2s ease, ease, ease delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | div.support-icon 71.4x84.0 bg #f9f9f9 r 8px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Ancestor paint | - | 1 up div.support-card shadow #000000 @ 0.05 0px 30px 40px 0px | = | = |

Crops: `email-card-default.png`, `email-card-hover.png`, `email-card-focus-visible.png`, `email-card-pressed.png`.

### Mobile (390 wide)

#### m-header

Mobile header. The phone top bar: Fable mark, "Sign up or log in" and cart icons. The off-canvas nav sheet is measured below in its opened state.

Page: mobile. Selector: `mobile header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 60 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | #000000 @ 0.04 0px 2px 3px -2px |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | button.css-kfjk5e: Inter 24px/36px 600, #070607, ls -0.25px |
| Transition | none |
| Icon | 82 x 33, colour #000000 |
| Painted layers | header.css-1vg9pjt 390.0x60.0 shadow #000000 @ 0.04 0px 2px 3px -2px; div.css-1g7irsi 374.0x50.0 bg #ffffff border T:1px #ededed / R:1px #ededed / B:1px #ededed / L:1px #ededed r 12px shadow #000000 @ 0.08 0px 4px 12px 0px; span.css-1pyn1fk 17.0x17.0 bg #ffffff border T:1px #ededed / L:1px #ededed r 2px 0px 0px; div.css-ghxh7s 390.0x844.0 bg #f7f4ee; button.css-kfjk5e 330.0x60.0 bg #ffffff border T:2px #ffffff / R:2px #ffffff / B:2px #ffffff / L:2px #ffffff r 60px; button.css-kfjk5e 330.0x60.0 bg #ffffff border T:2px #ffffff / R:2px #ffffff / B:2px #ffffff / L:2px #ffffff r 60px |
| How | at rest |

Crops: `m-header-default.png`.

#### m-logo

Mobile logo. The Fable mark-and-wordmark svg at 390 wide.

Page: mobile. Selector: `mobile header logo`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 82 x 33 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | border, background, color 0.2s, 0.2s, 0.2s ease, ease, ease delay 0s, 0s, 0s |
| Cursor | pointer |
| Icon | 82 x 33, colour #000000 |
| Ancestor paint | 3 up header.css-1vg9pjt shadow #000000 @ 0.04 0px 2px 3px -2px |
| How | at rest |

Crops: `m-logo-default.png`.

#### m-hero-h1

Mobile hero headline. The masthead at 390 wide.

Page: mobile. Selector: `mobile h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 320 x 80 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Heldane Display 46px/40px 500 |
| Letter spacing | normal |
| Colour | #f7f4ee |
| Transition | none |
| Cursor | default |
| How | at rest |

Crops: `m-hero-h1-default.png`.

#### m-getapp

Mobile Get the app. The hero "Get the app" pill at 390 wide; measured, never clicked.

Page: mobile. Selector: `mobile Get the app`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 160 x 52 | = | = | = |
| Padding | 0px | = | = | = |
| Border | 2px solid #ffffff | 2px solid #f9f9f9 | = | 2px solid #f9f9f9 |
| Radius | 60px | = | = | = |
| Background | #ffffff | #f9f9f9 | = | #f9f9f9 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #116ecd offset 4px | = |
| Font | Inter 14px/21px 600 | = | = | = |
| Letter spacing | -0.25px | = | = | = |
| Colour | #161015 | #332e32 | = | #332e32 |
| Transition | border, background, color 0.2s, 0.2s, 0.2s ease, ease, ease delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.css-165o2av 160.0x52.0 bg #ffffff border T:2px #ffffff / R:2px #ffffff / B:2px #ffffff / L:2px #ffffff r 60px | button.css-165o2av 160.0x52.0 bg #f9f9f9 border T:2px #f9f9f9 / R:2px #f9f9f9 / B:2px #f9f9f9 / L:2px #f9f9f9 r 60px | button.css-165o2av 160.0x52.0 bg #ffffff border T:2px #ffffff / R:2px #ffffff / B:2px #ffffff / L:2px #ffffff r 60px outline 2px solid #116ecd offset 4px | button.css-165o2av 160.0x52.0 bg #f9f9f9 border T:2px #f9f9f9 / R:2px #f9f9f9 / B:2px #f9f9f9 / L:2px #f9f9f9 r 60px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-getapp-default.png`, `m-getapp-hover.png`, `m-getapp-focus-visible.png`, `m-getapp-pressed.png`.

#### m-club-card

Mobile club card. A Popular-clubs card at 390 wide.

Page: mobile. Selector: `mobile club-card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 316.89 x 380 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | b: Inter 10px/12px 700, #3f383d, ls -0.2px |
| Transition | none |
| Cursor | pointer |
| Icon | 10 x 10, colour #000000, fill #433944 |
| Painted layers | div.css-1xixpw4 85.0x136.0 border T:2px #ffffff / R:2px #ffffff / B:2px #ffffff / L:2px #ffffff r 8px |
| How | at rest |

Crops: `m-club-card-default.png`.

#### m-footer

Mobile footer. The near-black footer stacked at 390 wide.

Page: mobile. Selector: `mobile footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 762 |
| Padding | 80px 24px |
| Border | none |
| Radius | 0px |
| Background | #070607 |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | h2.css-175qsu5: Inter 18px/24px 600, #847f7c, ls -0.2px |
| Transition | none |
| Icon | 82 x 33, colour #ffffff |
| Painted layers | footer.css-147llds 390.0x762.0 bg #070607; div.css-75av4b 342.0x215.0 border T:1px #ffffff @ 0.1 / B:1px #ffffff @ 0.1 |
| How | at rest |

Crops: `m-footer-default.png`.

#### m-menu-btn

Mobile menu button. The hamburger div opening the off-canvas nav sheet; its rest states were measured and the sheet was opened once for the rows below.

Page: mobile. Selector: `[aria-label="Open menu"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 18 x 16 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | 4px | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #116ecd offset 4px | = |
| Font | Inter 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | span 18.0x2.0 bg #161015; span 18.0x2.0 bg #161015; span 18.0x2.0 bg #161015 | = | div.css-1tnrd7z 18.0x16.0 r 4px outline 2px solid #116ecd offset 4px; span 18.0x2.0 bg #161015; span 18.0x2.0 bg #161015; span 18.0x2.0 bg #161015 | = |
| Ancestor paint | 1 up header.css-1vg9pjt shadow #000000 @ 0.04 0px 2px 3px -2px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-menu-btn-default.png`, `m-menu-btn-hover.png`, `m-menu-btn-focus-visible.png`, `m-menu-btn-pressed.png`.

#### m-nav

Mobile nav sheet. The full-screen cream nav sheet slid in from x=-390: pill links (Clubs / Books / Library / Blog / Log in), footer links and the copyright line. Opened by clicking the hamburger — a local UI toggle.

Page: mobile. Selector: `header off-canvas nav sheet`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 844 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #f7f4ee |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | button.css-kfjk5e: Inter 24px/36px 600, #070607, ls -0.25px |
| Transition | transform 0.2s ease |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Painted layers | div.css-11ztho2 390.0x844.0 bg #f7f4ee; button.css-kfjk5e 330.0x60.0 bg #ffffff border T:2px #ffffff / R:2px #ffffff / B:2px #ffffff / L:2px #ffffff r 60px; button.css-kfjk5e 330.0x60.0 bg #ffffff border T:2px #ffffff / R:2px #ffffff / B:2px #ffffff / L:2px #ffffff r 60px; button.css-kfjk5e 330.0x60.0 bg #ffffff border T:2px #ffffff / R:2px #ffffff / B:2px #ffffff / L:2px #ffffff r 60px; button.css-kfjk5e 330.0x60.0 bg #ffffff border T:2px #ffffff / R:2px #ffffff / B:2px #ffffff / L:2px #ffffff r 60px; button.css-kfjk5e 330.0x60.0 bg #ffffff border T:2px #ffffff / R:2px #ffffff / B:2px #ffffff / L:2px #ffffff r 60px |
| Ancestor paint | 1 up header.css-1vg9pjt shadow #000000 @ 0.04 0px 2px 3px -2px |
| How | at rest |

Crops: `m-nav-default.png`.

#### m-nav-link

Nav sheet link. A pill link inside the opened nav sheet; measured while the sheet was open, never followed.

Page: mobile. Selector: `nav sheet button Clubs`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 330 x 60 | = | = | = |
| Padding | 0px | = | = | = |
| Border | 2px solid #ffffff | 2px solid #f9f9f9 | 2px solid #f9f9f9 | 2px solid #f9f9f9 |
| Radius | 60px | = | = | = |
| Background | #ffffff | #f9f9f9 | #f9f9f9 | #f9f9f9 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #116ecd offset 4px | 2px solid #116ecd offset 4px |
| Font | Inter 24px/36px 600 | = | = | = |
| Letter spacing | -0.25px | = | = | = |
| Colour | #070607 | #332e32 | #332e32 | #332e32 |
| Transition | border, background, color 0.2s, 0.2s, 0.2s ease, ease, ease delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.css-kfjk5e 330.0x60.0 bg #ffffff border T:2px #ffffff / R:2px #ffffff / B:2px #ffffff / L:2px #ffffff r 60px | button.css-kfjk5e 330.0x60.0 bg #f9f9f9 border T:2px #f9f9f9 / R:2px #f9f9f9 / B:2px #f9f9f9 / L:2px #f9f9f9 r 60px | button.css-kfjk5e 330.0x60.0 bg #f9f9f9 border T:2px #f9f9f9 / R:2px #f9f9f9 / B:2px #f9f9f9 / L:2px #f9f9f9 r 60px outline 2px solid #116ecd offset 4px | button.css-kfjk5e 330.0x60.0 bg #f9f9f9 border T:2px #f9f9f9 / R:2px #f9f9f9 / B:2px #f9f9f9 / L:2px #f9f9f9 r 60px outline 2px solid #116ecd offset 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-nav-link-default.png`, `m-nav-link-hover.png`, `m-nav-link-focus-visible.png`, `m-nav-link-pressed.png`.

### Discover (dark)

#### disc-wall

Cover wall. The /discover cover wall under its dark-green radial scrim (rgba(12, 92, 66, 0.85)); a whole-page dark surface, not a .dark-scope paint.

Page: discover. Selector: `main.app-content > div`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 900 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Background image | radial-gradient(120% 95% at 50% 32%, #0c5c42 @ 0.85, #000000 @ 0 64%), radial-gradient(85% 75% at 12% 4%, #094a36 @ 0.6, #000000 @ 0 62%), radial-gradient(80% 70% at 92% 100%, #03281d @ 0.7, #000000 @ 0 64%), linear-grad |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #f7f4ee |
| Text node | span.css-1jrewy3: Heldane Display 20px/20px 600, #f7f4ee, ls -0.1px |
| Transition | none |
| Icon | 80.75 x 32.5, colour #f7f4ee |
| Painted layers | div.css-1h32q44 1440.0x900.0 image radial-gradient(120% 95% at 50% 32%, #0c5c42 @ 0.85, #000000 @ 0 64%), radial-gradient(85%; div.drift-card.css-rhf5bg 76.2x114.3 r 8px shadow #000000 @ 0.45 0px 1px 2px 0px, #000000 @ 0.5 0px 6px 18px 0px, #f7f4ee @ 0.1 0px 0px 10px 1px, #f7f4ee @ 0.05 0px 0px 24px 6px; div.drift-card.css-rhf5bg 76.2x114.3 r 8px shadow #000000 @ 0.45 0px 1px 2px 0px, #000000 @ 0.5 0px 6px 18px 0px, #f7f4ee @ 0.1 0px 0px 10px 1px, #f7f4ee @ 0.05 0px 0px 24px 6px; div.drift-card.css-rhf5bg 76.2x114.3 r 8px shadow #000000 @ 0.45 0px 1px 2px 0px, #000000 @ 0.5 0px 6px 18px 0px, #f7f4ee @ 0.1 0px 0px 10px 1px, #f7f4ee @ 0.05 0px 0px 24px 6px; div.drift-card.css-rhf5bg 76.2x114.3 r 8px shadow #000000 @ 0.45 0px 1px 2px 0px, #000000 @ 0.5 0px 6px 18px 0px, #f7f4ee @ 0.1 0px 0px 10px 1px, #f7f4ee @ 0.05 0px 0px 24px 6px; div.drift-card.css-rhf5bg 76.2x114.3 r 8px shadow #000000 @ 0.45 0px 1px 2px 0px, #000000 @ 0.5 0px 6px 18px 0px, #f7f4ee @ 0.1 0px 0px 10px 1px, #f7f4ee @ 0.05 0px 0px 24px 6px |
| How | at rest |

Crops: `disc-wall-default.png`.

#### disc-h1

Discover headline. "Find new books by browsing similar covers" — the Heldane Display 64px pearl masthead on the dark wall.

Page: discover. Selector: `discover h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1119.91 x 69.11 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Heldane Display 64px/69.12px 500 |
| Letter spacing | normal |
| Colour | #f7f4ee |
| Transition | none |
| Cursor | default |
| How | at rest |

Crops: `disc-h1-default.png`.

#### disc-field

Book search field. The white 420x60 search pill ("Search for a book you love..."); focused and typed into then cleared — never submitted.

Page: discover. Selector: `input[placeholder*="book you love"]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 420 x 60.19 | = | = |
| Padding | 19.6px 30.8px 19.6px 61px | = | = |
| Border | none | = | = |
| Radius | 60px | = | = |
| Background | #ffffff | = | = |
| Box shadow | #0c0c0c @ 0.45 0px 10px 34px 0px | #0c0c0c @ 0.45 0px 10px 34px 0px, #f7f4ee @ 0.7 0px 0px 0px 3px | #0c0c0c @ 0.45 0px 10px 34px 0px, #f7f4ee @ 0.7 0px 0px 0px 3px |
| Outline | none | = | = |
| Font | Inter 14px/21px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #161015 | = | = |
| Transition | background, color, box-shadow 0.2s, 0.2s, 0.2s ease, ease, ease delay 0s, 0s, 0s | = | = |
| Cursor | text | = | = |
| Placeholder | #161015 @ 0.5, opacity 1 | = | = |
| Painted layers | input.css-1nlrkcz 420.0x60.2 bg #ffffff r 60px shadow #0c0c0c @ 0.45 0px 10px 34px 0px | input.css-1nlrkcz 420.0x60.2 bg #ffffff r 60px shadow #0c0c0c @ 0.45 0px 10px 34px 0px, #f7f4ee @ 0.7 0px 0px 0px 3px | input.css-1nlrkcz 420.0x60.2 bg #ffffff r 60px shadow #0c0c0c @ 0.45 0px 10px 34px 0px, #f7f4ee @ 0.7 0px 0px 0px 3px |
| How | at rest | clicked into the field | typed "project hail mary", then deleted; nothing sent |

Crops: `disc-field-default.png`, `disc-field-focused.png`, `disc-field-filled.png`.

#### disc-random

Random button. The forest-400 "Random" pill shuffling the cover wall; measured, never clicked.

Page: discover. Selector: `button Random`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 126.78 x 50.38 | = | = | = |
| Padding | 14.7px 22.4px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 999px | = | = | = |
| Background | #042119 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 14px/21px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #c5c1c5 | #f7f4ee | = | #f7f4ee |
| Transition | border, background, color 0.2s, 0.2s, 0.2s ease, ease, ease delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 17 x 17, colour #c5c1c5 | 17 x 17, colour #f7f4ee | = | 17 x 17, colour #f7f4ee |
| Painted layers | button.css-pt1o18 126.8x50.4 bg #042119 r 999px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `disc-random-default.png`, `disc-random-hover.png`, `disc-random-focus-visible.png`, `disc-random-pressed.png`.

#### disc-whatis

What is this button. The matching "What is this?" pill; measured, never clicked.

Page: discover. Selector: `button What is this`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 135.78 x 50.38 | = | = | = |
| Padding | 14.7px 22.4px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 999px | = | = | = |
| Background | #042119 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 14px/21px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #c5c1c5 | #f7f4ee | = | #f7f4ee |
| Transition | border, background, color 0.2s, 0.2s, 0.2s ease, ease, ease delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.css-pt1o18 135.8x50.4 bg #042119 r 999px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `disc-whatis-default.png`, `disc-whatis-hover.png`, `disc-whatis-focus-visible.png`, `disc-whatis-pressed.png`.

#### disc-wordmark

Fable wordmark (discover). The fable wordmark link at the top of the dark wall; measured, never followed.

Page: discover. Selector: `discover wordmark`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 80.75 x 32.5 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/16px 500 |
| Letter spacing | normal |
| Colour | #f7f4ee |
| Transition | border, background, color 0.2s, 0.2s, 0.2s ease, ease, ease delay 0s, 0s, 0s |
| Cursor | pointer |
| Icon | 80.75 x 32.5, colour #f7f4ee |
| How | at rest |

Crops: `disc-wordmark-default.png`.

## Transitions declared in the readable stylesheets

fable.co serves its CSS cross-origin from fablecdn.net, so the CSSOM cannot read the app bundles' rules and this list holds the transitions the same-origin inline sheets declare on each page; the per-state Transition rows above are computed values and cover every rule the page paints.

- book: `transform 0.1s linear, opacity 0.2s linear, visibility linear`, `flex-grow 1s linear`, `none`, `opacity 0.2s linear, visibility 0.2s linear 0.2s`, `opacity 0.2s linear, visibility linear`, `background-color 0.15s, color 0.15s, opacity 0.15s, border-color 0.15s`, `background-color 0.12s, border-color 0.12s`, `opacity 0.12s`, `transform 0.2s cubic-bezier(0.2, 0.7, 0.3, 1)`, `transform 0.2s cubic-bezier(0.4, 0, 0.6, 1)`, `border-color 0.12s`, `transform 0.12s`

- club: `transform 0.1s linear, opacity 0.2s linear, visibility linear`, `flex-grow 1s linear`, `none`, `opacity 0.2s linear, visibility 0.2s linear 0.2s`, `opacity 0.2s linear, visibility linear`, `background-color 0.15s, color 0.15s, opacity 0.15s, border-color 0.15s`, `background-color 0.12s, border-color 0.12s`, `opacity 0.12s`, `transform 0.2s cubic-bezier(0.2, 0.7, 0.3, 1)`, `transform 0.2s cubic-bezier(0.4, 0, 0.6, 1)`, `border-color 0.12s`, `transform 0.12s`

- clubs: `transform 0.1s linear, opacity 0.2s linear, visibility linear`, `flex-grow 1s linear`, `none`, `opacity 0.2s linear, visibility 0.2s linear 0.2s`, `opacity 0.2s linear, visibility linear`, `background-color 0.15s, color 0.15s, opacity 0.15s, border-color 0.15s`, `background-color 0.12s, border-color 0.12s`, `opacity 0.12s`, `transform 0.2s cubic-bezier(0.2, 0.7, 0.3, 1)`, `transform 0.2s cubic-bezier(0.4, 0, 0.6, 1)`, `border-color 0.12s`, `transform 0.12s`

- discover: `transform 0.1s linear, opacity 0.2s linear, visibility linear`, `flex-grow 1s linear`, `none`, `opacity 0.2s linear, visibility 0.2s linear 0.2s`, `opacity 0.2s linear, visibility linear`, `opacity 0.2s`, `border 0.2s, background 0.2s, color 0.2s`, `opacity 900ms`, `background 1200ms`, `background 0.2s, color 0.2s, box-shadow 0.2s`, `max-width 0.28s cubic-bezier(0.22, 1, 0.36, 1), opacity 0.18s, margin 0.28s cubic-bezier(0.22, 1, 0.36, 1), padding 0.28s cubic-bezier(0.22, 1, 0.36, 1)`, `background 0.2s`

- home: `transform 0.1s linear, opacity 0.2s linear, visibility linear`, `flex-grow 1s linear`, `none`, `opacity 0.2s linear, visibility 0.2s linear 0.2s`, `opacity 0.2s linear, visibility linear`, `opacity 0.2s`, `border 0.2s, background 0.2s, color 0.2s`, `background-color 0.2s`, `height 0.2s, background-color 0.2s`, `opacity 0.2s 0.2s`, `color 0.2s`, `transform 0.2s`

- signin: `transform 0.1s linear, opacity 0.2s linear, visibility linear`, `flex-grow 1s linear`, `none`, `opacity 0.2s linear, visibility 0.2s linear 0.2s`, `opacity 0.2s linear, visibility linear`, `opacity 0.2s`, `border 0.2s, background 0.2s, color 0.2s`, `background-color 0.2s`, `height 0.2s, background-color 0.2s`, `opacity 0.2s 0.2s`, `color 0.2s`, `transform 0.2s`

- support: `transform 0.1s linear, opacity 0.2s linear, visibility linear`, `flex-grow 1s linear`, `none`, `opacity 0.2s linear, visibility 0.2s linear 0.2s`, `opacity 0.2s linear, visibility linear`, `opacity 0.2s`, `border 0.2s, background 0.2s, color 0.2s`, `background-color 0.2s`, `height 0.2s, background-color 0.2s`, `opacity 0.2s 0.2s`, `color 0.2s`, `transform 0.2s`

## Reduced motion

- book (`button[class*="Button-module"]` under prefers-reduced-motion): transition `all`, animation `none 0s ease 0s 1 normal none running`, html scroll-behavior `auto`
