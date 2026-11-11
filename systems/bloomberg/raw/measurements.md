# Component measurements

Computed styles read from bloomberg.com on 2026-11-10 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) in the site's one light theme, with the media-ui privacy-preferences modal hidden after measurement (never answered), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### privacy-dialog

Privacy preferences modal. The consent/preferences card every front page mounts. Measured as it arrives, then hidden; no checkbox or button was ever answered.

Page: home. Selector: `[class*="media-ui-Privacy_wrapper"]`. States: .

Not found on the page at capture time.

#### privacy-checkbox

Privacy checkbox.

Page: home. Selector: `checkbox inside the privacy modal`. States: .

Not found on the page at capture time.

#### privacy-button

Privacy modal button. The modal’s own button, states only — a real click would answer the prompt, which never happens.

Page: home. Selector: `privacy modal button`. States: .

Not found on the page at capture time.

#### utility-bar

Utility bar. The thin top strip: "Bloomberg the Company & Its Products", Terminal demo, Anywhere login, customer support.

Page: home. Selector: `nav.bb-that`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 30 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | AvenirNextPForBBG 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | a.bb-that__skip-to-content: AvenirNextPForBBG 15px/22.5px 400, #f3f4ef |
| Transition | none |
| Painted layers | a.bb-that__skip-to-content 20.0x1.0 bg #000000; a.bb-that-header__link 219.5x12.0 border L:1px solid #b3b3b3; a.bb-that-header__link 239.2x16.0 border L:1px solid #b3b3b3; a.bb-that-header__link 188.5x12.0 border L:1px solid #b3b3b3; section.bb-that-category 327.2x231.0 bg #141414; section.bb-that-category 327.2x193.7 bg #141414 |
| Ancestor paint | 1 up div bg #000000 |
| How | at rest |

Crops: `utility-bar-default.png`.

#### utility-toggle

Company sitemap toggle. Opens the "Bloomberg the Company & Its Products" sitemap dropdown.

Page: home. Selector: `button:has-text("Bloomberg the Company")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 246.45 x 12 | = | = | = |
| Padding | 0px 27px 0px 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 2px | = |
| Font | AvenirNextPForBBG 12px/12px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #f3f4ef | = | = | = |
| Text node | span: AvenirNextPForBBG 12px/12px 600, #f3f4ef | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 9px x 9px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.bb-that-header__link.bb-that-header--sitemap-trigger 246.5x12.0 outline 1px auto #005fcc offset 2px | = |

Crops: `utility-toggle-default.png`, `utility-toggle-hover.png`, `utility-toggle-focus-visible.png`, `utility-toggle-pressed.png`.

#### utility-toggle-open

Company sitemap, open. The toggle after its own press; the dropdown shows in the crop of the opened panel.

Page: home. Selector: `button:has-text("Bloomberg the Company")`. States: opened.

| Property | opened |
|---|---|
| Error | toggle refused: A "Bloomberg the Company & Its Products" |

Crops: none.

#### logo-bar

Logo bar. The black bar: wordmark, Sign In, Subscribe, search.

Page: home. Selector: `[class*="nav-ui-LogoBar__bar"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1326 x 52 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | BWHaasGroteskWeb 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | button.nav-ui-LogoBar__signInButton__TG9nb: BWHaasGroteskWeb 14px/21px 500, #ffffff, ls 0.2px |
| Transition | none |
| Icon | 211 x 42, colour #ffffff |
| Painted layers | div.nav-ui-Logo__logo__TG9nb.nav-ui-Logo__dark__TG9nb 211.0x42.0 bg #000000; button.nav-ui-LogoBar__signInButton__TG9nb 66.8x30.0 bg #000000; a.nav-ui-LogoBar__subscribeButton__TG9nb 91.2x30.0 bg #ffffff border T:1px solid #767676 / R:1px solid #767676 / B:1px solid #767676 / L:1px solid #767676 r 4px; div.nav-ui-LogoBar__search__TG9nb 1440.0x0.0 bg #1c1c1c |
| Ancestor paint | 1 up div.nav-ui-LogoBar__logoBarContainer__TG9nb.nav-ui-LogoBar__dark__TG9nb bg #000000 |
| How | at rest |

Crops: `logo-bar-default.png`.

#### logo

Logo.

Page: home. Selector: `a[class*="nav-ui-Logo__logo"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 211 x 42 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | BWHaasGroteskWeb 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| Cursor | pointer |
| Icon | 211 x 42, colour #ffffff |
| Ancestor paint | 1 up div.nav-ui-Logo__logo__TG9nb.nav-ui-Logo__dark__TG9nb bg #000000 |
| How | at rest |

Crops: `logo-default.png`.

#### signin-button

Sign In button. Opens the sign-in sheet; never a real sign-in.

Page: home. Selector: `button:has-text("Sign In")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 66.77 x 30 | = | = | = |
| Padding | 6px 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | #000000 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | BWHaasGroteskWeb 14px/21px 500 | = | = | = |
| Letter spacing | 0.2px | = | = | = |
| Colour | #ffffff | #cccccc | = | #cccccc |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.nav-ui-LogoBar__signInButton__TG9nb 66.8x30.0 bg #000000 | = | button.nav-ui-LogoBar__signInButton__TG9nb 66.8x30.0 bg #000000 outline 1px auto #005fcc offset 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signin-button-default.png`, `signin-button-hover.png`, `signin-button-focus-visible.png`, `signin-button-pressed.png`.

#### subscribe-nav

Subscribe button. The white Subscribe CTA in the logo bar. Measured, never followed.

Page: home. Selector: `a[class*="subscribeButton"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 91.16 x 30 | = | = | = |
| Padding | 6px 10px | = | = | = |
| Border | 1px solid #767676 | = | = | = |
| Radius | 4px | = | = | = |
| Background | #ffffff | #1c1c1c | = | #1c1c1c |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | BWHaasGroteskWeb 14px/21px 500 | = | = | = |
| Letter spacing | 0.2px | = | = | = |
| Colour | #000000 | #ffffff | = | #ffffff |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.nav-ui-LogoBar__subscribeButton__TG9nb 91.2x30.0 bg #ffffff border T:1px solid #767676 / R:1px solid #767676 / B:1px solid #767676 / L:1px solid #767676 r 4px | a.nav-ui-LogoBar__subscribeButton__TG9nb 91.2x30.0 bg #1c1c1c border T:1px solid #767676 / R:1px solid #767676 / B:1px solid #767676 / L:1px solid #767676 r 4px | a.nav-ui-LogoBar__subscribeButton__TG9nb 91.2x30.0 bg #ffffff border T:1px solid #767676 / R:1px solid #767676 / B:1px solid #767676 / L:1px solid #767676 r 4px outline 1px auto #005fcc offset 1px | a.nav-ui-LogoBar__subscribeButton__TG9nb 91.2x30.0 bg #1c1c1c border T:1px solid #767676 / R:1px solid #767676 / B:1px solid #767676 / L:1px solid #767676 r 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `subscribe-nav-default.png`, `subscribe-nav-hover.png`, `subscribe-nav-focus-visible.png`, `subscribe-nav-pressed.png`.

#### search-button

Search button.

Page: home. Selector: `nav search control`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 28 x 28 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | BWHaasGroteskWeb 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | #cccccc | = | #cccccc |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #ffffff | 24 x 24, colour #cccccc | = | 24 x 24, colour #cccccc |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.nav-ui-LogoBar__searchButton__TG9nb 28.0x28.0 outline 1px auto #005fcc offset 0px | = |

Crops: `search-button-default.png`, `search-button-hover.png`, `search-button-focus-visible.png`, `search-button-pressed.png`.

#### section-nav

Section nav. The strip under the logo bar: Live TV, Markets, Finance, Economics …

Page: home. Selector: `[class*="nav-ui-Nav"]`. States: .

Not found on the page at capture time.

#### nav-link

Section link.

Page: home. Selector: `section nav a:has-text("Economics")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 75.34 x 21 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | BWHaasGroteskWeb 14px/21px 500 | = | = | = |
| Letter spacing | 0.2px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a 75.3x21.0 outline 1px auto #005fcc offset 1px | = |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### nav-dropdown

Nav dropdown. A chevron item in the section nav; opens a subnav list.

Page: home. Selector: `nav button:has-text("More")`. States: .

Not found on the page at capture time.

#### nav-dropdown-open

Nav dropdown, open. After its own toggle; the opened list shows in the crop.

Page: home. Selector: `nav button:has-text("More")`. States: .

Not found on the page at capture time.

#### edition-select

Edition selector.

Page: home. Selector: `button:has-text("Edition")`. States: .

Not found on the page at capture time.

#### signin-sheet

Sign-in sheet. The /account/iframe/login sheet the Sign In button mounts. Opened and left; never used.

Page: home. Selector: `iframe[src*="/account/iframe/login"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 700 x 675 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | #000000 @ 0.3 0px 0px 5px 0px |
| Outline | none |
| Font | BWHaasGroteskWeb 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Painted layers | div.reg-ui-client__uverify-iframe-container 700.0x675.0 bg #ffffff shadow #000000 @ 0.3 0px 0px 5px 0px |
| Ancestor paint | 1 up div.reg-ui-client bg #ffffff @ 0.9 |
| How | at rest |

Crops: `signin-sheet-default.png`.

#### signin-email

Sign-in email field. Inside the sign-in iframe. Focused only; nothing typed.

Page: home. Selector: `input inside the sign-in iframe`. States: .

Not found on the page at capture time.

#### signin-continue

Sign-in continue. The sheet’s submit, measured at rest and never pressed.

Page: home. Selector: `button inside the sign-in iframe`. States: .

Not found on the page at capture time.

### Home front

#### ticker-bar

Ticker bar. The securities strip: Top Securities plus index quotes.

Page: home. Selector: `[class*="TickerBar"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1326 x 55 |
| Padding | 0px 0px 1px 0px |
| Border | T: none; R: 1px solid #b3b3b3; B: 1px solid #b3b3b3; L: 1px solid #b3b3b3 |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | BWHaasGroteskWeb 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.media-ui-DropdownButton_text-5quqCVafbwY-: BWHaasGroteskWeb 14px/21px 500, #000000 |
| Transition | none |
| Icon | 16 x 16, colour #000000 |
| Painted layers | div.PhoenixTickerBarWrapper_tickerBarWrapper__2cAU2 1326.0x55.0 border R:1px solid #b3b3b3 / B:1px solid #b3b3b3 / L:1px solid #b3b3b3; div.media-ui-TickerBarWithPill_securities-QkJSeChnEgQ-.button-dropdown 165.4x53.0 shadow #000000 0px 0px 0px 0px; ul.media-ui-ButtonDropdown_menu-nTOQvv7qJHg- 0.0x0.0 bg #ffffff border T:1px solid #f8f8f8 / R:1px solid #f8f8f8 / B:1px solid #f8f8f8 / L:1px solid #f8f8f8 r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 1px 3px 0px, #000000 @ 0.1 0px 1px 2px -1px; ul.media-ui-ButtonDropdown_menu-nTOQvv7qJHg- 0.0x0.0 bg #ffffff border T:1px solid #f8f8f8 / R:1px solid #f8f8f8 / B:1px solid #f8f8f8 / L:1px solid #f8f8f8 r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 1px 3px 0px, #000000 @ 0.1 0px 1px 2px -1px; div.media-ui-SecurityPill_securityPill-tHtSdrlxcjI-.media-ui-SecurityPill_negative-3yJm-9q9Vkg- 201.7x31.5 bg #1c1c1c r 8px; div.media-ui-SecurityPill_securityPill-tHtSdrlxcjI-.media-ui-SecurityPill_negative-3yJm-9q9Vkg- 201.7x31.5 bg #1c1c1c r 8px |
| Ancestor paint | 1 up div.media-ui-LeaderboardAd_parallaxWrapper-JMVgdxR--aU- bg #ffffff |
| How | at rest |

Crops: `ticker-bar-default.png`.

#### ticker-item

Ticker quote. One index in the strip (S&P 500 and its change). Links to the quote page; measured, never followed.

Page: home. Selector: `a[class*="TickerBarWithPill_ticker"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 211.73 x 31.5 | = | = | = |
| Padding | 0px 10px 0px 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | BWHaasGroteskWeb 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.media-ui-SecurityPill_ticker-kNwKDByGgQM-: BWHaasGroteskWeb 14px/17.5px 500, #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 12 x 10, colour #f05143 | = | = | = |
| Painted layers | div.media-ui-SecurityPill_securityPill-tHtSdrlxcjI-.media-ui-SecurityPill_negative-3yJm-9q9Vkg- 201.7x31.5 bg #1c1c1c r 8px | = | a.media-ui-TickerBarWithPill_ticker-5arx5cdkyZQ- 211.7x31.5 outline 1px auto #005fcc offset 1px; div.media-ui-SecurityPill_securityPill-tHtSdrlxcjI-.media-ui-SecurityPill_negative-3yJm-9q9Vkg- 201.7x31.5 bg #1c1c1c r 8px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `ticker-item-default.png`, `ticker-item-hover.png`, `ticker-item-focus-visible.png`, `ticker-item-pressed.png`.

#### ticker-pill

Security pill.

Page: home. Selector: `[class*="SecurityPill"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 201.73 x 31.5 |
| Padding | 6px 8px 8px 8px |
| Gap | 0px |
| Border | none |
| Radius | 8px |
| Background | #1c1c1c |
| Box shadow | none |
| Outline | none |
| Font | BWHaasGroteskWeb 12px/18px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span.media-ui-SecurityPill_ticker-kNwKDByGgQM-: BWHaasGroteskWeb 14px/17.5px 500, #ffffff |
| Transition | none |
| Cursor | pointer |
| Icon | 12 x 10, colour #f05143 |
| Painted layers | div.media-ui-SecurityPill_securityPill-tHtSdrlxcjI-.media-ui-SecurityPill_negative-3yJm-9q9Vkg- 201.7x31.5 bg #1c1c1c r 8px |
| How | at rest |

Crops: `ticker-pill-default.png`.

#### hero-story

Lead story block. The top-story frame on the front page.

Page: home. Selector: `[class*="StoryBlock_storyBlock"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 459 x 109.56 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | BWHaasGroteskWeb 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span: BWHaasHead 32px/33.6px 500, #000000, ls 0.48px |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `hero-story-default.png`.

#### hero-headline

Lead headline. The big BWHaasGrotesk headline of the lead story.

Page: home. Selector: `[class*="Headline_phoenix"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 459 x 67.19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | BWHaasHead 32px/33.6px 500 |
| Letter spacing | 0.48px |
| Colour | #000000 |
| Text node | span: BWHaasHead 32px/33.6px 500, #000000, ls 0.48px |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `hero-headline-default.png`.

#### story-secondary

Secondary story. A smaller story block beside the lead.

Page: home. Selector: `[class*="StoryBlock_secondaryStory"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 333 x 38.38 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | BWHaasGroteskWeb 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span: BWHaasGroteskWeb 16px/19.2px 500, #000000 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `story-secondary-default.png`.

#### story-link

Story link. A headline link; measured, never followed.

Page: home. Selector: `a[class*="StoryBlock_storyLink"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 333 x 38.38 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | BWHaasGroteskWeb 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span: BWHaasGroteskWeb 16px/19.2px 500, #000000 | = | span: BWHaasGroteskWeb 16px/19.2px 500, #545454 | span: BWHaasGroteskWeb 16px/19.2px 500, #545454 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.StoryBlock_storyLink__5nXw8 333.0x38.4 outline 1px auto #005fcc offset 1px | = |

Crops: `story-link-default.png`, `story-link-hover.png`, `story-link-focus-visible.png`, `story-link-pressed.png`.

#### dek

Story dek. The summary paragraph under a headline.

Page: home. Selector: `[class*="Summary_summary"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 459 x 36.38 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | BWHaasGroteskWeb 14px/18.2px 400 |
| Letter spacing | normal |
| Colour | #3c3c3c |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `dek-default.png`.

#### section-title

Module title. A section header on the front (a topic or lane name).

Page: home. Selector: `h3[class*="ModuleHeader_title"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 48.42 x 19.19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | BWHaasGroteskWeb 16px/19.2px 700 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | a: BWHaasGroteskWeb 16px/19.2px 700, #000000 |
| Transition | none |
| How | at rest |

Crops: `section-title-default.png`.

#### subscriber-badge

Subscriber-only badge. The caps label marking paywalled stories.

Page: home. Selector: `[class*="subscriberOnlyLabel"]`. States: .

Not found on the page at capture time.

#### media-module

Media module. A video/story card in a topic lane.

Page: home. Selector: `[class*="LineupContentTopic_primaryStory"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 565 x 216.33 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | BWHaasGroteskWeb 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.styles_boldPrepend__40b8E: BWHaasGroteskWeb 10px/12px 500, #545454 |
| Transition | none |
| Icon | 0 x 0, colour #ffffff |
| Painted layers | div.video-js.vjs-paused 247.0x138.9 bg #000000; div.vjs-title-bar.vjs-hidden 0.0x0.0 image linear-gradient(#000000 @ 0.8 4.32%, #000000 @ 0 95.05%); div.vjs-loading-spinner 0.0x0.0 border T:8px solid #2b333f @ 0.7 / R:8px solid #2b333f @ 0.7 / B:8px solid #2b333f @ 0.7 / L:8px solid #2b333f @ 0.7 r 50%; div::before.vjs-loading-spinner 70pxx70px border T:8px solid #ffffff / R:8px solid #000000 @ 0 / B:8px solid #000000 @ 0 / L:8px solid #000000 @ 0 r 50%; div::after.vjs-loading-spinner 70pxx70px border T:8px solid #ffffff / R:8px solid #000000 @ 0 / B:8px solid #000000 @ 0 / L:8px solid #000000 @ 0 r 50%; div.vjs-control-bar 0.0x0.0 image linear-gradient(0deg, #000000 @ 0.8, #000000 @ 0 89.84%) |
| How | at rest |

Crops: `media-module-default.png`.

### Markets

#### markets-title

Markets title.

Page: markets. Selector: `h1`. States: .

Not found on the page at capture time.

#### index-card

Index card. A market index summary card.

Page: markets. Selector: `[class*="IndexCard"]`. States: .

Not found on the page at capture time.

#### quote-link

Quote link. A row linking a security’s quote page; measured, never followed.

Page: markets. Selector: `a[href*="/quote/"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 211.73 x 31.5 | = | = | = |
| Padding | 0px 10px 0px 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | BWHaasGroteskWeb 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.media-ui-SecurityPill_ticker-kNwKDByGgQM-: BWHaasGroteskWeb 14px/17.5px 500, #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 12 x 10, colour #f05143 | = | = | = |
| Painted layers | div.media-ui-SecurityPill_securityPill-tHtSdrlxcjI-.media-ui-SecurityPill_negative-3yJm-9q9Vkg- 201.7x31.5 bg #1c1c1c r 8px | div.media-ui-SecurityPill_securityPill-tHtSdrlxcjI-.media-ui-SecurityPill_negative-3yJm-9q9Vkg- 201.7x31.5 bg #3c3c3c r 8px | a.media-ui-TickerBarWithPill_ticker-5arx5cdkyZQ- 211.7x31.5 outline 1px auto #005fcc offset 1px; div.media-ui-SecurityPill_securityPill-tHtSdrlxcjI-.media-ui-SecurityPill_negative-3yJm-9q9Vkg- 201.7x31.5 bg #1c1c1c r 8px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `quote-link-default.png`, `quote-link-hover.png`, `quote-link-focus-visible.png`, `quote-link-pressed.png`.

#### market-tab

Market tab.

Page: markets. Selector: `tab/button naming a market board`. States: .

Not found on the page at capture time.

### Quote page

#### quote-title

Quote title. The index name and ticker (S&P 500 INDEX / SPX:IND).

Page: quote. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 618 x 72.39 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | BWHaasGroteskWeb 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | div.media-ui-SecurityName_securityName-WpFW87DcVnk-.media-ui-SecurityName_extraLarge-CPbNyHrfjZI-: BWHaasGroteskWeb 32px/38.4px 700, #000000 |
| Transition | none |
| Icon | 16 x 16, colour #ffffff |
| Painted layers | button.media-ui-RoundedToggleButton_RoundedToggleButton-jupSnVE3YEE-.media-ui-RoundedToggleButton_baseBackground-xtN1SsCKNUk- 113.0x31.0 bg #000000 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 9999px; button.media-ui-RoundedToggleButton_RoundedToggleButton-jupSnVE3YEE-.media-ui-RoundedToggleButton_baseBackground-xtN1SsCKNUk- 0.0x0.0 bg #000000 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 9999px |
| How | at rest |

Crops: `quote-title-default.png`.

#### follow-button

Follow button. The Follow toggle beside the title — a real press would need an account, so it was never pressed.

Page: quote. Selector: `button:has-text("Follow")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 113 x 31 | = | = | = |
| Padding | 4px 12px | = | = | = |
| Border | 1px solid #000000 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #000000 | = | = | #3c3c3c |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | BWHaasGroteskWeb 14px/21px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | div.media-ui-RoundedToggleButton_buttonText-iZD8r7vw2dA-: BWHaasGroteskWeb 14px/21px 500, #ffffff | = | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #ffffff | = | = | = |
| Painted layers | button.media-ui-RoundedToggleButton_RoundedToggleButton-jupSnVE3YEE-.media-ui-RoundedToggleButton_baseBackground-xtN1SsCKNUk- 113.0x31.0 bg #000000 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 9999px | = | button.media-ui-RoundedToggleButton_RoundedToggleButton-jupSnVE3YEE-.media-ui-RoundedToggleButton_baseBackground-xtN1SsCKNUk- 113.0x31.0 bg #000000 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 9999px outline 1px auto #005fcc offset 0px | button.media-ui-RoundedToggleButton_RoundedToggleButton-jupSnVE3YEE-.media-ui-RoundedToggleButton_baseBackground-xtN1SsCKNUk- 113.0x31.0 bg #3c3c3c border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 9999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `follow-button-default.png`, `follow-button-hover.png`, `follow-button-focus-visible.png`, `follow-button-pressed.png`.

#### quote-price

Last price.

Page: quote. Selector: `[class*="price" i]`. States: .

Not found on the page at capture time.

#### quote-change

Price change.

Page: quote. Selector: `[class*="change" i]`. States: .

Not found on the page at capture time.

#### quote-stat

Key stat. A key-statistics row (open, range, market cap).

Page: quote. Selector: `[class*="stat" i] / table tr`. States: .

Not found on the page at capture time.

### Live TV

#### live-player

Live player. The gated live-TV frame; the stream itself needs an account.

Page: live. Selector: `[class*="GatedLiveVideo"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1252 x 457.48 |
| Padding | 0px |
| Gap | 32px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | BWHaasGroteskWeb 16px/18.4px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | h2.ErrorDisplay-module__title___zRe0A: BWHaasGroteskWeb 20px/24px 500, #ffffff |
| Transition | gap 0.3s ease-in-out |
| Icon | 0 x 0, colour #ffffff |
| Painted layers | div.video-js.vjs-paused 813.3x457.5 bg #000000; div.vjs-title-bar.vjs-hidden 0.0x0.0 image linear-gradient(#000000 @ 0.8 4.32%, #000000 @ 0 95.05%); div.vjs-loading-spinner 0.0x0.0 border T:8px solid #2b333f @ 0.7 / R:8px solid #2b333f @ 0.7 / B:8px solid #2b333f @ 0.7 / L:8px solid #2b333f @ 0.7 r 50%; div::before.vjs-loading-spinner 70pxx70px border T:8px solid #ffffff / R:8px solid #000000 @ 0 / B:8px solid #000000 @ 0 / L:8px solid #000000 @ 0 r 50%; div::after.vjs-loading-spinner 70pxx70px border T:8px solid #ffffff / R:8px solid #000000 @ 0 / B:8px solid #000000 @ 0 / L:8px solid #000000 @ 0 r 50%; div.vjs-control-bar 0.0x0.0 image linear-gradient(0deg, #000000 @ 0.8, #000000 @ 0 89.84%) |
| How | at rest |

Crops: `live-player-default.png`.

#### live-paywall

Live paywall.

Page: live. Selector: `[class*="PaywallAnchor"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 813.33 x 457.48 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | BWHaasGroteskWeb 16px/18.4px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | h2.ErrorDisplay-module__title___zRe0A: BWHaasGroteskWeb 20px/24px 500, #ffffff |
| Transition | none |
| Icon | 0 x 0, colour #ffffff |
| Painted layers | div.video-js.vjs-paused 813.3x457.5 bg #000000; div.vjs-title-bar.vjs-hidden 0.0x0.0 image linear-gradient(#000000 @ 0.8 4.32%, #000000 @ 0 95.05%); div.vjs-loading-spinner 0.0x0.0 border T:8px solid #2b333f @ 0.7 / R:8px solid #2b333f @ 0.7 / B:8px solid #2b333f @ 0.7 / L:8px solid #2b333f @ 0.7 r 50%; div::before.vjs-loading-spinner 70pxx70px border T:8px solid #ffffff / R:8px solid #000000 @ 0 / B:8px solid #000000 @ 0 / L:8px solid #000000 @ 0 r 50%; div::after.vjs-loading-spinner 70pxx70px border T:8px solid #ffffff / R:8px solid #000000 @ 0 / B:8px solid #000000 @ 0 / L:8px solid #000000 @ 0 r 50%; div.vjs-control-bar 0.0x0.0 image linear-gradient(0deg, #000000 @ 0.8, #000000 @ 0 89.84%) |
| How | at rest |

Crops: `live-paywall-default.png`.

#### live-schedule

Schedule row.

Page: live. Selector: `schedule row`. States: .

Not found on the page at capture time.

### Subscription offers

#### offer-header

Offers header.

Page: subscriptions. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1254 x 30 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | AvenirNextPForBBG 12px/30px 600 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span: AvenirNextPForBBG 12px/12px 600, #f3f4ef |
| Transition | none |
| ::before | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| ::after | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| Painted layers | a.bb-that-header__link 219.5x12.0 border L:1px solid #b3b3b3; a.bb-that-header__link 239.2x16.0 border L:1px solid #b3b3b3; a.bb-that-header__link 188.5x12.0 border L:1px solid #b3b3b3 |
| How | at rest |

Crops: `offer-header-default.png`.

#### offer-hero

Offer hero. The lead WordPress offer block ("Get context beyond the headlines").

Page: subscriptions. Selector: `[class*="offers-header-block"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1290 x 512 |
| Padding | 16px 18px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24.8px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.offers-header-block-title: BW Haas Grotesk Web 40px/44px 700, #ffffff |
| Transition | none |
| Painted layers | div.wp-block-group.header-left-column 534.0x359.6 bg #000000; a.wp-ga-button.button-dark-theme 247.0x48.0 bg #3523ff r 8px |
| Ancestor paint | 1 up div.wp-block-group.alignfull bg #000000 |
| How | at rest |

Crops: `offer-hero-default.png`.

#### offer-price

Offer price.

Page: subscriptions. Selector: `[class*="price"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 372.75 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | BW Haas Grotesk Web 20px/24px 700 |
| Letter spacing | normal |
| Colour | #9ba2ff |
| Text node | s: BW Haas Grotesk Web 20px/24px 700, #808080 |
| Transition | none |
| How | at rest |

Crops: `offer-price-default.png`.

#### offer-cta

Offer CTA. The offer’s own action; links to checkout, measured, never followed.

Page: subscriptions. Selector: `a.wp-ga-button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 247 x 48 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 11.2px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | BW Haas Grotesk Web 16px/24.8px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | a.wp-ga-button.button-dark-theme: BW Haas Grotesk Web 16px/24.8px 500, #ffffff | = | = | = |
| Transition | none | = | = | = |
| Painted layers | a.wp-ga-button.button-dark-theme 247.0x48.0 bg #3523ff r 8px | a.wp-ga-button.button-dark-theme 247.0x48.0 bg #4f4fff r 8px | a.wp-ga-button.button-dark-theme 247.0x48.0 bg #3523ff r 8px outline 1px dotted #ffffff offset 2px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `offer-cta-default.png`, `offer-cta-hover.png`, `offer-cta-focus-visible.png`, `offer-cta-pressed.png`.

#### plan-card

Plan card. A rate-plan option block (billing choices).

Page: subscriptions. Selector: `[class*="rateplan-option-block"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 402 x 255.56 |
| Padding | 24px 0px |
| Border | 1px solid #b3b3b3 |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | BW Haas Grotesk Web 16px/19.2px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.rateplan-option-block-title: BW Haas Grotesk Web 20px/24px 500, #000000 |
| Transition | none |
| Painted layers | div.wp-block-payments-rateplan-option-block.rateplan-option-block 402.0x255.6 bg #ffffff border T:1px solid #b3b3b3 / R:1px solid #b3b3b3 / B:1px solid #b3b3b3 / L:1px solid #b3b3b3; a.wp-ga-button.button-light-theme 354.0x48.0 bg #ffffff border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 8px |
| How | at rest |

Crops: `plan-card-default.png`.

#### plan-cta

Plan CTA.

Page: subscriptions. Selector: `a.wp-ga-button:has-text("Choose")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 376 x 48 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 11.2px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | BW Haas Grotesk Web 16px/19.2px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | a.wp-ga-button.button-light-theme: BW Haas Grotesk Web 16px/19.2px 500, #000000 | = | = | = |
| Transition | none | = | = | = |
| Painted layers | a.wp-ga-button.button-light-theme 354.0x48.0 bg #ffffff border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 8px | a.wp-ga-button.button-light-theme 354.0x48.0 bg #efefef border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 8px | a.wp-ga-button.button-light-theme 354.0x48.0 bg #ffffff border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 8px outline 1px dotted #000000 offset 2px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `plan-cta-default.png`, `plan-cta-hover.png`, `plan-cta-focus-visible.png`, `plan-cta-pressed.png`.

### Article (paywalled)

#### article-kicker

Kicker. The section breadcrumb over the headline (Technology / AI).

Page: article. Selector: `[class*="Eyebrow"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 194 x 116.19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | BWHaasGroteskWeb 24px/28.8px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | a: BWHaasGroteskWeb 24px/28.8px 400, #000000 |
| Transition | none |
| How | at rest |

Crops: `article-kicker-default.png`.

#### article-headline

Article headline.

Page: article. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 777 x 88.19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | BWHaasGroteskWeb 42px/44.1px 700 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `article-headline-default.png`.

#### byline

Byline.

Page: article. Selector: `[class*="Byline"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 618 x 127.78 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | BWHaasGroteskWeb 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | div.ArticleByline_articleBylineAuthors__Y0EHu: BWHaasGroteskWeb 18px/21.6px 400, #000000 |
| Transition | none |
| Icon | 20 x 20, colour #000000 |
| Painted layers | button._bookmarksButton_1jxg5_1.outlined-button 87.0x30.0 bg #ffffff border T:1px solid #6b7280 / R:1px solid #6b7280 / B:1px solid #6b7280 / L:1px solid #6b7280 r 9999px; button.styles_readInEnglish__DG_5t.outlined-button 103.1x30.0 bg #ffffff border T:1px solid #6b7280 / R:1px solid #6b7280 / B:1px solid #6b7280 / L:1px solid #6b7280 r 9999px |
| How | at rest |

Crops: `byline-default.png`.

#### lede-media

Lede media. The lede image/video frame (the video itself errors headless).

Page: article. Selector: `[class*="BasicLede"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 618 x 399.63 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | BWHaasGroteskWeb 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h2.ErrorDisplay-module__title___zRe0A: BWHaasGroteskWeb 20px/24px 500, #ffffff |
| Transition | none |
| Icon | 0 x 0, colour #000000 |
| Painted layers | button.media-ui-IconButton_wrapper-ZtMlyZ3p34k-.media-ui-IconButton_outlined-z7c334w-V9s- 0.0x0.0 border T:1px solid #999999 / R:1px solid #999999 / B:1px solid #999999 / L:1px solid #999999 r 9999px; button::after.media-ui-IconButton_wrapper-ZtMlyZ3p34k-.media-ui-IconButton_outlined-z7c334w-V9s- autoxauto bg #000000; button.media-ui-IconButton_wrapper-ZtMlyZ3p34k-.media-ui-IconButton_outlined-z7c334w-V9s- 0.0x0.0 border T:1px solid #999999 / R:1px solid #999999 / B:1px solid #999999 / L:1px solid #999999 r 9999px; button::after.media-ui-IconButton_wrapper-ZtMlyZ3p34k-.media-ui-IconButton_outlined-z7c334w-V9s- autoxauto bg #000000; button.media-ui-IconButton_wrapper-ZtMlyZ3p34k-.media-ui-IconButton_outlined-z7c334w-V9s- 0.0x0.0 border T:1px solid #999999 / R:1px solid #999999 / B:1px solid #999999 / L:1px solid #999999 r 9999px; button::after.media-ui-IconButton_wrapper-ZtMlyZ3p34k-.media-ui-IconButton_outlined-z7c334w-V9s- autoxauto bg #000000 |
| How | at rest |

Crops: `lede-media-default.png`.

#### share-button

Share link.

Page: article. Selector: `share/social link`. States: .

Not found on the page at capture time.

#### topic-link

Topic link. A related-topic pill under the nav.

Page: article. Selector: `a:has-text("IPO Target")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 199.61 x 19 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | BWHaasGroteskWeb 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a 199.6x19.0 outline 1px auto #005fcc offset 1px | = |

Crops: `topic-link-default.png`, `topic-link-hover.png`, `topic-link-focus-visible.png`, `topic-link-pressed.png`.

#### paywall

Paywall fence. The "Get unlimited access" band that gates the article body. The boundary of the public capture: nothing past it is public.

Page: article. Selector: `[class*="paywall" i] / Claim-offer band`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 164.39 |
| Padding | 0px 16px 24px 16px |
| Border | none |
| Radius | 0px |
| Background | #1c1c1c |
| Box shadow | none |
| Outline | none |
| Font | BWHaasGroteskWeb 16px/18px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span._showOnDesktop_2jr69_31: BWHaasGroteskWeb 32px/32px 700, #ffffff |
| Transition | none |
| Painted layers | div._content_1ot87_155 1440.0x164.4 bg #1c1c1c; button.media-ui-Button_button-phoenix-D1e3y3-dPnA-.media-ui-Button_default-1-Rsg7503aw- 171.1x46.0 bg #ffffff r 8px |
| Ancestor paint | 1 up div._banner_1ot87_100._readyToFly_1ot87_109 bg #1c1c1c |
| How | at rest |

Crops: `paywall-default.png`.

#### claim-offer

Claim offer CTA. The paywall’s action; links to the offers page, measured, never followed.

Page: article. Selector: `:has-text("Claim This Offer")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 171.08 x 46 | = | = | = |
| Padding | 0px 24px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #ffffff | #efefef | = | #efefef |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | BWHaasGroteskWeb 16px/16px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | div.media-ui-Button_text-N76nbJyFyw0-.bb--button-text-inner: BWHaasGroteskWeb 16px/16px 500, #000000 | = | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.media-ui-Button_button-phoenix-D1e3y3-dPnA-.media-ui-Button_default-1-Rsg7503aw- 171.1x46.0 bg #ffffff r 8px | button.media-ui-Button_button-phoenix-D1e3y3-dPnA-.media-ui-Button_default-1-Rsg7503aw- 171.1x46.0 bg #efefef r 8px | button.media-ui-Button_button-phoenix-D1e3y3-dPnA-.media-ui-Button_default-1-Rsg7503aw- 171.1x46.0 bg #ffffff r 8px outline 1px auto #005fcc offset 0px | button.media-ui-Button_button-phoenix-D1e3y3-dPnA-.media-ui-Button_default-1-Rsg7503aw- 171.1x46.0 bg #efefef r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `claim-offer-default.png`, `claim-offer-hover.png`, `claim-offer-focus-visible.png`, `claim-offer-pressed.png`.

#### article-body

Body paragraph. A body-text paragraph; absent while the paywall holds.

Page: article. Selector: `article p`. States: .

Not found on the page at capture time.

### Footer

#### footer

Footer.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 605.52 x 21 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | BWHaasGroteskWeb 14px/21px 500 |
| Letter spacing | 0.2px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link.

Page: home. Selector: `footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 177 x 42 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | BWHaasGroteskWeb 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 211 x 42, colour #ffffff | = | = | = |
| Ancestor paint | 1 up div.nav-ui-Logo__logo__TG9nb.nav-ui-Logo__dark__TG9nb bg #1c1c1c | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.nav-ui-Logo__logo__TG9nb 177.0x42.0 outline 1px auto #005fcc offset 1px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

## Transitions declared in the readable stylesheets

bloomberg.com inlines its CSS-module sheets, so this list holds what the CSSOM could read on each page; the per-state Transition rows above are computed values and cover every rule the page paints.

- article: `transform 300ms ease-in-out`, `all var(--duration, '4000ms') ease`, `background-color 5000s ease-in-out`, `background 0.2s`, `opacity 500ms`, `border, background 300ms`, `border 300ms`, `0.25s ease-in-out`, `0.15s ease-in-out`, `opacity 0.1s ease-out, content 0.3s ease-in-out`, `opacity 0.1s ease-out`, `color 0.1s ease-out`

- home: `transform 300ms ease-in-out`, `all var(--duration, '4000ms') ease`, `background-color 5000s ease-in-out`, `background 0.2s`, `opacity 500ms`, `border, background 300ms`, `border 300ms`, `0.25s ease-in-out`, `0.15s ease-in-out`, `opacity 0.1s ease-out, content 0.3s ease-in-out`, `opacity 0.1s ease-out`, `color 0.1s ease-out`

- live: `transform 300ms ease-in-out`, `all var(--duration, '4000ms') ease`, `background-color 5000s ease-in-out`, `background 0.2s`, `opacity 500ms`, `border, background 300ms`, `border 300ms`, `0.25s ease-in-out`, `0.15s ease-in-out`, `opacity 0.1s ease-out, content 0.3s ease-in-out`, `opacity 0.1s ease-out`, `color 0.1s ease-out`

- markets: `0.25s ease-in-out`, `0.15s ease-in-out`, `opacity 0.1s ease-out, content 0.3s ease-in-out`, `opacity 0.1s ease-out`, `color 0.1s ease-out`, `0.6s ease-in-out`, `none`, `0.8s cubic-bezier(0, 1, 0.7, 1)`, `max-height 0.6s ease-in-out, visibility 0.6s ease-in-out`, `transform 0.35s`

- quote: `background-color 0.4s ease-out`, `top 0.4s cubic-bezier(0.4, 0, 0.2, 1), left 0.4s cubic-bezier(0.4, 0, 0.2, 1), width 0.4s cubic-bezier(0.4, 0, 0.2, 1), height 0.4s cubic-bezier(0.4, 0, 0.2, 1), border-radius 0.4s cubic-bezier(0.4, 0, 0.2, 1)`, `max-height 0.2s linear, visibility 0.2s linear 0.2s`, `transform 0.5s ease-in-out`, `transform 300ms ease-in-out`, `all var(--duration, '4000ms') ease`, `background-color 5000s ease-in-out`, `background 0.2s`, `opacity 500ms`, `border, background 300ms`, `border 300ms`, `height 0.5s`

- subscriptions: `0.25s ease-in-out`, `0.15s ease-in-out`, `opacity 0.1s ease-out, content 0.3s ease-in-out`, `opacity 0.1s ease-out`, `color 0.1s ease-out`, `0.6s ease-in-out`, `none`, `0.8s cubic-bezier(0, 1, 0.7, 1)`, `max-height 0.6s ease-in-out, visibility 0.6s ease-in-out`, `transform 0.35s`, `opacity 0.2s`
