// Captures lottiefiles.com public pages into RAW (full-colour PNGs).
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node public.mjs [name,name]
//
// Desktop 1440x900 at 1x. Phone 390x844 at 2x, names prefixed mobile-.
// Nothing is submitted. Login and signup are recorded as walls and not typed into.
// The cookie banner is hidden, never accepted.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, UA_MOBILE, BASE, hideConsent, LAUNCH_OPTS } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', path.basename(PKG), 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  const cap = Math.min(h, 4800);
  for (let y = 0; y < cap; y += 700) {
    await p.evaluate((y) => scrollTo(0, y), y);
    await wait(p, 180);
  }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 400);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr) {
    this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr };
    this.count = 0;
  }
  async view(name) {
    await hideConsent(this.p);
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    this.count++;
    log('  shot', this.prefix + '-' + name);
  }
  async full(name = 'full') {
    const p = this.p;
    await lazyScroll(p);
    await hideConsent(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const MAXH = 4 * chunk;
    const hCap = Math.min(H, MAXH);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(path.basename(f) + '.part'))) fs.unlinkSync(`${RAW}/${old}`);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px, capturing first ${hCap}px`);
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
      await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    }
    this.count++;
    log('  shot', this.prefix + '-' + name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
  }
}

const step = async (label, fn) => {
  try { await fn(); }
  catch (e) { log('  FAILED', label, String(e.message || e).split('\n')[0]); }
};

async function hoverMenu(p, name) {
  const btn = p.getByRole('button', { name, exact: true }).first();
  const box = await btn.boundingBox();
  if (!box) throw new Error('no box ' + name);
  await p.mouse.move(box.x + box.width / 2, box.y + box.height / 2);
  await wait(p, 700);
}

const PAGES = [
  ['home', '/'],
  ['pricing', '/pricing'],
  ['platform', '/platform'],
  ['creator', '/lottie-creator'],
  ['integrations', '/integrations'],
  ['plugin-figma', '/plugins/figma'],
  ['tools', '/tools'],
  ['preview', '/preview'],
  ['animations', '/featured-free-animations'],
  ['animation', '/free-animation/loader-cat-dWUie0iIVk'],
  ['marketplace', '/marketplace'],
  ['case-studies', '/case-studies'],
  ['case-study', '/case-studies/wise'],
  ['blog', '/blog'],
  ['what-is-lottie', '/what-is-lottie'],
  ['education', '/education'],
  ['contact', '/contact-sales'],
  ['not-found', '/login'],
  ['privacy', '/page/privacy-policy'],
];

const browser = await chromium.launch(LAUNCH_OPTS);
let total = 0;

async function runWidth(mobile) {
  const vw = mobile ? 390 : 1440;
  const vh = mobile ? 844 : 900;
  const dpr = mobile ? 2 : 1;
  const prefix0 = mobile ? 'mobile-' : '';
  for (const [key, route] of PAGES) {
    const name = prefix0 + key;
    if (pageArg.length && !pageArg.includes(name) && !pageArg.includes(key)) continue;
    const ctx = await browser.newContext({
      viewport: { width: vw, height: vh },
      deviceScaleFactor: dpr,
      userAgent: mobile ? UA_MOBILE : UA,
      isMobile: mobile,
      hasTouch: mobile,
      locale: 'en-US',
    });
    await ctx.addInitScript(() => { Object.defineProperty(navigator, 'webdriver', { get: () => undefined }); });
    // Block Google One Tap so the public page is not covered by a Google sign-in prompt. Never click it.
    await ctx.route(/accounts\.google\.com|gsi\/client/, (route) => route.abort());
    const p = await ctx.newPage();
    const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
    log(name, route);
    try {
      const res = await p.goto(BASE + route, { waitUntil: 'domcontentloaded', timeout: 60000 });
      await wait(p, 2200);
      const status = res && res.status();
      log('  status', status, 'url', new URL(p.url()).pathname);
      if (key === 'home' && !mobile) {
        await S.view('promo');
        await hideConsent(p);
        await step('dismiss-promo', async () => {
          const d = p.getByRole('button', { name: 'Dismiss' }).first();
          if (await d.count()) { await d.click(); await wait(p, 400); }
        });
      }
      await hideConsent(p);
      await S.view('default');
      if (['home', 'pricing', 'animations', 'tools', 'case-studies', 'blog', 'privacy', 'what-is-lottie'].includes(key)) {
        await S.full();
      }
      if (key === 'home' && !mobile) {
        await step('products-menu', async () => {
          await p.getByRole('button', { name: 'Products', exact: true }).click();
          await wait(p, 600);
          await S.view('products-menu');
          await p.keyboard.press('Escape');
        });
        await step('integrations-menu', async () => {
          await hoverMenu(p, 'Integrations');
          await S.view('integrations-menu');
          await p.mouse.move(720, 860);
        });
        await step('tools-menu', async () => {
          await p.getByRole('button', { name: 'Tools', exact: true }).click();
          await wait(p, 600);
          await S.view('tools-menu');
          await p.keyboard.press('Escape');
        });
        await step('learn-menu', async () => {
          await hoverMenu(p, 'Learn');
          await S.view('learn-menu');
          await p.mouse.move(720, 860);
        });
        await step('customers-menu', async () => {
          await p.getByRole('button', { name: 'Customers', exact: true }).click();
          await wait(p, 600);
          await S.view('customers-menu');
          await p.keyboard.press('Escape');
        });
        await step('language-menu', async () => {
          await p.getByRole('button', { name: 'En', exact: true }).click();
          await wait(p, 400);
          await S.view('language-menu');
          await p.keyboard.press('Escape');
        });
        await step('search', async () => {
          await p.getByRole('button', { name: /Search animations/ }).first().click();
          await wait(p, 500);
          const input = p.locator('input[placeholder="Search for animations..."]').first();
          await input.click();
          await input.fill('loader');
          await wait(p, 900);
          await S.view('search');
          await p.keyboard.press('Escape');
        });
        await step('login-wall', async () => {
          await p.getByRole('button', { name: 'Log in', exact: true }).click();
          await wait(p, 1200);
          await S.view('login-wall');
          await p.keyboard.press('Escape');
          await wait(p, 300);
        });
        await step('nav-hover', async () => {
          await p.getByRole('link', { name: 'Pricing', exact: true }).first().hover();
          await wait(p, 300);
          await S.view('nav-hover');
        });
        await step('cta-focus', async () => {
          const cta = p.getByRole('link', { name: 'Get started for free' }).first();
          await cta.focus();
          await wait(p, 250);
          await S.view('cta-focus');
        });
      }
      if (key === 'home' && mobile) {
        await step('mobile-menu', async () => {
          const ham = p.locator('header button, button').filter({ has: p.locator('svg') }).last();
          const buttons = p.locator('button');
          const n = await buttons.count();
          for (let i = 0; i < Math.min(n, 8); i++) {
            const b = buttons.nth(i);
            const box = await b.boundingBox();
            const aria = await b.getAttribute('aria-label');
            if (box && box.y < 80 && box.x > 280 && aria !== 'Dismiss') {
              await b.click();
              await wait(p, 600);
              await S.view('menu');
              break;
            }
          }
        });
        await step('mobile-scrolled', async () => {
          await p.evaluate(() => scrollTo(0, 700));
          await wait(p, 400);
          await S.view('scrolled');
          await p.evaluate(() => scrollTo(0, 0));
        });
      }
      if (key === 'pricing' && !mobile) {
        await step('plan-hover', async () => {
          const card = p.getByText('Individual', { exact: true }).first();
          await card.scrollIntoViewIfNeeded();
          await card.hover();
          await wait(p, 300);
          await S.view('plan-hover');
        });
      }
      if (key === 'animation' && !mobile) {
        await step('download-menu', async () => {
          const b = p.getByRole('button', { name: 'Download', exact: true }).first();
          await b.scrollIntoViewIfNeeded();
          await b.click();
          await wait(p, 500);
          await S.view('download-menu');
          await p.keyboard.press('Escape');
        });
      }
      if (key === 'contact' && !mobile) {
        await step('field-focus', async () => {
          const field = p.locator('input, textarea').nth(1);
          if (await field.count()) {
            await field.scrollIntoViewIfNeeded();
            await field.focus();
            await wait(p, 250);
            await S.view('field-focus');
          }
        });
      }
      if (key === 'animations' && !mobile) {
        await step('filter', async () => {
          const chip = p.getByRole('button', { name: 'loading', exact: true }).first();
          if (await chip.count()) {
            await chip.scrollIntoViewIfNeeded();
            await chip.click();
            await wait(p, 700);
            await S.view('filter');
          }
        });
      }
    } catch (e) {
      log('  PAGE FAILED', name, String(e.message || e).split('\n')[0]);
    }
    total += S.count;
    await ctx.close();
  }
}

await runWidth(false);
await runWidth(true);
log('done', total, '->', RAW);
await browser.close();
