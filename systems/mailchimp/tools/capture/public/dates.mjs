// Read dates for measure.mjs's merge into raw/components-computed.json. Pure, so
// tools/capture/public/test_dates.mjs checks it without a browser.
//
// A rerun starts from the committed readings, so _meta.read keeps the earlier date until this run
// reads a state, and _meta.lastAttempt records the run either way. A component's `run` and each
// state's `run` likewise move only on a successful read (markRead), never on first touch.

export function startRun(out, run) {
  out._meta ??= {};
  out.components ??= {};
  out._meta.lastAttempt = run;
  return out;
}

export function markRead(out, c, state, reading, run) {
  c.states[state] = { ...reading, run };
  c.run = run;
  out._meta.read = run;
}
