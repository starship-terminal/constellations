// Shared helpers for rendering and measuring the static NotebookLM page copies.
// Adapted from systems/linear/tools/capture/signed-in/lib.mjs (itself from the kit).
//
// A copy is a signed-in notebook.google.com page with every same-origin stylesheet inlined, so
// what still comes from the network is Google Fonts (Google Sans, Google Sans Text and Code, the
// Luminous Symbols icon font), the Google bar's stylesheet and a few gstatic images. Every
// response from those hosts is kept in a local cache directory the first time it is fetched
// (CDN_CACHE, default <SNAPS>-cdn-cache beside the copies) and served from there afterwards, so a
// re-run is offline and identical. Nothing is ever requested from notebook.google.com itself or
// any other host: those requests are aborted.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
export const { chromium } = pw.default ?? pw;

export const HERE = path.dirname(new URL(import.meta.url).pathname);
export const REF = path.resolve(HERE, '..', '..', '..');
export const RAW = path.join(REF, 'raw');
export const CROPS = path.join(REF, 'components', 'crops');
export const SNAPS = process.env.SNAPS ? path.resolve(process.env.SNAPS) : null;
export const CACHE = process.env.CDN_CACHE ? path.resolve(process.env.CDN_CACHE) : SNAPS && `${SNAPS}-cdn-cache`;

// Inner-scroll overrides per copy (none: snapshot.js marks every scrolled element).
export const SCROLL = {};

// PRODUCT (adapt): the host that serves the product's stylesheets, fonts and images.
const CDN = /^https:\/\/(fonts\.googleapis\.com|fonts\.gstatic\.com|www\.gstatic\.com)\//;
export async function routeCdn(ctx) {
  fs.mkdirSync(CACHE, { recursive: true });
  await ctx.route('**/*', async (route) => {
    const url = route.request().url();
    if (url.startsWith('file:') || url.startsWith('data:') || url.startsWith('blob:')) return route.continue();
    if (!CDN.test(url) || route.request().method() !== 'GET') return route.abort();
    const key = crypto.createHash('sha1').update(url).digest('hex');
    const body = path.join(CACHE, key);
    const meta = body + '.json';
    if (fs.existsSync(meta)) {
      const m = JSON.parse(fs.readFileSync(meta, 'utf8'));
      return route.fulfill({ status: m.status, headers: m.headers, body: fs.readFileSync(body) });
    }
    try {
      const res = await route.fetch({ timeout: 30000 });
      const buf = await res.body();
      const headers = { 'content-type': res.headers()['content-type'] || 'application/octet-stream', 'access-control-allow-origin': '*' };
      if (res.status() === 200) {
        fs.writeFileSync(body, buf);
        fs.writeFileSync(meta, JSON.stringify({ url, status: 200, headers }));
      }
      return route.fulfill({ status: res.status(), headers, body: buf });
    } catch {
      return route.abort();
    }
  });
}

// NotebookLM's own tokens are declared as light-dark(light, dark) and Angular Material's per theme
// under .dark-theme, and the body's class picks one: a copy taken in dark becomes light by
// swapping that class, which is what the in-app Light setting does.
// PRODUCT (adapt): how this product switches a copy from dark to light.
export async function setLight(page) {
  await page.evaluate(() => { document.body.classList.remove('dark-theme'); document.body.classList.add('light-theme'); });
  await page.waitForTimeout(300);
}

// Opens a copy: file:// URL, fonts settled, the inner scroll restored (the data-snap-scroll marks
// snapshot.js left, or the SCROLL rule), and the layout checked for having come up styled (the
// shell is a 100vh box, so a document much taller than the captured one means the CSS did not
// apply); up to two reloads are tried before giving up.
export async function openSnap(ctx, label, { light = false } = {}) {
  const meta = metaOf(label);
  const page = await ctx.newPage();
  page.setDefaultTimeout(8000);
  for (let attempt = 0; attempt < 3; attempt++) {
    try {
      await page.goto(`file://${SNAPS}/${label}.html`, { waitUntil: 'load', timeout: 90000 });
    } catch (e) {
      if (attempt === 2) throw e;
      continue;
    }
    await page.evaluate(() => document.fonts && document.fonts.ready);
    await page.waitForTimeout(1500);
    const ok = await page.evaluate((docH) => document.documentElement.scrollHeight <= Math.max(docH, innerHeight) * 1.5 && [...document.styleSheets].length >= 4, meta.docH || meta.h); // PRODUCT (adapt): stylesheets a styled copy has
    if (ok) break;
    if (attempt === 2) throw new Error(`${label}: layout did not come up styled`);
  }
  if (light) await setLight(page);
  await applyScroll(page, label);
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' });
  await page.waitForTimeout(400);
  return page;
}

export async function applyScroll(page, label) {
  const flag = SCROLL[label];
  await page.evaluate((flag) => {
    const marked = document.querySelectorAll('[data-snap-scroll]');
    if (marked.length && !flag) {
      marked.forEach((n) => { const [t, l] = n.getAttribute('data-snap-scroll').split(',').map(Number); n.scrollTop = t; n.scrollLeft = l; });
    } else if (flag) {
      const all = [...document.querySelectorAll('*')].filter((e) => !e.closest('nav') && /(auto|scroll)/.test(getComputedStyle(e).overflowY) && e.scrollHeight > e.clientHeight + 20);
      const sc = all.sort((a, b) => b.scrollHeight - a.scrollHeight)[0];
      if (sc) sc.scrollTop = flag === 'max' ? sc.scrollHeight : Number(flag);
    }
  }, flag);
  await page.waitForTimeout(300);
}

export function metaOf(label) {
  return JSON.parse(fs.readFileSync(path.join(SNAPS, `${label}.json`), 'utf8'));
}

export async function newContext(browser, meta, light = false) {
  // No isMobile/hasTouch for the 390 copies, matching render.mjs (which made the PNGs): the
  // phone captures are the same DOM at a narrow viewport.
  const ctx = await browser.newContext({
    viewport: { width: meta.w, height: meta.h }, deviceScaleFactor: 2, locale: 'en-US',
    colorScheme: light ? 'light' : 'dark', reducedMotion: 'no-preference',
  });
  await routeCdn(ctx);
  return ctx;
}
