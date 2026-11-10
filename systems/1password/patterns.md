# 1Password patterns

How the measured components combine into the public site's screens. Every value named here is a token in [tokens.json](tokens.json); the component entries are in [components.md](components.md) and the screens in [screenshots/](screenshots).

## Site chrome

Every page hangs from the same two-strip chrome: the `component` announcement strip (`background.announcement` tan, small ink copy with a Learn more link and Sign in at the right) over `component.header` — the white `header-navigation` bar with the wordmark, the nav-group flyout buttons (Business, Personal, Developers, Partners, Resources), the Pricing link, Talk to sales and the `component.button.primary` blue pill. On mobile it collapses to a hamburger that opens `m-nav-drawer`.

- Desktop: [home-light-default](screenshots/home-light-default.png), [nav flyout](#nav-flyout)
- Mobile: [mobile-home-light-default](screenshots/mobile-home-light-default.png)

## Hero

The hero is `background.brand` — the `bg-hero-gradient-blue` navy field carrying `typography.display` (88px, weight 300, -1.76px tracking, inverse text), a 350-weight sub-line, and the hero CTA pair: a white `cta-btn` pill (primary on dark) and the bordered outline pill. The product collage and the cross-origin `video-embed` Vimeo iframe sit inside the same band.

- [home-light-full](screenshots/home-light-full.png), [hero](components/crops/hero-default.png), [hero-title](components/crops/hero-title-default.png)

## Nav flyout

The nav groups open `component.nav-flyout` on click (`header-navigation__dropdown`, `transition-all duration-300`, z under the header's 50): a 1248px panel of product and feature links in columns. Only the Business panel was measured; the other four groups behave identically.

- [home-light-menu](screenshots/home-light-menu.png), [nav-flyout](components/crops/nav-flyout-open.png)

## Plan selection

Pricing's `component.plan-selector` is a 49px-radius bordered pill pair beside `typography.title` — the same `segment-selector` control that picks the platform on the download page (`platform-pill`). The grid below is `component.product-column`s: kicker, product name, blurb, a Request a quote pill and a feature list, divided by `border.divider` hairlines.

- [pricing-light-default](screenshots/pricing-light-default.png), [pricing-light-full](screenshots/pricing-light-full.png)
- [download-light-default](screenshots/download-light-default.png), [platform-pill](components/crops/platform-pill-default.png)

## FAQ

`component.faq-row` rows toggle open to `faq-answer` bodies — the accordion pattern repeated on pricing and product pages.

- [pricing-light-faq](screenshots/pricing-light-faq.png), [faq-answer](components/crops/faq-answer-open.png)

## Forms and embeds

The contact-sales form is not painted by the site's own CSS: `component.form-embed` is a 504x915 Marketo iframe on `integrations.1passwordservices.com`, measured as a box only. The hero's `video-embed` is the same story — a 1248x702 player.vimeo.com iframe. Neither's contents are introspectable, and nothing was submitted.

- [contact-light-default](screenshots/contact-light-default.png), [contact-light-full](screenshots/contact-light-full.png)

## Sign-in boundary

The vault is credential-gated (account + secret key + master password) and `start.1password.com` redirects headless browsers to `/unsupported` — captured as `unsupported-card`, the honest edge of the public surface.

- [account-light-default](screenshots/account-light-default.png), [unsupported-title](components/crops/unsupported-title-default.png)
