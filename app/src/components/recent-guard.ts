/** Remembers when something last ran, so a burst of triggers runs it once. */
export function createRecentGuard(
  windowMs: number,
  now: () => number = Date.now,
) {
  let last = -Infinity;
  return {
    mark() {
      last = now();
    },
    /** True when `mark` was called less than `windowMs` ago. */
    fresh() {
      return now() - last < windowMs;
    },
  };
}
