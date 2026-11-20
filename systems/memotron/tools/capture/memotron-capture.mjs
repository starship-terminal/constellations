// Memotron public capture. Measures computed styles and screenshots the signed-out
// marketing site and the signed-out web-app signup. Nothing is submitted.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs \
//     node tools/capture/memotron-capture.mjs
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
fs.mkdirSync(RAW, { recursive: true });
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);

const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';

const PAGES = [
  { name: 'home', url: 'https://memotron.app/' },
  { name: 'pricing', url: 'https://memotron.app/pricing' },
  { name: 'compare', url: 'https://memotron.app/compare' },
  { name: 'privacy', url: 'https://memotron.app/privacy' },
  { name: 'tos', url: 'https://memotron.app/tos' },
  { name: 'refund', url: 'https://memotron.app/policies/refundpolicy' },
  { name: 'signup', url: 'https://web.memotron.app/signup' },
];

function rgbToHex(c) {
  const m = String(c).match(/rgba?\((\d+),\s*(\d+),\s*(\d+)(?:,\s*([\d.]+))?\)/);
  if (!m) return c;
  const hex = '#' + [m[1], m[2], m[3]].map((n) => (+n).toString(16).padStart(2, '0')).join('');
  const a = m[4] === undefined ? 1 : +m[4];
  return a === 1 ? hex : `${hex} / ${a}`;
}

async function readPage(page) {
  return page.evaluate(() => {
    const host = document.querySelector('[class*="cs_tidigit"]') || document.body;
    const hs = getComputedStyle(host);
    const colors = {};
    for (let i = 0; i < hs.length; i++) {
      const n = hs[i];
      if (n.startsWith('--colors-') || n.startsWith('--font')) colors[n] = hs.getPropertyValue(n).trim();
    }
    const props = ['color', 'backgroundColor', 'fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'letterSpacing', 'borderRadius', 'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft', 'borderTopWidth', 'borderTopStyle', 'borderTopColor', 'boxShadow', 'height', 'minHeight', 'gap', 'display', 'textDecorationLine'];
    const pick = (el) => {
      if (!el) return null;
      const s = getComputedStyle(el);
      const o = {
        tag: el.tagName,
        cls: (el.className || '').toString().slice(0, 220),
        text: (el.innerText || el.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim().slice(0, 80),
      };
      for (const p of props) o[p] = s[p];
      const r = el.getBoundingClientRect();
      o.box = [Math.round(r.x), Math.round(r.y), Math.round(r.width), Math.round(r.height)];
      return o;
    };
    const seen = new Set();
    const nodes = [];
    for (const el of document.querySelectorAll('h1,h2,h3,h4,button,a,p,input,header,nav,footer,label')) {
      const key = el.tagName + '|' + (el.className || '').toString().slice(0, 90);
      if (seen.has(key)) continue;
      seen.add(key);
      if (nodes.length < 48) nodes.push(pick(el));
    }
    const links = [...document.querySelectorAll('a')].slice(0, 60).map((a) => ({
      t: (a.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 40),
      h: a.getAttribute('href'),
    }));
    return {
      title: document.title,
      href: location.href,
      hostClass: (host.className || '').toString().slice(0, 240),
      colors,
      bodyFont: getComputedStyle(document.body).fontFamily,
      bodySize: getComputedStyle(document.body).fontSize,
      scrollH: document.documentElement.scrollHeight,
      inner: [innerWidth, innerHeight],
      dpr: devicePixelRatio,
      text: (document.body.innerText || '').slice(0, 1800),
      nodes,
      links,
      cf: /just a moment|cf-challenge-running/i.test(document.title) || !!document.querySelector('#challenge-form'),
    };
  });
}

const browser = await chromium.launch({ headless: true });
const readings = { readAt: new Date().toISOString().slice(0, 10), pages: {} };

for (const spec of PAGES) {
  for (const mob of [false, true]) {
    const vw = mob ? 390 : 1440;
    const vh = mob ? 844 : 900;
    const dpr = mob ? 2 : 1;
    const prefix = (mob ? 'mobile-' : '') + spec.name + '-dark';
    const ctx = await browser.newContext({
      viewport: { width: vw, height: vh },
      deviceScaleFactor: dpr,
      userAgent: UA,
      locale: 'en-US',
      colorScheme: 'dark',
      isMobile: mob,
      hasTouch: mob,
    });
    const page = await ctx.newPage();
    log(prefix, spec.url);
    try {
      const res = await page.goto(spec.url, { waitUntil: 'domcontentloaded', timeout: 45000 });
      await page.waitForTimeout(2500);
      const status = res ? res.status() : null;
      const title = await page.title();
      const bodyStart = await page.evaluate(() => (document.body && document.body.innerText || '').slice(0, 180));
      const blocked = /just a moment|cf-browser-verification|attention required/i.test(title + bodyStart);
      log('  status', status, 'title', JSON.stringify(title).slice(0, 80), 'blocked', blocked);
      if (blocked) {
        readings.pages[prefix] = { url: spec.url, blocked: true, title, status };
        await ctx.close();
        continue;
      }
      const data = await readPage(page);
      readings.pages[prefix] = { url: spec.url, status, ...data, blocked: false };
      const requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, sanitizedSourceUrl: spec.url };
      await screenshotWithMetadata(page, { path: path.join(RAW_SHOTS, `${prefix}-default.png`) }, requested);
      // full page, capped
      const H = await page.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
      if (H > vh + 40 && H < 14000) {
        await screenshotWithMetadata(page, { path: path.join(RAW_SHOTS, `${prefix}-full.png`), fullPage: true }, requested);
      }
      log('  shot', prefix, 'H', H);
    } catch (e) {
      log('  FAILED', prefix, String(e.message).split('\n')[0]);
      readings.pages[prefix] = { url: spec.url, error: String(e.message).split('\n')[0] };
    }
    await ctx.close();
  }
}

// Component states on the home page and signup, desktop only.
{
  const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US', colorScheme: 'dark' });
  const page = await ctx.newPage();
  await page.goto('https://memotron.app/', { waitUntil: 'domcontentloaded', timeout: 45000 });
  await page.waitForTimeout(2000);
  const states = {};
  async function measure(name, locator) {
    const el = page.locator(locator).first();
    if (!(await el.count())) { log('  missing', name); return; }
    await el.scrollIntoViewIfNeeded().catch(() => {});
    const rest = await el.evaluate((node) => {
      const s = getComputedStyle(node);
      const r = node.getBoundingClientRect();
      return {
        text: (node.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 60),
        color: s.color, backgroundColor: s.backgroundColor, borderRadius: s.borderRadius,
        fontSize: s.fontSize, fontWeight: s.fontWeight, lineHeight: s.lineHeight,
        padding: s.padding, borderTopWidth: s.borderTopWidth, borderTopColor: s.borderTopColor,
        boxShadow: s.boxShadow, height: s.height, fontFamily: s.fontFamily,
        box: [Math.round(r.x), Math.round(r.y), Math.round(r.width), Math.round(r.height)],
        cls: (node.className || '').toString().slice(0, 180),
      };
    });
    states[name] = { rest };
    await el.hover().catch(() => {});
    await page.waitForTimeout(350);
    states[name].hover = await el.evaluate((node) => {
      const s = getComputedStyle(node);
      return { color: s.color, backgroundColor: s.backgroundColor, borderTopColor: s.borderTopColor, transform: s.transform };
    });
    log('  measured', name, rest.text);
  }
  await measure('nav-pricing', 'a[href="/pricing"]');
  await measure('cta-web-app', 'a[href="https://web.memotron.app"]');
  await measure('cta-download', 'a[href*="apps.apple.com"]');
  readings.components = { home: states };
  await ctx.close();
}

fs.writeFileSync(path.join(RAW, 'live-readings.json'), JSON.stringify(readings, null, 1) + '\n');
log('wrote', path.join(RAW, 'live-readings.json'));
await browser.close();
