// Captures rox.com public pages into RAW (full-colour PNGs). quantize.py turns them into screenshots/.
//
//   RAW=~/.design-systems/rox/raw-full PLAYWRIGHT=... node shoot.mjs
//
// Desktop 1440x900 at 1x, phone 390x844 at 2x. Names are {page}-light-{state}.png.
// Nothing is typed or submitted. Auth hosts (run.rox.com, Auth0) are never opened.
// Consent and promo overlays are hidden, never answered.
import fs from 'node:fs';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, UA_MOBILE } from './lib.mjs';

const RAW = process.env.RAW || `${process.env.HOME}/.design-systems/rox/raw-full`;
fs.mkdirSync(RAW, { recursive: true });
const only = (process.env.ONLY || '').split(',').filter(Boolean);
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const wait = (p, ms) => p.waitForTimeout(ms);

const PAGES = [
  ['home', '/'],
  ['platform', '/platform'],
  ['pricing', '/pricing'],
  ['customers', '/customers'],
  ['customer', '/customers/mongodb'],
  ['research', '/research'],
  ['resources', '/resources'],
  ['company', '/company'],
  ['contact', '/contact'],
  ['security', '/security'],
  ['downloads', '/downloads'],
  ['academy', '/rox-academy'],
  ['articles', '/articles'],
  ['article', '/articles/announcing-rox-s-series-b-at-a-1.3b-valuation'],
  ['legal', '/legal'],
  ['docs', '/docs/about-rox/readme'],
  ['category', '/platform-categories/agentic-workflows'],
  ['capability', '/featured-agent-capabilities/outbound'],
  ['report', '/reports/gartner-magic-quadrant'],
];

async function hideOverlays(p) {
  await p.evaluate(() => {
    document.querySelectorAll('#onetrust-banner-sdk, [id*="onetrust" i], [class*="cookie" i], [class*="consent" i], [id*="termly" i], #iubenda-cs-banner, .warmly-widget, #warmly-widget').forEach((el) => {
      el.style.setProperty('display', 'none', 'important');
    });
  }).catch(() => {});
}

async function lazyScroll(p) {
  const h = await p.evaluate(() => Math.min(document.documentElement.scrollHeight, 12000));
  for (let y = 0; y < h; y += 700) {
    await p.evaluate((yy) => scrollTo(0, yy), y);
    await wait(p, 120);
  }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 400);
}

async function shot(p, prefix, name, requested, full = false) {
  await hideOverlays(p);
  const path = `${RAW}/${prefix}-${name}.png`;
  if (full) {
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const dpr = requested.deviceScaleFactor;
    const chunk = Math.floor(14000 / dpr);
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log('  boundary', name, H, '->', hCap);
    if (hCap <= chunk) {
      await screenshotWithMetadata(p, { path, fullPage: true }, requested);
    } else {
      for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
        await screenshotWithMetadata(p, {
          path: `${RAW}/${prefix}-${name}.part${i}.png`,
          fullPage: true,
          clip: { x: 0, y, width: requested.viewport.width, height: Math.min(chunk, hCap - y) },
        }, requested);
      }
    }
    await p.evaluate(() => scrollTo(0, 0));
  } else {
    await p.evaluate(() => scrollTo(0, 0));
    await screenshotWithMetadata(p, { path }, requested);
  }
  log('  shot', prefix, name);
}

async function runWidth(mobile) {
  const vw = mobile ? 390 : 1440;
  const vh = mobile ? 844 : 900;
  const dpr = mobile ? 2 : 1;
  const requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr };
  const browser = await chromium.launch({ headless: true });
  for (const [name, path] of PAGES) {
    const prefix = (mobile ? 'mobile-' : '') + name + '-light';
    if (only.length && !only.includes(name) && !only.includes(prefix)) continue;
    const ctx = await browser.newContext({
      viewport: { width: vw, height: vh },
      deviceScaleFactor: dpr,
      userAgent: mobile ? UA_MOBILE : UA,
      isMobile: mobile,
      hasTouch: mobile,
      locale: 'en-US',
    });
    await ctx.addInitScript(() => { Object.defineProperty(navigator, 'webdriver', { get: () => undefined }); });
    const p = await ctx.newPage();
    log(prefix, path);
    try {
      await p.goto('https://www.rox.com' + path, { waitUntil: 'domcontentloaded', timeout: 45000 });
      await wait(p, 1600);
      const title = await p.title();
      if (/just a moment|attention required/i.test(title)) { log('  BLOCKED', title); await ctx.close(); continue; }
      await shot(p, prefix, 'default', requested, false);
      if (!mobile && name === 'home') {
        await p.locator('a').filter({ hasText: /^Platform$/ }).first().hover();
        await wait(p, 700);
        await shot(p, prefix, 'platform-menu', requested, false);
        await p.mouse.move(700, 800);
        await wait(p, 300);
        await p.locator('a').filter({ hasText: /^Resources$/ }).first().hover();
        await wait(p, 600);
        await shot(p, prefix, 'resources-menu', requested, false);
        await p.mouse.move(700, 800);
        await wait(p, 300);
        await p.locator('a').filter({ hasText: /^Company$/ }).first().hover();
        await wait(p, 600);
        await shot(p, prefix, 'company-menu', requested, false);
      }
      if (mobile && name === 'home') {
        const burger = p.locator('.framer-dkldq9').first();
        if (await burger.count()) {
          await burger.click({ timeout: 4000 }).catch(() => {});
          await wait(p, 700);
          await shot(p, prefix, 'menu', requested, false);
        }
      }
      if (name === 'docs') {
        await p.keyboard.press('Control+k');
        await wait(p, 600);
        await shot(p, prefix, 'search', requested, false);
        await p.keyboard.press('Escape');
      }
      if (name === 'contact') {
        const email = p.locator('input[name="Email"]').first();
        if (await email.count()) {
          await email.focus();
          await wait(p, 300);
          await shot(p, prefix, 'focus', requested, false);
        }
      }
      await shot(p, prefix, 'full', requested, true);
    } catch (e) {
      log('  FAIL', prefix, String(e.message).split('\n')[0]);
    }
    await ctx.close();
  }
  await browser.close();
}

await runWidth(false);
await runWidth(true);
log('done');
