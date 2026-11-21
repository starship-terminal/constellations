# Aritzia

Public capture of [https://www.aritzia.com](https://www.aritzia.com), resolved to [https://www.aritzia.com/intl/en](https://www.aritzia.com/intl/en), on 2026-11-22. Region stayed Singapore (S$). Desktop 1440 by 900.

The shop is black and camel on the homepage, white and ink on a product page. Type is Non-Seasonal Geo. The wordmark is an inline SVG.


## Files

| File | What it holds |
|---|---|
| [DESIGN.md](DESIGN.md) | Generated export of the tokens |
| [components.md](components.md) | Public components named from the capture |
| [icon.png](icon.png) | Product icon, 128 px |
| [icons/](icons/) | Icon redraws |
| [patterns.md](patterns.md) | Public patterns named from the capture |
| [raw/](raw/) | Readings the tokens were measured from |
| [screenshots/](screenshots/) | Public page screenshots |
| [site-tree.md](site-tree.md) | Public pages and where the walk stopped |
| [style-guide.html](style-guide.html) | Renders the tokens |
| [tokens.json](tokens.json) | Measured colours, type, and sizes |
| [tools/](tools/) | Builders for this package |

## What's here

- [site-tree.md](site-tree.md) maps the header, the department menus, the footer, and the pages this pass opened.
- [tokens.json](tokens.json) holds colours and type measured from the live page.
- [DESIGN.md](DESIGN.md), [components.md](components.md), and [patterns.md](patterns.md) describe the public chrome.
- [style-guide.html](style-guide.html) paints the measured tokens.
- [screenshots/](screenshots/) holds the homepage, a product page, the about page, and the empty sign-in wall.

## Don't

- Keep the homepage black and the wordmark camel. The page is `#000000` and the mark is `#d89f71`. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- Use a square for the one action. Add to Bag and Sign In are black fills, radius `0px`. [screenshots/product-light-1440.png](screenshots/product-light-1440.png)
- Stop at the empty sign-in wall. Email and password were empty. Sign In was not clicked. [screenshots/login-light-1440.png](screenshots/login-light-1440.png)

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the page, accent, and button tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
