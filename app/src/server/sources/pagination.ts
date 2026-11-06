/**
 * Read `limit` and `offset` from a list route's query. A missing value takes
 * its default and a large one is clamped; anything but a whole number from 0
 * to Number.MAX_SAFE_INTEGER (an empty value, a fraction, a negative, 1e400)
 * is invalid and returns null so the route answers 400.
 */
export function parsePagination(
  params: URLSearchParams,
  defaults: { limit: number; maxLimit: number },
): { limit: number; offset: number } | null {
  const read = (name: string, fallback: number, max: number) => {
    const raw = params.get(name);
    if (raw === null) return fallback;
    const value = raw.trim() === "" ? NaN : Number(raw);
    return Number.isSafeInteger(value) && value >= 0
      ? Math.min(max, value)
      : null;
  };
  const limit = read("limit", defaults.limit, defaults.maxLimit),
    offset = read("offset", 0, Number.MAX_SAFE_INTEGER);
  return limit === null || offset === null ? null : { limit, offset };
}
