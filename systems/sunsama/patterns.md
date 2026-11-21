# Patterns

How the measured components combine on the public site. Screens are light only, 1440x900 and 390x844. Control map: [site-tree.md](site-tree.md).

## Marketing shell

Desktop: [header](components.md) (1440x84, transparent) with logo, flat links, Login, and the orange Start for Free button. Links go to a URL or to `#features`. They do not open a menu. Login is a stop branch. Start for Free is a stop branch.

The page ground is `light.page` (`#fafafa`). Body type is DM Sans. The footer is a tall link region ([footer](components/crops/footer-default.png)) with a newsletter field that was not filled.

Screens: [home-light-default](screenshots/home-light-default.png), [home-light-full](screenshots/home-light-full.png).

## Home hero

A large DM Sans headline ([hero-title](components/crops/hero-title-default.png), 51.2px / 600) sits on the warm grey page. The primary action is the orange button ([cta-primary](components/crops/cta-primary-default.png)). Below it, the assistant pill ([ai-pill](components/crops/ai-pill-default.png)) opens a white dialog ([ai-panel](components/crops/ai-panel-opened.png)) with a 24px / 48px shadow. Tabs inside that dialog use a 1px inset ink ring when selected.

Testimonial arrows ([slider-next](components/crops/slider-next-default.png)) move the quote. They do not navigate.

Screens: [home-light-ai-panel](screenshots/home-light-ai-panel.png), [home-light-ai-chatgpt](screenshots/home-light-ai-chatgpt.png), [home-light-slider-next](screenshots/home-light-slider-next.png).

## Feature and proof pages

Feature, role, team, love, about, blog, and desktop/mobile download pages reuse the same shell. The daily-planning page adds a green in-page demo button ([demo-button](components/crops/demo-button-default.png), `#30c78a`, 6px radius) that opens a panel on the same URL.

Compare uses eight logo tabs. The selected tab is opaque white. The rest sit at opacity 0.7. See [compare-light-motion-tab](screenshots/compare-light-motion-tab.png).

Integrations open a Webflow lightbox from an image link. See [integration-light-lightbox](screenshots/integration-light-lightbox.png).

Pro tips filter with a small combobox. Opened and hover ink is `#2da8ff`. Search was not typed. See [protips-light-categories](screenshots/protips-light-categories.png).

## Pricing

Two static price cards ([price-card](components/crops/price-card-default.png)): half-white fill, 32px padding, a soft 16px/30px shadow. Copy states $17 billed yearly and $22 billed monthly. There is no monthly/yearly toggle. FAQ titles are expanded headings, not disclosures.

Screens: [pricing-light-default](screenshots/pricing-light-default.png), [pricing-light-faq](screenshots/pricing-light-faq.png), [pricing-light-full](screenshots/pricing-light-full.png).

## Signup wall

`/start/signup` replaces the marketing shell with a short form: Outfit display title, one email field, a trial button, a login link, and a Turnstile region. The field's focus border is `rgb(56, 152, 236)`. Nothing was typed or submitted. Google and Apple are not on this page.

Screens: [signup-light-wall](screenshots/signup-light-wall.png), [mobile-signup-light-wall](screenshots/mobile-signup-light-wall.png).

The app login URL is a separate wall (email, password, Google, Outlook, SSO). It was not captured in this pass. The earlier probe recorded the controls and did not submit a password.

## Phone fold

At 390 the header is 76px tall with 20px padding. The link row is gone. `.menu-button-2` (36px) opens an overlay whose links are 20px DM Sans, 51px tall. Focus on those links uses an amber ring (`rgb(229, 151, 0)`), not the desktop blue ring. Start for Free stays in the header, outside the overlay.

Screens: [mobile-home-light-default](screenshots/mobile-home-light-default.png), [mobile-home-light-menu](screenshots/mobile-home-light-menu.png), [mobile-pricing-light-default](screenshots/mobile-pricing-light-default.png), [mobile-blog-light-default](screenshots/mobile-blog-light-default.png), [mobile-compare-light-default](screenshots/mobile-compare-light-default.png).

## Not a pattern here

The signed-in daily planner (tasks, calendar, focus mode, settings) is behind login. App colour tokens in `light.app` and `dark.app` describe the embedded demo stylesheet. They are not a captured app screen.
