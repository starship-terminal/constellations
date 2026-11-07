import type { NextConfig } from "next";

// The app runs `next start` in place from the clone (the designs-web unit on
// the box), so `output: "standalone"` is off: nothing consumes the emitted
// bundle, Next warns that `next start` does not support it, and the traced
// node_modules come out incomplete under pnpm anyway (server.js fails to
// boot on a missing lazy require). The app still reads the repo's generated
// data at request time — `make build` output shows up with no frontend
// rebuild — controlled by DESIGN_SYSTEMS_REPO when run outside the checkout.
const config: NextConfig = {
  reactStrictMode: true,
};

export default config;
