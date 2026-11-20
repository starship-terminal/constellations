// Measure the customer order portal's sign-in controls at rest. Nothing is typed or submitted.
// Writes into the existing components-computed.json, keeping every reading it does not retake.
import fs from 'node:fs';
import path from 'node:path';
import { launch, styleOf, crop, RAW } from './lib.mjs';
import { datePrior } from '../merge-dates.mjs';

const OUT = path.join(RAW, 'components-computed.json');
const existing = JSON.parse(fs.readFileSync(OUT, 'utf8'));
// Each state carries its own read date; kept states keep theirs (merge-dates.mjs).
const RUN = new Date().toLocaleDateString('en-CA');
const out = existing;
datePrior(out.components, out._meta && out._meta.captured);
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');

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
    c.states[state] = { ...s, crop: file, via: opts.via, read: RUN };
    log('  ', key, state, Math.round(s.rect.w) + 'x' + Math.round(s.rect.h), s.style.backgroundColor, s.style.color);
  } catch (e) {
    // A failed re-read keeps the committed reading and notes the failure beside it.
    const prior = c.states[state];
    if (prior && !prior.error) { c.states[state] = { ...prior, recaptureError: String(e.message || e).slice(0, 200), recaptureRun: RUN }; return; }
    c.states[state] = { error: String(e.message || e).slice(0, 200), read: RUN };
    log('  !', key, state, String(e.message).slice(0, 140));
  }
}

function comp(key, meta) {
  const prev = out.components[key];
  out.components[key] = {
    page: meta.page,
    url: meta.url,
    title: meta.title,
    group: meta.group,
    desc: meta.desc,
    selector: meta.sel,
    states: { ...(prev?.states || {}) },
  };
}

try {
  page = await context.newPage();
  cdp = await context.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');

  // state change: recorded as a boundary, not performed. The committed login-error, smp-card and
  // smp-cta readings (2026-11-18) were taken after this script typed the account's address and
  // password into the live sign-in form and submitted the business-intent signup form. Neither is
  // done any more; those three entries stay in raw/components-computed.json as they were read and
  // are not re-measured here.

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
