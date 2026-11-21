# Amie patterns

How the measured components combine on amie.so's public surface, read from
the screenshots and the component entries in [components.md](components.md).
The site paints one light theme; all values are from the light set unless noted.

## The shell

The public tree of controls is [site-tree.md](site-tree.md). A floating 59px bar on the cream ground ([home-light-default](screenshots/home-light-default.png)):
the red-dot logo, a Radix **Features** flyout button ([nav-flyout-button](components/crops/nav-flyout-button-default.png),
opened: [home-light-features](screenshots/home-light-features.png)), text links
(Pricing, Login) and the small blue Get started. At 390px the bar stays but the
links collapse — no hamburger is offered, recorded as a gap
([mobile-home-light-default](screenshots/mobile-home-light-default.png)).

## CTA vocabulary

Two button recipes repeat everywhere: the filled `--color-blue-500` (#11a8ff)
primary in semibold white — 32px nav size, 50px rounded-xl hero size
([cta-primary](components/crops/cta-primary-default.png)) — and the white
hairline ghost with the natural shadow ([cta-secondary](components/crops/cta-secondary-default.png)).
Pricing adds a third: the black 36px trial CTA
([plan-cta](components/crops/plan-cta-default.png)) next to plain white
Select rows ([plan-select](components/crops/plan-select-default.png)).

## Hero and announcement

The hero sets a large bold headline on the #fafafa cream, under it the
changelog pill — a blur-backed text link carrying the latest entry
([changelog-pill](components/crops/changelog-pill-default.png)) — then the
blue + ghost CTA pair. Section headlines stay bold at ~28px
([section-title](components/crops/section-title-default.png)).

## Pricing

The billing control is a pill segmented pair (Bill monthly / Bill yearly,
[billing-yearly-on](components/crops/billing-yearly-on-opened.png)) whose
press re-renders the plan cards. Each plan is a white bordered card with its
own CTA; below, the FAQ is a column of 68px hairline-separated Radix
accordions ([faq-question](components/crops/faq-question-default.png),
opened: [faq-open](components/crops/faq-open-opened.png),
[pricing-light-faq](screenshots/pricing-light-faq.png)).

## Docs and dialogs

Documentation adds a left sidebar plus an "On this page" rail
([documentation-light-default](screenshots/documentation-light-default.png)).
Watch demo opens a scrimmed dialog over a feature page
([features-notes-light-demo](screenshots/features-notes-light-demo.png)):
scrim rgba(0, 0, 0, 0.6), black panel, 16px radius.

## Forms

The contact page stacks 54px rounded-12px fields
([contact-field](components/crops/contact-field-focused.png)) — focused
only, nothing typed. Download carries the platform buttons
([download-button](components/crops/download-button-default.png),
[download-light-default](screenshots/download-light-default.png)) — measured,
never pressed.

## Footer

A wide link grid on the same cream: three columns of product links
(Blog/Templates/MCP/Routines), a company column (Contact us, Download,
Affiliates), the socials (LinkedIn, Instagram, x.com) and the legal row
([footer-link](components/crops/footer-link-default.png),
[footer-legal](components/crops/footer-legal-default.png)).
