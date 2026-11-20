// Harvest Mural's public marketing site and the signed-out login.
// Measures computed styles, writes screenshots, crops, icons and raw JSON.
// Does not submit a form, start a trial, or enter a password.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node tools/capture/harvest.mjs
import crypto from 'node:crypto';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { execFileSync } from 'node:child_process';
import { screenshotWithMetadata } from './screenshot.mjs';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const PYTHON = process.env.PYTHON || 'python3';
const HERE = path.dirname(fileURLToPath(import.meta.url));
const PKG = path.resolve(HERE, '..', '..');
const RAW = path.join(PKG, 'raw');
const CROPS = path.join(PKG, 'components', 'crops');
const SHOTS = path.join(os.homedir(), '.design-systems', 'mural', 'raw-shots');
const ICONS = path.join(PKG, 'icons');
for (const d of [RAW, CROPS, SHOTS, ICONS]) fs.mkdirSync(d, { recursive: true });

const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
const UA_MOBILE = 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';

const PAGES = [
  { key: 'home', url: 'https://www.mural.co/' },
  { key: 'pricing', url: 'https://www.mural.co/pricing' },
  { key: 'product', url: 'https://www.mural.co/product' },
  { key: 'templates', url: 'https://www.mural.co/templates' },
  { key: 'enterprise', url: 'https://www.mural.co/enterprise' },
  { key: 'integrations', url: 'https://www.mural.co/integrations' },
  { key: 'signin', url: 'https://app.mural.co/signin' },
  { key: 'signup', url: 'https://app.mural.co/signup' },
];

const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);

function quantize(file) {
  execFileSync(PYTHON, ['-c',
    'import sys\nfrom PIL import Image\nf=sys.argv[1]\nim=Image.open(f).convert("RGB")\nif im.width*im.height>1200000: im=im.resize((im.width//2, im.height//2), Image.LANCZOS)\nim.quantize(256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).save(f, optimize=True)',
    file]);
}

async function settle(page) {
  await page.addStyleTag({ content: [
    '*{caret-color:transparent!important}',
    // Hide third-party overlays. Never click Accept, and never start a guide.
    '#onetrust-consent-sdk, .onetrust-pc-dark-filter, #cookie-law-info-bar, [class*="cookie-banner"], [id*="cookie-banner"]{display:none!important}',
    '[class*="pendo-"], #pendo-base, .pendo-resource-center-badge{display:none!important}',
  ].join('\n') }).catch(() => {});
  // Dismiss a visible close control only when its label is a dismiss, never a signup.
  const close = page.locator('button[aria-label="Close"], button[aria-label="Dismiss"], [aria-label="Close dialog"]').first();
  if (await close.count() && await close.isVisible().catch(() => false)) {
    const t = await close.evaluate((el) => (el.getAttribute('aria-label') || el.innerText || '').trim());
    if (/^(close|dismiss)/i.test(t)) await close.click({ timeout: 2000 }).catch(() => {});
  }
  await page.waitForTimeout(400);
}

async function lazyScroll(page) {
  const h = await page.evaluate(() => document.documentElement.scrollHeight);
  const cap = Math.min(h, 9000);
  for (let y = 0; y < cap; y += 700) {
    await page.evaluate((y) => scrollTo(0, y), y);
    await page.waitForTimeout(180);
  }
  await page.evaluate(() => scrollTo(0, 0));
  await page.waitForTimeout(400);
}

const PROPS = [
  'display', 'position', 'boxSizing', 'width', 'height',
  'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft',
  'gap', 'flexDirection', 'alignItems', 'justifyContent',
  'borderTopWidth', 'borderTopStyle', 'borderTopColor',
  'borderRightWidth', 'borderRightStyle', 'borderRightColor',
  'borderBottomWidth', 'borderBottomStyle', 'borderBottomColor',
  'borderLeftWidth', 'borderLeftStyle', 'borderLeftColor',
  'borderTopLeftRadius', 'borderTopRightRadius', 'borderBottomRightRadius', 'borderBottomLeftRadius',
  'backgroundColor', 'backgroundImage', 'boxShadow',
  'outlineWidth', 'outlineStyle', 'outlineColor', 'outlineOffset',
  'fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'letterSpacing', 'textTransform',
  'color', 'textDecorationLine', 'transitionProperty', 'transitionDuration', 'transitionTimingFunction',
  'cursor', 'opacity',
];

function styleOfExpr() {
  const props = PROPS;
  return (el) => {
    const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\(\s*(?!['"]?(?:data:|#))(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|[^)]*)\s*\)/g, 'url(…)') : v);
    const cs = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    const style = {};
    for (const p of props) style[p] = noUrl(cs[p]);
    const text = (el.innerText || el.getAttribute('aria-label') || el.getAttribute('placeholder') || '').trim().replace(/\s+/g, ' ').slice(0, 90);
    const out = {
      tag: el.tagName.toLowerCase(),
      classes: [...el.classList].slice(0, 5).join(' '),
      text,
      rect: { x: +r.x.toFixed(1), y: +r.y.toFixed(1), w: +r.width.toFixed(2), h: +r.height.toFixed(2) },
      style,
    };
    const walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT, { acceptNode: (t) => (t.textContent.trim() ? 1 : 3) });
    const tn = walker.nextNode();
    if (tn && tn.parentElement && tn.parentElement !== el) {
      const tc = getComputedStyle(tn.parentElement);
      out.textStyle = {
        node: tn.parentElement.tagName.toLowerCase(),
        text: tn.textContent.trim().slice(0, 40),
        fontFamily: tc.fontFamily, fontSize: tc.fontSize, lineHeight: tc.lineHeight,
        fontWeight: tc.fontWeight, letterSpacing: tc.letterSpacing, color: tc.color,
      };
    }
    if (el.tagName === 'INPUT' || el.tagName === 'TEXTAREA') {
      const ph = getComputedStyle(el, '::placeholder');
      out.placeholder = { color: ph.color, fontSize: ph.fontSize };
    }
    return out;
  };
}

async function crop(page, locator, name) {
  const file = path.join(CROPS, `${name}.png`);
  const box = await locator.boundingBox();
  if (!box || box.width < 2 || box.height < 2) throw new Error('no box ' + name);
  const vp = page.viewportSize();
  const pad = 10;
  const clip = {
    x: Math.max(0, box.x - pad),
    y: Math.max(0, box.y - pad),
    width: Math.min(vp.width - Math.max(0, box.x - pad), box.width + 2 * pad),
    height: Math.min(vp.height - Math.max(0, box.y - pad), box.height + 2 * pad),
  };
  if (clip.width < 4 || clip.height < 4) throw new Error('clip too small ' + name);
  await page.screenshot({ path: file, clip, animations: 'disabled' });
  quantize(file);
  return path.relative(PKG, file);
}

async function readVars(page) {
  return page.evaluate(() => {
    const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\(\s*(?!['"]?(?:data:|#))(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|[^)]*)\s*\)/g, 'url(…)') : v);
    const root = getComputedStyle(document.documentElement);
    const rules = [];
    const fonts = [];
    const walk = (list, ctx, file) => {
      for (const r of list) {
        if (r.type === CSSRule.FONT_FACE_RULE) {
          const o = { file };
          for (let i = 0; i < r.style.length; i++) o[r.style[i]] = noUrl(r.style.getPropertyValue(r.style[i]).trim()).slice(0, 180);
          fonts.push(o);
          continue;
        }
        if (r.cssRules && !r.style) {
          const head = r.media ? '@media ' + r.media.mediaText : (r.conditionText ? '@supports ' + r.conditionText : 'group');
          try { walk(r.cssRules, [...ctx, head], file); } catch (e) {}
          continue;
        }
        if (!r.style) continue;
        const props = {};
        for (let i = 0; i < r.style.length; i++) {
          const k = r.style[i];
          if (k && k.startsWith('--')) props[k] = noUrl(r.style.getPropertyValue(k).trim()).slice(0, 240);
        }
        if (Object.keys(props).length) rules.push({ file, selector: (r.selectorText || '').slice(0, 160), context: ctx, properties: props });
      }
    };
    const hrefs = [];
    let blocked = 0;
    for (const sheet of document.styleSheets) {
      const href = sheet.href || 'inline';
      let ruleset;
      try { ruleset = sheet.cssRules; } catch (e) { blocked++; hrefs.push({ href: href.slice(0, 160), blocked: true }); continue; }
      hrefs.push({ href: href.slice(0, 160), rules: ruleset.length });
      walk(ruleset, [], href.slice(0, 80));
    }
    const resolved = {};
    const names = [...new Set(rules.flatMap((r) => Object.keys(r.properties)))];
    for (const n of names) {
      const v = noUrl(root.getPropertyValue(n).trim());
      if (v) resolved[n] = v.slice(0, 240);
    }
    return {
      hrefs, blocked, rules, fonts, resolved,
      body: {
        fontFamily: getComputedStyle(document.body).fontFamily,
        fontSize: getComputedStyle(document.body).fontSize,
        color: getComputedStyle(document.body).color,
        backgroundColor: getComputedStyle(document.body).backgroundColor,
        fontWeight: getComputedStyle(document.body).fontWeight,
      },
    };
  });
}

function collectIconsExpr() {
  return () => {
    const rgb = (c) => { const m = String(c).match(/rgba?\(([^)]+)\)/); return m ? m[1].split(',').slice(0, 3).map((x) => Math.round(parseFloat(x))).join(',') : c; };
    const hex = (c) => { const m = String(c).match(/rgba?\(([^)]+)\)/); if (!m) return c; const [r, g, b] = m[1].split(',').map((x) => Math.round(parseFloat(x))); return '#' + [r, g, b].map((v) => v.toString(16).padStart(2, '0')).join(''); };
    return [...document.querySelectorAll('svg')].filter((s) => {
      const r = s.getBoundingClientRect();
      if (!(r.width >= 10 && r.width <= 48 && r.height >= 10 && r.height <= 48)) return false;
      if (s.closest('svg svg')) return false;
      return getComputedStyle(s).visibility !== 'hidden' && r.bottom > 0 && r.top < innerHeight + 200;
    }).slice(0, 40).map((s) => {
      const r = s.getBoundingClientRect();
      const col = rgb(getComputedStyle(s).color);
      const c = s.cloneNode(true);
      const shapes = [...s.querySelectorAll('path,circle,rect,line,polyline,polygon,ellipse')];
      const cshapes = [...c.querySelectorAll('path,circle,rect,line,polyline,polygon,ellipse')];
      shapes.forEach((e, i) => {
        const cs = getComputedStyle(e);
        const t = cshapes[i];
        if (!t) return;
        for (const a of ['fill', 'stroke']) {
          const attr = t.getAttribute(a);
          if (attr && attr.startsWith('var(')) t.setAttribute(a, rgb(cs[a]) === col ? 'currentColor' : hex(cs[a]));
        }
        if (!t.hasAttribute('fill') && cs.fill && cs.fill !== 'none' && !String(cs.fill).startsWith('url')) {
          t.setAttribute('fill', rgb(cs.fill) === col ? 'currentColor' : hex(cs.fill));
        }
      });
      c.setAttribute('xmlns', 'http://www.w3.org/2000/svg');
      for (const a of ['id', 'class', 'style', 'focusable', 'aria-hidden']) c.removeAttribute(a);
      c.querySelectorAll('[id],[class],[style]').forEach((e) => { e.removeAttribute('id'); e.removeAttribute('class'); e.removeAttribute('style'); });
      if (!c.getAttribute('viewBox')) c.setAttribute('viewBox', `0 0 ${Math.round(r.width)} ${Math.round(r.height)}`);
      const holder = s.closest('a,button,[role=button]');
      const label = (s.getAttribute('aria-label') || holder?.getAttribute('aria-label') || holder?.innerText || '').trim().replace(/\s+/g, ' ').slice(0, 40);
      return { w: Math.round(r.width), h: Math.round(r.height), html: c.outerHTML.slice(0, 8000), label };
    });
  };
}

async function shot(page, name, requested) {
  const file = path.join(SHOTS, name + '.png');
  await screenshotWithMetadata(page, { path: file }, requested);
  log('  shot', name);
  return file;
}

async function fullShot(page, name, requested) {
  await lazyScroll(page);
  const H = await page.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
  const dpr = requested.deviceScaleFactor;
  const chunk = Math.floor(14000 / dpr);
  const cap = Math.min(H, 8 * chunk);
  const base = path.join(SHOTS, name);
  if (cap <= chunk) {
    await screenshotWithMetadata(page, { path: base + '.png', fullPage: true }, { ...requested, sanitizedSourceUrl: requested.sanitizedSourceUrl });
  } else {
    for (let i = 0, y = 0; y < cap; i++, y += chunk) {
      await screenshotWithMetadata(page, {
        path: `${base}.part${i}.png`, fullPage: true,
        clip: { x: 0, y, width: requested.viewport.width, height: Math.min(chunk, cap - y) },
      }, requested);
    }
  }
  log('  full', name, 'H=' + H);
  await page.evaluate(() => scrollTo(0, 0));
}

const components = {};
const layout = {};
const icons = new Map();
const pageNotes = [];

function rememberIcon(list, pageKey) {
  for (const ic of list) {
    const key = crypto.createHash('md5').update(ic.html.replace(/\s(width|height)="[^"]*"/g, '')).digest('hex').slice(0, 10);
    const hit = icons.get(key);
    if (hit) { hit.where.add(pageKey); if (ic.label) hit.labels.add(ic.label); continue; }
    icons.set(key, { ...ic, key, where: new Set([pageKey]), labels: new Set(ic.label ? [ic.label] : []) });
  }
}

async function measureNamed(page, pageKey, specs) {
  const read = styleOfExpr();
  for (const spec of specs) {
    try {
      const loc = page.locator(spec.sel).filter({ visible: true }).first();
      if (!(await loc.count())) { log('  miss', spec.key); continue; }
      await loc.evaluate((el) => el.scrollIntoView({ block: 'center', inline: 'nearest' })).catch(() => {});
      await page.waitForTimeout(200);
      const box = await loc.boundingBox();
      if (!box || box.y < -20 || box.y > 860) {
        // still measure if in view after scroll
      }
      if (spec.state === 'hover') {
        await loc.hover({ timeout: 4000 }).catch(() => {});
        await page.waitForTimeout(350);
      } else if (spec.state === 'focus-visible') {
        await loc.focus().catch(() => {});
        await page.keyboard.press('Shift+Tab').catch(() => {});
        await page.keyboard.press('Tab').catch(() => {});
        await page.waitForTimeout(250);
      } else if (spec.state === 'focused') {
        await loc.click({ timeout: 3000 }).catch(() => {});
        await page.waitForTimeout(250);
      } else if (spec.state === 'filled') {
        await loc.click({ timeout: 3000 }).catch(() => {});
        await page.keyboard.type('design@example.com', { delay: 8 });
        await page.waitForTimeout(200);
      }
      const s = await loc.evaluate(read);
      let cropFile = null;
      try { cropFile = await crop(page, loc, `${spec.key}-${spec.state}`); } catch (e) { s.cropError = String(e.message).slice(0, 120); }
      const c = components[spec.key] ??= { title: spec.title, group: spec.group, page: pageKey, selector: spec.sel, states: {} };
      c.states[spec.state] = { ...s, crop: cropFile, via: spec.via || spec.state };
      log('  ', spec.key, spec.state, s.rect && (s.rect.w + 'x' + s.rect.h));
      if (spec.state === 'filled') {
        await loc.focus().catch(() => {});
        await page.keyboard.press('Meta+a').catch(() => {});
        await page.keyboard.press('Backspace').catch(() => {});
      }
      await page.mouse.move(8, 8).catch(() => {});
    } catch (e) {
      log('  !', spec.key, spec.state, String(e.message).slice(0, 140));
    }
  }
}

const HOME_SPECS = [
  { key: 'nav-link', title: 'Nav link', group: 'Navigation', sel: 'a.nav-link_toggle.is-link', state: 'default' },
  { key: 'nav-link', title: 'Nav link', group: 'Navigation', sel: 'a.nav-link_toggle.is-link', state: 'hover', via: 'mouse hover' },
  { key: 'button-primary', title: 'Sign up button', group: 'Buttons', sel: 'a.button_component.test-dark-navbar-new', state: 'default' },
  { key: 'button-primary', title: 'Sign up button', group: 'Buttons', sel: 'a.button_component.test-dark-navbar-new', state: 'hover', via: 'mouse hover' },
  { key: 'button-outline', title: 'Book a demo button', group: 'Buttons', sel: 'a.button_component.test-light-outline-new-6', state: 'default' },
  { key: 'button-outline', title: 'Book a demo button', group: 'Buttons', sel: 'a.button_component.test-light-outline-new-6', state: 'hover', via: 'mouse hover' },
  { key: 'display', title: 'Hero display', group: 'Type', sel: 'h1.home_hero-h1', state: 'default' },
  { key: 'body', title: 'Hero body', group: 'Type', sel: '.section_home-hero p', state: 'default' },
  { key: 'eyebrow', title: 'Logo eyebrow', group: 'Type', sel: 'h2.logos_h2', state: 'default' },
  { key: 'text-link', title: 'Inline link', group: 'Links', sel: 'main a.button_component, main a[class*="text-link"], main a.link', state: 'default' },
];

const PRICING_SPECS = [
  { key: 'pricing-card', title: 'Pricing card', group: 'Cards', sel: '[class*="pricing"] [class*="card"], [class*="price-card"], [class*="plan"]', state: 'default' },
  { key: 'pricing-cta', title: 'Pricing call to action', group: 'Buttons', sel: 'main a.button_component', state: 'default' },
];

const SIGNIN_SPECS = [
  { key: 'text-field', title: 'Work email field', group: 'Fields', sel: 'input[type="email"], input[name="email"], input[autocomplete="username"]', state: 'default' },
  { key: 'text-field', title: 'Work email field', group: 'Fields', sel: 'input[type="email"], input[name="email"], input[autocomplete="username"]', state: 'focused', via: 'clicked into the field' },
  { key: 'text-field', title: 'Work email field', group: 'Fields', sel: 'input[type="email"], input[name="email"], input[autocomplete="username"]', state: 'filled', via: 'typed design@example.com, then deleted; nothing sent' },
  { key: 'login-button', title: 'Log in button', group: 'Buttons', sel: 'button[type="submit"], button', state: 'default' },
  { key: 'checkbox', title: 'Remember me', group: 'Fields', sel: 'input[type="checkbox"]', state: 'default' },
  { key: 'auth-link', title: 'Sign up for free', group: 'Links', sel: 'a', state: 'default' },
];

const browser = await chromium.launch({ headless: true });

async function runWidth(mobile) {
  const vw = mobile ? 390 : 1440;
  const vh = mobile ? 844 : 900;
  const dpr = mobile ? 2 : 1;
  const prefix = mobile ? 'mobile-' : '';
  const ctx = await browser.newContext({
    viewport: { width: vw, height: vh },
    deviceScaleFactor: dpr,
    userAgent: mobile ? UA_MOBILE : UA,
    isMobile: mobile,
    hasTouch: mobile,
    locale: 'en-US',
  });
  const page = await ctx.newPage();
  page.setDefaultTimeout(12000);
  for (const spec of PAGES) {
    const name = prefix + spec.key;
    log('open', name, spec.url);
    let status = 0;
    try {
      const res = await page.goto(spec.url, { waitUntil: 'domcontentloaded', timeout: 60000 });
      status = res ? res.status() : 0;
      await page.waitForTimeout(2800);
      const gate = await page.evaluate(() => ({
        title: document.title,
        href: location.href.split('?')[0],
        cf: /just a moment|attention required|cloudflare/i.test(document.title),
      }));
      if (gate.cf) {
        pageNotes.push({ page: name, url: spec.url, blocked: 'cloudflare', title: gate.title });
        log('  CLOUDFLARE', name);
        continue;
      }
      await settle(page);
      const requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, sanitizedSourceUrl: spec.url };
      await shot(page, `${name}-light-default`, requested);
      if (!mobile && (spec.key === 'home' || spec.key === 'pricing' || spec.key === 'signin')) {
        await fullShot(page, `${name}-light-full`, requested);
      }
      if (!mobile && spec.key === 'home') {
        const vars = await readVars(page);
        fs.writeFileSync(path.join(RAW, 'css-vars.json'), JSON.stringify({
          readAt: new Date().toISOString().slice(0, 10),
          source: 'computed custom properties and readable stylesheets on https://www.mural.co/ at 1440x900, light, signed out',
          viewport: { width: vw, height: vh },
          ...vars,
        }, null, 1) + '\n');
        log('  vars', Object.keys(vars.resolved).length, 'fonts', vars.fonts.length, 'rules', vars.rules.length);
        await measureNamed(page, 'home', HOME_SPECS);
        // Open the Product menu without navigating away, if it is a disclosure.
        const product = page.locator('nav button, .navbar_v2_component button, [class*="nav-link"] button, .w-dropdown-toggle').filter({ hasText: /^Product$/ }).first();
        if (await product.count()) {
          await product.click({ timeout: 3000 }).catch(() => {});
          await page.waitForTimeout(500);
          await shot(page, 'home-light-product-menu', requested);
          await page.keyboard.press('Escape').catch(() => {});
        }
      }
      if (!mobile && spec.key === 'pricing') await measureNamed(page, 'pricing', PRICING_SPECS);
      if (!mobile && spec.key === 'signin') await measureNamed(page, 'signin', SIGNIN_SPECS);
      if (!mobile && spec.key === 'signup') {
        const gate2 = await page.evaluate(() => (document.body.innerText || '').slice(0, 400));
        pageNotes.push({ page: 'signup', text: gate2.replace(/\s+/g, ' ').slice(0, 240), href: page.url().split('?')[0] });
      }
      const iconsHere = await page.evaluate(collectIconsExpr());
      rememberIcon(iconsHere, name);
      const lay = await page.evaluate(() => {
        const R = (e) => { if (!e) return null; const r = e.getBoundingClientRect(); return { x: +r.x.toFixed(1), y: +r.y.toFixed(1), w: +r.width.toFixed(1), h: +r.height.toFixed(1) }; };
        const nav = document.querySelector('nav, .navbar_v2_component, header');
        const h1 = document.querySelector('h1');
        const main = document.querySelector('main');
        return {
          title: document.title,
          href: location.href.split('?')[0],
          vw: innerWidth, vh: innerHeight, dpr: devicePixelRatio,
          nav: nav && { ...R(nav), bg: getComputedStyle(nav).backgroundColor, h: getComputedStyle(nav).height },
          h1: h1 && { text: h1.innerText.replace(/\s+/g, ' ').slice(0, 80), font: getComputedStyle(h1).fontFamily, size: getComputedStyle(h1).fontSize, weight: getComputedStyle(h1).fontWeight, color: getComputedStyle(h1).color, ls: getComputedStyle(h1).letterSpacing, lh: getComputedStyle(h1).lineHeight, ...R(h1) },
          mainH: main ? main.getBoundingClientRect().height : null,
          scrollH: document.documentElement.scrollHeight,
        };
      });
      layout[name] = { url: spec.url, status, ...lay };
      pageNotes.push({ page: name, status, title: lay.title, href: lay.href });
    } catch (e) {
      log('  PAGE FAILED', name, String(e.message).split('\n')[0]);
      pageNotes.push({ page: name, url: spec.url, error: String(e.message).slice(0, 200) });
    }
  }
  await ctx.close();
}

await runWidth(false);
await runWidth(true);
await browser.close();

// Icons
const index = ['file\trole\tpages\tpx'];
let n = 0;
for (const ic of icons.values()) {
  if (n >= 24) break;
  const role = [...ic.labels][0] || 'icon-' + ic.key;
  const file = (role.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '').slice(0, 40) || 'icon') + '-' + ic.key + '.svg';
  fs.writeFileSync(path.join(ICONS, file), ic.html);
  index.push([file, role.replace(/\t/g, ' '), [...ic.where].join(','), `${ic.w}x${ic.h}`].join('\t'));
  n++;
}
fs.writeFileSync(path.join(ICONS, 'INDEX.tsv'), index.join('\n') + '\n');

// measure-only.mjs is the one writer of raw/components-computed.json (the committed readings); the
// harvest keeps its own looser first pass apart so a rerun cannot replace them.
fs.writeFileSync(path.join(RAW, 'components-harvest.json'), JSON.stringify({
  _meta: {
    product: 'Mural',
    readAt: new Date().toISOString(),
    source: 'computed styles on public mural.co pages and the signed-out app.mural.co login, 1440x900, light',
    note: 'No form was submitted. The filled email was design@example.com and was deleted.',
  },
  components,
}, null, 1) + '\n');
fs.writeFileSync(path.join(RAW, 'layout.json'), JSON.stringify(layout, null, 1) + '\n');
fs.writeFileSync(path.join(RAW, 'pages.json'), JSON.stringify(pageNotes, null, 1) + '\n');
log('done', 'components', Object.keys(components).length, 'icons', n, 'pages', pageNotes.length);
