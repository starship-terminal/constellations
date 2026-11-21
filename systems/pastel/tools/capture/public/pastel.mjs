// Pastel public capture. Headless Playwright only. Never types an email, phone,
// password, name, or URL into a field, never submits a form, never clicks
// Login, Sign up, Google, Apple, SSO, or Intercom.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs \
//     node tools/capture/public/pastel.mjs [names...]
//
// Writes full-colour PNGs to ~/.design-systems/pastel/raw-shots/ and a
// readings JSON beside them. quantize.py turns the PNGs into screenshots/.

import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from '../screenshot.mjs';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;

const HERE = path.dirname(fileURLToPath(import.meta.url));
const PKG = path.resolve(HERE, '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'pastel', 'raw-shots');
const READINGS = path.join(PKG, 'raw', 'readings.json');
fs.mkdirSync(RAW, { recursive: true });
fs.mkdirSync(path.dirname(READINGS), { recursive: true });

const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
const UA_MOBILE = 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';

const only = new Set((process.argv[2] || '').split(',').filter(Boolean));
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);

const PAGES = [
  ['home', 'https://usepastel.com/'],
  ['features', 'https://usepastel.com/features'],
  ['agents', 'https://usepastel.com/agents'],
  ['plans', 'https://usepastel.com/plans'],
  ['faq', 'https://usepastel.com/faq'],
  ['markup-alternative', 'https://usepastel.com/markup-alternative'],
  ['terms', 'https://usepastel.com/terms'],
  ['privacy', 'https://usepastel.com/privacy'],
  ['blog', 'https://usepastel.com/blog'],
  ['reviews', 'https://usepastel.com/reviews'],
  ['sitemap', 'https://usepastel.com/sitemap'],
  ['blog-post', 'https://usepastel.com/blog/approvals'],
  ['blog-tag', 'https://usepastel.com/blog-tag/product-features'],
  ['website-annotation-tool', 'https://usepastel.com/website-annotation-tool'],
  ['pdf-annotation-tool', 'https://usepastel.com/pdf-annotation-tool'],
  ['email-tool', 'https://usepastel.com/email'],
  ['design-reviews', 'https://usepastel.com/design-reviews'],
  ['website-qa', 'https://usepastel.com/website-qa-testing'],
  ['client-approval', 'https://usepastel.com/client-project-approval'],
  ['copy-changes', 'https://usepastel.com/copy-changes'],
  ['adobe-xd', 'https://usepastel.com/adobe-xd'],
  ['marker', 'https://usepastel.com/marker-illustrations'],
  ['bugherd', 'https://usepastel.com/bugherd-alternative'],
  ['broken-links', 'https://usepastel.com/broken-link-checker'],
  ['hourly', 'https://usepastel.com/hourly-rate-calculator'],
  ['responsive', 'https://usepastel.com/responsive-website-test'],
  ['box-shadow', 'https://usepastel.com/box-shadow-generator'],
  ['compare-pixels', 'https://usepastel.com/compare-pixels'],
  ['on-demo', 'https://usepastel.com/on'],
  ['on-any-website', 'https://usepastel.com/on-any-website'],
  ['customers', 'https://usepastel.com/customers'],
  ['customer', 'https://usepastel.com/customers/calendly'],
  ['teams', 'https://usepastel.com/teams'],
  ['about', 'https://usepastel.com/about'],
  ['how-it-works', 'https://usepastel.com/how-it-works'],
  ['website-revisions', 'https://usepastel.com/website-revisions'],
  ['trackduck', 'https://usepastel.com/trackduck-alternative'],
  ['help', 'https://help.usepastel.com/en/'],
  ['help-using', 'https://help.usepastel.com/en/collections/1169706-using-pastel'],
  ['status', 'https://status.usepastel.com/'],
  // Walls: load, record, do not interact with the form.
  ['login', 'https://usepastel.com/login'],
  ['signup', 'https://usepastel.com/signup'],
];

const FULL = new Set(['home', 'features', 'plans', 'faq', 'blog', 'customers', 'help', 'status', 'agents']);

function safeUrl(u) {
  try {
    const x = new URL(u);
    x.search = '';
    x.hash = '';
    return x.origin + x.pathname;
  } catch {
    return null;
  }
}

async function hideThirdParty(page) {
  await page.addStyleTag({
    content: `
      #intercom-container, .intercom-lightweight-app, .intercom-launcher,
      iframe[name*="intercom"], [class*="intercom-"] { display: none !important; }
      iframe[src*="youtube.com"] { visibility: hidden !important; }
    `,
  }).catch(() => {});
}

async function shot(page, file, requested, extra = {}) {
  await screenshotWithMetadata(page, { path: file, ...extra }, requested);
}

async function fullPage(page, prefix, requested) {
  const H = await page.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
  const vw = requested.viewport.width;
  const dpr = requested.deviceScaleFactor;
  const chunk = Math.floor(14000 / dpr);
  const MAXH = 8 * chunk;
  const hCap = Math.min(H, MAXH);
  const f = `${prefix}-full`;
  for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(path.basename(f) + '.part'))) fs.unlinkSync(path.join(RAW, old));
  if (H > MAXH) log('  truncated', H, 'to', hCap);
  if (hCap <= chunk) {
    await shot(page, f + '.png', requested, { fullPage: true });
  } else {
    for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
      await shot(page, `${f}.part${i}.png`, requested, {
        fullPage: true,
        clip: { x: 0, y, width: vw, height: Math.min(chunk, hCap - y) },
      });
    }
  }
  await page.evaluate(() => scrollTo(0, 0)).catch(() => {});
  return { scrollHeight: H, capturedHeight: hCap, truncated: H > MAXH };
}

async function readFoundations(page) {
  return page.evaluate(() => {
    const cs = getComputedStyle(document.body);
    const root = getComputedStyle(document.documentElement);
    const vars = {};
    for (const sheet of document.styleSheets) {
      let rules;
      try { rules = sheet.cssRules; } catch { continue; }
      const walk = (list) => {
        for (const r of list) {
          if (r.cssRules && !r.style) { try { walk(r.cssRules); } catch { /* cross-origin */ } continue; }
          if (!r.style) continue;
          for (let i = 0; i < r.style.length; i++) {
            const k = r.style[i];
            if (k.startsWith('--') && !(k in vars)) vars[k] = r.style.getPropertyValue(k).trim().slice(0, 180);
          }
        }
      };
      try { walk(rules); } catch { /* ignore */ }
    }
    const pick = (el) => {
      if (!el) return null;
      const c = getComputedStyle(el);
      const r = el.getBoundingClientRect();
      return {
        text: (el.innerText || el.getAttribute('aria-label') || '').trim().replace(/\s+/g, ' ').slice(0, 60),
        fontFamily: c.fontFamily,
        fontSize: c.fontSize,
        fontWeight: c.fontWeight,
        lineHeight: c.lineHeight,
        letterSpacing: c.letterSpacing,
        color: c.color,
        backgroundColor: c.backgroundColor,
        borderRadius: c.borderRadius,
        padding: `${c.paddingTop} ${c.paddingRight} ${c.paddingBottom} ${c.paddingLeft}`,
        height: c.height,
        boxShadow: c.boxShadow,
        border: `${c.borderTopWidth} ${c.borderTopStyle} ${c.borderTopColor}`,
        rect: { x: +r.x.toFixed(1), y: +r.y.toFixed(1), w: +r.width.toFixed(1), h: +r.height.toFixed(1) },
      };
    };
    const first = (sel) => document.querySelector(sel);
    const h1 = first('h1');
    const cta = [...document.querySelectorAll('a, button')].find((a) => /start a free trial|get started|sign up free|try pastel/i.test(a.innerText || '') && a.getBoundingClientRect().width > 40);
    const nav = first('a.navbar-button, .navbar a, header a, nav a');
    return {
      body: {
        fontFamily: cs.fontFamily,
        fontSize: cs.fontSize,
        lineHeight: cs.lineHeight,
        color: cs.color,
        backgroundColor: cs.backgroundColor,
      },
      rootBg: root.backgroundColor,
      rootColor: root.color,
      vars,
      h1: pick(h1),
      cta: pick(cta),
      nav: pick(nav),
      viewport: { w: innerWidth, h: innerHeight, dpr: devicePixelRatio },
    };
  });
}

const readings = fs.existsSync(READINGS) ? JSON.parse(fs.readFileSync(READINGS, 'utf8')) : { pages: {}, capturedAt: new Date().toISOString() };

const browser = await chromium.launch({ headless: true });

async function runWidth(mobile) {
  const width = mobile ? 390 : 1440;
  const height = mobile ? 844 : 900;
  const dpr = mobile ? 2 : 1;
  const prefix0 = mobile ? 'mobile-' : '';
  const context = await browser.newContext({
    viewport: { width, height },
    deviceScaleFactor: dpr,
    userAgent: mobile ? UA_MOBILE : UA,
    isMobile: mobile,
    hasTouch: mobile,
    locale: 'en-US',
  });
  const requested = { viewport: { width, height }, deviceScaleFactor: dpr };

  for (const [name, url] of PAGES) {
    const key = prefix0 + name;
    if (only.size && !only.has(key) && !only.has(name)) continue;
    const page = await context.newPage();
    log(key, url);
    try {
      const res = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 50000 });
      await page.waitForTimeout(1600);
      await hideThirdParty(page);
      const final = safeUrl(page.url());
      const wall = /\/login|\/signup/.test(final || '') || name === 'login' || name === 'signup';
      const file = path.join(RAW, `${key}-light-default.png`);
      await shot(page, file, { ...requested, sanitizedSourceUrl: safeUrl(url) });
      const foundations = await readFoundations(page);
      const row = {
        url: safeUrl(url),
        final,
        status: res?.status() ?? null,
        wall,
        width,
        height,
        dpr,
        foundations,
      };
      if (!wall && FULL.has(name)) {
        row.full = await fullPage(page, path.join(RAW, `${key}-light`), requested);
      }
      if (!wall && name === 'plans' && !mobile) {
        const annual = page.locator('.toggle-text.annual');
        if (await annual.count()) {
          await annual.click();
          await page.waitForTimeout(500);
          await shot(page, path.join(RAW, `${key}-light-annual.png`), { ...requested, sanitizedSourceUrl: safeUrl(url) });
          row.annualClicked = true;
        }
      }
      if (!wall && name === 'faq' && !mobile) {
        const q = page.locator('.faq-accordion-question').first();
        if (await q.count()) {
          await q.click();
          await page.waitForTimeout(400);
          await shot(page, path.join(RAW, `${key}-light-open.png`), { ...requested, sanitizedSourceUrl: safeUrl(url) });
          row.faqOpened = true;
        }
      }
      if (!wall && name === 'home' && mobile) {
        const btn = page.locator('.nav-menu-button');
        if (await btn.count()) {
          await btn.click();
          await page.waitForTimeout(500);
          await shot(page, path.join(RAW, `${key}-light-menu.png`), { ...requested, sanitizedSourceUrl: safeUrl(url) });
          row.menuOpened = true;
        }
      }
      if (!wall && name === 'blog' && mobile) {
        const btn = page.locator('.menu-mob, .w-nav-button').first();
        if (await btn.count()) {
          await btn.click();
          await page.waitForTimeout(500);
          await shot(page, path.join(RAW, `${key}-light-menu.png`), { ...requested, sanitizedSourceUrl: safeUrl(url) });
          row.menuOpened = true;
        }
      }
      if (!wall && name === 'status' && !mobile) {
        const graph = page.getByRole('button', { name: /Read uptime graph/ }).first();
        if (await graph.count()) {
          await graph.click();
          await page.waitForTimeout(600);
          await shot(page, path.join(RAW, `${key}-light-graph.png`), { ...requested, sanitizedSourceUrl: safeUrl(url) });
          row.graphOpened = true;
        }
      }
      readings.pages[key] = row;
      fs.writeFileSync(READINGS, JSON.stringify(readings, null, 1) + '\n');
      log('  ok', final, wall ? 'WALL' : '');
    } catch (e) {
      log('  FAIL', e.message.split('\n')[0]);
      readings.pages[key] = { url: safeUrl(url), error: e.message.split('\n')[0] };
      fs.writeFileSync(READINGS, JSON.stringify(readings, null, 1) + '\n');
    }
    await page.close();
  }
  await context.close();
}

await runWidth(false);
await runWidth(true);
await browser.close();
log('done', Object.keys(readings.pages).length, 'pages ->', RAW);
