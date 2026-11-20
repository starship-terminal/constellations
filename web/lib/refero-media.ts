// Client-safe refero media URLs, shared by the index grid and the detail
// page. Local mirrors live under /refero-media/<kind>/<slug>.<ext>; the
// index's mediaBase points them at the public host, empty keeps them on the
// app's own /media/ route (the rule loadReferoEntity applies).
import type { ReferoCard, ReferoIndex } from "@/lib/refero";

export interface MediaPair {
  local: string | null;
  remote: string | null;
}

/** The bare host of a source URL, without "www.": parsed, so a query or
    fragment with no path ("https://acme.example?ref=x") is not kept. */
export const host = (u: string | null) => {
  const s = String(u || "").trim();
  if (!s) return "";
  try {
    return new URL(/^[a-z][a-z0-9+.-]*:\/\//i.test(s) ? s : `https://${s}`).hostname.replace(/^www\./, "");
  } catch {
    return s.replace(/^https?:\/\//, "").replace(/^www\./, "").replace(/[/?#].*$/, "");
  }
};

export const localMedia = (base: string, kind: string, slug: string, ext: string) =>
  `${base || "/media"}/refero-media/${kind}/${encodeURIComponent(slug)}.${ext}`;

export const cdnUrl = (cdn: string, u: string | null) => (u ? (u.includes("://") ? u : `${cdn}${u}`) : null);

export const faviconFor = (src: string | null) =>
  src
    ? `https://t0.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=${encodeURIComponent(`https://${host(src)}`)}&size=128`
    : null;

export const cardImg = (index: ReferoIndex, s: ReferoCard): MediaPair => ({
  local: s.card ? localMedia(index.mediaBase, s.card === "p" ? "posters" : "shots", s.slug, "jpg") : null,
  remote: cdnUrl(index.cdn, s.cardRemote),
});
export const cardFav = (index: ReferoIndex, s: ReferoCard): MediaPair => ({
  local: localMedia(index.mediaBase, "favicons", s.slug, "png"),
  remote: faviconFor(s.src),
});
export const cardVideo = (index: ReferoIndex, s: ReferoCard): MediaPair => ({
  local: localMedia(index.mediaBase, "videos", s.slug, "mp4"),
  remote: cdnUrl(index.cdn, s.videoRemote),
});
