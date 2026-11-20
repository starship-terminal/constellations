# Patterns

stage.so no longer serves the Stage design product. The public URL is one Spaceship listing. There is no signed-out app shell and no login route on this host.

## Listing

At 1440 the page is a split. A navy field (`#171f66`) carries a cover SVG and two radial gradients (violet `rgba(144, 56, 255, 0.55)` and brand `rgba(57, 78, 255, 0.5)`). The left column holds the eyebrow, the domain name, three feature lines, and "Listed with spaceship.com". The right column is the white purchase card: kicker, Buy now at $3,900, Make offer, payment marks, and Next. A benefit row and a translucent footer sit below.

![Desktop listing](screenshots/listing-desktop-default.png)

At 390 the same content stacks. The kicker is hidden. The card radius drops to 8px. The domain name stays 48px.

![Phone listing](screenshots/listing-phone-default.png)

## What is not here

No marketing page for the old Stage product, no app chrome, no form with a validation error, no empty or loading state, no destructive confirm, no search, no list, no onboarding. Next leaves this host for spaceship.com checkout. That URL was not opened.
