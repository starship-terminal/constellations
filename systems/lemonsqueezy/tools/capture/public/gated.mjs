// Signed-in pass for Lemon Squeezy. New store signups are closed; this
// records that gate, the login error, and the Stripe Managed Payments
// recommendation. It never follows Get started, Google, Twitter, bank or
// payout KYC.
//
//   RAW=~/.design-systems/lemonsqueezy/raw-shots \
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs \
//   node gated.mjs
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { hideConsent, chromium, UA, UA_MOBILE, AUTH } from './lib.mjs';

const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'lemonsqueezy', 'raw-shots');
const PROFILE = process.env.LS_PROFILE || path.join(os.homedir(), '.design-systems', 'lemonsqueezy', 'chrome-profile');
const PW_FILE = path.join(os.homedir(), '.design-systems', 'lemonsqueezy', 'password');
fs.mkdirSync(RAW, { recursive: true });
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);
const password = fs.readFileSync(PW_FILE, 'utf8').trim();
const EMAIL_FILE = path.join(os.homedir(), '.design-systems', 'lemonsqueezy', 'email');
const EMAIL = (process.env.LS_EMAIL || fs.readFileSync(EMAIL_FILE, 'utf8')).trim();
const REDACT_EMAIL = 'learner@example.com';

class Shooter {
  constructor(p, prefix, vw, vh, dpr) {
    this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr };
    this.count = 0;
  }
  async view(name) {
    await hideConsent(this.p);
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png`, animations: 'disabled' }, this.requested);
    this.count++;
    log('  shot', this.prefix, name);
  }
}

async function shotPage(ctxOpts, prefix, vw, vh, dpr, fn) {
  const browser = await chromium.launch({ headless: true });
  const ctx = await browser.newContext({
    viewport: { width: vw, height: vh },
    deviceScaleFactor: dpr,
    userAgent: ctxOpts.mobile ? UA_MOBILE : UA,
    isMobile: !!ctxOpts.mobile,
    hasTouch: !!ctxOpts.mobile,
    locale: 'en-US',
  });
  await ctx.addInitScript(() => { Object.defineProperty(navigator, 'webdriver', { get: () => undefined }); });
  const p = await ctx.newPage();
  p.setDefaultTimeout(25000);
  const S = new Shooter(p, prefix, vw, vh, dpr);
  try {
    await fn(p, S);
  } catch (e) {
    log('  FAILED', prefix, String(e.message).split('\n')[0]);
  }
  await ctx.close();
  await browser.close();
  return S.count;
}

let total = 0;

// Native required-field tooltip on the business-intent step.
total += await shotPage({}, 'register-light', 1440, 900, 1, async (p, S) => {
  await p.goto(AUTH + '/signup/business-intent', { waitUntil: 'domcontentloaded' });
  await wait(p, 1500);
  await hideConsent(p);
  await p.locator('#business_name').fill('Personal testing');
  await p.getByRole('button', { name: /continue/i }).click();
  await wait(p, 400);
  await S.view('validation');
});

// Closed-signup / Stripe Managed Payments recommendation. Do not click Get started.
async function reachSmp(p) {
  await p.goto(AUTH + '/signup/business-intent', { waitUntil: 'domcontentloaded' });
  await wait(p, 1200);
  await hideConsent(p);
  await p.locator('#business_name').fill('Personal testing');
  await p.locator('#website_url').fill('https://example.com');
  await p.locator('#country').selectOption('US');
  await p.getByRole('button', { name: /continue/i }).click();
  await p.waitForURL(/\/signup\/smp/, { timeout: 15000 }).catch(() => {});
  await wait(p, 1200);
  await hideConsent(p);
}

total += await shotPage({}, 'register-smp-light', 1440, 900, 1, async (p, S) => {
  await reachSmp(p);
  log('  smp url', p.url());
  await S.view('default');
});
total += await shotPage({ mobile: true }, 'mobile-register-smp-light', 390, 844, 2, async (p, S) => {
  await reachSmp(p);
  await S.view('default');
});

// Login error. Submit once, then replace the typed email so the PNG has no inbox.
async function loginError(p, S) {
  await p.goto(AUTH + '/login', { waitUntil: 'domcontentloaded' });
  await wait(p, 1200);
  await hideConsent(p);
  await p.locator('#email').fill(EMAIL);
  await p.locator('#password').fill(password);
  await p.getByRole('button', { name: /^sign in$/i }).click();
  await wait(p, 2500);
  await p.locator('#email').fill(REDACT_EMAIL);
  await p.locator('#password').fill('');
  await S.view('error');
}

total += await shotPage({}, 'login-light', 1440, 900, 1, async (p, S) => { await loginError(p, S); });
total += await shotPage({ mobile: true }, 'mobile-login-light', 390, 844, 2, async (p, S) => { await loginError(p, S); });

// Probe the app host. Expected: bounce to login. Stop if Stripe/KYC/CAPTCHA/phone.
for (const [name, url] of [
  ['app-root', 'https://app.lemonsqueezy.com/'],
  ['app-products', 'https://app.lemonsqueezy.com/products'],
  ['app-orders', 'https://app.lemonsqueezy.com/orders'],
  ['app-customers', 'https://app.lemonsqueezy.com/customers'],
  ['app-settings', 'https://app.lemonsqueezy.com/settings'],
  ['my-orders', 'https://app.lemonsqueezy.com/my-orders'],
]) {
  total += await shotPage({}, `${name}-light`, 1440, 900, 1, async (p, S) => {
    await p.goto(url, { waitUntil: 'domcontentloaded', timeout: 30000 });
    await wait(p, 1800);
    const body = ((await p.locator('body').innerText().catch(() => '')) || '').slice(0, 500);
    log('  probe', name, p.url());
    log('  text', body.replace(/\s+/g, ' ').slice(0, 240));
    if (/captcha|phone|verify your|stripe|kyc|payout|bank account/i.test(body) && !/Sign in to Lemon Squeezy/i.test(body)) {
      log('  STOP', name, 'matched a stop condition');
    }
    await S.view('default');
  });
}

log('done', total, 'screenshots ->', RAW);
log('gated.mjs', fileURLToPath(import.meta.url));
