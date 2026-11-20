// One-shot public capture for synthesia.io. Measures computed styles and
// screenshots of signed-out marketing pages. Never follows login, signup,
// demo booking, or checkout.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs \
//     node tools/capture/harvest.mjs
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;

const HERE = path.dirname(fileURLToPath(import.meta.url));
const PKG = path.resolve(HERE, '..', '..');
const RAW = path.join(PKG, 'raw');
const SHOTS = path.join(PKG, 'screenshots');
const CROPS = path.join(PKG, 'components', 'crops');
fs.mkdirSync(RAW, { recursive: true });
fs.mkdirSync(SHOTS, { recursive: true });
fs.mkdirSync(CROPS, { recursive: true });

const UA =
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';

const PAGES = [
  ['home', 'https://www.synthesia.io/'],
  ['pricing', 'https://www.synthesia.io/pricing'],
  ['enterprise', 'https://www.synthesia.io/enterprise'],
  ['video', 'https://www.synthesia.io/video'],
  ['book-demo', 'https://www.synthesia.io/book-a-demo'],
  ['blog', 'https://www.synthesia.io/blog'],
  ['features-avatars', 'https://www.synthesia.io/features/avatars'],
  ['missing', 'https://www.synthesia.io/this-page-does-not-exist-capture'],
];

const HARVEST = () => {
  const root = getComputedStyle(document.documentElement);
  const declared = {};
  const walk = (rules, ctx) => {
    if (!rules) return;
    for (const rule of rules) {
      if (rule.cssRules) {
        const media = rule.media ? rule.media.mediaText : '';
        walk(rule.cssRules, media ? ctx.concat(media) : ctx);
        continue;
      }
      if (!rule.style) continue;
      const props = {};
      for (let i = 0; i < rule.style.length; i++) {
        const p = rule.style[i];
        if (p.startsWith('--')) props[p] = rule.style.getPropertyValue(p).trim();
      }
      if (!Object.keys(props).length) continue;
      const key = (rule.selectorText || '') + ' @ ' + ctx.join(' | ');
      declared[key] = { selector: rule.selectorText || '', context: ctx, properties: props };
    }
  };
  const sheets = [];
  for (const sheet of document.styleSheets) {
    let rules = null;
    let blocked = false;
    try { rules = sheet.cssRules; } catch (e) { blocked = true; }
    sheets.push({ href: sheet.href, rules: rules ? rules.length : 0, blocked });
    if (rules) walk(rules, []);
  }
  const resolved = {};
  const names = new Set();
  for (const block of Object.values(declared)) {
    for (const n of Object.keys(block.properties)) names.add(n);
  }
  for (const n of names) {
    const v = root.getPropertyValue(n).trim();
    if (v) resolved[n] = v;
  }
  const fonts = [];
  for (const sheet of document.styleSheets) {
    let rules;
    try { rules = sheet.cssRules; } catch (e) { continue; }
    const walkFonts = (rules) => {
      if (!rules) return;
      for (const rule of rules) {
        if (rule.cssRules) walkFonts(rule.cssRules);
        if (rule.type === CSSRule.FONT_FACE_RULE) {
          fonts.push({
            family: rule.style.getPropertyValue('font-family'),
            weight: rule.style.getPropertyValue('font-weight'),
            style: rule.style.getPropertyValue('font-style'),
            display: rule.style.getPropertyValue('font-display'),
            src: (rule.style.getPropertyValue('src') || '').replace(/url\([^)]+\)/g, 'url(…)'),
          });
        }
      }
    };
    walkFonts(rules);
  }
  return {
    url: location.href,
    title: document.title,
    innerWidth: innerWidth,
    innerHeight: innerHeight,
    dpr: devicePixelRatio,
    colorScheme: root.colorScheme,
    declared,
    resolved,
    fonts,
    sheets,
    reducedMotion: matchMedia('(prefers-reduced-motion: reduce)').matches,
  };
};

const MEASURE = () => {
  const pick = (el) => {
    if (!el) return null;
    const s = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    if (r.width < 2 || r.height < 2) return null;
    return {
      tag: el.tagName.toLowerCase(),
      text: (el.innerText || el.getAttribute('aria-label') || '').trim().replace(/\s+/g, ' ').slice(0, 90),
      cls: String(el.className || '').slice(0, 140),
      href: el.href || null,
      rect: { x: +r.x.toFixed(1), y: +r.y.toFixed(1), w: +r.width.toFixed(1), h: +r.height.toFixed(1) },
      bg: s.backgroundColor,
      color: s.color,
      font: s.fontFamily,
      size: s.fontSize,
      weight: s.fontWeight,
      lh: s.lineHeight,
      ls: s.letterSpacing,
      radius: s.borderRadius,
      border: `${s.borderTopWidth} ${s.borderTopStyle} ${s.borderTopColor}`,
      pad: s.padding,
      shadow: s.boxShadow,
      gap: s.gap,
      display: s.display,
      transition: `${s.transitionProperty} ${s.transitionDuration} ${s.transitionTimingFunction}`,
    };
  };
  const all = (sel) => [...document.querySelectorAll(sel)];
  const firstVisible = (list) => list.map(pick).find(Boolean) || null;
  const byText = (sel, re) => firstVisible(all(sel).filter((el) => re.test((el.innerText || '').trim())));
  const h1 = firstVisible(all('h1'));
  const nav = firstVisible(all('nav, header'));
  const primary = byText('a.button, a.button.is-small', /^Get started/);
  const secondary = byText('a.button-secondary', /^(Book demo|Get started)/);
  const tertiary = byText('a.button-tertiary-new, a.button-tertiary', /.+/);
  const login = byText('a', /^Log in$/);
  const footer = firstVisible(all('footer'));
  const inputs = all('input, textarea, select').slice(0, 12).map((el) => {
    const s = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    return {
      tag: el.tagName.toLowerCase(),
      type: el.type || null,
      name: el.name || null,
      placeholder: el.placeholder || null,
      required: el.required,
      rect: { w: +r.width.toFixed(1), h: +r.height.toFixed(1) },
      bg: s.backgroundColor,
      color: s.color,
      border: `${s.borderTopWidth} ${s.borderTopStyle} ${s.borderTopColor}`,
      radius: s.borderRadius,
      pad: s.padding,
      size: s.fontSize,
      font: s.fontFamily,
      shadow: s.boxShadow,
    };
  });
  const cards = all('[class*="card"], [class*="pricing"]').slice(0, 6).map(pick).filter(Boolean);
  const body = getComputedStyle(document.body);
  return {
    url: location.href,
    title: document.title,
    h1,
    nav,
    primary,
    secondary,
    tertiary,
    login,
    footer: footer && { bg: footer.bg, color: footer.color, h: footer.rect.h },
    inputs,
    cards,
    body: { bg: body.backgroundColor, color: body.color, font: body.fontFamily, size: body.fontSize },
    cookieText: ([...document.querySelectorAll('button, a')].find((el) => /accept|cookie|consent/i.test(el.innerText || '')) || {}).innerText || null,
  };
};

// Consent: hide the banner, never choose. The committed readings were taken after an earlier
// version of this script clicked "Accept all" (README); this one only hides fixed layers that carry
// cookie or consent copy.
async function dismissCookies(page) {
  const hidden = await page.evaluate(() => {
    let n = 0;
    for (const el of document.querySelectorAll('body *')) {
      const st = getComputedStyle(el);
      if ((st.position === 'fixed' || st.position === 'sticky') && /cookie|consent/i.test(el.innerText || '') && (el.innerText || '').length < 2000) {
        el.style.setProperty('display', 'none', 'important');
        n++;
      }
    }
    return n;
  }).catch(() => 0);
  if (hidden) await page.waitForTimeout(300);
  return hidden ? `hidden ${hidden}` : null;
}

function writePngMeta(file, extra) {
  const meta = {
    screenshot: path.basename(file),
    requested: extra.requested,
    actual: extra.actual,
    capture: { mode: extra.fullPage ? 'fullPage' : 'viewport', scale: 'device' },
    note: extra.note || 'headless Chromium; preview browser returned no screenshot frames',
  };
  fs.writeFileSync(file + '.capture.json', JSON.stringify(meta, null, 2));
}

const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({
  viewport: { width: 1440, height: 900 },
  deviceScaleFactor: 1,
  userAgent: UA,
  locale: 'en-US',
});
const page = await context.newPage();

const harvests = {};
const measures = {};
const log = [];

for (const [name, url] of PAGES) {
  try {
    const res = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
    await page.waitForTimeout(2500);
    const status = res ? res.status() : null;
    const finalUrl = page.url();
    const challenge = await page.evaluate(() => /just a moment|cf-challenge|cloudflare/i.test(document.title + document.body.innerText.slice(0, 300)));
    if (challenge) {
      log.push({ name, url, status, challenge: true, skipped: true });
      continue;
    }
    const cookie = await dismissCookies(page);
    const harvest = await page.evaluate(HARVEST);
    const measure = await page.evaluate(MEASURE);
    harvest.status = status;
    harvest.finalUrl = finalUrl;
    harvest.cookieDismissed = cookie;
    harvests[name] = harvest;
    measures[name] = measure;
    const shot = path.join(SHOTS, `${name}-light-default.png`);
    const actual = await page.evaluate(() => ({
      innerWidth: innerWidth,
      innerHeight: innerHeight,
      dpr: devicePixelRatio,
      vv: visualViewport ? { w: visualViewport.width, h: visualViewport.height, scale: visualViewport.scale } : null,
    }));
    await page.screenshot({ path: shot, fullPage: false });
    writePngMeta(shot, {
      requested: { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1 },
      actual,
      fullPage: false,
    });
    log.push({ name, status, finalUrl, title: harvest.title, vars: Object.keys(harvest.resolved).length, cookie });
    console.log('ok', name, status, finalUrl);
  } catch (e) {
    log.push({ name, url, error: String(e).split('\n')[0] });
    console.log('fail', name, String(e).split('\n')[0]);
  }
}

// Login wall: load only, do not type, do not submit.
{
  const url = 'https://app.synthesia.io/welcome';
  try {
    const res = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 45000 });
    await page.waitForTimeout(3000);
    const info = await page.evaluate(() => ({
      url: location.href,
      title: document.title,
      text: (document.body.innerText || '').replace(/\s+/g, ' ').slice(0, 800),
      inputs: [...document.querySelectorAll('input, button, a')].slice(0, 30).map((el) => ({
        tag: el.tagName.toLowerCase(),
        type: el.type || null,
        text: (el.innerText || el.getAttribute('aria-label') || el.placeholder || '').trim().slice(0, 60),
        name: el.name || null,
      })),
      challenge: /just a moment|cf-challenge|cloudflare/i.test(document.title),
    }));
    info.status = res ? res.status() : null;
    // probe.mjs owns raw/login-wall.json (one writer per raw file); this pass keeps its own copy.
    fs.writeFileSync(path.join(RAW, 'harvest-login-wall.json'), JSON.stringify(info, null, 2));
    if (!info.challenge) {
      const shot = path.join(SHOTS, 'login-light-signed-out.png');
      await page.screenshot({ path: shot, fullPage: false });
      const actual = await page.evaluate(() => ({ innerWidth, innerHeight, dpr: devicePixelRatio }));
      writePngMeta(shot, { requested: { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1 }, actual, fullPage: false, note: 'signed-out login wall, nothing typed or submitted' });
    }
    log.push({ name: 'login', status: info.status, finalUrl: info.url, challenge: info.challenge, title: info.title });
    console.log('login', info.status, info.url, info.challenge);
  } catch (e) {
    log.push({ name: 'login', error: String(e).split('\n')[0] });
    console.log('login fail', String(e).split('\n')[0]);
  }
}

// Mobile home only.
{
  const mob = await browser.newContext({
    viewport: { width: 390, height: 844 },
    deviceScaleFactor: 2,
    userAgent: 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1',
    isMobile: true,
    hasTouch: true,
    locale: 'en-US',
  });
  const mp = await mob.newPage();
  try {
    await mp.goto('https://www.synthesia.io/', { waitUntil: 'domcontentloaded', timeout: 60000 });
    await mp.waitForTimeout(2500);
    await dismissCookies(mp);
    const shot = path.join(SHOTS, 'home-light-mobile.png');
    const actual = await mp.evaluate(() => ({ innerWidth, innerHeight, dpr: devicePixelRatio }));
    await mp.screenshot({ path: shot, fullPage: false });
    writePngMeta(shot, { requested: { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2 }, actual, fullPage: false });
    const nav = await mp.evaluate(() => {
      const burger = [...document.querySelectorAll('button, a, div')].find((el) => /menu|hamburger/i.test((el.className || '') + (el.getAttribute('aria-label') || '')));
      return burger ? { tag: burger.tagName, cls: String(burger.className).slice(0, 80), aria: burger.getAttribute('aria-label') } : null;
    });
    log.push({ name: 'mobile-home', actual, nav });
    console.log('mobile', JSON.stringify(actual), JSON.stringify(nav));
  } catch (e) {
    log.push({ name: 'mobile-home', error: String(e).split('\n')[0] });
  }
  await mob.close();
}

// Merge resolved vars: home is the source of truth, others fill gaps.
const merged = { ...(harvests.home?.resolved || {}) };
const extra = {};
for (const [name, h] of Object.entries(harvests)) {
  for (const [k, v] of Object.entries(h.resolved || {})) {
    if (!(k in merged)) extra[k] = { value: v, page: name };
    else if (merged[k] !== v) extra[k + '@' + name] = { value: v, home: merged[k] };
  }
}

// probe.mjs owns raw/css-vars.json, which build_tokens.py reads; this pass writes its own file so a
// rerun cannot replace the committed readings with a different shape.
fs.writeFileSync(path.join(RAW, 'harvest-css-vars.json'), JSON.stringify({
  source: 'computed custom properties on https://www.synthesia.io/ at 1440x900, headless Chromium, 2026-11-19',
  sheets: harvests.home?.sheets || [],
  fonts: harvests.home?.fonts || [],
  declaredCount: Object.keys(harvests.home?.declared || {}).length,
  resolved: merged,
  pageDeltas: extra,
  viewport: { innerWidth: harvests.home?.innerWidth, innerHeight: harvests.home?.innerHeight, dpr: harvests.home?.dpr },
}, null, 2));
fs.writeFileSync(path.join(RAW, 'measurements.json'), JSON.stringify(measures, null, 2));
fs.writeFileSync(path.join(RAW, 'capture-log.json'), JSON.stringify(log, null, 2));

await browser.close();
console.log('wrote', Object.keys(harvests).length, 'pages');
