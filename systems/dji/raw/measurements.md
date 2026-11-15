# DJI component measurements

Computed styles read from dji.com's geo-locale /sg site on 2026-11-15 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the site's painted surfaces — the home hero (/sg), the category pages (/camera-drones, /handheld), a product page (/mavic-4-pro), /support, /company and /where-to-buy/online-stores — and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Site chrome

#### nv-bar

Site header. The top nav — DJI mark, product menus, ecosystem links, Login/Register, Store (the home page paints the legacy dui-navbar; category and product pages paint the newer siteHeader module).

Page: home. Selector: `siteHeader/dui-navbar`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 64 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Open Sans 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | a.nav-item-title.ga-data: Open Sans 14px/14px 400, #ffffff, ls -0.28px |
| Transition | none |
| Painted layers | span.navbar-brand-logo 45.0x26.0 image url(data:…); div.dui-dropdown-menu 1230.0x0.0 bg #ffffff shadow #000000 @ 0.1 0px 16px 16px 0px; div.dui-dropdown-menu 1230.0x0.0 bg #ffffff shadow #000000 @ 0.1 0px 16px 16px 0px; div.dui-dropdown-menu 1230.0x0.0 bg #ffffff shadow #000000 @ 0.1 0px 16px 16px 0px; ul 132.4x96.0 bg #ffffff r 4px shadow #000000 @ 0.1 0px 8px 16px 0px; div.dui-dropdown-menu 1230.0x0.0 bg #ffffff shadow #000000 @ 0.1 0px 16px 16px 0px |
| How | at rest |

Crops: `nv-bar-default.png`.

#### nv-mark

DJI mark. The DJI logo link in the header; measured, never followed.

Page: home. Selector: `logo link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 93 x 64 | = | = | = |
| Padding | 19px 48px 19px 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Open Sans 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | span.navbar-brand-logo 45.0x26.0 image url(data:…) | = | a.navbar-brand.ga-data 93.0x64.0 outline 1px auto #101010 offset 1px; span.navbar-brand-logo 45.0x26.0 image url(data:…) | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nv-mark-default.png`, `nv-mark-hover.png`, `nv-mark-focus-visible.png`, `nv-mark-pressed.png`.

#### nv-item

Nav menu item. A product menu link (Camera Drones) that opens the mega-menu; hover measured, menu opened via toggle below.

Page: home. Selector: `nav product link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 100.38 x 64 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Open Sans 14px/14px 400 | = | = | = |
| Letter spacing | -0.28px | = | = | = |
| Colour | #ffffff | #ffffff @ 0.65 | = | #ffffff @ 0.65 |
| Transition | all 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 100.375px x 2px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.nav-item-title.ga-data 100.4x64.0 outline 1px auto #101010 offset 1px | = |

Crops: `nv-item-default.png`, `nv-item-hover.png`, `nv-item-focus-visible.png`, `nv-item-pressed.png`.

#### nv-store

Store button. The "Store" nav button linking to store.dji.com; measured, never followed — the store gates on a DJI account.

Page: home. Selector: `store-btn`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 83.61 x 32 | = | = | = |
| Padding | 8px 16px 8px 34px | = | = | = |
| Border | none | = | = | = |
| Radius | 1408px | = | = | = |
| Background | #0070d5 | #2490e3 | = | #0058b0 |
| Background image | url(data:…) | = | = | = |
| Box shadow | none | = | #1890ff 0px 0px 0px 3px | = |
| Outline | none | = | 2px dotted #ff0000 offset 1px | = |
| Font | Open Sans 14px/14px 400 | = | = | = |
| Letter spacing | -0.28px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.normal-btn.dui-btn 83.6x32.0 bg #0070d5 image url(data:…) r 1408px | a.normal-btn.dui-btn 83.6x32.0 bg #2490e3 image url(data:…) r 1408px | a.normal-btn.dui-btn 83.6x32.0 bg #0070d5 image url(data:…) r 1408px shadow #1890ff 0px 0px 0px 3px outline 2px dotted #ff0000 offset 1px | a.normal-btn.dui-btn 83.6x32.0 bg #0058b0 image url(data:…) r 1408px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nv-store-default.png`, `nv-store-hover.png`, `nv-store-focus-visible.png`, `nv-store-pressed.png`.

#### nv-login

Login link. The Login link in the header; measured, never followed — it redirects to the DJI account.

Page: home. Selector: `login link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 110 x 44 | = | = | = |
| Padding | 16px 32px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Open Sans 12px/12px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #303233 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Ancestor paint | 1 up li.nav-item bg #ffffff; 2 up ul bg #ffffff shadow #000000 @ 0.2 0px 2px 8px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.login-link.ga-data 110.0x44.0 outline 1px auto #101010 offset 1px | = |

Crops: `nv-login-default.png`, `nv-login-hover.png`, `nv-login-focus-visible.png`, `nv-login-pressed.png`.

#### ft-bar

Site footer. The DJI sitemap footer — product/support/company columns and locale links.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 833 |
| Padding | 32px 0px |
| Border | none |
| Radius | 0px |
| Background | #272727 |
| Box shadow | none |
| Outline | none |
| Font | Open Sans 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | div.one-sentence-title: Open Sans 18px/24px 600, #ffffff, ls -0.54px |
| Transition | none |
| Painted layers | footer.site-footer.dji-edit-module 1440.0x833.0 bg #272727; div.store-point-wrapper.is-pc 1200.0x149.0 border B:1px solid #ffffff @ 0.12; a.ga-data.learn-more-link 139.2x40.0 bg #ffffff @ 0.08 r 99px; div.mask 1440.0x900.0 bg #000000 @ 0.5; button.close-btn.close-btn-new-dark 36.0x36.0 bg #000000 @ 0.04 r 50%; button.btn.ok-btn 237.6x36.0 bg #000000 @ 0.85 r 999px |
| How | at rest |

Crops: `ft-bar-default.png`.

#### ft-link

Footer link. A footer column link; hover measured, never followed.

Page: home. Selector: `footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 161 x 17 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Open Sans 12px/16px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff @ 0.85 | = | = | #ffffff |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.ga-data 161.0x17.0 outline 1px auto #101010 offset 1px | = |

Crops: `ft-link-default.png`, `ft-link-hover.png`, `ft-link-focus-visible.png`, `ft-link-pressed.png`.

### Home hero

#### hm-slide

Hero panel. A home hero panel — product art over a dark or light backdrop with the CTA row.

Page: home. Selector: `hero panel`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 800 |
| Padding | 112px 0px 0px 0px |
| Border | none |
| Radius | 0px |
| Background | #ededed |
| Background image | image-set(url(…) 1dppx, url(…) 2dppx) |
| Box shadow | none |
| Outline | none |
| Font | Open Sans 16px/normal 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | div.eyebrow-text.eyebrow: Open Sans 16px/20px 400, #ffffff @ 0.65 |
| Transition | none |
| Painted layers | div.banner-content.theme-light 1440.0x800.0 bg #ededed image image-set(url(…) 1dppx, url(…) 2dppx); a.banner-button.ga-data 133.0x32.0 border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 64px; a.banner-button.ga-data 115.0x32.0 border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 64px |
| How | at rest |

Crops: `hm-slide-default.png`.

#### hm-learn

Learn More CTA. The hero "Learn More" link to the product page; measured, never followed.

Page: home. Selector: `Learn More`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 133 x 32 | = | = | = |
| Padding | 5px 16px | = | = | = |
| Border | 1px solid #ffffff | = | = | = |
| Radius | 64px | = | = | = |
| Background | transparent | = | = | #ffffff @ 0.09 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0.984375px | = |
| Font | Open Sans 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | div.text: Open Sans 14px/20px 400, #ffffff | = | = | = |
| Transition | all 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.banner-button.ga-data 133.0x32.0 border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 64px | = | a.banner-button.ga-data 133.0x32.0 border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 64px outline 1px auto #101010 offset 0.984375px | a.banner-button.ga-data 133.0x32.0 bg #ffffff @ 0.09 border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 64px |
| How | at rest | mouse hover | keydown then focus() | CDP forcePseudoState :active:hover |

Crops: `hm-learn-default.png`, `hm-learn-hover.png`, `hm-learn-focus-visible.png`, `hm-learn-pressed.png`.

#### hm-buy

Buy Now CTA. The hero "Buy Now" CTA linking to the store; measured, never followed — checkout gates on a DJI account.

Page: home. Selector: `Buy Now`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 115 x 32 | = | = | = |
| Padding | 5px 16px | = | = | = |
| Border | 1px solid #ffffff | = | = | = |
| Radius | 64px | = | = | = |
| Background | transparent | = | = | #ffffff @ 0.09 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Open Sans 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | div.text: Open Sans 14px/20px 400, #ffffff | = | = | = |
| Transition | all 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.banner-button.ga-data 115.0x32.0 border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 64px | = | a.banner-button.ga-data 115.0x32.0 border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 64px outline 1px auto #101010 offset 1px | a.banner-button.ga-data 115.0x32.0 bg #ffffff @ 0.09 border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 64px |
| How | at rest | mouse hover | keydown then focus() | CDP forcePseudoState :active:hover |

Crops: `hm-buy-default.png`, `hm-buy-focus-visible.png`, `hm-buy-pressed.png`.

### Category page

#### ct-h1

Category heading. The "Camera Drones" listing heading.

Page: drones. Selector: `category h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 693 x 52 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Open Sans 48px/52px 600 |
| Letter spacing | -1.44px |
| Colour | #000000 @ 0.85 |
| Transition | all 0.6s ease-in-out |
| How | at rest |

Crops: `ct-h1-default.png`.

#### ct-subnav

Sub-nav Store button. The "Store"/"Buy Now" button pinned in the page sub-nav; measured, never followed.

Page: drones. Selector: `sub-nav/store-btn`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 83.61 x 32 | = | = | = |
| Padding | 8px 16px 8px 34px | = | = | = |
| Border | none | = | = | = |
| Radius | 1408px | = | = | = |
| Background | #0070d5 | #2490e3 | = | #0058b0 |
| Background image | url(data:…) | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Open Sans 14px/14px 400 | = | = | = |
| Letter spacing | -0.28px | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span: Open Sans 14px/14px 400, #ffffff, ls -0.28px | = | = | = |
| Transition | background-color 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.style__store-btn___2BG_Z 83.6x32.0 bg #0070d5 image url(data:…) r 1408px | a.style__store-btn___2BG_Z 83.6x32.0 bg #2490e3 image url(data:…) r 1408px | a.style__store-btn___2BG_Z 83.6x32.0 bg #0070d5 image url(data:…) r 1408px outline 1px auto #101010 offset 1px | a.style__store-btn___2BG_Z 83.6x32.0 bg #0058b0 image url(data:…) r 1408px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `ct-subnav-default.png`, `ct-subnav-hover.png`, `ct-subnav-focus-visible.png`, `ct-subnav-pressed.png`.

#### hh-h1

Handheld heading. The handheld category heading (Osmo action cameras, gimbals, mics).

Page: handheld. Selector: `handheld h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 693 x 48 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Open Sans 40px/48px 600 |
| Letter spacing | -1.2px |
| Colour | #000000 @ 0.85 |
| Transition | all 0.6s ease-in-out |
| How | at rest |

Crops: `hh-h1-default.png`.

### Product cards

#### ct-card

Product card. A 2-up atom-design hero-vertical-card on the category grid — product art, tagline and name (the page's H1 banner and full-width series intro share the class, so the filter anchors on a DJI product name); hover measured, never followed.

Page: drones. Selector: `hero-vertical-card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 696 x 600 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | #f5f5f5 | = |
| Background image | url(…) | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Open Sans 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #3b3e40 | = |
| Text node | h2.text-ms-12.style__eyebrow-text___1gRhT: Open Sans 12px/16px 400, #be4e04, ls -0.36px | = |
| Transition | none | = |
| Painted layers | div.atom-design-v1.style__hero-vertical-card___2B64y 696.0x600.0 bg #f5f5f5; button.atom-design-v1.style__dji-btn___ILmHs 128.0x40.0 bg #0070d5 r 60px; button.atom-design-v1.style__dji-btn___ILmHs 128.0x40.0 border T:1px solid #000000 @ 0.85 / R:1px solid #000000 @ 0.85 / B:1px solid #000000 @ 0.85 / L:1px solid #000000 @ 0.85 r 60px | = |
| How | at rest | mouse hover |

Crops: `ct-card-default.png`, `ct-card-hover.png`.

#### hh-card

Handheld card. A 2-up handheld product card (atom hero-vertical-card; the full-width Osmo Pocket hero shares the class, so the filter anchors on a grid product name); hover measured, never followed.

Page: handheld. Selector: `hero-vertical-card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 696 x 600 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | #f5f5f5 | = |
| Background image | url(…) | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Open Sans 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #3b3e40 | = |
| Text node | h2.text-ms-12.style__eyebrow-text___1gRhT: Open Sans 12px/16px 400, #be4e04, ls -0.36px | = |
| Transition | none | = |
| Painted layers | div.atom-design-v1.style__hero-vertical-card___2B64y 696.0x600.0 bg #f5f5f5; button.atom-design-v1.style__dji-btn___ILmHs 128.0x40.0 bg #0070d5 r 60px; button.atom-design-v1.style__dji-btn___ILmHs 128.0x40.0 border T:1px solid #000000 @ 0.85 / R:1px solid #000000 @ 0.85 / B:1px solid #000000 @ 0.85 / L:1px solid #000000 @ 0.85 r 60px | = |
| How | at rest | mouse hover |

Crops: `hh-card-default.png`, `hh-card-hover.png`.

### Product page

#### pd-subnav

Product sub-nav. The product page sticky sub-nav — section links and the Buy Now button.

Page: product. Selector: `sub-nav bar`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 64 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Open Sans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #3b3e40 |
| Text node | a: Open Sans 14px/64px 400, #ffffff |
| Transition | none |
| Painted layers | nav.style__sub-nav___AjIC_ 1440.0x64.0 bg #232526 @ 0.9; a.style__sub-nav-btn___fguHS 91.0x30.0 bg #0070d5 r 2px; div.popover__flex-box___14szQ 320.0x88.0 bg #ffffff r 4px; div.popover__cover-image___1yWkS 40.0x40.0 bg #f5f5f5 r 99px; div.popover__close___1jBk4 32.0x32.0 image url(data:…) r 99px; div.popover__arrow___29rRa 22.0x12.0 border R:11px solid #000000 @ 0 / B:12px solid #ffffff / L:11px solid #000000 @ 0 |
| How | at rest |

Crops: `pd-subnav-default.png`.

#### pd-buy

Atom Buy button. The atom-design-v1 primary "Buy Now" button (dji-btn-lg); states measured, never pressed — purchase gates on the store account.

Page: product. Selector: `atom dji-btn`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 144 x 40 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 60px | = | = | = |
| Background | #ffffff | #ffffff @ 0.9 | #ffffff @ 0.9 | #ffffff @ 0.8 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Open Sans 16px/20px 400 | = | = | = |
| Letter spacing | -0.32px | = | = | = |
| Colour | #000000 @ 0.85 | = | = | = |
| Text node | div.style__button-inner___3_kJl: Open Sans 16px/20px 400, #000000 @ 0.85, ls -0.32px | = | = | = |
| Transition | all 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.atom-design-v1.style__dji-btn___ILmHs 144.0x40.0 bg #ffffff r 60px | button.atom-design-v1.style__dji-btn___ILmHs 144.0x40.0 bg #ffffff @ 0.9 r 60px | button.atom-design-v1.style__dji-btn___ILmHs 144.0x40.0 bg #ffffff @ 0.9 r 60px | button.atom-design-v1.style__dji-btn___ILmHs 144.0x40.0 bg #ffffff @ 0.8 r 60px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `pd-buy-default.png`, `pd-buy-hover.png`, `pd-buy-focus-visible.png`, `pd-buy-pressed.png`.

#### pd-watch

Atom ghost button. The secondary "Watch Video" atom button; states measured, never pressed.

Page: product. Selector: `atom dji-btn ghost`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 147.48 x 40 | = | = | = |
| Padding | 0px 15px | = | = | = |
| Border | 1px solid #ffffff | = | = | = |
| Radius | 60px | = | = | = |
| Background | transparent | #ffffff @ 0.09 | #ffffff @ 0.09 | #ffffff @ 0.15 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Open Sans 16px/20px 400 | = | = | = |
| Letter spacing | -0.32px | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span: Open Sans 16px/20px 400, #ffffff, ls -0.32px | = | = | = |
| Transition | all 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.atom-design-v1.style__dji-btn___ILmHs 147.5x40.0 border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 60px | button.atom-design-v1.style__dji-btn___ILmHs 147.5x40.0 bg #ffffff @ 0.09 border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 60px | button.atom-design-v1.style__dji-btn___ILmHs 147.5x40.0 bg #ffffff @ 0.09 border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 60px | button.atom-design-v1.style__dji-btn___ILmHs 147.5x40.0 bg #ffffff @ 0.15 border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 60px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `pd-watch-default.png`, `pd-watch-hover.png`, `pd-watch-focus-visible.png`, `pd-watch-pressed.png`.

#### pd-eyebrow

Eyebrow heading. A section eyebrow line (e.g. "Triple-Camera Imaging System") using the text-ms-24 size utility.

Page: product. Selector: `eyebrow text-ms-24`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 693 x 52 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Open Sans 20px/52px 600 |
| Letter spacing | -0.6px |
| Colour | #ffffff @ 0.85 |
| Transition | all 0.6s ease-in-out |
| Cursor | pointer |
| How | at rest |

Crops: `pd-eyebrow-default.png`.

#### pd-h

Product heading. A product page display heading.

Page: product. Selector: `product h1/h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 693 x 32 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Open Sans 24px/32px 600 |
| Letter spacing | -0.72px |
| Colour | #ffffff |
| Transition | all 0.6s ease-in-out |
| How | at rest |

Crops: `pd-h-default.png`.

#### pd-spec

Spec line. A spec value line on the product page.

Page: product. Selector: `spec text`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 895.02 x 55 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Background image | linear-gradient(90deg, #f68128 0%, #ffae66 52%, #f68128 100%) |
| Box shadow | none |
| Outline | none |
| Font | Open Sans 20px/28px 600 |
| Letter spacing | -0.6px |
| Colour | #000000 @ 0 |
| Transition | none |
| Painted layers | span 895.0x55.0 image linear-gradient(90deg, #f68128 0%, #ffae66 52%, #f68128 100%) |
| How | at rest |

Crops: `pd-spec-default.png`.

### Support / company

#### sp-h1

Support heading. The support portal heading.

Page: support. Selector: `support h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1200 x 56 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Open Sans 48px/56px 500 |
| Letter spacing | -1.44px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `sp-h1-default.png`.

#### sp-card

Support tile. A support category tile (repairs, service, downloads); hover measured, never followed.

Page: support. Selector: `support tile a`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 325.33 x 120 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Open Sans 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #3b3e40 | = |
| Text node | h3.style__headline___1ripS.style__headline-text___1tW5r: Open Sans 20px/24px 600, #000000 @ 0.85, ls -0.6px | = |
| Transition | none | = |
| How | at rest | mouse hover |

Crops: `sp-card-default.png`, `sp-card-hover.png`.

#### sp-search

Support search. The support search field; focus/fill measured, never submitted.

Page: support. Selector: `support search`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 640 x 32 | = | = |
| Padding | 4px 8px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | #ffffff | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Open Sans 16px/normal 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #303233 | = | = |
| Transition | none | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = |
| Cursor | text | = | = |
| Placeholder | #757575, opacity 1 | = | = |
| Painted layers | input.style__search-input___NgQFL 640.0x32.0 bg #ffffff | = | = |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `sp-search-default.png`, `sp-search-focused.png`, `sp-search-filled.png`.

#### co-h1

About DJI nav heading. The "About DJI" section heading in the company sidebar nav — the page paints its hero as image, so this named link is its display text.

Page: company. Selector: `about nav item`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 61 x 19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Open Sans 14px/20px 400 |
| Letter spacing | normal |
| Colour | #707473 |
| Transition | none |
| How | at rest |

Crops: `co-h1-default.png`.

#### co-lede

Company lede. The first body paragraph on the company page.

Page: company. Selector: `company p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 395 x 48 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Open Sans 16px/24px 400 |
| Letter spacing | -0.32px |
| Colour | #000000 @ 0.65 |
| Transition | none |
| Ancestor paint | 1 up div.modal-box bg #ffffff |
| How | at rest |

Crops: `co-lede-default.png`.

#### st-h1

Where to Buy heading. The where-to-buy page heading.

Page: stores. Selector: `stores h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1200 x 76.19 |
| Padding | 24px 0px 16px 0px |
| Border | T: none; R: none; B: 1px solid #f0f1f2; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Open Sans 32px/35.2px 600 |
| Letter spacing | normal |
| Colour | #3b3e40 |
| Transition | none |
| Painted layers | h1.bread-title 1200.0x76.2 border B:1px solid #f0f1f2 |
| How | at rest |

Crops: `st-h1-default.png`.

#### st-link

Store-type link. A store-type link (Flagship Stores); measured, never followed.

Page: stores. Selector: `ga-data link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 126 x 40 | = | = | = |
| Padding | 8px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Open Sans 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 @ 0.65 | #000000 @ 0.85 | #000000 @ 0.85 | #000000 @ 0.85 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `st-link-default.png`, `st-link-hover.png`, `st-link-focus-visible.png`, `st-link-pressed.png`.

### Mobile (390 wide)

#### m-bar

Mobile header. The phone header at 390px — mark and menu affordance.

Page: mobile. Selector: `mobile header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 50 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Open Sans 16px/normal 400 |
| Letter spacing | -0.32px |
| Colour | #000000 |
| Text node | a.ga-data.title: Open Sans 14px/20px 400, #000000 @ 0.85, ls -0.28px |
| Transition | none |
| Painted layers | span::before.control-icon 22pxx2px bg #ffffff r 0px 2px; span::before.control-icon 22pxx2px bg #ffffff r 0px 2px; span::before.control-icon 22pxx2px bg #ffffff r 0px 2px; i.search-trigger 28.0x28.0 image url(data:…); a.navbar-shopingbag.ga-data 32.0x32.0 image url(data:…) r 1408px; a.navbar-shopingbag.active 0.0x0.0 image url(data:…) r 1408px |
| How | at rest |

Crops: `m-bar-default.png`.

#### m-cta

Mobile CTA. A hero CTA at 390px; measured, never followed.

Page: mobile. Selector: `mobile CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 133 x 32 | = | = | = |
| Padding | 5px 16px | = | = | = |
| Border | 1px solid #ffffff | = | = | = |
| Radius | 60px | = | = | = |
| Background | transparent | = | = | #ffffff @ 0.15 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #e59700 offset 1px | = |
| Font | Open Sans 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | span.text: Open Sans 14px/20px 400, #ffffff | = | = | = |
| Transition | all 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.banner-button.ga-data 133.0x32.0 border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 60px | = | a.banner-button.ga-data 133.0x32.0 border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 60px outline 1px auto #e59700 offset 1px | a.banner-button.ga-data 133.0x32.0 bg #ffffff @ 0.15 border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 60px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-cta-default.png`, `m-cta-hover.png`, `m-cta-focus-visible.png`, `m-cta-pressed.png`.

#### m-tab

Mobile nav tab. A category tab in the mobile nav row (the phone UA is redirected to the separate /sg/mobile site); measured, never followed.

Page: mobile. Selector: `mobile nav tab`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 354 x 20 | = | = | = |
| Padding | 0px 32px 0px 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #e59700 offset 1px | = |
| Font | Open Sans 14px/20px 400 | = | = | = |
| Letter spacing | -0.28px | = | = | = |
| Colour | #000000 @ 0.85 | = | = | = |
| Transition | all 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.ga-data.title 354.0x20.0 outline 1px auto #e59700 offset 1px | = |

Crops: `m-tab-hover.png`, `m-tab-focus-visible.png`, `m-tab-pressed.png`.

#### m-menu

Mobile menu button. The hamburger control in the /sg/mobile navbar; measured, never toggled open.

Page: mobile. Selector: `a.navbar-control`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 54 x 50 | = | = | = |
| Padding | 13px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #e59700 offset 1px | = |
| Font | Open Sans 16px/normal 400 | = | = | = |
| Letter spacing | -0.32px | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | span::before.control-icon 22pxx2px bg #ffffff r 0px 2px; span::before.control-icon 22pxx2px bg #ffffff r 0px 2px; span::before.control-icon 22pxx2px bg #ffffff r 0px 2px | = | a.navbar-control 54.0x50.0 outline 1px auto #e59700 offset 1px; span::before.control-icon 22pxx2px bg #ffffff r 0px 2px; span::before.control-icon 22pxx2px bg #ffffff r 0px 2px; span::before.control-icon 22pxx2px bg #ffffff r 0px 2px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-menu-default.png`, `m-menu-hover.png`, `m-menu-focus-visible.png`, `m-menu-pressed.png`.

## Transitions declared in the readable stylesheets

dji.com serves its CSS bundles cross-origin from www-cdn.djiits.com; the readable sheets are whichever ones the page exposes (inline <style> plus CORS-readable links), so this list holds the transitions those sheets declare on each page; the per-state Transition rows above are computed values and cover every rule the page paints.

- company: `background-color 0.3s`, `opacity, transform 0.3s`, `0.6s`, `none`, `height 0.2s linear`, `width 0.3s linear`, `background-color 0.218s, border-color 0.218s`, `background-color 0.218s`, `top 0.5s`, `0.1s`, `opacity 1s ease-in-out`, `0.5s`

- drones: `background-color 0.3s`, `opacity, transform 0.3s`, `0.6s`, `none`, `top 0.5s`, `0.1s`, `opacity 1s ease-in-out`, `0.5s`, `height 0.2s linear`, `width 0.3s linear`, `background-color 0.218s, border-color 0.218s`, `background-color 0.218s`

- handheld: `none`, `background-color 0.3s`, `opacity, transform 0.3s`, `0.6s`, `height 0.2s linear`, `width 0.3s linear`, `background-color 0.218s, border-color 0.218s`, `background-color 0.218s`, `top 0.5s`, `0.1s`, `opacity 1s ease-in-out`, `0.5s`

- home: `background-color 0.3s`, `opacity, transform 0.3s`, `0.6s`, `none`, `height 0.2s linear`, `width 0.3s linear`, `background-color 0.218s, border-color 0.218s`, `background-color 0.218s`, `top 0.5s`, `0.1s`, `opacity 1s ease-in-out`, `0.5s`

- product: `background-color 0.3s`, `opacity, transform 0.3s`, `0.6s`, `none`, `height 0.2s linear`, `width 0.3s linear`, `background-color 0.218s, border-color 0.218s`, `background-color 0.218s`, `top 0.5s`, `0.1s`, `opacity 1s ease-in-out`, `0.5s`

- stores: `background-color 0.3s`, `opacity, transform 0.3s`, `0.6s`, `none`, `height 0.2s linear`, `width 0.3s linear`, `background-color 0.218s, border-color 0.218s`, `background-color 0.218s`, `top 0.5s`, `0.1s`, `opacity 1s ease-in-out`, `0.5s`

- support: `none`, `height 0.2s linear`, `width 0.3s linear`, `background-color 0.218s, border-color 0.218s`, `background-color 0.218s`, `top 0.5s`, `0.1s`, `opacity 1s ease-in-out`, `0.5s`, `color 0.3s`, `opacity 0.3s`, `transform 0.3s cubic-bezier(0.23, 1, 0.32, 1), opacity 0.3s`
