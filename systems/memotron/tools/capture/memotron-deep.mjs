// Second pass: scroll the marketing site's inner scroller, shoot sections,
// harvest CSS custom properties, and measure component states.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs \
//     node tools/capture/memotron-deep.mjs
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from './screenshot.mjs';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const HERE = path.dirname(fileURLToPath(import.meta.url));
const PKG = path.resolve(HERE, '..', '..');
const RAW_SHOTS = process.env.RAW || path.join(os.homedir(), '.design-systems', 'memotron', 'raw-shots');
const RAW = path.join(PKG, 'raw');
fs.mkdirSync(RAW_SHOTS, { recursive: true });
fs.mkdirSync(path.join(PKG, 'components', 'crops'), { recursive: true });
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';

const browser = await chromium.launch({ headless: true });

// Pull stylesheet text in Node (page fetch can be CORS-blocked for some sheets).
async function fetchSheets(page) {
  const hrefs = await page.evaluate(() => [...document.querySelectorAll('link[rel="stylesheet"]')].map((l) => l.href));
  const sheets = [];
  for (const href of hrefs) {
    const res = await page.request.get(href);
    const css = await res.text();
    sheets.push({ href, status: res.status(), bytes: css.length, css });
    log('  sheet', res.status(), css.length, href.slice(0, 90));
  }
  return sheets;
}

function extractVars(css) {
  const rules = [];
  // crude but enough: blocks that declare --colors- or --font
  const re = /([^{}]+)\{([^{}]*--(?:colors|font|radius|space|size|duration|ease)[^{}]*)\}/g;
  let m;
  let n = 0;
  while ((m = re.exec(css)) && n < 4000) {
    n++;
    const sel = m[1].trim().slice(-180);
    const body = m[2];
    const props = {};
    const pre = /(--[A-Za-z0-9_-]+)\s*:\s*([^;]+);/g;
    let p;
    while ((p = pre.exec(body))) props[p[1]] = p[2].trim();
    if (Object.keys(props).length) rules.push({ selector: sel.replace(/\s+/g, ' '), properties: props });
  }
  return rules;
}

const ctx = await browser.newContext({
  viewport: { width: 1440, height: 900 },
  deviceScaleFactor: 1,
  userAgent: UA,
  locale: 'en-US',
  colorScheme: 'dark',
});
const page = await ctx.newPage();
const requested = { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, sanitizedSourceUrl: 'https://memotron.app/' };

await page.goto('https://memotron.app/', { waitUntil: 'domcontentloaded', timeout: 45000 });
await page.waitForTimeout(2000);

const scroller = await page.evaluate(() => {
  const all = [...document.querySelectorAll('*')];
  const hits = [];
  for (const el of all) {
    if (el.scrollHeight > el.clientHeight + 80 && el.clientHeight > 200) {
      hits.push({
        tag: el.tagName,
        cls: (el.className || '').toString().slice(0, 120),
        sh: el.scrollHeight,
        ch: el.clientHeight,
      });
    }
  }
  return hits.slice(0, 8);
});
log('scrollers', JSON.stringify(scroller));

// Scroll the tallest inner scroller and shoot slices.
const slices = await page.evaluate(async () => {
  const all = [...document.querySelectorAll('*')];
  let best = null;
  for (const el of all) {
    if (el.scrollHeight > el.clientHeight + 80 && el.clientHeight > 400) {
      if (!best || el.scrollHeight > best.scrollHeight) best = el;
    }
  }
  if (!best) return { error: 'no scroller' };
  best.setAttribute('data-memo-scroll', '1');
  return { sh: best.scrollHeight, ch: best.clientHeight };
});
log('best', JSON.stringify(slices));

const step = 800;
const sh = slices.sh || 900;
for (let y = 0, i = 0; y < sh && i < 14; y += step, i++) {
  await page.evaluate((y) => {
    const el = document.querySelector('[data-memo-scroll]');
    if (el) el.scrollTop = y;
    else scrollTo(0, y);
  }, y);
  await page.waitForTimeout(400);
  await screenshotWithMetadata(page, { path: path.join(RAW_SHOTS, `home-dark-slice${i}.png`) }, requested);
  log('  slice', i, 'y', y);
}

// Resources menu
await page.evaluate(() => { const el = document.querySelector('[data-memo-scroll]'); if (el) el.scrollTop = 0; });
await page.waitForTimeout(300);
const resources = page.getByText('Resources', { exact: true }).first();
await resources.click().catch((e) => log('resources click', e.message));
await page.waitForTimeout(600);
await screenshotWithMetadata(page, { path: path.join(RAW_SHOTS, 'home-dark-resources-menu.png') }, requested);
log('resources menu shot');

// Stylesheets
const sheets = await fetchSheets(page);
const cssVars = [];
for (const s of sheets) {
  if (!s.css) continue;
  const rules = extractVars(s.css);
  cssVars.push({ href: s.href, bytes: s.bytes, ruleCount: rules.length, rules });
  log('  vars from', s.href.slice(-40), rules.length);
}
fs.writeFileSync(path.join(RAW, 'css-rules.json'), JSON.stringify({
  readAt: new Date().toISOString().slice(0, 10),
  source: 'link[rel=stylesheet] on https://memotron.app/, fetched with the page request context',
  sheets: cssVars.map(({ href, bytes, ruleCount, rules }) => ({ href, bytes, ruleCount, rules })),
}, null, 1) + '\n');

// Type scale classes from computed styles of known class names.
const typeScale = await page.evaluate(() => {
  const classes = ['text-h1', 'text-h2', 'text-h3', 'text-h4', 'text-base', 'text-b1', 'text-b2', 'text-b3', 'text-lb2', 'text-lbase', 'text-fgs1', 'text-fgs2', 'bg-bgs1', 'bg-bgs2', 'bg-fgs1', 'text-aps1'];
  const host = document.createElement('div');
  // The probe takes the theme classes of the page's cs_tidigit wrapper; without one the read stops
  // with a plain message instead of a TypeError.
  const wrapper = document.querySelector('[class*="cs_tidigit"]');
  // Throw, so page.evaluate rejects and the run stops before it writes over the saved readings.
  if (!wrapper) throw new Error('no cs_tidigit wrapper on the page; the type probe has nothing to copy');
  host.className = wrapper.className;
  host.style.cssText = 'position:absolute;left:-9999px;top:0';
  document.body.appendChild(host);
  const out = {};
  for (const c of classes) {
    const el = document.createElement('div');
    el.className = c;
    el.textContent = 'Ag';
    host.appendChild(el);
    const s = getComputedStyle(el);
    out[c] = { fontSize: s.fontSize, fontWeight: s.fontWeight, lineHeight: s.lineHeight, color: s.color, backgroundColor: s.backgroundColor, letterSpacing: s.letterSpacing };
  }
  host.remove();
  return out;
});
fs.writeFileSync(path.join(RAW, 'type-scale.json'), JSON.stringify(typeScale, null, 1) + '\n');
log('type scale', Object.keys(typeScale).length);

await ctx.close();

// Pricing full scroll + billing toggle + signup states
async function scrollShots(url, prefix, extra) {
  const c = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US', colorScheme: 'dark' });
  const p = await c.newPage();
  const req = { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, sanitizedSourceUrl: url.split('?')[0] };
  await p.goto(url, { waitUntil: 'domcontentloaded', timeout: 45000 });
  await p.waitForTimeout(1800);
  const info = await p.evaluate(() => {
    const all = [...document.querySelectorAll('*')];
    let best = null;
    for (const el of all) {
      if (el.scrollHeight > el.clientHeight + 40 && el.clientHeight > 300) {
        if (!best || el.scrollHeight > best.scrollHeight) best = el;
      }
    }
    if (best) best.setAttribute('data-memo-scroll', '1');
    return best ? { sh: best.scrollHeight, ch: best.clientHeight } : { sh: document.documentElement.scrollHeight, ch: innerHeight, doc: true };
  });
  log(prefix, JSON.stringify(info));
  const step = 780;
  for (let y = 0, i = 0; y < info.sh && i < 10; y += step, i++) {
    await p.evaluate((y) => {
      const el = document.querySelector('[data-memo-scroll]');
      if (el) el.scrollTop = y; else scrollTo(0, y);
    }, y);
    await p.waitForTimeout(350);
    await screenshotWithMetadata(p, { path: path.join(RAW_SHOTS, `${prefix}-slice${i}.png`) }, req);
  }
  if (extra) await extra(p, req);
  await c.close();
}

await scrollShots('https://memotron.app/pricing', 'pricing-dark', async (p, req) => {
  const monthly = p.getByText('Monthly', { exact: true }).first();
  if (await monthly.count()) {
    await monthly.click().catch(() => {});
    await p.waitForTimeout(500);
    await p.evaluate(() => { const el = document.querySelector('[data-memo-scroll]'); if (el) el.scrollTop = 200; });
    await screenshotWithMetadata(p, { path: path.join(RAW_SHOTS, 'pricing-dark-monthly.png') }, req);
    log('  monthly toggle');
  }
});
await scrollShots('https://memotron.app/compare', 'compare-dark');

// Signup component measurements + crops via element screenshots
{
  const c = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US', colorScheme: 'dark' });
  const p = await c.newPage();
  await p.goto('https://web.memotron.app/signup', { waitUntil: 'domcontentloaded', timeout: 45000 });
  await p.waitForTimeout(2000);
  const crops = path.join(PKG, 'components', 'crops');
  async function shoot(name, locator) {
    const el = p.locator(locator).first();
    if (!(await el.count())) { log('  missing', name); return null; }
    const box = await el.boundingBox();
    if (!box) return null;
    const pad = 8;
    const clip = {
      x: Math.max(0, box.x - pad),
      y: Math.max(0, box.y - pad),
      width: Math.min(1440 - Math.max(0, box.x - pad), box.width + pad * 2),
      height: Math.min(900 - Math.max(0, box.y - pad), box.height + pad * 2),
    };
    await el.screenshot({ path: path.join(crops, `${name}.png`) }).catch(async () => {
      await p.screenshot({ path: path.join(crops, `${name}.png`), clip });
    });
    const style = await el.evaluate((node) => {
      const s = getComputedStyle(node);
      return {
        text: (node.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 80),
        color: s.color, backgroundColor: s.backgroundColor, borderRadius: s.borderRadius,
        fontSize: s.fontSize, fontWeight: s.fontWeight, lineHeight: s.lineHeight,
        padding: s.padding, border: s.borderTopWidth + ' ' + s.borderTopStyle + ' ' + s.borderTopColor,
        height: s.height, fontFamily: s.fontFamily, boxShadow: s.boxShadow,
      };
    });
    log('  crop', name, style.text);
    return { style, box };
  }
  const components = {};
  components['button-google-default'] = await shoot('button-google-default', 'button:has-text("Continue with Google")');
  // hover
  await p.locator('button:has-text("Continue with Google")').first().hover();
  await p.waitForTimeout(300);
  components['button-google-hover'] = await shoot('button-google-hover', 'button:has-text("Continue with Google")');
  components['button-apple-default'] = await shoot('button-apple-default', 'button:has-text("Continue with Apple")');
  components['button-offline-default'] = await shoot('button-offline-default', 'button:has-text("Continue offline")');
  await p.locator('button:has-text("Continue offline")').first().hover();
  await p.waitForTimeout(300);
  components['button-offline-hover'] = await shoot('button-offline-hover', 'button:has-text("Continue offline")');
  components['link-terms-default'] = await shoot('link-terms-default', 'button:has-text("Terms of Service")');
  components['heading-welcome'] = await shoot('heading-welcome-default', 'h3');
  fs.writeFileSync(path.join(RAW, 'signup-components.json'), JSON.stringify(components, null, 1) + '\n');
  await c.close();
}

// Home CTA crops at 2x
{
  const c = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US', colorScheme: 'dark' });
  const p = await c.newPage();
  await p.goto('https://memotron.app/', { waitUntil: 'domcontentloaded', timeout: 45000 });
  await p.waitForTimeout(1500);
  const crops = path.join(PKG, 'components', 'crops');
  async function shoot(name, locator) {
    const el = p.locator(locator).first();
    if (!(await el.count())) { log('  missing', name); return; }
    await el.screenshot({ path: path.join(crops, `${name}.png`) });
    log('  crop', name);
  }
  await shoot('button-webapp-default', 'a[href="https://web.memotron.app"]');
  await p.locator('a[href="https://web.memotron.app"]').first().hover();
  await p.waitForTimeout(250);
  await shoot('button-webapp-hover', 'a[href="https://web.memotron.app"]');
  await shoot('button-download-default', 'a[href*="apps.apple.com"]');
  await p.locator('a[href*="apps.apple.com"]').first().hover();
  await p.waitForTimeout(250);
  await shoot('button-download-hover', 'a[href*="apps.apple.com"]');
  // A hover pair is the same element at rest and under the pointer (it was /pricing, then /compare).
  await shoot('nav-link-default', 'a[href="/pricing"]');
  await p.locator('a[href="/pricing"]').first().hover();
  await p.waitForTimeout(250);
  await shoot('nav-link-hover', 'a[href="/pricing"]');
  await p.mouse.move(2, 2);
  await shoot('wordmark-default', 'a[href="/"]');
  await c.close();
}

await browser.close();
log('deep capture done');
