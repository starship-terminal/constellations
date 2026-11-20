import type { NextConfig } from "next";

// The app runs `next start` in place from the clone (the designs-web unit on
// the box), so `output: "standalone"` is off: nothing consumes the emitted
// bundle, Next warns that `next start` does not support it, and the traced
// node_modules come out incomplete under pnpm anyway (server.js fails to
// boot on a missing lazy require). The app still reads the repo's generated
// data at request time — `make build` output shows up with no frontend
// rebuild — controlled by DESIGN_SYSTEMS_REPO when run outside the checkout.
//
// distDir is the build output folder. Rebuilding into the `.next` the live
// server is reading makes it serve a half-written build for the minute the
// build takes. The home-server deploy sets NEXT_DIST_DIR to a separate folder,
// builds there, then swaps the running unit over to it; everywhere else
// (`make dev`, CI, a plain `pnpm build`) the default stays `.next`. A relative
// path resolves against web/.
const config: NextConfig = {
  distDir: process.env.NEXT_DIST_DIR || ".next",
  reactStrictMode: true,
};

export default config;
