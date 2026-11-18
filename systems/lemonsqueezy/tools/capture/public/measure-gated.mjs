// Measure the closed-signup SMP card and the login error. Get started is
// measured, never clicked. Writes into the existing components-computed.json.
import fs from 'node:fs';
import path from 'node:path';
import os from 'node:os';
import { AUTH, launch, open, styleOf, crop, centre, RAW } from './lib.mjs';

const OUT = path.join(RAW, 'components-computed.json');
const existing = JSON.parse(fs.readFileSync(OUT, 'utf8'));
const out = existing;
out._meta.gated = '2026-11-18 closed-signup + login-error';
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const password = fs.readFileSync(path.join(os.homedir(), '.design-systems/lemonsqueezy/password'), 'utf8').trim();
const EMAIL = (process.env.LS_EMAIL || fs.readFileSync(path.join(os.homedir(), '.design-systems/lemonsqueezy/email'), 'utf8')).trim();

const { browser, context } = await launch({ width: 1440, height: 900, dpr: 2 });
let page, cdp;

async function measure(key, state, loc, opts = {}) {
  const c = out.components[key];
  try {
    const s = await styleOf(loc);
    let file;
    if (opts.crop !== false) {
      try { file = await crop(page, loc, `${key}-${state}`, opts.pad ?? 12); }
      catch (e) { s.cropError = String(e.message || e).slice(0, 140); }
    }
    c.states[state] = { ...s, crop: file, via: opts.via };
    log('  ', key, state, Math.round(s.rect.w) + 'x' + Math.round(s.rect.h), s.style.backgroundColor, s.style.color);
  } catch (e) {
    c.states[state] = { error: String(e.message || e).slice(0, 200) };
    log('  !', key, state, String(e.message).slice(0, 140));
  }
}

function comp(key, meta) {
  out.components[key] = {
    page: meta.page,
    url: meta.url,
    title: meta.title,
    group: meta.group,
    desc: meta.desc,
    selector: meta.sel,
    states: {},
  };
}

try {
  page = await context.newPage();
  cdp = await context.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');

  await open(page, AUTH + '/login', { wait: 1400 });
  await page.locator('#email').fill(EMAIL);
  await page.locator('#password').fill(password);
  await page.getByRole('button', { name: /^sign in$/i }).click();
  await page.waitForTimeout(2500);
  await page.locator('#email').fill('learner@example.com');
  await page.locator('#password').fill('');

  const err = page.locator('text=These credentials do not match our records').first();
  comp('login-error', {
    page: 'login', url: AUTH + '/login', title: 'Login error', group: 'status',
    desc: 'Server error after a failed email/password sign-in. The typed address was replaced with learner@example.com before the crop.',
    sel: 'credentials-do-not-match',
  });
  if (await err.count()) await measure('login-error', 'default', err, { via: 'failed sign-in, email redacted in the field', pad: 8 });
  else log('  ! missing login-error');

  await page.goto(AUTH + '/signup/business-intent', { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(1200);
  await page.locator('#business_name').fill('Personal testing');
  await page.locator('#website_url').fill('https://example.com');
  await page.locator('#country').selectOption('US');
  await page.getByRole('button', { name: /continue/i }).click();
  await page.waitForURL(/\/signup\/smp/, { timeout: 15000 });
  await page.waitForTimeout(1200);

  const smpUrl = AUTH + '/signup/smp';
  const card = page.locator('text=Managed Payments').first();
  // Prefer the recommended card container
  const cardBox = page.locator('div').filter({ hasText: 'Recommended for your business' }).filter({ hasText: 'Get started' }).first();
  comp('smp-card', {
    page: 'register-smp', url: smpUrl, title: 'Managed Payments card', group: 'card',
    desc: 'Closed-signup recommendation card. Get started was not clicked.',
    sel: 'Recommended for your business card',
  });
  if (await cardBox.count()) await measure('smp-card', 'default', cardBox, { via: 'at rest after business-intent submit', pad: 16 });
  else if (await card.count()) await measure('smp-card', 'default', card, { via: 'fallback heading', pad: 16 });

  const cta = page.getByRole('link', { name: /get started/i }).or(page.getByRole('button', { name: /get started/i })).first();
  comp('smp-cta', {
    page: 'register-smp', url: smpUrl, title: 'Get started', group: 'button',
    desc: 'Purple CTA on the closed-signup card. Measured, never followed (Stripe onboarding).',
    sel: 'Get started',
  });
  if (await cta.count()) {
    await measure('smp-cta', 'default', cta, { via: 'at rest' });
    await cta.hover().catch(() => {});
    await page.waitForTimeout(300);
    await measure('smp-cta', 'hover', cta, { via: 'mouse hover' });
    await page.mouse.move(4, 4);
  }

  await page.goto('https://app.lemonsqueezy.com/my-orders', { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(2200);
  const ordersBtn = page.getByRole('button', { name: /sign in/i }).first();
  comp('orders-submit', {
    page: 'my-orders', url: 'https://app.lemonsqueezy.com/my-orders/login', title: 'Customer orders Sign In', group: 'button',
    desc: 'Customer order portal sign-in. Email magic-link was not sent.',
    sel: 'Sign In',
  });
  if (await ordersBtn.count()) await measure('orders-submit', 'default', ordersBtn, { via: 'at rest, nothing submitted' });
  const ordersField = page.locator('input[type="email"], input[placeholder*="Email" i]').first();
  comp('orders-email', {
    page: 'my-orders', url: 'https://app.lemonsqueezy.com/my-orders/login', title: 'Customer orders email', group: 'text-field',
    desc: 'Email field on the customer order portal. Not filled, not submitted.',
    sel: 'input email',
  });
  if (await ordersField.count()) await measure('orders-email', 'default', ordersField, { via: 'at rest' });
} finally {
  save();
  await browser.close();
}
console.log('wrote', OUT, 'components', Object.keys(out.components).length);
