// Stopping an agent run that is still going when run.mjs gives up on it (a step past TIMEOUT, or a frame that
// failed). Kept apart from product.mjs (which loads Playwright) so `node --test` can check it; test_stop.py runs
// that from `make test`.
//
// stopRun takes the product's own reads and clicks:
//   running()  true while the run shows any sign of work (product.mjs reads Capy's Stop run button, the
//              Working glyph and a live shimmer)
//   stop()     clicks the control that stops it; called once, only while running() is true. If the click fails
//              and the run has ended meanwhile, that counts as stopped; if it is still running, the error is thrown
//   wait(ms)   sleeps (page.waitForTimeout in the capture, a fake clock in the tests)
// It resolves `false` when nothing was running, `true` once the run reads as stopped, and throws when the run is
// still going `timeout` ms after the click, so the capture fails loudly instead of leaving an agent working.
export async function stopRun({ running, stop, wait, timeout = 30000, interval = 500 }) {
  if (!(await running())) return false;
  // The run can end on its own between the read and the click, taking the Stop button with it; the click then
  // fails, which only matters if the run is still going.
  try { await stop(); } catch (e) { if (await running()) throw e; return true; }
  for (let waited = 0; waited < timeout; waited += interval) {
    await wait(interval);
    if (!(await running())) return true;
  }
  throw new Error(`the agent run did not stop within ${timeout} ms of clicking Stop: stop it by hand`);
}
