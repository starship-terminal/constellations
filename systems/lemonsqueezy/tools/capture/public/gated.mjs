// Gated pass for Lemon Squeezy, signed out. It shows the business-intent step at rest and probes
// the app host, which bounces to sign-in. It never fills or submits a form and never follows
// Get started, Google, Twitter, bank or payout KYC.
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
fs.mkdirSync(RAW, { recursive: true });
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

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

// state change: recorded as a boundary, not performed. The committed screenshots
// register-light-validation, register-smp-light-default, mobile-register-smp-light-default,
// login-light-error and mobile-login-light-error (2026-11-18) were taken after this script submitted the business-intent signup form
// and typed the account's address and password into the live sign-in form. A rerun no longer
// fills or submits either form; it shows the business-intent step at rest instead.
total += await shotPage({}, 'register-light', 1440, 900, 1, async (p, S) => {
  await p.goto(AUTH + '/signup/business-intent', { waitUntil: 'domcontentloaded' });
  await wait(p, 1500);
  await hideConsent(p);
  await S.view('default');
});

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
      log('  STOP', name, 'matched a stop condition; no screenshot taken');
      return;
    }
    await S.view('default');
  });
}

log('done', total, 'screenshots ->', RAW);
log('gated.mjs', fileURLToPath(import.meta.url));
