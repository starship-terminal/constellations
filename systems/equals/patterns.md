# Equals patterns

How the measured components combine on each captured surface. Every value cited is in [tokens.json](tokens.json); the components are in [components.md](components.md) and the full-page evidence in [screenshots/](screenshots).

Equals paints **three distinct public surfaces**: the marketing site on equals.com (light only, themed per page by `.accent--*`/`.label--*` body classes), the signed-out sign-in card on go.equals.com (light only, its own app palette), and the Mintlify docs on docs.equals.com (the one real light/dark switch, on `html.dark`). The spreadsheet workspace behind login was never reached; the "workbook" on the marketing pages is a demo mockup, not the app.

## Marketing chrome (equals.com, light)

The 52px header (`core.component.header-height`, matching declared `--header-height`) sits on the cream field (`light.marketing.surface` → `color.brand.grey-1` `#faf9f5`) with the ~108px wordmark, 14px Unica77 nav links (`light.marketing.text` → `color.brand.black`), the Use-cases mega-menu trigger and a Sign-in link. Hovers underline via a `text-decoration 0.1s ease-out` transition (the `mkt-nav-link` reading in components.md; `core.motion.control` is the CTAs' `background-color 0.15s ease-out`); keyboard focus draws the browser's default `1px auto #101010` ring, which has no product token (it is listed under `_gaps` in raw/component-tokens.json).

The hero sets "What's after Excel?" in Serrif Condensed at 110px/110px with -2.2px tracking (`core.font.family.serif-condensed`, `core.font.size.display`, `font.tracking.display`), a 24px/32px Unica77 lede, then the email capture: a 56px pill field (`core.component.hero-field-height`, `radius.cta`) whose placeholder is 60% black (`light.marketing.muted` → `color.brand.grey-5`), beside the 44px orchid CTA (`light.marketing.accent.orchid.background` `#b074ce`, `radius.cta` 60px). The CTA lifts to a darker accent mix on hover (`light.marketing.action.hover`) and draws an inset shadow when pressed (`core.shadow.pressed`).

Sections below run on the same field: an eyebrow label in Aeonik Fono 14px at the page's `--section-label-color` (`light.marketing.label.<name>` — `#ff3716` amber on the home page), a 48px/50px Serrif section heading (`core.font.size.section`), persona tabs (`build-tab`, ~402x129) and the animated workbook mockup (`wb-mockup`, 980x640 on a 12px radius with ring+drop shadows — a marketing demo of the product's look).

## Per-page accent themes

Every marketing page carries `.accent--<name>` and `.label--<name>` on the body; the classes resolve `--accent-background`, `--accent-light-background` and `--accent-color` (text on the accent) plus `--section-label-color`. Resolved values live under `light.marketing.accent.<name>.{background,light,on}` and `light.marketing.label.<name>`: orchid `#b074ce` on black, green `#20a277` on white with an `#85fac1` wash, amber `#ff3716` on white with `#ffcc91` wash, blue `#0000bb` on white with `#c4f2f7` wash, purple `#611848` on white, black on white. The same nine hues are the `core.color.brand.*` scale.

## The mega-menu and the drawer

The Use-cases trigger opens a ~634x360 mega-menu (`light.marketing.menu-surface` → `color.brand.white`): 12px radius (`radius.card`), a three-layer shadow (`core.shadow.menu` — a 0.5px ring plus two drops), items on 6px radius (`radius.small`) with a 5%-black hover wash (`light.marketing.menu-hover` → `color.brand.grey-2`). It animates `opacity/transform` over `0.16s cubic-bezier(0.16,1,0.3,1)`. On the phone the 40px hamburger (`core.component.hamburger`) opens a full-width drawer instead (`m-drawer`).

## Pricing

/pricing keeps the marketing chrome and lays out ~421x569 plan cards (`core.component.plan-card-width`, 32px padding) on the cream field — they read as cards by layout and feature rows, not a contrasting fill (`light.marketing.card` resolves to the same `color.brand.grey-1`). The plan name sets small, the price in Serrif 48px/52.8px, and each card's action is a 42px pill (`core.component.plan-cta-height`): black `color.brand.black` or the orchid accent. The FAQ accordion draws 10%-black hairlines (`light.marketing.line`) and opens on its question row.

## Sign in (go.equals.com, light)

The app serves one signed-out card centred on the `#fcfcfc` canvas (`light.signin.canvas` → `color.app.background`), in neue-haas-unica:

```
+--------------------------------------------------+
|              .              .                    |
|   Sign in to Equals        <- 300px card         |
|   subheading copy                                 |
|   +------------------------------------------+   |
|   | (empty field)          <- 30px #f5f5f5   |   |
|   +------------------------------------------+   |
|   +------------------------------------------+   |
|   | Continue               <- 27px #7c3aed   |   |
|   +------------------------------------------+   |
|   footer links · grey-500                     |
+--------------------------------------------------+
```

- Card (`core.component.signin-card-width` 300px): heading ink black (`light.signin.heading`), 12px copy in app greys.
- Field (`core.component.signin-field-height` 30px, `radius.field` 8px): `#f5f5f5` fill (`light.signin.field` → `color.app.grey.100`), `#a3a3a3` placeholder (`light.signin.placeholder` → `color.app.grey.400`), `#262626` text (`light.signin.text` → `color.app.grey.800`); on focus it draws a purple border (`light.signin.focus` → `color.app.purple.600`).
- Submit (`core.component.app-submit-height` 27px, same 8px radius): `#7c3aed` purple-600 (`light.signin.action`) lifting to `#6d28d9` purple-700 on hover (`light.signin.action-hover`), white text (`light.signin.on-action`). Measured, never submitted.
- Footer copy paints `#737373` grey-500 (`light.signin.muted`).

## Docs shell (docs.equals.com, light and dark)

The Mintlify docs are the one surface that truly switches themes. Light: a white canvas (`light.docs.surface` → `--background-light`) with a 288px rail (`core.component.docs-sidebar-width`) hairlined at grey-100; dark: `#0b0a0f` (`dark.docs.surface` → `--background-dark`) with a 10%-white hairline (`dark.docs.line`).

```
+----------+------------------------------------------+
| logo     |  search pill 36px · theme · assistant    |
+----------+------------------------------------------+
| 288px    |  h1 36/40 Inter 600                      |
| nav      |  paragraphs · links in #7839e5           |
| 32px     |  code blocks, Paper Mono                 |
| rows     |                                          |
+----------+------------------------------------------+
```

- Search (`core.component.search-height` 36px, `radius.pill` 9999px): a 3%-ink wash (`light.docs.field`) / 3%-white on dark (`dark.docs.field`); keyboard focus draws the primary outline (`light.docs.focus`/`dark.docs.focus` — `1px auto #7839e5`).
- Nav items (`core.component.nav-item-height` 32px, `radius.small` 6px): the active row paints a ~10% primary wash (`light.docs.nav-hover`, `dark.docs.nav-hover`).
- Text: 36px/40 weight-600 Inter headings (`light.docs.text` → `color.docs.gray.900` / `dark.docs.text` → `color.docs.gray.200`), 18px/28 body (`docs.body-text` → grey-700 / grey-400), links and the active nav in `#7839e5` (`docs.primary` → `--primary`).
- Code blocks: Paper Mono 14px/21px on a 6px chip — near-white fill light (`light.docs.code-bg`), 5%-white dark (`dark.docs.code-bg`). The `--twoslash-*` syntax palette flips with the theme (`docs.twoslash.*` in both sets).
- The theme button (`core.component.theme-button` 30px) opens a menu; the capture's dark evidence came from applying `html.dark` in the probe context, not from clicking it.

## Mobile (390px)

The phone keeps the same cream marketing surface: a 53px header (`core.component.mobile-header-height`) with wordmark and the 40px hamburger, the hero display dropping to 48px (`core.font.size.mobile-display`), and the 52px email pill (`core.component.mobile-field-height`). The drawer replaces the mega-menu. No separate mobile token set — the light set resolves unchanged.

## Motion and focus

Marketing controls transition `background-color`/`text-decoration` over `0.1s-0.15s ease-out` (`core.motion.control`, matching the declared `--default-transition-duration` 150ms); the mega-menu uses the `0.16s cubic-bezier(0.16,1,0.3,1)` entrance. The docs sidebar animates `rotate/scale/transform/translate` over `0.1s cubic-bezier(0.4,0,0.2,1)` (the mobile rail slide). Focus is an outline treatment everywhere public: `1px auto #101010` on marketing and the sign-in card, `1px auto #7839e5` on the docs controls — declared `--default-transition-timing-function` is `ease-out` (`core.motion.easing`).
