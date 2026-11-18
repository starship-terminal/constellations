// Captures the join/sign-in 6-digit code step after submitting the capture email.
// The address is read from CAPTURE_EMAIL or ~/.design-systems/kinhive/email and
// replaced in the DOM before each shot. LinkedIn is never pressed.
//
//   RAW=... PLAYWRIGHT=... node code.mjs
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', path.basename(PKG), 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const PROFILE = path.join(os.homedir(), '.design-systems', 'kinhive', 'chrome-profile');
const EMAIL_FILE = path.join(os.homedir(), '.design-systems', 'kinhive', 'email');
const EMAIL = (process.env.CAPTURE_EMAIL || (fs.existsSync(EMAIL_FILE) ? fs.readFileSync(EMAIL_FILE, 'utf8') : '')).trim();
if (!EMAIL) { console.error('set CAPTURE_EMAIL or write ~/.design-systems/kinhive/email'); process.exit(2); }
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function redact(page) {
  await page.evaluate((email) => {
    const re = new RegExp(email.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'ig');
    for (const el of document.querySelectorAll('input, textarea')) {
      if (re.test(el.value || '')) el.value = 'you@email.com';
    }
    const walk = (n) => {
      if (n.nodeType === 3 && re.test(n.nodeValue || '')) {
        n.nodeValue = n.nodeValue.replace(re, 'you@email.com');
      }
      for (const c of n.childNodes || []) walk(c);
    };
    walk(document.body);
  }, EMAIL);
}

async function shot(page, name, vw, vh, dpr, sourceUrl) {
  await closePromo(page);
  await redact(page);
  await screenshotWithMetadata(page, { path: `${RAW}/${name}.png` }, {
    viewport: { width: vw, height: vh },
    deviceScaleFactor: dpr,
    sanitizedSourceUrl: sourceUrl,
  });
  log('  shot', name);
}

async function fillJoin(page) {
  await page.locator('#first').fill('Kai');
  await page.locator('#last').fill('Chen');
  await page.locator('#email').fill(EMAIL);
  await page.getByRole('button', { name: 'Continue', exact: true }).click();
  await page.waitForFunction(() => !!document.querySelector('#code'), { timeout: 20000 });
  await wait(page, 600);
}

async function fillSignin(page) {
  await page.locator('#email').fill(EMAIL);
  await page.getByRole('button', { name: /Email me a sign-in code/i }).click();
  await page.waitForFunction(() => !!document.querySelector('#code'), { timeout: 20000 });
  await wait(page, 600);
}

async function wrongCode(page) {
  await page.locator('#code').fill('000000');
  await wait(page, 300);
  const btn = page.getByRole('button', { name: 'Continue', exact: true });
  await btn.click({ timeout: 8000 });
  await wait(page, 1500);
}

async function runOne({ mobile, kind }) {
  const vw = mobile ? 390 : 1440;
  const vh = mobile ? 844 : 900;
  const dpr = mobile ? 2 : 1;
  const prefix = (mobile ? 'mobile-' : '') + (kind === 'join' ? 'join-code' : 'signin-code') + '-light';
  const pathName = kind === 'join' ? '/join' : '/sign-in';
  log(prefix);
  const context = await chromium.launchPersistentContext(PROFILE, {
    headless: true,
    viewport: { width: vw, height: vh },
    deviceScaleFactor: dpr,
    userAgent: mobile ? UA_MOBILE : UA,
    isMobile: mobile,
    hasTouch: mobile,
    locale: 'en-US',
    colorScheme: 'light',
    args: ['--disable-blink-features=AutomationControlled'],
  });
  await patch(context);
  const page = context.pages()[0] || await context.newPage();
  try {
    await page.goto(BASE + pathName, { waitUntil: 'domcontentloaded', timeout: 45000 });
    await wait(page, 1800);
    const ok = await clearChallenge(page, { tries: 4, step: 800 });
    if (!ok) log('  challenge still up', prefix);
    await closePromo(page);
    const text = await page.evaluate(() => document.body.innerText || '');
    if (/captcha|verify you are human|phone number|payment|stripe|checkout/i.test(text) && !/#code|We sent a code/i.test(text)) {
      log('  STOP challenge/phone/payment', prefix);
      fs.writeFileSync(path.join(os.homedir(), '.design-systems', 'kinhive', 'stop.json'), JSON.stringify({ prefix, text: text.slice(0, 2000) }, null, 2));
      await context.close();
      return;
    }
    if (!documentHasCode(text)) {
      if (kind === 'join') await fillJoin(page);
      else await fillSignin(page);
    }
    const after = await page.evaluate(() => document.body.innerText || '');
    if (!/#code|We sent a code/i.test(after) && !(await page.locator('#code').count())) {
      log('  no code field', prefix, after.slice(0, 300).replace(/\n/g, ' '));
      await context.close();
      return;
    }
    await shot(page, `${prefix}-default`, vw, vh, dpr, BASE + pathName);
    await wrongCode(page);
    await shot(page, `${prefix}-error`, vw, vh, dpr, BASE + pathName);
  } catch (e) {
    log('  FAILED', prefix, String(e.message).split('\n')[0]);
  }
  await context.close();
}

function documentHasCode(text) {
  return /We sent a code/i.test(text);
}

for (const mobile of [false, true]) {
  for (const kind of ['join', 'signin']) {
    await runOne({ mobile, kind });
  }
}
log('done ->', RAW);
