// Measure Instagram's signed-out controls from the live DOM.
// Nothing is typed or submitted. Hover is a real mouse hover. Focus is
// keyboard focus. Pressed is CSS.forcePseudoState, so the control never fires.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node measure.mjs
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { chromium, UA, hideConsent, patch } from './lib.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const REF = path.resolve(here, '..', '..', '..');
const OUT = path.join(REF, 'raw', 'components-computed.json');
const CROPS = path.join(REF, 'components', 'crops');
fs.mkdirSync(path.dirname(OUT), { recursive: true });
fs.mkdirSync(CROPS, { recursive: true });

const PROPS = [
  'display', 'boxSizing', 'width', 'height',
  'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft',
  'fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'letterSpacing',
  'color', 'backgroundColor', 'borderTopWidth', 'borderTopColor', 'borderTopStyle',
  'borderRadius', 'boxShadow', 'outlineWidth', 'outlineStyle', 'outlineColor',
  'opacity',
];

async function pick(page, kind) {
  return page.evaluate((kind) => {
    const vis = (el) => {
      const r = el.getBoundingClientRect();
      return r.width > 8 && r.height > 8 && r.bottom > 0 && r.top < innerHeight;
    };
    const textOf = (el) => (el.innerText || el.getAttribute('aria-label') || el.getAttribute('placeholder') || '').replace(/\s+/g, ' ').trim();
    let el = null;
    if (kind === 'login-submit') {
      el = [...document.querySelectorAll('button, [role="button"], div[role="button"]')].find((e) => vis(e) && /^log in$/i.test(textOf(e)));
    } else if (kind === 'facebook') {
      el = [...document.querySelectorAll('button, [role="button"], a')].find((e) => vis(e) && /facebook/i.test(textOf(e)));
    } else if (kind === 'create') {
      el = [...document.querySelectorAll('a, button, [role="button"]')].find((e) => vis(e) && /create new account/i.test(textOf(e)));
    } else if (kind === 'forgot') {
      el = [...document.querySelectorAll('a, button')].find((e) => vis(e) && /forgot password/i.test(textOf(e)));
    } else if (kind === 'username') {
      el = document.querySelector('input[name="email"]') || document.querySelector('input[aria-label*="username" i]');
    } else if (kind === 'password') {
      el = document.querySelector('input[name="pass"]') || document.querySelector('input[type="password"]');
    } else if (kind === 'logo') {
      el = document.querySelector('img[alt*="Instagram" i]') || [...document.querySelectorAll('svg, i')].find((e) => vis(e) && e.getBoundingClientRect().width > 40 && e.getBoundingClientRect().y < 120);
    } else if (kind === 'language') {
      el = document.querySelector('select[aria-label="Switch Display Language"]');
    } else if (kind === 'submit') {
      el = [...document.querySelectorAll('button, [role="button"]')].find((e) => vis(e) && /^submit$/i.test(textOf(e)));
    } else if (kind === 'already') {
      el = [...document.querySelectorAll('button, [role="button"], a')].find((e) => vis(e) && /already have an account/i.test(textOf(e)));
    } else if (kind === 'email') {
      el = document.querySelector('input[type="text"]') || document.querySelector('input[aria-label*="email" i]');
    } else if (kind === 'month') {
      el = document.querySelector('[aria-label="Select Month"]') || document.querySelector('[role="combobox"]');
    } else if (kind === 'about-cta') {
      el = [...document.querySelectorAll('a, button')].find((e) => vis(e) && /try it now|get instagram/i.test(textOf(e)));
    } else if (kind === 'about-login') {
      el = [...document.querySelectorAll('a')].find((e) => vis(e) && /^log in$/i.test(textOf(e)));
    } else if (kind === 'hero') {
      el = document.querySelector('h1');
    } else if (kind === 'explore-login') {
      el = [...document.querySelectorAll('a, button')].find((e) => vis(e) && /^log in$/i.test(textOf(e)));
    } else if (kind === 'explore-signup') {
      el = [...document.querySelectorAll('a, button')].find((e) => vis(e) && /^sign up$/i.test(textOf(e)));
    } else if (kind === 'help-search') {
      el = document.querySelector('input[placeholder*="Search" i], input[type="search"], [role="searchbox"]');
    } else if (kind === 'help-link') {
      el = [...document.querySelectorAll('a')].find((e) => vis(e) && /reels/i.test(textOf(e)) && e.getBoundingClientRect().x > 200);
    } else if (kind === 'dialog-signup') {
      el = [...document.querySelectorAll('button, [role="button"], a')].find((e) => vis(e) && /^sign up$/i.test(textOf(e)));
    } else if (kind === 'dialog') {
      el = document.querySelector('[role="dialog"]');
    }
    if (!el) return null;
    el.setAttribute('data-ig-measure', kind);
    return { text: textOf(el).slice(0, 80), tag: el.tagName };
  }, kind);
}

async function readMarked(page, kind) {
  return page.evaluate(({ kind, props }) => {
    const el = document.querySelector(`[data-ig-measure="${kind}"]`);
    if (!el) return null;
    const cs = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    const o = {};
    for (const p of props) o[p] = cs[p];
    // The painted control is often a wrapper. Record the nearest ancestor
    // that has a visible background or border, so the crop matches the button.
    let paint = el;
    for (let n = el, i = 0; n && i < 4; n = n.parentElement, i++) {
      const s = getComputedStyle(n);
      const bg = s.backgroundColor;
      const bw = parseFloat(s.borderTopWidth) || 0;
      if ((bg && bg !== 'rgba(0, 0, 0, 0)' && bg !== 'transparent') || bw > 0) { paint = n; break; }
    }
    const ps = getComputedStyle(paint);
    const pr = paint.getBoundingClientRect();
    return {
      text: (el.innerText || el.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim().slice(0, 80),
      tag: el.tagName,
      box: { x: Math.round(pr.x), y: Math.round(pr.y), w: Math.round(pr.width), h: Math.round(pr.height) },
      style: o,
      paint: {
        tag: paint.tagName,
        backgroundColor: ps.backgroundColor,
        color: ps.color,
        borderRadius: ps.borderRadius,
        borderTopWidth: ps.borderTopWidth,
        borderTopColor: ps.borderTopColor,
        height: ps.height,
        fontSize: ps.fontSize,
        fontWeight: ps.fontWeight,
        fontFamily: ps.fontFamily.slice(0, 80),
      },
    };
  }, { kind, props: PROPS });
}

async function crop(page, kind, name) {
  const box = await page.evaluate((kind) => {
    const el = document.querySelector(`[data-ig-measure="${kind}"]`);
    if (!el) return null;
    let paint = el;
    for (let n = el, i = 0; n && i < 4; n = n.parentElement, i++) {
      const s = getComputedStyle(n);
      const bg = s.backgroundColor;
      const bw = parseFloat(s.borderTopWidth) || 0;
      if ((bg && bg !== 'rgba(0, 0, 0, 0)' && bg !== 'transparent') || bw > 0) { paint = n; break; }
    }
    const r = paint.getBoundingClientRect();
    return { x: r.x, y: r.y, w: r.width, h: r.height };
  }, kind);
  if (!box || box.w < 2 || box.h < 2) return;
  const pad = 6;
  const dpr = 2;
  const clip = {
    x: Math.max(0, box.x - pad),
    y: Math.max(0, box.y - pad),
    width: Math.min(box.w + pad * 2, 700),
    height: Math.min(box.h + pad * 2, 180),
  };
  await page.screenshot({ path: path.join(CROPS, name + '.png'), clip });
}

// Forces a pseudo-class through the DevTools protocol: CSS.forcePseudoState exists only there, not
// in the page (inside page.evaluate it is undefined, so a "pressed" reading was the resting style).
// Returns a function that clears the forced state.
async function force(page, kind, pseudo) {
  const cdp = await page.context().newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  const { root } = await cdp.send('DOM.getDocument', { depth: -1 });
  const { nodeId } = await cdp.send('DOM.querySelector', { nodeId: root.nodeId, selector: `[data-ig-measure="${kind}"]` });
  if (!nodeId) { await cdp.detach(); return async () => {}; }
  const states = [pseudo.replace(/^:/, ''), 'hover'];
  await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: states });
  return async () => { await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: [] }).catch(() => {}); await cdp.detach().catch(() => {}); };
}

// Every state starts from rest: pointer in a corner, nothing focused.
async function reset(page) {
  await page.mouse.move(2, 2);
  await page.evaluate(() => document.activeElement && document.activeElement.blur && document.activeElement.blur());
}

const browser = await chromium.launch({ headless: true });
const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US' });
await patch(ctx);
const page = await ctx.newPage();
const out = { product: 'instagram', captured: new Date().toLocaleDateString('en-CA'), note: 'Signed-out controls. Hover is a real mouse move. Focus is element.focus(). Pressed is CSS.forcePseudoState through CDP and never fires the control. No field was filled.', components: {} };

async function record(page, key, kind, { hover = false, focus = false, press = false, cropName } = {}) {
  const found = await pick(page, kind);
  if (!found) { console.log('  missing', key); return; }
  await reset(page);
  if (hover) {
    const box = await page.evaluate((kind) => {
      const el = document.querySelector(`[data-ig-measure="${kind}"]`);
      const r = el.getBoundingClientRect();
      return { x: r.x + r.width / 2, y: r.y + r.height / 2 };
    }, kind);
    await page.mouse.move(box.x, box.y);
  }
  if (focus) {
    await page.evaluate((kind) => document.querySelector(`[data-ig-measure="${kind}"]`).focus(), kind);
  }
  const unforce = press ? await force(page, kind, ':active') : null;
  await page.waitForTimeout(220);
  const data = await readMarked(page, kind);
  out.components[key] = data;
  if (cropName) await crop(page, kind, cropName);
  if (unforce) await unforce();
  const p = data && data.paint;
  console.log(' ', key, p && p.backgroundColor, p && p.color, p && p.borderRadius, data && data.box && data.box.h);
}

console.log('login');
await page.goto('https://www.instagram.com/', { waitUntil: 'domcontentloaded', timeout: 90000 });
await page.waitForTimeout(2800);
await hideConsent(page);
await record(page, 'button.login.default', 'login-submit', { cropName: 'button-login-default' });
await record(page, 'button.login.hover', 'login-submit', { hover: true, cropName: 'button-login-hover' });
await record(page, 'button.login.focus', 'login-submit', { focus: true, cropName: 'button-login-focus' });
await record(page, 'button.login.pressed', 'login-submit', { press: true, cropName: 'button-login-pressed' });
await record(page, 'button.facebook.default', 'facebook', { cropName: 'button-facebook-default' });
await record(page, 'link.create.default', 'create', { cropName: 'link-create-default' });
await record(page, 'link.create.hover', 'create', { hover: true, cropName: 'link-create-hover' });
await record(page, 'link.forgot.default', 'forgot', { cropName: 'link-forgot-default' });
await record(page, 'field.username.default', 'username', { cropName: 'field-username-default' });
await record(page, 'field.username.focus', 'username', { focus: true, cropName: 'field-username-focus' });
await record(page, 'field.password.default', 'password', { cropName: 'field-password-default' });
await record(page, 'logo.mark', 'logo', { cropName: 'logo-mark' });
await record(page, 'select.language.default', 'language', { cropName: 'select-language-default' });

console.log('signup');
await page.goto('https://www.instagram.com/accounts/emailsignup/', { waitUntil: 'domcontentloaded', timeout: 90000 });
await page.waitForTimeout(2800);
await hideConsent(page);
await record(page, 'button.submit.default', 'submit', { cropName: 'button-submit-default' });
await record(page, 'button.submit.hover', 'submit', { hover: true, cropName: 'button-submit-hover' });
await record(page, 'button.already.default', 'already', { cropName: 'button-already-default' });
await record(page, 'field.email.default', 'email', { cropName: 'field-email-default' });
await record(page, 'field.email.focus', 'email', { focus: true, cropName: 'field-email-focus' });
await record(page, 'select.month.default', 'month', { cropName: 'select-month-default' });

console.log('about');
await page.goto('https://about.instagram.com/', { waitUntil: 'domcontentloaded', timeout: 90000 });
await page.waitForTimeout(2500);
await hideConsent(page);
await record(page, 'link.about-cta.default', 'about-cta', { cropName: 'link-about-cta-default' });
await record(page, 'link.about-cta.hover', 'about-cta', { hover: true, cropName: 'link-about-cta-hover' });
await record(page, 'link.about-login.default', 'about-login', { cropName: 'link-about-login-default' });
await record(page, 'type.about-hero', 'hero', { cropName: 'type-about-hero' });

console.log('explore');
await page.goto('https://www.instagram.com/explore/locations/', { waitUntil: 'domcontentloaded', timeout: 90000 });
await page.waitForTimeout(2200);
await hideConsent(page);
await record(page, 'button.explore-login.default', 'explore-login', { cropName: 'button-explore-login-default' });
await record(page, 'link.explore-signup.default', 'explore-signup', { cropName: 'link-explore-signup-default' });

console.log('help');
await page.goto('https://help.instagram.com/', { waitUntil: 'domcontentloaded', timeout: 90000 });
await page.waitForTimeout(2500);
await hideConsent(page);
await record(page, 'field.help-search.default', 'help-search', { cropName: 'field-help-search-default' });
await record(page, 'link.help-topic.default', 'help-link', { cropName: 'link-help-topic-default' });

console.log('profile gate');
await page.goto('https://www.instagram.com/instagram/', { waitUntil: 'domcontentloaded', timeout: 90000 });
await page.waitForTimeout(2500);
await hideConsent(page);
await record(page, 'dialog.signup-gate', 'dialog', { cropName: 'dialog-signup-gate' });
await record(page, 'button.dialog-signup.default', 'dialog-signup', { cropName: 'button-dialog-signup-default' });

fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
console.log('wrote', OUT, 'crops', fs.readdirSync(CROPS).filter((n) => n.endsWith('.png')).length);
await browser.close();
