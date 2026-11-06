import type { NextConfig } from "next";
const config: NextConfig = {
  devIndicators: false,
  serverExternalPackages: ["@libsql/client"],
};
export default config;
