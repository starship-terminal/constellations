# Voicenotes patterns

Public pages only. Viewport 1169 by 731. No screenshots: the preview browser did not produce frames.

## Marketing home

`https://voicenotes.com/`. Fixed header, 70px, page colour at 95% opacity. Wordmark, Download, Enterprise, Pricing, Resources, Log in, then a lined "Book a demo" and a filled "Start for free".

Hero heading is P22 Mackinac. At this width it computes to 48px, not the 60px in the class. Section headings are Instrument Serif at 60px, colour `#222222`. Body lede is Inter Regular 18px / 28px.

The page includes a product demo (Notes, Ask AI, a sample meeting). That demo is marketing content, not the signed-in app.

## Pricing

`https://voicenotes.com/pricing`. Mackinac title, a Monthly / Annual pill, four plan cards (Free, Pro, Business, Enterprise). Pro's "Get started" is the filled button. The others are the sand quiet button. A compare section and an FAQ accordion sit below. "Talk to sales" does not open a card form on this page.

## Login

Log in opens a modal on the marketing origin. First step: Welcome back, Continue with Google, Microsoft, Apple, Email, Twitter, and SSO. Email reveals email and password fields plus Continue. Sign up links to `/signup`. The form asks for a password, so it was not submitted. SSO, Google, Apple, Microsoft and Twitter were not clicked.

## Enterprise

`https://voicenotes.com/enterprise`. Instrument Serif title, then a Typeform iframe (`typeform.com/meetvoicenotes`). The form was not filled.

## Blog

`https://voicenotes.com/blog/` is a separate template: Inter for UI, "P22 Mackinac Pro" with a Georgia fallback for the 80px title, black pill "Try Voicenotes". A post uses 56px Mackinac for the title, Inter 24px / 32px for h2, and `#0088FF` underlined links.

## Reviews

`https://voicenotes.com/reviews`. Inter SemiBold 24px / 32px heading, "Loved by 850,000+ note-takers." Log in and Sign up are 14px, 8px radius, and also open in place (`javascript:void(null)`).

## Not captured

Signed-in app shell, empty, loading and error states, destructive confirmation, search, onboarding, and any payment or checkout. Phone layout was not measured.
