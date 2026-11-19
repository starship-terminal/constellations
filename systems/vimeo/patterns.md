# Patterns

## Marketing page

`https://vimeo.com/solutions/marketing` is a light marketing page. At 1440 the header is a fixed 84px bar: wordmark, text menus, Contact sales, a cyan Join button, and icon buttons. The hero is an eyebrow in ABC Repro Mono, a 72px heading, an 18px muted paragraph, and a cyan Start for free button. Page background computed as `rgb(250, 252, 253)`.

Screenshots: [screenshots/marketing-light-desktop.png](screenshots/marketing-light-desktop.png) (1440 by 900, dpr 1 in the file), [screenshots/marketing-light-phone.png](screenshots/marketing-light-phone.png) (390 by 844). At 390 the menus collapse into a bottom bar (Menu, Upload, Staff Picks, Watch) and a cyan Join for free chip.

## Watch feed

`https://vimeo.com/` redirects to `https://vimeo.com/watch` for a signed-out visitor. The page background is `#f6f8fa`. A left nav lists Explore, Staff Picks, Feed, Channels, Categories, Groups, and On Demand. The top bar has search, Pricing, Log in, and Join. Category chips sit above video cards. This is the public feed, not a signed-in library. No screenshot: the preview browser did not produce frames.

## Pricing

`https://vimeo.com/upgrade-plan` uses the app token set (`chakra-ui-light`, page `#f6f8fa`). A yearly/monthly switch sits above white plan cards. Trial buttons are the cyan brand control. Prices in this session were in Singapore dollars and are not part of the system. No card was entered.

## Login

Log in opens a dialog, and `https://vimeo.com/login` redirects to `https://vimeo.com/log_in`. The form is Continue with Google, Facebook, or Apple, then an email field and Continue with email. That is not an email-only form, so no address was entered and no account was created. A hidden Stripe iframe was present in the page; it was not a checkout and nothing was submitted.
