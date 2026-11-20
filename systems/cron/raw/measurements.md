# Component measurements

Computed styles read from cron.com on 2026-11-12 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the dark home page, /blog, /changelog and a /blog/<post> article (the Mobile group on the home and /blog) — and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### site-header

Site header. The 120px header: the Cron logotype and the nav (Blog / Changelog / Docs / Login / Sign up).

Page: home. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 120 |
| Padding | 0px 140px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Helvetica Neue 22px/37.4px 400 |
| Letter spacing | normal |
| Colour | #cccccc |
| Text node | a: Helvetica Neue 22px/37.4px 500, #ffffff |
| Transition | none |
| Icon | 0 x 0, colour #cccccc |
| Painted layers | a.primary-link-button.glow 125.4x46.0 bg #ff4700 r 9999px shadow #ff4700 @ 0.2 0px 0px 100px 0px |
| Ancestor paint | 1 up body bg #161412 |
| How | at rest |

Crops: `site-header-default.png`.

#### logotype

Logotype. The Cron logotype image (40px tall).

Page: home. Selector: `#logotype`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 126.66 x 40 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Helvetica Neue 22px/37.4px 500 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `logotype-default.png`.

#### nav-link

Nav link. A top-nav link (Blog); measured, never followed.

Page: home. Selector: `.nav-menu a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 46.89 x 37.41 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Helvetica Neue 22px/37.4px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a 46.9x37.4 outline 1px auto #005fcc offset 1px | = |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### login-link

Login link. The Login link to calendar.notion.so; measured, never followed.

Page: home. Selector: `Login link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 56.66 x 37.41 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Helvetica Neue 22px/37.4px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a 56.7x37.4 outline 1px auto #005fcc offset 1px | = |

Crops: `login-link-default.png`, `login-link-hover.png`, `login-link-focus-visible.png`, `login-link-pressed.png`.

#### signup-btn

Sign up button. The #ff4700 Sign up pill (9999px radius, the --glow shadow var); measured, never followed.

Page: home. Selector: `a.primary-link-button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 125.42 x 46 | = | = | = |
| Padding | 12px 24px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #ff4700 | = | = | = |
| Box shadow | #ff4700 @ 0.2 0px 0px 100px 0px | #ff4700 @ 0.4 0px 0px 25px 0px | = | #ff4700 @ 0.4 0px 0px 25px 0px |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Helvetica Neue 22px/22px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | opacity, box-shadow 0.175s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.primary-link-button.glow 125.4x46.0 bg #ff4700 r 9999px shadow #ff4700 @ 0.2 0px 0px 100px 0px | a.primary-link-button.glow 125.4x46.0 bg #ff4700 r 9999px shadow #ff4700 @ 0.4 0px 0px 25px 0px | a.primary-link-button.glow 125.4x46.0 bg #ff4700 r 9999px shadow #ff4700 @ 0.2 0px 0px 100px 0px outline 1px auto #005fcc offset 1px | a.primary-link-button.glow 125.4x46.0 bg #ff4700 r 9999px shadow #ff4700 @ 0.4 0px 0px 25px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signup-btn-default.png`, `signup-btn-hover.png`, `signup-btn-focus-visible.png`, `signup-btn-pressed.png`.

### Home

#### banner

Rebrand banner. "Cron is now Notion Calendar →" — the #161412 pill with the orange inset ring and glow shadow; measured, never followed.

Page: home. Selector: `.banner`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 269.19 x 45 | = | = | = |
| Padding | 0px 24px 1px 24px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | #161412 | = | = | = |
| Box shadow | #ff4700 @ 0.5 0px 0px 0px 0.5px inset, #ff4800 @ 0.2 0px 0px 28px 0px | #ff4700 @ 0.75 0px 0px 0px 0.5px inset, #ff4800 @ 0.2 0px 0px 28px 0px | = | #ff4700 @ 0.75 0px 0px 0px 0.5px inset, #ff4800 @ 0.2 0px 0px 28px 0px |
| Outline | none | = | = | = |
| Font | Helvetica Neue 15px/15px 400 | = | = | = |
| Letter spacing | 0.15px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | box-shadow 0.175s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.banner 269.2x45.0 bg #161412 r 4px shadow #ff4700 @ 0.5 0px 0px 0px 0.5px inset, #ff4800 @ 0.2 0px 0px 28px 0px | a.banner 269.2x45.0 bg #161412 r 4px shadow #ff4700 @ 0.75 0px 0px 0px 0.5px inset, #ff4800 @ 0.2 0px 0px 28px 0px | = | a.banner 269.2x45.0 bg #161412 r 4px shadow #ff4700 @ 0.75 0px 0px 0px 0.5px inset, #ff4800 @ 0.2 0px 0px 28px 0px |
| Ancestor paint | 1 up body bg #161412 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `banner-default.png`, `banner-hover.png`, `banner-focus-visible.png`, `banner-pressed.png`.

#### hero-h1

Hero heading. "It's about time." — 140px/-3px tracking Helvetica at 90% leading.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1000 x 126 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Helvetica Neue 140px/126px 700 |
| Letter spacing | -3px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `hero-h1-default.png`.

#### hero-sub

Hero subline. "Cron is the next-generation calendar for professionals and teams."

Page: home. Selector: `hero p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1000 x 37.41 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Helvetica Neue 22px/37.4px 400 |
| Letter spacing | normal |
| Colour | #cccccc |
| Transition | none |
| How | at rest |

Crops: `hero-sub-default.png`.

### Footer

#### footer

Footer. The #0f0d0a footer: Privacy / Terms / Web app / Download links.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 180 |
| Padding | 20px 140px 40px 140px |
| Border | none |
| Radius | 0px |
| Background | #0f0d0a |
| Box shadow | none |
| Outline | none |
| Font | Helvetica Neue 13px/37.4px 400 |
| Letter spacing | normal |
| Colour | #cccccc |
| Text node | a: Helvetica Neue 13px/19.5px 500, #ffffff |
| Transition | none |
| Painted layers | footer 1440.0x180.0 bg #0f0d0a |
| Ancestor paint | 1 up body bg #161412 |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link. A footer link (Privacy Policy); measured, never followed.

Page: home. Selector: `footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 84.58 x 16 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Helvetica Neue 13px/19.5px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a 84.6x16.0 outline 1px auto #005fcc offset 1px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

### Blog

#### blog-h1

Blog heading. "Cron Blog" — the index heading.

Page: blog. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 676 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Helvetica Neue 40px/24px 700 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `blog-h1-default.png`.

#### post-entry

Post entry. A blog index entry: date, title, byline and excerpt; measured, never followed.

Page: blog. Selector: `post entry`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 676 x 987.53 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Helvetica Neue 16px/24px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #000000 | = | - | = |
| Text node | a: Helvetica Neue 16px/16px 400, #616161 | = | - | = |
| Transition | none | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `post-entry-default.png`, `post-entry-hover.png`, `post-entry-pressed.png`.

### Changelog

#### changelog-h1

Changelog heading. "Cron Changelog" — the index heading.

Page: changelog. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 676 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Helvetica Neue 40px/24px 700 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `changelog-h1-default.png`.

#### changelog-entry

Changelog entry. A dated release entry (title + notes).

Page: changelog. Selector: `changelog entry`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 676 x 1014.66 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Helvetica Neue 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | a: Helvetica Neue 16px/16px 400, #616161 |
| Transition | none |
| Painted layers | div.Changelog_coverImage__bo_xl.emailFullWidth 676.0x450.7 image linear-gradient(#fa6c38, #f44e25); code 32.5x19.0 bg #cccccc r 3px; code 19.4x19.0 bg #cccccc r 3px; code 14.3x19.0 bg #cccccc r 3px; code 32.5x19.0 bg #cccccc r 3px; code 19.4x19.0 bg #cccccc r 3px |
| How | at rest |

Crops: `changelog-entry-default.png`.

#### feature-h2

Feature heading. A feature title inside an entry ("New name").

Page: changelog. Selector: `feature heading`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 676 x 36 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Helvetica Neue 24px/36px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `feature-h2-default.png`.

#### demo-link

Demo link. The "View demo" link inside a release entry; measured, never followed.

Page: changelog. Selector: `View demo link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 79.13 x 18 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Helvetica Neue 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ff4700 | #ca3800 | = | #ca3800 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.Changelog_demo__Goa_z 79.1x18.0 outline 1px auto #005fcc offset 1px | = |

Crops: `demo-link-default.png`, `demo-link-hover.png`, `demo-link-focus-visible.png`, `demo-link-pressed.png`.

### Post

#### post-h1

Post title. "Cron is now Notion Calendar" — the post heading.

Page: post. Selector: `post h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 676 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Helvetica Neue 32px/24px 700 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `post-h1-default.png`.

#### post-meta

Post byline. The date + "By Raphael Schaad" byline.

Page: post. Selector: `post byline`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 139.61 x 18 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Helvetica Neue 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `post-meta-default.png`.

#### post-body

Body paragraph. A body paragraph in the post (22px/170%).

Page: post. Selector: `post p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 676 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Helvetica Neue 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | em: Helvetica Neue 16px/24px 400, #000000 |
| Transition | none |
| How | at rest |

Crops: `post-body-default.png`.

#### post-video

Post media. The post's demo video/image (16px radius on desktop).

Page: post. Selector: `post media`. States: .

Not found on the page at capture time.

#### post-media

Post media. The post's demo media (675x450).

Page: post. Selector: `post media`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 675.98 x 450.66 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Helvetica Neue 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ff4700 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `post-media-default.png`.

#### post-back

Back link. "← All blog posts" — the article back link; measured, never followed.

Page: post. Selector: `back link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 117.94 x 16 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Helvetica Neue 16px/16px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #616161 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a 117.9x16.0 outline 1px auto #005fcc offset 1px | = |

Crops: `post-back-default.png`, `post-back-hover.png`, `post-back-focus-visible.png`, `post-back-pressed.png`.

### Mobile (390 wide)

#### m-header

Mobile header.

Page: home. Selector: `header at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 96 |
| Padding | 28px 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Helvetica Neue 16px/27.2px 400 |
| Letter spacing | normal |
| Colour | #cccccc |
| Transition | none |
| Icon | 24 x 24, colour #cccccc |
| Painted layers | ul.nav-menu 0.0x0.0 bg #161412; a.primary-link-button.glow 0.0x0.0 bg #ff4700 r 9999px shadow #ff4700 @ 0.2 0px 0px 100px 0px |
| Ancestor paint | 1 up body bg #161412 |
| How | at rest |

Crops: `m-header-default.png`.

#### m-menu-button

Menu button. The 24x18 menu icon that toggles body.showing-menu.

Page: home. Selector: `.nav-menu-button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 24 x 18 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Helvetica Neue 16px/27.2px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #cccccc | = | - | = |
| Transition | none | = | - | = |
| Icon | 24 x 24, colour #cccccc | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `m-menu-button-default.png`, `m-menu-button-hover.png`, `m-menu-button-pressed.png`.

#### m-menu-open

Mobile menu, open. The opened nav overlay (.nav-menu over #161412).

Page: home. Selector: `opened mobile menu`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 768 |
| Padding | 16px 0px |
| Border | none |
| Radius | 0px |
| Background | #161412 |
| Box shadow | none |
| Outline | none |
| Font | Helvetica Neue 16px/27.2px 400 |
| Letter spacing | normal |
| Colour | #cccccc |
| Text node | a: Helvetica Neue 24px/27.2px 500, #ffffff |
| Transition | none |
| Painted layers | ul.nav-menu 390.0x768.0 bg #161412; a.primary-link-button.glow 342.0x54.0 bg #ff4700 r 9999px shadow #ff4700 @ 0.2 0px 0px 100px 0px |
| How | at rest |

Crops: `m-menu-open-default.png`.

#### m-nav-item

Mobile menu row. A 24px row inside the opened nav overlay.

Page: home. Selector: `mobile menu row`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 83.16 x 59.2 | = | = | = |
| Padding | 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Helvetica Neue 24px/27.2px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a 83.2x59.2 outline 1px auto #005fcc offset 1px | = |

Crops: `m-nav-item-default.png`, `m-nav-item-hover.png`, `m-nav-item-focus-visible.png`, `m-nav-item-pressed.png`.

#### m-signup-btn

Mobile sign up. The full-width Sign up pill inside the menu.

Page: home. Selector: `.nav-menu .primary-link-button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 342 x 54 | = | = | = |
| Padding | 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #ff4700 | = | = | = |
| Box shadow | #ff4700 @ 0.2 0px 0px 100px 0px | #ff4700 @ 0.4 0px 0px 25px 0px | = | #ff4700 @ 0.4 0px 0px 25px 0px |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Helvetica Neue 24px/22px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | opacity, box-shadow 0.175s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.primary-link-button.glow 342.0x54.0 bg #ff4700 r 9999px shadow #ff4700 @ 0.2 0px 0px 100px 0px | a.primary-link-button.glow 342.0x54.0 bg #ff4700 r 9999px shadow #ff4700 @ 0.4 0px 0px 25px 0px | a.primary-link-button.glow 342.0x54.0 bg #ff4700 r 9999px shadow #ff4700 @ 0.2 0px 0px 100px 0px outline 1px auto #005fcc offset 1px | a.primary-link-button.glow 342.0x54.0 bg #ff4700 r 9999px shadow #ff4700 @ 0.4 0px 0px 25px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-signup-btn-default.png`, `m-signup-btn-hover.png`, `m-signup-btn-focus-visible.png`, `m-signup-btn-pressed.png`.

#### m-heading

Mobile heading.

Page: home. Selector: `painted heading at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 358 x 144 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Helvetica Neue 80px/72px 700 |
| Letter spacing | -2px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `m-heading-default.png`.

## Transitions declared in the readable stylesheets

The readable CSSOM lists only the rules each page exposes; the per-state Transition rows above are the computed values the page paints.

- blog: none

- changelog: none

- home: `box-shadow 0.175s`

- post: none
