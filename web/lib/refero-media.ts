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

export const cardImg = (index: ReferoIndex, s: ReferoCard): MediaPair => ({
  local: s.card ? localMedia(index.mediaBase, s.card === "p" ? "posters" : "shots", s.slug, "jpg") : null,
  remote: cdnUrl(index.cdn, s.cardRemote),
});
// A favicon has no remote: asking a favicon service for a style's host would
// tell it which styles are browsed. The mirrored file shows when it exists,
// the letter tile otherwise.
export const cardFav = (index: ReferoIndex, s: ReferoCard): MediaPair => ({
  local: localMedia(index.mediaBase, "favicons", s.slug, "png"),
  remote: null,
});
export const cardVideo = (index: ReferoIndex, s: ReferoCard): MediaPair => ({
  local: localMedia(index.mediaBase, "videos", s.slug, "mp4"),
  remote: cdnUrl(index.cdn, s.videoRemote),
});
