# Meta AI patterns

The signed-out product is one long page at `https://www.meta.ai/`. The document itself does not scroll. A `div` with classes `h-full overflow-y-auto` scrolls: 6034 px tall at 1440 by 900, 7523 px tall at 390 by 844.

## App shell

A left sidebar and a top-right pair of pills frame the page. The sidebar is 56 px when collapsed and 256 px when open. The page background and the sidebar background are both `#181819`. At 390 px the header pills still sit on one row: Download app at x 174, Log in at x 303. The hero and composer reflow: the h1 drops from 48 px to 28.08 px and its width becomes 342 px.

## Composer

The hero heading sits above a 768 px composer. The field's accessible name is "Ask Meta AI". Attach and Send are icon buttons inside the shell. Send stays disabled and at opacity 0.5 while the field is empty. This capture did not type into the field and did not send.

## Feature sections

The scroller holds eight headings, in order:

1. Describe the image you want
2. Edit photos with ease
3. Discover and shop products that match your style
4. Find the best spots around you
5. Go deeper with research
6. Stay connected to your business
7. Write the caption, plan the post
8. Ready to try Meta AI?

Each section pairs a 30 px title with a short paragraph, a pill button, and a published demo (an image, a chat bubble, or a product card). Those demos are marketing, not a signed-in thread.

## Auth

`Log in` leaves `www.meta.ai` for `auth.meta.com`. The first card offers Continue with Facebook, Continue with Instagram, and "Use mobile number or email address". The email step is a single field plus Continue. This capture opened that step, focused the field, and stopped. No address was typed and Continue was not pressed. The card is light (`#ffffff`) on a white page, with 16 px radius controls. It does not use the product page's dark tokens.

## Footer

Two text links, Muse and AI Learning Hub, sit at the bottom in secondary text, 16 px semibold, no underline.

## Not on this surface

Search, a data table, onboarding, a destructive confirm, toasts, and empty or error states of a conversation were not on the signed-out page. The settings gear did not open a menu.
