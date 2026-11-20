import type {
  ScreenFacet,
  ScreenItem,
  ScreenQuery,
  ScreenResponse,
} from "@/contracts/screens";
import { listCapturedMedia, MAX_CACHE_AGE, sourceStamp } from "./index";
import { categoryGroup, matchesCategory } from "@/contracts/categories";
import { withReferenceCategories } from "@/server/taxonomy/library";
import { getStore } from "@/server/db";

export class UnknownScreenTermError extends Error {}

export function validScreenTermId(value: string): boolean {
  return (
    value.length <= 400 &&
    /^[a-z][a-z0-9-]*:[\p{L}\p{N}][\p{L}\p{N}-]*$/u.test(value)
  );
}

const pending = new Map<string, Promise<ScreenItem[]>>();
let cache: { key: string; loadedAt: number; items: ScreenItem[] } | undefined;
export function validScreenId(value: string): boolean {
  if (value.length > 2400) return false;
  const match = /^systems:([a-z0-9][a-z0-9-]*):(.+)$/.exec(value);
  return (
    !!match &&
    match[2].startsWith(`systems/${match[1]}/`) &&
    !match[2].includes("\\") &&
    !match[2].includes("\0") &&
    !match[2].split("/").some((part) => !part || part === "." || part === "..")
  );
}
async function capturedScreens(): Promise<ScreenItem[]> {
  // Listing every capture resolves each screenshot and crop on disk, so the
  // list lives as long as the library sources do: until a catalog, generated
  // data or the media mirror changes, and at most MAX_CACHE_AGE.
  const key = await sourceStamp();
  if (cache?.key === key && Date.now() - cache.loadedAt < MAX_CACHE_AGE)
    return cache.items;
  const current = pending.get(key);
  if (current) return current;
  const load = (async () => {
    const captures = await listCapturedMedia();
    const seen = new Set<string>();
    const items = captures.flatMap(({ reference, media }) =>
      media.flatMap((asset): ScreenItem[] => {
        if (
          asset.type !== "image" ||
          !["screenshot", "crop"].includes(asset.kind || "")
        )
          return [];
        const id = `${reference.id}:${asset.id}`;
        if (seen.has(id)) return [];
        seen.add(id);
        return [{ id, reference, media: asset }];
      }),
    );
    cache = { key, loadedAt: Date.now(), items };
    return items;
  })();
  pending.set(key, load);
  try {
    return await load;
  } finally {
    if (pending.get(key) === load) pending.delete(key);
  }
}

function counts(
  items: ScreenItem[],
  values: (item: ScreenItem) => string[],
): ScreenFacet[] {
  const result = new Map<string, number>();
  for (const item of items)
    for (const value of new Set(values(item).filter(Boolean)))
      result.set(value, (result.get(value) || 0) + 1);
  return [...result]
    .map(([value, count]) => ({ value, count }))
    .sort((a, b) => b.count - a.count || a.value.localeCompare(b.value));
}

function captureTermIds(item: ScreenItem): string[] {
  return [
    ...new Set([
      ...(item.reference.categoryIds || []),
      ...(item.termIds || []),
    ]),
  ];
}

/** At most `perProduct` captures per product, interleaved across products in first-seen order. */
export function samplePerProduct(
  items: ScreenItem[],
  perProduct: number,
): ScreenItem[] {
  const cap = Math.max(0, Math.floor(perProduct));
  const groups = new Map<string, ScreenItem[]>();
  for (const item of items) {
    const group = groups.get(item.reference.id) || [];
    if (group.length < cap) group.push(item);
    groups.set(item.reference.id, group);
  }
  const sampled: ScreenItem[] = [];
  for (let round = 0; round < cap; round++)
    for (const group of groups.values())
      if (group[round]) sampled.push(group[round]);
  return sampled;
}

/** Search genuine capture names/groups and recorded package metadata. No inferred taxonomy. */
export function queryScreens(
  items: ScreenItem[],
  query: ScreenQuery = {},
): ScreenResponse {
  const words = (query.query || "")
    .trim()
    .toLowerCase()
    .split(/[\s_-]+/)
    .filter(Boolean);
  const referenceIds = new Set(query.referenceIds || []);
  const selectedTerms = [...new Set(query.termIds || [])];
  const available = query.mode === "flows" ? [] : items;
  const corpus = available.filter(
    ({ reference, media }) =>
      reference.source === "systems" &&
      (!query.platform || reference.platform === query.platform) &&
      (query.screenId && !query.kind
        ? true
        : media.kind === (query.kind || "screenshot")),
  );
  const termCounts = Object.fromEntries(
    counts(corpus, captureTermIds).map(({ value, count }) => [value, count]),
  );
  const scoped = corpus.filter(
    ({ reference, media }) =>
      (!referenceIds.size || referenceIds.has(reference.id)) &&
      (!query.theme ||
        (media.tags.some((tag) => tag === "light" || tag === "dark")
          ? media.tags
          : reference.themes
        ).some(
          (theme) =>
            theme === query.theme || theme.startsWith(`${query.theme}-`),
        )),
  );
  const filtered = scoped
    .filter((item) => {
      const { reference, media } = item;
      const terms = new Set(captureTermIds(item));
      return (
        selectedTerms.every((term) => terms.has(term)) &&
        (!query.screenId || `${reference.id}:${media.id}` === query.screenId) &&
        (!query.category || matchesCategory(reference, query.category)) &&
        (!query.group || media.group === query.group) &&
        (!query.tag ||
          media.tags.includes(query.tag) ||
          reference.tags.includes(query.tag)) &&
        words.every((word) => {
          const mediaText = `${media.name} ${media.path || ""} ${media.group || ""} ${media.tags.join(" ")}`;
          const packageText =
            query.scope === "media"
              ? ""
              : ` ${reference.name} ${reference.slug} ${reference.description} ${reference.category} ${(reference.categories || []).map((term) => term.label).join(" ")} ${reference.tags.join(" ")}`;
          return `${mediaText}${packageText}`.toLowerCase().includes(word);
        })
      );
    })
    .sort(
      (a, b) =>
        (query.sort === "name"
          ? 0
          : (b.reference.captured || "").localeCompare(
              a.reference.captured || "",
            )) ||
        a.reference.name.localeCompare(b.reference.name) ||
        a.media.name.localeCompare(b.media.name) ||
        a.id.localeCompare(b.id),
    );
  const offset = Number.isFinite(query.offset)
    ? Math.max(0, Math.floor(query.offset!))
    : 0;
  const limit = Number.isFinite(query.limit)
    ? Math.min(200, Math.max(0, Math.floor(query.limit!)))
    : 60;
  const page =
    !query.screenId && query.perProduct !== undefined
      ? samplePerProduct(filtered, query.perProduct)
      : filtered;
  return {
    items: query.screenId
      ? filtered.slice(0, 1)
      : page.slice(offset, offset + limit),
    total: filtered.length,
    pageable: page.length,
    termCounts,
    facets: {
      platforms: counts(available, ({ reference }) => [reference.platform]),
      categories: counts(
        scoped,
        ({ reference }) =>
          reference.categoryIds || [categoryGroup(reference.category)],
      ),
      tags: counts(scoped, ({ reference, media }) => [
        ...reference.tags,
        ...media.tags,
      ]),
      groups: counts(scoped, ({ media }) => [media.group || ""]),
      kinds: counts(available, ({ media }) => [media.kind || ""]),
    },
  };
}

export async function listScreens(
  query: ScreenQuery = {},
): Promise<ScreenResponse> {
  const store = await getStore();
  if (query.termIds?.length) {
    const knownTerms = new Set(
      (await store.listTaxonomyGroups())
        .filter((group) => group.kind === "taxonomy")
        .flatMap((group) => group.terms.map((term) => term.id)),
    );
    for (const termId of query.termIds)
      if (!validScreenTermId(termId) || !knownTerms.has(termId))
        throw new UnknownScreenTermError(
          `Unknown capture filter term: ${termId}`,
        );
  }
  if (query.mode === "flows") return queryScreens([], query);
  const captures = await capturedScreens();
  const [references, byMedia] = await Promise.all([
    withReferenceCategories(
      [
        ...new Map(
          captures.map((item) => [item.reference.id, item.reference]),
        ).values(),
      ],
      store,
    ),
    store.mediaTermsByMedia(),
  ]);
  const byId = new Map(
    references.map((reference) => [reference.id, reference]),
  );
  return queryScreens(
    captures.map((item) => ({
      ...item,
      reference: byId.get(item.reference.id)!,
      termIds: byMedia.get(item.id) || [],
    })),
    query,
  );
}
