// Collects foodnoms.com's distinct UI icons into icons/ and writes icons/INDEX.tsv.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node icons.mjs
//
// Two sources on the Framer site: inline <svg> elements (the wordmark label,
// the search magnifier, the nav-overlay close glyph) and, more importantly,
// data-URI SVGs painted through -webkit-mask-image/mask-image — the site
// renders most glyphs that way (the pricing-table checks, the values-card
// symbols, the goal-pill icons, the accordion chevrons): a div carries the
// mask and its background-color supplies the tint, which is recorded in
// INDEX.tsv. Files are named from the nearest [data-framer-name] ancestor or
// the role of the control they sit in, and deduplicated by geometry: the
// same artwork seen on several pages is one file with every sighting listed.
// The press outlet logos in the "As Featured By" strip, the App Store badge
// and the Foodnoms app icon are brand/customer artwork, not interface icons,
// and are left out. Colour is kept exactly as shipped.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { BASE, UA, UA_MOBILE, launch, clearChallenge, patch, closePromo } from './lib.mjs';

const HERE = path.dirname(new URL(import.meta.url).pathname);
const REF = path.resolve(HERE, '..', '..', '..');
const ICONS = path.join(REF, 'icons');
fs.mkdirSync(ICONS, { recursive: true });

// A mask's background-color reports as color(display-p3 …): INDEX.tsv keeps
// the sRGB hex so a reader does not have to redo the gamut map (the same
// conversion build_tokens.py applies to the declared palette).
function srgbOf(tint) {
  if (!tint || !tint.startsWith('color(display-p3')) return tint;
  const dec = (x) => (x <= 0.04045 ? x / 12.92 : Math.pow((x + 0.055) / 1.055, 2.4));
  const enc = (x) => {
    x = Math.max(0, Math.min(1, x));
    return x <= 0.0031308 ? x * 12.92 : 1.055 * Math.pow(x, 1 / 2.4) - 0.055;
  };
  const m = tint.match(/color\(display-p3 ([\d.]+) ([\d.]+) ([\d.]+)(?: \/ ([\d.]+))?\)/);
  if (!m) return tint;
  const [rl, gl, bl] = [dec(+m[1]), dec(+m[2]), dec(+m[3])];
  const ch = [
    Math.round(enc(1.224940176 * rl - 0.224703265 * gl) * 255),
    Math.round(enc(-0.042056955 * rl + 1.042586621 * gl) * 255),
    Math.round(enc(-0.019637555 * rl - 0.078636046 * gl + 1.098273614 * bl) * 255),
  ];
  const hex = '#' + ch.map((v) => v.toString(16).padStart(2, '0')).join('');
  return m[4] && +m[4] !== 1 ? `rgba(${ch.join(', ')}, ${+m[4]})` : hex;
}

const PAGES = ['/', '/plus', '/help', '/news', '/press', '/family-plan', '/vs/myfitnesspal', '/help/barcode-scanning', '/news/foodnoms-2'];

const { browser } = await launch();
const context = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US' });
await patch(context);
const page = await context.newPage();
// seen: hash -> {svg, name, vb, style, seen:Set, label:Set}
const seen = new Map();
// The press outlets' and partners' brand artwork: never the product's own
// interface icons. Tested against the icon's full ancestor data-framer-name
// chain too — the "As Featured By" strip (MacStories, iMore, 9to5Mac,
// PopSugar, Good Housekeeping, Prevention), the App Store download badge and
// the Foodnoms app icon are brand marks, left out.
const SKIP = /macstories|imore|9to5|popsugar|good housekeeping|prevention|featured in|app store|apple|app icon|logo\b/i;

// Curated names for artwork the DOM cannot name: geometry hash -> file name,
// the same mechanism the other kits keep in tools/capture/icon-names.tsv.
const NAMED = new Map();
try {
  for (const l of fs.readFileSync(new URL('../icon-names.tsv', import.meta.url), 'utf8').split('\n')) {
    const [k, n] = l.split('\t');
    if (k && n && k !== 'hash') NAMED.set(k, n);
  }
} catch { /* optional */ }

async function harvest(url, tag) {
  await page.goto(BASE + url, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
  await clearChallenge(page);
  await page.waitForTimeout(7000);
  await closePromo(page);
  const items = await page.evaluate(() => {
    // Every data-framer-name on the element's ancestor chain, innermost
    // first, so SKIP can see past anonymous "Frame" wrappers around the
    // trusted-by logo wall (Logo1…Logo9, icon--logo_large).
    const chainOf = (el) => {
      const c = [];
      for (let n = el.parentElement; n && n !== document.body; n = n.parentElement) {
        const nm = n.getAttribute && n.getAttribute('data-framer-name');
        if (nm) c.push(nm);
      }
      return c.join(' ');
    };
    const ctxOf = (el) => {
      for (let n = el; n && n !== document.body; n = n.parentElement) {
        const nm = n.getAttribute && n.getAttribute('data-framer-name');
        if (nm) return nm;
      }
      const ctl = el.closest && el.closest('a,button,[role="button"],div[aria-label]');
      return ctl ? (ctl.getAttribute('aria-label') || (ctl.innerText || '').trim().slice(0, 30)) : '';
    };
    const out = [];
    for (const s of document.querySelectorAll('svg')) {
      const r = s.getBoundingClientRect();
      if (r.width < 6 || r.height < 6) continue;
      // Framer ships artwork as <use href="#spriteId"> into a shared hidden
      // sprite: resolve the reference so the saved file carries real paths.
      let html = s.outerHTML;
      let vbAttr = s.getAttribute('viewBox') || '';
      const u = s.querySelector('use');
      if (u) {
        const ref = u.getAttribute('href') || u.getAttribute('xlink:href') || '';
        const target = ref.startsWith('#') ? document.getElementById(ref.slice(1)) : null;
        if (target) {
          const vb = s.getAttribute('viewBox') || target.getAttribute('viewBox') || (() => { const b = r; return `0 0 ${b.width | 0} ${b.height | 0}`; })();
          const inner = target.tagName === 'SYMBOL' ? target.innerHTML : target.outerHTML;
          html = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="${vb}">${inner}</svg>`;
          vbAttr = vb;
        }
      }
      if (!/<(path|rect|circle|ellipse|line|polyline|polygon|text|image|g)\b/.test(html)) continue;
      out.push({ kind: 'inline', html, vb: vbAttr, w: r.width | 0, h: r.height | 0, ctx: ctxOf(s), chain: chainOf(s), htmlCtx: (s.closest('[class*="container"], [data-framer-name], a, button') || s.parentElement).outerHTML.slice(0, 300) });
    }
    for (const el of document.querySelectorAll('div,span,i')) {
      const cs = getComputedStyle(el);
      // Framer paints most glyphs as -webkit-mask-image data-URI SVGs: the
      // div's background-color is the tint, recorded beside the artwork. The
      // computed value is a layer list ("url("..."), none"), so each
      // data-URI layer is extracted, and the CSS escaping (\" stays as "
      // inside the URL) is undone before the SVG is kept.
      const bg = cs.backgroundImage;
      const mk = cs.webkitMaskImage && cs.webkitMaskImage !== 'none' ? cs.webkitMaskImage : cs.maskImage;
      for (const [kind, prop, tint] of [['mask', mk, cs.backgroundColor], ['bg', bg, null]]) {
        if (!prop || prop === 'none') continue;
        const r = el.getBoundingClientRect();
        if (r.width < 6 || r.width > 120 || r.height < 6 || r.height > 120) break;
        for (const m of prop.matchAll(/url\("data:image\/svg\+xml,(.*?)"\)/g)) {
          let svg;
          try { svg = decodeURIComponent(m[1]).replace(/\\(["'\\/])/g, '$1'); } catch { continue; }
          if (!svg.includes('<svg')) continue;
          out.push({ kind, html: svg, vb: (svg.match(/viewBox=(\\?)"([^"\\]*)/) || [])[2] || '', w: r.width | 0, h: r.height | 0, ctx: ctxOf(el), chain: chainOf(el), tint, htmlCtx: el.outerHTML.slice(0, 300) });
          break; // the same div is one glyph even if it painted several layers
        }
      }
    }
    return out;
  });
  for (const it of items) {
    const geo = crypto.createHash('sha1').update(it.html.replace(/\s+/g, ' ')).digest('hex').slice(0, 8);
    if (SKIP.test(it.htmlCtx) || SKIP.test(it.ctx) || SKIP.test(it.chain)) continue;
    const e = seen.get(geo) || { svg: it.html, vb: it.vb, sizes: new Set(), style: it.kind, seen: new Set(), label: new Set(), tints: new Set() };
    e.sizes.add(`${it.w}x${it.h}`);
    e.seen.add(tag);
    if (it.ctx) e.label.add(it.ctx.slice(0, 50));
    if (it.tint) e.tints.add(it.tint);
    seen.set(geo, e);
  }
}

for (const u of PAGES) await harvest(u, u === '/' ? 'home' : u.replace(/^\//, '').replace(/\//g, '-'));
// the mobile hamburger and close glyphs
const mctx = await browser.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' });
await patch(mctx);
const mp = await mctx.newPage();
await mp.goto(BASE + '/', { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
await mp.waitForTimeout(7000);
await mp.locator('button[aria-label="Open navigation menu"]').first().click().catch(() => {});
await mp.waitForTimeout(1200);
for (const it of await mp.evaluate(() => [...document.querySelectorAll('svg')].map((s) => {
  const r = s.getBoundingClientRect();
  const ctl = s.closest('div[aria-label],a,button');
  const chain = (() => { const c = []; for (let n = s.parentElement; n && n !== document.body; n = n.parentElement) { const nm = n.getAttribute && n.getAttribute('data-framer-name'); if (nm) c.push(nm); } return c.join(' '); })();
  let html = s.outerHTML;
  let vbAttr = s.getAttribute('viewBox') || '';
  const u = s.querySelector('use');
  if (u) {
    const ref = u.getAttribute('href') || u.getAttribute('xlink:href') || '';
    const target = ref.startsWith('#') ? document.getElementById(ref.slice(1)) : null;
    if (target) {
      const vb = s.getAttribute('viewBox') || target.getAttribute('viewBox') || `0 0 ${r.width | 0} ${r.height | 0}`;
      const inner = target.tagName === 'SYMBOL' ? target.innerHTML : target.outerHTML;
      html = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="${vb}">${inner}</svg>`;
      vbAttr = vb;
    }
  }
  if (!/<(path|rect|circle|ellipse|line|polyline|polygon|text|image|g)\b/.test(html)) return null;
  return r.width < 6 ? null : { kind: 'inline', html, vb: vbAttr, w: r.width | 0, h: r.height | 0, ctx: (ctl && (ctl.getAttribute('aria-label') || ctl.getAttribute('data-framer-name') || '')) || '', chain, htmlCtx: (ctl || s.parentElement).outerHTML.slice(0, 300) };
}).filter(Boolean))) {
  const geo = crypto.createHash('sha1').update(it.html.replace(/\s+/g, ' ')).digest('hex').slice(0, 8);
  // The same SKIP as the desktop pass: without it this mobile sweep keeps
  // the trusted-by customer logos (a LogoN/icon--logo_large ancestor).
  if (SKIP.test(it.htmlCtx) || SKIP.test(it.ctx) || SKIP.test(it.chain)) continue;
  const e = seen.get(geo) || { svg: it.html, vb: it.vb, sizes: new Set(), style: 'inline', seen: new Set(), label: new Set(), tints: new Set() };
  e.sizes.add(`${it.w}x${it.h}`);
  e.seen.add('mobile-home');
  if (it.ctx) e.label.add(it.ctx.slice(0, 50));
  if (it.tint) e.tints.add(it.tint);
  seen.set(geo, e);
}
await browser.close();

// name files: a curated name from icon-names.tsv when one exists, else the
// framer-name context, else the control role, else the hash
const taken = new Map();
const rows = [];
const order = [...seen.entries()].sort((a, b) => (a[1].label.size ? 0 : 1) - (b[1].label.size ? 0 : 1));
for (const [geo, e] of order) {
  // A 1px-tall "icon" is a rule, not a glyph.
  if ([...e.sizes].every((sz) => parseFloat(sz.split('x')[1]) <= 2)) continue;
  const raw = NAMED.get(geo) || [...e.label][0] || '';
  let name = raw.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '') || `icon-${geo}`;
  if (name.length > 40) name = name.slice(0, 40).replace(/-$/, '');
  if (!NAMED.has(geo) && (/^(frame|section|container|component|default|defult|variant)/.test(name) || name.length < 3)) name = `icon-${geo}`;
  if (taken.has(name)) name = `${name}-${geo}`;
  taken.set(name, geo);
  const file = `${name}.svg`;
  fs.writeFileSync(path.join(ICONS, file), e.svg.includes('xmlns') ? e.svg : e.svg.replace('<svg', '<svg xmlns="http://www.w3.org/2000/svg"'));
  const src = e.style === 'bg' ? 'background data-URI' : e.style === 'mask' ? 'mask data-URI' : 'inline';
  rows.push([file, name, geo, [...e.sizes].join(', '), e.vb || '-', src, [...e.tints].map(srgbOf).join(', ') || '-', [...e.seen].sort().join(', '), [...e.label].join('; ')].map((x) => String(x).replace(/[\t\n]+/g, ' ')));
}
const header = 'file\tname\thash\trendered sizes\tviewBox\tsource\ttint\tseen on\tnext to\n';
fs.writeFileSync(path.join(ICONS, 'INDEX.tsv'), header + rows.map((r) => r.join('\t')).join('\n') + '\n');
console.log(`${rows.length} icons ->`, ICONS);
for (const r of rows) console.log(' ', r[0], '|', r[3], '|', r[6], '|', r[7]);
