// Reads shell geometry for Hello Klean's public pages.
//   PLAYWRIGHT=... node layout.mjs
import fs from 'node:fs';
import path from 'node:path';
import { chromium, UA, UA_MOBILE, BASE, RAW, clearChallenge, closePromo, patch } from './public/lib.mjs';

const PAGES = [
  ['home', '/en-int'],
  ['shop', '/en-int/collections/filters'],
  ['product', '/en-int/products/hello-klean-skin-filter'],
  ['faq', '/en-int/pages/faqs'],
  ['about', '/en-int/pages/about-us'],
];
const WIDTHS = [1440, 1024, 390];

async function read(page) {
  return page.evaluate(() => {
    const box = (el) => {
      if (!el) return null;
      const r = el.getBoundingClientRect();
      const cs = getComputedStyle(el);
      return { tag: el.tagName.toLowerCase(), cls: (el.className || '').toString().slice(0, 80), x: +r.x.toFixed(1), y: +r.y.toFixed(1), w: +r.width.toFixed(1), h: +r.height.toFixed(1), position: cs.position, bg: cs.backgroundColor, color: cs.color };
    };
    const h1 = document.querySelector('h1');
    return {
      url: location.href.split('?')[0],
      title: document.title,
      innerWidth: window.innerWidth,
      innerHeight: window.innerHeight,
      dpr: window.devicePixelRatio,
      visualViewport: window.visualViewport ? { w: window.visualViewport.width, h: window.visualViewport.height, scale: window.visualViewport.scale } : null,
      scrollHeight: document.documentElement.scrollHeight,
      header: box(document.querySelector('header')),
      announcement: box(document.querySelector('[class*="announcement"]')),
      nav: box(document.querySelector('nav')),
      main: box(document.querySelector('main')),
      footer: box(document.querySelector('footer')),
      h1: h1 ? { text: (h1.innerText || '').trim().slice(0, 80), ...box(h1) } : null,
    };
  });
}

const browser = await chromium.launch();
const out = { captured: new Date().toISOString(), pages: [] };
for (const width of WIDTHS) {
  const mobile = width < 500;
  const ctx = await browser.newContext({
    viewport: { width, height: mobile ? 844 : 900 },
    deviceScaleFactor: mobile ? 2 : 1,
    userAgent: mobile ? UA_MOBILE : UA,
    isMobile: mobile,
    hasTouch: mobile,
    locale: 'en-GB',
  });
  await patch(ctx);
  const page = await ctx.newPage();
  for (const [name, urlPath] of PAGES) {
    await page.goto(BASE + urlPath, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    if (!(await clearChallenge(page))) { out.pages.push({ name, width, blocked: true }); continue; }
    await page.waitForTimeout(2500);
    await closePromo(page);
    const row = await read(page);
    row.name = name;
    row.requestedWidth = width;
    out.pages.push(row);
    console.log(name, width, 'inner', row.innerWidth, 'h1', row.h1 && row.h1.text);
  }
  await ctx.close();
}
fs.mkdirSync(RAW, { recursive: true });
fs.writeFileSync(path.join(RAW, 'layout.json'), JSON.stringify(out, null, 2));
console.log('wrote layout.json', out.pages.length);
await browser.close();
