# Hashnode components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Read from hashnode.com and townhall.hashnode.com on 2026-11-17, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Later recaptures merge into the same file, so every entry names the date its own states were read; a state a re-read missed keeps its earlier date and says so. Nothing was signed into, bought, searched or submitted; the only presses were local UI toggles the page's own chrome provides — the ⌘K search dialogs, the Theme and More menus, the sidebar toggle, FAQ accordions, changelog and install tabs, and the phone's navigation sheet; every link was measured, never followed.

**Where this was read.** Two public surfaces carry the system: hashnode.com itself — the signed-out marketing pages, feed, public posts, profiles and product sections — and townhall.hashnode.com, the official blog on the hosted blog engine (one design system: the same custom-property layer resolves to the same values, and the blog adds prose roles like --reading-text). engineering.hashnode.com answered 429 from the capture host; help/docs/blog/api/support/changelog/weekly subdomains do not resolve; /login and everything behind it was never entered. All of those are boundaries listed under Gaps, not captures.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (69 components, 144 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Inter 16/20.8 400, #000000`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (137 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-{state}.png` where `{theme}` is the surface the page painted at capture: every page boots `light`; `{page}-dark-*` shots on hashnode.com are the same page after the sidebar's own Theme menu (Light / Dark / System) repainted html.dark, verified by the painted surface and switched back after; on `th-*` blog pages dark was painted by emulated `prefers-color-scheme: dark` + reload — the signal the engine honours, since its toggle produced no repaint headless. Desktop shots are 1440 x 900 at 1x; `-full` shots are the whole page at 1x — hashnode.com scrolls inside a viewport-high pane, relaxed to natural height for the shot and restored after — bounded at eight chunks with the boundary recorded in the shot's `.capture.json` sidecar; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x). `blog-light-*` is hashnode.com/blog, which redirects to the Town Hall index.

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-dark-default.png), [full](screenshots/home-dark-full.png), [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [menu](screenshots/home-light-menu.png), [search](screenshots/home-light-search.png), [theme-menu](screenshots/home-light-theme-menu.png) |
| Feed | `/feed` | [default](screenshots/feed-dark-default.png), [full](screenshots/feed-dark-full.png), [default](screenshots/feed-light-default.png), [full](screenshots/feed-light-full.png) |
| Public post | `/posts/…` | [default](screenshots/post-dark-default.png), [full](screenshots/post-dark-full.png), [default](screenshots/post-light-default.png), [full](screenshots/post-light-full.png) |
| Public profile | `/@anish78` | [default](screenshots/profile-light-default.png), [full](screenshots/profile-light-full.png) |
| Hashnode Pro | `/pro` | [default](screenshots/pro-dark-default.png), [full](screenshots/pro-dark-full.png), [default](screenshots/pro-light-default.png), [faq-open](screenshots/pro-light-faq-open.png), [full](screenshots/pro-light-full.png) |
| Hashnode for Agents | `/agents` | [default](screenshots/agents-light-default.png), [full](screenshots/agents-light-full.png), [tab-cli](screenshots/agents-light-tab-cli.png) |
| Changelog | `/changelog` | [default](screenshots/changelog-dark-default.png), [full](screenshots/changelog-dark-full.png), [default](screenshots/changelog-light-default.png), [full](screenshots/changelog-light-full.png), [tab-features](screenshots/changelog-light-tab-features.png) |
| Hackathons | `/hackathons` | [default](screenshots/hackathons-light-default.png), [full](screenshots/hackathons-light-full.png) |
| Brand | `/brand` | [default](screenshots/brand-light-default.png), [full](screenshots/brand-light-full.png) |
| Alternatives: Medium | `/alternatives/medium` | [default](screenshots/alt-medium-light-default.png), [full](screenshots/alt-medium-light-full.png) |
| Code of conduct | `/code-of-conduct` | [default](screenshots/code-of-conduct-light-default.png), [full](screenshots/code-of-conduct-light-full.png) |
| Onboarding (rest only) | `/onboard` | [default](screenshots/onboard-light-default.png), [full](screenshots/onboard-light-full.png) |
| Blog redirect | `/blog → townhall.hashnode.com` | [default](screenshots/blog-light-default.png), [full](screenshots/blog-light-full.png) |
| Town Hall index | `townhall.hashnode.com/` | [default](screenshots/th-home-dark-default.png), [default](screenshots/th-home-light-default.png), [full](screenshots/th-home-light-full.png), [menu](screenshots/th-home-light-menu.png), [search](screenshots/th-home-light-search.png) |
| Town Hall article | `townhall.hashnode.com/…e2e-testing…` | [default](screenshots/th-post-dark-default.png), [default](screenshots/th-post-light-default.png), [full](screenshots/th-post-light-full.png) |
| Town Hall archive | `townhall.hashnode.com/archive` | [default](screenshots/th-archive-light-default.png), [full](screenshots/th-archive-light-full.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [drawer](screenshots/mobile-home-light-drawer.png), [full](screenshots/mobile-home-light-full.png) |
| Feed, phone | `/feed` | [default](screenshots/mobile-feed-light-default.png), [full](screenshots/mobile-feed-light-full.png) |
| Public post, phone | `/posts/…` | [default](screenshots/mobile-post-light-default.png), [full](screenshots/mobile-post-light-full.png) |
| Pro, phone | `/pro` | [default](screenshots/mobile-pro-light-default.png), [full](screenshots/mobile-pro-light-full.png) |
| Town Hall, phone | `townhall.hashnode.com/` | [default](screenshots/mobile-th-home-light-default.png), [full](screenshots/mobile-th-home-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Search dialog (⌘K) | home, Town Hall index | the page's own Search button / Ctrl+K — the dialog opened, captured and closed with Escape; nothing was searched | [home-light-search](screenshots/home-light-search.png), [th-home-light-search](screenshots/th-home-light-search.png) |
| Theme menu | home sidebar | the 'Theme' button's own press — the Light / Dark / System menu opened, captured, closed | [home-light-theme-menu](screenshots/home-light-theme-menu.png) |
| More menu | home sidebar, Town Hall header | the 'More' button's own press, closed with Escape | [home-light-menu](screenshots/home-light-menu.png), [th-home-light-menu](screenshots/th-home-light-menu.png) |
| FAQ accordion | Hashnode Pro | a question row's own press — the answer expanded | [pro-light-faq-open](screenshots/pro-light-faq-open.png) |
| Category tab | changelog | the 'Features' tab's own activation — a local UI toggle | [changelog-light-tab-features](screenshots/changelog-light-tab-features.png) |
| Install tab | Hashnode for Agents | the 'CLI' tab's own activation | [agents-light-tab-cli](screenshots/agents-light-tab-cli.png) |
| Mobile nav sheet | home, phone width | the 'Open menu' button's own press | [mobile-home-light-drawer](screenshots/mobile-home-light-drawer.png) |
| Dark theme | hashnode.com pages | the Theme menu's own 'Dark' choice; the painted surface was verified before each shot, then switched back | [home-dark-default](screenshots/home-dark-default.png), [post-dark-default](screenshots/post-dark-default.png) |
| Dark theme (blog engine) | townhall.hashnode.com | emulated prefers-color-scheme: dark + reload — the engine's own OS-preference path; its 'Toggle theme' button produced no repaint headless | [th-home-dark-default](screenshots/th-home-dark-default.png), [th-post-dark-default](screenshots/th-post-dark-default.png) |
| Sign-in, signup, dashboard | /login and everything behind it | the auth wall — never entered | boundary; see Gaps |
| Engineering blog, help centre, docs | engineering. / help. / docs. subdomains | 429 rate-limit and NXDOMAIN from the capture host — never reached | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 20 components were given a real keyboard focus. 9 draw an outline ring: `post-title-link` (2px solid lab(61.3712 9.00993 -60.4412), offset 2px), `post-upvote` (2px solid lab(61.3712 9.00993 -60.4412), offset 2px), `post-bookmark` (2px solid lab(61.3712 9.00993 -60.4412), offset 2px), `post-share` (2px solid lab(46.0225 28.2872 -84.5408), offset 2px), `changelog-tab` (1px solid lab(46.0225 28.2872 -84.5408), offset 2px), `agents-copy` (2px solid lab(61.3712 9.00993 -60.4412), offset 2px), `th-nav-link` (2px solid lab(46.0225 28.2872 -84.5408), offset 2px), `th-search-button` (2px solid lab(46.0225 28.2872 -84.5408), offset 2px), `th-prose-link` (2px solid lab(46.0225 28.2872 -84.5408), offset 2px). 9 draw a focus ring as a shadow instead: `app-nav-link`, `app-search-button`, `feed-load-more`, `profile-share`, `faq-question`, `onboard-combobox`, `onboard-textarea`, `onboard-next`, `th-load-more`. The other 2 show no measured change: `app-cta`, `comment-submit`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.15s | `cubic-bezier(0.16, 1, 0.3, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, all, background-color, border-color, box-shadow, color, fill, height, outline-color, padding, stroke, text-decoration-color, width | agents-copy, agents-tab, app-cta, app-more-menu, app-nav-active, app-nav-link, app-search-button, app-sidebar-toggle and more |
| 0.15s | `cubic-bezier(0.4, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, background-color, border-color, color, fill, outline-color, stroke, text-decoration-color | th-load-more, th-more-menu, th-nav-link, th-page-prev, th-search-button, th-theme-toggle, th-toc-link |
| 0.15s | `ease` | text-decoration-color | th-prose-link |
| 0.2s | `cubic-bezier(0.16, 1, 0.3, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, background-color, border-color, color, fill, outline-color, stroke, text-decoration-color | post-card |
| 0.2s | `ease` | all | app-search-dialog, th-search-dialog |
| 0.3s | `cubic-bezier(0.4, 0, 0.2, 1)` | rotate, scale, transform, translate | m-th-header, th-header |
| 0.5s | `cubic-bezier(0.4, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, -webkit-backdrop-filter, backdrop-filter, background-color, border-color, box-shadow, color, content-visibility, display, fill, filter, opacity, outline-color, overlay, pointer-events, rotate, scale, stroke, text-decoration-color, transform, translate | m-app-drawer |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Search dialog](#search-dialog) | 672 x 594 | 1px solid lab(90.4636 -0.177681 -2.26592) | 12px | lab(100 0 0) | rgba(19, 22, 28, 0.06) 0px 1px 2px 0px, rgba(19, 22, 28, 0.22) 0px 12px 32px -12px | 0 |
| [App sidebar](#app-sidebar) | 1440 x 900 | - | - | transparent | none | 0 |
| [Feed post card](#feed-post-card) | 1020 x 293.16 | - | - | transparent | none | 0 |
| [Comment textarea](#comment-textarea) | 670 x 72 | - | - | transparent | none | 12px 16px |
| [Main navigation pill](#main-navigation-pill) | 468.59 x 36 | - | - | transparent | none | 0 |
| [Post card](#post-card) | 651.59 x 514.08 | - | - | transparent | none | 0 |
| [Nav sheet (open)](#nav-sheet-open) | 288 x 844 | R: 1px solid lab(90.4636 -0.177681 -2.26592) | - | lab(97.552 -0.0918508 -1.13482) | rgba(19, 22, 28, 0.06) 0px 1px 2px 0px, rgba(19, 22, 28, 0.22) 0px 12px 32px -12px | 0 |

## Components

### App chrome

The viewport-high shell every hashnode.com page carries: the left sidebar (logo, Home/Feed/Pro/Agents nav, the Search ⌘K / Theme / More menu buttons, the 'Start your blog' CTA and Sign-in link), its collapse toggle, and the sign-up call-to-action that links to /login — measured, never followed.

#### App sidebar
The left sidebar (bg-sidebar): logo, Home/Feed/Pro/Agents nav links, the Search / Theme / More menu buttons, sidebar footer with the resource links and the Sign-in link. Read as `app-sidebar` on the / page.
States read on 2026-11-17T04:06:34.697Z (default); 2026-11-17T04:06:55.419Z (dark).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 1440 x 900; background transparent; text -apple-system 16/24 400, lab(7.16472 -0.140898 -4.74486); icon 16 x 16, lab(43.1077 -0.29406 -4.49811); layers div.bg-sidebar.group-data-[variant=floating]:border-sidebar-border 64.0x876.0 lab(97.552 -0.0918508 -1.13482) rgba(0, 0, 0, 0) 0px 0px 0px 0px, oklab(0.199999 -0.00136095 -0.0129235 / 0.06) 0px 0px 0px 1px inset, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px 28px; button.peer/menu-button.flex 40.0x40.0 lab(100 0 0) rgba(0, 0, 0, 0) 0px 0px 0px |
| dark | text -apple-system 16/24 400, lab(91.8598 -0.149757 -1.88929); icon 16 x 16, lab(67.6029 -0.225931 -3.01496); layers div.bg-sidebar.group-data-[variant=floating]:border-sidebar-border 64.0x876.0 lab(1.96624 -0.036478 -1.47524) rgba(0, 0, 0, 0) 0px 0px 0px 0px, oklab(0.929998 -0.000531942 -0.00495064 / 0.06) 0px 0px 0px 1px inset, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px 28px; button.peer/menu-button.flex 40.0x40.0 lab(7.73499 -0.163585 -3.70654) rgba(0, |

Child layers that carry the look: div 64x876 background lab(97.552 -0.0918508 -1.13482) radius 28px shadow transparent 0px 0px 0px 0px, oklab(0.199999 -0.00136095 -0.0129235 / 0.06) 0px 0px 0px 1px inset, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px; button 40x40 background lab(100 0 0) radius 3.35544e+07px shadow transparent 0px 0px 0px 0px, lab(90.4636 -0.177681 -2.26592) 0px 0px 0px 1px inset, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(19, 22, 28, 0.05) 0px 1px 2px 0px; kbd 0x0 background lab(95.8079 -0.121295 -1.51228) radius 6px.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Sidebar nav link
A primary nav link in the sidebar ("Feed"), a peer/menu-button row. Read as `app-nav-link` on the / page.
States read on 2026-11-17T04:06:58.359Z (default); 2026-11-17T04:07:00.187Z (hover); 2026-11-17T04:07:01.677Z (focus-visible).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 40 x 40; padding 12px; radius 3.35544e+07px; background transparent; text -apple-system 14/20 400, lab(7.16472 -0.140898 -4.74486); transition width 0.15s cubic-bezier(0.16, 1, 0.3, 1), height 0.15s cubic-bezier(0.16, 1, 0.3, 1), padding 0.15s cubic-bezier(0.16, 1, 0.3, 1), color 0.15s cubic-bezier(0.16, 1, 0.3, 1); icon 16 x 16, lab(43.1077 -0.29406 -4.49811) |
| hover | background lab(93.0156 -0.17792 -2.26609); icon 16 x 16, lab(7.16472 -0.140898 -4.74486) |
| focus-visible | shadow lab(42.9458 7.59417 -58.6769) 0px 0px 0px 2px; layers a.peer/menu-button.flex 40.0x40.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, lab(42.9458 7.59417 -58.6769) 0px 0px 0px 2px, rgba(0, 0, 0, 0) 0px 0px 0px 0px 3.35544e+07px |

![Sidebar nav link default](components/crops/app-nav-link-default.png) ![Sidebar nav link hover](components/crops/app-nav-link-hover.png) ![Sidebar nav link focus-visible](components/crops/app-nav-link-focus-visible.png)

#### Sidebar active nav link
The link for the page being read ("Home"), painted with the active style. Read as `app-nav-active` on the / page.
Read on 2026-11-17T04:07:02.829Z.

**Values (default).** size 40 x 40; padding 12px; radius 3.35544e+07px; background lab(100 0 0); shadow lab(90.4636 -0.177681 -2.26592) 0px 0px 0px 1px inset, rgba(19, 22, 28, 0.05) 0px 1px 2px 0px; text -apple-system 14/20 600, lab(7.16472 -0.140898 -4.74486); transition width 0.15s cubic-bezier(0.16, 1, 0.3, 1), height 0.15s cubic-bezier(0.16, 1, 0.3, 1), padding 0.15s cubic-bezier(0.16, 1, 0.3, 1), color 0.15s cubic-bezier(0.16, 1, 0.3, 1); icon 16 x 16, lab(7.16472 -0.140898 -4.74486).

![Sidebar active nav link default](components/crops/app-nav-active-default.png)

#### "Toggle Sidebar" button
The sidebar footer control that collapses the rail — a local UI toggle. "opened" is its own press (the rail collapsed), restored afterwards. Read as `app-sidebar-toggle` on the / page.
States read on 2026-11-17T04:07:03.726Z (opened); 2026-11-17T04:07:06.354Z (default); 2026-11-17T04:07:10.108Z (hover). `opened` failed at capture (locator.evaluate: Timeout 8000ms exceeded.).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 40 x 40; radius 3.35544e+07px; background transparent; text -apple-system 14/20 600, lab(43.1077 -0.29406 -4.49811); transition all 0.15s cubic-bezier(0.16, 1, 0.3, 1); icon 16 x 16, lab(43.1077 -0.29406 -4.49811) |
| hover | background lab(93.0156 -0.17792 -2.26609); text -apple-system 14/20 600, lab(7.16472 -0.140898 -4.74486); icon 16 x 16, lab(7.16472 -0.140898 -4.74486) |

!["Toggle Sidebar" button default](components/crops/app-sidebar-toggle-default.png) !["Toggle Sidebar" button hover](components/crops/app-sidebar-toggle-hover.png)

#### Search button (Ctrl K)
The sidebar "Search" menu-button carrying the ⌘K hint; opens the command search dialog. Read as `app-search-button` on the / page.
States read on 2026-11-17T04:07:40.847Z (default); 2026-11-17T04:07:43.100Z (hover); 2026-11-17T04:07:46.464Z (focus-visible).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 232 x 36; padding 8px 12px; radius 3.35544e+07px; background lab(100 0 0); shadow lab(90.4636 -0.177681 -2.26592) 0px 0px 0px 1px inset, rgba(19, 22, 28, 0.05) 0px 1px 2px 0px; text -apple-system 14/20 400, lab(43.1077 -0.29406 -4.49811); transition width 0.15s cubic-bezier(0.16, 1, 0.3, 1), height 0.15s cubic-bezier(0.16, 1, 0.3, 1), padding 0.15s cubic-bezier(0.16, 1, 0.3, 1), color 0.15s cubic-bezier(0.16, 1, 0.3, 1); icon 18 x 18, lab(43.1077 -0.29406 -4.49811) |
| hover | icon 18 x 18, lab(7.16472 -0.140898 -4.74486) |
| focus-visible | shadow lab(90.4636 -0.177681 -2.26592) 0px 0px 0px 1px inset, lab(42.9458 7.59417 -58.6769) 0px 0px 0px 2px, rgba(19, 22, 28, 0.05) 0px 1px 2px 0px |

![Search button (Ctrl K) default](components/crops/app-search-button-default.png) ![Search button (Ctrl K) hover](components/crops/app-search-button-hover.png) ![Search button (Ctrl K) focus-visible](components/crops/app-search-button-focus-visible.png)

#### Theme menu button
The "Theme" menu-button that opens Light / Dark / System. "opened" is its own press; the menu is then closed with Escape. Read as `app-theme-button` on the / page.
States read on 2026-11-17T04:07:47.797Z (default); 2026-11-17T04:07:49.986Z (opened); 2026-11-17T04:07:50.868Z (opened-menu).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: opened, opened-menu) | size 97.33 x 32; padding 8px 12px; radius 3.35544e+07px; background transparent; text -apple-system 14/20 400, lab(7.16472 -0.140898 -4.74486); transition width 0.15s cubic-bezier(0.16, 1, 0.3, 1), height 0.15s cubic-bezier(0.16, 1, 0.3, 1), padding 0.15s cubic-bezier(0.16, 1, 0.3, 1), color 0.15s cubic-bezier(0.16, 1, 0.3, 1); icon 18 x 18, lab(43.1077 -0.29406 -4.49811) |

![Theme menu button default](components/crops/app-theme-button-default.png) ![Theme menu button opened](components/crops/app-theme-button-opened.png) ![Theme menu button opened-menu](components/crops/app-theme-button-opened-menu.png)

#### "More" menu button
The "More" menu-button (carries a "New" badge) opening the overflow nav menu. "opened" is its own press, closed with Escape. Read as `app-more-menu` on the / page.
States read on 2026-11-17T04:07:53.928Z (default); 2026-11-17T04:07:56.089Z (hover); 2026-11-17T04:08:01.926Z (opened).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, opened) | size 130.67 x 32; padding 8px 12px; radius 3.35544e+07px; background transparent; text -apple-system 14/20 400, lab(7.16472 -0.140898 -4.74486); transition width 0.15s cubic-bezier(0.16, 1, 0.3, 1), height 0.15s cubic-bezier(0.16, 1, 0.3, 1), padding 0.15s cubic-bezier(0.16, 1, 0.3, 1), color 0.15s cubic-bezier(0.16, 1, 0.3, 1); icon 16 x 16, lab(43.1077 -0.29406 -4.49811); layers span.absolute.-right-1 0.0x0.0 lab(46.0225 28.2872 -84.5408) 3.35544e+07px; span.ml-auto.inline-flex 40.9x18.0 lab(46.0225 28.2872 -84.5408) 3.35544e+07px |

Child layers that carry the look: span 0x0 background lab(46.0225 28.2872 -84.5408) radius 3.35544e+07px; span 40.9x18 background lab(46.0225 28.2872 -84.5408) radius 3.35544e+07px.

!["More" menu button default](components/crops/app-more-menu-default.png) !["More" menu button hover](components/crops/app-more-menu-hover.png) !["More" menu button opened](components/crops/app-more-menu-opened.png)

#### "Start your blog, free" CTA
The solid sign-up call-to-action in the sidebar footer (bg-primary text-primary-foreground, rounded-full). Links to /login — measured, never followed. Read as `app-cta` on the / page.
States read on 2026-11-17T04:08:03.899Z (default); 2026-11-17T04:08:05.894Z (hover); 2026-11-17T04:08:07.236Z (focus-visible); 2026-11-17T04:08:36.866Z (pressed); 2026-11-17T04:08:43.651Z (dark).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 242.55 x 56; padding 0px 28px; radius 3.35544e+07px; background lab(9.58302 -0.18093 -4.0814); shadow rgba(19, 22, 28, 0.06) 0px 1px 2px 0px, rgba(19, 22, 28, 0.22) 0px 12px 32px -12px; text -apple-system 16/24 600, lab(100 0 0); transition all 0.15s cubic-bezier(0.16, 1, 0.3, 1); icon 18 x 18, lab(100 0 0) |
| dark | background lab(91.8598 -0.149757 -1.88929); shadow rgba(0, 0, 0, 0.4) 0px 1px 2px 0px, rgba(0, 0, 0, 0.6) 0px 12px 32px -12px; text -apple-system 16/24 600, lab(7.73499 -0.163585 -3.70654); icon 18 x 18, lab(7.73499 -0.163585 -3.70654) |

!["Start your blog, free" CTA default](components/crops/app-cta-default.png) !["Start your blog, free" CTA hover](components/crops/app-cta-hover.png) !["Start your blog, free" CTA focus-visible](components/crops/app-cta-focus-visible.png) !["Start your blog, free" CTA pressed](components/crops/app-cta-pressed.png) !["Start your blog, free" CTA dark](components/crops/app-cta-dark.png)

#### "Sign in" link
The quiet sign-in link in the sidebar footer — measured, never followed. Read as `app-signin` on the / page.
States read on 2026-11-17T04:08:46.507Z (default); 2026-11-17T04:08:55.218Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 232 x 40; padding 8px 12px; radius 3.35544e+07px; background lab(100 0 0); shadow lab(90.4636 -0.177681 -2.26592) 0px 0px 0px 1px inset, rgba(19, 22, 28, 0.05) 0px 1px 2px 0px; text -apple-system 14/20 600, lab(7.16472 -0.140898 -4.74486); transition width 0.15s cubic-bezier(0.16, 1, 0.3, 1), height 0.15s cubic-bezier(0.16, 1, 0.3, 1), padding 0.15s cubic-bezier(0.16, 1, 0.3, 1), color 0.15s cubic-bezier(0.16, 1, 0.3, 1); icon 18 x 18, lab(7.16472 -0.140898 -4.74486) |

!["Sign in" link default](components/crops/app-signin-default.png) !["Sign in" link hover](components/crops/app-signin-hover.png)

### Feed

The public content stream: post cards (author avatar + name, title, excerpt, cover), the upvote/bookmark/comment actions under each card, the 'Load more' paginator and the Trending rail. Card actions were measured, never pressed.

#### Feed post card
A post row in the feed (article.group/card, border-b separator): author avatar + name, time, title, excerpt, cover thumb, upvote/comments/bookmark actions. Read as `post-card` on the / page.
States read on 2026-11-17T04:09:11.253Z (default); 2026-11-17T04:09:33.543Z (dark).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 1020 x 293.16; background transparent; text -apple-system 12/16 600, lab(43.1077 -0.29406 -4.49811); transition color 0.2s cubic-bezier(0.16, 1, 0.3, 1), background-color 0.2s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.2s cubic-bezier(0.16, 1, 0.3, 1), outline-color 0.2s cubic-bezier(0.16, 1, 0.3, 1), text-decoration-color 0.2s cubic-bezier(0.16, 1, 0.3, 1), fill 0.2s cubic-bezier(0.16, 1, 0.3, 1), stroke 0.2s cubic-bezier(0.16, 1, 0.3, 1), --tw-gradient-from 0.2s cubic-bezier(0.16, 1, 0.3, 1), --tw-gradient-via 0.2s cubic-bezier(0.16, 1, 0.3, 1), --tw-gradient-to 0.2s cubic-bezier(0.16, 1, 0.3, 1); icon 14 x 14, lab(43.1077 -0.29406 -4.49811); layers div.relative.aspect-[800/420] 558.4x293.2 lab(95.8079 -0.121295 -1.51228) 12px; div.pointer-events-none.absolute 558.4x293.2 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, oklab(0 0 0 / 0.1) 0px 0px 0px 1px inset, rgba(0, 0, 0, 0) 0px 0px 0px 0px 12px; span.relative.inline-flex 24.0x24.0 lab(95.8079 -0.121295 -1.51228) 3.35544e+07px; div.relat |
| dark | text -apple-system 12/16 600, lab(67.6029 -0.225931 -3.01496); icon 14 x 14, lab(67.6029 -0.225931 -3.01496); layers div.relative.aspect-[800/420] 558.4x293.2 lab(10.0472 -0.183955 -4.0827) 12px; div.pointer-events-none.absolute 558.4x293.2 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, oklab(0.999994 0.0000455678 0.0000200868 / 0.1) 0px 0px 0px 1px inset, rgba(0, 0, 0, 0) 0px 0px 0px 0px 12px; span.relative.inline-flex 24.0x24.0 lab(10.0472 -0.183955 -4.082 |

Child layers that carry the look: div 558.4x293.2 background lab(95.8079 -0.121295 -1.51228) radius 12px; div 558.4x293.2 radius 12px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, oklab(0 0 0 / 0.1) 0px 0px 0px 1px inset, transparent 0px 0px 0px 0px; span 24x24 background lab(95.8079 -0.121295 -1.51228) radius 3.35544e+07px.

![Feed post card default](components/crops/post-card-default.png)

#### Post title link
The post's title inside a feed card — the card's main link. Read as `post-title-link` on the / page.
States read on 2026-11-17T04:10:00.347Z (default); 2026-11-17T04:10:02.357Z (hover); 2026-11-17T04:10:07.107Z (focus-visible).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 162 x 24; background transparent; text Inter 12/16 600, lab(67.6029 -0.225931 -3.01496); layers span.relative.inline-flex 24.0x24.0 lab(10.0472 -0.183955 -4.0827) 3.35544e+07px |
| focus-visible | outline 2px solid lab(61.3712 9.00993 -60.4412), offset 2px; layers a.group/author.flex 162.0x24.0 2px solid lab(61.3712 9.00993 -60.4412) offset 2px; span.relative.inline-flex 24.0x24.0 lab(10.0472 -0.183955 -4.0827) 3.35544e+07px |

Child layers that carry the look: span 24x24 background lab(10.0472 -0.183955 -4.0827) radius 3.35544e+07px.

![Post title link default](components/crops/post-title-link-default.png) ![Post title link hover](components/crops/post-title-link-hover.png) ![Post title link focus-visible](components/crops/post-title-link-focus-visible.png)

#### Upvote button
The upvote action under a feed card (aria-label "Upvote"): count + arrow icon — measured, never pressed. Read as `post-upvote` on the / page.
States read on 2026-11-17T04:10:15.808Z (default); 2026-11-17T04:10:18.405Z (hover); 2026-11-17T04:10:20.537Z (focus-visible); 2026-11-17T04:10:21.828Z (pressed).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 53 x 32; padding 0px 12px 0px 10px; radius 3.35544e+07px; background lab(10.0472 -0.183955 -4.0827); text Inter 14/20 400, lab(91.8598 -0.149757 -1.88929); transition color 0.15s cubic-bezier(0.16, 1, 0.3, 1), background-color 0.15s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.15s cubic-bezier(0.16, 1, 0.3, 1), outline-color 0.15s cubic-bezier(0.16, 1, 0.3, 1), text-decoration-color 0.15s cubic-bezier(0.16, 1, 0.3, 1), fill 0.15s cubic-bezier(0.16, 1, 0.3, 1), stroke 0.15s cubic-bezier(0.16, 1, 0.3, 1), --tw-gradient-from 0.15s cubic-bezier(0.16, 1, 0.3, 1), --tw-gradient-via 0.15s cubic-bezier(0.16, 1, 0.3, 1), --tw-gradient-to 0.15s cubic-bezier(0.16, 1, 0.3, 1); icon 16 x 16, lab(91.8598 -0.149757 -1.88929) |
| hover | background lab(15.0313 -0.215963 -4.46058) |
| focus-visible | outline 2px solid lab(61.3712 9.00993 -60.4412), offset 2px |
| pressed | background lab(15.0313 -0.215963 -4.46058) |

![Upvote button default](components/crops/post-upvote-default.png) ![Upvote button hover](components/crops/post-upvote-hover.png) ![Upvote button focus-visible](components/crops/post-upvote-focus-visible.png) ![Upvote button pressed](components/crops/post-upvote-pressed.png)

#### Bookmark icon button
The bookmark action under a feed card (aria-label "Bookmark this post") — an icon-only ghost button. Read as `post-bookmark` on the / page.
States read on 2026-11-17T04:10:22.757Z (default); 2026-11-17T04:10:24.576Z (hover); 2026-11-17T04:10:28.158Z (focus-visible).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 32 x 32; radius 3.35544e+07px; background lab(10.0472 -0.183955 -4.0827); text Inter 16/24 400, lab(91.8598 -0.149757 -1.88929); transition color 0.15s cubic-bezier(0.16, 1, 0.3, 1), background-color 0.15s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.15s cubic-bezier(0.16, 1, 0.3, 1), outline-color 0.15s cubic-bezier(0.16, 1, 0.3, 1), text-decoration-color 0.15s cubic-bezier(0.16, 1, 0.3, 1), fill 0.15s cubic-bezier(0.16, 1, 0.3, 1), stroke 0.15s cubic-bezier(0.16, 1, 0.3, 1), --tw-gradient-from 0.15s cubic-bezier(0.16, 1, 0.3, 1), --tw-gradient-via 0.15s cubic-bezier(0.16, 1, 0.3, 1), --tw-gradient-to 0.15s cubic-bezier(0.16, 1, 0.3, 1); icon 16 x 16, lab(91.8598 -0.149757 -1.88929) |
| hover | background lab(15.0313 -0.215963 -4.46058) |
| focus-visible | outline 2px solid lab(61.3712 9.00993 -60.4412), offset 2px |

![Bookmark icon button default](components/crops/post-bookmark-default.png) ![Bookmark icon button hover](components/crops/post-bookmark-hover.png) ![Bookmark icon button focus-visible](components/crops/post-bookmark-focus-visible.png)

#### Comments link
The comments-count link under a feed card, pointing at the post's discussion page. Read as `post-comments-link` on the / page.
States read on 2026-11-17T04:10:46.752Z (default); 2026-11-17T04:11:30.803Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 103 x 32; padding 0px 6px 0px 10px; radius 3.35544e+07px; background lab(10.0472 -0.183955 -4.0827); text Inter 14/20 400, lab(91.8598 -0.149757 -1.88929); transition color 0.15s cubic-bezier(0.16, 1, 0.3, 1), background-color 0.15s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.15s cubic-bezier(0.16, 1, 0.3, 1), outline-color 0.15s cubic-bezier(0.16, 1, 0.3, 1), text-decoration-color 0.15s cubic-bezier(0.16, 1, 0.3, 1), fill 0.15s cubic-bezier(0.16, 1, 0.3, 1), stroke 0.15s cubic-bezier(0.16, 1, 0.3, 1), --tw-gradient-from 0.15s cubic-bezier(0.16, 1, 0.3, 1), --tw-gradient-via 0.15s cubic-bezier(0.16, 1, 0.3, 1), --tw-gradient-to 0.15s cubic-bezier(0.16, 1, 0.3, 1); icon 16 x 16, lab(91.8598 -0.149757 -1.88929) |
| hover | background lab(15.0313 -0.215963 -4.46058) |

![Comments link hover](components/crops/post-comments-link-hover.png)

#### Author link + avatar
The author row on a feed card: avatar image and profile link. Read as `post-author` on the / page.
States read on 2026-11-17T04:11:31.663Z (default); 2026-11-17T04:11:33.470Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 162 x 24; background transparent; text Inter 12/16 600, lab(67.6029 -0.225931 -3.01496); layers span.relative.inline-flex 24.0x24.0 lab(10.0472 -0.183955 -4.0827) 3.35544e+07px |

Child layers that carry the look: span 24x24 background lab(10.0472 -0.183955 -4.0827) radius 3.35544e+07px.

![Author link + avatar default](components/crops/post-author-default.png) ![Author link + avatar hover](components/crops/post-author-hover.png)

#### "Load more" button
The feed's pagination button — measured, never pressed (it would grow the stream). Read as `feed-load-more` on the /feed page.
States read on 2026-11-17T04:12:04.578Z (default); 2026-11-17T04:12:07.426Z (hover); 2026-11-17T04:12:08.734Z (focus-visible).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 101 x 32; padding 0px 12px; border 1px solid lab(83.7271 -0.230253 -3.0174); radius 8px; background lab(100 0 0); shadow rgba(19, 22, 28, 0.05) 0px 1px 2px 0px; text Inter 14/20 600, lab(7.16472 -0.140898 -4.74486); transition all 0.15s cubic-bezier(0.16, 1, 0.3, 1) |
| hover | background lab(93.0156 -0.17792 -2.26609) |
| focus-visible | border 1px solid lab(46.0225 28.2872 -84.5408); shadow oklab(0.561988 -0.023436 -0.238834 / 0.5) 0px 0px 0px 3px, rgba(19, 22, 28, 0.05) 0px 1px 2px 0px |

!["Load more" button default](components/crops/feed-load-more-default.png) !["Load more" button hover](components/crops/feed-load-more-hover.png) !["Load more" button focus-visible](components/crops/feed-load-more-focus-visible.png)

#### Trending aside
The "Trending" rail beside the feed column (aria-label "Trending"). Read as `feed-trending` on the /feed page.
Read on 2026-11-17T04:13:07.877Z.

**Values (default).** size 352 x 3865.77; radius 28px; background lab(97.552 -0.0918508 -1.13482); shadow oklab(0.199999 -0.00136095 -0.0129235 / 0.06) 0px 0px 0px 1px inset; text Inter 20/28 600, lab(7.16472 -0.140898 -4.74486); icon 14 x 14, lab(46.0225 28.2872 -84.5408).

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

### Discussion

The public post page's discussion layer: the 'Share your thoughts' comment field (clicked into, never typed in), its Comment button, share and overflow icon buttons and reply links.

#### Comment textarea
The "Share your thoughts…" textarea on a discussion page. "focused" is the field clicked into — nothing is typed. Read as `comment-box` on the /posts/i-used-to-be-a-magician/6afadee8cd8f659889f399ed page.
States read on 2026-11-17T04:13:27.946Z (focused); 2026-11-17T04:13:50.237Z (default); 2026-11-17T04:14:20.562Z (dark). `focused` failed at capture (locator.evaluate: Timeout 8000ms exceeded.).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 670 x 72; padding 12px 16px; background transparent; text -apple-system 14/20 400, lab(7.16472 -0.140898 -4.74486); placeholder lab(43.1077 -0.29406 -4.49811) |
| dark | text -apple-system 14/20 400, lab(91.8598 -0.149757 -1.88929); placeholder lab(67.6029 -0.225931 -3.01496) |

![Comment textarea default](components/crops/comment-box-default.png) ![Comment textarea dark](components/crops/comment-box-dark.png)

#### "Comment" button
The submit under the comment box — measured, never pressed. Read as `comment-submit` on the /posts/i-used-to-be-a-magician/6afadee8cd8f659889f399ed page.
States read on 2026-11-17T04:14:26.813Z (default); 2026-11-17T04:14:29.504Z (hover); 2026-11-17T04:14:41.801Z (focus-visible).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible) | size 92.64 x 32; padding 0px 12px; radius 8px; background lab(95.8079 -0.121295 -1.51228); text -apple-system 14/20 600, lab(64.5824 -0.249207 -3.38902); transition all 0.15s cubic-bezier(0.16, 1, 0.3, 1) |

!["Comment" button default](components/crops/comment-submit-default.png) !["Comment" button hover](components/crops/comment-submit-hover.png) !["Comment" button focus-visible](components/crops/comment-submit-focus-visible.png)

#### Share icon button
The "Share this post" icon button — measured, never pressed. Read as `post-share` on the /posts/i-used-to-be-a-magician/6afadee8cd8f659889f399ed page.
States read on 2026-11-17T04:14:43.126Z (default); 2026-11-17T04:14:45.020Z (hover); 2026-11-17T04:14:46.386Z (focus-visible).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 32 x 32; radius 3.35544e+07px; background lab(95.8079 -0.121295 -1.51228); text -apple-system 16/24 400, lab(7.16472 -0.140898 -4.74486); transition color 0.15s cubic-bezier(0.16, 1, 0.3, 1), background-color 0.15s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.15s cubic-bezier(0.16, 1, 0.3, 1), outline-color 0.15s cubic-bezier(0.16, 1, 0.3, 1), text-decoration-color 0.15s cubic-bezier(0.16, 1, 0.3, 1), fill 0.15s cubic-bezier(0.16, 1, 0.3, 1), stroke 0.15s cubic-bezier(0.16, 1, 0.3, 1), --tw-gradient-from 0.15s cubic-bezier(0.16, 1, 0.3, 1), --tw-gradient-via 0.15s cubic-bezier(0.16, 1, 0.3, 1), --tw-gradient-to 0.15s cubic-bezier(0.16, 1, 0.3, 1); icon 16 x 16, lab(7.16472 -0.140898 -4.74486) |
| hover | background lab(93.0156 -0.17792 -2.26609) |
| focus-visible | outline 2px solid lab(46.0225 28.2872 -84.5408), offset 2px |

![Share icon button default](components/crops/post-share-default.png) ![Share icon button hover](components/crops/post-share-hover.png) ![Share icon button focus-visible](components/crops/post-share-focus-visible.png)

#### "More options" icon button
The overflow action on a comment row (aria-label "More options") — measured, never pressed. Read as `post-more-options` on the /posts/i-used-to-be-a-magician/6afadee8cd8f659889f399ed page.
States read on 2026-11-17T04:14:47.339Z (default); 2026-11-17T04:14:49.235Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 24 x 24; radius 8px; background transparent; text -apple-system 14/20 400, lab(43.1077 -0.29406 -4.49811); transition color 0.15s cubic-bezier(0.16, 1, 0.3, 1), background-color 0.15s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.15s cubic-bezier(0.16, 1, 0.3, 1), outline-color 0.15s cubic-bezier(0.16, 1, 0.3, 1), text-decoration-color 0.15s cubic-bezier(0.16, 1, 0.3, 1), fill 0.15s cubic-bezier(0.16, 1, 0.3, 1), stroke 0.15s cubic-bezier(0.16, 1, 0.3, 1), --tw-gradient-from 0.15s cubic-bezier(0.16, 1, 0.3, 1), --tw-gradient-via 0.15s cubic-bezier(0.16, 1, 0.3, 1), --tw-gradient-to 0.15s cubic-bezier(0.16, 1, 0.3, 1); icon 14 x 14, lab(43.1077 -0.29406 -4.49811) |
| hover | background lab(95.8079 -0.121295 -1.51228); text -apple-system 14/20 400, lab(7.16472 -0.140898 -4.74486); icon 14 x 14, lab(7.16472 -0.140898 -4.74486) |

!["More options" icon button default](components/crops/post-more-options-default.png) !["More options" icon button hover](components/crops/post-more-options-hover.png)

#### "Reply" button
The reply action under a comment — measured, never pressed. Read as `comment-reply` on the /posts/i-used-to-be-a-magician/6afadee8cd8f659889f399ed page.
States read on 2026-11-17T04:14:50.114Z (default); 2026-11-17T04:14:52.238Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 84.63 x 32; padding 0px 12px; border 1px solid lab(90.4636 -0.177681 -2.26592); radius 3.35544e+07px; background transparent; text -apple-system 14/20 600, lab(7.16472 -0.140898 -4.74486); transition color 0.15s cubic-bezier(0.16, 1, 0.3, 1), background-color 0.15s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.15s cubic-bezier(0.16, 1, 0.3, 1), outline-color 0.15s cubic-bezier(0.16, 1, 0.3, 1), text-decoration-color 0.15s cubic-bezier(0.16, 1, 0.3, 1), fill 0.15s cubic-bezier(0.16, 1, 0.3, 1), stroke 0.15s cubic-bezier(0.16, 1, 0.3, 1), --tw-gradient-from 0.15s cubic-bezier(0.16, 1, 0.3, 1), --tw-gradient-via 0.15s cubic-bezier(0.16, 1, 0.3, 1), --tw-gradient-to 0.15s cubic-bezier(0.16, 1, 0.3, 1); icon 16 x 16, lab(7.16472 -0.140898 -4.74486) |
| hover | background lab(93.0156 -0.17792 -2.26609) |

!["Reply" button default](components/crops/comment-reply-default.png) !["Reply" button hover](components/crops/comment-reply-hover.png)

### Profile

The public @handle page: the sticky profile header (avatar, name, Share button) and the sections nav.

#### Profile header
The sticky profile bar (avatar, name, handle, Share button) above the sections nav. Read as `profile-header` on the /@anish78 page.

Not on the page when it was captured.

#### Profile sections nav
The "Profile sections" tab-like nav (Posts / Series / …) under the header. Read as `profile-nav` on the /@anish78 page.
Read on 2026-11-17T04:15:16.181Z.

**Values (default).** size 676 x 48; border B: 1px solid lab(90.4636 -0.177681 -2.26592); background transparent; text -apple-system 14/20 600, lab(7.16472 -0.140898 -4.74486); layers nav.flex.h-12 676.0x48.0 B:1px solid; a.-mb-px.inline-flex 53.1x48.0 B:2px solid; a.-mb-px.inline-flex 75.6x48.0 B:2px solid.

Child layers that carry the look: nav 676x48 border 1px solid; a 53.1x48 border 2px solid; a 75.6x48 border 2px solid.

![Profile sections nav default](components/crops/profile-nav-default.png)

#### Profile "Share" button
The outlined Share action in the profile header — measured, never pressed. Read as `profile-share` on the /@anish78 page.
States read on 2026-11-17T04:15:28.416Z (default); 2026-11-17T04:15:31.032Z (hover); 2026-11-17T04:15:33.023Z (focus-visible).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 89.72 x 36; padding 8px 12px; border 1px solid lab(83.7271 -0.230253 -3.0174); radius 8px; background lab(100 0 0); shadow rgba(19, 22, 28, 0.05) 0px 1px 2px 0px; text -apple-system 14/20 600, lab(7.16472 -0.140898 -4.74486); transition all 0.15s cubic-bezier(0.16, 1, 0.3, 1); icon 16 x 16, lab(7.16472 -0.140898 -4.74486) |
| hover | background lab(93.0156 -0.17792 -2.26609) |
| focus-visible | border 1px solid lab(46.0225 28.2872 -84.5408); shadow oklab(0.561988 -0.023436 -0.238834 / 0.5) 0px 0px 0px 3px, rgba(19, 22, 28, 0.05) 0px 1px 2px 0px |

![Profile "Share" button default](components/crops/profile-share-default.png) ![Profile "Share" button hover](components/crops/profile-share-hover.png) ![Profile "Share" button focus-visible](components/crops/profile-share-focus-visible.png)

### Pro

The /pro marketing page: plan cards, the 'Get Pro' call-to-action that links to /login, and the FAQ accordion whose question rows open answers locally.

#### Plan card
A Pro / Growth pricing card on /pro. Read as `pro-plan-card` on the /pro page.
Read on 2026-11-17T04:15:53.024Z.

**Values (default).** size 232 x 32; padding 8px 12px; radius 3.35544e+07px; background lab(100 0 0); shadow lab(90.4636 -0.177681 -2.26592) 0px 0px 0px 1px inset, rgba(19, 22, 28, 0.05) 0px 1px 2px 0px; text -apple-system 14/20 600, lab(7.16472 -0.140898 -4.74486); transition width 0.15s cubic-bezier(0.16, 1, 0.3, 1), height 0.15s cubic-bezier(0.16, 1, 0.3, 1), padding 0.15s cubic-bezier(0.16, 1, 0.3, 1), color 0.15s cubic-bezier(0.16, 1, 0.3, 1); icon 18 x 18, lab(7.16472 -0.140898 -4.74486).

![Plan card default](components/crops/pro-plan-card-default.png)

#### "Get Pro" CTA
A plan call-to-action ("Get Pro, $5 a month") — links to /login, measured never followed. Read as `pro-cta` on the /pro page.

Not on the page when it was captured.

#### FAQ accordion question
A question row in the /pro FAQ accordion. "opened" is its own press revealing the answer. Read as `faq-question` on the /pro page.
States read on 2026-11-17T04:15:55.084Z (default); 2026-11-17T04:16:12.190Z (hover); 2026-11-17T04:16:13.753Z (focus-visible); 2026-11-17T04:16:32.949Z (opened).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 860 x 52; padding 20px 0px 8px 0px; radius 8px; background transparent; text -apple-system 16/24 600, lab(7.16472 -0.140898 -4.74486) |
| focus-visible | shadow oklab(0.561988 -0.023436 -0.238834 / 0.5) 0px 0px 0px 3px; layers button.flex.flex-1 860.0x52.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, oklab(0.561988 -0.023436 -0.238834 / 0.5) 0px 0px 0px 3px, rgba(0, 0, 0, 0) 0px 0px 0px 0px 8px |
| opened | size 860 x 64; padding 20px 0px; icon 16 x 16, lab(43.1077 -0.29406 -4.49811) |

![FAQ accordion question default](components/crops/faq-question-default.png) ![FAQ accordion question hover](components/crops/faq-question-hover.png) ![FAQ accordion question focus-visible](components/crops/faq-question-focus-visible.png) ![FAQ accordion question opened](components/crops/faq-question-opened.png)

### Changelog

The /changelog page's category tablist (All / Features / Improvements / Fixes / Deprecated) — a local UI toggle that re-filters the list.

#### Category tablist
The All / Features / Improvements / Fixes / Deprecated tablist. Read as `changelog-tablist` on the /changelog page.
Read on 2026-11-17T04:16:50.858Z.

**Values (default).** size 423.94 x 34; padding 3px; radius 8px; background lab(95.8079 -0.121295 -1.51228); text -apple-system 14/20 600, lab(7.16472 -0.140898 -4.74486).

![Category tablist default](components/crops/changelog-tablist-default.png)

#### Category tab
One category tab. "selected" is the tab's own activation — a local UI toggle that re-filters the list. Read as `changelog-tab` on the /changelog page.
States read on 2026-11-17T04:16:52.755Z (default); 2026-11-17T04:16:55.394Z (hover); 2026-11-17T04:16:56.693Z (focus-visible); 2026-11-17T04:17:00.176Z (selected).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 85 x 28; padding 0px 12px; radius 6px; background transparent; text -apple-system 14/20 600, lab(43.1077 -0.29406 -4.49811); transition color 0.15s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.15s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.15s cubic-bezier(0.16, 1, 0.3, 1) |
| hover | text -apple-system 14/20 600, lab(7.16472 -0.140898 -4.74486) |
| focus-visible | background lab(100 0 0); shadow oklab(0.561988 -0.023436 -0.238834 / 0.5) 0px 0px 0px 3px, rgba(19, 22, 28, 0.05) 0px 1px 2px 0px; outline 1px solid lab(46.0225 28.2872 -84.5408), offset 2px; text -apple-system 14/20 600, lab(7.16472 -0.140898 -4.74486) |
| selected | background lab(100 0 0); shadow rgba(19, 22, 28, 0.05) 0px 1px 2px 0px; text -apple-system 14/20 600, lab(7.16472 -0.140898 -4.74486) |

![Category tab default](components/crops/changelog-tab-default.png) ![Category tab hover](components/crops/changelog-tab-hover.png) ![Category tab focus-visible](components/crops/changelog-tab-focus-visible.png) ![Category tab selected](components/crops/changelog-tab-selected.png)

### Agents

The /agents page: install-method tabs (MCP server / Agent skill / CLI) and the copy-to-clipboard buttons beside the install commands.

#### Install-method tab
One of the MCP server / Agent skill / CLI tabs. "selected" is its own activation. Read as `agents-tab` on the /agents page.
States read on 2026-11-17T04:17:12.987Z (default); 2026-11-17T04:17:15.663Z (hover); 2026-11-17T04:17:17.433Z (selected).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, selected) | size 329.33 x 110; padding 20px 24px; radius 16px; background lab(100 0 0); shadow lab(90.4636 -0.177681 -2.26592) 0px 0px 0px 1px, rgba(19, 22, 28, 0.05) 0px 1px 2px 0px; text -apple-system 16/24 600, lab(7.16472 -0.140898 -4.74486); transition color 0.15s cubic-bezier(0.16, 1, 0.3, 1), background-color 0.15s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.15s cubic-bezier(0.16, 1, 0.3, 1), outline-color 0.15s cubic-bezier(0.16, 1, 0.3, 1), text-decoration-color 0.15s cubic-bezier(0.16, 1, 0.3, 1), fill 0.15s cubic-bezier(0.16, 1, 0.3, 1), stroke 0.15s cubic-bezier(0.16, 1, 0.3, 1), --tw-gradient-from 0.15s cubic-bezier(0.16, 1, 0.3, 1), --tw-gradient-via 0.15s cubic-bezier(0.16, 1, 0.3, 1), --tw-gradient-to 0.15s cubic-bezier(0.16, 1, 0.3, 1) |

![Install-method tab default](components/crops/agents-tab-default.png) ![Install-method tab hover](components/crops/agents-tab-hover.png) ![Install-method tab selected](components/crops/agents-tab-selected.png)

#### "Copy to clipboard" button
The copy icon-button beside an install command — pressed only with forcePseudoState. Read as `agents-copy` on the /agents page.
States read on 2026-11-17T04:17:18.905Z (default); 2026-11-17T04:17:20.709Z (hover); 2026-11-17T04:17:21.936Z (focus-visible); 2026-11-17T04:17:23.264Z (pressed).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 32 x 32; radius 8px; background transparent; text -apple-system 14/20 400, lab(67.6029 -0.225931 -3.01496); transition color 0.15s cubic-bezier(0.16, 1, 0.3, 1), background-color 0.15s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.15s cubic-bezier(0.16, 1, 0.3, 1), outline-color 0.15s cubic-bezier(0.16, 1, 0.3, 1), text-decoration-color 0.15s cubic-bezier(0.16, 1, 0.3, 1), fill 0.15s cubic-bezier(0.16, 1, 0.3, 1), stroke 0.15s cubic-bezier(0.16, 1, 0.3, 1), --tw-gradient-from 0.15s cubic-bezier(0.16, 1, 0.3, 1), --tw-gradient-via 0.15s cubic-bezier(0.16, 1, 0.3, 1), --tw-gradient-to 0.15s cubic-bezier(0.16, 1, 0.3, 1); icon 14 x 14, lab(67.6029 -0.225931 -3.01496) |
| hover | background lab(15.0313 -0.215963 -4.46058); text -apple-system 14/20 400, lab(91.8598 -0.149757 -1.88929); icon 14 x 14, lab(91.8598 -0.149757 -1.88929) |
| focus-visible | outline 2px solid lab(61.3712 9.00993 -60.4412), offset 2px; layers button.absolute.top-1 32.0x32.0 2px solid lab(61.3712 9.00993 -60.4412) offset 2px 8px |

!["Copy to clipboard" button default](components/crops/agents-copy-default.png) !["Copy to clipboard" button hover](components/crops/agents-copy-hover.png) !["Copy to clipboard" button focus-visible](components/crops/agents-copy-focus-visible.png) !["Copy to clipboard" button pressed](components/crops/agents-copy-pressed.png)

### Onboarding form

The /onboard form's fields — measured at rest only: nothing was typed into them and 'Next' was never pressed.

#### Text input (name)
The "Alex Johnson" placeholder name field — measured at rest; nothing is entered. Read as `onboard-input` on the /onboard page.

Not on the page when it was captured.

#### Combobox (city)
The "City, Country" location combobox — measured at rest, never opened (it would fetch suggestions). Read as `onboard-combobox` on the /onboard page.
States read on 2026-11-17T04:17:37.053Z (default); 2026-11-17T04:17:38.402Z (focus-visible).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 386 x 40; padding 4px 12px 4px 8px; background transparent; text -apple-system 14/20 400, lab(7.16472 -0.140898 -4.74486); transition color 0.15s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.15s cubic-bezier(0.16, 1, 0.3, 1); placeholder lab(43.1077 -0.29406 -4.49811); layers input.file:text-foreground.placeholder:text-muted-foreground 386.0x40.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px |
| focus-visible | shadow oklab(0.561988 -0.023436 -0.238834 / 0.5) 0px 0px 0px 0px; layers input.file:text-foreground.placeholder:text-muted-foreground 386.0x40.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, oklab(0.561988 -0.023436 -0.238834 / 0.5) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px |

![Combobox (city) default](components/crops/onboard-combobox-default.png) ![Combobox (city) focus-visible](components/crops/onboard-combobox-focus-visible.png)

#### Tagline textarea
The bio/tagline textarea — measured at rest. Read as `onboard-textarea` on the /onboard page.
States read on 2026-11-17T04:17:39.569Z (default); 2026-11-17T04:17:42.495Z (focus-visible).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 416 x 68; padding 8px 12px; border 1px solid lab(83.7271 -0.230253 -3.0174); radius 8px; background transparent; text -apple-system 14/20 400, lab(7.16472 -0.140898 -4.74486); transition color 0.15s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.15s cubic-bezier(0.16, 1, 0.3, 1); placeholder lab(43.1077 -0.29406 -4.49811) |
| focus-visible | border 1px solid lab(46.0225 28.2872 -84.5408); shadow oklab(0.561988 -0.023436 -0.238834 / 0.5) 0px 0px 0px 3px |

![Tagline textarea default](components/crops/onboard-textarea-default.png) ![Tagline textarea focus-visible](components/crops/onboard-textarea-focus-visible.png)

#### "Upload photo" button
The avatar upload control — measured, never pressed (it opens a file dialog). Read as `onboard-upload` on the /onboard page.
States read on 2026-11-17T04:17:46.235Z (default); 2026-11-17T04:17:49.278Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 120.81 x 32; padding 0px 12px; border 1px solid lab(83.7271 -0.230253 -3.0174); radius 8px; background lab(100 0 0); shadow rgba(19, 22, 28, 0.05) 0px 1px 2px 0px; text -apple-system 14/20 600, lab(7.16472 -0.140898 -4.74486); transition all 0.15s cubic-bezier(0.16, 1, 0.3, 1) |
| hover | background lab(93.0156 -0.17792 -2.26609) |

!["Upload photo" button default](components/crops/onboard-upload-default.png) !["Upload photo" button hover](components/crops/onboard-upload-hover.png)

#### "Next" button
The form's primary action — measured, never pressed (it would submit). Read as `onboard-next` on the /onboard page.
States read on 2026-11-17T04:17:50.558Z (default); 2026-11-17T04:17:52.427Z (hover); 2026-11-17T04:17:54.497Z (focus-visible).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 416 x 40; padding 0px 16px; radius 8px; background lab(9.58302 -0.18093 -4.0814); shadow rgba(255, 255, 255, 0.12) 0px 1px 0px 0px inset, rgba(19, 22, 28, 0.2) 0px 1px 2px 0px; text -apple-system 14/20 600, lab(100 0 0); transition all 0.15s cubic-bezier(0.16, 1, 0.3, 1); icon 16 x 16, lab(100 0 0) |
| hover | background oklab(0.220999 -0.00115209 -0.0109341 / 0.9) |
| focus-visible | shadow oklab(0.561988 -0.023436 -0.238834 / 0.5) 0px 0px 0px 3px, rgba(255, 255, 255, 0.12) 0px 1px 0px 0px inset, rgba(19, 22, 28, 0.2) 0px 1px 2px 0px |

!["Next" button default](components/crops/onboard-next-default.png) !["Next" button hover](components/crops/onboard-next-hover.png) !["Next" button focus-visible](components/crops/onboard-next-focus-visible.png)

### Brand

The /brand page's palette swatch buttons.

#### Palette swatch button
A named colour swatch on /brand (Graphite 500) — a button that copies the value. Read as `brand-swatch` on the /brand page.
States read on 2026-11-17T04:18:06.312Z (default); 2026-11-17T04:18:08.639Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 257 x 173; padding 16px; border B: 1px solid lab(90.4636 -0.177681 -2.26592); L: 1px solid lab(90.4636 -0.177681 -2.26592); background transparent; text -apple-system 16/24 600, lab(7.16472 -0.140898 -4.74486); transition color 0.15s cubic-bezier(0.16, 1, 0.3, 1), background-color 0.15s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.15s cubic-bezier(0.16, 1, 0.3, 1), outline-color 0.15s cubic-bezier(0.16, 1, 0.3, 1), text-decoration-color 0.15s cubic-bezier(0.16, 1, 0.3, 1), fill 0.15s cubic-bezier(0.16, 1, 0.3, 1), stroke 0.15s cubic-bezier(0.16, 1, 0.3, 1), --tw-gradient-from 0.15s cubic-bezier(0.16, 1, 0.3, 1), --tw-gradient-via 0.15s cubic-bezier(0.16, 1, 0.3, 1), --tw-gradient-to 0.15s cubic-bezier(0.16, 1, 0.3, 1); layers button.flex.cursor-pointer 257.0x173.0 B:1px solid / L:1px solid; span.h-14.w-full 224.0x56.0 rgb(113, 115, 121) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, oklab(0 0 0 / 0.1) 0px 0px 0px 1px inset, rgba(0, 0, 0, 0) 0px 0px 0px 0px 8px |
| hover | background lab(95.8079 -0.121295 -1.51228); layers none |

Child layers that carry the look: button 257x173 border 1px solid; span 224x56 background #717379 radius 8px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, oklab(0 0 0 / 0.1) 0px 0px 0px 1px inset, transparent 0px 0px 0px 0px.

![Palette swatch button default](components/crops/brand-swatch-default.png) ![Palette swatch button hover](components/crops/brand-swatch-hover.png)

### Blog chrome

townhall.hashnode.com — the hosted blog engine on the same design system: the sticky header (wordmark, pill nav, Search ⌘K and Toggle theme buttons, the More menu), the about-the-publication aside and the footer.

#### Blog header bar
The sticky blog header (border-b, backdrop blur): wordmark, the pill main nav, Search (Ctrl K) and Toggle theme buttons. Read as `th-header` on the / page.
States read on 2026-11-17T04:25:10.394Z (default); 2026-11-17T04:25:17.450Z (dark).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 1440 x 72; background oklab(0.999998 -0.00000980496 0.0000234246 / 0.8); text -apple-system 14/20 400, lab(7.16472 -0.140898 -4.74486); transition transform 0.3s cubic-bezier(0.4, 0, 0.2, 1), translate 0.3s cubic-bezier(0.4, 0, 0.2, 1), scale 0.3s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.3s cubic-bezier(0.4, 0, 0.2, 1); icon 22 x 22, lab(43.1077 -0.29406 -4.49811) |
| dark | background oklab(0.168999 -0.00115149 -0.0109353 / 0.8); text -apple-system 14/20 400, lab(91.8598 -0.149757 -1.88929); icon 22 x 22, lab(67.6029 -0.225931 -3.01496) |

![Blog header bar default](components/crops/th-header-default.png) ![Blog header bar dark](components/crops/th-header-dark.png)

#### Main navigation pill
The centred pill nav (bg-surface, rounded-full border) holding the publication's nav links. Read as `th-nav` on the / page.
Read on 2026-11-17T04:25:29.701Z.

**Values (default).** size 468.59 x 36; background transparent; text -apple-system 14/20 400, lab(7.16472 -0.140898 -4.74486); icon 12 x 12, lab(43.1077 -0.29406 -4.49811); layers ul.flex.h-9 468.6x36.0 lab(97.552 -0.0918508 -1.13482) T:1px solid / R:1px solid / B:1px solid / L:1px solid 3.35544e+07px.

Child layers that carry the look: ul 468.6x36 background lab(97.552 -0.0918508 -1.13482) border 1px solid radius 3.35544e+07px.

![Main navigation pill default](components/crops/th-nav-default.png)

#### Nav link
A nav item in the pill ("News 📰"), hover:bg-background. Read as `th-nav-link` on the / page.
States read on 2026-11-17T04:25:30.852Z (default); 2026-11-17T04:25:32.908Z (hover); 2026-11-17T04:25:34.190Z (focus-visible).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 86.97 x 30; padding 0px 14px; radius 3.35544e+07px; background transparent; text -apple-system 14/20 400, lab(7.16472 -0.140898 -4.74486); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background lab(100 0 0) |
| focus-visible | outline 2px solid lab(46.0225 28.2872 -84.5408), offset 2px; layers a.inline-flex.h-full 87.0x30.0 2px solid lab(46.0225 28.2872 -84.5408) offset 2px 3.35544e+07px |

![Nav link default](components/crops/th-nav-link-default.png) ![Nav link hover](components/crops/th-nav-link-hover.png) ![Nav link focus-visible](components/crops/th-nav-link-focus-visible.png)

#### Search button (Ctrl K)
The header search button (aria-label "Open search (press Control or Command and K)") carrying the ⌘K hint. Read as `th-search-button` on the / page.
States read on 2026-11-17T04:25:36.131Z (default); 2026-11-17T04:25:39.672Z (hover); 2026-11-17T04:25:45.038Z (focus-visible).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 128.28 x 36; padding 0px 6px 0px 12px; border 1px solid lab(90.4636 -0.177681 -2.26592); radius 3.35544e+07px; background transparent; text -apple-system 14/20 400, lab(43.1077 -0.29406 -4.49811); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 12 x 12, lab(43.1077 -0.29406 -4.49811) |
| hover | background lab(97.552 -0.0918508 -1.13482) |
| focus-visible | outline 2px solid lab(46.0225 28.2872 -84.5408), offset 2px |

![Search button (Ctrl K) default](components/crops/th-search-button-default.png) ![Search button (Ctrl K) hover](components/crops/th-search-button-hover.png) ![Search button (Ctrl K) focus-visible](components/crops/th-search-button-focus-visible.png)

#### "Toggle theme" button
The header theme toggle. Pressed headless it produced no repaint and no menu (verified 2026-11-17) — measured at rest and after the prefers-color-scheme repaint, which is how the engine shows dark. Read as `th-theme-toggle` on the / page.
States read on 2026-11-17T04:25:46.150Z (default); 2026-11-17T04:25:54.995Z (darkblog).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 36 x 36; radius 3.35544e+07px; background transparent; text -apple-system 14/20 600, lab(43.1077 -0.29406 -4.49811); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, lab(43.1077 -0.29406 -4.49811) |
| darkblog | text -apple-system 14/20 600, lab(67.6029 -0.225931 -3.01496); icon none |

!["Toggle theme" button default](components/crops/th-theme-toggle-default.png) !["Toggle theme" button darkblog](components/crops/th-theme-toggle-darkblog.png)

#### "More" menu button
The header overflow menu. "opened" is its own press, closed with Escape. Read as `th-more-menu` on the / page.
States read on 2026-11-17T04:26:03.106Z (default); 2026-11-17T04:26:06.154Z (hover); 2026-11-17T04:26:08.330Z (opened).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 76.58 x 30; padding 0px 12px 0px 14px; radius 3.35544e+07px; background transparent; text -apple-system 14/20 400, lab(7.16472 -0.140898 -4.74486); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 12 x 12, lab(43.1077 -0.29406 -4.49811) |
| hover, opened | background lab(100 0 0) |

!["More" menu button default](components/crops/th-more-menu-default.png) !["More" menu button hover](components/crops/th-more-menu-hover.png) !["More" menu button opened](components/crops/th-more-menu-opened.png)

#### About-the-publication aside
The "About the publication" sidebar card on the index. Read as `th-about` on the / page.
Read on 2026-11-17T04:26:24.400Z.

**Values (default).** size 1120 x 144; background transparent; text -apple-system 20/28 600, lab(7.16472 -0.140898 -4.74486); icon 14 x 14, lab(7.16472 -0.140898 -4.74486); layers div.flex.flex-col 1120.0x144.0 lab(97.552 -0.0918508 -1.13482) 20px; a.inline-flex.size-9 36.0x36.0 T:1px solid / R:1px solid / B:1px solid / L:1px solid 3.35544e+07px; a.inline-flex.size-9 36.0x36.0 T:1px solid / R:1px solid / B:1px solid / L:1px solid 3.35544e+07px; a.inline-flex.size-9 36.0x36.0 T:1px solid / R:1px solid / B:1px solid / L:1px solid 3.35544e+07px.

Child layers that carry the look: div 1120x144 background lab(97.552 -0.0918508 -1.13482) radius 20px; a 36x36 border 1px solid radius 3.35544e+07px; a 36x36 border 1px solid radius 3.35544e+07px.

![About-the-publication aside default](components/crops/th-about-default.png)

#### Blog footer
The footer (aria-label "Footer") with the publication's footer nav and "Powered by Hashnode" link. Read as `th-footer` on the / page.
States read on 2026-11-17T04:26:28.007Z (default); 2026-11-17T04:26:36.742Z (dark).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 1440 x 153; border T: 1px solid lab(90.4636 -0.177681 -2.26592); background transparent; text -apple-system 14/20 400, lab(43.1077 -0.29406 -4.49811); icon 14 x 14, lab(46.0225 28.2872 -84.5408) |
| dark | border T: 1px solid lab(16.8878 -0.22532 -4.46479); text -apple-system 14/20 400, lab(67.6029 -0.225931 -3.01496); icon 14 x 14, lab(61.3712 9.00993 -60.4412) |

![Blog footer default](components/crops/th-footer-default.png) ![Blog footer dark](components/crops/th-footer-dark.png)

### Blog feed

The blog index: post cards, title links and the 'Load more posts' paginator — measured, never pressed.

#### Post card
A post row on the blog index (li > article): cover thumb, title, excerpt, author + date. Read as `th-post-card` on the / page.
States read on 2026-11-17T04:26:46.650Z (default); 2026-11-17T04:26:59.389Z (dark).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 651.59 x 514.08; background transparent; text -apple-system 12/16 600, lab(7.16472 -0.140898 -4.74486); icon 12 x 12, lab(7.16472 -0.140898 -4.74486); layers div.relative.aspect-[800/420] 651.6x342.1 lab(95.8079 -0.121295 -1.51228) 20px; div::after.relative.aspect-[800/420] 651.594pxx342.078px T:1px solid / R:1px solid / B:1px solid / L:1px solid 20px; span.absolute.left-3 79.7x24.0 lab(100 0 0) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(19, 22, 28, 0.05)  |
| dark | text -apple-system 12/16 600, lab(91.8598 -0.149757 -1.88929); icon 12 x 12, lab(91.8598 -0.149757 -1.88929); layers div.relative.aspect-[800/420] 651.6x342.1 lab(10.0472 -0.183955 -4.0827) 20px; div::after.relative.aspect-[800/420] 651.594pxx342.078px T:1px solid / R:1px solid / B:1px solid / L:1px solid 20px; span.absolute.left-3 79.7x24.0 lab(4.32278 -0.0849143 -3.03079) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba |

Child layers that carry the look: div 651.6x342.1 background lab(95.8079 -0.121295 -1.51228) radius 20px; div::after 651.594pxx342.078px border 1px solid radius 20px; span 79.7x24 background lab(100 0 0) radius 3.35544e+07px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(19, 22, 28, 0.05) 0px 1px 2px 0px.

![Post card default](components/crops/th-post-card-default.png) ![Post card dark](components/crops/th-post-card-dark.png)

#### Post title link
The title link inside an index card. Read as `th-post-title` on the / page.
States read on 2026-11-17T04:27:40.088Z (default); 2026-11-17T04:27:52.692Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 651.59 x 514.08; radius 16px; background transparent; text -apple-system 12/16 600, lab(7.16472 -0.140898 -4.74486); icon 12 x 12, lab(7.16472 -0.140898 -4.74486); layers div.relative.aspect-[800/420] 651.6x342.1 lab(95.8079 -0.121295 -1.51228) 20px; div::after.relative.aspect-[800/420] 651.594pxx342.078px T:1px solid / R:1px solid / B:1px solid / L:1px solid 20px; span.absolute.left-3 79.7x24.0 lab(100 0 0) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(19, 22, 28, 0.05)  |

Child layers that carry the look: div 651.6x342.1 background lab(95.8079 -0.121295 -1.51228) radius 20px; div::after 651.594pxx342.078px border 1px solid radius 20px; span 79.7x24 background lab(100 0 0) radius 3.35544e+07px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(19, 22, 28, 0.05) 0px 1px 2px 0px.

![Post title link default](components/crops/th-post-title-default.png) ![Post title link hover](components/crops/th-post-title-hover.png)

#### "Load more posts" button
The index pagination button — measured, never pressed. Read as `th-load-more` on the / page.
States read on 2026-11-17T04:27:59.846Z (default); 2026-11-17T04:28:03.064Z (hover); 2026-11-17T04:28:04.921Z (focus-visible).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 149.47 x 36; padding 0px 16px; border 1px solid lab(83.7271 -0.230253 -3.0174); radius 3.35544e+07px; background lab(100 0 0); text -apple-system 14/20 600, lab(7.16472 -0.140898 -4.74486); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background lab(93.0156 -0.17792 -2.26609) |
| focus-visible | shadow oklab(0.561988 -0.023436 -0.238834 / 0.5) 0px 0px 0px 2px |

!["Load more posts" button default](components/crops/th-load-more-default.png) !["Load more posts" button hover](components/crops/th-load-more-hover.png) !["Load more posts" button focus-visible](components/crops/th-load-more-focus-visible.png)

### Blog prose

The blog article layer: the text-article-title h1, section headings, body paragraphs and links, the tinted --code-block panels, and the 'On this page' table of contents.

#### Article header
The page-frame article header: title (text-article-title), meta, cover. Read as `th-article-header` on the /why-diy-qa-doesnt-work-anymore-a-2025-guide-to-e2e-testing-for-modern-web-apps page.
States read on 2026-11-17T04:20:30.252Z (default); 2026-11-17T04:20:50.704Z (dark).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 1120 x 391; padding 80px 0px 0px 0px; background transparent; text -apple-system 36/44 600, lab(7.16472 -0.140898 -4.74486); icon 14 x 14, lab(43.1077 -0.29406 -4.49811); layers a.group.flex 680.0x46.0 T:1px solid / R:1px solid / B:1px solid / L:1px solid 16px |
| dark | text -apple-system 36/44 600, lab(91.8598 -0.149757 -1.88929); icon 14 x 14, lab(67.6029 -0.225931 -3.01496) |

Child layers that carry the look: a 680x46 border 1px solid radius 16px.

![Article header default](components/crops/th-article-header-default.png) ![Article header dark](components/crops/th-article-header-dark.png)

#### Article title (h1)
The post title, text-article-title. Read as `th-prose-h1` on the /why-diy-qa-doesnt-work-anymore-a-2025-guide-to-e2e-testing-for-modern-web-apps page.
States read on 2026-11-17T04:20:59.653Z (default); 2026-11-17T04:21:06.603Z (dark).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 680 x 132; background transparent; text -apple-system 36/44 600, lab(7.16472 -0.140898 -4.74486) |
| dark | text -apple-system 36/44 600, lab(91.8598 -0.149757 -1.88929) |

![Article title (h1) default](components/crops/th-prose-h1-default.png) ![Article title (h1) dark](components/crops/th-prose-h1-dark.png)

#### Section heading (h2)
An in-article heading. Read as `th-prose-h2` on the /why-diy-qa-doesnt-work-anymore-a-2025-guide-to-e2e-testing-for-modern-web-apps page.
Read on 2026-11-17T04:21:19.533Z.

**Values (default).** size 680 x 32; background transparent; text -apple-system 24/32 600, lab(7.16472 -0.140898 -4.74486); icon 16 x 16, lab(43.1077 -0.29406 -4.49811).

![Section heading (h2) default](components/crops/th-prose-h2-default.png)

#### Body paragraph
A paragraph of article prose (text-reading). Read as `th-prose-p` on the /why-diy-qa-doesnt-work-anymore-a-2025-guide-to-e2e-testing-for-modern-web-apps page.
States read on 2026-11-17T04:21:23.359Z (default); 2026-11-17T04:21:33.351Z (dark).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 208 x 16; background transparent; text -apple-system 12/16 600, lab(43.1077 -0.29406 -4.49811) |
| dark | text -apple-system 12/16 600, lab(67.6029 -0.225931 -3.01496) |

![Body paragraph default](components/crops/th-prose-p-default.png) ![Body paragraph dark](components/crops/th-prose-p-dark.png)

#### Prose link
A body-text link inside the article. Read as `th-prose-link` on the /why-diy-qa-doesnt-work-anymore-a-2025-guide-to-e2e-testing-for-modern-web-apps page.
States read on 2026-11-17T04:21:39.878Z (default); 2026-11-17T04:21:42.550Z (hover); 2026-11-17T04:21:44.819Z (focus-visible).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 60.02 x 24; background transparent; text -apple-system 18/28 500, lab(46.0225 28.2872 -84.5408); transition text-decoration-color 0.15s ease |
| focus-visible | outline 2px solid lab(46.0225 28.2872 -84.5408), offset 2px; layers a 60.0x24.0 2px solid lab(46.0225 28.2872 -84.5408) offset 2px |

![Prose link default](components/crops/th-prose-link-default.png) ![Prose link hover](components/crops/th-prose-link-hover.png) ![Prose link focus-visible](components/crops/th-prose-link-focus-visible.png)

#### Code block
A fenced code block in the article (bg-code-block, tinted dark in both themes). Read as `th-code-block` on the /why-diy-qa-doesnt-work-anymore-a-2025-guide-to-e2e-testing-for-modern-web-apps page.

Not on the page when it was captured.

#### "On this page" TOC
The article's table-of-contents rail (aria-label "On this page"). Read as `th-toc` on the /why-diy-qa-doesnt-work-anymore-a-2025-guide-to-e2e-testing-for-modern-web-apps page.
Read on 2026-11-17T04:21:46.853Z.

**Values (default).** size 208 x 380; background transparent; text -apple-system 14/20 400, lab(43.1077 -0.29406 -4.49811).

!["On this page" TOC default](components/crops/th-toc-default.png)

#### TOC link
One entry in the table of contents. Read as `th-toc-link` on the /why-diy-qa-doesnt-work-anymore-a-2025-guide-to-e2e-testing-for-modern-web-apps page.
States read on 2026-11-17T04:21:47.877Z (default); 2026-11-17T04:21:49.712Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 208 x 28; padding 4px 0px; background transparent; text -apple-system 14/20 400, lab(43.1077 -0.29406 -4.49811); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | text -apple-system 14/20 400, lab(7.16472 -0.140898 -4.74486) |

![TOC link default](components/crops/th-toc-link-default.png) ![TOC link hover](components/crops/th-toc-link-hover.png)

### Blog archive

The blog archive's Previous/Next pagination — measured, never pressed.

#### Pagination nav
The archive's Previous / Next pagination (aria-label "Pagination"). Read as `th-pagination` on the /archive page.
Read on 2026-11-17T04:22:01.067Z.

**Values (default).** size 1120 x 82; padding 40px 0px 0px 0px; background transparent; text -apple-system 14/20 600, lab(7.16472 -0.140898 -4.74486); icon 16 x 16, lab(7.16472 -0.140898 -4.74486); layers button.inline-flex.items-center 109.9x36.0 lab(100 0 0) T:1px solid / R:1px solid / B:1px solid / L:1px solid 3.35544e+07px; ol.hidden.list-none 217.1x42.0 lab(97.552 -0.0918508 -1.13482) T:1px solid / R:1px solid / B:1px solid / L:1px solid 3.35544e+07px; span.inline-flex.size-8 32.0x32.0 lab(100 0 0) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px.

Child layers that carry the look: button 109.9x36 background lab(100 0 0) border 1px solid radius 3.35544e+07px; ol 217.1x42 background lab(97.552 -0.0918508 -1.13482) border 1px solid radius 3.35544e+07px; span 32x32 background lab(100 0 0) radius 3.35544e+07px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(19, 22, 28, 0.05) 0px 1px 2px 0px.

![Pagination nav default](components/crops/th-pagination-default.png)

#### "Previous" button
The previous-page control — measured, never pressed. Read as `th-page-prev` on the /archive page.
States read on 2026-11-17T04:22:01.943Z (default); 2026-11-17T04:22:03.773Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 109.92 x 36; padding 0px 16px; border 1px solid lab(83.7271 -0.230253 -3.0174); radius 3.35544e+07px; background lab(100 0 0); text -apple-system 14/20 600, lab(7.16472 -0.140898 -4.74486); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); opacity 0.5; icon 16 x 16, lab(7.16472 -0.140898 -4.74486) |

!["Previous" button default](components/crops/th-page-prev-default.png) !["Previous" button hover](components/crops/th-page-prev-hover.png)

### App search

The ⌘K command menu: the modal the sidebar Search button and the page's own shortcut open — opened and closed only through the page's own controls; nothing was searched.

#### Search input
The command field in the open dialog; "focused" is the field clicked into — nothing is typed. Read as `app-search-input` on the / page.
States read on 2026-11-17T04:22:27.169Z (default); 2026-11-17T04:22:31.801Z (focused).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 622 x 48; padding 12px 48px 12px 0px; radius 8px; background transparent; text Inter 16/24 400, lab(7.16472 -0.140898 -4.74486); placeholder lab(43.1077 -0.29406 -4.49811) |

![Search input default](components/crops/app-search-input-default.png) ![Search input focused](components/crops/app-search-input-focused.png)

#### Suggestion row
A suggestion row in the open menu. Read as `app-search-item` on the / page.
States read on 2026-11-17T04:22:38.183Z (default); 2026-11-17T04:22:41.092Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 638 x 40; padding 10px; radius 8px; background lab(93.0156 -0.17792 -2.26609); text Inter 14/20 400, lab(7.16472 -0.140898 -4.74486); icon 16 x 16, lab(43.1077 -0.29406 -4.49811) |

![Suggestion row default](components/crops/app-search-item-default.png) ![Suggestion row hover](components/crops/app-search-item-hover.png)

#### Search dialog
The ⌘K command dialog, painted by the page's own shortcut. Read as `app-search-dialog` on the / page.
States read on 2026-11-17T04:22:45.508Z (default); 2026-11-17T04:22:57.398Z (dark).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 672 x 594; border 1px solid lab(90.4636 -0.177681 -2.26592); radius 12px; background lab(100 0 0); shadow rgba(19, 22, 28, 0.06) 0px 1px 2px 0px, rgba(19, 22, 28, 0.22) 0px 12px 32px -12px; text ui-monospace 12/16 600, lab(43.1077 -0.29406 -4.49811); transition all 0.2s ease; icon 16 x 16, lab(43.1077 -0.29406 -4.49811) |
| dark | border 1px solid lab(16.8878 -0.22532 -4.46479); background lab(11.0916 -0.19037 -4.0855); shadow rgba(0, 0, 0, 0.4) 0px 1px 2px 0px, rgba(0, 0, 0, 0.6) 0px 12px 32px -12px; text ui-monospace 12/16 600, lab(67.6029 -0.225931 -3.01496); icon 16 x 16, lab(67.6029 -0.225931 -3.01496) |

![Search dialog default](components/crops/app-search-dialog-default.png) ![Search dialog dark](components/crops/app-search-dialog-dark.png)

### Blog search

The blog engine's own ⌘K search dialog — same control, same restraint.

#### Search input
The command field in the open dialog; "focused" is the field clicked into — nothing is typed. Read as `th-search-input` on the / page.
States read on 2026-11-17T04:23:20.375Z (default); 2026-11-17T04:23:21.695Z (focused).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 510.03 x 56; padding 12px 0px; background transparent; text -apple-system 16/24 400, lab(7.16472 -0.140898 -4.74486); placeholder lab(43.1077 -0.29406 -4.49811) |

![Search input default](components/crops/th-search-input-default.png) ![Search input focused](components/crops/th-search-input-focused.png)

#### Suggestion row
A suggestion row in the open menu. Read as `th-search-item` on the / page.

Not on the page when it was captured.

#### Search dialog
The ⌘K command dialog, painted by the page's own shortcut. Read as `th-search-dialog` on the / page.
Read on 2026-11-17T04:23:25.216Z.

**Values (default).** size 672 x 460; border 1px solid lab(90.4636 -0.177681 -2.26592); radius 16px; background lab(100 0 0); shadow rgba(19, 22, 28, 0.06) 0px 1px 2px 0px, rgba(19, 22, 28, 0.22) 0px 12px 32px -12px; text system-ui 12/16 600, lab(43.1077 -0.29406 -4.49811); transition all 0.2s ease; icon 16 x 16, lab(43.1077 -0.29406 -4.49811).

![Search dialog default](components/crops/th-search-dialog-default.png)

### App chrome (mobile)

The 390px surface: the compact header and the 'Open menu' button's nav sheet.

#### Mobile header
The sticky bar at 390px (md:hidden): menu button, logo, search. Read as `m-app-header` on the / page.
Read on 2026-11-17T04:23:45.962Z.

**Values (default).** size 390 x 52; padding 0px 12px; border B: 1px solid lab(90.4636 -0.177681 -2.26592); background oklab(0.999998 -0.00000980496 0.0000234246 / 0.8); text Inter 16/24 400, lab(7.16472 -0.140898 -4.74486); icon 16 x 16, lab(7.16472 -0.140898 -4.74486).

![Mobile header default](components/crops/m-app-header-default.png)

#### "Open menu" button
The hamburger that opens the nav sheet. Read as `m-app-menu-button` on the / page.
States read on 2026-11-17T04:23:56.163Z (default); 2026-11-17T04:23:58.621Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 32 x 32; radius 8px; background transparent; text Inter 14/20 600, lab(7.16472 -0.140898 -4.74486); transition all 0.15s cubic-bezier(0.16, 1, 0.3, 1); icon 16 x 16, lab(7.16472 -0.140898 -4.74486) |

!["Open menu" button default](components/crops/m-app-menu-button-default.png) !["Open menu" button hover](components/crops/m-app-menu-button-hover.png)

#### Nav sheet (open)
The opened navigation sheet — an overlay panel over the page. The "Open menu" press happens in find(). Read as `m-app-drawer` on the / page.
Read on 2026-11-17T04:24:10.686Z.

**Values (opened).** size 288 x 844; border R: 1px solid lab(90.4636 -0.177681 -2.26592); background lab(97.552 -0.0918508 -1.13482); shadow rgba(19, 22, 28, 0.06) 0px 1px 2px 0px, rgba(19, 22, 28, 0.22) 0px 12px 32px -12px; text Inter 14/20 400, lab(43.1077 -0.29406 -4.49811); transition color 0.5s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.5s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.5s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.5s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.5s cubic-bezier(0.4, 0, 0.2, 1), fill 0.5s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.5s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.5s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.5s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.5s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.5s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.5s cubic-bezier(0.4, 0, 0.2, 1), transform 0.5s cubic-bezier(0.4, 0, 0.2, 1), translate 0.5s cubic-bezier(0.4, 0, 0.2, 1), scale 0.5s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.5s cubic-bezier(0.4, 0, 0.2, 1), filter 0.5s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.5s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.5s cubic-bezier(0.4, 0, 0.2, 1), display 0.5s cubic-bezier(0.4, 0, 0.2, 1), content-visibility 0.5s cubic-bezier(0.4, 0, 0.2, 1), overlay 0.5s cubic-bezier(0.4, 0, 0.2, 1), pointer-events 0.5s cubic-bezier(0.4, 0, 0.2, 1); icon 118.53 x 16, lab(7.16472 -0.140898 -4.74486).

![Nav sheet (open) opened](components/crops/m-app-drawer-opened.png)

### Blog chrome (mobile)

The 390px blog surface: the compact header.

#### Mobile blog header
The sticky blog bar at 390px: wordmark, More, search and theme icons. Read as `m-th-header` on the / page.
Read on 2026-11-17T04:24:25.842Z.

**Values (default).** size 390 x 64; background oklab(0.999998 -0.00000980496 0.0000234246 / 0.8); text -apple-system 16/24 400, lab(7.16472 -0.140898 -4.74486); transition transform 0.3s cubic-bezier(0.4, 0, 0.2, 1), translate 0.3s cubic-bezier(0.4, 0, 0.2, 1), scale 0.3s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.3s cubic-bezier(0.4, 0, 0.2, 1); icon 20 x 20, lab(43.1077 -0.29406 -4.49811).

![Mobile blog header default](components/crops/m-th-header-default.png)

## Icons

113 distinct inline-SVG icons were collected from the live pages into [icons/](icons) by `tools/capture/icons.mjs`, indexed in [icons/INDEX.tsv](icons/INDEX.tsv): a file is named from `tools/capture/icon-names.tsv` where its geometry hash is listed, else the label or class of the control it sits in, else `icon-<hash>`; colour is kept as `currentColor` wherever it matched the text colour, so each icon recolours from CSS `color` the way it does on the site. The icons are the product's artwork — borrow the set's grammar (sizes, stroke-vs-fill, naming roles), never the artwork itself.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|
| [the-foreword-by-hashnode](icons/the-foreword-by-hashnode.svg) | 16x16 18x18 | 0 0 40 40 | fill | home; feed; post; profile; pro; agents; changelog; brand; alt-medium; search dialog; sidebar; nav; dark | The foreword by Hashnode |
| [in-the-hashnode-feed](icons/in-the-hashnode-feed.svg) | 16x16 18x18 | 0 0 24 24 | stroke | home; feed; post; profile; pro; agents; changelog; brand; alt-medium; search dialog; sidebar; nav; dark | In the Hashnode feed / Feed |
| [more](icons/more.svg) | 16x16 | 0 0 24 24 | stroke | home; feed; post; profile; pro; agents; changelog; brand; alt-medium; search dialog; sidebar; nav; dark | More |
| [sign-in](icons/sign-in.svg) | 16x16 18x18 | 0 0 24 24 | stroke | home; feed; post; profile; pro; agents; changelog; brand; alt-medium; search dialog; sidebar; nav; dark | Sign in |
| [home-feed](icons/home-feed.svg) | 16x16 18x18 | 0 0 24 24 | stroke | home; feed; post; profile; pro; agents; changelog; brand; alt-medium; search dialog; sidebar; nav; dark | Home feed / Home |
| [hashnode-pro](icons/hashnode-pro.svg) | 14x14 16x16 18x18 | 0 0 24 24 | fill | home; feed; post; profile; pro; agents; changelog; brand; alt-medium; search dialog; sidebar; nav; dark | Hashnode Pro / Hashnode Growth Pro included / Get Hashnode P |
| [hashnode-for-agents](icons/hashnode-for-agents.svg) | 16x16 18x18 | 0 0 24 24 | stroke | home; feed; post; profile; pro; agents; changelog; brand; alt-medium; search dialog; sidebar; nav; dark | Hashnode for Agents |
| [i-text-muted-foreground](icons/i-text-muted-foreground-c25d23da.svg) | 16x16 18x18 20x20 | 0 0 24 24 | stroke | home; feed; post; profile; pro; agents; changelog; brand; alt-medium; search dialog; sidebar; nav; dark | Structured data and sitemaps / Search and read Search your p |
| [toggle-sidebar](icons/toggle-sidebar.svg) | 16x16 | 0 0 24 24 | stroke | home; feed; post; profile; pro; agents; changelog; brand; alt-medium; search dialog; sidebar; nav; dark | Toggle Sidebar |
| [theme](icons/theme.svg) | 16x16 18x18 | 0 0 24 24 | stroke | home; feed; post; profile; pro; agents; changelog; brand; alt-medium; search dialog; sidebar; nav | Theme |
| [scheduled-posts-pro](icons/scheduled-posts-pro.svg) | 14x14 16x16 | 0 0 24 24 | stroke | home; feed; post; profile; search dialog; sidebar; nav; dark | Scheduled posts Pro / 4 min read / 8 min read |
| [upvote-5](icons/upvote-5.svg) | 14x14 16x16 | 0 0 24 24 | stroke | home; feed; post; profile; search dialog; sidebar; nav; dark | Upvote (5) / Upvote (4) / Upvote (3) |
| [bookmark-this-post](icons/bookmark-this-post.svg) | 16x16 | 0 0 24 24 | stroke | home; feed; post; search dialog; sidebar; nav; dark | Bookmark this post / Bookmarks |
| [see-what-pro-includes](icons/see-what-pro-includes.svg) | 14x14 | 0 0 24 24 | stroke | home; feed; pro; search dialog; sidebar; nav; dark | See what Pro includes / See what Growth includes / See every |
| [live](icons/live.svg) | 14x14 20x20 | 0 0 24 24 | stroke | home; pro; agents; search dialog; sidebar; nav; dark | Live / Read docs/launch.md / Uploaded cover.png |
| [icon-9da8b27f](icons/icon-9da8b27f.svg) | 14x14 16x16 20x20 | 0 0 24 24 | stroke | home; changelog; alt-medium; search dialog; sidebar; nav; dark | 🪶 cover.png 3200 × 1680 · 2.4 MB 🪶 cov / 🎯 Improvement Octob |
| [comments](icons/comments.svg) | 16x16 | 0 0 24 24 | stroke | home; feed; profile; search dialog; sidebar; nav; dark | Comments / 4 comments / 2 comments |
| [icon-10a2e36b](icons/icon-10a2e36b.svg) | 12x12 13x13 14x14 16x16 22x22 | 0 0 24 24 | fill | home; pro; search dialog; sidebar; nav; dark | 9.5B Visits to AI assistants every month / vs 25.7% How much |
| [medium](icons/medium.svg) | 14x14 16x16 18x18 | 0 0 24 24 | stroke | home; agents; search dialog; sidebar; nav; dark | Medium / Substack / Ghost |
| [nuxt](icons/nuxt.svg) | 14x14 | 0 3.9 24 16 | fill | home; pro; search dialog; sidebar; nav; dark | Nuxt |
| [what-agents-read](icons/what-agents-read.svg) | 14x14 16x16 18x18 | 0 0 24 24 | stroke | home; pro; agents; search dialog; sidebar; dark | What agents read / Agent skill for the API One command teac  |
| [ga-plausible-7](icons/ga-plausible-7.svg) | 16x16 18x18 | 0 0 24 24 | stroke | home; agents; search dialog; sidebar; nav; dark | GA, Plausible, +7 |
| [icon-49bede3f](icons/icon-49bede3f.svg) | 14x14 16x16 22x22 | 0 0 24 24 | fill | home; pro; search dialog; sidebar; nav; dark | 9.5B Visits to AI assistants every month / Claude Code ~/ale |
| [substack](icons/substack.svg) | 18x20 21x24 | 0 0 448 511.471 | fill | home; alt-medium; search dialog; sidebar; nav; dark | Substack / Hashnode vs Substack Own your domain, pu |
| [ghost](icons/ghost.svg) | 20x20 24x24 | 0 0 24 24 | stroke | home; alt-medium; search dialog; sidebar; nav; dark | Ghost / Hashnode vs Ghost Ownership and headless |
| [astro](icons/astro.svg) | 14x14 | 0 0 24 24 | fill | home; pro; search dialog; sidebar; nav; dark | Astro |
| [custom-domain-pro](icons/custom-domain-pro.svg) | 16x16 | 0 0 24 24 | stroke | home; profile; search dialog; sidebar; nav; dark | Custom domain Pro / Website |
| [series-tags-pages](icons/series-tags-pages.svg) | 16x16 18x18 | 0 0 24 24 | stroke | home; pro; search dialog; sidebar; nav; dark | Series, tags, pages / Up to 10 publications Upgrading one pu |
| [icon-7009b37d](icons/icon-7009b37d.svg) | 14x14 16x16 22x22 | 0 0 24 24 | fill | home; pro; search dialog; sidebar; nav; dark | 9.5B Visits to AI assistants every month / vs 25.7% How much |
| [ask-ai](icons/ask-ai.svg) | 12x12 14x14 | 0 0 24 24 | stroke | home; pro; search dialog; sidebar; nav; dark | Ask AI / Tighten the intro / Rewrite |
| [612](icons/612.svg) | 14x14 15x15 | 0 0 24 24 | fill | home; pro; search dialog; sidebar; nav; dark | 612 |
| [next-js](icons/next-js.svg) | 14x14 | 0 0 24 24 | fill | home; pro; search dialog; sidebar; nav; dark | Next.js |
| [icon-9808f451](icons/icon-9808f451.svg) | 14x14 16x16 22x22 | 0 0 24 24 | fill | home; pro; search dialog; sidebar; nav; dark | AI Overview 15% → 8% Google visits that  / 9.5B Visits to AI |
| [no-branding-pro](icons/no-branding-pro.svg) | 16x16 18x18 | 0 0 24 24 | stroke | home; pro; search dialog; sidebar; nav; dark | No branding Pro / Hide Hashnode branding Remove the "Power |
| [notion](icons/notion.svg) | 20x20 24x24 | 0 0 100 100 | fill | home; alt-medium; search dialog; sidebar; nav; dark | Notion / Hashnode vs Notion A blog built to rank, |
| [react](icons/react.svg) | 14x14 | -11.5 -10.23 23 20.46 | fill | home; pro; search dialog; sidebar; nav; dark | React |
| [hashnode](icons/hashnode.svg) | 12x12 16x16 22x22 24x24 | 0 0 39 39 | fill | home; alt-medium; search dialog; sidebar; nav; dark | Hashnode |
| [ai-rephrase](icons/ai-rephrase.svg) | 14x14 16x16 18x18 | 0 0 24 24 | stroke | home; pro; search dialog; sidebar; nav; dark | AI Rephrase / AI writing tools Pro / Rewrite as Q&A One clic |
| [markdown-editor](icons/markdown-editor.svg) | 16x16 20x20 | 0 0 24 24 | stroke | home; agents; search dialog; sidebar; nav; dark | Markdown editor / Edit published posts Change a title, sub / |
| [cover](icons/cover.svg) | 14x14 16x16 | 0 0 24 24 | stroke | home; search dialog; sidebar; nav; dark | Cover / Embeds, tables, images |
| [webhooks-pro](icons/webhooks-pro.svg) | 16x16 | 0 0 24 24 | stroke | home; search dialog; sidebar; nav; dark | Webhooks Pro |
| [built-in-analytics](icons/built-in-analytics.svg) | 16x16 | 0 0 24 24 | stroke | home; search dialog; sidebar; nav; dark | Built-in analytics |
| [team-roles-review](icons/team-roles-review.svg) | 16x16 | 0 0 24 24 | stroke | home; search dialog; sidebar; nav; dark | Team roles, review |
| [icon-2b9ebaf8](icons/icon-2b9ebaf8.svg) | 16x16 | 0 0 24 24 | stroke | home; search dialog; sidebar; nav; dark | Hosted blog, live in a minute / Unlimited posts, Markdown ed |
| [800-420-64-kb](icons/800-420-64-kb.svg) | 12x12 | 0 0 24 24 | stroke | home; search dialog; sidebar; nav; dark | 800 × 420 · 64 KB |
| [suggest-three-titles](icons/suggest-three-titles.svg) | 14x14 | 0 0 24 24 | stroke | home; search dialog; sidebar; nav; dark | Suggest three titles |
| [bulk-import-pro](icons/bulk-import-pro.svg) | 16x16 | 0 0 24 24 | stroke | home; search dialog; sidebar; nav; dark | Bulk import Pro |
| [start-your-blog-free](icons/start-your-blog-free.svg) | 18x18 | 0 0 24 24 | stroke | home; search dialog; sidebar; nav; dark | Start your blog, free |
| [free-forever](icons/free-forever.svg) | 14x14 | 0 0 24 24 | stroke | home; search dialog; sidebar; nav; dark | Free forever / No card needed / Export your posts any time |
| [copilot](icons/copilot.svg) | 14x14 | 0 0 24 24 | fill | home; search dialog; sidebar; nav; dark | Copilot |
| [github-backup-pro](icons/github-backup-pro.svg) | 16x16 | 0 0 24 24 | stroke | home; search dialog; sidebar; nav; dark | GitHub backup Pro |
| [posts-as-markdown](icons/posts-as-markdown.svg) | 16x16 | 0 0 24 24 | stroke | home; search dialog; sidebar; nav; dark | Posts as Markdown / A Markdown copy of every post |
| [social-cards-built-in](icons/social-cards-built-in.svg) | 16x16 | 0 0 24 24 | stroke | home; search dialog; sidebar; nav; dark | Social cards, built in / RSS and social cards, built in |
| [code-in-25-languages](icons/code-in-25-languages.svg) | 16x16 | 0 0 24 24 | stroke | home; search dialog; sidebar; nav; dark | Code in 25 languages |
| [icon-9e48ceb8](icons/icon-9e48ceb8.svg) | 16x16 17x17 22x22 | 0 0 24 24 | fill | home; search dialog; sidebar; nav; dark | AI Overview 15% → 8% Google visits that  / vs 25.7% How much |
| [cursor](icons/cursor.svg) | 14x14 | 0 0 24 24 | fill | home; search dialog; sidebar; nav; dark | Cursor |
| [what-readers-see](icons/what-readers-see.svg) | 14x14 | 0 0 24 24 | stroke | home; search dialog; sidebar; nav; dark | What readers see |
| [sitemap-rss-json-ld](icons/sitemap-rss-json-ld.svg) | 16x16 | 0 0 24 24 | stroke | home; search dialog; sidebar; nav; dark | Sitemap, RSS, JSON-LD |
| [latex-and-mermaid](icons/latex-and-mermaid.svg) | 16x16 | 0 0 24 24 | stroke | home; search dialog; sidebar; nav; dark | LaTeX and Mermaid |
| [icon-04ec9756](icons/icon-04ec9756.svg) | 44x44 | 0 0 24 24 | fill | home; search dialog; sidebar; nav |  |
| [icon-42a73ac0](icons/icon-42a73ac0.svg) | 14x14 | 0 0 24 24 | stroke | home; search dialog; sidebar; dark |  |
| [icon-774f8134](icons/icon-774f8134.svg) | 14x14 | 0 0 24 24 | stroke | home; search dialog; sidebar; dark |  |
| [icon-7aecc7ab](icons/icon-7aecc7ab.svg) | 14x14 | 0 0 24 24 | stroke | home; search dialog; sidebar; dark |  |
| [icon-7c47e0bb](icons/icon-7c47e0bb.svg) | 14x14 | 0 0 24 24 | stroke | home; search dialog; sidebar; dark |  |
| [icon-90440096](icons/icon-90440096.svg) | 14x14 | 0 0 24 24 | stroke | home; search dialog; sidebar; dark |  |
| [icon-9f73d1c0](icons/icon-9f73d1c0.svg) | 14x14 15x15 | 0 0 24 24 | fill | home; search dialog; sidebar; nav |  |
| [icon-b6c1e5b2](icons/icon-b6c1e5b2.svg) | 14x14 | 0 0 24 24 | stroke | home; search dialog; sidebar; dark |  |
| [icon-bbbcf79b](icons/icon-bbbcf79b.svg) | 14x14 | 0 0 24 24 | stroke | home; search dialog; sidebar; dark |  |
| [icon-d0bea0aa](icons/icon-d0bea0aa.svg) | 14x14 | 0 0 24 24 | stroke | home; search dialog; sidebar; dark |  |
| [subheading](icons/subheading.svg) | 14x14 | 0 0 24 24 | stroke | home; search dialog; sidebar; dark | Subheading |
| [icon-fd33dc78](icons/icon-fd33dc78.svg) | 14x14 | 0 0 24 24 | stroke | home; search dialog; sidebar; dark |  |
| [icon-fee419d5](icons/icon-fee419d5.svg) | 14x14 | 0 0 24 24 | stroke | home; search dialog; sidebar; dark |  |
| [icon-4ee09870](icons/icon-4ee09870.svg) | 16x16 | 0 0 24 24 | stroke | pro; agents; alt-medium | Is Pro per publication or per account? / How does pricing wo |
| [what-do-i-get-with-pro](icons/what-do-i-get-with-pro.svg) | 16x16 | 0 0 24 24 | stroke | pro; agents; alt-medium | What do I get with Pro? / Which one should I use? / Can I mo |
| [contact-us](icons/contact-us.svg) | 16x16 | 0 0 24 24 | stroke | changelog; search dialog | Contact us / Support: hello@hashnode.com |
| [feed](icons/feed.svg) | 14x14 16x16 | 0 0 24 24 | stroke | post; alt-medium | Feed / Alternatives |
| [share-this-post](icons/share-this-post.svg) | 16x16 | 0 0 24 24 | stroke | post; profile | Share this post / Share |
| [icon-148c97b8](icons/icon-148c97b8.svg) | 44x44 | 0 0 24 24 | fill | dark |  |
| [alternatives](icons/alternatives.svg) | 14x14 | 0 0 24 24 | stroke | feed | Alternatives |
| [icon-16a9bf4c](icons/icon-16a9bf4c.svg) | 20x20 | 0 0 24 24 | stroke | agents | Publish posts Publish markdown with tags |
| [i-text-muted-foreground](icons/i-text-muted-foreground-182a5d05.svg) | 16x16 | 0 0 24 24 | stroke | dark |  |
| [set-up-your-agent](icons/set-up-your-agent.svg) | 18x18 | 0 0 24 24 | stroke | agents | Set up your agent |
| [prev](icons/prev.svg) | 14x14 | 0 0 24 24 | stroke | feed | Prev |
| [theme-set-to-dark](icons/theme-set-to-dark.svg) | 16x16 | 0 0 24 24 | stroke | dark | Theme set to dark |
| [open-menu](icons/open-menu.svg) | 16x16 | 0 0 24 24 | stroke | nav | Open menu |
| [icon-2f2f3802](icons/icon-2f2f3802.svg) | 64x14 | 0 0 64 14 | stroke | alt-medium | Hashnode vs WordPress Own your domain an / Hashnode vs Ghost |
| [svg-not-class-text-text-muted-fo](icons/svg-not-class-text-text-muted-fo-33728032.svg) | 18x18 | 14 13.2 36 36 | fill | sidebar | Buildful New AI coding agent that delive |
| [support](icons/support.svg) | 16x16 | 0 0 24 24 | stroke | sidebar | Support |
| [joined-december-2020](icons/joined-december-2020.svg) | 14x14 | 0 0 24 24 | stroke | profile | Joined December 2020 |
| [icon-470ff566](icons/icon-470ff566.svg) | 18x18 | 0 0 24 24 | stroke | agents |  |
| [brand](icons/brand.svg) | 16x16 | 0 0 24 24 | fill | search dialog | Brand |
| [2px](icons/2px.svg) | 14x14 | 0 0 30 10 | fill | dark |  |
| [icon-582a162a](icons/icon-582a162a.svg) | 20x20 | 0 0 24 24 | stroke | agents | Draft first Save a draft, review it, the |
| [icon-6168cd16](icons/icon-6168cd16.svg) | 18x18 | 0 0 24 24 | stroke | pro | FAQ blocks with structured data Add up t |
| [kathmandu-nepal](icons/kathmandu-nepal.svg) | 14x14 | 0 0 24 24 | stroke | profile | kathmandu, Nepal |
| [close-toast](icons/close-toast.svg) | 12x12 | 0 0 24 24 | stroke | dark | Close toast |
| [view-all-posts](icons/view-all-posts.svg) | 14x14 | 0 0 24 24 | stroke | feed | View all posts |
| [svg-not-class-text-text-muted-fo](icons/svg-not-class-text-text-muted-fo-7e154a3f.svg) | 18x18 | 0 0 300 300 | fill | sidebar | Bug0 The AI-native e2e QA regression tes |
| [icon-8379f2bb](icons/icon-8379f2bb.svg) | 18x18 | 0 0 24 24 | stroke | pro | Scheduled publishing Schedule drafts to  / Freshness queue E |
| [svg](icons/svg.svg) | 16x16 | 0 0 24 24 | stroke | brand | SVG |
| [icon-8b65ef96](icons/icon-8b65ef96.svg) | 20x20 | 0 0 24 24 | stroke | agents | Review team drafts Submit a draft for re |
| [drafts](icons/drafts.svg) | 16x16 | 0 0 24 24 | stroke | search dialog | Drafts |
| [terms](icons/terms.svg) | 16x16 | 0 0 24 24 | stroke | search dialog | Terms / Privacy Policy / Code of Conduct |
| [more-options](icons/more-options.svg) | 14x14 | 0 0 24 24 | stroke | post | More options |
| [icon-bff2ed0b](icons/icon-bff2ed0b.svg) | 18x18 | 0 0 24 24 | stroke | pro | Bulk markdown import Bring an existing p |
| [icon-c204ec86](icons/icon-c204ec86.svg) | 18x18 | 0 0 24 24 | stroke | pro | Posts are never auto-deleted Off-topic p |
| [icon-d79bc653](icons/icon-d79bc653.svg) | 16x16 | 0 0 24 24 | stroke | search dialog |  |
| [settings](icons/settings.svg) | 16x16 | 0 0 24 24 | stroke | search dialog | Settings / General settings / Account |
| [ai-writing-tools](icons/ai-writing-tools.svg) | 19x19 | 0 0 24 24 | fill | pro | AI writing tools |
| [reply](icons/reply.svg) | 16x16 | 0 0 24 24 | stroke | post | Reply |
| [copy-to-clipboard](icons/copy-to-clipboard.svg) | 14x14 | 0 0 24 24 | stroke | agents | Copy to clipboard |
| [close](icons/close.svg) | 16x16 | 0 0 24 24 | stroke | search dialog | Close |
| [icon-fc37157e](icons/icon-fc37157e.svg) | 20x20 | 0 0 24 24 | stroke | agents | Upload images Upload a local image and g |

## Gaps

### The blocked product surfaces

The signed-in product was never entered: **/login** and everything behind it (the dashboard, the post editor, account settings, onboarding completion) stays outside — the 'Sign in' / 'Start your blog' / 'Get Pro' links were measured, never followed. **engineering.hashnode.com** answered HTTP 429 from the capture host on every try; **help.hashnode.com**, **blog.hashnode.com** and **docs.hashnode.com** do not resolve (NXDOMAIN), and **api.**, **support.**, **changelog.** and **weekly.** subdomains are unreachable or nonexistent. **status.hashnode.com** resolves to a Better Stack status page — not a Hashnode product surface. All are documented as boundaries, never faked.

### Pages

- **/login and every post-auth surface** — the auth wall, see above. The sign-up CTAs were measured, never followed.
- **engineering.hashnode.com** — HTTP 429 from the capture host; never reached.
- **help. / docs. / blog. / api. / support. / changelog. / weekly. subdomains** — NXDOMAIN or unreachable; documented boundaries.
- **status.hashnode.com** — a Better Stack status page, not a Hashnode product surface; excluded by scope.
- **Other public blogs on the engine** — townhall.hashnode.com stands in for the hosted-blog engine; individual *.hashnode.dev / custom-domain blogs share the same templates (index card, article page, TOC rail, code panel) and were not each crawled.
- **The infinite feed** — /feed and the home stream grow on scroll; full-page shots are bounded at eight chunks (the sidecars record the boundary) and only the top of the stream was measured.

### States

- **Pressed** was forced with DevTools on the controls that carry it, so a state a script adds on mousedown (if any) is missing.
- **The search fields were never typed into** — both ⌘K dialogs were captured open with their resting suggestion lists and closed with Escape; no query was run, so result lists are uncaptured.
- **The comment and onboarding fields were never typed into** — the comment box was clicked into for its focus look and nothing was entered; the onboarding fields were measured at rest and 'Next' was never pressed.
- **Upvote, bookmark and 'Load more'** — measured, never pressed (they would post to the account or grow the stream).
- **The theme menu** was used to paint dark for the `dark` states and shots, then switched back — no theme was held across navigations.
- **The blog engine's 'Toggle theme' button** produced no repaint headless and no menu — its resting state is measured, and blog `dark` states come from emulated prefers-color-scheme, recorded as such in each state's `via`.

### Themes

hashnode.com boots `html.light` and the sidebar carries a real Theme menu (Light / Dark / System). `light` is the painted default; `dark` states and `{page}-dark-*` screenshots were painted through that menu, verified by the painted surface (html class, color-scheme and the computed background), and the theme was switched back afterwards. townhall.hashnode.com paints `html.dark` under prefers-color-scheme — the captured dark shots use that path. Both token themes resolve from the same semantic declarations — `.dark`/`:root.dark` re-points them.

### Fonts

- **Inter** is the product face (`--font-inter`, loaded through next/font with a metrics-matched fallback); the app UI paints the system stack (`--font-app`: -apple-system first) and code the ui-monospace stack (`--font-mono`). Inter's woff2 under /_next/static/media is the licensed file — declared and measured, not shipped. The style guide falls back to the system sans and mono.

### Screenshots

- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.
- The rendered brand strings on the captured pages (the wordmark and copy) are the product's published content.
- Public author names, handles and avatars on captured posts and cards are published content and are kept; nothing private was captured.

### Content left out

- Article copy, post titles, author bios and pricing text are the product's published content; only frames and components were measured.
