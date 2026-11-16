# Glorify patterns

How the measured components combine on each captured surface. Every value cited is in [tokens.json](tokens.json); the components are in [components.md](components.md) and the full-page evidence in [screenshots/](screenshots).

## Marketing chrome (light)

The 64px top bar (`core.component.topbar-height`) floats over every marketing page: the Glorify wordmark (`mkt-logo`), the "Who is it for?"/Features/Resources/Templates dropdowns, a plain Pricing link (`nav-link`), a ghost Login (`nav-login`) and the solid "Play for free" button (`nav-play`, the same fill and 119x42 box the hero CTA paints). On /pricing the header carries a wider "Get Started Now" CTA instead (`nav-cta`, 188x42, `light.action.cta-fill`).

The Features nav item opens a hover dropdown listing the feature pages — a local UI toggle measured open, never followed ([home-light-features-menu](screenshots/home-light-features-menu.png)).

## Marketing hero and sections (light)

The home hero is an 838px measure of display type (`hero-h1`, `core.font.family.display`, `core.font.size.hero`) over a 432px subline (`hero-sub`) and an outlined "Play for free" ghost on the dark band (`hero-cta`, transparent `light.action.hero-cta-fill` with the 1px `light.action.hero-cta-border` stroke and white ink, `radius.cta`). Below the fold the page alternates h2 section headings (`home-h2`, `core.font.size.h2`) with feature cards (`home-card`, 252x257), "Learn more" links, a FAQs strip and the sitemap footer (`footer-col`, `footer-link`).

## Pricing (light)

/pricing centers the billing switcher — two leaf labels, Monthly and Yearly (`bill-monthly`, `bill-yearly`), whose click is a Framer variant swap measured as `opened` — over the plan row: three "Card/Card Plans Free" cards ~230x154 (`plan-card`, `light.surface.card`, `radius.card`) each carrying a price figure (`plan-price`, `core.font.size.planName`), a feature list (`plan-row`) and a "Start … Trial" action (`plan-cta`, `core.component.plan-cta-height`). Trial CTAs point at /dashboard/register; they were measured in every state, never followed — no trial was started. A "Compare Plans" table sits under the cards (`compare-h2`).

## Feature pages (light)

/features/background-remover and its siblings repeat the marketing shell with a 568px display heading (`feat-h1`, `core.font.size.display`), a filled "Get Started Now →" action (`feat-cta`, 178x48 on the same blue as `light.action.cta-fill`), benefit cards (`feat-card`, 1200x572) and long-form prose (`feat-prose`, `core.font.family.body`). /templates is a draggable marquee canvas of template tiles (`tpl-card`) with category pills (`tpl-cat`); /template-marketplace pairs filter pills (`mk-tag`) with real 384x256 template cards (`mk-card`); /learn is the article hub — "All" category pill (`learn-cat`), 384x434 article cards (`learn-card`) with category tags (`learn-tag`).

## The dark app shell (signed out)

app.glorify.com paints its own vocabulary — the `app` token set. /welcome redirects to /dashboard/login: a 576px dark panel holding a 352x384 sign-in card (`login-card`, `app.surface.card`) with the "Sign in to your account" title (`login-title`, `app.text.ink`), e-mail and password fields (`login-field`, `login-pass`, `app.surface.field-bg`, `app.border.field-focus`), a Remember-me/Forgot-password row (`login-forgot`, `app.text.link`), a primary submit (`login-submit`) that sits on `app.action.primary-fill-disabled` until both fields validate — the enabled fill is `app.action.primary-fill` — and a Google OAuth button (`login-google`, `app.action.oauth-fill`). /dashboard/register repeats the card with a name field, terms links and the same OAuth row. The fields were typed into and cleared; the submits were measured in every state, never clicked.

## The anonymous editor (signed out)

"Play for free" opens /designer/use-template/0, which creates an anonymous scratch file at /file/<id> — the product's own public demo path. It paints two layers:

- **Onboarding**: the "Generate designs for your campaign" upload screen (`ob-title`, `app.text.body`) — a drag-and-drop zone (`ob-drop`, never fed), the "Try with Placeholder Image" card (`ob-ph`) and an "I'll get started on my own" link (`ob-own`, which bounces to registration signed out).
- **Editor chrome**: a 56px top bar (`ed-header`, `app.surface.chrome-fill`) with Login/Signup (`ed-login`, `ed-signup` on `app.action.signup-fill`), zoom (`ed-zoom`), Share and Download (all measured, never pressed); a 68px left rail of 48x48 `.dropdown-toolbar` tools (`ed-tool`, the Pointer active on `app.action.tool-fill-active`); and the 280x824 right inspector (`ed-inspector`, `app.surface.inspector-fill`) with EDIT/LAYERS/PAGES tabs (`ed-tab`, `ed-tab-layers`) and the page-background hex field (`ed-color`).

Choosing "Try with Placeholder Image" opens the **Craft dialog** (`ed-craft`, 792x640 `app.surface.dialog-fill`, `radius.dialog`): a brand-name textarea (`ed-craft-field`), a product-description textarea (`ed-craft-area`), a style grid whose "Modern" card selects with `app.border.style-selected-border` (`ed-craft-style`), a Replace button on the image pane (`ed-replace`) and "Add to canvas" (`ed-add`) — disabled (`app.action.craft-cta-disabled`) until a style is picked, then enabled (`app.action.craft-cta-fill`). The button was never pressed; the dialog's own close is `ed-close`.

## Mobile (390px)

The marketing site collapses to a 64px top bar (`m-topbar`) carrying the wordmark and the 60x60 burger (`m-burger`) that opens the full-width "Menu" overlay (link row `m-menu-link`, [mobile-home-light-menu](screenshots/mobile-home-light-menu.png)). The hero re-types to 350px (`m-hero-h1`, `core.font.size.mobileHero`) over the same outlined ghost CTA (`m-hero-cta`, `core.component.mobile-cta-height`) — transparent fill with a 1px stroke, blue rather than desktop's white. The app login card renders the same dark theme at 390 wide ([mobile-login-app-default](screenshots/mobile-login-app-default.png)).

## Motion and focus

Marketing controls transition on hover (`core.motion.control` — the measured nav-link transition). Keyboard focus paints an outline on marketing controls where the browser draws one (`light.border.focus-ring`); the reduced-motion probe is recorded in `raw/components-computed.json` `_meta.reducedMotion`. On the dark app surface, field focus is a border treatment (`app.border.field-focus` on `login-field focused`).
