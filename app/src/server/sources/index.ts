import type {
  LibraryDetail,
  LibraryItem,
  LibraryQuery,
  ReferenceMedia,
  ReferenceValue,
  Source,
} from "@/contracts/library";
import { promises as fs } from "node:fs";
import path from "node:path";
import {
  contained,
  imageUrl,
  mediaMime,
  readJson,
  readText,
  referoMedia,
  remoteUrl,
  repoRoot,
} from "./files";

// Source JSON is deliberately accepted at the boundary; only normalized contracts leave this module.
type Raw = Record<string, any>;
const strings = (v: unknown): string[] =>
  Array.isArray(v) ? v.filter((s): s is string => typeof s === "string") : [];
export function parseReferenceId(
  id: string,
): { source: Source; slug: string } | null {
  const match = /^(systems|refero):([a-z0-9][a-z0-9-]*)$/i.exec(id);
  return match
    ? { source: match[1].toLowerCase() as Source, slug: match[2] }
    : null;
}
async function sourceRows(): Promise<{
  systems: Raw[];
  refero: Raw[];
  cdn: string;
}> {
  const [catalog, generated, referoCatalog, referoIndex] = await Promise.all([
    readJson<Raw>("catalog.json"),
    readJson<Raw>("web/data/data.json"),
    readJson<Raw>("refero/catalog.json"),
    readJson<Raw>("web/data/refero/index.json"),
  ]);
  const systems = (catalog?.systems || []).map((s: Raw) => ({
    ...generated?.systems?.find((g: Raw) => g.slug === s.slug),
    ...s,
  }));
  const refero = (referoCatalog?.styles || referoIndex?.styles || []).map(
    (s: Raw) => ({
      ...s,
      ...referoIndex?.styles?.find((g: Raw) => g.slug === s.slug),
    }),
  );
  return {
    systems,
    refero,
    cdn:
      remoteUrl(referoIndex?.cdn) ||
      "https://images.refero.design/styles/refero.design/",
  };
}
async function normalize(
  source: Source,
  row: Raw,
  cdn: string,
): Promise<LibraryItem> {
  const measured = source === "systems";
  const meta =
    !measured && !row.cardRemote
      ? await readJson<Raw>(`refero/${row.slug}/meta.json`)
      : null;
  const cdnUrl = (value: unknown) => {
    try {
      return typeof value === "string"
        ? remoteUrl(new URL(value, cdn).href)
        : null;
    } catch {
      return null;
    }
  };
  const remoteCard =
    cdnUrl(row.cardRemote) || meta?.video_poster_url || meta?.screenshot_url;
  const image = measured
    ? (await imageUrl(row.cover?.thumb)) ||
      (await imageUrl(row.cover?.path)) ||
      (await imageUrl(row.preview?.cover))
    : await referoMedia(
        `/refero-media/${row.card === "s" ? "shots" : "posters"}/${row.slug}.jpg`,
        remoteCard,
      );
  const tags = strings(row.tags);
  return {
    id: `${source}:${row.slug}`,
    source,
    slug: row.slug,
    name: row.name || row.slug,
    description: row.goodFor || row.tagline || "",
    platform:
      row.platform ||
      (measured
        ? tags.find((t) => ["web", "mobile", "desktop"].includes(t)) || "web"
        : "web"),
    themes: strings(row.themes).length
      ? strings(row.themes)
      : row.theme
        ? [row.theme]
        : [],
    tags,
    category:
      row.category || row.industry || row.product_type || row.type || "",
    image,
    icon: measured
      ? await imageUrl(row.preview?.icon || row.icon)
      : await referoMedia(`/refero-media/favicons/${row.slug}.png`, null),
    video:
      !measured && (row.videoRemote || meta?.video_url)
        ? await referoMedia(
            `/refero-media/videos/${row.slug}.mp4`,
            cdnUrl(row.videoRemote) || meta?.video_url,
          )
        : null,
    evidence: measured ? "measured" : "interpreted",
    captured: row.captured || row.extracted_at || null,
  };
}
// A short cache avoids thousands of filesystem lookups on each filter keystroke, while allowing captures to refresh.
let cache: { key: string; until: number; rows: LibraryItem[] } | null = null;
const pendingLoads = new Map<string, Promise<LibraryItem[]>>();
async function allItems(): Promise<LibraryItem[]> {
  const key = [
    repoRoot(),
    process.env.DESIGN_SYSTEMS_MEDIA,
    process.env.DESIGN_SYSTEMS_MEDIA_BASE,
  ].join("|");
  if (cache?.key === key && cache.until > Date.now()) return cache.rows;
  const pending = pendingLoads.get(key);
  if (pending) return pending;
  const load = (async () => {
    const { systems, refero, cdn } = await sourceRows();
    const rows = await Promise.all([
      ...systems.map((row) => normalize("systems", row, cdn)),
      ...refero.map((row) => normalize("refero", row, cdn)),
    ]);
    cache = { key, until: Date.now() + 10_000, rows };
    return rows;
  })();
  pendingLoads.set(key, load);
  try {
    return await load;
  } finally {
    // Rejected loads must release the slot so the next request can retry.
    if (pendingLoads.get(key) === load) pendingLoads.delete(key);
  }
}
export async function listLibrary(
  query: LibraryQuery = {},
): Promise<LibraryItem[]> {
  const words = (query.query || "")
    .trim()
    .toLowerCase()
    .split(/\s+/)
    .filter(Boolean);
  const rows = (await allItems()).filter(
    (item) =>
      (!query.source || item.source === query.source) &&
      (!query.platform || item.platform === query.platform) &&
      (!query.theme || item.themes.includes(query.theme)) &&
      words.every((w) =>
        `${item.name} ${item.slug} ${item.description} ${item.tags.join(" ")} ${item.category}`
          .toLowerCase()
          .includes(w),
      ),
  );
  const offset = Number.isFinite(query.offset)
    ? Math.max(0, Math.floor(query.offset!))
    : 0;
  const limit = Number.isFinite(query.limit)
    ? Math.max(0, Math.floor(query.limit!))
    : rows.length;
  return rows.slice(offset, offset + limit);
}
export async function getSourceStats(): Promise<{
  systems: number;
  refero: number;
}> {
  const rows = await allItems();
  return {
    systems: rows.filter((r) => r.source === "systems").length,
    refero: rows.filter((r) => r.source === "refero").length,
  };
}
// Packages preserve provenance in both legacy source objects and newer evidence fields.
// Derive a label only when a legacy source string states the label explicitly.
function tokenEvidence(extensions: Raw): string | undefined {
  const labels = [
    extensions.evidence,
    extensions.source?.evidence,
    extensions["com.design-systems.evidence"]?.status,
    extensions.status,
  ];
  const explicit = labels.find(
    (label) => typeof label === "string" && label.trim(),
  );
  if (explicit) return explicit;
  if (typeof extensions.source !== "string") return undefined;
  const stated =
    /^(measured|derived|sampled|observed|reconstruction|not captured|not inspected)\b/i.exec(
      extensions.source.trim(),
    );
  if (stated)
    return stated[1][0].toUpperCase() + stated[1].slice(1).toLowerCase();
  return /^estimated from screenshot\b/i.test(extensions.source.trim())
    ? "Sampled"
    : undefined;
}
function flattenTokens(
  node: Raw,
  prefix = "",
  result: (ReferenceValue & { type?: string })[] = [],
): (ReferenceValue & { type?: string })[] {
  if (!node || typeof node !== "object") return result;
  if ("$value" in node) {
    const ext = node.$extensions || {};
    result.push({
      name: prefix,
      value:
        typeof node.$value === "string"
          ? node.$value
          : JSON.stringify(node.$value),
      role: node.$description,
      type: node.$type,
      evidence: tokenEvidence(ext),
    });
  } else
    for (const [key, value] of Object.entries(node))
      if (!key.startsWith("$"))
        flattenTokens(value, prefix ? `${prefix}.${key}` : key, result);
  return result;
}
function resolvedTokens(tokens: Raw): (ReferenceValue & { type?: string })[] {
  const values = flattenTokens(tokens);
  const byName = new Map(values.map((v) => [v.name, v.value]));
  const resolve = (value: string, seen: Set<string>): string =>
    value.replace(/\{([^{}]+)\}/g, (match, alias: string) => {
      if (seen.has(alias) || !byName.has(alias)) return match;
      return resolve(byName.get(alias)!, new Set([...seen, alias]));
    });
  return values.map((v) => ({
    ...v,
    value: resolve(v.value, new Set([v.name])),
  }));
}
async function packageMedia(slug: string, row: Raw): Promise<ReferenceMedia[]> {
  const generated = await readJson<Raw>("web/data/data.json");
  const rich = generated?.systems?.find((s: Raw) => s.slug === slug) || row;
  let shots: Raw[] = [...(rich.screenshots || []), ...(rich.components || [])];
  if (!shots.length) {
    const packageDir = path.join(
      /* turbopackIgnore: true */ repoRoot(),
      "systems",
      slug,
    );
    try {
      const [realRepo, realPackage, screenshots] = await Promise.all([
        fs.realpath(/* turbopackIgnore: true */ repoRoot()),
        fs.realpath(/* turbopackIgnore: true */ packageDir),
        fs.realpath(
          /* turbopackIgnore: true */ path.join(
            /* turbopackIgnore: true */ packageDir,
            "screenshots",
          ),
        ),
      ]);
      if (
        contained(realRepo, realPackage) &&
        contained(realPackage, screenshots)
      ) {
        let directories = 0;
        // Captures may group screenshots under light/dark or screen-specific folders.
        // Ignore symlink entries and cap traversal even in unusually large packages.
        async function walk(
          dir: string,
          relative: string,
          depth: number,
        ): Promise<void> {
          if (depth > 8 || directories >= 100 || shots.length >= 500) return;
          directories++;
          const entries = (
            await fs.readdir(/* turbopackIgnore: true */ dir, {
              withFileTypes: true,
            })
          ).sort((a, b) => (a.name < b.name ? -1 : a.name > b.name ? 1 : 0));
          for (const entry of entries) {
            if (shots.length >= 500) break;
            const nested = relative ? `${relative}/${entry.name}` : entry.name;
            if (entry.isDirectory()) {
              await walk(
                path.join(/* turbopackIgnore: true */ dir, entry.name),
                nested,
                depth + 1,
              );
            } else if (entry.isFile() && mediaMime(entry.name)) {
              shots.push({
                path: `systems/${slug}/screenshots/${nested}`,
                name: nested.replace(/\.[^.]+$/, ""),
                tags: nested
                  .split("/")
                  .filter((part) => part === "light" || part === "dark"),
              });
            }
          }
        }
        await walk(screenshots, "", 0);
      }
    } catch {
      /* No captured screenshots available in this checkout. */
    }
  }
  const media = await Promise.all(
    shots.map(async (shot, i): Promise<ReferenceMedia | null> => {
      const url = (await imageUrl(shot.path)) || (await imageUrl(shot.thumb));
      return url
        ? {
            id: `${slug}-${i}`,
            name: shot.name || path.basename(shot.path),
            url,
            type: /\.(mp4|webm|mov)$/i.test(shot.path) ? "video" : "image",
            tags: strings(shot.tags),
          }
        : null;
    }),
  );
  return media.filter((m): m is ReferenceMedia => !!m);
}
export type ExportFormat =
  "DESIGN.md" | "variables.css" | "theme.css" | "tokens.json";
const formats: ExportFormat[] = [
  "DESIGN.md",
  "variables.css",
  "theme.css",
  "tokens.json",
];
export async function readExport(
  id: string,
  format: string,
): Promise<string | null> {
  const parsed = parseReferenceId(id);
  if (!parsed || !formats.includes(format as ExportFormat)) return null;
  if (!(await allItems()).some((x) => x.id === id)) return null;
  const { source, slug } = parsed;
  if (source === "refero" || format === "DESIGN.md" || format === "tokens.json")
    return readText(`${source}/${slug}/${format}`);
  // Existing catalog exports resolve aliases with the library's own builder.
  if (format === "variables.css")
    return readText(`web/data/export/${slug}.css`);
  return null;
}
async function exportLinks(item: LibraryItem): Promise<Record<string, string>> {
  const links: Record<string, string> = {};
  await Promise.all(
    formats.map(async (format) => {
      if ((await readExport(item.id, format)) !== null)
        links[format] =
          `/api/library/${item.source}/${item.slug}/export?format=${encodeURIComponent(format)}`;
    }),
  );
  return links;
}
export async function getReference(id: string): Promise<LibraryDetail | null> {
  const parsed = parseReferenceId(id);
  if (!parsed) return null;
  const items = await allItems(),
    item = items.find((i) => i.id === id);
  if (!item) return null;
  const { source, slug } = parsed;
  const tokens = (await readJson<Raw>(`${source}/${slug}/tokens.json`)) || {};
  const values = resolvedTokens(tokens);
  let media: ReferenceMedia[] = [],
    descriptionLong = item.description,
    guidelines: string[] = [],
    sourceUrl: string | null = null;
  let colors = values.filter((v) => v.type === "color"),
    typography = values.filter(
      (v) =>
        /font|typography|lineHeight|letterSpacing/i.test(v.type || "") ||
        /typography|fontFamily/.test(v.name),
    );
  let spacing = values.filter((v) =>
      /(^|\.)(spacing|space)(\.|$)/i.test(v.name),
    ),
    radii = values.filter((v) => /radius|radii/.test(v.name));
  const { systems } = await sourceRows();
  if (source === "systems") {
    const row = systems.find((r) => r.slug === slug) || {};
    sourceUrl = remoteUrl(row.url);
    media = await packageMedia(slug, row);
    // Preserve individual evidence labels. Package-level "measured" describes the capture source, not every value.
    const readme = await readText(`systems/${slug}/README.md`);
    if (readme)
      guidelines = readme
        .split("\n")
        .filter((line) => /^[-*] /.test(line))
        .slice(0, 12)
        .map((line) => line.replace(/^[-*] /, ""));
  } else {
    const [meta, entity, ds] = await Promise.all([
      readJson<Raw>(`refero/${slug}/meta.json`),
      readJson<Raw>(`web/data/refero/style/${slug}.json`),
      readJson<Raw>(`refero/${slug}/design-system.json`),
    ]);
    const design = ds || entity?.ds || {};
    sourceUrl = remoteUrl(meta?.source_url || entity?.source_url);
    descriptionLong = design.description || item.description;
    const candidates = entity?.media || {
      shot: {
        local: `/refero-media/shots/${slug}.jpg`,
        remote: meta?.screenshot_url,
      },
      video: {
        local: `/refero-media/videos/${slug}.mp4`,
        remote: meta?.video_url,
      },
      detail: {
        local: `/refero-media/detail/${slug}.mp4`,
        remote: meta?.video_detail_url,
      },
    };
    for (const [key, value] of Object.entries(candidates) as [string, Raw][]) {
      if (!value || ["favicon", "poster", "detail_poster"].includes(key))
        continue;
      const url = await referoMedia(value.local, value.remote);
      if (url)
        media.push({
          id: key,
          name:
            key === "shot"
              ? "Full page"
              : key === "detail"
                ? "Detail recording"
                : "Page recording",
          url,
          type: ["video", "detail"].includes(key) ? "video" : "image",
          tags: [],
        });
    }
    if (Array.isArray(design.colors))
      colors = design.colors
        .filter((c: Raw) => c.hex)
        .map((c: Raw) => ({
          name: c.name || c.hex,
          value: c.hex,
          role: c.role,
          evidence: "interpreted",
        }));
    if (Array.isArray(design.typography))
      typography = design.typography.map((t: Raw) => ({
        name: t.family || "Typeface",
        value: t.family || "",
        role: t.role,
        evidence: "interpreted",
      }));
    if (design.spacing) {
      spacing = Object.entries(design.spacing)
        .filter(
          ([key, v]) =>
            !["radius", "density"].includes(key) && typeof v === "string",
        )
        .map(([name, value]) => ({
          name,
          value: String(value),
          evidence: "interpreted",
        }));
      radii = Object.entries(design.spacing.radius || {}).map(
        ([name, value]) => ({
          name,
          value: String(value),
          evidence: "interpreted",
        }),
      );
    }
    guidelines = strings(design.dos || design.do).concat(
      strings(design.donts || design.dont).map((s) => `Avoid: ${s}`),
    );
  }
  return {
    ...item,
    sourceUrl,
    media,
    colors,
    typography,
    spacing,
    radii,
    descriptionLong,
    guidelines,
    exports: await exportLinks(item),
    related: items
      .filter(
        (i) =>
          i.id !== id &&
          i.source === source &&
          (i.category === item.category ||
            i.tags.some((t) => item.tags.includes(t))),
      )
      .slice(0, 6),
  };
}

export async function readReferenceImage(
  reference: LibraryDetail,
): Promise<{ data: Uint8Array; mediaType: string } | null> {
  const { readLocalImage } = await import("./files");
  for (const media of reference.media
    .filter((m) => m.type === "image")
    .slice(0, 8)) {
    const result = await readLocalImage(media.url);
    if (result) return result;
  }
  return reference.image ? readLocalImage(reference.image) : null;
}
