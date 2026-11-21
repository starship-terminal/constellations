// Captures byborre.com public pages. Cookie banner is hidden, never accepted.
// Login and sign-up dialogs are photographed and not filled. Nothing is submitted.
//
//   PLAYWRIGHT=... node public.mjs
import fs from 'node:fs';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, patch, closePromo, UA, UA_MOBILE, BASE } from './lib.mjs';

const RAW = process.env.RAW || `${process.env.HOME}/.design-systems/byborre/raw-shots`;
fs.mkdirSync(RAW, { recursive: true });
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

class Shooter {
  constructor(p, prefix, vw, vh, dpr) {
    this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr };
  }
  async view(name) {
    await closePromo(this.p);
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    log('  shot', this.prefix, name);
  }
  async full(name = 'full') {
    await closePromo(this.p);
    const H = await this.p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const hCap = Math.min(H, 8 * chunk);
    const f = `${RAW}/${this.prefix}-${name}`;
    if (hCap <= chunk) await screenshotWithMetadata(this.p, { path: f + '.png', fullPage: true }, this.requested);
    else {
      for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
        await screenshotWithMetadata(this.p, { path: `${f}.part${i}.png`, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
      }
    }
    log('  shot', this.prefix, name, 'H=' + H);
    await this.p.evaluate(() => scrollTo(0, 0));
  }
}

async function goto(page, path) {
  const url = path.startsWith('http') ? path : BASE + path;
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await wait(page, 1800);
  await closePromo(page);
  log('  ->', page.url());
}

const browser = await chromium.launch({ headless: true });

async function desk(name, fn) {
  const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US' });
  await patch(ctx);
  const page = await ctx.newPage();
  const S = new Shooter(page, `${name}-light`, 1440, 900, 1);
  try { await fn(page, S); } catch (e) { log('  FAILED', name, e.message.split('\n')[0]); }
  await ctx.close();
}

async function phone(name, fn) {
  const ctx = await browser.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' });
  await patch(ctx);
  const page = await ctx.newPage();
  const S = new Shooter(page, `mobile-${name}-light`, 390, 844, 2);
  try { await fn(page, S); } catch (e) { log('  FAILED', name, e.message.split('\n')[0]); }
  await ctx.close();
}

log('home');
await desk('home', async (page, S) => {
  await goto(page, '/');
  await S.view('default');
  await page.getByRole('button', { name: 'Collaborations', exact: true }).click();
  await wait(page, 700);
  await S.view('collaborations');
  await page.keyboard.press('Escape');
  await page.getByRole('button', { name: 'About', exact: true }).click();
  await wait(page, 700);
  await S.view('about');
  await page.keyboard.press('Escape');
  await page.getByRole('button', { name: 'Cart' }).first().click();
  await wait(page, 700);
  await S.view('cart');
  await page.getByRole('button', { name: 'Close', exact: true }).click().catch(() => page.keyboard.press('Escape'));
  await wait(page, 400);
  await page.locator('header button:visible').last().click();
  await wait(page, 900);
  await S.view('login');
  await page.keyboard.press('Escape');
  await S.full();
});

log('collection');
await desk('collection', async (page, S) => {
  await goto(page, '/collection');
  await S.view('default');
  await page.getByRole('button', { name: 'Pattern' }).first().click();
  await wait(page, 600);
  await S.view('pattern');
  await page.keyboard.press('Escape');
  await S.full();
});

log('textile');
await desk('textile', async (page, S) => {
  await goto(page, '/collection/blink?color=orange&shade=balance');
  await S.view('default');
  await page.getByRole('button', { name: 'Material' }).first().click().catch(() => {});
  await wait(page, 500);
  await S.view('accordion');
  await S.full();
});

for (const [name, path] of [['contact', '/contact'], ['faq', '/faq'], ['popup', '/popup-store'], ['creative', '/creative-control'], ['responsibility', '/responsibility'], ['projects', '/projects'], ['notfound', '/this-page-is-not-real']]) {
  log(name);
  await desk(name, async (page, S) => {
    await goto(page, path);
    await S.view('default');
    await S.full();
  });
}

log('login wall');
await desk('login', async (page, S) => {
  await goto(page, '/?redirectTo=/dashboard');
  await wait(page, 800);
  await S.view('default');
  const dialog = page.locator('div').filter({ has: page.locator('input[type="email"]') }).filter({ hasText: 'Log in to continue' }).last();
  await dialog.getByRole('button', { name: 'Sign up', exact: true }).click();
  await wait(page, 800);
  await S.view('signup');
  await page.keyboard.press('Escape');
  await page.goto(BASE + '/?redirectTo=/dashboard', { waitUntil: 'domcontentloaded', timeout: 45000 });
  await wait(page, 1200);
  await closePromo(page);
  await page.getByRole('button', { name: /forgot password/i }).click();
  await wait(page, 700);
  await S.view('forgot');
});

log('mobile');
await phone('home', async (page, S) => {
  await goto(page, '/');
  await S.view('default');
  await page.getByRole('button', { name: 'Open menu' }).click();
  await wait(page, 700);
  await S.view('menu');
  await S.full('full');
});

await browser.close();
log('done', RAW);
