# ElevenMusic components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from elevenmusic.io on 2026-11-13, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. elevenmusic.io is one Next.js app shell painting dark by default (a real light theme flips from the footer's own segmented control): a fixed left rail, a header, an inner scroller per page and a bottom player bar once a track plays, set in Inter with waldenburg display headings. Nothing was signed into, created, liked, remixed, shared or submitted; the email field was filled with sample text and cleared; a track card's Play was pressed to mount the player bar, and every gated control was measured, never pressed.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (99 components, 296 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (294 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-state.png`: the app paints `dark` by default and the `*-light-*` shots were taken after the footer's own Light-theme toggle. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x (the pages scroll inside one inner element, expanded for the shot); mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-dark-default.png), [full](screenshots/home-dark-full.png), [menu](screenshots/home-dark-menu.png), [search](screenshots/home-dark-search.png), [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png) |
| Explore | `/explore` | [default](screenshots/explore-dark-default.png), [full](screenshots/explore-dark-full.png), [playing](screenshots/explore-dark-playing.png), [default](screenshots/explore-light-default.png) |
| Charts | `/charts` | [default](screenshots/charts-dark-default.png), [full](screenshots/charts-dark-full.png), [default](screenshots/charts-light-default.png) |
| Tracks | `/tracks` | [default](screenshots/tracks-dark-default.png), [full](screenshots/tracks-dark-full.png) |
| Genres | `/genres` | [default](screenshots/genres-dark-default.png), [full](screenshots/genres-dark-full.png) |
| Genre: Electronic | `/genres/electronic` | [default](screenshots/genre-electronic-dark-default.png), [full](screenshots/genre-electronic-dark-full.png) |
| Sounds | `/sounds` | [default](screenshots/sounds-dark-default.png), [full](screenshots/sounds-dark-full.png) |
| Tools | `/tools` | [default](screenshots/tools-dark-default.png), [full](screenshots/tools-dark-full.png) |
| Artist profile | `/artists/ghostmkc-5JuuiL` | [default](screenshots/artist-dark-default.png), [full](screenshots/artist-dark-full.png) |
| Playlist | `/playlists/69eb381eb3c0fe73c21c695c` | [default](screenshots/playlist-dark-default.png), [full](screenshots/playlist-dark-full.png) |
| Blog | `/blog` | [default](screenshots/blog-dark-default.png), [full](screenshots/blog-dark-full.png) |
| Pricing | `/pricing` | [default](screenshots/pricing-dark-default.png), [full](screenshots/pricing-dark-full.png), [default](screenshots/pricing-light-default.png) |
| Log in | `/login` | [default](screenshots/login-dark-default.png), [options](screenshots/login-dark-options.png), [default](screenshots/login-light-default.png) |
| Sign in (alias) | `/sign-in` | [default](screenshots/signin-dark-default.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-dark-default.png), [full](screenshots/mobile-home-dark-full.png) |
| Explore, phone | `/explore` | [default](screenshots/mobile-explore-dark-default.png), [full](screenshots/mobile-explore-dark-full.png) |
| Charts, phone | `/charts` | [default](screenshots/mobile-charts-dark-default.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Resources dropdown | every header | the Resources trigger's own click | [home-dark-menu](screenshots/home-dark-menu.png), [nav-dropdown](#nav-dropdown), [menu-link](#menu-link) |
| Sign-in dialog (Search) | every page | the sidebar Search button's own click — search is gated behind an account | [home-dark-search](screenshots/home-dark-search.png) |
| Player bar | /explore | a track card's own Play — local media playback; Like/Remix/Share never pressed | [explore-dark-playing](screenshots/explore-dark-playing.png), [player-bar](#player-bar) |
| Email options | /login | the Show-other-options button's own toggle; the form was never submitted | [login-dark-options](screenshots/login-dark-options.png), [email-field](#email-field) |
| Light theme | the footer theme control | the Light segment's own toggle (persisted by the product's cookie) | [home-light-default](screenshots/home-light-default.png) |
| Cookiebot / Google One-Tap overlays | every page | hidden, never answered (no consent button was ever clicked, nothing signed into) | hidden before every shot and reading |
| Signed-in product | create, library, composer, chat, publish | every Create/Library/Composer surface and Like/Remix/Share sits behind sign-in | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 58 components were given a real keyboard focus. 52 draw an outline ring: `sidebar-nav` (1px solid #fafafa `dark.color.ink.foreground`, offset 2px), `sidebar-action` (1px solid #fafafa `dark.color.ink.foreground`, offset 2px), `sidebar-promo` (1px solid #fafafa `dark.color.ink.foreground`, offset 2px), `playlist-row` (1px solid #fafafa `dark.color.ink.foreground`, offset 1px), `icon-button` (1px solid #ffffff `dark.color.focus.ring`, offset 2px), `sidebar-collapse` (1px solid #ffffff `dark.color.focus.ring`, offset 2px), `new-playlist-btn` (1px solid #ffffff `dark.color.focus.ring`, offset 2px), `signin-btn` (1px solid #ffffff `dark.color.focus.ring`, offset 2px), `cta-btn` (1px solid #ffffff `dark.color.focus.ring`, offset 2px), `attach-btn` (1px solid #ffffff `dark.color.focus.ring`, offset 2px), `send-button` (1px solid #ffffff `dark.color.focus.ring`, offset 2px), `seg-tab-on` (1px solid #ffffff `dark.color.focus.ring`, offset 2px), `demo-card` (1px solid #ffffff `dark.color.focus.ring`, offset 2px), `carousel-prev` (1px solid #ffffff `dark.color.focus.ring`, offset 2px), `carousel-dot` (1px solid #ffffff `dark.color.focus.ring`, offset 2px), `footer-link` (1px solid #ffffff `dark.color.focus.ring`, offset 2px), `lang-btn` (1px solid #ffffff `dark.color.focus.ring`, offset 2px), `cookie-btn` (1px solid #ffffff `dark.color.focus.ring`, offset 2px), `theme-dark-btn` (1px solid #ffffff `dark.color.focus.ring`, offset 2px), `theme-light-btn` (1px solid #ffffff `dark.color.focus.ring`, offset 2px), `play-feature` (1px solid #ffffff `dark.color.focus.ring`, offset 2px), `remix-chip` (1px solid #ffffff `dark.color.focus.ring`, offset 2px), `genre-card` (on a child: 1px solid #ffffff `dark.color.focus.ring` offset 2px), `play-genre` (1px solid #ffffff `dark.color.focus.ring`, offset 2px), `artist-link` (1px auto rgba(255, 255, 255, 0.5) `dark.color.border.field-border-focus`, offset 1px), `player-play` (1px solid #ffffff `dark.color.focus.ring`, offset 2px), `player-prev` (1px solid #ffffff `dark.color.focus.ring`, offset 2px), `player-next` (1px solid #ffffff `dark.color.focus.ring`, offset 2px), `player-repeat` (1px solid #ffffff `dark.color.focus.ring`, offset 2px), `chart-play` (1px solid #ffffff `dark.color.focus.ring`, offset 2px), `shuffle-btn` (1px solid #ffffff `dark.color.focus.ring`, offset 2px), `share-btn` (1px solid #ffffff `dark.color.focus.ring`, offset 2px), `chart-row` (on a child: 1px auto rgba(255, 255, 255, 0.5) `dark.color.border.field-border-focus` offset 1px), `like-btn` (1px solid #ffffff `dark.color.focus.ring`, offset 2px), `remix-btn` (1px solid #ffffff `dark.color.focus.ring`, offset 2px), `chart-artist` (1px auto rgba(255, 255, 255, 0.5) `dark.color.border.field-border-focus`, offset 1px), `plan-cta-free` (2px solid #fafafa `dark.color.ink.foreground`, offset 4px), `plan-cta-pro` (2px solid #fafafa `dark.color.ink.foreground`, offset 4px), `faq-item` (1px solid #ffffff `dark.color.focus.ring`, offset 2px), `sso-google` (1px solid #ffffff `dark.color.focus.ring`, offset 2px), `sso-apple` (1px solid #ffffff `dark.color.focus.ring`, offset 2px), `options-btn` (1px solid #ffffff `dark.color.focus.ring`, offset 2px), `tos-checkbox` (1px solid #ffffff `dark.color.focus.ring`, offset 2px), `tos-link` (1px auto rgba(255, 255, 255, 0.5) `dark.color.border.field-border-focus`, offset 1px), `tryit-link` (1px auto rgba(255, 255, 255, 0.5) `dark.color.border.field-border-focus`, offset 1px), `m-search-btn` (1px solid #ffffff `dark.color.focus.ring`, offset 2px), `m-cta` (1px solid #ffffff `dark.color.focus.ring`, offset 2px), `m-tab` (1px auto rgba(255, 255, 255, 0.5) `dark.color.border.field-border-focus`, offset 1px), `m-menu-btn` (1px solid #ffffff `dark.color.focus.ring`, offset 2px), `player-volume` (1px solid #ffffff `dark.color.focus.ring`, offset 2px), `player-queue` (1px solid #ffffff `dark.color.focus.ring`, offset 2px), `m-menu-link` (1px solid #ffffff `dark.color.focus.ring`, offset 2px). 2 draw a focus ring as a shadow instead: `nav-link`, `nav-trigger`. The other 4 show no measured change: `menu-link`, `prompt-chip`, `track-row`, `play-hero`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.075s | `cubic-bezier(0.4, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, background-color, border-color, color, fill, outline-color, stroke, text-decoration-color | attach-btn |
| 0.1s | `cubic-bezier(0.4, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, background-color, border-color, color, fill, outline-color, rotate, scale, stroke, text-decoration-color, transform, translate | m-tab, seg-tab-off, seg-tab-on |
| 0.15s | `cubic-bezier(0, 0, 0.2, 1)` | background-color, color, transform | m-chip, prompt-chip |
| 0.15s | `cubic-bezier(0.4, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, all, background-color, border-color, box-shadow, color, fill, outline-color, rotate, scale, stroke, text-decoration-color, transform, translate | carousel-next, carousel-prev, chart-play, continue-btn, cookie-btn, cta-btn, demo-card, email-field and more |
| 0.2s | `cubic-bezier(0, 0, 0.2, 1)` | background-color, transform | play-hero |
| 0.2s | `cubic-bezier(0.4, 0, 0.2, 1)` | opacity, transform | send-button |
| 0.22s | `cubic-bezier(0.23, 1, 0.32, 1)` | rotate, scale, transform, translate | genre-card |
| 0.3s | `cubic-bezier(0, 0, 0.2, 1)` | background-color, transform | plan-cta-free, plan-cta-pro |
| 0.3s | `cubic-bezier(0.4, 0, 0.2, 1)` | height, width | nav-dropdown |
| 0.5s | `cubic-bezier(0.2, 0.8, 0.2, 1)` | background-color, width | carousel-dot |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Feature card](#feature-card) | 328 x 328.5 | - | 6px | #171717 `dark.color.surface.muted` | rgba(255, 255, 255, 0.1) 0px 0px 0px 1px inset | 0 |
| [Track card](#track-card) | 208 x 237 | - | - | transparent | none | 0px 0px 0px 16px |
| [Genre card](#genre-card) | 192 x 192 | - | 14px | rgba(255, 255, 255, 0.04) `dark.color.alpha.gray-50` | none | 0 |
| [Stem card](#stem-card) | 156 x 68 | - | 16px | #222222 `dark.color.surface.elevated` | rgba(255, 255, 255, 0.07) 0px 0px 0px 1px, rgba(0, 0, 0, 0.5) 0px 1px 2px 0px | 12px |
| [Plan card, Free](#plan-card-free) | 472 x 909.38 | - | 24px | #000000 `dark.color.surface.background` | none | 0 |
| [Plan card, Pro](#plan-card-pro) | 472 x 909.38 | - | 24px | #fafafa `dark.color.ink.foreground` | none | 0 |
| [Auth column](#auth-column) | 384 x 844 | - | - | transparent | none | 0 |
| [Sidebar promo](#sidebar-promo) | 224 x 49 | - | 24px | #222222 `dark.color.surface.elevated` | rgba(255, 255, 255, 0.07) 0px 0px 0px 1px, rgba(0, 0, 0, 0.5) 0px 1px 2px 0px | 6px 14px 6px 6px |

## Components

### Shell and navigation

The app chrome: the fixed left rail (logo, Search, nav, the Publish promo, playlists), the header with its Resources dropdown, and the Sign-in / Start-free pair.

#### Sidebar
The fixed left rail (248px): logo, Search, primary nav, the Publish-your-music promo and the Playlists list. Read as `sidebar` on the home page.

**Values (default).** size 248 x 900; background transparent; text Inter 14/20 450, #868686 `dark.color.ink.muted-foreground`; icon 7.72 x 13, #fafafa `dark.color.ink.foreground`; layers button.font-normal.focus-visible:focus-ring 224.0x49.0 #222222 `dark.color.surface.elevated` transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(255, 255, 255, 0.07) 0px 0px 0px 1px, rgba(0, 0, 0, 0.5) 0px 1px 2px 0px 24px; span.-right-1.-bottom-1 18.0x18.0 #000000 `dark.color.surface.background` 3.35544e+07px; div.absolute.inset.

Child layers that carry the look: button 224x49 background #222222 `dark.color.surface.elevated` radius 24px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(255, 255, 255, 0.07) 0px 0px 0px 1px, rgba(0, 0, 0, 0.5) 0px 1px 2px 0px; span 18x18 background #000000 `dark.color.surface.background` radius 3.35544e+07px; div 0x0 background #171717 `dark.color.surface.muted`.

![Sidebar default](components/crops/sidebar-default.png)

#### Sidebar nav item
A primary nav row in the rail (icon + label, 36px); Explore holds the selected state on /. Read as `sidebar-nav` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 224 x 36; padding 0px 8px 2px 8px; radius 10px; background transparent; text Inter 14/20 450, #868686 `dark.color.ink.muted-foreground`; icon 18 x 18, #868686 `dark.color.ink.muted-foreground`; layers ::before transparent 0px none 1 |
| hover | text Inter 14/20 450, #fafafa `dark.color.ink.foreground`; icon 18 x 18, #fafafa `dark.color.ink.foreground`; layers ::before rgba(255, 255, 255, 0.04) `dark.color.alpha.gray-50` 0px none 1; a::before.group/row.relative 224pxx34px rgba(255, 255, 255, 0.04) `dark.color.alpha.gray-50` 10px |
| focus-visible | outline 1px solid #fafafa `dark.color.ink.foreground`, offset 2px; layers ::before transparent 0px none 1; a.group/row.relative 224.0x36.0 1px solid #fafafa `dark.color.ink.foreground` offset 2px 10px |
| pressed | text Inter 14/20 450, #fafafa `dark.color.ink.foreground`; icon 18 x 18, #fafafa `dark.color.ink.foreground`; layers ::before rgba(255, 255, 255, 0.04) `dark.color.alpha.gray-50` 0px none 1; a::before.group/row.relative 224pxx34px rgba(255, 255, 255, 0.04) `dark.color.alpha.gray-50` 10px |

![Sidebar nav item default](components/crops/sidebar-nav-default.png) ![Sidebar nav item hover](components/crops/sidebar-nav-hover.png) ![Sidebar nav item focus-visible](components/crops/sidebar-nav-focus-visible.png) ![Sidebar nav item pressed](components/crops/sidebar-nav-pressed.png)

#### Sidebar action
A gated rail action (Composer/Chat) that prompts sign-in; measured, never pressed. Read as `sidebar-action` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 224 x 36; padding 0px 8px 2px 8px; radius 10px; background transparent; text Inter 14/20 450, #868686 `dark.color.ink.muted-foreground`; transition background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), color 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 18 x 18, #868686 `dark.color.ink.muted-foreground`; layers ::before transparent 0px none 1 |
| hover | text Inter 14/20 450, #fafafa `dark.color.ink.foreground`; icon 18 x 18, #fafafa `dark.color.ink.foreground`; layers ::before rgba(255, 255, 255, 0.04) `dark.color.alpha.gray-50` 0px none 1; button::before.transition-[background-color,color,box-shadow,border-color].focus-visible:focus-ring 224pxx34px rgba(255, 255, 255, 0.04) `dark.color.alpha.gray-50` 10px |
| focus-visible | outline 1px solid #fafafa `dark.color.ink.foreground`, offset 2px; layers ::before transparent 0px none 1; button.transition-[background-color,color,box-shadow,border-color].focus-visible:focus-ring 224.0x36.0 1px solid #fafafa `dark.color.ink.foreground` offset 2px 10px |
| pressed | text Inter 14/20 450, #fafafa `dark.color.ink.foreground`; icon 18 x 18, #fafafa `dark.color.ink.foreground`; layers ::before rgba(255, 255, 255, 0.04) `dark.color.alpha.gray-50` 0px none 1; button::before.transition-[background-color,color,box-shadow,border-color].focus-visible:focus-ring 224pxx34px rgba(255, 255, 255, 0.04) `dark.color.alpha.gray-50` 10px |

![Sidebar action default](components/crops/sidebar-action-default.png) ![Sidebar action hover](components/crops/sidebar-action-hover.png) ![Sidebar action focus-visible](components/crops/sidebar-action-focus-visible.png) ![Sidebar action pressed](components/crops/sidebar-action-pressed.png)

#### Sidebar promo
The Publish-your-music promo card in the rail (surface-1 fill, artwork chip). Read as `sidebar-promo` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 224 x 49; padding 6px 14px 6px 6px; radius 24px; background #222222 `dark.color.surface.elevated`; shadow rgba(255, 255, 255, 0.07) 0px 0px 0px 1px, rgba(0, 0, 0, 0.5) 0px 1px 2px 0px; text Inter 13/20 500, #fafafa `dark.color.ink.foreground`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #a1a1a1 `dark.color.ink.sidebar-foreground` |
| hover | background #2b2b2b `dark.color.surface.elevated-hover` |
| focus-visible | outline 1px solid #fafafa `dark.color.ink.foreground`, offset 2px |
| pressed | background #2b2b2b `dark.color.surface.elevated-hover` |

![Sidebar promo default](components/crops/sidebar-promo-default.png) ![Sidebar promo hover](components/crops/sidebar-promo-hover.png) ![Sidebar promo focus-visible](components/crops/sidebar-promo-focus-visible.png) ![Sidebar promo pressed](components/crops/sidebar-promo-pressed.png)

#### Playlist row
A media row in the rail's Playlists list (36px art + name + Featured tag). Read as `playlist-row` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 224 x 50; padding 0px 7px; radius 15px; background transparent; text Inter 13/18 400, rgba(250, 250, 250, 0.85); layers ::before transparent 0px none 1; div.absolute.inset-0 36.0x36.0 #171717 `dark.color.surface.muted`; div.cover-border.pointer-events-none 36.0x36.0 rgba(255, 255, 255, 0.05) 0px 0px 0px 1px inset 8px |
| hover | background rgba(255, 255, 255, 0.04) `dark.color.alpha.gray-50`; layers ::before transparent 0px none 1 |
| focus-visible | outline 1px solid #fafafa `dark.color.ink.foreground`, offset 1px; layers ::before transparent 0px none 1; a.group/media.[--row:3.125rem] 224.0x50.0 1px solid #fafafa `dark.color.ink.foreground` offset 1px 15px; div.absolute.inset-0 36.0x36.0 #171717 `dark.color.surface.muted`; div.cover-border.pointer-events-none 36.0x36.0 rgba(255, 255, 255, 0.05) 0px 0px 0px 1px inset 8px |
| pressed | background rgba(255, 255, 255, 0.04) `dark.color.alpha.gray-50`; layers ::before transparent 0px none 1 |

Child layers that carry the look: div 36x36 background #171717 `dark.color.surface.muted`; div 36x36 radius 8px shadow rgba(255, 255, 255, 0.05) 0px 0px 0px 1px inset.

![Playlist row default](components/crops/playlist-row-default.png) ![Playlist row hover](components/crops/playlist-row-hover.png) ![Playlist row focus-visible](components/crops/playlist-row-focus-visible.png) ![Playlist row pressed](components/crops/playlist-row-pressed.png)

#### Icon button
The rail's 30px Search icon button (opens the sign-in dialog). Read as `icon-button` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 30 x 30; radius 10px; background transparent; text Inter 14/20 400, #868686 `dark.color.ink.muted-foreground`; transition background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), color 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #868686 `dark.color.ink.muted-foreground` |
| hover | background rgba(255, 255, 255, 0.08) `dark.color.border.sidebar-border`; text Inter 14/20 400, #fafafa `dark.color.ink.foreground`; icon 16 x 16, #fafafa `dark.color.ink.foreground` |
| focus-visible | outline 1px solid #ffffff `dark.color.focus.ring`, offset 2px; layers button.inline-flex.items-center 30.0x30.0 1px solid #ffffff `dark.color.focus.ring` offset 2px 10px |
| pressed | size 29.4 x 29.4; background rgba(255, 255, 255, 0.08) `dark.color.border.sidebar-border`; text Inter 14/20 400, #fafafa `dark.color.ink.foreground`; icon 15.68 x 15.68, #fafafa `dark.color.ink.foreground` |

![Icon button default](components/crops/icon-button-default.png) ![Icon button hover](components/crops/icon-button-hover.png) ![Icon button focus-visible](components/crops/icon-button-focus-visible.png) ![Icon button pressed](components/crops/icon-button-pressed.png)

#### Sidebar collapse
The 32px rail-collapse icon button; measured, never pressed. Read as `sidebar-collapse` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 32 x 32; radius 10px; background transparent; text Inter 14/20 400, #868686 `dark.color.ink.muted-foreground`; transition background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), color 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #868686 `dark.color.ink.muted-foreground` |
| hover | background rgba(255, 255, 255, 0.08) `dark.color.border.sidebar-border`; text Inter 14/20 400, #fafafa `dark.color.ink.foreground`; icon 16 x 16, #fafafa `dark.color.ink.foreground` |
| focus-visible | outline 1px solid #ffffff `dark.color.focus.ring`, offset 2px; layers button.items-center.justify-center 32.0x32.0 1px solid #ffffff `dark.color.focus.ring` offset 2px 10px |
| pressed | size 31.36 x 31.36; background rgba(255, 255, 255, 0.08) `dark.color.border.sidebar-border`; text Inter 14/20 400, #fafafa `dark.color.ink.foreground`; icon 15.68 x 15.68, #fafafa `dark.color.ink.foreground` |

![Sidebar collapse default](components/crops/sidebar-collapse-default.png) ![Sidebar collapse hover](components/crops/sidebar-collapse-hover.png) ![Sidebar collapse focus-visible](components/crops/sidebar-collapse-focus-visible.png) ![Sidebar collapse pressed](components/crops/sidebar-collapse-pressed.png)

#### New-playlist button
The 24px + button on the Playlists heading; measured, never pressed. Read as `new-playlist-btn` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 24 x 24; radius 6px; background transparent; text Inter 12/16 400, rgba(255, 255, 255, 0.4) `dark.color.ink.subtle`; transition background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), color 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, rgba(255, 255, 255, 0.4) `dark.color.ink.subtle` |
| hover | background rgba(255, 255, 255, 0.08) `dark.color.border.sidebar-border`; text Inter 12/16 400, #fafafa `dark.color.ink.foreground`; icon 16 x 16, #fafafa `dark.color.ink.foreground` |
| focus-visible | outline 1px solid #ffffff `dark.color.focus.ring`, offset 2px; layers button.inline-flex.items-center 24.0x24.0 1px solid #ffffff `dark.color.focus.ring` offset 2px 6px |
| pressed | background rgba(255, 255, 255, 0.08) `dark.color.border.sidebar-border`; text Inter 12/16 400, #fafafa `dark.color.ink.foreground`; icon 16 x 16, #fafafa `dark.color.ink.foreground` |

![New-playlist button default](components/crops/new-playlist-btn-default.png) ![New-playlist button hover](components/crops/new-playlist-btn-hover.png) ![New-playlist button focus-visible](components/crops/new-playlist-btn-focus-visible.png) ![New-playlist button pressed](components/crops/new-playlist-btn-pressed.png)

#### Header
The app header (52px, translucent lab(0 0 0 / .95)): Main nav, Sign in, Start free. Read as `header` on the home page.

**Values (default).** size 1186 x 52; padding 0px 10px; background rgba(0, 0, 0, 0.95); text Inter 13/19.5 500, #868686 `dark.color.ink.muted-foreground`; icon 16 x 16, #868686 `dark.color.ink.muted-foreground`.

![Header default](components/crops/header-default.png)

#### Logo
The ElevenMusic wordmark/mark anchor. Read as `logo` on the home page.

**Values (default).** size 124.33 x 32; padding 0px 8px; radius 10px; background transparent; text Inter 16/24 400, #fafafa `dark.color.ink.foreground`; icon 7.72 x 13, #fafafa `dark.color.ink.foreground`.

![Logo default](components/crops/logo-default.png)

#### Header nav link
A header nav link (28px pill); measured, never followed. Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 62.56 x 28; padding 0px 10px; radius 3.35544e+07px; background transparent; text Inter 13/19.5 500, #868686 `dark.color.ink.muted-foreground`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background rgba(255, 255, 255, 0.04) `dark.color.alpha.gray-50`; text Inter 13/19.5 500, #fafafa `dark.color.ink.foreground` |
| focus-visible | shadow #ffffff 0px 0px 0px 2px; layers a.flex.h-7 62.6x28.0 transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, #ffffff `dark.color.focus.ring` 0px 0px 0px 2px, transparent 0px 0px 0px 0px 3.35544e+07px |
| pressed | background rgba(255, 255, 255, 0.04) `dark.color.alpha.gray-50`; text Inter 13/19.5 500, #fafafa `dark.color.ink.foreground` |

![Header nav link default](components/crops/nav-link-default.png) ![Header nav link hover](components/crops/nav-link-hover.png) ![Header nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Header nav link pressed](components/crops/nav-link-pressed.png)

#### Resources trigger
The header Resources button that opens the dropdown; toggled for the open state. Read as `nav-trigger` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 86.55 x 28; padding 0px 10px; radius 3.35544e+07px; background transparent; text Inter 13/19.5 500, #868686 `dark.color.ink.muted-foreground`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background rgba(255, 255, 255, 0.08) `dark.color.border.sidebar-border`; text Inter 13/19.5 500, #fafafa `dark.color.ink.foreground` |
| focus-visible | shadow #ffffff 0px 0px 0px 2px; layers button.flex.h-7 86.5x28.0 transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, #ffffff `dark.color.focus.ring` 0px 0px 0px 2px, transparent 0px 0px 0px 0px 3.35544e+07px |
| pressed | background rgba(255, 255, 255, 0.04) `dark.color.alpha.gray-50`; text Inter 13/19.5 500, #fafafa `dark.color.ink.foreground` |

![Resources trigger default](components/crops/nav-trigger-default.png) ![Resources trigger hover](components/crops/nav-trigger-hover.png) ![Resources trigger focus-visible](components/crops/nav-trigger-focus-visible.png) ![Resources trigger pressed](components/crops/nav-trigger-pressed.png)

#### Sign-in button
The dark Sign-in pill (surface-2 fill); measured, never pressed. Read as `signin-btn` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 69.84 x 32; padding 0px 12px; radius 3.35544e+07px; background #222222 `dark.color.surface.elevated`; shadow rgba(255, 255, 255, 0.07) 0px 0px 0px 1px, rgba(0, 0, 0, 0.5) 0px 1px 2px 0px; text Inter 14/20 400, #fafafa `dark.color.ink.foreground`; transition background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), color 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #2b2b2b `dark.color.surface.elevated-hover` |
| focus-visible | outline 1px solid #ffffff `dark.color.focus.ring`, offset 2px |
| pressed | size 68.45 x 31.36; background #2b2b2b `dark.color.surface.elevated-hover` |

![Sign-in button default](components/crops/signin-btn-default.png) ![Sign-in button hover](components/crops/signin-btn-hover.png) ![Sign-in button focus-visible](components/crops/signin-btn-focus-visible.png) ![Sign-in button pressed](components/crops/signin-btn-pressed.png)

#### Start-free CTA
The white Start-free pill (primary fill); measured, never pressed. Read as `cta-btn` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 85.66 x 32; padding 0px 12px; radius 3.35544e+07px; background #fafafa `dark.color.ink.foreground`; text Inter 14/20 400, #0a0a0a `dark.color.ink.primary-foreground`; transition background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), color 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #faf8f7 `dark.color.action.primary-hover` |
| focus-visible | outline 1px solid #ffffff `dark.color.focus.ring`, offset 2px |
| pressed | size 83.94 x 31.36; background #faf8f7 `dark.color.action.primary-hover` |

![Start-free CTA default](components/crops/cta-btn-default.png) ![Start-free CTA hover](components/crops/cta-btn-hover.png) ![Start-free CTA focus-visible](components/crops/cta-btn-focus-visible.png) ![Start-free CTA pressed](components/crops/cta-btn-pressed.png)

#### Resources dropdown
The Resources menu panel (popover fill, opened by its own trigger). Read as `nav-dropdown` on the home page.

**Values (default).** size 274 x 194; radius 14px; background #2e2e2e `dark.color.surface.popover`; shadow rgba(0, 0, 0, 0.35) 0px 20px 24px 0px, rgba(0, 0, 0, 0.18) 0px 5px 8px 0px, rgba(255, 255, 255, 0.06) 0px 0px 0px 0.5px; text Inter 13/20 500, #fafafa `dark.color.ink.foreground`; transition width 0.3s cubic-bezier(0.4, 0, 0.2, 1), height 0.3s cubic-bezier(0.4, 0, 0.2, 1).

![Resources dropdown default](components/crops/nav-dropdown-default.png)

#### Menu link
A link inside the opened Resources dropdown. Read as `menu-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 222 x 20; background transparent; text Inter 13/20 500, #fafafa `dark.color.ink.foreground`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover, focus-visible, pressed | text Inter 13/20 500, #868686 `dark.color.ink.muted-foreground` |

![Menu link default](components/crops/menu-link-default.png) ![Menu link hover](components/crops/menu-link-hover.png) ![Menu link focus-visible](components/crops/menu-link-focus-visible.png) ![Menu link pressed](components/crops/menu-link-pressed.png)

### Home hero

The 'Make music yours.' waldenburg headline over the composer — the prompt field, the Attach/Create circles and the prompt chips — plus the demo list and carousel.

#### Hero headline
The "Make music yours." display headline (font-display light). Read as `hero-title` on the home page.

**Values (default).** size 349.08 x 44; background transparent; text waldenburg 40/44 300, #fafafa `dark.color.ink.foreground`.

![Hero headline default](components/crops/hero-title-default.png)

#### Hero copy
The muted lede under the headline. Read as `hero-lede` on the home page.

**Values (default).** size 349.08 x 20; background transparent; text Inter 14/20 400, #868686 `dark.color.ink.muted-foreground`.

![Hero copy default](components/crops/hero-lede-default.png)

#### Composer field
The prompt input in the hero composer (556px); sample text was typed and deleted, nothing sent. Read as `composer-field` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 556 x 36; padding 0px 8px 0px 6px; background transparent; text Inter 15/22.5 400, #fafafa `dark.color.ink.foreground`; placeholder #fafafa `dark.color.ink.foreground` |

![Composer field default](components/crops/composer-field-default.png) ![Composer field focused](components/crops/composer-field-focused.png) ![Composer field filled](components/crops/composer-field-filled.png)

#### Attach button
The composer's 36px + button (black circle); measured, never pressed. Read as `attach-btn` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 36 x 36; radius 3.35544e+07px; background #000000 `dark.color.surface.background`; shadow rgba(255, 255, 255, 0.06) 0px 0px 0px 1px, rgba(0, 0, 0, 0.06) 0px 0px 0px 1px, rgba(0, 0, 0, 0.06) 0px 1px 1px -0.5px, rgba(0, 0, 0, 0.06) 0px 3px 3px -1.5px; text Inter 16/24 500, #fafafa `dark.color.ink.foreground`; transition color 0.075s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.075s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.075s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.075s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.075s cubic-bezier(0.4, 0, 0.2, 1), fill 0.075s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.075s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.075s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.075s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.075s cubic-bezier(0.4, 0, 0.2, 1); icon 10 x 10, #fafafa `dark.color.ink.foreground` |
| focus-visible | shadow rgba(255, 255, 255, 0.6) 0px 0px 0px 2px, rgba(0, 0, 0, 0.06) 0px 0px 0px 1px, rgba(0, 0, 0, 0.06) 0px 1px 1px -0.5px, rgba(0, 0, 0, 0.06) 0px 3px 3px -1.5px; outline 1px solid #ffffff `dark.color.focus.ring`, offset 2px |

![Attach button default](components/crops/attach-btn-default.png) ![Attach button hover](components/crops/attach-btn-hover.png) ![Attach button focus-visible](components/crops/attach-btn-focus-visible.png) ![Attach button pressed](components/crops/attach-btn-pressed.png)

#### Send button
The composer's white 36px circular send button (Create); measured, never pressed. Read as `send-button` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 36 x 36; radius 3.35544e+07px; background #fafafa `dark.color.ink.foreground`; text Inter 16/24 400, #000000 `dark.color.surface.background`; transition opacity 0.2s cubic-bezier(0.4, 0, 0.2, 1), transform 0.2s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #000000 `dark.color.surface.background` |
| focus-visible | outline 1px solid #ffffff `dark.color.focus.ring`, offset 2px |
| pressed | size 34.2 x 34.2; icon 15.2 x 15.2, #000000 `dark.color.surface.background` |

![Send button default](components/crops/send-button-default.png) ![Send button hover](components/crops/send-button-hover.png) ![Send button focus-visible](components/crops/send-button-focus-visible.png) ![Send button pressed](components/crops/send-button-pressed.png)

#### Prompt chip
A suggestion chip under the composer (lighten-100 fill, pill). Read as `prompt-chip` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 78.53 x 28; padding 0px 12px; radius 3.35544e+07px; background rgba(255, 255, 255, 0.08) `dark.color.border.sidebar-border`; text Inter 12/16 400, #868686 `dark.color.ink.muted-foreground`; transition background-color 0.15s cubic-bezier(0, 0, 0.2, 1), color 0.15s cubic-bezier(0, 0, 0.2, 1), transform 0.15s cubic-bezier(0, 0, 0.2, 1) |
| hover | background rgba(255, 255, 255, 0.11) `dark.color.alpha.gray-150`; text Inter 12/16 400, #fafafa `dark.color.ink.foreground` |
| pressed | size 76.18 x 27.16; background rgba(255, 255, 255, 0.11) `dark.color.alpha.gray-150`; text Inter 12/16 400, #fafafa `dark.color.ink.foreground` |

![Prompt chip default](components/crops/prompt-chip-default.png) ![Prompt chip hover](components/crops/prompt-chip-hover.png) ![Prompt chip focus-visible](components/crops/prompt-chip-focus-visible.png) ![Prompt chip pressed](components/crops/prompt-chip-pressed.png)

#### Segmented tab, selected
The selected segment (Songs) of the Songs/Sounds control (lighten-150 fill). Read as `seg-tab-on` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 74.52 x 40; padding 0px 16px; radius 3.35544e+07px; background rgba(255, 255, 255, 0.11) `dark.color.alpha.gray-150`; text Inter 14/20 500, #fafafa `dark.color.ink.foreground`; transition color 0.1s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), fill 0.1s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.1s cubic-bezier(0.4, 0, 0.2, 1); layers ::after #fafafa `dark.color.ink.foreground` 0px none 0 |
| focus-visible | outline 1px solid #ffffff `dark.color.focus.ring`, offset 2px |

![Segmented tab, selected default](components/crops/seg-tab-on-default.png) ![Segmented tab, selected hover](components/crops/seg-tab-on-hover.png) ![Segmented tab, selected focus-visible](components/crops/seg-tab-on-focus-visible.png) ![Segmented tab, selected pressed](components/crops/seg-tab-on-pressed.png)

#### Segmented tab
An unselected segment (Sounds/Featured rail tabs). Read as `seg-tab-off` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 82.84 x 40; padding 0px 16px; radius 3.35544e+07px; background transparent; text Inter 14/20 500, #868686 `dark.color.ink.muted-foreground`; transition color 0.1s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.1s cubic-bezier(0.4, 0, 0.2, 1), fill 0.1s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.1s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.1s cubic-bezier(0.4, 0, 0.2, 1); layers ::after #fafafa `dark.color.ink.foreground` 0px none 0; button::after.relative.inline-flex 82.8438pxx2px #fafafa `dark.color.ink.foreground` |
| hover, pressed | background rgba(255, 255, 255, 0.08) `dark.color.border.sidebar-border`; text Inter 14/20 500, #fafafa `dark.color.ink.foreground`; layers ::after #fafafa `dark.color.ink.foreground` 0px none 0 |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

Child layers that carry the look: button::after 82.8438pxx2px background #fafafa `dark.color.ink.foreground`.

![Segmented tab default](components/crops/seg-tab-off-default.png) ![Segmented tab hover](components/crops/seg-tab-off-hover.png) ![Segmented tab pressed](components/crops/seg-tab-off-pressed.png)

#### Track row
A song row in the demo list (art + title + artist); measured, never pressed. Read as `track-row` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 614.66 x 52; radius 16px; background transparent; text Inter 16/24 400, #fafafa `dark.color.ink.foreground`; transition background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), color 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1) |

![Track row default](components/crops/track-row-default.png) ![Track row hover](components/crops/track-row-hover.png) ![Track row focus-visible](components/crops/track-row-focus-visible.png) ![Track row pressed](components/crops/track-row-pressed.png)

#### Stem card
A stem/description card in the hero demo (surface-1 fill). Read as `demo-card` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 156 x 68; padding 12px; radius 16px; background #222222 `dark.color.surface.elevated`; shadow rgba(255, 255, 255, 0.07) 0px 0px 0px 1px, rgba(0, 0, 0, 0.5) 0px 1px 2px 0px; text Inter 14/20 500, #fafafa `dark.color.ink.foreground`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #2b2b2b `dark.color.surface.elevated-hover` |
| focus-visible | outline 1px solid #ffffff `dark.color.focus.ring`, offset 2px |
| pressed | background #2b2b2b `dark.color.surface.elevated-hover` |

![Stem card default](components/crops/demo-card-default.png) ![Stem card hover](components/crops/demo-card-hover.png) ![Stem card focus-visible](components/crops/demo-card-focus-visible.png) ![Stem card pressed](components/crops/demo-card-pressed.png)

#### Carousel previous
The 32px frosted carousel arrow. Read as `carousel-prev` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 32 x 32; radius 3.35544e+07px; background rgba(46, 46, 46, 0.85); shadow rgba(0, 0, 0, 0.35) 0px 20px 24px 0px, rgba(0, 0, 0, 0.18) 0px 5px 8px 0px, rgba(255, 255, 255, 0.06) 0px 0px 0px 0.5px; text Inter 16/24 400, #fafafa `dark.color.ink.foreground`; transition transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #fafafa `dark.color.ink.foreground` |
| hover | background #2e2e2e `dark.color.surface.popover` |
| focus-visible | outline 1px solid #ffffff `dark.color.focus.ring`, offset 2px |
| pressed | size 30.4 x 30.4; background #2e2e2e `dark.color.surface.popover`; icon 15.2 x 15.2, #fafafa `dark.color.ink.foreground` |

![Carousel previous default](components/crops/carousel-prev-default.png) ![Carousel previous hover](components/crops/carousel-prev-hover.png) ![Carousel previous focus-visible](components/crops/carousel-prev-focus-visible.png) ![Carousel previous pressed](components/crops/carousel-prev-pressed.png)

#### Carousel next
The 32px frosted carousel arrow. Read as `carousel-next` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 32 x 32; radius 3.35544e+07px; background rgba(46, 46, 46, 0.85); shadow rgba(0, 0, 0, 0.35) 0px 20px 24px 0px, rgba(0, 0, 0, 0.18) 0px 5px 8px 0px, rgba(255, 255, 255, 0.06) 0px 0px 0px 0.5px; text Inter 16/24 400, #fafafa `dark.color.ink.foreground`; transition transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #fafafa `dark.color.ink.foreground` |
| pressed | size 30.4 x 30.4; background #2e2e2e `dark.color.surface.popover`; icon 15.2 x 15.2, #fafafa `dark.color.ink.foreground` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Carousel next default](components/crops/carousel-next-default.png) ![Carousel next hover](components/crops/carousel-next-hover.png) ![Carousel next pressed](components/crops/carousel-next-pressed.png)

#### Carousel dot
A carousel pagination dot (the active one is a white 32x6 pill). Read as `carousel-dot` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 6 x 6; radius 3.35544e+07px; background rgba(250, 250, 250, 0.3); text Inter 16/24 400, #fafafa `dark.color.ink.foreground`; transition width 0.5s cubic-bezier(0.2, 0.8, 0.2, 1), background-color 0.5s cubic-bezier(0.2, 0.8, 0.2, 1) |
| hover | background rgba(250, 250, 250, 0.5) |
| focus-visible | outline 1px solid #ffffff `dark.color.focus.ring`, offset 2px |
| pressed | background rgba(250, 250, 250, 0.5) |

![Carousel dot default](components/crops/carousel-dot-default.png) ![Carousel dot hover](components/crops/carousel-dot-hover.png) ![Carousel dot focus-visible](components/crops/carousel-dot-focus-visible.png) ![Carousel dot pressed](components/crops/carousel-dot-pressed.png)

#### Round play button
A white circular play button (36-48px); measured, never pressed here. Read as `play-hero` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 48 x 48; radius 3.35544e+07px; background rgba(255, 255, 255, 0.1) `dark.color.border.border`; shadow rgba(255, 255, 255, 0.12) 0px 0px 0px 1px inset; text Inter 16/24 400, #ffffff `dark.color.focus.ring`; transition background-color 0.2s cubic-bezier(0, 0, 0.2, 1), transform 0.2s cubic-bezier(0, 0, 0.2, 1); icon 20 x 20, #ffffff `dark.color.focus.ring` |
| hover | background rgba(255, 255, 255, 0.15) `dark.color.alpha.gray-200` |
| pressed | size 45.6 x 45.6; background rgba(255, 255, 255, 0.15) `dark.color.alpha.gray-200`; icon 19 x 19, #ffffff `dark.color.focus.ring` |

![Round play button default](components/crops/play-hero-default.png) ![Round play button hover](components/crops/play-hero-hover.png) ![Round play button focus-visible](components/crops/play-hero-focus-visible.png) ![Round play button pressed](components/crops/play-hero-pressed.png)

### Explore and browse

The create surface: the pill nav, the prompt input, the featured carousel, track and genre cards, and the shelf headings.

#### Sidebar nav item, selected
The Explore row held selected on its own page. Read as `sidebar-nav-selected` on the explore page.

**Values (selected).** size 224 x 36; padding 0px 8px 2px 8px; radius 10px; background transparent; text Inter 14/20 450, #fafafa `dark.color.ink.foreground`; icon 18 x 18, #fafafa `dark.color.ink.foreground`; layers ::before #222222 `dark.color.surface.elevated` 0px transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(255, 255, 255, 0.07) 0px 0px 0px 1px, rgba(0, 0, 0, 0.5) 0px 1px 2px 0px 1; a::before.group/row.relative 224pxx34px #222222 `dark.color.surface.elevated` transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px .

Child layers that carry the look: a::before 224pxx34px background #222222 `dark.color.surface.elevated` radius 10px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(255, 255, 255, 0.07) 0px 0px 0px 1px, rgba(0, 0, 0, 0.5) 0px 1px 2px 0px.

![Sidebar nav item, selected selected](components/crops/sidebar-nav-selected-selected.png)

#### Explore title
The "Create music" page heading. Read as `explore-title` on the explore page.

**Values (default).** size 444.42 x 44; background transparent; text waldenburg 40/44 300, #fafafa `dark.color.ink.foreground`.

![Explore title default](components/crops/explore-title-default.png)

#### Create nav
The pill nav under the title (Create/Composer/Styles/Sounds/Library — every item gated behind sign-in). Read as `create-nav` on the explore page.

**Values (default).** size 752 x 70; background transparent; text Inter 14/20 500, #fafafa `dark.color.ink.foreground`; icon 20 x 20, #868686 `dark.color.ink.muted-foreground`; layers div.composer-hairline.flex 40.0x40.0 #151515 `dark.color.surface.composer-surface` rgba(255, 255, 255, 0.15) `dark.color.alpha.gray-200` 0px 1px 0px 0px inset, #2b2b2b `dark.color.surface.elevated-hover` 0px 0px 0px 1px inset, rgba(255, 255, 255, 0.08) `dark.color.border.sidebar-border` 0px -1px 0px 0px inset, rgba(28, 25, 23, 0.53) `light.color.alpha.gray-500` 0px 1px 2px -1px, rgba(28, 25, 23, 0.

Child layers that carry the look: div 40x40 background #151515 `dark.color.surface.composer-surface` radius 12px shadow rgba(255, 255, 255, 0.15) `dark.color.alpha.gray-200` 0px 1px 0px 0px inset, #2b2b2b `dark.color.surface.elevated-hover` 0px 0px 0px 1px inset, rgba(255, 255, 255, 0.08) `dark.color.border.sidebar-border` 0px -1px 0px 0px inset, rgba(28, 25, 23, 0.53) `light.color.alpha.gray-500` 0px 1px 2px -1px, rgba(28, 25, 23, 0.53) `light.color.alpha.gray-500` 0px 10px 24px -10px; div 40x40 background #151515 `dark.color.surface.composer-surface` radius 12px shadow rgba(255, 255, 255, 0.15) `dark.color.alpha.gray-200` 0px 1px 0px 0px inset, #2b2b2b `dark.color.surface.elevated-hover` 0px 0px 0px 1px inset, rgba(255, 255, 255, 0.08) `dark.color.border.sidebar-border` 0px -1px 0px 0px inset, rgba(28, 25, 23, 0.53) `light.color.alpha.gray-500` 0px 1px 2px -1px, rgba(28, 25, 23, 0.53) `light.color.alpha.gray-500` 0px 10px 24px -10px; div 40x40 background #151515 `dark.color.surface.composer-surface` radius 12px shadow rgba(255, 255, 255, 0.15) `dark.color.alpha.gray-200` 0px 1px 0px 0px inset, #2b2b2b `dark.color.surface.elevated-hover` 0px 0px 0px 1px inset, rgba(255, 255, 255, 0.08) `dark.color.border.sidebar-border` 0px -1px 0px 0px inset, rgba(28, 25, 23, 0.53) `light.color.alpha.gray-500` 0px 1px 2px -1px, rgba(28, 25, 23, 0.53) `light.color.alpha.gray-500` 0px 10px 24px -10px.

![Create nav default](components/crops/create-nav-default.png)

#### Prompt input
The "Describe your song" prompt field (556px); sample text typed and deleted, nothing sent. Read as `explore-input` on the explore page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 556 x 36; padding 0px 8px 0px 6px; background transparent; text Inter 15/22.5 400, #fafafa `dark.color.ink.foreground`; placeholder #fafafa `dark.color.ink.foreground` |

![Prompt input default](components/crops/explore-input-default.png) ![Prompt input focused](components/crops/explore-input-focused.png) ![Prompt input filled](components/crops/explore-input-filled.png)

#### Feature card
The featured track's carousel card (artwork, title, artist, Remix chip). Read as `feature-card` on the explore page.

**Values (default).** size 328 x 328.5; radius 6px; background #171717 `dark.color.surface.muted`; shadow rgba(255, 255, 255, 0.1) 0px 0px 0px 1px inset; text Inter 16/24 400, #fafafa `dark.color.ink.foreground`; icon 16 x 16, #000000 `dark.color.surface.background`.

![Feature card default](components/crops/feature-card-default.png)

#### Card play button
The 36px play control on a feature card; pressed once below to mount the player bar. Read as `play-feature` on the explore page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 36 x 36; background transparent; text Inter 16/24 400, #fafafa `dark.color.ink.foreground`; transition background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), color 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #000000 `dark.color.surface.background`; layers span.flex.h-9 36.0x36.0 #ffffff `dark.color.focus.ring` transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 10px 15px -3px, rgba(0, 0, 0, 0.1) 0px 4px 6px -4px 3.35544e+07px |
| focus-visible | outline 1px solid #ffffff `dark.color.focus.ring`, offset 2px; layers button.items-center.transition-[background-color,color,box-shadow,border-color] 36.0x36.0 1px solid #ffffff `dark.color.focus.ring` offset 2px; span.flex.h-9 36.0x36.0 #ffffff `dark.color.focus.ring` transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 10px 15px -3px, rgba(0, 0, 0, 0.1) 0px 4px 6px -4px 3.35544e+ |

Child layers that carry the look: span 36x36 background #ffffff `dark.color.focus.ring` radius 3.35544e+07px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 10px 15px -3px, rgba(0, 0, 0, 0.1) 0px 4px 6px -4px.

![Card play button default](components/crops/play-feature-default.png) ![Card play button hover](components/crops/play-feature-hover.png) ![Card play button focus-visible](components/crops/play-feature-focus-visible.png) ![Card play button pressed](components/crops/play-feature-pressed.png)

#### Remix chip
The Remix chip on a feature card; measured, never pressed (gated). Read as `remix-chip` on the explore page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 78.42 x 32; padding 0px 10px; radius 3.35544e+07px; background #1c1c1c `dark.color.surface.surface-2`; text Inter 12/16 500, #fafafa `dark.color.ink.foreground`; transition background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), color 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #fafafa `dark.color.ink.foreground` |
| hover | background #292929 `dark.color.surface.composer-chip-hover` |
| focus-visible | outline 1px solid #ffffff `dark.color.focus.ring`, offset 2px |
| pressed | size 76.85 x 31.36; background #292929 `dark.color.surface.composer-chip-hover`; icon 15.68 x 15.68, #fafafa `dark.color.ink.foreground` |

![Remix chip default](components/crops/remix-chip-default.png) ![Remix chip hover](components/crops/remix-chip-hover.png) ![Remix chip focus-visible](components/crops/remix-chip-focus-visible.png) ![Remix chip pressed](components/crops/remix-chip-pressed.png)

#### Track card
A 208px track card in a shelf (artwork, title, artist, version badge); hover raises the play button. Read as `track-card` on the explore page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 208 x 237; padding 0px 0px 0px 16px; background transparent; text Inter 13/20 500, #fafafa `dark.color.ink.foreground`; icon 14.4 x 14.4, #000000 `dark.color.surface.background`; layers div.absolute.overflow-hidden 192.0x192.0 rgba(255, 255, 255, 0.04) `dark.color.alpha.gray-50` 14px; div.absolute.inset-0 192.0x192.0 #171717 `dark.color.surface.muted`; button.transition-[background-color,color,box-shadow,border-color].outline-hidden 32.4x32.4 #ffffff `dark.color.focus.ring` transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px  |
| hover | icon 16 x 16, #000000 `dark.color.surface.background`; layers div.absolute.overflow-hidden 192.0x192.0 rgba(255, 255, 255, 0.04) `dark.color.alpha.gray-50` 14px; div.absolute.inset-0 192.0x192.0 #171717 `dark.color.surface.muted`; button.transition-[background-color,color,box-shadow,border-color].outline-hidden 36.0x36.0 #ffffff `dark.color.focus.ring` transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px  |

Child layers that carry the look: div 192x192 background rgba(255, 255, 255, 0.04) `dark.color.alpha.gray-50` radius 14px; div 192x192 background #171717 `dark.color.surface.muted`; button 32.4x32.4 background #ffffff `dark.color.focus.ring` radius 3.35544e+07px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 10px 15px -3px, rgba(0, 0, 0, 0.1) 0px 4px 6px -4px.

![Track card default](components/crops/track-card-default.png) ![Track card hover](components/crops/track-card-hover.png)

#### Track play button
The white 32px circular play button a card raises on hover. Read as `play-track` on the explore page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 32.4 x 32.4; radius 3.35544e+07px; background #ffffff `dark.color.focus.ring`; shadow rgba(0, 0, 0, 0.1) 0px 10px 15px -3px, rgba(0, 0, 0, 0.1) 0px 4px 6px -4px; text Inter 16/24 400, #fafafa `dark.color.ink.foreground`; transition background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), color 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 14.4 x 14.4, #000000 `dark.color.surface.background` |
| hover | size 36 x 36; icon 16 x 16, #000000 `dark.color.surface.background` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Track play button default](components/crops/play-track-default.png) ![Track play button hover](components/crops/play-track-hover.png) ![Track play button pressed](components/crops/play-track-pressed.png)

#### Version badge
The "v2.5" badge on track cards. Read as `version-badge` on the explore page.

**Values (default).** size 34.25 x 16; background transparent; text Inter 10/10 500, #868686 `dark.color.ink.muted-foreground`; layers span.inline-flex.h-4 34.3x16.0 T:1px solid rgba(255, 255, 255, 0.15) `dark.color.alpha.gray-200` / R:1px solid rgba(255, 255, 255, 0.15) `dark.color.alpha.gray-200` / B:1px solid rgba(255, 255, 255, 0.15) `dark.color.alpha.gray-200` / L:1px solid rgba(255, 255, 255, 0.15) `dark.color.alpha.gray-200` 3.35544e+07px.

Child layers that carry the look: span 34.3x16 border 1px solid rgba(255, 255, 255, 0.15) `dark.color.alpha.gray-200` radius 3.35544e+07px.

![Version badge default](components/crops/version-badge-default.png)

#### Genre card
A genre tile in Genres & Moods (artwork + name + play chip). Read as `genre-card` on the explore page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible, pressed) | size 192 x 192; radius 14px; background rgba(255, 255, 255, 0.04) `dark.color.alpha.gray-50`; text Inter 16/24 400, #fafafa `dark.color.ink.foreground`; transition transform 0.22s cubic-bezier(0.23, 1, 0.32, 1), translate 0.22s cubic-bezier(0.23, 1, 0.32, 1), scale 0.22s cubic-bezier(0.23, 1, 0.32, 1), rotate 0.22s cubic-bezier(0.23, 1, 0.32, 1); icon 14.4 x 14.4, #000000 `dark.color.surface.background` |
| hover | size 192.26 x 188.96; transform matrix3d(0.998, 0, 0, 0, 0, 0.996444, 0.0557099, -6.33067e-05, 0, -0.0558215, 0.998441, -0.00113459, 0, 0, 0, 1); icon 16.13 x 16.04, #000000 `dark.color.surface.background` |

![Genre card default](components/crops/genre-card-default.png) ![Genre card hover](components/crops/genre-card-hover.png) ![Genre card focus-visible](components/crops/genre-card-focus-visible.png) ![Genre card pressed](components/crops/genre-card-pressed.png)

#### Genre play button
The white 25px circular play button on a genre tile. Read as `play-genre` on the explore page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 25.2 x 25.2; radius 3.35544e+07px; background #ffffff `dark.color.focus.ring`; shadow rgba(0, 0, 0, 0.1) 0px 10px 15px -3px, rgba(0, 0, 0, 0.1) 0px 4px 6px -4px; text Inter 16/24 400, #fafafa `dark.color.ink.foreground`; transition background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), color 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 14.4 x 14.4, #000000 `dark.color.surface.background` |
| hover | size 28.22 x 28.07; icon 16.13 x 16.04, #000000 `dark.color.surface.background` |
| focus-visible | outline 1px solid #ffffff `dark.color.focus.ring`, offset 2px |

![Genre play button default](components/crops/play-genre-default.png) ![Genre play button hover](components/crops/play-genre-hover.png) ![Genre play button focus-visible](components/crops/play-genre-focus-visible.png) ![Genre play button pressed](components/crops/play-genre-pressed.png)

#### Artist link
An artist-name link under a track title; measured, never followed. Read as `artist-link` on the explore page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 95.34 x 18.75; background transparent; text Inter 15/18.75 500, #868686 `dark.color.ink.muted-foreground`; icon 12 x 12, #fafafa `dark.color.ink.foreground` |
| focus-visible | outline 1px auto rgba(255, 255, 255, 0.5) `dark.color.border.field-border-focus`, offset 1px; layers a.inline-flex.min-w-0 95.3x18.8 1px auto rgba(255, 255, 255, 0.5) `dark.color.border.field-border-focus` offset 1px |

![Artist link default](components/crops/artist-link-default.png) ![Artist link hover](components/crops/artist-link-hover.png) ![Artist link focus-visible](components/crops/artist-link-focus-visible.png) ![Artist link pressed](components/crops/artist-link-pressed.png)

#### Shelf heading
A shelf heading ("Featured", "Genres & Moods"). Read as `shelf-heading` on the explore page.

**Values (default).** size 85.73 x 28; background transparent; text Inter 20/28 400, #fafafa `dark.color.ink.foreground`.

![Shelf heading default](components/crops/shelf-heading-default.png)

### Player

The transport bar mounted by pressing a card's own Play: progress, prev/play/next, repeat, volume, queue and the gated Remix.

#### Player bar
The bottom transport bar mounted by pressing a card's Play (art, progress, transport, volume). Read as `player-bar` on the explore page.

**Values (default).** size 1186 x 72; radius 16px; background #000000 `dark.color.surface.background`; shadow rgba(255, 255, 255, 0.16) 0px 0px 0px 0.5px, rgba(0, 0, 0, 0.45) 0px 1px 2px 0px, rgba(0, 0, 0, 0.4) 0px 4px 8px -2px, rgba(0, 0, 0, 0.35) 0px 12px 24px -6px; text Inter 14/20 500, #fafafa `dark.color.ink.foreground`; icon 12 x 12, #fafafa `dark.color.ink.foreground`.

![Player bar default](components/crops/player-bar-default.png)

#### Player play/pause
The transport's central pause button (a playing track). Read as `player-play` on the explore page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 36 x 36; radius 3.35544e+07px; background #fafafa `dark.color.ink.foreground`; text Inter 14/20 400, #000000 `dark.color.surface.background`; transition transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #000000 `dark.color.surface.background` |
| hover | background rgba(250, 250, 250, 0.9) |
| focus-visible | outline 1px solid #ffffff `dark.color.focus.ring`, offset 2px |
| pressed | size 34.2 x 34.2; background rgba(250, 250, 250, 0.9); icon 15.2 x 15.2, #000000 `dark.color.surface.background` |

![Player play/pause default](components/crops/player-play-default.png) ![Player play/pause hover](components/crops/player-play-hover.png) ![Player play/pause focus-visible](components/crops/player-play-focus-visible.png) ![Player play/pause pressed](components/crops/player-play-pressed.png)

#### Player previous
The transport previous button (the unlabeled control before Pause). Read as `player-prev` on the explore page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 36 x 36; radius 3.35544e+07px; background transparent; text Inter 14/20 400, rgba(250, 250, 250, 0.8); transition background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), color 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, rgba(250, 250, 250, 0.8) |
| hover | background rgba(255, 255, 255, 0.08) `dark.color.border.sidebar-border`; text Inter 14/20 400, #fafafa `dark.color.ink.foreground`; icon 16 x 16, #fafafa `dark.color.ink.foreground` |
| focus-visible | outline 1px solid #ffffff `dark.color.focus.ring`, offset 2px; layers button.inline-flex.items-center 36.0x36.0 1px solid #ffffff `dark.color.focus.ring` offset 2px 3.35544e+07px |
| pressed | size 35.28 x 35.28; background rgba(255, 255, 255, 0.08) `dark.color.border.sidebar-border`; text Inter 14/20 400, #fafafa `dark.color.ink.foreground`; icon 15.68 x 15.68, #fafafa `dark.color.ink.foreground` |

![Player previous default](components/crops/player-prev-default.png) ![Player previous hover](components/crops/player-prev-hover.png) ![Player previous focus-visible](components/crops/player-prev-focus-visible.png) ![Player previous pressed](components/crops/player-prev-pressed.png)

#### Player next
The transport next button (the unlabeled control after Pause). Read as `player-next` on the explore page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 36 x 36; radius 3.35544e+07px; background transparent; text Inter 14/20 400, rgba(250, 250, 250, 0.8); transition background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), color 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, rgba(250, 250, 250, 0.8) |
| hover | background rgba(255, 255, 255, 0.08) `dark.color.border.sidebar-border`; text Inter 14/20 400, #fafafa `dark.color.ink.foreground`; icon 16 x 16, #fafafa `dark.color.ink.foreground` |
| focus-visible | outline 1px solid #ffffff `dark.color.focus.ring`, offset 2px; layers button.inline-flex.items-center 36.0x36.0 1px solid #ffffff `dark.color.focus.ring` offset 2px 3.35544e+07px |
| pressed | size 35.28 x 35.28; background rgba(255, 255, 255, 0.08) `dark.color.border.sidebar-border`; text Inter 14/20 400, #fafafa `dark.color.ink.foreground`; icon 15.68 x 15.68, #fafafa `dark.color.ink.foreground` |

![Player next default](components/crops/player-next-default.png) ![Player next hover](components/crops/player-next-hover.png) ![Player next focus-visible](components/crops/player-next-focus-visible.png) ![Player next pressed](components/crops/player-next-pressed.png)

#### Player repeat
The transport repeat toggle. Read as `player-repeat` on the explore page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 36 x 36; radius 3.35544e+07px; background transparent; text Inter 14/20 400, rgba(250, 250, 250, 0.8); transition background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), color 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 14 x 14, rgba(250, 250, 250, 0.8) |
| hover | background rgba(255, 255, 255, 0.08) `dark.color.border.sidebar-border`; text Inter 14/20 400, #fafafa `dark.color.ink.foreground`; icon 14 x 14, #fafafa `dark.color.ink.foreground` |
| focus-visible | outline 1px solid #ffffff `dark.color.focus.ring`, offset 2px; layers button.inline-flex.items-center 36.0x36.0 1px solid #ffffff `dark.color.focus.ring` offset 2px 3.35544e+07px |
| pressed | size 35.28 x 35.28; background rgba(255, 255, 255, 0.08) `dark.color.border.sidebar-border`; text Inter 14/20 400, #fafafa `dark.color.ink.foreground`; icon 13.72 x 13.72, #fafafa `dark.color.ink.foreground` |

![Player repeat default](components/crops/player-repeat-default.png) ![Player repeat hover](components/crops/player-repeat-hover.png) ![Player repeat focus-visible](components/crops/player-repeat-focus-visible.png) ![Player repeat pressed](components/crops/player-repeat-pressed.png)

#### Player progress
The seek rail across the player's top edge. Read as `player-progress` on the explore page.

**Values (default).** size 328 x 4; radius 3.35544e+07px; background rgba(250, 250, 250, 0.15); text Inter 16/24 400, #fafafa `dark.color.ink.foreground`.

![Player progress default](components/crops/player-progress-default.png)

#### Player volume
The transport volume control. Read as `player-volume` on the explore page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 36 x 36; radius 3.35544e+07px; background transparent; text Inter 14/20 400, rgba(250, 250, 250, 0.8); transition background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), color 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, rgba(250, 250, 250, 0.8) |
| hover | background rgba(255, 255, 255, 0.08) `dark.color.border.sidebar-border`; text Inter 14/20 400, #fafafa `dark.color.ink.foreground`; icon 16 x 16, #fafafa `dark.color.ink.foreground` |
| focus-visible | outline 1px solid #ffffff `dark.color.focus.ring`, offset 2px; layers button.inline-flex.items-center 36.0x36.0 1px solid #ffffff `dark.color.focus.ring` offset 2px 3.35544e+07px |
| pressed | size 35.28 x 35.28; background rgba(255, 255, 255, 0.08) `dark.color.border.sidebar-border`; text Inter 14/20 400, #fafafa `dark.color.ink.foreground`; icon 15.68 x 15.68, #fafafa `dark.color.ink.foreground` |

![Player volume default](components/crops/player-volume-default.png) ![Player volume hover](components/crops/player-volume-hover.png) ![Player volume focus-visible](components/crops/player-volume-focus-visible.png) ![Player volume pressed](components/crops/player-volume-pressed.png)

#### Player queue
The transport queue button. Read as `player-queue` on the explore page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 36 x 36; radius 3.35544e+07px; background transparent; text Inter 14/20 400, rgba(250, 250, 250, 0.8); transition background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), color 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, rgba(250, 250, 250, 0.8) |
| hover | background rgba(255, 255, 255, 0.08) `dark.color.border.sidebar-border`; text Inter 14/20 400, #fafafa `dark.color.ink.foreground`; icon 16 x 16, #fafafa `dark.color.ink.foreground` |
| focus-visible | outline 1px solid #ffffff `dark.color.focus.ring`, offset 2px; layers button.inline-flex.items-center 36.0x36.0 1px solid #ffffff `dark.color.focus.ring` offset 2px 3.35544e+07px |
| pressed | size 35.28 x 35.28; background rgba(255, 255, 255, 0.08) `dark.color.border.sidebar-border`; text Inter 14/20 400, #fafafa `dark.color.ink.foreground`; icon 15.68 x 15.68, #fafafa `dark.color.ink.foreground` |

![Player queue default](components/crops/player-queue-default.png) ![Player queue hover](components/crops/player-queue-hover.png) ![Player queue focus-visible](components/crops/player-queue-focus-visible.png) ![Player queue pressed](components/crops/player-queue-pressed.png)

#### Player remix
The transport Remix button; measured, never pressed (gated). Read as `player-remix` on the explore page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 31.36 x 31.36; radius 3.35544e+07px; background transparent; text Inter 16/24 400, rgba(255, 255, 255, 0.7) `dark.color.alpha.gray-700`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 17.64 x 17.64, rgba(255, 255, 255, 0.7) `dark.color.alpha.gray-700` |
| pressed | text Inter 16/24 400, #ffffff `dark.color.focus.ring`; icon 17.64 x 17.64, #ffffff `dark.color.focus.ring` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Player remix default](components/crops/player-remix-default.png) ![Player remix pressed](components/crops/player-remix-pressed.png)

### Charts

The ranked chart: the Play-all and Shuffle pills, Share, chart rows and the gated Like/Remix icon buttons.

#### Charts title
The charts page heading. Read as `charts-title` on the charts page.

**Values (default).** size 842 x 83; padding 0px 0px 8px 0px; background transparent; text waldenburg 60/75 300, #ffffff `dark.color.focus.ring`.

![Charts title default](components/crops/charts-title-default.png)

#### Play-all button
The white 40px Play pill at the top of the chart. Read as `chart-play` on the charts page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 79.86 x 40; padding 0px 14px; radius 3.35544e+07px; background #ffffff `dark.color.focus.ring`; text Inter 14/20 400, #000000 `dark.color.surface.background`; transition background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), color 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #000000 `dark.color.surface.background` |
| hover | background rgba(255, 255, 255, 0.9) `light.color.surface.composer` |
| focus-visible | outline 1px solid #ffffff `dark.color.focus.ring`, offset 2px |
| pressed | size 78.26 x 39.2; background rgba(255, 255, 255, 0.9) `light.color.surface.composer`; icon 15.68 x 15.68, #000000 `dark.color.surface.background` |

![Play-all button default](components/crops/chart-play-default.png) ![Play-all button hover](components/crops/chart-play-hover.png) ![Play-all button focus-visible](components/crops/chart-play-focus-visible.png) ![Play-all button pressed](components/crops/chart-play-pressed.png)

#### Shuffle button
The 40px Shuffle pill next to Play. Read as `shuffle-btn` on the charts page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 98.92 x 40; padding 0px 14px; radius 3.35544e+07px; background rgba(255, 255, 255, 0.15) `dark.color.alpha.gray-200`; text Inter 14/20 400, #ffffff `dark.color.focus.ring`; transition background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), color 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #ffffff `dark.color.focus.ring` |
| hover | background rgba(255, 255, 255, 0.25) |
| focus-visible | outline 1px solid #ffffff `dark.color.focus.ring`, offset 2px |
| pressed | size 96.94 x 39.2; background rgba(255, 255, 255, 0.25); icon 15.68 x 15.68, #ffffff `dark.color.focus.ring` |

![Shuffle button default](components/crops/shuffle-btn-default.png) ![Shuffle button hover](components/crops/shuffle-btn-hover.png) ![Shuffle button focus-visible](components/crops/shuffle-btn-focus-visible.png) ![Shuffle button pressed](components/crops/shuffle-btn-pressed.png)

#### Share button
The 32px Share pill; measured, never pressed. Read as `share-btn` on the charts page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 82.33 x 32; padding 0px 10px; radius 3.35544e+07px; background rgba(255, 255, 255, 0.15) `dark.color.alpha.gray-200`; text Inter 14/20 400, #ffffff `dark.color.focus.ring`; transition background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), color 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #ffffff `dark.color.focus.ring` |
| hover | background rgba(255, 255, 255, 0.25) |
| focus-visible | outline 1px solid #ffffff `dark.color.focus.ring`, offset 2px |
| pressed | size 80.68 x 31.36; background rgba(255, 255, 255, 0.25); icon 15.68 x 15.68, #ffffff `dark.color.focus.ring` |

![Share button default](components/crops/share-btn-default.png) ![Share button hover](components/crops/share-btn-hover.png) ![Share button focus-visible](components/crops/share-btn-focus-visible.png) ![Share button pressed](components/crops/share-btn-pressed.png)

#### Chart row
A ranked chart row (rank, art, title, artist, Like/Remix icons). Read as `chart-row` on the charts page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 810 x 40; background transparent; text Inter 14/17.5 500, #fafafa `dark.color.ink.foreground`; icon 12 x 12, #868686 `dark.color.ink.muted-foreground`; layers span.inline-flex.cursor-default 18.0x18.0 rgba(23, 23, 23, 0.6) T:1px solid rgba(255, 255, 255, 0.06) / R:1px solid rgba(255, 255, 255, 0.06) / B:1px solid rgba(255, 255, 255, 0.06) / L:1px solid rgba(255, 255, 255, 0.06) 3.35544e+07px |
| focus-visible | layers a.pointer-events-auto.min-w-0 55.7x16.3 1px auto rgba(255, 255, 255, 0.5) `dark.color.border.field-border-focus` offset 1px; span.inline-flex.cursor-default 18.0x18.0 rgba(23, 23, 23, 0.6) T:1px solid rgba(255, 255, 255, 0.06) / R:1px solid rgba(255, 255, 255, 0.06) / B:1px solid rgba(255, 255, 255, 0.06) / L:1px solid rgba(255, 255, 255, 0.06) 3.35544e+07px |

Child layers that carry the look: span 18x18 background rgba(23, 23, 23, 0.6) border 1px solid rgba(255, 255, 255, 0.06) radius 3.35544e+07px.

![Chart row default](components/crops/chart-row-default.png) ![Chart row hover](components/crops/chart-row-hover.png) ![Chart row focus-visible](components/crops/chart-row-focus-visible.png) ![Chart row pressed](components/crops/chart-row-pressed.png)

#### Like button
A row's 32px heart icon button; measured, never pressed (gated). Read as `like-btn` on the charts page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 32 x 32; radius 3.35544e+07px; background transparent; text Inter 14/20 400, #868686 `dark.color.ink.muted-foreground`; transition background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), color 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #868686 `dark.color.ink.muted-foreground` |
| hover | background rgba(255, 255, 255, 0.08) `dark.color.border.sidebar-border`; text Inter 14/20 400, #fafafa `dark.color.ink.foreground`; icon 16 x 16, #fafafa `dark.color.ink.foreground` |
| focus-visible | outline 1px solid #ffffff `dark.color.focus.ring`, offset 2px; layers button.inline-flex.shrink-0 32.0x32.0 1px solid #ffffff `dark.color.focus.ring` offset 2px 3.35544e+07px |
| pressed | size 31.36 x 31.36; background rgba(255, 255, 255, 0.08) `dark.color.border.sidebar-border`; text Inter 14/20 400, #fafafa `dark.color.ink.foreground`; icon 15.68 x 15.68, #fafafa `dark.color.ink.foreground` |

![Like button default](components/crops/like-btn-default.png) ![Like button hover](components/crops/like-btn-hover.png) ![Like button focus-visible](components/crops/like-btn-focus-visible.png) ![Like button pressed](components/crops/like-btn-pressed.png)

#### Remix button
A row's 32px Remix icon button; measured, never pressed (gated). Read as `remix-btn` on the charts page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 32 x 32; radius 3.35544e+07px; background transparent; text Inter 14/20 400, #868686 `dark.color.ink.muted-foreground`; transition background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), color 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #868686 `dark.color.ink.muted-foreground` |
| hover | background #1e1e1e `dark.color.surface.secondary`; text Inter 14/20 400, #fafafa `dark.color.ink.foreground`; icon 16 x 16, #fafafa `dark.color.ink.foreground` |
| focus-visible | outline 1px solid #ffffff `dark.color.focus.ring`, offset 2px; layers button.inline-flex.shrink-0 32.0x32.0 1px solid #ffffff `dark.color.focus.ring` offset 2px 3.35544e+07px |
| pressed | size 31.36 x 31.36; background #1e1e1e `dark.color.surface.secondary`; text Inter 14/20 400, #fafafa `dark.color.ink.foreground`; icon 15.68 x 15.68, #fafafa `dark.color.ink.foreground` |

![Remix button default](components/crops/remix-btn-default.png) ![Remix button hover](components/crops/remix-btn-hover.png) ![Remix button focus-visible](components/crops/remix-btn-focus-visible.png) ![Remix button pressed](components/crops/remix-btn-pressed.png)

#### Chart artist link
An artist link inside a chart row. Read as `chart-artist` on the charts page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 55.7 x 16.25; background transparent; text Inter 13/16.25 400, #868686 `dark.color.ink.muted-foreground` |
| hover | text Inter 13/16.25 400, #fafafa `dark.color.ink.foreground` |
| focus-visible | outline 1px auto rgba(255, 255, 255, 0.5) `dark.color.border.field-border-focus`, offset 1px; layers a.pointer-events-auto.min-w-0 55.7x16.3 1px auto rgba(255, 255, 255, 0.5) `dark.color.border.field-border-focus` offset 1px |
| pressed | text Inter 13/16.25 400, #fafafa `dark.color.ink.foreground` |

![Chart artist link default](components/crops/chart-artist-default.png) ![Chart artist link hover](components/crops/chart-artist-hover.png) ![Chart artist link focus-visible](components/crops/chart-artist-focus-visible.png) ![Chart artist link pressed](components/crops/chart-artist-pressed.png)

### Pricing

The pricing surface: Free and Pro plan cards (the Pro card an inverted white island on the dark field), the feature rows and the FAQ accordion.

#### Pricing title
The "Free to start. Pro when you're ready." heading. Read as `pricing-h1` on the pricing page.

**Values (default).** size 960 x 42; background transparent; text waldenburg 36/42 300, #fafafa `dark.color.ink.foreground`.

![Pricing title default](components/crops/pricing-h1-default.png)

#### Plan card, Free
The Free plan card (dark surface, hairline border). Read as `plan-card` on the pricing page.

**Values (default).** size 472 x 909.38; radius 24px; background #000000 `dark.color.surface.background`; text Inter 14/20 500, #fafafa `dark.color.ink.foreground`; icon 16 x 16, #fafafa `dark.color.ink.foreground`.

![Plan card, Free default](components/crops/plan-card-default.png)

#### Plan card, Pro
The Pro plan card — an inverted white island on the dark page. Read as `plan-card-pro` on the pricing page.

**Values (default).** size 472 x 909.38; radius 24px; background #fafafa `dark.color.ink.foreground`; text Inter 14/20 500, #000000 `dark.color.surface.background`; icon 16 x 16, #000000 `dark.color.surface.background`.

![Plan card, Pro default](components/crops/plan-card-pro-default.png)

#### Plan price
The $9.99/month price figure on the Pro card. Read as `plan-price` on the pricing page.

**Values (default).** size 126.69 x 52; background transparent; text waldenburg 48/52 300, #000000 `dark.color.surface.background`.

![Plan price default](components/crops/plan-price-default.png)

#### Plan feature row
A checked feature row inside a plan card. Read as `plan-feature` on the pricing page.

**Values (default).** size 408 x 47; padding 12px 0px; border B: 1px solid rgba(255, 255, 255, 0.1) `dark.color.border.border`; background transparent; text Inter 15/22 400, #fafafa `dark.color.ink.foreground`; icon 16 x 16, #fafafa `dark.color.ink.foreground`; layers li.flex.items-center 408.0x47.0 B:1px solid rgba(255, 255, 255, 0.1) `dark.color.border.border`.

Child layers that carry the look: li 408x47 border 1px solid rgba(255, 255, 255, 0.1) `dark.color.border.border`.

![Plan feature row default](components/crops/plan-feature-default.png)

#### Plan CTA, Free
The Start-free pill on the Free card (white fill on dark); measured, never followed. Read as `plan-cta-free` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 110.91 x 44; padding 0px 20px; radius 3.35544e+07px; background #fafafa `dark.color.ink.foreground`; text Inter 16/24 400, #000000 `dark.color.surface.background`; transition transform 0.3s cubic-bezier(0, 0, 0.2, 1), background-color 0.3s cubic-bezier(0, 0, 0.2, 1) |
| hover | opacity 0.85 |
| focus-visible | outline 2px solid #fafafa `dark.color.ink.foreground`, offset 4px |
| pressed | size 108.69 x 43.12; opacity 0.85 |

![Plan CTA, Free default](components/crops/plan-cta-free-default.png) ![Plan CTA, Free hover](components/crops/plan-cta-free-hover.png) ![Plan CTA, Free focus-visible](components/crops/plan-cta-free-focus-visible.png) ![Plan CTA, Free pressed](components/crops/plan-cta-free-pressed.png)

#### Plan CTA, Pro
The Get-Pro pill on the Pro card (dark fill on the white island); measured, never followed. Read as `plan-cta-pro` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 96.58 x 44; padding 0px 20px; radius 3.35544e+07px; background #1e1e1e `dark.color.surface.secondary`; shadow rgba(255, 255, 255, 0.07) 0px 0px 0px 1px, rgba(0, 0, 0, 0.5) 0px 1px 2px 0px; text Inter 16/24 400, #fafafa `dark.color.ink.foreground`; transition transform 0.3s cubic-bezier(0, 0, 0.2, 1), background-color 0.3s cubic-bezier(0, 0, 0.2, 1) |
| focus-visible | outline 2px solid #fafafa `dark.color.ink.foreground`, offset 4px |
| pressed | size 94.65 x 43.12 |

![Plan CTA, Pro default](components/crops/plan-cta-pro-default.png) ![Plan CTA, Pro hover](components/crops/plan-cta-pro-hover.png) ![Plan CTA, Pro focus-visible](components/crops/plan-cta-pro-focus-visible.png) ![Plan CTA, Pro pressed](components/crops/plan-cta-pro-pressed.png)

#### FAQ accordion
A pricing FAQ row (68px, border-t); the expanded state was opened by its own toggle. Read as `faq-item` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 960 x 68; padding 20px 0px; radius 4px; background transparent; text Inter 18/28 400, #fafafa `dark.color.ink.foreground`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 5.3 x 5.3, #868686 `dark.color.ink.muted-foreground` |
| hover | icon 5.3 x 5.3, #fafafa `dark.color.ink.foreground` |
| focus-visible | outline 1px solid #ffffff `dark.color.focus.ring`, offset 2px; layers button.flex.flex-1 960.0x68.0 1px solid #ffffff `dark.color.focus.ring` offset 2px 4px |
| pressed, expanded | icon 5.3 x 5.3, #fafafa `dark.color.ink.foreground` |

![FAQ accordion default](components/crops/faq-item-default.png) ![FAQ accordion hover](components/crops/faq-item-hover.png) ![FAQ accordion focus-visible](components/crops/faq-item-focus-visible.png) ![FAQ accordion pressed](components/crops/faq-item-pressed.png) ![FAQ accordion expanded](components/crops/faq-item-expanded.png)

#### FAQ row
The accordion item wrapper (question + answer region). Read as `faq-answer` on the pricing page.

**Read in the wrong state.** faq-item's `expanded` reading opened this row and left it open, so this default reading (152px tall, against the 68px closed row) is of the open item. tools/capture/public/measure.mjs now closes it after the reading. The entry needs a recapture.

**Values (default).** size 960 x 152; background transparent; text Inter 18/28 400, #fafafa `dark.color.ink.foreground`; icon 5.3 x 5.3, #868686 `dark.color.ink.muted-foreground`.

![FAQ row default](components/crops/faq-answer-default.png)

### Log in and sign up

The auth boundary card, measured but never submitted: the SSO buttons, the expanded email form, the terms checkbox and the disabled Continue.

#### Auth column
The centred 384px log-in/sign-up column on the bare page; nothing submitted. Read as `auth-card` on the log in page.

**Values (default).** size 384 x 844; background transparent; text waldenburg 30/36 300, #fafafa `dark.color.ink.foreground`; icon 24.08 x 28, #fafafa `dark.color.ink.foreground`; layers button.inline-flex.shrink-0 384.0x40.0 #222222 `dark.color.surface.elevated` transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(255, 255, 255, 0.07) 0px 0px 0px 1px, rgba(0, 0, 0, 0.5) 0px 1px 2px 0px 3.35544e+07px; button.inline-flex.shrink-0 384.0x40.0 #222222 `dark.color.surface.elevated` transparent 0px 0px 0px 0px, transpar.

Child layers that carry the look: button 384x40 background #222222 `dark.color.surface.elevated` radius 3.35544e+07px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(255, 255, 255, 0.07) 0px 0px 0px 1px, rgba(0, 0, 0, 0.5) 0px 1px 2px 0px; button 384x40 background #222222 `dark.color.surface.elevated` radius 3.35544e+07px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(255, 255, 255, 0.07) 0px 0px 0px 1px, rgba(0, 0, 0, 0.5) 0px 1px 2px 0px; div 173.2x1 border 1px dashed rgba(255, 255, 255, 0.1) `dark.color.border.border`.

![Auth column default](components/crops/auth-card-default.png)

#### Auth title
The "Log in or sign up" heading. Read as `auth-title` on the log in page.

**Values (default).** size 384 x 36; background transparent; text waldenburg 30/36 300, #fafafa `dark.color.ink.foreground`.

![Auth title default](components/crops/auth-title-default.png)

#### Google SSO button
The Continue-with-Google button (surface-1 fill, 40px); measured, never pressed. Read as `sso-google` on the log in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 384 x 40; padding 0px 16px; radius 3.35544e+07px; background #222222 `dark.color.surface.elevated`; shadow rgba(255, 255, 255, 0.07) 0px 0px 0px 1px, rgba(0, 0, 0, 0.5) 0px 1px 2px 0px; text Inter 14/20 400, #fafafa `dark.color.ink.foreground`; transition background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), color 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #fafafa `dark.color.ink.foreground` |
| hover | background #2b2b2b `dark.color.surface.elevated-hover` |
| focus-visible | outline 1px solid #ffffff `dark.color.focus.ring`, offset 2px |
| pressed | size 376.32 x 39.2; background #2b2b2b `dark.color.surface.elevated-hover`; icon 15.68 x 15.68, #fafafa `dark.color.ink.foreground` |

![Google SSO button default](components/crops/sso-google-default.png) ![Google SSO button hover](components/crops/sso-google-hover.png) ![Google SSO button focus-visible](components/crops/sso-google-focus-visible.png) ![Google SSO button pressed](components/crops/sso-google-pressed.png)

#### Apple SSO button
The Continue-with-Apple button; measured, never pressed. Read as `sso-apple` on the log in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 384 x 40; padding 0px 16px; radius 3.35544e+07px; background #222222 `dark.color.surface.elevated`; shadow rgba(255, 255, 255, 0.07) 0px 0px 0px 1px, rgba(0, 0, 0, 0.5) 0px 1px 2px 0px; text Inter 14/20 400, #fafafa `dark.color.ink.foreground`; transition background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), color 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #fafafa `dark.color.ink.foreground` |
| hover | background #2b2b2b `dark.color.surface.elevated-hover` |
| focus-visible | outline 1px solid #ffffff `dark.color.focus.ring`, offset 2px |
| pressed | size 376.32 x 39.2; background #2b2b2b `dark.color.surface.elevated-hover`; icon 15.68 x 15.68, #fafafa `dark.color.ink.foreground` |

![Apple SSO button default](components/crops/sso-apple-default.png) ![Apple SSO button hover](components/crops/sso-apple-hover.png) ![Apple SSO button focus-visible](components/crops/sso-apple-focus-visible.png) ![Apple SSO button pressed](components/crops/sso-apple-pressed.png)

#### Other-options toggle
The Show-other-options button that expands the email form in place; toggled for the expanded state, never submitted. Read as `options-btn` on the log in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 384 x 36; padding 0px 14px; radius 3.35544e+07px; background #1e1e1e `dark.color.surface.secondary`; text Inter 14/20 400, #fafafa `dark.color.ink.foreground`; transition background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), color 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #2b2b2b `dark.color.surface.elevated-hover` |
| focus-visible | outline 1px solid #ffffff `dark.color.focus.ring`, offset 2px |
| pressed | size 376.32 x 35.28; background #2b2b2b `dark.color.surface.elevated-hover` |

![Other-options toggle default](components/crops/options-btn-default.png) ![Other-options toggle hover](components/crops/options-btn-hover.png) ![Other-options toggle focus-visible](components/crops/options-btn-focus-visible.png) ![Other-options toggle pressed](components/crops/options-btn-pressed.png)

#### Email field
The Enter-email-address input revealed by the options toggle; sample text was typed and deleted, nothing sent. Read as `email-field` on the log in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 376 x 36; padding 4px 14px; border 1px solid rgba(255, 255, 255, 0.12) `dark.color.border.input`; radius 12px; background rgba(255, 255, 255, 0.04) `dark.color.alpha.gray-50`; text Inter 14/20 400, #fafafa `dark.color.ink.foreground`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1); placeholder #868686 `dark.color.ink.muted-foreground` |
| focused, filled | border 1px solid rgba(255, 255, 255, 0.5) `dark.color.border.field-border-focus` |

![Email field default](components/crops/email-field-default.png) ![Email field focused](components/crops/email-field-focused.png) ![Email field filled](components/crops/email-field-filled.png)

#### Terms checkbox
The agree-to-Terms checkbox; measured, never checked. Read as `tos-checkbox` on the log in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 16 x 16; border 1px solid rgba(255, 255, 255, 0.2) `dark.color.border.outline`; radius 4px; background transparent; text Inter 14/20 400, #fafafa `dark.color.ink.foreground`; transition box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| focus-visible | outline 1px solid #ffffff `dark.color.focus.ring`, offset 2px |

![Terms checkbox default](components/crops/tos-checkbox-default.png) ![Terms checkbox hover](components/crops/tos-checkbox-hover.png) ![Terms checkbox focus-visible](components/crops/tos-checkbox-focus-visible.png) ![Terms checkbox pressed](components/crops/tos-checkbox-pressed.png)

#### Continue button
The Continue-with-Email submit (disabled until the box is checked); measured, never pressed. Read as `continue-btn` on the log in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 376 x 36; padding 0px 14px; radius 3.35544e+07px; background #fafafa `dark.color.ink.foreground`; text Inter 14/20 400, #0a0a0a `dark.color.ink.primary-foreground`; transition background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), color 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1); opacity 0.4 |
| pressed | size 368.48 x 35.28; background #faf8f7 `dark.color.action.primary-hover` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Continue button default](components/crops/continue-btn-default.png) ![Continue button hover](components/crops/continue-btn-hover.png) ![Continue button pressed](components/crops/continue-btn-pressed.png)

#### Terms link
An underlined legal link; measured, never followed. Read as `tos-link` on the log in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 96.66 x 15; background transparent; text Inter 12/19.5 400, #868686 `dark.color.ink.muted-foreground`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | text Inter 12/19.5 400, #fafafa `dark.color.ink.foreground` |
| focus-visible | outline 1px auto rgba(255, 255, 255, 0.5) `dark.color.border.field-border-focus`, offset 1px; layers a.underline.transition-colors 96.7x15.0 1px auto rgba(255, 255, 255, 0.5) `dark.color.border.field-border-focus` offset 1px |
| pressed | text Inter 12/19.5 400, #fafafa `dark.color.ink.foreground` |

![Terms link default](components/crops/tos-link-default.png) ![Terms link hover](components/crops/tos-link-hover.png) ![Terms link focus-visible](components/crops/tos-link-focus-visible.png) ![Terms link pressed](components/crops/tos-link-pressed.png)

#### Try-it link
The muted Try-it-first link under the form. Read as `tryit-link` on the log in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 63.27 x 20; background transparent; text Inter 14/20 400, #868686 `dark.color.ink.muted-foreground`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | text Inter 14/20 400, #fafafa `dark.color.ink.foreground` |
| focus-visible | outline 1px auto rgba(255, 255, 255, 0.5) `dark.color.border.field-border-focus`, offset 1px; layers a.text-muted-foreground.underline-offset-4 63.3x20.0 1px auto rgba(255, 255, 255, 0.5) `dark.color.border.field-border-focus` offset 1px |
| pressed | text Inter 14/20 400, #fafafa `dark.color.ink.foreground` |

![Try-it link default](components/crops/tryit-link-default.png) ![Try-it link hover](components/crops/tryit-link-hover.png) ![Try-it link focus-visible](components/crops/tryit-link-focus-visible.png) ![Try-it link pressed](components/crops/tryit-link-pressed.png)

### Footer

The site footer inside the shell: language selector, link columns, legal, Cookie settings and the System/Light/Dark theme control.

#### Footer
The site footer inside the shell: language selector, link columns, legal and the theme control. Read as `footer` on the home page.

**Values (default).** size 1186 x 708; background transparent; text Inter 14/20 500, #fafafa `dark.color.ink.foreground`; icon 24.08 x 28, #fafafa `dark.color.ink.foreground`; layers div.flex.items-center 76.0x28.0 rgba(250, 250, 250, 0.05) transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(250, 250, 250, 0.06) 0px 0px 0px 1px, transparent 0px 0px 0px 0px 3.35544e+07px; span.absolute.inset-0 24.0x24.0 rgba(250, 250, 250, 0.08) transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(250, 250, 250, 0.08.

Child layers that carry the look: div 76x28 background rgba(250, 250, 250, 0.05) radius 3.35544e+07px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(250, 250, 250, 0.06) 0px 0px 0px 1px, transparent 0px 0px 0px 0px; span 24x24 background rgba(250, 250, 250, 0.08) radius 3.35544e+07px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(250, 250, 250, 0.08) 0px 0px 0px 1px, rgba(0, 0, 0, 0.1) 0px 1px 3px 0px, rgba(0, 0, 0, 0.1) 0px 1px 2px -1px.

![Footer default](components/crops/footer-default.png)

#### Footer link
A footer column link (36px row). Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 106.14 x 36; padding 8px 6px; radius 6px; background transparent; text Inter 14/20 500, #fafafa `dark.color.ink.foreground`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | text Inter 14/20 500, #868686 `dark.color.ink.muted-foreground` |
| focus-visible | outline 1px solid #ffffff `dark.color.focus.ring`, offset 2px; layers a.focus-visible:focus-ring.-mx-1.5 106.1x36.0 1px solid #ffffff `dark.color.focus.ring` offset 2px 6px |
| pressed | text Inter 14/20 500, #868686 `dark.color.ink.muted-foreground` |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Language selector
The English locale button; measured, never opened. Read as `lang-btn` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 103.17 x 28; padding 0px 6px; radius 6px; background transparent; text Inter 14/20 500, #fafafa `dark.color.ink.foreground`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #fafafa `dark.color.ink.foreground` |
| focus-visible | outline 1px solid #ffffff `dark.color.focus.ring`, offset 2px; layers button.group.focus-visible:focus-ring 103.2x28.0 1px solid #ffffff `dark.color.focus.ring` offset 2px 6px |

![Language selector default](components/crops/lang-btn-default.png) ![Language selector hover](components/crops/lang-btn-hover.png) ![Language selector focus-visible](components/crops/lang-btn-focus-visible.png) ![Language selector pressed](components/crops/lang-btn-pressed.png)

#### Cookie settings
The Cookie-settings button (opens Cookiebot; measured, never pressed). Read as `cookie-btn` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 114.5 x 36; padding 8px 6px; radius 6px; background transparent; text Inter 14/20 500, #fafafa `dark.color.ink.foreground`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | text Inter 14/20 500, #868686 `dark.color.ink.muted-foreground` |
| focus-visible | outline 1px solid #ffffff `dark.color.focus.ring`, offset 2px; layers button.items-center.outline-hidden 114.5x36.0 1px solid #ffffff `dark.color.focus.ring` offset 2px 6px |
| pressed | text Inter 14/20 500, #868686 `dark.color.ink.muted-foreground` |

![Cookie settings default](components/crops/cookie-btn-default.png) ![Cookie settings hover](components/crops/cookie-btn-hover.png) ![Cookie settings focus-visible](components/crops/cookie-btn-focus-visible.png) ![Cookie settings pressed](components/crops/cookie-btn-pressed.png)

#### Theme control
The System/Light/Dark segmented control in the footer. Read as `theme-seg` on the home page.

**Values (default).** size 76 x 28; padding 2px; radius 3.35544e+07px; background rgba(250, 250, 250, 0.05); shadow rgba(250, 250, 250, 0.06) 0px 0px 0px 1px; text Inter 16/24 400, #fafafa `dark.color.ink.foreground`; icon 14 x 14, #868686 `dark.color.ink.muted-foreground`.

![Theme control default](components/crops/theme-seg-default.png)

#### Theme dark button
The Dark segment of the theme control (selected when the page paints dark). Read as `theme-dark-btn` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 24 x 24; radius 3.35544e+07px; background transparent; text Inter 16/24 400, #fafafa `dark.color.ink.foreground`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 14 x 14, #fafafa `dark.color.ink.foreground`; layers span.absolute.inset-0 24.0x24.0 rgba(250, 250, 250, 0.08) transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(250, 250, 250, 0.08) 0px 0px 0px 1px, rgba(0, 0, 0, 0.1) 0px 1px 3px 0px, rgba(0, 0, 0, 0.1) 0px 1px 2px -1px 3.35544e+07px |
| focus-visible | outline 1px solid #ffffff `dark.color.focus.ring`, offset 2px; layers button.focus-visible:focus-ring.motion-reduce:active:scale-100 24.0x24.0 1px solid #ffffff `dark.color.focus.ring` offset 2px 3.35544e+07px; span.absolute.inset-0 24.0x24.0 rgba(250, 250, 250, 0.08) transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(250, 250, 250, 0.08) 0px 0px 0px 1px, rgba(0, 0, 0, 0.1) 0px 1px 3px 0px, rgba(0, 0, 0, 0.1) 0px 1px 2px -1px |

Child layers that carry the look: span 24x24 background rgba(250, 250, 250, 0.08) radius 3.35544e+07px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(250, 250, 250, 0.08) 0px 0px 0px 1px, rgba(0, 0, 0, 0.1) 0px 1px 3px 0px, rgba(0, 0, 0, 0.1) 0px 1px 2px -1px.

![Theme dark button default](components/crops/theme-dark-btn-default.png) ![Theme dark button hover](components/crops/theme-dark-btn-hover.png) ![Theme dark button focus-visible](components/crops/theme-dark-btn-focus-visible.png) ![Theme dark button pressed](components/crops/theme-dark-btn-pressed.png)

#### Theme light button
The Light segment of the theme control; measured, never pressed here (the light pass toggles it). Read as `theme-light-btn` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 24 x 24; radius 3.35544e+07px; background transparent; text Inter 16/24 400, #868686 `dark.color.ink.muted-foreground`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 14 x 14, #868686 `dark.color.ink.muted-foreground` |
| hover | text Inter 16/24 400, #fafafa `dark.color.ink.foreground`; icon 14 x 14, #fafafa `dark.color.ink.foreground` |
| focus-visible | outline 1px solid #ffffff `dark.color.focus.ring`, offset 2px; layers button.focus-visible:focus-ring.motion-reduce:active:scale-100 24.0x24.0 1px solid #ffffff `dark.color.focus.ring` offset 2px 3.35544e+07px |
| pressed | text Inter 16/24 400, #fafafa `dark.color.ink.foreground`; icon 14 x 14, #fafafa `dark.color.ink.foreground` |

![Theme light button default](components/crops/theme-light-btn-default.png) ![Theme light button hover](components/crops/theme-light-btn-hover.png) ![Theme light button focus-visible](components/crops/theme-light-btn-focus-visible.png) ![Theme light button pressed](components/crops/theme-light-btn-pressed.png)

### Mobile (390 wide)

The app at phone width: the compact header, the bottom Explore/Create/Library tab bar, and the fullscreen menu sheet.

#### Mobile header
The compact header at 390: mark, Search, Start free, menu. Read as `m-header` on the home page at 390 wide.

**Values (default).** size 390 x 52; padding 0px 10px; background rgba(0, 0, 0, 0.95); text Inter 14/20 400, #0a0a0a `dark.color.ink.primary-foreground`.

![Mobile header default](components/crops/m-header-default.png)

#### Mobile logo
The mark at 390. Read as `m-logo` on the home page at 390 wide.

**Values (default).** size 29.2 x 32; padding 0px 6px; radius 10px; background transparent; text Inter 16/24 400, #fafafa `dark.color.ink.foreground`; icon 17.2 x 20, #fafafa `dark.color.ink.foreground`.

![Mobile logo default](components/crops/m-logo-default.png)

#### Mobile search button
The header search icon at 390. Read as `m-search-btn` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 32 x 32; radius 3.35544e+07px; background #151515 `dark.color.surface.composer-surface`; text Inter 16/24 400, #fafafa `dark.color.ink.foreground`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 18.39 x 18.39, #fafafa `dark.color.ink.foreground`; layers ::after transparent 0px none 1 |
| focus-visible | outline 1px solid #ffffff `dark.color.focus.ring`, offset 2px |

![Mobile search button default](components/crops/m-search-btn-default.png) ![Mobile search button hover](components/crops/m-search-btn-hover.png) ![Mobile search button focus-visible](components/crops/m-search-btn-focus-visible.png) ![Mobile search button pressed](components/crops/m-search-btn-pressed.png)

#### Mobile CTA
The Start-free pill at 390. Read as `m-cta` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 85.66 x 32; padding 0px 12px; radius 3.35544e+07px; background #fafafa `dark.color.ink.foreground`; text Inter 14/20 400, #0a0a0a `dark.color.ink.primary-foreground`; transition background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), color 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1); layers ::after transparent 0px none 1 |
| focus-visible | outline 1px solid #ffffff `dark.color.focus.ring`, offset 2px |
| pressed | size 83.94 x 31.36 |

![Mobile CTA default](components/crops/m-cta-default.png) ![Mobile CTA hover](components/crops/m-cta-hover.png) ![Mobile CTA focus-visible](components/crops/m-cta-focus-visible.png) ![Mobile CTA pressed](components/crops/m-cta-pressed.png)

#### Mobile headline
The "Make music yours." headline at 390. Read as `m-hero` on the home page at 390 wide.

**Values (default).** size 349.08 x 35.52; background transparent; text waldenburg 32.29/35.52 300, #fafafa `dark.color.ink.foreground`.

![Mobile headline default](components/crops/m-hero-default.png)

#### Mobile composer
The prompt field at 390. Read as `m-composer` on the home page at 390 wide.

**Values (default).** size 258 x 36; padding 0px 8px 0px 6px; background transparent; text Inter 15/22.5 400, #fafafa `dark.color.ink.foreground`; placeholder #fafafa `dark.color.ink.foreground`.

![Mobile composer default](components/crops/m-composer-default.png)

#### Mobile prompt chip
A suggestion chip at 390. Read as `m-chip` on the home page at 390 wide.

**Values (default).** size 82.53 x 40; padding 0px 14px; radius 3.35544e+07px; background rgba(255, 255, 255, 0.08) `dark.color.border.sidebar-border`; text Inter 12/16 400, #868686 `dark.color.ink.muted-foreground`; transition background-color 0.15s cubic-bezier(0, 0, 0.2, 1), color 0.15s cubic-bezier(0, 0, 0.2, 1), transform 0.15s cubic-bezier(0, 0, 0.2, 1).

![Mobile prompt chip default](components/crops/m-chip-default.png)

#### Mobile tab bar
The bottom tab bar pinned to the viewport (Explore / Create / Library). Read as `m-tab-bar` on the home page at 390 wide.

**Values (default).** size 390 x 56; border T: 1px solid rgba(255, 255, 255, 0.1) `dark.color.border.border`; background #000000 `dark.color.surface.background`; text Inter 11/11 600, #fafafa `dark.color.ink.foreground`; icon 22 x 22, #fafafa `dark.color.ink.foreground`.

![Mobile tab bar default](components/crops/m-tab-bar-default.png)

#### Mobile tab
A tab-bar item (the selected Explore tab). Read as `m-tab` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 132.5 x 55; background transparent; text Inter 11/11 600, #fafafa `dark.color.ink.foreground`; transition transform 0.1s cubic-bezier(0.4, 0, 0.2, 1), translate 0.1s cubic-bezier(0.4, 0, 0.2, 1), scale 0.1s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.1s cubic-bezier(0.4, 0, 0.2, 1); icon 22 x 22, #fafafa `dark.color.ink.foreground` |
| focus-visible | outline 1px auto rgba(255, 255, 255, 0.5) `dark.color.border.field-border-focus`, offset 1px; layers a.flex.h-full 132.5x55.0 1px auto rgba(255, 255, 255, 0.5) `dark.color.border.field-border-focus` offset 1px |
| pressed | size 124.55 x 51.7; icon 20.68 x 20.68, #fafafa `dark.color.ink.foreground` |

![Mobile tab default](components/crops/m-tab-default.png) ![Mobile tab hover](components/crops/m-tab-hover.png) ![Mobile tab focus-visible](components/crops/m-tab-focus-visible.png) ![Mobile tab pressed](components/crops/m-tab-pressed.png)

#### Mobile menu button
The header hamburger. Read as `m-menu-btn` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 36 x 36; padding 6px; radius 3.35544e+07px; background transparent; text Inter 16/24 400, #fafafa `dark.color.ink.foreground`; transition background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), color 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1); layers ::after transparent 0px none 1; span.absolute.left-0 18.0x1.5 #fafafa `dark.color.ink.foreground` 3.35544e+07px; span.absolute.left-0 18.0x1.5 #fafafa `dark.color.ink.foreground` 3.35544e+07px |
| focus-visible | shadow #ffffff 0px 0px 0px 2px; outline 1px solid #ffffff `dark.color.focus.ring`, offset 2px; layers ::after transparent 0px none 1; button.inline-flex.items-center 36.0x36.0 transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, #ffffff `dark.color.focus.ring` 0px 0px 0px 2px, transparent 0px 0px 0px 0px 1px solid #ffffff `dark.color.focus.ring` offset 2px 3.35544e+07px; span.absolute.left-0 18.0x1.5 #fafafa `dark.color.ink.foreground` 3.35544e+07px; span.absolute |

Child layers that carry the look: span 18x1.5 background #fafafa `dark.color.ink.foreground` radius 3.35544e+07px; span 18x1.5 background #fafafa `dark.color.ink.foreground` radius 3.35544e+07px.

![Mobile menu button default](components/crops/m-menu-btn-default.png) ![Mobile menu button hover](components/crops/m-menu-btn-hover.png) ![Mobile menu button focus-visible](components/crops/m-menu-btn-focus-visible.png) ![Mobile menu button pressed](components/crops/m-menu-btn-pressed.png)

#### Mobile menu, open
The fullscreen nav sheet the hamburger opens (measured, then dismissed). Read as `m-menu-sheet` on the home page at 390 wide.

**Values (default).** size 390 x 844; background transparent; text Inter 14/20 400, #0a0a0a `dark.color.ink.primary-foreground`; icon 17.2 x 20, #fafafa `dark.color.ink.foreground`; layers div.flex.h-[3.25rem] 390.0x52.0 #000000 `dark.color.surface.background`; button.inline-flex.shrink-0 0.0x0.0 #222222 `dark.color.surface.elevated` transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(255, 255, 255, 0.07) 0px 0px 0px 1px, rgba(0, 0, 0, 0.5) 0px 1px 2px 0px 3.35544e+07px; button.inline-flex.shrink-0 85.7x32.0 #fafaf.

Child layers that carry the look: div 390x52 background #000000 `dark.color.surface.background`; button 0x0 background #222222 `dark.color.surface.elevated` radius 3.35544e+07px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(255, 255, 255, 0.07) 0px 0px 0px 1px, rgba(0, 0, 0, 0.5) 0px 1px 2px 0px; button 85.7x32 background #fafafa `dark.color.ink.foreground` radius 3.35544e+07px.

![Mobile menu, open default](components/crops/m-menu-sheet-default.png)

#### Mobile menu link
A link inside the open nav sheet. Read as `m-menu-link` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 366 x 44; padding 12px 12px 12px 16px; radius 12px; background transparent; text Inter 12/20 500, #fafafa `dark.color.ink.foreground`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 20 x 20, #868686 `dark.color.ink.muted-foreground` |
| focus-visible, pressed | shadow #ffffff 0px 0px 0px 2px; outline 1px solid #ffffff `dark.color.focus.ring`, offset 2px; layers button.focus-visible:focus-ring.motion-reduce:active:scale-100 366.0x44.0 transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, #ffffff `dark.color.focus.ring` 0px 0px 0px 2px, transparent 0px 0px 0px 0px 1px solid #ffffff `dark.color.focus.ring` offset 2px 12px |

![Mobile menu link default](components/crops/m-menu-link-default.png) ![Mobile menu link hover](components/crops/m-menu-link-hover.png) ![Mobile menu link focus-visible](components/crops/m-menu-link-focus-visible.png) ![Mobile menu link pressed](components/crops/m-menu-link-pressed.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the ElevenMusic mark, the Google and Apple SSO glyphs, the Lucide-style control glyphs, album and artist artwork) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

ElevenMusic's product — Create, Composer, Library, Chat, Tools' generation surfaces, publishing ("Publish your music"), Likes, Remixes, Shares, playlist saving and account settings — lives behind sign-in and was never reached. Search itself opens the log-in dialog, captured as evidence of the wall. Nothing was created, liked, remixed, shared, published or submitted, and no OAuth button was ever pressed.

### Pages

- **The workspace.** Every post-login surface (Create, Composer, Chat, Library, artist-page publishing, settings, billing) needs an account and was never reached; /login and /sign-in were captured as forms and never submitted.
- **Generation.** Every Create button, prompt submit and Attach control was measured, never pressed — sending a prompt would consume the product's generation quota and produce user content.
- **Like, Remix, Share.** Measured on the charts and explore surfaces, never pressed — each is gated behind an account.
- **Purchase.** The Get-Pro and Start-free CTAs were measured, never followed past the public card.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Hover on player-prev and player-next** could not be held (the forced hover reported the element outside the viewport); the failure is recorded in the JSON, not promoted to a reading.
- **Error, loading and empty states** were not seen on the public surface.
- **Focus-visible** was a real keyboard focus on every control that would take it; a small number of controls show no measured change and are named in the Focus paragraph above.

### Themes

elevenmusic.io paints **dark by default** (`html.dark`, `color-scheme: dark`) and declares a real light theme: the footer's System/Light/Dark segmented control re-binds the same semantic roles to a warm-paper field (#fdfcfb) and persists by cookie. Both passes are resolved in tokens.json (the `--lighten-*` white-alpha ramp resolves in the dark pass only).

### Fonts

- **Inter** (variable 100-900) is the UI face; **waldenburg** (light and regular) is the display face on headlines; **GeistMono** is declared for code and IDs. All are served from the site's own Next.js media; the style guide falls back to system sans.

### Screenshots

- Album art, artist photography, playlist covers, the auth dialog's marketing panel and the ElevenMusic mark in the screenshots are the product's published content.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.
- `/charts` and `/` mobile scroll beyond one GPU texture; their full shots are tiled `*.part0/.part1` PNGs — an inner-scroller boundary, not missing content.

### Content left out

- Track titles, artist names, prompt copy, blog posts and plan copy are the product's content; only frames and components were measured.
