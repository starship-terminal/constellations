// Remeasure Mural components. Does not submit forms.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { execFileSync } from 'node:child_process';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const PYTHON = process.env.PYTHON || 'python3';
const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..');
const RAW = path.join(PKG, 'raw');
const CROPS = path.join(PKG, 'components', 'crops');
fs.mkdirSync(CROPS, { recursive: true });
const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);

const PROPS = ['display','position','boxSizing','paddingTop','paddingRight','paddingBottom','paddingLeft','gap','borderTopWidth','borderTopStyle','borderTopColor','borderRightWidth','borderRightStyle','borderRightColor','borderBottomWidth','borderBottomStyle','borderBottomColor','borderLeftWidth','borderLeftStyle','borderLeftColor','borderTopLeftRadius','borderTopRightRadius','borderBottomRightRadius','borderBottomLeftRadius','backgroundColor','backgroundImage','boxShadow','outlineWidth','outlineStyle','outlineColor','outlineOffset','fontFamily','fontSize','fontWeight','lineHeight','letterSpacing','textTransform','color','textDecorationLine','transitionProperty','transitionDuration','transitionTimingFunction','cursor','opacity'];

function quantize(file) {
  execFileSync(PYTHON, ['-c', 'import sys\nfrom PIL import Image\nf=sys.argv[1]\nim=Image.open(f).convert("RGB")\nif im.width*im.height>1200000: im=im.resize((im.width//2, im.height//2), Image.LANCZOS)\nim.quantize(256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).save(f, optimize=True)', file]);
}

function reader() {
  return (el) => {
    const props = ['display','position','boxSizing','paddingTop','paddingRight','paddingBottom','paddingLeft','gap','borderTopWidth','borderTopStyle','borderTopColor','borderRightWidth','borderRightStyle','borderRightColor','borderBottomWidth','borderBottomStyle','borderBottomColor','borderLeftWidth','borderLeftStyle','borderLeftColor','borderTopLeftRadius','borderTopRightRadius','borderBottomRightRadius','borderBottomLeftRadius','backgroundColor','backgroundImage','boxShadow','outlineWidth','outlineStyle','outlineColor','outlineOffset','fontFamily','fontSize','fontWeight','lineHeight','letterSpacing','textTransform','color','textDecorationLine','transitionProperty','transitionDuration','transitionTimingFunction','cursor','opacity'];
    const cs = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    const style = {};
    for (const p of props) style[p] = cs[p];
    const out = {
      tag: el.tagName.toLowerCase(),
      classes: [...el.classList].slice(0, 6).join(' '),
      text: (el.innerText || el.getAttribute('aria-label') || el.getAttribute('placeholder') || '').trim().replace(/\s+/g, ' ').slice(0, 90),
      rect: { x: +r.x.toFixed(1), y: +r.y.toFixed(1), w: +r.width.toFixed(2), h: +r.height.toFixed(2) },
      style,
    };
    const walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT, { acceptNode: (t) => t.textContent.trim() ? 1 : 3 });
    const tn = walker.nextNode();
    if (tn && tn.parentElement && tn.parentElement !== el) {
      const tc = getComputedStyle(tn.parentElement);
      out.textStyle = { node: tn.parentElement.tagName.toLowerCase(), text: tn.textContent.trim().slice(0, 40), fontFamily: tc.fontFamily, fontSize: tc.fontSize, lineHeight: tc.lineHeight, fontWeight: tc.fontWeight, letterSpacing: tc.letterSpacing, color: tc.color };
    }
    if (el.tagName === 'INPUT') {
      const ph = getComputedStyle(el, '::placeholder');
      out.placeholder = { color: ph.color, fontSize: ph.fontSize, fontFamily: ph.fontFamily };
    }
    const label = el.closest('label') || document.querySelector(`label[for="${el.id}"]`);
    return out;
  };
}

async function crop(page, loc, name) {
  const file = path.join(CROPS, name + '.png');
  await loc.evaluate((el) => el.scrollIntoView({ block: 'center', inline: 'nearest' }));
  await page.waitForTimeout(200);
  const box = await loc.boundingBox();
  if (!box) throw new Error('no box');
  const vp = page.viewportSize();
  const pad = 12;
  const clip = {
    x: Math.max(0, box.x - pad),
    y: Math.max(0, box.y - pad),
    width: Math.min(vp.width - Math.max(0, box.x - pad), box.width + pad * 2),
    height: Math.min(vp.height - Math.max(0, box.y - pad), box.height + pad * 2),
  };
  await page.screenshot({ path: file, clip, animations: 'disabled' });
  quantize(file);
  return path.relative(PKG, file);
}

const browser = await chromium.launch({ headless: true });
const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US' });
const page = await ctx.newPage();
const read = reader();
const components = {};

async function open(url) {
  log('open', url);
  const res = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(2500);
  await page.addStyleTag({ content: '#onetrust-consent-sdk,[class*=pendo-]{display:none!important} *{caret-color:transparent!important}' }).catch(() => {});
  const gate = await page.evaluate(() => /just a moment|cloudflare/i.test(document.title));
  if (gate) throw new Error('cloudflare ' + url);
  return res && res.status();
}

async function one(key, meta, loc, state, via, prep) {
  const c = components[key] ??= { ...meta, states: {} };
  try {
    const el = loc.filter({ visible: true }).first();
    if (!(await el.count())) { log('  miss', key, state); c.states[state] = { error: 'missing' }; return; }
    if (prep) await prep(el);
    const s = await el.evaluate(read);
    let file = null;
    try { file = await crop(page, el, `${key}-${state}`); } catch (e) { s.cropError = String(e.message).slice(0, 100); }
    c.states[state] = { ...s, crop: file, via };
    log('  ', key, state, s.rect.w + 'x' + s.rect.h, s.text.slice(0, 40), s.style.backgroundColor, s.style.color, s.style.fontSize);
  } catch (e) {
    c.states[state] = { error: String(e.message).slice(0, 180) };
    log('  !', key, state, String(e.message).slice(0, 140));
  }
}

await open('https://www.mural.co/');
await one('nav-link', { title: 'Nav link', group: 'Navigation', page: 'home', selector: 'a.nav-link_toggle' }, page.locator('a.nav-link_toggle').filter({ hasText: 'Pricing' }), 'default', 'at rest');
await one('nav-link', { title: 'Nav link', group: 'Navigation', page: 'home' }, page.locator('a.nav-link_toggle').filter({ hasText: 'Pricing' }), 'hover', 'mouse hover', async (el) => { await el.hover(); await page.waitForTimeout(400); });
await one('button-primary', { title: 'Sign up free', group: 'Buttons', page: 'home', selector: 'a.button_component' }, page.locator('a.button_component').filter({ hasText: 'Sign up free' }), 'default', 'at rest');
await one('button-primary', { title: 'Sign up free', group: 'Buttons', page: 'home' }, page.locator('a.button_component').filter({ hasText: 'Sign up free' }), 'hover', 'mouse hover', async (el) => { await el.hover(); await page.waitForTimeout(450); });
await one('button-outline', { title: 'Book a demo', group: 'Buttons', page: 'home', selector: 'a.button_component' }, page.locator('a.button_component').filter({ hasText: 'Book a demo' }), 'default', 'at rest');
await one('button-outline', { title: 'Book a demo', group: 'Buttons', page: 'home' }, page.locator('a.button_component').filter({ hasText: 'Book a demo' }), 'hover', 'mouse hover', async (el) => { await el.hover(); await page.waitForTimeout(450); });
await one('display', { title: 'Hero display', group: 'Type', page: 'home', selector: 'h1' }, page.locator('h1').first(), 'default', 'at rest');
await one('lede', { title: 'Hero lede', group: 'Type', page: 'home', selector: 'p' }, page.locator('.section_home-hero p, main p').first(), 'default', 'at rest');
await one('eyebrow', { title: 'Section eyebrow', group: 'Type', page: 'home', selector: 'h2.logos_h2' }, page.locator('h2').first(), 'default', 'at rest');

// Open product menu
const toggle = page.locator('.w-dropdown-toggle, button').filter({ hasText: /^Product$/ }).first();
if (await toggle.count()) {
  await toggle.click().catch(() => {});
  await page.waitForTimeout(600);
  const menu = page.locator('.w-dropdown-list, [class*=dropdown-list], [role=menu]').first();
  await one('menu', { title: 'Product menu', group: 'Navigation', page: 'home' }, menu, 'open', 'clicked Product, not followed');
  await page.keyboard.press('Escape').catch(() => {});
}

await open('https://www.mural.co/pricing');
const cards = page.locator('[class*=pricing_card], [class*=price-card], [class*=plan-card], [class*=pricing-card]');
log('pricing cards', await cards.count());
const cardSel = (await cards.count()) ? cards : page.locator('main [class*=card]').filter({ hasText: /Free|Team|Business|Enterprise/ });
log('card fallback', await cardSel.count());
await one('pricing-card', { title: 'Pricing card', group: 'Cards', page: 'pricing' }, cardSel, 'default', 'at rest');
const cta = page.locator('main a').filter({ hasText: /Get started|Start|Sign up|Try/i }).first();
await one('pricing-cta', { title: 'Pricing action', group: 'Buttons', page: 'pricing' }, cta, 'default', 'at rest');

await open('https://app.mural.co/signin');
const email = page.locator('input[type="email"], input[name="email"], input[type="text"]').first();
await one('text-field', { title: 'Work email', group: 'Fields', page: 'signin', selector: 'input' }, email, 'default', 'at rest');
await one('text-field', { title: 'Work email', group: 'Fields', page: 'signin' }, email, 'focused', 'clicked into the field', async (el) => { await el.click(); await page.waitForTimeout(300); });
await one('text-field', { title: 'Work email', group: 'Fields', page: 'signin' }, email, 'filled', 'typed design@example.com then deleted', async (el) => {
  await el.click();
  await page.keyboard.type('design@example.com', { delay: 8 });
  await page.waitForTimeout(200);
});
await email.focus().catch(() => {});
await page.keyboard.press('Meta+a').catch(() => {});
await page.keyboard.press('Backspace').catch(() => {});
const login = page.getByRole('button', { name: /log in/i }).first();
await one('login-button', { title: 'Log in', group: 'Buttons', page: 'signin' }, login, 'default', 'at rest, not submitted');
await one('login-button', { title: 'Log in', group: 'Buttons', page: 'signin' }, login, 'hover', 'mouse hover', async (el) => { await el.hover(); await page.waitForTimeout(350); });
const box = page.locator('input[type="checkbox"]').first();
await one('checkbox', { title: 'Remember me', group: 'Fields', page: 'signin' }, box, 'default', 'at rest, not toggled');
const signupLink = page.getByRole('link', { name: /sign up/i }).first();
await one('auth-link', { title: 'Sign up for free', group: 'Links', page: 'signin' }, signupLink, 'default', 'at rest, not followed');

// Dump a short DOM map of signin and pricing for the README.
const maps = {};
maps.signin = await page.evaluate(() => {
  const vis = (el) => { const r = el.getBoundingClientRect(); return r.width > 8 && r.height > 8 && r.top < innerHeight && r.bottom > 0; };
  return {
    inputs: [...document.querySelectorAll('input')].map((el) => ({ type: el.type, name: el.name, ph: el.placeholder, id: el.id })),
    buttons: [...document.querySelectorAll('button')].filter(vis).map((el) => (el.innerText || el.getAttribute('aria-label') || '').trim().slice(0, 40)),
    links: [...document.querySelectorAll('a')].filter(vis).slice(0, 12).map((el) => ({ t: (el.innerText || '').trim().slice(0, 40), h: el.pathname })),
    h1: document.querySelector('h1')?.innerText?.slice(0, 60),
    fonts: getComputedStyle(document.body).fontFamily,
  };
});
await open('https://www.mural.co/pricing');
maps.pricing = await page.evaluate(() => {
  const heads = [...document.querySelectorAll('h1,h2,h3')].slice(0, 16).map((el) => el.tagName + ' ' + el.innerText.replace(/\s+/g, ' ').slice(0, 70));
  const classes = [...new Set([...document.querySelectorAll('[class*=pric], [class*=plan], [class*=card]')].map((el) => (el.className || '').toString().slice(0, 80)))].slice(0, 20);
  return { heads, classes };
});
fs.writeFileSync(path.join(RAW, 'dom-map.json'), JSON.stringify(maps, null, 1) + '\n');
fs.writeFileSync(path.join(RAW, 'components-computed.json'), JSON.stringify({
  _meta: { product: 'Mural', readAt: new Date().toISOString(), source: 'computed styles, 1440 CSS px, deviceScaleFactor 2, light, signed out. No form submitted.' },
  components,
}, null, 1) + '\n');
log('wrote', Object.keys(components).length);
await browser.close();
