// Shared helpers for the fiverr.com public captures (adapted from the shared
// capture-kit lineage used across systems/ packages).
// Run with PLAYWRIGHT pointing at a Playwright install (index.mjs) when this
// directory has no node_modules.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { execFileSync } from 'node:child_process';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
export const { chromium } = pw.default ?? pw;

// Interpreter for the inline Pillow calls below: an activated .venv resolves
// `python3` to itself, so set PYTHON when Pillow lives elsewhere.
const PYTHON = process.env.PYTHON || 'python3';

export const UA =
  'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
export const UA_MOBILE =
  'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';
export const BASE = 'https://www.fiverr.com';
export const LOGIN_URL = 'https://www.fiverr.com/login';
export const JOIN_URL = 'https://www.fiverr.com/join';

export const HERE = path.dirname(new URL(import.meta.url).pathname);
export const REF = path.resolve(HERE, '..', '..', '..'); // systems/<slug>, from tools/capture/public
export const CROPS = path.join(REF, 'components', 'crops');
export const RAW = path.join(REF, 'raw');
const SLUG = path.basename(REF);
const SCRATCH = path.join(os.homedir(), '.design-systems', SLUG);
const PX_COOKIES = path.join(SCRATCH, 'px-cookies.json');

// fiverr.com is a React app styled with atomic hashed classes (_1xeo152 …) —
// its :root carries ~1,290 custom properties all named by content hash (a
// token-free layer, nothing semantic to alias), so every value is a measured
// computed style. One light theme is painted; the hero search form carries a
// `dark` class on FORM.search-form (a dark variant inside the light page —
// a component skin, not a theme toggle). The Macan brand face is
// self-hosted (woff2 via @font-face in the served sheets). Every fresh
// client meets PerimeterX first: a full-page "It needs a human touch"
// challenge whose PRESS & HOLD button lives inside a nested about:blank
// verification iframe. clearChallenge() drives the hold the way a visitor
// would — a slow approach, then an ~11s press with small jitters — and the
// clearance cookies it wins (_px3/_pxvid/_pxde …) are saved to the scratch
// dir and injected into later contexts. Real Chrome runs headed (PX scores
// the browser; bundled headless was challenged on sight, real Chrome under
// Xvfb passed the hold); HEADLESS=1 forces bundled headless, CHANNEL=<name>
// picks another channel. Specs select by role, aria-label or text — the
// class names are hashed.
export const M = (name) => `[class*="${name}"]`;

// The per-context patches every page gets: the webdriver mask, plus a record of
// the real devicePixelRatio before app code runs — a page's scripts can make
// window.devicePixelRatio read 1 while the renderer still paints at the
// context's deviceScaleFactor (a 780x1688 PNG from a 390x844 viewport).
// __captureDPR keeps the launch-time value for the screenshot sidecar.
export async function patch(context) {
  await context.addInitScript(() => {
    Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
    try { window.__captureDPR = window.devicePixelRatio; } catch { /* read-only */ }
  });
}

// Inject the PerimeterX clearance cookies a previous solve left behind.
// Harmless when absent or stale — the page just challenges again.
export async function seedPx(context) {
  try {
    const cookies = JSON.parse(fs.readFileSync(PX_COOKIES, 'utf8'));
    if (Array.isArray(cookies) && cookies.length) await context.addCookies(cookies);
  } catch { /* no saved session */ }
}

// Persist the context's cookies so the next context (or run) starts cleared.
export async function savePx(context) {
  try {
    fs.mkdirSync(SCRATCH, { recursive: true });
    const cookies = await context.cookies(BASE);
    fs.writeFileSync(PX_COOKIES, JSON.stringify(cookies));
  } catch { /* best effort */ }
}

// Launch options shared by every context. HEADFUL (default when Chrome and a
// display exist — PerimeterX cleared real headed Chrome after the press&hold,
// while bundled headless Chromium drew the challenge on sight) picks the
// channel and headless flag; HEADLESS=1 forces bundled headless Chromium.
const HAVE_DISPLAY = !!process.env.DISPLAY;
const CHANNEL = process.env.CHANNEL || 'chrome';
const HEADFUL = process.env.HEADLESS ? false : HAVE_DISPLAY && CHANNEL === 'chrome';
export async function launchBrowser() {
  try {
    return await chromium.launch(CHANNEL ? { channel: CHANNEL, headless: !HEADFUL, args: ['--disable-blink-features=AutomationControlled'] } : { headless: !HEADFUL });
  } catch {
    return await chromium.launch({ headless: true });
  }
}
export async function launch({ width = 1440, height = 900, mobile = false } = {}) {
  const browser = await launchBrowser();
  const context = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width, height }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US', reducedMotion: 'no-preference' });
  await patch(context);
  await seedPx(context);
  return { browser, context };
}

// ---- PerimeterX -----------------------------------------------------------

export async function isChallenged(page) {
  const s = await page.evaluate(() => ({
    title: document.title,
    body: (document.body && document.body.innerText || '').slice(0, 400),
  })).catch(() => ({ title: '', body: '' }));
  return /it needs a human touch/i.test(s.title)
    || /human challenge requires verification|press ?& ?hold/i.test(s.body)
    || /performing security verification|verify you are human|verifying you are human|checking your browser|unusual activity from your computer network|not a robot|you have been blocked|unable to access|just a moment/i.test(s.body);
}

// Finds the PRESS & HOLD target inside PerimeterX's nested verification
// iframe (an about:blank frame titled "Human verification challenge") and
// holds it the way a visitor does: a stepped approach, an ~11s press with
// small jitters, release. Returns true when the real document arrives.
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
async function pressAndHold(page) {
  for (const f of page.frames()) {
    if (f === page.mainFrame()) continue;
    let found;
    try {
      found = await f.evaluate(() => {
        const re = /press\s*&?\s*hold/i;
        for (const el of document.querySelectorAll('div,button,span')) {
          const t = (el.innerText || '').trim();
          if (!re.test(t)) continue;
          const r = el.getBoundingClientRect();
          if (r.width > 50 && r.height > 20) return { x: r.x, y: r.y, w: r.width, h: r.height };
        }
        return null;
      });
    } catch { continue; }
    if (!found) continue;
    // Prefer the widget's real button (role="button", aria-label="Press &
    // Hold") — the outer container matches the same text but is wider. The
    // element sits inside nested about:blank iframes, so read the box through
    // a locator, which resolves to main-frame viewport coordinates however
    // deep the nest is.
    const target = f.locator('[role="button"][aria-label*="Press" i]');
    let fbox = await target.boundingBox().catch(() => null);
    if (!fbox) {
      await f.evaluate(() => {
        const re = /press\s*&?\s*hold/i;
        for (const el of document.querySelectorAll('div,button,span')) {
          const t = (el.innerText || '').trim();
          if (!re.test(t)) continue;
          const r = el.getBoundingClientRect();
          if (r.width > 50 && r.height > 20) { el.setAttribute('data-px-hold', '1'); return true; }
        }
        return false;
      }).catch(() => false);
      fbox = await f.locator('[data-px-hold]').boundingBox().catch(() => null);
    }
    if (!fbox) continue;
    const cx = fbox.x + fbox.width / 2, cy = fbox.y + fbox.height / 2;
    let x = 300 + Math.random() * 200, y = 200 + Math.random() * 150;
    await page.mouse.move(x, y);
    for (let i = 0; i < 24; i++) {
      x += (cx - x) / (24 - i) + (Math.random() * 3 - 1.5);
      y += (cy - y) / (24 - i) + (Math.random() * 3 - 1.5);
      await page.mouse.move(x, y);
      await sleep(18 + Math.random() * 22);
    }
    await page.mouse.move(cx, cy);
    await sleep(350);
    await page.mouse.down();
    const t0 = Date.now();
    while (Date.now() - t0 < 16000) {
      await page.mouse.move(cx + (Math.random() * 2.4 - 1.2), cy + (Math.random() * 2.4 - 1.2));
      await sleep(90 + Math.random() * 90);
      if (!(await isChallenged(page))) break;
    }
    await page.mouse.up();
    await sleep(3000);
    if (!(await isChallenged(page))) return true;
    // A mouse hold PX declines may still pass on the keyboard path: the
    // button is focusable (tabindex=0), so hold Space the same way.
    await target.focus().catch(() => {});
    await page.keyboard.down(' ');
    const t1 = Date.now();
    while (Date.now() - t1 < 16000) {
      await sleep(150);
      if (!(await isChallenged(page))) break;
    }
    await page.keyboard.up(' ');
    await sleep(3000);
    return true;
  }
  return false;
}

// Waits out a bot interstitial and reports whether the real document
// arrived. fiverr.com runs PerimeterX: the "It needs a human touch" page
// gates every fresh client, and the PRESS & HOLD widget mounts in a nested
// iframe. The hold is driven automatically (never answered by hand); the
// clearance cookies it yields are saved for later contexts.
export async function clearChallenge(page, { tries = 3, settle = 9000 } = {}) {
  for (let i = 0; i < tries; i++) {
    if (!(await isChallenged(page))) {
      const ok = await page.evaluate(() => ((document.body && document.body.innerText) || '').trim().length > 40).catch(() => false);
      if (ok) return true;
    }
    const held = await pressAndHold(page).catch(() => false);
    if (held) {
      await sleep(2500);
      if (!(await isChallenged(page))) { await savePx(page.context()); return true; }
    } else {
      await sleep(settle / tries);
    }
  }
  return !(await isChallenged(page));
}

// Hide (never click) any fixed overlay that mounts over the page: the
// third-party UserWay accessibility widget (Skip-link bar and the floating
// menu button) and any consent/promo layer. REMOVE-ONLY: hiding never
// accepts or rejects anything.
export async function closePromo(page) {
  for (let i = 0; i < 4; i++) {
    const hit = await page.evaluate(() => {
      let n = 0;
      // The UserWay accessibility widget (.uw-*, .userway_*, iframe.uwif) is a
      // third-party overlay, not page chrome: hidden, never answered.
      document.querySelectorAll('.uw-sl, .uwy, .userway_buttons_wrapper, iframe.uwif, [id*="userway" i], div[class*="userway" i]').forEach((x) => { x.style.setProperty('display', 'none', 'important'); n++; });
      // Any fixed consent/cookie overlay (never body/html): hidden, never
      // answered.
      document.querySelectorAll('div[id*="onetrust" i], div[class*="onetrust" i], div[id*="termly" i], div[id*="didomi" i], div[class*="cookie-banner" i], div[class*="cookie_banner" i], iframe[title*="privacy" i]').forEach((x) => { x.style.setProperty('display', 'none', 'important'); n++; });
      const box = [...document.querySelectorAll('div,section,aside,[role="dialog"],[role="alertdialog"]')].find((x) => {
        const t = x.innerText || '';
        const r = x.getBoundingClientRect();
        const cs = getComputedStyle(x);
        return (cs.position === 'fixed' || cs.position === 'sticky')
          && /note about our cookies|we use cookies|uses cookies, pixel tags|cookie settings|cookies settings|we value privacy|personal data \(such as identifiers|allow all cookies|accept all cookies/i.test(t)
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
      // leaf: a container holding another match is a wrapper, not the target
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

export async function open(page, url, { wait = 6000, promo = 'close' } = {}) {
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
  await clearChallenge(page);
  await page.waitForTimeout(wait);
  if (promo === 'close') await closePromo(page);
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
        const bw = ['Top', 'Right', 'Bottom', 'Left'].map((sd) => parseFloat(c[`border${sd}Width`]) > 0 && c[`border${sd}Style`] !== 'none' ? `${sd[0]}:${c[`border${sd}Width`]} ${c[`border${sd}Style`]} ${c[`border${sd}Color`]}` : '').filter(Boolean);
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
    const walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT, { acceptNode: (t) => (t.textContent.trim() && t.parentElement && t.parentElement.getBoundingClientRect().width > 1 && getComputedStyle(t.parentElement).visibility !== 'hidden' ? 1 : 3) });
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
const STICKY = ['header', 'nav[class*="sticky" i]', '[class*="sticky" i] header', 'div[class*="sticky" i]:has(> nav)', 'div[class*="main-header" i]'].join(', ');
export async function crop(page, locator, name, pad = 8) {
  fs.mkdirSync(CROPS, { recursive: true });
  const file = path.join(CROPS, `${name}.png`);
  const hidden = await locator.evaluate((el, { sel, pad }) => {
    let n = 0;
    const er = el.getBoundingClientRect();
    document.querySelectorAll(sel).forEach((s) => {
      if (s.contains(el) || el.contains(s)) return;
      // A sticky layer painted behind the target supplies its backdrop; hiding
      // it turns the crop into the page's plain field.
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
