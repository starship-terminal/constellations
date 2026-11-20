// Repository paths and bounded file resolution, ported from tools/catalog.py's
// repo_file() and the Refero media path rules. Every path the
// app serves from the checkout goes through resolveMedia so `..` segments and
// symlinks can never climb out of the allowed roots.
import { execFile } from "node:child_process";
import { promises as fs } from "node:fs";
import { existsSync } from "node:fs";
import path from "node:path";
import "./env.ts";

export const ROOT = (() => {
  // `next dev`/`next start` run with cwd = web/. Allow an explicit override.
  if (process.env.DESIGN_SYSTEMS_REPO) return path.resolve(process.env.DESIGN_SYSTEMS_REPO);
  const cwd = process.cwd();
  if (path.basename(cwd) === "web") return path.dirname(cwd);
  if (existsSync(path.join(cwd, "catalog.json"))) return cwd;
  if (existsSync(path.join(path.dirname(cwd), "catalog.json"))) return path.dirname(cwd);
  return cwd;
})();

// Request prefixes answered from the checkout: catalog.py's REPO_PATHS minus
// /example/, which holds only gitignored clones and a README nothing links to.
const REPO_PATHS = ["/systems/", "/tools/", "/catalog.json", "/README.md"];
// Extra roots that do not resolve 1:1 from the repo root: generated app data
// lives under web/data/ ("data/thumbs/x.jpg"), docs assets under docs/
// ("docs/assets/y.svg").
const EXTRA_PATHS: Record<string, string> = { "/data/": "web/data", "/docs/": "docs" };

const norm = (p: string) => path.posix.normalize(p);

function inside(target: string, dir: string): boolean {
  const rel = path.relative(dir, target);
  return rel === "" || (!rel.startsWith("..") && !path.isAbsolute(rel));
}

export function repoFile(urlPath: string): string | null {
  const clean = decodeURIComponent(urlPath.split("?")[0].split("#")[0]);
  const p = norm(clean);
  const extra = Object.keys(EXTRA_PATHS).find((pre) => p.startsWith(pre));
  const repo =
    !extra && REPO_PATHS.some((pre) => p === pre.replace(/\/$/, "") || p.startsWith(pre));
  if (!extra && !repo) return null;
  const target = extra
    ? path.resolve(ROOT, EXTRA_PATHS[extra], p.slice(extra.length))
    : path.resolve(ROOT, p.replace(/^\/+/, ""));
  const allowed = repoRoots();
  if (!allowed.some((a) => target === a || inside(target, a))) return null;
  return target;
}

// Gitignored material on disk (capture dumps, proprietary fonts, scratch
// output) is private even though it sits under a served root. One `git
// ls-files` call lists every ignored path, with wholly ignored folders
// collapsed to "dir/"; the answer is cached briefly so a gallery page's
// hundreds of image requests share one listing. Tracked files are never in
// it, so anything committed stays servable.
const IGNORED_TTL_MS = 10_000;
let ignoredCache: { at: number; list: Promise<Set<string> | null> } | null = null;

function listIgnored(): Promise<Set<string> | null> {
  return new Promise((resolve) => {
    execFile(
      "git",
      ["-C", ROOT, "ls-files", "--others", "--ignored", "--exclude-standard", "--directory", "-z"],
      { maxBuffer: 64 * 1024 * 1024 },
      (err, stdout) => resolve(err ? null : new Set(stdout.split("\0").filter(Boolean))),
    );
  });
}

/** True when a file or folder (a real path) is gitignored, so it must not be served or
    listed. Outside a git checkout nothing is ignored; inside one, a git
    failure or a path outside the checkout counts as ignored (fail closed). */
export async function isGitIgnored(abs: string): Promise<boolean> {
  if (!existsSync(path.join(ROOT, ".git"))) return false;
  // Compare real paths: callers pass a realpath'd file, and git reports
  // paths relative to the checkout's real location.
  const rel = path.relative(await fs.realpath(ROOT), abs).split(path.sep).join("/");
  if (!rel || rel.startsWith("..") || path.isAbsolute(rel)) return true;
  // The listing names paths, not rules, so a file created after it was taken
  // (a new capture dump) is missing from it: refresh before judging one.
  const changed = await fs.stat(abs).then((st) => st.ctimeMs, () => Infinity);
  if (!ignoredCache || Date.now() - ignoredCache.at > IGNORED_TTL_MS || changed >= ignoredCache.at)
    ignoredCache = { at: Date.now(), list: listIgnored() };
  const ignored = await ignoredCache.list;
  if (!ignored) return true;
  // A folder can be passed too: wholly ignored ones are listed as "dir/".
  if (ignored.has(rel) || ignored.has(rel + "/")) return true;
  const parts = rel.split("/");
  for (let i = 1; i < parts.length; i++) if (ignored.has(parts.slice(0, i).join("/") + "/")) return true;
  return false;
}

/** The real path of `target` when it, after following symlinks, still sits
    inside the real path of `root`; null otherwise or when it is missing. */
export async function realInside(target: string, root: string): Promise<string | null> {
  try {
    const [real, realRoot] = await Promise.all([fs.realpath(target), fs.realpath(root)]);
    return real === realRoot || inside(real, realRoot) ? real : null;
  } catch {
    return null;
  }
}

// The served roots on disk, for realInside's containment check.
export function repoRoots(): string[] {
  return [
    ...REPO_PATHS.map((x) => path.resolve(ROOT, x.replace(/^\/+|\/+$/g, ""))),
    ...Object.values(EXTRA_PATHS).map((d) => path.resolve(ROOT, d)),
  ];
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

export { mediaBase } from "./media-base.ts";

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
  ".ttf": "font/ttf",
  ".otf": "font/otf",
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
