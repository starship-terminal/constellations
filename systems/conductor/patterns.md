# Patterns

Public pages on conductor.build, captured 2026-11-22. The signed-in app was not entered.

## Marketing shell

A full-width announcement bar, then a dark header, then a centered hero over a starfield. The hero headline is 36px sans weight 600. The body under it is mono. The primary action is a light pill on the dark page.

[screenshots/home-dark-desktop.png](screenshots/home-dark-desktop.png)

At 390 the header collapses to the mark and Open menu. The hero headline wraps and the Get Conductor pill goes full width.

[screenshots/home-dark-phone.png](screenshots/home-dark-phone.png)

## Docs shell

Docs use a left sidebar and a prose column. The same `html.dark` / `html.light` switch paints the page. The sidebar is the product's public documentation, not the signed-in app.

[screenshots/docs-dark-desktop.png](screenshots/docs-dark-desktop.png)

## Auth wall

Sign in and Sign up are the same layout: mark, title, three identity-provider buttons, a quieter "Other sign-in options" line, and a switch to the other wall. A quote card sits under the form. No field was filled.

[screenshots/login-wall-dark-desktop.png](screenshots/login-wall-dark-desktop.png)

[screenshots/signup-wall-dark-desktop.png](screenshots/signup-wall-dark-desktop.png)

## Empty, loading, error

The public changelog, docs, blog, brand kit, privacy, and terms pages all had content. No public empty, loading, or error state was shown. The signed-in empty states were not reached.

## Theme

Dark is the default on this machine's colour scheme. Light follows `prefers-color-scheme: light` and swaps `html` from `dark` to `light`. There is no theme toggle on the marketing header.

[screenshots/home-light-desktop.png](screenshots/home-light-desktop.png)
