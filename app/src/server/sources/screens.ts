import type {
  ScreenFacet,
  ScreenItem,
  ScreenQuery,
  ScreenResponse,
} from "@/contracts/screens";
import { listCapturedMedia } from "./index";
import { repoRoot } from "./files";

const pending = new Map<string, Promise<ScreenItem[]>>();
let cache: { key: string; until: number; items: ScreenItem[] } | undefined;
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
  const key = [
    repoRoot(),
    process.env.DESIGN_SYSTEMS_MEDIA,
    process.env.DESIGN_SYSTEMS_MEDIA_BASE,
  ].join("|");
  if (cache?.key === key && cache.until > Date.now()) return cache.items;
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
    cache = { key, until: Date.now() + 30_000, items };
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
  const scoped = items.filter(
    ({ reference, media }) =>
      reference.source === "systems" &&
      (!query.platform || reference.platform === query.platform) &&
      (!query.referenceId || reference.id === query.referenceId) &&
      (!query.theme ||
        (media.tags.some((tag) => tag === "light" || tag === "dark")
          ? media.tags
          : reference.themes
        ).some(
          (theme) =>
            theme === query.theme || theme.startsWith(`${query.theme}-`),
        )) &&
      (query.screenId && !query.kind
        ? true
        : media.kind === (query.kind || "screenshot")),
  );
  const filtered = scoped
    .filter(
      ({ reference, media }) =>
        (!query.screenId || `${reference.id}:${media.id}` === query.screenId) &&
        (!query.category || reference.category === query.category) &&
        (!query.group || media.group === query.group) &&
        (!query.tag ||
          media.tags.includes(query.tag) ||
          reference.tags.includes(query.tag)) &&
        words.every((word) => {
          const mediaText = `${media.name} ${media.path || ""} ${media.group || ""} ${media.tags.join(" ")}`;
          const packageText =
            query.scope === "media"
              ? ""
              : ` ${reference.name} ${reference.slug} ${reference.description} ${reference.category} ${reference.tags.join(" ")}`;
          return `${mediaText}${packageText}`.toLowerCase().includes(word);
        }),
    )
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
  return {
    items: query.screenId
      ? filtered.slice(0, 1)
      : filtered.slice(offset, offset + limit),
    total: filtered.length,
    facets: {
      platforms: counts(items, ({ reference }) => [reference.platform]),
      categories: counts(scoped, ({ reference }) => [reference.category]),
      tags: counts(scoped, ({ reference, media }) => [
        ...reference.tags,
        ...media.tags,
      ]),
      groups: counts(scoped, ({ media }) => [media.group || ""]),
      kinds: counts(items, ({ media }) => [media.kind || ""]),
    },
    taxonomy: { pageTypes: [], uiElements: [], uxPatterns: [] },
  };
}

export async function listScreens(
  query: ScreenQuery = {},
): Promise<ScreenResponse> {
  return queryScreens(await capturedScreens(), query);
}
