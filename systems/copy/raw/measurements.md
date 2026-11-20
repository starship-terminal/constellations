# Component measurements

Computed styles read from copy.ai on 2026-11-12 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the home page, /prices, /contact-us and the public login.copy.ai auth card — with the HubSpot cookie banner and chat widget hidden (never answered) — and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### top-banner

Top banner. The dark promo strip above the nav ("The 2026 Benchmarks Report is Finally Here!" with its arrow action); static, scrolls with the page.

Page: home. Selector: `.top-banner_component`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 48 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #171717 |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/20px 400 |
| Letter spacing | normal |
| Colour | #171717 |
| Text node | div.text--w-medium.text-shadow-small: Inter 16px/24px 500, #ffffff |
| Transition | none |
| Icon | 16 x 11, colour #fbfbfc, fill #000000 |
| Painted layers | div.top-banner_component 1440.0x48.0 bg #171717; div.top-banner_content 1440.0x48.0 bg #171717; div.link--arrow-wr.is-clear 32.0x32.0 bg #ffffff @ 0.2 border T:1px solid #e0e0e0 / R:1px solid #e0e0e0 / B:1px solid #e0e0e0 / L:1px solid #e0e0e0 r 8px |
| How | at rest |

Crops: `top-banner-default.png`.

#### header

Header. The sticky nav.mega--nav (z 1000): wordmark, the Platform/Use cases/Resources/Pricing/GTM AI triggers, Login and the Get a Demo action.

Page: home. Selector: `nav.mega--nav`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 88 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/20px 400 |
| Letter spacing | normal |
| Colour | #171717 |
| Text node | div: Inter 16px/24px 500, #222222 |
| Transition | none |
| Icon | 20 x 20, colour #222222 |
| Painted layers | nav.mega--nav 1440.0x88.0 bg #ffffff; nav.mega--nav_dd_list.w-dropdown-list 0.0x0.0 bg #ffffff; div.dd_group_heading-wr 0.0x0.0 border B:1px solid #e0e0e0; div.dd-link_icon-wr 0.0x0.0 bg #fbfbfc border T:1px solid #e0e0e0 / R:1px solid #e0e0e0 / B:1px solid #e0e0e0 / L:1px solid #e0e0e0 r 8px; div.dd-link_icon-wr 0.0x0.0 bg #fbfbfc border T:1px solid #e0e0e0 / R:1px solid #e0e0e0 / B:1px solid #e0e0e0 / L:1px solid #e0e0e0 r 8px; div.dd-link_icon-wr 0.0x0.0 bg #fbfbfc border T:1px solid #e0e0e0 / R:1px solid #e0e0e0 / B:1px solid #e0e0e0 / L:1px solid #e0e0e0 r 8px |
| How | at rest |

Crops: `header-default.png`.

#### logo

Logo. The copy.ai wordmark anchor.

Page: home. Selector: `a.navbar_brand`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 100 x 30 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/20px 400 |
| Letter spacing | normal |
| Colour | #333333 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `logo-default.png`.

#### nav-dd-toggle

Nav dropdown trigger. The Platform trigger that opens the mega-menu; toggled for the menu screenshot, never followed.

Page: home. Selector: `.mega--nav_dd_toggle`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 132.31 x 88 | = | = | = |
| Padding | 8px 24px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | #171717 0px -1px 0px 0px inset | = | #171717 0px -1px 0px 0px inset |
| Outline | none | = | 2px solid #4d65ff offset 2px | = |
| Font | Inter 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #222222 | = | = | = |
| Text node | div: Inter 16px/24px 500, #222222 | = | = | = |
| Transition | box-shadow 0.4s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #222222 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | div.mega--nav_dd_toggle.w-dropdown-toggle 132.3x88.0 shadow #171717 0px -1px 0px 0px inset | div.mega--nav_dd_toggle.w-dropdown-toggle 132.3x88.0 outline 2px solid #4d65ff offset 2px | div.mega--nav_dd_toggle.w-dropdown-toggle 132.3x88.0 shadow #171717 0px -1px 0px 0px inset |

Crops: `nav-dd-toggle-default.png`, `nav-dd-toggle-hover.png`, `nav-dd-toggle-focus-visible.png`, `nav-dd-toggle-pressed.png`.

#### btn-nav

Nav CTA. The purple "Get a Demo" button in the header; measured, never followed.

Page: home. Selector: `a.btn_nav`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 121.78 x 47 | = | = | = |
| Padding | 12px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | #693edf | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #171717 | = | = | = |
| Text node | div.btn--primary_text.text-color-white: Inter 16px/24px 700, #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.btn_nav.w-inline-block 121.8x47.0 bg #693edf r 4px | = | a.btn_nav.w-inline-block 121.8x47.0 bg #693edf r 4px outline 1px auto #005fcc offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `btn-nav-default.png`, `btn-nav-hover.png`, `btn-nav-focus-visible.png`, `btn-nav-pressed.png`.

#### login-link

Login link. The header Login action (app.copy.ai); measured, never followed.

Page: home. Selector: `a.mega--nav_login-link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 42.28 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #171717 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.mega--nav_login-link 42.3x24.0 outline 1px auto #005fcc offset 1px | = |

Crops: `login-link-default.png`, `login-link-hover.png`, `login-link-focus-visible.png`, `login-link-pressed.png`.

#### nav-dd-panel

Mega-menu panel. The opened Platform mega-menu (OVERVIEW / WORKFLOWS / INTELLIGENCE LAYER / TECHNICAL RESOURCES columns).

Page: home. Selector: `opened Platform dropdown`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 389 |
| Padding | 40px |
| Border | T: 1px solid #e0e0e0; R: none; B: none; L: none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | #000000 @ 0.03 0px 40px 34px 0px |
| Outline | none |
| Font | Inter 14px/20px 400 |
| Letter spacing | normal |
| Colour | #171717 |
| Text node | div: Inter 12px/24px 500, #171717 |
| Transition | none |
| Icon | 16 x 16, colour #171717 |
| Painted layers | nav.mega--nav_dd_list.w-dropdown-list 1440.0x389.0 bg #ffffff border T:1px solid #e0e0e0 shadow #000000 @ 0.03 0px 40px 34px 0px; div.dd_group_heading-wr 277.3x41.0 border B:1px solid #e0e0e0; div.dd-link_icon-wr 32.0x32.0 bg #fbfbfc border T:1px solid #e0e0e0 / R:1px solid #e0e0e0 / B:1px solid #e0e0e0 / L:1px solid #e0e0e0 r 8px; div.dd-link_icon-wr 32.0x32.0 bg #fbfbfc border T:1px solid #e0e0e0 / R:1px solid #e0e0e0 / B:1px solid #e0e0e0 / L:1px solid #e0e0e0 r 8px; div.dd-link_icon-wr 32.0x32.0 bg #fbfbfc border T:1px solid #e0e0e0 / R:1px solid #e0e0e0 / B:1px solid #e0e0e0 / L:1px solid #e0e0e0 r 8px; div.dd_group_heading-wr 277.3x41.0 border B:1px solid #e0e0e0 |
| How | at rest |

Crops: `nav-dd-panel-default.png`.

#### dd-link

Dropdown link. A link inside the opened Platform mega-menu (How it Works et al.); measured, never followed.

Page: home. Selector: `mega-menu a.dd-link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 277.33 x 32 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #4d65ff offset 2px | 2px solid #4d65ff offset 2px |
| Font | Inter 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #171717 | = | = | = |
| Text node | div: Inter 16px/24px 500, #171717 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #171717 | 16 x 16, colour #ffffff | 16 x 16, colour #ffffff | 16 x 16, colour #ffffff |
| Painted layers | div.dd-link_icon-wr 32.0x32.0 bg #fbfbfc border T:1px solid #e0e0e0 / R:1px solid #e0e0e0 / B:1px solid #e0e0e0 / L:1px solid #e0e0e0 r 8px | div.dd-link_icon-wr 32.0x32.0 bg #693ee0 border T:1px solid #3b0d96 / R:1px solid #3b0d96 / B:1px solid #3b0d96 / L:1px solid #3b0d96 r 8px | a.dd-link.w-inline-block 277.3x32.0 outline 2px solid #4d65ff offset 2px; div.dd-link_icon-wr 32.0x32.0 bg #693ee0 border T:1px solid #3b0d96 / R:1px solid #3b0d96 / B:1px solid #3b0d96 / L:1px solid #3b0d96 r 8px | a.dd-link.w-inline-block 277.3x32.0 outline 2px solid #4d65ff offset 2px; div.dd-link_icon-wr 32.0x32.0 bg #693ee0 border T:1px solid #3b0d96 / R:1px solid #3b0d96 / B:1px solid #3b0d96 / L:1px solid #3b0d96 r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `dd-link-default.png`, `dd-link-hover.png`, `dd-link-focus-visible.png`, `dd-link-pressed.png`.

### Home

#### hero-title

Hero headline. The "The First AI-Native GTM Platform" display.

Page: home. Selector: `h1.home--hero_h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 349 x 176 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ABC Normal 88px/88px 600 |
| Letter spacing | normal |
| Colour | #171717 |
| Transition | none |
| How | at rest |

Crops: `hero-title-default.png`.

#### hero-sub

Hero copy. The lede under the hero headline (Infuse AI across your go-to-market engine…).

Page: home. Selector: `p.home--hero_small-text`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 384 x 110 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/22px 400 |
| Letter spacing | normal |
| Colour | #566b76 |
| Transition | none |
| How | at rest |

Crops: `hero-sub-default.png`.

#### hero-email

Email field. The hero "What's your email?" field; focused and given sample text that was deleted again — the form was never submitted.

Page: home. Selector: `input#Email.form--input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 308 x 42 | = | = |
| Padding | 0px 8px 0px 18px | = | = |
| Border | 1px solid #e4edf1 | 1px solid #171717 | 1px solid #171717 |
| Radius | 0px | = | = |
| Background | #f6fafb | = | = |
| Box shadow | none | #000000 @ 0.07 0px 6px 20px 0px | #000000 @ 0.07 0px 6px 20px 0px |
| Outline | none | = | = |
| Font | Inter 16px/22.8571px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #171717 | = | = |
| Transition | border-color, box-shadow 0.2s, 0.2s ease, ease delay 0s, 0s | = | = |
| Cursor | text | = | = |
| Placeholder | #6c8d9d, opacity 1 | = | = |
| Painted layers | input.form--input.w-input 308.0x42.0 bg #f6fafb border T:1px solid #e4edf1 / R:1px solid #e4edf1 / B:1px solid #e4edf1 / L:1px solid #e4edf1 | input.form--input.w-input 308.0x42.0 bg #f6fafb border T:1px solid #171717 / R:1px solid #171717 / B:1px solid #171717 / L:1px solid #171717 shadow #000000 @ 0.07 0px 6px 20px 0px | input.form--input.w-input 308.0x42.0 bg #f6fafb border T:1px solid #171717 / R:1px solid #171717 / B:1px solid #171717 / L:1px solid #171717 shadow #000000 @ 0.07 0px 6px 20px 0px |
| Ancestor paint | 3 up div.hero--form-wr bg #ffffff shadow #e4edf1 @ 0.07 0px 2px 14px 0px | = | = |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `hero-email-default.png`, `hero-email-focused.png`, `hero-email-filled.png`.

#### hero-submit

Hero submit. The black "Get a demo" submit of the hero email form; measured, never pressed.

Page: home. Selector: `input.is-submit`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 128.3 x 40 | = | - | = |
| Padding | 0px 20px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | #171717 | #693ee0 | - | #693ee0 |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Inter 16px/24px 700 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #ffffff | = | - | = |
| Transition | border-color, background-color 0.3s, 0.3s ease, ease delay 0s, 0s | = | - | = |
| Cursor | default | = | - | = |
| Placeholder | #ffffff, opacity 1 | = | - | = |
| Painted layers | input.button.is-submit 128.3x40.0 bg #171717 | input.button.is-submit 128.3x40.0 bg #693ee0 | - | input.button.is-submit 128.3x40.0 bg #693ee0 |
| Ancestor paint | 3 up div.hero--form-wr bg #ffffff shadow #e4edf1 @ 0.07 0px 2px 14px 0px | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `hero-submit-default.png`, `hero-submit-hover.png`, `hero-submit-pressed.png`.

#### playbook-card

Playbook card. A "Get Demo" playbook card (the purple GTM-AI-Playbook rail); measured, never followed.

Page: home. Selector: `a.btn--playbook`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 90.63 x 28 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Border | 1px solid #ccd9e0 | 1px solid #000000 | = | 1px solid #000000 |
| Radius | 4px | = | = | = |
| Background | #ffffff | #131516 | = | #131516 |
| Box shadow | #ccd9e0 @ 0.2 0px -3px 0px 0px inset | none | = | none |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #364045 | #ffffff | = | #ffffff |
| Text node | div.btn-text: Inter 12px/14px 400, #364045 | div.btn-text: Inter 12px/14px 400, #ffffff | = | div.btn-text: Inter 12px/14px 400, #ffffff |
| Transition | box-shadow, color, background-color, border-color 0.1s, 0.3s, 0.3s, 0.3s ease, ease, ease, ease delay 0s, 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.btn--playbook.w-inline-block 90.6x28.0 bg #ffffff border T:1px solid #ccd9e0 / R:1px solid #ccd9e0 / B:1px solid #ccd9e0 / L:1px solid #ccd9e0 r 4px shadow #ccd9e0 @ 0.2 0px -3px 0px 0px inset | a.btn--playbook.w-inline-block 90.6x28.0 bg #131516 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 4px | a.btn--playbook.w-inline-block 90.6x28.0 bg #ffffff border T:1px solid #ccd9e0 / R:1px solid #ccd9e0 / B:1px solid #ccd9e0 / L:1px solid #ccd9e0 r 4px shadow #ccd9e0 @ 0.2 0px -3px 0px 0px inset outline 1px auto #005fcc offset 1px | a.btn--playbook.w-inline-block 90.6x28.0 bg #131516 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Ancestor paint | - | 2 up div.playbook_card bg #ffffff shadow #ccd9e0 0px 8px 24px 0px | = | = |

Crops: `playbook-card-default.png`, `playbook-card-hover.png`, `playbook-card-focus-visible.png`, `playbook-card-pressed.png`.

#### invert-cta

Inverted CTA. A "Get a demo" action on a dark band (the inverted variant); measured, never followed.

Page: home. Selector: `a.btn--primary-invert`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 178.3 x 63 | = | = | = |
| Padding | 20px 32px | = | = | = |
| Gap | normal 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #ffffff | #693ee0 | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #171717 | = | = | = |
| Text node | div.btn--primary_text.text-color-black: Inter 16px/24px 700, #171717 | = | = | = |
| Transition | none | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.btn--primary-invert.w-inline-block 178.3x63.0 bg #ffffff r 8px | a.btn--primary-invert.w-inline-block 178.3x63.0 bg #693ee0 r 8px | a.btn--primary-invert.w-inline-block 178.3x63.0 bg #ffffff r 8px outline 1px auto #005fcc offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `invert-cta-default.png`, `invert-cta-hover.png`, `invert-cta-focus-visible.png`, `invert-cta-pressed.png`.

#### platform-card

Platform card. A platform-feature card (Agents Automate…); measured, never followed.

Page: home. Selector: `a.platfrom_right-card`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 700 x 121.97 | = | = | = |
| Padding | 24px 105px 24px 24px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | #29007a | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #171717 | = | = | = |
| Text node | h3.heading-workflows: ABC Normal 28px/42px 500, #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.platfrom_right-card.is-top 700.0x122.0 bg #29007a | = | a.platfrom_right-card.is-top 700.0x122.0 bg #29007a outline 1px auto #005fcc offset 1px | = |
| Ancestor paint | 3 up div.platform-wr shadow #6c8d9d @ 0.2 0px 12px 48px -7px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `platform-card-default.png`, `platform-card-hover.png`, `platform-card-focus-visible.png`, `platform-card-pressed.png`.

#### section-h2

Section heading. A 56px section heading (Design Your GTM AI Playbook).

Page: home. Selector: `h2.heading--h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1329 x 66 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ABC Normal 56px/66px 500 |
| Letter spacing | normal |
| Colour | #171717 |
| Transition | none |
| How | at rest |

Crops: `section-h2-default.png`.

#### blog-card

Blog card. A blog/article card in the home slider; measured, never followed.

Page: home. Selector: `a.blog-slider_card`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 360 x 462.78 | = | = | = |
| Padding | 0px 8px | = | = | = |
| Border | 1px solid #e0e0e0 | = | = | 1px solid #171717 |
| Radius | 0px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #171717 | = | = | #693ee0 |
| Text node | h3.heading--h5: ABC Normal 24px/33.6px 500, #000b0f | = | = | = |
| Transition | border-color 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.blog-slider_card.w-inline-block 360.0x462.8 bg #ffffff border T:1px solid #e0e0e0 / R:1px solid #e0e0e0 / B:1px solid #e0e0e0 / L:1px solid #e0e0e0 | = | a.blog-slider_card.w-inline-block 360.0x462.8 bg #ffffff border T:1px solid #e0e0e0 / R:1px solid #e0e0e0 / B:1px solid #e0e0e0 / L:1px solid #e0e0e0 outline 1px auto #005fcc offset 1px | a.blog-slider_card.w-inline-block 360.0x462.8 bg #ffffff border T:1px solid #171717 / R:1px solid #171717 / B:1px solid #171717 / L:1px solid #171717 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `blog-card-default.png`, `blog-card-hover.png`, `blog-card-focus-visible.png`, `blog-card-pressed.png`.

### Pricing

#### pricing-h1

Pricing title. The "Copy.ai pricing" display heading.

Page: pricing. Selector: `h1.heading--h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 427.72 x 74 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ABC Normal 64px/74px 500 |
| Letter spacing | normal |
| Colour | #171717 |
| Transition | none |
| How | at rest |

Crops: `pricing-h1-default.png`.

#### plan-toggle

Plan toggle. The Self-Serve / Enterprise segmented control; measured at rest — toggling it swaps the pricing view, so the pressed state is the CDP-forced one.

Page: pricing. Selector: `button.price_menu-toggle`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 264 x 56 | = | = | = |
| Padding | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 48px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | #000000 @ 0.06 0px 28px 64px 0px | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | Inter 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #171717 | = | = | = |
| Text node | div.price_menu-text: Inter 16px/24px 500, #171717 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.price_menu-toggle 264.0x56.0 bg #ffffff r 48px shadow #000000 @ 0.06 0px 28px 64px 0px; div.price_menu-item.is-active 128.0x48.0 bg #ffffff; div.price_circle.is-top 130.0x48.0 bg #a284ff @ 0 r 48px | = | button.price_menu-toggle 264.0x56.0 bg #ffffff r 48px shadow #000000 @ 0.06 0px 28px 64px 0px outline 1px auto #005fcc offset 0px; div.price_menu-item.is-active 128.0x48.0 bg #ffffff; div.price_circle.is-top 130.0x48.0 bg #a284ff @ 0 r 48px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `plan-toggle-default.png`, `plan-toggle-hover.png`, `plan-toggle-focus-visible.png`, `plan-toggle-pressed.png`.

#### plan-card

Plan card. The Chat plan card (name, checklist, Monthly|Annually control, the 20% SAVING badge, $29/mo and Get started).

Page: pricing. Selector: `plan card (.price_layout-new)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 360 x 594.59 |
| Padding | 24px |
| Gap | 24px |
| Border | 1px solid #e0e0e0 |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/20px 400 |
| Letter spacing | normal |
| Colour | #171717 |
| Text node | div.heading--h4: ABC Normal 32px/42px 500, #171717 |
| Transition | none |
| Icon | 20 x 20, colour #76879d |
| Painted layers | div.price_card.is-pricing-new 360.0x594.6 bg #ffffff border T:1px solid #e0e0e0 / R:1px solid #e0e0e0 / B:1px solid #e0e0e0 / L:1px solid #e0e0e0; div.price_card_line 310.0x1.0 border B:1px solid #e0e0e0; button.price_toggle 50.0x20.0 bg #171717 r 16px; div.price_circle 16.0x16.0 bg #a284ff r 100%; div.discount 101.4x24.0 border T:1px solid #693ee0 / R:1px solid #693ee0 / B:1px solid #693ee0 / L:1px solid #693ee0 r 40px; a.btn--price.w-inline-block 310.0x47.0 bg #171717 r 8px |
| How | at rest |

Crops: `plan-card-default.png`.

#### plan-price

Plan price. The $29/mo price figure in the plan card.

Page: pricing. Selector: `plan $ figure`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 310 x 33.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ABC Normal 24px/33.6px 500 |
| Letter spacing | normal |
| Colour | #693ee0 |
| Transition | none |
| How | at rest |

Crops: `plan-price-default.png`.

#### plan-cta

Plan CTA. The plan card's "Get started" action; measured, never followed.

Page: pricing. Selector: `a.btn--price`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 310 x 47 | = | = | = |
| Padding | 12px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #171717 | #683ee0 | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #171717 | = | = | = |
| Text node | div.text--bold.text-color-white: Inter 16px/24px 700, #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.btn--price.w-inline-block 310.0x47.0 bg #171717 r 8px | a.btn--price.w-inline-block 310.0x47.0 bg #683ee0 r 8px | a.btn--price.w-inline-block 310.0x47.0 bg #171717 r 8px outline 1px auto #005fcc offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `plan-cta-default.png`, `plan-cta-hover.png`, `plan-cta-focus-visible.png`, `plan-cta-pressed.png`.

#### saving-badge

Saving badge. The "20% SAVING" outlined badge inside the plan card.

Page: pricing. Selector: `SAVING badge`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 101.42 x 24 |
| Padding | 0px 12px |
| Border | 1px solid #693ee0 |
| Radius | 40px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 12px/22px 500 |
| Letter spacing | normal |
| Colour | #693ee0 |
| Transition | none |
| Painted layers | div.discount 101.4x24.0 border T:1px solid #693ee0 / R:1px solid #693ee0 / B:1px solid #693ee0 / L:1px solid #693ee0 r 40px |
| How | at rest |

Crops: `saving-badge-default.png`.

#### faq-item

FAQ row. An FAQ accordion row (question + the open chevron); measured closed, the opened state is the screenshot toggle.

Page: pricing. Selector: `.faq_trigger`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 758 x 82 | = | = | = |
| Padding | 24px 72px 24px 24px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #4d65ff offset 2px | = |
| Font | Inter 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #3a4554 | = | = | = |
| Text node | h3.faq--text: ABC Normal 24px/34px 500, #171717 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20.92 x 28.8, colour #5d5d5d @ 0.7, fill #000000 | = | = | = |
| Painted layers | div.faq_trigger.w-dropdown-toggle 758.0x82.0 bg #ffffff | = | div.faq_trigger.w-dropdown-toggle 758.0x82.0 bg #ffffff outline 2px solid #4d65ff offset 2px | = |
| Ancestor paint | 1 up div.faq_card.w-dropdown bg #ffffff | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `faq-item-default.png`, `faq-item-hover.png`, `faq-item-focus-visible.png`, `faq-item-pressed.png`.

### Contact

#### contact-h1

Contact title. The "Got Questions?" display heading.

Page: contact. Selector: `h1.heading-01-hero`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 488.75 x 82 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ABC Normal 72px/82px 700 |
| Letter spacing | -2.16px |
| Colour | #171717 |
| Transition | none |
| How | at rest |

Crops: `contact-h1-default.png`.

#### name-input

Name field. The "Your Name" field of the contact form; focused and given sample text that was deleted again — never submitted.

Page: contact. Selector: `input#Name`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 550 x 48 | = | = |
| Padding | 12px 16px | = | = |
| Border | 1px solid #e0e0e0 | 1px solid #693ee0 | 1px solid #693ee0 |
| Radius | 5px | = | = |
| Background | #ffffff | = | = |
| Box shadow | none | #000000 @ 0.03 0px 2px 6px 0px | #000000 @ 0.03 0px 2px 6px 0px |
| Outline | none | = | = |
| Font | Inter 14px/20px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #171717 | = | = |
| Transition | color, box-shadow, border-color 0.2s, 0.2s, 0.2s ease, ease, ease delay 0s, 0s, 0s | = | = |
| Cursor | text | = | = |
| Placeholder | #5d5d5d @ 0.4, opacity 1 | = | = |
| Painted layers | input.request_input-field.w-input 550.0x48.0 bg #ffffff border T:1px solid #e0e0e0 / R:1px solid #e0e0e0 / B:1px solid #e0e0e0 / L:1px solid #e0e0e0 r 5px | input.request_input-field.w-input 550.0x48.0 bg #ffffff border T:1px solid #693ee0 / R:1px solid #693ee0 / B:1px solid #693ee0 / L:1px solid #693ee0 r 5px shadow #000000 @ 0.03 0px 2px 6px 0px | input.request_input-field.w-input 550.0x48.0 bg #ffffff border T:1px solid #693ee0 / R:1px solid #693ee0 / B:1px solid #693ee0 / L:1px solid #693ee0 r 5px shadow #000000 @ 0.03 0px 2px 6px 0px |
| How | at rest | clicked into the field | typed "Ada Example", then deleted; nothing sent |

Crops: `name-input-default.png`, `name-input-focused.png`, `name-input-filled.png`.

#### email-input

Email field. The "Your Email" field of the contact form.

Page: contact. Selector: `input#Email.request_input-field`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 550 x 48 |
| Padding | 12px 16px |
| Border | 1px solid #e0e0e0 |
| Radius | 5px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/20px 400 |
| Letter spacing | normal |
| Colour | #171717 |
| Transition | color, box-shadow, border-color 0.2s, 0.2s, 0.2s ease, ease, ease delay 0s, 0s, 0s |
| Cursor | text |
| Placeholder | #5d5d5d @ 0.4, opacity 1 |
| Painted layers | input.request_input-field.w-input 550.0x48.0 bg #ffffff border T:1px solid #e0e0e0 / R:1px solid #e0e0e0 / B:1px solid #e0e0e0 / L:1px solid #e0e0e0 r 5px |
| How | at rest |

Crops: `email-input-default.png`.

#### message-field

Message field. The "What would you like to learn?" textarea.

Page: contact. Selector: `textarea.request_input-field`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 550 x 80 |
| Padding | 12px 16px |
| Border | 1px solid #e0e0e0 |
| Radius | 5px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/20px 400 |
| Letter spacing | normal |
| Colour | #171717 |
| Transition | color, box-shadow, border-color 0.2s, 0.2s, 0.2s ease, ease, ease delay 0s, 0s, 0s |
| Cursor | text |
| Placeholder | #5d5d5d @ 0.4, opacity 1 |
| Painted layers | textarea.request_input-field.ms-text-area 550.0x80.0 bg #ffffff border T:1px solid #e0e0e0 / R:1px solid #e0e0e0 / B:1px solid #e0e0e0 / L:1px solid #e0e0e0 r 5px |
| How | at rest |

Crops: `message-field-default.png`.

#### send-button

Send button. The "Send message" action of the contact form (the input[type=submit] twin is hidden); measured, never pressed.

Page: contact. Selector: `form a.btn--primary`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 178.83 x 63 | = | = | = |
| Padding | 20px 32px | = | = | = |
| Gap | normal 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #171717 | #683ee0 | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | div.btn--primary_text.text-color-white: Inter 16px/24px 700, #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.btn--primary.align-left 178.8x63.0 bg #171717 r 8px | a.btn--primary.align-left 178.8x63.0 bg #683ee0 r 8px | a.btn--primary.align-left 178.8x63.0 bg #171717 r 8px outline 1px auto #005fcc offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `send-button-default.png`, `send-button-hover.png`, `send-button-focus-visible.png`, `send-button-pressed.png`.

#### contact-faq

Contact FAQ row. An FAQ accordion row beside the form; measured closed, never expanded.

Page: contact. Selector: `.faq_trigger`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 548 x 82 | = | = | = |
| Padding | 24px 72px 24px 24px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #4d65ff offset 2px | = |
| Font | Inter 18px/25.92px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #3a4554 | = | = | = |
| Text node | h3.faq--text: ABC Normal 24px/34px 500, #171717 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 18.67 x 28.8, colour #5d5d5d @ 0.7, fill #000000 | = | = | = |
| Painted layers | div.faq_trigger.w-dropdown-toggle 548.0x82.0 bg #ffffff | = | div.faq_trigger.w-dropdown-toggle 548.0x82.0 bg #ffffff outline 2px solid #4d65ff offset 2px | = |
| Ancestor paint | 1 up div.faq_card.w-dropdown bg #ffffff | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `contact-faq-default.png`, `contact-faq-hover.png`, `contact-faq-focus-visible.png`, `contact-faq-pressed.png`.

### Login

#### auth-card

Auth card. The login.copy.ai sign-in card (email field, Continue with email, the OAuth buttons, the Sign up link); captured, never used.

Page: login. Selector: `auth card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 344 x 283.89 |
| Padding | 0px |
| Gap | 24px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | interFont 16px/24px 400 |
| Letter spacing | normal |
| Colour | #202020 |
| Text node | label.rt-Text.rt-r-size-2: interFont 14px/20px 600, #202020 |
| Transition | none |
| Icon | 15 x 15, colour #202020 |
| Painted layers | div.rt-TextFieldRoot.rt-r-size-3 344.0x40.0 bg #ffffff @ 0.85 r 4.5px shadow #000000 @ 0.192 0px 0px 0px 1px inset; button.rt-reset.rt-BaseButton 344.0x40.0 bg #693ee0 r 4.5px shadow #000000 @ 0 0px 0px 0px 1px inset; div::before.rt-Text.rt-r-size-1 151.516pxx1px bg #000000 @ 0.15; div::after.rt-Text.rt-r-size-1 151.516pxx1px bg #000000 @ 0.15; a.rt-reset.rt-BaseButton 344.0x40.0 bg #ffffff @ 0.8 r 4.5px shadow #000000 @ 0.192 0px 0px 0px 1px inset; a.rt-reset.rt-BaseButton 344.0x40.0 bg #ffffff @ 0.8 r 4.5px shadow #000000 @ 0.192 0px 0px 0px 1px inset |
| Ancestor paint | 2 up div.rt-reset.rt-BaseCard shadow #939393 @ 0.341176 0px 0px 0px 1px inset |
| How | at rest |

Crops: `auth-card-default.png`.

#### auth-email

Auth email field. The "Your email address" input; focused and given sample text that was deleted again — nothing sent.

Page: login. Selector: `input[type=email]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 342 x 38 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 3.5px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | interFont 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #202020 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #000000 @ 0.486, opacity 1 | = | = |
| Ancestor paint | 1 up div.rt-TextFieldRoot.rt-r-size-3 bg #ffffff @ 0.85 shadow #000000 @ 0.192 0px 0px 0px 1px inset | 1 up div.rt-TextFieldRoot.rt-r-size-3 bg #ffffff @ 0.85 shadow #000000 @ 0.192 0px 0px 0px 1px inset outline 2px solid #a396ff | 1 up div.rt-TextFieldRoot.rt-r-size-3 bg #ffffff @ 0.85 shadow #000000 @ 0.192 0px 0px 0px 1px inset outline 2px solid #a396ff |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `auth-email-default.png`, `auth-email-focused.png`, `auth-email-filled.png`.

#### auth-continue

Continue button. The "Continue with email" submit; measured, never pressed.

Page: login. Selector: `Continue with email`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 344 x 40 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Gap | 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 4.5px | = | = | = |
| Background | #693ee0 | #5b36c3 | = | #4e22b1 |
| Box shadow | #000000 @ 0 0px 0px 0px 1px inset | = | = | = |
| Outline | none | = | 2px solid #a396ff offset 2px | = |
| Font | interFont 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span: interFont 16px/24px 500, #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.rt-reset.rt-BaseButton 344.0x40.0 bg #693ee0 r 4.5px shadow #000000 @ 0 0px 0px 0px 1px inset | button.rt-reset.rt-BaseButton 344.0x40.0 bg #5b36c3 r 4.5px shadow #000000 @ 0 0px 0px 0px 1px inset | button.rt-reset.rt-BaseButton 344.0x40.0 bg #693ee0 r 4.5px shadow #000000 @ 0 0px 0px 0px 1px inset outline 2px solid #a396ff offset 2px | button.rt-reset.rt-BaseButton 344.0x40.0 bg #4e22b1 r 4.5px shadow #000000 @ 0 0px 0px 0px 1px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `auth-continue-default.png`, `auth-continue-hover.png`, `auth-continue-focus-visible.png`, `auth-continue-pressed.png`.

#### auth-oauth

OAuth button. The "Continue with Google" action (an anchor); measured, never followed — it would leave for the OAuth flow.

Page: login. Selector: `Continue with Google`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 344 x 40 | = | = | = |
| Padding | 0px 8px | = | = | = |
| Gap | 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 4.5px | = | = | = |
| Background | #ffffff @ 0.8 | = | = | #000000 @ 0.06 |
| Box shadow | #000000 @ 0.192 0px 0px 0px 1px inset | #000000 @ 0.267 0px 0px 0px 1px inset | = | #000000 @ 0.267 0px 0px 0px 1px inset |
| Outline | none | = | 2px solid #a396ff offset -1px | = |
| Font | interFont 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #202020 | = | = | = |
| Text node | span.rt-Text.rt-r-size-2: interFont 16px/24px 500, #202020 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 15 x 15, colour #202020 | = | = | = |
| Painted layers | a.rt-reset.rt-BaseButton 344.0x40.0 bg #ffffff @ 0.8 r 4.5px shadow #000000 @ 0.192 0px 0px 0px 1px inset | a.rt-reset.rt-BaseButton 344.0x40.0 bg #ffffff @ 0.8 r 4.5px shadow #000000 @ 0.267 0px 0px 0px 1px inset | a.rt-reset.rt-BaseButton 344.0x40.0 bg #ffffff @ 0.8 r 4.5px shadow #000000 @ 0.192 0px 0px 0px 1px inset outline 2px solid #a396ff offset -1px | a.rt-reset.rt-BaseButton 344.0x40.0 bg #000000 @ 0.06 r 4.5px shadow #000000 @ 0.267 0px 0px 0px 1px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `auth-oauth-default.png`, `auth-oauth-hover.png`, `auth-oauth-focus-visible.png`, `auth-oauth-pressed.png`.

#### auth-signup

Sign-up link. The "Sign up" link on the auth card; measured, never followed.

Page: login. Selector: `Sign up link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 50.03 x 17 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | 0.735px | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #a396ff offset 2px | = |
| Font | interFont 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #5753c6 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Ancestor paint | 3 up div.rt-reset.rt-BaseCard shadow #939393 @ 0.341176 0px 0px 0px 1px inset | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.rt-Text.BrandedLink 50.0x17.0 r 0.735px outline 2px solid #a396ff offset 2px | = |

Crops: `auth-signup-default.png`, `auth-signup-hover.png`, `auth-signup-focus-visible.png`, `auth-signup-pressed.png`.

### Footer

#### footer

Footer. The footer: the link columns, social icons and legal.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 1066 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/20px 400 |
| Letter spacing | normal |
| Colour | #171717 |
| Text node | div.body-bold_v2: Inter 16px/24px 700, #171717 |
| Transition | none |
| Painted layers | div.foot-line_v2 260.0x1.0 bg #171717; div.foot-line_v2 260.0x1.0 bg #171717; div.foot-line_v2 260.0x1.0 bg #171717; div.foot-line_v2 260.0x1.0 bg #171717; div.footer--bottom 1440.0x165.0 bg #171717 |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link. A footer column link (Blog / Contact Support / Changelog); measured, never followed.

Page: home. Selector: `a.footer_link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 260 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #171717 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.footer_link 260.0x24.0 outline 1px auto #005fcc offset 1px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### social-icon

Social link. A social link in the footer.

Page: home. Selector: `footer social a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 36 x 35 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #171717 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.w-inline-block 36.0x35.0 outline 1px auto #005fcc offset 1px | = |

Crops: `social-icon-default.png`, `social-icon-hover.png`, `social-icon-focus-visible.png`, `social-icon-pressed.png`.

### Mobile (390 wide)

#### m-header

Mobile header.

Page: mobile. Selector: `nav.mega--nav at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 80 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/20px 400 |
| Letter spacing | normal |
| Colour | #171717 |
| Transition | none |
| Icon | 0 x 0, colour #222222 |
| Painted layers | nav.mega--nav 390.0x80.0 bg #ffffff; div.mega--nav_menu 0.0x0.0 bg #ffffff; div.mega--nav_dd_toggle.w-dropdown-toggle 0.0x0.0 border B:1px solid #e0e0e0; nav.mega--nav_dd_list.w-dropdown-list 0.0x0.0 bg #ffffff; div.dd-link_icon-wr 0.0x0.0 bg #fbfbfc border T:1px solid #e0e0e0 / R:1px solid #e0e0e0 / B:1px solid #e0e0e0 / L:1px solid #e0e0e0 r 8px; div.dd-link_icon-wr 0.0x0.0 bg #fbfbfc border T:1px solid #e0e0e0 / R:1px solid #e0e0e0 / B:1px solid #e0e0e0 / L:1px solid #e0e0e0 r 8px |
| How | at rest |

Crops: `m-header-default.png`.

#### m-menu-button

Menu button. The circled burger toggle (a.mega--nav_burger_trigger).

Page: mobile. Selector: `.mega--nav_burger_trigger`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 46 x 46 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #171717 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 17.59 x 17.59, colour #171717, fill #000000 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.mega--nav_burger_trigger.w-inline-block 46.0x46.0 outline 1px auto #005fcc offset 1px | = |

Crops: `m-menu-button-default.png`, `m-menu-button-hover.png`, `m-menu-button-focus-visible.png`, `m-menu-button-pressed.png`.

#### m-menu-open

Mobile menu, open. The opened mobile menu: the accordion rows (Platform / Use cases / Resources / Pricing / GTM AI) over the page with Login and Contact Sales at the foot.

Page: mobile. Selector: `opened mobile menu`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 844 |
| Padding | 0px |
| Border | T: 1px solid #e0e0e0; R: none; B: none; L: none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/20px 400 |
| Letter spacing | normal |
| Colour | #171717 |
| Text node | div: Inter 16px/24px 500, #222222 |
| Transition | none |
| Icon | 20 x 20, colour #222222 |
| Painted layers | div.mega--nav_burger_list 390.0x844.0 bg #ffffff border T:1px solid #e0e0e0; div.mega--nav_menu 350.0x445.0 bg #ffffff; div.mega--nav_dd_toggle.w-dropdown-toggle 350.0x89.0 border B:1px solid #e0e0e0; nav.mega--nav_dd_list.w-dropdown-list 0.0x0.0 bg #ffffff; div.dd-link_icon-wr 0.0x0.0 bg #fbfbfc border T:1px solid #e0e0e0 / R:1px solid #e0e0e0 / B:1px solid #e0e0e0 / L:1px solid #e0e0e0 r 8px; div.dd-link_icon-wr 0.0x0.0 bg #fbfbfc border T:1px solid #e0e0e0 / R:1px solid #e0e0e0 / B:1px solid #e0e0e0 / L:1px solid #e0e0e0 r 8px |
| How | at rest |

Crops: `m-menu-open-default.png`.

#### m-nav-item

Mobile menu row. A row inside the opened mobile menu.

Page: mobile. Selector: `mobile menu row`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 350 x 89 | = | = | = |
| Padding | 32px 0px | = | = | = |
| Border | T: none; R: none; B: 1px solid #e0e0e0; L: none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | #171717 0px -1px 0px 0px inset | = | #171717 0px -1px 0px 0px inset |
| Outline | none | = | 2px solid #4d65ff offset 2px | = |
| Font | Inter 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #222222 | = | = | = |
| Text node | div: Inter 16px/24px 500, #222222 | = | = | = |
| Transition | all, box-shadow 0.2s, 0.4s ease, ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #222222 | = | = | = |
| Painted layers | div.mega--nav_dd_toggle.w-dropdown-toggle 350.0x89.0 border B:1px solid #e0e0e0 | div.mega--nav_dd_toggle.w-dropdown-toggle 350.0x89.0 border B:1px solid #e0e0e0 shadow #171717 0px -1px 0px 0px inset | div.mega--nav_dd_toggle.w-dropdown-toggle 350.0x89.0 border B:1px solid #e0e0e0 outline 2px solid #4d65ff offset 2px | div.mega--nav_dd_toggle.w-dropdown-toggle 350.0x89.0 border B:1px solid #e0e0e0 shadow #171717 0px -1px 0px 0px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-nav-item-default.png`, `m-nav-item-hover.png`, `m-nav-item-focus-visible.png`, `m-nav-item-pressed.png`.

#### m-login

Mobile login. The Login action inside the mobile menu; measured, never followed.

Page: mobile. Selector: `mobile menu Login`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 118 x 50 | = | = | = |
| Padding | 12px 16px | = | = | = |
| Border | 1px solid #e0e0e0 | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter 16px/24px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #171717 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.mega--nav_login-link 118.0x50.0 border T:1px solid #e0e0e0 / R:1px solid #e0e0e0 / B:1px solid #e0e0e0 / L:1px solid #e0e0e0 r 8px | = | a.mega--nav_login-link 118.0x50.0 border T:1px solid #e0e0e0 / R:1px solid #e0e0e0 / B:1px solid #e0e0e0 / L:1px solid #e0e0e0 r 8px outline 1px auto #005fcc offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-login-default.png`, `m-login-hover.png`, `m-login-focus-visible.png`, `m-login-pressed.png`.

#### m-sales

Mobile sales CTA. The purple Contact Sales action inside the mobile menu; measured, never followed.

Page: mobile. Selector: `mobile menu Contact Sales`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 208 x 50 | = | = | = |
| Padding | 12px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | #693edf | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #171717 | = | = | = |
| Text node | div.btn--primary_text.text-color-white: Inter 16px/24px 700, #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.btn_nav.w-inline-block 208.0x50.0 bg #693edf r 4px | = | a.btn_nav.w-inline-block 208.0x50.0 bg #693edf r 4px outline 1px auto #005fcc offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-sales-default.png`, `m-sales-hover.png`, `m-sales-focus-visible.png`, `m-sales-pressed.png`.

#### m-hero

Mobile headline.

Page: mobile. Selector: `h1 at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 215.08 x 107.25 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ABC Normal 42.9px/53.625px 600 |
| Letter spacing | normal |
| Colour | #171717 |
| Transition | none |
| How | at rest |

Crops: `m-hero-default.png`.

## Transitions declared in the readable stylesheets

copy.ai serves its Webflow sheets cross-origin from cdn.prod.website-files.com, so the readable CSSOM holds only the inline styles; this list covers the transition rules the page itself exposes, and the per-state Transition rows above are the computed values the page paints.

- contact: `inherit`, `unset`, `background-color 0.1s, color 0.1s`, `0.3s`, `border-color 0.3s, background-color 0.3s`, `background-color 0.15s`, `color 0.4s`, `background-color 0.3s`, `border-color 0.35s`, `color 0.2s, transform 0.2s`, `box-shadow 0.4s`, `opacity 0.2s, transform 0.2s`

- home: `inherit`, `unset`, `background-color 0.1s, color 0.1s`, `0.3s`, `border-color 0.3s, background-color 0.3s`, `color 0.1s`, `color 0.4s`, `background-color 0.3s`, `color 0.2s, transform 0.2s`, `opacity 0.3s`, `box-shadow 0.4s`, `opacity 0.2s, transform 0.2s`

- login: `unset`, `inherit`, `box-shadow 0.12s`, `box-shadow 0.12s, background-color 0.12s`, `transform 0.12s`, `background-color 0.1s`, `background-position linear, background-color ease-in-out, box-shadow ease-in-out, filter ease-in-out`, `transform 0.14s cubic-bezier(0.45, 0.05, 0.55, 0.95), box-shadow 0.14s ease-in-out`, `none`, `box-shadow 0.18s`, `inline-size 0.3s cubic-bezier(0.22, 1, 0.36, 1)`, `opacity 0.15s ease-out, transform 0.15s ease-out, visibility 0.15s`

- pricing: `inherit`, `unset`, `background-color 0.1s, color 0.1s`, `0.3s`, `color 0.1s`, `color 0.4s`, `background-color 0.3s`, `border-color 0.35s`, `color 0.2s, transform 0.2s`, `opacity 0.3s`, `box-shadow 0.4s`, `opacity 0.2s, transform 0.2s`
