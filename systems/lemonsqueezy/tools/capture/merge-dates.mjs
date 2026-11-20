// Capture dates for a components file that a run merges into instead of replacing.
//
// _meta.captured names the latest run. Each state also carries its own `read`
// date: a state measured now gets the run's date, and a state kept from an
// earlier run keeps the date it was read (states saved before per-state dates
// existed take the earlier file's _meta.captured). So a reading that survived a
// failed visit never looks like part of today's capture.

/** Give every state of the prior file a `read` date, from the prior _meta.captured. */
export function datePrior(components, priorCaptured) {
  if (!priorCaptured) return components;
  for (const c of Object.values(components || {})) {
    for (const st of Object.values((c && c.states) || {})) {
      if (st && typeof st === 'object' && !st.read) st.read = priorCaptured;
    }
  }
  return components;
}
