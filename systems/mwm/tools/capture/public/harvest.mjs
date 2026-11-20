// One-shot harvest for MWM's public signed-out surfaces.
// Writes raw readings under RAW (default ~/.design-systems/mwm/raw-shots) and
// copies the JSON the package keeps into systems/mwm/raw/.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node harvest.mjs
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from '../screenshot.mjs';

const PLAYWRIGHT = process.env.PLAYWRIGHT;
if (!PLAYWRIGHT) { console.error('set PLAYWRIGHT'); process.exit(2); }
const { chromium } = await import(PLAYWRIGHT);

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'mwm', 'raw-shots');
const KEEP = path.join(PKG, 'raw');
fs.mkdirSync(RAW, { recursive: true });
fs.mkdirSync(KEEP, { recursive: true });

const PAGES = [
  ['home', 'https://mwm.ai/'],
  ['pricing', 'https://mwm.ai/pricing'],
  ['mwm-ai', 'https://mwm.ai/mwm-ai'],
  ['mwm-console', 'https://mwm.ai/mwm-console'],
  ['company', 'https://mwm.ai/company'],
  ['apps', 'https://mwm.ai/apps/'],
  ['console-sign-in', 'https://console.mwm.ai/'],
  ['create-sign-in', 'https://create.mwm.ai/'],
];

const PROBE = `(() => {
  const root = getComputedStyle(document.documentElement);
  const names = new Set();
  const declared = [];
  const reduced = [];
  const keyframes = [];
  function walk(list, href) {
    if (!list) return;
    for (const r of list) {
      if (r.type === CSSRule.KEYFRAMES_RULE && keyframes.length < 40) keyframes.push(r.name);
      const media = r.conditionText || (r.media && r.media.mediaText) || '';
      if (r.cssRules && /prefers-reduced-motion/.test(media) && reduced.length < 12) reduced.push(media.slice(0, 140));
      if (r.style) {
        const props = {};
        for (let i = 0; i < r.style.length; i++) {
          const n = r.style[i];
          if (n.startsWith('--') && !n.startsWith('--tw-') && !n.startsWith('--p-')) {
            names.add(n);
            props[n] = r.style.getPropertyValue(n).trim().slice(0, 160);
          }
        }
        const sel = r.selectorText || '';
        if (Object.keys(props).length && /:root|mwm-theme|html/.test(sel) && declared.length < 8) {
          declared.push({ selector: sel.slice(0, 80), href: href ? href.split('/').pop() : null, props });
        }
      }
      if (r.cssRules) walk(r.cssRules, href);
    }
  }
  const sheets = [];
  for (const s of document.styleSheets) {
    let n = 0, err = null;
    try { n = s.cssRules.length; walk(s.cssRules, s.href); } catch (e) { err = String(e.message).slice(0, 80); }
    sheets.push({ href: s.href, rules: n, err });
  }
  const resolved = {};
  for (const n of [...names].sort()) {
    const v = root.getPropertyValue(n).trim();
    if (v) resolved[n] = v.slice(0, 180);
  }
  const fonts = new Set();
  for (const s of document.styleSheets) {
    let rules; try { rules = s.cssRules; } catch (e) { continue; }
    const walkF = (list) => { for (const r of list) { if (r.type === CSSRule.FONT_FACE_RULE) fonts.add(r.style.getPropertyValue('font-family')); if (r.cssRules) walkF(r.cssRules); } };
    walkF(rules);
  }
  return {
    href: location.href.split('?')[0],
    title: document.title,
    inner: [innerWidth, innerHeight],
    dpr: devicePixelRatio,
    colorScheme: root.colorScheme,
    bodyBg: getComputedStyle(document.body).backgroundColor,
    bodyColor: getComputedStyle(document.body).color,
    bodyFont: getComputedStyle(document.body).fontFamily,
    themeColor: (document.querySelector('meta[name=theme-color]') || {}).content || null,
    favicon: [...document.querySelectorAll('link[rel*=icon]')].map(l => l.href),
    challenge: /just a moment|cf-challenge|checking your browser/i.test(document.body.innerText.slice(0, 400)),
    text: document.body.innerText.replace(/\\s+/g, ' ').slice(0, 500),
    resolved, declared, reduced, keyframes, fonts: [...fonts], sheets,
  };
})()`;

function log(...a) { console.log(new Date().toISOString().slice(11, 19), ...a); }

const browser = await chromium.launch({ headless: true });
const readings = {};
for (const [name, url] of PAGES) {
  const ctx = await browser.newContext({
    viewport: { width: 1440, height: 900 },
    deviceScaleFactor: 1,
    locale: 'en-US',
    userAgent: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
  });
  const page = await ctx.newPage();
  log('open', name, url);
  try {
    await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 45000 });
    await page.waitForTimeout(2500);
    const title = await page.title();
    const body = await page.evaluate(() => document.body.innerText.slice(0, 180));
    if (/just a moment|checking your browser|cf-challenge/i.test(title + body)) {
      log('  BLOCKED', name);
      readings[name] = { blocked: true, url, title };
    } else {
      const probe = await page.evaluate(PROBE);
      readings[name] = probe;
      const shot = path.join(RAW, name + '-dark-default.png');
      await screenshotWithMetadata(page, { path: shot, fullPage: false }, {
        viewport: { width: 1440, height: 900 },
        deviceScaleFactor: 1,
        sanitizedSourceUrl: url,
      });
      log('  ok', probe.href, 'vars', Object.keys(probe.resolved).length);
    }
  } catch (e) {
    log('  FAIL', name, String(e.message).split('\n')[0]);
    readings[name] = { error: String(e.message).split('\n')[0], url };
  }
  await ctx.close();
}

// Phone width of the marketing home, one shot.
{
  const ctx = await browser.newContext({
    viewport: { width: 390, height: 844 },
    deviceScaleFactor: 2,
    isMobile: true,
    hasTouch: true,
    locale: 'en-US',
    userAgent: 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1',
  });
  const page = await ctx.newPage();
  log('open mobile home');
  try {
    await page.goto('https://mwm.ai/', { waitUntil: 'domcontentloaded', timeout: 45000 });
    await page.waitForTimeout(2500);
    const shot = path.join(RAW, 'mobile-home-dark-default.png');
    await screenshotWithMetadata(page, { path: shot }, {
      viewport: { width: 390, height: 844 },
      deviceScaleFactor: 2,
      sanitizedSourceUrl: 'https://mwm.ai/',
    });
    const inner = await page.evaluate(() => [innerWidth, innerHeight, devicePixelRatio]);
    readings.mobileHome = { inner };
    log('  mobile', inner.join('x'));
  } catch (e) { log('  mobile FAIL', e.message.split('\n')[0]); }
  await ctx.close();
}
await browser.close();

const out = path.join(KEEP, 'pages.json');
fs.writeFileSync(out, JSON.stringify(readings, null, 1) + '\n');
log('wrote', out);
