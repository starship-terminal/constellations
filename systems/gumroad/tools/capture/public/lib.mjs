// Shared helpers for the gumroad.com public captures, adapted from the shared
// capture-kit lineage used across systems/ packages. Run with PLAYWRIGHT
// pointing at a Playwright install (index.mjs) when this directory has no
// node_modules.
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
export const BASE = 'https://gumroad.com';
// Product pages and creator profiles live on per-creator subdomains
// (<creator>.gumroad.com[/l/<slug>]); the capture follows the public links the
// Discover grid serves and picks one representative product page.
export const PRODUCT_URL = 'https://ichigo.gumroad.com/l/ichigo-reader';
export const CREATOR_URL = 'https://ichigo.gumroad.com/';
// The product page's own "Subscribe" link target — gumroad.com/checkout with
// the product's opaque option key. Public: the same URL any visitor reaches.
export const CHECKOUT_URL = 'https://gumroad.com/checkout?product=rsMja&option=6Fm6gGP9cDXYcJRRo8U3pA%3D%3D&recurrence=monthly&quantity=1';

export const HERE = path.dirname(new URL(import.meta.url).pathname);
export const REF = path.resolve(HERE, '..', '..', '..'); // systems/<slug>, from tools/capture/public
export const CROPS = path.join(REF, 'components', 'crops');
export const RAW = path.join(REF, 'raw');

// gumroad.com is a Rails + Inertia (React) app styled with Tailwind v4
// utilities and a single Vite stylesheet, design-*.css, served from
// assets.gumroad.com (cross-origin — read from network responses). It
// declares a real token layer on :root: the brand set --pink/--purple/
// --green/--orange/--red/--yellow, semantic roles as RGB channel triplets
// (--accent/--primary/--color/--filled/--success/--warning/--danger/--info
// plus their --contrast-* partners), --spacer-1..8, --border-radius-1..3,
// --box-shadow-1/2 (hard offset shadows), --border-width, --font-family
// (ABC Favorit), --form-element-height, --transition-duration and z-index
// steps. The dark theme is real: a @media (prefers-color-scheme:dark) :root
// block repaints the roles (--body-bg #242423, --color/--filled swap,
// --border-alpha .35) and the markup carries dark:* Tailwind utilities —
// there is no in-page toggle, so the colour scheme emulation is the control.
// Specs select by role, aria-label or structure.
export const M = (name) => `[class*="${name}"]`;

// The per-context patches every page gets: a record of
// the real devicePixelRatio before app code runs — a page's scripts can make
// window.devicePixelRatio read 1 while the renderer still paints at the
// context's deviceScaleFactor (a 780x1688 PNG from a 390x844 viewport).
// __captureDPR keeps the launch-time value for the screenshot sidecar.
export async function patch(context) {
  await context.addInitScript(() => {
    // automation flag: left as the browser sets it (navigator.webdriver is not masked).
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
// arrived. gumroad.com serves real pages headless; a host answering a
// challenge instead is recorded as a boundary, not retried past the cap.
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

// Hide (never click) any fixed overlay that mounts over the page: a consent or
// promo layer. REMOVE-ONLY: hiding never accepts or rejects anything.
export async function closePromo(page) {
  for (let i = 0; i < 4; i++) {
    const hit = await page.evaluate(() => {
      let n = 0;
      document.querySelectorAll('[aria-label*="cookie consent" i], [aria-label="Consent Manager" i], [id*="cookie-consent" i], [id*="cookie_consent" i], [class*="cookie-banner" i], [class*="cookie_banner" i]').forEach((x) => { x.style.setProperty('display', 'none', 'important'); n++; });
      document.querySelectorAll('div[id*="onetrust" i], div[class*="onetrust" i], div[id*="termly" i], iframe[title*="privacy" i]').forEach((x) => { x.style.setProperty('display', 'none', 'important'); n++; });
      const box = [...document.querySelectorAll('div,section,aside,[role="dialog"],[role="alertdialog"]')].find((x) => {
        const t = x.innerText || '';
        const r = x.getBoundingClientRect();
        const cs = getComputedStyle(x);
        return (cs.position === 'fixed' || cs.position === 'sticky')
          && /note about our cookies|we use cookies|uses cookies, pixel tags|cookie settings|cookies settings|we value (your )?privacy|personal data \(such as identifiers|allow all cookies|consents verified by/i.test(t)
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

// gumroad.com's dark theme is painted by @media (prefers-color-scheme:dark):
// the :root dark block swaps the channel-triplet roles and the dark:*
// utilities come on. There is no in-page toggle, so the colour-scheme
// emulation is the control — the same media the product's own CSS answers.
// paintedTheme() reads the painted surface (body luminance), so a dark pass
// that never repaints can never publish a light page as dark evidence.
export async function paintedTheme(p) {
  return p.evaluate(() => {
    const lum = (bg) => {
      const m = /rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)/.exec(bg || '');
      if (!m || (m[4] !== undefined && +m[4] === 0)) return null;
      return (0.2126 * +m[1] + 0.7152 * +m[2] + 0.0722 * +m[3]) < 128;
    };
    return {
      scheme: getComputedStyle(document.documentElement).colorScheme,
      mediaDark: matchMedia('(prefers-color-scheme: dark)').matches,
      htmlDark: lum(getComputedStyle(document.documentElement).backgroundColor),
      bodyDark: lum(getComputedStyle(document.body).backgroundColor),
      mainDark: lum(getComputedStyle(document.querySelector('main,header') || document.body).backgroundColor),
    };
  }).catch(() => ({}));
}

export async function themeReached(p, want) {
  const s = await paintedTheme(p);
  const darkPainted = s.mediaDark === true && (s.bodyDark === true || s.mainDark === true || s.htmlDark === true);
  return want === 'dark' ? darkPainted : !darkPainted;
}

// Drives the theme to `want` through the colour-scheme emulation — the media
// feature the product's own stylesheets respond to (there is no in-page
// control to click). Returns whether the painted state was reached.
export async function setTheme(p, want) {
  await p.emulateMedia({ colorScheme: want }).catch(() => {});
  await p.waitForTimeout(800);
  return await themeReached(p, want);
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

// Returns whether the page was reached and any bot check cleared by itself (it is waited out,
// never solved). A caller that gets false records the page as a boundary instead of measuring it.
export async function open(page, url, { wait = 6000, promo = 'close' } = {}) {
  let reached = true;
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch((e) => {
    reached = false;
    console.log('  ! navigation failed', url, String(e.message || e).split('\n')[0]);
  });
  const cleared = reached && (await clearChallenge(page));
  await page.waitForTimeout(wait);
  if (promo === 'close') await closePromo(page);
  return cleared;
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
const STICKY = ['header[class*="fixed" i]', 'header', 'nav[class*="sticky" i]', '[class*="sticky" i] header', 'div[class*="sticky" i]:has(> nav)'].join(', ');
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
    // font request hangs; retry once, then fail without leaving a stale crop
    // from an earlier run behind.
    let lastErr;
    for (let i = 0; i < 2; i++) {
      try {
        if (inView) {
          const clip = {
            x: Math.max(0, box.x - pad),
            y: Math.max(0, box.y - pad),
            width: Math.min(vp.width - Math.max(0, box.x - pad), box.width + 2 * pad),
            height: Math.min(vp.height - Math.max(0, box.y - pad), box.height + 2 * pad),
          };
          await page.screenshot({ path: file, clip, animations: 'allow' });
        } else {
          await locator.screenshot({ path: file, animations: 'allow' });
        }
        lastErr = null;
        break;
      } catch (e) { lastErr = e; await page.waitForTimeout(900); }
    }
    if (lastErr) { try { fs.unlinkSync(file); } catch { /* none */ } throw lastErr; }
  } finally {
    if (hidden) await page.evaluate(() => document.querySelectorAll('[data-m-hidden]').forEach((n) => { n.style.removeProperty('visibility'); n.removeAttribute('data-m-hidden'); }));
  }
  quantize(file);
  return path.relative(REF, file);
}

export async function centre(locator) {
  await locator.evaluate((el) => el.scrollIntoView({ block: 'center', inline: 'nearest', behavior: 'instant' })).catch(() => {});
  await locator.page().waitForTimeout(350);
}

// 256 colours, and a crop larger than about 1.2 megapixels (a whole sidebar or
// section at 2x) is halved, so the folder stays small.
export function quantize(file) {
  execFileSync(PYTHON, [
    '-c',
    'import sys\nfrom PIL import Image\nf=sys.argv[1]\nim=Image.open(f).convert("RGB")\nif im.width*im.height>1200000: im=im.resize((im.width//2, im.height//2), Image.LANCZOS)\nim.quantize(256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).save(f, optimize=True)',
    file,
  ]);
}

export function slug(s) {
  return s.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
}
