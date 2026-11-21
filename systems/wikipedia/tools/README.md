# Tools

`style-guide.html` was produced from `tokens.json` by hand. The page was written from the measured tokens in that file (canvas, content, ink, title, progressive, visited, night roles, and the search control). It is not a generated rebuild.

No builder lives in this package. There is no `build_style_guide.py` and no other script that writes `style-guide.html`. Do not invent a pipeline to regenerate it. `catalog.json` was left alone, so `make design-md` does not own this package.
