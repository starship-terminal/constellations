// Measures Monarch Money's public components. Nothing is signed up, signed
// in, linked to a bank, or submitted. Osano is hidden, never answered.
// OAuth buttons and Sign up are measured, never pressed.
//
//   PLAYWRIGHT=... node measure.mjs
import fs from 'node:fs';
import path from 'node:path';
import { BASE, APP, launch, open, hideConsent, styleOf, crop, centre, RAW } from './lib.mjs';

fs.mkdirSync(RAW, { recursive: true });
const OUT = path.join(RAW, 'components-computed.json');
// Start from the committed readings and replace each component this run reaches, so a page that
// fails part way keeps the earlier readings of every later component.
const prev = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : { components: {} };
// _meta.captured moves to today only once a component is read again, and each component records its
// own read date, so a failed run cannot give earlier readings a new date.
const today = new Date().toLocaleDateString('en-CA');
const out = { _meta: { ...(prev._meta || {}), product: 'Monarch Money', route: 'public-web' }, components: prev.components || {} };
if (!out._meta.captured) out._meta.captured = today;
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');

let page, cdp, current;

async function reset() {
  await page.evaluate(() => document.activeElement && document.activeElement.blur && document.activeElement.blur()).catch(() => {});
  const vw = page.viewportSize()?.width ?? 1440;
  await page.mouse.move(vw - 4, 4);
  await page.waitForTimeout(180);
}

async function kbFocus(loc) {
  await loc.evaluate((el) => el.focus());
  await page.keyboard.press('Shift+Tab').catch(() => {});
  await page.keyboard.press('Tab').catch(() => {});
  let ok = await loc.evaluate((el) => document.activeElement === el || el.contains(document.activeElement));
  if (!ok) {
    await loc.evaluate((el) => el.focus());
    ok = await loc.evaluate((el) => document.activeElement === el || el.contains(document.activeElement));
  }
  await page.waitForTimeout(280);
  return ok ? 'keyboard focus' : 'focus failed';
}

async function forcePseudo(loc, classes) {
  await page.evaluate(() => document.querySelectorAll('[data-m-force]').forEach((n) => n.removeAttribute('data-m-force')));
  await loc.evaluate((el) => el.setAttribute('data-m-force', '1'));
  const { root } = await cdp.send('DOM.getDocument', { depth: 0 });
  const { nodeId } = await cdp.send('DOM.querySelector', { nodeId: root.nodeId, selector: '[data-m-force]' });
  if (!nodeId) return async () => {};
  await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: classes });
  await page.waitForTimeout(280);
  return async () => { await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: [] }).catch(() => {}); };
}

async function measure(key, state, loc, via) {
  const target = loc.filter({ visible: true }).first();
  if (!(await target.count())) {
    out.components[key].states[state] = { error: 'missing' };
    log('  ! missing', key, state);
    return;
  }
  try {
    const s = await styleOf(target);
    let file;
    try { file = await crop(page, target, `${key}-${state}`, 8); } catch (e) { s.cropError = String(e.message || e).slice(0, 140); }
    out.components[key].states[state] = { ...s, crop: file, via };
    log('  ', key, state, Math.round(s.rect.w) + 'x' + Math.round(s.rect.h), s.style.backgroundColor, s.style.fontSize);
  } catch (e) {
    out.components[key].states[state] = { error: String(e.message || e).slice(0, 180) };
    log('  !', key, state, String(e.message).slice(0, 100));
  }
}

async function S(key, loc, states, meta) {
  out.components[key] = { title: meta.title, group: meta.group, desc: meta.desc, page: current, read: today, states: {} };
  out._meta.captured = today;
  const target = loc.filter({ visible: true }).first();
  if (!(await target.count())) {
    out.components[key].missing = true;
    log('  ! missing', key);
    return;
  }
  for (const st of states) {
    let undo;
    let via = 'at rest';
    try {
      await reset();
      await centre(target);
      await hideConsent(page);
      if (st === 'hover') {
        await target.hover({ timeout: 4000 }).catch(() => target.hover({ force: true, timeout: 4000 }));
        await page.waitForTimeout(350);
        via = 'mouse hover';
      } else if (st === 'focus-visible') {
        via = await kbFocus(target);
      } else if (st === 'pressed') {
        undo = await forcePseudo(target, ['active', 'hover']);
        via = 'CDP forcePseudoState :active:hover; not clicked';
      } else if (st === 'focused') {
        await target.click({ timeout: 3000 });
        await page.waitForTimeout(250);
        via = 'clicked into the field; nothing typed that is submitted';
      }
      await measure(key, st, loc, via);
    } catch (e) {
      out.components[key].states[st] = { error: String(e.message || e).slice(0, 180) };
      log('  !', key, st, String(e.message).slice(0, 100));
    }
    if (undo) await undo().catch(() => {});
  }
}

const q = (sel) => page.locator(sel);
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];

async function boot(url, label) {
  current = label;
  page = await context.newPage();
  page.setDefaultTimeout(8000);
  cdp = await context.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  log('open', label, url);
  await open(page, url, { wait: 2000 });
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' });
}

let context;
const { browser, context: ctx } = await launch({ width: 1440, height: 900, dpr: 1 });
context = ctx;

try {
  await boot(BASE + '/', 'home');
  const g = 'Marketing frame';
  await S('announcement', q('header').locator('a, p, span').filter({ hasText: /OFF|WELCOME/ }).first(), ['default'], { group: g, title: 'Announcement bar', desc: 'The 32px promo strip above the nav. Measured, the code was not used.' });
  await S('nav-link', q('header nav a, header a').filter({ hasText: 'Pricing' }).first(), B4, { group: g, title: 'Nav link', desc: 'A 36px pill in the desktop bar. Hover and pressed are visual only; the link was not followed.' });
  await S('nav-features', q('header button').filter({ hasText: 'Features' }).first(), ['default', 'hover', 'focus-visible'], { group: g, title: 'Features menu button', desc: 'Opens the features menu. Measured closed. Not opened, so no navigation.' });
  await S('sign-in-button', q('header a').filter({ hasText: /^Sign in$/ }).first(), B4, { group: g, title: 'Sign in button', desc: 'White pill, 1px border, 36px. Measured, never followed.' });
  await S('sign-up-button', q('header a').filter({ hasText: /^Sign up$/ }).first(), B4, { group: g, title: 'Sign up button', desc: 'Orange pill in the bar. Measured, never followed. Signup, bank linking and payment were not started.' });
  await S('hero-title', q('h1').first(), ['default'], { group: 'Home', title: 'Hero title', desc: 'The first visible display heading on the home page.' });
  await S('footer-cta', q('a').filter({ hasText: 'Get started today' }).first(), B4, { group: 'Home', title: 'Footer call to action', desc: 'White pill on the dark close band. Measured, never followed.' });
  await S('footer', q('footer').first(), ['default'], { group: g, title: 'Footer', desc: 'The site footer.' });
  await page.close();

  await boot(BASE + '/pricing', 'pricing');
  await S('pricing-title', q('h1').first(), ['default'], { group: 'Pricing', title: 'Pricing title', desc: 'The pricing page heading.' });
  await S('plan-card', q('.dpp-plan, [class*="plan"]').filter({ hasText: 'Core' }).first(), ['default'], { group: 'Pricing', title: 'Core plan card', desc: 'The Core price card. The trial link was not followed.' });
  await S('plan-cta', q('a.dpp-cta').first(), B4, { group: 'Pricing', title: 'Plan trial link', desc: 'Try Monarch free for 7 days. Measured, never followed. No card, phone or bank was entered.' });
  await S('faq-item', q('button').filter({ hasText: 'What is the cost' }).first(), ['default', 'hover', 'focus-visible'], { group: 'Pricing', title: 'FAQ summary', desc: 'A pricing FAQ row. Left closed so the accordion stays at rest.' });
  await page.close();

  await boot(APP + '/login', 'signin');
  const a = 'Sign-in boundary';
  await S('oauth-apple', q('button').filter({ hasText: 'Continue with Apple' }).first(), B4, { group: a, title: 'Continue with Apple', desc: 'Measured, never pressed. OAuth was not followed.' });
  await S('oauth-google', q('button').filter({ hasText: 'Continue with Google' }).first(), B4, { group: a, title: 'Continue with Google', desc: 'Measured, never pressed. OAuth was not followed.' });
  await S('email-field', q('input[name="username"]'), ['default', 'hover', 'focus-visible', 'focused'], { group: a, title: 'Email field', desc: 'The sign-in email field. Focused and left empty. Nothing was typed or submitted.' });
  await S('password-field', q('input[name="password"]'), ['default', 'focus-visible'], { group: a, title: 'Password field', desc: 'Empty. Nothing was typed. Show password was not pressed.' });
  await S('signin-submit', q('button[type="submit"]').filter({ hasText: 'Sign in' }).first(), ['default', 'hover', 'focus-visible'], { group: a, title: 'Sign in submit', desc: 'The disabled-looking submit at rest (half orange). Not pressed. No credentials were entered.' });
  await S('stay-signed-in', q('label').filter({ hasText: 'Stay signed in' }).first(), ['default'], { group: a, title: 'Stay signed in', desc: 'The checkbox label. The box was not toggled.' });
  await S('forgot-link', q('a').filter({ hasText: 'Forgot password' }).first(), ['default', 'hover', 'focus-visible'], { group: a, title: 'Forgot password link', desc: 'Measured, never followed.' });
  await S('signup-link', q('a').filter({ hasText: /^Sign up$/ }).first(), ['default', 'hover'], { group: a, title: 'Sign up link on the wall', desc: 'Measured, never followed.' });
  await page.close();

  await boot(APP + '/signup', 'signup');
  await S('signup-heading', q('h1, h2').first(), ['default'], { group: a, title: 'Sign-up heading', desc: 'The sign-up wall heading. The form was not filled. No email, phone, card or bank was entered.' });
  const signupBtn = q('button, a').filter({ hasText: /Continue with Google|Continue with Apple|Sign up/ }).first();
  await S('signup-oauth', signupBtn, ['default'], { group: a, title: 'Sign-up primary control', desc: 'Photographed at the boundary. Not pressed.' });
  await page.close();
} finally {
  save();
  await browser.close();
  log('wrote', OUT, Object.keys(out.components).length, 'components');
}
