// Shared bits for the docs surface: listing docs/*.md and pulling a doc's
// title + excerpt out of its markdown (frontmatter stripped first).
import { promises as fs } from "node:fs";
import path from "node:path";
import { ROOT } from "@/lib/repo";
import { readRepoText } from "@/lib/catalog";

// One [...path] segment: names only, never dots that could climb out of docs/.
export const SAFE_SEG = /^[A-Za-z0-9][A-Za-z0-9._-]*$/;

const FRONT = /^---\s*\n[\s\S]*?\n---\s*\n/;
export const stripFront = (src: string) => src.replace(FRONT, "");

export interface DocEntry {
  slug: string; // path under docs/ without .md ("index", "DESIGN-SYSTEM")
  file: string; // the file name (DESIGN-SYSTEM.md)
  title: string; // first h1, else the slug
  excerpt: string; // first paragraph as plain text
}

const cleanInline = (t: string) =>
  t
    .replace(/!\[([^\]]*)\]\([^)]*\)/g, "$1")
    .replace(/\[([^\]]+)\]\([^)]*\)/g, "$1")
    .replace(/<[^>]+>/g, "")
    .replace(/[*_`]/g, "")
    .trim();

export function docTitle(src: string): string | null {
  const m = stripFront(src).match(/^#\s+(.+)$/m);
  return m ? cleanInline(m[1]) || null : null;
}

// The first real paragraph after the h1: skips headings, tables, lists,
// admonitions and raw-html blocks until prose shows up.
export function docExcerpt(src: string): string {
  const lines = stripFront(src).split("\n");
  const buf: string[] = [];
  let pastH1 = false;
  for (const l of lines) {
    const t = l.trim();
    if (!pastH1) {
      if (/^#\s/.test(t)) pastH1 = true;
      continue;
    }
    const blockish = /^(#{1,6}\s|[-*+>|`]|<|\||!!!|\d+\.\s)/.test(t);
    if (!t || blockish) {
      if (buf.length) break;
      continue;
    }
    buf.push(t);
  }
  const text = cleanInline(buf.join(" "));
  return text.length > 220 ? text.slice(0, 217).trimEnd() + "…" : text;
}

// Every top-level docs/*.md, index first then by file name.
export async function listDocs(): Promise<DocEntry[]> {
  let names: string[] = [];
  try {
    names = (await fs.readdir(path.join(ROOT, "docs"), { withFileTypes: true }))
      .filter((e) => e.isFile() && e.name.endsWith(".md"))
      .map((e) => e.name)
      .sort((a, b) => a.localeCompare(b));
  } catch {
    return [];
  }
  const docs: DocEntry[] = [];
  for (const name of names) {
    const src = (await readRepoText(`docs/${name}`)) ?? "";
    const slug = name.replace(/\.md$/i, "");
    docs.push({ slug, file: name, title: docTitle(src) ?? slug, excerpt: docExcerpt(src) });
  }
  docs.sort((a, b) => (a.slug === "index" ? -1 : b.slug === "index" ? 1 : 0));
  return docs;
}
