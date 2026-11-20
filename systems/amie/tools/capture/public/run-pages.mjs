// Page bookkeeping for measure.mjs. A page runner that throws is logged and
// recorded as broken, and the run goes on to the next page, so one failure
// does not lose the others. exitStatus() then turns any broken page into a
// nonzero exit naming the pages that threw, so a caller can see the capture
// is incomplete. A page counts as finished only when its runner returns.
export function pageRunner(getCurrent, log = console.log) {
  const finished = new Set();
  const broken = new Map(); // page -> first line of the error
  async function runPage(fn, ...args) {
    try {
      await fn(...args);
      const c = getCurrent();
      if (c) finished.add(c);
    } catch (e) {
      const msg = String((e && e.message) || e).split('\n')[0];
      broken.set(getCurrent() || fn.name || 'unknown page', msg);
      log('PAGE FAILED', fn.name, msg);
    }
  }
  return { finished, broken, runPage };
}

export function exitStatus(broken, log = console.error) {
  if (!broken.size) return 0;
  log('INCOMPLETE: pages threw: ' + [...broken].map(([p, m]) => `${p} (${m})`).join('; '));
  return 1;
}
