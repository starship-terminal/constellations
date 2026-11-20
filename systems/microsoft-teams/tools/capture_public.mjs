// Capture Microsoft Teams public marketing pages. No sign-in. Stops if Cloudflare
// or a login wall replaces the marketing page.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node tools/capture_public.mjs
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
const PKG = path.resolve(here, '..');
const RAW = path.join(PKG, 'raw');
const SHOTS = path.join(PKG, 'screenshots');
const CROPS = path.join(PKG, 'components', 'crops');
const ICONS = path.join(PKG, 'icons');
fs.mkdirSync(RAW, { recursive: true });
fs.mkdirSync(SHOTS, { recursive: true });
fs.mkdirSync(CROPS, { recursive: true });
fs.mkdirSync(ICONS, { recursive: true });

// The kit pattern: PLAYWRIGHT names the module, else the installed package (no machine-specific path).
const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;

const HOME = 'https://www.microsoft.com/en-us/microsoft-teams/';
const PAGES = [
  { name: 'home', url: HOME },
  { name: 'pricing', url: 'https://www.microsoft.com/en-us/microsoft-teams/compare-microsoft-teams-options?activetab=pivot:primaryr1' },
  { name: 'download', url: 'https://www.microsoft.com/en-us/microsoft-teams/download-app' },
  { name: 'free', url: 'https://www.microsoft.com/en-us/microsoft-teams/teams-free' },
];

function blocked(info) {
  const blob = (info.title + ' ' + info.body).slice(0, 800);
  return /just a moment|cf-browser-verification|challenge-platform|Attention Required|Checking your browser/i.test(blob);
}

async function meta(page) {
  return page.evaluate(() => ({
    href: location.href,
    title: document.title,
    body: (document.body.innerText || '').slice(0, 500),
    innerWidth, innerHeight, devicePixelRatio,
    vv: visualViewport ? { width: visualViewport.width, height: visualViewport.height, scale: visualViewport.scale } : null,
    colorScheme: getComputedStyle(document.documentElement).colorScheme,
    scrollHeight: document.documentElement.scrollHeight,
  }));
}

function styleOf(el) {
  if (!el) return null;
  const s = getComputedStyle(el);
  const r = el.getBoundingClientRect();
  const pick = (k) => s[k];
  return {
    text: (el.innerText || el.getAttribute('aria-label') || '').trim().replace(/\s+/g, ' ').slice(0, 90),
    tag: el.tagName,
    cls: (el.className || '').toString().slice(0, 140),
    box: { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) },
    backgroundColor: pick('backgroundColor'),
    color: pick('color'),
    fontFamily: pick('fontFamily'),
    fontSize: pick('fontSize'),
    fontWeight: pick('fontWeight'),
    lineHeight: pick('lineHeight'),
    letterSpacing: pick('letterSpacing'),
    borderRadius: pick('borderRadius'),
    padding: pick('padding'),
    borderTop: `${pick('borderTopWidth')} ${pick('borderTopStyle')} ${pick('borderTopColor')}`,
    borderBottom: `${pick('borderBottomWidth')} ${pick('borderBottomStyle')} ${pick('borderBottomColor')}`,
    boxShadow: pick('boxShadow'),
    outline: pick('outline'),
    textDecoration: pick('textDecorationLine'),
    gap: pick('gap'),
    display: pick('display'),
    height: pick('height'),
    minHeight: pick('minHeight'),
  };
}

async function readVars(page) {
  return page.evaluate(() => {
    const root = getComputedStyle(document.documentElement);
    const names = new Set();
    const fonts = [];
    const motion = [];
    const walk = (list) => {
      if (!list) return;
      for (const r of list) {
        if (r.type === CSSRule.FONT_FACE_RULE) {
          fonts.push({
            family: r.style.getPropertyValue('font-family'),
            weight: r.style.getPropertyValue('font-weight'),
            style: r.style.getPropertyValue('font-style'),
            src: (r.style.getPropertyValue('src') || '').slice(0, 80),
          });
          continue;
        }
        if (r.cssRules && !r.style) { walk(r.cssRules); continue; }
        if (!r.style) continue;
        for (let i = 0; i < r.style.length; i++) {
          const p = r.style[i];
          if (p.startsWith('--')) names.add(p);
        }
        const anim = r.style.getPropertyValue('animation') || r.style.getPropertyValue('transition');
        if (anim && motion.length < 40) {
          motion.push({ selector: (r.selectorText || '').slice(0, 120), value: anim.slice(0, 160) });
        }
      }
    };
    const sheets = [];
    for (const sheet of document.styleSheets) {
      let rules;
      try { rules = sheet.cssRules; } catch (e) { sheets.push({ href: sheet.href, blocked: true }); continue; }
      sheets.push({ href: sheet.href, rules: rules ? rules.length : 0 });
      walk(rules);
    }
    const prefixes = [
      '--ds-app-color-', '--ds-app-space-', '--ds-app-type-', '--ds-app-radius',
      '--ds-app-border', '--ds-app-elevation', '--ds-app-shadow', '--ds-app-font',
      '--ds-app-motion', '--ds-app-duration', '--ds-app-ease', '--mwf-',
    ];
    const interesting = [...names].filter((n) => prefixes.some((p) => n.startsWith(p))).sort();
    const resolved = {};
    for (const n of interesting) resolved[n] = root.getPropertyValue(n).trim();
    return {
      varCount: names.size,
      interestingCount: interesting.length,
      resolved,
      fontFaces: fonts.slice(0, 40),
      motionSample: motion,
      sheets,
    };
  });
}

async function components(page) {
  return page.evaluate(() => {
    function one(el) {
      if (!el) return null;
      const s = getComputedStyle(el);
      const r = el.getBoundingClientRect();
      if (r.width < 8 || r.height < 8) return null;
      return {
        text: (el.innerText || el.getAttribute('aria-label') || '').trim().replace(/\s+/g, ' ').slice(0, 90),
        tag: el.tagName,
        cls: (el.className || '').toString().slice(0, 160),
        box: { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) },
        backgroundColor: s.backgroundColor,
        color: s.color,
        fontFamily: s.fontFamily,
        fontSize: s.fontSize,
        fontWeight: s.fontWeight,
        lineHeight: s.lineHeight,
        letterSpacing: s.letterSpacing,
        borderRadius: s.borderRadius,
        padding: s.padding,
        border: `${s.borderTopWidth} ${s.borderTopStyle} ${s.borderTopColor}`,
        boxShadow: s.boxShadow,
        outline: s.outline,
        textDecoration: s.textDecorationLine,
        height: s.height,
      };
    }
    const byText = (re, tag = 'a,button') => [...document.querySelectorAll(tag)].find((el) => {
      const t = (el.innerText || '').trim();
      return re.test(t) && el.getBoundingClientRect().width > 20 && el.getBoundingClientRect().height > 16;
    });
    const h1 = document.querySelector('h1');
    const header = document.querySelector('header.uhf-header, header');
    const banner = document.querySelector('.chatgpt-banner, [class*=announcement], [class*=promo-banner]');
    const field = document.querySelector('input[type=search], input[type=text], input[type=email], textarea');
    const card = document.querySelector('[class*=card], [class*=pricing]');
    const link = [...document.querySelectorAll('a.link, a')].find((a) => /learn more/i.test(a.innerText || '') && a.getBoundingClientRect().width > 40);
    const navLink = document.querySelector('header a, .uhf-menu a, nav a');
    const footer = document.querySelector('footer');
    return {
      h1: one(h1),
      h2: one(document.querySelector('h2')),
      body: one(document.body),
      header: one(header),
      navLink: one(navLink),
      primary: one(byText(/^(Download now|Try for free|Get started free|Sign up)/i)),
      secondary: one(byText(/^(Download Teams|Sign in|See plans)/i)),
      link: one(link),
      field: one(field),
      card: one(card),
      banner: one(banner),
      footer: one(footer),
      buttons: [...document.querySelectorAll('a.btn, button.btn, a[class*=btn]')].slice(0, 8).map(one).filter(Boolean),
      headings: [...document.querySelectorAll('h2')].slice(0, 12).map((h) => (h.innerText || '').trim().slice(0, 90)),
    };
  });
}

async function hoverAndFocus(page, label) {
  const loc = page.locator('a.btn, a[class*=btn]').filter({ hasText: label }).first();
  if (!(await loc.count())) return {};
  const rest = await loc.evaluate((el) => {
    const s = getComputedStyle(el);
    return { backgroundColor: s.backgroundColor, color: s.color, borderRadius: s.borderRadius, boxShadow: s.boxShadow, outline: s.outline };
  });
  await loc.hover();
  await page.waitForTimeout(250);
  const hover = await loc.evaluate((el) => {
    const s = getComputedStyle(el);
    return { backgroundColor: s.backgroundColor, color: s.color, boxShadow: s.boxShadow, outline: s.outline, textDecoration: s.textDecorationLine };
  });
  await loc.focus();
  await page.waitForTimeout(150);
  const focus = await loc.evaluate((el) => {
    const s = getComputedStyle(el);
    return { backgroundColor: s.backgroundColor, outline: s.outline, outlineOffset: s.outlineOffset, boxShadow: s.boxShadow };
  });
  return { rest, hover, focus };
}

async function icons(page) {
  return page.evaluate(() => {
    const svgs = [...document.querySelectorAll('svg')].slice(0, 40);
    return svgs.map((svg, i) => {
      const r = svg.getBoundingClientRect();
      const label = svg.getAttribute('aria-label') || svg.closest('a,button')?.getAttribute('aria-label') || svg.closest('a')?.innerText || '';
      return {
        i,
        label: (label || '').trim().replace(/\s+/g, ' ').slice(0, 40),
        w: Math.round(r.width),
        h: Math.round(r.height),
        html: svg.outerHTML,
      };
      // A size check applies to <use> icons too, and an icon too long to keep is skipped, never cut into invalid SVG.
    }).filter((s) => s.w >= 12 && s.w <= 48 && (s.html.includes('<path') || s.html.includes('<use')) && s.html.length <= 4000);
  });
}

const browser = await chromium.launch({ headless: true });
const captured = {};

async function shoot(context, prefix, pageName, url, extra) {
  const page = await context.newPage();
  const resp = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(3500);
  const info = await meta(page);
  if (blocked(info)) {
    console.error('CLOUDFLARE', url);
    await browser.close();
    process.exit(3);
  }
  const loginWall = /sign in to your account|work or school account|enter your email/i.test(info.body) && !/Microsoft Teams/i.test(info.title + info.body.slice(0, 200));
  console.log(prefix, pageName, resp && resp.status(), info.href, 'loginWall=' + loginWall);
  const file = path.join(SHOTS, `${prefix}${pageName}-light-default.png`);
  await page.screenshot({ path: file });
  const sidecar = {
    capturedAt: new Date().toISOString(),
    sanitizedSourceUrl: url.split('?')[0],
    requested: { viewport: page.viewportSize(), deviceScaleFactor: prefix ? 2 : 1 },
    actual: { innerWidth: info.innerWidth, innerHeight: info.innerHeight, devicePixelRatio: info.devicePixelRatio, visualViewport: info.vv, colorScheme: info.colorScheme, documentHeight: info.scrollHeight },
    title: info.title,
    finalHost: new URL(info.href).host + new URL(info.href).pathname,
  };
  fs.writeFileSync(file + '.capture.json', JSON.stringify(sidecar, null, 2) + '\n');
  // Whole page, bounded at eight viewports (AGENTS.md "Bound every full-page capture").
  const full = path.join(SHOTS, `${prefix}${pageName}-light-full.png`);
  const vp = page.viewportSize();
  const docH = await page.evaluate(() => document.documentElement.scrollHeight);
  const capH = Math.min(docH, vp.height * 8);
  await page.screenshot({ path: full, clip: { x: 0, y: 0, width: vp.width, height: capH }, fullPage: true });
  // A capped shot is recorded as a boundary: its sidecar and the page's readings say how tall the
  // document was and how much was kept, so the image is never read as the whole page.
  const fullPage = { documentHeight: docH, capturedHeight: capH, truncated: capH < docH };
  fs.writeFileSync(full + '.capture.json', JSON.stringify({ ...sidecar, fullPage }, null, 2) + '\n');
  if (fullPage.truncated) console.warn(`  ${prefix}${pageName}: full-page shot capped at ${capH}px of ${docH}px (8 viewports)`);
  extra = { ...(extra || {}), fullPage };
  const comp = await components(page);
  let states = {};
  if (pageName === 'home' && !prefix) states = await hoverAndFocus(page, /Download now/);
  let svg = [];
  if (pageName === 'home' && !prefix) svg = await icons(page);
  await page.close();
  return { info, comp, states, svg, extra };
}

const desk = await browser.newContext({
  viewport: { width: 1440, height: 900 },
  deviceScaleFactor: 1,
  locale: 'en-US',
  userAgent: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
});
const phone = await browser.newContext({
  viewport: { width: 390, height: 844 },
  deviceScaleFactor: 2,
  isMobile: true,
  hasTouch: true,
  locale: 'en-US',
  userAgent: 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1',
});

const readings = { capturedAt: new Date().toISOString(), pages: {}, mobile: {} };
for (const spec of PAGES) {
  readings.pages[spec.name] = await shoot(desk, '', spec.name, spec.url);
  console.log('  desktop', spec.name, 'h1', readings.pages[spec.name].comp.h1 && readings.pages[spec.name].comp.h1.text);
}
readings.mobile.home = await shoot(phone, 'mobile-', 'home', HOME);
readings.vars = await (async () => {
  const page = await desk.newPage();
  await page.goto(HOME, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(3000);
  const v = await readVars(page);
  await page.close();
  return v;
})();

// crops of the home controls
{
  const page = await desk.newPage();
  await page.goto(HOME, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(2500);
  const close = page.locator('button[aria-label="Close"], button[aria-label*="Dismiss"], .uhf-promo button').first();
  // leave the ignite banner; it is product chrome
  async function crop(name, locator) {
    const loc = typeof locator === 'string' ? page.locator(locator).first() : locator;
    if (!(await loc.count())) { console.log('  no crop', name); return; }
    try {
      await loc.scrollIntoViewIfNeeded();
      await page.waitForTimeout(200);
      await loc.screenshot({ path: path.join(CROPS, name) });
      console.log('  crop', name);
    } catch (e) {
      console.log('  crop fail', name, e.message.split('\n')[0]);
    }
  }
  await crop('button-primary-default.png', page.locator('a.btn').filter({ hasText: 'Download now' }).first());
  await page.locator('a.btn').filter({ hasText: 'Download now' }).first().hover().catch(() => {});
  await page.waitForTimeout(200);
  await crop('button-primary-hover.png', page.locator('a.btn').filter({ hasText: 'Download now' }).first());
  await page.locator('a.btn').filter({ hasText: 'Download now' }).first().focus().catch(() => {});
  await page.waitForTimeout(150);
  await crop('button-primary-focus.png', page.locator('a.btn').filter({ hasText: 'Download now' }).first());
  await crop('button-secondary-default.png', page.locator('a').filter({ hasText: 'Download Teams' }).first());
  await crop('button-signin-default.png', page.locator('header a').filter({ hasText: 'Sign in' }).first());
  await crop('button-try-default.png', page.locator('header a, a.btn').filter({ hasText: 'Try for free' }).first());
  await crop('link-default.png', page.locator('a.link').filter({ hasText: 'Learn more' }).first());
  await crop('heading-hero.png', page.locator('h1').first());
  await crop('header-default.png', page.locator('header').first());
  const field = page.locator('input').first();
  if (await field.count()) {
    await crop('field-default.png', field);
    await field.focus().catch(() => {});
    await page.waitForTimeout(150);
    await crop('field-focus.png', field);
  }
  await page.close();
}

// icons
const svgList = readings.pages.home.svg || [];
const index = ['file\trole\tw\th'];
let n = 0;
for (const svg of svgList) {
  if (n >= 16) break;
  const safe = (svg.label || 'mark-' + svg.i).toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '').slice(0, 32) || ('mark-' + svg.i);
  const file = `${safe}-${n}.svg`;
  fs.writeFileSync(path.join(ICONS, file), svg.html.includes('xmlns') ? svg.html : svg.html.replace('<svg', '<svg xmlns="http://www.w3.org/2000/svg"'));
  index.push(`${file}\t${svg.label || 'unlabeled'}\t${svg.w}\t${svg.h}`);
  n++;
}
fs.writeFileSync(path.join(ICONS, 'INDEX.tsv'), index.join('\n') + '\n');

// drop bulky svg html from readings
if (readings.pages.home.svg) readings.pages.home.svg = readings.pages.home.svg.map(({ html, ...rest }) => rest);

fs.writeFileSync(path.join(RAW, 'readings.json'), JSON.stringify(readings, null, 2));
console.log('vars', readings.vars.interestingCount, 'of', readings.vars.varCount);
console.log('wrote', RAW);
await browser.close();
