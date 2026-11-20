// Measures Klarna's public components. Nothing is signed into or submitted.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node measure.mjs
import fs from 'node:fs';
import path from 'node:path';
import { BASE, launch, open, hideConsent, styleOf, crop, RAW, CROPS } from './lib.mjs';

fs.mkdirSync(RAW, { recursive: true });
fs.mkdirSync(CROPS, { recursive: true });
const OUT = path.join(RAW, 'components-computed.json');
// Earlier readings are loaded and merged, so a page that fails mid-run (the finally below still
// writes) keeps every component it did not reach instead of erasing them.
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : { components: {} };
out.components ??= {};
// Each refreshed component carries its own run date; _meta.captured moves only when the whole
// run finishes, so retained readings never take a date they were not measured on.
const RUN = new Date().toLocaleDateString('en-CA');
out._meta = { ...(out._meta || {}), product: 'Klarna', route: 'public-web', market: 'https://www.klarna.com/us/', lastRun: RUN };
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);

const { browser, context } = await launch({ width: 1440, height: 900, dpr: 2 });
let page;

async function go(url) {
  page = await context.newPage();
  page.setDefaultTimeout(8000);
  await open(page, url.startsWith('http') ? url : BASE + url, { wait: 3500 });
  const close = page.getByRole('button', { name: /close announcement/i });
  if (await close.count()) await close.first().click().catch(() => {});
  await page.waitForTimeout(400);
}

async function reset() {
  await page.mouse.move(1430, 8).catch(() => {});
  await page.evaluate(() => document.activeElement && document.activeElement.blur && document.activeElement.blur()).catch(() => {});
  await page.waitForTimeout(200);
}

async function kbFocus(loc) {
  await loc.evaluate((el) => el.focus());
  await page.keyboard.press('Shift+Tab');
  await page.keyboard.press('Tab');
  await page.waitForTimeout(300);
  const ok = await loc.evaluate((el) => el === document.activeElement || el.contains(document.activeElement));
  return ok ? 'Shift+Tab, Tab' : 'focus failed';
}

// One CDP session per page, reused for every forced state (a new one per call was never detached).
const sessions = new WeakMap();
async function cdpFor(p) {
  if (!sessions.has(p)) {
    const cdp = await context.newCDPSession(p);
    await cdp.send('DOM.enable');
    await cdp.send('CSS.enable');
    sessions.set(p, cdp);
  }
  return sessions.get(p);
}

async function forcePseudo(loc, classes) {
  const cdp = await cdpFor(page);
  // Clear the marker an earlier call left: DOM.querySelector returns the first marked node in
  // document order, so a stale marker made every later pressed state force the wrong element.
  await page.evaluate(() => document.querySelectorAll('[data-m-force]').forEach((n) => n.removeAttribute('data-m-force')));
  await loc.evaluate((el) => el.setAttribute('data-m-force', '1'));
  const { root } = await cdp.send('DOM.getDocument', { depth: 0 });
  const { nodeId } = await cdp.send('DOM.querySelector', { nodeId: root.nodeId, selector: '[data-m-force]' });
  if (!nodeId) return async () => {};
  await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: classes });
  await page.waitForTimeout(300);
  return async () => { await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: [] }).catch(() => {}); };
}

async function measure(key, state, loc, via) {
  const c = out.components[key];
  const target = loc.filter({ visible: true }).first();
  if (!(await target.count())) {
    c.states[state] = { error: 'missing' };
    log('  ! missing', key, state);
    return;
  }
  await target.scrollIntoViewIfNeeded().catch(() => {});
  await page.waitForTimeout(200);
  const s = await styleOf(target);
  const file = path.join(CROPS, `${key}-${state}.png`);
  try {
    await crop(target, file, 10);
    s.crop = `components/crops/${key}-${state}.png`;
  } catch (e) {
    s.cropError = String(e.message || e).slice(0, 140);
  }
  s.via = via;
  c.states[state] = s;
  log('  ', key, state, s.rect.w + 'x' + s.rect.h, s.style.backgroundColor, s.style.color);
}

function comp(key, meta) {
  out.components[key] = { ...meta, run: RUN, states: {} };
}

async function states(key, loc, list, meta) {
  comp(key, meta);
  for (const st of list) {
    let undo;
    try {
      await reset();
      const target = loc.filter({ visible: true }).first();
      let via = 'at rest';
      if (st === 'hover') {
        await target.hover({ timeout: 4000 }).catch(() => target.hover({ force: true }));
        await page.waitForTimeout(400);
        via = 'mouse hover';
      } else if (st === 'focus-visible') {
        via = await kbFocus(target);
      } else if (st === 'pressed') {
        undo = await forcePseudo(target, ['active', 'hover']);
        via = 'CDP forcePseudoState :active:hover';
      } else if (st === 'focused') {
        await target.click({ timeout: 4000 });
        await page.waitForTimeout(300);
        via = 'clicked into the field; nothing submitted';
      } else if (st === 'filled') {
        await target.click({ timeout: 4000 });
        await page.keyboard.type('headphones', { delay: 15 });
        await page.waitForTimeout(250);
        undo = async () => {
          await target.focus();
          await page.keyboard.press('Meta+a').catch(() => {});
          await page.keyboard.press('Control+a').catch(() => {});
          await page.keyboard.press('Backspace');
        };
        via = 'typed "headphones", then deleted; nothing submitted';
      }
      await measure(key, st, loc, via);
    } catch (e) {
      out.components[key].states[st] = { error: String(e.message || e).slice(0, 180) };
      log('  !', key, st, String(e.message).split('\n')[0]);
    }
    if (undo) await undo().catch(() => {});
  }
}

const B4 = ['default', 'hover', 'focus-visible', 'pressed'];

try {
  await go('/us/');
  log('home', page.url());
  await states('nav-link', page.getByRole('link', { name: 'Shop', exact: true }), B4, {
    title: 'Nav link', group: 'Shell', desc: 'A text link in the sticky header. Pill radius, Klarna Text 14.',
  });
  await states('sign-in-button', page.getByRole('link', { name: /^Sign in$/ }), ['default', 'hover', 'focus-visible', 'pressed'], {
    title: 'Sign in button', group: 'Shell', desc: 'Ink pill in the header. Measured, never followed. The app behind app.klarna.com/login was not entered.',
  });
  await states('primary-button', page.locator('a.button').filter({ hasText: 'Get the app' }).first(), B4, {
    title: 'Primary brand button', group: 'Actions', desc: 'Pink brand pill, Klarna Text 16, height 52. Measured, never followed into the app store or login.',
  });
  await states('ink-button', page.locator('a.button').filter({ hasText: 'Shop now' }).first(), B4, {
    title: 'Ink button', group: 'Actions', desc: 'Near-black pill with off-white text.',
  });
  await states('icon-button', page.getByRole('button', { name: /next slide|previous slide/i }).first(), B4, {
    title: 'Icon button', group: 'Actions', desc: 'Round carousel control, 44px.',
  });
  await states('hero-title', page.locator('h1').first(), ['default'], {
    title: 'Hero title', group: 'Type', desc: 'Klarna Title display heading on the home hero.',
  });
  await states('search-field', page.getByRole('searchbox', { name: /search for any product/i }).first(), ['default', 'hover', 'focused', 'filled', 'focus-visible'], {
    title: 'Search field', group: 'Fields', desc: 'Product search on the marketing home. Text was typed and deleted. Enter was never pressed, so no results page was opened.',
  });
  await states('announcement', page.getByRole('button', { name: /close announcement/i }), ['default'], {
    title: 'Announcement close', group: 'Overlays', desc: 'The phishing-warning strip close control. The strip itself is a public notice, not a consent dialog.',
  }).catch(() => {});

  // language menu (a real menu, not a form submit)
  const lang = page.getByRole('button', { name: /select language/i }).first();
  if (await lang.count()) {
    await lang.click();
    await page.waitForTimeout(500);
    const item = page.getByRole('link', { name: /Español|Spanish|ES/i }).first();
    const menu = page.locator('[role="menu"], [role="listbox"], dialog').first();
    const target = (await item.count()) ? item : menu;
    if (await target.count()) {
      await states('menu-item', target, ['default', 'hover'], {
        title: 'Language menu item', group: 'Overlays', desc: 'An item in the language menu. Hovered only. The link was not followed.',
      });
    }
    await page.keyboard.press('Escape');
  }

  await page.close();

  await go('/us/help/');
  log('help', page.url());
  const summary = page.locator('details summary, button[aria-expanded]').first();
  if (await summary.count()) {
    await states('accordion', summary, ['default', 'hover', 'focus-visible'], {
      title: 'Accordion row', group: 'Help', desc: 'A help topic row. Not expanded if expansion would submit; a disclosure toggle is a UI toggle and is opened below.',
    });
    await summary.click().catch(() => {});
    await page.waitForTimeout(400);
    await states('accordion-open', summary, ['default'], {
      title: 'Accordion row, open', group: 'Help', desc: 'The same row after its disclosure was toggled. No form was submitted.',
    });
  }
  const helpSearch = page.getByRole('searchbox').first();
  if (await helpSearch.count()) {
    await states('help-search', helpSearch, ['default', 'focused'], {
      title: 'Help search', group: 'Fields', desc: 'Help centre search at rest and focused. Nothing was submitted.',
    });
  }
  await page.close();

  await go('/us/shopping/');
  log('shopping', page.url());
  const card = page.locator('a').filter({ hasText: /shop|deal|store/i }).first();
  if (await card.count()) {
    await states('card', card, ['default', 'hover'], {
      title: 'Shop card', group: 'Shopping', desc: 'A linked card on the public shop page. Hovered, never followed into checkout.',
    });
  }
  await page.close();

  // sign-in boundary, measured at rest, never submitted
  await go('https://app.klarna.com/login?market=US&locale=en-US');
  log('signin', page.url(), await page.title());
  await page.waitForTimeout(1500);
  const email = page.locator('input[type="email"], input[name="email"], input[type="text"]').first();
  if (await email.count()) {
    await states('signin-field', email, ['default', 'focused'], {
      title: 'Sign-in field', group: 'Boundary', desc: 'The email or phone field on app.klarna.com/login, measured at rest and focused. Nothing was typed or submitted.',
    });
  }
  const cont = page.getByRole('button', { name: /continue|next|log in|sign in/i }).first();
  if (await cont.count()) {
    await states('signin-continue', cont, ['default', 'hover'], {
      title: 'Sign-in continue', group: 'Boundary', desc: 'The continue control on the login card. Hovered only. The login flow was not started.',
    });
  }
  await page.close();
  out._meta.captured = RUN;   // every page ran
} finally {
  fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
  await browser.close();
}
log('wrote', OUT, Object.keys(out.components).length, 'components');
