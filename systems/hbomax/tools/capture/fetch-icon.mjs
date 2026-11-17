// fetch-icon.mjs — pull the site's own favicon/apple-touch-icon through the
// headed Chromium session (Akamai returns 403 to plain curl, so the icon has
// to ride in on a real page load's cookie/session). Picks the largest declared
// raster icon and writes it to the package's icon.png path.
import { writeFileSync } from 'node:fs';
import { open, chromium, UA, BASE, LOCALE } from './public/lib.mjs';

const OUT = process.argv[2] || '/tmp/hbomax-icon-src.png';

const browser = await chromium.launch({ headless: process.env.HEADLESS === '1' });
const context = await browser.newContext({
  viewport: { width: 1440, height: 900 }, userAgent: UA, locale: 'en-US',
});
const page = await context.newPage();
await open(page, BASE + LOCALE, { promo: 'none' });

const links = await page.$$eval('link[rel*="icon"], link[rel="apple-touch-icon"]', (els) =>
  els.map((e) => ({ rel: e.rel, href: e.href, sizes: e.sizes?.value || '' })),
);
console.log('icon links:', JSON.stringify(links));

// Largest declared raster first; apple-touch-icon preferred over generic icon.
const rank = (l) => {
  const n = parseInt((l.sizes.match(/\d+/) || ['0'])[0], 10);
  const apple = l.rel === 'apple-touch-icon' ? 10000 : 0;
  const svg = l.href.endsWith('.svg') ? -5000 : 0;
  return apple + n + svg;
};
links.sort((a, b) => rank(b) - rank(a));

for (const l of links) {
  try {
    const resp = await page.context().request.get(l.href);
    if (!resp.ok()) { console.log(`skip ${l.href}: ${resp.status()}`); continue; }
    const buf = await resp.body();
    if (buf.length < 200) continue;
    writeFileSync(OUT, buf);
    console.log(`saved ${l.href} (${buf.length} bytes) -> ${OUT}`);
    break;
  } catch (e) { console.log(`fail ${l.href}: ${e.message}`); }
}
await browser.close();
