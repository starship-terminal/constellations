// Layout readings for the public marketing shell at 1440, 1024 and 390.
//   PLAYWRIGHT=... node tools/capture/layout.mjs
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { chromium, UA, UA_MOBILE, BASE, hideConsent, RAW } from './public/lib.mjs';

const OUT = path.join(RAW, 'layout.json');
fs.mkdirSync(RAW, { recursive: true });
const browser = await chromium.launch({ headless: true });
const widths = [
  { name: '1440', width: 1440, height: 900, mobile: false },
  { name: '1024', width: 1024, height: 800, mobile: false },
  { name: '390', width: 390, height: 844, mobile: true },
];
const pages = ['/', '/pricing', '/feature/paywalls', '/docs'];
const out = { capturedAt: new Date().toISOString().slice(0, 10), widths: {} };

for (const w of widths) {
  const ctx = await browser.newContext({
    viewport: { width: w.width, height: w.height },
    deviceScaleFactor: w.mobile ? 2 : 1,
    userAgent: w.mobile ? UA_MOBILE : UA,
    isMobile: w.mobile,
    hasTouch: w.mobile,
    locale: 'en-US',
  });
  const page = await ctx.newPage();
  out.widths[w.name] = {};
  for (const pth of pages) {
    await page.goto(BASE + pth, { waitUntil: 'domcontentloaded', timeout: 40000 });
    await page.waitForTimeout(1200);
    await hideConsent(page);
    const reading = await page.evaluate(() => {
      const header = document.querySelector('header');
      const hr = header ? header.getBoundingClientRect() : null;
      const h1 = document.querySelector('h1');
      const main = document.querySelector('main') || document.body;
      const mr = main.getBoundingClientRect();
      return {
        innerWidth: window.innerWidth,
        innerHeight: window.innerHeight,
        dpr: window.devicePixelRatio,
        scrollHeight: document.documentElement.scrollHeight,
        header: hr ? { h: +hr.height.toFixed(1), y: +hr.top.toFixed(1) } : null,
        h1: h1 ? { size: getComputedStyle(h1).fontSize, weight: getComputedStyle(h1).fontWeight, family: getComputedStyle(h1).fontFamily, w: +h1.getBoundingClientRect().width.toFixed(1) } : null,
        mainWidth: +mr.width.toFixed(1),
      };
    });
    out.widths[w.name][pth] = reading;
    console.log(w.name, pth, reading.innerWidth, 'header', reading.header && reading.header.h);
  }
  await ctx.close();
}
fs.writeFileSync(OUT, JSON.stringify(out, null, 2));
console.log('wrote', OUT);
await browser.close();
