// The tool layer behind the gallery chat, ported from server/library.py
// plus the tools/catalog.py helpers it calls (load_catalog, find, swatches,
// export_tokens, repo_file, Resolver). Every tool returns a JSON-able object.
//
// Two differences from the Python, both data-source swaps the caller asked for:
// the refero store reads the prebuilt JSON index under web/data/refero/
// instead of refero.db's sqlite, and view_media falls back to a prebuilt
// web/data/thumbs/ thumbnail instead of a Pillow downscale. Site-relative
// media URLs are "/media/<repo-relative>" for the app's media route.
import { promises as fs, realpathSync } from "node:fs";
import path from "node:path";
// The checkout comes from the one resolver every server route uses, so
// DESIGN_SYSTEMS_REPO points the tools at the same tree as /media/ and docs.
import { ROOT } from "../repo.ts";

export { ROOT };

type Obj = Record<string, unknown>;

// The checkout with symlinks resolved, as Python's ROOT.resolve(): every
// containment check and every repo-relative URL is computed from real paths.
const REAL_ROOT = (() => {
  try {
    return realpathSync(ROOT);
  } catch {
    return path.resolve(ROOT);
  }
})();

const REFERO_DIR = path.join(ROOT, "web", "data", "refero");
const REFERO_INDEX = path.join(REFERO_DIR, "index.json");
const THUMBS_DIR = path.join(ROOT, "web", "data", "thumbs");

const IMAGE_TYPES: Record<string, string> = {
  ".png": "image/png",
  ".jpg": "image/jpeg",
  ".jpeg": "image/jpeg",
  ".webp": "image/webp",
  ".gif": "image/gif",
};
const TEXT_TYPES = new Set([".md", ".txt", ".json", ".css", ".html", ".svg", ".csv"]);
const MEDIA_DIRS = ["screenshots", "components", "icons", "boards"] as const;
// Package paths the tools never read, matching the research app's package
// document rules (app/src/server/sources/files.ts) and the package entries in
// .gitignore: raw captures, fonts, dependency and capture-scratch folders, and
// any dot segment.
const PRIVATE_DIRS = new Set(["raw", "fonts", "node_modules", "__pycache__"]);
const PRIVATE_PREFIXES = ["tools/capture/dumps/", "tools/capture/out/", "tools/capture/winid"];

// A tool result's JSON text is capped before it goes back to the model: a whole
// token group or a README can run past what a turn should carry.
// Sizes are UTF-8 bytes of compact JSON, measured the same way in the Python.
export const RESULT_CAP = 32_000;
export const DOC_CAP = 24_000;
export const TOKEN_PAGE = RESULT_CAP - 1_000; // bytes of name/value pairs one get_tokens page carries
// How a handoff prompt names the library's checkout.
const HOME_VAR = "$DESIGN_SYSTEMS_HOME";
export const IMAGE_CAP = 3_500_000; // bytes on disk

export class ToolError extends Error {
  // A tool's readable failure, returned to the model as its result text.
}

// UTF-8 bytes of obj as compact JSON: _json_size() in server/library.py.
const jsonSize = (obj: unknown): number => Buffer.byteLength(JSON.stringify(obj) ?? "", "utf8");

const isObj = (v: unknown): v is Obj => typeof v === "object" && v !== null && !Array.isArray(v);
const asStr = (v: unknown): string => (v == null ? "" : String(v));
const optStr = (v: unknown): string | null => (v == null ? null : String(v));
const asArr = (v: unknown): unknown[] => (Array.isArray(v) ? v : []);
const cmpStr = (a: string, b: string) => (a < b ? -1 : a > b ? 1 : 0);
const inside = (target: string, dir: string): boolean => {
  const rel = path.relative(dir, target);
  return rel === "" || (!rel.startsWith("..") && !path.isAbsolute(rel));
};
const asInt = (v: unknown): number => {
  // Mirrors int(): floats truncate, non-numeric raises a ToolError the caller reads.
  if (typeof v === "number" && Number.isFinite(v)) return Math.trunc(v);
  const n = Number(String(v).trim());
  if (!Number.isFinite(n)) throw new ToolError(`invalid int: ${String(v).slice(0, 80)}`);
  return Math.trunc(n);
};

// ------------------------------------------------------------ catalog helpers

async function loadCatalog(): Promise<Obj> {
  return JSON.parse(await fs.readFile(path.join(ROOT, "catalog.json"), "utf8")) as Obj;
}

async function entry(slug: string): Promise<Obj> {
  const cat = await loadCatalog();
  for (const s of asArr(cat.systems)) if (isObj(s) && s.slug === slug) return s;
  throw new ToolError(`no systems package '${slug}'`);
}

async function realOr(p: string): Promise<string> {
  // The real path, or the lexical one when it does not exist (resolve(strict=False)).
  return fs.realpath(p).catch(() => path.resolve(p));
}

const pkgDir = (e: Obj): Promise<string> => realOr(path.resolve(REAL_ROOT, "systems", asStr(e.slug)));

function privatePath(rel: string): boolean {
  // True for a package-relative path the tools must not read.
  if (rel === "" || rel === ".") return false;
  const parts = rel.split("/");
  return (
    parts.some((p) => p.startsWith(".") || PRIVATE_DIRS.has(p)) ||
    PRIVATE_PREFIXES.some((pre) => rel === pre.replace(/\/$/, "") || rel.startsWith(pre))
  );
}

// Mirrors catalog.py's REPO_PATHS: request prefixes answered from the checkout.
const REPO_PATHS = ["/systems/", "/tools/", "/catalog.json", "/README.md"];

async function repoFile(urlPath: string): Promise<string | null> {
  // The path is unquoted and normalised before the prefix check, so `..`
  // segments (plain or percent-encoded) can never climb out of the allowed
  // folders, and the real file must still sit inside the checkout, so a
  // symlink cannot either.
  const raw = urlPath.split("?")[0].split("#")[0];
  let clean = raw;
  try {
    clean = decodeURIComponent(raw);
  } catch {
    // unquote() never fails; a bad % sequence stays literal.
  }
  const norm = path.posix.normalize(clean);
  if (!REPO_PATHS.some((p) => norm === p.replace(/\/+$/, "") || norm.startsWith(p))) return null;
  const target = await realOr(path.resolve(REAL_ROOT, norm.replace(/^\/+/, "")));
  const allowed = await Promise.all(REPO_PATHS.map((p) => realOr(path.resolve(REAL_ROOT, p.replace(/^\/+|\/+$/g, "")))));
  if (!allowed.some((a) => target === a || inside(target, a))) return null;
  return target;
}

async function repoFileRequired(rel: string): Promise<string> {
  const target = await repoFile("/" + rel.replace(/^\/+/, ""));
  if (target === null) throw new ToolError(`path outside the served set: ${rel}`);
  return target;
}

async function bounded(e: Obj, rel: string): Promise<string> {
  // Resolve a package-relative path, refusing anything that climbs out.
  // Accepts the repo-relative and site-absolute forms other tools emit, and
  // the /media/ URL list_media returns (percent-decoded), so the model can pass
  // a path it saw verbatim. Containment is checked on the real path, so a
  // symlink inside the package cannot point out of it, and private folders
  // (raw/, fonts/, dot paths) are refused under either name.
  const base = await pkgDir(e);
  const slug = asStr(e.slug);
  let raw = rel;
  if (raw.replace(/^\/+/, "").startsWith("media/")) {
    raw = raw.split("?")[0].split("#")[0];
    try {
      raw = decodeURIComponent(raw);
    } catch {
      // unquote() never fails; a bad % sequence stays literal.
    }
  }
  let clean = path.posix.normalize("/" + raw.replace(/^\/+/, "")).replace(/^\/+/, "");
  for (const prefix of [`media/systems/${slug}/`, `systems/${slug}/`])
    if (clean.startsWith(prefix)) {
      clean = clean.slice(prefix.length);
      break;
    }
  const target = await realOr(path.resolve(base, clean));
  if (target !== base && !inside(target, base)) throw new ToolError(`path leaves the package: ${rel}`);
  const real = path.relative(base, target).split(path.sep).join("/");
  if (privatePath(path.posix.normalize(clean)) || privatePath(real))
    throw new ToolError(`not readable through the tools: ${rel}`);
  return target;
}

const mediaUrl = (p: string): string => {
  const rel = path.relative(REAL_ROOT, path.resolve(p));
  return "/media/" + rel.split(path.sep).map(encodeURIComponent).join("/");
};

// ------------------------------------------------------- catalog.py token port

function flatten(tokens: unknown): Obj {
  // Map dotted paths to raw values. Reads DTCG ($value) and Tokens Studio (value).
  const flat: Obj = {};
  const walk = (node: unknown, parts: string[]) => {
    if (!isObj(node)) return;
    if (Object.hasOwn(node, "$value")) {
      flat[parts.join(".")] = node.$value;
      return;
    }
    if (Object.hasOwn(node, "value") && !isObj(node.value)) {
      flat[parts.join(".")] = node.value;
      return;
    }
    for (const [key, child] of Object.entries(node)) if (!key.startsWith("$")) walk(child, [...parts, key]);
  };
  walk(tokens, []);
  return flat;
}

// Python's round() is banker's rounding; token components land on .5 rarely,
// but matching it keeps hex output identical to tools/catalog.py.
const pyRound = (x: number): number => {
  const f = Math.floor(x);
  const d = x - f;
  return d > 0.5 ? f + 1 : d < 0.5 ? f : f % 2 === 0 ? f : f + 1;
};

function hexOf(value: unknown): string | null {
  // DTCG 2025 colour objects carry components, not a string.
  if (isObj(value) && "components" in value) {
    if (value.hex) return asStr(value.hex);
    const comps = asArr(value.components).slice(0, 3);
    if (comps.length < 3) return null;
    const [r, g, b] = comps.map((c) => pyRound(Number(c) * 255));
    const alpha = typeof value.alpha === "number" ? value.alpha : 1;
    const h = [r, g, b].map((c) => c.toString(16).padStart(2, "0")).join("");
    return `#${h}` + (alpha === 1 ? "" : pyRound(alpha * 255).toString(16).padStart(2, "0"));
  }
  return null;
}

class Resolver {
  // Resolves {alias} references the way Tokens Studio does with every set
  // active: first inside the token's own set, then in `core`, then from root.
  flat: Obj;
  constructor(tokens: unknown) {
    this.flat = flatten(tokens);
  }
  lookup(p: string, depth = 0): unknown {
    if (!Object.hasOwn(this.flat, p)) return null;
    return this.resolve(this.flat[p], p.split(".")[0], depth);
  }
  private resolve(value: unknown, setName: string, depth: number): unknown {
    if (depth > 12) return null;
    const asHex = hexOf(value);
    if (asHex) return asHex;
    if (Array.isArray(value)) return value.map((v) => String(v)).join(", ");
    if (typeof value !== "string") return value;
    const m = /^\{([^}]+)\}$/.exec(value.trim());
    if (!m) return value;
    const ref = m[1];
    for (const cand of [`${setName}.${ref}`, `core.${ref}`, ref])
      if (Object.hasOwn(this.flat, cand)) return this.lookup(cand, depth + 1);
    return null;
  }
  final(p: string, depth = 0, theme: string | null = null): unknown {
    // The raw value at `p` with every alias resolved, including aliases inside
    // lists and objects. `theme` is a set to try after the token's own one, for
    // shared tokens in `core` that point at a theme's colours.
    if (!Object.hasOwn(this.flat, p)) return null;
    return this.deep(this.flat[p], p.split(".")[0], depth, theme);
  }
  private deep(value: unknown, setName: string, depth: number, theme: string | null): unknown {
    if (depth > 12) return null;
    if (typeof value === "string") {
      const m = /^\{([^}]+)\}$/.exec(value.trim());
      if (!m) return value;
      const ref = m[1];
      const sets = [setName, ...(theme && theme !== setName ? [theme] : []), "core"];
      for (const cand of [...sets.map((s) => `${s}.${ref}`), ref])
        if (Object.hasOwn(this.flat, cand)) return this.final(cand, depth + 1, theme);
      return null;
    }
    if (Array.isArray(value)) return value.map((v) => this.deep(v, setName, depth, theme));
    if (isObj(value)) return Object.fromEntries(Object.entries(value).map(([k, v]) => [k, this.deep(v, setName, depth, theme)]));
    return value;
  }
}

// Parsed token files, reused until the file changes on disk (a pull or a
// rebuild), so a long-running server never serves stale swatches.
const resolvers = new Map<string, { mtime: number; size: number; res: Resolver }>();
async function resolverFor(tokensPath: string): Promise<Resolver> {
  const file = path.resolve(ROOT, tokensPath);
  const st = await fs.stat(file);
  const hit = resolvers.get(file);
  if (hit && hit.mtime === st.mtimeMs && hit.size === st.size) return hit.res;
  const res = new Resolver(JSON.parse(await fs.readFile(file, "utf8")));
  resolvers.set(file, { mtime: st.mtimeMs, size: st.size, res });
  return res;
}

async function swatches(system: Obj): Promise<Obj> {
  const res = await resolverFor(asStr(system.tokens));
  const sets = isObj(system.preview) && isObj(system.preview.swatches) ? system.preview.swatches : {};
  const out: Obj = {};
  for (const [theme, roles] of Object.entries(sets))
    if (isObj(roles))
      out[theme] = Object.entries(roles).map(([role, p]) => ({
        role,
        token: p,
        value: res.lookup(asStr(p)) ?? null,
      }));
  return out;
}

const CSS_IDENT = /^-?[A-Za-z_][A-Za-z0-9_-]*$/;

function fontName(name: string): string {
  name = name.trim();
  const words = name === "" ? [] : name.split(/\s+/);
  if (name.startsWith("'") || name.startsWith('"') || name.startsWith("var(") || words.every((w) => CSS_IDENT.test(w)))
    return name;
  return '"' + name.replace(/"/g, '\\"') + '"';
}

function shadow(layer: unknown): string | null {
  if (!isObj(layer) || !("offsetX" in layer) || !("offsetY" in layer)) return null;
  const colour = hexOf(layer.color) ?? layer.color;
  const parts = layer.inset ? ["inset"] : [];
  for (const k of ["offsetX", "offsetY", "blur", "spread"])
    if (k in layer) parts.push(String(dimension(layer[k]) ?? layer[k]));
  if (typeof colour !== "string") return null;
  return [...parts, colour].join(" ");
}

function dimension(value: unknown): string | null {
  // DTCG 2025 dimensions and durations are {value, unit} objects.
  if (isObj(value) && Object.keys(value).length === 2 && "value" in value && "unit" in value)
    return `${value.value}${value.unit}`;
  return null;
}

function cssValue(raw: unknown): string | null {
  // One CSS value for a fully resolved DTCG value, or null when there is none
  // (typography objects, booleans, mixed lists).
  if (typeof raw === "boolean" || raw == null) return null;
  if (typeof raw === "number") return String(raw);
  if (typeof raw === "string") return raw;
  const asHex = hexOf(raw);
  if (asHex) return asHex;
  const dim = dimension(raw);
  if (dim) return dim;
  if (isObj(raw)) return shadow(raw);
  if (Array.isArray(raw) && raw.length) {
    if (raw.length === 4 && raw.every((v) => typeof v === "number"))
      return "cubic-bezier(" + raw.map((v) => String(v)).join(", ") + ")";
    if (raw.every((v) => typeof v === "string")) return raw.map((v) => fontName(v as string)).join(", ");
    const layers = raw.map(shadow);
    if (layers.every((l) => l !== null)) return layers.join(", ");
  }
  return null;
}

function unresolved(raw: unknown): boolean {
  // True when an alias somewhere in a resolved value pointed at nothing.
  if (raw == null) return true;
  if (isObj(raw)) return Object.values(raw).some(unresolved);
  if (Array.isArray(raw)) return raw.some(unresolved);
  return false;
}

const cssName = (parts: string[]): string =>
  "--" + parts.map((p) => p.replace(/[^A-Za-z0-9_-]+/g, "-")).join("-").replace(/^-+|-+$/g, "");

interface Exported {
  base: Record<string, string>;
  themes: Record<string, Record<string, string>>;
  skipped: string[];
  unresolved: string[];
}

function exportTokens(tokens: unknown, themes: string[]): Exported {
  // Resolve a token file into flat name -> value maps. Sets named after a theme
  // become per-theme maps with the set name dropped; `core` is merged into base
  // with its name dropped; any other set goes into base under its own name.
  // A `core` token whose aliases only resolve inside a theme set goes into each
  // theme's map, unless that theme defines the same CSS name itself; it must
  // resolve in every theme, otherwise a light-only value on :root would leak
  // into the other themes, so it is unresolved.
  const res = new Resolver(tokens);
  const themeSets = themes.filter((t) => isObj(tokens) && Object.hasOwn(tokens, t));
  const out: Exported = { base: {}, themes: Object.fromEntries(themeSets.map((t) => [t, {}])), skipped: [], unresolved: [] };
  // Names each theme defines itself, whether or not they resolve, so a shared
  // value never replaces one.
  const own: Record<string, Set<string>> = {};
  for (const t of themeSets)
    own[t] = new Set(
      Object.keys(res.flat)
        .filter((p) => p.split(".")[0] === t)
        .map((p) => cssName(p.split(".").slice(1))),
    );
  for (const p of Object.keys(res.flat)) {
    const parts = p.split(".");
    const raw = res.final(p);
    let broken = unresolved(raw);
    const value = broken ? null : cssValue(raw);
    if (value === null && parts[0] === "core" && themeSets.length) {
      const perRaw = Object.fromEntries(themeSets.map((t) => [t, res.final(p, 0, t)]));
      broken = Object.values(perRaw).some(unresolved);
      const perTheme = Object.fromEntries(themeSets.map((t) => [t, broken ? null : cssValue(perRaw[t])]));
      if (!broken && Object.values(perTheme).every((v) => v !== null)) {
        const name = cssName(parts.slice(1));
        for (const [theme, themed] of Object.entries(perTheme))
          if (!own[theme].has(name)) out.themes[theme][name] = String(themed);
        continue;
      }
    }
    if (broken) {
      out.unresolved.push(p);
      continue;
    }
    if (value === null) {
      out.skipped.push(p);
      continue;
    }
    if (themeSets.includes(parts[0])) out.themes[parts[0]][cssName(parts.slice(1))] = String(value);
    else if (parts[0] === "core") out.base[cssName(parts.slice(1))] = String(value);
    else out.base[cssName(parts)] = String(value);
  }
  return out;
}

async function findSystems(words: string[]): Promise<Obj[]> {
  // Packages ranked by how many query words they match; name and tag hits
  // count double.
  const cat = await loadCatalog();
  const categories = isObj(cat.categories) ? (cat.categories as Record<string, unknown>) : {};
  const ranked: { score: number; s: Obj }[] = [];
  for (const s of asArr(cat.systems)) {
    if (!isObj(s)) continue;
    const strong = [s.slug, s.name, ...asArr(s.tags)].map(asStr).join(" ").toLowerCase();
    const weak = [s.goodFor, s.category, categories[asStr(s.category)] ?? "", ...asArr(s.themes)]
      .map(asStr)
      .join(" ")
      .toLowerCase();
    const score = words.reduce((n, w) => n + (strong.includes(w.toLowerCase()) ? 2 : weak.includes(w.toLowerCase()) ? 1 : 0), 0);
    if (score || !words.length) ranked.push({ score, s });
  }
  ranked.sort((a, b) => b.score - a.score || cmpStr(asStr(a.s.slug), asStr(b.s.slug)));
  return ranked.map(({ score, s }) => ({
    slug: s.slug,
    name: s.name,
    score,
    goodFor: s.goodFor,
    tags: asArr(s.tags),
    themes: s.themes,
    entry: s.entry,
    tokens: s.tokens,
    styleGuide: s.styleGuide,
  }));
}

// ---------------------------------------------------------------- refero store
// The Python reads refero.db (sqlite); the port reads the prebuilt JSON the
// gallery ships: index.json for search, style/<slug>.json for a single style.

interface ReferoStyle {
  slug?: string;
  name?: string;
  tagline?: string;
  theme?: string;
  industry?: string;
  type?: string;
  style?: string;
  tags?: unknown[];
  src?: string;
  source_url?: string;
  page_url?: string;
}

let referoCache: { mtime: number; styles: ReferoStyle[] } | null = null;

async function referoStyles(): Promise<ReferoStyle[] | null> {
  // The index stands in for the db handle: absent or unreadable means the
  // refero store is offline, like _refero_db() returning None.
  try {
    const st = await fs.stat(REFERO_INDEX);
    if (referoCache && referoCache.mtime === st.mtimeMs) return referoCache.styles;
    const idx = JSON.parse(await fs.readFile(REFERO_INDEX, "utf8"));
    const styles = asArr(idx.styles).filter(isObj) as ReferoStyle[];
    referoCache = { mtime: st.mtimeMs, styles };
    return styles;
  } catch {
    return null;
  }
}

async function referoStyle(slug: string): Promise<ReferoStyle | null> {
  // The file name is a slug, never a path segment the model controls.
  if (!/^[A-Za-z0-9][A-Za-z0-9_-]*$/.test(slug)) return null;
  try {
    return JSON.parse(await fs.readFile(path.join(REFERO_DIR, "style", `${slug}.json`), "utf8")) as ReferoStyle;
  } catch {
    return null;
  }
}

async function referoSearch(words: string[], style: string | null, limit: number): Promise<Obj[]> {
  const styles = await referoStyles();
  if (!styles) return [];
  const hits: { score: number; s: ReferoStyle }[] = [];
  for (const s of styles) {
    if (s.slug == null) continue;
    const labels = (Array.isArray(s.tags) ? s.tags : []).map((t) => String(t).toLowerCase());
    if (style && s.style !== style) continue;
    const strong = [s.slug, s.name, s.style, s.type, ...labels].map((v) => v ?? "").join(" ").toLowerCase();
    const weak = [s.tagline, s.theme, s.src].map((v) => v ?? "").join(" ").toLowerCase();
    const score = words.reduce((n, w) => n + (strong.includes(w) ? 2 : weak.includes(w) ? 1 : 0), 0);
    if (score || !words.length) hits.push({ score, s });
  }
  hits.sort((a, b) => b.score - a.score || cmpStr(asStr(a.s.slug), asStr(b.s.slug)));
  return hits.slice(0, limit).map(({ score, s }) => ({
    store: "refero",
    slug: s.slug,
    name: s.name,
    score,
    tagline: s.tagline,
    theme: s.theme,
    designStyle: s.style,
    productType: s.type,
    src: s.src,
  }));
}

// ---------------------------------------------------------------- tools

async function searchStyles(args: Obj): Promise<Obj> {
  // Rank styles by free-text words. systems hits score name/tag hits double.
  const query = asStr(args.query);
  const store = args.store === undefined ? "all" : optStr(args.store);
  const platform = optStr(args.platform);
  const style = optStr(args.style);
  const words = query
    .split(/\s+/)
    .filter((w) => w.trim())
    .map((w) => w.toLowerCase());
  const limit = Math.max(1, Math.min(asInt((args.limit ?? 8) || 8), 20));
  const out: Obj[] = [];
  // The catalog's platforms are web, mobile and desktop; "ios" stays an alias
  // for mobile, the value the schema offered first.
  const wanted = platform === "ios" ? "mobile" : platform;
  if (store === "all" || store === "systems") {
    // One catalog read per call, not one per hit.
    const cat = await loadCatalog();
    const bySlug = new Map(asArr(cat.systems).filter(isObj).map((s) => [s.slug, s]));
    for (const hit of await findSystems(words)) {
      const e = bySlug.get(hit.slug);
      if (!e) continue;
      if (platform && !asArr(e.tags).includes(platform) && e.platform !== wanted) continue;
      out.push({
        store: "systems",
        slug: hit.slug,
        name: hit.name,
        score: hit.score,
        goodFor: hit.goodFor,
        tags: hit.tags,
        themes: hit.themes,
        platform: e.platform ?? null,
      });
    }
  }
  if (store === "all" || store === "refero") out.push(...(await referoSearch(words, style, limit)));
  out.sort((a, b) => (a.store === "systems" ? 0 : 1) - (b.store === "systems" ? 0 : 1) || Number(b.score ?? 0) - Number(a.score ?? 0));
  return {
    query,
    hits: out.slice(0, limit),
    note: "systems/ values carry evidence labels; prefer them over refero when both fit",
  };
}

async function getStyle(args: Obj): Promise<Obj> {
  // The catalog entry distilled. `store` disambiguates a slug the two stores
  // share; without it systems wins, then refero.
  const slug = asStr(args.slug);
  const store = optStr(args.store);
  let e: Obj | null = null;
  if (store === null || store === "systems") {
    try {
      e = await entry(slug);
    } catch (err) {
      if (store === "systems") throw err;
    }
  }
  if (e === null) {
    const styles = await referoStyles();
    if (!styles) throw new ToolError(`no systems package '${slug}'`);
    const row = await referoStyle(slug);
    if (!row) throw new ToolError(`no ${store === "refero" ? "refero " : ""}style '${slug}'`);
    const idx = styles.find((s) => s.slug === slug);
    return {
      store: "refero",
      slug: row.slug ?? slug,
      name: row.name ?? null,
      tagline: row.tagline ?? null,
      theme: row.theme ?? null,
      source_url: row.source_url ?? null,
      page_url: row.page_url ?? null,
      product_type: row.type ?? null,
      design_style: row.style ?? null,
      tags: idx?.tags ?? [],
      note: "interpreted third-party data; browse screenshots and tokens, never treat a value as measured",
    };
  }
  return {
    store: "systems",
    slug: e.slug,
    name: e.name,
    url: e.url ?? null,
    category: e.category ?? null,
    goodFor: e.goodFor ?? null,
    tags: asArr(e.tags),
    themes: asArr(e.themes),
    platform: e.platform ?? null,
    shape: e.shape ?? null,
    widths: asArr(e.widths),
    captured: e.captured ?? null,
    access: e.access ?? null,
    capture: e.capture ?? null,
    swatches: await swatches(e),
    files: {
      readme: e.entry ?? null,
      tokens: e.tokens ?? null,
      styleGuide: e.styleGuide ?? null,
      dir: `systems/${asStr(e.slug)}`,
    },
  };
}

async function getTokens(args: Obj): Promise<Obj> {
  // Resolved token values. Without a group it lists the groups and their
  // sizes; with one it returns that group's flat name -> CSS value map. A group
  // too big for one result comes back a page at a time: `offset` and `limit`
  // count tokens, and a truncated page names the `nextOffset` to ask for.
  const slug = asStr(args.slug);
  const group = optStr(args.group);
  const e = await entry(slug);
  const tokens = JSON.parse(await fs.readFile(await repoFileRequired(asStr(e.tokens)), "utf8"));
  const exported = exportTokens(tokens, asArr(e.themes).map(asStr));
  const groups: Record<string, Record<string, string>> = { base: exported.base, ...exported.themes };
  if (!group)
    return {
      slug,
      groups: Object.fromEntries(Object.entries(groups).map(([k, v]) => [k, Object.keys(v).length])),
      skipped: exported.skipped.length,
      unresolved: exported.unresolved.length,
      note: "call again with group=<name> for its values",
    };
  if (!Object.hasOwn(groups, group)) throw new ToolError(`no token group '${group}'; groups: ${Object.keys(groups).join(", ")}`);
  const offset = asInt(args.offset || 0);
  const limit = args.limit == null ? null : asInt(args.limit);
  if (offset < 0) throw new ToolError("offset must be 0 or more");
  if (limit !== null && limit < 1) throw new ToolError("limit must be 1 or more");
  // Sorted by name so a page holds the same tokens in both twins (JSON.parse
  // reorders integer-like keys, so the file's order cannot be shared).
  const items = Object.entries(groups[group]).sort((a, b) => cmpStr(a[0], b[0]));
  const page: Record<string, string> = {};
  let used = 2;
  let n = 0;
  for (const [name, value] of items.slice(offset)) {
    if (limit !== null && n >= limit) break;
    const size = jsonSize(name) + jsonSize(value) + 2; // the colon and comma
    if (n && used + size > TOKEN_PAGE) break;
    page[name] = value;
    used += size;
    n++;
  }
  const end = offset + n;
  const out: Obj = { slug, group, tokens: page, count: items.length, offset, truncated: end < items.length };
  if (out.truncated) out.nextOffset = end;
  return out;
}

async function readDoc(args: Obj): Promise<Obj> {
  // A text file from the package: its README (the default), components.md,
  // patterns.md, tokens.json. Path is relative to systems/<slug>/. A file over
  // DOC_CAP characters comes back a page at a time: `offset` is where the page
  // starts, and a truncated page names the `nextOffset` to ask for.
  const slug = asStr(args.slug);
  const e = await entry(slug);
  const rel = optStr(args.path) || path.basename(asStr(e.entry));
  const offset = asInt(args.offset || 0);
  if (offset < 0) throw new ToolError("offset must be 0 or more");
  const target = await bounded(e, rel);
  const st = await fs.stat(target).catch(() => null);
  if (st?.isDirectory()) throw new ToolError(`${rel} is a directory`);
  if (!st?.isFile()) throw new ToolError(`no file ${rel} in systems/${slug}/`);
  if (!TEXT_TYPES.has(path.extname(target).toLowerCase())) throw new ToolError(`not a text file: ${rel}`);
  // utf8 decoding replaces bad sequences, matching read_text(errors="replace").
  // Offsets count code points, as Python's str indexes do.
  const chars = Array.from(await fs.readFile(target, "utf8"));
  const end = offset + DOC_CAP;
  const truncated = chars.length > end;
  const relInPkg = path.relative(await pkgDir(e), target).split(path.sep).join("/");
  const out: Obj = {
    slug,
    path: `systems/${slug}/${relInPkg}`,
    text: chars.slice(offset, end).join(""),
    truncated,
    offset,
    length: chars.length,
  };
  if (truncated) out.nextOffset = end;
  return out;
}

async function walkFiles(dir: string): Promise<string[]> {
  // Every regular file under dir, symlinks skipped (neither followed into a
  // directory nor listed as a file), sorted by path like the Python.
  const out: string[] = [];
  const stack = [dir];
  while (stack.length) {
    const cur = stack.pop() as string;
    for (const de of await fs.readdir(cur, { withFileTypes: true })) {
      const p = path.join(cur, de.name);
      if (de.isDirectory()) stack.push(p);
      else if (de.isFile()) out.push(p);
    }
  }
  return out.sort(cmpStr);
}

async function listMedia(args: Obj): Promise<Obj> {
  // Screenshot, crop, icon and board files with site-relative URLs the page
  // can render. kind is one of screenshots|components|icons|boards.
  const slug = asStr(args.slug);
  const kind = optStr(args.kind);
  const e = await entry(slug);
  const kinds = kind ? [kind] : [...MEDIA_DIRS];
  if (kinds.some((k) => !(MEDIA_DIRS as readonly string[]).includes(k)))
    throw new ToolError(`kind must be one of ${MEDIA_DIRS.join(", ")}`);
  const items: Obj[] = [];
  const base = await pkgDir(e);
  for (const k of kinds) {
    const d = path.join(base, k);
    // A symlinked media folder is skipped like any other symlink.
    if (!(await fs.lstat(d).catch(() => null))?.isDirectory()) continue;
    for (const p of await walkFiles(d)) {
      const ext = path.extname(p).toLowerCase();
      const rel = path.relative(base, p).split(path.sep).join("/");
      if (IMAGE_TYPES[ext] && !privatePath(rel)) items.push({ kind: k, name: path.basename(p, ext), url: mediaUrl(p) });
    }
  }
  return { slug, count: items.length, items: items.slice(0, 60), capped: items.length > 60 };
}

async function viewMedia(args: Obj): Promise<Obj> {
  // One image from the package as an image block the model can see. Path is
  // relative to systems/<slug>/ (as list_media reports it).
  const slug = asStr(args.slug);
  const rel = asStr(args.path);
  const e = await entry(slug);
  const target = await bounded(e, rel);
  let mediaType = IMAGE_TYPES[path.extname(target).toLowerCase()];
  const st = await fs.stat(target).catch(() => null);
  if (!st?.isFile() || !mediaType) throw new ToolError(`no image at ${rel}`);
  let data: Buffer = await fs.readFile(target);
  if (data.length > IMAGE_CAP) {
    const shrunk = await thumbnail(target);
    if (shrunk === null)
      throw new ToolError(
        `image is ${Math.floor(data.length / 1000)} KB, over the ${IMAGE_CAP / 1000} KB cap; ask list_media for a thumbnail instead`,
      );
    [data, mediaType] = shrunk;
  }
  return {
    _image: {
      media_type: mediaType,
      data: data.toString("base64"),
      url: mediaUrl(target),
      name: `${slug}/${path.basename(target)}`,
    },
  };
}

async function thumbnail(target: string): Promise<[Buffer, string] | null> {
  // The Python downscales with Pillow; the port reuses the prebuilt gallery
  // thumbnail for the same file (catalog.py's _thumb_name pattern) when one
  // was generated.
  const rel = path.relative(REAL_ROOT, target).split(path.sep).join("/");
  const name = rel.replaceAll("/", "__").replace(/\.[^.]*$/, "") + ".jpg";
  try {
    const buf = await fs.readFile(path.join(THUMBS_DIR, name));
    return [buf, "image/jpeg"];
  } catch {
    return null;
  }
}

async function handoffPrompt(args: Obj): Promise<Obj> {
  // The apply-style prompt for a coding agent, the same shape the gallery's
  // "Copy agent prompt" button writes.
  const slug = asStr(args.slug);
  const appDescription = optStr(args.app_description);
  const e = await entry(slug);
  const tokens = JSON.parse(await fs.readFile(await repoFileRequired(asStr(e.tokens)), "utf8"));
  const groups = isObj(tokens) ? Object.keys(tokens).filter((k) => !k.startsWith("$")).join(", ") : "";
  // Paths are repo-relative under $DESIGN_SYSTEMS_HOME, the variable the
  // design-systems plugin and AGENTS.md use to find a checkout, so the
  // prompt works on the agent's machine instead of naming the server's.
  const root = HOME_VAR;
  const target = appDescription ? ` for ${appDescription}` : "";
  const text =
    `Match the ${asStr(e.name)} design style from my design-systems library${target}.\n` +
    `${root} is that library's checkout on this machine (set it, or replace it with the path).\n` +
    `1. Read ${root}/${asStr(e.entry)} in full first. It says what was captured and what to distrust.\n` +
    `2. Take colour, type, spacing and radius values from ${root}/${asStr(e.tokens)}. Its top-level ` +
    `token groups are ${groups}; the README says which group holds colour roles and which holds ` +
    `scales. Never read a colour off a screenshot.\n` +
    `3. Use ${root}/systems/${slug}/screenshots/ for layout and proportion only. ` +
    `${root}/${asStr(e.styleGuide)} renders every token.\n` +
    `4. Borrow structure and proportions, not the product's logo, icons, illustrations or brand colours.\n` +
    `5. In your summary, name the package and the tokens you used.`;
  return { slug, prompt: text };
}

// ---------------------------------------------------------------- dispatch

interface Spec {
  name: string;
  description: string;
  parameters: {
    type: "object";
    additionalProperties: false;
    properties: Record<string, unknown>;
    required?: string[];
  };
  fn: (args: Obj) => Promise<Obj>;
}

// One schema serves both provider adapters: chat.ts maps it onto Anthropic's
// `tools` and OpenAI's `functions` wire shapes.
export const SPECS: Spec[] = [
  {
    name: "search_styles",
    fn: searchStyles,
    description:
      "Rank styles by free-text words across the systems packages " +
      "(measured, preferred) and the refero snapshot (interpreted). " +
      "Returns slugs the page renders as cards.",
    parameters: {
      type: "object",
      additionalProperties: false,
      properties: {
        query: { type: "string", description: "Free text: mood, layout, use, product words" },
        store: { type: "string", enum: ["all", "systems", "refero"], default: "all" },
        platform: {
          type: "string",
          enum: ["web", "mobile", "desktop", "ios"],
          description: "The catalog's platform; ios is an alias for mobile",
        },
        style: { type: "string", description: "Refero design_style label filter" },
        limit: { type: "integer", minimum: 1, maximum: 20, default: 8 },
      },
      required: ["query"],
    },
  },
  {
    name: "get_style",
    fn: getStyle,
    description:
      "A style's distilled catalog entry: what it is for, its themes, " +
      "palette preview and which files hold the detail. Pass the store " +
      "a search_styles hit came from so a shared slug keeps its identity.",
    parameters: {
      type: "object",
      additionalProperties: false,
      properties: {
        slug: { type: "string" },
        store: { type: "string", enum: ["systems", "refero"] },
      },
      required: ["slug"],
    },
  },
  {
    name: "get_tokens",
    fn: getTokens,
    description:
      "Resolved token values for a systems package. Call without a " +
      "group to list groups, then with one for its flat map. A large " +
      "group comes back in pages: when truncated is true, call again " +
      "with offset=nextOffset.",
    parameters: {
      type: "object",
      additionalProperties: false,
      properties: {
        slug: { type: "string" },
        group: { type: "string", description: "e.g. light, dark, base" },
        offset: {
          type: "integer",
          minimum: 0,
          default: 0,
          description: "Token index to start from (a previous page's nextOffset)",
        },
        limit: { type: "integer", minimum: 1, description: "Most tokens to return; a page also stops before the result cap" },
      },
      required: ["slug"],
    },
  },
  {
    name: "read_doc",
    fn: readDoc,
    description:
      "Read a text file inside a package: its README (default), " +
      "components.md, patterns.md, tokens.json. Long files come back " +
      "in pages: when truncated is true, call again with offset=nextOffset.",
    parameters: {
      type: "object",
      additionalProperties: false,
      properties: {
        slug: { type: "string" },
        path: {
          type: "string",
          description: "Package-relative path (a systems/<slug>/ or /systems/<slug>/ path also works); default README.md",
        },
        offset: {
          type: "integer",
          minimum: 0,
          default: 0,
          description: "Character offset to start from (a previous page's nextOffset)",
        },
      },
      required: ["slug"],
    },
  },
  {
    name: "list_media",
    fn: listMedia,
    description: "List a package's screenshots, component crops, icons and boards with page-renderable URLs.",
    parameters: {
      type: "object",
      additionalProperties: false,
      properties: {
        slug: { type: "string" },
        kind: { type: "string", enum: [...MEDIA_DIRS] },
      },
      required: ["slug"],
    },
  },
  {
    name: "view_media",
    fn: viewMedia,
    description:
      "See one image from a systems package (a screenshot or crop). " +
      "Use for questions tags cannot answer: density, layout, mood.",
    parameters: {
      type: "object",
      additionalProperties: false,
      properties: {
        slug: { type: "string" },
        path: { type: "string", description: "Package-relative path (or a list_media url)" },
      },
      required: ["slug", "path"],
    },
  },
  {
    name: "handoff_prompt",
    fn: handoffPrompt,
    description: "The apply-style prompt that hands a chosen style to a coding agent, for 'use this one'.",
    parameters: {
      type: "object",
      additionalProperties: false,
      properties: {
        slug: { type: "string" },
        app_description: { type: "string", description: "What the style is being applied to" },
      },
      required: ["slug"],
    },
  },
];

const BY_NAME = new Map(SPECS.map((s) => [s.name, s]));

export async function call(name: string, args: Obj | null): Promise<Obj> {
  // Run one tool by name, capping the JSON the caller sends on. Every failure
  // (missing arguments, bad types, tool errors) surfaces as a ToolError so one
  // bad call can never take down a caller's loop.
  const spec = BY_NAME.get(name);
  if (!spec) throw new ToolError(`unknown tool '${name}'`);
  const props = spec.parameters.properties;
  const clean: Obj = {};
  for (const [k, v] of Object.entries(args ?? {})) if (Object.hasOwn(props, k)) clean[k] = v;
  const missing = (spec.parameters.required ?? []).filter((k) => !Object.hasOwn(clean, k));
  if (missing.length) throw new ToolError(`${name} needs ${missing.join(", ")}`);
  let result: Obj;
  try {
    result = await spec.fn(clean);
  } catch (e) {
    // Argument checks throw ToolError with text written for the caller.
    // Anything else (a filesystem error names an absolute path, a JSON.parse
    // of a server file quotes its content) is logged here and reaches the
    // caller, and through the chat a third-party model, only as its type.
    if (e instanceof ToolError) throw e;
    console.error(`library: ${name}:`, e);
    throw new ToolError(`${name} failed (${e instanceof Error ? e.name : typeof e})`);
  }
  if ("_image" in result) return result;
  const size = jsonSize(result);
  if (size > RESULT_CAP) {
    const bytes = Buffer.from(JSON.stringify(result), "utf8").subarray(0, RESULT_CAP);
    // Drop a multi-byte character cut in half, as Python's decode("ignore").
    const partial = new TextDecoder("utf-8", { fatal: false }).decode(bytes).replace(/\uFFFD$/, "");
    return { truncated: true, bytes: size, partial };
  }
  return result;
}
