# Acuity Scheduling patterns

How Acuity Scheduling's components combine on its public marketing pages, written from the 2026-11-21 captures (signed out, 1440×900 and 390×844). Each pattern says when the site uses it, the components it is built from (entries in [components.md](components.md), values in [tokens.json](tokens.json)), the layout, and the screens that show it. The control map is [site-tree.md](site-tree.md). These are observations of what the site does, not Squarespace's own guidance.

| Pattern | Captured | Example screen |
|---|---|---|
| [Shell and navigation](#shell-and-navigation) | yes | [home-light-default](screenshots/home-light-default.png) |
| [Pastel hero](#pastel-hero) | yes | [home-light-default](screenshots/home-light-default.png) |
| [Card sections](#card-sections) | yes | [home-light-full](screenshots/home-light-full.png) |
| [Pricing page](#pricing-page) | yes | [pricing-light-default](screenshots/pricing-light-default.png) |
| [Login wall](#auth-gate) | photographed, not filled | [login-light-default](screenshots/login-light-default.png) |
| [Enterprise lead](#enterprise-lead) | empty form only | [enterprise-light-default](screenshots/enterprise-light-default.png) |
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

## Login wall

**When.** `/login.php` is the public email wall. Nav Log in and Get started redirect to login.squarespace.com. Those branches stop. See [site-tree.md](site-tree.md).

**What was captured.** The login wall shows a wordmark, CREATE ACCOUNT (not followed), the heading "Log in to Acuity Scheduling", an EMAIL ADDRESS label, an empty username field, and a disabled NEXT button. The field was focused empty. Nothing was typed. Squarespace was not clicked. The password step was not reached.

**Measured on 2026-11-21.** The email field is Clarkson 16px, 310×52, white, 1px border. NEXT is 12px medium, `#cccccc` on `#ebebeb`, 310×55, disabled. Those readings are in [raw/components-computed.json](raw/components-computed.json).

**Not captured.** The Squarespace signup dialog (Google, Apple, email, MORE OPTIONS) and the Squarespace login card (Google, Apple, Facebook). Earlier crops of those surfaces were removed from this package because this capture did not open them.

**Screens.** [login-light-default](screenshots/login-light-default.png), [login-light-full](screenshots/login-light-full.png), [mobile-login-wall-light-default](screenshots/mobile-login-wall-light-default.png).

## Enterprise lead

**When.** `/enterprise` ends in a Salesforce web-to-lead form. The form is part of the page, so the empty fields are in the full-page shot.

**What was captured.** An empty text field (Clarkson 16px, 8px radius, 1px `#c1ccca` border, 670×46) and an ink submit (14px, `#283849`, 12px radius, 95×43). Not typed. Not submitted. Validation, error, and success are Not captured.

**Screens.** [enterprise-light-default](screenshots/enterprise-light-default.png), [enterprise-light-benefit](screenshots/enterprise-light-benefit.png).

## Mobile fold

**When.** Every page at 390: the bar collapses and navigation moves into a sheet.

**Components.** [Mobile header](components.md#m-header), [Hamburger](components.md#m-hamburger), [Mobile menu](components.md#m-menu), [Mobile menu link](components.md#m-menu-link), [Mobile hero](components.md#m-hero).

**Layout.** The 55px bar (`layout.nav-height-mobile`) keeps the wordmark and a hamburger; the sheet is a full-height white panel over a 50% scrim (`overlay`): 28/37.52 Clarkson links (`typography.menu`, `#2d2d2d`) on `#f2f2f2` hairline rows, an ink Get-started bar and a Log in under it. Focus inside the sheet is the amber `#e59700` ring (`focus-alt`). The mega-menu's two columns collapse into disclosure rows; heroes stack single-column.

**Screens.** [mobile-home-light-default](screenshots/mobile-home-light-default.png), [mobile-home-light-menu](screenshots/mobile-home-light-menu.png), [mobile-home-light-menu-solutions](screenshots/mobile-home-light-menu-solutions.png), [mobile-pricing-light-default](screenshots/mobile-pricing-light-default.png).
