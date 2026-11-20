// Public base URL for mirrored refero media (the R2 bucket), the web side of
// tools/refero/refero_media.py media_base(). DESIGN_SYSTEMS_MEDIA_BASE
// overrides it; empty serves the files from this app's /media/. Its own
// module, free of filesystem code, so proxy.ts can read it for the
// Content-Security-Policy without pulling lib/repo.ts into the proxy bundle.
import "./env.ts";

export function mediaBase(): string {
  return process.env.DESIGN_SYSTEMS_MEDIA_BASE ?? "https://pub-b22e019453104cc8b3c214b1009a6c42.r2.dev";
}
