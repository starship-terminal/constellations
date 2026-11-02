import type { NextConfig } from "next";
import path from "node:path";

// The app reads the repo's generated data at request time (that is the design:
// `make build` output shows up with no frontend rebuild). The standalone
// bundle must not copy that data — it is read live from the checkout, or from
// DESIGN_SYSTEMS_REPO when the server runs outside it.
const REPO = path.resolve(__dirname, "..");

const config: NextConfig = {
  output: "standalone",
  outputFileTracingRoot: REPO,
  outputFileTracingExcludes: {
    "*": [
      "systems/**",
      "docs/gallery/thumbs/**",
      "docs/gallery/refero/**",
      "refero/**",
      "site/**",
      "example/**",
      ".git/**",
      "node_modules/**",
      "tools/kit/**",
    ],
  },
  reactStrictMode: true,
};

export default config;
