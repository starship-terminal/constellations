# Anthropic patterns

How the measured components combine into the public pages. Values are tokens from [tokens.json](tokens.json); the components behind them are in [components.md](components.md).

## The shared shell

Every page on www.anthropic.com and claude.com runs the same chrome on the `light.page` ivory ground:

- An 84px bar (`core.layout.nav-height`): serif wordmark left, 15px section links (`light.text.secondary`, ink at hover), then two pills — the Search ⌘K pill and the 28px `light.button.pill-*` "Try Claude" CTA, both `core.radius.pill` ivory-on-ink-border pills that invert to ink on hover. See [nav-bar](components/crops/nav-bar-default.png), [nav-cta](components/crops/nav-cta-default.png).
- The nav's dropdown opens on click: a `light.surface-raised` white panel, `core.radius.md`, `core.shadow.lg`. See [home-light-nav-research](screenshots/home-light-nav-research.png).
- The footer is full-bleed `light.sheet.bg` ink: ivory link columns, a `light.footer.input-bg` prompt bar with `light.footer.input-border` border and a `light.button.clay-*` Send, then the legal row. See [footer](components/crops/footer-default.png).

## The serif hero page

The marketing pattern: an `core.typography.display`/`headline` serif line on the ivory ground, one `light.button.primary-*` ink CTA (radius 10, 12/24 padding), then big quiet cards. The home hero is ~41px at 1440 because claude.com's clamp() fluid scale lands between the marketing px steps — and it is a mixed face: the h1 is anthropicSerif while its lead line inside renders anthropicSans 600 at the same size (the 390 hero reads the same). See [hero-title](components/crops/hero-title-default.png), [hero-cta](components/crops/hero-cta-default.png), [home-light-full](screenshots/home-light-full.png).

## Card indexes

Index pages are grids of quiet cards: news and engineering cards are hairline-framed on ivory; research cards sit on ink-tinted media with `light.text.inverse` type; the product page's media cards are `light.surface-sunken` at `core.radius.2xl` (19px). See [news-card](components/crops/news-card-default.png), [research-card](components/crops/research-card-default.png), [product-card](components/crops/product-card-default.png).

## The pricing page

A serif title, then the `light.tab.*` segmented control: `light.tab.track` pill at radius 16 holding `light.tab.fg` tabs and a `light.tab.selected-*` white segment at radius 12. Below, `light.surface-raised` plan cards at `core.radius.xl` (24px) with `light.button.primary-*` CTAs, the `light.switch.*` batch toggle, and `faq-item` rows (serif 19px questions, hairline separated). The 2026-11-21 refresh did not recapture claude.com/pricing. The crops remain from 2026-11-09: [plan-tabs](components/crops/plan-tabs-default.png), [batch-toggle](components/crops/batch-toggle-default.png).

## The sales form

claude.com/contact-sales: a ~755px column of `light.field.*` rows — `core.radius.lg` (16px) ivory fields padding 16/24, whose border steps `light.field.border` → `light.field.border-focus` under focus, a matching text area and select, and `light.radio.*` circles. The form was measured and focused on 2026-11-09, never submitted. The 2026-11-21 refresh stayed on anthropic.com and did not recapture that page. See [text-field-focused](components/crops/text-field-focused.png), [topic-radio](components/crops/topic-radio-default.png).

## The docs three-rail page

docs.claude.com is a different system on the same faces: a 56px topbar on `light.docs.page` (#fcfcfb) with product tabs, the `light.docs.field-bg` Search ⌘K field and a language picker; a 264px sidebar of 14px links with a `light.docs.nav-active` ink-tint current pill; and a ~750px reading column of `core.typography.docs-body` prose, serif titles at weight 300-520, `core.typography.code` blocks and the `light.docs.accent` method badge. Every hairline is `light.docs.border` (ink at 10%). The ⌘K dialog is `light.docs.surface` at `core.radius.md` over `core.shadow.docs-lg` plus an ink ring. In dark the same rails invert to `#151515`/`#1a1a19` with `#f0efec` text. The 2026-11-21 refresh did not recapture docs.claude.com. The dark values remain in [tokens.json](tokens.json) from 2026-11-09.

## The mobile fold

At 390 the pill bar collapses to the wordmark, a `core.radius.sm` menu button and the CTA pill; the menu opens a full-screen `light.sheet.bg` ink sheet with 30px ivory links over `light.sheet.muted` secondary text. Heroes drop to `core.font.size.body-large-1` (25px) serif and cards go single-column. See [m-nav-menu-btn](components/crops/m-nav-menu-btn-default.png), [m-nav-sheet](components/crops/m-nav-sheet-default.png), [mobile-home-light-full](screenshots/mobile-home-light-full.png).
