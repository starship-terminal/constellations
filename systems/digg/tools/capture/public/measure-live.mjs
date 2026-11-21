// Measure Digg public components and map the signed-out site tree.
// Hides section.cookie-notice (does not click Accept). Does not submit forms
// or click identity providers.
//
//   PLAYWRIGHT=... node measure-live.mjs
import fs from 'node:fs';
import path from 'node:path';
import os from 'node:os';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'digg', 'readings');
fs.mkdirSync(RAW, { recursive: true });

const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
const PROPS = [
  'display', 'position', 'boxSizing', 'width', 'height', 'minHeight',
  'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft',
  'marginTop', 'gap', 'fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'letterSpacing',
  'color', 'backgroundColor', 'borderTopColor', 'borderTopWidth', 'borderTopStyle',
  'borderRadius', 'boxShadow', 'outline', 'textDecorationLine', 'opacity',
];

function pick(style) {
  const out = {};
  for (const k of PROPS) out[k] = style[k];
  return out;
}

const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({
  viewport: { width: 1440, height: 900 },
  deviceScaleFactor: 1,
  userAgent: UA,
  locale: 'en-US',
});
const page = await context.newPage();
page.setDefaultTimeout(15000);

async function hideConsent(p) {
  await p.addStyleTag({ content: 'section.cookie-notice, .cookie-notice { display: none !important; visibility: hidden !important; pointer-events: none !important; }' }).catch(() => {});
}
async function go(url) {
  const resp = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(1400);
  await hideConsent(page);
  return { status: resp && resp.status(), url: page.url() };
}

async function measure(label, locator) {
  const el = locator.first();
  if (!(await el.count())) return { label, missing: true };
  const box = await el.boundingBox();
  const styles = await el.evaluate((node, props) => {
    const cs = getComputedStyle(node);
    const out = {};
    for (const k of props) out[k] = cs[k];
    return {
      styles: out,
      text: (node.innerText || node.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim().slice(0, 80),
      tag: node.tagName,
      role: node.getAttribute('role'),
      dataSlot: node.getAttribute('data-slot'),
      dataVariant: node.getAttribute('data-variant'),
      dataSize: node.getAttribute('data-size'),
      disabled: node.matches(':disabled') || node.getAttribute('aria-disabled') === 'true',
    };
  }, PROPS);
  return { label, box, ...styles };
}

async function forceState(locator, state) {
  const el = locator.first();
  if (!(await el.count())) return 'missing';
  if (state === 'hover') {
    await el.hover();
    return 'hover';
  }
  if (state === 'focus-visible') {
    await el.focus();
    return 'focus';
  }
  if (state === 'pressed') {
    await page.evaluate((sel) => {
      // applied by caller via element handle
    });
    return 'pressed-skip';
  }
  return state;
}

const readings = { capturedAt: new Date().toISOString(), viewport: { width: 1440, height: 900 }, components: {} };

await go('https://digg.com/');

const homeSpecs = {
  'button-signup': page.locator('a[href*="/sign-up"]').filter({ hasText: 'Sign up' }),
  'button-login': page.locator('a[href*="/login"]').filter({ hasText: 'Log in' }),
  'button-theme': page.locator('button[aria-label*="Switch theme"]'),
  'nav-link-home': page.locator('a[href="/"]').filter({ hasText: 'Home' }),
  'nav-link-tech': page.locator('a[href="/tech"]'),
  'button-feed-view': page.locator('button[aria-label="Feed View"]'),
  'button-feed-display': page.locator('button[aria-label^="Feed display"]'),
  'icon-button-sidebar': page.locator('button[aria-label="Toggle Sidebar"]').first(),
  'card-post': page.locator('main article, main [data-slot="card"]').first(),
  'link-story': page.locator('main a[href*="/ai/"], main a[href*="/tech/"]').first(),
  'badge-topic': page.locator('main a[href="/ai"]').filter({ hasText: /^AI$/ }).first(),
  'avatar': page.locator('a[href^="/u/"]').first(),
  'sidebar': page.locator('aside, [data-slot="sidebar"]').first(),
};

async function readStates(name, locator) {
  const base = await measure(name + '-default', locator);
  readings.components[name] = { default: base };
  if (base.missing) return;
  const el = locator.first();
  await el.hover().catch(() => {});
  await page.waitForTimeout(150);
  readings.components[name].hover = await measure(name + '-hover', locator);
  await page.mouse.move(700, 450);
  await el.focus().catch(() => {});
  await page.waitForTimeout(80);
  readings.components[name].focus = await measure(name + '-focus', locator);
  // pressed via CDP
  const pressed = await el.evaluate((node, props) => {
    node.setAttribute('data-digg-press', '1');
    return null;
  }, PROPS).catch(() => null);
  try {
    const session = await context.newCDPSession(page);
    const { nodeId } = await session.send('DOM.getDocument').then(() => null).catch(() => ({ nodeId: null }));
  } catch {}
  const forced = await el.evaluate((node, props) => {
    const prev = node.style.cssText;
    // Force :active is not possible from CSSOM; read active styles by toggling a class the product uses.
    return { note: 'pressed not forced here' };
  }, PROPS);
  readings.components[name].pressedNote = 'Not captured: active:translate-y-px is in the class list; a held press was not measured.';
}

for (const [name, loc] of Object.entries(homeSpecs)) {
  try { await readStates(name, loc); console.log('measured', name, readings.components[name].default.missing ? 'MISSING' : readings.components[name].default.text); }
  catch (e) { readings.components[name] = { error: String(e.message).split('\n')[0] }; console.log('fail', name, e.message.split('\n')[0]); }
}

// Open feed view listbox and measure an option
await page.locator('button[aria-label="Feed View"]').click();
await page.waitForTimeout(300);
readings.components['menu-feed-view'] = {
  open: await measure('feed-option', page.locator('[role="option"]').first()),
  options: await page.locator('[role="option"]').allTextContents(),
};
await page.keyboard.press('Escape');

await page.locator('button[aria-label^="Feed display"]').click();
await page.waitForTimeout(300);
readings.components['menu-feed-display'] = {
  open: await measure('display-option', page.locator('[role="option"]').first()),
  options: await page.locator('[role="option"]').allTextContents(),
};
await page.keyboard.press('Escape');

// Layout
readings.layout = await page.evaluate(() => {
  const root = getComputedStyle(document.documentElement);
  const main = document.querySelector('main');
  const aside = document.querySelector('aside, [data-sidebar="sidebar"]');
  const mr = main ? main.getBoundingClientRect() : null;
  const ar = aside ? aside.getBoundingClientRect() : null;
  return {
    innerWidth: innerWidth,
    innerHeight: innerHeight,
    dpr: devicePixelRatio,
    visualViewport: visualViewport ? { width: visualViewport.width, height: visualViewport.height, scale: visualViewport.scale } : null,
    main: mr && { x: mr.x, y: mr.y, w: mr.width, h: mr.height },
    aside: ar && { x: ar.x, y: ar.y, w: ar.width, h: ar.height },
    radius: root.getPropertyValue('--radius').trim(),
    fontSans: root.getPropertyValue('--font-sans').trim(),
    fontHeading: root.getPropertyValue('--font-heading').trim(),
    fontMono: root.getPropertyValue('--font-mono').trim(),
  };
});

// Login wall: record controls, do not type or click Google/X
const loginNav = await go('https://digg.com/login?redirect_url=%2F');
readings.login = { ...loginNav };
readings.login.fields = await page.locator('input').evaluateAll((els) => els.map((el) => ({
  type: el.getAttribute('type'), name: el.getAttribute('name'), placeholder: el.getAttribute('placeholder'), id: el.id,
})));
readings.login.idp = await page.locator('button').evaluateAll((els) => els.map((el) => (el.innerText || '').replace(/\s+/g, ' ').trim()).filter((t) => /google|twitter|^x$|continue/i.test(t)));
readings.components['text-field-email'] = { default: await measure('email', page.locator('#identifier-field')) };
readings.components['text-field-password'] = { default: await measure('password', page.locator('#password-field')) };
readings.components['button-continue'] = { default: await measure('continue', page.getByRole('button', { name: 'Continue', exact: true })) };
// focus email without typing
await page.locator('#identifier-field').focus();
readings.components['text-field-email'].focus = await measure('email-focus', page.locator('#identifier-field'));
console.log('login fields', JSON.stringify(readings.login.fields), 'idp', readings.login.idp);

const signupNav = await go('https://digg.com/sign-up?redirect_url=%2F');
readings.signup = {
  ...signupNav,
  fields: await page.locator('input').evaluateAll((els) => els.map((el) => ({ type: el.getAttribute('type'), name: el.getAttribute('name'), placeholder: el.getAttribute('placeholder') }))),
  idp: await page.locator('button').evaluateAll((els) => els.map((el) => (el.innerText || '').replace(/\s+/g, ' ').trim()).filter((t) => /google|twitter|continue/i.test(t))),
  heading: await page.locator('h1').allTextContents(),
};
console.log('signup', readings.signup.heading, readings.signup.idp);

// Story page
const story = await go('https://digg.com/ai/f7vysbah');
readings.story = story;
readings.story.controls = await page.evaluate(() => [...document.querySelectorAll('main button, main a')].filter((el) => {
  const r = el.getBoundingClientRect();
  return r.width > 8 && r.height > 8 && r.top > 0 && r.top < 700;
}).slice(0, 30).map((el) => ({
  text: (el.innerText || el.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim().slice(0, 70),
  href: el.getAttribute('href') || '',
  tag: el.tagName,
})));
readings.components['button-digg'] = { default: await measure('digg', page.locator('main button').filter({ hasText: /digg it/i }).first()) };
console.log('story controls', readings.story.controls.length);

// Comment hash: may be a wall
const comments = await go('https://digg.com/ai/f7vysbah#comments');
await page.waitForTimeout(600);
readings.comments = {
  ...comments,
  snippet: await page.evaluate(() => (document.body.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 400)),
  dialog: await page.locator('[role="dialog"]').count(),
};
console.log('comments dialogs', readings.comments.dialog);

// Follow button destination without submitting
await go('https://digg.com/u/justinmezzell');
const follow = page.locator('main button').filter({ hasText: /^Follow$/ }).first();
readings.profile = {
  url: page.url(),
  followExists: await follow.count(),
};
if (await follow.count()) {
  readings.components['button-follow'] = { default: await measure('follow', follow) };
  await follow.click();
  await page.waitForTimeout(800);
  readings.profile.afterFollow = { url: page.url(), title: await page.title() };
  console.log('follow click landed', readings.profile.afterFollow.url);
}

// Static pages headings + links
const staticPages = ['/about', '/contact', '/privacy', '/tos', '/community-guidelines'];
readings.staticPages = {};
for (const pth of staticPages) {
  const nav = await go('https://digg.com' + pth);
  const info = await page.evaluate(() => ({
    title: document.title,
    h1: [...document.querySelectorAll('h1')].map((el) => el.innerText.replace(/\s+/g, ' ').trim()).slice(0, 3),
    links: [...document.querySelectorAll('main a, article a')].map((a) => ({ text: (a.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 60), href: a.href })).filter((l) => l.href && !l.href.startsWith('mailto:')).slice(0, 25),
    inputs: document.querySelectorAll('input, textarea, form').length,
  }));
  readings.staticPages[pth] = { ...nav, ...info };
  console.log('static', pth, info.h1.join(' / '));
}

// llms.txt is text, not a page to screenshot as UI; record status only
try {
  const r = await page.goto('https://digg.com/llms.txt', { waitUntil: 'domcontentloaded', timeout: 30000 });
  readings.llms = { status: r && r.status(), url: page.url(), contentType: r && r.headers()['content-type'] };
} catch (e) {
  readings.llms = { error: String(e.message).split('\n')[0] };
}

// 404
const missing = await go('https://digg.com/this-page-does-not-exist-capture');
readings.notFound = {
  ...missing,
  title: await page.title(),
  h1: await page.locator('h1').allTextContents().catch(() => []),
  snippet: await page.evaluate(() => (document.body.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 240)),
};
console.log('404', readings.notFound.title, readings.notFound.snippet.slice(0, 120));

// Motion + reduced motion from stylesheets already in vars; sample computed transition on signup button
await go('https://digg.com/');
readings.motion = await page.locator('a[href*="/sign-up"]').first().evaluate((node) => {
  const cs = getComputedStyle(node);
  const root = getComputedStyle(document.documentElement);
  return {
    transition: cs.transition,
    transitionDuration: cs.transitionDuration,
    transitionTimingFunction: cs.transitionTimingFunction,
    defaultDuration: root.getPropertyValue('--default-transition-duration').trim(),
    easeOut: root.getPropertyValue('--ease-out').trim(),
    easeInOut: root.getPropertyValue('--ease-in-out').trim(),
  };
});

// breakpoints from stylesheet media
readings.breakpoints = await page.evaluate(() => {
  const found = new Set();
  for (const sheet of document.styleSheets) {
    let rules;
    try { rules = sheet.cssRules; } catch { continue; }
    const walk = (list) => {
      for (const r of list) {
        if (r.type === CSSRule.MEDIA_RULE) {
          const t = r.conditionText || r.media.mediaText;
          if (/width|min-width|max-width/.test(t) && t.length < 80) found.add(t);
          walk(r.cssRules);
        }
      }
    };
    walk(rules);
  }
  return [...found].slice(0, 40);
});

fs.writeFileSync(path.join(RAW, 'components.json'), JSON.stringify(readings, null, 2));
console.log('wrote components.json');
await browser.close();
