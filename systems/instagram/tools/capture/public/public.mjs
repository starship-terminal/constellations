// Captures Instagram's signed-out surfaces into RAW (full-colour PNGs).
// quantize.py turns them into screenshots/.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node public.mjs [page,...]
//
// Desktop 1440x900 at 1x, phone 390x844 at 2x.
// Consent layers are hidden, never clicked. Login and signup are photographed
// at rest. No field is filled and no Facebook login control is pressed.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, UA_MOBILE, hideConsent, patch, setDark } from './lib.mjs';

const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'instagram', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  let last = 0;
  for (let i = 0; i < 18; i++) {
    const h = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body ? document.body.scrollHeight : 0));
    const y = Math.min(i * 700, Math.max(0, h - 400));
    await p.evaluate((yy) => scrollTo(0, yy), y);
    await wait(p, 160);
    if (h === last && y + 800 >= h) break;
    last = h;
  }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 400);
  await hideConsent(p);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr, sourceUrl) {
    this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, sanitizedSourceUrl: sourceUrl };
    this.count = 0;
  }
  async view(name) {
    await hideConsent(this.p);
    const file = `${RAW}/${this.prefix}-${name}.png`;
    await screenshotWithMetadata(this.p, { path: file }, this.requested);
    this.count++;
    log('  shot', this.prefix, name);
  }
  async full(name = 'full') {
    const p = this.p;
    await hideConsent(p);
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body ? document.body.scrollHeight : 0));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only`);
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
      await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    }
    this.count++;
    log('  shot', this.prefix, name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
  }
}

const desktop = {
  login: { url: 'https://www.instagram.com/', theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('username-focused', async () => {
      const field = p.locator('input[name="email"], input[aria-label="Phone number, username, or email"]').first();
      await field.focus();
      await wait(p, 400);
      await S.view('username-focused');
    });
    await step('login-hover', async () => {
      const btn = p.getByRole('button', { name: 'Log in', exact: true }).first();
      await btn.hover();
      await wait(p, 300);
      await S.view('login-hover');
    });
  } },
  'login-dark': { url: 'https://www.instagram.com/', theme: 'dark', dark: true, run: async (p, S) => {
    await S.view('default');
  } },
  // No theme is requested here, so the file is labelled light like the committed signup-light-* shots.
  signup: { url: 'https://www.instagram.com/accounts/emailsignup/', theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('email-focused', async () => {
      const field = p.getByRole('textbox', { name: /Mobile number or email/ }).first();
      await field.focus();
      await wait(p, 400);
      await S.view('email-focused');
    });
  } },
  about: { url: 'https://about.instagram.com/', theme: 'light', run: async (p, S) => { await S.view('default'); await S.full(); } },
  features: { url: 'https://about.instagram.com/features', theme: 'light', run: async (p, S) => { await S.view('default'); await S.full(); } },
  help: { url: 'https://help.instagram.com/', theme: 'light', run: async (p, S) => { await S.view('default'); await S.full(); } },
  privacy: { url: 'https://privacycenter.instagram.com/policy/', theme: 'light', run: async (p, S) => { await S.view('default'); } },
  explore: { url: 'https://www.instagram.com/explore/locations/', theme: 'light', run: async (p, S) => { await S.view('default'); } },
  instagram: { url: 'https://www.instagram.com/instagram/', theme: 'light', run: async (p, S) => { await S.view('default'); } },
  'password-reset': { url: 'https://www.instagram.com/accounts/password/reset/', theme: 'light', run: async (p, S) => { await S.view('default'); } },
};

const mobile = {
  login: { url: 'https://www.instagram.com/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  signup: { url: 'https://www.instagram.com/accounts/emailsignup/', run: async (p, S) => { await S.view('default'); } },
  about: { url: 'https://about.instagram.com/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  help: { url: 'https://help.instagram.com/', run: async (p, S) => { await S.view('default'); } },
};

const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };

async function runOne(name, spec, { mobile: mob }) {
  const prefix = (mob ? 'mobile-' : '') + name + '-' + (spec.theme || 'light');
  const vw = mob ? 390 : 1440;
  const vh = mob ? 844 : 900;
  const dpr = mob ? 2 : 1;
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext(mob
    ? { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, userAgent: UA, locale: 'en-US' });
  await patch(context);
  const page = await context.newPage();
  log('open', prefix, spec.url);
  await page.goto(spec.url, { waitUntil: 'domcontentloaded', timeout: 90000 });
  await wait(page, 2800);
  await hideConsent(page);
  if (spec.dark) await setDark(page);
  const S = new Shooter(page, prefix, vw, vh, dpr, spec.url);
  await spec.run(page, S);
  await browser.close();
  return S.count;
}

let total = 0;
const runs = [
  ...Object.entries(desktop).map(([k, spec]) => ({ k, spec, mob: false })),
  ...Object.entries(mobile).map(([k, spec]) => ({ k, spec, mob: true })),
];
for (const { k, spec, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name) && !pageArg.includes(k)) continue;
  try { total += await runOne(k, spec, { mobile: mob }); }
  catch (e) { log('FAILED page', name, String(e.message).split('\n')[0]); }
}
log('done shots', total, 'dir', RAW);
