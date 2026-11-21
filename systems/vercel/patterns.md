# Vercel patterns

Public pages only. Signed out. 2026-11-21.

## App shell

Desktop: a short header with two menu buttons, two destination links, and
three actions on the right. The primary action is the filled Sign Up.
The page sits on `#fafafa` in light and `#000000` in dark.

Phone: the header collapses to the mark and one "Open menu" button. The
drawer holds the same destinations as stacked rows and full-width actions.

Screenshots: [home-light-desktop.png](screenshots/home-light-desktop.png),
[home-dark-desktop.png](screenshots/home-dark-desktop.png),
[home-light-phone.png](screenshots/home-light-phone.png),
[home-dark-phone.png](screenshots/home-dark-phone.png).

## Marketing page

The homepage hero is a 64px weight-400 headline, a triangle mark, three
short lines, and two actions ("Deploy now", "Talk to sales"). A logo row
sits at the bottom of the first screen. The triangle is a public demo of
the mark, not a signed-in dashboard.

## Pricing

[pricing-light-desktop.png](screenshots/pricing-light-desktop.png) and
[pricing-dark-desktop.png](screenshots/pricing-dark-desktop.png). Phone:
[pricing-light-phone.png](screenshots/pricing-light-phone.png). Plan buttons
were not followed. No card was entered.

## Docs landing

[docs-light-desktop.png](screenshots/docs-light-desktop.png) and
[docs-dark-desktop.png](screenshots/docs-dark-desktop.png). The landing is
public. Inner doc pages were not walked.

## Login and signup walls

[login-light-desktop.png](screenshots/login-light-desktop.png) is an empty
email field plus provider buttons. Stopped there.

[signup-light-desktop.png](screenshots/signup-light-desktop.png) is a card
of provider buttons and no email field. "Show other options" stays on the
same page: [signup-other-light-desktop.png](screenshots/signup-other-light-desktop.png).
Stopped there.

## Empty, loading, error

The login field's empty state is the placeholder. A validation error was
not triggered, because that would mean submitting the form. A loading state
was not shown. The domains empty state from an older signed-in walk was
removed in this refresh.

## Theme

The footer labels system, light, and dark are the theme control. Dark is a
real class on `html`, not a reconstructed stylesheet.
