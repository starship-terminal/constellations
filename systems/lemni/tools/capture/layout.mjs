// Reads page geometry from Lemni's public pages and writes raw/layout.json.
// Public route: opens the live URLs. PRODUCT (adapt): the shell regions below
// name Lemni's nav, hero, docs rail and auth card.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node tools/capture/layout.mjs
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { chromium, UA, UA_MOBILE, patch, clearChallenge, closePromo, BASE, APP } from './public/lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..');
const OUT = path.join(REF, 'raw', 'layout.json');

function reader() {
  const R = (e) => { if (!e) return null; const r = e.getBoundingClientRect(); return { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) }; };
  const vis = (e) => { const r = e.getBoundingClientRect(); const cs = getComputedStyle(e); return r.width > 0 && r.height > 0 && cs.visibility !== 'hidden' && +cs.opacity > 0; };
  const F = (e) => { const c = getComputedStyle(e); return `${c.fontWeight} ${c.fontSize}/${c.lineHeight} ${c.fontFamily.split(',')[0]}`; };
  const nav = document.querySelector('nav');
  const h1 = document.querySelector('h1');
  const footer = document.querySelector('footer');
  return {
    vw: innerWidth, vh: innerHeight,
    scrollH: document.documentElement.scrollHeight,
    bodyBg: getComputedStyle(document.body).backgroundColor,
    bodyColor: getComputedStyle(document.body).color,
    nav: nav && vis(nav) ? { ...R(nav), bg: getComputedStyle(nav).backgroundColor, name: nav.getAttribute('data-framer-name') } : null,
    h1: h1 && vis(h1) ? { text: (h1.innerText || '').slice(0, 80), font: F(h1), color: getComputedStyle(h1).color, ...R(h1) } : null,
    footer: footer && vis(footer) ? R(footer) : null,
    inputs: [...document.querySelectorAll('input, textarea')].filter(vis).map((e) => ({ type: e.type, ph: e.placeholder, ...R(e), radius: getComputedStyle(e).borderRadius })),
    links: [...document.querySelectorAll('a')].filter(vis).slice(0, 8).map((e) => ({ t: (e.innerText || '').trim().slice(0, 24), ...R(e) })),
  };
}

const pages = [
  ['home-1440', BASE + '/', false],
  ['pricing-1440', BASE + '/pricing', false],
  ['docs-1440', BASE + '/docs', false],
  ['signin-1440', APP + '/signup', false],
  ['home-390', BASE + '/', true],
  ['pricing-390', BASE + '/pricing', true],
  ['signin-390', APP + '/signup', true],
];

const browser = await chromium.launch();
const TODAY = new Date().toLocaleDateString('en-CA');
// Keep the pages this script does not read (the signed-in app-inbox-1440 and
// app-settings-1440 readings build_tokens.py needs) and the date each was read.
const prev = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : { pages: {} };
const out = { readAt: TODAY, pages: { ...(prev.pages || {}) } };
for (const [k, v] of Object.entries(out.pages)) if (v && !v.readAt && prev.readAt) v.readAt = prev.readAt;
for (const [key, url, mobile] of pages) {
  const ctx = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US' });
  await patch(ctx);
  const page = await ctx.newPage();
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
  if (await clearChallenge(page, { tries: 5, step: 1000 })) {
    await page.waitForTimeout(2500);
    await closePromo(page);
    out.pages[key] = { ...(await page.evaluate(reader)), readAt: TODAY };
    console.log(key, out.pages[key].bodyBg, 'nav', out.pages[key].nav && out.pages[key].nav.h, 'h1', out.pages[key].h1 && out.pages[key].h1.text);
  } else console.log('blocked', key);
  await ctx.close();
}
fs.mkdirSync(path.join(REF, 'raw'), { recursive: true });
fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
console.log('wrote', OUT);
await browser.close();
