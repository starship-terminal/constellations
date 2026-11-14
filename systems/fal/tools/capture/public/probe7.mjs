import { BASE, UA, launch, patch, open } from './lib.mjs';
const { browser } = await launch();
const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, colorScheme: 'dark' });
await patch(ctx);
const p = await ctx.newPage();
await open(p, BASE + '/models/krea/v3/text-to-image', { wait: 12000 });
await p.waitForTimeout(3000);
const info = await p.evaluate(() =>
  [...document.querySelectorAll('a[href*="sandbox" i]')].map((a) => {
    const r = a.getBoundingClientRect();
    return { href: a.getAttribute('href'), text: a.textContent.trim().slice(0, 60), w: Math.round(r.width), h: Math.round(r.height), cls: String(a.className).slice(0, 80), vis: getComputedStyle(a).visibility };
  }));
console.log(JSON.stringify(info, null, 1));
await ctx.close(); await browser.close();
