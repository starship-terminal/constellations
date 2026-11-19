// Component-state readings for MonoDesk public + signed-out surfaces.
// Hover is a real mouse move. Focus-visible is keyboard. Pressed is a CDP
// forcePseudoState, never a real click on a submit or navigation control.
// Nav menus and FAQ rows are local toggles. Nothing is typed or submitted.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;

const HERE = path.dirname(fileURLToPath(import.meta.url));
const PKG = path.resolve(HERE, '..', '..', '..');
const CROPS = path.join(PKG, 'components', 'crops');
const RAW = path.join(PKG, 'raw');
fs.mkdirSync(CROPS, { recursive: true });
fs.mkdirSync(RAW, { recursive: true });

const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';

function hex(c) {
  const m = String(c || '').match(/rgba?\(\s*([\d.]+)[,\s]+([\d.]+)[,\s]+([\d.]+)(?:[,\s/]+([\d.]+))?\s*\)/);
  if (!m) return c;
  const h = (n) => Math.round(Number(n)).toString(16).padStart(2, '0');
  const a = m[4] === undefined ? 1 : Number(m[4]);
  if (a >= 0.999) return `#${h(m[1])}${h(m[2])}${h(m[3])}`;
  return `rgba(${Math.round(+m[1])}, ${Math.round(+m[2])}, ${Math.round(+m[3])}, ${Math.round(a * 1000) / 1000})`;
}

async function read(el) {
  if (!el) return null;
  const box = await el.boundingBox();
  const style = await el.evaluate((node) => {
    const cs = getComputedStyle(node);
    const keys = ['fontFamily','fontSize','fontWeight','lineHeight','letterSpacing','color','backgroundColor','borderRadius','borderTopWidth','borderTopColor','borderTopStyle','paddingTop','paddingRight','paddingBottom','paddingLeft','boxShadow','outline','outlineOffset','textTransform','height','gap','display'];
    const o = {};
    for (const k of keys) o[k] = cs[k];
    return o;
  });
  for (const k of ['color','backgroundColor','borderTopColor']) style[k] = hex(style[k]);
  return { box, style, text: ((await el.innerText().catch(() => '')) || '').trim().slice(0, 60) };
}

async function crop(page, el, name, pad = 8) {
  const box = await el.boundingBox();
  if (!box) return null;
  const file = path.join(CROPS, `${name}.png`);
  await page.screenshot({
    path: file,
    clip: {
      x: Math.max(0, box.x - pad),
      y: Math.max(0, box.y - pad),
      width: Math.min(1400, box.width + pad * 2),
      height: Math.min(800, box.height + pad * 2),
    },
  });
  return file;
}

async function force(page, el, state) {
  const session = await page.context().newCDPSession(page);
  const objectId = await el.evaluateHandle((n) => n);
  // Playwright element handle to CDP node via DOM.describeNode is awkward.
  // Use CSS.forcePseudoState through the element's backend node.
  const { node } = await session.send('DOM.describeNode', { objectId: objectId._objectId || (await objectId.evaluateHandle?.()) });
  return session;
}

const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US' });
const page = await context.newPage();
const cdp = await context.newCDPSession(page);
const out = { capturedAt: new Date().toISOString(), components: {} };

async function forcePseudo(el, states) {
  const handle = await el.elementHandle();
  if (!handle) return;
  const node = await cdp.send('DOM.describeNode', { objectId: handle._objectId ? undefined : undefined, backendNodeId: undefined }).catch(() => null);
  // Resolve via DOM.getDocument + query is unreliable. Use Runtime + DOM.requestNode.
  const obj = await cdp.send('DOM.requestNode', { objectId: (await handle.evaluateHandle((n) => n))._remoteObject?.objectId });
}

async function pseudo(el, states) {
  const handle = await el.elementHandle();
  const remote = handle._remoteObject || (await page.evaluateHandle((n) => n, handle));
  // Playwright ElementHandle has a private object id via CDP:
  const objectId = handle._objectId || remote._objectId;
  let nodeId;
  try {
    const described = await cdp.send('DOM.describeNode', { objectId });
    nodeId = described.node.backendNodeId;
    await cdp.send('CSS.enable');
    await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: states });
  } catch (e) {
    // fallback: DOM.requestNode
    try {
      const req = await cdp.send('DOM.requestNode', { objectId });
      await cdp.send('CSS.enable');
      await cdp.send('CSS.forcePseudoState', { nodeId: req.nodeId, forcedPseudoClasses: states });
      return async () => { await cdp.send('CSS.forcePseudoState', { nodeId: req.nodeId, forcedPseudoClasses: [] }).catch(() => {}); };
    } catch (e2) {
      return null;
    }
  }
  return async () => { await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: [] }).catch(() => {}); };
}

async function record(name, el, page) {
  const data = await read(el);
  await crop(page, el, name);
  out.components[name] = data;
  console.log(' ', name, data && data.style && data.style.backgroundColor, data && data.style && data.style.color, data && data.text);
}

// --- marketing home ---
await page.goto('https://www.monodesk.com/', { waitUntil: 'domcontentloaded', timeout: 45000 });
await page.waitForTimeout(1500);
const cta = page.getByRole('link', { name: /Get started free/ }).first();
await record('cta-primary-default', cta, page);
await cta.hover();
await page.waitForTimeout(250);
await record('cta-primary-hover', cta, page);
await cta.focus();
await page.waitForTimeout(150);
await record('cta-primary-focus', cta, page);
const clear = await pseudo(cta, ['focus-visible']);
await page.waitForTimeout(80);
await record('cta-primary-focus-visible', cta, page);
if (clear) await clear();
const clearP = await pseudo(cta, ['active']);
await page.waitForTimeout(80);
await record('cta-primary-pressed', cta, page);
if (clearP) await clearP();

const login = page.getByRole('link', { name: /^Log in$/ }).nth(1);
if (await login.count()) {
  await record('cta-secondary-default', login, page);
  await login.hover();
  await page.waitForTimeout(200);
  await record('cta-secondary-hover', login, page);
}

const navLogin = page.getByRole('link', { name: /^Log in$/ }).first();
await record('nav-link-default', navLogin, page);
await navLogin.hover();
await page.waitForTimeout(200);
await record('nav-link-hover', navLogin, page);

const nav = page.locator('header, nav').first();
await record('site-nav-default', nav, page);

const h1 = page.locator('h1').first();
await record('heading-hero', h1, page);

// nav menu
const featuresBtn = page.getByRole('button', { name: /Features/ }).first();
if (await featuresBtn.count()) {
  await featuresBtn.hover();
  await page.waitForTimeout(600);
  await record('nav-menu-trigger-hover', featuresBtn, page);
  const menu = page.locator('[role="menu"], [data-state="open"], header ul, nav ul').first();
  // try a visible dropdown panel
  const panel = page.locator('header a, nav a').filter({ hasText: 'Projects' }).first();
  if (await panel.count() && await panel.isVisible().catch(() => false)) {
    const wrap = panel.locator('xpath=ancestor::*[contains(@class,"menu") or contains(@class,"dropdown") or self::ul][1]');
    await record('nav-menu-item', panel, page);
  }
  await page.mouse.move(700, 700);
  await page.keyboard.press('Escape');
}

// FAQ on home if present
const faq = page.locator('button').filter({ hasText: /What is MonoDesk/ }).first();
if (await faq.count()) {
  await faq.scrollIntoViewIfNeeded();
  await page.waitForTimeout(300);
  await record('faq-default', faq, page);
  await faq.click();
  await page.waitForTimeout(400);
  await record('faq-open', faq, page);
}

// --- pricing ---
await page.goto('https://www.monodesk.com/pricing', { waitUntil: 'domcontentloaded', timeout: 45000 });
await page.waitForTimeout(1400);
const price = page.locator('text=$0').first();
if (await price.count()) await record('price-amount', price, page);
const planCta = page.getByRole('link', { name: /^Get started$/ }).first();
if (await planCta.count()) {
  await planCta.scrollIntoViewIfNeeded();
  await record('plan-cta-default', planCta, page);
  await planCta.hover();
  await page.waitForTimeout(200);
  await record('plan-cta-hover', planCta, page);
}
const badge = page.getByText('MOST POPULAR').first();
if (await badge.count()) await record('badge-popular', badge, page);
const pill = page.getByText(/ALWAYS FREE/i).first();
if (await pill.count()) await record('badge-free', pill, page);

// --- help (search field) ---
await page.goto('https://www.monodesk.com/help', { waitUntil: 'domcontentloaded', timeout: 45000 });
await page.waitForTimeout(1200);
const search = page.locator('input').first();
if (await search.count()) {
  await record('search-default', search, page);
  await search.focus();
  await page.waitForTimeout(200);
  await record('search-focus', search, page);
}

// --- login ---
await page.goto('https://app.monodesk.com/login', { waitUntil: 'domcontentloaded', timeout: 45000 });
await page.waitForTimeout(2200);
const email = page.locator('input[type="email"], input[placeholder*="email" i]').first();
const pass = page.locator('input[type="password"]').first();
const google = page.getByRole('button', { name: /Google/ }).first();
const submit = page.getByRole('button', { name: /^Login$/ }).first();
const card = page.locator('text=Login to your account').locator('xpath=ancestor::div[1]');
if (await email.count()) {
  await record('field-email-default', email, page);
  await email.hover();
  await page.waitForTimeout(150);
  await record('field-email-hover', email, page);
  await email.focus();
  await page.waitForTimeout(200);
  await record('field-email-focus', email, page);
}
if (await pass.count()) await record('field-password-default', pass, page);
if (await google.count()) {
  await record('button-google-default', google, page);
  await google.hover();
  await page.waitForTimeout(200);
  await record('button-google-hover', google, page);
}
if (await submit.count()) {
  await record('button-login-default', submit, page);
  await submit.hover();
  await page.waitForTimeout(200);
  await record('button-login-hover', submit, page);
  const clr = await pseudo(submit, ['active']);
  await page.waitForTimeout(80);
  await record('button-login-pressed', submit, page);
  if (clr) await clr();
  // disabled? don't submit. record as-is (empty form may already be disabled)
  await record('button-login-rest', submit, page);
}
const create = page.getByText('Create account').first();
if (await create.count()) {
  await record('link-create-default', create, page);
  await create.hover();
  await page.waitForTimeout(150);
  await record('link-create-hover', create, page);
}
const forgot = page.getByText('Forgot password?').first();
if (await forgot.count()) await record('link-forgot-default', forgot, page);

// card: the white panel
const panel = page.locator('div').filter({ hasText: 'Login to your account' }).filter({ has: page.locator('input') }).last();
if (await panel.count()) await record('login-card', panel, page);

// --- create (do not submit) ---
await page.goto('https://app.monodesk.com/create', { waitUntil: 'domcontentloaded', timeout: 45000 });
await page.waitForTimeout(2200);
const createH = page.locator('text=/Create account|first thing/i').first();
if (await createH.count()) await record('create-heading', createH, page);
const g2 = page.getByRole('button', { name: /Google/ }).first();
if (await g2.count()) await record('button-google-create', g2, page);
const email2 = page.locator('input').first();
if (await email2.count()) await record('field-create-email', email2, page);

await browser.close();
fs.writeFileSync(path.join(RAW, 'components-computed.json'), JSON.stringify(out, null, 2));
console.log('wrote', Object.keys(out.components).length, 'components');
