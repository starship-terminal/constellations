# Family component measurements

Computed styles read from family.co and app.family.co on 2026-11-14 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the site's painted surfaces — home, /blog + a post, /changelog, /support + an article, /faqs, /legal, the docs pages and the Aave Account login — and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Header and navigation

#### mkt-header

Site header. The fixed top bar: the Family wordmark, the Developers/Resources hover dropdowns, X (Twitter), Log In and the dark Get Started pill.

Page: home. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1024 x 94 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/normal 400 |
| Letter spacing | normal |
| Colour | #474645 |
| Text node | a: Inter 15px/10px 500, #282624 |
| Transition | none |
| Transform | matrix3d(1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1) |
| Icon | 72 x 18, colour #262626 |
| Painted layers | a 119.0x32.9 bg #ffffff r 6px; div.Nav__DropdownContainer-sc-141m4ur-3.jmGeWm 303.4x129.6 bg #ffffff r 8px shadow #000000 @ 0.1 0px 3px 16px 0px; div.Nav__IconContainer-sc-141m4ur-2.jhkKsN 34.6x34.6 bg #ffffff r 9.6px shadow #000000 @ 0.04 0px 0px 0px 1px; div.Nav__IconContainer-sc-141m4ur-2.jhkKsN 34.6x34.6 bg #ffffff r 9.6px shadow #000000 @ 0.04 0px 0px 0px 1px; a 113.0x32.9 bg #ffffff r 6px; div.Nav__DropdownContainer-sc-141m4ur-3.jmGeWm 157.4x161.3 bg #ffffff r 8px shadow #000000 @ 0.1 0px 3px 16px 0px |
| How | at rest |

Crops: `mkt-header-default.png`.

#### mkt-logo

Logo. The Family wordmark at the left of the header.

Page: home. Selector: `header logo`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 96 x 34 |
| Padding | 8px 12px |
| Border | none |
| Radius | 6px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/normal 500 |
| Letter spacing | normal |
| Colour | #474645 |
| Transition | all 0.2s ease-out |
| Cursor | pointer |
| Icon | 72 x 18, colour #262626 |
| How | at rest |

Crops: `mkt-logo-default.png`.

#### nav-developers

Developers menu. The Developers dropdown trigger; hover opens the ConnectKit/Family card menu — measured, never followed.

Page: home. Selector: `header Developers`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 119 x 32.91 | = | = | = |
| Padding | 11px 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 6px | = | = | = |
| Background | #ffffff | color(display-p3 0.984314 0.980392 0.976471) | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid color(display-p3 0.517647 0.509804 0.505882) offset 1px | = |
| Font | Inter 15px/10px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #282624 | color(display-p3 0.203922 0.203922 0.2) | = | = |
| Transition | background, color 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 10 x 10, colour #282624 | 10 x 10, colour color(display-p3 0.203922 0.203922 0.2) | = | = |
| Painted layers | a 119.0x32.9 bg #ffffff r 6px | a 119.0x32.9 bg color(display-p3 0.984314 0.980392 0.976471) r 6px | a 119.0x32.9 bg #ffffff r 6px outline 2px solid color(display-p3 0.517647 0.509804 0.505882) offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-developers-default.png`, `nav-developers-hover.png`, `nav-developers-focus-visible.png`, `nav-developers-pressed.png`.

#### nav-dropdown

Nav dropdown. The Developers dropdown panel (ConnectKit and Family cards); opened by hovering the trigger.

Page: home. Selector: `Nav__DropdownContainer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 316 x 135 |
| Padding | 4px |
| Border | none |
| Radius | 8px |
| Background | #ffffff |
| Box shadow | #000000 @ 0.1 0px 3px 16px 0px |
| Outline | none |
| Font | Inter 16px/normal 400 |
| Letter spacing | normal |
| Colour | #474645 |
| Text node | h5.Typography__Paragraph-sc-p3xo6h-7.hAxgce: Inter 15px/22px 500, #121212, ls -0.13px |
| Transition | opacity, transform 0.1s ease |
| Transform | matrix3d(1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1) |
| Icon | 23 x 28, colour color(display-p3 0.203922 0.203922 0.2) |
| ::before | 316px x 8px, absolute, bg #000000 @ 0, radius 0px |
| Painted layers | div.Nav__DropdownContainer-sc-141m4ur-3.jmGeWm 316.0x135.0 bg #ffffff r 8px shadow #000000 @ 0.1 0px 3px 16px 0px; div.Nav__IconContainer-sc-141m4ur-2.jhkKsN 36.0x36.0 bg #ffffff r 9.6px shadow #000000 @ 0.04 0px 0px 0px 1px; div.Nav__IconContainer-sc-141m4ur-2.jhkKsN 36.0x36.0 bg #ffffff r 9.6px shadow #000000 @ 0.04 0px 0px 0px 1px |
| How | at rest |

Crops: `nav-dropdown-default.png`.

#### nav-resources

Resources menu. The Resources dropdown trigger (Blog / Changelog / Help & Support / FAQs); measured, never followed.

Page: home. Selector: `header Resources`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 113 x 32.91 | = | = | = |
| Padding | 11px 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 6px | = | = | = |
| Background | #ffffff | color(display-p3 0.984314 0.980392 0.976471) | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid color(display-p3 0.517647 0.509804 0.505882) offset 1px | = |
| Font | Inter 15px/10px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #282624 | color(display-p3 0.203922 0.203922 0.2) | = | = |
| Transition | background, color 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 10 x 10, colour #282624 | 10 x 10, colour color(display-p3 0.203922 0.203922 0.2) | = | = |
| Painted layers | a 113.0x32.9 bg #ffffff r 6px | a 113.0x32.9 bg color(display-p3 0.984314 0.980392 0.976471) r 6px | a 113.0x32.9 bg #ffffff r 6px outline 2px solid color(display-p3 0.517647 0.509804 0.505882) offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-resources-default.png`, `nav-resources-hover.png`, `nav-resources-focus-visible.png`, `nav-resources-pressed.png`.

#### nav-twitter

X (Twitter) link. The header social link; measured, never followed.

Page: home. Selector: `header X (Twitter)`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 97 x 32 | = | = | = |
| Padding | 11px 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 6px | = | = | = |
| Background | #ffffff | color(display-p3 0.984314 0.980392 0.976471) | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid color(display-p3 0.517647 0.509804 0.505882) offset 1px | = |
| Font | Inter 15px/10px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #282624 | color(display-p3 0.203922 0.203922 0.2) | = | = |
| Transition | background, color 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a 97.0x32.0 bg #ffffff r 6px | a 97.0x32.0 bg color(display-p3 0.984314 0.980392 0.976471) r 6px | a 97.0x32.0 bg #ffffff r 6px outline 2px solid color(display-p3 0.517647 0.509804 0.505882) offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-twitter-default.png`, `nav-twitter-hover.png`, `nav-twitter-focus-visible.png`, `nav-twitter-pressed.png`.

#### login-btn

Log In button. The beige Log In pill in the header, inside a link to app.family.co; measured, never followed.

Page: home. Selector: `a.login-button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 70.47 x 32 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 16px/normal 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #474645 | = | = | = |
| Text node | button.Button__Container-sc-1jjqbrw-0.hACioR: Inter 15px/normal 500, #121212, ls -0.09px | = | = | = |
| Transition | all 0.2s ease-out | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.Button__Container-sc-1jjqbrw-0.hACioR 70.5x32.0 bg #f6f4ef r 32px | button.Button__Container-sc-1jjqbrw-0.hACioR 70.5x32.0 bg #eae6dd r 32px | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `login-btn-default.png`, `login-btn-hover.png`, `login-btn-focus-visible.png`, `login-btn-pressed.png`.

#### getstarted-btn

Get Started button. The near-black Get Started pill; measured, never pressed (it starts the download flow).

Page: home. Selector: `header Get Started`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 109.02 x 32 | = | = | = |
| Padding | 0px 14px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 32px | = | = | = |
| Background | #171717 | #121212 | = | #121212 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 15px/normal 500 | = | = | = |
| Letter spacing | -0.09px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color 0.1s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.Button__Container-sc-1jjqbrw-0.fnjIlG 109.0x32.0 bg #171717 r 32px | button.Button__Container-sc-1jjqbrw-0.fnjIlG 109.0x32.0 bg #121212 r 32px | = | button.Button__Container-sc-1jjqbrw-0.fnjIlG 109.0x32.0 bg #121212 r 32px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `getstarted-btn-default.png`, `getstarted-btn-hover.png`, `getstarted-btn-focus-visible.png`, `getstarted-btn-pressed.png`.

### Home

#### hero-h1

Hero headline. "Your favorite crypto wallet." — the Family display face hero.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1024 x 165.59 |
| Padding | 0px 0px 16px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Family 68px/74.8px 500 |
| Letter spacing | -1.36px |
| Colour | color(display-p3 0.203922 0.203922 0.2) |
| Text node | span: Family 68px/74.8px 500, color(display-p3 0.203922 0.203922 0.2), ls -1.36px |
| Transition | none |
| How | at rest |

Crops: `hero-h1-default.png`.

#### hero-sub

Hero subline. The "Explore Ethereum with the best wallet for iOS" subline under the hero.

Page: home. Selector: `hero subline`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 408 x 52 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 17px/26px 500 |
| Letter spacing | -0.22px |
| Colour | #474645 |
| Transition | none |
| How | at rest |

Crops: `hero-sub-default.png`.

#### download-cta

Download CTA. The "Download on iOS" pill; measured, never followed (it goes to the App Store).

Page: home. Selector: `Download on iOS`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 209.7 x 48 | = | = | = |
| Padding | 0px 24px 0px 22px | = | = | = |
| Gap | 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 32px | = | = | = |
| Background | #171717 | #121212 | = | #121212 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 17px/17px 500 | = | = | = |
| Letter spacing | -0.22px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color 0.1s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 20, colour #ffffff | = | = | = |
| Painted layers | a.SectionIntro__Button-sc-1nhl813-4.dQyCQZ 209.7x48.0 bg #171717 r 32px | a.SectionIntro__Button-sc-1nhl813-4.dQyCQZ 209.7x48.0 bg #121212 r 32px | = | a.SectionIntro__Button-sc-1nhl813-4.dQyCQZ 209.7x48.0 bg #121212 r 32px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `download-cta-default.png`, `download-cta-hover.png`, `download-cta-focus-visible.png`, `download-cta-pressed.png`.

#### watch-video

Watch the Video. The "Watch the Video" action beside the download pill; measured, never pressed.

Page: home. Selector: `Watch the Video`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 199.7 x 48 | = | - | = |
| Padding | 0px 20px 0px 19px | = | - | = |
| Gap | 11px | = | - | = |
| Border | none | = | - | = |
| Radius | 32px | = | - | = |
| Background | #f6f4ef | #eae6dd | - | #eae6dd |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Inter 17px/17px 500 | = | - | = |
| Letter spacing | -0.22px | = | - | = |
| Colour | #121212 | = | - | = |
| Transition | background-color 0.1s ease | = | - | = |
| Cursor | pointer | = | - | = |
| Icon | 18 x 20, colour #121212 | = | - | = |
| Painted layers | a.SectionIntro__Button-sc-1nhl813-4.cxKtcG 199.7x48.0 bg #f6f4ef r 32px | a.SectionIntro__Button-sc-1nhl813-4.cxKtcG 199.7x48.0 bg #eae6dd r 32px | - | a.SectionIntro__Button-sc-1nhl813-4.cxKtcG 199.7x48.0 bg #eae6dd r 32px |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `watch-video-default.png`, `watch-video-hover.png`, `watch-video-pressed.png`.

#### feature-h2

Section heading. A marketing section heading ("Explore Ethereum in a whole new way.").

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1024 x 48 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Family 44px/48px 500 |
| Letter spacing | -1.35px |
| Colour | #121212 |
| Transition | none |
| How | at rest |

Crops: `feature-h2-default.png`.

#### feature-label

Feature label. A feature label in the intro grid (Easy / Secure / Fast / Powerful / Fun).

Page: home. Selector: `feature label`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 38.13 x 26 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 17px/26px 600 |
| Letter spacing | -0.22px |
| Colour | #121212 |
| Transition | none |
| How | at rest |

Crops: `feature-label-default.png`.

#### feature-body

Feature body. Feature body copy ("Whether you’re a beginner or seasoned pro, Family makes it easy.").

Page: home. Selector: `feature body`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 273.06 x 44 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 15px/22px 400 |
| Letter spacing | -0.13px |
| Colour | #474645 @ 0.7 |
| Transition | none |
| How | at rest |

Crops: `feature-body-default.png`.

#### demo-btn

Watch-the-demo button. A "Watch the demo" button under a feature; opens the video overlay — measured, the press opens a local overlay only.

Page: home. Selector: `Watch the demo`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 314.69 x 68 | = | = | = |
| Padding | 12px 32px 12px 12px | = | = | = |
| Gap | 12.8px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | color(display-p3 0.94902 0.941176 0.929412) 0px 0px 0px 0px inset | color(display-p3 0.94902 0.941176 0.929412) 0px 0px 0px 1px inset | color(display-p3 0.517647 0.509804 0.505882) 0px 0px 0px 2px inset | color(display-p3 0.94902 0.941176 0.929412) 0px 0px 0px 1px inset |
| Outline | none | = | = | = |
| Font | Inter 13.3333px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | color(display-p3 0.286275 0.266667 0.25098) | = | = | = |
| Text node | h5.Typography__Paragraph-sc-p3xo6h-7.hAxgce: Inter 15px/22px 500, #121212, ls -0.13px | = | = | = |
| Transition | box-shadow 0.1s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 26 x 28, colour color(display-p3 0.286275 0.266667 0.25098) | = | = | = |
| Painted layers | button.WatchDemo__Container-sc-1kj9jjo-0.dIaiHi 314.7x68.0 r 12px shadow color(display-p3 0.94902 0.941176 0.929412) 0px 0px 0px 0px inset; div.WatchDemo__ImageContainer-sc-1kj9jjo-1.dKfigb 78.0x44.0 bg color(display-p3 0.94902 0.941176 0.929412) r 4px; div::before.sc-gsFSXq.kakWLo 78pxx43.875px bg #fbfaf9 image linear-gradient(90deg, #fbfaf9 50%, #e5e4e4, #fbfaf9) r 8px | button.WatchDemo__Container-sc-1kj9jjo-0.dIaiHi 314.7x68.0 r 12px shadow color(display-p3 0.94902 0.941176 0.929412) 0px 0px 0px 1px inset; div.WatchDemo__ImageContainer-sc-1kj9jjo-1.dKfigb 78.0x44.0 bg color(display-p3 0.94902 0.941176 0.929412) r 4px; div::before.sc-gsFSXq.kakWLo 78pxx43.875px bg #fbfaf9 image linear-gradient(90deg, #fbfaf9 50%, #e5e4e4, #fbfaf9) r 8px | button.WatchDemo__Container-sc-1kj9jjo-0.dIaiHi 314.7x68.0 r 12px shadow color(display-p3 0.517647 0.509804 0.505882) 0px 0px 0px 2px inset; div.WatchDemo__ImageContainer-sc-1kj9jjo-1.dKfigb 78.0x44.0 bg color(display-p3 0.94902 0.941176 0.929412) r 4px; div::before.sc-gsFSXq.kakWLo 78pxx43.875px bg #fbfaf9 image linear-gradient(90deg, #fbfaf9 50%, #e5e4e4, #fbfaf9) r 8px | button.WatchDemo__Container-sc-1kj9jjo-0.dIaiHi 314.7x68.0 r 12px shadow color(display-p3 0.94902 0.941176 0.929412) 0px 0px 0px 1px inset; div.WatchDemo__ImageContainer-sc-1kj9jjo-1.dKfigb 78.0x44.0 bg color(display-p3 0.94902 0.941176 0.929412) r 4px; div::before.sc-gsFSXq.kakWLo 78pxx43.875px bg #fbfaf9 image linear-gradient(90deg, #fbfaf9 50%, #e5e4e4, #fbfaf9) r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `demo-btn-default.png`, `demo-btn-hover.png`, `demo-btn-focus-visible.png`, `demo-btn-pressed.png`.

#### demo-overlay

Demo overlay. The full-viewport video overlay "Watch the demo" mounts; measured open, then closed.

Page: home. Selector: `WatchDemo__OverlayContainer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 900 |
| Padding | 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/normal 400 |
| Letter spacing | normal |
| Colour | #474645 |
| Text node | span.sc-aXZVg.fLBVfX: Inter 16px/22px 500, #ffffff |
| Transition | none |
| Icon | 14 x 14, colour #000000 |
| Painted layers | div.WatchDemo__OverlayBackground-sc-1kj9jjo-4.kCuicB 1440.0x900.0 bg #f9f7f5 @ 0.8; div.WatchDemo__VideoContainer-sc-1kj9jjo-5.cgVGwv 860.0x483.8 bg #cccccc r 12px; div.WatchDemo__IconContainer-sc-1kj9jjo-8.fnJard 860.0x483.8 bg #000000 @ 0.1 |
| How | at rest |

Crops: `demo-overlay-default.png`.

#### feature-h3

Feature tag. A feature tag ("Send & Receive", "WalletConnect Enabled") beside a section.

Page: home. Selector: `h5 feature tag`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 472 x 20 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/20px 600 |
| Letter spacing | -0.09px |
| Colour | color(display-p3 0.215686 0.517647 0.956863) |
| Transition | none |
| How | at rest |

Crops: `feature-h3-default.png`.

#### section-h3

Feature section heading. A feature section heading ("Send, receive, swap. All in one place.").

Page: home. Selector: `section h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1024 x 96 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Family 44px/48px 500 |
| Letter spacing | -1.35px |
| Colour | #121212 |
| Text node | span: Family 44px/48px 500, #121212, ls -1.35px |
| Transition | none |
| How | at rest |

Crops: `section-h3-default.png`.

#### faq-item

FAQ item. A collapsible question/answer item in the home FAQ ("Is Family safe?").

Page: home. Selector: `Item__StyledCollapsableItem`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 512 x 56 |
| Padding | 0px 0px 28px 0px |
| Gap | 24px |
| Border | T: none; R: none; B: 1px solid color(display-p3 0.94902 0.941176 0.929412); L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/normal 400 |
| Letter spacing | normal |
| Colour | #474645 |
| Text node | h4.Typography__Paragraph-sc-p3xo6h-7.eHgZom: Inter 19px/27px 500, #121212, ls -0.3px |
| Transition | none |
| Painted layers | div.Item__StyledCollapsableItem-sc-bjycf3-2.egfBPj 512.0x56.0 border B:1px solid color(display-p3 0.94902 0.941176 0.929412); div 14.0x2.0 bg color(display-p3 1 0.32549 0.0627451) r 2px; div 2.0x14.0 bg color(display-p3 1 0.32549 0.0627451) r 2px; a::after 132.266pxx2px bg #1a88f8 r 2px |
| How | at rest |

Crops: `faq-item-default.png`.

#### faq-toggle

FAQ toggle. The 14px collapse toggle on an FAQ item; measured, never pressed.

Page: home. Selector: `Item__Toggle`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 14 x 14 | = | 14 x 16 | = |
| Padding | 4px 0px | = | 8px 0px | = |
| Border | none | = | = | = |
| Radius | 0px | = | 4px | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid color(display-p3 0.517647 0.509804 0.505882) offset 0px | = |
| Font | Inter 13.3333px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | color(display-p3 1 0.32549 0.0627451) | = | = | = |
| Transition | none | = | = | = |
| Cursor | default | = | = | = |
| Painted layers | div 14.0x2.0 bg color(display-p3 1 0.32549 0.0627451) r 2px; div 2.0x14.0 bg color(display-p3 1 0.32549 0.0627451) r 2px | = | button.Item__Toggle-sc-bjycf3-4.iIeMnL 14.0x16.0 r 4px outline 2px solid color(display-p3 0.517647 0.509804 0.505882) offset 0px; div 14.0x2.0 bg color(display-p3 1 0.32549 0.0627451) r 2px; div 2.0x14.0 bg color(display-p3 1 0.32549 0.0627451) r 2px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `faq-toggle-default.png`, `faq-toggle-hover.png`, `faq-toggle-focus-visible.png`, `faq-toggle-pressed.png`.

#### tweet-card

Tweet card. A "Friends of Family" testimonial card linking to a tweet; measured, never followed.

Page: home. Selector: `Testimonials__Panel`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 540 x 204 | = | - | = |
| Padding | 32px | = | - | = |
| Border | none | = | - | = |
| Radius | 10px | = | - | = |
| Background | color(display-p3 1 1 1) | = | - | color(display-p3 0.984314 0.980392 0.976471) |
| Box shadow | color(display-p3 0.94902 0.941176 0.929412) 0px 0px 0px 1px inset | = | - | color(display-p3 0.984314 0.980392 0.976471) 0px 0px 0px 0px inset |
| Outline | none | = | - | = |
| Font | Inter 16px/normal 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #474645 | = | - | = |
| Text node | div.Typography__Paragraph-sc-p3xo6h-7.cfflXR: Inter 15px/22px 600, #474645, ls -0.13px | = | - | = |
| Transition | box-shadow, background 0.1s ease | = | - | = |
| Icon | 20 x 21.11, colour color(display-p3 0.203922 0.203922 0.2) | = | - | = |
| Painted layers | div.Testimonials__Panel-sc-1rcs3hw-3.gqyXuo 540.0x204.0 bg color(display-p3 1 1 1) r 10px shadow color(display-p3 0.94902 0.941176 0.929412) 0px 0px 0px 1px inset; div::before.sc-gsFSXq.cBSgSE 40pxx40px bg #fbfaf9 image linear-gradient(90deg, #fbfaf9 50%, #e5e4e4, #fbfaf9) r 40px | = | - | div.Testimonials__Panel-sc-1rcs3hw-3.gqyXuo 540.0x204.0 bg color(display-p3 0.984314 0.980392 0.976471) r 10px shadow color(display-p3 0.984314 0.980392 0.976471) 0px 0px 0px 0px inset; div::before.sc-gsFSXq.cBSgSE 40pxx40px bg #fbfaf9 image linear-gradient(90deg, #fbfaf9 50%, #e5e4e4, #fbfaf9) r 40px |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `tweet-card-default.png`, `tweet-card-hover.png`, `tweet-card-pressed.png`.

### Blog

#### blog-card

Post card. A post card on /blog; measured, never followed.

Page: blog. Selector: `a[href^=/blog/]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 1024 x 280 | = | = | = |
| Padding | 96px 0px 72px 0px | = | = | = |
| Gap | 32px | = | = | = |
| Border | T: none; R: none; B: 1px solid color(display-p3 0.94902 0.941176 0.929412); L: none | = | = | = |
| Radius | 0px | = | 8px | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid color(display-p3 0.517647 0.509804 0.505882) offset 1px | = |
| Font | Inter 16px/normal 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #474645 | = | = | = |
| Text node | p.Typography__Paragraph-sc-p3xo6h-7.gPoOIL: Inter 15px/22px 400, color(display-p3 0.517647 0.509804 0.505882), ls -0.13px | = | = | = |
| Transition | opacity 0.1s ease | = | none | = |
| Cursor | pointer | = | = | = |
| Painted layers | a 1024.0x280.0 border B:1px solid color(display-p3 0.94902 0.941176 0.929412); span.dot 0.0x0.0 bg color(display-p3 0.517647 0.509804 0.505882) r 50% | = | a 1024.0x280.0 border B:1px solid color(display-p3 0.94902 0.941176 0.929412) r 8px outline 2px solid color(display-p3 0.517647 0.509804 0.505882) offset 1px; span.dot 0.0x0.0 bg color(display-p3 0.517647 0.509804 0.505882) r 50% | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.75 | = | 0.75 |

Crops: `blog-card-default.png`, `blog-card-hover.png`, `blog-card-focus-visible.png`, `blog-card-pressed.png`.

#### blog-h1

Blog title. The "Blog" page title.

Page: blog. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 88.63 x 48 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Family 44px/48px 500 |
| Letter spacing | -1.35px |
| Colour | #121212 |
| Text node | span: Family 44px/48px 500, #121212, ls -1.35px |
| Transition | none |
| How | at rest |

Crops: `blog-h1-default.png`.

#### blog-filter

Blog filter. A topic filter button (All / News / Wallet); "opened" is its selected state — a local filter toggle, never a submission.

Page: blog. Selector: `blog filter button`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 43 x 33.38 | = | = | = | = |
| Padding | 7.2px 12px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 32px | = | = | = | = |
| Background | color(display-p3 0.917647 0.917647 0.917647) | = | = | = | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 2px solid color(display-p3 0.517647 0.509804 0.505882) offset 0px | = | = |
| Font | Inter 15px/normal 500 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | color(display-p3 0.203922 0.203922 0.2) | = | = | = | = |
| Transition | transform, color, background 0.2s ease | = | none | transform, color, background 0.1s ease | = |
| Cursor | pointer | = | = | = | = |
| Painted layers | button.Filters__Button-sc-ef5306-1.hrdrRW 43.0x33.4 bg color(display-p3 0.917647 0.917647 0.917647) r 32px | = | button.Filters__Button-sc-ef5306-1.hrdrRW 43.0x33.4 bg color(display-p3 0.917647 0.917647 0.917647) r 32px outline 2px solid color(display-p3 0.517647 0.509804 0.505882) offset 0px | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |

Crops: `blog-filter-default.png`, `blog-filter-hover.png`, `blog-filter-focus-visible.png`, `blog-filter-pressed.png`, `blog-filter-opened.png`.

#### blog-date

Post date line. The post date/tag meta line on a post card ("13 May, 2025  News, Wallet").

Page: blog. Selector: `post date`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 160 x 111 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 15px/22px 400 |
| Letter spacing | -0.13px |
| Colour | color(display-p3 0.517647 0.509804 0.505882) |
| Transition | none |
| Cursor | pointer |
| Painted layers | span.dot 0.0x0.0 bg color(display-p3 0.517647 0.509804 0.505882) r 50% |
| How | at rest |

Crops: `blog-date-default.png`.

#### post-h1

Article title. The blog article title ("The Crypto Wallet Problem – Why We Created Family Accounts").

Page: blogpost. Selector: `article h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 732 x 96 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Family 44px/48px 500 |
| Letter spacing | -1.35px |
| Colour | #121212 |
| Transition | none |
| How | at rest |

Crops: `post-h1-default.png`.

#### post-h2

Article subheading. An H2 subheading inside the article.

Page: blogpost. Selector: `article h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 732 x 27 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 19px/27px 500 |
| Letter spacing | -0.3px |
| Colour | #121212 |
| Transition | none |
| How | at rest |

Crops: none.

#### post-body

Article body. Article body copy.

Page: blogpost. Selector: `article p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 732 x 162 |
| Padding | 0px 0px 32px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 17px/26px 400 |
| Letter spacing | -0.22px |
| Colour | #474645 |
| Transition | none |
| How | at rest |

Crops: none.

#### post-back

Back link. The article’s back/index link if present; measured, never followed.

Page: blogpost. Selector: `back link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 149.76 x 38.4 | = | = | = |
| Padding | 9px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 6px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid color(display-p3 0.517647 0.509804 0.505882) offset 1px | = |
| Font | Inter 15px/normal 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | color(display-p3 0.203922 0.203922 0.2) | = | = | = |
| Text node | span.Typography__Paragraph-sc-p3xo6h-7.hAxgce: Inter 15px/22px 500, color(display-p3 0.203922 0.203922 0.2), ls -0.13px | = | = | = |
| Transition | all 0.2s ease-out | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.active 149.8x38.4 r 6px outline 2px solid color(display-p3 0.517647 0.509804 0.505882) offset 1px | = |

Crops: `post-back-hover.png`, `post-back-focus-visible.png`.

### Footer

#### site-footer

Site footer. The sitemap footer (Developers / Resources / Company, © 2026).

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1024 x 316 |
| Padding | 68px 0px 96px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/normal 400 |
| Letter spacing | normal |
| Colour | #707070 @ 0.4 |
| Text node | h5.Typography__Paragraph-sc-p3xo6h-7.deiBcl: Inter 13px/18px 500, #121212, ls -0.13px |
| Transition | none |
| Icon | 60 x 62, colour color(display-p3 0.517647 0.509804 0.505882), fill #000000 |
| How | at rest |

Crops: `site-footer-default.png`.

### Changelog

#### cl-h1

Changelog title. The "Changelog" page title.

Page: changelog. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 222.91 x 48 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Family 44px/48px 500 |
| Letter spacing | -1.35px |
| Colour | #121212 |
| Text node | span: Family 44px/48px 500, #121212, ls -1.35px |
| Transition | none |
| How | at rest |

Crops: `cl-h1-default.png`.

#### cl-filter

Changelog filter. A filter button on /changelog (All / ConnectKit); measured, never pressed.

Page: changelog. Selector: `changelog filter button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 43 x 33.38 | = | = | = |
| Padding | 7.2px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 32px | = | = | = |
| Background | color(display-p3 0.917647 0.917647 0.917647) | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid color(display-p3 0.517647 0.509804 0.505882) offset 0px | = |
| Font | Inter 15px/normal 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | color(display-p3 0.203922 0.203922 0.2) | = | = | = |
| Transition | transform, color, background 0.2s ease | = | none | transform, color, background 0.1s ease |
| Cursor | pointer | = | = | = |
| Painted layers | button.Filters__Button-sc-ef5306-1.hrdrRW 43.0x33.4 bg color(display-p3 0.917647 0.917647 0.917647) r 32px | = | button.Filters__Button-sc-ef5306-1.hrdrRW 43.0x33.4 bg color(display-p3 0.917647 0.917647 0.917647) r 32px outline 2px solid color(display-p3 0.517647 0.509804 0.505882) offset 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `cl-filter-default.png`, `cl-filter-hover.png`, `cl-filter-focus-visible.png`, `cl-filter-pressed.png`.

#### cl-entry

Entry heading. A changelog entry heading ("Updated").

Page: changelog. Selector: `changelog h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 732 x 34 |
| Padding | 0px 0px 8px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 17px/26px 600 |
| Letter spacing | -0.22px |
| Colour | #121212 |
| Transition | none |
| How | at rest |

Crops: `cl-entry-default.png`.

#### cl-entry-body

Entry body. Changelog entry copy.

Page: changelog. Selector: `changelog entry paragraph`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 732 x 84 |
| Padding | 0px 0px 32px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 17px/26px 400 |
| Letter spacing | -0.22px |
| Colour | #474645 |
| Transition | none |
| How | at rest |

Crops: `cl-entry-body-default.png`.

### Help and support

#### sup-h1

Support title. The "Help & Support" page title.

Page: support. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 300.11 x 48 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Family 44px/48px 500 |
| Letter spacing | -1.35px |
| Colour | #121212 |
| Transition | none |
| How | at rest |

Crops: `sup-h1-default.png`.

#### sup-search

Support search. The "Search Help & Support" field; typed into then cleared, never submitted.

Page: support. Selector: `support search input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 269 x 36 | = | = |
| Padding | 10px 15px 9px 34px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Inter 14px/normal 500 | = | = |
| Letter spacing | -0.13008px | = | = |
| Colour | #373737 | = | = |
| Transition | none | = | = |
| Cursor | text | = | wait |
| Placeholder | #373737 @ 0.3, opacity 1 | = | = |
| Ancestor paint | 1 up div.styles__InputContainer-sc-cr4yjr-2.eFpyTu bg #ffffff shadow #eaeaea 0px 0px 0px 1px inset | 1 up div.styles__InputContainer-sc-cr4yjr-2.eFpyTu bg #ffffff shadow #b3b3b3 0px 0px 0px 1px inset | 1 up div.styles__InputContainer-sc-cr4yjr-2.eFpyTu bg #ffffff shadow #b3b3b3 0px 0px 0px 1px inset |
| How | at rest | clicked into the field | typed "recover my wallet", then deleted; nothing sent |

Crops: `sup-search-default.png`, `sup-search-focused.png`, `sup-search-filled.png`.

#### sup-category

Category button. A help-category button ("Ethereum 101", "Getting Started with Family"); measured, never followed.

Page: support. Selector: `support category`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 240 x 29.92 | = | = | = |
| Padding | 10px 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 14px/normal 400 | Inter 14px/normal 500 | = | Inter 14px/normal 500 |
| Letter spacing | -0.09008px | = | = | = |
| Colour | #848281 | #4e5360 | = | #4e5360 |
| Text node | span.sc-aXZVg.gJAfGz: Inter 14px/22px 400, #848281, ls -0.09008px | span.sc-aXZVg.gJAfGz: Inter 14px/22px 500, #4e5360, ls -0.09008px | = | span.sc-aXZVg.gJAfGz: Inter 14px/22px 500, #4e5360, ls -0.09008px |
| Transition | all 0.08s ease-out | all 0.18s ease-out | = | all 0.18s ease-out |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `sup-category-default.png`, `sup-category-hover.png`, `sup-category-focus-visible.png`, `sup-category-pressed.png`.

#### sup-article-link

Article link. A help-article link; measured, never followed.

Page: support. Selector: `a[href^=/support/]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 224 x 29.92 | = | = | = |
| Padding | 10px 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 14px/normal 400 | = | Inter 14px/normal 500 | Inter 14px/normal 500 |
| Letter spacing | -0.09008px | = | = | = |
| Colour | #848281 | = | #4e5360 | #121212 |
| Text node | span.sc-aXZVg.gJAfGz: Inter 14px/22px 400, #848281, ls -0.09008px | = | span.sc-aXZVg.gJAfGz: Inter 14px/22px 500, #4e5360, ls -0.09008px | span.sc-aXZVg.gJAfGz: Inter 14px/22px 500, #121212, ls -0.09008px |
| Transition | all 0.08s ease-out | = | all 0.18s ease-out | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `sup-article-link-default.png`, `sup-article-link-hover.png`, `sup-article-link-focus-visible.png`, `sup-article-link-pressed.png`.

#### art-h1

Article title. The help-article title ("Import a wallet from MetaMask").

Page: supportart. Selector: `article h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 620.86 x 48 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Family 44px/48px 500 |
| Letter spacing | -1.35px |
| Colour | #121212 |
| Transition | none |
| How | at rest |

Crops: `art-h1-default.png`.

#### art-h2

Article heading. A "How to" section heading inside the help article.

Page: supportart. Selector: `article h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 704 x 27 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 19px/27px 500 |
| Letter spacing | -0.3px |
| Colour | #121212 |
| Transition | none |
| How | at rest |

Crops: `art-h2-default.png`.

#### art-body

Article body. Help-article body copy.

Page: supportart. Selector: `article p/li`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 704 x 136 |
| Padding | 0px 0px 32px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 17px/26px 400 |
| Letter spacing | -0.22px |
| Colour | #474645 |
| Transition | none |
| How | at rest |

Crops: `art-body-default.png`.

#### art-side-link

Side-nav link. A related-category/article link beside the article; measured, never followed.

Page: supportart. Selector: `a[href^=/support/]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 224 x 29.92 | = | = | = |
| Padding | 10px 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 14px/normal 400 | = | Inter 14px/normal 500 | Inter 14px/normal 500 |
| Letter spacing | -0.09008px | = | = | = |
| Colour | #848281 | = | #4e5360 | #121212 |
| Text node | span.sc-aXZVg.gJAfGz: Inter 14px/22px 400, #848281, ls -0.09008px | = | span.sc-aXZVg.gJAfGz: Inter 14px/22px 500, #4e5360, ls -0.09008px | span.sc-aXZVg.gJAfGz: Inter 14px/22px 500, #121212, ls -0.09008px |
| Transition | all 0.08s ease-out | = | all 0.18s ease-out | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `art-side-link-default.png`, `art-side-link-hover.png`, `art-side-link-focus-visible.png`, `art-side-link-pressed.png`.

#### faq-h1

FAQs title. The "FAQs" page title.

Page: faqs. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 104.63 x 48 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Family 44px/48px 500 |
| Letter spacing | -1.35px |
| Colour | #121212 |
| Text node | span: Family 44px/48px 500, #121212, ls -1.35px |
| Transition | none |
| How | at rest |

Crops: `faq-h1-default.png`.

### Docs pages

#### legal-h1

Legal title. The "Legal" page title.

Page: legal. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 109.28 x 48 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Family 44px/48px 500 |
| Letter spacing | -1.35px |
| Colour | #121212 |
| Text node | span: Family 44px/48px 500, #121212, ls -1.35px |
| Transition | none |
| How | at rest |

Crops: `legal-h1-default.png`.

#### legal-section

Legal section. A legal section link (Family App / Sweepstakes / privacy / terms); measured, never followed.

Page: legal. Selector: `legal section`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 212 x 30.59 | = | = | = |
| Padding | 4.8px 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 16px/normal 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #018dff | = | = | = |
| Text node | span.Typography__Paragraph-sc-p3xo6h-7.idDTlz: Inter 14px/20px 400, #018dff, ls -0.09px | = | = | = |
| Transition | all 0.2s ease-out | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.75 | = | 0.75 |

Crops: `legal-section-default.png`, `legal-section-hover.png`, `legal-section-focus-visible.png`, `legal-section-pressed.png`.

#### docs-h1

Docs title. The "Getting Started" docs title.

Page: docs. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 710 x 22.67 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 32px/28.64px 600 |
| Letter spacing | -0.45px |
| Colour | #343433 |
| Transition | none |
| ::before | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| ::after | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| How | at rest |

Crops: `docs-h1-default.png`.

#### docs-body

Docs body. Docs body copy.

Page: docs. Selector: `docs body`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 212.19 x 19.2 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/20px 400 |
| Letter spacing | -0.09px |
| Colour | #848281 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `docs-body-default.png`.

#### ck-h1

ConnectKit title. The "ConnectKit 1.9.1" docs title.

Page: connectkit. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 710 x 24.5 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 32px/40px 600 |
| Letter spacing | -0.45px |
| Colour | #343433 |
| Transition | none |
| ::before | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| ::after | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| Painted layers | span.Tag__Container-sc-1f7fvlr-0.jUrfYZ 41.8x24.0 bg #fafafa r 6px |
| How | at rest |

Crops: `ck-h1-default.png`.

#### ck-h2

Docs heading. A section heading on the ConnectKit doc page.

Page: connectkit. Selector: `docs h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 710 x 14.17 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 20px/22.67px 500 |
| Letter spacing | -0.28px |
| Colour | #343433 |
| Transition | none |
| ::before | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| ::after | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| How | at rest |

Crops: `ck-h2-default.png`.

#### ck-cta

Docs CTA. A docs action button ("Stay Updated" / "Contact Us"); measured, never pressed.

Page: connectkit. Selector: `docs CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 116 x 32 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 16px/normal 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #474645 | = | = | = |
| Text node | span.sc-aXZVg.gJAfGz: Inter 14px/22px 500, #ffffff | = | = | = |
| Transition | all 0.2s ease-out | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.sc-dAlyuH.DTESE 116.0x32.0 bg #343433 r 6px shadow #000000 @ 0 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px | button.sc-dAlyuH.DTESE 116.0x32.0 bg #171717 r 6px shadow #000000 @ 0 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `ck-cta-default.png`, `ck-cta-hover.png`, `ck-cta-focus-visible.png`, `ck-cta-pressed.png`.

#### acct-h1

Family doc title. The "Family" docs title (the Family account doc).

Page: account. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 710 x 24.5 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 32px/40px 600 |
| Letter spacing | -0.45px |
| Colour | #343433 |
| Transition | none |
| ::before | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| ::after | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| How | at rest |

Crops: `acct-h1-default.png`.

### App login (app.family.co)

#### login-card

Login card. The Aave Account login card on app.family.co — the container holding the welcome text and the field; at rest, never submitted.

Page: login. Selector: `login card container`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 380 x 284 |
| Padding | 0px |
| Gap | 24px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | inter 16px/normal 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Text node | h1: inter 18px/19px 600, #222222, ls -0.13px |
| Transition | none |
| Icon | 58 x 30, colour #222222 |
| Painted layers | div.styles-module-scss-module__EkH3Mq__inputContainer 380.0x48.0 bg #f6f7f9 r 14px shadow #000000 @ 0 0px 0px 0px 1px inset |
| How | at rest |

Crops: `login-card-default.png`.

#### login-h1

Login title. "Welcome to Aave Account" — the login heading (Family Accounts is now Aave Account).

Page: login. Selector: `login h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 380 x 19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | inter 18px/19px 600 |
| Letter spacing | -0.13px |
| Colour | #222222 |
| Transition | none |
| How | at rest |

Crops: `login-h1-default.png`.

#### login-sub

Login subline. "Log in or sign up to get started. We’ll create an account if you don’t have one yet."

Page: login. Selector: `login subline`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 380 x 19 |
| Padding | 0px |
| Gap | 4px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | inter 16px/19px 400 |
| Letter spacing | -0.13px |
| Colour | #171717 @ 0.5 |
| Transition | none |
| How | at rest |

Crops: `login-sub-default.png`.

#### login-field

Email/phone field. The "Email or Phone Number" login field; typed into then cleared, never submitted.

Page: login. Selector: `#email-or-number`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 380 x 48 | = | = |
| Padding | 15px 16.96px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | inter 16px/18px 500 | = | = |
| Letter spacing | -0.13px | = | = |
| Colour | #171717 | = | = |
| Transition | opacity 0.3s ease | = | = |
| Cursor | text | = | = |
| Placeholder | #171717 @ 0.2, opacity 1 | = | = |
| Ancestor paint | 2 up div.styles-module-scss-module__EkH3Mq__inputContainer bg #f6f7f9 shadow #000000 @ 0 0px 0px 0px 1px inset | 2 up div.styles-module-scss-module__EkH3Mq__inputContainer bg #f6f7f9 shadow color(display-p3 0.596078 0.588235 1) 0px 0px 0px 2px inset | 2 up div.styles-module-scss-module__EkH3Mq__inputContainer bg #f6f7f9 shadow color(display-p3 0.596078 0.588235 1) 0px 0px 0px 2px inset |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `login-field-default.png`, `login-field-focused.png`, `login-field-filled.png`.

#### login-learn

Learn More link. The "Learn More" link under the rebrand note; measured, never followed.

Page: login. Selector: `Learn More`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 135.44 x 32 | = | = | = |
| Padding | 7px 16px 7px 16.736px | = | = | = |
| Gap | 5.6px | = | = | = |
| Border | none | = | = | = |
| Radius | 18px | = | = | = |
| Background | color(display-p3 0.9765 0.9686 0.9608) | #f5f2ef | = | #f5f2ef |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #007aff @ 0.5 offset 1px | = |
| Font | inter 14px/normal 500 | = | = | = |
| Letter spacing | -0.09008px | = | = | = |
| Colour | color(display-p3 0.0706 0.0706 0.0706) | = | = | = |
| Text node | span: inter 14px/normal 500, color(display-p3 0.0706 0.0706 0.0706), ls -0.09008px | = | = | = |
| Transition | background 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 18 x 18, colour color(display-p3 0.0706 0.0706 0.0706) | = | = | = |
| Painted layers | a 135.4x32.0 bg color(display-p3 0.9765 0.9686 0.9608) r 18px | a 135.4x32.0 bg #f5f2ef r 18px | a 135.4x32.0 bg color(display-p3 0.9765 0.9686 0.9608) r 18px outline 2px solid #007aff @ 0.5 offset 1px | a 135.4x32.0 bg #f5f2ef r 18px |
| Ancestor paint | 1 up div.styles-module-scss-module__Tt6TIW__wrapper bg #ffffff | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `login-learn-default.png`, `login-learn-hover.png`, `login-learn-focus-visible.png`, `login-learn-pressed.png`.

#### login-footer-link

Login footer link. A footer link on the login page (Developers / Privacy / Terms); measured, never followed.

Page: login. Selector: `login footer link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 69.7 x 16 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #007aff @ 0.5 offset 1px | = |
| Font | inter 13px/normal 400 | = | = | = |
| Letter spacing | -0.13008px | = | = | = |
| Colour | #171717 @ 0.5 | #111111 | = | #111111 |
| Transition | color 0.1s ease | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a 69.7x16.0 outline 2px solid #007aff @ 0.5 offset 1px | = |

Crops: `login-footer-link-default.png`, `login-footer-link-hover.png`, `login-footer-link-focus-visible.png`, `login-footer-link-pressed.png`.

### Mobile (390 wide)

#### m-header

Mobile header. The phone top bar: wordmark, menu button and the Get Started pill.

Page: mobile. Selector: `mobile header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 342 x 70 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/normal 400 |
| Letter spacing | normal |
| Colour | #474645 |
| Text node | button.Button__Container-sc-1jjqbrw-0.fnjIlG: Inter 15px/normal 500, #ffffff, ls -0.09px |
| Transition | none |
| Transform | matrix3d(1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1) |
| Icon | 72 x 18, colour #262626 |
| Painted layers | a 0.0x0.0 bg #ffffff r 6px; div.Nav__DropdownContainer-sc-141m4ur-3.jmGeWm 0.0x0.0 bg #ffffff r 8px shadow #000000 @ 0.1 0px 3px 16px 0px; div.Nav__IconContainer-sc-141m4ur-2.jhkKsN 0.0x0.0 bg #ffffff r 9.6px shadow #000000 @ 0.04 0px 0px 0px 1px; div.Nav__IconContainer-sc-141m4ur-2.jhkKsN 0.0x0.0 bg #ffffff r 9.6px shadow #000000 @ 0.04 0px 0px 0px 1px; a 0.0x0.0 bg #ffffff r 6px; div.Nav__DropdownContainer-sc-141m4ur-3.jmGeWm 0.0x0.0 bg #ffffff r 8px shadow #000000 @ 0.1 0px 3px 16px 0px |
| How | at rest |

Crops: `m-header-default.png`.

#### m-menu

Mobile menu button. The hamburger that opens the mobile nav drawer; measured, its press is a local toggle.

Page: mobile. Selector: `Nav__MenuButton`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 13.3333px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | default | = | = | = |
| Painted layers | button.Nav__MenuButton-sc-141m4ur-7.fMLkQg 32.0x32.0 bg #ffffff r 8px; div::before.Nav__Hamburger-sc-141m4ur-6.iVRvzB 14pxx2px bg color(display-p3 0.203922 0.203922 0.2) r 2px; div::after.Nav__Hamburger-sc-141m4ur-6.iVRvzB 14pxx2px bg color(display-p3 0.203922 0.203922 0.2) r 2px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-menu-default.png`, `m-menu-hover.png`, `m-menu-focus-visible.png`, `m-menu-pressed.png`.

#### m-h1

Mobile headline. The phone hero heading.

Page: mobile. Selector: `mobile h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 342 x 112 |
| Padding | 0px 0px 16px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Family 44px/48px 500 |
| Letter spacing | -1.35px |
| Colour | color(display-p3 0.203922 0.203922 0.2) |
| Text node | span: Family 44px/48px 500, color(display-p3 0.203922 0.203922 0.2), ls -1.35px |
| Transition | none |
| How | at rest |

Crops: `m-h1-default.png`.

#### m-download

Mobile download CTA. The "Download on iOS" pill on the phone hero; measured, never followed.

Page: mobile. Selector: `mobile Download on iOS`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 209.7 x 48 | = | = | = |
| Padding | 0px 24px 0px 22px | = | = | = |
| Gap | 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 32px | = | = | = |
| Background | #171717 | #121212 | = | #121212 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 17px/17px 500 | = | = | = |
| Letter spacing | -0.22px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color 0.1s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 20, colour #ffffff | = | = | = |
| Painted layers | a.SectionIntro__Button-sc-1nhl813-4.dQyCQZ 209.7x48.0 bg #171717 r 32px | a.SectionIntro__Button-sc-1nhl813-4.dQyCQZ 209.7x48.0 bg #121212 r 32px | = | a.SectionIntro__Button-sc-1nhl813-4.dQyCQZ 209.7x48.0 bg #121212 r 32px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-download-default.png`, `m-download-hover.png`, `m-download-focus-visible.png`, `m-download-pressed.png`.

#### m-faq-item

Mobile FAQ item. A collapsible FAQ item at 390 wide.

Page: mobile. Selector: `mobile FAQ item`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 342 x 56 |
| Padding | 0px 0px 28px 0px |
| Gap | 24px |
| Border | T: none; R: none; B: 1px solid color(display-p3 0.94902 0.941176 0.929412); L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/normal 400 |
| Letter spacing | normal |
| Colour | #474645 |
| Text node | h4.Typography__Paragraph-sc-p3xo6h-7.eHgZom: Inter 19px/27px 500, #121212, ls -0.3px |
| Transition | none |
| Painted layers | div.Item__StyledCollapsableItem-sc-bjycf3-2.egfBPj 342.0x56.0 border B:1px solid color(display-p3 0.94902 0.941176 0.929412); div 14.0x2.0 bg color(display-p3 1 0.32549 0.0627451) r 2px; div 2.0x14.0 bg color(display-p3 1 0.32549 0.0627451) r 2px; a::after 132.266pxx2px bg #1a88f8 r 2px |
| How | at rest |

Crops: `m-faq-item-default.png`.

#### m-footer

Mobile footer. The phone footer.

Page: mobile. Selector: `mobile footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 342 x 504.88 |
| Padding | 24px 0px 48px 0px |
| Gap | 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/normal 400 |
| Letter spacing | normal |
| Colour | #707070 @ 0.4 |
| Text node | h5.Typography__Paragraph-sc-p3xo6h-7.deiBcl: Inter 13px/18px 500, #121212, ls -0.13px |
| Transition | none |
| Icon | 16 x 16, colour #e4e4e4 |
| How | at rest |

Crops: `m-footer-default.png`.

## Transitions declared in the readable stylesheets

family.co and app.family.co serve their CSS same-origin, so this list holds the transitions the readable sheets declare on each page; the per-state Transition rows above are computed values and cover every rule the page paints.

- blog: `0.2s ease-out`, `color 140ms`, `none`, `inherit`, `background-color 100ms`, `transform 200ms`, `opacity 100ms, transform`, `background 200ms, color`, `background 100ms, transform`, `opacity 100ms`, `transform 200ms, color, background`

- blogpost: `100ms`, `0.2s ease-out`, `color 140ms`, `none`, `inherit`, `background-color 100ms`, `transform 200ms`, `opacity 100ms, transform`, `background 200ms, color`, `opacity 220ms ease-out`, `background 100ms, transform`, `opacity 100ms`

- changelog: `transform 220ms cubic-bezier(0.19, 1, 0.22, 1)`, `opacity 100ms ease-in-out`, `opacity 200ms ease-in-out`, `0.2s ease-out`, `color 140ms`, `none`, `inherit`, `background-color 100ms`, `transform 200ms`, `opacity 100ms, transform`, `background 200ms, color`, `background 100ms, transform`

- connectkit: `inherit`, `transform 220ms cubic-bezier(0.19, 1, 0.22, 1)`, `opacity 100ms ease-in-out`, `opacity 200ms ease-in-out`, `100ms`, `0.2s ease-out`, `color 140ms`, `none`, `background-color 100ms`, `opacity 300ms ease-in-out, transform`, `opacity 300ms ease-in-out 400ms, left, top`, `transform 200ms`

- docs: `inherit`, `0.2s ease-out`, `color 140ms`, `none`, `background-color 100ms`, `opacity 300ms ease-in-out, transform`, `opacity 300ms ease-in-out 400ms, left, top`, `transform 200ms`, `opacity 100ms, transform`, `background 200ms, color`, `220ms cubic-bezier(0.19, 1, 0.22, 1)`, `80ms ease-out`

- faqs: `0.2s ease-out`, `color 140ms`, `none`, `inherit`, `background-color 100ms`, `transform 200ms`, `opacity 100ms, transform`, `background 200ms, color`, `background 100ms, transform`, `opacity 100ms`

- home: `transform 220ms cubic-bezier(0.19, 1, 0.22, 1)`, `opacity 100ms ease-in-out`, `opacity 200ms ease-in-out`, `0.2s ease-out`, `color 140ms`, `none`, `inherit`, `background-color 100ms`, `transform 200ms`, `opacity 100ms, transform`, `background 200ms, color`, `background 100ms, transform`

- login: `transform .2s var(--ease-snappy-out)`, `all .1s var(--ease-snappy-out)`, `none`, `opacity .2s var(--ease-snappy-out)`, `color 0.1s`, `opacity 0.3s`, `background 0.6s cubic-bezier(0, 0, 0.2, 1), box-shadow 0.6s cubic-bezier(0, 0, 0.2, 1), color 0.6s cubic-bezier(0, 0, 0.2, 1)`, `opacity 0.1s`, `background 0.6s, box-shadow 0.6s`, `0.2s`, `opacity 0.2s, transform 0.2s`, `inherit`

- support: `0.2s ease-out`, `color 140ms`, `none`, `inherit`, `background-color 100ms`, `transform 200ms`, `opacity 100ms, transform`, `background 200ms, color`, `220ms cubic-bezier(0.19, 1, 0.22, 1)`, `80ms ease-out`, `background 100ms, box-shadow`, `200ms`

- supportart: `0.2s ease-out`, `color 140ms`, `none`, `inherit`, `background-color 100ms`, `transform 200ms`, `opacity 100ms, transform`, `background 200ms, color`, `opacity 220ms ease-out`, `220ms cubic-bezier(0.19, 1, 0.22, 1)`, `80ms ease-out`, `background 100ms, box-shadow`
