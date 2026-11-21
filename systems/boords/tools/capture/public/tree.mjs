// Photographs the public Boords tree from site-tree.md.
//
//   RAW=~/.design-systems/boords/raw PLAYWRIGHT=... node tree.mjs [name,name]
//
// Desktop 1440x900 at 1x, phone 390x844 at 2x. Viewport plus one full-page
// shot per page. Menus, drawers and overlays are viewport shots. Consent is
// hidden, never clicked. Login, signup, newsletter and enterprise forms are
// never typed into or submitted. Google and other SSO buttons are never clicked.
import fs from 'fs';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

const RAW = process.env.RAW || new URL('../../../../../../.design-systems/boords/raw/', import.meta.url).pathname;
fs.mkdirSync(RAW, { recursive: true });
const only = new Set((process.argv[2] || '').split(',').filter(Boolean));
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

class Shooter {
  constructor(p, prefix, vw, vh, dpr) {
    this.p = p; this.prefix = prefix; this.vw = vw; this.vh = vh; this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, sanitizedSourceUrl: null };
  }
  async view(name) {
    await closePromo(this.p);
    const file = `${RAW}/${this.prefix}-${name}.png`;
    await screenshotWithMetadata(this.p, { path: file }, this.requested);
    log('  shot', this.prefix + '-' + name);
  }
  async full(name = 'full') {
    const p = this.p;
    await closePromo(p);
    const h0 = await p.evaluate(() => document.documentElement.scrollHeight);
    for (let y = 0; y < h0; y += 700) {
      await p.evaluate((y) => scrollTo(0, y), y);
      await wait(p, 120);
    }
    await p.evaluate(() => scrollTo(0, 0));
    await wait(p, 400);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px, first ${hCap}px only`);
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else {
      for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
        await screenshotWithMetadata(p, {
          path: `${f}.part${i}.png`, fullPage: true,
          clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) },
        }, this.requested);
      }
    }
    log('  shot', this.prefix + '-' + name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
  }
}

async function go(page, path) {
  const url = path.startsWith('http') ? path : BASE + path;
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
  const ok = await clearChallenge(page);
  await wait(page, 1600);
  await closePromo(page);
  return ok;
}

async function hoverMenu(page, label) {
  const btn = page.locator('button.nav-menu-trigger').filter({ hasText: new RegExp('^' + label + '$') }).first();
  await btn.hover();
  await wait(page, 700);
  const open = await btn.getAttribute('data-state');
  if (open !== 'open') throw new Error(label + ' menu did not open');
}

const desktopPages = [
  ['home', '/'],
  ['pricing', '/pricing'],
  ['demo', '/demo'],
  ['script-editor', '/script-editor'],
  ['storyboard-software', '/storyboard-software'],
  ['animatic-software', '/animatic-software'],
  ['shot-list', '/shot-list-software'],
  ['collaborate', '/collaborate'],
  ['agent', '/agent'],
  ['ai-storyboard', '/ai-storyboard-generator'],
  ['ai-script', '/ai-script-generator'],
  ['mcp', '/mcp'],
  ['integrations', '/integrations'],
  ['enterprise', '/enterprise'],
  ['customers', '/customers'],
  ['customer-mobula', '/customers/mobula'],
  ['docs', '/docs'],
  ['docs-article', '/docs/quick-start'],
  ['script-timer', '/script-timer'],
  ['learn', '/learn'],
  ['blog', '/blog'],
  ['changelog', '/changelog'],
  ['newsletter', '/newsletter'],
  ['about', '/about'],
  ['security', '/security'],
  ['privacy', '/privacy'],
  ['terms', '/terms'],
  ['compare', '/compare'],
  ['storyboard-template', '/storyboard-template'],
  ['video-script-template', '/video-script-template'],
  ['not-found', '/login'],
];

const phonePages = [
  ['home', '/'],
  ['pricing', '/pricing'],
  ['demo', '/demo'],
  ['docs', '/docs'],
  ['customers', '/customers'],
  ['script-timer', '/script-timer'],
  ['blog', '/blog'],
];

async function runDesktop(browser) {
  const ctx = await browser.newContext({
    viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US',
  });
  await patch(ctx);
  const page = await ctx.newPage();
  const S = (prefix) => new Shooter(page, prefix + '-light', 1440, 900, 1);

  for (const [name, path] of desktopPages) {
    if (only.size && !only.has(name) && !only.has('desktop')) continue;
    log('desktop', name);
    try {
      if (!(await go(page, path))) { log('  BLOCKED', path); continue; }
      const shot = S(name);
      await shot.view('default');
      await shot.full();
    } catch (e) { log('  FAILED', name, String(e.message).split('\n')[0]); }
  }

  if (!only.size || only.has('home-features') || only.has('overlays')) {
    log('desktop overlays');
    try {
      await go(page, '/');
      const shot = S('home');
      await hoverMenu(page, 'Features');
      await shot.view('features-menu');
      await page.mouse.move(10, 800);
      await wait(page, 300);
      await hoverMenu(page, 'Resources');
      await shot.view('resources-menu');
      await page.keyboard.press('Escape');
      await wait(page, 300);
      const watch = page.getByRole('button', { name: /Watch the 34s overview/ }).first();
      if (await watch.count()) {
        await watch.click();
        await wait(page, 1200);
        await shot.view('video-overlay');
        await page.keyboard.press('Escape');
      }
    } catch (e) { log('  FAILED overlays', String(e.message).split('\n')[0]); }
  }

  if (!only.size || only.has('pricing-yearly')) {
    log('desktop pricing yearly');
    try {
      await go(page, '/pricing');
      const tab = page.locator('button[role="tab"]').filter({ hasText: /year/i }).first();
      if (await tab.count()) { await tab.click(); await wait(page, 700); }
      await S('pricing').view('yearly');
    } catch (e) { log('  FAILED yearly', e.message.split('\n')[0]); }
  }

  if (!only.size || only.has('customers-founders')) {
    log('desktop customers founders');
    try {
      await go(page, '/customers');
      const b = page.getByRole('button', { name: /Founders/ }).first();
      if (await b.count()) { await b.click(); await wait(page, 500); }
      await S('customers').view('founders');
    } catch (e) { log('  FAILED founders', e.message.split('\n')[0]); }
  }

  if (!only.size || only.has('docs-dark')) {
    log('desktop docs dark');
    try {
      await go(page, '/docs');
      await page.getByRole('radio', { name: 'Dark' }).click();
      await wait(page, 500);
      const dark = new Shooter(page, 'docs-dark', 1440, 900, 1);
      await dark.view('default');
      await go(page, '/docs/quick-start');
      const cls = await page.evaluate(() => document.documentElement.className);
      if (!/\bdark\b/.test(cls)) await page.getByRole('radio', { name: 'Dark' }).click();
      await wait(page, 400);
      const article = new Shooter(page, 'docs-article-dark', 1440, 900, 1);
      await article.view('default');
    } catch (e) { log('  FAILED docs dark', e.message.split('\n')[0]); }
  }

  if (!only.size || only.has('integrations-tab')) {
    log('desktop integrations tab');
    try {
      await go(page, '/integrations');
      const tab = page.getByRole('tab', { name: 'Premiere Pro' }).first();
      if (await tab.count()) { await tab.click(); await wait(page, 400); }
      await S('integrations').view('premiere');
    } catch (e) { log('  FAILED integrations', e.message.split('\n')[0]); }
  }

  if (!only.size || only.has('script-timer-filled')) {
    log('desktop timer filled');
    try {
      await go(page, '/script-timer');
      const ta = page.locator('textarea').first();
      if (await ta.count()) {
        await ta.fill('A studio. Three frames. The timer counts the words and shows a running time. Nothing is submitted.');
        await wait(page, 500);
        await S('script-timer').view('filled');
      }
    } catch (e) { log('  FAILED timer', e.message.split('\n')[0]); }
  }

  if (!only.size || only.has('login-wall')) {
    log('login wall record only');
    try {
      await page.goto('https://app.boords.com/login', { waitUntil: 'domcontentloaded', timeout: 60000 });
      await wait(page, 2000);
      await S('login-wall').view('default');
      log('  recorded https://app.boords.com/login and stopped. no typing.');
    } catch (e) { log('  FAILED login wall', e.message.split('\n')[0]); }
  }

  await ctx.close();
}

async function runPhone(browser) {
  const ctx = await browser.newContext({
    viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE,
    isMobile: true, hasTouch: true, locale: 'en-US',
  });
  await patch(ctx);
  const page = await ctx.newPage();
  for (const [name, path] of phonePages) {
    const key = 'mobile-' + name;
    if (only.size && !only.has(key) && !only.has('phone')) continue;
    log('phone', name);
    try {
      if (!(await go(page, path))) { log('  BLOCKED', path); continue; }
      const shot = new Shooter(page, key + '-light', 390, 844, 2);
      await shot.view('default');
      await shot.full();
    } catch (e) { log('  FAILED', key, e.message.split('\n')[0]); }
  }
  if (!only.size || only.has('mobile-menu')) {
    log('phone menu');
    try {
      await go(page, '/');
      const shot = new Shooter(page, 'mobile-home-light', 390, 844, 2);
      await page.locator('button[aria-label="Open menu"]').click();
      await wait(page, 800);
      await shot.view('menu');
      await page.getByRole('button', { name: 'Features' }).first().click();
      await wait(page, 500);
      await shot.view('features');
      await page.getByRole('button', { name: 'Back' }).first().click().catch(() => {});
      await wait(page, 300);
      await page.getByRole('button', { name: 'Resources' }).first().click();
      await wait(page, 500);
      await shot.view('resources');
    } catch (e) { log('  FAILED phone menu', e.message.split('\n')[0]); }
  }
  if (!only.size || only.has('mobile-docs-dark')) {
    log('phone docs dark');
    try {
      await go(page, '/docs');
      const dark = page.getByRole('radio', { name: 'Dark' });
      if (await dark.count()) await dark.click();
      await wait(page, 400);
      await new Shooter(page, 'mobile-docs-dark', 390, 844, 2).view('default');
    } catch (e) { log('  FAILED phone docs', e.message.split('\n')[0]); }
  }
  await ctx.close();
}

const browser = await chromium.launch();
try {
  await runDesktop(browser);
  await runPhone(browser);
} finally {
  await browser.close();
}
log('done ->', RAW);
