// The refero snapshot built by `make build` into docs/gallery/refero/:
// index.json (~1300 cards) plus one style/<slug>.json entity per style.
import { promises as fs } from "node:fs";
import path from "node:path";
import { ROOT, mediaBase } from "./repo";

export interface ReferoCard {
  slug: string;
  name: string | null;
  tagline: string | null;
  theme: string | null;
  industry: string | null;
  type: string | null;
  style: string | null;
  tags: string[];
  src: string | null;
  card: "p" | "s" | null;
  cardRemote: string | null;
  video: boolean;
  videoRemote: string | null;
}
export interface ReferoIndex {
  version: number;
  cdn: string;
  mediaBase: string;
  styles: ReferoCard[];
}
export interface ReferoMedia {
  local: string | null;
  remote: string | null;
}
export interface ReferoEntity {
  slug: string;
  name: string | null;
  tagline: string | null;
  theme: string | null;
  industry: string | null;
  type: string | null;
  style: string | null;
  source_url: string | null;
  page_url: string | null;
  media: Record<string, ReferoMedia | null>;
  docs: Record<string, string | null>;
  ds: Record<string, unknown>;
  similar: { slug: string | null; name: string | null; why: string | null }[];
  mediaBase: string;
}

const DIR = () => path.join(ROOT, "docs", "gallery", "refero");

let indexCache: { mtime: number; data: ReferoIndex } | null = null;

export async function loadReferoIndex(): Promise<ReferoIndex> {
  const p = path.join(DIR(), "index.json");
  const st = await fs.stat(p);
  if (indexCache && indexCache.mtime === st.mtimeMs) return indexCache.data;
  const data = JSON.parse(await fs.readFile(p, "utf8")) as ReferoIndex;
  indexCache = { mtime: st.mtimeMs, data };
  return data;
}

export async function loadReferoEntity(slug: string): Promise<ReferoEntity | null> {
  if (!/^[a-z0-9][a-z0-9-]*$/i.test(slug)) return null;
  try {
    const e = JSON.parse(await fs.readFile(path.join(DIR(), "style", `${slug}.json`), "utf8")) as ReferoEntity;
    // Resolve `local` media paths the way app.js did: mediaBase prepends the
    // public host (R2); empty keeps them served here, under /media/refero-media/.
    const base = e.mediaBase !== undefined ? e.mediaBase : mediaBase();
    if (e.media) {
      for (const key of Object.keys(e.media)) {
        const m = e.media[key];
        if (m && typeof m.local === "string" && m.local.startsWith("/"))
          m.local = base ? base + m.local : "/media" + m.local;
      }
    }
    return e;
  } catch {
    return null;
  }
}
