import type { LibraryItem } from "@/contracts/library";

export type StyleFacet = "theme" | "type" | "style" | "industry";
/** Some upstream RSC strings look like `$1e`; they are not captured HTML. */
export function hasComponentMarkup(value: unknown): value is string {
  return typeof value === "string" && /<[a-z][\s\S]*>/i.test(value);
}
export function isUnresolvedCapture(value: unknown): boolean {
  return typeof value === "string" && /^\$[\w]+$/.test(value.trim());
}
export interface StyleFilters {
  q: string;
  theme: string;
  type: string;
  style: string;
  industry: string;
  tags: string[];
  video: boolean;
}
const STOP = new Set(
  "a an the and or of for in on to with by at is it this that site sites website websites page pages design designed style styles app apps web landing product products".split(
    " ",
  ),
);
export const styleFacet = (item: LibraryItem, key: StyleFacet): string =>
  key === "theme"
    ? item.themes[0] || ""
    : key === "type"
      ? item.productType || ""
      : key === "style"
        ? item.designStyle || ""
        : item.industry || "";
export function styleHost(url?: string | null): string {
  try {
    return url ? new URL(url).hostname.replace(/^www\./, "") : "";
  } catch {
    return "";
  }
}
export function filterStyles(
  items: LibraryItem[],
  filters: StyleFilters,
): LibraryItem[] {
  const words = filters.q
    .toLowerCase()
    .split(/\s+/)
    .filter((word) => word && !STOP.has(word));
  return items
    .filter((item) => item.source === "refero")
    .filter(
      (item) =>
        (["theme", "type", "style", "industry"] as const).every(
          (key) => !filters[key] || styleFacet(item, key) === filters[key],
        ) &&
        (!filters.video || !!item.video) &&
        filters.tags.every((tag) => item.tags.includes(tag)),
    )
    .map((item) => {
      const facetWords = [
        ...item.themes,
        item.productType,
        item.designStyle,
        item.industry,
        ...item.tags,
      ]
        .filter(Boolean)
        .map((v) => v!.toLowerCase());
      const hay = [
        item.name,
        item.slug,
        item.description,
        styleHost(item.sourceUrl),
        ...facetWords,
      ]
        .join(" ")
        .toLowerCase();
      const hits = words.map((word) =>
        facetWords.includes(word) ? 2 : hay.includes(word) ? 1 : 0,
      );
      const satisfied =
        hits.filter(Boolean).length >=
        (words.length <= 2 ? words.length : words.length - 1);
      return {
        item,
        score: satisfied
          ? hits.reduce<number>((a, b) => a + b, 0) +
            words
              .slice(0, -1)
              .reduce(
                (n, word, i) =>
                  n + (hay.includes(`${word} ${words[i + 1]}`) ? 1.5 : 0),
                0,
              )
          : -1,
      };
    })
    .filter(({ score }) => score >= 0)
    .sort((a, b) => (words.length ? b.score - a.score : 0))
    .map(({ item }) => item);
}
export function styleCounts(
  items: LibraryItem[],
  key: StyleFacet | "tag",
): [string, number][] {
  const counts = new Map<string, number>();
  for (const item of items)
    for (const value of key === "tag" ? item.tags : [styleFacet(item, key)])
      if (value) counts.set(value, (counts.get(value) || 0) + 1);
  return [...counts].sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0]));
}
