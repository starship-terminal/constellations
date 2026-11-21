# Krea components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from www.krea.ai on 2026-11-17, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. The public app paints html.dark. Nothing was signed into or purchased. Sign in, Log in, Sign up, Continue with Google/Apple/SSO, Book a call and Generate were measured, never followed. Continue with Email was submitted once on 2026-11-18 and stopped on captcha_failed. Consent overlays were hidden, never answered.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (42 components, 90 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (89 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-dark-state.png`: the painted theme is dark (html.dark), including marketing pages that share the app token layer. Desktop shots are 1440 x 900 at 1x. Mobile shots are 390 x 844 at 1x, because the page forces devicePixelRatio to 1 and a 2x capture failed the dimension check.

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-dark-default.png), [full](screenshots/home-dark-full.png), [mcp-menu](screenshots/home-dark-mcp-menu.png), [search](screenshots/home-dark-search.png), [sidebar-folded](screenshots/home-dark-sidebar-folded.png) |
| Pricing | `/pricing` | [default](screenshots/pricing-dark-default.png), [full](screenshots/pricing-dark-full.png) |
| Enterprise | `/enterprise` | [default](screenshots/enterprise-dark-default.png), [full](screenshots/enterprise-dark-full.png) |
| Blog | `/blog` | [default](screenshots/blog-dark-default.png), [full](screenshots/blog-dark-full.png) |
| Plugins | `/plugins` | [default](screenshots/plugins-dark-default.png), [full](screenshots/plugins-dark-full.png) |
| MCP | `/mcp` | [default](screenshots/mcp-dark-default.png), [full](screenshots/mcp-dark-full.png) |
| Image generator feature | `/features/ai-image-generator` | [default](screenshots/features-dark-default.png), [full](screenshots/features-dark-full.png) |
| Login boundary | `/login` | [default](screenshots/login-dark-default.png) |
| Image tool | `/image` | [default](screenshots/image-dark-default.png) |
| Docs | `/docs` | [default](screenshots/docs-dark-default.png), [full](screenshots/docs-dark-full.png) |
| Not found | `/about` | [default](screenshots/notfound-dark-default.png) |
| Terms | `/terms` | [default](screenshots/terms-dark-default.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-dark-default.png), [full](screenshots/mobile-home-dark-full.png), [nav](screenshots/mobile-home-dark-nav.png) |
| Pricing, phone | `/pricing` | [default](screenshots/mobile-pricing-dark-default.png), [full](screenshots/mobile-pricing-dark-full.png) |
| Login, phone | `/login` | [default](screenshots/mobile-login-dark-default.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| MCP menu | the app sidebar | the MCP button clicked locally | [home-dark-mcp-menu](screenshots/home-dark-mcp-menu.png) |
| Sidebar folded | the app shell | Toggle Sidebar clicked locally | [home-dark-sidebar-folded](screenshots/home-dark-sidebar-folded.png) |
| Phone nav | home at 390 | the menu control clicked locally | [mobile-home-dark-nav](screenshots/mobile-home-dark-nav.png) |
| Offer strip | home | measured, Claim offer never followed | [promo-banner](#promo-banner) |
| Consent overlay | pages that show one | hidden for clean captures, never answered | boundary; see Gaps |
| Sign in / login | sidebar and /login | measured, never followed | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 13 components were given a real keyboard focus. 3 draw an outline ring: `ent-cta` (1px auto #007aff, offset 1px), `plug-link` (1px auto #007aff, offset 1px), `login-google` (1px auto #101010 `core.color.primary.950`, offset 0px). 8 draw a focus ring as a shadow instead: `sidebar-toggle`, `nav-signin`, `tools-button`, `search-button`, `mkt-login`, `mkt-signup`, `price-cta`, `m-menu`. The other 2 show no measured change: `nav-home`, `nav-pricing`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.1s | `cubic-bezier(0.4, 0, 0.2, 1)` | colors, opacity, saturate | login-email-btn |
| 0.15s | `cubic-bezier(0, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, background-color, border-color, color, fill, outline-color, scale, stroke, text-decoration-color | announce-card, login-sso |
| 0.15s | `cubic-bezier(0.2, 0, 0, 1)` | margin, opacity, transform | nav-pricing, tools-button |
| 0.15s | `cubic-bezier(0.4, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, -webkit-backdrop-filter, all, backdrop-filter, background-color, border-color, box-shadow, color, fill, filter, height, opacity, outline-color, padding, rotate, scale, stroke, text-decoration-color, transform, translate, width | login-email, m-menu, mkt-login, mkt-signup, nav-home, price-badge, price-cta, promo-banner and more |
| 0.15s | `ease-out` | transform | search-button |
| 0.2s | `cubic-bezier(0.4, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, background-color, border-color, color, fill, outline-color, stroke, text-decoration-color | ent-cta, price-interval |
| 0.2s | `ease-out` | background-color, color | mkt-nav |
| 0.3s | `cubic-bezier(0, 0, 0.2, 1)` | background-color, transform | nav-signin |
| 0.35s | `cubic-bezier(0, 0, 0.2, 1)` | all | login-apple, login-google |
| 0.5s | `cubic-bezier(0, 0, 0.2, 1)` | opacity | announce-card |
| 0.7s | `cubic-bezier(0.4, 0, 0.2, 1)` | transform | mkt-nav |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Feed card](#feed-card) | 362 x 649 | - | - | #df9443 | none | 0 |
| [Announcement card](#announcement-card) | 143.95 x 40 | - | 3.35544e+07px | oklab(0.173028 0.00000786781 0.00000345707 / 0.4) | none | 0px 40px |
| [Blog card](#blog-card) | 409.72 x 18.89 | - | - | transparent | none | 0 |
| [Get Pro](#get-pro) | 280 x 40 | - | 3.35544e+07px | #ffffff `core.color.primary.0` | none | 0px 32px |
| [Continue with Google](#continue-with-google) | 352 x 46 | 1px solid #ffffff `core.color.primary.0` | 14px | #ffffff `core.color.primary.0` | none | 12px 16px |

## Components

### App shell

The signed-out app sidebar on html.dark: Home, Agent, Train, Nodes, Assets, the tool list, Pricing with a 40% off chip, Enterprise, and a white Sign in button. Suisse Intl at 14px.

#### Sidebar
The signed-out app sidebar: Home, Agent, Train, Nodes, Assets, tool links, Pricing, Enterprise, Sign in. About 256px, near-black. Read as `sidebar` on the home page.

**Values (default).** size 255 x 622; background transparent; text Suisse Intl 14/20 400, oklch(0.985 0 0); icon 12 x 12, oklch(0.985 0 0); layers a.peer/menu-button.ring-sidebar-ring 239.0x36.0 oklch(0.269 0 0) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, oklab(0.999994 0.0000455678 0.0000200868 / 0.1) 0px 0px 0px 0.5px inset, rgba(0, 0, 0, 0.05) 0px 1px 2px 0px 10px.

Child layers that carry the look: a 239x36 background oklch(0.269 0 0) radius 10px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, oklab(0.999994 0.0000455678 0.0000200868 / 0.1) 0px 0px 0px 0.5px inset, rgba(0, 0, 0, 0.05) 0px 1px 2px 0px.

![Sidebar default](components/crops/sidebar-default.png)

#### Sidebar toggle
The "Toggle Sidebar" icon button. A local fold control. Read as `sidebar-toggle` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 36 x 36; radius 10px; background transparent; text Suisse Intl 14/20 450, oklch(0.708 0 0); transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 20 x 20, oklch(0.708 0 0) |
| hover | background oklch(0.269 0 0); text Suisse Intl 14/20 450, oklch(0.985 0 0); icon 20 x 20, oklch(0.985 0 0) |
| focus-visible | shadow oklab(0.556 0 0 / 0.5) 0px 0px 0px 3px; layers button.focus-visible:border-ring.focus-visible:ring-ring/50 36.0x36.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, oklab(0.556 0 0 / 0.5) 0px 0px 0px 3px, rgba(0, 0, 0, 0) 0px 0px 0px 0px 10px |
| pressed | background oklch(0.269 0 0); text Suisse Intl 14/20 450, oklch(0.985 0 0); icon 20 x 20, oklch(0.985 0 0) |

![Sidebar toggle default](components/crops/sidebar-toggle-default.png) ![Sidebar toggle hover](components/crops/sidebar-toggle-hover.png) ![Sidebar toggle focus-visible](components/crops/sidebar-toggle-focus-visible.png) ![Sidebar toggle pressed](components/crops/sidebar-toggle-pressed.png)

#### Sidebar home link
The Home item in the sidebar. Selected at rest (data-active). Read as `nav-home` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible) | size 239 x 36; padding 8px; radius 10px; background oklch(0.269 0 0); shadow oklab(0.999994 0.0000455678 0.0000200868 / 0.1) 0px 0px 0px 0.5px inset, rgba(0, 0, 0, 0.05) 0px 1px 2px 0px; text Suisse Intl 14/20 400, oklch(0.985 0 0); transition width 0.15s cubic-bezier(0.4, 0, 0.2, 1), height 0.15s cubic-bezier(0.4, 0, 0.2, 1), padding 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| pressed | size 234.22 x 35.28; transform scale(0.98) |

![Sidebar home link default](components/crops/nav-home-default.png) ![Sidebar home link hover](components/crops/nav-home-hover.png) ![Sidebar home link focus-visible](components/crops/nav-home-focus-visible.png) ![Sidebar home link pressed](components/crops/nav-home-pressed.png)

#### Pricing link
The sidebar Pricing link, including the yearly-discount badge. Measured, never followed from this spec. Read as `nav-pricing` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 239 x 36; padding 0px 8px; border T: 1px solid oklab(0.999994 0.0000455678 0.0000200868 / 0.5); radius 10px; background transparent; image linear-gradient(to right, oklch(0.932 0.032 255.585) 0%, oklch(0.809 0.105 251.813) 50%, oklch(0.424 0.199 265.638) 100%); shadow rgba(126, 112, 219, 0.3) 0px 0px 12px -2px, rgba(112, 160, 219, 0.2) 0px 0px 20px -4px, rgba(255, 255, 255, 0.2) 0px 0px 6px 0px inset; text Suisse Intl 14/20 400, oklch(0.379 0.146 265.522); transition margin 0.15s cubic-bezier(0.2, 0, 0, 1), opacity 0.15s cubic-bezier(0.2, 0, 0, 1), transform 0.15s cubic-bezier(0.2, 0, 0, 1); layers ::after rgba(0, 0, 0, 0) 0px rgba(139, 125, 232, 0.5) 0px 0px 10px 0px, rgba(126, 112, 219, 0.3) 0px 0px 20px 0px, rgba(255, 255, 255, 0.3) 0px 0px 8px 0px inset 0 |
| hover | background oklch(0.269 0 0); layers ::after rgba(0, 0, 0, 0) 0px rgba(139, 125, 232, 0.5) 0px 0px 10px 0px, rgba(126, 112, 219, 0.3) 0px 0px 20px 0px, rgba(255, 255, 255, 0.3) 0px 0px 8px 0px inset 0.823217 |
| focus-visible | layers ::after rgba(0, 0, 0, 0) 0px rgba(139, 125, 232, 0.5) 0px 0px 10px 0px, rgba(126, 112, 219, 0.3) 0px 0px 20px 0px, rgba(255, 255, 255, 0.3) 0px 0px 8px 0px inset 0.0142897 |
| pressed | size 234.22 x 35.28; background oklch(0.269 0 0); transform scale(0.98); layers ::after rgba(0, 0, 0, 0) 0px rgba(139, 125, 232, 0.5) 0px 0px 10px 0px, rgba(126, 112, 219, 0.3) 0px 0px 20px 0px, rgba(255, 255, 255, 0.3) 0px 0px 8px 0px inset 0.717429 |

![Pricing link default](components/crops/nav-pricing-default.png) ![Pricing link hover](components/crops/nav-pricing-hover.png) ![Pricing link focus-visible](components/crops/nav-pricing-focus-visible.png) ![Pricing link pressed](components/crops/nav-pricing-pressed.png)

#### Sign in
The white sidebar Sign in button. Measured, never followed. It opens /login. Read as `nav-signin` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 239 x 48; padding 8px; radius 10px; background oklch(0.985 0 0); shadow oklab(0 0 0 / 0.1) 0px 0px 0px 0.5px; text Suisse Intl 14/20 400, oklch(0.145 0 0); transition background-color 0.3s cubic-bezier(0, 0, 0.2, 1), transform 0.3s cubic-bezier(0, 0, 0.2, 1) |
| hover | background #e5e5e5 `core.color.primary.200` |
| focus-visible | shadow oklab(0 0 0 / 0.1) 0px 0px 0px 2px |
| pressed | size 234.22 x 47.04; background #e5e5e5 `core.color.primary.200`; transform scale(0.98) |

![Sign in default](components/crops/nav-signin-default.png) ![Sign in hover](components/crops/nav-signin-hover.png) ![Sign in focus-visible](components/crops/nav-signin-focus-visible.png) ![Sign in pressed](components/crops/nav-signin-pressed.png)

#### Tools menu button
The Tools button that opens the tool list. A local menu toggle. Read as `tools-button` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 239 x 36; padding 0px 8px; radius 10px; background transparent; text Suisse Intl 14/20 400, oklab(0.985 0 0 / 0.3); transition margin 0.15s cubic-bezier(0.2, 0, 0, 1), opacity 0.15s cubic-bezier(0.2, 0, 0, 1), transform 0.15s cubic-bezier(0.2, 0, 0, 1) |
| hover | background oklch(0.269 0 0) |
| focus-visible | shadow oklch(0.439 0 0) 0px 0px 0px 2px; layers button.text-sidebar-foreground/30.ring-sidebar-ring 239.0x36.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, oklch(0.439 0 0) 0px 0px 0px 2px, rgba(0, 0, 0, 0) 0px 0px 0px 0px 10px |
| pressed | size 234.22 x 35.28; background oklch(0.269 0 0); transform scale(0.98) |
| opened | background oklch(0.269 0 0) |

![Tools menu button default](components/crops/tools-button-default.png) ![Tools menu button hover](components/crops/tools-button-hover.png) ![Tools menu button focus-visible](components/crops/tools-button-focus-visible.png) ![Tools menu button pressed](components/crops/tools-button-pressed.png) ![Tools menu button opened](components/crops/tools-button-opened.png)

#### Search button
The sidebar Search control. Measured at rest. Opening the command palette and submitting a query are not done here. Read as `search-button` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 20 x 20; radius 6px; background transparent; text Suisse Intl 16/24 400, oklch(0.985 0 0); transition transform 0.15s ease-out; opacity 0; icon 12 x 12, oklch(0.985 0 0) |
| hover | background oklch(0.269 0 0); opacity none |
| focus-visible | shadow oklch(0.439 0 0) 0px 0px 0px 2px; layers button.text-sidebar-foreground.ring-sidebar-ring 20.0x20.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, oklch(0.439 0 0) 0px 0px 0px 2px, rgba(0, 0, 0, 0) 0px 0px 0px 0px 6px |
| pressed | size 19 x 19; background oklch(0.269 0 0); transform scale(0.95); icon 11.4 x 11.4, oklch(0.985 0 0) |

![Search button default](components/crops/search-button-default.png) ![Search button hover](components/crops/search-button-hover.png) ![Search button focus-visible](components/crops/search-button-focus-visible.png) ![Search button pressed](components/crops/search-button-pressed.png)

### Home feed

The signed-out home: an offer strip, a model-announcement carousel, a public generation feed, and a prompt composer. Generation is not submitted.

#### Offer banner
The top offer strip ("Unlimited Nano Banana for 7 days"). A campaign surface, hidden from other shots by closePromo when it is a dismiss overlay. Measured, never claimed. Read as `promo-banner` on the home page.

**Values (default).** size 119.22 x 40; padding 0px 24px; radius 3.35544e+07px; background oklab(0.173028 0.00000786781 0.00000345707 / 0.4); text Suisse Intl 14/20 450, #ffffff `core.color.primary.0`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1); layers ::after rgba(0, 0, 0, 0) 0px rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, oklab(0 0 0 / 0.1) 0px 0px 0px 0px inset, rgba(255, 255, 255, 0.25) 0px -1px 1px 0px inset, rgba(255, 255, 255, 0.25) 0px 1px 1px 0px inset 1; ancestors div.@container.relative bg transparent.

![Offer banner default](components/crops/promo-banner-default.png)

#### Feed card
A published generation card on the signed-out home feed. A public demo, not a signed-in asset. Read as `feed-card` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 362 x 649; background #df9443; text Suisse Intl 16/24 400, #ffffff `core.color.primary.0`; ancestors div.relative.w-full bg transparent |
| hover | text Suisse Intl 14/20 450, oklch(0 0 0); icon 16 x 16, #ffffff `core.color.primary.0` |

![Feed card default](components/crops/feed-card-default.png) ![Feed card hover](components/crops/feed-card-hover.png)

#### Announcement card
A model-announcement card on the home feed. Read as `announce-card` on the home page.

**Values (default).** size 143.95 x 40; padding 0px 40px; radius 3.35544e+07px; background oklab(0.173028 0.00000786781 0.00000345707 / 0.4); text Suisse Intl 14/20 450, #ffffff `core.color.primary.0`; transition opacity 0.5s cubic-bezier(0, 0, 0.2, 1), scale 0.15s cubic-bezier(0, 0, 0.2, 1), background-color 0.15s cubic-bezier(0, 0, 0.2, 1); opacity 0; layers ::after rgba(0, 0, 0, 0) 0px rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, oklab(0 0 0 / 0.1) 0px 0px 0px 0px inset, rgba(255, 255, 255, 0.25) 0px -1px 1px 0px inset, rgba(255, 255, 255, 0.25) 0px 1px 1px 0px inset 1.

![Announcement card default](components/crops/announce-card-default.png)

#### Home composer
The signed-out prompt ("Describe an idea or upload an image to edit it"). Sample text is typed and deleted. The generate control is never pressed. Read as `composer` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 822 x 48; padding 6px 10px; background transparent; text Suisse Intl 16/24 400, #ffffff `core.color.primary.0`; placeholder oklab(0.999994 0.0000455678 0.0000200868 / 0.5); ancestors div.group/promptbox.bg-primary-100/85 bg transparent |
| focused | shadow #ffffff 0px 0px 0px 0px, oklch(0.546 0.245 262.881) 0px 0px 0px 0px; outline 2px solid transparent, offset 2px; layers textarea.min-h-[2lh]!.w-full 822.0x48.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgb(255, 255, 255) 0px 0px 0px 0px, oklch(0.546 0.245 262.881) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px 2px solid rgba(0, 0, 0, 0) offset 2px; ancestors div.group/promptbox.bg-primary-100/85 bg rgba(0, 0, 0, 0.34) |
| filled | shadow #ffffff 0px 0px 0px 0px, oklch(0.546 0.245 262.881) 0px 0px 0px 0px; outline 2px solid transparent, offset 2px; layers textarea.min-h-[2lh]!.w-full 822.0x48.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgb(255, 255, 255) 0px 0px 0px 0px, oklch(0.546 0.245 262.881) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px 2px solid rgba(0, 0, 0, 0) offset 2px; ancestors div.group/promptbox.bg-primary-100/85 bg rgba(0, 0, 0, 0.35) |

![Home composer default](components/crops/composer-default.png) ![Home composer focused](components/crops/composer-focused.png) ![Home composer filled](components/crops/composer-filled.png)

#### Composer generate
The circular Generate control on the home composer (aria-label Generate). Measured, never clicked. Sending a prompt is a gated generation. Read as `composer-send` on the home page.

Not on the page when it was captured.

### Pricing

The /pricing marketing page: a white Sign up pill, a dark Log in pill, four plan cards (Free, Basic, Pro, Max) and a Monthly/Yearly interval. Get Pro and Get Free were measured, never followed.

#### Marketing nav
The pricing-page top nav: App, Features, Plugins, Image, Video, API, MCP, Pricing, Enterprise, Sign up, Log in. Read as `mkt-nav` on the pricing page.

**Values (default).** size 1440 x 79.5; padding 16px 64px; border B: 1px solid oklab(0 0 0 / 0.15); background transparent; text Suisse Intl 15/22.5 400, #ffffff `core.color.primary.0`; transition transform 0.7s cubic-bezier(0.4, 0, 0.2, 1), color 0.2s ease-out, background-color 0.2s ease-out; icon 22 x 22, #ffffff `core.color.primary.0`; layers header.header.section-container 1440.0x79.5 B:1px solid oklab(0 0 0 / 0.15); button.focus-visible:border-ring.focus-visible:ring-ring/50 132.8x36.0 rgb(255, 255, 255) T:1px solid oklab(0 0 0 / 0.2) / R:1px solid oklab(0 0 0 / 0.2) / B:1px solid oklab(0 0 0 / 0.2) / L:1px solid oklab(0 0 0 / 0.2) 3.35544e+07px; button.focus-visible:border-ring.focus-visible:ring-ring/50 71.6x36.0 rgb(38, 38, 38) 3..

Child layers that carry the look: header 1440x79.5 border 1px solid oklab(0 0 0 / 0.15); button 132.8x36 background #ffffff `core.color.primary.0` border 1px solid oklab(0 0 0 / 0.2) radius 3.35544e+07px; button 71.6x36 background #262626 `core.color.primary.800` radius 3.35544e+07px.

![Marketing nav default](components/crops/mkt-nav-default.png)

#### Log in
The marketing Log in control. Measured, never followed. Destination is /login. Read as `mkt-login` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 71.61 x 36; padding 8px 16px; radius 3.35544e+07px; background #262626 `core.color.primary.800`; text Suisse Intl 14/20 450, #ffffff `core.color.primary.0`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #202020 `core.color.primary.850` |
| focus-visible | shadow oklab(0.556 0 0 / 0.5) 0px 0px 0px 3px |
| pressed | background #202020 `core.color.primary.850` |

![Log in default](components/crops/mkt-login-default.png) ![Log in hover](components/crops/mkt-login-hover.png) ![Log in focus-visible](components/crops/mkt-login-focus-visible.png) ![Log in pressed](components/crops/mkt-login-pressed.png)

#### Sign up for free
The marketing Sign up control. Measured, never followed. Read as `mkt-signup` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 132.81 x 36; padding 8px 16px; border 1px solid oklab(0 0 0 / 0.2); radius 3.35544e+07px; background #ffffff `core.color.primary.0`; text Suisse Intl 14/20 450, #000000 `core.color.primary.1000`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #f5f5f5 `core.color.primary.100` |
| focus-visible | border 1px solid oklch(0.556 0 0); shadow oklab(0.556 0 0 / 0.5) 0px 0px 0px 3px |
| pressed | background #f5f5f5 `core.color.primary.100` |

![Sign up for free default](components/crops/mkt-signup-default.png) ![Sign up for free hover](components/crops/mkt-signup-hover.png) ![Sign up for free focus-visible](components/crops/mkt-signup-focus-visible.png) ![Sign up for free pressed](components/crops/mkt-signup-pressed.png)

#### Pricing heading
"Pick your plan". Read as `price-h1` on the pricing page.

**Values (default).** size 1184 x 40; background transparent; text Suisse Intl 36/40 450, oklch(0.985 0 0).

![Pricing heading default](components/crops/price-h1-default.png)

#### Free plan card
The Free plan column on /pricing: $0/month, Get Free. Read as `price-card` on the pricing page.

Not on the page when it was captured.

#### Pro plan heading
The Pro plan name. Read as `price-pro` on the pricing page.

**Values (default).** size 37.64 x 17.41; background transparent; text Suisse Intl 24/32 500, #ffffff `core.color.primary.0`; ancestors div.home-card.flex bg oklab(0 0 0 / 0.45).

![Pro plan heading default](components/crops/price-pro-default.png)

#### Billing interval
The monthly/yearly toggle on pricing. A local UI toggle, never a checkout. Read as `price-interval` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 118 x 36; padding 0px 12px; radius 3.35544e+07px; background transparent; text Suisse Intl 14/20 500, #ffffff `core.color.primary.0`; transition color 0.2s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), fill 0.2s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1); ancestors div.relative.flex bg oklab(0.999994 0.0000455678 0.0000200868 / 0.15) |

![Billing interval default](components/crops/price-interval-default.png) ![Billing interval hover](components/crops/price-interval-hover.png) ![Billing interval pressed](components/crops/price-interval-pressed.png)

#### Get Pro
The Pro plan button. Measured, never followed. Checkout and account creation sit behind this control. Read as `price-cta` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 280 x 40; padding 0px 32px; radius 3.35544e+07px; background #ffffff `core.color.primary.0`; text Suisse Intl 14/20 450, #000000 `core.color.primary.1000`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #000000 `core.color.primary.1000` |
| hover | background oklab(0.999994 0.0000455678 0.0000200868 / 0.9) |
| focus-visible | shadow oklab(0.556 0 0 / 0.5) 0px 0px 0px 3px |
| pressed | size 277.2 x 39.6; background oklab(0.999994 0.0000455678 0.0000200868 / 0.9); icon 15.84 x 15.84, #000000 `core.color.primary.1000` |

![Get Pro default](components/crops/price-cta-default.png) ![Get Pro hover](components/crops/price-cta-hover.png) ![Get Pro focus-visible](components/crops/price-cta-focus-visible.png) ![Get Pro pressed](components/crops/price-cta-pressed.png)

#### Yearly discount badge
The blue "40% off" chip on the Yearly interval. Read as `price-badge` on the pricing page.

**Values (default).** size 55.45 x 21; padding 4px 6px; border 1px solid transparent; radius 8px; background oklch(0.579 0.2497 257.07); text Suisse Intl 11/11 450, #ffffff `core.color.primary.0`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1).

![Yearly discount badge default](components/crops/price-badge-default.png)

#### Most popular badge
The badge on the Pro card. Read as `price-popular` on the pricing page.

**Values (default).** size 86.5 x 17.5; background transparent; text Suisse Intl 14/17.5 500, #ffffff `core.color.primary.0`; ancestors span.focus-visible:border-ring.focus-visible:ring-ring/50 bg transparent.

![Most popular badge default](components/crops/price-popular-default.png)

#### FAQ row
A pricing FAQ summary. Opened with its own toggle. Read as `faq-item` on the pricing page.

Not on the page when it was captured.

### Enterprise

The /enterprise page. Book a call was measured, never followed.

#### Enterprise heading
The enterprise hero heading. Read as `ent-h1` on the enterprise page.

**Values (default).** size 539.13 x 191.66; background transparent; text Suisse Intl 74.88/65.89 500, #ffffff `core.color.primary.0`.

![Enterprise heading default](components/crops/ent-h1-default.png)

#### Book a call
The sales CTA. Measured, never followed. The booking form is a gated surface. Read as `ent-cta` on the enterprise page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 119.06 x 40; padding 0px 24px; radius 3.35544e+07px; background #ffffff `core.color.primary.0`; text Suisse Intl 14/20 500, #000000 `core.color.primary.1000`; transition color 0.2s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), fill 0.2s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1) |
| focus-visible | outline 1px auto #007aff, offset 1px |

![Book a call default](components/crops/ent-cta-default.png) ![Book a call hover](components/crops/ent-cta-hover.png) ![Book a call focus-visible](components/crops/ent-cta-focus-visible.png) ![Book a call pressed](components/crops/ent-cta-pressed.png)

### Blog

The public blog index.

#### Blog heading
The blog index heading. Read as `blog-h1` on the blog page.

**Values (default).** size 1392 x 40; background transparent; text system-ui 36/40 500, #000000 `core.color.primary.1000`.

![Blog heading default](components/crops/blog-h1-default.png)

#### Blog card
A published blog card. Measured, not opened in this pass. Read as `blog-card` on the blog page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 409.72 x 18.89; background transparent; text system-ui 12/16.2 600, #ffffff `core.color.primary.0`; layers span.announce-label 42.7x18.2 rgba(255, 255, 255, 0.2) 999px; ancestors div.announce bg #2b5cff |

Child layers that carry the look: span 42.7x18.2 background rgba(255, 255, 255, 0.2) radius 999px.

![Blog card default](components/crops/blog-card-default.png) ![Blog card hover](components/crops/blog-card-hover.png)

### Plugins

The plugins marketing page, including the light hero on the marketing chrome.

#### Plugins heading
The plugins marketing heading. Read as `plug-h1` on the plugins page.

**Values (default).** size 768 x 135.34; background transparent; text Suisse Intl 72/67.68 500, #000000 `core.color.primary.1000`.

![Plugins heading default](components/crops/plug-h1-default.png)

#### Plugin link
A plugin product link. Measured, never followed into an install flow. Read as `plug-link` on the plugins page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 72 x 72; radius 22%; background rgba(255, 255, 255, 0.3); shadow rgba(255, 255, 255, 0.85) 0px 1px 0px 0px inset, rgba(255, 255, 255, 0.35) 0px 0px 0px 1px inset, rgba(0, 0, 0, 0.06) 0px 1px 2px 0px; text Suisse Intl 13/19.5 500, #ffffff `core.color.primary.0` |
| hover | size 111.59 x 111.59 |
| focus-visible | outline 1px auto #007aff, offset 1px |

![Plugin link default](components/crops/plug-link-default.png) ![Plugin link hover](components/crops/plug-link-hover.png) ![Plugin link focus-visible](components/crops/plug-link-focus-visible.png)

### Login boundary

The /login page: Continue with Google, Continue with Apple, Single Sign-On (SSO), and an email field. Nothing was submitted and no OAuth flow was followed.

#### Login heading
"Welcome to Krea" / "Log in or sign up". The auth boundary. Nothing is submitted. Read as `login-h1` on the login page.

**Values (default).** size 352 x 40; background transparent; text Suisse Intl 34/40 600, #ffffff `core.color.primary.0`.

![Login heading default](components/crops/login-h1-default.png)

#### Continue with Google
OAuth button. Measured, never clicked through. Following it is an OAuth flow. Read as `login-google` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 352 x 46; padding 12px 16px; border 1px solid #ffffff `core.color.primary.0`; radius 14px; background #ffffff `core.color.primary.0`; text Suisse Intl 14/20 500, #000000 `core.color.primary.1000`; transition all 0.35s cubic-bezier(0, 0, 0.2, 1); icon 16 x 16, #000000 `core.color.primary.1000` |
| hover | background #e5e5e5 `core.color.primary.200` |
| focus-visible | outline 1px auto #101010 `core.color.primary.950`, offset 0px |
| pressed | background #e5e5e5 `core.color.primary.200` |

![Continue with Google default](components/crops/login-google-default.png) ![Continue with Google hover](components/crops/login-google-hover.png) ![Continue with Google focus-visible](components/crops/login-google-focus-visible.png) ![Continue with Google pressed](components/crops/login-google-pressed.png)

#### Continue with Apple
OAuth button. Measured, never followed. Read as `login-apple` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 352 x 46; padding 12px 16px; border 1px solid #ffffff `core.color.primary.0`; radius 14px; background #ffffff `core.color.primary.0`; text Suisse Intl 14/20 500, #000000 `core.color.primary.1000`; transition all 0.35s cubic-bezier(0, 0, 0.2, 1); icon 18 x 18, #000000 `core.color.primary.1000` |
| hover | background #e5e5e5 `core.color.primary.200` |

![Continue with Apple default](components/crops/login-apple-default.png) ![Continue with Apple hover](components/crops/login-apple-hover.png)

#### SSO
SSO button. Measured, never followed. Read as `login-sso` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 352 x 46; padding 12px 16px; border 1px solid #ffffff `core.color.primary.0`; radius 14px; background #ffffff `core.color.primary.0`; text Suisse Intl 14/20 500, #000000 `core.color.primary.1000`; transition color 0.15s cubic-bezier(0, 0, 0.2, 1), background-color 0.15s cubic-bezier(0, 0, 0.2, 1), border-color 0.15s cubic-bezier(0, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0, 0, 0.2, 1), fill 0.15s cubic-bezier(0, 0, 0.2, 1), stroke 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0, 0, 0.2, 1); icon 20 x 20, #000000 `core.color.primary.1000` |
| hover | background #e5e5e5 `core.color.primary.200` |

![SSO default](components/crops/login-sso-default.png) ![SSO hover](components/crops/login-sso-hover.png)

#### Email field
The email field on the login boundary. Sample text is typed and deleted. Enter is never pressed, and Continue with Email is never clicked. Read as `login-email` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 352 x 46; padding 12px 12px 12px 44px; border 1px solid #404040 `core.color.primary.700`; radius 14px; background oklab(0 0 0 / 0.25); text Suisse Intl 14/20 450, #ffffff `core.color.primary.0`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1); placeholder #737373 `core.color.primary.500` |
| focused, filled | background #000000 `core.color.primary.1000`; shadow #ffffff 0px 0px 0px 0px, oklch(0.546 0.245 262.881) 0px 0px 0px 0px |

![Email field default](components/crops/login-email-default.png) ![Email field focused](components/crops/login-email-focused.png) ![Email field filled](components/crops/login-email-filled.png)

#### Continue with Email
The email submit control. Measured at rest and hover only. Never clicked, so no account is created and no code is sent. Read as `login-email-btn` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 352 x 46; padding 13px 0px; radius 14px; background oklab(0.579 -0.0558729 -0.243369 / 0.15); shadow rgba(0, 0, 0, 0.05) 0px 1px 2px 0px; text Suisse Intl 14/20 500, oklch(0.579 0.2497 257.07); transition colors 0.1s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.1s cubic-bezier(0.4, 0, 0.2, 1), saturate 0.1s cubic-bezier(0.4, 0, 0.2, 1); opacity 0.75 |

![Continue with Email default](components/crops/login-email-btn-default.png) ![Continue with Email hover](components/crops/login-email-btn-hover.png)

#### Terms link
The Terms of Service link on the login page. Read as `login-terms` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 93 x 16; background transparent; text Suisse Intl 12/16 450, #e5e5e5 `core.color.primary.200` |
| hover | text Suisse Intl 12/16 450, #ffffff `core.color.primary.0` |

![Terms link default](components/crops/login-terms-default.png) ![Terms link hover](components/crops/login-terms-hover.png)

### Image tool (signed out)

The /image tool signed out: a model gallery and a prompt. Generate was measured where it painted, never clicked.

#### Image tool shell
The signed-out /image tool. Generation is gated: the prompt is measured if present, never submitted. Read as `image-shell` on the image page.

**Values (default).** size 1440 x 900; background transparent; text Suisse Intl 16/24 500, oklch(0.708 0 0); icon 20 x 20, oklch(0.708 0 0); layers div.bg-primary-0.sm:bg-primary-150 1440.0x900.0 rgb(0, 0, 0); div.fixed.inset-y-0 256.0x900.0 R:1px solid oklch(1 0 0 / 0.1); div.bg-sidebar.group-data-[variant=floating]:border-sidebar-border 255.0x900.0 oklch(0 0 0); a.peer/menu-button.ring-sidebar-ring 239.0x36.0 oklch(0.269 0 0) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, oklab(0.999994.

Child layers that carry the look: div 1440x900 background #000000 `core.color.primary.1000`; div 256x900 border 1px solid oklch(1 0 0 / 0.1); div 255x900 background oklch(0 0 0).

![Image tool shell default](components/crops/image-shell-default.png)

#### Prompt field
The image prompt, if the signed-out page paints one. Sample text is typed and deleted. Generate is never pressed. Read as `image-prompt` on the image page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 870 x 48; padding 6px 10px; background transparent; text Suisse Intl 16/24 400, #ffffff `core.color.primary.0`; placeholder oklab(0.999994 0.0000455678 0.0000200868 / 0.5) |
| focused, filled | shadow #ffffff 0px 0px 0px 0px, oklch(0.546 0.245 262.881) 0px 0px 0px 0px; outline 2px solid transparent, offset 2px; layers textarea.min-h-[2lh]!.w-full 870.0x48.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgb(255, 255, 255) 0px 0px 0px 0px, oklch(0.546 0.245 262.881) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px 2px solid rgba(0, 0, 0, 0) offset 2px |

![Prompt field default](components/crops/image-prompt-default.png) ![Prompt field focused](components/crops/image-prompt-focused.png) ![Prompt field filled](components/crops/image-prompt-filled.png)

#### Generate
The generate control on /image (aria-label Generate). Measured, never clicked. Submitting a generation is a gated action. Read as `image-generate` on the image page.

Not on the page when it was captured.

### Mobile (390 wide)

The phone shell at 390px: Explore, Upgrade, tool chips, and a search field.

#### Mobile shell
The app shell at 390px. Read as `m-sidebar` on the home page at 390 wide.

Not on the page when it was captured.

#### Mobile menu button
The sidebar toggle at 390px. A local control. Read as `m-menu` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 52 x 64; background transparent; text Suisse Intl 14/20 450, oklch(0.985 0 0); transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 20 x 20, oklch(0.985 0 0); ancestors header.bg-background.fixed bg oklch(0.145 0 0) |
| hover | background oklab(0.269 0 0 / 0.5) |
| focus-visible | shadow oklab(0.556 0 0 / 0.5) 0px 0px 0px 3px; layers button.focus-visible:border-ring.focus-visible:ring-ring/50 52.0x64.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, oklab(0.556 0 0 / 0.5) 0px 0px 0px 3px, rgba(0, 0, 0, 0) 0px 0px 0px 0px |
| pressed | background oklab(0.269 0 0 / 0.5) |

![Mobile menu button default](components/crops/m-menu-default.png) ![Mobile menu button hover](components/crops/m-menu-hover.png) ![Mobile menu button focus-visible](components/crops/m-menu-focus-visible.png) ![Mobile menu button pressed](components/crops/m-menu-pressed.png)

#### Mobile Sign in
Sign in at 390px. Measured, never followed. Read as `m-signin` on the home page at 390 wide.

Not on the page when it was captured.

## Icons

No standalone SVG icon set was lifted on this pass. The wordmark, tool glyphs and plan icons are visible in the crops and screenshots. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### Account, generation and checkout

The 2026-11-21 refresh stopped at the empty login wall. Google, Apple, SSO and Continue with Email were not clicked. Nothing was typed. No account was created. Files redirects to login and was not followed. The empty wall is [login-dark-default](screenshots/login-dark-default.png).

### Pages

- **https://www.krea.ai/login.** Welcome to Krea, the Google, Apple and SSO buttons, and the email field. Continue with Email was submitted once; Turnstile returned captcha_failed.
- **https://www.krea.ai/assets.** Redirects to /login?redirect=%2Fassets. The signed-in asset library was not captured: the email pass never got past Turnstile.
- **https://www.krea.ai/pricing.** Get Free, Get Basic, Get Pro and Get Max open account or checkout. They were measured, never followed.
- **https://www.krea.ai/enterprise.** Book a call is a sales form. It was measured, never followed.
- **https://www.krea.ai/ and https://www.krea.ai/image.** Generate and the composer submit a generation. They were measured, never clicked.
- **Train, Node Editor, account settings, billing and API keys.** The signed-in icon rail lists them. Settings navigated toward /manage/profile and did not paint. They were not opened.
- **Claim offer** on the home strip links into a gated signup. It was not followed.
- **https://www.krea.ai/docs** Get API key, and **https://www.krea.ai/mcp** Add Krea connector, are gated actions. They were not followed.
- **Other tool routes** (/video, /enhancer, /agent) share the signed-out shell. They were not shot individually.

### States

- **Pressed** was forced with DevTools, so a script that runs on a real mousedown is not in the reading.
- **Tools menu, sidebar fold and the pricing interval** were toggled locally. Nothing was submitted.
- **Validation, disabled, loading and error states** of generation and checkout do not paint signed out. They are absent, not measured.
- **composer-send, image-generate, price-card, faq-item, m-sidebar and m-signin** were not found as stable elements on the pass that wrote components-computed.json. The controls that did paint (Sign in, Get Pro, the composer field, the phone menu) are in the inventory.

### Themes

One painted public theme: html.dark, a #101010 field, white controls, #006eff action blue. An html.light comparison was resolved and is not a shipped public theme. Marketing heroes on /plugins and /features can paint a light field while html stays dark. Docs (/docs) uses a separate light sheet set and is not folded into the app tokens. The painted semantic roles are stored in the light set. The dark set is empty.

### Fonts

- **Suisse Intl** is the UI face and **Suisse Intl Mono** is the mono face. Both are served by the site. Font files are not shipped in this package.

### Screenshots

- Published generation cards, blog posts and marketing copy are the product's public content. Only frames and components were measured.
- Screenshots are stored as 256-colour PNGs. Read exact colours from the tokens or the raw files.

### Content left out

- Feed artwork, plan prices and blog copy are the product's content. Only frames and components were measured.
