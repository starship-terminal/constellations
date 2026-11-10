# Acuity Scheduling patterns

How Acuity Scheduling's components combine to do the recurring jobs on its public marketing pages, written from the captures of 2026-11-09/10 (signed out, 1440 and 390 wide). Each pattern says when the site uses it, the components it is built from (entries in [components.md](components.md), values in [tokens.json](tokens.json)), the layout, and the screens that show it. These are observations of what the site does, not Squarespace's own guidance.

| Pattern | Captured | Example screen |
|---|---|---|
| [Shell and navigation](#shell-and-navigation) | yes | [home-light-default](screenshots/home-light-default.png) |
| [Pastel hero](#pastel-hero) | yes | [home-light-default](screenshots/home-light-default.png) |
| [Card sections](#card-sections) | yes | [home-light-full](screenshots/home-light-full.png) |
| [Pricing page](#pricing-page) | yes | [pricing-light-default](screenshots/pricing-light-default.png) |
| [Auth gate](#auth-gate) | yes, at rest and state-forced only | [login-light-default](screenshots/login-light-default.png) |
| [Mobile fold](#mobile-fold) | yes | [mobile-home-light-menu](screenshots/mobile-home-light-menu.png) |

## Shell and navigation

**When.** Every marketing page — home, pricing, features, solutions, about, learn — sits inside the same shell.

**Components.** [Header](components.md#header), [Wordmark](components.md#logo), [Nav link](components.md#nav-link), [Nav dropdown trigger](components.md#nav-trigger), [Nav dropdown](components.md#nav-dropdown), [Dropdown item](components.md#dropdown-item), [Log in link](components.md#login-link), [Nav CTA](components.md#nav-cta), and the footer set: [Footer](components.md#footer), [Footer column title](components.md#footer-col-title), [Footer link](components.md#footer-link), [Social link](components.md#social-link), [Legal link](components.md#footer-legal).

**Layout.** An 80px white bar (`layout.nav-height`) holds the wordmark left, five 14/18.76 Clarkson items centre (Solutions, Product and Resources open 22px-radius mega-menu panels padded 44px, captured in `home-light-dropdown`), Log in and the ink Get-started pill right (`component.button-primary-bg`, 12px radius, 42.8px). Hover fades links to 50%; the pill lightens to `#3e5772`. The footer is a plain white band: 16px column titles over 12px links, social circles, a hairline legal row. The shell draws no shadows; sections separate by whitespace and band fills.

**Screens.** [home-light-default](screenshots/home-light-default.png), [home-light-dropdown](screenshots/home-light-dropdown.png), [features-light-default](screenshots/features-light-default.png), [about-light-default](screenshots/about-light-default.png).

## Pastel hero

**When.** The top of the home page, and the pattern the industry and product pages borrow: a soft pastel ground under a centred serif headline.

**Components.** [Hero](components.md#hero), [Hero title](components.md#hero-title), [Hero sub](components.md#hero-sub), [Sign up with email](components.md#hero-cta-email), [Sign up with Google](components.md#hero-cta-google), [Signup legal line](components.md#hero-terms).

**Layout.** The hero paints a `linear-gradient(66deg)` over the white page — nine declared pastel variants rotate per load (`gradient.hero` records the captured one) with a white ::after wash at its foot. The title is Clarkson Serif 40/48 medium in ink (`typography.display`); the sub is Clarkson 16/25.6 in the same ink. Two 56px ghost CTAs sit side by side on 1px ink rules (`component.button-outline-border`) and fade to 80% on hover; a 10px legal line trails them. A client-site preview carousel scrolls under the hero's fold.

**Screens.** [home-light-default](screenshots/home-light-default.png), [beauty-light-default](screenshots/beauty-light-default.png), [how-it-works-light-default](screenshots/how-it-works-light-default.png).

## Card sections

**When.** The home page's middle: industries, the feature band and testimonials — the site's card vocabulary.

**Components.** [Industry card](components.md#vertical-card), [Industries CTA](components.md#vertical-cta), [Feature card](components.md#feature-card), [Feature card title](components.md#feature-card-title), [Testimonial card](components.md#testimonial-card), [Carousel dots](components.md#carousel-dots), [Integration logo](components.md#integration-logo), [Bottom CTA](components.md#bottom-cta).

**Layout.** Cream `#fdf9f7` industry cards (`surface-warm`, 16px radius, `shadow.card`) tile the solutions grid; a `#f4f4f4` feature card (`surface-mist`) pairs 40px padding, a serif card title and an ink CTA. Testimonials auto-play in a 22px-radius frame: a lavender `#d6d0ed` card on a `#fafafa` slide with a tag pill (`component.tag-bg`), marked by a dash indicator — there are no arrows (`carousel-nav` is an honest miss). The page closes on the pale-blue `#e0ebf4` band (`surface-band`): the navy support card (serif headline, link row, photo) then a 230 x 72 ink `bottom-cta`, then the footer.

**Screens.** [home-light-full](screenshots/home-light-full.png), [solutions-light-default](screenshots/solutions-light-default.png), [learn-light-default](screenshots/learn-light-default.png).

## Pricing page

**When.** /pricing: a photographic hero over the plan grid and the navy FAQ.

**Components.** [Pricing plans block](components.md#pricing-hero), [Plan card](components.md#plan-card), [Plan name](components.md#plan-name), [Plan price](components.md#plan-price), [Plan CTA](components.md#plan-cta), [Plan feature row](components.md#plan-feature), [FAQ accordion](components.md#faq-accordion), [FAQ question](components.md#accordion-title), [FAQ answer](components.md#accordion-panel), [FAQ question, open](components.md#accordion-title-open).

**Layout.** The top band is a background photograph (not a flat fill) carrying a white serif title and the segment toggle — a translucent track holding a 100px-radius white pill. Three white plan cards (~449px, 1px `#e4e4e4` hairline, 12px radius) hold a serif plan name, an 18/27 price, a 46px ink `plan-cta` (hover `#1e2d3a`, pressed `scale(0.9)`), a hairline divider and 14/22 feature rows whose dashed markers open near-black tooltips (`component.tooltip-bg`, r4, `shadow.overlay`). Below, the FAQ runs on the ink band (`section.signup-faqs`, `surface-inverse`): 640px white rows separated by 10%-white hairlines (`border-on-dark`), the open answer measured in `pricing-light-faq-open`.

**Screens.** [pricing-light-default](screenshots/pricing-light-default.png), [pricing-light-faq-open](screenshots/pricing-light-faq-open.png), [pricing-light-full](screenshots/pricing-light-full.png), [mobile-pricing-light-default](screenshots/mobile-pricing-light-default.png).

## Auth gate

**When.** Get started and Log in hand off to Squarespace's shared account surface: the create-account dialog at /get-started and the sign-in card at secure.acuityscheduling.com — the package's only forms.

**Components.** [Create-account card](components.md#gate-card), [Continue with Google](components.md#gate-google), [Continue with Apple](components.md#gate-apple), [Continue with Email](components.md#gate-email), [MORE OPTIONS](components.md#more-options) and [open](components.md#more-options-open), [Email field](components.md#login-email), [Password field](components.md#login-password), [Log in submit](components.md#login-submit), [OAuth row](components.md#oauth-google), [Can't log in](components.md#cant-login), [Create account link](components.md#create-account-link).

**Layout.** A 540px white dialog at 6px radius on `shadow.modal`. Its controls are not the marketing buttons: square 55px rows on 1px black rules (`component.button-gate-border`) in 14/22 medium, underlined text fields with `#949494` placeholders (`muted`), and caps labels (12/22 medium, uppercase, 0.5px tracking, `typography.caps`). The submit stays on the disabled `#f2f2f2`/`#b7b7b7` pair (`component.field-disabled-bg`, `disabled-text`) until the form validates. Focus is a double box-shadow ring (`shadow.focus-ring`). Everything was measured and state-forced, never submitted: the fields were typed with a throwaway address and cleared.

**Screens.** [get-started-light-default](screenshots/get-started-light-default.png), [get-started-light-more-options](screenshots/get-started-light-more-options.png), [login-light-default](screenshots/login-light-default.png), [login-light-full](screenshots/login-light-full.png).

## Mobile fold

**When.** Every page at 390: the bar collapses and navigation moves into a sheet.

**Components.** [Mobile header](components.md#m-header), [Hamburger](components.md#m-hamburger), [Mobile menu](components.md#m-menu), [Mobile menu link](components.md#m-menu-link), [Mobile hero](components.md#m-hero).

**Layout.** The 55px bar (`layout.nav-height-mobile`) keeps the wordmark and a hamburger; the sheet is a full-height white panel over a 50% scrim (`overlay`): 28/37.52 Clarkson links (`typography.menu`, `#2d2d2d`) on `#f2f2f2` hairline rows, an ink Get-started bar and a Log in under it. Focus inside the sheet is the amber `#e59700` ring (`focus-alt`). The mega-menu's two columns collapse into disclosure rows; heroes stack single-column.

**Screens.** [mobile-home-light-default](screenshots/mobile-home-light-default.png), [mobile-home-light-menu](screenshots/mobile-home-light-menu.png), [mobile-home-light-full](screenshots/mobile-home-light-full.png), [mobile-pricing-light-default](screenshots/mobile-pricing-light-default.png).
