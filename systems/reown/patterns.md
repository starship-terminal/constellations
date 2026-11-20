# Patterns

Public signed-out pages only. Measured 2026-11-19. Screenshots are headless Playwright of pages that loaded without a Cloudflare challenge. The T3 preview tab did not produce screenshot frames.

## Marketing shell

https://reown.com/ sits on `#9a9a9a`. The header is a transparent bar, 52px tall, padding 8px. Left side is the wordmark: a black pill reading `. / reown` plus a grey plus. Right side is blue pills (Learn, Docs, Demo) and a white Log in pill. The hero is a `#202020` panel with 160px radius, white 36px KHTeka headline, `#e4e4e4` 18px lead, a blue Start building pill and a white-outline Explore Plans pill. Below that, an orange announcement at 40px radius, then coloured content cards.

Screenshot: [home-light-default.png](screenshots/home-light-default.png). Phone width 390: [home-light-phone.png](screenshots/home-light-phone.png). At 390 the nav pills collapse to a plus, and the headline stacks above the phone mock.

## Pricing

https://reown.com/pricing sets `body` class `dark` and paints `#363636` with white text. Three plan cards: Starter on `#202020`, Pro inside a `#0988f0` ring, Growth inside a `#18ac65` ring. Prices are 40px KHTeka. A blue-tinted banner sits above the cards.

Screenshot: [pricing-dark-default.png](screenshots/pricing-dark-default.png).

## FAQ

https://reown.com/faq keeps the grey marketing page. A black pill reads FAQ. Rows are black 16px-radius accordions. One row was opened.

Screenshot: [faq-light-default.png](screenshots/faq-light-default.png).

## Blog

https://reown.com/blog/why-choose-reown-for-web3-app-analytics pairs a grey info card (radius 64px) with a `#e9e9e9` article card (radius 88px, padding 40px). Body copy is `#383838` 16px / 24px, measure about 662px.

Screenshot: [blog-light-default.png](screenshots/blog-light-default.png).

## Docs

https://docs.reown.com/ is a separate shell. Dark is the default: Inter, header bar `#202020`, h1 `#dee2e0` at 36px weight 600, green `#008847` for the active item and the AppKit Demo pill. A theme menu offers System, Light and Dark. Light was measured, then dark was restored.

Screenshots: [docs-dark-default.png](screenshots/docs-dark-default.png), [docs-light-default.png](screenshots/docs-light-default.png).

## Contact

https://reown.com/contact is another grey page with a black hero. Department links and a newsletter field sit lower on the page. The form was not submitted.

Screenshot: [contact-light-default.png](screenshots/contact-light-default.png).

## Sign-in wall

https://cloud.reown.com/sign-in redirects to https://dashboard.reown.com/sign-in. The page is `#202020`, KHTeka, with Continue with Google, an email field, a password field, and a Sign In button at `#0989f1`. Nothing was submitted. No wallet was connected. No API key was created. No screenshot was taken of this page, because the rule forbids a new headless session against a login page, and the preview browser produced no frames.
