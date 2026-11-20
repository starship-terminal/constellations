// Second measurement pass: the controls the first pass selected too loosely,
// plus motion, footer, and the sign-in field. Nothing is submitted.
import fs from 'node:fs';
import path from 'node:path';
import { mergeReadings } from './merge-readings.mjs';
const pw = await import(process.env.PLAYWRIGHT || 'playwright');  // PLAYWRIGHT=/path/to/playwright/index.mjs
const { chromium } = pw.default ?? pw;

const ROOT = path.resolve(path.dirname(new URL(import.meta.url).pathname), '../..');
const RAW = path.join(ROOT, 'raw');
const CROPS = path.join(ROOT, 'components', 'crops');
const SHOTS = path.join(ROOT, 'screenshots');
fs.mkdirSync(CROPS, { recursive: true });

const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';

async function styleOf(locator) {
  return locator.evaluate((el) => {
    const props = ['color','backgroundColor','fontFamily','fontSize','fontWeight','lineHeight','letterSpacing','paddingTop','paddingRight','paddingBottom','paddingLeft','borderTopWidth','borderTopStyle','borderTopColor','borderTopLeftRadius','boxShadow','outlineWidth','outlineStyle','outlineColor','outlineOffset','width','height','textDecorationLine','textTransform','opacity','transitionProperty','transitionDuration','transitionTimingFunction'];
    const noUrl = (v) => typeof v === 'string' ? v.replace(/url\(\s*(?!['"]?(?:data:|#))(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|[^)]*)\s*\)/g, 'url(…)') : v;
    const pick = (cs) => Object.fromEntries(props.map((p) => [p, noUrl(cs[p])]));
    const cs = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    const out = {
      tag: el.tagName.toLowerCase(),
      classes: [...el.classList].slice(0, 6).join(' '),
      text: (el.innerText || el.getAttribute('placeholder') || el.getAttribute('aria-label') || '').trim().replace(/\s+/g, ' ').slice(0, 100),
      rect: { x: +r.x.toFixed(1), y: +r.y.toFixed(1), w: +r.width.toFixed(1), h: +r.height.toFixed(1) },
      style: pick(cs),
    };
    for (const pe of ['::before', '::after']) {
      const p = getComputedStyle(el, pe);
      if (p.content && p.content !== 'none') {
        out[pe] = { content: String(p.content).slice(0, 40), backgroundColor: p.backgroundColor, backgroundImage: noUrl(p.backgroundImage).slice(0, 300), boxShadow: p.boxShadow, borderRadius: p.borderRadius, width: p.width, height: p.height };
      }
    }
    if (el.tagName === 'INPUT') {
      const ph = getComputedStyle(el, '::placeholder');
      out.placeholder = { color: ph.color, fontSize: ph.fontSize, fontFamily: ph.fontFamily.split(',')[0] };
    }
    return out;
  });
}

async function crop(page, loc, name) {
  const box = await loc.boundingBox();
  if (!box) return null;
  const vp = page.viewportSize();
  const pad = 8;
  const clip = {
    x: Math.max(0, box.x - pad),
    y: Math.max(0, box.y - pad),
    width: Math.min(vp.width - Math.max(0, box.x - pad), box.width + pad * 2),
    height: Math.min(vp.height - Math.max(0, box.y - pad), box.height + pad * 2),
  };
  await page.screenshot({ path: path.join(CROPS, name + '.png'), clip, animations: 'disabled' });
  return name + '.png';
}

const out = { components: {}, motion: {}, notes: [] };
const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US' });
const page = await context.newPage();
// One missing selector or a throw must not lose the whole pass: whatever was read is written.
try {

  await page.goto('https://clay.earth/', { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(3000);

  // Real hero CTA: the painted inner of the main CTA, not the header "Get started" link.
  const hero = page.locator('[class*="mainCTA"] [class*="ctaInner"], [class*="mainCTA"]').first();
  if (await hero.count()) {
    out.components['hero-cta'] = { default: await styleOf(hero), crop: await crop(page, hero, 'hero-cta-default') };
    await hero.hover().catch(() => {});
    await page.waitForTimeout(300);
    out.components['hero-cta'].hover = await styleOf(hero);
    await crop(page, hero, 'hero-cta-hover');
  } else out.notes.push('hero CTA selector missed');

  const bottom = page.locator('[class*="ctaButton"]').first();
  if (await bottom.count()) {
    await bottom.scrollIntoViewIfNeeded();
    await page.waitForTimeout(400);
    out.components['bottom-cta'] = { default: await styleOf(bottom), crop: await crop(page, bottom, 'bottom-cta-default') };
  }

  const logo = page.locator('header a, nav a, a[href="/"]').first();
  out.components.logo = { default: await styleOf(logo) };

  const footer = page.locator('footer').first();
  if (await footer.count()) {
    await footer.scrollIntoViewIfNeeded();
    out.components.footer = { default: await styleOf(footer), crop: await crop(page, footer, 'footer-default') };
    const link = footer.locator('a').first();
    if (await link.count()) out.components['footer-link'] = { default: await styleOf(link) };
  }

  // Filter pill
  const pill = page.locator('[class*="filterButton"]').first();
  if (await pill.count()) {
    await pill.scrollIntoViewIfNeeded();
    out.components['filter-pill'] = { default: await styleOf(pill), crop: await crop(page, pill, 'filter-pill-default') };
    await pill.hover().catch(() => {});
    await page.waitForTimeout(250);
    out.components['filter-pill'].hover = await styleOf(pill);
  }

  // Nav pill container
  const nav = page.locator('[class$="_nav"], [class*="_nav"]').first();
  if (await nav.count()) {
    await page.evaluate(() => scrollTo(0, 0));
    out.components['nav-pill'] = { default: await styleOf(nav), crop: await crop(page, nav, 'nav-pill-default') };
  }

  // Motion sample: computed transitions on a few controls, plus reduced-motion media.
  out.motion.home = await page.evaluate(() => {
    const sample = (sel) => {
      const el = document.querySelector(sel);
      if (!el) return null;
      const cs = getComputedStyle(el);
      return { sel, transition: cs.transition, animation: cs.animationName + ' ' + cs.animationDuration, scroll: getComputedStyle(document.documentElement).scrollBehavior };
    };
    const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
    return {
      reduce,
      samples: [
        sample('[class*="mainCTA"]'),
        sample('[class*="signInBtn"]'),
        sample('a[href="/pricing"]'),
        sample('[class*="filterButton"]'),
      ].filter(Boolean),
    };
  });

  await page.emulateMedia({ reducedMotion: 'reduce' });
  await page.waitForTimeout(200);
  out.motion.homeReduced = await page.evaluate(() => ({
    reduce: matchMedia('(prefers-reduced-motion: reduce)').matches,
    htmlScroll: getComputedStyle(document.documentElement).scrollBehavior,
    cta: (() => { const el = document.querySelector('[class*="mainCTA"]'); if (!el) return null; const cs = getComputedStyle(el); return { transition: cs.transition, animation: cs.animationName + ' ' + cs.animationDuration }; })(),
  }));

  // Pricing extras
  await page.goto('https://me.sh/pricing', { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(2500);
  const popular = page.locator('[class*="popular"]').first();
  if (await popular.count()) {
    await popular.scrollIntoViewIfNeeded();
    out.components['plan-popular'] = { default: await styleOf(popular), crop: await crop(page, popular, 'plan-popular-default') };
  }
  const planBtn = page.locator('[class*="_card"] [class*="button"]').first();
  if (await planBtn.count()) {
    await planBtn.scrollIntoViewIfNeeded();
    out.components['plan-cta'] = { default: await styleOf(planBtn), crop: await crop(page, planBtn, 'plan-cta-default') };
    await planBtn.hover().catch(() => {});
    await page.waitForTimeout(250);
    out.components['plan-cta'].hover = await styleOf(planBtn);
    await crop(page, planBtn, 'plan-cta-hover');
  }
  const toggle = page.locator('[class*="toggle"]').filter({ hasText: /month|annual/i }).first();
  if (await toggle.count()) {
    out.components['billing-toggle'] = { default: await styleOf(toggle), crop: await crop(page, toggle, 'billing-toggle-default') };
  }
  const price = page.locator('[class*="planPrice"], [class*="price"]').first();
  if (await price.count()) out.components['plan-price'] = { default: await styleOf(price) };

  // Sign-in field. Focus only. Do not type. Do not click Sign in with email / Apple / Google / SSO.
  const sign = await context.newPage();
  await sign.goto('https://app.me.sh/login?signin', { waitUntil: 'domcontentloaded', timeout: 60000 });
  await sign.waitForTimeout(2500);
  const email = sign.locator('input[placeholder="Enter your email"]').first();
  if (await email.count()) {
    out.components['signin-email'] = { default: await styleOf(email), crop: await crop(sign, email, 'signin-email-default') };
    await email.focus();
    await sign.waitForTimeout(200);
    out.components['signin-email'].focus = await styleOf(email);
    await crop(sign, email, 'signin-email-focus');
  } else out.notes.push('email placeholder not found');
  const emailBtn = sign.getByRole('button', { name: /sign in with email/i });
  if (await emailBtn.count()) {
    out.components['signin-email-btn'] = { default: await styleOf(emailBtn), crop: await crop(sign, emailBtn, 'signin-email-btn-default') };
    await emailBtn.hover().catch(() => {});
    await sign.waitForTimeout(200);
    out.components['signin-email-btn'].hover = await styleOf(emailBtn);
  }
  const google = sign.getByRole('button', { name: /google/i });
  if (await google.count()) out.components['signin-google'] = { default: await styleOf(google), crop: await crop(sign, google, 'signin-google-default') };
  const apple = sign.getByRole('button', { name: /apple/i });
  if (await apple.count()) out.components['signin-apple'] = { default: await styleOf(apple) };
  out.notes.push('signin buttons measured at rest or hover only; Apple, Google, SSO, Create account and Sign in with email were not clicked');
  out.signinPage = await sign.evaluate(() => ({
    htmlBg: getComputedStyle(document.documentElement).backgroundColor,
    bodyFont: getComputedStyle(document.body).fontFamily,
    bodySize: getComputedStyle(document.body).fontSize,
    bodyColor: getComputedStyle(document.body).color,
  }));

  await sign.close();
} catch (e) {
  out.notes.push('pass stopped early: ' + String(e.message || e).split('\n')[0]);
} finally {
  // Merge into the earlier file state by state (merge-readings.mjs): a state is replaced only by a
  // reading this run took, so a retry whose hover read fails keeps the earlier hover, and every
  // reading keeps the date of the run that took it.
  const file = path.join(RAW, 'readings-pass2.json');
  let earlier = {};
  try { earlier = JSON.parse(fs.readFileSync(file, 'utf8')); } catch { /* first run */ }
  fs.writeFileSync(file, JSON.stringify(mergeReadings(earlier, out, new Date().toISOString().slice(0, 10)), null, 2));
  await browser.close().catch(() => {});
}
console.log('components', Object.keys(out.components));
console.log('notes', out.notes);
for (const [k, v] of Object.entries(out.components)) {
  const d = v.default;
  if (!d || !d.style) { console.log(k, 'no style'); continue; }
  const s = d.style;
  console.log(`\n${k} <${d.tag}.${d.classes.slice(0,40)}> ${d.rect.w}x${d.rect.h} text=${JSON.stringify(d.text).slice(0,60)}`);
  console.log('  color', s.color, 'bg', s.backgroundColor, 'font', s.fontFamily.split(',')[0], s.fontSize, s.fontWeight, 'lh', s.lineHeight, 'ls', s.letterSpacing);
  console.log('  radius', s.borderTopLeftRadius, 'border', s.borderTopWidth, s.borderTopColor, 'pad', s.paddingTop, s.paddingRight, s.paddingBottom, s.paddingLeft);
  console.log('  shadow', s.boxShadow);
  if (d['::before']) console.log('  before', d['::before'].backgroundImage?.slice(0, 180) || d['::before'].backgroundColor, d['::before'].boxShadow?.slice(0, 120));
  if (v.hover) {
    const h = v.hover.style;
    console.log('  HOVER color', h.color, 'bg', h.backgroundColor, 'shadow', (h.boxShadow || '').slice(0, 80));
  }
  if (v.focus) console.log('  FOCUS outline', v.focus.style.outlineWidth, v.focus.style.outlineStyle, v.focus.style.outlineColor, 'shadow', v.focus.style.boxShadow);
  if (d.placeholder) console.log('  ph', d.placeholder);
}
console.log('\nmotion', JSON.stringify(out.motion, null, 2).slice(0, 1500));
