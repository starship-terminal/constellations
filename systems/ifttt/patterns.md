# IFTTT patterns

How the measured components combine on each captured surface. Every value cited is in [tokens.json](tokens.json); the components are in [components.md](components.md), the multi-width geometry in [raw/layout.json](raw/layout.json), and the full-page evidence in [screenshots/](screenshots).

Two surfaces carry the one system: **ifttt.ai** (the marketing home, where ifttt.com/ 301s) and **ifttt.com** (the /explore gallery, the detail pages, /plans and the corporate/legal pages). Both paint the same unified header, the same white ground and the same pill-first control set; Sass-compiled Rails classes carry literal values, so the design system is the measured component layer, not a variable layer.

## The unified header

Every page carries `header.unified-header`: the **IFTTT.ai pill wordmark** (the blue/orange pill mark), a centred **search field** ("Search for Applets, services, etc." — a rounded input, measured clicked-into, never queried), the **Explore** and **Plans** text links, then the two action pills — **Log in** (outlined black pill) and **Get started** (solid near-black pill). On the dark heroes (explore, service, applet, connect) the header paints on the dark ground: the links and outlined pill flip to white ink, Get started inverts to a white pill with black text. On the gallery and corporate pages it sits on white with black ink. At 390px the search field, links and pills collapse behind a **hamburger** (`button.closed` → `body.mobile-menu-opened`): a full-screen menu listing the logo, Explore and Plans in large type, with Log in (outlined) and Get started (solid) as stacked pills at the bottom, closed with the X it swaps to.

## The prompt heroes

- **Home** (ifttt.ai): a centred hero on the white ground — "The easiest way to automate anything" in Museo Sans Rounded 900, a two-line subhead ("Your apps and devices work better together. Connect 1,000+ services in minutes."), then the **prompt field** ("Describe what you'd like to build") with the solid **Start building** pill below it. Floating service-icon tiles frame the hero on blue and orange grounds — the brand colour arrives through the services, not the chrome. Below the hero the featured section carries a row of **category tabs** (`.featured-tab` pills, the active one filled).
- **Explore** (/explore): the hero paints a **dark ground** — `light.component.dark.heroBg` — with a cycling headline "Automate *X* with *Y*" where X and Y rotate through service names in their brand colours (the `--cycle-*` custom properties drive the rotation), above a white **prompt card** ("In a few words, tell us what you'd like to automate and we'll build it for you") holding its own Start building pill, and a "Try these examples" row of ghost cards on the dark ground. Below, "Explore automations built by the IFTTT community" introduces a search field and the gallery tabs.

## The gallery grid

/explore (+/explore/services, /explore/stories, /explore/applets — /applets, /services and /search all redirect into it) is a tabbed card gallery under the explore hero: the **All / Applets / Services / Stories** tab strip, a search field, then a responsive grid of **Applet/service cards** — rounded tiles carrying the service icons, the card title, the author handle and the use count, each tile painted by `--card-color` (the one custom property the system actually uses: per-card brand tint). The grids run long (explore-services is ~33.8k px at 1440, ~92k px at 390) and lazy-load on scroll — the full shots are bounded tiles and the bound is in each sidecar.

## The plans surface

/plans (the pricing surface; /pricing is not a live route) is "Pay only for what you use" on white: the **Monthly/Yearly switch** (`button.switch-field` — a pill toggle with `.switch-field-knob`, Yearly carries a green "SAVE 30%" badge) above four **plan cards** — Free ($0.00), Starter ($2.99), Pro ($7.99, carrying the dark RECOMMENDED header band), Pro+ ($19.99). Each card is a bordered white panel: plan name, large price + "/month", the credits chip ("20,000 credits / month"), a check-list of features, and the **Get started** pill (outlined on Free/Starter/Pro+, solid black on the recommended Pro). The CTAs lead to checkout — measured, never followed. The switch was toggled both ways for the `-monthly` and `-yearly` repaints.

## The detail pages

Service (/twitter, /todoist), applet and connect pages share a chrome: **Back** and **Share** pills in the hero corners, a **brand-coloured hero** (X black on /twitter, iRobot green on the applet, Discord/Instagram brand art on connect) holding the service icons, the page title in large type and the byline (author handle + use count), then white-ground content below — the "About" prose with a **"show more" `.clamp-toggle`** expander (pressed for the expanded state), and for applets the giant **Connect toggle**: a track-height black pill with a brand-tinted knob, the install action measured at rest and never pressed. **Share** opens the product's own modal (`button.modal-open` → `.share-modal`): a dimmed overlay and a centred white card with the short ift.tt URL field, the X/Facebook/LinkedIn/Reddit icon row, a black **Copy** pill and the close X — the modal was opened through its own button, measured, captured and closed through its X; Copy and the social icons were never pressed.

## Corporate and legal surfaces

/mcp, /solutions/productivity, /solutions/smart-home, /about, /careers and /partners reuse the header, the white ground and the pill CTAs in long marketing sections (partners runs ~32k px). /terms is a plain legal document (long prose, ~52.8k px at 390). The 404 keeps the header and paints the not-found page inside it.

## Mobile compression

At 390px the unified header collapses to wordmark + hamburger (the full-screen menu above), the heroes stack their prompt card and copy full-width, the plan cards become a single column (the switch stays), the gallery grid narrows to one card across, and the detail heroes keep their brand grounds with Back/Share pinned. `mobile-*` shots cover home (default + menu-open), explore, plans, a service page and the applet.

## Motion and focus

The motion probe ([raw/motion.json](raw/motion.json)) records the live animation inventory — the explore hero's service-name cycler, the home hero's floating icon tiles, carousels and reveal animations across five pages. `prefers-reduced-motion` is **partially honoured**: some animated groups stop under the emulated reduction while others keep animating — the probe's per-page verdicts are the evidence; the package claims no reduced-motion guarantee. Focus paints through the pill outlines — the prompt field and search field show a focus ring state on keyboard focus (`*-focused` crops); pressed states in the crops are DevTools-forced pseudo-classes.

## The no-theme architecture

IFTTT declares almost no custom properties and paints a single theme. The token set therefore splits three ways: `core.palette.*` holds the literal colours the stylesheets declare (with their selectors as provenance), `core.font.family.*` and `core.typography.*` hold the Museo Sans Rounded face names and measured composites, and `light.*` holds the semantic roles read off the painted page — `light.color.*` for the page/action/text roles, `light.misc.*` for the few real variables, and `light.component.dark.*` for the grounds the dark sections paint. A dark theme does not exist and is not fabricated.
