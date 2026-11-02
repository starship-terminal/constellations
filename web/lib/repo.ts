// Repository paths and bounded file resolution, ported from tools/catalog.py's
// repo_file() and tools/refero/refero_media.py's media_file(). Every path the
// app serves from the checkout goes through resolveMedia so `..` segments and
// symlinks can never climb out of the allowed roots.
import { promises as fs } from "node:fs";
import { existsSync } from "node:fs";
import path from "node:path";
import "./env";

export const ROOT = (() => {
  // `next dev`/`next start` run with cwd = web/. Allow an explicit override.
  if (process.env.DESIGN_SYSTEMS_REPO) return path.resolve(process.env.DESIGN_SYSTEMS_REPO);
  const cwd = process.cwd();
  if (path.basename(cwd) === "web") return path.dirname(cwd);
  if (existsSync(path.join(cwd, "catalog.json"))) return cwd;
  if (existsSync(path.join(path.dirname(cwd), "catalog.json"))) return path.dirname(cwd);
  return cwd;
})();

// Mirrors REPO_PATHS in catalog.py: request prefixes answered from the checkout.
const REPO_PATHS = ["/systems/", "/tools/", "/example/", "/catalog.json", "/README.md"];
// Built gallery artifacts and docs assets live under docs/; data paths the
// gallery uses are site-relative ("gallery/thumbs/x.jpg", "docs/assets/y.svg").
const EXTRA_PATHS = ["/gallery/", "/docs/"];

const norm = (p: string) => path.posix.normalize(p);

function inside(target: string, dir: string): boolean {
  const rel = path.relative(dir, target);
  return rel === "" || (!rel.startsWith("..") && !path.isAbsolute(rel));
}

export function repoFile(urlPath: string): string | null {
  const clean = decodeURIComponent(urlPath.split("?")[0].split("#")[0]);
  const p = norm(clean);
  if (![...REPO_PATHS, ...EXTRA_PATHS].some((pre) => p === pre.replace(/\/$/, "") || p.startsWith(pre)))
    return null;
  const target = path.resolve(ROOT, p.replace(/^\/+/, ""));
  const allowed = [
    ...REPO_PATHS.map((x) => path.resolve(ROOT, x.replace(/^\/+|\/+$/g, ""))),
    path.resolve(ROOT, "docs"),
  ];
  if (!allowed.some((a) => target === a || inside(target, a))) return null;
  return target;
}

const MEDIA_KINDS: Record<string, [string, string]> = {
  shots: [".jpg", "image/"],
  posters: [".jpg", "image/"],
  videos: [".mp4", "video/"],
  detail: [".mp4", "video/"],
  "detail-posters": [".jpg", "image/"],
  favicons: [".png", "image/"],
};

export function mediaRoot(): string {
  return path.resolve(
    process.env.DESIGN_SYSTEMS_MEDIA ||
      path.join(process.env.HOME || "~", "services/design-systems/media/refero"),
  );
}

export function mediaBase(): string {
  return process.env.DESIGN_SYSTEMS_MEDIA_BASE ?? "https://pub-b22e019453104cc8b3c214b1009a6c42.r2.dev";
}

export function referoMediaFile(urlPath: string): string | null {
  const clean = decodeURIComponent(urlPath.split("?")[0].split("#")[0]);
  const p = norm(clean);
  const prefix = "/refero-media/";
  if (!p.startsWith(prefix)) return null;
  const rel = p.slice(prefix.length);
  if (!rel || rel.startsWith("/")) return null;
  const root = mediaRoot();
  const target = path.resolve(root, rel);
  if (!inside(target, root)) return null;
  return target;
}

export function referoLocalPath(kind: string, slug: string): string {
  return `/refero-media/${kind}/${slug}${MEDIA_KINDS[kind]?.[0] ?? ""}`;
}

const MIME: Record<string, string> = {
  ".png": "image/png",
  ".jpg": "image/jpeg",
  ".jpeg": "image/jpeg",
  ".webp": "image/webp",
  ".gif": "image/gif",
  ".svg": "image/svg+xml",
  ".ico": "image/x-icon",
  ".mp4": "video/mp4",
  ".webm": "video/webm",
  ".json": "application/json; charset=utf-8",
  ".md": "text/markdown; charset=utf-8",
  ".txt": "text/plain; charset=utf-8",
  ".css": "text/css; charset=utf-8",
  ".html": "text/html; charset=utf-8",
  ".js": "text/javascript; charset=utf-8",
  ".mjs": "text/javascript; charset=utf-8",
  ".tsv": "text/tab-separated-values; charset=utf-8",
  ".csv": "text/csv; charset=utf-8",
  ".yml": "text/yaml; charset=utf-8",
  ".yaml": "text/yaml; charset=utf-8",
  ".py": "text/plain; charset=utf-8",
  ".woff": "font/woff",
  ".woff2": "font/woff2",
};

export const mimeOf = (file: string) => MIME[path.extname(file).toLowerCase()] || "application/octet-stream";

export async function fileExists(p: string | null): Promise<boolean> {
  if (!p) return false;
  try {
    return (await fs.stat(p)).isFile();
  } catch {
    return false;
  }
}
