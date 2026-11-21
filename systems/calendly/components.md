# Components

Public marketing components measured on calendly.com, signed out, on 2026-11-21. Crops were not cut. States are the ones visible in [screenshots/](screenshots/).

| Component | Where | States seen | Notes |
|---|---|---|---|
| Button (primary) | Header "Get started for free", login "Continue with email" | default | Midnight fill #071a31, magnolia text, 16px radius, 48px tall, 12px 16px padding |
| Button (secondary) | Header "Log In", "Talk to sales" | default | Quiet outline or text |
| Icon button | Homepage carousel previous/next, mobile close | default | |
| Link | Footer, menus, "Sign up with email" | default | |
| Text field | Login and signup email | empty, unfocused | Placeholder "Enter your email". Not filled. |
| Menu | Header Product, Solutions, Resources | closed, open (hover) | [home-light-product-menu](screenshots/home-light-product-menu.png) |
| Dialog | Login and signup cards | default | Marketing walls, not the app |
| Card | Homepage product panel, plan cards | default | |
| Badge | "Beta" on Callie | default | |
| Accordion | Pricing FAQ, homepage feature rows | closed, one open | [pricing-light-faq](screenshots/pricing-light-faq.png) |
| Tabs / carousel | Homepage product chips | default | |
| Avatar | Booking profile initials | default | [booking-light-default](screenshots/booking-light-default.png) |
| List row | Booking event row, footer columns | default | |

Not present on the captured public surface: text area (contact forms exist and were not opened), select, checkbox, radio, switch, tooltip, toast, table. The booking time-slot list and the booking form were not reached because November 2026 had no open times and the month controls were disabled.

## Gaps

- Hover, focus-visible, pressed, and disabled were not measured per control. The token file has hover fills for badges and icon buttons (`--color-iconbutton-bg-hover`, `--color-badge-*-bg-hover`).
- Loading and error states of the email walls were not triggered. Submitting the email was out of scope.
- Dark theme was not painted on any captured page. Dark shadow tokens exist and were not observed in use.
