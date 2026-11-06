// The gallery's data.json (written by `make build` / tools/catalog.py), loaded
// from disk and cached by mtime so a rebuild shows up without a restart.
import { promises as fs } from "node:fs";
import path from "node:path";
import { ROOT } from "./repo";
import { mediaUrl } from "./url";

export { mediaUrl };

export interface Swatch {
  role: string;
  token: string;
  value: string | null;
}
export interface Shot {
  path: string;
  name: string;
  group: string;
  tags: string[];
  thumb?: string;
}
export interface SystemScore {
  meets: number;
  partly: number;
  missing: number;
  na: number;
  applicable: number;
  date: string;
  contrast: string | null;
}
export interface FontSpec {
  token: string;
  family: string;
  stack: string;
}
export interface TypeStyle {
  name: string;
  family?: string;
  size?: string;
  weight?: number;
  lineHeight?: string | number;
  letterSpacing?: string;
}
export interface NameValue {
  name: string;
  value: string;
}
export interface ShadowSpec {
  token: string;
  css: string;
}
export interface Capture {
  method?: string;
  viewport?: string;
  date?: string;
  [k: string]: unknown;
}
export interface DesignSystem {
  slug: string;
  name: string;
  url: string;
  category: string;
  goodFor: string;
  shape: string;
  captured: string;
  themes: string[];
  tags: string[];
  entry: string;
  tokens: string;
  styleGuide: string;
  access: string;
  capture: Capture | null;
  widths: string[];
  notes: string;
  dir: string;
  cover: { path: string; thumb?: string };
  icon?: string;
  swatches: Record<string, Swatch[]>;
  tokenGroups: string[];
  fonts: FontSpec[];
  score: SystemScore | null;
  screenshots: Shot[];
  components: Shot[];
  docs: string[];
  tokenTheme: string;
  typeStyles: TypeStyle[];
  radii: NameValue[];
  spacing: NameValue[];
  shadows: ShadowSpec[];
  omitted: Record<string, string>;
  icons: { total: number; items: string[] };
  layoutGaps: Record<string, string>;
}
export interface GalleryData {
  root: string;
  categories: Record<string, string>;
  systems: DesignSystem[];
}

interface Cache {
  mtime: number;
  data: GalleryData;
}
let cache: Cache | null = null;

const DATA_PATH = () => path.join(ROOT, "web", "data", "data.json");

export async function loadData(): Promise<GalleryData> {
  const st = await fs.stat(DATA_PATH());
  if (cache && cache.mtime === st.mtimeMs) return cache.data;
  const data = JSON.parse(await fs.readFile(DATA_PATH(), "utf8")) as GalleryData;
  cache = { mtime: st.mtimeMs, data };
  return data;
}

export async function getSystem(slug: string): Promise<DesignSystem | undefined> {
  const data = await loadData();
  return data.systems.find((s) => s.slug === slug);
}

export interface PkgFile {
  rel: string; // repo-relative path, e.g. systems/duolingo/tokens.json
  name: string;
  size: number;
}
const SKIP_DIRS = new Set(["raw", "boards", "__pycache__", "node_modules", ".git"]);
const SKIP_EXT = new Set([".png", ".jpg", ".jpeg", ".webp", ".gif", ".mp4", ".webm", ".woff", ".woff2", ".zip"]);

// Every human-readable file in a package, grouped for the Files section.
// Skips the heavy evidence dirs (raw/, boards/) and binaries that the
// screenshots/components sections already cover.
export async function listPackageFiles(slug: string): Promise<Record<string, PkgFile[]>> {
  const dir = path.join(ROOT, "systems", slug);
  const out: Record<string, PkgFile[]> = {};
  async function walk(rel: string) {
    let entries;
    try {
      entries = await fs.readdir(path.join(dir, rel), { withFileTypes: true });
    } catch {
      return;
    }
    for (const e of entries.sort((a, b) => a.name.localeCompare(b.name))) {
      const r = rel ? `${rel}/${e.name}` : e.name;
      if (e.isDirectory()) {
        if (!SKIP_DIRS.has(e.name)) await walk(r);
      } else if (e.isFile() && !SKIP_EXT.has(path.extname(e.name).toLowerCase())) {
        const st = await fs.stat(path.join(dir, r));
        const group = rel ? rel.split("/")[0] : "";
        (out[group] ||= []).push({ rel: `systems/${slug}/${r}`, name: r, size: st.size });
      }
    }
  }
  await walk("");
  return out;
}

// Read a file inside systems/<slug>/, bounded. Returns null outside/missing.
export async function readPackageFile(slug: string, rel: string): Promise<{ text: string; rel: string } | null> {
  if (!/^[a-z0-9][a-z0-9-]*$/i.test(slug)) return null;
  const dir = path.resolve(ROOT, "systems", slug);
  const target = path.resolve(dir, rel);
  const within = path.relative(dir, target);
  if (within.startsWith("..") || path.isAbsolute(within)) return null;
  try {
    return { text: await fs.readFile(target, "utf8"), rel: `systems/${slug}/${within}` };
  } catch {
    return null;
  }
}

// Read a repo text file inside an allowed tree (docs/, systems/<slug>/), used
// for markdown sources. Returns null when outside or unreadable.
export async function readRepoText(rel: string): Promise<string | null> {
  const clean = rel.replace(/^\/+/, "");
  const target = path.resolve(ROOT, clean);
  const relToRoot = path.relative(ROOT, target);
  if (relToRoot.startsWith("..") || path.isAbsolute(relToRoot)) return null;
  try {
    return await fs.readFile(target, "utf8");
  } catch {
    return null;
  }
}

// mediaUrl is re-exported for server callers; client components must import it
// from "@/lib/url" so node:fs never enters the browser bundle.
