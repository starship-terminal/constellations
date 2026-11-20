// Signed-in Krisp app capture for a free account.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node app.mjs
//
// Session is ~/.design-systems/krisp/session.json (mode 600, never git).
// Chromium profile: ~/.design-systems/krisp/chrome-profile.
// Shots: ~/.design-systems/krisp/raw-shots-app
//
// Does not download the desktop app, connect a calendar, buy a plan,
// change email, enable 2FA, delete the account, or click OneTrust.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from '../screenshot.mjs';

const pw = await import(process.env.PLAYWRIGHT || path.join(os.homedir(), '.design-systems/pw/node_modules/playwright/index.mjs'));
const { chromium } = pw.default ?? pw;

const HERE = path.dirname(fileURLToPath(import.meta.url));
const PKG = path.resolve(HERE, '..', '..', '..');
const HOME = os.homedir();
const RAW = process.env.RAW || path.join(HOME, '.design-systems', 'krisp', 'raw-shots-app');
const SESSION = path.join(HOME, '.design-systems', 'krisp', 'session.json');
const PROFILE = path.join(HOME, '.design-systems', 'krisp', 'chrome-profile');
const PKG_RAW = path.join(PKG, 'raw');
fs.mkdirSync(RAW, { recursive: true });
fs.mkdirSync(PROFILE, { recursive: true });

const session = JSON.parse(fs.readFileSync(SESSION, 'utf8'));
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
const UA_MOBILE = 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';

const PAGES = [
  { id: 'app-setup', path: '/setup' },
  { id: 'app-notes', path: '/meeting-notes', full: true },
  { id: 'app-action-items', path: '/action-items', full: true },
  { id: 'app-settings-account', path: '/settings/account', full: true },
  { id: 'app-settings-note-taker', path: '/settings/ai-note-taker', full: true },
  { id: 'app-settings-templates', path: '/settings/templates' },
  { id: 'app-settings-integrations', path: '/settings/integrations', full: true },
  { id: 'app-settings-privacy', path: '/settings/privacy-and-consent' },
  { id: 'app-settings-personalization', path: '/settings/personalization' },
  { id: 'app-settings-calendar', path: '/settings/calendar' },
  { id: 'app-settings-app', path: '/settings/app', full: true },
  { id: 'app-settings-notification', path: '/settings/notification' },
  { id: 'app-settings-users', path: '/settings/users' },
  { id: 'app-connect-calendar', path: '/connect-calendar' },
  { id: 'app-billing', path: '/billing-team', full: true },
];

const MOBILE = ['app-setup', 'app-notes', 'app-action-items', 'app-settings-account', 'app-connect-calendar', 'app-billing'];

async function hideConsent(page) {
  await page.evaluate(() => {
    const css = '#onetrust-consent-sdk,#onetrust-banner-sdk,.onetrust-pc-dark-filter,#onetrust-pc-sdk,[id^=hs-web-interactives]{display:none!important;visibility:hidden!important;pointer-events:none!important}';
    if (!document.getElementById('m-hide-consent')) {
      const s = document.createElement('style');
      s.id = 'm-hide-consent';
      s.textContent = css;
      document.documentElement.appendChild(s);
    }
  }).catch(() => {});
}

async function ready(page) {
  await wait(page, 1200);
  await hideConsent(page);
  for (let i = 0; i < 12; i++) {
    const n = await page.evaluate(() => (document.body.innerText || '').replace(/\s+/g, ' ').trim().length);
    if (n > 40) break;
    await wait(page, 400);
  }
  await hideConsent(page);
  await wait(page, 400);
}

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  for (let y = 0; y < Math.min(h, 8000); y += 700) {
    await p.evaluate((y) => scrollTo(0, y), y);
    await wait(p, 160);
  }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 400);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr) {
    this.p = p;
    this.prefix = prefix;
    this.vw = vw;
    this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr };
    this.count = 0;
  }
  async view(name, url) {
    const requested = { ...this.requested, sanitizedSourceUrl: url ? `https://app.krisp.ai${url.split('?')[0]}` : null };
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, requested);
    this.count++;
    log('  shot', `${this.prefix}-${name}`);
  }
  async full(name = 'full', url) {
    const p = this.p;
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    const requested = { ...this.requested, sanitizedSourceUrl: url ? `https://app.krisp.ai${url.split('?')[0]}` : null };
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, requested);
    else {
      for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
        await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, requested);
      }
    }
    this.count++;
    log('  shot', `${this.prefix}-${name}`, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
    await wait(p, 300);
  }
}

async function applySession(context) {
  await context.addCookies(session.cookies);
  await context.addInitScript((ls) => {
    for (const [k, v] of Object.entries(ls)) localStorage.setItem(k, v);
  }, session.localStorage);
}

async function dumpVars(page, theme) {
  return page.evaluate((theme) => {
    const root = getComputedStyle(document.documentElement);
    const wanted = [];
    for (const sheet of document.styleSheets) {
      let rules;
      try { rules = [...sheet.cssRules]; } catch { continue; }
      for (const rule of rules) {
        if (!rule.style) continue;
        for (let i = 0; i < rule.style.length; i++) {
          const k = rule.style[i];
          if (k.startsWith('--') && !/^--\d/.test(k)) wanted.push(k);
        }
      }
    }
    const uniq = [...new Set(wanted)].sort();
    const vars = {};
    for (const k of uniq) {
      const v = root.getPropertyValue(k).trim();
      if (v) vars[k] = v;
    }
    const pick = (sel) => {
      const el = document.querySelector(sel);
      if (!el) return null;
      const s = getComputedStyle(el);
      const r = el.getBoundingClientRect();
      return {
        sel, tag: el.tagName.toLowerCase(),
        rect: { x: r.x, y: r.y, w: r.width, h: r.height },
        style: {
          color: s.color, backgroundColor: s.backgroundColor, borderTopColor: s.borderTopColor,
          borderTopWidth: s.borderTopWidth, borderTopLeftRadius: s.borderTopLeftRadius,
          fontFamily: s.fontFamily, fontSize: s.fontSize, fontWeight: s.fontWeight,
          lineHeight: s.lineHeight, height: s.height, paddingTop: s.paddingTop, paddingRight: s.paddingRight,
        },
      };
    };
    return {
      theme,
      url: location.pathname,
      dataTheme: document.documentElement.getAttribute('data-theme'),
      colorScheme: getComputedStyle(document.documentElement).colorScheme,
      prefersDark: matchMedia('(prefers-color-scheme: dark)').matches,
      font: getComputedStyle(document.body).fontFamily,
      pageBg: getComputedStyle(document.body).backgroundColor,
      canvas: vars['--canvas-lighter-1'] || null,
      surface: vars['--surface-lighter-1'] || null,
      vars,
      components: {
        sidebar: pick('aside, [class*=sidebar], [data-test-id*=Sidebar]'),
        primaryBtn: pick('button.btn-v2-primary, .btn-v2-primary, button[class*=primary]'),
        back: pick('button'),
        input: pick('input:not([type=hidden])'),
        nav: pick('[class*=navigation], nav'),
      },
    };
  }, theme);
}

async function captureRun({ mobile, theme, pages }) {
  const vw = mobile ? 390 : 1440;
  const vh = mobile ? 844 : 900;
  const dpr = mobile ? 2 : 1;
  const prefixExtra = mobile ? 'mobile-' : '';
  log(`run ${prefixExtra}${theme} ${vw}x${vh}@${dpr}`);

  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({
    viewport: { width: vw, height: vh },
    deviceScaleFactor: dpr,
    userAgent: mobile ? UA_MOBILE : UA,
    isMobile: mobile,
    hasTouch: mobile,
    locale: 'en-US',
    colorScheme: theme,
  });
  await applySession(context);
  const page = await context.newPage();
  await page.emulateMedia({ colorScheme: theme });
  const readings = [];

  for (const spec of pages) {
    const prefix = `${prefixExtra}${spec.id}-${theme}`;
    log(prefix);
    try {
      await page.goto('https://app.krisp.ai' + spec.path, { waitUntil: 'load', timeout: 60000 });
      await ready(page);
      const landed = await page.evaluate(() => location.pathname);
      const S = new Shooter(page, prefix, vw, vh, dpr);
      await S.view('default', landed);
      if (spec.full && !mobile) await S.full('full', landed);
      if (!mobile && (spec.id === 'app-notes' || spec.id === 'app-settings-account')) {
        readings.push(await dumpVars(page, theme));
      }
    } catch (e) {
      log('  FAILED', spec.id, String(e.message).split('\n')[0]);
    }
  }

  await context.close();
  await browser.close();
  return readings;
}

const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const desktopPages = PAGES.filter((p) => !pageArg.length || pageArg.includes(p.id) || pageArg.includes('desktop-' + p.id));
const mobilePages = PAGES.filter((p) => MOBILE.includes(p.id) && (!pageArg.length || pageArg.includes(p.id) || pageArg.includes('mobile-' + p.id)));

const readings = [];
readings.push(...await captureRun({ mobile: false, theme: 'light', pages: desktopPages }));
readings.push(...await captureRun({ mobile: false, theme: 'dark', pages: desktopPages.filter((p) => ['app-setup', 'app-notes', 'app-action-items', 'app-settings-account', 'app-billing', 'app-connect-calendar'].includes(p.id)) }));
readings.push(...await captureRun({ mobile: true, theme: 'light', pages: mobilePages }));
readings.push(...await captureRun({ mobile: true, theme: 'dark', pages: mobilePages.filter((p) => ['app-notes', 'app-settings-account'].includes(p.id)) }));

fs.mkdirSync(PKG_RAW, { recursive: true });
fs.writeFileSync(path.join(PKG_RAW, 'app-css-vars.json'), JSON.stringify({
  capturedAt: new Date().toISOString(),
  note: 'Computed custom properties on the signed-in app. Values that look like an email, a token or an id are dropped.',
  readings: readings.map((r) => {
    // Filter on the value, not the name: a design var such as --*-token-* or --author* stays, and
    // an address, a JWT or a long opaque id is dropped whatever its name.
    const vars = {};
    for (const [k, v] of Object.entries(r.vars || {})) {
      const val = String(v);
      if (/[^\s@"']+@[^\s@"']+\.[a-z]{2,}/i.test(val) || /\beyJ[\w-]{10,}/.test(val) || /\b[0-9a-f]{24,}\b/i.test(val) || /\b[\w-]{32,}\b/.test(val)) continue;
      vars[k] = v;
    }
    return { ...r, vars };
  }),
}, null, 2) + '\n');

log('done shots ->', RAW);
