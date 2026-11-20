import { withReferenceCategories } from "@/server/taxonomy/library";
import { matchesCategory } from "@/contracts/categories";
import type {
  LibraryDetail,
  LibraryItem,
  LibraryQuery,
  ReferenceMedia,
  MeasuredPackageDetail,
  InterpretedStyleDetail,
  ReferenceValue,
  Source,
} from "@/contracts/library";
import { promises as fs } from "node:fs";
import path from "node:path";
import { readStyleExport, type ExportVariant } from "./style-exports";
import { parseJson, pyJsonStringify } from "./pyjson";
import { hasUnresolved, tokenHex, tokenLeaves, tokenResolver } from "./tokens";
import {
  contained,
  imageUrl,
  mediaMime,
  readJson,
  readText,
  hasFile,
  referoMedia,
  remoteUrl,
  repoRoot,
  listPackageDocuments,
  readPackageDocument,
  mediaRoot,
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
type SourceRows = {
  systems: Map<string, Raw>;
  refero: Map<string, Raw>;
  cdn: string;
};
const bySlug = (rows: unknown): Map<string, Raw> =>
  new Map(
    (Array.isArray(rows) ? rows : [])
      .filter((row: Raw) => typeof row?.slug === "string")
      .map((row: Raw) => [row.slug, row]),
  );
async function readSourceRows(): Promise<SourceRows> {
  const [catalog, generated, referoCatalog, referoIndex] = await Promise.all([
    readJson<Raw>("catalog.json"),
    readJson<Raw>("web/data/data.json"),
    readJson<Raw>("refero/catalog.json"),
    readJson<Raw>("web/data/refero/index.json"),
  ]);
  const generatedSystems = bySlug(generated?.systems),
    referoGenerated = bySlug(referoIndex?.styles);
  const systems = (catalog?.systems || []).map((s: Raw) => ({
    ...generatedSystems.get(s.slug),
    ...s,
  }));
  const refero = (referoCatalog?.styles || referoIndex?.styles || []).map(
    (s: Raw) => ({ ...s, ...referoGenerated.get(s.slug) }),
  );
  return {
    systems: bySlug(systems),
    refero: bySlug(refero),
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
    imageFallback: measured
      ? await imageUrl(row.cover?.path || row.preview?.cover)
      : remoteUrl(remoteCard),
    videoFallback: measured
      ? null
      : cdnUrl(row.videoRemote) || remoteUrl(meta?.video_url),
    // Only the favicon Refero recorded. A favicon service fallback would tell
    // that service which private library entries are being browsed.
    iconFallback: measured ? null : remoteUrl(meta?.favicon_url),
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
    productType: row.product_type || row.type || null,
    designStyle: row.design_style || row.style || null,
    industry: row.industry || null,
    sourceUrl: remoteUrl(row.url || row.source_url || meta?.source_url),
    fonts: measured
      ? (row.fonts || []).map((f: Raw) => f.family).filter(Boolean)
      : [],
    previewFrames: measured
      ? (
          await Promise.all(
            (row.screenshots || [])
              .slice(0, 8)
              .map((shot: Raw) => imageUrl(shot.thumb || shot.path)),
          )
        ).filter((url): url is string => !!url)
      : [],
  };
}
// Normalizing every row costs thousands of filesystem lookups, so the rows stay
// cached until a catalog, generated index or media folder changes. A few stats
// per call notice a capture, a `catalog.py build` or a media mirror run; the
// age limit catches a file hydrated in place (an LFS pull) that changes none.
const STAMP_FILES = [
  "catalog.json",
  "web/data/data.json",
  "refero/catalog.json",
  "web/data/refero/index.json",
  "web/data/thumbs",
];
const MEDIA_FOLDERS = ["shots", "posters", "favicons", "videos"];
export const MAX_CACHE_AGE = 5 * 60_000;
/** Changes when the catalogs, generated data or media mirror change. */
export async function sourceStamp(): Promise<string> {
  const root = repoRoot(),
    media = mediaRoot();
  const stats = await Promise.all(
    [
      ...STAMP_FILES.map((file) =>
        path.join(/* turbopackIgnore: true */ root, file),
      ),
      ...MEDIA_FOLDERS.map((dir) =>
        path.join(/* turbopackIgnore: true */ media, dir),
      ),
    ].map((file) =>
      fs.stat(/* turbopackIgnore: true */ file).then(
        (stat) => `${stat.mtimeMs}:${stat.size}`,
        () => "-",
      ),
    ),
  );
  return [root, media, process.env.DESIGN_SYSTEMS_MEDIA_BASE, ...stats].join(
    "|",
  );
}
type Loaded = SourceRows & {
  items: LibraryItem[];
  byId: Map<string, LibraryItem>;
};
let cache: { key: string; loadedAt: number; value: Loaded } | null = null;
const pendingLoads = new Map<string, Promise<Loaded>>();
async function loadSources(): Promise<Loaded> {
  const key = await sourceStamp();
  if (cache?.key === key && Date.now() - cache.loadedAt < MAX_CACHE_AGE)
    return cache.value;
  const pending = pendingLoads.get(key);
  if (pending) return pending;
  const load = (async () => {
    const rows = await readSourceRows();
    const items = await Promise.all([
      ...[...rows.systems.values()].map((row) =>
        normalize("systems", row, rows.cdn),
      ),
      ...[...rows.refero.values()].map((row) =>
        normalize("refero", row, rows.cdn),
      ),
    ]);
    const value = {
      ...rows,
      items,
      byId: new Map(items.map((item) => [item.id, item])),
    };
    cache = { key, loadedAt: Date.now(), value };
    return value;
  })();
  pendingLoads.set(key, load);
  try {
    return await load;
  } finally {
    // Rejected loads must release the slot so the next request can retry.
    if (pendingLoads.get(key) === load) pendingLoads.delete(key);
  }
}
async function allItems(): Promise<LibraryItem[]> {
  return (await loadSources()).items;
}
export async function listLibrary(
  query: LibraryQuery = {},
): Promise<LibraryItem[]> {
  const words = (query.query || "")
    .trim()
    .toLowerCase()
    .split(/\s+/)
    .filter(Boolean);
  const rows = (await withReferenceCategories(await allItems())).filter(
    (item) =>
      (!query.source || item.source === query.source) &&
      (!query.platform || item.platform === query.platform) &&
      (!query.theme ||
        item.themes.some(
          (theme) =>
            theme === query.theme || theme.startsWith(`${query.theme}-`),
        )) &&
      (!query.category || matchesCategory(item, query.category)) &&
      (!query.productType || item.productType === query.productType) &&
      (!query.designStyle || item.designStyle === query.designStyle) &&
      (!query.industry || item.industry === query.industry) &&
      (!query.tag || item.tags.includes(query.tag)) &&
      words.every((w) =>
        `${item.name} ${item.slug} ${item.description} ${item.tags.join(" ")} ${item.category} ${(item.categories || []).map((term) => term.label).join(" ")} ${item.themes.join(" ")} ${(item.fonts || []).join(" ")} ${item.productType || ""} ${item.designStyle || ""} ${item.industry || ""}`
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
function displayValue(value: unknown): string {
  if (typeof value === "string") return value;
  const hex = tokenHex(value);
  if (hex) return hex;
  // A list is a font stack or an easing, shown the way catalog.py looks it up.
  if (Array.isArray(value)) return value.map(String).join(", ");
  return pyJsonStringify(value);
}
// Aliases resolve inside the token's own set, then `core`, then the root, and
// legacy `value` leaves read like `$value` ones, matching tools/catalog.py.
function resolvedTokens(tokens: Raw): (ReferenceValue & { type?: string })[] {
  const leaves = tokenLeaves(tokens),
    resolver = tokenResolver(leaves);
  return leaves.map((leaf) => {
    const resolved = resolver.final(leaf.name);
    return {
      name: leaf.name,
      value: displayValue(hasUnresolved(resolved) ? leaf.value : resolved),
      role: leaf.description,
      type: leaf.type,
      evidence: tokenEvidence(leaf.extensions || {}),
    };
  });
}
async function scanPackageMedia(
  slug: string,
  folder: string,
  kind: "screenshot" | "crop" | "icon" | "board",
): Promise<Raw[]> {
  const dir = path.join(
    /* turbopackIgnore: true */ repoRoot(),
    "systems",
    slug,
  );
  const out: Raw[] = [];
  try {
    const [realRepo, realPackage, realFolder] = await Promise.all([
      fs.realpath(/* turbopackIgnore: true */ repoRoot()),
      fs.realpath(/* turbopackIgnore: true */ dir),
      fs.realpath(/* turbopackIgnore: true */ path.join(dir, folder)),
    ]);
    if (
      !contained(realRepo, realPackage) ||
      !contained(realPackage, realFolder)
    )
      return [];
    async function walk(relative: string, depth: number): Promise<void> {
      if (depth > 12 || out.length > 20_000) return;
      const entries = (
        await fs.readdir(
          path.join(/* turbopackIgnore: true */ realFolder, relative),
          { withFileTypes: true },
        )
      ).sort((a, b) => (a.name < b.name ? -1 : a.name > b.name ? 1 : 0));
      for (const entry of entries) {
        const nested = relative ? `${relative}/${entry.name}` : entry.name;
        if (entry.isDirectory() && !entry.name.startsWith("."))
          await walk(nested, depth + 1);
        else if (entry.isFile() && mediaMime(entry.name))
          out.push({
            path: `systems/${slug}/${folder}/${nested}`,
            name: nested.replace(/\.[^.]+$/, ""),
            kind,
            group: relative ? `${folder}/${relative}` : folder,
            tags: [
              ...new Set(
                nested
                  .split(/[\/_.-]/)
                  .filter((part) => ["light", "dark", "mobile"].includes(part)),
              ),
            ],
          });
      }
    }
    await walk("", 0);
  } catch {
    /* This package has no directory for this media kind. */
  }
  return out;
}
async function packageMedia(
  slug: string,
  row: Raw,
  capturesOnly = false,
): Promise<ReferenceMedia[]> {
  const screenshots: Raw[] = row.screenshots?.length
    ? row.screenshots
    : await scanPackageMedia(slug, "screenshots", "screenshot");
  const crops: Raw[] = row.components?.length
    ? row.components
    : await scanPackageMedia(slug, "components", "crop");
  // The generated icon preview is capped. Enumerate the canonical icon directory.
  const [icons, boards] = capturesOnly
    ? [[], []]
    : await Promise.all([
        scanPackageMedia(slug, "icons", "icon"),
        scanPackageMedia(slug, "boards", "board"),
      ]);
  const shots: Raw[] = [
    ...screenshots.map((s) => ({ ...s, kind: "screenshot" as const })),
    ...crops.map((s) => ({ ...s, kind: "crop" as const })),
    ...icons,
    ...boards,
  ];
  const media = await Promise.all(
    shots.map(async (shot): Promise<ReferenceMedia | null> => {
      // Require the original to be a valid hydrated package asset. Thumbnails never
      // substitute for the original identity or allow reads outside this package.
      if (
        typeof shot.path !== "string" ||
        !shot.path.startsWith(`systems/${slug}/`)
      )
        return null;
      const url = await imageUrl(shot.path);
      if (!url) return null;
      return {
        id: shot.path,
        path: shot.path,
        kind: shot.kind,
        name: shot.name || path.basename(shot.path),
        url,
        thumbnail: await imageUrl(shot.thumb),
        group: shot.group || "",
        type: /\.(mp4|webm|mov)$/i.test(shot.path) ? "video" : "image",
        tags: strings(shot.tags),
      };
    }),
  );
  return media.filter((m): m is ReferenceMedia => !!m);
}
/** Captured media metadata without reading tokens, documents or related styles. */
export async function listCapturedMedia(): Promise<
  { reference: LibraryItem; media: ReferenceMedia[] }[]
> {
  const { items, systems } = await loadSources();
  const result: { reference: LibraryItem; media: ReferenceMedia[] }[] = [];
  // Keep original-file verification bounded to one package at a time.
  for (const reference of items.filter((item) => item.source === "systems")) {
    const row = systems.get(reference.slug) || {};
    result.push({
      reference,
      media: await packageMedia(reference.slug, row, true),
    });
  }
  return result;
}
function packageRelative(
  slug: string,
  value: unknown,
  fallback: string,
): string {
  if (typeof value !== "string") return fallback;
  return value.replace(new RegExp(`^systems/${slug}/`), "");
}
async function measuredDetail(
  slug: string,
  row: Raw,
  media: ReferenceMedia[],
): Promise<MeasuredPackageDetail> {
  const id = `systems:${slug}`;
  const readmePath = packageRelative(slug, row.entry, "README.md");
  const [documents, readme, guide] = await Promise.all([
    listPackageDocuments(id),
    readPackageDocument(id, readmePath),
    readPackageDocument(
      id,
      packageRelative(slug, row.styleGuide, "style-guide.html"),
    ),
  ]);
  const icons = media.filter((m) => m.kind === "icon");
  return {
    screenshots: media.filter((m) => m.kind === "screenshot"),
    crops: media.filter((m) => m.kind === "crop"),
    icons,
    boards: media.filter((m) => m.kind === "board"),
    iconTotal: icons.length,
    documents,
    readme: readme?.text || "",
    readmePath,
    styleGuide: guide
      ? `/api/packages/${slug}/guide/${guide.path.split("/").map(encodeURIComponent).join("/")}`
      : null,
    capture: row.capture || null,
    widths: Array.isArray(row.widths)
      ? row.widths
          .filter(
            (value: unknown) =>
              typeof value === "string" || typeof value === "number",
          )
          .map(String)
      : [],
    access: row.access || "",
    notes: row.notes || "",
    tokenTheme: row.tokenTheme || row.themes?.[0] || "light",
    swatches: row.swatches || {},
    fonts: row.fonts || [],
    typeStyles: row.typeStyles || [],
    spacing: row.spacing || [],
    radii: row.radii || [],
    shadows: row.shadows || [],
    omitted: row.omitted || {},
    layoutGaps: row.layoutGaps || {},
  };
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
  variant?: ExportVariant,
): Promise<string | null> {
  const parsed = parseReferenceId(id);
  if (!parsed || !formats.includes(format as ExportFormat)) return null;
  if (!(await loadSources()).byId.has(id)) return null;
  const { source, slug } = parsed;
  if (variant) {
    if (source !== "refero") return null;
    return readStyleExport(slug, format as ExportFormat, variant);
  }
  const file = exportFile(source, slug, format as ExportFormat);
  return file ? readText(file) : null;
}
function exportFile(
  source: string,
  slug: string,
  format: ExportFormat,
): string | null {
  if (source === "refero" || format === "DESIGN.md" || format === "tokens.json")
    return `${source}/${slug}/${format}`;
  // Existing catalog exports resolve aliases with the library's own builder.
  if (format === "variables.css") return `web/data/export/${slug}.css`;
  return null;
}
// Existence only: reading every export to test for it read whole files.
async function exportLinks(item: LibraryItem): Promise<Record<string, string>> {
  const links: Record<string, string> = {};
  await Promise.all(
    formats.map(async (format) => {
      const file = exportFile(item.source, item.slug, format);
      if (file && (await hasFile(file)))
        links[format] =
          `/api/library/${item.source}/${item.slug}/export?format=${encodeURIComponent(format)}`;
    }),
  );
  return links;
}
/** A Refero style's recordings and stills, local mirror first. */
async function referoStyleMedia(
  slug: string,
  meta: Raw | null,
  entity: Raw | null,
): Promise<ReferenceMedia[]> {
  const media: ReferenceMedia[] = [];
  const listed: Record<string, Raw> = entity?.media || {
    shot: {
      local: `/refero-media/shots/${slug}.jpg`,
      remote: meta?.screenshot_url,
    },
    poster: {
      local: `/refero-media/posters/${slug}.jpg`,
      remote: meta?.video_poster_url,
    },
    video: {
      local: `/refero-media/videos/${slug}.mp4`,
      remote: meta?.video_url,
    },
    detail: {
      local: `/refero-media/detail/${slug}.mp4`,
      remote: meta?.video_detail_url,
    },
    detail_poster: {
      local: `/refero-media/detail-posters/${slug}.jpg`,
      remote: meta?.video_detail_poster_url,
    },
    favicon: {
      local: `/refero-media/favicons/${slug}.png`,
      remote: meta?.favicon_url,
    },
  };
  // tools/catalog.py's generated media point a favicon's remote at a favicon
  // service, which would learn the style being browsed. Keep only the one
  // Refero recorded.
  const candidates: Record<string, Raw> = listed.favicon
    ? { ...listed, favicon: { ...listed.favicon, remote: meta?.favicon_url } }
    : listed;
  const labels: Record<string, string> = {
    shot: "Full page",
    poster: "Page recording poster",
    video: "Page recording",
    detail: "Detail recording",
    detail_poster: "Detail recording poster",
    favicon: "Favicon",
  };
  for (const key of [
    "shot",
    "poster",
    "video",
    "detail",
    "detail_poster",
    "favicon",
  ] as const) {
    const value = candidates[key];
    if (!value) continue;
    const url = await referoMedia(value.local, value.remote);
    if (!url) continue;
    const poster = candidates[key === "detail" ? "detail_poster" : "poster"];
    media.push({
      id: key,
      kind: key,
      name: labels[key],
      url,
      path: value.local,
      group: "refero",
      type: ["video", "detail"].includes(key) ? "video" : "image",
      tags: [],
      fallback: remoteUrl(value.remote),
      poster:
        ["video", "detail"].includes(key) && poster
          ? await referoMedia(poster.local, poster.remote)
          : null,
    });
  }
  return media;
}
/** The library card for one reference, without reading its package. */
export async function getReferenceSummary(
  id: string,
): Promise<LibraryItem | null> {
  if (!parseReferenceId(id)) return null;
  const item = (await loadSources()).byId.get(id);
  return item ? (await withReferenceCategories([item]))[0] : null;
}
/** One reference's media without tokens, documents or related styles. */
export async function getReferenceMedia(
  id: string,
): Promise<{ reference: LibraryItem; media: ReferenceMedia[] } | null> {
  const parsed = parseReferenceId(id);
  const reference = await getReferenceSummary(id);
  if (!parsed || !reference) return null;
  const { slug } = parsed;
  if (parsed.source === "systems")
    return {
      reference,
      media: await packageMedia(
        slug,
        (await loadSources()).systems.get(slug) || {},
      ),
    };
  const [meta, entity] = await Promise.all([
    readJson<Raw>(`refero/${slug}/meta.json`),
    readJson<Raw>(`web/data/refero/style/${slug}.json`),
  ]);
  return {
    reference,
    media: await referoStyleMedia(slug, meta, entity),
  };
}
export async function getReference(id: string): Promise<LibraryDetail | null> {
  const parsed = parseReferenceId(id);
  if (!parsed) return null;
  // Only same-source references can be related, so only they need categories.
  const items = await withReferenceCategories(
      (await allItems()).filter((i) => i.source === parsed.source),
    ),
    item = items.find((i) => i.id === id);
  if (!item) return null;
  const { source, slug } = parsed;
  // Parsed so a float written `1.0` prints as Python prints it.
  const tokenText = await readText(`${source}/${slug}/tokens.json`);
  let tokens: Raw = {};
  try {
    tokens = (tokenText && (parseJson(tokenText) as Raw)) || {};
  } catch {}
  const values = resolvedTokens(tokens);
  let media: ReferenceMedia[] = [],
    descriptionLong = item.description,
    guidelines: string[] = [],
    sourceUrl: string | null = null;
  let measured: MeasuredPackageDetail | undefined;
  let interpreted: InterpretedStyleDetail | undefined;
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
  const { systems, refero } = await loadSources();
  if (source === "systems") {
    const row = systems.get(slug) || {};
    sourceUrl = remoteUrl(row.url);
    media = await packageMedia(slug, row);
    measured = await measuredDetail(slug, row, media);
    // Preserve individual evidence labels. Package-level "measured" describes the capture source, not every value.
    // measuredDetail has usually read the README already.
    const readme =
      measured.readmePath === "README.md" && measured.readme
        ? measured.readme
        : await readText(`systems/${slug}/README.md`);
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
    media = await referoStyleMedia(slug, meta, entity);
    const row = refero.get(slug) || {};
    const similar = entity?.similar || design.similar || [];
    interpreted = {
      designSystem: design,
      pageUrl: remoteUrl(meta?.page_url || entity?.page_url || row.page_url),
      sourceUrl,
      productType: item.productType || entity?.type || null,
      designStyle: item.designStyle || entity?.style || null,
      industry: item.industry || entity?.industry || null,
      tags: item.tags,
      theme: item.themes[0] || null,
      similar: Array.isArray(similar)
        ? similar.map((r: Raw) => {
            const name =
              typeof r.name === "string"
                ? r.name
                : typeof r.business === "string"
                  ? r.business
                  : null;
            const match = items.find(
              (candidate) =>
                candidate.source === "refero" &&
                (candidate.slug === r.slug ||
                  (name &&
                    candidate.name.toLowerCase() === name.toLowerCase())),
            );
            return {
              slug: match?.slug || null,
              name,
              why: typeof r.why === "string" ? r.why : null,
            };
          })
        : [],
    };
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
    measured,
    interpreted,
    media,
    colors,
    typography,
    spacing,
    radii,
    descriptionLong,
    guidelines,
    exports: await exportLinks(item),
    related: items
      .filter((i) => i.id !== id && i.source === source)
      .map((candidate) => ({
        candidate,
        score:
          (candidate.category === item.category ? 2 : 0) +
          (candidate.productType && candidate.productType === item.productType
            ? 3
            : 0) +
          (candidate.designStyle && candidate.designStyle === item.designStyle
            ? 3
            : 0) +
          candidate.tags.filter((tag) => item.tags.includes(tag)).length +
          (candidate.themes.some((theme) => item.themes.includes(theme))
            ? 1
            : 0),
      }))
      .filter(({ score }) => score > 0)
      .sort(
        (a, b) =>
          b.score - a.score || a.candidate.name.localeCompare(b.candidate.name),
      )
      .slice(0, 6)
      .map(({ candidate }) => candidate),
  };
}

/** The first readable captured image; `read` lets a caller reuse its own reads. */
export async function readReferenceImage(
  reference: LibraryDetail,
  read?: (
    url: string,
  ) => Promise<{ data: Uint8Array; mediaType: string } | null>,
): Promise<{ data: Uint8Array; mediaType: string } | null> {
  const readImage = read || (await import("./files")).readLocalImage;
  for (const media of reference.media
    .filter((m) => m.type === "image")
    .slice(0, 8)) {
    const result = await readImage(media.url);
    if (result) return result;
  }
  return reference.image ? readImage(reference.image) : null;
}
