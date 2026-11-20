# HTTPie components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Read from httpie.io on 2026-11-17, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Later recaptures merge into the same file, so every entry names the date its own states were read; a state a re-read missed keeps its earlier date and says so. Nothing was signed into, bought, typed, searched or submitted; the only presses were local UI toggles the product's own chrome provides — the footer's ThemeToggle radios, the /app method and Incognito-space menus, the request and environments tabs, the docs' ⌘K search dialog — and nothing was sent anywhere: Send was never pressed on /app, so the response pane is its resting 'Not sent' state; every link was measured, never followed.

**Where this was read.** Two public surfaces carry the system: the httpie.io marketing and docs pages — home, /desktop, /cli, /ai, /docs(+desktop,+cli), /jobs, /blog, /download, /about, /terms, /privacy — and /app, HTTPie-for-Web running signed out in its 'Incognito space'. Sign-in and every account surface were never entered; the HTTPie AI 'Try it out' action was never pressed (generation is an account feature); /pricing 404s and /discord redirects off-site — all documented as boundaries under Gaps, not captures.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (49 components, 98 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the token in [tokens.json](tokens.json) with the same value, when there is one (the `dark.*` roles first — the painted default). Text is written family size/line-height weight, then its colour, for example `Pie Body 16/26 400, #f5f5f0`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (94 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-{state}.png` where `{theme}` is the surface the page painted at capture: every page boots `html.dark`, so `{page}-dark-*` shots are the painted default and `{page}-light-*` shots the same page after the footer's own LIGHT MODE radio repainted html.light, verified by the painted surface and switched back after (on /app the choice persisted through localStorage.theme — the same signal the app reads). Desktop shots are 1440 x 900 at 1x; `-full` shots are the whole page at 1x, bounded at eight chunks with the boundary recorded in the shot's `.capture.json` sidecar (the blog index and terms are the long pages); mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x). `notfound-*` is /pricing, which 404s — captured as the product's not-found page.

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-dark-default.png), [full](screenshots/home-dark-full.png), [theme-toggle](screenshots/home-dark-theme-toggle.png), [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png) |
| Desktop | `/desktop` | [default](screenshots/desktop-page-dark-default.png), [full](screenshots/desktop-page-dark-full.png), [default](screenshots/desktop-page-light-default.png) |
| Terminal / CLI | `/cli` | [default](screenshots/cli-dark-default.png), [full](screenshots/cli-dark-full.png), [default](screenshots/cli-light-default.png) |
| AI | `/ai` | [default](screenshots/ai-dark-default.png), [default](screenshots/ai-light-default.png) |
| Docs index | `/docs` | [default](screenshots/docs-dark-default.png), [full](screenshots/docs-dark-full.png) |
| Desktop docs | `/docs/desktop` | [default](screenshots/docs-desktop-dark-default.png), [full](screenshots/docs-desktop-dark-full.png), [default](screenshots/docs-desktop-light-default.png) |
| CLI docs | `/docs/cli` | [default](screenshots/docs-cli-dark-default.png), [full](screenshots/docs-cli-dark-full.png) |
| Jobs | `/jobs` | [default](screenshots/jobs-dark-default.png), [full](screenshots/jobs-dark-full.png), [default](screenshots/jobs-light-default.png) |
| Blog index | `/blog` | [default](screenshots/blog-dark-default.png), [full](screenshots/blog-dark-full.png), [default](screenshots/blog-light-default.png) |
| Changelog post | `/blog/changelog-0027` | [default](screenshots/blog-post-dark-default.png), [full](screenshots/blog-post-dark-full.png), [default](screenshots/blog-post-light-default.png) |
| Download | `/download` | [default](screenshots/download-dark-default.png), [full](screenshots/download-dark-full.png), [default](screenshots/download-light-default.png) |
| About | `/about` | [default](screenshots/about-dark-default.png), [full](screenshots/about-dark-full.png) |
| Terms | `/terms` | [default](screenshots/terms-dark-default.png), [full](screenshots/terms-dark-full.png) |
| Privacy | `/privacy` | [default](screenshots/privacy-dark-default.png), [full](screenshots/privacy-dark-full.png) |
| 404 page (/pricing probe) | `/pricing` | [default](screenshots/notfound-dark-default.png), [full](screenshots/notfound-dark-full.png) |
| HTTPie for Web — Incognito space | `/app` | [ai-promo](screenshots/app-dark-ai-promo.png), [default](screenshots/app-dark-default.png), [env-settings](screenshots/app-dark-env-settings.png), [environments](screenshots/app-dark-environments.png), [method-menu](screenshots/app-dark-method-menu.png), [space-panel](screenshots/app-dark-space-panel.png), [tab-auth](screenshots/app-dark-tab-auth.png), [tab-body](screenshots/app-dark-tab-body.png), [tab-headers](screenshots/app-dark-tab-headers.png), [tab-response](screenshots/app-dark-tab-response.png), [default](screenshots/app-light-default.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-dark-default.png), [full](screenshots/mobile-home-dark-full.png) |
| Terminal / CLI, phone | `/cli` | [default](screenshots/mobile-cli-dark-default.png), [full](screenshots/mobile-cli-dark-full.png) |
| Blog index, phone | `/blog` | [default](screenshots/mobile-blog-dark-default.png), [full](screenshots/mobile-blog-dark-full.png) |
| Desktop docs, phone | `/docs/desktop` | [default](screenshots/mobile-docs-desktop-dark-default.png), [full](screenshots/mobile-docs-desktop-dark-full.png) |
| HTTPie for Web, phone | `/app` | [ai-promo](screenshots/mobile-app-dark-ai-promo.png), [default](screenshots/mobile-app-dark-default.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Theme toggle | every marketing page footer | the LIGHT MODE / AUTO / DARK MODE radio segments' own press — the painted surface verified, then switched back | [home-dark-theme-toggle](screenshots/home-dark-theme-toggle.png), [home-light-default](screenshots/home-light-default.png) |
| Incognito space panel | /app | the 'Incognito space' switcher's own press — the current space's tab (variables/settings) opened in the strip; no dropdown menu paints for the unsigned product | [app-dark-space-panel](screenshots/app-dark-space-panel.png) |
| Method menu | /app | the request line's GET button own press — the GET/HEAD/POST/… menu opened, captured, closed | [app-dark-method-menu](screenshots/app-dark-method-menu.png) |
| Request panel tabs | /app | the Headers / Auth / Body tabs' own activation — local UI toggles | [app-dark-tab-auth](screenshots/app-dark-tab-auth.png), [app-dark-tab-body](screenshots/app-dark-tab-body.png) |
| Environments manager | /app | the 'Environments' selector's own press — the manager opened as a strip tab with Variables/Settings/Defaults | [app-dark-environments](screenshots/app-dark-environments.png), [app-dark-env-settings](screenshots/app-dark-env-settings.png) |
| Response panel | /app | the Response panel tab's own activation — Send was never pressed (a network side effect), so the panel is its resting 'Not sent' surface | [app-dark-tab-response](screenshots/app-dark-tab-response.png) |
| HTTPie AI promo | /app | the 'Introducing HTTPie AI' dialog that mounts on some first loads — captured when it rendered, then closed with its own Close button; 'Try it out' was never pressed | [app-dark-ai-promo](screenshots/app-dark-ai-promo.png), [mobile-app-dark-ai-promo](screenshots/mobile-app-dark-ai-promo.png) |
| Docs search dialog (⌘K) | docs pages | the DocSearch button / Ctrl+K — opened, captured, closed with Escape; nothing was searched | see icons; dialog closed before shots |
| Light theme | all captured pages | the footer's own LIGHT MODE radio press; the painted surface was verified before each shot, then DARK restored | [home-light-default](screenshots/home-light-default.png), [app-light-default](screenshots/app-light-default.png) |
| Sign-in, account spaces, HTTPie AI | the account product | never entered — generation and sync are account features | boundary; see Gaps |
| Desktop app, CLI binaries | /download | the native builds behind the download buttons — marketing pages only | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 6 components were given a real keyboard focus. 1 draw an outline ring: `cli-install-select` (1px auto #101010, offset 0px). 1 draw a focus ring as a shadow instead: `app-send-button`. 4 change only their border: `nav-link`, `nav-cta`, `button-secondary`, `button-counter`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.15s | `cubic-bezier(0.4, 0, 0.2, 1)` | -webkit-backdrop-filter, all, backdrop-filter, background-color, border-color, box-shadow, color, fill, filter, opacity, stroke, text-decoration-color, transform | button-counter, button-secondary, button-share, cli-install-select, copy-button, early-access-badge, nav-cta, nav-link and more |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [App sidebar](#app-sidebar) | 49 x 900 | R: 1px solid rgba(255, 255, 255, 0.04) `dark.border.default` | - | transparent | none | 0 |
| [Request tab card](#request-tab-card) | 104 x 28 | - | 6px | #201c1c `dark.bg.z2` | none | 4px 2px 4px 4px |
| [URL field](#url-field) | 848.5 x 44 | - | - | transparent | none | 8px 0px |
| ["Send" button](#send-button) | 57 x 28 | - | 6px | #73dc8c `dark.accent.default` | rgba(255, 255, 255, 0.2) 0px 0px 0px 1px inset, rgba(0, 0, 0, 0.25) 0px 1px 2px 0px | 2px 12px |
| [Environments manager](#environments-manager) | 1026.5 x 796 | - | - | #1c1818 `dark.bg.z1` | none | 0 |
| [Testimonial card](#testimonial-card) | 360 x 238 | - | 10px | #4b78e6 `dark.altAccent.hover` | none | 44px 30px 30px 30px |
| [Newsletter email input](#newsletter-email-input) | 427.33 x 44 | 2px solid transparent | 9999px | #3354a6 `light.code.blue` | none | 12px 12px 13px 20px |
| [Post preview card](#post-preview-card) | 653 x 398.2 | - | - | transparent | none | 64px 0px 72px 0px |
| [Theme toggle (LIGHT / AUTO / DARK)](#theme-toggle-light--auto--dark) | 70 x 194.44 | - | - | transparent | none | 0 |

## Components

### Site chrome

The frame every marketing and docs page carries: the top nav (wordmark, Desktop / Terminal / AI / Docs / Jobs / Blog links, the solid 'Go to App →' primary button), the footer with its link columns and social buttons, and the LIGHT MODE / AUTO / DARK MODE ThemeToggle — the product's real theme control, pressed for the light states.

#### Site navigation bar
The top nav (Navigation_navigation): wordmark, Desktop / Terminal / AI / Docs / Jobs / Blog links and the "Go to App →" primary button. Read as `site-nav` on the / page.
States read on 2026-11-17T09:23:58.889Z (default); 2026-11-17T09:24:15.214Z (light).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 1440 x 130; padding 0px 55px; background transparent; text Pie Body 18/30 400, #f5f5f0 `dark.text.primary`; layers span.Count_count__p9ULf.Navigation_count__CXLW6 19.0x19.0 #363636 9999px; button.Button_button__mg_cR.Button_primary__PFIP8 180.0x51.0 #73dc8c T:2px solid / R:2px solid / B:2px solid / L:2px solid 9999px; div.Navigation_featuredIconCircle__n4aZN 0.0x0.0 #363636 9999px |
| light | text Pie Body 18/30 400, #1e1919; layers span.Count_count__p9ULf.Navigation_count__CXLW6 19.0x19.0 #ededeb 9999px; button.Button_button__mg_cR.Button_primary__PFIP8 180.0x51.0 #73dc8c T:2px solid / R:2px solid / B:2px solid / L:2px solid 9999px; div.Navigation_featuredIconCircle__n4aZN 0.0x0.0 #d1d1cf 9999px |

Child layers that carry the look: span 19x19 background #363636 `light.code.primary` radius 9999px; button 180x51 background #73dc8c `dark.accent.default` border 2px solid radius 9999px; div 0x0 background #363636 `light.code.primary` radius 9999px.

![Site navigation bar default](components/crops/site-nav-default.png) ![Site navigation bar light](components/crops/site-nav-light.png)

#### Nav link
A primary nav link ("Terminal"). Read as `nav-link` on the / page.
States read on 2026-11-17T09:24:56.123Z (default); 2026-11-17T09:25:05.853Z (hover); 2026-11-17T09:25:09.516Z (focus-visible).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 70.59 x 30; background transparent; text Pie Body 18/30 400, #f5f5f0 `dark.text.primary`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | text Pie Body 18/30 400, #73dc8c `dark.accent.default` |
| focus-visible | outline 2px solid transparent, offset 2px; text Pie Body 18/30 400, #73dc8c `dark.accent.default`; layers a.Link_link__58k5P.Navigation_link__hMCGF 70.6x30.0 2px solid transparent offset 2px |

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png)

#### "Go to App →" button
The solid primary button in the nav — links to /app, measured never followed. Read as `nav-cta` on the / page.
States read on 2026-11-17T09:25:14.224Z (default); 2026-11-17T09:25:18.827Z (hover); 2026-11-17T09:25:20.177Z (focus-visible); 2026-11-17T09:25:36.338Z (pressed); 2026-11-17T09:25:40.507Z (light).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: light) | size 180 x 51; padding 13px 21px 13px 19px; border 2px solid transparent; radius 9999px; background #73dc8c `dark.accent.default`; text Pie Body 15/21 400, #1e1919; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #4f4d4d; text Pie Body 15/21 400, #73dc8c `dark.accent.default` |
| focus-visible | border 2px solid #73dc8c `dark.accent.default`; background #4f4d4d; outline 2px solid transparent, offset 2px; text Pie Body 15/21 400, #73dc8c `dark.accent.default` |
| pressed | background #4f4d4d; text Pie Body 15/21 400, #73dc8c `dark.accent.default` |

!["Go to App →" button default](components/crops/nav-cta-default.png) !["Go to App →" button hover](components/crops/nav-cta-hover.png) !["Go to App →" button focus-visible](components/crops/nav-cta-focus-visible.png) !["Go to App →" button pressed](components/crops/nav-cta-pressed.png) !["Go to App →" button light](components/crops/nav-cta-light.png)

#### Site footer
The page footer (Footer_footer): link columns, the social icons, and the LIGHT MODE / AUTO / DARK MODE theme control. Read as `site-footer` on the / page.
Read on 2026-11-17T09:26:21.637Z.

**Values (default).** size 1440 x 440.22; padding 75px 0px 40px 0px; background #363636 `light.code.primary`; text Pie Body 16/22.4 600, #f5f5f0 `dark.text.primary`.

![Site footer default](components/crops/site-footer-default.png)

#### Theme toggle (LIGHT / AUTO / DARK)
The footer's three-segment ThemeToggle radio stack — the product's real theme control. "light" is its own LIGHT MODE press, restored to DARK after. Read as `theme-toggle` on the / page.
States read on 2026-11-17T09:26:22.747Z (default); 2026-11-17T09:26:27.368Z (light).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 70 x 194.44; background transparent; text Pie Body 10/14 400, #ededeb; layers div.ThemeToggle_container__5I861 70.0x30.0 #1e1919 9999px; div.ThemeToggle_radio__IFs89 4.0x4.0 #666663 9999px; div.ThemeToggle_radio__IFs89 4.0x4.0 #666663 9999px; div.ThemeToggle_radio__IFs89.ThemeToggle_active__3wrnM 14.0x14.0 #f5f5f0 9999px |
| light | text Pie Body 10/14 400, #363636 `light.code.primary`; layers div.ThemeToggle_container__5I861 70.0x30.0 #7d7d7d 9999px; div.ThemeToggle_radio__IFs89 4.0x4.0 #b5b5b2 9999px; div.ThemeToggle_radio__IFs89.ThemeToggle_active__3wrnM 14.0x14.0 #f5f5f0 9999px; div.ThemeToggle_radio__IFs89 4.0x4.0 #b5b5b2 9999px |

Child layers that carry the look: div 70x30 background #1e1919 radius 9999px; div 4x4 background #666663 radius 9999px; div 4x4 background #666663 radius 9999px.

![Theme toggle (LIGHT / AUTO / DARK) default](components/crops/theme-toggle-default.png) ![Theme toggle (LIGHT / AUTO / DARK) light](components/crops/theme-toggle-light.png)

#### Social button
A footer social action ("Discord") — a Button_secondary with an icon. Read as `social-button` on the / page.
States read on 2026-11-17T09:26:38.390Z (default); 2026-11-17T09:26:40.269Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 119.16 x 51; padding 13px 18px; border 2px solid transparent; radius 9999px; background #f5f5f0 `dark.text.primary`; text Pie Body 15/21 400, #1e1919; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 17 x 20.19, #1e1919 |
| hover | background #4f4d4d; text Pie Body 15/21 400, #f5f5f0 `dark.text.primary`; icon 17 x 20.19, #f5f5f0 `dark.text.primary` |

![Social button default](components/crops/social-button-default.png) ![Social button hover](components/crops/social-button-hover.png)

### Buttons and links

The marketing actions: the outlined secondary button, the 'Star on GitHub' counter button, the 'Share on Twitter' share button and the underlined text links. Links were measured, never followed.

#### Secondary button
An outlined action ("Read blog post" on the changelog banner). Read as `button-secondary` on the / page.
States read on 2026-11-17T09:26:40.271Z (pressed); 2026-11-17T09:26:42.248Z (default); 2026-11-17T09:26:45.010Z (hover); 2026-11-17T09:26:47.153Z (focus-visible). `pressed` failed at capture (cdpSession.send: Protocol error (DOM.getNodeForLocation): No node found at given location).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 180 x 51; padding 13px 18px; border 2px solid transparent; radius 9999px; background #f5f5f0 `dark.text.primary`; text Pie Body 15/21 400, #1e1919; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #4f4d4d; text Pie Body 15/21 400, #f5f5f0 `dark.text.primary` |
| focus-visible | border 2px solid #f5f5f0 `dark.text.primary`; background #4f4d4d; outline 2px solid transparent, offset 2px; text Pie Body 15/21 400, #f5f5f0 `dark.text.primary` |

![Secondary button default](components/crops/button-secondary-default.png) ![Secondary button hover](components/crops/button-secondary-hover.png) ![Secondary button focus-visible](components/crops/button-secondary-focus-visible.png)

#### Counter button ("Star on GitHub")
The GitHub star button carrying its live count — Button_counter. Read as `button-counter` on the / page.
States read on 2026-11-17T09:26:59.543Z (default); 2026-11-17T09:27:06.692Z (hover); 2026-11-17T09:27:08.066Z (focus-visible).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 253.31 x 53; padding 14px 100px 14px 18px; border 2px solid transparent; radius 9999px; background #f5f5f0 `dark.text.primary`; text Pie Body 15/21 400, #1e1919; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 17 x 17, #1e1919 |
| hover | background #4f4d4d; text Pie Body 15/21 400, #f5f5f0 `dark.text.primary`; icon 17 x 17, #f5f5f0 `dark.text.primary` |
| focus-visible | border 2px solid #f5f5f0 `dark.text.primary`; background #4f4d4d; outline 2px solid transparent, offset 2px; text Pie Body 15/21 400, #f5f5f0 `dark.text.primary`; icon 17 x 17, #f5f5f0 `dark.text.primary` |

![Counter button ("Star on GitHub") default](components/crops/button-counter-default.png) ![Counter button ("Star on GitHub") hover](components/crops/button-counter-hover.png) ![Counter button ("Star on GitHub") focus-visible](components/crops/button-counter-focus-visible.png)

#### Share button
"Share on Twitter" in the testimonial wall footer — Button_share. Read as `button-share` on the / page.
States read on 2026-11-17T09:27:09.087Z (default); 2026-11-17T09:27:11.279Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 183.64 x 51; padding 13px 18px; border 2px solid transparent; radius 9999px; background #363636 `light.code.primary`; text Pie Body 15/21 400, #f5f5f0 `dark.text.primary`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 17 x 13.81, #f5f5f0 `dark.text.primary` |
| hover | background #7d7d7d `dark.code.gray` |

![Share button default](components/crops/button-share-default.png) ![Share button hover](components/crops/button-share-hover.png)

#### Text link
A Link_link in page content. Read as `text-link` on the / page.
States read on 2026-11-17T09:27:12.377Z (default); 2026-11-17T09:27:14.270Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 140 x 40; background transparent; text Pie Body 16/24 400, #f5f5f0 `dark.text.primary`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1) |

![Text link default](components/crops/text-link-default.png) ![Text link hover](components/crops/text-link-hover.png)

### Home

The home surface: the 'FLOW THROUGH APIs.' hero in Pie Headline, the β Public beta pill, the community tweet-card wall and the newsletter forms — the email fields were clicked into for their focus look, never typed in or submitted.

#### Hero headline
The home hero h1 "FLOW THROUGH APIs" — Pie Headline (FK Screamer). Read as `hero-headline` on the / page.
States read on 2026-11-17T09:27:15.315Z (default); 2026-11-17T09:27:17.538Z (light).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 296.16 x 261.61; background transparent; text Pie Headline 109/87.2 400, #f5f5f0 `dark.text.primary` |
| light | text Pie Headline 109/87.2 400, #1e1919 |

![Hero headline default](components/crops/hero-headline-default.png) ![Hero headline light](components/crops/hero-headline-light.png)

#### Testimonial card
A tweet card in the community wall (TestimonialCard_tweet): avatar, name, handle, body, timestamp. Read as `testimonial-card` on the / page.
Read on 2026-11-17T09:27:47.638Z.

**Values (default).** size 360 x 238; padding 44px 30px 30px 30px; radius 10px; background #4b78e6 `dark.altAccent.hover`; text Pie Body 15/21 400, #f5f5f0 `dark.text.primary`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1).

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Newsletter email input
The "Enter email address" field of a NewsletterForm. "focused" is the field clicked into — nothing is typed, the form is never submitted. Read as `newsletter-input` on the / page.
States read on 2026-11-17T09:28:10.310Z (default); 2026-11-17T09:28:12.017Z (focused); 2026-11-17T09:28:14.216Z (light).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: light) | size 427.33 x 44; padding 12px 12px 13px 20px; border 2px solid transparent; radius 9999px; background #3354a6 `light.code.blue`; text Pie Body 16/24 400, #f5f5f0 `dark.text.primary`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1); placeholder #b5b5b2 |
| focused | border 2px solid #73dc8c `dark.accent.default`; shadow #ffffff 0px 0px 0px 0px, #73dc8c 0px 0px 0px 1px, #73dc8c 0px 0px 0px 1px; outline 2px solid transparent, offset 2px |

![Newsletter email input default](components/crops/newsletter-input-default.png) ![Newsletter email input focused](components/crops/newsletter-input-focused.png) ![Newsletter email input light](components/crops/newsletter-input-light.png)

#### Newsletter submit button
The form's arrow submit — measured, never pressed. Read as `newsletter-button` on the / page.
States read on 2026-11-17T09:28:45.856Z (default); 2026-11-17T09:28:48.532Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 38 x 38; radius 9999px; background #73dc8c `dark.accent.default`; text Pie Body 16/24 400, #f5f5f0 `dark.text.primary`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 8 x 14.39, #1e1919 |
| hover | size 32.3 x 32.3; transform scale(0.85); icon 6.8 x 12.23, #1e1919 |

![Newsletter submit button default](components/crops/newsletter-button-default.png) ![Newsletter submit button hover](components/crops/newsletter-button-hover.png)

#### "Public beta" badge
The β Public beta pill on the hero (EarlyAccessBadge). Read as `early-access-badge` on the / page.
Read on 2026-11-17T09:28:49.492Z.

**Values (default).** size 132.7 x 34; padding 4px 12px 4px 4px; radius 9999px; background #363636 `light.code.primary`; text Pie Body 14/24 600, #1e1919; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1).

!["Public beta" badge default](components/crops/early-access-badge-default.png)

#### Section heading
A home section heading (the testimonial wall's h2). Read as `section-heading` on the / page.
Read on 2026-11-17T09:28:50.521Z.

**Values (default).** size 653 x 84; background transparent; text Pie Body 30/42 600, #f5f5f0 `dark.text.primary`.

![Section heading default](components/crops/section-heading-default.png)

### Terminal page

The /cli surface: the package-manager install picker pills, the dark terminal/code blocks and the copy buttons beside install commands — pressed only with forcePseudoState.

#### Install tool selector
A package-manager pill in the CLI install picker (InstallationSelect_tool: apt / brew / choco…). Read as `cli-install-select` on the /cli page.
States read on 2026-11-17T09:29:16.486Z (default); 2026-11-17T09:29:19.959Z (hover); 2026-11-17T09:30:05.544Z (focus-visible).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 54.73 x 21; background transparent; text Pie Monospace 15/21 600, #a1b8f2; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 12 x 10, #a1b8f2 |
| hover | text Pie Monospace 15/21 600, #73dc8c `dark.accent.default`; icon 12 x 10, #73dc8c `dark.accent.default` |
| focus-visible | outline 1px auto #101010, offset 0px; text Pie Monospace 15/21 600, #73dc8c `dark.accent.default`; icon 12 x 10, #73dc8c `dark.accent.default`; layers span.InstallationSelect_tool__G9vXs 54.7x21.0 1px auto #101010 offset 0px |

![Install tool selector default](components/crops/cli-install-select-default.png) ![Install tool selector hover](components/crops/cli-install-select-hover.png) ![Install tool selector focus-visible](components/crops/cli-install-select-focus-visible.png)

#### Terminal/code block
A dark code panel with an install command and its copy button. Read as `cli-code-block` on the /cli page.
States read on 2026-11-17T09:30:06.639Z (default); 2026-11-17T09:30:22.060Z (light).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: light) | size 626.23 x 39; background transparent; text Pie Monospace 15/21 400, #fa9bfa `dark.code.pink` |

![Terminal/code block default](components/crops/cli-code-block-default.png) ![Terminal/code block light](components/crops/cli-code-block-light.png)

#### Copy button
The CopyButton beside an install command — pressed only with forcePseudoState. Read as `copy-button` on the /cli page.
States read on 2026-11-17T09:30:34.479Z (pressed); 2026-11-17T09:30:36.098Z (default); 2026-11-17T09:30:39.079Z (hover). `pressed` failed at capture (cdpSession.send: Protocol error (DOM.getNodeForLocation): No node found at given location).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 28 x 24; background transparent; text Pie Body 13/18.2 300, #1e1919; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 14 x 18.11, #d1d1cf `dark.code.primary`; layers div.Tooltip_tooltip__MB_31.CopyButton_tooltip__SPsgL 60.0x26.2 #b5b5b2 5px; div::before.Tooltip_tooltip__MB_31.CopyButton_tooltip__SPsgL 20pxx8px R:10px solid / B:8px solid / L:10px solid; div::after.Tooltip_tooltip__MB_31.CopyButton_tooltip__SPsgL 16pxx8px R:8px solid / B:8px solid / L:8px solid |

Child layers that carry the look: div 60x26.2 background #b5b5b2 radius 5px; div::before 20pxx8px border 10px solid; div::after 16pxx8px border 8px solid.

![Copy button default](components/crops/copy-button-default.png) ![Copy button hover](components/crops/copy-button-hover.png)

### Blog

The /blog changelog index: post preview cards and title links — measured, never followed.

#### Post preview card
A changelog post row on the blog index (PostPreview_post): title, excerpt, meta. Read as `post-card` on the /blog page.
States read on 2026-11-17T09:31:44.433Z (default); 2026-11-17T09:31:49.303Z (light).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 653 x 398.2; padding 64px 0px 72px 0px; background transparent; text Pie Body 12/16.8 400, #f5f5f0 `dark.text.primary`; layers button.Button_button__mg_cR.Button_secondary__kYMEY 180.0x51.0 #f5f5f0 T:2px solid / R:2px solid / B:2px solid / L:2px solid 9999px |
| light | text Pie Body 12/16.8 400, #1e1919; layers button.Button_button__mg_cR.Button_secondary__kYMEY 180.0x51.0 #1e1919 T:2px solid / R:2px solid / B:2px solid / L:2px solid 9999px |

Child layers that carry the look: button 180x51 background #f5f5f0 `dark.text.primary` border 2px solid radius 9999px.

![Post preview card default](components/crops/post-card-default.png) ![Post preview card light](components/crops/post-card-light.png)

#### Post title link
The post's title inside an index card. Read as `post-title-link` on the /blog page.
States read on 2026-11-17T09:32:19.554Z (default); 2026-11-17T09:32:21.876Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 628.88 x 72; background transparent; text Pie Body 30/42 600, #f5f5f0 `dark.text.primary`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1) |

![Post title link default](components/crops/post-title-link-default.png) ![Post title link hover](components/crops/post-title-link-hover.png)

### Prose

The changelog article layer: the title h1, body paragraphs and links, inline code and the syntax-tinted fenced blocks.

#### Article title (h1)
The changelog post title. Read as `prose-h1` on the /blog/changelog-0027 page.
States read on 2026-11-17T09:32:47.525Z (default); 2026-11-17T09:33:07.248Z (light).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 653 x 84; background transparent; text Pie Body 30/42 600, #f5f5f0 `dark.text.primary` |
| light | text Pie Body 30/42 600, #1e1919 |

![Article title (h1) default](components/crops/prose-h1-default.png)

#### Body paragraph
A paragraph of article prose. Read as `prose-p` on the /blog/changelog-0027 page.
Read on 2026-11-17T09:33:30.412Z.

**Values (default).** size 653 x 75.61; background transparent; text Pie Body 18/25.2 300, #ededeb.

![Body paragraph default](components/crops/prose-p-default.png)

#### Prose link
A body-text link inside the article. Read as `prose-link` on the /blog/changelog-0027 page.
States read on 2026-11-17T09:33:32.849Z (default); 2026-11-17T09:33:34.856Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 68.39 x 30; background transparent; text Pie Body 18/30 400, #f5f5f0 `dark.text.primary`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | text Pie Body 18/30 400, #73dc8c `dark.accent.default` |

![Prose link default](components/crops/prose-link-default.png) ![Prose link hover](components/crops/prose-link-hover.png)

#### Inline code
An inline code span in prose. Read as `prose-code` on the /blog/changelog-0027 page.
Read on 2026-11-17T09:33:35.926Z.

**Values (default).** size 75.27 x 25; padding 1px 5px 1px 4px; border 1px solid #4f4d4d; radius 4px; background #363636 `light.code.primary`; text Pie Monospace 15/21 300, #f5f5f0 `dark.text.primary`.

![Inline code default](components/crops/prose-code-default.png)

#### Code block
A fenced code block in the article (syntax-tinted). Read as `prose-pre` on the /blog/changelog-0027 page.

Not on the page when it was captured.

### Docs

The docs surface: the 'On this page' table-of-contents rail and the left-nav section links.

#### Docs table of contents
The right-rail "On this page" TOC aside on a docs page. Read as `docs-toc` on the /docs/desktop page.
States read on 2026-11-17T10:26:54.383Z (default); 2026-11-17T10:26:57.957Z (light).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 314.5 x 770; padding 0px 0px 60px 0px; background transparent; text Pie Body 15/32 700, #f5f5f0 `dark.text.primary` |
| light | text Pie Body 15/32 700, #1e1919 |

![Docs table of contents default](components/crops/docs-toc-default.png) ![Docs table of contents light](components/crops/docs-toc-light.png)

#### Docs nav section link
A section link in the docs left nav ("Request method"). Read as `docs-side-link` on the /docs/desktop page.
States read on 2026-11-17T10:27:35.144Z (default); 2026-11-17T10:28:27.564Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 271.98 x 33; background transparent; text Pie Body 32/44.8 600, #f5f5f0 `dark.text.primary`; layers ::before transparent 0px none 0 |
| hover | layers ::before transparent 0px none 0.8 |

![Docs nav section link default](components/crops/docs-side-link-default.png) ![Docs nav section link hover](components/crops/docs-side-link-hover.png)

#### Docs code block
A fenced code block inside the docs article pane — the surface the code-* syntax palette paints (the captured changelog post carries no fenced block, so this is the package's syntax-block evidence). Read as `docs-code-block` on the /docs/desktop page.
States read on 2026-11-17T10:28:45.587Z (default); 2026-11-17T10:28:47.762Z (light).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: light) | size 745.5 x 48; background transparent; text Pie Body 15/21 400, #fa9bfa `dark.code.pink` |

![Docs code block default](components/crops/docs-code-block-default.png) ![Docs code block light](components/crops/docs-code-block-light.png)

#### Docs inline code
An inline code span inside the docs article pane. Read as `docs-inline-code` on the /docs/desktop page.
Read on 2026-11-17T10:29:31.322Z.

**Values (default).** size 167.06 x 25; padding 1px 5px 1px 4px; border 1px solid #4f4d4d; radius 4px; background #363636 `light.code.primary`; text Pie Monospace 15/21 300, #f5f5f0 `dark.text.primary`.

![Docs inline code default](components/crops/docs-inline-code-default.png)

### App shell

HTTPie-for-Web signed out — the 'Incognito space': the left rail (space switcher, Collection/Drafts shelf, Import) and the Environments selector. The switcher's press opens the space's own tab; the environments manager was opened through its own button.

#### App sidebar
The left rail (Layout_sidebar): space switcher, Collection/Drafts/Environments panel. Read as `app-sidebar` on the /app page.
States read on 2026-11-17T13:07:59.558Z (default); 2026-11-17T13:08:11.917Z (light).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 49 x 900; border R: 1px solid rgba(255, 255, 255, 0.04) `dark.border.default`; background transparent; text PolySans 16/24 400, #f5f5f0 `dark.text.primary`; icon 30 x 32, #73dc8c `dark.accent.default`; layers aside.Layout_sidebar__OHKsB 49.0x900.0 R:1px solid; span.Layout_logoLink__fn7pT 32.0x48.0 2px solid transparent offset 2px; button.MenuItem_button__lVvmy.mt-1 32.0x32.0 rgba(255, 255, 255, 0.06) 8px; hr.m-1.border-t 24.0x1.0 T:1px solid |
| light | border R: 1px solid rgba(0, 0, 0, 0.06) `light.border.default`; text PolySans 16/24 400, #1c1818 `dark.bg.z1`; icon 30 x 32, #52ab66 `light.accent.default`; layers aside.Layout_sidebar__OHKsB 49.0x900.0 R:1px solid; span.Layout_logoLink__fn7pT 32.0x48.0 2px solid transparent offset 2px; button.MenuItem_button__lVvmy.mt-1 32.0x32.0 rgba(0, 0, 0, 0.06) 8px; hr.m-1.border-t 24.0x1.0 T:1px solid |

Child layers that carry the look: aside 49x900 border 1px solid; span 32x48; button 32x32 background rgba(255, 255, 255, 0.06) `dark.item.selected` radius 8px.

![App sidebar default](components/crops/app-sidebar-default.png) ![App sidebar light](components/crops/app-sidebar-light.png)

#### "Incognito space" button
The space switcher button. "opened" is its own press opening the current space's tab (variables/settings) in the strip — no dropdown menu paints for the unsigned product. Read as `app-space-button` on the /app page.
States read on 2026-11-17T13:08:51.171Z (default); 2026-11-17T13:08:52.999Z (hover); 2026-11-17T13:08:55.604Z (opened).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 109 x 24; padding 0px 0px 0px 6px; background transparent; text PolySans 14.2/24 400, rgba(245, 245, 240, 0.6) `dark.text.secondary` |
| opened | size 1042.5 x 900; padding 0px 8px; text PolySans 12.8/16 400, #f5f5f0 `dark.text.primary`; icon 16 x 16, #7d7d7d `dark.code.gray`; layers div::before.Container_container__Dzv7w.Tabs_tabsScrollableContainer__YxAiG 32pxx28px; div::after.Container_container__Dzv7w.Tabs_tabsScrollableContainer__YxAiG 32pxx28px; div.TabCard_tab__0R39Q.Tab_tab__eWtGS 152.0x28.0 #201c1c 2px solid transparent offset 2px 6px; div.EntityIcon_substrate__eAQqs.group-hover:bg-code-gray 20.0x20.0 #7d7d7d T:1px solid / R:1px solid / B:1px solid / L:1px solid 4px;  |

!["Incognito space" button default](components/crops/app-space-button-default.png) !["Incognito space" button hover](components/crops/app-space-button-hover.png) !["Incognito space" button opened](components/crops/app-space-button-opened.png)

#### "Drafts" shelf header
The Drafts collection header in the sidebar panel — the unsaved-requests shelf. Read as `app-drafts-tab` on the /app page.
States read on 2026-11-17T13:08:23.372Z (default); 2026-11-17T13:08:25.203Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 291.5 x 24; padding 0px 6px; background transparent; text PolySans 14.2/24 400, #f5f5f0 `dark.text.primary` |
| hover | size 249.5 x 24 |

!["Drafts" shelf header default](components/crops/app-drafts-tab-default.png) !["Drafts" shelf header hover](components/crops/app-drafts-tab-hover.png)

#### "Environments" selector
The Environments button in the tab bar — opens the environments manager panel. Read as `app-env-button` on the /app page.
States read on 2026-11-17T13:08:57.695Z (default); 2026-11-17T13:09:00.337Z (hover); 2026-11-17T13:09:03.165Z (opened).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 111 x 28; padding 4px 8px; radius 6px; background transparent; text PolySans 12.8/16 400, rgba(245, 245, 240, 0.6) `dark.text.secondary`; icon 16 x 16, #7d7d7d `dark.code.gray` |
| hover | background rgba(255, 255, 255, 0.03) `dark.item.hover` |
| opened | size 152 x 24; padding 0px 6px; radius 4px; text PolySans 14.2/24 400, #f5f5f0 `dark.text.primary`; icon none; layers div.AdornmentableTextControl_container__h_T_O.MultilineInput_container__pe_B3 152.0x24.0 transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px 4px |

!["Environments" selector default](components/crops/app-env-button-default.png) !["Environments" selector hover](components/crops/app-env-button-hover.png) !["Environments" selector opened](components/crops/app-env-button-opened.png)

#### Drafts empty state
The InfoBlock inside the Drafts shelf: "Drafts are your unsaved requests. Organize the ones you want to keep in a collection" — the signed-out draft list is empty. Read as `app-drafts-empty` on the /app page.
Read on 2026-11-17T13:08:26.143Z.

**Values (default).** size 323.5 x 52; padding 8px; border 2px solid rgba(255, 255, 255, 0.04) `dark.border.default`; radius 8px; background transparent; text PolySans 12.8/16 400, rgba(245, 245, 240, 0.6) `dark.text.secondary`.

![Drafts empty state default](components/crops/app-drafts-empty-default.png)

### Request builder

The request workspace: the tab card, the method menu (its own GET press paints the GET/HEAD/POST/… menu), the URL field holding the prefilled httpie.io/hello, the Send button, the Params/Headers/Auth/Body panel tabs and the response pane. Send was never pressed — issuing a request is a network side effect, so the response pane stands at its resting 'Not sent' state.

#### Request tab card
The "GET untitled" draft tab (TabCard_tab, Tab_isActive) in the tab strip. Read as `app-request-tab` on the /app page.
States read on 2026-11-17T13:08:27.012Z (default); 2026-11-17T13:08:28.861Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 104 x 28; padding 4px 2px 4px 4px; radius 6px; background #201c1c `dark.bg.z2`; outline 2px solid transparent, offset 2px; text PolySansMono 8.5/16 400, #73dc8c `dark.accent.default`; icon 12 x 12, rgba(245, 245, 240, 0.6) `dark.text.secondary` |

![Request tab card default](components/crops/app-request-tab-default.png) ![Request tab card hover](components/crops/app-request-tab-hover.png)

#### Method select (GET)
The method dropdown button on the request line. "opened" is its own press painting the GET/HEAD/POST/… menu — closed with Escape. Read as `app-method-button` on the /app page.
States read on 2026-11-17T13:08:30.051Z (default); 2026-11-17T13:08:31.991Z (hover); 2026-11-17T13:08:34.559Z (opened).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 53 x 28; padding 2px 6px 2px 8px; radius 6px; background transparent; text PolySansMono 14.2/24 400, #73dc8c `dark.accent.default`; icon 12 x 12, #73dc8c `dark.accent.default` |
| hover | background rgba(255, 255, 255, 0.03) `dark.item.hover` |
| opened | size 140 x 249; padding none; radius none; text PolySans 14.2/24 400, #73dc8c `dark.accent.default`; icon 16 x 16, #f5f5f0 `dark.text.primary`; layers button.DropdownItemButton_button___Abfj.DropdownItemButton_selected__Uq5_o 140.0x28.0 rgba(255, 255, 255, 0.06) 2px solid transparent offset 2px 6px; button.DropdownItemButton_button___Abfj.DropdownItemButton_withCheckmark__YxXws 140.0x28.0 2px solid transparent offset 2px 6px; button.DropdownItemButton_button___Abfj.DropdownItemButton_withCheckmark__YxXws 140.0x28.0 2px solid transparent offset 2 |

![Method select (GET) default](components/crops/app-method-button-default.png) ![Method select (GET) hover](components/crops/app-method-button-hover.png) ![Method select (GET) opened](components/crops/app-method-button-opened.png)

#### URL field
The request URL editor (UrlBar, a CodeMirror single-line field) holding the prefilled httpie.io/hello. Read as `app-url-field` on the /app page.
States read on 2026-11-17T13:08:35.647Z (default); 2026-11-17T13:08:37.253Z (focused).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 848.5 x 44; padding 8px 0px; background transparent; text PolySansMono 14.2/24 400, rgba(245, 245, 240, 0.35) `dark.text.placeholders`; layers div.cm-cursor.cm-cursor-primary 0.0x0.0 L:1px solid |
| focused | layers div.cm-cursor.cm-cursor-primary 1.0x14.0 L:1px solid |

Child layers that carry the look: div 0x0 border 1px solid.

![URL field default](components/crops/app-url-field-default.png) ![URL field focused](components/crops/app-url-field-focused.png)

#### "Send" button
The request's primary action — measured at rest and with forcePseudoState only; a real press would issue a network request, so it is never fired. Read as `app-send-button` on the /app page.
States read on 2026-11-17T13:08:38.148Z (default); 2026-11-17T13:08:40.051Z (hover); 2026-11-17T13:08:41.668Z (focus-visible); 2026-11-17T13:08:43.003Z (pressed).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 57 x 28; padding 2px 12px; radius 6px; background #73dc8c `dark.accent.default`; shadow rgba(255, 255, 255, 0.2) 0px 0px 0px 1px inset, rgba(0, 0, 0, 0.25) 0px 1px 2px 0px; text PolySans 14.2/24 400, #1c1818 `dark.bg.z1` |
| hover | background #a1e8b0 `dark.accent.hover` |
| focus-visible | shadow #3b5eba 0px 0px 0px 2px; outline 2px solid transparent, offset 2px |

!["Send" button default](components/crops/app-send-button-default.png) !["Send" button hover](components/crops/app-send-button-hover.png) !["Send" button focus-visible](components/crops/app-send-button-focus-visible.png) !["Send" button pressed](components/crops/app-send-button-pressed.png)

#### Request panel tablist
The Params / Headers / Auth / Body tablist (PanelTabs) above the request editor. Read as `app-panel-tabs` on the /app page.
Read on 2026-11-17T13:08:43.887Z.

**Values (default).** size 237 x 28; background transparent; text PolySans 14.2/24 400, #f5f5f0 `dark.text.primary`; layers button.PanelTabButton_button__iYu6s.PanelTabs_aloneActiveTab___1VKK 64.0x28.0 rgba(255, 255, 255, 0.06) 6px.

Child layers that carry the look: button 64x28 background rgba(255, 255, 255, 0.06) `dark.item.selected` radius 6px.

![Request panel tablist default](components/crops/app-panel-tabs-default.png)

#### Request panel tab
One request panel tab ("Headers"). "selected" is its own activation — a local UI toggle. Read as `app-panel-tab` on the /app page.
States read on 2026-11-17T13:08:44.745Z (default); 2026-11-17T13:08:46.587Z (hover); 2026-11-17T13:08:48.353Z (selected).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 70 x 28; padding 2px 8px; radius 6px; background transparent; text PolySans 14.2/24 400, rgba(245, 245, 240, 0.6) `dark.text.secondary` |
| hover | background rgba(255, 255, 255, 0.03) `dark.item.hover` |
| selected | background rgba(255, 255, 255, 0.06) `dark.item.selected`; outline 2px solid transparent, offset 2px; text PolySans 14.2/24 400, #f5f5f0 `dark.text.primary` |

![Request panel tab default](components/crops/app-panel-tab-default.png) ![Request panel tab hover](components/crops/app-panel-tab-hover.png) ![Request panel tab selected](components/crops/app-panel-tab-selected.png)

#### Param row checkbox
The enable checkbox on a params row — the painted box is Checkbox_container; the real input is a hidden 1px control. Read as `app-param-checkbox` on the /app page.
Read on 2026-11-17T13:08:49.220Z.

**Values (default).** size 16 x 16; border 1px solid rgba(255, 255, 255, 0.04) `dark.border.default`; radius 4px; background transparent; text PolySans 16/12 400, #f5f5f0 `dark.text.primary`.

![Param row checkbox default](components/crops/app-param-checkbox-default.png)

#### Response empty state
The response panel before any send ("Not sent" — the send surface is never fired, so this resting panel is the honest evidence). Read as `app-response-empty` on the /app page.
Read on 2026-11-17T13:08:50.297Z.

**Values (default).** size 599.3 x 712; background transparent; text PolySans 14.2/24 400, rgba(245, 245, 240, 0.6) `dark.text.secondary`; icon 48 x 48, rgba(245, 245, 240, 0.6) `dark.text.secondary`; layers div.PanelState_iconCircle__DPIoa.mb-2 64.0x64.0 rgba(255, 255, 255, 0.04) 9999px.

Child layers that carry the look: div 64x64 background rgba(255, 255, 255, 0.04) `dark.border.default` radius 9999px.

![Response empty state default](components/crops/app-response-empty-default.png)

#### Auth panel (opened)
The Auth tab's panel: the "No authentication" select with None / Basic auth / Bearer token / API key options. The tab's own press opens it. Read as `app-auth-tab` on the /app page.
Read on 2026-11-17T10:24:55.184Z.

**Values (opened).** size 118 x 24; background transparent; text PolySans 14.2/24 400, rgba(245, 245, 240, 0.6) `dark.text.secondary`.

![Auth panel (opened) opened](components/crops/app-auth-tab-opened.png)

#### Body panel (opened)
The Body tab's panel: the body-type select (None / Text / Form / File / GraphQL). Read as `app-body-tab` on the /app page.
Read on 2026-11-17T10:24:57.075Z.

**Values (opened).** size 53 x 24; background transparent; text PolySans 14.2/24 400, rgba(245, 245, 240, 0.6) `dark.text.secondary`.

![Body panel (opened) opened](components/crops/app-body-tab-opened.png)

#### Auth type select
The "None" auth-type control inside the opened Auth panel — measured, its menu never opened. Read as `app-auth-select` on the /app page.
States read on 2026-11-17T10:24:58.921Z (default); 2026-11-17T10:25:00.833Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 74 x 24; padding 4px 8px; radius 4px; background rgba(255, 255, 255, 0.04) `dark.border.default`; shadow rgba(255, 255, 255, 0.02) 0px 0px 0px 1px inset, rgba(0, 0, 0, 0.25) 0px 1px 2px 0px; text PolySans 12.8/16 400, rgba(245, 245, 240, 0.6) `dark.text.secondary`; icon 16 x 16, rgba(245, 245, 240, 0.6) `dark.text.secondary` |
| hover | background rgba(255, 255, 255, 0.06) `dark.item.selected` |

![Auth type select default](components/crops/app-auth-select-default.png) ![Auth type select hover](components/crops/app-auth-select-hover.png)

### Environments

The environments manager the Environments button opens: Variables/Settings/Defaults tabs and 'Create environment' — measured, never pressed.

#### Environments manager
The environments manager (Variables / Settings / Defaults tabs, "Create environment"), opened by the Environments selector's own press. Read as `app-env-panel` on the /app page.
States read on 2026-11-17T13:09:36.622Z (opened); 2026-11-17T13:10:04.153Z (light).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| opened | size 1026.5 x 796; background #1c1818 `dark.bg.z1`; text PolySans 14.2/24 400, #f5f5f0 `dark.text.primary`; icon 16 x 16, rgba(245, 245, 240, 0.6) `dark.text.secondary` |
| light | background #f5f5f0 `dark.text.primary`; text PolySans 14.2/24 400, #1c1818 `dark.bg.z1`; icon 16 x 16, rgba(28, 24, 24, 0.6) `light.text.secondary` |

![Environments manager opened](components/crops/app-env-panel-opened.png) ![Environments manager light](components/crops/app-env-panel-light.png)

#### "Create environment" button
The environments manager's primary action — measured, never pressed. Read as `app-env-create` on the /app page.
States read on 2026-11-17T10:12:57.760Z (default); 2026-11-17T10:13:00.123Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 147 x 24; padding 4px 8px; radius 4px; background transparent; text PolySans 12.8/16 400, rgba(245, 245, 240, 0.6) `dark.text.secondary`; icon 16 x 16, rgba(245, 245, 240, 0.6) `dark.text.secondary` |
| hover | background rgba(255, 255, 255, 0.03) `dark.item.hover` |

!["Create environment" button default](components/crops/app-env-create-default.png) !["Create environment" button hover](components/crops/app-env-create-hover.png)

### Site chrome (mobile)

The 390px surface: the nav, links wrapped.

#### Mobile nav
The nav at 390px (links wrap; no hamburger). Read as `m-nav` on the / page.
Read on 2026-11-17T09:41:05.050Z.

**Values (default).** size 390 x 85; padding 0px 16px; background transparent; text Pie Body 16/24 400, #f5f5f0 `dark.text.primary`; layers span.Count_count__p9ULf.Navigation_count__CXLW6 0.0x0.0 #363636 9999px; button.Button_button__mg_cR.Button_primary__PFIP8 0.0x0.0 #73dc8c T:2px solid / R:2px solid / B:2px solid / L:2px solid 9999px; div.Navigation_featuredIconCircle__n4aZN 45.0x45.0 #363636 9999px.

Child layers that carry the look: span 0x0 background #363636 `light.code.primary` radius 9999px; button 0x0 background #73dc8c `dark.accent.default` border 2px solid radius 9999px; div 45x45 background #363636 `light.code.primary` radius 9999px.

![Mobile nav default](components/crops/m-nav-default.png)

## Icons

42 distinct inline-SVG icons were collected from the live pages into [icons/](icons) by `tools/capture/icons.mjs`, indexed in [icons/INDEX.tsv](icons/INDEX.tsv): a file is named from `tools/capture/icon-names.tsv` where its geometry hash is listed, else the label or class of the control it sits in, else `icon-<hash>`; colour is kept as `currentColor` wherever it matched the text colour, so each icon recolours from CSS `color` the way it does on the site. The icons are the product's artwork — borrow the set's grammar (sizes, stroke-vs-fill, naming roles), never the artwork itself.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|
| [star-on-github-47-961](icons/star-on-github-47-961.svg) | 16x16 17x17 20x20 | 0 0 16 16 | fill | home; desktop; cli; ai; docs; docs-desktop; docs-cli; jobs; blog; blog-post; download; about; search dialog; mobile; light | Star on GitHub 47,961 / Star 38,722 / Edit on GitHub |
| [share-on-twitter](icons/share-on-twitter.svg) | 16x13 17x14 20x20 28x23 | 0 0 16 13 | fill | home; desktop; cli; ai; docs; docs-desktop; docs-cli; jobs; blog; blog-post; download; about; search dialog; mobile; light | Share on Twitter / Follow @httpie / Twitter |
| [discord](icons/discord.svg) | 16x19 17x20 | 0 0 16 19 | fill | home; desktop; cli; ai; docs; docs-desktop; docs-cli; jobs; blog; blog-post; download; about; search dialog; mobile; light | Discord |
| [socialicon](icons/socialicon-3df105f6.svg) | 16x16 | 0 0 16 16 | fill | home; desktop; cli; docs; docs-desktop; docs-cli; jobs; blog; blog-post; download; about; search dialog; mobile; light |  |
| [socialicon](icons/socialicon-6d0eaa0e.svg) | 16x18 | 0 0 448 512 | fill | home; desktop; cli; docs; docs-desktop; docs-cli; jobs; blog; blog-post; download; about; search dialog; mobile; light |  |
| [linkedin](icons/linkedin.svg) | 16x16 20x20 26x26 | 0 0 16 16 | fill | home; desktop; cli; download; about; mobile; light |  |
| [show-more-love](icons/show-more-love.svg) | 16x14 | 0 0 16 14 | fill | home; desktop; cli; jobs; download; mobile; light | Show more love / See more |
| [icon](icons/icon-0070315b.svg) | 10x13 14x18 | 0 0 17 22 | fill | home; cli; docs-desktop; docs-cli; mobile; light |  |
| [get-the-mac-app](icons/get-the-mac-app.svg) | 14x17 17x21 23x29 | 0 0 16 20 | fill | home; desktop; cli; download; mobile; light | Get the Mac App / Download for Mac (Intel) / Download for Ma |
| [facebook](icons/facebook.svg) | 18x18 30x30 | 0 0 16 16 | fill | home; desktop; cli; download; mobile; light |  |
| [google](icons/google.svg) | 17x17 28x28 | 0 0 16 16 | fill | home; desktop; cli; download; mobile; light |  |
| [amazon](icons/amazon.svg) | 22x20 36x34 | 0 0 16 15 | fill | home; desktop; cli; download; mobile; light |  |
| [brew](icons/brew.svg) | 12x10 12x22 17x14 | 0 0 12 10 | fill | home; cli; docs-cli; blog-post; mobile; light | brew / Version: 3.2.4 2024-11-01 (latest) / Download |
| [spotify](icons/spotify.svg) | 30x30 | 0 0 16 16 | fill | home; desktop; cli; download; light |  |
| [collapse](icons/collapse.svg) | 12x12 | 0 0 12 12 | fill | app; app method menu | Collapse |
| [collection](icons/collection.svg) | 12x12 | 0 0 12 12 | stroke | app; app method menu | Collection |
| [icon](icons/icon-1d0b1e6a.svg) | 16x16 | 0 0 16 16 | stroke | app; app method menu |  |
| [icon](icons/icon-302559ca.svg) | 16x16 | 0 0 16 16 | stroke | app; app method menu |  |
| [avatar](icons/avatar.svg) | 24x24 | 0 0 24 24 | fill | app; app method menu |  |
| [icon](icons/icon-52db8db9.svg) | 48x48 | 0 0 48 48 | stroke | app; app method menu |  |
| [get](icons/get-5bbeb224.svg) | 12x12 | 0 0 12 12 | fill | app; app method menu | GET |
| [environments](icons/environments.svg) | 16x16 | 0 0 16 16 | fill | app; app method menu | Environments |
| [icon](icons/icon-6344bfb8.svg) | 16x16 | 0 0 16 16 | stroke | app; app method menu |  |
| [icon](icons/icon-6409cde8.svg) | 24x24 | 0 0 24 24 | fill | app; app method menu |  |
| [incognito-space](icons/incognito-space.svg) | 16x16 | 0 0 16 16 | fill | app; app method menu | Incognito space |
| [loader](icons/loader.svg) | 24x24 | 0 0 24 24 | fill | app; app method menu |  |
| [icon](icons/icon-7005be5a.svg) | 16x16 | 0 0 16 16 | fill | app; app method menu |  |
| [close-tab](icons/close-tab.svg) | 12x12 | 0 0 12 12 | stroke | app; app method menu | Close tab |
| [icon](icons/icon-78f95929.svg) | 16x16 | 0 0 16 16 | fill | app; app method menu |  |
| [icon](icons/icon-8d193ae6.svg) | 16x16 | 0 0 16 16 | fill | app; app method menu |  |
| [logo](icons/logo.svg) | 30x32 | 0 0 22 24 | fill | app; app method menu |  |
| [icon](icons/icon-eafe1641.svg) | 24x24 | 0 0 24 24 | fill | app; app method menu |  |
| [icon](icons/icon-fb9960e8.svg) | 24x24 | 0 0 24 24 | fill | app; app method menu |  |
| [closeicon](icons/closeicon.svg) | 36x36 | 0 0 12 12 | fill | mobile |  |
| [footer-icon](icons/footer-icon.svg) | 16x16 | 0 0 16 16 | fill | ai | Read HTTPie AI 1.0 announcement |
| [download-for-windows](icons/download-for-windows.svg) | 16x16 | 0 0 16 16 | fill | download | Download for Windows |
| [get](icons/get-3a8487e9.svg) | 16x16 | 0 0 16 16 | stroke | app method menu | GET |
| [featuredicon](icons/featuredicon.svg) | 18x10 | 0 0 16 9 | fill | mobile |  |
| [download-for-linux](icons/download-for-linux.svg) | 16x18 | 0 0 16 18 | fill | download | Download for Linux |
| [icon](icons/icon-9809fee7.svg) | 26x26 | 0 0 24 24 | stroke | app |  |
| [custom](icons/custom.svg) | 16x16 | 0 0 16 16 | stroke | app method menu | Custom |
| [httpie-ai](icons/httpie-ai.svg) | 24x24 | 0 0 24 24 | fill | app | HTTPie AI |

## Gaps

### The blocked product surfaces

The signed-in product was never entered: HTTPie-for-Web runs signed out in its 'Incognito space', and the sign-in entry points (named spaces, sync, shared collections) were never used and no account was created. The **HTTPie AI 'Try it out'** action inside /app was never pressed — generation is an account/paid feature. The **desktop app and CLI binaries** behind /download were never fetched — only the marketing pages that describe them were captured. **/pricing** answers 404 (captured as the not-found page) and **/discord** redirects off-site to discord.com. All are documented as boundaries, never faked.

### Pages

- **Sign-in / account surfaces** — named spaces, synced collections, shared workspaces: the incognito product's own boundary, never entered.
- **HTTPie AI 'Try it out'** — the assistant action inside /app; generation is an account feature, never pressed.
- **The native desktop app and CLI binaries** — /download links to builds; only the marketing pages were captured.
- **/pricing** — 404; the capture records the not-found page itself, not a pricing surface.
- **/discord and the social links** — off-site redirects (discord.com, twitter.com, github.com); external surfaces, out of scope.
- **/app on a phone** — the client shell renders at 390 but the request builder is desktop-first; the mobile shots are a limited read of it.
- **Long pages** — /blog (~15.5k px) and /terms (~19.9k px) shots are bounded at eight chunks; the sidecars record the boundary.

### States

- **Pressed** was forced with DevTools on the controls that carry it, so a state a script adds on mousedown (if any) is missing.
- **The search field was never typed into** — the docs' ⌘K DocSearch dialog was opened for its icons and closed with Escape; no query was run, so result lists are uncaptured.
- **The newsletter email fields were never typed into or submitted** — clicked into for the focus look only.
- **Send was never pressed** — issuing a request is a network side effect, so the Response tab's resting 'Not sent' panel is the honest signed-out evidence and the used response surface (status line, headers, pretty/raw body) is an uncaptured boundary.
- **'Import', 'Migrate your data' and 'Create environment'** — measured, never pressed (they write state or open pickers).
- **The theme radios** painted the `light` states and shots, then DARK MODE was restored — the theme choice is persisted in localStorage.theme, which /app reads as the same signal.

### Themes

httpie.io boots `html.dark` — AUTO follows prefers-color-scheme and headless Chromium's light preference still resolves dark, so `dark` is the painted default. The footer's ThemeToggle radio stack (LIGHT MODE / AUTO / DARK MODE) repaints `html.light` and persists to localStorage.theme, which /app reads: `light` states and `{page}-light-*` screenshots were painted through that control, verified by the painted surface (html class, color-scheme and the computed background), and DARK was restored afterwards. Both token themes resolve the same `--color-*` declarations — `.dark:root` re-points them.

### Fonts

- **The Pie faces are proprietary and never shipped**: 'Pie Headline' is FK Screamer (the display face), 'Pie Body' is PolyPie (text and UI), 'Pie Monospace' covers code and the URL field, 'Pie Symbols' the icons — their woff2 files under /_next/static/media are licensed assets, declared and measured by name only. The style guide falls back to system faces.

### Screenshots

- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.
- The rendered brand strings on the captured pages (the wordmark and copy) are the product's published content.
- Public author names, handles and avatars on the captured tweet cards and the jobs page are published content and are kept; nothing private was captured.

### Content left out

- Article copy, changelog text and testimonial tweets are the product's published content; only frames and components were measured.
