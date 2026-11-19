// Reads public Mangomint page geometry into raw/layout.json.
// Adapted from the kit: the kit's layout.mjs reads signed-in page copies.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node tools/capture/layout.mjs
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { chromium, UA, BASE, APP, BOOK, hidePromo } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');
const pages = [
  ['home', BASE + '/'],
  ['pricing', BASE + '/pricing/'],
  ['login', APP + '/login'],
  ['book', BOOK],
];

function measure() {
  const R = (e) => {
    if (!e) return null;
    const r = e.getBoundingClientRect();
    return { x: Math.round(r.left), y: Math.round(r.top), w: Math.round(r.width), h: Math.round(r.height) };
  };
  const header = document.querySelector('header');
  const h1 = document.querySelector('h1');
  return {
    vw: innerWidth,
    vh: innerHeight,
    scrollH: document.documentElement.scrollHeight,
    header: header ? { ...R(header), bg: getComputedStyle(header).backgroundColor } : null,
    h1: h1 ? { text: (h1.innerText || '').slice(0, 60), ...R(h1), size: getComputedStyle(h1).fontSize, weight: getComputedStyle(h1).fontWeight } : null,
    body: { bg: getComputedStyle(document.body).backgroundColor, font: getComputedStyle(document.body).fontFamily, size: getComputedStyle(document.body).fontSize },
  };
}

const browser = await chromium.launch({ headless: true });
const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, userAgent: UA, locale: 'en-US' });
const page = await ctx.newPage();
const out = {};
for (const [name, url] of pages) {
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 50000 });
  await page.waitForTimeout(1600);
  await hidePromo(page);
  out[name] = { url, ...await page.evaluate(measure) };
  console.log(name, out[name].scrollH, out[name].h1 && out[name].h1.text);
}
fs.mkdirSync(path.join(REF, 'raw'), { recursive: true });
fs.writeFileSync(path.join(REF, 'raw', 'layout.json'), JSON.stringify(out, null, 2) + '\n');
await browser.close();
