// Live public capture for the clay slug.
// clay.earth 301s to https://me.sh/ (the Clay product rebranded to Mesh).
// Signed-out marketing pages only. Sign-in is opened and measured, never submitted.
// Nothing is typed into a phone, card, SSO, or CRM import.
import fs from 'node:fs';
import path from 'node:path';
const pw = await import(process.env.PLAYWRIGHT || 'playwright');  // PLAYWRIGHT=/path/to/playwright/index.mjs
const { chromium } = pw.default ?? pw;

const ROOT = path.resolve(path.dirname(new URL(import.meta.url).pathname), '../..');
const RAW = path.join(ROOT, 'raw');
const SHOTS = path.join(ROOT, 'screenshots');
const CROPS = path.join(ROOT, 'components', 'crops');
fs.mkdirSync(RAW, { recursive: true });
fs.mkdirSync(SHOTS, { recursive: true });
fs.mkdirSync(CROPS, { recursive: true });

const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
const UA_MOBILE = 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';

const PROPS = [
  'display', 'position', 'boxSizing', 'width', 'height',
  'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft',
  'marginTop', 'marginRight', 'marginBottom', 'marginLeft',
  'gap', 'borderTopWidth', 'borderTopStyle', 'borderTopColor',
  'borderTopLeftRadius', 'borderTopRightRadius', 'borderBottomRightRadius', 'borderBottomLeftRadius',
  'backgroundColor', 'backgroundImage', 'boxShadow',
  'outlineWidth', 'outlineStyle', 'outlineColor', 'outlineOffset',
  'fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'letterSpacing', 'textTransform',
  'color', 'textDecorationLine', 'opacity', 'cursor',
  'transitionProperty', 'transitionDuration', 'transitionTimingFunction',
];

const noUrl = (v) => (typeof v === 'string'
  ? v.replace(/url\(\s*(?!['"]?(?:data:|#))(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|[^)]*)\s*\)/g, 'url(…)')
  : v);

async function styleOf(locator) {
  return locator.evaluate((el, props) => {
    const noUrl = (v) => (typeof v === 'string'
      ? v.replace(/url\(\s*(?!['"]?(?:data:|#))(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|[^)]*)\s*\)/g, 'url(…)')
      : v);
    const pick = (cs) => {
      const o = {};
      for (const p of props) o[p] = noUrl(cs[p]);
      return o;
    };
    const cs = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    const out = {
      tag: el.tagName.toLowerCase(),
      id: el.id || undefined,
      classes: [...el.classList].slice(0, 6).join(' '),
      text: (el.innerText || el.getAttribute('aria-label') || el.getAttribute('placeholder') || '').trim().replace(/\s+/g, ' ').slice(0, 90),
      href: el.href || undefined,
      rect: { x: +r.x.toFixed(1), y: +r.y.toFixed(1), w: +r.width.toFixed(1), h: +r.height.toFixed(1) },
      style: pick(cs),
    };
    for (const pe of ['::before', '::after']) {
      const p = getComputedStyle(el, pe);
      if (p.content && p.content !== 'none' && p.content !== 'normal') {
        out[pe] = {
          content: noUrl(p.content).slice(0, 60),
          backgroundColor: p.backgroundColor,
          backgroundImage: noUrl(p.backgroundImage).slice(0, 240),
          boxShadow: p.boxShadow,
          width: p.width, height: p.height, borderRadius: p.borderRadius, opacity: p.opacity,
        };
      }
    }
    const paint = [];
    const nodes = [el, ...el.querySelectorAll('*')].slice(0, 80);
    for (const n of nodes) {
      if (paint.length >= 8) break;
      const c = getComputedStyle(n);
      const bg = c.backgroundColor !== 'rgba(0, 0, 0, 0)' ? c.backgroundColor : '';
      const sh = c.boxShadow !== 'none' ? c.boxShadow : '';
      const bw = parseFloat(c.borderTopWidth) > 0 ? `${c.borderTopWidth} ${c.borderTopStyle} ${c.borderTopColor}` : '';
      if (!(bg || sh || bw)) continue;
      const rr = n.getBoundingClientRect();
      paint.push({
        node: n.tagName.toLowerCase() + [...n.classList].slice(0, 2).map((x) => '.' + x).join(''),
        size: `${rr.width.toFixed(0)}x${rr.height.toFixed(0)}`,
        bg: bg || undefined, shadow: sh || undefined, border: bw || undefined,
        radius: c.borderRadius !== '0px' ? c.borderRadius : undefined,
        color: c.color, fontSize: c.fontSize, fontWeight: c.fontWeight, fontFamily: c.fontFamily.split(',')[0],
      });
    }
    if (paint.length) out.paint = paint;
    if (el.tagName === 'INPUT' || el.tagName === 'TEXTAREA') {
      const ph = getComputedStyle(el, '::placeholder');
      out.placeholder = { color: ph.color, fontSize: ph.fontSize, fontFamily: ph.fontFamily.split(',')[0] };
    }
    return out;
  }, PROPS);
}

async function clearChallenge(page) {
  for (let i = 0; i < 8; i++) {
    const s = await page.evaluate(() => ({
      title: document.title,
      body: (document.body && document.body.innerText || '').slice(0, 400),
    })).catch(() => ({ title: '', body: '' }));
    const challenging = /just a moment/i.test(s.title)
      || /performing security verification|verify you are human|checking your browser|cloudflare/i.test(s.body.slice(0, 200));
    if (!challenging && s.body.length > 40) return { ok: true, title: s.title };
    await page.waitForTimeout(1500);
  }
  return { ok: false };
}

async function meta(page) {
  return page.evaluate(() => ({
    href: location.href,
    title: document.title,
    innerWidth: window.innerWidth,
    innerHeight: window.innerHeight,
    dpr: window.devicePixelRatio,
    visualViewport: window.visualViewport && {
      width: window.visualViewport.width,
      height: window.visualViewport.height,
      scale: window.visualViewport.scale,
    },
    colorScheme: getComputedStyle(document.documentElement).colorScheme,
    htmlBg: getComputedStyle(document.documentElement).backgroundColor,
    bodyBg: getComputedStyle(document.body).backgroundColor,
    bodyColor: getComputedStyle(document.body).color,
    bodyFont: getComputedStyle(document.body).fontFamily,
    bodySize: getComputedStyle(document.body).fontSize,
    bodyWeight: getComputedStyle(document.body).fontWeight,
    bodyLine: getComputedStyle(document.body).lineHeight,
    scrollHeight: document.documentElement.scrollHeight,
  }));
}

async function vars(page) {
  return page.evaluate(() => {
    const props = {};
    const fonts = [];
    const walk = (rules, ctx) => {
      for (const r of rules) {
        if (r.cssRules) {
          const media = r.conditionText || r.media?.mediaText || '';
          walk(r.cssRules, media ? ctx.concat(media) : ctx);
          continue;
        }
        if (r.style) {
          for (const name of r.style) {
            if (name.startsWith('--')) {
              props[name] = props[name] || { value: r.style.getPropertyValue(name).trim().slice(0, 180), selector: (r.selectorText || '').slice(0, 120), context: ctx.slice(0, 3) };
            }
          }
        }
        if (r.type === CSSRule.FONT_FACE_RULE) {
          fonts.push({
            family: r.style.getPropertyValue('font-family').replace(/['"]/g, ''),
            weight: r.style.getPropertyValue('font-weight'),
            style: r.style.getPropertyValue('font-style'),
          });
        }
      }
    };
    let sheetErrors = 0;
    for (const ss of document.styleSheets) {
      try { walk(ss.cssRules, []); } catch { sheetErrors++; }
    }
    const root = {};
    const cs = getComputedStyle(document.documentElement);
    for (const name of Object.keys(props)) root[name] = cs.getPropertyValue(name).trim().slice(0, 180);
    return { declared: Object.keys(props).length, sheetErrors, props, fonts, resolvedOnRoot: root };
  });
}

const MAX_CHUNKS = 8;  // bound every full-page shot (AGENTS.md): at most 8 viewport heights, as the kit's shooter

async function shot(page, name, full = false) {
  const file = path.join(SHOTS, name + '.png');
  const m = await meta(page);
  const docH = full ? await page.evaluate(() => document.documentElement.scrollHeight) : 0;
  const truncated = full && docH > MAX_CHUNKS * m.innerHeight;
  await page.screenshot({ path: file, fullPage: full, animations: 'disabled',
    ...(truncated ? { clip: { x: 0, y: 0, width: m.innerWidth, height: MAX_CHUNKS * m.innerHeight } } : {}) });
  const buf = fs.readFileSync(file);
  const pngW = buf.readUInt32BE(16);
  const pngH = buf.readUInt32BE(20);
  const sidecar = {
    capturedAt: new Date().toISOString(),
    screenshot: name + '.png',
    sourceUrl: m.href.split('?')[0],
    title: m.title,
    requested: { viewport: { width: m.innerWidth, height: m.innerHeight } },
    actual: m,
    png: { width: pngW, height: pngH },
    fullPage: full,
    ...(truncated ? { boundary: `document is ${docH}px tall; the shot stops at ${MAX_CHUNKS} viewport heights` } : {}),
    note: 'Live headless Chromium. Preview browser could not navigate off a stuck tab and returned "The browser is not producing screenshot frames".',
  };
  fs.writeFileSync(file + '.capture.json', JSON.stringify(sidecar, null, 2) + '\n');
  return sidecar;
}

async function crop(page, locator, name) {
  const file = path.join(CROPS, name + '.png');
  const box = await locator.boundingBox().catch(() => null);
  if (!box || box.width < 2 || box.height < 2) return null;
  const vp = page.viewportSize();
  const pad = 6;
  const clip = {
    x: Math.max(0, box.x - pad),
    y: Math.max(0, box.y - pad),
    width: Math.min(vp.width - Math.max(0, box.x - pad), box.width + 2 * pad),
    height: Math.min(vp.height - Math.max(0, box.y - pad), box.height + 2 * pad),
  };
  if (clip.width < 4 || clip.height < 4) return null;
  await page.screenshot({ path: file, clip, animations: 'disabled' });
  return path.relative(ROOT, file);
}

const readings = { capturedAt: new Date().toISOString(), pages: {}, components: {}, gaps: [] };

async function openPage(context, url) {
  const page = await context.newPage();
  const resp = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 }).catch((e) => ({ error: String(e) }));
  const gate = await clearChallenge(page);
  await page.waitForTimeout(2500);
  return { page, status: resp && resp.status ? resp.status() : null, gate, finalUrl: page.url() };
}

function pick(page, sel) {
  return page.locator(sel).first();
}

async function record(page, key, locator, states, extra = {}) {
  const entry = { ...extra, states: {} };
  const loc = locator;
  const count = await loc.count().catch(() => 0);
  if (!count) {
    entry.missing = true;
    readings.components[key] = entry;
    return;
  }
  const target = loc;
  for (const st of states) {
    try {
      if (st === 'hover') {
        await target.hover({ timeout: 4000 });
        await page.waitForTimeout(250);
      } else if (st === 'focus-visible') {
        // keyboard focus only: a click fallback followed nav links and navigated mid-recording
        await target.focus();
        await page.waitForTimeout(200);
      }
      const style = await styleOf(target);
      let cropPath = null;
      if (st === 'default' || st === 'hover') cropPath = await crop(page, target, `${key}-${st}`);
      entry.states[st] = { via: st === 'default' ? 'at rest' : st, style, crop: cropPath };
    } catch (e) {
      entry.states[st] = { error: String(e.message || e).slice(0, 180) };
    }
  }
  readings.components[key] = entry;
}

async function runDesktop() {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({
    viewport: { width: 1440, height: 900 },
    deviceScaleFactor: 1,
    userAgent: UA,
    locale: 'en-US',
  });
  const routes = [
    ['home', 'https://clay.earth/'],
    ['pricing', 'https://me.sh/pricing'],
    ['integrations', 'https://me.sh/integrations'],
    ['teams', 'https://me.sh/teams'],
    ['about', 'https://me.sh/about'],
    ['contact', 'https://me.sh/contact'],
    ['signin', 'https://app.me.sh/login?signin'],
  ];
  for (const [name, url] of routes) {
    console.log('page', name, url);
    const { page, status, gate, finalUrl } = await openPage(context, url);
    const m = await meta(page);
    const v = name === 'home' || name === 'signin' || name === 'pricing' ? await vars(page) : null;
    readings.pages[name] = { requested: url, status, gate, finalUrl, meta: m, vars: v && { declared: v.declared, sheetErrors: v.sheetErrors, fontCount: v.fonts.length, fonts: v.fonts, propNames: Object.keys(v.props), resolvedOnRoot: v.resolvedOnRoot } };
    if (v) fs.writeFileSync(path.join(RAW, `css-vars-${name}.json`), JSON.stringify(v, null, 2));
    const theme = m.htmlBg === 'rgb(0, 0, 0)' ? 'dark' : 'light';  // every shot name takes the painted theme
    await shot(page, `${name}-${theme}-default`, false);
    if (name === 'home') {
      await page.evaluate(() => window.scrollTo(0, 0));
      await record(page, 'page', pick(page, 'html'), ['default'], { group: 'Foundations', title: 'Page ground' });
      await record(page, 'body', pick(page, 'body'), ['default'], { group: 'Foundations', title: 'Body' });
      await record(page, 'hero-title', pick(page, 'h1'), ['default'], { group: 'Type', title: 'Hero title' });
      await record(page, 'section-title', pick(page, 'h2'), ['default'], { group: 'Type', title: 'Section title' });
      await record(page, 'nav-link', page.getByRole('link', { name: /^pricing$/i }).first(), ['default', 'hover', 'focus-visible'], { group: 'Navigation', title: 'Nav link' });
      await record(page, 'primary-cta', page.getByRole('link', { name: /get mesh free|get started/i }).first(), ['default', 'hover'], { group: 'Button', title: 'Primary CTA' });
      await record(page, 'signin-link', page.getByRole('link', { name: /sign in/i }).first(), ['default', 'hover'], { group: 'Link', title: 'Sign in link' });
      // local menu toggle only
      const menuBtn = page.locator('button').filter({ hasText: /releases|resources|company/i }).first();
      if (await menuBtn.count()) {
        await record(page, 'nav-menu-trigger', menuBtn, ['default'], { group: 'Menu', title: 'Nav menu trigger' });
        await menuBtn.click({ timeout: 3000 }).catch(() => {});
        await page.waitForTimeout(600);
        await shot(page, `home-${theme}-menu`, false);
        await record(page, 'nav-menu', page.locator('[role="menu"], [class*="dropdown"], [class*="Dropdown"], [class*="popover"]').first(), ['default'], { group: 'Menu', title: 'Opened nav menu' });
        await page.keyboard.press('Escape');
      } else {
        readings.gaps.push('home: no Releases/Resources/Company menu button found');
      }
      await shot(page, `home-${theme}-full`, true);
    }
    if (name === 'pricing') {
      await record(page, 'pricing-ground', pick(page, 'main'), ['default'], { group: 'Foundations', title: 'Pricing ground' });
      await record(page, 'pricing-title', pick(page, 'h1'), ['default'], { group: 'Type', title: 'Pricing title' });
      await record(page, 'plan-card', page.locator('[class*="card"]').first(), ['default'], { group: 'Card', title: 'Plan card' });
      await shot(page, `pricing-${theme}-full`, true);
    }
    if (name === 'signin') {
      const email = page.locator('input[type="email"], input[name="email"], input[autocomplete="email"]').first();
      await record(page, 'signin-email', email, ['default', 'focus-visible'], { group: 'Text field', title: 'Sign-in email field' });
      // Do not type. Do not submit. Record whether other forbidden fields exist.
      const inventory = await page.evaluate(() => ({
        inputs: [...document.querySelectorAll('input, textarea, select, button')].slice(0, 40).map((el) => ({
          tag: el.tagName.toLowerCase(),
          type: el.getAttribute('type'),
          name: el.getAttribute('name'),
          autocomplete: el.getAttribute('autocomplete'),
          placeholder: el.getAttribute('placeholder'),
          text: (el.innerText || '').trim().slice(0, 60),
        })),
        text: (document.body.innerText || '').slice(0, 1200),
      }));
      readings.pages.signin.inventory = inventory;
      const forbidden = inventory.inputs.filter((i) => /tel|phone|card|password|ssn/i.test(`${i.type} ${i.name} ${i.autocomplete} ${i.placeholder}`));
      if (forbidden.length) readings.gaps.push('signin asks for more than email: ' + JSON.stringify(forbidden));
      const emailOnly = inventory.inputs.filter((i) => i.tag === 'input').every((i) => !i.type || /email|text|hidden/i.test(i.type));
      readings.pages.signin.emailOnlyForm = emailOnly && inventory.inputs.some((i) => /email/i.test(`${i.type} ${i.name} ${i.placeholder} ${i.autocomplete}`));
      readings.gaps.push('signin: email field focused for the focus ring only; nothing typed and nothing submitted. AgentMail signup not used because the form is the app sign-in, not a marketing email-only newsletter, and the rule is public marketing plus signed-out login as a boundary.');
    }
    if (name === 'contact') {
      const inputs = await page.evaluate(() => [...document.querySelectorAll('input, textarea')].map((el) => ({
        type: el.getAttribute('type'), name: el.getAttribute('name'), placeholder: el.getAttribute('placeholder'),
      })));
      readings.pages.contact.inputs = inputs;
      if (inputs.some((i) => /tel|phone/i.test(`${i.type} ${i.name} ${i.placeholder}`))) {
        readings.gaps.push('contact form asks for a phone field; not entered');
      }
    }
    await page.close();
  }
  await context.close();

  // phone width
  const mctx = await browser.newContext({
    viewport: { width: 390, height: 844 },
    deviceScaleFactor: 2,
    userAgent: UA_MOBILE,
    isMobile: true,
    hasTouch: true,
    locale: 'en-US',
  });
  const { page } = await openPage(mctx, 'https://clay.earth/');
  const m = await meta(page);
  readings.pages.mobileHome = { finalUrl: page.url(), meta: m };
  const mTheme = m.htmlBg === 'rgb(0, 0, 0)' ? 'dark' : 'light';
  await shot(page, `home-${mTheme}-mobile`, false);
  const burger = page.locator('button').filter({ hasText: /menu/i }).first();
  const anyBtn = page.locator('header button, nav button, button[aria-label*="menu" i], button[class*="toggle" i], button[class*="hamburger" i]').first();
  const opener = (await burger.count()) ? burger : anyBtn;
  if (await opener.count()) {
    await opener.click({ timeout: 3000 }).catch(() => {});
    await page.waitForTimeout(700);
    await shot(page, `home-${mTheme}-mobile-menu`, false);
    readings.pages.mobileHome.menuOpened = true;
  } else {
    readings.gaps.push('mobile: hamburger control not found by role or class');
    readings.pages.mobileHome.buttons = await page.evaluate(() => [...document.querySelectorAll('button')].slice(0, 12).map((b) => ({
      text: (b.innerText || b.getAttribute('aria-label') || '').trim().slice(0, 40),
      cls: [...b.classList].slice(0, 3).join(' '),
      box: (() => { const r = b.getBoundingClientRect(); return { x: r.x, y: r.y, w: r.width, h: r.height }; })(),
    })));
  }
  await page.close();
  await mctx.close();
  await browser.close();
}

await runDesktop();
fs.writeFileSync(path.join(RAW, 'readings.json'), JSON.stringify(readings, null, 2));
console.log('wrote', path.join(RAW, 'readings.json'));
console.log('pages', Object.keys(readings.pages));
console.log('components', Object.keys(readings.components));
console.log('gaps', readings.gaps);
