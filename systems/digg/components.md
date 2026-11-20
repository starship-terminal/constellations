# Digg components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from digg.com (the 2025 Digg reboot — 'News, before it trends') on 2026-11-14, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, bought or submitted and no form was ever sent; the sort controls, sidebar rows, vote pills, comment and source links were measured, never followed, and the dark readings come from cycling the sidebar theme pill to dark.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (53 components, 129 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (123 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-{state}.png`: home and story are captured in both `light` and `dark` (the dark shots paint the real theme after cycling the sidebar pill); the other surfaces paint `light`. Desktop shots are 1440 x 900 at 1x; the phone surfaces are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x). The mobile home feed captures as two `partN` clip tiles (7000 + 3339 px — the full 10,339 px page, bounded).

| Surface | URL | Screenshots |
|---|---|---|
| Home feed | `/` | [default](screenshots/home-dark-default.png), [full](screenshots/home-dark-full.png), [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png) |
| Technology category | `/tech` | [default](screenshots/tech-light-default.png), [full](screenshots/tech-light-full.png) |
| Story | `/world-business/k7vz2u4u` | [default](screenshots/story-dark-default.png), [full](screenshots/story-dark-full.png), [default](screenshots/story-light-default.png), [full](screenshots/story-light-full.png) |
| Source profile | `/u/wired` | [default](screenshots/profile-light-default.png), [full](screenshots/profile-light-full.png) |
| Log in | `/login` | [default](screenshots/login-light-default.png), [full](screenshots/login-light-full.png) |
| Sign up | `/sign-up` | [default](screenshots/signup-light-default.png), [full](screenshots/signup-light-full.png) |
| Home feed, phone | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png) |
| Story, phone | `/world-business/k7vz2u4u` | [default](screenshots/mobile-story-light-default.png), [full](screenshots/mobile-story-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Dark theme | the sidebar pill | the theme control cycles System -> Light -> Dark; it was clicked twice to dark and the real dark surface measured | the Dark theme group + home/story dark shots |
| Sort dropdown | / | the Trending trigger was opened in place — the opened state is measured | [feed-trending](#sort-dropdown) opened |
| Auth fields | /login and /sign-up | the email fields were focused and filled (never submitted); focused and filled states recorded | [lg-email](#email-field), [su-email](#sign-up-email) |
| The signed-in product | a Digg account | voting, commenting, submitting and profile settings all need an account | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 18 components were given a real keyboard focus. 1 draw an outline ring: `lg-signup` (1px auto rgba(171, 171, 191, 0.5), offset 1px). 16 draw a focus ring as a shadow instead: `sb-home`, `sb-tech`, `sb-pill`, `sb-login`, `sb-signup`, `feed-trending`, `d-vote`, `d-signup`, `d-trending`, `st-sources`, `st-crumb`, `lg-google`, `lg-x`, `lg-continue`, `su-continue`, `m-vote`. The other 1 show no measured change: `st-vote`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.1s | `cubic-bezier(0.4, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, background, background-color, border-color, box-shadow, color, fill, opacity, outline-color, stroke, text-decoration-color, transform | cat-card, d-card, lg-continue, lg-google, lg-x, m-card, pf-card, post-card and more |
| 0.15s | `cubic-bezier(0.4, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, all, background-color, border-color, box-shadow, color, fill, height, outline-color, padding, stroke, text-decoration-color, width | cat-tech-active, d-signup, d-trending, d-vote, feed-compact, feed-trending, lg-email, lg-pass and more |
| 0.15s | `ease-out` | color, opacity, text-decoration-color | lg-signup, post-avatars, post-sources, st-sources |
| 0.16s | `cubic-bezier(0.23, 1, 0.32, 1)` | scale | st-vote |
| 0.28s | `cubic-bezier(0.77, 0, 0.175, 1)` | background-color, border-color, color | st-vote |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Story card](#story-card) | 704 x 183 | 1px solid transparent | 18px | transparent | none | 14px 16px |
| [Category card](#category-card) | 704 x 160 | 1px solid transparent | 18px | transparent | none | 14px 16px |
| [Top Contributors](#top-contributors) | 376 x 352 | 1px solid rgba(0, 0, 0, 0.08) | 18px | #ffffff `color.white` | rgba(22, 22, 23, 0.1) 0px 0px 0px 0px | 24px 0px |
| [Top Posts panel](#top-posts-panel) | 376 x 556 | 1px solid rgba(0, 0, 0, 0.08) | 18px | #ffffff `color.white` | rgba(22, 22, 23, 0.1) 0px 0px 0px 0px | 24px 0px |
| [Stat card](#stat-card) | 376 x 384 | 1px solid rgba(0, 0, 0, 0.08) | 18px | #ffffff `color.white` | rgba(22, 22, 23, 0.1) 0px 0px 0px 0px | 24px 0px |
| [Sources list](#sources-list) | 376 x 246 | 1px solid rgba(0, 0, 0, 0.08) | 18px | #ffffff `color.white` | rgba(22, 22, 23, 0.1) 0px 0px 0px 0px | 24px 0px |
| [Card (dark)](#card-dark) | 704 x 183 | 1px solid transparent | 18px | transparent | none | 14px 16px |
| [Mobile card](#mobile-card) | 390 x 207 | 1px solid transparent | 18px | transparent | none | 14px 16px |

## Components

### Left sidebar

The left rail on every surface: pill-radius category rows (the active row fills #f0f0f5), the System -> Light -> Dark theme pill and the Log in / Sign up CTAs.

#### Sidebar item (active)
The Home row in the left sidebar — icon + label pill, painted selected on the feed; measured, never followed. Read as `sb-home` on the home feed page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 231 x 40; padding 4px 12px; radius 3.35544e+07px; background #f0f0f5; text roobert 14/20 600, #161617; transition width 0.15s cubic-bezier(0.4, 0, 0.2, 1), height 0.15s cubic-bezier(0.4, 0, 0.2, 1), padding 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| focus-visible | shadow #ababbf 0px 0px 0px 2px |

![Sidebar item (active) default](components/crops/sb-home-default.png) ![Sidebar item (active) hover](components/crops/sb-home-hover.png) ![Sidebar item (active) focus-visible](components/crops/sb-home-focus-visible.png) ![Sidebar item (active) pressed](components/crops/sb-home-pressed.png)

#### Sidebar item
A category row in the left sidebar (Technology, with its badge icon); measured, never followed. Read as `sb-tech` on the home feed page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 231 x 40; padding 4px 12px; radius 3.35544e+07px; background transparent; text roobert 14/20 600, #161617; transition width 0.15s cubic-bezier(0.4, 0, 0.2, 1), height 0.15s cubic-bezier(0.4, 0, 0.2, 1), padding 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #f0f0f5 |
| focus-visible | shadow #ababbf 0px 0px 0px 2px; layers a.peer/menu-button.group/menu-button 231.0x40.0 transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, #ababbf 0px 0px 0px 2px, transparent 0px 0px 0px 0px 3.35544e+07px |
| pressed | background #f0f0f5 |

![Sidebar item default](components/crops/sb-tech-default.png) ![Sidebar item hover](components/crops/sb-tech-hover.png) ![Sidebar item focus-visible](components/crops/sb-tech-focus-visible.png) ![Sidebar item pressed](components/crops/sb-tech-pressed.png)

#### Theme pill
The sidebar theme pill (System / Light / Dark cycle); pressed is CDP-forced — the real cycle is exercised by the dark pass. Read as `sb-pill` on the home feed page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 231 x 40; padding 0px 16px; border 1px solid transparent; radius 26px; background #f0f0f5; text roobert 14/20 500, #161617; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #161617 |
| hover | background #dbe3f6 |
| focus-visible | border 1px solid #ababbf; shadow rgba(171, 171, 191, 0.5) 0px 0px 0px 3px |
| pressed | background #dbe3f6 |

![Theme pill default](components/crops/sb-pill-default.png) ![Theme pill hover](components/crops/sb-pill-hover.png) ![Theme pill focus-visible](components/crops/sb-pill-focus-visible.png) ![Theme pill pressed](components/crops/sb-pill-pressed.png)

#### Log in link
The sidebar Log in link to /login; measured, never followed. Read as `sb-login` on the home feed page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 231 x 40; padding 0px 16px; border 1px solid transparent; radius 26px; background #f0f0f5; text roobert 14/20 500, #161617; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #dbe3f6 |
| focus-visible | border 1px solid #ababbf; shadow rgba(171, 171, 191, 0.5) 0px 0px 0px 3px |
| pressed | background #dbe3f6 |

![Log in link default](components/crops/sb-login-default.png) ![Log in link hover](components/crops/sb-login-hover.png) ![Log in link focus-visible](components/crops/sb-login-focus-visible.png) ![Log in link pressed](components/crops/sb-login-pressed.png)

#### Sign up CTA
The blue Sign up button at the foot of the sidebar; measured, never followed. Read as `sb-signup` on the home feed page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 231 x 40; padding 0px 16px; border 1px solid transparent; radius 26px; background #1c66eb `color.blue.500`; text roobert 14/20 500, #ffffff `color.white`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background rgba(28, 102, 235, 0.8) `action.primary-hover` |
| focus-visible | border 1px solid #ababbf; shadow rgba(171, 171, 191, 0.5) 0px 0px 0px 3px |
| pressed | background rgba(28, 102, 235, 0.801409) |

![Sign up CTA default](components/crops/sb-signup-default.png) ![Sign up CTA hover](components/crops/sb-signup-hover.png) ![Sign up CTA focus-visible](components/crops/sb-signup-focus-visible.png) ![Sign up CTA pressed](components/crops/sb-signup-pressed.png)

#### Sidebar item (selected)
The Technology sidebar row on /tech — the painted selected state of a category item. Read as `cat-tech-active` on the technology category page.

**Values (default).** size 231 x 40; padding 4px 12px; radius 3.35544e+07px; background #f0f0f5; text roobert 14/20 600, #161617; transition width 0.15s cubic-bezier(0.4, 0, 0.2, 1), height 0.15s cubic-bezier(0.4, 0, 0.2, 1), padding 0.15s cubic-bezier(0.4, 0, 0.2, 1).

![Sidebar item (selected) default](components/crops/cat-tech-active-default.png)

#### Category crumb
The category chip link beside the back button; measured, never followed. Read as `st-crumb` on the story page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 170.55 x 40; padding 0px 16px; border 1px solid transparent; radius 26px; background #f0f0f5; text roobert 14/20 500, #161617; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #dbe3f6 |
| focus-visible | border 1px solid #ababbf; shadow rgba(171, 171, 191, 0.5) 0px 0px 0px 3px |
| pressed | background #dbe3f6 |

![Category crumb default](components/crops/st-crumb-default.png) ![Category crumb hover](components/crops/st-crumb-hover.png) ![Category crumb focus-visible](components/crops/st-crumb-focus-visible.png) ![Category crumb pressed](components/crops/st-crumb-pressed.png)

### Feed controls

The feed's sort and density controls: the Trending dropdown (105 x 36, opened state measured) and the Compact toggle (64 x 36).

#### Sort dropdown
The Trending sort trigger over the feed; its opened state is a local dropdown of sort options. Read as `feed-trending` on the home feed page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed, opened) | size 105.28 x 36; padding 8px 12px; border 1px solid #e5e5e5; radius 26px; background rgba(229, 229, 229, 0.3); text roobert 14/20 400, #161617; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, rgba(22, 22, 23, 0.7) |
| focus-visible | border 1px solid #ababbf; shadow rgba(171, 171, 191, 0.5) 0px 0px 0px 3px |

![Sort dropdown default](components/crops/feed-trending-default.png) ![Sort dropdown hover](components/crops/feed-trending-hover.png) ![Sort dropdown focus-visible](components/crops/feed-trending-focus-visible.png) ![Sort dropdown pressed](components/crops/feed-trending-pressed.png) ![Sort dropdown opened](components/crops/feed-trending-opened.png)

#### Density toggle
The Compact density control beside the sort dropdown; measured, never toggled. Read as `feed-compact` on the home feed page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 64 x 36; padding 8px 12px; border 1px solid #e5e5e5; radius 26px; background rgba(229, 229, 229, 0.3); text roobert 14/20 400, #161617; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #161617 |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Density toggle default](components/crops/feed-compact-default.png) ![Density toggle hover](components/crops/feed-compact-hover.png) ![Density toggle pressed](components/crops/feed-compact-pressed.png)

#### Category heading
The Technology feed heading. Read as `cat-title` on the technology category page.

**Values (default).** size 656 x 36; background transparent; text roobert 30/36 700, #161617.

![Category heading default](components/crops/cat-title-default.png)

### Story card

The feed's story card (704 x 183): semibold 16px headline, muted summary, the vote pill with its odometer digits, the comment count, the source-avatar cluster, the 'N Sources' link and the 120 x 80 thumbnail.

#### Story card
A feed story card: category chip, headline, summary, vote pill, comment link and source cluster, thumbnail at right. Read as `post-card` on the home feed page.

**Values (default).** size 704 x 183; padding 14px 16px; border 1px solid transparent; radius 18px; background transparent; text roobert 12/16 600, #161617; transition color 0.1s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), fill 0.1s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.1s cubic-bezier(0.4, 0, 0.2, 1); icon 12 x 12, rgba(22, 22, 23, 0.7).

![Story card default](components/crops/post-card-default.png)

#### Card headline
The card’s stretched headline link (data-post-headline); measured, never followed. Read as `post-headline` on the home feed page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 536 x 48; background transparent; text roobert 16/24 600, #161617 |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Card headline default](components/crops/post-headline-default.png) ![Card headline hover](components/crops/post-headline-hover.png) ![Card headline pressed](components/crops/post-headline-pressed.png)

#### Card summary
The one-two line summary under the headline. Read as `post-summary` on the home feed page.

**Values (default).** size 536 x 40; background transparent; text roobert 14/20 400, rgba(22, 22, 23, 0.7).

![Card summary default](components/crops/post-summary-default.png)

#### Vote pill
The digg-it vote pill on the card (icon + odometer count); pressed is CDP-forced — a real press would cast a vote. Read as `post-vote` on the home feed page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 32 x 24; radius 3.35544e+07px 26px 26px 3.35544e+07px; background transparent; text roobert 14/20 500, rgba(22, 22, 23, 0.7); transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 12 x 12, rgba(22, 22, 23, 0.7); layers ::after transparent 0px none 1; button.group/button.inline-flex 32.0x24.0 transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px 3.35544e+07px 26px 26px 3.35544e+07px; span.relative.flex 32.0x24.0 rgba(28, 102, 235, 0.05) T:1px solid rgba(28, 102, 235, 0.2) `border.vote-border` / R:1px solid rgba(28, 102, 235, |
| hover, pressed | text roobert 14/20 500, #161617; icon 12 x 12, #161617 |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Vote pill default](components/crops/post-vote-default.png) ![Vote pill hover](components/crops/post-vote-hover.png) ![Vote pill pressed](components/crops/post-vote-pressed.png)

#### Comment link
The comment-count link on the card; measured, never followed. Read as `post-comment` on the home feed page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 32 x 32; border 1px solid rgba(0, 0, 0, 0.08); radius 26px; background transparent; text roobert 14/20 500, #161617; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, rgba(22, 22, 23, 0.7) |
| hover, pressed | background rgba(229, 229, 229, 0.5) |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Comment link default](components/crops/post-comment-default.png) ![Comment link hover](components/crops/post-comment-hover.png) ![Comment link pressed](components/crops/post-comment-pressed.png)

#### Source avatar
A source avatar in the card’s cluster (popover anchor, initials); measured, never followed. Read as `post-avatars` on the home feed page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 24 x 24; radius 3.35544e+07px; background transparent; text roobert 12/16 400, rgba(22, 22, 23, 0.7); transition color 0.15s ease-out, text-decoration-color 0.15s ease-out, opacity 0.15s ease-out; layers span.group/avatar.flex 24.0x24.0 #fdfdff 0px 0px 0px 1.5px 3.35544e+07px; span.flex.size-full 24.0x24.0 #f0f0f5 3.35544e+07px; span.pointer-events-none.absolute 24.0x24.0 transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(0, 0, 0, 0.08) 0px 0px 0px 1px inset, rgba(0, 0, 0, 0.12) 0px 2px 4px 0px inset 3.35544e+07px |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

Child layers that carry the look: span 24x24 radius 3.35544e+07px shadow #fdfdff 0px 0px 0px 1.5px; span 24x24 background #f0f0f5 radius 3.35544e+07px; span 24x24 radius 3.35544e+07px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(0, 0, 0, 0.08) 0px 0px 0px 1px inset, rgba(0, 0, 0, 0.12) 0px 2px 4px 0px inset.

![Source avatar default](components/crops/post-avatars-default.png) ![Source avatar hover](components/crops/post-avatars-hover.png) ![Source avatar pressed](components/crops/post-avatars-pressed.png)

#### Sources link
The "N Sources, updated Xm ago" meta link; measured, never followed. Read as `post-sources` on the home feed page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 87 x 16; radius 2px; background transparent; text roobert 14/20 600, rgba(22, 22, 23, 0.7); transition color 0.15s ease-out, text-decoration-color 0.15s ease-out, opacity 0.15s ease-out |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Sources link default](components/crops/post-sources-default.png) ![Sources link hover](components/crops/post-sources-hover.png) ![Sources link pressed](components/crops/post-sources-pressed.png)

#### Card thumbnail
The story’s right-side thumbnail inside the card. Read as `post-thumb` on the home feed page.

**Values (default).** size 120 x 80; background transparent; text roobert 14/20 400, transparent.

![Card thumbnail default](components/crops/post-thumb-default.png)

#### Category card
A story card on the Technology feed — same anatomy as the trending card. Read as `cat-card` on the technology category page.

**Values (default).** size 704 x 160; padding 14px 16px; border 1px solid transparent; radius 18px; background transparent; text roobert 16/24 600, #161617; transition color 0.1s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), fill 0.1s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.1s cubic-bezier(0.4, 0, 0.2, 1); icon 12 x 12, rgba(22, 22, 23, 0.7).

![Category card default](components/crops/cat-card-default.png)

### Right rail

The two white rail panels beside the feed: Top Contributors (with the #e37b4c rank-one accent) and Top Posts Yesterday.

#### Top Contributors
The right-rail "Top Contributors" ranked panel. Read as `rail-contribs` on the home feed page.

**Values (default).** size 376 x 352; padding 24px 0px; border 1px solid rgba(0, 0, 0, 0.08); radius 18px; background #ffffff `color.white`; shadow rgba(22, 22, 23, 0.1) 0px 0px 0px 0px; text roobert 16/24 600, #161617.

![Top Contributors default](components/crops/rail-contribs-default.png)

#### Top Posts panel
The right-rail "Top Posts Yesterday" list with thumbnails. Read as `rail-posts` on the home feed page.

**Values (default).** size 376 x 556; padding 24px 0px; border 1px solid rgba(0, 0, 0, 0.08); radius 18px; background #ffffff `color.white`; shadow rgba(22, 22, 23, 0.1) 0px 0px 0px 0px; text roobert 16/24 600, #161617; icon 12 x 12, rgba(22, 22, 23, 0.7).

![Top Posts panel default](components/crops/rail-posts-default.png)

### Footer

The muted footer links at the bottom of the feed.

#### Site footer
The mono sitemap footer (About / Contact / Privacy Policy / Terms / Community Guidelines / © digg). Read as `site-footer` on the home feed page.

**Values (default).** size 376 x 56; padding 8px 0px 16px 0px; background transparent; text roobert 12/16 400, rgba(22, 22, 23, 0.7).

![Site footer default](components/crops/site-footer-default.png)

### Dark theme

The same feed measured with the theme pill set to dark: #161617 page, #1c1c1f cards, #fdfdff ink — real painted dark, not declared-only.

#### Card (dark)
A feed story card measured with the dark theme painted via the sidebar pill. Read as `d-card` on the home feed (theme pill set to dark) page.

**Values (default).** size 704 x 183; padding 14px 16px; border 1px solid transparent; radius 18px; background transparent; text roobert 12/16 600, #fdfdff; transition color 0.1s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), fill 0.1s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.1s cubic-bezier(0.4, 0, 0.2, 1); icon 12 x 12, rgba(253, 253, 255, 0.7).

![Card (dark) default](components/crops/d-card-default.png)

#### Headline (dark)
The card headline under the dark theme. Read as `d-headline` on the home feed (theme pill set to dark) page.

**Values (default).** size 536 x 48; background transparent; text roobert 16/24 600, #fdfdff.

![Headline (dark) default](components/crops/d-headline-default.png)

#### Vote pill (dark)
The digg-it vote pill under the dark theme. Read as `d-vote` on the home feed (theme pill set to dark) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 32 x 24; radius 3.35544e+07px 26px 26px 3.35544e+07px; background transparent; text roobert 14/20 500, rgba(253, 253, 255, 0.7); transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 12 x 12, rgba(253, 253, 255, 0.7); layers ::after transparent 0px none 1; button.group/button.inline-flex 32.0x24.0 transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px 3.35544e+07px 26px 26px 3.35544e+07px; span.relative.flex 32.0x24.0 rgba(28, 102, 235, 0.05) T:1px solid rgba(28, 102, 235, 0.2) `border.vote-border` / R:1px solid rgba(28, 102, 235, |
| hover | text roobert 14/20 500, #fdfdff; icon 12 x 12, #fdfdff |
| focus-visible | shadow rgba(28, 102, 235, 0.5) 0px 0px 0px 3px; text roobert 14/20 500, #fdfdff; icon 12 x 12, #fdfdff; layers ::after transparent 0px none 1; button.group/button.inline-flex 32.0x24.0 transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(28, 102, 235, 0.5) 0px 0px 0px 3px, transparent 0px 0px 0px 0px 3.35544e+07px 26px 26px 3.35544e+07px; span.relative.flex 32.0x24.0 rgba(28, 102, 235, 0.05) T:1px solid rgba(28, 102, 235, 0.2) `border.vote-border` / R:1px solid rgba(2 |
| pressed | text roobert 14/20 500, #fdfdff; icon 12 x 12, #fdfdff |

![Vote pill (dark) default](components/crops/d-vote-default.png) ![Vote pill (dark) hover](components/crops/d-vote-hover.png) ![Vote pill (dark) focus-visible](components/crops/d-vote-focus-visible.png) ![Vote pill (dark) pressed](components/crops/d-vote-pressed.png)

#### Sign up (dark)
The blue Sign up CTA under the dark theme. Read as `d-signup` on the home feed (theme pill set to dark) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 231 x 40; padding 0px 16px; border 1px solid transparent; radius 26px; background #1c66eb `color.blue.500`; text roobert 14/20 500, #ffffff `color.white`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background rgba(28, 102, 235, 0.8) `action.primary-hover` |
| focus-visible | border 1px solid #1c66eb `color.blue.500`; shadow rgba(28, 102, 235, 0.5) 0px 0px 0px 3px |
| pressed | background rgba(28, 102, 235, 0.8) `action.primary-hover` |

![Sign up (dark) default](components/crops/d-signup-default.png) ![Sign up (dark) hover](components/crops/d-signup-hover.png) ![Sign up (dark) focus-visible](components/crops/d-signup-focus-visible.png) ![Sign up (dark) pressed](components/crops/d-signup-pressed.png)

#### Sort dropdown (dark)
The Trending sort trigger under the dark theme. Read as `d-trending` on the home feed (theme pill set to dark) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 105.28 x 36; padding 8px 12px; border 1px solid rgba(255, 255, 255, 0.15); radius 26px; background rgba(255, 255, 255, 0.045); text roobert 14/20 400, #fdfdff; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, rgba(253, 253, 255, 0.7) |
| hover | background rgba(255, 255, 255, 0.075) |
| focus-visible | border 1px solid #1c66eb `color.blue.500`; shadow rgba(28, 102, 235, 0.5) 0px 0px 0px 3px |
| pressed | background rgba(255, 255, 255, 0.075) |

![Sort dropdown (dark) default](components/crops/d-trending-default.png) ![Sort dropdown (dark) hover](components/crops/d-trending-hover.png) ![Sort dropdown (dark) focus-visible](components/crops/d-trending-focus-visible.png) ![Sort dropdown (dark) pressed](components/crops/d-trending-pressed.png)

#### Rail panel (dark)
The Top Contributors panel under the dark theme. Read as `d-rail` on the home feed (theme pill set to dark) page.

**Values (default).** size 376 x 352; padding 24px 0px; border 1px solid rgba(255, 255, 255, 0.08); radius 18px; background #1c1c1f; shadow rgba(253, 253, 255, 0.1) 0px 0px 0px 0px; text roobert 16/24 600, #fdfdff.

![Rail panel (dark) default](components/crops/d-rail-default.png)

### Story page

A story detail page: the REPORT kicker, 36px headline, 20px summary, the 138 x 44 digg-it pill, the stat card (TODAY'S RANK over COMBINED VIEWS), the sources list and the TLDR prose.

#### REPORT kicker
The tracked-out REPORT label over the story headline. Read as `st-kicker` on the story page.

**Values (default).** size 672 x 24; background transparent; text roobert 12/16 600, rgba(22, 22, 23, 0.7).

![REPORT kicker default](components/crops/st-kicker-default.png)

#### Story headline
The serif story headline. Read as `st-h1` on the story page.

**Values (default).** size 672 x 80; background transparent; text roobert 36/40 700, #161617.

![Story headline default](components/crops/st-h1-default.png)

#### Story summary
The one-two line summary under the headline. Read as `st-summary` on the story page.

**Values (default).** size 672 x 56; background transparent; text roobert 20/28 400, rgba(22, 22, 23, 0.7).

![Story summary default](components/crops/st-summary-default.png)

#### digg it button
The "digg it" vote pill under the headline (icon + count); pressed is CDP-forced — a real press would cast a vote. Read as `st-vote` on the story page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 138.33 x 44; padding 3px 11px 3px 3px; border 1px solid rgba(28, 102, 235, 0.2) `border.vote-border`; radius 999px; background #fdfdff; text roobert 12/16 600, #1c66eb `color.blue.500`; transition background-color 0.28s cubic-bezier(0.77, 0, 0.175, 1), border-color 0.28s cubic-bezier(0.77, 0, 0.175, 1), color 0.28s cubic-bezier(0.77, 0, 0.175, 1), scale 0.16s cubic-bezier(0.23, 1, 0.32, 1); icon 12 x 12, #1c66eb `color.blue.500` |
| hover | border 1px solid rgba(28, 102, 235, 0.3) |
| pressed | size 134.18 x 42.68; border 1px solid rgba(28, 102, 235, 0.3); icon 11.64 x 11.64, #1c66eb `color.blue.500` |

![digg it button default](components/crops/st-vote-default.png) ![digg it button hover](components/crops/st-vote-hover.png) ![digg it button focus-visible](components/crops/st-vote-focus-visible.png) ![digg it button pressed](components/crops/st-vote-pressed.png)

#### Sources meta
The "N Sources, first seen Xh ago" meta cluster; measured, never followed. Read as `st-sources` on the story page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 86 x 16; radius 2px; background transparent; text roobert 14/20 600, rgba(22, 22, 23, 0.7); transition color 0.15s ease-out, text-decoration-color 0.15s ease-out, opacity 0.15s ease-out |
| focus-visible | shadow #fdfdff 0px 0px 0px 2px, #ababbf 0px 0px 0px 4px; layers a.rounded-xs.font-semibold 86.0x16.0 transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, #fdfdff 0px 0px 0px 2px, #ababbf 0px 0px 0px 4px, transparent 0px 0px 0px 0px 2px |

![Sources meta default](components/crops/st-sources-default.png) ![Sources meta hover](components/crops/st-sources-hover.png) ![Sources meta focus-visible](components/crops/st-sources-focus-visible.png) ![Sources meta pressed](components/crops/st-sources-pressed.png)

#### Stat card
The right-rail stat card — TODAY'S RANK over COMBINED VIEWS and the like/comment/save counts. Read as `st-stat` on the story page.

**Values (default).** size 376 x 384; padding 24px 0px; border 1px solid rgba(0, 0, 0, 0.08); radius 18px; background #ffffff `color.white`; shadow rgba(22, 22, 23, 0.1) 0px 0px 0px 0px; text roobert 12/16 600, rgba(22, 22, 23, 0.7); icon 12 x 12, rgba(22, 22, 23, 0.7).

![Stat card default](components/crops/st-stat-default.png)

#### Sources list
The right-rail "N Sources" list of source posts. Read as `st-srclist` on the story page.

**Values (default).** size 376 x 246; padding 24px 0px; border 1px solid rgba(0, 0, 0, 0.08); radius 18px; background #ffffff `color.white`; shadow rgba(22, 22, 23, 0.1) 0px 0px 0px 0px; text roobert 12/16 600, rgba(22, 22, 23, 0.7); icon 12 x 12, rgba(22, 22, 23, 0.7).

![Sources list default](components/crops/st-srclist-default.png)

#### TLDR label
The tracked TLDR section label over the summary prose. Read as `st-tldr` on the story page.

**Values (default).** size 605 x 16; background transparent; text roobert 10/16 600, rgba(22, 22, 23, 0.7).

![TLDR label default](components/crops/st-tldr-default.png)

#### TLDR paragraph
A body paragraph in the TLDR section. Read as `st-para` on the story page.

**Values (default).** size 605 x 189; background transparent; text roobert 18/31.5 500, #161617.

![TLDR paragraph default](components/crops/st-para-default.png)

### Source profile

A /u/<source> profile: the 20px source name over the same story cards as the feed.

#### Profile name
The source profile heading (@wired). Read as `pf-name` on the source profile page.

**Values (default).** size 61.06 x 28; background transparent; text roobert 20/28 600, #161617.

![Profile name default](components/crops/pf-name-default.png)

#### Profile story card
A story card in the source’s profile feed. Read as `pf-card` on the source profile page.

**Values (default).** size 704 x 183; padding 14px 16px; border 1px solid transparent; radius 18px; background transparent; text roobert 12/16 600, #161617; transition color 0.1s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), fill 0.1s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.1s cubic-bezier(0.4, 0, 0.2, 1); icon 12 x 12, rgba(22, 22, 23, 0.7).

![Profile story card default](components/crops/pf-card-default.png)

### Sign-in / sign-up

The Clerk auth surfaces: OAuth outline buttons, the 8px-rounded fields with their 0 1px 2px shadow, the primary Continue pill and the sign-up link. Measured signed out; never submitted.

#### Sign-in heading
"Welcome back!" — the Clerk sign-in card heading. Read as `lg-h1` on the login page.

**Values (default).** size 353 x 32; background transparent; text roobert 24/32 600, #161617.

![Sign-in heading default](components/crops/lg-h1-default.png)

#### Google OAuth
The "Continue with Google" outline button; measured, never followed. Read as `lg-google` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 353 x 36; padding 0px 10px; border 1px solid rgba(0, 0, 0, 0.08); radius 3.35544e+07px; background #fdfdff; shadow rgba(0, 0, 0, 0.05) 0px 1px 2px 0px; text roobert 13/18 500, rgba(22, 22, 23, 0.62); transition background-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), background 0.1s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), color 0.1s cubic-bezier(0.4, 0, 0.2, 1), fill 0.1s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.1s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.1s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.1s cubic-bezier(0.4, 0, 0.2, 1), transform 0.1s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #f0f0f5 |
| focus-visible | border 1px solid #ababbf; shadow rgba(171, 171, 191, 0.5) 0px 0px 0px 3px, rgba(0, 0, 0, 0.05) 0px 1px 2px 0px; transition background-color 0.2s ease, background 0.2s ease, border-color 0.2s ease, color 0.2s ease, fill 0.2s ease, stroke 0.2s ease, opacity 0.2s ease, box-shadow 0.2s ease, transform 0.2s ease |
| pressed | background #f0f0f5 |

![Google OAuth default](components/crops/lg-google-default.png) ![Google OAuth hover](components/crops/lg-google-hover.png) ![Google OAuth focus-visible](components/crops/lg-google-focus-visible.png) ![Google OAuth pressed](components/crops/lg-google-pressed.png)

#### X OAuth
The "Continue with X / Twitter" outline button; measured, never followed. Read as `lg-x` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 353 x 36; padding 0px 10px; border 1px solid rgba(0, 0, 0, 0.08); radius 3.35544e+07px; background #fdfdff; shadow rgba(0, 0, 0, 0.05) 0px 1px 2px 0px; text roobert 13/18 500, rgba(22, 22, 23, 0.62); transition background-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), background 0.1s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), color 0.1s cubic-bezier(0.4, 0, 0.2, 1), fill 0.1s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.1s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.1s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.1s cubic-bezier(0.4, 0, 0.2, 1), transform 0.1s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #f0f0f5 |
| focus-visible | border 1px solid #ababbf; shadow rgba(171, 171, 191, 0.5) 0px 0px 0px 3px, rgba(0, 0, 0, 0.05) 0px 1px 2px 0px; transition background-color 0.2s ease, background 0.2s ease, border-color 0.2s ease, color 0.2s ease, fill 0.2s ease, stroke 0.2s ease, opacity 0.2s ease, box-shadow 0.2s ease, transform 0.2s ease |
| pressed | background #f0f0f5 |

![X OAuth default](components/crops/lg-x-default.png) ![X OAuth hover](components/crops/lg-x-hover.png) ![X OAuth focus-visible](components/crops/lg-x-focus-visible.png) ![X OAuth pressed](components/crops/lg-x-pressed.png)

#### Email field
The "Enter your email address" identifier field; the filled state types an address then deletes it — nothing is submitted. Read as `lg-email` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 353 x 36; padding 4px 10px; border 1px solid #e5e5e5; radius 8px; background transparent; shadow rgba(0, 0, 0, 0.05) 0px 1px 2px 0px; text roobert 14/20 400, #161617; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1); placeholder rgba(22, 22, 23, 0.7) |
| focused, filled | border 1px solid #ababbf; shadow rgba(171, 171, 191, 0.5) 0px 0px 0px 3px, rgba(0, 0, 0, 0.05) 0px 1px 2px 0px |

![Email field default](components/crops/lg-email-default.png) ![Email field focused](components/crops/lg-email-focused.png) ![Email field filled](components/crops/lg-email-filled.png)

#### Password field
The password field; focused via a click-in, never filled. Read as `lg-pass` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 197 x 36; padding 4px 10px; border 1px solid #e5e5e5; radius 8px; background transparent; shadow rgba(0, 0, 0, 0.05) 0px 1px 2px 0px; text roobert 14/20 400, #161617; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1); placeholder rgba(22, 22, 23, 0.7) |
| focused | border 1px solid #ababbf; shadow rgba(171, 171, 191, 0.5) 0px 0px 0px 3px, rgba(0, 0, 0, 0.05) 0px 1px 2px 0px |

![Password field default](components/crops/lg-pass-default.png) ![Password field focused](components/crops/lg-pass-focused.png)

#### Continue button
The blue Continue submit; hover/focus measured, never pressed — it would submit the sign-in. Read as `lg-continue` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 353 x 36; padding 0px 10px; border 1px solid transparent; radius 3.35544e+07px; background #1c66eb `color.blue.500`; text roobert 14/20 500, #ffffff `color.white`; transition background-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), background 0.1s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), color 0.1s cubic-bezier(0.4, 0, 0.2, 1), fill 0.1s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.1s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.1s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.1s cubic-bezier(0.4, 0, 0.2, 1), transform 0.1s cubic-bezier(0.4, 0, 0.2, 1); layers ::after transparent 0px none 1 |
| hover | background rgba(28, 102, 235, 0.8) `action.primary-hover`; layers ::after transparent 0px none 0 |
| focus-visible | border 1px solid #ababbf; shadow rgba(171, 171, 191, 0.5) 0px 0px 0px 3px; transition background-color 0.2s ease, background 0.2s ease, border-color 0.2s ease, color 0.2s ease, fill 0.2s ease, stroke 0.2s ease, opacity 0.2s ease, box-shadow 0.2s ease, transform 0.2s ease |

![Continue button default](components/crops/lg-continue-default.png) ![Continue button hover](components/crops/lg-continue-hover.png) ![Continue button focus-visible](components/crops/lg-continue-focus-visible.png)

#### Sign up link
The "Don’t have an account? Sign up" link under the form; measured, never followed. Read as `lg-signup` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 46 x 17.98; background transparent; text roobert 13/18 500, #1c66eb `color.blue.500`; transition color 0.15s ease-out, text-decoration-color 0.15s ease-out, opacity 0.15s ease-out |
| hover | text roobert 13/18 500, #3a7bee |
| focus-visible | outline 1px auto rgba(171, 171, 191, 0.5), offset 1px; layers a.cl-footerActionLink.🔒️ 46.0x18.0 1px auto rgba(171, 171, 191, 0.5) offset 1px |
| pressed | text roobert 13/18 500, #1359d7 |

![Sign up link default](components/crops/lg-signup-default.png) ![Sign up link hover](components/crops/lg-signup-hover.png) ![Sign up link focus-visible](components/crops/lg-signup-focus-visible.png) ![Sign up link pressed](components/crops/lg-signup-pressed.png)

#### Sign-up heading
The Clerk sign-up card heading. Read as `su-h1` on the sign-up page.

**Values (default).** size 353 x 32; background transparent; text roobert 24/32 600, #161617.

![Sign-up heading default](components/crops/su-h1-default.png)

#### Sign-up email
The sign-up identifier field; the filled state types an address then deletes it — nothing is submitted. Read as `su-email` on the sign-up page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 353 x 36; padding 4px 10px; border 1px solid #e5e5e5; radius 8px; background transparent; shadow rgba(0, 0, 0, 0.05) 0px 1px 2px 0px; text roobert 14/20 400, #161617; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1); placeholder rgba(22, 22, 23, 0.7) |
| focused, filled | border 1px solid #ababbf; shadow rgba(171, 171, 191, 0.5) 0px 0px 0px 3px, rgba(0, 0, 0, 0.05) 0px 1px 2px 0px |

![Sign-up email default](components/crops/su-email-default.png) ![Sign-up email focused](components/crops/su-email-focused.png) ![Sign-up email filled](components/crops/su-email-filled.png)

#### Sign-up Continue
The sign-up Continue submit; hover/focus measured, never pressed. Read as `su-continue` on the sign-up page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 353 x 36; padding 0px 10px; border 1px solid transparent; radius 3.35544e+07px; background #1c66eb `color.blue.500`; text roobert 14/20 500, #ffffff `color.white`; transition background-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), background 0.1s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), color 0.1s cubic-bezier(0.4, 0, 0.2, 1), fill 0.1s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.1s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.1s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.1s cubic-bezier(0.4, 0, 0.2, 1), transform 0.1s cubic-bezier(0.4, 0, 0.2, 1); layers ::after transparent 0px none 1 |
| hover | background rgba(28, 102, 235, 0.8) `action.primary-hover`; layers ::after transparent 0px none 0 |
| focus-visible | border 1px solid #ababbf; shadow rgba(171, 171, 191, 0.5) 0px 0px 0px 3px; transition background-color 0.2s ease, background 0.2s ease, border-color 0.2s ease, color 0.2s ease, fill 0.2s ease, stroke 0.2s ease, opacity 0.2s ease, box-shadow 0.2s ease, transform 0.2s ease |

![Sign-up Continue default](components/crops/su-continue-default.png) ![Sign-up Continue hover](components/crops/su-continue-hover.png) ![Sign-up Continue focus-visible](components/crops/su-continue-focus-visible.png)

### Mobile (390 wide)

The phone surface at 390 wide: the 107px top bar, the story card and the feed footer.

#### Mobile top bar
The phone top bar (digg wordmark + menu trigger). Read as `m-bar` on the home feed page at 390 wide.

**Values (default).** size 390 x 107; background #f8f8fb; text roobert 14/20 500, #ffffff `color.white`; icon 21 x 21, rgba(22, 22, 23, 0.7).

![Mobile top bar default](components/crops/m-bar-default.png)

#### Mobile card
A story card at 390px. Read as `m-card` on the home feed page at 390 wide.

**Values (default).** size 390 x 207; padding 14px 16px; border 1px solid transparent; radius 18px; background transparent; text roobert 12/16 600, #161617; transition color 0.1s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), fill 0.1s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.1s cubic-bezier(0.4, 0, 0.2, 1); icon 12 x 12, rgba(22, 22, 23, 0.7).

![Mobile card default](components/crops/m-card-default.png)

#### Mobile vote pill
The digg-it vote pill at 390px. Read as `m-vote` on the home feed page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 32 x 24; radius 3.35544e+07px 26px 26px 3.35544e+07px; background transparent; text roobert 14/20 500, rgba(22, 22, 23, 0.7); transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 12 x 12, rgba(22, 22, 23, 0.7); layers ::after transparent 0px none 1; button.group/button.inline-flex 32.0x24.0 transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px 3.35544e+07px 26px 26px 3.35544e+07px; span.relative.flex 32.0x24.0 rgba(28, 102, 235, 0.05) T:1px solid rgba(28, 102, 235, 0.2) `border.vote-border` / R:1px solid rgba(28, 102, 235, |
| focus-visible | shadow rgba(171, 171, 191, 0.5) 0px 0px 0px 3px; text roobert 14/20 500, #161617; icon 12 x 12, #161617; layers ::after transparent 0px none 1; button.group/button.inline-flex 32.0x24.0 transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(171, 171, 191, 0.5) 0px 0px 0px 3px, transparent 0px 0px 0px 0px 3.35544e+07px 26px 26px 3.35544e+07px; span.relative.flex 32.0x24.0 rgba(28, 102, 235, 0.05) T:1px solid rgba(28, 102, 235, 0.2) `border.vote-border` / R:1px solid rgba( |

![Mobile vote pill default](components/crops/m-vote-default.png) ![Mobile vote pill hover](components/crops/m-vote-hover.png) ![Mobile vote pill focus-visible](components/crops/m-vote-focus-visible.png) ![Mobile vote pill pressed](components/crops/m-vote-pressed.png)

#### Mobile footer
The phone footer. Read as `m-footer` on the home feed page at 390 wide.

**Values (default).** size 358 x 48; background transparent; text roobert 12/16 400, rgba(22, 22, 23, 0.7).

![Mobile footer default](components/crops/m-footer-default.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the digg wordmark, the vote chevrons, the comment glyph, source favicons and the odometer digits) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

Everything interactive needs an account — digging a story, commenting, submitting, following sources, settings — and none of it was reached. What is genuinely public signed out: the home feed, the category feeds (/tech, /gaming, /entertainment, /world-business, /science, /sports, /ai), story pages, /u/<source> profiles, /login, /sign-up and /privacy. The vote pills and comment links were measured, never pressed — pressing them opens the sign-in flow, not a count.

### Pages

- **Vote and comment actions.** The digg-it pills and comment links gate on sign-in; they were measured at default/hover/focus-visible/pressed, never pressed — no vote count exists in this capture beyond what the feed prints.
- **Follow actions.** Sidebar category links, story cards and crumbs were measured and followed where they are plain links; the 'N Sources' links point at external publications and were measured, never followed.
- **Cookie banner.** A consent banner painted on first load; it was hidden for screenshots only — no consent choice was made.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error and loading states** were not seen on the public surface.

### Themes

Both themes paint signed out: the sidebar theme pill cycles System -> Light -> Dark, and the dark readings and screenshots were taken after cycling it to dark (verified paint: near-black #161617 field). System follows prefers-color-scheme; the light shots are the default render.

### Fonts

- **roobert** (everything — UI, cards, headings at 400-700), **ibmPlexSans** (declared @font-face for typeset prose) and **vt323** (the retro bitmap mono of the vote odometer's digits) are the served faces. They are served from Digg's CDN; the style guide falls back to system fonts.

### Screenshots

- The phone home feed captures as two `partN` clip tiles (7000 + 3339 px — the full 10,339 px page, bounded); every other full-page shot is a single document capture.
- Story headlines, summaries, thumbnails, avatars and source names are the product's published content; screenshots are 256-colour PNGs, read exact colours from the tokens or the raw files.

### Content left out

- Story headlines, summaries, TLDR prose, contributor names and avatars are the product's content; only frames and components were measured.
