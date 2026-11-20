// Shared helpers for the joinhandshake.com public captures (adapted from the
// shared capture-kit lineage used across systems/ packages; this copy is the
// immediate ancestor). Run with PLAYWRIGHT pointing at a Playwright install
// (index.mjs) when this directory has no node_modules.
import fs from 'node:fs';
import path from 'node:path';
import { execFileSync } from 'node:child_process';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
export const { chromium } = pw.default ?? pw;

// Interpreter for the inline Pillow calls below: an activated .venv resolves
// `python3` to itself, so set PYTHON when Pillow lives elsewhere.
const PYTHON = process.env.PYTHON || 'python3';

export const UA =
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
export const UA_MOBILE =
  'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';
export const BASE = 'https://joinhandshake.com';
// The signed-out consumer surface: app.joinhandshake.com/login redirects to
// /access, the "Log in or sign up" page the Rails consumer app (the Rosetta
// design system) serves. It sits behind a Cloudflare managed challenge that
// intermittently lets a plain headless load through — every app-surface
// reader retries fresh contexts and treats a challenge that never clears as
// a recorded boundary, never something to solve.
//   app.joinhandshake.com/access    the login/signup page (captured when it loads)
//   app.joinhandshake.com/explore   Cloudflare challenge, never cleared (blocked)
//   app.joinhandshake.com/signup -> /student_account_registrations/new
//                                 Cloudflare challenge, never cleared (blocked)
//   support.joinhandshake.com       Cloudflare challenge, never cleared (blocked)
export const APP_BASE = 'https://app.joinhandshake.com';
export const APP_URL = APP_BASE + '/access';

export const HERE = path.dirname(new URL(import.meta.url).pathname);
export const REF = path.resolve(HERE, '..', '..', '..'); // systems/<slug>, from tools/capture/public
export const CROPS = path.join(REF, 'components', 'crops');
export const RAW = path.join(REF, 'raw');

// joinhandshake.com is the marketing site: one Next.js app whose CSS arrives
// as route-scoped /_next/static/css/*.css chunks (Tailwind v4 utilities over a
// thin declared layer — the --font-noi-grotesk/--font-sans-plomb* faces, the
// --spacing unit, --container-3xs..7xl, --leading-xs..xl, --tracking-sm/-lg,
// --font-weight-*, --ease-*, --animate-*, --blur-*, --drop-shadow-*,
// --breakpoint-lg, plus the nav/hero geometry vars like --desktop-nav-height
// and --notification-banner-height). Colour is authored mostly as literal
// hexes inside utilities and product vars (--lime-30/-50, --cta(-hover|
// -active|-visited), --link-hover-color, --nav-background-color). No theme
// control exists: colorScheme reads "normal", no dark class or media query —
// the site paints light only.
// app.joinhandshake.com is the consumer app: the "Log in or sign up" page at
// /access ships the Rosetta design system's own sheets from
// handshake-production-cdn.joinhandshake.com (a --rosetta-bg-*/--rosetta-fg-*/
// --rosetta-interactive-*/--rosetta-shadow-*/--rosetta-type-*/--rosetta-
// spacing-*/--rosetta-font-family-* layer plus component vars like
// --button-* and --nav-top-nav-*), light only.
// Specs select by role, aria-label or structure.
export const M = (name) => `[class*="${name}"]`;

// The per-context patches every page gets: the webdriver mask, plus a record of
// the real devicePixelRatio before app code runs — a page's scripts can make
// window.devicePixelRatio read 1 while the renderer still paints at the
// context's deviceScaleFactor (a 780x1688 PNG from a 390x844 viewport).
// __captureDPR keeps the launch-time value for the screenshot sidecar.
export async function patch(context) {
  await context.addInitScript(() => {
    // no navigator.webdriver mask: removed in the 2026-11 audit (D7), not run since
    try { window.__captureDPR = window.devicePixelRatio; } catch { /* read-only */ }
  });
}

export async function launch({ width = 1440, height = 900, mobile = false } = {}) {
  const browser = await chromium.launch();
  const context = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width, height }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US', reducedMotion: 'no-preference' });
  await patch(context);
  return { browser, context };
}

// Waits out any bot interstitial and reports whether the real document
// arrived. joinhandshake.com serves real pages headless; app.joinhandshake.com
// and support.joinhandshake.com sit behind a Cloudflare managed challenge that
// passes only intermittently — a challenge that never clears is a boundary.
export async function clearChallenge(page, { tries = 12, step = 2000 } = {}) {
  for (let i = 0; i < tries; i++) {
    const s = await page.evaluate(() => ({
      title: document.title,
      body: (document.body && document.body.innerText || '').slice(0, 400),
    })).catch(() => ({ title: '', body: '' }));
    const challenging = /just a moment|attention required/i.test(s.title)
      || /performing security verification|verify you are human|verifying you are human|checking your browser|unusual activity from your computer network|press ?& ?hold|not a robot|you have been blocked|unable to access/i.test(s.body);
    if (!challenging && s.body.length > 40) return true;
    await page.waitForTimeout(step);
  }
  return false;
}

// Hide (never click) any fixed overlay that mounts over the page: the Ketch
// consent banner, a promo layer. REMOVE-ONLY: hiding never accepts or rejects
// anything.
export async function closePromo(page) {
  for (let i = 0; i < 4; i++) {
    const hit = await page.evaluate(() => {
      let n = 0;
      document.querySelectorAll('[aria-label*="cookie consent" i], [aria-label="Consent Manager" i], [id*="cookie-consent" i], [id*="cookie_consent" i], [class*="cookie-banner" i], [class*="cookie_banner" i]').forEach((x) => { x.style.setProperty('display', 'none', 'important'); n++; });
      document.querySelectorAll('div[id*="onetrust" i], div[class*="onetrust" i], div[id*="termly" i], iframe[title*="privacy" i]').forEach((x) => { x.style.setProperty('display', 'none', 'important'); n++; });
      // Ketch (joinhandshake.com's consent manager): the fixed banner and any
      // modal it mounts. Hidden, never pressed — Accept/Reject would set a
      // real consent choice.
      document.querySelectorAll('[id*="ketch" i], [class*="ketch" i], iframe[src*="ketch" i], #lanyard_root').forEach((x) => {
        const r = x.getBoundingClientRect();
        if (r.width > 0) { x.style.setProperty('display', 'none', 'important'); n++; }
      });
      const box = [...document.querySelectorAll('div,section,aside,[role="dialog"],[role="alertdialog"]')].find((x) => {
        const t = x.innerText || '';
        const r = x.getBoundingClientRect();
        const cs = getComputedStyle(x);
        return (cs.position === 'fixed' || cs.position === 'sticky')
          && /note about our cookies|we use cookies|uses cookies, pixel tags|cookie settings|cookies settings|we value (your )?privacy|personal data \(such as identifiers|allow all cookies|consents verified by|your privacy choices/i.test(t)
          && t.length < 1600 && r.width > 200 && r.width < 1400 && r.height > 60 && +cs.zIndex > 5;
      });
      if (box) { box.style.setProperty('display', 'none', 'important'); n++; }
      if (document.body) document.body.style.removeProperty('overflow');
      document.documentElement && document.documentElement.style.removeProperty('overflow');
      return n;
    }).catch(() => 0);
    if (!hit) { await page.waitForTimeout(600); continue; }
    await page.waitForTimeout(600);
  }
  return true;
}

// The site paints light only: there is no theme control (no dark class, no
// theme button, no prefers-color-scheme rule in any sheet) — so nothing here
// switches themes. paintedTheme is kept for the evidence record.
export async function paintedTheme(p) {
  return p.evaluate(() => {
    const lum = (bg) => {
      const m = /rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)/.exec(bg || '');
      if (!m || (m[4] !== undefined && +m[4] === 0)) return null;
      return (0.2126 * +m[1] + 0.7152 * +m[2] + 0.0722 * +m[3]) < 128;
    };
    return {
      dark: document.documentElement.classList.contains('dark'),
      light: document.documentElement.classList.contains('light'),
      scheme: getComputedStyle(document.documentElement).colorScheme,
      htmlDark: lum(getComputedStyle(document.documentElement).backgroundColor),
      bodyDark: lum(getComputedStyle(document.body).backgroundColor),
      stored: (() => { try { return localStorage.getItem('theme'); } catch { return null; } })(),
    };
  }).catch(() => ({}));
}

// Finds a visible element in-page whose trimmed innerText matches reText,
// tags it with data-m-mark="<tag>" and returns a locator for it. up optionally
// retargets an ancestor (closest()). Use where getByRole/hasText miss nodes
// whose text lives in nested spans.
export async function domFind(page, reText, { sel = 'button, a', tag = 'm', up = null, nth = 0, leaf = true, minW = 0, minH = 0 } = {}) {
  const ok = await page.evaluate(
    ([src, flags, s, t, upSel, i, leafOnly, w, h]) => {
      const re = new RegExp(src, flags);
      document.querySelectorAll(`[data-m-mark="${t}"]`).forEach((n) => n.removeAttribute('data-m-mark'));
      const els = [...document.querySelectorAll(s)].filter((n) => {
        const r = n.getBoundingClientRect();
        const cs = getComputedStyle(n);
        return r.width >= w && r.height >= h && r.width > 0 && r.height > 0 && cs.visibility !== 'hidden' && cs.opacity !== '0' && re.test((n.innerText || '').trim());
      });
      const pool = leafOnly ? els.filter((n) => !els.some((o) => o !== n && n.contains(o))) : els;
      const el = pool[i] || els[i];
      if (!el) return false;
      (upSel ? el.closest(upSel) || el : el).setAttribute('data-m-mark', t);
      return true;
    },
    [reText.source, reText.flags, sel, tag, up, nth, leaf, minW, minH],
  );
  return ok ? page.locator(`[data-m-mark="${tag}"]`) : page.locator('[data-m-mark="__none__"]');
}

export async function open(page, url, { wait = 6000, promo = 'close', tries = 1 } = {}) {
  for (let i = 0; i < tries; i++) {
    await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    if (await clearChallenge(page, { tries: 4, step: 2000 })) break;
    if (i === tries - 1) return false;
  }
  await page.waitForTimeout(wait);
  if (promo === 'close') await closePromo(page);
  return true;
}

// Computed style properties recorded for every component and state.
export const PROPS = [
  'display', 'position', 'boxSizing', 'width', 'height', 'minWidth', 'maxWidth', 'minHeight',
  'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft',
  'marginTop', 'marginRight', 'marginBottom', 'marginLeft',
  'gap', 'rowGap', 'columnGap', 'flexDirection', 'alignItems', 'justifyContent',
  'gridTemplateColumns',
  'borderTopWidth', 'borderTopStyle', 'borderTopColor',
  'borderRightWidth', 'borderRightStyle', 'borderRightColor',
  'borderBottomWidth', 'borderBottomStyle', 'borderBottomColor',
  'borderLeftWidth', 'borderLeftStyle', 'borderLeftColor',
  'borderTopLeftRadius', 'borderTopRightRadius', 'borderBottomRightRadius', 'borderBottomLeftRadius',
  'backgroundColor', 'backgroundImage', 'boxShadow', 'backdropFilter',
  'outlineWidth', 'outlineStyle', 'outlineColor', 'outlineOffset',
  'fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'letterSpacing', 'textTransform',
  'color', 'textDecorationLine', 'textDecorationColor', 'textDecorationThickness', 'textUnderlineOffset',
  'transitionProperty', 'transitionDuration', 'transitionTimingFunction', 'transitionDelay',
  'cursor', 'opacity', 'transform', 'overflow', 'zIndex', 'top',
];

// Reads the computed style of the element, its ::before/::after if they paint
// anything, the rect, the painted layers in its subtree, a focus ring or fill
// painted by an ancestor, the first text node's type, and the first svg icon.
export async function styleOf(locator) {
  return locator.evaluate((el, props) => {
    const cls = (n) => [...n.classList].map((c) => String(c)).filter((c) => c && !/^x[0-9a-z]{5,8}$/.test(c));
    // A url() in a computed value (a background photo, a cursor) can be a signed URL: recorded as
    // url(…), only data: and #fragment references kept.
    const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\(\s*(?!['"]?(?:data:|#))(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|[^)]*)\s*\)/g, 'url(…)') : v);
    const pick = (cs) => {
      const o = {};
      for (const p of props) o[p] = noUrl(cs[p]);
      return o;
    };
    const cs = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    const out = {
      tag: el.tagName.toLowerCase(),
      classes: cls(el).slice(0, 4).join(' '),
      text: (el.innerText || el.getAttribute('aria-label') || el.getAttribute('placeholder') || '').trim().replace(/\s+/g, ' ').slice(0, 80),
      rect: { x: +r.x.toFixed(1), y: +r.y.toFixed(1), w: +r.width.toFixed(2), h: +r.height.toFixed(2) },
      style: pick(cs),
    };
    for (const pe of ['::before', '::after']) {
      const p = getComputedStyle(el, pe);
      if (p.content && p.content !== 'none' && p.content !== 'normal') {
        out[pe] = {
          content: noUrl(p.content).slice(0, 40), width: p.width, height: p.height, position: p.position,
          backgroundColor: p.backgroundColor, backgroundImage: noUrl(p.backgroundImage).slice(0, 200), boxShadow: p.boxShadow,
          borderTopWidth: p.borderTopWidth, borderTopStyle: p.borderTopStyle, borderTopColor: p.borderTopColor,
          borderRadius: p.borderRadius, inset: `${p.top} ${p.right} ${p.bottom} ${p.left}`, opacity: p.opacity, transition: p.transition,
        };
      }
    }
    const paint = [];
    const nodes = [el, ...el.querySelectorAll('*')].slice(0, 400);
    for (const n of nodes) {
      if (paint.length >= 14) break;
      if (n.closest('svg') && n.tagName.toLowerCase() !== 'svg') continue;
      for (const pe of [null, '::before', '::after']) {
        const c = getComputedStyle(n, pe);
        if (pe && (c.content === 'none' || c.content === 'normal')) continue;
        const bw = ['Top', 'Right', 'Bottom', 'Left'].map((sd) => parseFloat(c[`border${sd}Width`]) > 0 && c[`border${sd}Style`] !== 'none' ? `${sd[0]}:${c[`border${sd}Width`]} ${c[`border${sd}Style`]}` : '').filter(Boolean);
        const bg = c.backgroundColor !== 'rgba(0, 0, 0, 0)' ? c.backgroundColor : '';
        const bgi = c.backgroundImage !== 'none' && !/^url\("?https?:/.test(c.backgroundImage) ? noUrl(c.backgroundImage).replace(/url\("data:[^)]{60,}\)/g, 'url(data:…)').slice(0, 200) : '';
        const sh = c.boxShadow !== 'none' ? c.boxShadow : '';
        const ol = c.outlineStyle !== 'none' && parseFloat(c.outlineWidth) > 0 ? `${c.outlineWidth} ${c.outlineStyle} ${c.outlineColor} offset ${c.outlineOffset}` : '';
        if (!(bw.length || bg || bgi || sh || ol)) continue;
        if (n.tagName === 'IMG' && !bw.length && !sh) continue;
        const rr = n.getBoundingClientRect();
        paint.push({
          node: n.tagName.toLowerCase() + (pe || '') + cls(n).slice(0, 2).map((x) => '.' + x).join(''),
          size: pe ? `${c.width}x${c.height}` : `${rr.width.toFixed(1)}x${rr.height.toFixed(1)}`,
          border: bw.join(' | ') || undefined, bg: bg || undefined, bgImage: bgi || undefined, shadow: sh || undefined, outline: ol || undefined,
          radius: c.borderRadius !== '0px' ? c.borderRadius : undefined,
        });
      }
    }
    if (paint.length) out.paint = paint;
    const anc = [];
    for (let n = el.parentElement, i = 0; n && i < 3; n = n.parentElement, i++) {
      const c = getComputedStyle(n);
      const fill = i < 1 && c.backgroundColor !== 'rgba(0, 0, 0, 0)';
      if (fill || c.boxShadow !== 'none' || (c.outlineStyle !== 'none' && parseFloat(c.outlineWidth) > 0 && c.outlineColor !== 'rgba(0, 0, 0, 0)')) {
        anc.push({ up: i + 1, node: n.tagName.toLowerCase() + cls(n).slice(0, 2).map((x) => '.' + x).join(''), shadow: c.boxShadow !== 'none' ? c.boxShadow : undefined, outline: c.outlineStyle !== 'none' ? `${c.outlineWidth} ${c.outlineStyle} ${c.outlineColor}` : undefined, radius: c.borderRadius, bg: c.backgroundColor });
      }
    }
    if (anc.length) out.ancestors = anc;
    const walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT, { acceptNode: (t) => (t.textContent.trim() && t.parentElement && t.parentElement.getBoundingClientRect().width > 1 && getComputedStyle(t.parentElement).visibility !== 'hidden' && getComputedStyle(t.parentElement).opacity !== '0' ? 1 : 3) });
    const tn = walker.nextNode();
    if (tn && tn.parentElement !== el) {
      const t = tn.parentElement;
      const tc = getComputedStyle(t);
      out.textStyle = { node: t.tagName.toLowerCase() + cls(t).slice(0, 2).map((x) => '.' + x).join(''), text: tn.textContent.trim().slice(0, 40), fontFamily: tc.fontFamily, fontSize: tc.fontSize, lineHeight: tc.lineHeight, fontWeight: tc.fontWeight, letterSpacing: tc.letterSpacing, color: tc.color, textDecorationLine: tc.textDecorationLine, textTransform: tc.textTransform };
    }
    if (el.tagName === 'INPUT' || el.tagName === 'TEXTAREA') {
      const ph = getComputedStyle(el, '::placeholder');
      out.placeholder = { color: ph.color, opacity: ph.opacity, fontSize: ph.fontSize };
    }
    const svg = el.tagName.toLowerCase() === 'svg' ? el : el.querySelector('svg');
    if (svg) {
      const sr = svg.getBoundingClientRect();
      const scs = getComputedStyle(svg);
      out.icon = { w: +sr.width.toFixed(2), h: +sr.height.toFixed(2), fill: scs.fill, stroke: scs.stroke, color: scs.color };
    }
    return out;
  }, PROPS);
}

// Element screenshot into components/crops/<name>.png, padded so a focus ring
// or shadow is not clipped, then quantized to 256 colours. Sticky bars that do
// not hold the element are hidden for the shot.
const STICKY = ['header[class*="fixed" i]', 'header', 'nav[class*="sticky" i]', '[class*="sticky" i] header', 'div[class*="sticky" i]:has(> nav)', 'nav[class*="fixed" i]'].join(', ');
export async function crop(page, locator, name, pad = 8) {
  fs.mkdirSync(CROPS, { recursive: true });
  const file = path.join(CROPS, `${name}.png`);
  const hidden = await locator.evaluate((el, { sel, pad }) => {
    let n = 0;
    const er = el.getBoundingClientRect();
    document.querySelectorAll(sel).forEach((s) => {
      if (s.contains(el) || el.contains(s)) return;
      const sr = s.getBoundingClientRect();
      const overlap = !(sr.right < er.left - pad || sr.left > er.right + pad || sr.bottom < er.top - pad || sr.top > er.bottom + pad);
      if (overlap) return;
      s.setAttribute('data-m-hidden', '1');
      s.style.setProperty('visibility', 'hidden', 'important');
      n++;
    });
    return n;
  }, { sel: STICKY, pad });
  try {
    const box = await locator.boundingBox();
    if (!box) throw new Error(`no box for ${name}`);
    const vp = page.viewportSize();
    const inView = box.y - pad >= 0 && box.y + box.height + pad <= vp.height && box.x >= 0 && box.x + box.width <= vp.width + 1;
    // A screenshot can stall waiting for document.fonts.ready while a lazy
    // font still streams: race it so the crop is not lost to a slow webfont.
    const shot = page.screenshot({ path: file, clip: { x: Math.max(0, box.x - pad), y: Math.max(0, box.y - pad), width: box.width + pad * 2, height: box.height + pad * 2 }, timeout: 15000 });
    await Promise.race([shot, page.waitForTimeout(17000)]);
    if (!inView) console.log('  ! crop', name, 'near viewport edge — check it');
  } finally {
    await page.evaluate(() => { document.querySelectorAll('[data-m-hidden]').forEach((s) => { s.style.removeProperty('visibility'); s.removeAttribute('data-m-hidden'); }); }).catch(() => {});
  }
  // sRGB 256 colours, in place: the crop stays a small indexed PNG.
  try {
    execFileSync(PYTHON, ['-c', `from PIL import Image
im = Image.open(${JSON.stringify(file)}).convert('RGB')
im = im.quantize(colors=256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE)
im.save(${JSON.stringify(file)}, optimize=True)`]);
  } catch (e) { console.log('  ! crop quantize failed for', name); }
  // The package-relative path the caller records on the state's `crop` field.
  return `components/crops/${name}.png`;
}

// The centre of a locator, scrolled into view — used before a real hover so
// the pointer lands inside the element.
export async function centre(locator) {
  await locator.evaluate((el) => el.scrollIntoView({ block: 'center', inline: 'center' })).catch(() => {});
  await locator.page().waitForTimeout(300);
}
