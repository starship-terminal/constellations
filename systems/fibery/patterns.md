# Fibery patterns

How the measured components combine on each captured surface. Every value cited is in [tokens.json](tokens.json); the components are in [components.md](components.md) and the full-page evidence in [screenshots/](screenshots). Fibery paints one light theme signed out — a warm paper palette — so every pattern below is the same `light` set.

## Marketing chrome

A fixed 88px bar (`component.header-height`) on the warm `light.fibery.menu.bg.color` #fff5e8 field carries the 127px Fibery wordmark (`component.logo-width`), the nav — Solutions, Platform and the other HeaderMenuItem triggers as 34px pills (`component.nav-item-height`, `core.font.size.nav` 16px at `core.font.weight.nav` 500) — and, on the right, the text "Log in" link plus the dark "Sign up for free" FiberyButton (40px, `component.nav-button-height`, `light.action.ctaFill` #251d1a inked `light.action.ctaInk` #faebd6). Hovering a menu trigger opens the dropdown panel — a 740 x 383 cream card (`component.dropdown-width`/`height`, `core.radius.menu` 12px) of MenuItem tiles with icons and descriptions; it opens on pointer hover, a local UI toggle, and its links were never followed.

## Home (light)

The home page sits on `light.background.page` — the "soup" #faebd6 field that is Fibery's signature. The hero stacks a small announcement pill (`announce-bar` — the "Spill the tea" blog link, a bordered lozenge), a 64px/800 Suisse Intl display headline (`core.font.size.display`, `core.font.weight.display`), an 18px lede (`core.font.size.lede`), then the paired CTAs: the solid dark "Sign up" and the outlined "Book a Demo" ghost (`light.border.ctaOutline`), both 40px pills (`component.hero-cta-height`, `core.radius.pill` 6px). Beside them the `product-frame` — an 855 x 481 product video mock — is marketing content, not the signed-in app. Section headings further down step to `core.font.size.h2` 48px/800. The palette is deliberately edible: `color.named.soup`, `tea`, `rusty`, `terracotta`, `mudText` — warm browns and peach tints against the near-black `color.basic.black` #251d1a ink.

## Pricing

/pricing keeps the same soup field. The `price-h1` heads a Monthly/Yearly `price-switch` — a real checkbox toggle measured in both positions (a local UI toggle; prices flip, nothing is sent) — then a row of plan tiles (`plan-card`, 282 x 559, `core.radius.card` 12px on `light.background.planTint` cream) each carrying its own `plan-cta` pill. Below, the `faq-item` accordions (73px heads, `component.faq-head-height`) open with a chevron, and the `extend-table` compares plans in a bordered grid. The `#3b758c` website/form blue (`light.fibery.business.blue.color`, `light.fibery.form.button.blue.color`) is spent on links and form-adjacent controls, not fills.

## Templates

/templates is an index of `tpl-card` tiles (271 x 436) — a rounded card holding the 36px `tpl-icon` square (a `--template-color`-tinted TemplateSingleItemIcon), the template name and a description; hovering raises the card. One template detail page was captured (`/templates/content-marketing`) with the same chrome.

## Sign-up wizard (fibery.io)

fibery.io/sign-up is the first app surface: a 560px `su-panel` (`component.signup-panel-width`) on the shared light field holding the 164px `su-field` AI prompt textarea (`component.prompt-field-height`, `light.background.field` white, `light.text.fieldInk`), the premade-solution chips (`su-premade`), the step dots (`su-steps`), the "Start without AI" skip (`su-skip`) and the `su-submit` "Create workspace" pill — disabled until the prompt holds text; its enabled state was measured after typing, and the text was cleared without submitting. The wizard was never advanced past step one.

## Login (fibery.io)

fibery.io/login/ paints the same sheets on a two-panel layout: the 360px `login-panel` (`component.login-panel-width`) form column beside the `login-hint` "Did you know?" card. Inside the panel: the `login-google` and `login-ms` OAuth POST forms (36px buttons, `component.oauth-height` — measured, never pressed), the `login-email` "Continue with Email" button whose `opened` state reveals the `login-email-field` (typed into then cleared, never submitted), and the `login-sso` "Workspace SSO" link (never followed). No CSRF field was ever sent.

## Mobile (390px)

The phone surface keeps the same palette and voices: a 77px top bar (`component.mobile-topbar-height`) carries the wordmark and the 20px sandwich button (`component.mobile-menu-size`, `HeaderMainMenu_sandwichBtn`). Activating it — a local UI toggle — grows the `HeaderMainMenu_mobileMenu` drawer to a 366 x 750 cream panel (`m-drawer`) of the same nav tree plus "Sign up for free", "Log in" and "Book a demo" buttons and the collapsible menu sections. The display headline steps down to `core.font.size.displayMobile` 46px and the hero CTAs keep the 40px pill profile full-width.

## Motion and focus

Controls transition over 0.3s (`core.motion.control`, `core.motion.navItem` — the nav-link `color 0.3s` is the measured rule, matching the stylesheets' `0.3s` transitions on FiberyButton, menu links and icons). Focus is an outline ring (`light.border.focusRing` #101010) drawn on the control, measured on the header CTA, nav pills, footer links and the login buttons. The one declared shadow is `core.shadow.m` — a soft 10px/16px spread at 8% black, spent on raised cards and panels, not a multi-level elevation scale.
