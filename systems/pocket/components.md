# Components

Pocket’s public site on 2026-11-19 is a shutdown notice. The only controls on the page are a secondary link styled as a button, footer links, and a language select. Privacy and terms both return the same error page, which adds one primary button. Everything else in the checklist is a gap.

Crops are 2x, taken from the live page.

## Button

The shutdown page’s “Additional details” link uses `a.button.secondary.large`. Rest is white with a 1px `#1a1a1a` border, 8px radius, 20px Graphik Web, padding 16px 24px. Hover fills `#1a1a1a` and sets the label to `#f2f2f2`. Focus-visible draws a 1px `#009990` outline, 1px outside the border.

![Secondary button](components/crops/button-secondary-default.png)

![Secondary hover](components/crops/button-secondary-hover.png)

![Secondary focus](components/crops/button-secondary-focus.png)

The error page’s “Contact Support” link uses `a.button.primary.large`. Rest is `#008078` with white text. Hover is `#004d48`. Focus uses the same teal outline.

![Primary button](components/crops/button-primary-default.png)

![Primary hover](components/crops/button-primary-hover.png)

![Primary focus](components/crops/button-primary-focus.png)

Disabled, pressed, loading, and the brand button (`.button.brand`, coral `#ef4056`) are declared in the stylesheet and were not painted.

## Link

Footer links are Graphik Web 16px, `#1a1a1a`, underlined. The stylesheet sets hover to `--color-textLinkHover` (`#008078` in light). A live hover was not captured as its own crop.

![Get help](components/crops/link-default.png)

## Select

The footer language control is a native `select`, 220px by 36px, 1px `#8c8c8c` border, 4px radius, padding 4px 32px 4px 8px, appearance none, with the light down-arrow. Focus uses the same 1px `#009990` outline.

![Language select](components/crops/select-default.png)

![Language select focused](components/crops/select-focus.png)

## Wordmark

The header logo is a 94 by 24 CSS-pixel background image. The SVG is in [icons/wordmark.svg](icons/wordmark.svg). The pocket mark is `#EF4056`.

![Pocket wordmark](components/crops/logo.png)

## Gaps

| Component | Status |
|---|---|
| Button default, hover, focus | Captured. Primary on the error page, secondary on the shutdown page. |
| Button pressed, disabled, loading, brand | Not painted. Brand and disabled rules exist in the stylesheet. |
| Icon button | Not on the page. |
| Link | Captured at rest. Hover colour is declared, not cropped. |
| Text field, text area | Declared (`--borderRadius` 4px, `--color-formFieldBorder`). Not on the page. |
| Select | Captured, default and focus. Open menu not captured. |
| Checkbox, radio, switch | Declared (24px box, 64 by 36 toggle, 50ms and 100ms transitions). Not on the page. |
| Tabs, menu, tooltip, dialog, toast | Declared (tooltip keyframes, dialog durations). Not on the page. |
| Card, list row, table, avatar, badge | Not on the shutdown page. The illustrations are marketing images, not components. |
