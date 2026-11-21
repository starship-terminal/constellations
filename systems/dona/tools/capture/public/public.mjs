// Public captures of dona.ai. Signed-out only. Never fills a form, never clicks
// Accept, never follows SSO, never types an email.
//
//   RAW=~/.design-systems/dona/raw-shots PLAYWRIGHT=... node public.mjs
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, UA_MOBILE, BASE, hideConsent, waitReady } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'dona', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

class Shooter {
  constructor(p, prefix, vw, vh, dpr) {
    this.p = p;
    this.prefix = prefix;
    this.vw = vw;
    this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr };
  }
  async view(name) {
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    log('  shot', this.prefix + '-' + name);
  }
  async full(name = 'full') {
    const p = this.p;
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
      await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    }
    log('  shot', this.prefix + '-' + name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
    await wait(p, 300);
  }
}

async function settle(page) {
  await page.goto(page.url() === 'about:blank' ? BASE + '/' : page.url(), { waitUntil: 'domcontentloaded', timeout: 45000 }).catch(() => {});
}

async function go(page, url) {
  const resp = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 45000 });
  await waitReady(page);
  await hideConsent(page);
  return resp;
}

const desktopPages = {
  home: { url: BASE + '/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await p.getByRole('button', { name: 'Watch video' }).click({ force: true });
    await wait(p, 900);
    await S.view('video');
    await p.keyboard.press('Escape');
    await wait(p, 400);
  } },
  about: { url: BASE + '/about/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  terms: { url: BASE + '/terms-of-service/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  privacy: { url: BASE + '/privacy-policy/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  notfound: { url: BASE + '/no-such-page', run: async (p, S) => { await S.view('default'); } },
};

const mobilePages = {
  home: { url: BASE + '/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await p.getByRole('button', { name: 'Watch video' }).click({ force: true });
    await wait(p, 900);
    await S.view('video');
  } },
  about: { url: BASE + '/about/', run: async (p, S) => { await S.view('default'); } },
  notfound: { url: BASE + '/no-such-page', run: async (p, S) => { await S.view('default'); } },
};

async function runSet(pages, { width, height, dpr, mobile, prefix }) {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext(mobile
    ? { viewport: { width, height }, deviceScaleFactor: dpr, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width, height }, deviceScaleFactor: dpr, userAgent: UA, locale: 'en-US' });
  for (const [name, spec] of Object.entries(pages)) {
    const page = await context.newPage();
    page.setDefaultTimeout(12000);
    log('page', prefix + name, spec.url);
    try {
      await go(page, spec.url);
      const S = new Shooter(page, prefix + name + '-light', width, height, dpr);
      await spec.run(page, S);
    } catch (e) {
      log('  FAILED', name, String(e.message).split('\n')[0]);
    }
    await page.close();
  }
  await browser.close();
}

// Login wall: record the page, do not type, do not submit.
async function loginWall() {
  const browser = await chromium.launch({ headless: true });
  for (const [name, url, width, height, dpr, mobile] of [
    ['login-light-default', 'https://app.dona.ai/login', 1440, 900, 1, false],
    ['register-light-default', 'https://app.dona.ai/register', 1440, 900, 1, false],
    ['forgot-light-default', 'https://app.dona.ai/forgot-password', 1440, 900, 1, false],
    ['mobile-login-light-default', 'https://app.dona.ai/login', 390, 844, 2, true],
  ]) {
    const context = await browser.newContext(mobile
      ? { viewport: { width, height }, deviceScaleFactor: dpr, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
      : { viewport: { width, height }, deviceScaleFactor: dpr, userAgent: UA, locale: 'en-US' });
    const page = await context.newPage();
    log('wall', name, url);
    try {
      await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 30000 });
      await waitReady(page);
      const S = new Shooter(page, name.replace('-default', ''), width, height, dpr);
      await S.view('default');
    } catch (e) {
      log('  FAILED', name, String(e.message).split('\n')[0]);
    }
    await context.close();
  }
  await browser.close();
}

await runSet(desktopPages, { width: 1440, height: 900, dpr: 1, mobile: false, prefix: '' });
await runSet(mobilePages, { width: 390, height: 844, dpr: 2, mobile: true, prefix: 'mobile-' });
await loginWall();
log('done', RAW);
