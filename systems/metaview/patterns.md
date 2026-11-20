# Patterns

Public marketing on www.metaview.ai, plus the signed-out auth screens on app.metaview.ai. Captured 2026-11-19 at 1440x900 (desktop) and 390x844 (phone). Marketing has one theme. The app has light and dark.

## Marketing shell

A black announcement bar, then a white header, then a long single column. The home hero is a two-column split: a headline and two pills on the left, a photograph on the right. Later sections alternate white and a deep green (`rgb(10, 33, 25)`, `--mv-color-dark-color`).

![Home](screenshots/home-light-default.png)

The phone home keeps the announcement and stacks the headline over the photograph.

![Home, phone](screenshots/mobile-home-light-default.png)

## Product page

Sourcing, Screening, Notes, Reports and fillmore share the marketing shell and a product headline. Each is a long sales page, not the app.

![Sourcing](screenshots/sourcing-light-default.png)

![fillmore](screenshots/fillmore-light-default.png)

## Pricing

A mint page (`--mv-color-light-lime1` family) with a plan-family switch and four cards: Free, Pro, Max, Enterprise. Prices are published on the page ($0, $60, $300, tailored).

![Pricing](screenshots/pricing-light-default.png)

## Demo

Book a demo is a public form page. It was captured. It was not submitted.

![Demo](screenshots/demo-light-default.png)

## Sign-in

The app auth screen is a centered card on a flat page, with Google, Microsoft, an email field and a theme switch. Headless Chromium opened it in light. The preview browser opened it in dark, and setting `data-theme="dark"` reproduces that sheet. Neither path asked for a card, a phone number or a government id. The email field was left empty.

![Sign in, light](screenshots/auth-signin-light-default.png)

![Sign in, dark](screenshots/auth-signin-dark-default.png)

Sign-up is a split page: the form on a pale mint field, a dark panel on the right.

![Sign up](screenshots/auth-signup-light-default.png)

## What the signed-in app would add

The workspace behind auth (candidate lists, interview notes, reports, settings) was not opened. Those patterns are a gap, not a guess.
