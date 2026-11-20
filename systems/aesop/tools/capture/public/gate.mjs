// The bot-check boundary for the aesop.com captures: one load per page, no
// way around a challenge. Kept free of Playwright so a stub page can test it
// (test_gate.mjs).
//
// aesop.com sits behind Cloudflare Turnstile, which challenges the second
// document a browser context loads. The committed readings of the product
// page were taken by giving each product page a fresh context whose first
// document was that page, which is getting past the check rather than
// recording it. A bot check is a boundary (2026-11 audit; not run since):
// each page is loaded once, in its run's own context, and a page that shows
// a challenge or an error is recorded as blocked and never measured or shot.
// There is no reload, no retry and no new context for a challenged page.

const CHALLENGE_TITLE = /just a moment/i;
const CHALLENGE_BODY = /performing security verification|verify you are human|verifying you are human|checking your browser/i;
const ERROR_BODY = /something went wrong|^not found$|page cannot be found/i;

// What the page shows now: 'challenge', 'error', 'empty' or 'ok'.
export async function pageState(page) {
  const s = await page.evaluate(() => ({
    title: document.title,
    body: ((document.body && document.body.innerText) || '').trim(),
  })).catch(() => ({ title: '', body: '' }));
  if (CHALLENGE_TITLE.test(s.title) || CHALLENGE_BODY.test(s.body)) return 'challenge';
  if (ERROR_BODY.test(s.body)) return 'error';
  if (s.body.length <= 40) return 'empty';
  return 'ok';
}

// Waits, without acting on the page, for an interstitial to finish on its own
// (up to ~tries*step), and reports whether a document that is not a challenge
// arrived. Nothing is clicked, solved, reloaded or retried.
export async function clearChallenge(page, { tries = 12, step = 2000 } = {}) {
  for (let i = 0; i < tries; i++) {
    const state = await pageState(page);
    if (state === 'ok' || state === 'error') return true;
    await page.waitForTimeout(step);
  }
  return false;
}

// Loads `url` once in `page`. Resolves { ok: true } when the page is the
// product, else { ok: false, reason } and leaves the tab on about:blank so
// nothing downstream can measure or shoot the challenge as the product.
export async function loadOnce(page, url, { timeout = 90000, tries, step } = {}) {
  let reason = null;
  try {
    await page.goto(url, { waitUntil: 'domcontentloaded', timeout });
  } catch (e) {
    reason = `load failed: ${String(e.message).split('\n')[0]}`;
  }
  if (!reason) {
    if (!(await clearChallenge(page, { tries, step }))) {
      reason = (await pageState(page)) === 'challenge' ? 'bot check did not clear' : 'page served no content';
    } else if ((await pageState(page)) === 'error') {
      reason = 'page served an error';
    }
  }
  if (!reason) return { ok: true };
  await page.goto('about:blank').catch(() => {});
  return { ok: false, reason };
}

// Records a blocked page in a reading file's _meta, leaving every earlier
// reading (out.components and the rest) as it was.
export function recordBlocked(out, key, url, reason, run) {
  out._meta ??= {};
  out._meta.blocked ??= {};
  out._meta.blocked[key] = { url, reason, run };
  return out;
}
