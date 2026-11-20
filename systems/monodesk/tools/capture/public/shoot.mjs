// MonoDesk public + signed-out capture.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node shoot.mjs
//
// Writes full-colour PNGs to ~/.design-systems/monodesk/raw-shots and a
// measurements JSON to raw/components-computed.json. Nothing is submitted:
// login, create-account, Google, and "Email me the link" are never pressed.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from '../screenshot.mjs';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;

const HERE = path.dirname(fileURLToPath(import.meta.url));
const PKG = path.resolve(HERE, '..', '..', '..');
const RAW_SHOTS = process.env.RAW || path.join(os.homedir(), '.design-systems', 'monodesk', 'raw-shots');
const RAW = path.join(PKG, 'raw');
fs.mkdirSync(RAW_SHOTS, { recursive: true });
fs.mkdirSync(RAW, { recursive: true });

const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
const UA_MOBILE = 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';

const SITE = 'https://www.monodesk.com';
const APP = 'https://app.monodesk.com';

const PAGES = [
  { name: 'home', url: `${SITE}/` },
  { name: 'pricing', url: `${SITE}/pricing` },
  { name: 'features', url: `${SITE}/features` },
  { name: 'about', url: `${SITE}/about-us` },
  { name: 'help', url: `${SITE}/help` },
  { name: 'blog', url: `${SITE}/blog` },
  { name: 'for-freelancers', url: `${SITE}/for-creative-pros/freelancers` },
  { name: 'feature-projects', url: `${SITE}/features/projects` },
  { name: 'playground', url: `${SITE}/playground` },
  { name: 'app-login', url: `${APP}/login`, app: true },
  { name: 'app-create', url: `${APP}/create`, app: true },
];

const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

function rgbToHex(c) {
  if (!c) return c;
  const m = String(c).match(/rgba?\(\s*([\d.]+)[,\s]+([\d.]+)[,\s]+([\d.]+)(?:[,\s/]+([\d.]+))?\s*\)/);
  if (!m) return c;
  const h = (n) => Math.round(Number(n)).toString(16).padStart(2, '0');
  const a = m[4] === undefined ? 1 : Number(m[4]);
  if (a >= 0.999) return `#${h(m[1])}${h(m[2])}${h(m[3])}`;
  return `rgba(${Math.round(m[1])}, ${Math.round(m[2])}, ${Math.round(m[3])}, ${Math.round(a * 1000) / 1000})`;
}

// Consent is hidden, never answered: no button is clicked (a loose /ok/ label matched "Book a demo"
// and "Facebook", and clicking accept answers the banner). Known banner ids are hidden outright; a
// broader cookie/consent match is hidden only when it is an overlay (fixed or sticky, or a dialog),
// so a cookie-settings link or a policy section in the page stays in the shot. Returns the count.
async function dismissCookie(page) {
  return page.evaluate(() => {
    let n = 0;
    const hide = (el) => { el.style.setProperty('display', 'none', 'important'); n++; };
    document.querySelectorAll('#onetrust-banner-sdk, #onetrust-consent-sdk, #CybotCookiebotDialog, #usercentrics-root').forEach(hide);
    const broad = '[id*="cookie" i], [class*="cookie" i], [id*="consent" i], [class*="consent" i], [aria-label*="cookie" i]';
    for (const el of document.querySelectorAll(broad)) {
      if (el === document.body || el === document.documentElement || el.closest('[style*="display: none"]')) continue;
      const pos = getComputedStyle(el).position;
      const overlay = pos === 'fixed' || pos === 'sticky' || el.getAttribute('role') === 'dialog' || el.getAttribute('aria-modal') === 'true';
      if (overlay) hide(el);
    }
    return n;
  }).catch(() => 0);
}

async function pauseMedia(page) {
  await page.evaluate(() => {
    document.querySelectorAll('video').forEach((v) => { try { v.pause(); } catch (e) {} });
  }).catch(() => {});
}

async function lazyScroll(page) {
  const h = await page.evaluate(() => document.documentElement.scrollHeight);
  const steps = Math.min(24, Math.ceil(h / 700));
  for (let i = 0; i < steps; i++) {
    await page.evaluate((y) => scrollTo(0, y), i * 700);
    await wait(page, 120);
  }
  await page.evaluate(() => scrollTo(0, 0));
  await wait(page, 400);
}

async function shot(page, file, requested, extra = {}) {
  await pauseMedia(page);
  await screenshotWithMetadata(page, { path: file, ...extra }, requested);
}

async function capturePage(context, spec, prefix, vw, vh, dpr) {
  const page = await context.newPage();
  const requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, sanitizedSourceUrl: spec.url };
  log('open', prefix, spec.url);
  const res = await page.goto(spec.url, { waitUntil: 'domcontentloaded', timeout: 45000 });
  await page.waitForTimeout(spec.app ? 2500 : 1600);
  const title = await page.title();
  const bodyText = (await page.locator('body').innerText({ timeout: 8000 }).catch(() => '')).slice(0, 400);
  const cf = /just a moment|cf-browser-verification|challenge-platform|Attention Required/i.test(title + ' ' + bodyText);
  if (cf) {
    log('  CLOUDFLARE', spec.url, title);
    await page.close();
    return { name: spec.name, url: spec.url, blocked: 'cloudflare', title };
  }
  const cookie = await dismissCookie(page);
  const stem = path.join(RAW_SHOTS, `${prefix}-default`);
  await shot(page, `${stem}.png`, requested);
  log('  viewport', title, 'status', res && res.status(), cookie ? `cookie:${cookie}` : '');

  if (!spec.app) {
    await lazyScroll(page);
    const H = await page.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / dpr);
    const full = path.join(RAW_SHOTS, `${prefix}-full`);
    if (H <= chunk) {
      await shot(page, `${full}.png`, { ...requested, capturedHeight: H }, { fullPage: true, scale: 'css', timeout: 90000 });
    } else {
      const hCap = Math.min(H, 8 * chunk);
      for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
        await shot(page, `${full}.part${i}.png`, { ...requested, capturedHeight: hCap, partIndex: i }, {
          fullPage: true, scale: 'css', timeout: 90000,
          clip: { x: 0, y, width: vw, height: Math.min(chunk, hCap - y) },
        });
      }
      if (H > hCap) log('  truncated', H, 'to', hCap);
    }
    log('  full H', H);
    await page.evaluate(() => scrollTo(0, 0));
  }

  const reading = await page.evaluate(() => {
    const csRoot = getComputedStyle(document.documentElement);
    const vars = {};
    for (let i = 0; i < csRoot.length; i++) {
      const n = csRoot[i];
      if (n.startsWith('--')) vars[n] = csRoot.getPropertyValue(n).trim();
    }
    function pick(el) {
      if (!el) return null;
      const cs = getComputedStyle(el);
      const r = el.getBoundingClientRect();
      return {
        tag: el.tagName,
        text: (el.innerText || el.getAttribute('placeholder') || el.getAttribute('aria-label') || '').trim().slice(0, 80),
        fontFamily: cs.fontFamily,
        fontSize: cs.fontSize,
        fontWeight: cs.fontWeight,
        lineHeight: cs.lineHeight,
        letterSpacing: cs.letterSpacing,
        color: cs.color,
        backgroundColor: cs.backgroundColor,
        borderRadius: cs.borderRadius,
        borderTopWidth: cs.borderTopWidth,
        borderTopColor: cs.borderTopColor,
        borderTopStyle: cs.borderTopStyle,
        padding: cs.padding,
        boxShadow: cs.boxShadow,
        height: Math.round(r.height),
        width: Math.round(r.width),
      };
    }
    const h1 = document.querySelector('h1');
    const h2 = document.querySelector('h2');
    const p = document.querySelector('main p, p');
    const links = [...document.querySelectorAll('a')].slice(0, 30).map((a) => ({
      t: (a.innerText || '').trim().slice(0, 40),
      h: a.getAttribute('href'),
    }));
    const buttons = [...document.querySelectorAll('a,button')].filter((el) => {
      const t = (el.innerText || el.getAttribute('aria-label') || '').trim();
      return /get started|log in|login|create|watch|pricing|features/i.test(t) && t.length < 40;
    }).slice(0, 8).map(pick);
    const inputs = [...document.querySelectorAll('input')].slice(0, 6).map(pick);
    const body = getComputedStyle(document.body);
    return {
      title: document.title,
      url: location.href.split('?')[0],
      w: innerWidth,
      h: innerHeight,
      dpr: devicePixelRatio,
      vv: visualViewport && { w: visualViewport.width, h: visualViewport.height, scale: visualViewport.scale },
      htmlClass: document.documentElement.className,
      bodyClass: document.body.className,
      colorScheme: body.colorScheme,
      body: { fontFamily: body.fontFamily, fontSize: body.fontSize, color: body.color, backgroundColor: body.backgroundColor },
      h1: pick(h1),
      h2: pick(h2),
      p: pick(p),
      buttons,
      inputs,
      links,
      varCount: Object.keys(vars).length,
      vars,
    };
  });
  await page.close();
  return { name: spec.name, prefix, reading, cookie };
}

const browser = await chromium.launch({ headless: true });
const desktop = await browser.newContext({
  viewport: { width: 1440, height: 900 },
  deviceScaleFactor: 1,
  userAgent: UA,
  locale: 'en-US',
});
const mobile = await browser.newContext({
  viewport: { width: 390, height: 844 },
  deviceScaleFactor: 2,
  userAgent: UA_MOBILE,
  isMobile: true,
  hasTouch: true,
  locale: 'en-US',
});

const only = (process.argv[2] || '').split(',').filter(Boolean);
const pages = only.length ? PAGES.filter((p) => only.includes(p.name)) : PAGES;
const readings = [];

for (const spec of pages) {
  try {
    const r = await capturePage(desktop, spec, spec.name + '-light', 1440, 900, 1);
    readings.push(r);
  } catch (e) {
    log('FAILED', spec.name, String(e).split('\n')[0]);
    readings.push({ name: spec.name, error: String(e).split('\n')[0] });
  }
}

const mobilePages = pages.filter((p) => ['home', 'pricing', 'app-login', 'app-create'].includes(p.name));
for (const spec of mobilePages) {
  try {
    const r = await capturePage(mobile, spec, 'mobile-' + spec.name + '-light', 390, 844, 2);
    readings.push(r);
  } catch (e) {
    log('FAILED mobile', spec.name, String(e).split('\n')[0]);
    readings.push({ name: 'mobile-' + spec.name, error: String(e).split('\n')[0] });
  }
}

// App dark: emulate prefers-color-scheme and reload login + create.
const dark = await browser.newContext({
  viewport: { width: 1440, height: 900 },
  deviceScaleFactor: 1,
  userAgent: UA,
  locale: 'en-US',
  colorScheme: 'dark',
});
for (const spec of pages.filter((p) => p.app)) {
  try {
    const r = await capturePage(dark, spec, spec.name + '-dark', 1440, 900, 1);
    readings.push(r);
  } catch (e) {
    log('FAILED dark', spec.name, String(e).split('\n')[0]);
    readings.push({ name: spec.name + '-dark', error: String(e).split('\n')[0] });
  }
}

await browser.close();

const out = {
  capturedAt: new Date().toISOString(),
  viewportPlan: { desktop: [1440, 900], mobile: [390, 844] },
  pages: readings.map((r) => ({
    name: r.name,
    prefix: r.prefix,
    blocked: r.blocked || null,
    error: r.error || null,
    cookie: r.cookie || null,
    reading: r.reading ? {
      title: r.reading.title,
      url: r.reading.url,
      w: r.reading.w,
      h: r.reading.h,
      dpr: r.reading.dpr,
      vv: r.reading.vv,
      htmlClass: r.reading.htmlClass,
      bodyClass: r.reading.bodyClass,
      colorScheme: r.reading.colorScheme,
      body: r.reading.body,
      h1: r.reading.h1,
      h2: r.reading.h2,
      p: r.reading.p,
      buttons: r.reading.buttons,
      inputs: r.reading.inputs,
      links: r.reading.links,
      varCount: r.reading.varCount,
    } : null,
  })),
};
fs.writeFileSync(path.join(RAW, 'pages.json'), JSON.stringify(out, null, 2));

// Keep the richest var dump (app login has the Tamagui scale).
const varDumps = {};
for (const r of readings) {
  if (r.reading && r.reading.vars) varDumps[r.prefix || r.name] = r.reading.vars;
}
fs.writeFileSync(path.join(RAW, 'css-vars.json'), JSON.stringify({
  capturedAt: new Date().toISOString(),
  note: 'Computed custom properties on documentElement, per captured surface. Marketing :root is the small brand set. The app dump is the Tamagui scale as painted (dark tokens resolve even on the light login page).',
  dumps: varDumps,
}, null, 2));
log('wrote', path.join(RAW, 'pages.json'), 'shots', RAW_SHOTS);
