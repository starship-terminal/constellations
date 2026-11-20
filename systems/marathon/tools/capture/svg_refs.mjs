// The ids an SVG's markup refers to inside itself: url(#id) in paint and filter values, and
// href="#id" or xlink:href="#id" on <use> and gradients. icons.mjs keeps exactly these ids when it
// strips the rest, so a <use href="#glyph"> still finds its glyph. Pure: it reads a string, so
// tools/test_build_tokens.py runs it on a fixture, and icons.mjs passes its source into the page.
export function fragmentRefs(html) {
  const refs = new Set();
  for (const m of String(html).matchAll(/url\(\s*(?:&quot;|["'])?#([^)"'&\s]+)/g)) refs.add(m[1]);
  for (const m of String(html).matchAll(/(?:^|[\s<])(?:xlink:)?href\s*=\s*(?:"#([^"]+)"|'#([^']+)')/g)) refs.add(m[1] || m[2]);
  return refs;
}
