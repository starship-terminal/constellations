# Variant live readings

Captured 2026-11-19 from the live host `https://variant.com/` (title: "Variant – Endless designs for your ideas, just scroll"). Confirmed this is Variant Design, Inc., the product the constellations manifest names ("Endless designs for your ideas, just scroll"), not a reseller.

Host confirmed: `location.host` was `variant.com`. No Cloudflare challenge. The page was complete before any reading.

## Browser

T3 preview tab `tab_6x_b476fa69-d865-4d9c-9974-6281ced1c8e8`, opened with `reuseExistingTab: false` at `https://variant.com/`.

`preview_snapshot` failed twice with: "The browser is not producing screenshot frames. For a desktop tab, show or restore the T3 Code window and try again." No screenshots were invented. Values below were read with `preview_evaluate` from the attached page (computed styles and authored CSS custom properties).

Viewport after `preview_resize` freeform 1440×900: `window.innerWidth` 1440, `window.innerHeight` 900, `devicePixelRatio` 2, `visualViewport` 1440×900 scale 1. The tool's reported viewport object said 1280×800; the page's `innerWidth` is the measurement used.

Phone pass: freeform 390×844. Page reported `innerWidth` 390, `innerHeight` 844, `devicePixelRatio` 2.

`prefers-color-scheme: light` was forced with `preview_set_appearance`. `matchMedia('(prefers-color-scheme: dark)')` then returned false. Body background stayed `rgb(34, 34, 34)` and the h1 stayed `rgb(240, 237, 229)`. The signed-out surfaces do not follow the preference.

## Surfaces opened

| URL | What it is |
|---|---|
| https://variant.com/ | Signed-out homepage. Left column (408px) plus a design grid. |
| https://variant.com/authentication | Opened by clicking "Sign up / Sign in". Not submitted. |
| https://variant.com/terms-and-privacy | Terms of Service and Privacy Policy tabs. |

Fetch of `/login`, `/signin`, `/signup`, `/pricing`, `/about`, `/blog`, `/privacy`, `/terms` from the page returned opaque redirects. Those paths were not navigated. No separate marketing, pricing, about, or blog page was found from the homepage (zero `<a>` on `/`).

## Not entered

- Email form was not submitted. The field was typed with `not-an-email` and later `a@b.co` only to read the enabled button, then cleared. No account was created. AgentMail was not used: the form is not email-only (Continue with Google is present).
- Continue with Google was not clicked (company SSO).
- Submit on the homepage composer was not clicked.
- Add image and Select style were not opened (file picker and style modal).
- No payment, card, phone, or KYC field appeared on the signed-out pages. Billing colours exist only as unused CSS custom properties.
- Signed-in app (sidebar, chat, billing modal, style modal) was not opened. Their CSS is in the same Next.js bundles and is labelled as bundled, not live.

## Computed page ground

- `body` background `rgb(34, 34, 34)`, color `rgb(255, 255, 255)`, font `Inter, "Inter Fallback", system-ui, sans-serif`, size 16px, weight 400.
- Homepage left and right columns background `rgb(7, 7, 6)`.
- Auth page wrapper `.page_page__JR_T_` background `rgb(0, 0, 0)`.
- Off-white ink used on the homepage hero: `rgb(240, 237, 229)`, which matches authored `--homepage-offwhite: #f0ede5`.
