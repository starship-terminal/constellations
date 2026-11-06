// The listings' shared search scoring, ported from the old app.js: stop
// words drop out, a term that names a facet value the row holds counts
// double, one term may miss once a query has 3+ words, and adjacent terms
// found as a phrase score extra.
const SEARCH_STOP = new Set(
  "a an the and or of for in on to with by at is it this that site sites website websites page pages design designed style styles app apps web landing product products".split(
    " ",
  ),
);

export const terms = (q: string): string[] =>
  q
    .trim()
    .toLowerCase()
    .split(/\s+/)
    .filter((w) => w && !SEARCH_STOP.has(w));

/** [the facet's values, does this row hold value t]. */
export type Facet<T> = [Set<string>, (row: T, t: string) => boolean];

/** 0 hides the row; with no terms every row scores 1. `hay` is lower case. */
export function scoreRow<T>(row: T, hay: string, toks: string[], facets: Facet<T>[]): number {
  if (!toks.length) return 1;
  let sat = 0;
  let sc = 0;
  for (const t of toks) {
    let hit = hay.includes(t) ? 1 : 0;
    for (const [values, test] of facets)
      if (values.has(t) && test(row, t)) {
        hit = 2;
        break;
      }
    if (hit) {
      sat++;
      sc += hit;
    }
  }
  if (sat < (toks.length <= 2 ? toks.length : toks.length - 1)) return 0;
  for (let i = 0; i < toks.length - 1; i++) if (hay.includes(`${toks[i]} ${toks[i + 1]}`)) sc += 1.5;
  return sc;
}
