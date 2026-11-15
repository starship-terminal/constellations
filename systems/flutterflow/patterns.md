# FlutterFlow patterns

How the measured components combine on the signed-out pages. Everything here was captured public, in headless Chromium at 1440 x 900 (mobile 390 x 844); the page-level geometry is in [raw/layout.json](raw/layout.json) and the components in [components.md](components.md).

## The frame every page shares

A translucent 64px bar (56px at 390) floats over the page — `color.page` at ~86% with backdrop blur, hairline under it — holding the wordmark, a nav of quiet muted links (`typography.nav`), the Product dropdown button and the Sign in + Start building pair at the right. At 390 it collapses to brand + a 36px Open menu icon button that opens a full-screen sheet ([m-menu-dialog](components.md#m-menu-dialog)). Content runs in a single `size.content` 1344px column inside `space.gutter` side margins (20-48px by width); sections are spaced by `space.section` (clamp 64-128px). The closing band and footer repeat on every page, and the footer carries the Light/Dark theme switch ([home-light-full](screenshots/home-light-full.png), [mobile-home-light-full](screenshots/mobile-home-light-full.png)).

- Layout: [home@1440](raw/layout.json) reads the bar `fixed`, content x 48, 1344 wide; at 1920 the same 1344 column centres, at 1024 it reads 976, at 390 it fills with 20px gutters.

## Prompt-first hero (home)

The home hero is the product pitch as a control: a 720px prompt composer ([composer](components.md#composer)) centred under a display headline in `typography.display` (66px at 1440, -2.31px tracking). Ghost idea text cycles inside; the previous/next idea arrows and a mono `Tab` chip sit in the field's bar with the 36px send at 8% ink — it arms to `color.send` accent blue only once text is entered. The composer was typed in and cleared, never submitted ([home-light-composer-focused](screenshots/home-light-composer-focused.png)). A slimmer 640px variant ([ff-composer](components.md#ff-composer)) recurs on later pages.

## Pricing: segment, grid, accordion

Monthly/Yearly is a 3px-padded pill segmented control whose selected cell lifts a `color.card` tile over the ring ([billing-seg](components.md#billing-seg); the Yearly state was set through the control itself, [pricing-light-billing-yearly](screenshots/pricing-light-billing-yearly.png)). Below, the plan grid is four 336px cards in the 1344 column, each a `radius.card` sheet with `space.cell` padding, ending in a 44px pill CTA — contrast fill on the featured plan, card fill with the 0.5px ring on the rest ([plan-card](components.md#plan-card), [plan-cta](components.md#plan-cta)). The FAQ is an 840px accordion of hairline-separated items; the first item ships open, and the saved shot shows the same list toggled shut through its own summary ([pricing-light-faq-closed](screenshots/pricing-light-faq-closed.png), [accordion-item](components.md#accordion-item)).

## Enterprise contact form

A two-column layout: pitch left, the 904px form card right ([contact-form](components.md#contact-form)). Fields are 44px pill inputs (`component.field`: card fill, ink-12% edge, `shadow.field`); focus adds a 4px ink-6% ring without moving the layout ([enterprise-light-field-focused](screenshots/enterprise-light-field-focused.png)). The tall "How can we help?" textarea takes `radius.field-tall` (22px); radios are 18px ink-ringed circles that fill contrast when checked; the custom select opens a 410px popup with `shadow.floating` ([select-popup](components.md#select-popup)). The submit is the standard 44px contrast pill. Nothing was sent.

## Feature tabs and disclosure

/product walks through the builder with a vertical 376px tab list on the left (quiet muted labels, selected flips to ink) and a demo panel on the right; the Backend tab was selected through the control ([product-light-tab-selected](screenshots/product-light-tab-selected.png)). Accordions (`ff-acc`) reuse the same 840px hairline-list pattern on product, pricing and Studio FAQ.

## Studio content pages

Studio pages mark themselves with the `color.studio-tint`/`color.studio-ink` tag chip ([ptag-studio](components.md#ptag-studio)) and carry showcase cards — tall `radius.card` tiles with a shot over a meta row ([showcase-card](components.md#showcase-card), [studio-showcase-light-full](screenshots/studio-showcase-light-full.png)). Feature lists use a 3-column cells grid (448px cells at 1440, [cells-grid](components.md#cells-grid)).

## Themes

The same surfaces, rebound: dark flips `color.page` to near-black, cards to #1b1b1b, ink to #ededed, accent to a lighter #5aa2f0 and every hairline to white-8% — one `data-theme` attribute on `<html>` swaps all of it ([home-dark-dark-full](screenshots/home-dark-dark-full.png), [pricing-dark-dark-full](screenshots/pricing-dark-dark-full.png)). The home page's earlier skin tracks its own `legacy.*` aliases to the same values, so the two generations of the site theme together.
